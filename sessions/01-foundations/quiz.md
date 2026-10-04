# Quiz 1: Toolkit and regression foundations

Closed book, 10 questions in 10 minutes, one correct answer each. Opens Wednesday 7 October 2026, 9 am, closes Monday 12 October 2026, 11:59 pm. Each quiz counts 5 % of the grade. Tests understanding, not code.

**1. In a regression of log(units) on log(price), the price coefficient is -1.4. What does this mean?**

- a) A 1 EUR price increase lowers units by 1.4 thousand
- b) A 1 % price increase lowers units by about 1.4 % **(correct)**
- c) Price explains 1.4 % of the variance of units
- d) The price is 1.4 times too high

*Rationale: in a log-log model the slope is the ratio of percentage changes, that is, an elasticity.*

**2. A coefficient has an estimate of -1.2 and a standard error of 0.3. Which statement is right?**

- a) The 95 % confidence interval is about -1.8 to -0.6 **(correct)**
- b) The effect is not statistically significant
- c) The p-value is 0.3
- d) The coefficient explains 30 % of the variance

*Rationale: the 95 % interval is roughly the estimate plus or minus two standard errors; here |t| = 4, which is significant.*

**3. Adding promotion share to the German model turned the price coefficient from -2.0 to +1.2. What is the most likely explanation?**

- a) Germans like higher prices
- b) Promotion share is irrelevant and should be dropped
- c) Promotion and price are correlated, and a third factor (trend) is still omitted **(correct)**
- d) The sample is too small for two variables

*Rationale: price moves with promotion and with inflation; without a trend, the remaining price variation is confounded with brand growth.*

**4. What does R² = 0.95 tell you about a model?**

- a) The coefficients are unbiased
- b) The model explains 95 % of the variance of the outcome in the estimation sample **(correct)**
- c) The model will predict next year with 95 % accuracy
- d) The price elasticity is significant at the 5 % level

*Rationale: R² describes in-sample fit only; it says nothing about bias or out-of-sample accuracy.*

**5. A model has a variance inflation factor of 10 for log price. What is the consequence?**

- a) The price coefficient is biased towards zero
- b) The price coefficient has a wider standard error than it would with independent regressors **(correct)**
- c) The model will not converge
- d) Price must be removed from the model

*Rationale: collinearity inflates variances of estimates but does not bias them; removing a relevant variable would introduce bias.*

**6. Why does the course use Fourier terms (sine and cosine of the week) instead of 52 week-of-year dummies for seasonality?**

- a) Fourier terms capture a smooth annual cycle with a few coefficients, so they overfit less **(correct)**
- b) Dummies cannot be used in log models
- c) Fourier terms are required by statsmodels
- d) Week dummies are only valid for Christmas

*Rationale: each week dummy is estimated from very few observations; a few smooth terms generalise better, which the holdout test confirmed.*

**7. In a pooled model `log_sales ~ C(country) * log_price`, the coefficient on `C(country)[T.PL]:log_price` is -0.37 and the coefficient on `log_price` is -0.95. What is Poland's elasticity?**

- a) -0.37
- b) -0.95
- c) -1.32 **(correct)**
- d) +0.58

*Rationale: the interaction is the difference from the reference country (Austria, first alphabetically), so Poland's slope is -0.95 - 0.37.*

**8. A model has an in-sample MAPE of 2 % and a 2025 holdout MAPE of 15 %. Another has 4 % and 5 %. Which should you use for planning?**

- a) The first, because it fits better
- b) The second, because it generalises to data it has not seen **(correct)**
- c) Neither, because holdout errors must be zero
- d) The first, if its R² is higher

*Rationale: the gap between in-sample and holdout error is the signature of overfitting; the planning model must predict, not memorise.*

**9. Which of these is a legitimate reason to treat an estimated price elasticity as an association rather than a causal effect?**

- a) The coefficient is negative
- b) Managers set prices in response to expected demand, and media spend is not in the model **(correct)**
- c) The confidence interval is narrow
- d) The regression used logs

*Rationale: reverse causality and omitted variables both break the causal reading; experiments (Session 4) are the remedy.*

**10. According to the course rules on AI assistants, which statement is true?**

- a) Code written by an assistant does not need to be checked
- b) You may use an assistant in the quizzes
- c) You are responsible for every reported number and must document the prompts behind non-trivial code **(correct)**
- d) Only GitHub Copilot is allowed

*Rationale: the syllabus makes the student responsible for all results, requires a prompt log, and keeps quizzes closed-book.*
