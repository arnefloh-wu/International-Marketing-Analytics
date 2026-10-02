# Quiz 3 · Marketing mix modelling II: many countries, one budget

Closed book, 10 questions, one correct answer each. 20 minutes.

**1. Alpenglow estimates a separate MMM for each of its six countries. Which statement about the small markets (Austria, Poland) is most accurate?**

a) Their coefficients are biased towards zero because small budgets cannot move sales.
b) Their coefficients are unbiased but have wide confidence intervals because media spend varies little relative to sales noise. **(correct)**
c) Their coefficients are more precise because small markets have fewer channels.
d) Their coefficients cannot be estimated without at least five years of data.

*Rationale: separate OLS is unbiased under its assumptions; the problem in small markets is low signal-to-noise, hence wide intervals, not bias.*

**2. A pooled regression with country fixed effects (`C(country)`) assumes that:**

a) each country has its own media coefficients and its own intercept.
b) all countries share the same intercept but have different media coefficients.
c) all countries share the same media coefficients; only the intercepts differ. **(correct)**
d) countries with more data receive a higher weight on their media coefficients.

*Rationale: fixed effects shift the level per country; slopes (media effects) are common unless interactions are added.*

**3. In partial pooling (shrinkage), a country's estimate is pulled towards the cross-country mean. The pull is strongest when:**

a) the country's own estimate is very precise and countries are very different.
b) the country's own estimate is noisy and countries appear similar. **(correct)**
c) the country has the largest budget.
d) the pooled estimate has a large standard error.

*Rationale: the weight on own data is tau^2 / (tau^2 + se^2); a large se and a small between-country variance tau^2 give a small weight.*

**4. In a Bayesian MMM, the prior on a channel's adstock decay is best described as:**

a) the value the data would give with an infinite sample.
b) a distribution expressing what is believed about the parameter before seeing this dataset. **(correct)**
c) the estimate from the pooled model.
d) a constraint that the optimiser must satisfy.

*Rationale: the prior encodes business knowledge; it is updated by the likelihood to give the posterior.*

**5. The Austrian model reports P(ROAS of OOH > 1) = 0.35. The most appropriate reading is:**

a) OOH loses money in 65 % of weeks.
b) Given the model and data, there is a 35 % probability that OOH pays back its cost on average. **(correct)**
c) OOH returns EUR 0.35 per euro spent.
d) The estimate is not statistically significant, so OOH has no effect.

*Rationale: the posterior probability is a statement about the parameter, not about individual weeks or significance.*

**6. For a fixed total budget and smooth, concave response curves with no binding constraints, the optimal allocation has:**

a) equal spend in every cell.
b) equal average ROAS in every cell.
c) equal marginal ROAS in every cell. **(correct)**
d) all spend in the cell with the highest average ROAS.

*Rationale: if marginal returns differed, moving a euro from the lower to the higher cell would raise total revenue.*

**7. An unbounded budget optimiser puts the entire Austrian budget into paid social. The most likely reason is:**

a) paid social has the largest adstock.
b) the estimated paid social curve is nearly linear over the observed range, so the model sees no diminishing returns. **(correct)**
c) the optimiser has a bug.
d) paid social is the cheapest channel per impression.

*Rationale: corner solutions arise when a curve does not saturate within the data; the optimiser extrapolates the straight line.*

**8. Management imposes "no country loses more than 30 % of its budget". In the optimisation this is:**

a) a bound on each cell.
b) an equality constraint on the total.
c) an inequality constraint on the sum of a country's cells. **(correct)**
d) a change to the response curves.

*Rationale: country floors restrict sums over cells, implemented as inequality constraints in SLSQP.*

**9. The recommended plan is evaluated under 200 coefficient draws and gains revenue in 95 % of them. Which statement is correct?**

a) The plan will gain revenue in 95 % of future weeks.
b) The plan's expected gain is robust to estimation uncertainty in the coefficients, given the assumed curve shapes. **(correct)**
c) The model has 95 % accuracy.
d) The gain is guaranteed as long as the budget stays fixed.

*Rationale: the draws vary the coefficients, not the functional form or future conditions; the statement is conditional on the model.*

**10. Poland entered the market four years ago and the MMM says Polish TV has a low marginal ROAS. The best managerial response is:**

a) Cut Polish TV to zero immediately.
b) Ignore the model because Poland is culturally different.
c) Treat the result as a short-term estimate, cut gradually within bounds and test, because three years of data cannot capture brand building in a young market. **(correct)**
d) Increase Polish TV because awareness always pays off.

*Rationale: market maturity moderates what an MMM can see; young markets need caution and experiments, not corner solutions.*
