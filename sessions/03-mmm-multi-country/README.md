# Session 3 · Marketing mix modelling II: many countries, one budget

**Decision of the day: "Where should the next euro go?"**

Session 2 measured what TV did for Alpenglow in Germany. Session 3 turns measurement into allocation: six countries, five channels, one weekly budget of about EUR 710k. The session compares three ways of estimating media effects across markets (separate models, pooled fixed effects, hierarchical or partial pooling), introduces Bayesian MMM with PyMC-Marketing for Austria, a small market where priors matter, and ends with a constrained optimisation that re-allocates the 2025 budget across all 30 country-channel cells, with an uncertainty band on the gain. International moderators (currency and price levels, market maturity, retail concentration, culture) frame how the allocation should be read. The lab is the core of the group project: teams leave with a first model table and a first draft of their 2027 allocation.

## Learning outcomes

After this session you can:

1. Explain why small markets give noisy estimates and big markets dominate pooled models, and choose between separate, pooled and partially pooled estimation.
2. Estimate panel regressions with country fixed effects and country x channel interactions in statsmodels or linearmodels, and apply an empirical-Bayes shrinkage formula.
3. Describe a Bayesian MMM in terms of priors, likelihood and posterior, and read `az.summary` diagnostics (mean, HDI, ESS, r-hat).
4. Run the PyMC-Marketing workflow (adstock, saturation, controls, seasonality, fit, check, contributions, ROAS with uncertainty, budget optimisation) and explain why budget bounds are needed.
5. Formulate and solve a cross-country allocation with `scipy.optimize` (total fixed, cell bounds, country floors) and interpret marginal ROAS.
6. Quantify the uncertainty of an allocation's gain and communicate it to a board.
7. Use country metadata (GDP, years in market, retail concentration, Hofstede scores) to moderate and explain channel effectiveness across markets.

## Files

| File | Purpose |
|---|---|
| `slides.qmd` | Concept lecture (reveal.js and PowerPoint), about 36 slides with speaker notes |
| `lab.qmd` | Guided lab in three parts: A panel OLS, B Bayesian MMM for Austria, C cross-country allocation. Runs in about 2 minutes |
| `exercises.qmd` | Five team exercises, including the one-page allocation memo |
| `quiz.md` | Ten closed-book multiple-choice questions |

Data: `data/mmm/alpenglow_weekly.csv`, `data/mmm/country_meta.csv`. Helpers: `assets/mma.py`.

## Timing plan (4 hours)

| Time | Block | Content |
|---|---|---|
| 0:00 - 0:10 | Opening | Decision of the day, recap of Session 2 (adstock, saturation, ROAS vs marginal ROAS) |
| 0:10 - 0:60 | Lecture | Multi-market problem; separate vs pooled vs hierarchical; Bayesian MMM intuition; PyMC-Marketing workflow; allocation and constraints; uncertainty; international moderators; pitfalls |
| 1:00 - 1:30 | Lab Part A | Adstock within country, scaled spend, three OLS strategies, shrinkage chart |
| 1:30 - 2:10 | Lab Part B | PyMC-Marketing for Austria: fit (start it first, 90 s), diagnostics, ROAS with uncertainty, response curves, bounded vs unbounded optimiser |
| 2:10 - 2:25 | Break | |
| 2:25 - 2:50 | Lab Part C | 30-cell response curves, SLSQP allocation, heatmap, 200-draw uncertainty band |
| 2:50 - 3:40 | Team exercise | First draft of the 2027 allocation: Exercises 2 and 3 (constraints and bounds), start the memo (Exercise 5) |
| 3:40 - 3:55 | Debrief | Compare allocations across teams; what moves budget where and why; project milestone |
| 3:55 - 4:00 | Close | Quiz 3 opens; preview of Session 4 (can we trust the model?) |

## Deliverables

- Quiz 3 (opens Wednesday 9 am, closes Monday 11:59 pm, 5 % of the grade).
- Project milestone: the team's first model table (`country, channel, model, adstock_alpha, coefficient, se, roas, mroas`) committed to the group repository before Session 4.
