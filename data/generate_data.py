"""
Synthetic data generator for International Marketing Analytics (WU Vienna, CEMS).

Generates three teaching datasets around a fictional premium chocolate brand,
"Alpenglow", headquartered in Vienna and selling in six European markets.

1. data/mmm/alpenglow_weekly.csv
   Weekly country panel (6 countries x 156 weeks, 2023-01-02 .. 2025-12-29):
   media spend in five channels, price, promotion, distribution, competitor
   activity, macro controls, holidays, and unit sales / revenue.
   The true data-generating process uses geometric adstock + Hill saturation
   with country-specific effectiveness. Ground truth is stored under
   instructor/ground_truth/ (never share with students before grading).

2. data/experiments/geolift_germany.csv
   Region-week panel for a geo-lift test in Germany: 40 regions, 64 weeks.
   Twelve treated regions receive a paid-social uplift for 8 weeks.

3. data/attribution/journeys.csv  and  journeys_long.csv
   Customer-journey (multi-touch) data across the six markets with a
   conversion flag, generated from a known logistic model.

Run:  python data/generate_data.py
Deterministic: seed = 2026.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize

SEED = 2026
rng = np.random.default_rng(SEED)

ROOT = Path(__file__).resolve().parents[1]
MMM_DIR = ROOT / "data" / "mmm"
EXP_DIR = ROOT / "data" / "experiments"
ATT_DIR = ROOT / "data" / "attribution"
GT_DIR = ROOT / "instructor" / "ground_truth"
for d in (MMM_DIR, EXP_DIR, ATT_DIR, GT_DIR):
    d.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Country metadata (approximate public figures, for teaching only)
# ---------------------------------------------------------------------------
COUNTRIES = ["AT", "DE", "FR", "IT", "NL", "PL"]
COUNTRY_META = pd.DataFrame(
    {
        "country": COUNTRIES,
        "country_name": ["Austria", "Germany", "France", "Italy", "Netherlands", "Poland"],
        "population_m": [9.1, 84.5, 68.4, 58.9, 17.9, 36.7],
        "gdp_per_capita_eur_k": [52.0, 49.5, 41.0, 35.5, 57.0, 20.5],
        "hofstede_idv": [55, 67, 71, 76, 80, 60],
        "hofstede_uai": [70, 65, 86, 75, 53, 93],
        "hofstede_ltowvs": [60, 83, 63, 61, 67, 38],
        "eurozone": [1, 1, 1, 1, 1, 0],
        "years_in_market": [40, 25, 12, 10, 8, 4],
        "retail_concentration": [0.78, 0.85, 0.72, 0.55, 0.80, 0.62],
    }
)

# ---------------------------------------------------------------------------
# 2. Weekly country panel (MMM)
# ---------------------------------------------------------------------------
WEEKS = pd.date_range("2023-01-02", periods=156, freq="W-MON")
T = len(WEEKS)
CHANNELS = ["tv", "online_video", "paid_search", "paid_social", "ooh"]

# Adstock decay (geometric), channel-specific, same across countries
ADSTOCK = {"tv": 0.70, "online_video": 0.50, "paid_search": 0.10, "paid_social": 0.30, "ooh": 0.60}
MAX_LAG = 12

# Base weekly sales (thousand units) at reference price, no media
BASE_SALES = {"AT": 95.0, "DE": 520.0, "FR": 260.0, "IT": 210.0, "NL": 120.0, "PL": 90.0}
# Average retail price per unit (EUR); Poland priced lower; premium positioning
REF_PRICE = {"AT": 3.20, "DE": 3.10, "FR": 3.35, "IT": 3.05, "NL": 3.25, "PL": 2.40}
# Price elasticity of baseline demand
PRICE_ELAST = {"AT": -1.4, "DE": -1.7, "FR": -1.5, "IT": -1.9, "NL": -1.6, "PL": -2.3}
# Promotion effect: baseline uplift per unit of promo share (0..1)
PROMO_EFF = {"AT": 0.55, "DE": 0.70, "FR": 0.60, "IT": 0.80, "NL": 0.50, "PL": 0.95}

# Media effectiveness: beta = maximum incremental weekly sales (thousand units)
# at full saturation, per channel and country. Country heterogeneity is the
# point of the course (e.g. TV weaker in NL, search stronger in DE, social
# strong in PL, OOH strong in FR/IT).
BETA = pd.DataFrame(
    {
        "tv":           {"AT": 28, "DE": 150, "FR": 80, "IT": 75, "NL": 18, "PL": 30},
        "online_video": {"AT": 14, "DE": 70,  "FR": 32, "IT": 26, "NL": 26, "PL": 20},
        "paid_search":  {"AT": 10, "DE": 75,  "FR": 28, "IT": 20, "NL": 20, "PL": 9},
        "paid_social":  {"AT": 12, "DE": 55,  "FR": 30, "IT": 34, "NL": 24, "PL": 32},
        "ooh":          {"AT": 9,  "DE": 40,  "FR": 36, "IT": 30, "NL": 8,  "PL": 7},
    }
).T  # rows = channel, cols = country

# Hill saturation: response = x^s / (x^s + K^s). K = half-saturation spend
# (thousand EUR of *adstocked* spend). Scaled with market size.
MARKET_SCALE = {"AT": 0.18, "DE": 1.00, "FR": 0.55, "IT": 0.45, "NL": 0.22, "PL": 0.20}
HILL_K_BASE = {"tv": 180.0, "online_video": 60.0, "paid_search": 45.0, "paid_social": 50.0, "ooh": 70.0}
HILL_S = {"tv": 1.6, "online_video": 1.3, "paid_search": 1.1, "paid_social": 1.4, "ooh": 1.8}

# Weekly planned spend (thousand EUR) by channel, per country, before flighting
PLANNED_SPEND = pd.DataFrame(
    {
        "tv":           {"AT": 22, "DE": 150, "FR": 70, "IT": 60, "NL": 20, "PL": 18},
        "online_video": {"AT": 8,  "DE": 45,  "FR": 22, "IT": 16, "NL": 14, "PL": 9},
        "paid_search":  {"AT": 6,  "DE": 40,  "FR": 18, "IT": 12, "NL": 9,  "PL": 5},
        "paid_social":  {"AT": 7,  "DE": 38,  "FR": 20, "IT": 18, "NL": 12, "PL": 12},
        "ooh":          {"AT": 5,  "DE": 30,  "FR": 25, "IT": 18, "NL": 5,  "PL": 4},
    }
).T


def geometric_adstock(x: np.ndarray, alpha: float, max_lag: int = MAX_LAG) -> np.ndarray:
    """Geometric adstock with normalised weights (sum of weights = 1)."""
    w = alpha ** np.arange(max_lag + 1)
    w = w / w.sum()
    out = np.zeros_like(x, dtype=float)
    for lag, wl in enumerate(w):
        out[lag:] += wl * x[: len(x) - lag]
    return out


def hill(x: np.ndarray, k: float, s: float) -> np.ndarray:
    xs = np.power(np.clip(x, 0, None), s)
    return xs / (xs + k**s)


def season_curve(dates: pd.DatetimeIndex) -> np.ndarray:
    """Chocolate seasonality: strong Q4, Easter bump, summer dip."""
    doy = dates.dayofyear.values
    base = 1.0 + 0.18 * np.cos(2 * np.pi * (doy - 355) / 365.25)  # peak around late Dec
    summer_dip = -0.10 * np.exp(-((doy - 200) ** 2) / (2 * 25**2))
    return base + summer_dip


def holiday_flags(dates: pd.DatetimeIndex) -> pd.DataFrame:
    easter = {2023: "2023-04-09", 2024: "2024-03-31", 2025: "2025-04-20"}
    df = pd.DataFrame(index=dates)
    df["xmas"] = ((dates.month == 12) & (dates.day >= 4)).astype(int)
    df["easter"] = 0
    df["valentine"] = ((dates.month == 2) & (dates.day >= 5) & (dates.day <= 14)).astype(int)
    for y, e in easter.items():
        e = pd.Timestamp(e)
        mask = (dates >= e - pd.Timedelta(days=20)) & (dates <= e)
        df.loc[mask, "easter"] = 1
    return df


def make_spend(country: str) -> pd.DataFrame:
    """Planned budgets with Q4 uplift (endogenous to demand seasonality),
    campaign bursts, TV flighting and noise."""
    season = season_curve(WEEKS)
    spend = {}
    for ch in CHANNELS:
        plan = PLANNED_SPEND.loc[ch, country]
        # Budget follows seasonality (the classic confound in MMM)
        level = plan * (0.6 + 0.6 * (season - season.min()) / (season.max() - season.min()))
        # Year-on-year budget growth differs by channel (digital shift)
        growth = {"tv": -0.04, "online_video": 0.12, "paid_search": 0.08, "paid_social": 0.15, "ooh": 0.0}[ch]
        level = level * (1 + growth) ** (np.arange(T) / 52)
        noise = rng.lognormal(0, 0.35, T)
        x = level * noise
        # Campaign bursts: 3-4 per year for TV/OOH, flighting pattern
        if ch in ("tv", "ooh"):
            on = np.zeros(T)
            for y in range(3):
                starts = rng.choice(np.arange(52 * y + 2, 52 * y + 44), size=rng.integers(3, 5), replace=False)
                for s in starts:
                    on[s : s + rng.integers(3, 7)] = 1
            # Always on in the weeks before Christmas
            on[(WEEKS.month == 11) | ((WEEKS.month == 12) & (WEEKS.day <= 20))] = 1
            x = x * (0.15 + 0.85 * on) * 1.6
        # Occasional dark weeks for search/social (budget pauses)
        if ch in ("paid_search", "paid_social"):
            dark = rng.random(T) < 0.03
            x[dark] = 0
        spend[ch] = np.round(x, 2)
    return pd.DataFrame(spend, index=WEEKS)


def make_country_panel(country: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    spend = make_spend(country)
    hol = holiday_flags(WEEKS)
    season = season_curve(WEEKS)
    trend = (1 + {"AT": 0.01, "DE": 0.02, "FR": 0.03, "IT": 0.02, "NL": 0.05, "PL": 0.09}[country]) ** (np.arange(T) / 52)

    # Price: reference price with slow inflation and promotional dips
    inflation = (1 + {"AT": 0.035, "DE": 0.03, "FR": 0.028, "IT": 0.03, "NL": 0.032, "PL": 0.06}[country]) ** (np.arange(T) / 52)
    promo_share = np.clip(rng.beta(1.6, 6, T) * (1 + 0.5 * hol["xmas"].values + 0.4 * hol["easter"].values), 0, 0.95)
    price = REF_PRICE[country] * inflation * (1 - 0.18 * promo_share) * rng.lognormal(0, 0.015, T)

    distribution = np.clip(0.70 + 0.004 * np.arange(T) / 4 + rng.normal(0, 0.02, T), 0.5, 0.98)
    if country == "PL":
        distribution = np.clip(0.35 + 0.0035 * np.arange(T) + rng.normal(0, 0.02, T), 0.3, 0.95)
    competitor_spend = PLANNED_SPEND[country].sum() * 0.9 * rng.lognormal(0, 0.3, T) * (0.8 + 0.4 * (season / season.max()))
    consumer_conf = -5 + np.cumsum(rng.normal(0, 0.8, T))
    consumer_conf = consumer_conf - consumer_conf.mean()
    temperature = {"AT": 10, "DE": 10, "FR": 13, "IT": 16, "NL": 11, "PL": 9}[country] + 10 * np.sin(2 * np.pi * (WEEKS.dayofyear.values - 110) / 365.25) + rng.normal(0, 2, T)

    # Baseline (no media)
    baseline = (
        BASE_SALES[country]
        * season
        * trend
        * (price / REF_PRICE[country]) ** PRICE_ELAST[country]
        * (1 + PROMO_EFF[country] * promo_share)
        * (distribution / distribution.mean()) ** 0.8
        * (1 + 0.006 * consumer_conf)
        * (1 - 0.004 * np.clip(temperature - 22, 0, None))  # heat hurts chocolate
        * (1 - 0.05 * np.log(competitor_spend / competitor_spend.mean()))
    )

    # Media contributions
    contrib = {}
    sat = {}
    for ch in CHANNELS:
        ad = geometric_adstock(spend[ch].values, ADSTOCK[ch])
        k = HILL_K_BASE[ch] * MARKET_SCALE[country]
        s = HILL_S[ch]
        sat[ch] = hill(ad, k, s)
        contrib[ch] = BETA.loc[ch, country] * sat[ch]
    contrib = pd.DataFrame(contrib, index=WEEKS)

    noise = rng.normal(0, 0.035, T)
    sales = (baseline + contrib.sum(axis=1).values) * (1 + noise)
    sales = np.clip(sales, 1, None)

    df = pd.DataFrame(
        {
            "week": WEEKS,
            "country": country,
            "sales_units_k": np.round(sales, 3),
            "revenue_eur_k": np.round(sales * price, 3),
            "price_eur": np.round(price, 3),
            "promo_share": np.round(promo_share, 3),
            "distribution": np.round(distribution, 3),
            "competitor_spend_k": np.round(competitor_spend, 2),
            "consumer_confidence": np.round(consumer_conf, 2),
            "temperature_c": np.round(temperature, 1),
            "xmas": hol["xmas"].values,
            "easter": hol["easter"].values,
            "valentine": hol["valentine"].values,
        }
    )
    for ch in CHANNELS:
        df[f"spend_{ch}_k"] = spend[ch].values

    truth = pd.DataFrame({"week": WEEKS, "country": country, "baseline": np.round(baseline, 3)})
    for ch in CHANNELS:
        truth[f"contrib_{ch}"] = np.round(contrib[ch].values, 3)
    truth["noise_factor"] = np.round(1 + noise, 4)
    return df, truth


panel, truth = [], []
for c in COUNTRIES:
    d, t = make_country_panel(c)
    panel.append(d)
    truth.append(t)
panel = pd.concat(panel, ignore_index=True)
truth = pd.concat(truth, ignore_index=True)

panel.to_csv(MMM_DIR / "alpenglow_weekly.csv", index=False)
COUNTRY_META.to_csv(MMM_DIR / "country_meta.csv", index=False)
truth.to_csv(GT_DIR / "mmm_true_contributions.csv", index=False)

# ---- Ground-truth summaries: ROAS, marginal ROAS, optimal allocation -------
gt_rows = []
for c in COUNTRIES:
    sub = panel[panel.country == c]
    tr = truth[truth.country == c]
    price_mean = sub.price_eur.mean()
    for ch in CHANNELS:
        spend_total = sub[f"spend_{ch}_k"].sum()
        contrib_total = tr[f"contrib_{ch}"].sum()  # thousand units
        gt_rows.append(
            {
                "country": c,
                "channel": ch,
                "total_spend_k": round(spend_total, 1),
                "total_incremental_units_k": round(contrib_total, 1),
                "total_incremental_revenue_k": round(contrib_total * price_mean, 1),
                "true_roas": round(contrib_total * price_mean / spend_total, 3),
                "beta_max_units_k": BETA.loc[ch, c],
                "hill_k": HILL_K_BASE[ch] * MARKET_SCALE[c],
                "hill_s": HILL_S[ch],
                "adstock_alpha": ADSTOCK[ch],
            }
        )
gt = pd.DataFrame(gt_rows)


def steady_state_revenue(spend_vec: np.ndarray, countries, channels) -> float:
    """Expected weekly incremental revenue at steady-state weekly spend."""
    rev = 0.0
    i = 0
    for c in countries:
        price_mean = panel.loc[panel.country == c, "price_eur"].mean()
        for ch in channels:
            # with normalised adstock weights, steady-state adstocked spend = spend
            k = HILL_K_BASE[ch] * MARKET_SCALE[c]
            rev += BETA.loc[ch, c] * hill(np.array([spend_vec[i]]), k, HILL_S[ch])[0] * price_mean
            i += 1
    return rev


# Optimal allocation of the 2025 average weekly media budget across all
# 30 country-channel cells, holding total constant.
last_year = panel[panel.week >= "2025-01-01"]
cells = [(c, ch) for c in COUNTRIES for ch in CHANNELS]
current = np.array([last_year.loc[last_year.country == c, f"spend_{ch}_k"].mean() for c, ch in cells])
budget = current.sum()
cons = {"type": "eq", "fun": lambda x: x.sum() - budget}
res = minimize(
    lambda x: -steady_state_revenue(x, COUNTRIES, CHANNELS),
    x0=current,
    bounds=[(0, budget)] * len(cells),
    constraints=[cons],
    method="SLSQP",
    options={"maxiter": 500},
)
opt = pd.DataFrame(
    {
        "country": [c for c, _ in cells],
        "channel": [ch for _, ch in cells],
        "current_weekly_spend_k_2025": np.round(current, 2),
        "optimal_weekly_spend_k": np.round(res.x, 2),
    }
)
opt["change_pct"] = np.round(100 * (opt.optimal_weekly_spend_k / opt.current_weekly_spend_k_2025 - 1), 1)
summary = {
    "weekly_budget_k": round(float(budget), 2),
    "weekly_incremental_revenue_current_k": round(steady_state_revenue(current, COUNTRIES, CHANNELS), 2),
    "weekly_incremental_revenue_optimal_k": round(-res.fun, 2),
    "improvement_pct": round(100 * (-res.fun / steady_state_revenue(current, COUNTRIES, CHANNELS) - 1), 2),
}
gt.to_csv(GT_DIR / "mmm_true_parameters.csv", index=False)
opt.to_csv(GT_DIR / "mmm_optimal_allocation.csv", index=False)
(GT_DIR / "mmm_ground_truth_summary.json").write_text(
    json.dumps(
        {
            "seed": SEED,
            "adstock_alpha": ADSTOCK,
            "hill_s": HILL_S,
            "hill_k_base": HILL_K_BASE,
            "market_scale": MARKET_SCALE,
            "price_elasticity": PRICE_ELAST,
            "promo_effect": PROMO_EFF,
            "base_sales_k": BASE_SALES,
            "beta_max_units_k": BETA.to_dict(),
            "optimisation": summary,
        },
        indent=2,
    )
)

# ---------------------------------------------------------------------------
# 3. Geo-lift experiment in Germany
# ---------------------------------------------------------------------------
REGIONS = [
    "Berlin", "Hamburg", "München", "Köln", "Frankfurt", "Stuttgart", "Düsseldorf", "Leipzig",
    "Dortmund", "Essen", "Bremen", "Dresden", "Hannover", "Nürnberg", "Duisburg", "Bochum",
    "Wuppertal", "Bielefeld", "Bonn", "Münster", "Mannheim", "Karlsruhe", "Augsburg", "Wiesbaden",
    "Mönchengladbach", "Gelsenkirchen", "Aachen", "Braunschweig", "Chemnitz", "Kiel", "Halle",
    "Magdeburg", "Freiburg", "Krefeld", "Mainz", "Lübeck", "Erfurt", "Oberhausen", "Rostock", "Kassel",
]
N_REG = len(REGIONS)
EXP_WEEKS = pd.date_range("2024-10-07", periods=64, freq="W-MON")  # 48 pre, 8 test, 8 post
TEST_START, TEST_END = 48, 56
region_size = rng.lognormal(np.log(12), 0.6, N_REG)  # weekly sales (thousand units)
region_season = season_curve(EXP_WEEKS)
common_shock = np.cumsum(rng.normal(0, 0.01, len(EXP_WEEKS)))
# Treatment assignment: stratified by size (teaches matched-market design)
order = np.argsort(region_size)
treated_idx = order[1::3][:12]  # every third region in the size ordering
treated = np.zeros(N_REG, dtype=int)
treated[treated_idx] = 1
TRUE_LIFT = 0.06  # 6% incremental sales during test weeks
rows = []
for i, r in enumerate(REGIONS):
    base_social = 0.9 * region_size[i] * rng.lognormal(0, 0.2, len(EXP_WEEKS))  # thousand EUR
    social = base_social.copy()
    social[TEST_START:TEST_END] *= np.where(treated[i], 2.5, 1.0)
    region_noise = rng.normal(0, 0.04, len(EXP_WEEKS))
    region_trend = (1 + rng.normal(0.02, 0.015)) ** (np.arange(len(EXP_WEEKS)) / 52)
    lift = np.ones(len(EXP_WEEKS))
    if treated[i]:
        lift[TEST_START:TEST_END] = 1 + TRUE_LIFT
        lift[TEST_END : TEST_END + 2] = 1 + TRUE_LIFT * np.array([0.4, 0.15])  # small carryover
    sales = region_size[i] * region_season * region_trend * (1 + common_shock) * lift * (1 + region_noise)
    for t, w in enumerate(EXP_WEEKS):
        rows.append(
            {
                "week": w,
                "region": r,
                "treated": treated[i],
                "test_period": int(TEST_START <= t < TEST_END),
                "post_period": int(t >= TEST_END),
                "paid_social_spend_k": round(social[t], 2),
                "sales_units_k": round(sales[t], 3),
                "population_k": int(round(region_size[i] * 55)),
            }
        )
geo = pd.DataFrame(rows)
geo.to_csv(EXP_DIR / "geolift_germany.csv", index=False)
(GT_DIR / "geolift_ground_truth.json").write_text(
    json.dumps({"true_lift_pct": TRUE_LIFT * 100, "treated_regions": [REGIONS[i] for i in treated_idx],
                "test_weeks": [str(EXP_WEEKS[TEST_START].date()), str(EXP_WEEKS[TEST_END - 1].date())],
                "carryover_weeks_after_test": 2}, indent=2)
)

# ---------------------------------------------------------------------------
# 4. Multi-market attribution journeys
# ---------------------------------------------------------------------------
ATT_CH = ["display", "paid_search", "paid_social", "email", "affiliate", "organic"]
N_JOURNEYS = 60_000
# True logistic coefficients (per touch), base rate by country, with country x channel interaction
ATT_BETA = {
    "display": 0.15, "paid_search": 0.55, "paid_social": 0.35, "email": 0.60, "affiliate": 0.45, "organic": 0.50,
}
COUNTRY_INTERCEPT = {"AT": -2.6, "DE": -2.4, "FR": -2.7, "IT": -2.9, "NL": -2.3, "PL": -3.1}
COUNTRY_MOD = {  # multiplicative modifier on channel coefficients
    "AT": {"paid_social": 0.9}, "DE": {"paid_search": 1.3}, "FR": {"display": 1.4, "email": 0.8},
    "IT": {"paid_social": 1.5}, "NL": {"email": 1.3}, "PL": {"paid_social": 1.6, "affiliate": 1.4},
}
CHANNEL_PROB = np.array([0.25, 0.22, 0.20, 0.10, 0.08, 0.15])
country_draw = rng.choice(COUNTRIES, size=N_JOURNEYS, p=[0.08, 0.40, 0.18, 0.14, 0.10, 0.10])
path_len = np.clip(rng.geometric(0.4, N_JOURNEYS), 1, 8)
jrows, lrows = [], []
for j in range(N_JOURNEYS):
    c = country_draw[j]
    touches = rng.choice(ATT_CH, size=path_len[j], p=CHANNEL_PROB)
    counts = {ch: int((touches == ch).sum()) for ch in ATT_CH}
    mobile = int(rng.random() < {"AT": 0.6, "DE": 0.55, "FR": 0.6, "IT": 0.7, "NL": 0.65, "PL": 0.75}[c])
    new_customer = int(rng.random() < 0.6)
    lin = COUNTRY_INTERCEPT[c] + 0.25 * mobile - 0.5 * new_customer
    for ch in ATT_CH:
        lin += ATT_BETA[ch] * COUNTRY_MOD[c].get(ch, 1.0) * counts[ch]
    # last-touch bonus for search (intent)
    lin += 0.3 * (touches[-1] == "paid_search")
    p = 1 / (1 + np.exp(-lin))
    conv = int(rng.random() < p)
    order_value = round(float(rng.lognormal(np.log(24), 0.4)), 2) if conv else 0.0
    start = pd.Timestamp("2025-01-01") + pd.Timedelta(days=int(rng.integers(0, 330)))
    jrows.append(
        {
            "journey_id": j + 1, "country": c, "start_date": start.date(), "path_length": int(path_len[j]),
            "first_touch": touches[0], "last_touch": touches[-1], "mobile": mobile, "new_customer": new_customer,
            **{f"n_{ch}": counts[ch] for ch in ATT_CH}, "converted": conv, "order_value_eur": order_value,
            "path": " > ".join(touches),
        }
    )
    for k, ch in enumerate(touches):
        lrows.append({"journey_id": j + 1, "country": c, "touch_order": k + 1,
                      "touch_date": (start + pd.Timedelta(days=int(k * rng.integers(0, 4)))).date(),
                      "channel": ch, "converted": conv})
journeys = pd.DataFrame(jrows)
journeys_long = pd.DataFrame(lrows)
journeys.to_csv(ATT_DIR / "journeys.csv", index=False)
journeys_long.to_csv(ATT_DIR / "journeys_long.csv", index=False)
(GT_DIR / "attribution_ground_truth.json").write_text(
    json.dumps({"beta": ATT_BETA, "country_intercept": COUNTRY_INTERCEPT, "country_modifier": COUNTRY_MOD,
                "mobile_effect": 0.25, "new_customer_effect": -0.5, "last_touch_search_bonus": 0.3}, indent=2)
)

print("Panel:", panel.shape, "| Geo-lift:", geo.shape, "| Journeys:", journeys.shape)
print("Conversion rate:", journeys.converted.mean().round(4))
print("Optimisation summary:", summary)
print(gt.pivot(index="country", columns="channel", values="true_roas").round(2))
