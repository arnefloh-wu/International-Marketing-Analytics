"""
Lab check-in 2 (after Session 4): forecasting, geo-lift and attribution.

Expected file in submissions/<github_username>/:
  check_session4.json with keys
    forecast_country, forecast_mape_regression, forecast_mape_seasonal_naive,
    geolift_lift_pct, geolift_ci_low, geolift_ci_high, geolift_roas,
    attribution_country, attribution_last_touch (dict channel -> share),
    attribution_logit (dict channel -> share)
"""

from __future__ import annotations

import json

import pytest

from conftest import ATTRIBUTION_CHANNELS, COUNTRIES, require_file

KEYS = [
    "forecast_country", "forecast_mape_regression", "forecast_mape_seasonal_naive",
    "geolift_lift_pct", "geolift_ci_low", "geolift_ci_high", "geolift_roas",
    "attribution_country", "attribution_last_touch", "attribution_logit",
]


@pytest.fixture
def result(submission) -> dict:
    with open(require_file(submission, "check_session4.json")) as f:
        return json.load(f)


def test_keys_present(result):
    missing = [k for k in KEYS if k not in result]
    assert not missing, f"missing keys: {missing}"
    assert result["forecast_country"] in COUNTRIES
    assert result["attribution_country"] in COUNTRIES


def test_forecast_mape_ranges(result):
    for k in ("forecast_mape_regression", "forecast_mape_seasonal_naive"):
        assert 0 <= result[k] <= 50, f"{k} = {result[k]} must be between 0 and 50 (percent)"


def test_regression_beats_seasonal_naive(result):
    assert result["forecast_mape_regression"] < result["forecast_mape_seasonal_naive"], (
        "the regression forecast should have a lower MAPE than the seasonal naive benchmark"
    )


def test_geolift_lift_range(result):
    lift = result["geolift_lift_pct"]
    assert 2 <= lift <= 10, f"geolift_lift_pct = {lift} must be between 2 and 10 percent"


def test_geolift_ci_brackets_estimate(result):
    lo, lift, hi = result["geolift_ci_low"], result["geolift_lift_pct"], result["geolift_ci_high"]
    assert lo < lift < hi, f"confidence interval [{lo}, {hi}] must bracket the estimate {lift}"


def test_geolift_roas_positive(result):
    assert result["geolift_roas"] > 0, "geolift_roas must be positive"


@pytest.mark.parametrize("key", ["attribution_last_touch", "attribution_logit"])
def test_attribution_shares(result, key):
    shares = result[key]
    assert isinstance(shares, dict), f"{key} must be a dict channel -> share"
    assert sorted(shares) == sorted(ATTRIBUTION_CHANNELS), f"{key} must have exactly the channels {ATTRIBUTION_CHANNELS}"
    assert all(v >= 0 for v in shares.values()), f"{key}: shares must be non-negative"
    total = sum(shares.values())
    assert abs(total - 1) <= 0.01, f"{key}: shares sum to {total:.4f}, expected 1 (tolerance 0.01)"
