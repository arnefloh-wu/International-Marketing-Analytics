# Quiz 2: Marketing mix modelling I (one country)

Closed-book, 10 questions, one correct answer each. Opens after Session 2, due before Session 3.

**1. In a marketing mix model, "baseline" sales are**

a) sales in the weeks with no advertising at all
b) the sales the model would predict with all media spend set to zero, given price, promotions, seasonality and other controls **(correct)**
c) the average weekly sales over the modelling period
d) the residual of the regression

*Rationale: the baseline is the model's prediction without media; it still includes price, promotion, seasonal and trend effects.*

**2. Geometric adstock with a decay parameter alpha = 0.7 means that**

a) 70 % of this week's spend is wasted
b) the effect of a week's spend is spread over time, with each later week keeping 70 % of the previous week's effect **(correct)**
c) 70 % of sales are caused by advertising
d) the campaign lasts exactly 7 weeks

*Rationale: geometric adstock weights are alpha^l for lag l; with alpha 0.7 the effect decays by 30 % per week and the mean lag is 0.7/0.3, about 2.3 weeks.*

**3. Which channel would you expect to have the shortest carryover (lowest alpha)?**

a) Television
b) Out-of-home
c) Paid search **(correct)**
d) Sponsorship

*Rationale: search captures existing intent and the click happens immediately; brand channels like TV and OOH build memory that decays slowly.*

**4. The half-saturation point k of a Hill curve is**

a) the spend level at which the channel delivers half of its maximum effect **(correct)**
b) the spend level at which ROAS equals 0.5
c) half of the maximum observed spend
d) the point where marginal ROAS becomes negative

*Rationale: Hill(x) = x^s / (x^s + k^s) equals 0.5 exactly when x = k.*

**5. Average ROAS and marginal ROAS differ because**

a) average ROAS uses revenue and marginal ROAS uses units
b) on a concave response curve the next euro returns less than the average euro **(correct)**
c) marginal ROAS ignores adstock
d) average ROAS is always smaller

*Rationale: with diminishing returns the slope of the curve (marginal) is below the slope of the chord from the origin (average) at every positive spend level.*

**6. Media budgets are usually higher before Christmas, when chocolate sales peak anyway. In an MMM without seasonal controls this leads to**

a) underestimated media effects, because the peak is noise
b) overestimated media effects, because the seasonal peak is attributed to media **(correct)**
c) no bias, because OLS is unbiased
d) a lower R² than with controls

*Rationale: this is the planning confound; spend and sales rise together for a common reason, and omitting the reason biases the media coefficients upwards.*

**7. Why is the adstock decay parameter not estimated by ordinary least squares together with the other coefficients?**

a) It is a categorical variable
b) It enters the model non-linearly, inside the transformation of spend, so it is chosen by grid search or by non-linear or Bayesian estimation **(correct)**
c) OLS can only estimate one parameter per channel
d) Statsmodels does not support it

*Rationale: OLS is linear in parameters; alpha sits inside adstock(x, alpha), so we try values on a grid and compare fit (AIC or holdout error).*

**8. A Durbin-Watson statistic of 0.9 for an MMM's residuals suggests that**

a) the model fits very well
b) the residuals are positively autocorrelated, so something that moves slowly over time is missing from the model **(correct)**
c) multicollinearity is severe
d) the holdout error will be low

*Rationale: DW near 2 means no autocorrelation; values well below 1.5 indicate positive autocorrelation, often a missing trend or mis-specified carryover.*

**9. Two saturation specifications fit the data equally well (same R² and holdout MAPE) but give TV ROAS of 1.3 and 2.6. The correct conclusion is**

a) take the average, 1.95
b) choose the higher one, because it fits as well and is better for the budget
c) the data do not identify the saturation shape; the ROAS depends on an assumption that must be justified by business logic, priors or an experiment **(correct)**
d) the model is wrong and should be discarded

*Rationale: a very concave curve is almost flat over the observed spend and acts like a second intercept, moving baseline sales into media; fit statistics cannot tell the two apart.*

**10. Which channel's ROAS from an MMM should you trust least?**

a) A channel with bursty, flighted spend over three years
b) A channel with large, varying spend
c) A channel that is always on at a nearly constant level **(correct)**
d) A channel with a short carryover

*Rationale: a nearly constant regressor is collinear with the intercept; the model cannot separate its effect from the baseline, and its alpha profile is flat.*
