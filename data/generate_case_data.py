"""
Case-study data for the group assignment (International Marketing Analytics, WU Vienna, WT 2026/27).

Alpenglow, the fictional Vienna chocolate brand of the labs, runs a direct-to-consumer web shop in
Austria, Germany and Switzerland and a subscription service, the "Alpenglow Club". The data are
built so that every method of Sessions 1-4 has something real to find:

1. data/case/alpenglow_shop_weekly.csv  (3 countries x 156 weeks, 2023-01-02 .. 2025-12-22)
   - Session 1: OLS, fit and interpretation (orders on price, discount, holidays, controls)
   - Session 2: log-log price elasticity (differs by country), dummies (holidays, free shipping,
     Black Friday), a non-linear temperature effect (hot weeks hurt shipped chocolate),
     moderation (paid social works twice as well in free-shipping weeks),
     mediation (TV and online video raise branded search, branded search raises orders),
     adstock and saturation (four channels), diagnostics (AR(1) errors, collinear spend)
   - Session 4: trend, yearly seasonality and autocorrelation for ARIMA / ARIMAX baselines
   The 13 weeks after the student file (2025-12-29 .. 2026-03-23) are kept back as a forecast
   holdout in instructor/ground_truth/case_shop_holdout.csv; data/case/plan_q1_2026.csv gives students the
   drivers known in advance for those weeks (prices, discounts, free shipping, holidays, media plan).

2. data/case/alpenglow_club_customers.csv  (6 000 subscribers)
   - Session 3: logistic regression for churn within six months, odds ratios, an interaction
     (late deliveries hurt monthly subscribers more), a non-linear tenure effect,
     classification and holdout evaluation.

Ground truth (true parameters, contributions, churn probabilities) goes to instructor/ground_truth/
and must not be shared with students before grading.

Run:  python data/generate_case_data.py        Deterministic: seed = 3011.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 3011
rng = np.random.default_rng(SEED)
ROOT = Path(__file__).resolve().parents[1]
CASE_DIR = ROOT / "data" / "case"
GT_DIR = ROOT / "instructor" / "ground_truth"
CASE_DIR.mkdir(parents=True, exist_ok=True)
GT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Weekly web-shop panel
# ---------------------------------------------------------------------------
N_STUDENT, N_HOLDOUT = 156, 13
WEEKS = pd.date_range("2023-01-02", periods=N_STUDENT + N_HOLDOUT, freq="W-MON")
T = len(WEEKS)
t = np.arange(T)
COUNTRIES = ["AT", "DE", "CH"]
CHANNELS = ["tv", "online_video", "paid_search", "paid_social"]

BASE_ORDERS = {"AT": 950.0, "DE": 4300.0, "CH": 650.0}          # weekly orders at reference price, no media
REF_PRICE = {"AT": 24.90, "DE": 23.90, "CH": 29.90}             # EUR per box
PRICE_ELAST = {"AT": -1.3, "DE": -1.7, "CH": -0.8}              # log-log price elasticity
GROWTH = {"AT": 0.08, "DE": 0.12, "CH": 0.30}                   # yearly trend in baseline demand
COUNTRY_TEMP = {"AT": 10.0, "DE": 10.0, "CH": 9.0}
TEMP_OPT, TEMP_QUAD = 8.0, -0.0020                              # log effect: TEMP_QUAD * (temp - 8)^2
FREE_SHIP_MAIN = 0.08                                            # log uplift in free-shipping weeks
HOLIDAY = {"xmas": 0.45, "black_friday": 0.35, "valentine": 0.25, "easter": 0.18, "mothers_day": 0.15}
ADSTOCK = {"tv": 0.60, "online_video": 0.40, "paid_search": 0.10, "paid_social": 0.30}
MAX_LAG = 10
# Direct media effects on log orders: beta * hill(adstock / K); TV and online video work mostly via search
BETA = {"tv": 0.04, "online_video": 0.03, "paid_search": 0.22, "paid_social": 0.20}
HILL_K = {"tv": 60.0, "online_video": 18.0, "paid_search": 14.0, "paid_social": 16.0}   # k EUR at DE scale
HILL_S = {"tv": 1.5, "online_video": 1.3, "paid_search": 1.1, "paid_social": 1.3}
SOCIAL_X_FREESHIP = 1.5                                          # paid social effect x (1 + 1.5 * free_shipping)
SEARCH_A = {"tv": 22.0, "online_video": 14.0}                    # branded-search index points at saturation
SEARCH_B = 0.55                                                  # log orders per unit log(branded search index)
SCALE = {"AT": 0.22, "DE": 1.00, "CH": 0.18}                     # market size for spend and half-saturation
PLANNED = {"tv": 55.0, "online_video": 16.0, "paid_search": 14.0, "paid_social": 15.0}  # k EUR / week, DE scale
AR_PHI, AR_SD = 0.55, 0.045


def geometric_adstock(x: np.ndarray, alpha: float, max_lag: int = MAX_LAG) -> np.ndarray:
    w = alpha ** np.arange(max_lag + 1)
    w = w / w.sum()
    out = np.zeros_like(x, dtype=float)
    for lag, wl in enumerate(w):
        out[lag:] += wl * x[: len(x) - lag]
    return out


def hill(x: np.ndarray, k: float, s: float) -> np.ndarray:
    xs = np.power(np.clip(x, 0, None), s)
    return xs / (xs + k**s)


def holidays(dates: pd.DatetimeIndex) -> pd.DataFrame:
    d = pd.DataFrame(index=dates)
    d["xmas"] = ((dates.month == 12) & (dates.day <= 21)).astype(int)
    d["valentine"] = ((dates.month == 2) & (dates.day >= 5) & (dates.day <= 14)).astype(int)
    bf = {2023: "2023-11-24", 2024: "2024-11-29", 2025: "2025-11-28"}
    easter = {2023: "2023-04-09", 2024: "2024-03-31", 2025: "2025-04-20", 2026: "2026-04-05"}
    mothers = {2023: "2023-05-14", 2024: "2024-05-12", 2025: "2025-05-11"}
    for col, days in (("black_friday", bf), ("easter", easter), ("mothers_day", mothers)):
        d[col] = 0
        for day in days.values():
            day = pd.Timestamp(day)
            span = 20 if col == "easter" else 6
            d.loc[(dates >= day - pd.Timedelta(days=span)) & (dates <= day), col] = 1
    return d


def seasonal_index(dates: pd.DatetimeIndex) -> np.ndarray:
    doy = dates.dayofyear.values
    return 0.20 * np.cos(2 * np.pi * (doy - 350) / 365.25)          # log scale, peak in mid December


def make_spend(country: str, season: np.ndarray) -> pd.DataFrame:
    out = {}
    for ch in CHANNELS:
        level = PLANNED[ch] * SCALE[country] * (1 + 0.8 * season)   # budgets follow demand (endogeneity)
        level *= (1 + {"tv": -0.03, "online_video": 0.10, "paid_search": 0.06, "paid_social": 0.12}[ch]) ** (t / 52)
        x = level * rng.lognormal(0, 0.40, T)
        if ch == "tv":
            if country == "CH":                                      # no TV in Switzerland
                x = np.zeros(T)
            else:
                on = np.zeros(T)
                for y in range(4):
                    starts = rng.choice(np.arange(52 * y + 3, min(52 * y + 46, T - 4)), size=3, replace=False)
                    for s in starts:
                        on[s:s + rng.integers(3, 6)] = 1
                on[(WEEKS.month == 11) | ((WEEKS.month == 12) & (WEEKS.day <= 14))] = 1
                x = x * on * 1.8
        if ch in ("paid_search", "paid_social"):
            x[rng.random(T) < 0.04] = 0
        out[ch] = np.round(x, 2)
    return pd.DataFrame(out, index=WEEKS)


rows, truth_rows = [], []
hol = holidays(WEEKS)
season = seasonal_index(WEEKS)
for c in COUNTRIES:
    spend = make_spend(c, season)
    inflation = (1.035 ** np.floor(t / 52))                          # list price rises each January
    discount = np.where(rng.random(T) < 0.18, rng.choice([0.10, 0.15, 0.20], T), 0.0)
    discount = np.where(hol["black_friday"].values == 1, 0.25, discount)
    price = REF_PRICE[c] * inflation * (1 - discount) * rng.lognormal(0, 0.01, T)
    free_ship = (rng.random(T) < 0.20).astype(int)
    free_ship[hol["xmas"].values == 1] = 1
    temp = COUNTRY_TEMP[c] + 10 * np.sin(2 * np.pi * (WEEKS.dayofyear.values - 110) / 365.25) + rng.normal(0, 3.5, T)

    ad = {ch: geometric_adstock(spend[ch].values, ADSTOCK[ch]) for ch in CHANNELS}
    sat = {ch: hill(ad[ch], HILL_K[ch] * SCALE[c], HILL_S[ch]) for ch in CHANNELS}

    # Mediator: branded search index (0-100), driven by TV and online video plus season and noise
    search = (30 + 6 * np.sign(season) * np.abs(season) / 0.2 + SEARCH_A["tv"] * sat["tv"]
              + SEARCH_A["online_video"] * sat["online_video"] + rng.normal(0, 3.0, T))
    search = np.clip(search, 5, 100)

    ar = np.zeros(T)
    shocks = rng.normal(0, AR_SD, T)
    for i in range(T):
        ar[i] = (AR_PHI * ar[i - 1] if i else 0) + shocks[i]

    parts = {
        "trend": np.log(1 + GROWTH[c]) * t / 52,
        "season": season,
        "price": PRICE_ELAST[c] * np.log(price / REF_PRICE[c]),
        "temperature": TEMP_QUAD * (temp - TEMP_OPT) ** 2,
        "holidays": sum(HOLIDAY[h] * hol[h].values for h in HOLIDAY),
        "free_shipping": FREE_SHIP_MAIN * free_ship,
        "branded_search": SEARCH_B * np.log(search / 30),
        "tv": BETA["tv"] * sat["tv"],
        "online_video": BETA["online_video"] * sat["online_video"],
        "paid_search": BETA["paid_search"] * sat["paid_search"],
        "paid_social": BETA["paid_social"] * sat["paid_social"] * (1 + SOCIAL_X_FREESHIP * free_ship),
        "ar_error": ar,
    }
    log_orders = np.log(BASE_ORDERS[c]) + sum(parts.values())
    orders = np.round(np.exp(log_orders)).astype(int)
    boxes_per_order = 1.35 + rng.normal(0, 0.03, T)
    df = pd.DataFrame({
        "week": WEEKS.date, "country": c, "orders": orders,
        "revenue_eur_k": np.round(orders * boxes_per_order * price / 1000, 2),
        "avg_price_eur": np.round(price, 2), "discount_pct": np.round(100 * discount).astype(int),
        "free_shipping": free_ship, "branded_search_index": np.round(search, 1),
        "temperature_c": np.round(temp, 1),
        **{h: hol[h].values for h in ["xmas", "black_friday", "valentine", "easter", "mothers_day"]},
        **{f"spend_{ch}_k": spend[ch].values for ch in CHANNELS},
    })
    rows.append(df)
    tr = pd.DataFrame({"week": WEEKS.date, "country": c, **{f"log_{k}": np.round(v, 5) for k, v in parts.items()}})
    truth_rows.append(tr)

shop = pd.concat(rows, ignore_index=True)
truth = pd.concat(truth_rows, ignore_index=True)
cut = pd.Timestamp(WEEKS[N_STUDENT - 1]).date()
shop[shop.week <= cut].to_csv(CASE_DIR / "alpenglow_shop_weekly.csv", index=False)
shop[shop.week > cut].to_csv(GT_DIR / "case_shop_holdout.csv", index=False)
truth.to_csv(GT_DIR / "case_shop_true_log_components.csv", index=False)

# Plan file for the Q1 2026 forecast: the exogenous drivers known in advance (prices, discounts, free-shipping
# weeks, holidays, media plan) for the holdout weeks; temperature as the 2023-2025 normal for that week of year.
hold = shop[shop.week > cut].copy()
student = shop[shop.week <= cut].copy()
student["woy"] = pd.to_datetime(student.week).dt.isocalendar().week.values
hold["woy"] = pd.to_datetime(hold.week).dt.isocalendar().week.values
normal = student.groupby(["country", "woy"]).temperature_c.mean().round(1).rename("temperature_normal_c")
plan = hold.merge(normal, on=["country", "woy"], how="left")
plan = plan[["week", "country", "avg_price_eur", "discount_pct", "free_shipping", "temperature_normal_c",
             "xmas", "black_friday", "valentine", "easter", "mothers_day"] + [f"spend_{ch}_k" for ch in CHANNELS]]
plan.to_csv(CASE_DIR / "plan_q1_2026.csv", index=False)

# ---------------------------------------------------------------------------
# 2. Alpenglow Club subscribers: churn within six months
# ---------------------------------------------------------------------------
N = 6000
country = rng.choice(COUNTRIES, N, p=[0.25, 0.60, 0.15])
plan = rng.choice(["monthly", "quarterly"], N, p=[0.65, 0.35])
tenure = np.clip(np.round(rng.gamma(2.0, 6.0, N)), 1, 48).astype(int)
age = np.clip(np.round(rng.normal(41, 12, N)), 18, 80).astype(int)
channel = rng.choice(["paid_search", "paid_social", "influencer", "referral", "tv_campaign"], N,
                     p=[0.30, 0.25, 0.15, 0.15, 0.15])
signup_discount = (rng.random(N) < np.where(np.isin(channel, ["paid_social", "influencer"]), 0.6, 0.3)).astype(int)
price_box = np.round(np.where(country == "CH", 29.9, np.where(country == "DE", 23.9, 24.9))
                     * np.where(plan == "quarterly", 0.92, 1.0), 2)
late = rng.poisson(np.where(country == "CH", 0.9, 0.5), N)
complaints = rng.binomial(3, np.clip(0.06 + 0.08 * late, 0, 0.9))
satisfaction = np.clip(np.round(8.0 - 0.6 * late - 0.8 * complaints + rng.normal(0, 1.3, N)), 1, 10).astype(int)
email_open = np.round(np.clip(rng.beta(2.5, 3.5, N) + 0.004 * np.minimum(tenure, 24), 0, 1), 3)
app_user = (rng.random(N) < np.clip(0.25 + 0.006 * (60 - age), 0.05, 0.8)).astype(int)

COEF = {"intercept": -0.60, "log_tenure": -0.55, "monthly": 0.55, "signup_discount": 0.50, "late_deliveries": 0.30,
        "late_x_monthly": 0.25, "complaints": 0.35, "satisfaction_c": -0.28, "email_open_rate": -1.40, "app_user": -0.45,
        "age_c10": -0.08, "country_CH": 0.20, "country_DE": 0.00,
        "channel_paid_social": 0.30, "channel_influencer": 0.45, "channel_referral": -0.50, "channel_tv_campaign": 0.05}
monthly = (plan == "monthly").astype(int)
eta = (COEF["intercept"] + COEF["log_tenure"] * np.log(tenure) + COEF["monthly"] * monthly
       + COEF["signup_discount"] * signup_discount + COEF["late_deliveries"] * late
       + COEF["late_x_monthly"] * late * monthly + COEF["complaints"] * complaints
       + COEF["satisfaction_c"] * (satisfaction - 7) + COEF["email_open_rate"] * email_open
       + COEF["app_user"] * app_user + COEF["age_c10"] * (age - 40) / 10
       + COEF["country_CH"] * (country == "CH") + sum(COEF[f"channel_{k}"] * (channel == k)
                                                     for k in ["paid_social", "influencer", "referral", "tv_campaign"]))
p = 1 / (1 + np.exp(-eta))
churned = (rng.random(N) < p).astype(int)
club = pd.DataFrame({
    "customer_id": [f"C{100000 + i}" for i in range(N)], "country": country, "plan": plan, "tenure_months": tenure,
    "age": age, "acquisition_channel": channel, "signup_discount": signup_discount, "price_per_box_eur": price_box,
    "late_deliveries_6m": late, "complaints_6m": complaints, "satisfaction": satisfaction,
    "email_open_rate": email_open, "app_user": app_user, "churned_6m": churned,
})
club.to_csv(CASE_DIR / "alpenglow_club_customers.csv", index=False)
pd.DataFrame({"customer_id": club.customer_id, "true_churn_probability": np.round(p, 4)}).to_csv(
    GT_DIR / "case_club_true_probabilities.csv", index=False)

json.dump({
    "seed": SEED,
    "shop": {"price_elasticity": PRICE_ELAST, "yearly_growth": GROWTH, "temperature": {"optimum_c": TEMP_OPT,
             "quadratic_log": TEMP_QUAD}, "holidays_log": HOLIDAY, "free_shipping_log": FREE_SHIP_MAIN,
             "adstock_decay": ADSTOCK, "beta_direct_log": BETA, "hill_k_de_scale": HILL_K, "hill_s": HILL_S,
             "market_scale": SCALE, "paid_social_x_free_shipping": SOCIAL_X_FREESHIP,
             "branded_search_points_at_saturation": SEARCH_A, "branded_search_log_coefficient": SEARCH_B,
             "ar1_phi": AR_PHI, "ar1_sd": AR_SD, "holdout_weeks": N_HOLDOUT},
    "club": {"logit_coefficients": COEF, "notes": "satisfaction_c = satisfaction - 7; age_c10 = (age - 40) / 10; "
                                                   "tenure enters as log(tenure_months)"},
}, open(GT_DIR / "case_truth.json", "w"), indent=2)

print("shop:", shop[shop.week <= cut].shape, "holdout:", shop[shop.week > cut].shape)
print(shop[shop.week <= cut].groupby("country")[["orders", "avg_price_eur", "branded_search_index"]].mean().round(1))
print("club:", club.shape, "churn rate", club.churned_6m.mean().round(3))
