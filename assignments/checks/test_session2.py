"""
Lab check-in 1 (after Session 2): a one-country OLS marketing mix model.

Expected files in submissions/<github_username>/:
  check_session2.csv   columns: country, channel, adstock_alpha, coefficient,
                       total_spend_k, incremental_units_k, roas
                       exactly 5 rows (one per channel), one country
  check_session2.json  keys: country, r2_train, r2_holdout, mape_holdout,
                       price_elasticity, n_weeks_train
"""

from __future__ import annotations

import json

import pandas as pd
import pytest

from conftest import COUNTRIES, MMM_CHANNELS, require_file

CSV_COLUMNS = ["country", "channel", "adstock_alpha", "coefficient", "total_spend_k", "incremental_units_k", "roas"]
JSON_KEYS = ["country", "r2_train", "r2_holdout", "mape_holdout", "price_elasticity", "n_weeks_train"]
ALLOWED_COUNTRIES = ["AT", "FR", "IT", "NL", "PL"]  # Germany is the lab example


@pytest.fixture
def table(submission) -> pd.DataFrame:
    return pd.read_csv(require_file(submission, "check_session2.csv"))


@pytest.fixture
def summary(submission) -> dict:
    with open(require_file(submission, "check_session2.json")) as f:
        return json.load(f)


# ---- files and schema ------------------------------------------------------

def test_csv_schema(table):
    missing = [c for c in CSV_COLUMNS if c not in table.columns]
    assert not missing, f"missing columns: {missing}"
    assert len(table) == 5, f"expected exactly 5 rows (one per channel), got {len(table)}"
    assert sorted(table.channel) == sorted(MMM_CHANNELS), f"channels must be {MMM_CHANNELS}"
    assert table.country.nunique() == 1, "all rows must refer to one country"
    assert table.country.iloc[0] in ALLOWED_COUNTRIES, f"country must be one of {ALLOWED_COUNTRIES}"
    for c in CSV_COLUMNS[2:]:
        assert pd.api.types.is_numeric_dtype(table[c]), f"column {c} must be numeric"
        assert table[c].notna().all(), f"column {c} has missing values"


def test_json_schema(summary):
    missing = [k for k in JSON_KEYS if k not in summary]
    assert not missing, f"missing keys: {missing}"
    assert summary["country"] in COUNTRIES


def test_csv_and_json_same_country(table, summary):
    assert table.country.iloc[0] == summary["country"]


# ---- plausibility of the model table ----------------------------------------

def test_adstock_alpha_range(table):
    bad = table[(table.adstock_alpha < 0) | (table.adstock_alpha >= 1)]
    assert bad.empty, f"adstock_alpha must satisfy 0 <= alpha < 1:\n{bad}"


def test_roas_range(table):
    bad = table[(table.roas < 0.1) | (table.roas > 8)]
    assert bad.empty, f"ROAS outside the plausible range 0.1 to 8:\n{bad}"


def test_incremental_units_mostly_positive(table):
    n_pos = int((table.incremental_units_k > 0).sum())
    assert n_pos >= 4, f"incremental_units_k must be positive for at least 4 of 5 channels (got {n_pos})"


def test_roas_consistent_with_units_price_spend(table, panel):
    country = table.country.iloc[0]
    mean_price = panel.loc[panel.country == country, "price_eur"].mean()  # 2023-2025 average
    implied = table.incremental_units_k * mean_price / table.total_spend_k
    rel_err = ((table.roas - implied).abs() / implied.abs()).max()
    assert rel_err <= 0.25, (
        "roas should equal incremental_units_k x mean price / total_spend_k within 25%:\n"
        f"{pd.DataFrame({'channel': table.channel, 'roas': table.roas, 'implied': implied.round(3)})}"
    )


def test_total_spend_matches_data(table, panel):
    country = table.country.iloc[0]
    sub = panel[panel.country == country]
    for _, row in table.iterrows():
        actual = sub[f"spend_{row.channel}_k"].sum()
        assert abs(row.total_spend_k - actual) / actual <= 0.01, (
            f"{row.channel}: total_spend_k {row.total_spend_k} differs from the data ({actual:.2f}) by more than 1%"
        )


# ---- plausibility of the fit summary ----------------------------------------

def test_r2_ranges(summary):
    for k in ("r2_train", "r2_holdout"):
        assert 0.5 < summary[k] < 1, f"{k} = {summary[k]} must be in (0.5, 1)"


def test_mape_holdout(summary):
    assert 0 <= summary["mape_holdout"] < 25, f"mape_holdout = {summary['mape_holdout']} must be below 25%"


def test_price_elasticity_range(summary):
    e = summary["price_elasticity"]
    assert -4 <= e <= -0.3, f"price_elasticity = {e} must lie between -4 and -0.3"


def test_n_weeks_train(summary):
    n = summary["n_weeks_train"]
    assert 100 <= n <= 110, f"n_weeks_train = {n}; train on 2023-2024 (about 104 weeks) and hold out 2025"
