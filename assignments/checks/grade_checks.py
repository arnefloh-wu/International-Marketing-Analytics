"""
Instructor grading script for the lab check-ins.

Runs the pytest auto-checks once per submission folder in
assignments/checks/submissions/<github_username>/ and writes a CSV with the
number of passed and total tests per check-in:

    python assignments/checks/grade_checks.py --out instructor/grades/checks.csv

Columns: username, session2_passed, session2_total, session4_passed,
session4_total, session2_pct, session4_pct, failed_tests.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conftest import discover_submissions  # noqa: E402

CHECKS_DIR = Path(__file__).resolve().parent
SUBMISSIONS = CHECKS_DIR / "submissions"
TEST_FILES = {"session2": "test_session2.py", "session4": "test_session4.py"}


def run_pytest(username: str, test_file: str) -> tuple[int, int, list[str]]:
    with tempfile.TemporaryDirectory() as tmp:
        xml_path = Path(tmp) / "report.xml"
        subprocess.run(
            [sys.executable, "-m", "pytest", str(CHECKS_DIR / test_file), "-k", username, "-q",
             "-p", "no:cacheprovider", f"--junitxml={xml_path}"],
            capture_output=True, text=True, cwd=CHECKS_DIR.parents[1],
        )
        if not xml_path.exists():
            return 0, 0, ["pytest did not produce a report"]
        root = ET.parse(xml_path).getroot()
        cases = root.iter("testcase")
        total, passed, failed = 0, 0, []
        for case in cases:
            total += 1
            if any(child.tag in ("failure", "error", "skipped") for child in case):
                failed.append(case.get("name").split("[")[0])  # skipped = file not submitted
            else:
                passed += 1
        return passed, total, failed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default=str(CHECKS_DIR / "grades_checks.csv"), help="output CSV path")
    args = parser.parse_args()

    folders = discover_submissions() if SUBMISSIONS.exists() else []
    folders = [f for f in folders if f.parent == SUBMISSIONS]
    if not folders:
        print(f"No submissions found in {SUBMISSIONS}. Grading the example submission instead.")
        folders = [CHECKS_DIR / "example_submission"]

    rows = []
    for folder in folders:
        row = {"username": folder.name}
        failed_all = []
        for session, test_file in TEST_FILES.items():
            passed, total, failed = run_pytest(folder.name, test_file)
            row[f"{session}_passed"] = passed
            row[f"{session}_total"] = total
            row[f"{session}_pct"] = round(100 * passed / total, 1) if total else 0.0
            failed_all += [f"{session}:{name}" for name in failed]
        row["failed_tests"] = "; ".join(failed_all)
        rows.append(row)
        print(f"{folder.name:30s} session2 {row['session2_passed']}/{row['session2_total']}   "
              f"session4 {row['session4_passed']}/{row['session4_total']}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out, index=False)
    print(f"Written {out}")


if __name__ == "__main__":
    main()
