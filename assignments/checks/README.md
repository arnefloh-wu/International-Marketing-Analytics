# Auto-checks for the lab check-ins and the group project

This folder holds the `pytest` checks behind the two individual **lab check-ins** (20 % of the grade, after Sessions 2 and 4) and the automated part of the **group project** check. The same tests run on your laptop and on the instructor's machine, so you know your score before you submit.

## What you submit

Create a folder with your GitHub username under `assignments/checks/submissions/` and put the files below in it. Submit by pull request to the course repository (one PR per check-in) before the start of the next session.

```
assignments/checks/submissions/<github_username>/
├── check_session2.csv    check-in 1, after Session 2
├── check_session2.json   check-in 1, after Session 2
└── check_session4.json   check-in 2, after Session 4
```

Your Quarto notebook (one per check-in, kept in your group repository or attached to the PR) must contain the code that writes these files. The files alone score nothing if the code does not produce them.

### Check-in 1 (Session 2): a one-country marketing mix model

Pick one country **other than Germany** (AT, FR, IT, NL or PL). Train on 2023 to 2024, hold out 2025.

`check_session2.csv`, exactly five rows (one per channel `tv, online_video, paid_search, paid_social, ooh`):

| Column | Meaning |
|---|---|
| `country` | ISO-2 code, the same in all rows |
| `channel` | channel name |
| `adstock_alpha` | geometric decay you selected, 0 <= alpha < 1 |
| `coefficient` | model coefficient on the (adstocked, possibly saturated) spend variable |
| `total_spend_k` | total 2023 to 2025 spend in this channel, thousand EUR (from the data) |
| `incremental_units_k` | total 2023 to 2025 incremental units attributed to the channel, thousands |
| `roas` | incremental revenue / spend, using the country's mean 2023 to 2025 price |

`check_session2.json`:

```json
{"country": "AT", "r2_train": 0.97, "r2_holdout": 0.94, "mape_holdout": 3.6,
 "price_elasticity": -0.73, "n_weeks_train": 105}
```

Tests: files exist and parse; schema; `0 <= adstock_alpha < 1`; `0.1 <= roas <= 8`; `incremental_units_k > 0` for at least four channels; `roas` consistent with `incremental_units_k x mean price / total_spend_k` within 25 %; `total_spend_k` matches the data within 1 % per channel; R-squared values in (0.5, 1); `mape_holdout < 25`; `-4 <= price_elasticity <= -0.3`; `100 <= n_weeks_train <= 110`.

### Check-in 2 (Session 4): forecast, geo-lift, attribution

`check_session4.json` with the keys below (one country of your choice for the forecast and one for the attribution):

| Key | Meaning |
|---|---|
| `forecast_country` | country forecast |
| `forecast_mape_regression` | MAPE (%) of your regression forecast on the 2025 holdout |
| `forecast_mape_seasonal_naive` | MAPE (%) of the seasonal naive benchmark (same week last year) |
| `geolift_lift_pct` | estimated paid-social lift in the German test, percent |
| `geolift_ci_low`, `geolift_ci_high` | 95 % confidence interval of the lift, percent |
| `geolift_roas` | incremental revenue / incremental paid-social spend in the test |
| `attribution_country` | country used for attribution |
| `attribution_last_touch` | dict channel -> share of conversions (last touch) |
| `attribution_logit` | dict channel -> share of credit from the logistic-regression model |

Attribution channels: `display, paid_search, paid_social, email, affiliate, organic`.

Tests: keys present; MAPEs between 0 and 50 and the regression MAPE below the seasonal naive MAPE; lift between 2 and 10 with `ci_low < lift < ci_high`; positive ROAS; both attribution dicts have exactly the six channels, non-negative shares that sum to 1 within 0.01.

### Group project: `allocation_2027.csv`

`test_project.py` checks the allocation file of a group repository (path in the environment variable `PROJECT_CSV`; default: the template file): 30 rows, all 6 countries x 5 channels, non-negative, sum equal to the 2027 weekly budget (2025 average weekly total media spend across all countries, tolerance 0.5 %).

## Running the checks yourself

From the repository root with the course environment active:

```bash
pytest assignments/checks -k <github_username>          # your check-ins only
pytest assignments/checks/test_session2.py -k <github_username>
PROJECT_CSV=../group-XX-alpenglow/allocation_2027.csv pytest assignments/checks/test_project.py
pytest assignments/checks                               # everything (all submissions, or the example)
```

Read the failure messages: they say which value is out of range and what the test expected. Tests for a check-in you have not submitted yet are *skipped*; when graded, a skipped test counts as not passed.

Folders named `your-github-username` (the default `GITHUB_USERNAME` in the labs) are ignored: rename the folder to your real username before you submit.

## Example submission

`example_submission/` contains valid files produced by `make_example_submission.py` (OLS MMM for Austria with adstock grid search, regression versus seasonal naive forecast for Germany, difference-in-differences on the geo-lift test, last-touch versus logistic attribution for Germany). When `submissions/` is empty, the tests run against this example. Regenerate it with

```bash
python assignments/checks/make_example_submission.py
```

## How the instructor grades

```bash
python assignments/checks/grade_checks.py --out instructor/grades/checks.csv
```

runs `test_session2.py` and `test_session4.py` once per submission folder and writes a CSV with `username, session2_passed, session2_total, session2_pct, session4_passed, session4_total, session4_pct, failed_tests`. The check-in score is the share of tests passed (each check-in is 10 % of the course grade), with a manual review of the notebook for the top and bottom cases and for any submission whose files are not produced by its code.
