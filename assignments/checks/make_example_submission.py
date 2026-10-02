"""
Generate the example lab check-in submission in assignments/checks/example_submission/.

The numbers are computed honestly from the student-facing data with simple
methods taught in Sessions 1 to 4 (no ground truth is used):

* check_session2.csv / .json: OLS marketing mix model for Austria with
  geometric adstock chosen by grid search, trained on 2023-2024 and validated
  on 2025.
* check_session4.json: regression forecast versus seasonal naive for Germany,
  difference-in-differences on the German geo-lift test, and last-touch versus
  logistic-regression attribution for Germany.

Run from the repository root:
    python assignments/checks/make_example_submission.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "assets"))
from mma import CHANNELS, add_fourier, geometric_adstock, mape  # noqa: E402

OUT = Path(__file__).resolve().parent / "example_submission"
OUT.mkdir(exist_ok=True)

MMM_COUNTRY = "AT"
FORECAST_COUNTRY = "DE"
ATTRIBUTION_COUNTRY = "DE"
ATT_CHANNELS = ["display", "paid_search", "paid_social", "email", "affiliate", "organic"]

panel = pd.read_csv(ROOT / "data/mmm/alpenglow_weekly.csv", parse_dates=["week"])
panel = panel.sort_values(["country", "week"]).reset_index(drop=True)
panel["t"] = panel.groupby("country").cumcount()


# ---------------------------------------------------------------------------
# Check-in 1: OLS MMM for one country
# ---------------------------------------------------------------------------
def design_matrix(df: pd.DataFrame, alphas: dict[str, float]) -> pd.DataFrame:
    """Controls + adstocked spend per channel (linear response, Session 2 lab style)."""
    d = add_fourier(df, order=2)
    X = pd.DataFrame(
        {
            "log_price": np.log(d.price_eur),
            "promo_share": d.promo_share,
            "distribution": d.distribution,
            "log_competitor": np.log(d.competitor_spend_k),
            "consumer_confidence": d.consumer_confidence,
            "temperature_c": d.temperature_c,
            "xmas": d.xmas,
            "easter": d.easter,
            "valentine": d.valentine,
            "trend": d.t / 52,
            "sin_1": d.sin_1, "cos_1": d.cos_1, "sin_2": d.sin_2, "cos_2": d.cos_2,
        },
        index=d.index,
    )
    for ch in CHANNELS:
        X[f"ad_{ch}"] = geometric_adstock(d[f"spend_{ch}_k"].values, alphas[ch])
    return sm.add_constant(X)


def fit_mmm(country: str):
    df = panel[panel.country == country].reset_index(drop=True)
    train = df[df.week < "2025-01-01"]
    y = df.sales_units_k
    grid = np.round(np.arange(0.0, 0.95, 0.1), 1)

    # Coordinate-wise grid search over the adstock decay per channel (AIC on the training window)
    alphas = {ch: 0.3 for ch in CHANNELS}
    for _ in range(2):
        for ch in CHANNELS:
            best = None
            for a in grid:
                trial = {**alphas, ch: float(a)}
                X = design_matrix(df, trial).loc[train.index]
                aic = sm.OLS(y.loc[train.index], X).fit().aic
                if best is None or aic < best[0]:
                    best = (aic, float(a))
            alphas[ch] = best[1]

    X = design_matrix(df, alphas)
    model = sm.OLS(y.loc[train.index], X.loc[train.index]).fit()
    pred_train = model.predict(X.loc[train.index])
    holdout = df.index.difference(train.index)
    pred_hold = model.predict(X.loc[holdout])
    r2_hold = 1 - np.sum((y.loc[holdout] - pred_hold) ** 2) / np.sum((y.loc[holdout] - y.loc[holdout].mean()) ** 2)

    mean_price = df.price_eur.mean()
    rows = []
    for ch in CHANNELS:
        coef = model.params[f"ad_{ch}"]
        incremental = float(coef * X[f"ad_{ch}"].sum())  # thousand units over 2023-2025
        spend = float(df[f"spend_{ch}_k"].sum())
        rows.append(
            {
                "country": country,
                "channel": ch,
                "adstock_alpha": alphas[ch],
                "coefficient": round(float(coef), 4),
                "total_spend_k": round(spend, 2),
                "incremental_units_k": round(incremental, 2),
                "roas": round(incremental * mean_price / spend, 3),
            }
        )
    table = pd.DataFrame(rows)
    summary = {
        "country": country,
        "r2_train": round(float(model.rsquared), 4),
        "r2_holdout": round(float(r2_hold), 4),
        "mape_holdout": round(mape(y.loc[holdout], pred_hold), 2),
        # Semi-log price term in a levels model: elasticity at the sample mean of sales
        "price_elasticity": round(float(model.params["log_price"] / y.loc[train.index].mean()), 3),
        "n_weeks_train": int(len(train)),
    }
    return table, summary, model


# ---------------------------------------------------------------------------
# Check-in 2a: forecast 2025 from 2023-2024 (regression vs seasonal naive)
# ---------------------------------------------------------------------------
def forecast_check(country: str) -> dict:
    df = panel[panel.country == country].reset_index(drop=True)
    d = add_fourier(df, order=3)
    d["trend"] = d.t / 52
    d["log_sales"] = np.log(d.sales_units_k)
    train = d[d.week < "2025-01-01"]
    test = d[d.week >= "2025-01-01"]
    formula = "log_sales ~ trend + xmas + easter + valentine + " + " + ".join(
        [f"sin_{k} + cos_{k}" for k in (1, 2, 3)]
    )
    fit = smf.ols(formula, data=train).fit()
    pred_reg = np.exp(fit.predict(test))
    # Seasonal naive: the same ISO week one year earlier
    naive = d.sales_units_k.shift(52).loc[test.index]
    return {
        "forecast_country": country,
        "forecast_mape_regression": round(mape(test.sales_units_k, pred_reg), 2),
        "forecast_mape_seasonal_naive": round(mape(test.sales_units_k, naive), 2),
    }


# ---------------------------------------------------------------------------
# Check-in 2b: geo-lift difference-in-differences
# ---------------------------------------------------------------------------
def geolift_check() -> dict:
    g = pd.read_csv(ROOT / "data/experiments/geolift_germany.csv", parse_dates=["week"])
    g = g[g.post_period == 0].copy()  # pre + test weeks only
    g["log_sales"] = np.log(g.sales_units_k)
    # Two-way fixed effects DiD in logs: coefficient on treated x test_period = log lift
    fit = smf.ols("log_sales ~ C(region) + C(week) + treated:test_period", data=g).fit(
        cov_type="cluster", cov_kwds={"groups": g.region}
    )
    b = fit.params["treated:test_period"]
    lo, hi = fit.conf_int().loc["treated:test_period"]
    lift_pct = 100 * (np.exp(b) - 1)
    # Incremental units and spend in the treated regions during the test
    tt = g[(g.treated == 1) & (g.test_period == 1)]
    counterfactual_units = tt.sales_units_k.sum() / np.exp(b)
    incremental_units_k = tt.sales_units_k.sum() - counterfactual_units
    pre_spend = g[(g.treated == 1) & (g.test_period == 0)].groupby("region").paid_social_spend_k.mean()
    incremental_spend_k = tt.paid_social_spend_k.sum() - pre_spend.sum() * tt.week.nunique()
    price_de = panel.loc[(panel.country == "DE") & (panel.week.dt.year == 2025), "price_eur"].mean()
    return {
        "geolift_lift_pct": round(float(lift_pct), 2),
        "geolift_ci_low": round(float(100 * (np.exp(lo) - 1)), 2),
        "geolift_ci_high": round(float(100 * (np.exp(hi) - 1)), 2),
        "geolift_roas": round(float(incremental_units_k * price_de / incremental_spend_k), 3),
    }


# ---------------------------------------------------------------------------
# Check-in 2c: attribution, last touch vs logistic regression
# ---------------------------------------------------------------------------
def attribution_check(country: str) -> dict:
    j = pd.read_csv(ROOT / "data/attribution/journeys.csv")
    j = j[j.country == country].copy()
    conv = j[j.converted == 1]
    last = conv.last_touch.value_counts(normalize=True).reindex(ATT_CHANNELS).fillna(0)

    X = sm.add_constant(j[[f"n_{ch}" for ch in ATT_CHANNELS] + ["mobile", "new_customer"]].astype(float))
    logit = sm.Logit(j.converted, X).fit(disp=0)
    # Channel credit = coefficient x average number of touches among converters (clipped at zero), normalised
    credit = np.array([max(logit.params[f"n_{ch}"], 0) * conv[f"n_{ch}"].mean() for ch in ATT_CHANNELS])
    credit = credit / credit.sum()
    return {
        "attribution_country": country,
        "attribution_last_touch": {ch: round(float(last[ch]), 4) for ch in ATT_CHANNELS},
        "attribution_logit": {ch: round(float(v), 4) for ch, v in zip(ATT_CHANNELS, credit)},
    }


if __name__ == "__main__":
    table, summary, model = fit_mmm(MMM_COUNTRY)
    table.to_csv(OUT / "check_session2.csv", index=False)
    (OUT / "check_session2.json").write_text(json.dumps(summary, indent=2))
    print(table.to_string(index=False))
    print(json.dumps(summary, indent=2))

    s4 = {**forecast_check(FORECAST_COUNTRY), **geolift_check(), **attribution_check(ATTRIBUTION_COUNTRY)}
    (OUT / "check_session4.json").write_text(json.dumps(s4, indent=2))
    print(json.dumps(s4, indent=2))
    print(f"Written to {OUT}")
