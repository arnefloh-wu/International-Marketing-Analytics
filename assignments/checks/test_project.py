"""
Group project auto-check: allocation_2027.csv.

Path taken from the environment variable PROJECT_CSV, default
assignments/group-project/template/allocation_2027.csv. Example:

    PROJECT_CSV=../group-07/allocation_2027.csv pytest assignments/checks/test_project.py

Columns: country, channel, weekly_spend_k. Thirty rows (6 countries x 5
channels), non-negative, summing to the 2027 weekly budget = 2025 average
weekly total media spend across all countries (tolerance 0.5%).
"""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
import pytest

from conftest import COUNTRIES, MMM_CHANNELS, ROOT

DEFAULT = ROOT / "assignments" / "group-project" / "template" / "allocation_2027.csv"


@pytest.fixture(scope="module")
def allocation() -> pd.DataFrame:
    path = Path(os.environ.get("PROJECT_CSV", DEFAULT))
    assert path.exists(), f"missing {path}"
    df = pd.read_csv(path)
    for c in ("country", "channel", "weekly_spend_k"):
        assert c in df.columns, f"missing column {c}"
    return df


def test_thirty_rows_all_cells(allocation):
    assert len(allocation) == 30, f"expected 30 rows (6 countries x 5 channels), got {len(allocation)}"
    cells = set(zip(allocation.country, allocation.channel))
    expected = {(c, ch) for c in COUNTRIES for ch in MMM_CHANNELS}
    assert cells == expected, f"missing cells: {expected - cells}; unexpected: {cells - expected}"
    assert not allocation.duplicated(["country", "channel"]).any(), "duplicate country x channel rows"


def test_non_negative_numeric(allocation):
    assert pd.api.types.is_numeric_dtype(allocation.weekly_spend_k), "weekly_spend_k must be numeric"
    assert allocation.weekly_spend_k.notna().all(), "weekly_spend_k has missing values"
    assert (allocation.weekly_spend_k >= 0).all(), "weekly_spend_k must be non-negative"


def test_sums_to_weekly_budget(allocation, weekly_budget_2027):
    total = allocation.weekly_spend_k.sum()
    assert abs(total - weekly_budget_2027) / weekly_budget_2027 <= 0.005, (
        f"allocation sums to {total:.2f} k EUR per week; the 2027 weekly budget is {weekly_budget_2027:.2f} k EUR (tolerance 0.5%)"
    )
