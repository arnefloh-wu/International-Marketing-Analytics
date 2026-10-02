"""
00_load.py: load the Alpenglow course data from the course repository.

Assumes the course repository is cloned next to your group repository:

    ~/wu/
    ├── International-Marketing-Analytics/   (course repo, read-only)
    └── group-XX-alpenglow/                  (your repo)

If the data are not found, the loader falls back to the raw-file URL of the
course repository on GitHub (fill in COURSE_DATA_URL after the instructor
publishes the repository). Do not copy the CSV files into your repository.

Run from the root of your group repository:  python code/00_load.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

CHANNELS = ["tv", "online_video", "paid_search", "paid_social", "ooh"]
COUNTRIES = ["AT", "DE", "FR", "IT", "NL", "PL"]

# Candidate locations of the course data, tried in order.
CANDIDATES = [
    Path("../International-Marketing-Analytics/data"),      # course repo next to group repo (run from repo root)
    Path("../../International-Marketing-Analytics/data"),   # run from code/ or report folder
    Path("../../../data"),                                  # template rendered inside the course repo itself
]
# Fallback: raw GitHub URL of the course repository (placeholder, instructor supplies the final one)
COURSE_DATA_URL = "https://raw.githubusercontent.com/<ORG>/International-Marketing-Analytics/main/data"

FILES = {
    "panel": "mmm/alpenglow_weekly.csv",
    "meta": "mmm/country_meta.csv",
    "geolift": "experiments/geolift_germany.csv",
    "journeys": "attribution/journeys.csv",
}


def data_root() -> str:
    for cand in CANDIDATES:
        if (cand / FILES["panel"]).exists():
            return str(cand)
    return COURSE_DATA_URL


def load_all() -> dict[str, pd.DataFrame]:
    root = data_root()
    data = {}
    for key, rel in FILES.items():
        path = f"{root}/{rel}"
        parse = ["week"] if key in ("panel", "geolift") else (["start_date"] if key == "journeys" else None)
        data[key] = pd.read_csv(path, parse_dates=parse)
    data["panel"] = data["panel"].sort_values(["country", "week"]).reset_index(drop=True)
    return data


def weekly_budget_2027(panel: pd.DataFrame) -> float:
    """2027 weekly media budget = 2025 average weekly total media spend across all countries (thousand EUR)."""
    spend_cols = [f"spend_{ch}_k" for ch in CHANNELS]
    y2025 = panel[panel.week.dt.year == 2025]
    return float(y2025[spend_cols].sum().sum() / y2025.week.nunique())


def placeholder_allocation(panel: pd.DataFrame) -> pd.DataFrame:
    """Current (2025 average) weekly spend per country x channel: the starting point for your allocation."""
    y2025 = panel[panel.week.dt.year == 2025]
    rows = []
    for c in COUNTRIES:
        sub = y2025[y2025.country == c]
        for ch in CHANNELS:
            rows.append({"country": c, "channel": ch, "weekly_spend_k": round(sub[f"spend_{ch}_k"].mean(), 2)})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    data = load_all()
    print(f"Data root: {data_root()}")
    for k, v in data.items():
        print(f"{k:10s} {v.shape[0]:>7,} rows x {v.shape[1]} columns")
    budget = weekly_budget_2027(data["panel"])
    print(f"2027 weekly budget: {budget:,.2f} thousand EUR  (52 weeks: {52 * budget:,.0f} thousand EUR)")
    alloc = placeholder_allocation(data["panel"])
    print(f"Placeholder allocation sums to {alloc.weekly_spend_k.sum():,.2f} thousand EUR per week")
    out = Path("allocation_2027.csv")
    if not out.exists():
        alloc.to_csv(out, index=False)
        print(f"Written {out} (2025 average spend; replace with your recommendation)")
