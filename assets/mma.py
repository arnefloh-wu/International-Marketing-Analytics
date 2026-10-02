"""
Helper functions for International Marketing Analytics (WU Vienna, CEMS).

Import in labs with:
    import sys; sys.path.append("../../assets")
    from mma import *
"""

from __future__ import annotations

import numpy as np
import pandas as pd

CHANNELS = ["tv", "online_video", "paid_search", "paid_social", "ooh"]
CHANNEL_LABELS = {
    "tv": "TV",
    "online_video": "Online video",
    "paid_search": "Paid search",
    "paid_social": "Paid social",
    "ooh": "Out-of-home",
}
COUNTRIES = ["AT", "DE", "FR", "IT", "NL", "PL"]
COUNTRY_NAMES = {
    "AT": "Austria", "DE": "Germany", "FR": "France", "IT": "Italy", "NL": "Netherlands", "PL": "Poland",
}


def load_panel(path: str = "data/mmm/alpenglow_weekly.csv") -> pd.DataFrame:
    """Load the Alpenglow weekly panel with parsed dates and a time index per country."""
    df = pd.read_csv(path, parse_dates=["week"])
    df = df.sort_values(["country", "week"]).reset_index(drop=True)
    df["t"] = df.groupby("country").cumcount()
    df["year"] = df.week.dt.year
    df["week_of_year"] = df.week.dt.isocalendar().week.astype(int)
    return df


def geometric_adstock(x: np.ndarray, alpha: float, max_lag: int = 12, normalise: bool = True) -> np.ndarray:
    """Geometric adstock: y_t = sum_l w_l x_{t-l}, w_l = alpha^l (normalised to sum 1 by default)."""
    x = np.asarray(x, dtype=float)
    w = alpha ** np.arange(max_lag + 1)
    if normalise:
        w = w / w.sum()
    out = np.zeros_like(x)
    for lag, wl in enumerate(w):
        out[lag:] += wl * x[: len(x) - lag]
    return out


def hill(x: np.ndarray, k: float, s: float = 1.0) -> np.ndarray:
    """Hill saturation in [0, 1): x^s / (x^s + k^s). k = half-saturation point."""
    x = np.clip(np.asarray(x, dtype=float), 0, None)
    return x**s / (x**s + k**s)


def logistic_saturation(x: np.ndarray, lam: float) -> np.ndarray:
    """Logistic saturation in [0, 1): 1 - exp(-lam * x)."""
    return 1 - np.exp(-lam * np.clip(np.asarray(x, dtype=float), 0, None))


def add_fourier(df: pd.DataFrame, t_col: str = "t", period: float = 52.18, order: int = 2) -> pd.DataFrame:
    """Add Fourier seasonality terms sin_k, cos_k for k = 1..order."""
    out = df.copy()
    for k in range(1, order + 1):
        out[f"sin_{k}"] = np.sin(2 * np.pi * k * out[t_col] / period)
        out[f"cos_{k}"] = np.cos(2 * np.pi * k * out[t_col] / period)
    return out


def mape(y_true, y_pred) -> float:
    y_true, y_pred = np.asarray(y_true, float), np.asarray(y_pred, float)
    return float(np.mean(np.abs((y_true - y_pred) / y_true)) * 100)


def rmse(y_true, y_pred) -> float:
    y_true, y_pred = np.asarray(y_true, float), np.asarray(y_pred, float)
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def contribution_table(contrib: pd.DataFrame, price: float | pd.Series, spend: pd.DataFrame) -> pd.DataFrame:
    """Summarise incremental units, revenue, spend and ROAS per channel.

    contrib: DataFrame with one column per channel (incremental units, thousands)
    price:   scalar or Series (EUR per unit)
    spend:   DataFrame with same columns (thousand EUR)
    """
    units = contrib.sum()
    revenue = (contrib.mul(price, axis=0) if isinstance(price, pd.Series) else contrib * price).sum()
    sp = spend.sum()
    out = pd.DataFrame({"incremental_units_k": units, "incremental_revenue_k": revenue, "spend_k": sp})
    out["roas"] = out.incremental_revenue_k / out.spend_k
    return out.round(2)
