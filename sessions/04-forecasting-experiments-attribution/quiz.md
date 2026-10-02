# Quiz 4: Forecasting, experiments and attribution

Closed book, 10 questions, one correct answer each. Opens after Session 4, closes Sunday 1 November 2026, 23:59. Best three of four quizzes count.

---

**1. Why does the course build a baseline sales forecast before discussing the 2027 budget?**

- A. Because the MMM cannot be estimated without a forecast
- B. Because every budget scenario is expressed as a change relative to the baseline, so a biased baseline biases every scenario **(correct)**
- C. Because forecasts replace the need for experiments
- D. Because finance requires a forecast before any regression is allowed

*Rationale: scenarios are incremental to the baseline; the forecast is also the simplest out-of-sample test of the model's structure.*

---

**2. In the regression forecaster, what is the role of the Fourier terms?**

- A. They remove autocorrelation from the residuals
- B. They capture smooth yearly seasonality with a handful of parameters instead of 51 week-of-year dummies **(correct)**
- C. They model the effect of holidays such as Christmas
- D. They convert the series to a stationary one before estimation

*Rationale: two pairs of sine and cosine terms describe a seasonal wave with four parameters; holidays are separate dummies.*

---

**3. What is the purpose of rolling-origin evaluation?**

- A. To estimate the model on the most recent data only
- B. To test forecast accuracy on several out-of-sample windows that mimic how the forecast will be used **(correct)**
- C. To choose the number of Fourier terms by maximising R-squared
- D. To remove leakage from the training data

*Rationale: fitting up to an origin, forecasting the horizon ahead, and rolling the origin forward gives several honest accuracy measurements.*

---

**4. A regression forecaster uses planned media spend, price and promotion share as inputs. When is this legitimate?**

- A. Never; future inputs are always leakage
- B. Only if the inputs are decided by the company in advance and will be executed as planned **(correct)**
- C. Only for a one-week horizon
- D. Only if the inputs are lagged by at least 52 weeks

*Rationale: a plan known at forecast time is a legitimate input; realised spend that reacted to realised sales would be leakage.*

---

**5. Why does an observational MMM tend to overstate media effects?**

- A. Because adstock double-counts spend
- B. Because budgets are planned to rise when demand is expected to be high, so spend and sales share an unobserved driver **(correct)**
- C. Because OLS cannot handle more than five channels
- D. Because sales are measured in units and spend in euros

*Rationale: the planning confound; seasonality and promotion controls absorb part of it, never all of it.*

---

**6. In the difference-in-differences regression log(sales) ~ treated:test_period + C(region) + C(week), what do the week fixed effects do?**

- A. They estimate the lift week by week
- B. They absorb everything that affected all regions in a given week, such as the national Christmas build-up **(correct)**
- C. They make standard errors robust to clustering
- D. They remove the need for a pre-period

*Rationale: week effects are the regression version of the control group's change; without them the seasonal rise would be attributed to the treatment.*

---

**7. Why are standard errors in the geo-lift regression clustered by region?**

- A. Because regions differ in size
- B. Because the weekly observations of one region are correlated, so there are far fewer independent units than rows **(correct)**
- C. Because the dependent variable is in logs
- D. Because the treatment was assigned at the week level

*Rationale: 2 560 rows but only 40 independent regions; naive OLS standard errors would be several times too small.*

---

**8. The German geo test gives an incremental ROAS of about 1.5 for the extra paid social spend, while the MMM reports an average ROAS of about 1.7. What is the correct reading?**

- A. The experiment proves the MMM overstates paid social and the channel's budget should be cut
- B. The experiment measures the marginal return on a large spend increase; a value a little below the average ROAS is what diminishing returns predict, and the right comparison is with the MMM's marginal ROAS at that spend level **(correct)**
- C. The MMM is right and the experiment is wrong because it uses three years of data instead of eight weeks
- D. The two numbers cannot be compared because one is in logs

*Rationale: under saturation marginal ROAS is below average ROAS; compare like with like after checking that both use the same spend and revenue definitions.*

---

**9. What does last-touch attribution measure?**

- A. The causal effect of each channel on conversion probability
- B. Which channel was present at the last step of converting journeys **(correct)**
- C. The average marginal contribution of each channel over all orders of touches
- D. The incremental sales of each channel after removing offline media

*Rationale: rule-based attribution counts presence; it rewards intent channels such as paid search regardless of influence.*

---

**10. Why does paid social receive a much larger attributed share in Italy and Poland than in Austria in the logistic regression with country × channel interactions?**

- A. Because Italy and Poland have more journeys in the data
- B. Because the model allows the effect of a paid social touch on conversion odds to differ by market, and it is larger where mobile and social shopping are more common **(correct)**
- C. Because the pooled model omitted the mobile variable
- D. Because last-touch attribution was used for those countries

*Rationale: interactions let channel effectiveness vary by market; the pooled model forces one share on all countries.*
