# Session 1: Toolkit and regression foundations

**Decision of the day: "Is our price too high in Poland?"**

Session 1 sets up the working environment (Positron, Quarto, GitHub, AI assistants with the course rules on their use) and rebuilds regression as the language of the course on the Alpenglow weekly panel. Starting from the Polish country manager's request for a 10 % price cut, students estimate log-log price and promotion elasticities for six countries, watch omitted variables (promotion, trend) flip the sign of the price coefficient, add holiday dummies and Fourier seasonality, compare six separate regressions with one pooled model with country × log price interactions, diagnose collinearity with VIFs, check a 2025 holdout, and relate the elasticities to GDP per capita and Hofstede scores from `country_meta.csv`. The session ends with a five-sentence answer for the management meeting and the first commit in each group repository.

## Learning outcomes

After this session, students can:

1. Describe the analytics workflow (question, data, model, check, decide) and the role of Positron, Quarto, GitHub and an AI assistant in it, including what assistants get wrong and the course rules on their use.
2. Read a statsmodels OLS summary: coefficient, standard error, t, p, confidence interval, R², Durbin-Watson.
3. Interpret log-log coefficients as elasticities, dummy coefficients as percentage uplifts, and share coefficients per 10 percentage points.
4. Explain omitted-variable bias with the promotion and trend example, and specify seasonality with holiday dummies and Fourier terms.
5. Estimate and compare country-specific slopes with dummies and interactions, and test whether two countries differ.
6. Diagnose multicollinearity with VIFs and judge a model by holdout fit rather than R².
7. Translate an elasticity with its interval into a price decision with a profit calculation and an explicit caveat about causality.

## Files

| File | Purpose |
|---|---|
| `slides.qmd` | Lecture deck, 39 slides; renders to reveal.js and PowerPoint |
| `lab.qmd` | Guided lab: Positron tour, GitHub Desktop, video game warm-up, Alpenglow elasticities |
| `exercises.qmd` | Five exercises (promotion response, distribution, DE vs PL test, chocolate cross-price elasticities, five-sentence answer) |
| `quiz.md` | Ten closed-book multiple-choice questions |

Solutions: `instructor/solutions/session01_solutions.qmd` (not for students).

## Timing plan (4 hours)

| Time | Block | Content |
|---|---|---|
| 0:00 to 0:20 | Setup clinic | Interpreter selection, Quarto preview, assistant sign-in; students who are ready start the Positron tour in `lab.qmd` |
| 0:20 to 1:20 | Lecture | Slides: course intro, why MMM is back, workflow, toolkit and AI rules, regression refresher on Alpenglow, cross-country discussion |
| 1:20 to 1:30 | Break | |
| 1:30 to 3:00 | Guided lab | `lab.qmd` Sections 2 to 4: first commit with GitHub Desktop, video game warm-up (20 min), Alpenglow model built step by step, elasticity table, pooled model, VIF, holdout, country metadata |
| 3:00 to 3:15 | Break | |
| 3:15 to 3:50 | Team exercise | Exercise 5 (five-sentence Poland answer) plus Exercise 1 or 2; each member commits to the group repository |
| 3:50 to 4:00 | Debrief | Three groups read their Poland answer; quiz 1 opens |

## Key numbers (full model: log price, promotion share, holidays, two Fourier pairs, trend)

| Country | Price elasticity (95 % CI) | Promotion coefficient | R² |
|---|---|---|---|
| AT | -0.93 (-1.56 to -0.30) | 0.41 | 0.91 |
| DE | -1.40 (-2.04 to -0.76) | 0.45 | 0.95 |
| FR | -1.09 (-1.69 to -0.50) | 0.37 | 0.94 |
| IT | -1.39 (-2.09 to -0.69) | 0.58 | 0.92 |
| NL | -0.96 (-1.57 to -0.36) | 0.40 | 0.95 |
| PL | -1.18 (-1.76 to -0.59) | 0.64 | 0.96 |

Pooled model: DE versus PL difference -0.24 (SE 0.47, p = 0.61); joint test of all country interactions p = 0.73. Holdout 2025 MAPE for the full model 4.3 to 5.6 %, versus 12 to 15 % for an over-flexible model with 52 week dummies.
