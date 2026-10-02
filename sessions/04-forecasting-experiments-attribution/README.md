# Session 4: Forecasting, experiments and attribution

**Tuesday 27 October 2026 · Decision of the day: "Can we trust the model?"**

The Session 3 budget allocation rests on one observational marketing mix model. This session tests that model from three sides before it goes to the board. Part A turns the MMM towards the future: a regression forecaster with trend, Fourier seasonality, holidays, lagged sales and planned media is evaluated with rolling origins against seasonal naive and ETS benchmarks, and produces the 2026 Q1 baseline per country that every budget scenario will be measured against. Part B analyses Alpenglow's German geo-lift test of paid social with difference-in-differences (region and week fixed effects, cluster-robust standard errors), an event-study plot and a synthetic control, converts the lift to an experimental ROAS and shows how the test calibrates the MMM. Part C compares attribution methods on 60 000 multi-market customer journeys (last touch, first touch, logistic regression removal effects, Shapley values) and explains why attribution differs across markets and why it disagrees with the MMM. Lab check-in 2 is set at the end of the lab.

## Learning outcomes

After this session you can:

1. Build and evaluate a short-term sales forecast as a regression with known future inputs, score it with MAPE and RMSE against naive benchmarks using rolling-origin evaluation, and report prediction intervals honestly.
2. Explain the planning confound in observational MMM and why a randomised geo experiment breaks it.
3. Design a geo-lift test (treatment and control regions, pre-period, power) and analyse it with difference-in-differences with fixed effects and clustered standard errors, including carryover and a synthetic-control check.
4. Convert an experimental lift into incremental units, incremental spend and ROAS, compare it correctly with the MMM (marginal vs average), and describe how a lift test calibrates an MMM.
5. Compute rule-based, logistic-regression and Shapley attribution, explain why they disagree with each other and with the MMM, and why the answer differs by market.
6. Triangulate experiment, MMM and attribution into one measurement story for a budget decision.

## Files

| File | Purpose |
|---|---|
| `slides.qmd` | Concept lecture (renders to reveal.js and PowerPoint): `quarto render slides.qmd --to revealjs,pptx` |
| `lab.qmd` | Guided lab, Parts A to C, runs end to end in about 30 seconds: `quarto render lab.qmd` |
| `exercises.qmd` | Five team exercises (26-week horizon, placebo DiD, lift in levels, new vs returning attribution, memo on a Polish geo test) |
| `quiz.md` | Quiz 4, ten closed-book multiple-choice questions |

Data used: `data/mmm/alpenglow_weekly.csv`, `data/experiments/geolift_germany.csv`, `data/attribution/journeys.csv`. Helper functions from `assets/mma.py`.

## Timing plan (4 hours)

| Time | Block | Content |
|---|---|---|
| 0:00 to 0:10 | Opening | Where we are, decision of the day, how the three parts test the model |
| 0:10 to 0:30 | Lecture A | Forecasting as regression, rolling-origin evaluation, benchmarks, intervals, pitfalls |
| 0:30 to 0:50 | Lecture B | Planning confound, geo-test design and power, DiD, synthetic control, carryover, lift to ROAS, calibration, ethics |
| 0:50 to 1:05 | Lecture C | Rule-based vs logit vs Shapley attribution, market differences, triangulation |
| 1:05 to 1:35 | Lab Part A | Forecast six countries, MAPE table, DE and PL intervals, 2026 Q1 baseline |
| 1:35 to 2:05 | Lab Part B | Geo-lift: balance, DiD, event study, synthetic Frankfurt, experimental ROAS vs own Session 2 ROAS |
| 2:05 to 2:20 | Break | |
| 2:20 to 2:45 | Lab Part C and check-in | Attribution tables, country interactions, Shapley; write `check_session4.json` |
| 2:45 to 3:40 | Team exercise | Exercise 5 (memo on a geo test in Poland) plus one of Exercises 1 to 4 per group, on the project data |
| 3:40 to 4:00 | Debrief | Groups present memos, quiz 4 opens, check-in 2 and project deadlines |

## Lab check-in 2

Individual, auto-checked with `pytest assignments/checks`, due before Session 5. Save a JSON file at

```
assignments/checks/submissions/<your_github_username>/check_session4.json
```

with exactly these keys (the last chunk of `lab.qmd` writes it for you; change only the username and your two country choices):

| Key | Type | Content |
|---|---|---|
| `forecast_country` | string | ISO-2 code of the country you report forecasting accuracy for |
| `forecast_mape_regression` | number | mean MAPE (%) of the regression forecaster over the four 2025 origins, 13-week horizon |
| `forecast_mape_seasonal_naive` | number | the same for seasonal naive |
| `geolift_lift_pct` | number | DiD lift in % from `log(sales) ~ treated:test_period + treated:post_period + C(region) + C(week)`, clustered by region |
| `geolift_ci_low`, `geolift_ci_high` | numbers | 95 % confidence interval of the lift in % |
| `geolift_roas` | number | experimental ROAS of paid social in Germany (incremental units × average DE price 2025 / incremental spend) |
| `attribution_country` | string | ISO-2 code of the country you report attribution for |
| `attribution_last_touch` | object | channel → share of that country's conversions under last touch (six channels, sums to 1) |
| `attribution_logit` | object | channel → removal-effect share from the logit with country × channel interactions, for that country (sums to 1) |

Commit the file to your fork and open a pull request to the course repository before the start of Session 5. Run `pytest assignments/checks -k <your_github_username>` from the repository root to check it yourself; the tests (keys present, MAPEs in range with regression below seasonal naive, lift between 2 and 10 % with a bracketing CI, positive ROAS, attribution shares over exactly six channels summing to one) are documented in `assignments/checks/README.md`.

## Before the session

- Run `lab.qmd` of Session 2 once more and note your MMM ROAS of paid social in Germany; the lab asks you to compare it with the experiment.
- Reading: Gordon, Zettelmeyer, Bhargava and Chapsky (2019), *Marketing Science*; Li and Kannan (2014), *Journal of Marketing Research*; Meta GeoLift methodology (overview page); PyMC-Marketing documentation on lift-test calibration.
