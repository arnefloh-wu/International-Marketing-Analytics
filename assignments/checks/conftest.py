"""
Shared fixtures for the lab check-in auto-checks.

Submissions live in assignments/checks/submissions/<github_username>/.
If that folder has no sub-folders, the tests run against
assignments/checks/example_submission/ so that `pytest assignments/checks`
always has something to check.

Run only your own submission with:  pytest assignments/checks -k <github_username>
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd
import pytest

CHECKS_DIR = Path(__file__).resolve().parent
ROOT = CHECKS_DIR.parents[1]
DATA = ROOT / "data"
SUBMISSIONS = CHECKS_DIR / "submissions"
EXAMPLE = CHECKS_DIR / "example_submission"

COUNTRIES = ["AT", "DE", "FR", "IT", "NL", "PL"]
MMM_CHANNELS = ["tv", "online_video", "paid_search", "paid_social", "ooh"]
ATTRIBUTION_CHANNELS = ["display", "paid_search", "paid_social", "email", "affiliate", "organic"]


# Folder names the labs write when GITHUB_USERNAME is left at its default; never real submissions.
PLACEHOLDER = re.compile(r"^your[-_]?github[-_]?username$", re.I)


def discover_submissions() -> list[Path]:
    if SUBMISSIONS.exists():
        folders = sorted(
            p for p in SUBMISSIONS.iterdir()
            if p.is_dir() and not p.name.startswith(".") and not PLACEHOLDER.match(p.name)
        )
        if folders:
            return folders
    return [EXAMPLE]


def require_file(submission: Path, name: str) -> Path:
    """Path to a submitted file; skips the test if the check-in has not been submitted yet."""
    path = submission / name
    if not path.exists():
        pytest.skip(f"{name} not submitted in {submission.name}/ (counts as not passed when graded)")
    return path


def pytest_generate_tests(metafunc):
    if "submission" in metafunc.fixturenames:
        folders = discover_submissions()
        metafunc.parametrize("submission", folders, ids=[p.name for p in folders])


@pytest.fixture(scope="session")
def panel() -> pd.DataFrame:
    df = pd.read_csv(DATA / "mmm" / "alpenglow_weekly.csv", parse_dates=["week"])
    return df.sort_values(["country", "week"]).reset_index(drop=True)


@pytest.fixture(scope="session")
def weekly_budget_2027(panel) -> float:
    """2027 weekly budget = average weekly total media spend across all six countries in 2025."""
    spend_cols = [f"spend_{ch}_k" for ch in MMM_CHANNELS]
    y2025 = panel[panel.week.dt.year == 2025]
    return float(y2025[spend_cols].sum().sum() / y2025.week.nunique())
