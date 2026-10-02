# Session 2: Marketing mix modelling I, one country

**Decision of the day:** *"What did TV do for us in Germany, and would the next euro be better spent elsewhere?"*

This session introduces marketing mix modelling (MMM) as a regression of weekly sales on media spend and controls, with two transformations that turn an OLS into an MMM: geometric adstock for carryover and a Hill or log saturation curve for diminishing returns. Using the German rows of the Alpenglow panel, students build the model step by step in `statsmodels` (controls only, raw spend, adstock grid search, saturation, decomposition, diagnostics, sensitivity), decompose sales into baseline and channel contributions, compute average and marginal ROAS, and learn why the saturation and carryover assumptions must be reported with the estimate. The team exercise replicates the model for France and compares the TV ROAS across the two markets. The lab check-in 1 (individual, graded) is specified at the bottom of this page.

## Learning outcomes

After this session you can:

1. Write down the MMM equation (baseline + media contributions + controls + error) and explain baseline vs incremental sales.
2. Explain geometric adstock and saturation (Hill, logistic, log1p), including the half-saturation point, mean lag and the difference between average and marginal ROAS.
3. Explain the planning confound between media budgets and seasonality and which controls protect against it.
4. Build an MMM for one country in Python with OLS, choose adstock and saturation parameters by grid search, and decompose sales into baseline and channel contributions.
5. Read an MMM output: stacked contribution chart, waterfall, ROAS table, response curves.
6. Diagnose an MMM with residual plots, Durbin-Watson, VIF and holdout MAPE, and run a sensitivity analysis on the carryover assumption.
7. Communicate an MMM result as a point estimate, a range and a recommendation.

## Files

| File | Purpose |
|---|---|
| `slides.qmd` | Lecture deck (reveal.js and PowerPoint), 40 slides with speaker notes |
| `lab.qmd` | Guided lab: the German MMM in seven steps, with check lists and prompt patterns; ends with the check-in code |
| `exercises.qmd` | Five team exercises (memory window, competitor spend, log1p vs Hill, dropping seasonality, memo) |
| `quiz.md` | Quiz 2, ten closed-book multiple-choice questions |
| `../../assets/mma.py` | Helper functions used in the lab (`geometric_adstock`, `hill`, `add_fourier`, `mape`, `contribution_table`) |

Render: `quarto render sessions/02-mmm-one-country/slides.qmd --to revealjs,pptx` and `quarto render sessions/02-mmm-one-country/lab.qmd`.

## Timing plan (4 hours)

| Time | Block | Content |
|---|---|---|
| 0:00 - 0:10 | Opening | Decision of the day; recap of Session 1 (price elasticity becomes a control) |
| 0:10 - 1:05 | Lecture | What MMM is and who uses it; the equation; baseline vs incremental; adstock; saturation; the planning confound and controls; flighting; model building sequence; reading an output; diagnostics; typical mistakes (slides 1 to 36) |
| 1:05 - 1:15 | Lab bridge | Walk through the lab structure and the prompt-pattern boxes; start Positron |
| 1:15 - 2:45 | Guided lab | Steps (a) to (g) in pairs, instructor circulates; checkpoint discussions after (b) (unstable coefficients), (d) (saturation lesson) and (e) (ROAS vs marginal ROAS) |
| 2:45 - 3:00 | Break | |
| 3:00 - 3:45 | Team exercise | "Your turn": replicate for France, compare TV ROAS and alpha; prepare three sentences for the European media director; start Exercise 5 (memo) |
| 3:45 - 4:00 | Debrief | Teams report TV ROAS for Germany and France; discuss the identification problems; quiz 2 opens; lab check-in 1 explained |

## Lab check-in 1 (graded, individual, 10 % of the final grade)

Run the lab for **one country other than Germany** (AT, FR, IT, NL or PL) and submit two files to `assignments/checks/submissions/<your_github_username>/` by pull request before Session 3. The last section of `lab.qmd` contains the code that writes both files (for DE as the worked example; change `COUNTRY_CODE` and `GITHUB_USERNAME`).

**`check_session2.csv`**: one row per channel (5 rows), columns `country, channel, adstock_alpha, coefficient, total_spend_k, incremental_units_k, roas`.

- `country`: ISO-2 code, not DE
- `channel`: `tv`, `online_video`, `paid_search`, `paid_social`, `ooh`
- `adstock_alpha`: the selected alpha, in [0, 0.9]
- `coefficient`: media coefficient of the final model estimated on all 156 weeks
- `total_spend_k`: 2023-2025 spend in thousand EUR
- `incremental_units_k`: 2023-2025 incremental units (thousand) from the decomposition
- `roas`: incremental revenue (weekly units x weekly price) divided by spend

**`check_session2.json`**: keys `country`, `r2_train`, `r2_holdout`, `mape_holdout` (model estimated on 2023-2024, evaluated on 2025), `price_elasticity` (log-price coefficient of the training model divided by mean training sales) and `n_weeks_train` (105).

The auto-check (`pytest assignments/checks`) verifies file names and columns, that the country is not DE, five channels, alphas within [0, 0.9], `n_weeks_train == 105`, and that `roas` is consistent with `incremental_units_k`, `total_spend_k` and the country's average price within a tolerance. Numbers are not graded against a single "right" answer; a defensible model with correct structure receives full marks. Groups should spread across countries so that every market has been modelled before Session 3.
