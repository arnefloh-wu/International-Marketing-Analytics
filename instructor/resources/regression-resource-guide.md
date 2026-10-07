# Regression analysis in Python: resource guide

Compiled on 5 October 2026 by parallel research agents for the course International Marketing Analytics (WU Vienna). Entries are ranked best first within each section. Links marked (unverified) or search-confirmed could not be fetched from the build environment and should be checked once before use.

Total entries: 137; new relative to the existing Notion list: 137.

---

# Regression in Python resources: software, web, video, data and real-world examples

Part 1 of the regression research brief (linear regression, non-linear effects, moderation, mediation, dummy and effect coding, assumptions and diagnostics, time-series regression). Versions and release dates were read from the PyPI JSON API on 5 October 2026; README and changelog text was read from github.com and raw.githubusercontent.com. Most documentation hosts (statsmodels.org, pingouin-stats.org, marginaleffects.com, *.github.io, realpython.com, YouTube, Kaggle, uber.com, booking.ai) are blocked by the sandbox proxy, so those links are confirmed from search listings only; anything not seen in a listing or fetched is marked "(unverified)".

Session mapping follows `instructor/course_design.md`: session 1 = toolkit and regression foundations (log-log elasticities, dummies, interactions, multicollinearity, Hofstede comparison); session 2 = MMM I, one country (adstock, saturation, residual autocorrelation, VIF, holdout); session 3 = MMM II, many countries (pooled vs fixed effects vs hierarchical); session 4 = forecasting as regression, experiments, attribution; session 5 = project pitches.

## 1. Software

### statsmodels (formula API, OLS/WLS/GLS, robust covariance, diagnostics)
- **Source:** statsmodels developers (Josef Perktold, Kevin Sheppard and others), 2009 to 2026, software. Version 0.15.0, released 27 August 2026, BSD-3-Clause, Python 3.10 or later.
- **Link:** https://pypi.org/project/statsmodels/ and https://github.com/statsmodels/statsmodels/releases
- **Why it matters:** The reference for teaching regression in Python: `smf.ols("np.log(sales) ~ np.log(price) + C(country) + promo:C(country)", df).fit(cov_type="HC3")` gives R-style output, `cov_type="cluster"` and `"HAC"` (Newey-West), `variance_inflation_factor`, `het_breuschpagan`, `acorr_breusch_godfrey`, `OLSInfluence` (Cook's distance, leverage), `plot_regress_exog`, and `statsmodels.stats.mediation.Mediation`. Release 0.15 abstracts the formula engine so either patsy or formulaic can be the backend and accepts polars DataFrames directly.
- **Use in course:** sessions 1 to 4 lab workhorse (elasticity models, MMM OLS, diagnostics, HAC errors); pin 0.15 in `requirements.txt`. Free.

### statsmodels.tsa (SARIMAX, ARDL, distributed lags)
- **Source:** statsmodels developers, part of statsmodels 0.15.0 (27 August 2026), software.
- **Link:** https://github.com/statsmodels/statsmodels/tree/main/examples/notebooks (see `autoregressive_distributed_lag.ipynb`, `statespace_sarimax_internet.ipynb`, `statespace_sarimax_faq.ipynb`)
- **Why it matters:** `SARIMAX(endog, exog=...)` is regression with ARIMA errors (ARIMAX), `ARDL` and `UECM` estimate distributed-lag models of advertising carry-over, `seasonal_decompose`/`STL` and `acf`/`pacf` plots diagnose residual autocorrelation; 0.15 adds Diebold-Mariano and Pesaran-Timmermann forecast tests.
- **Use in course:** session 2 (residual autocorrelation in the MMM, distributed lags as a bridge to adstock) and session 4 lab (forecast baseline). Free.

### PyFixest
- **Source:** Alexander Fischer, Styfen Schär and the py-econometrics team, 2023 to 2026, software. Version 0.60.0, 11 June 2026, MIT.
- **Link:** https://pypi.org/project/pyfixest/ and https://github.com/py-econometrics/pyfixest
- **Why it matters:** Port of R's fixest: `pf.feols("log_sales ~ log_price | country + week", data=df, vcov={"CRV1": "country"})` with fast high-dimensional fixed effects, IV and Poisson, wild cluster bootstrap (important with only 6 to 8 countries), randomisation inference, DiD and event-study estimators, multiple-estimation syntax, and `etable()` regression tables rendered with Great Tables. Integrates with marginaleffects.
- **Use in course:** session 3 (country and week fixed effects), session 4 (DiD on the geo-lift data). Free.

### marginaleffects (Python)
- **Source:** Vincent Arel-Bundock and contributors, 2023 to 2026, software. Version 0.6.1, 5 July 2026, GPL-3.0-or-later, Python 3.12 or later. The Python package now lives in the joint R/Python repository (the old pymarginaleffects repo was archived on 15 August 2026).
- **Link:** https://pypi.org/project/marginaleffects/ and https://github.com/vincentarelbundock/marginaleffects
- **Why it matters:** One consistent grammar (`predictions`, `comparisons`, `slopes`, `hypotheses`, `plot_slopes`) for interpreting interactions and non-linear terms: conditional slopes of price at each level of a cultural moderator, average marginal effects, contrasts between countries, delta-method or bootstrap intervals. Works on statsmodels formula models and pyfixest. The companion book *Model to Meaning* (CRC Press, 2026) is free online.
- **Use in course:** session 1 (interpreting an interaction with a Hofstede moderator), session 2 (slopes of non-linear response curves). Free.

### linearmodels
- **Source:** Kevin Sheppard, 2017 to 2025, software. Version 7.0, 21 October 2025, NCSA licence.
- **Link:** https://pypi.org/project/linearmodels/ and https://github.com/bashtage/linearmodels
- **Why it matters:** `PanelOLS` with entity and time effects and clustered covariance, `RandomEffects`, `BetweenOLS`, `FirstDifferenceOLS`, `IV2SLS`/`IVGMM` (price endogeneity), and a `compare()` table. Needs a (entity, time) MultiIndex, which is a useful lesson in panel data structure.
- **Use in course:** session 3 lab (panel OLS with country fixed effects, as named in the course design). Free.

### formulaic and patsy (formulas, dummy and effect coding)
- **Source:** formulaic: Matthew Wardrop, version 1.2.2, 2 June 2026, MIT. patsy: Nathaniel Smith, now maintained by Wardrop and Tomás Capretto, version 1.0.3, 29 August 2026, BSD-2.
- **Link:** https://pypi.org/project/formulaic/ and https://github.com/pydata/patsy
- **Why it matters:** These build the design matrix behind every formula: `C(country, Treatment(reference="DE"))`, `C(region, Sum)` for effect (deviation) coding, Helmert, polynomial contrasts, `bs()`/`cr()` splines and `I(price**2)`. The patsy README says it is no longer actively developed and recommends migrating to formulaic, which statsmodels 0.15 now supports as a backend.
- **Use in course:** session 1 (dummy vs effect coding of countries and seasons); background for the formula syntax students and AI assistants generate. Free.

### scikit-learn (linear models, splines, pipelines)
- **Source:** scikit-learn developers (Inria and community), 2007 to 2026, software. Version 1.9.1, 10 September 2026, BSD-3-Clause, Python 3.11 or later.
- **Link:** https://pypi.org/project/scikit-learn/
- **Why it matters:** `LinearRegression`, `Ridge` (the estimator inside Meta's Robyn MMM), `HuberRegressor`, `SplineTransformer` and `PolynomialFeatures` for non-linear effects, `OneHotEncoder(drop="first")` for dummies, `Pipeline`, `TimeSeriesSplit` for rolling-origin evaluation. No p-values or standard errors, which is a teachable contrast with statsmodels (prediction vs inference).
- **Use in course:** session 1 (out-of-sample fit), session 2 (ridge, holdout), session 4 (time-series cross-validation). Free.

### pingouin
- **Source:** Raphael Vallat, 2018 to 2026, software. Version 0.7.0, 26 September 2026, GPL-3.0, Python 3.11 or later.
- **Link:** https://pypi.org/project/pingouin/ and https://pingouin-stats.org/generated/pingouin.mediation_analysis.html (confirmed in search listing)
- **Why it matters:** `pg.mediation_analysis(data, x, m, y, covar, n_boot, seed)` returns a tidy table of a, b, total, direct and indirect paths with bias-corrected bootstrap intervals and supports parallel mediators; `pg.linear_regression` gives tidy OLS output with relative importance. No dedicated moderation function: moderation is a product term in `linear_regression` or statsmodels.
- **Use in course:** session 1 or background (simple mediation demo, e.g. advertising to brand attitude to sales). Free.

### PyProcessMacro (Python PROCESS)
- **Source:** Quentin André, 2017 to 2026, software. Version 2.2.0, 29 September 2026, MIT (distributed with Andrew Hayes's permission, not endorsed by him), Python 3.11 or later. Revived in September 2026 after years without releases.
- **Link:** https://pypi.org/project/pyprocessmacro/ and https://github.com/QuentinAndre/pyprocessmacro
- **Why it matters:** Reimplements all PROCESS models 1 to 76 (moderation, mediation, moderated mediation, serial mediation with model 6), tested against PROCESS 2.16 and, for the 42 models still defined, PROCESS for R 5.0; 2.2 adds multicategorical X and moderators (indicator, Helmert, effect coding), percentile spotlight values as in PROCESS 3+, negative binomial outcomes, `tidy()`/`glance()` outputs and `to_statsmodels()`. Note that its defaults follow PROCESS 2; `percent=True, spotlight="percentiles"` reproduces PROCESS 3 to 5.
- **Use in course:** background and optional lab for students who know PROCESS from SPSS courses; useful when a thesis supervisor expects PROCESS model numbers. Free.

### pyGAM
- **Source:** Daniel Servén Marín, Charlie Brummitt and contributors, 2018 to 2025, software. Version 0.12.0, 18 December 2025, Apache-2.0.
- **Link:** https://pypi.org/project/pygam/ and https://github.com/dswah/pyGAM
- **Why it matters:** Generalised additive models (`LinearGAM(s(0) + f(1) + te(2, 3))`) with penalised splines, factor terms, tensor interactions, monotonic and concave constraints and partial-dependence plots: a data-driven way to show students what a saturating spend-response curve looks like before imposing Hill or logistic forms.
- **Use in course:** session 2 (exploring the shape of the response curve). Free.

### Bambi
- **Source:** Tomás Capretto, Ravin Kumar, Osvaldo Martin and contributors (PyMC ecosystem), 2020 to 2026, software. Version 0.21.0, 10 September 2026, MIT, Python 3.12 or later.
- **Link:** https://pypi.org/project/bambi/ and https://bambinos.github.io/bambi/notebooks/plot_predictions.html (confirmed in search listing)
- **Why it matters:** Bayesian regression with R-style formulas, including hierarchical terms `(1 + log_price | country)`; its `interpret` module (`plot_predictions`, `plot_comparisons`, `plot_slopes`) is modelled on marginaleffects. A gentle step from OLS to the partial pooling used in PyMC-Marketing.
- **Use in course:** session 3 (partial pooling of elasticities across countries before PyMC-Marketing). Free.

### DoWhy and CausalML (causal mediation)
- **Source:** DoWhy: PyWhy (originally Microsoft Research), version 0.14, 8 November 2025, MIT. CausalML: Uber, version 0.17.0, 4 July 2026, Apache-2.0.
- **Link:** https://github.com/py-why/dowhy and https://www.pywhy.org/dowhy/v0.9/example_notebooks/dowhy_mediation_analysis.html (confirmed in search listing); https://pypi.org/project/causalml/
- **Why it matters:** DoWhy estimates natural direct and natural indirect effects from an explicit causal graph (and its GCM module quantifies causal influence), which shows students that mediation needs causal assumptions, not just a product of coefficients. CausalML focuses on uplift and heterogeneous treatment effects for marketing campaigns.
- **Use in course:** background; session 4 discussion of experiments vs observational estimates. Free.

### semopy
- **Source:** Georgy Meshcheryakov and Anastasia Igolkina, 2019 to 2024, software. Version 2.3.11, 4 January 2024, licence not stated on PyPI.
- **Link:** https://pypi.org/project/semopy/ (homepage semopy.com, unverified)
- **Why it matters:** lavaan-style SEM syntax in Python (`attitude ~ a*ad; sales ~ b*attitude + c*ad; ind := a*b`), so mediation with latent constructs (brand attitude measured by several items) can be estimated. No release since January 2024, so treat as stable but low-maintenance.
- **Use in course:** background only (thesis students with survey data). Free.

### StatsForecast and sktime (time-series regression and forecasting)
- **Source:** StatsForecast: Nixtla, version 2.1.1, 16 July 2026, Apache-2.0. sktime: sktime community, version 1.2.0, 22 September 2026, BSD-3-Clause. pmdarima 2.1.1 (17 November 2025, MIT) as an older auto-ARIMA option.
- **Link:** https://pypi.org/project/statsforecast/ and https://pypi.org/project/sktime/
- **Why it matters:** StatsForecast fits AutoARIMA (with exogenous regressors, i.e. ARIMAX), ETS and seasonal baselines quickly across many series (one per country) and is the engine used in the Python edition of *Forecasting: Principles and Practice*; sktime offers a scikit-learn-like interface with reduction (regression on lags) and pipelines.
- **Use in course:** session 4 lab (country-level forecasts, rolling-origin evaluation). Free.

### Regression tables: summary_col, PyFixest etable, stargazer and Great Tables
- **Source:** statsmodels `summary_col` (0.15.0); PyFixest `etable` (0.60.0); stargazer (Pietro Battiston and Matthew Burke), version 0.0.7, 4 April 2024, GPLv2; Great Tables (Posit), version 1.0.0, 25 September 2026, MIT.
- **Link:** https://github.com/StatsReporting/stargazer and https://pypi.org/project/great-tables/
- **Why it matters:** Side-by-side model tables (coefficients, standard errors, stars, R², N) for comparing pooled, fixed-effects and interaction models. `etable` already outputs Great Tables objects that render in Quarto HTML; stargazer mimics R's stargazer for statsmodels OLS but is barely maintained.
- **Use in course:** sessions 1 and 3 (model comparison table in the project repo milestone). Free.

### seaborn and Yellowbrick (diagnostic plots)
- **Source:** seaborn (Michael Waskom), version 0.13.2, 25 January 2024, BSD; Yellowbrick (District Data Labs), version 1.5, 21 August 2022, Apache-2.0.
- **Link:** https://pypi.org/project/seaborn/ and https://www.scikit-yb.org/en/latest/api/regressor/residuals.html (confirmed in search listing)
- **Why it matters:** `sns.regplot(order=2 / logx=True / lowess=True)`, `sns.residplot` and `sns.lmplot(hue="country")` make linearity, heteroscedasticity and group-specific slopes (moderation) visible in one line; Yellowbrick adds `ResidualsPlot`, `PredictionError` and `CooksDistance` for scikit-learn models. Yellowbrick has had no release since 2022.
- **Use in course:** sessions 1 and 2 (diagnostic plots in the lab). Free.

### ISLP (package)
- **Source:** James, Witten, Hastie, Tibshirani and Taylor, 2023 to 2026, software. Version 0.4.1, 3 February 2026, BSD-style licence.
- **Link:** https://pypi.org/project/ISLP/ and https://github.com/intro-stat-learning/ISLP
- **Why it matters:** Ships the textbook datasets (Carseats, OJ, Bikeshare, Credit, Wage and others) via `load_data()` plus `ModelSpec`, `poly()`, `bs()`, `ns()` helpers that make interaction and spline design matrices explicit; the companion Chapter 3 lab is a complete statsmodels regression walk-through.
- **Use in course:** session 1 warm-up data and exercises. Free.

### Reference points outside Python: R lm/fixest/marginaleffects and SPSS/R PROCESS
- **Source:** R Core (`lm`), Laurent Bergé (`fixest`), Arel-Bundock (`marginaleffects` for R), Jacob Long (`interactions`, Johnson-Neyman plots); Andrew F. Hayes, PROCESS macro for SPSS, SAS and R (current major release 5).
- **Link:** http://processmacro.org/ (workshops page confirmed in search listing) and https://cran.r-project.org/package=fixest (unverified)
- **Why it matters:** R remains the reference for regression teaching material, and most Python packages above are ports (pyfixest of fixest, marginaleffects, bambi of brms, pyprocessmacro of PROCESS). PROCESS is the de facto standard in marketing and consumer research for moderation and mediation, so students will meet "Model 4" and "Model 7" language in papers; pyprocessmacro lets them reproduce it without an SPSS licence.
- **Use in course:** background; one slide mapping SPSS PROCESS and R syntax to the Python equivalents.

## 2. Websites, documentation and blogs

### ISLP Chapter 3 lab: Linear Regression (Python)
- **Source:** James, Witten, Hastie, Tibshirani and Taylor, 2023, website (book lab notebook).
- **Link:** https://intro-stat-learning.github.io/ISLP/labs/Ch03-linreg-lab.html (confirmed in search listing)
- **Why it matters:** Short, rigorous statsmodels walk-through: simple and multiple regression, interaction terms, polynomial terms, qualitative predictors (Carseats `ShelveLoc` dummies), leverage and residual plots. Chapter 3 of the free book uses the Advertising data (TV x radio synergy) to explain interactions.
- **Use in course:** session 1 pre-reading and lab template. Free (book PDF free at statlearning.com).

### Model to Meaning: Interactions and polynomials chapter (marginaleffects.com)
- **Source:** Vincent Arel-Bundock, 2026, book website (CRC Press, free HTML).
- **Link:** https://marginaleffects.com/chapters/interactions.html (confirmed in search listing)
- **Why it matters:** Explains interactions, polynomial terms and conditional slopes with side-by-side R and Python code, and why raw coefficients on product terms mislead. The best current source for "how do I interpret this moderation model" with Python.
- **Use in course:** session 1 reading (moderation) and session 2 (non-linear slopes). Free.

### statsmodels example notebooks (regression diagnostics, interactions, contrasts, HAC, ARDL)
- **Source:** statsmodels developers, ongoing, documentation (Jupyter notebooks).
- **Link:** https://github.com/statsmodels/statsmodels/tree/main/examples/notebooks (fetched; rendered gallery at https://www.statsmodels.org/stable/examples/index.html, blocked here)
- **Why it matters:** Ready-made notebooks: `regression_diagnostics`, `linear_regression_diagnostics_plots`, `regression_plots` (influence, partial regression, CCPR), `contrasts` (treatment, sum, Helmert coding), `interactions_anova`, `categorical_interaction_plot`, `wls`, `gls`, `robust_models_*`, `autoregressive_distributed_lag`, `statespace_sarimax_*`.
- **Use in course:** sessions 1, 2 and 4 lab seeds; give students the diagnostic notebook as a checklist. Free.

### Coding for Economists: Regression, Regression diagnostics and visualisation chapters
- **Source:** Arthur Turrell (economist, formerly Bank of England), 2021 to 2026, online book (v1.0.0 archived on Zenodo, January 2024).
- **Link:** https://aeturrell.github.io/coding-for-economists/econmt-regression.html (confirmed in search listing)
- **Why it matters:** Practical, current Python regression chapters built on pyfixest and statsmodels: fixed effects, robust and clustered errors, transformations, interaction terms, multiple-model tables, plus chapters on diagnostics, generalised models and Bayesian regression with Bambi. Written for economists coming from Stata, which suits business students.
- **Use in course:** sessions 1 and 3 reading; template for regression tables. Free.

### Causal Inference for the Brave and True (chapters 5 to 7)
- **Source:** Matheus Facure, 2020 to 2022, online book.
- **Link:** https://matheusfacure.github.io/python-causality-handbook/05-The-Unreasonable-Effectiveness-of-Linear-Regression.html (confirmed in search listing)
- **Why it matters:** "The Unreasonable Effectiveness of Linear Regression", "Grouped and Dummy Regression" and "Beyond Confounders" explain regression as adjustment, Frisch-Waugh-Lovell, dummy variables and good vs bad controls (including why controlling for a mediator biases the total effect), all in statsmodels with business examples.
- **Use in course:** session 1 reading; session 4 background on causal interpretation. Free.

### The Effect, Chapter 13 Regression
- **Source:** Nick Huntington-Klein, 2021 (online), CRC Press 2022, book website.
- **Link:** https://theeffectbook.net/ch-StatisticalAdjustment.html (confirmed in search listing)
- **Why it matters:** Covers polynomials, logs, interaction terms (including why interactions are noisy and need much larger samples), heteroscedasticity-robust and clustered errors, with code in R, Stata and Python (statsmodels formulas with `I()`).
- **Use in course:** session 1 reading for interactions and transformations. Free online.

### Marginalia: a guide to marginal effects (Andrew Heiss)
- **Source:** Andrew Heiss (Georgia State University), 20 May 2022, blog post.
- **Link:** https://www.andrewheiss.com/blog/2022/05/20/marginalia/ (confirmed in search listing)
- **Why it matters:** Builds up marginal effects from slopes and partial derivatives, then distinguishes average marginal effects, marginal effects at the mean and conditional effects, with a summary table. R code, but concepts map one to one onto marginaleffects for Python.
- **Use in course:** background for the instructor; optional reading for session 1 interactions. Free.

### UCLA OARC: Contrast coding systems for categorical variables and PROCESS seminar
- **Source:** UCLA Office of Advanced Research Computing, Statistical Methods and Data Analytics, undated (maintained), website.
- **Link:** https://stats.oarc.ucla.edu/r/library/r-library-contrast-coding-systems-for-categorical-variables/ and https://stats.oarc.ucla.edu/other/mult-pkg/seminars/spss-process/ (both confirmed in search listings)
- **Why it matters:** The classic reference table of dummy, simple, deviation (effect), Helmert, difference and polynomial coding with what each coefficient means; the statsmodels/patsy contrasts page is a direct Python translation of it. The PROCESS seminar explains simple mediation and bootstrap indirect effects step by step.
- **Use in course:** session 1 (dummy vs effect coding for countries); background for mediation. Free.

### QuantEcon: Linear Regression in Python
- **Source:** Thomas J. Sargent and John Stachurski, QuantEcon, ongoing (PDF version dated 2020), lecture.
- **Link:** https://python.quantecon.org/ols.html (confirmed in search listing)
- **Why it matters:** Cross-country regression (institutions and GDP, replicating Acemoglu, Johnson and Robinson) with statsmodels and linearmodels, covering multivariate OLS, omitted variable bias, endogeneity and 2SLS. A good international example that is not marketing.
- **Use in course:** background; session 1 optional reading on cross-country regression and endogeneity. Free.

### Forecasting: Principles and Practice, the Pythonic Way, Chapter 7 Time series regression models
- **Source:** Rob J Hyndman, George Athanasopoulos, Azul Garza, Cristian Challu, Max Mergenthaler and Kin G. Olivares, 2025, online book (OTexts).
- **Link:** https://otexts.com/fpppy/07-regression.html (confirmed in search listing)
- **Why it matters:** Trend, seasonal dummies, Fourier terms, lagged predictors, intervention dummies and residual diagnostics for time-series regression, in Python with Nixtla's statsforecast and mlforecast. Chapter 10 (dynamic regression, ARIMA errors) is the bridge to ARIMAX.
- **Use in course:** session 4 core reading. Free.

### Real Python: Linear Regression in Python
- **Source:** Mirko Stojiljković, Real Python, website tutorial (originally 2019, updated; date unverified).
- **Link:** https://realpython.com/linear-regression-in-python/ (confirmed in search listing)
- **Why it matters:** Gentle introduction for non-programmers: simple, multiple and polynomial regression with scikit-learn and statsmodels, reading `summary()` output, under- and overfitting.
- **Use in course:** pre-course self-study before session 1. Free (some Real Python content needs a subscription).

### Python Data Science Handbook: In Depth, Linear Regression
- **Source:** Jake VanderPlas, 2016 (2nd edition O'Reilly 2022), online book chapter.
- **Link:** https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html (confirmed in search listing)
- **Why it matters:** Basis-function regression (polynomial and Gaussian bases) shows that "linear" means linear in coefficients, then ridge and lasso; ends with a bicycle-traffic time-series example with day-of-week and weather regressors.
- **Use in course:** session 2 background on non-linear effects and regularisation. Free online.

### Bambi interpret notebooks: Plot Predictions and Plot Comparisons
- **Source:** Bambi developers, 2023 to 2026, documentation.
- **Link:** https://bambinos.github.io/bambi/notebooks/plot_comparisons.html (confirmed in search listing)
- **Why it matters:** Worked examples of conditional predictions and comparisons for models with interactions, which double as a visual explanation of moderation (and of Bayesian uncertainty around it).
- **Use in course:** session 3 background. Free.

### You need 16 times the sample size to estimate an interaction (Gelman)
- **Source:** Andrew Gelman, Statistical Modeling, Causal Inference, and Social Science, 15 March 2018, blog post.
- **Link:** https://statmodeling.stat.columbia.edu/2018/03/15/need16/ (confirmed in search listing)
- **Why it matters:** The standard error of an interaction is about twice that of a main effect, and plausible interactions are smaller than main effects, so power collapses. A crucial caution before students claim that culture "moderates" an elasticity estimated on six countries.
- **Use in course:** session 1 or 3 discussion point. Free.

### Regression and Other Stories, Python ports
- **Source:** Pablo Insente (ROS-python) and Farhan Reynaldo (Bambi version), 2020 to 2023, GitHub/website; book by Gelman, Hill and Vehtari (Cambridge, 2020).
- **Link:** https://github.com/pabloinsente/ROS-python and https://farhanreynaldo.github.io/ros-python/ (both confirmed in search listing)
- **Why it matters:** Python versions of the book's examples on transformations, interactions, centring, log models and prediction; Gelman's own blog announced the port in August 2020.
- **Use in course:** background for the instructor. Free (book itself paid, PDF free on the authors' site, unverified).

### Seeing Theory: Regression Analysis, and R Psychologist interactive visualisations
- **Source:** Daniel Kunin et al., Brown University, 2017, interactive website; Kristoffer Magnusson, rpsychologist.com, interactive website.
- **Link:** https://seeing-theory.brown.edu/regression-analysis/index.html and https://rpsychologist.com/correlation/ (both confirmed in search listings)
- **Why it matters:** Drag points on Anscombe's quartet and watch the OLS line and R² react (Seeing Theory); Magnusson's correlation and r² visualisations show how outliers and restriction of range change estimates. No regression-specific moderation visual was found on rpsychologist.
- **Use in course:** session 1 lecture warm-up (influential points, R²). Free.

## 3. Video tutorials and courses

### StatQuest: Linear Regression, Clearly Explained; Multiple Regression; Using Linear Models for t-tests and ANOVA
- **Source:** Josh Starmer, StatQuest, YouTube videos (about 27 minutes for the linear regression video), beginner.
- **Link:** https://www.youtube.com/watch?v=7ArmBVF2dCs and https://www.youtube.com/watch?v=R7xd624pR1A (confirmed in search listings); index at https://statquest.org/video_index.html
- **Why it matters:** Least squares, R², why adding variables never lowers R², F-test p-values; the linear-models video shows that t-tests and ANOVA are regressions on dummy variables, the clearest intuition for dummy coding.
- **Use in course:** pre-session 1 viewing. Free.

### Statistical Learning with Python (Stanford, edX / YouTube)
- **Source:** Trevor Hastie, Robert Tibshirani and Jonathan Taylor, Stanford Online, 2023, video course; introductory to intermediate.
- **Link:** https://online.stanford.edu/courses/sohs-ystatslearningp-statistical-learning-python (confirmed in search listing)
- **Why it matters:** Chapter 3 lectures cover simple and multiple regression, interactions (Advertising TV x radio), qualitative predictors and the statsmodels lab; later chapters cover splines and GAMs. Lectures track the free ISLP book.
- **Use in course:** session 1 and 2 optional viewing. Free to audit; certificate about USD 186.

### Brandon Foltz: Statistics 101, Multiple Linear Regression playlist
- **Source:** Brandon Foltz, YouTube, playlist of 17 videos averaging about 20 minutes, beginner.
- **Link:** https://www.youtube.com/watch?v=fTfMdCQJz4s (Dummy Variables episode, confirmed in search listing)
- **Why it matters:** Slow, business-oriented explanations of multiple regression, dummy variables, two categorical predictors, multicollinearity and model building, with no programming, ideal for students without a statistics background.
- **Use in course:** pre-session 1 remedial viewing. Free.

### Ben Lambert: A full course in econometrics, undergraduate level
- **Source:** Ben Lambert, YouTube playlist (hundreds of short videos), undergraduate.
- **Link:** https://www.youtube.com/playlist?list=PLcZcY_ZXuygxO0CSE0lMa5WadbPpNix7v (confirmed in search listing)
- **Why it matters:** Intuition-first coverage of Gauss-Markov assumptions, heteroscedasticity (Breusch-Pagan, White, Goldfeld-Quandt), serial correlation (Durbin-Watson, Breusch-Godfrey), functional form and omitted variable bias.
- **Use in course:** sessions 1 and 2 reference clips on assumptions and diagnostics. Free.

### Andrew Hayes: Modern Integration of Mediation and Moderation Analysis
- **Source:** Andrew F. Hayes, YouTube talk (length unverified), intermediate.
- **Link:** https://www.youtube.com/watch?v=Lb8M-eQzL60 (confirmed in search listing)
- **Why it matters:** The author of PROCESS on conditional process analysis: why moderation and mediation belong in one model, the index of moderated mediation, and bootstrap inference.
- **Use in course:** background; optional viewing for students using mediation in projects. Free.

### Hayes / CCRAM: Mediation, Moderation, and Conditional Process Analysis (on demand and online course)
- **Source:** Andrew F. Hayes, Canadian Centre for Research Analysis and Methods (Haskayne, University of Calgary), paid workshop; online run 9 September 2026 to 9 March 2027 (per search listing).
- **Link:** https://haskayne.ucalgary.ca/CCRAM/mediation-moderation-and-conditional-process-analysis-on-demand (confirmed in search listing)
- **Why it matters:** The canonical training in PROCESS-style analysis (SPSS, SAS, R), based on Hayes's 3rd edition (2022).
- **Use in course:** background for the instructor; paid (fee unverified).

### DataCamp: Introduction to Regression with statsmodels in Python, and Intermediate Regression with statsmodels in Python
- **Source:** DataCamp, interactive courses, about 4 hours each, beginner and intermediate.
- **Link:** https://www.datacamp.com/courses/introduction-to-regression-with-statsmodels-in-python and https://www.datacamp.com/courses/intermediate-regression-with-statsmodels-in-python (confirmed in search listing)
- **Why it matters:** Browser-based exercises on `ols()` formulas, categorical predictors, transformations, prediction and diagnostics, then parallel slopes, interactions and Simpson's paradox. Suits students with no programming background.
- **Use in course:** pre-course or between sessions 1 and 2. Subscription (free via DataCamp Classrooms for teaching, unverified).

### Coursera: Fitting Statistical Models to Data with Python (University of Michigan)
- **Source:** Brenda Gunderson, Brady T. West and Kerby Shedden, University of Michigan, Coursera, course 3 of "Statistics with Python", intermediate, about 20 hours.
- **Link:** https://www.coursera.org/learn/fitting-statistical-models-data-python/ (confirmed in search listing)
- **Why it matters:** Linear and logistic regression, multilevel and marginal models in statsmodels and seaborn on real data, taught by a statsmodels core developer (Shedden).
- **Use in course:** optional self-study. Free to audit; certificate via Coursera subscription.

### Mostly Harmless Fixed Effects Regression in Python with PyFixest (PyCon DE and PyData Berlin 2024)
- **Source:** Alexander Fischer (trivago), conference talk, 24 April 2024, about 30 minutes (unverified), intermediate.
- **Link:** https://www.youtube.com/watch?v=kSQxGGA7Rr4 (confirmed in search listing)
- **Why it matters:** Fixed effects via Frisch-Waugh-Lovell, cluster-robust inference and wild bootstrap, A/B test analysis and staggered event studies in pyfixest, presented by a European industry economist.
- **Use in course:** session 3 background; Fischer is a plausible guest speaker (industry econometrics, Germany). Free.

### Mixtape Sessions: Causal Inference I
- **Source:** Scott Cunningham and guest instructors, Mixtape Sessions, multi-day live workshops, intermediate; code in R and Stata (Python not confirmed).
- **Link:** https://github.com/Mixtape-Sessions/Causal-Inference-1 and https://www.mixtapesessions.io/session/ci_i_sept27/ (confirmed in search listing)
- **Why it matters:** Regression as adjustment, potential outcomes, DAGs, IV and RDD with open slides and problem sets on GitHub; the companion book *Causal Inference: The Mixtape* includes Python code (unverified for every chapter).
- **Use in course:** background for session 4 (experiments, DiD). Paid live workshops (sliding-scale fee, unverified); materials free on GitHub.

### freeCodeCamp: regression analysis course for beginners
- **Source:** Ayush Singh for freeCodeCamp.org, YouTube, about 10 hours, beginner.
- **Link:** https://www.freecodecamp.org/news/master-regression-analysis-for-machine-learning/ (confirmed in search listing)
- **Why it matters:** Linear, multiple and polynomial regression, feature engineering and model evaluation in Python. Machine-learning framing (prediction rather than inference), so weaker on standard errors, moderation and mediation.
- **Use in course:** optional self-study only. Free.

### 3Blue1Brown: Essence of Linear Algebra
- **Source:** Grant Sanderson, YouTube series, beginner to intermediate.
- **Link:** https://www.youtube.com/c/3blue1brown (confirmed in search listing)
- **Why it matters:** No dedicated regression video was found; the linear-algebra series (projections, column space) is the best visual background for why OLS is a projection and why perfect multicollinearity breaks it.
- **Use in course:** background only. Free.

## 4. Data

### Advertising.csv (ISLR/ISLP)
- **Source:** James, Witten, Hastie and Tibshirani, *An Introduction to Statistical Learning*, dataset; 200 markets x 4 variables (TV, radio, newspaper spend in USD thousands; sales in thousand units).
- **Link:** https://www.statlearning.com/s/Advertising.csv (confirmed in search listing; not in the ISLP package's `load_data`)
- **Why it matters:** The canonical teaching set for multiple regression, the TV x radio interaction (synergy), diminishing returns (log or square-root TV) and the "newspaper is significant alone but not jointly" lesson in omitted variables.
- **Use in course:** session 1 warm-up and session 2 bridge to response curves. Free for teaching (book data).

### Carseats (ISLP)
- **Source:** ISLP package, simulated data, 400 stores x 11 variables (Sales, Price, CompPrice, Advertising, Income, ShelveLoc Bad/Medium/Good, Urban, US).
- **Link:** https://islp.readthedocs.io/en/latest/datasets/Carseats.html (confirmed in search listing) and https://github.com/intro-stat-learning/ISLP (fetched)
- **Why it matters:** Ideal for dummy coding (three-level `ShelveLoc` and changing the reference level), price x advertising and price x US interactions, and effect coding comparisons.
- **Use in course:** session 1 lab exercise. Free (BSD-style).

### OJ and Bikeshare (ISLP)
- **Source:** ISLP package. OJ: 1,070 orange juice purchases (Citrus Hill vs Minute Maid) with prices, discounts, specials, brand loyalty and store, from Stine, Foster and Waterman, *Business Analysis Using Regression* (1998). Bikeshare: hourly and daily Capital Bikeshare counts 2011 to 2012 with season, holiday, weather.
- **Link:** https://github.com/intro-stat-learning/ISLP/tree/main/docs/source/datasets (fetched)
- **Why it matters:** OJ is a compact price-and-promotion dataset (price differences, discounts, loyalty as a moderator); Bikeshare teaches seasonal dummies, hour-of-day effects and count outcomes.
- **Use in course:** sessions 1 (OJ, promotions) and 4 (Bikeshare, seasonality and time-series regression). Free.

### dunnhumby Source Files: Breakfast at the Frat
- **Source:** dunnhumby, dataset; 156 weeks of unit sales, spend, base and shelf price, feature (sale tag) and display for products in four categories (mouthwash, pretzels, frozen pizza, boxed cereal) across stores.
- **Link:** https://www.dunnhumby.com/source-files/ (confirmed in search listing; registration required)
- **Why it matters:** Real retail scanner data for log-log price elasticities, promotion dummies, feature x display interactions and store fixed effects, at a manageable size.
- **Use in course:** session 1 extension exercise or a project alternative. Free with registration; dunnhumby terms restrict redistribution (do not commit raw files to the course repo).

### dunnhumby: The Complete Journey (completejourney-py)
- **Source:** dunnhumby; Python port of the R `completejourney` package, version 0.1.0, MIT (data under dunnhumby terms); about 2,500 households, one year of transactions, campaigns, coupons and demographics.
- **Link:** https://pypi.org/project/completejourney-py/
- **Why it matters:** Household-level data for regression of spend on campaign exposure with demographic moderators (income, household size), and for discussing selection into campaigns.
- **Use in course:** background or project alternative. Free.

### Dominick's Finer Foods (Kilts Center, Chicago Booth)
- **Source:** Kilts Center for Marketing, University of Chicago Booth; about 9 years (1989 to 1997) of weekly store-level scanner data for roughly 100 Chicago stores and 3,500+ UPCs in 25+ categories, including randomised pricing experiments.
- **Link:** https://www.chicagobooth.edu/research/kilts/research-data/dominicks (confirmed in search listing); Eurostat's R/SAS helper repo https://github.com/eurostat/dff
- **Why it matters:** The classic dataset behind decades of price-elasticity and promotion research; good for log-log demand models with store and week fixed effects and for showing elasticity differences across store demographics.
- **Use in course:** background or advanced project data. Free for academic research only, acknowledgement required; files are large SAS/Stata zips.

### Rossmann Store Sales (Kaggle)
- **Source:** Rossmann (German drugstore chain), Kaggle competition, 2015; daily sales for 1,115 German stores 2013 to 2015 with Promo, Promo2, school and state holidays, competitor distance and store type.
- **Link:** https://www.kaggle.com/datasets/pratyushakar/rossmann-store-sales (mirror, confirmed in search listing; original competition at https://www.kaggle.com/c/rossmann-store-sales, unverified)
- **Why it matters:** A European, marketing-relevant time series: promotion dummies, day-of-week and holiday effects, trend, lagged effects and store heterogeneity (promotion x store type moderation).
- **Use in course:** session 4 (time-series regression with promotions) or session 1 promo-elasticity demo. Free with Kaggle login; competition rules govern use (check before redistributing).

### Walmart store sales and M5 (Kaggle)
- **Source:** Walmart Recruiting Store Sales Forecasting (Kaggle, 2014): weekly sales for 45 stores by department 2010 to 2012 with holiday flags and markdowns MarkDown1 to 5. M5 (Kaggle, 2020): 3,049 products in 10 US stores over 1,941 days with prices, SNAP days and events.
- **Link:** https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data (confirmed in search listing)
- **Why it matters:** Holiday dummies, promotion (markdown) effects, seasonality and hierarchical structure; M5 adds daily prices for elasticity estimation.
- **Use in course:** session 4 forecasting exercise or project extension. Free with Kaggle login; competition terms apply.

### Hofstede dimension data matrix
- **Source:** Geert Hofstede / Hofstede Insights, dataset (version 2015-12-08): six dimensions (PDI, IDV, MAS, UAI, LTO, IVR) for roughly 100 countries and regions (count unverified); .csv, .xls, .sav.
- **Link:** https://geerthofstede.com/research-and-vsm/dimension-data-matrix/ (confirmed in search listing)
- **Why it matters:** The standard country-level moderator: merge with country elasticities and regress elasticity on power distance or uncertainty avoidance (as in Datta et al. 2022), or interact log price with a dimension in a pooled model.
- **Use in course:** session 1 (already planned via `country_meta.csv`) and session 3. Free for research use; contact the owners for commercial use.

### World Bank WDI via wbgapi
- **Source:** World Bank, World Development Indicators; `wbgapi` Python client version 1.0.14, 27 February 2026.
- **Link:** https://pypi.org/project/wbgapi/
- **Why it matters:** GDP per capita, inflation, internet penetration, Gini and population for cross-country regressions and as moderators of marketing elasticities (income inequality in Datta et al. 2022). Data are CC BY 4.0.
- **Use in course:** sessions 1 and 3 (country covariates). Free.

### Eurostat via the eurostat package
- **Source:** Eurostat; `eurostat` Python package version 1.1.1, 13 June 2024.
- **Link:** https://pypi.org/project/eurostat/
- **Why it matters:** Harmonised EU retail trade volumes, HICP prices, household consumption and digital economy indicators by country and month: good for time-series regressions with seasonality and for EU cross-country panels.
- **Use in course:** session 4 (monthly retail trade series) or projects. Free (Eurostat reuse policy, attribution).

### Our World in Data and Gapminder
- **Source:** Our World in Data (`owid-catalog` 1.2.7, 5 October 2026) and the `gapminder` Python package (0.1, 2018, copy of the R teaching data: 142 countries, 1952 to 2007, life expectancy, population, GDP per capita).
- **Link:** https://pypi.org/project/owid-catalog/ and https://pypi.org/project/gapminder/
- **Why it matters:** Gapminder is the cleanest dataset for teaching log transformations (log GDP), continent dummies and continent x GDP interactions; OWID adds hundreds of current indicators, CC BY.
- **Use in course:** session 1 warm-up (logs and interactions with a non-marketing example). Free.

### statsmodels built-in datasets and Rdatasets
- **Source:** statsmodels `sm.datasets` (e.g. `macrodata`, `longley`, `grunfeld`) and `sm.datasets.get_rdataset()` access to Rdatasets (e.g. `Duncan` from carData, `Guerry` from HistData).
- **Link:** https://github.com/statsmodels/statsmodels/tree/main/statsmodels/datasets and https://vincentarelbundock.github.io/Rdatasets/ (from the statsmodels docs source, fetched)
- **Why it matters:** One-line loading; Duncan is the textbook case for influential observations (ministers, conductors), Guerry for cross-regional regression, `macrodata` for quarterly time-series regression with HAC errors.
- **Use in course:** session 1 and 2 diagnostics exercises. Free (`get_rdataset` needs internet).

### Housing datasets: caveats (Boston, California)
- **Source:** Boston housing (Harrison and Rubinfeld 1978) in ISLP; California housing (`sklearn.datasets.fetch_california_housing`, 20,640 block groups).
- **Link:** https://github.com/intro-stat-learning/ISLP (Boston listed in ISLP datasets, fetched)
- **Why it matters:** Boston was removed from scikit-learn (1.2) because of its racially constructed `B` variable and data issues; avoid it or use it only to discuss data ethics. California housing is fine for non-linear effects but is not marketing.
- **Use in course:** avoid in labs; mention as a caveat when students find these in AI-generated code. Free.

### Kaggle: Customer Personality Analysis (marketing campaign)
- **Source:** Kaggle community upload (originally an iFood-style case dataset), about 2,240 customers x 29 variables: demographics, spend by category, campaign responses, web and store purchases (size from search listings, unverified).
- **Link:** https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis (unverified)
- **Why it matters:** Easy cross-sectional marketing data for regression of spend on income with education and marital-status dummies, and moderation (income x kids at home).
- **Use in course:** optional practice data. Free with login; licence stated as CC0 on Kaggle (unverified).

## 5. Real-world examples

### Cross-national differences in market response (Datta, van Heerde, Dekimpe and Steenkamp 2022)
- **Source:** Hannes Datta, Harald J. van Heerde, Marnik G. Dekimpe and Jan-Benedict E. M. Steenkamp, *Journal of Marketing Research* 59(2), 2022, article.
- **Link:** https://doi.org/10.1177/00222437211058102 (confirmed in search listing)
- **Why it matters:** 1,600+ brands, 14 categories, 14 Indo-Pacific Rim countries over 10+ years: average price elasticity -0.42, line-length 0.46, distribution 0.37, with elasticities explained by brand, category and country factors; high power distance (Hofstede) and income inequality lower price and distribution elasticities. A direct model for the course's "elasticity moderated by culture" exercise.
- **Use in course:** session 1 case (second-stage regression of elasticities on Hofstede and GDP) and session 3. Paywalled; check WU library access.

### CUPED: regression adjustment in A/B tests at Microsoft and Booking.com
- **Source:** Alex Deng, Ya Xu, Ron Kohavi and Toby Walker, WSDM 2013, paper (Microsoft); Simon Jackson, Booking.com, 2018, engineering blog.
- **Link:** https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf and https://booking.ai/how-booking-com-increases-the-power-of-online-experiments-with-cuped-995d186fff1d (both confirmed in search listings)
- **Why it matters:** Adding the pre-period metric as a covariate (essentially regression adjustment) cuts variance and required sample size; Booking.com explains why tiny conversion effects across 1.5 million room nights a day need it. Shows students that "controls" in regression matter even in randomised experiments.
- **Use in course:** session 4 (experiments and geo-lift). Free.

### DoorDash CUPAC and Glovo covariate adjustment
- **Source:** DoorDash Engineering, 2020 (date unverified), blog; Glovo Engineering (Barcelona), Medium blog (date unverified).
- **Link:** https://careersatdoordash.com/blog/improving-experimental-power-through-control-using-predictions-as-covariate-cupac/ and https://medium.com/glovo-engineering/variance-reduction-in-experiments-using-covariate-adjustment-techniques-717b1e450185 (both confirmed in search listings)
- **Why it matters:** Extends CUPED by using a machine-learned prediction of the outcome as the regression covariate (CUPAC); Glovo, a European delivery platform, compares covariate-adjustment estimators in practice.
- **Use in course:** session 4 extension reading; Glovo is a possible European guest-speaker lead. Free.

### Uber Labs: mediation modelling and causal inference
- **Source:** Uber Engineering blog (Uber Labs: Totte Harinen, Bonnie Li and colleagues), 2019, engineering blog posts.
- **Link:** https://www.uber.com/us/en/blog/causal-inference-at-uber/ and https://uber.com/en-PL/blog/mediation-modeling (both confirmed in search listings)
- **Why it matters:** Uses mediation analysis to explain why a product change moved an outcome (for example, how delivery delays affect future Uber Eats engagement) and to promote a proven mediator to a short-term KPI. A business example of mediation beyond survey research, with the causal caveats spelled out.
- **Use in course:** session 1 or 4 example of mediation (marketing action to intermediate metric to sales). Free.

### Google geo experiments: geo-based and time-based regression
- **Source:** Jon Vaver and Jim Koehler, Google, 2011, white paper; Jouni Kerman, Peng Wang and Jon Vaver, Google, 2017, white paper.
- **Link:** https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/ and https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/ (both confirmed in search listings)
- **Why it matters:** Ad effectiveness (iROAS) estimated by weighted regression of post-period response on pre-period response across geos (GBR), and by a time-series regression of treated on control markets (TBR). Exactly the bridge from regression to the geo-lift test in session 4.
- **Use in course:** session 4 reading and lab rationale for `geolift_germany.csv`. Free.

### Facebook advertising RCTs vs observational regression (Gordon, Zettelmeyer, Bhargava and Chapsky 2019)
- **Source:** Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava and Dan Chapsky, *Marketing Science* 38(2), 2019, article.
- **Link:** https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf (confirmed in search listing); DOI 10.1287/mksc.2018.1135 (unverified)
- **Why it matters:** 15 Facebook campaigns run as RCTs (500 million user-experiment observations): matching and regression-based observational methods often overstated lift, sometimes by a factor of three or more. The strongest evidence for why regression coefficients on ad exposure are not automatically causal.
- **Use in course:** session 4 case (experiments vs models). Free working-paper PDF.

### Walmart and the M5 forecasting competition
- **Source:** Spyros Makridakis, Evangelos Spiliotis and Vassilios Assimakopoulos, *International Journal of Forecasting*, 2022, article; Walmart forecasting team (Brian Seaman and colleagues; authorship unverified), "Applicability of the M5 to Forecasting at Walmart", IJF 2022, commentary.
- **Link:** https://www.sciencedirect.com/science/article/pii/S0169207021001874 and https://www.sciencedirect.com/science/article/abs/pii/S0169207021001023 (both confirmed in search listings)
- **Why it matters:** Forecasting Walmart unit sales showed that pure extrapolation fails without price, promotion, holiday and event regressors; Walmart's own commentary explains what transfers to production forecasting.
- **Use in course:** session 4 reading (forecasting as regression with promotion covariates). Results paper open access (unverified); commentary paywalled.

### Meta Robyn: ridge regression MMM in production
- **Source:** Meta Marketing Science (facebookexperimental), 2021 to 2026, open-source software and documentation (R stable; Python version in beta).
- **Link:** https://github.com/facebookexperimental/Robyn (fetched)
- **Why it matters:** A widely used industry MMM that is, at its core, a ridge regression on adstocked and saturated media variables with trend and seasonality decomposed by Prophet: the clearest real-world proof that MMM is time-series regression with transformed regressors.
- **Use in course:** session 2 (link OLS MMM to industry practice). Free, MIT.

### statworx: Food for Regression, price elasticity from sales data
- **Source:** statworx (Frankfurt data-science consultancy), blog post (date unverified).
- **Link:** https://www.statworx.com/en/content-hub/blog/food-for-regression-using-sales-data-to-identify-price-elasticity (confirmed in search listing)
- **Why it matters:** A German consultancy's worked example of estimating price elasticity with log-log regression on retail sales, including the pitfalls (promotions, endogeneity, too little price variation). statworx is a realistic DACH guest-speaker lead.
- **Use in course:** session 1 reading alongside the "Is our price too high in Poland?" exercise. Free.

## Gaps and caveats

Most documentation and media hosts were blocked by the sandbox proxy, so links on statsmodels.org, pingouin-stats.org, marginaleffects.com, the *.github.io books, realpython.com, YouTube, Kaggle, DataCamp, Coursera, uber.com and booking.ai were confirmed from search listings only, not opened; video lengths, course fees and some publication dates (statworx, DoorDash, Glovo, Uber mediation post, Real Python) could not be checked. PyPI versions and dates are exact as of 5 October 2026; the GitHub API was not available, so star counts and commit activity are not given. Maintenance risk: patsy (maintenance only), stargazer (last release April 2024), semopy (January 2024) and Yellowbrick (August 2022) are stale; pyprocessmacro was revived only in late September 2026 and its defaults follow PROCESS 2, not PROCESS 5. marginaleffects and Bambi require Python 3.12 or later, and marginaleffects and pingouin are GPL-licensed (fine for teaching). No dedicated Python video on moderation or mediation of good quality was found, nor a 3Blue1Brown regression video; Keith Galli and Corey Schafer have no regression-specific statsmodels tutorials that could be confirmed. Kaggle and dunnhumby data require logins and have redistribution limits, Dominick's is for academic use only, and the Kaggle marketing-campaign dataset URL and licence are unverified. Datta et al. (2022), Gordon et al. (2019, journal version) and the Walmart M5 commentary are paywalled outside the WU library.

# Regression analysis with Python: books, journal articles, reports, teaching cases and course examples

Part 02 of the regression resource search (brief: `RESEARCH_BRIEF_REGRESSION.md`). Covers four categories: Books; Journal articles; Reports; Teaching cases and course examples. Searched 5 October 2026. The Consensus tool was out of quota (30 of 30 searches used), so every DOI below comes from web search listings (publisher, JSTOR, RePEc, SSRN or university repository pages). The sandbox proxy blocked almost every publisher and course host (Wiley, Springer, INFORMS, SAGE, Cambridge, otexts.com, statlearning.com, theeffectbook.net, quantecon.org, duke.edu, nist.gov, arxiv.org, Darden store, Crossref API); GitHub pages could be fetched and were used to confirm book code, notebooks and course repositories. Entries resting on a search listing alone for a detail are marked "(unverified)" at that detail.

Session map used below (from `instructor/course_design.md`): Session 1 regression foundations (coefficients, log-log elasticities, dummies, interactions, multicollinearity, cross-country comparison with Hofstede/GDP); Session 2 MMM I (adstock, saturation, residual autocorrelation, VIF); Session 3 MMM II (pooled vs fixed effects vs hierarchical, clustering); Session 4 forecasting as regression (trend, seasonality, lags), experiments, attribution; Session 5 pitches. Mediation is not a scheduled topic, so mediation material is tagged "background" or optional Session 1 extension.

## Books

### Regression Analysis (Handbook of Market Research)
- **Source:** Bernd Skiera, Jochen Reiner and Sönke Albers, in C. Homburg, M. Klarmann and A. Vomberg (eds), *Handbook of Market Research*, Springer, 2022, pp. 299 to 327, book chapter
- **Link:** https://doi.org/10.1007/978-3-319-57413-4_17 (PDF supplied by the instructor, licensed; not in the repository)
- **Why it matters:** Regression for marketing decisions from start to finish on one numerical example (quantity, price, advertising, salespersons in 16 districts): least squares, R² and F-test, standardised coefficients, the seven assumptions, multicollinearity with VIF (mailings and salespersons, r = 0.989, VIF 53), Durbin-Watson, heteroscedasticity tests, outliers with Cook's and Mahalanobis distance, the multiplicative (log-log) sales response function with elasticities (price -2.34), the optimal price and budget from the estimated function, and endogeneity.
- **Use in course:** Session 1 core reading; structure of the assumptions-and-tests part of the regression deck (01c). Paid (Springer; WU SpringerLink licence).

### An Introduction to Statistical Learning, with Applications in Python (ISLP)
- **Source:** James, Witten, Hastie, Tibshirani and Taylor, Springer, 2023, book (free PDF on the book website)
- **Link:** https://www.statlearning.com/ (host blocked; free PDF and Springer edition confirmed via search listing and https://link.springer.com/doi/10.1007/978-3-031-38747-0); labs confirmed at https://github.com/intro-stat-learning/ISLP_labs
- **Why it matters:** Chapter 3 (linear regression) uses the Advertising data (sales on TV, radio, newspaper), covers qualitative predictors, the TV x radio interaction, polynomial terms and residual diagnostics; Chapter 7 covers polynomials, step functions and splines. The `Ch03-linreg-lab.ipynb` notebook is maintained and uses statsmodels. The cleanest marketing-flavoured, free, Python-native regression text available.
- **Use in course:** Session 1 (Ch. 3 as core reading and lab warm-up), Session 2 (Ch. 7 sections on non-linear fits as background to saturation curves); free.

### Python for Marketing Research and Analytics
- **Source:** Jason S. Schwarz, Chris Chapman and Elea McDonnell Feit, Springer, 2020, book (283 pp.)
- **Link:** https://doi.org/10.1007/978-3-030-49720-0 (Springer, confirmed via listing); code and data at https://github.com/python-marketing-research/python-marketing-research-1ed (fetched; Apache-2.0)
- **Why it matters:** The only Python regression text written for marketers. Chapter 7 "Identifying Drivers of Outcomes: Linear Models" (doi 10.1007/978-3-030-49720-0_7) runs a satisfaction-drivers regression with statsmodels formulas, standardisation, factor (dummy) coding, interactions and a short marketing-mix example; Chapter 8 "Additional Linear Modeling Topics" covers collinearity/VIF, logistic regression and hierarchical models. All examples are Colab notebooks with simulated marketing data.
- **Use in course:** Session 1 (Ch. 7 as reading; notebooks as lab), Session 2 (Ch. 8 on collinearity); paid (Springer, often free via WU SpringerLink licence).

### Regression and Other Stories
- **Source:** Andrew Gelman, Jennifer Hill and Aki Vehtari, Cambridge University Press, 2020 (corrected online version), book; free PDF for personal use
- **Link:** https://users.aalto.fi/~ave/ROS.pdf (free PDF, confirmed via search listing; host blocked) and https://avehtari.github.io/ROS-Examples/ ; R code at https://github.com/avehtari/ROS-Examples (fetched, R only); Python/Bambi port at https://github.com/bambinos/Bambi_resources/tree/master/ROS (fetched)
- **Why it matters:** The best modern teaching text on interpreting regression. Ch. 10 (multiple predictors, indicator variables, interactions), Ch. 11 (assumptions, diagnostics, model evaluation, with a clear ranking of which assumptions matter most), Ch. 12 (log transformations and elasticity-style interpretation, standardising) and Chs. 18 to 21 (causal inference with regression) map directly onto Session 1. Simulation-first style suits AI-assisted coding.
- **Use in course:** Session 1 (Chs. 10 and 12 as reading), Session 2 (Ch. 11 on diagnostics); free PDF; examples are R/rstanarm, Python port partial.

### Introduction to Mediation, Moderation, and Conditional Process Analysis (3rd ed.)
- **Source:** Andrew F. Hayes, Guilford Press, January 2022, book (732 pp.)
- **Link:** https://www.routledge.com/Introduction-to-Mediation-Moderation-and-Conditional-Process-Analysis-Third-Edition-A-Regression-Based-Approach/Hayes/p/book/9781462549030 (confirmed via listing; author page with PROCESS downloads https://www.afhayes.com/introduction-to-mediation-moderation-and-conditional-process-analysis.html)
- **Why it matters:** The PROCESS reference used by almost every consumer-behaviour paper students will read. Parts on mediation, moderation (simple slopes, Johnson-Neyman, multicategorical moderators) and conditional process (moderated mediation) are all OLS-based; the 3rd edition adds PROCESS for R next to SPSS and SAS. Use it to give students the vocabulary, then reproduce the models in statsmodels.
- **Use in course:** background (instructor reference for moderation in Session 1 and any student project with survey data); paid (about EUR 80).

### Coding for Economists
- **Source:** Arthur Turrell, 2021 to present, free online book (Python, Quarto/Jupyter)
- **Link:** https://aeturrell.github.io/coding-for-economists (host blocked); source confirmed at https://github.com/aeturrell/coding-for-economists (fetched; MIT licence)
- **Why it matters:** Python-only, current and practical. The `econmt-regression` chapter shows statsmodels and pyfixest with formulas, fixed effects, robust and clustered standard errors and regression tables; `econmt-diagnostics` covers residual and influence diagnostics; `time-series` covers lags and autocorrelation. Closest in spirit to the course stack.
- **Use in course:** Session 1 and Session 3 (regression and fixed-effects chapters as lab reference), Session 4 (time-series chapter); free.

### Introductory Econometrics: A Modern Approach (8th ed.) with Using Python for Introductory Econometrics (2nd ed.)
- **Source:** Jeffrey M. Wooldridge, Cengage, January 2025, book; Florian Heiss and Daniel Brunner, 2024, free open-access Python companion
- **Link:** https://www.cengage.com/c/introductory-econometrics-a-modern-approach-8e-wooldridge/9780357900161/ and http://www.upfie.net/ (companion; both confirmed via listing)
- **Why it matters:** The standard applied econometrics text: Ch. 6 (logs, quadratics, interactions), Ch. 7 (dummy variables, interactions with dummies, Chow tests), Ch. 8 (heteroskedasticity-robust inference), Chs. 10 to 12 (time-series regression, trends, seasonality, serial correlation, HAC errors). Heiss and Brunner reproduce every example in Python with statsmodels and the `wooldridge` data package, chapter for chapter.
- **Use in course:** Session 1 (Chs. 6 to 7), Session 4 (Chs. 10 to 12); Wooldridge paid (about EUR 70 to 90), UPfIE free.

### Forecasting: Principles and Practice, the Pythonic Way
- **Source:** Rob J. Hyndman, George Athanasopoulos, Azul Garza, Cristian Challu, Max Mergenthaler and Kin G. Olivares, OTexts, 2025 (print May 2026), free online book
- **Link:** https://otexts.com/fpppy/ (host blocked; confirmed via IIF announcement https://forecasters.org/blog/2025/04/25/forecasting-principles-and-practice-the-pythonic-way/ and https://robjhyndman.com/hyndsight/fpppy.html)
- **Why it matters:** Python (Nixtla) edition of fpp3. The time-series regression chapter (trend, seasonal dummies, Fourier terms, lagged predictors, residual autocorrelation checks) and the dynamic regression chapter (regression with ARIMA errors, distributed lags) are the clearest free treatment of forecasting as regression. First 13 chapters follow fpp3 numbering (Ch. 7 time-series regression, Ch. 10 dynamic regression, unverified for the Python edition).
- **Use in course:** Session 4 (core reading for forecasting as regression), Session 2 (seasonality controls); free.

### The Effect: An Introduction to Research Design and Causality (2nd ed.)
- **Source:** Nick Huntington-Klein, Chapman and Hall/CRC (Routledge), July 2025, book; free online edition
- **Link:** https://theeffectbook.net/ (host blocked; confirmed via listing) and https://www.routledge.com/The-Effect-An-Introduction-to-Research-Design-and-Causality/Huntington-Klein/p/book/9781032580227
- **Why it matters:** Ch. 13 "Regression" explains controls, polynomial terms, logs, interactions, robust and clustered standard errors with R, Stata and Python code side by side; the causal-diagram chapters explain why "controlling for" a mediator distorts a marketing effect. Written for students with no maths background.
- **Use in course:** Session 1 (Ch. 13), Session 4 (difference-in-differences and synthetic control chapters); free online, print about EUR 60.

### Causal Inference for the Brave and True
- **Source:** Matheus Facure, 2020 to present, free online book (Python)
- **Link:** https://matheusfacure.github.io/python-causality-handbook/landing-page.html (host blocked); source confirmed at https://github.com/matheusfacure/python-causality-handbook (fetched)
- **Why it matters:** Short, humorous Python chapters on regression as a causal tool, omitted-variable bias, good and bad controls, dummy-variable regression, fixed effects and difference-in-differences, all in statsmodels. A good bridge from Session 1 elasticities to Session 4 experiments.
- **Use in course:** Session 1 and Session 4 (optional readings); free.

### Introduction to Econometrics (4th ed.)
- **Source:** James H. Stock and Mark W. Watson, Pearson, 2019 (Global Edition ISBN 9781292264455), book
- **Link:** https://www.pearson.com/en-gb/subject-catalog/p/introduction-to-econometrics-global-edition/P200000005500/9781292740652 (confirmed via listing)
- **Why it matters:** The "nonlinear regression functions" chapter (polynomials, logs, interactions between binary and continuous regressors) is the best textbook chapter on log-log versus log-linear interpretation; the time-series chapters cover distributed lags and HAC standard errors. Clear, intuitive, widely available in European libraries.
- **Use in course:** background (Session 1 for log specifications, Session 4 for dynamic causal effects); paid.

### Principles of Econometrics (5th ed.)
- **Source:** R. Carter Hill, William E. Griffiths and Guay C. Lim, Wiley, 2018, book (912 pp.)
- **Link:** https://www.wiley.com/en-us/Principles+of+Econometrics,+5th+Edition-p-9781119320944 and https://principlesofeconometrics.com/poe5/poe5.html (data; both confirmed via listing)
- **Why it matters:** More gentle and example-heavy than Wooldridge, with chapters on indicator variables, heteroskedasticity and time-series regression (lags, serial correlation, HAC errors). Data sets are downloadable in several formats, which makes it easy to port examples to Python.
- **Use in course:** background (alternative textbook for students needing more worked examples); paid.

### Multivariate Data Analysis (8th ed.)
- **Source:** Joseph F. Hair, William C. Black, Barry J. Babin and Rolph E. Anderson, Cengage, 2019, book (832 pp.)
- **Link:** https://www.cengageasia.com/TitleDetails/isbn/9781473756540 (confirmed via listing)
- **Why it matters:** The marketing-research classic; Ch. 5 "Multiple Regression" walks through design, assumptions, VIF thresholds, dummy coding and validation in the step-by-step style business students and reviewers expect. Software-neutral (no Python), and some rules of thumb (VIF cut-offs) are more conservative than current practice.
- **Use in course:** background (Ch. 5 as a checklist for the project report); paid.

### Discovering Statistics Using IBM SPSS Statistics (6th ed.)
- **Source:** Andy Field, SAGE, February 2024, book (1,144 pp.)
- **Link:** https://uk.sagepub.com/en-gb/eur/discovering-statistics-using-ibm-spss-statistics/book285130 (confirmed via listing)
- **Why it matters:** Ch. 11 (moderation and mediation with PROCESS, including a two-mediator example new in this edition) and Ch. 12 (categorical predictors and dummy coding) are the friendliest explanations for students with no maths background. SPSS-based, so use for concepts only.
- **Use in course:** background (students who need an intuitive explanation of interactions or dummy coding); paid.

### Statistical Rethinking (2nd ed.) with the PyMC port
- **Source:** Richard McElreath, CRC Press, 2020, book; PyMC port by the PyMC developers
- **Link:** https://github.com/pymc-devs/pymc-resources/tree/main/Rethinking_2 (confirmed via listing)
- **Why it matters:** Ch. 4 (linear regression, polynomials, splines), Ch. 5 (multiple regression, categorical variables, spurious association), Ch. 6 (causal diagrams, post-treatment bias) and Ch. 8 (interactions) give the Bayesian view students need before PyMC-Marketing in Session 3. The PyMC notebooks reproduce the code in Python.
- **Use in course:** Session 3 (background for Bayesian and hierarchical regression); book paid, notebooks free.

### Applied Regression Analysis and Generalized Linear Models (3rd ed.)
- **Source:** John Fox, SAGE, 2016 (published 2015), book
- **Link:** https://us.sagepub.com/en-us/nam/applied-regression-analysis-and-generalized-linear-models/book237254 (confirmed via listing)
- **Why it matters:** The reference for diagnostics: dummy-variable regression (Ch. 7), unusual and influential data (Ch. 11), non-normality, non-constant variance and non-linearity (Ch. 12), collinearity (Ch. 13). Graduate level; use for instructor preparation and for answering "is this outlier a problem?" questions.
- **Use in course:** background (Session 2 diagnostics); paid.

## Journal articles

**Linear regression and interpretation**

### A Tutorial on Teaching Data Analytics with Generative AI
- **Source:** Robert L. Bray, INFORMS Journal on Applied Analytics 55(4), 319-343, 2025, article
- **Link:** https://doi.org/10.1287/inte.2023.0053 (confirmed via listing; open preprint https://www.kellogg.northwestern.edu/faculty/bray/doc/chatgpt/chatgpt.pdf)
- **Why it matters:** A Kellogg MBA analytics course rebuilt around ChatGPT: custom GPTs that tutor students through linear, Poisson, logistic and ordered-logit regressions, students teaching each other the regression they learned from their GPT, and chat logs submitted as homework. The most concrete published model for AI-assisted regression teaching to business students.
- **Use in course:** background (instructor reading for course design; ideas for Session 1 lab and AI-assistant rules).

### A New Era of Learning: Considerations for ChatGPT as a Tool to Enhance Statistics and Data Science Education
- **Source:** Amanda R. Ellis and Emily Slade, Journal of Statistics and Data Science Education 31(2), 128-133, 2023, article
- **Link:** https://doi.org/10.1080/26939169.2023.2223609 (confirmed via ERIC listing EJ1395924)
- **Why it matters:** Short, practical piece on using ChatGPT to generate code, explain output and create practice data, with concrete prompts and warnings about plausible but wrong statistical answers. JSDSE has since opened a generative-AI collection (2025) worth monitoring.
- **Use in course:** background (instructor reading; supports the Session 1 "what AI assistants get wrong" segment).

### Generative AI and Marketing Education: What the Future Holds
- **Source:** Abhijit Guha, Dhruv Grewal and Stephen Atlas, Journal of Marketing Education 46(1), 6-17, 2024 (online December 2023), article
- **Link:** https://doi.org/10.1177/02734753231215436 (confirmed via listing)
- **Why it matters:** Survey of marketing educators, students and managers on how generative AI changes marketing teaching, including analytics tasks; useful for justifying an AI-assisted coding course design to a programme committee.
- **Use in course:** background.

### Elasticity benchmarks: price (Bijmolt, van Heerde and Pieters 2005) and advertising (Sethuraman, Tellis and Briesch 2011)
- **Source:** Bijmolt, van Heerde and Pieters, Journal of Marketing Research 42(2), 141-156, 2005; Sethuraman, Tellis and Briesch, Journal of Marketing Research 48(3), 457-471, 2011, articles (meta-analyses)
- **Link:** https://doi.org/10.1509/jmkr.42.2.141.62296 and https://doi.org/10.2307/23033851 (JSTOR DOI; both confirmed via listing)
- **Why it matters:** Mean price elasticity about -2.6 across 1,851 estimates; mean short-term advertising elasticity 0.12 and long-term 0.24, with moderators (country, product type, life-cycle stage, data interval). These are the benchmarks students should compare their log-log coefficients against, and both papers are themselves regressions with moderators.
- **Use in course:** Session 1 (benchmark slide for the Alpenglow elasticities; reading for interpreting log-log coefficients), Session 2 (advertising elasticity plausibility check).

**Non-linear effects**

### Thinking about U: Theorizing and testing U- and inverted U-shaped relationships in strategy research
- **Source:** Richard F. J. Haans, Constant Pieters and Zi-Lin He, Strategic Management Journal 37(7), 1177-1195, 2016, article
- **Link:** https://doi.org/10.1002/smj.2399 (confirmed via listing)
- **Why it matters:** The standard guide to quadratic terms: how to theorise them, the three-step test (sign, turning point inside the data range, slopes on both sides), and how moderators shift or flatten a U. Directly applicable to advertising wear-out and price-quality curves.
- **Use in course:** Session 2 (reading before saturation curves); paywalled, author copies circulate.

### Two Lines: A Valid Alternative to the Invalid Testing of U-Shaped Relationships With Quadratic Regressions
- **Source:** Uri Simonsohn, Advances in Methods and Practices in Psychological Science 1(4), 538-555, 2018, article (open access)
- **Link:** https://doi.org/10.1177/2515245918805755 (confirmed via listing)
- **Why it matters:** Shows that a significant quadratic term can appear when the true curve is merely concave (saturating), which is exactly the saturation-versus-wear-out confusion in MMM. Proposes the interrupted "two lines" test as a functional-form-free alternative.
- **Use in course:** Session 2 (short reading; good discussion point on why Hill curves and quadratics tell different stories).

### The Shape of Advertising Response Functions Revisited: A Model of Dynamic Probabilistic Thresholds
- **Source:** Demetrios Vakratsas, Fred M. Feinberg, Frank M. Bass and Gurumurthy Kalyanaram, Marketing Science 23(1), 109-119, 2004, article
- **Link:** https://doi.org/10.1287/mksc.1030.0035 (confirmed via listing)
- **Why it matters:** Marketing-science treatment of concave versus S-shaped advertising response, with thresholds. Gives theoretical grounding for the Session 2/3 Hill curve and the course's "shape uncertainty" lesson.
- **Use in course:** Session 2 (background reading for the instructor; excerpt for students).

### Your MMM is Broken: Identification of Nonlinear and Time-varying Effects in Marketing Mix Models
- **Source:** Ryan Dew, Nicolas Padilla and Anya Shchetkina, 2024, working paper (arXiv 2408.07678); authors (unverified)
- **Link:** https://ideas.repec.org/p/arx/papers/2408.07678.html (confirmed via listing)
- **Why it matters:** Shows that saturation and time-varying effects in MMM are hard to tell apart with typical weekly data, so different non-linear specifications fit equally well but imply different ROAS. Matches the course's own finding that saturation shape is weakly identified with 156 weeks.
- **Use in course:** Session 2 or 3 (advanced optional reading; supports caveat 2 in the course design).

**Moderation**

### Multiple Regression: Testing and Interpreting Interactions
- **Source:** Leona S. Aiken and Stephen G. West, SAGE, 1991, book (classic methods monograph)
- **Link:** https://us.sagepub.com/en-us/nam/multiple-regression/book3045 (unverified)
- **Why it matters:** Origin of the simple-slopes approach, centring advice and the plots of slopes at plus and minus one standard deviation that most published moderation analyses still follow. Cite as the classic, teach the modern refinements below.
- **Use in course:** background.

### Understanding Interaction Models: Improving Empirical Analyses
- **Source:** Thomas Brambor, William Roberts Clark and Matt Golder, Political Analysis 14(1), 63-82, 2006, article
- **Link:** https://doi.org/10.1093/pan/mpi014 (confirmed via listing; companion page https://mattgolder.com/interactions)
- **Why it matters:** The four-rule checklist: include all constitutive terms, do not read main-effect coefficients as unconditional effects, compute marginal effects with standard errors across the moderator, and plot them. Short and readable; the right text for "price elasticity depends on GDP per capita" models.
- **Use in course:** Session 1 (core reading for country-level moderation with Hofstede/GDP).

### Spotlights, Floodlights, and the Magic Number Zero: Simple Effects Tests in Moderated Regression
- **Source:** Stephen A. Spiller, Gavan J. Fitzsimons, John G. Lynch and Gary H. McClelland, Journal of Marketing Research 50(2), 277-288, 2013, article
- **Link:** https://doi.org/10.1509/jmr.12.0420 (confirmed via listing; author PDF https://stephenaspiller.com/assets/SpillerFitzsimonsLynchMcClelland2013.pdf)
- **Why it matters:** Marketing's reference for probing interactions: spotlight tests at meaningful moderator values, floodlight (Johnson-Neyman) regions otherwise, and why median splits are wrong. Simonsohn's working paper "GAMify Spotlight & Floodlight" (https://urisohn.com/sohn_files/papers/gamify.pdf) extends it to non-linear moderation.
- **Use in course:** Session 1 (reading; floodlight plot of the price effect across GDP or Hofstede scores as a lab extension, computable with marginaleffects or by hand in statsmodels).

### How Much Should We Trust Estimates from Multiplicative Interaction Models? Simple Tools to Improve Empirical Practice
- **Source:** Jens Hainmueller, Jonathan Mummolo and Yiqing Xu, Political Analysis 27(2), 163-192, 2019, article
- **Link:** https://doi.org/10.1017/pan.2018.46 (confirmed via listing)
- **Why it matters:** Replicates 46 published interactions and finds many rest on a linear-interaction assumption or on moderator values with no data. Proposes binning and kernel estimators (interflex package, R/Stata). Essential when the moderator is a country characteristic with only six countries, as in Alpenglow.
- **Use in course:** Session 1 (reading; caution that six countries cannot support a continuous moderator claim).

### Misleading Heuristics and Moderated Multiple Regression Models
- **Source:** Julie R. Irwin and Gary H. McClelland, Journal of Marketing Research 38(1), 100-109, 2001, article
- **Link:** https://doi.org/10.1509/jmkr.38.1.100.18835 (confirmed via listing)
- **Why it matters:** Explains which simple-regression habits fail once an interaction is added (reading lower-order coefficients as main effects, standardised coefficients, R-squared change logic). Marketing examples.
- **Use in course:** Session 1 (instructor background; one-slide summary for students).

### The mean-centring debate: Echambadi and Hess (2007); Iacobucci et al. (2016); McClelland et al. (2017)
- **Source:** Echambadi and Hess, Marketing Science 26(3), 438-445, 2007; Iacobucci, Schneider, Popovich and Bakamitsos, Behavior Research Methods 48(4), 1308-1317, 2016; McClelland, Irwin, Disatnik and Sivan, Behavior Research Methods 49, 394-402, 2017, articles
- **Link:** https://doi.org/10.1287/mksc.1060.0263 ; https://doi.org/10.3758/s13428-015-0624-x ; https://doi.org/10.3758/s13428-016-0785-2 (all confirmed via listing)
- **Why it matters:** Echambadi and Hess prove that centring changes neither precision nor fit in a moderated regression; Iacobucci et al. distinguish "micro" (helped by centring) from "macro" multicollinearity; McClelland et al. reply that multicollinearity is a red herring for moderators. Together they settle a question AI assistants routinely get wrong ("centre to fix the VIF").
- **Use in course:** Session 1 (multicollinearity segment; short reading or instructor background).

### The Difference Between "Significant" and "Not Significant" is not Itself Statistically Significant
- **Source:** Andrew Gelman and Hal Stern, The American Statistician 60(4), 328-331, 2006, article
- **Link:** https://doi.org/10.1198/000313006X152649 (confirmed via listing)
- **Why it matters:** Four pages that prevent the commonest cross-country error: "the elasticity is significant in Italy but not in Austria, so the markets differ". Motivates testing the interaction directly.
- **Use in course:** Session 1 (short reading tied to the country comparison exercise).

**Mediation**

### Reconsidering Baron and Kenny: Myths and Truths about Mediation Analysis
- **Source:** Xinshu Zhao, John G. Lynch and Qimei Chen, Journal of Consumer Research 37(2), 197-206, 2010, article
- **Link:** https://doi.org/10.1086/651257 (confirmed via listing)
- **Why it matters:** The marketing reference that replaced the causal-steps logic: only the indirect effect a x b matters, no total effect is required, and a decision tree classifies complementary, competitive and indirect-only mediation. Non-technical.
- **Use in course:** background (optional Session 1 extension, e.g. price affects sales via perceived quality or brand attitude).

### The Moderator-Mediator Variable Distinction in Social Psychological Research
- **Source:** Reuben M. Baron and David A. Kenny, Journal of Personality and Social Psychology 51(6), 1173-1182, 1986, article
- **Link:** https://doi.org/10.1037/0022-3514.51.6.1173 (confirmed via listing; PubMed https://pubmed.ncbi.nlm.nih.gov/3806354/)
- **Why it matters:** One of the most cited papers in social science and still the source of the moderator/mediator definitions; its causal-steps test is now discouraged (see Zhao et al., Hayes). Read for the definitions, not the procedure.
- **Use in course:** background.

### Asymptotic and resampling strategies for assessing and comparing indirect effects in multiple mediator models
- **Source:** Kristopher J. Preacher and Andrew F. Hayes, Behavior Research Methods 40(3), 879-891, 2008, article
- **Link:** https://doi.org/10.3758/BRM.40.3.879 (confirmed via listing)
- **Why it matters:** Established bootstrap confidence intervals for indirect effects and contrasts between mediators; the logic is easy to code in Python with a resampling loop over two statsmodels regressions.
- **Use in course:** background.

### An Index and Test of Linear Moderated Mediation
- **Source:** Andrew F. Hayes, Multivariate Behavioral Research 50(1), 1-22, 2015, article
- **Link:** https://doi.org/10.1080/00273171.2014.962683 (confirmed via listing)
- **Why it matters:** Defines the index of moderated mediation, the single test for whether an indirect effect differs across a moderator (for example, across countries or cultural clusters). The standard citation in conditional process papers.
- **Use in course:** background.

### A General Approach to Causal Mediation Analysis
- **Source:** Kosuke Imai, Luke Keele and Dustin Tingley, Psychological Methods 15(4), 309-334, 2010, article
- **Link:** https://doi.org/10.1037/a0020761 (confirmed via listing)
- **Why it matters:** Potential-outcomes definition of mediation (ACME, ADE), the sequential ignorability assumption and sensitivity analysis. Implemented in Python as `statsmodels.stats.mediation.Mediation` (https://www.statsmodels.org/stable/generated/statsmodels.stats.mediation.Mediation.html, confirmed via listing), so students can run it without R.
- **Use in course:** background (instructor reference for any project with a mediator).

### Meaningful Mediation Analysis: Plausible Causal Inference and Informative Communication
- **Source:** Rik Pieters, Journal of Consumer Research 44(3), 692-716, 2017, article
- **Link:** https://doi.org/10.1093/jcr/ucx081 (confirmed via listing)
- **Why it matters:** Reviews 166 JCR mediation analyses and asks for effect decomposition, effect sizes, difference tests and data sharing; also discusses when a mediation claim is causally plausible. The best bridge between PROCESS practice and causal thinking for marketers.
- **Use in course:** background.

### That's a Lot to Process! Pitfalls of Popular Path Models
- **Source:** Julia M. Rohrer, Paul Hünermund, Ruben C. Arslan and Malte Elson, Advances in Methods and Practices in Psychological Science 5(2), 2022, article (open access)
- **Link:** https://doi.org/10.1177/25152459221095827 (confirmed via listing)
- **Why it matters:** Shows with causal diagrams how PROCESS-style mediation and moderated mediation can be badly biased by mediator-outcome confounding; argues for explicit assumptions. Co-author Hünermund (CBS) is a good European name for a causal-inference guest slot.
- **Use in course:** background (instructor reading; critique to pair with Hayes).

### Theorizing, testing, and concluding for mediation in SCM research: Tutorial and procedural recommendations
- **Source:** Manus Rungtusanatham, Jason W. Miller and Kenneth K. Boyer, Journal of Operations Management 32(3), 99-113, 2014, article (note: JOM, not Journal of Supply Chain Management)
- **Link:** https://doi.org/10.1016/j.jom.2014.01.002 (confirmed via listing)
- **Why it matters:** Business-school tutorial with eight procedural recommendations, from theorising the mechanism to reporting bootstrapped indirect effects. Useful template for student projects outside consumer psychology.
- **Use in course:** background.

**Dummy coding and categorical predictors**

### Negative Consequences of Dichotomizing Continuous Predictor Variables
- **Source:** Julie R. Irwin and Gary H. McClelland, Journal of Marketing Research 40(3), 366-371, 2003, article
- **Link:** https://doi.org/10.1509/jmkr.40.3.366.19237 (confirmed via listing)
- **Why it matters:** The dichotomising paper (often confused with their 2001 paper): median splits lose power and can create spurious effects. Students turning GDP or Hofstede scores into "high/low" dummies need this.
- **Use in course:** Session 1 (short reading or one slide).

### A Tutorial on Testing, Visualizing, and Probing an Interaction Involving a Multicategorical Variable in Linear Regression Analysis
- **Source:** Andrew F. Hayes and Amanda K. Montoya, Communication Methods and Measures 11(1), 1-30, 2017, article
- **Link:** https://doi.org/10.1080/19312458.2016.1271116 (confirmed via listing)
- **Why it matters:** Explains indicator, sequential and Helmert coding of a multi-level factor and how coding choice changes what each interaction coefficient means. Directly relevant to "country (six levels) x price" models; translate to patsy `C(country, Treatment('AT'))` or `Sum` coding.
- **Use in course:** Session 1 (instructor background; lab note on coding choices).

### How to capitalize on a priori contrasts in linear (mixed) models: A tutorial
- **Source:** Daniel J. Schad, Shravan Vasishth, Sven Hohenstein and Reinhold Kliegl, Journal of Memory and Language 110, 104038, 2020, article (open access)
- **Link:** https://doi.org/10.1016/j.jml.2019.104038 (unverified)
- **Why it matters:** The clearest modern tutorial on treatment, sum (effect), sliding-difference and Helmert contrasts, with the hypothesis matrix behind each. Written for R, but the contrast logic is identical in patsy and formulaic.
- **Use in course:** background (instructor reference for effect coding of countries).

**Assumptions, diagnostics and robust inference**

### Collinearity, Power, and Interpretation of Multiple Regression Analysis
- **Source:** Charlotte H. Mason and William D. Perreault, Journal of Marketing Research 28(3), 268-280, 1991, article
- **Link:** https://doi.org/10.2307/3172863 (JSTOR DOI, confirmed via listing; open copy at https://cdr.lib.unc.edu/downloads/028715161)
- **Why it matters:** Marketing simulation showing that fears about collinearity are often exaggerated and that sample size, R-squared and effect size matter as much as VIF. A healthy counterweight to mechanical VIF cut-offs in MMM.
- **Use in course:** Session 1 (multicollinearity), Session 2 (VIF in MMM diagnostics).

### Some heteroskedasticity-consistent covariance matrix estimators with improved finite sample properties
- **Source:** James G. MacKinnon and Halbert White, Journal of Econometrics 29(3), 305-325, 1985, article
- **Link:** https://doi.org/10.1016/0304-4076(85)90158-7 (confirmed via listing)
- **Why it matters:** Source of HC1, HC2 and HC3; shows HC3 performs best in small samples. Explains the `cov_type="HC3"` option in statsmodels and why it is a sensible default for small weekly datasets.
- **Use in course:** Session 2 (background for robust SEs in the lab).

### How Robust Standard Errors Expose Methodological Problems They Do Not Fix, and What to Do About It
- **Source:** Gary King and Margaret E. Roberts, Political Analysis 23(2), 159-179, 2015, article
- **Link:** https://doi.org/10.1093/pan/mpu015 (confirmed via listing)
- **Why it matters:** If classical and robust standard errors differ a lot, the model is misspecified and the coefficients may be wrong too; robust errors are a diagnostic, not a cure. A crucial correction to "always add robust SEs" advice from AI assistants.
- **Use in course:** Session 2 (reading; compare classical and HC3 SEs as a diagnostic step).

### Clustered standard errors: Cameron and Miller (2015) and Abadie, Athey, Imbens and Wooldridge (2023)
- **Source:** A. Colin Cameron and Douglas L. Miller, Journal of Human Resources 50(2), 317-372, 2015; Alberto Abadie, Susan Athey, Guido W. Imbens and Jeffrey M. Wooldridge, Quarterly Journal of Economics 138(1), 1-35, 2023, articles
- **Link:** https://doi.org/10.3368/jhr.50.2.317 (open copy https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf) and https://doi.org/10.1093/qje/qjac038 (both confirmed via listing)
- **Why it matters:** Cameron and Miller is the practitioner guide (when to cluster, few-cluster problems, wild bootstrap); Abadie et al. explain that clustering is a design question (sampling or assignment), not a reflex. With six countries the few-clusters warning is directly relevant.
- **Use in course:** Session 3 (background for panel OLS with country fixed effects; why not to cluster on six countries naively).

**Time-series regression**

### A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix
- **Source:** Whitney K. Newey and Kenneth D. West, Econometrica 55(3), 703-708, 1987, article
- **Link:** https://doi.org/10.2307/1913610 (confirmed via listing)
- **Why it matters:** The HAC (Newey-West) estimator behind `cov_type="HAC"` in statsmodels; the correct fix for autocorrelated residuals in weekly sales regressions when the model is otherwise sound.
- **Use in course:** Session 2 and Session 4 (background; one slide on HAC errors with `maxlags`).

### The Persistence of Marketing Effects on Sales, and the 2024 update on persistence modelling
- **Source:** Marnik G. Dekimpe and Dominique M. Hanssens, Marketing Science 14(1), 1-21, 1995; and "Persistence Modeling in Marketing: Descriptive, Predictive, and Normative Uses", Australasian Marketing Journal, 2024, articles
- **Link:** https://doi.org/10.1287/mksc.14.1.1 and https://doi.org/10.1177/14413582231222311 (both confirmed via listing)
- **Why it matters:** The founding paper of persistence modelling (unit roots, VAR, impulse responses) using advertising for a home-improvement chain, plus the authors' own 30-year retrospective. Explains why short-run regression coefficients understate long-run marketing effects.
- **Use in course:** Session 2 (background on carryover), Session 4 (reading on long-term effects).

### Modeling Marketing Dynamics by Time Series Econometrics
- **Source:** Koen Pauwels, Imran Currim, Marnik G. Dekimpe, Eric Ghysels, Dominique M. Hanssens, Natalie Mizik and Prasad Naik, Marketing Letters 15(4), 167-183, 2004, article
- **Link:** https://doi.org/10.1007/s11002-005-0455-0 (confirmed via listing)
- **Why it matters:** Short overview of the time-series toolkit for marketing (unit-root tests, VAR/VECM, impulse response, state-space models) by the leading names, with guidance on which tool answers which managerial question.
- **Use in course:** Session 4 (reading).

### Dynamic Models for Dynamic Theories: The Ins and Outs of Lagged Dependent Variables
- **Source:** Luke Keele and Nathan J. Kelly, Political Analysis 14(2), 186-205, 2006, article
- **Link:** https://www.cambridge.org/core/journals/political-analysis/article/abs/dynamic-models-for-dynamic-theories-the-ins-and-outs-of-lagged-dependent-variables/F4AB52C3E9964515825D1E6F20C9EA42 (confirmed via listing); DOI 10.1093/pan/mpj006 (unverified)
- **Why it matters:** When a lagged dependent variable is appropriate (dynamic theory, Koyck-style carryover) and when it biases estimates (autocorrelated errors). Koyck lags are the regression form of geometric adstock, so this links Session 2 to Session 4.
- **Use in course:** Session 4 (background reading).

### Lagged Outcomes, Lagged Predictors, and Lagged Errors: A Clarification on Common Factors
- **Source:** Scott J. Cook and Clayton Webb, Political Analysis 29(4), 561-569, 2021, article
- **Link:** https://doi.org/10.1017/pan.2020.53 (confirmed via listing)
- **Why it matters:** Recent clarification of the lagged-dependent-variable debate: a model with lagged outcome, lagged predictors and autocorrelated errors (common-factor restriction) and what each specification assumes. No "Kelly 2020" paper on lagged dependent variables could be found; this is the closest recent paper and probably the intended one, alongside Keele and Kelly 2006.
- **Use in course:** background (instructor reference for Session 4 specification choices).

## Reports

### What's in a p? Reassessing best practices for conducting and reporting hypothesis-testing research
- **Source:** Klaus E. Meyer, Arjen van Witteloostuijn and Sjoerd Beugelsdijk, Journal of International Business Studies 48, 535-551, 2017, editorial (methods guidelines)
- **Link:** https://doi.org/10.1057/s41267-017-0078-8 (confirmed via listing)
- **Why it matters:** JIBS's own reporting standard for regression-based IB research: drop significance stars, report exact p-values, confidence intervals and effect sizes, show robustness and discuss economic significance. The right reporting norm for an international marketing course.
- **Use in course:** Session 5 (reporting checklist for project pitches and reports); Session 1 (how to report an elasticity).

### Hypothesis-testing research in international business: progress, pitfalls, and a way forward
- **Source:** Jelena Cerar, B. Sebastian Reiche and Phillip C. Nell, Journal of International Business Studies 57(7), 1115-1129, 2026, article (open access; follow-up audit of the 2017 guidelines)
- **Link:** https://link.springer.com/article/10.1057/s41267-026-00859-6 (confirmed via listing)
- **Why it matters:** Audits all significance-testing articles in JIBS and JWB from 2012 to 2024: rigour has improved, but reporting of standard errors, confidence intervals, effect sizes and outlier treatment still lags, with signs of p-hacking. Co-author Nell is at WU Vienna, which makes him an obvious local guest for a reporting-standards slot.
- **Use in course:** Session 5 (reading); guest-talk angle (WU colleague).

### The ASA Statement on p-Values (2016) and "Moving to a World Beyond p < 0.05" (2019)
- **Source:** Ronald L. Wasserstein and Nicole A. Lazar, The American Statistician 70(2), 129-133, 2016; Wasserstein, Allen L. Schirm and Lazar, The American Statistician 73(sup1), 1-19, 2019, official statement and editorial
- **Link:** https://doi.org/10.1080/00031305.2016.1154108 and https://doi.org/10.1080/00031305.2019.1583913 (both confirmed via listing; open access)
- **Why it matters:** Six principles on what a p-value does and does not mean, followed by the "ATOM" advice (accept uncertainty, be thoughtful, open, modest). Short enough for students; underpins how the course reports regression output.
- **Use in course:** Session 1 (two-page reading on interpreting coefficients and p-values).

### Journal Article Reporting Standards for Quantitative Research (JARS-Quant)
- **Source:** Mark Appelbaum, Harris Cooper, Rex B. Kline, Evan Mayo-Wilson, Arthur M. Nezu and Stephen M. Rao, American Psychologist 73(1), 3-25, 2018, APA task force report
- **Link:** https://doi.org/10.1037/amp0000191 and https://apastyle.apa.org/jars/quantitative (both confirmed via listing)
- **Why it matters:** The APA reporting checklist used by consumer-behaviour journals: report estimates with confidence intervals, effect sizes, assumption checks, handling of outliers and missing data, and full model specifications, including for mediation and moderation models.
- **Use in course:** Session 5 (checklist for the written project report).

### NIST/SEMATECH e-Handbook of Statistical Methods, Chapter 4: Process Modeling
- **Source:** National Institute of Standards and Technology, online handbook (maintained since 2003, updated 2012), government report
- **Link:** https://www.itl.nist.gov/div898/handbook/pmd/pmd.htm (host blocked; section pages such as https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd141.htm confirmed via listing)
- **Why it matters:** Free, authoritative and plain-language chapter on linear, non-linear and weighted least squares, model validation with residual plots, and lack-of-fit testing. Engineering examples, but the residual-diagnostics pages are the best free visual reference.
- **Use in course:** Session 2 (diagnostics reference); free.

### Google media mix modelling technical reports: Jin et al. (2017) and Chan and Perry (2017)
- **Source:** Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan and Jim Koehler, "Bayesian Methods for Media Mix Modeling with Carryover and Shape Effects"; David Chan and Michael Perry, "Challenges and Opportunities in Media Mix Modeling", Google Inc., 2017, technical reports
- **Link:** https://research.google.com/pubs/archive/46001.pdf and https://services.google.com/fh/files/misc/challenges_and_opportunities_in_media_mix_modeling.pdf (both confirmed via listing)
- **Why it matters:** Jin et al. define the adstock and Hill-saturation regression that PyMC-Marketing and Meridian build on; Chan and Perry explain, in regression language, why MMM struggles (collinear channels, endogenous budgets, limited data). Together they turn the regression topics of Session 1 into the MMM of Sessions 2 and 3.
- **Use in course:** Session 2 (Jin et al. as core reading), Session 3 (Chan and Perry as discussion reading); free.

## Teaching cases and course examples

### Linear Regression (HBS background note 9-622-100)
- **Source:** Iavor I. Bojinov, Michael Parzen and Paul J. Hamilton, Harvard Business School, 2022, revised 6 January 2025, background note (20 pp.)
- **Link:** Harvard Business Publishing, product 9-622-100 (PDF licensed to the instructor; distribute through Canvas only, never in a public repository)
- **Why it matters:** A short, managerial introduction: correlation and its rule of thumb, correlation versus causation, the correlation matrix, simple regression and least squares, inference for coefficients, R² and residual standard error, prediction intervals, multiple regression, the overall F-test and dummy variables, with example prompts for doing each step with generative AI tools.
- **Use in course:** Session 1 core reading for students without a statistics background; the AI-prompt examples fit the course's "the AI writes, you check" rule.

### ISLP Chapter 3 lab and Stanford Online "Statistical Learning with Python"
- **Source:** Hastie, Tibshirani and Taylor (Stanford), 2023 onwards, course (edX, 11 weeks) with Jupyter labs
- **Link:** https://online.stanford.edu/courses/sohs-ystatslearningp-statistical-learning-python (confirmed via listing); lab https://github.com/intro-stat-learning/ISLP_labs/blob/main/Ch03-linreg-lab.ipynb (repository fetched)
- **Why it matters:** The Advertising data set (sales vs TV, radio, newspaper budgets) is the canonical classroom example of a marketing regression with an interaction (TV x radio synergy) and diminishing returns; the lab is maintained Python (statsmodels, ISLP helpers) and the lecture videos are free to audit.
- **Use in course:** Session 1 (warm-up lab before the Alpenglow panel; videos as optional preparation); free to audit.

### Pilgrim Bank (A): Customer Profitability
- **Source:** Frances X. Frei and Dennis Campbell, Harvard Business School, 2001 (revised later), case with data spreadsheet
- **Link:** https://www.hbs.edu/faculty/Pages/item.aspx?num=28546 and https://www.thecasecentre.org/products/view?id=80157 (both confirmed via listing)
- **Why it matters:** Classic data case: about 30,000 customers, does online banking raise profitability? Students move from a naive comparison to multiple regression with age, income, tenure and district dummies and see the online effect shrink. Teaches confounding, dummy coding and low R-squared interpretation in a decision setting. Pilgrim Bank (B) adds retention (logistic regression).
- **Use in course:** Session 1 (case discussion; data easily loaded in Python); paid (HBP academic price, about USD 5 to 10 per student).

### Store24 (A): Managing Employee Retention
- **Source:** Frances X. Frei and Dennis Campbell, Harvard Business School case 602-096, 2001 (revised October 2017), case with store-level data
- **Link:** https://hbsp.harvard.edu/product/602096-PDF-ENG (confirmed via listing)
- **Why it matters:** Store-level profit regressed on manager and crew tenure, competition, population and visibility; the natural extension is a non-linear (diminishing) tenure effect and a tenure x location interaction. Five pages, quick to teach.
- **Use in course:** Session 1 (alternative or second case on interpretation and non-linear terms); paid.

### Multiple Regression and Marketing-Mix Models (Darden technical note)
- **Source:** Darden Business Publishing, University of Virginia, technical note (used in the Darden elective "Big Data in Marketing"); authors and product number (unverified)
- **Link:** https://store.darden.virginia.edu/multiple-regression-and-marketing-mix-models (confirmed via listing; host blocked)
- **Why it matters:** A business-school note that moves from simple regression to multiple regression for marketing-mix models, with particular attention to omitted-variable bias in marketing coefficients. Matches the course's own "Session 1 elasticities are attenuated because media are omitted" lesson.
- **Use in course:** Session 1 to 2 (pre-reading bridging regression foundations and MMM); paid.

### Python for Marketing Research and Analytics notebooks
- **Source:** Schwarz, Chapman and Feit, 2020 onwards, GitHub repository of Colab notebooks and data
- **Link:** https://github.com/python-marketing-research/python-marketing-research-1ed (fetched; Apache-2.0)
- **Why it matters:** Ready-made, marketing-specific Python labs: Chapter 7 amusement-park satisfaction drivers (OLS, standardised coefficients, factor coding, interactions), Chapter 8 collinearity and logistic regression. Simulated data, so no licensing issues; can be ported to Quarto in Positron.
- **Use in course:** Session 1 (backup lab or homework); free.

### Linear Regression in Python (QuantEcon)
- **Source:** Thomas J. Sargent and John Stachurski (QuantEcon), lecture in "Intermediate Quantitative Economics with Python", continuously updated, course page
- **Link:** https://python.quantecon.org/ols.html (host blocked); source fetched at https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/ols.md
- **Why it matters:** Clear, polished walk-through of OLS in statsmodels and IV with linearmodels (Acemoglu-Johnson-Robinson institutions data, with continent dummies), including the matrix algebra for those who want it. Good model of a Jupyter Book/MyST lecture format similar to Quarto.
- **Use in course:** Session 1 (optional reading on omitted-variable bias and endogeneity); free.

### Data 100: Principles and Techniques of Data Science (UC Berkeley)
- **Source:** UC Berkeley Data 100 teaching team, every semester (Fall 2026 site live), course notes and labs
- **Link:** https://ds100.org/ (course site, confirmed via listing) and https://github.com/ds-100/course-notes (fetched; BSD-3-Clause)
- **Why it matters:** Python-first lectures and labs on OLS, feature engineering (one-hot encoding, polynomial features), bias-variance and inference for regression using pandas, statsmodels and scikit-learn. Shows how a large course teaches dummy encoding and non-linear features to non-statisticians.
- **Use in course:** background (instructor template for labs and auto-checked exercises); free.

### Statistical forecasting: notes on regression and time series analysis (Duke Decision 411)
- **Source:** Robert Nau, Fuqua School of Business, Duke University, course notes (online since the 2000s, last major revision about 2019)
- **Link:** https://people.duke.edu/~rnau/411home.htm (host blocked; confirmed via listing with https://people.duke.edu/~rnau/Decision411CoursePagetest.html)
- **Why it matters:** MBA-level notes that remain among the best plain-language explanations of regression for forecasting: transformations, dummy variables for seasons and events, residual autocorrelation, lags and ARIMA, with a weekly beer-sales example across 2,000 stores. Software is Statgraphics, so concepts only.
- **Use in course:** Session 4 (reading on regression for forecasting, seasonal dummies and lags); free.

### COMET: Dummy Variables and Interactions notebooks (UBC Economics)
- **Source:** UBC Vancouver School of Economics, COMET project, 2022 onwards, open notebooks
- **Link:** https://comet.arts.ubc.ca/docs/5_Research/econ490-r/12_Dummy.html (confirmed via listing) and https://github.com/ubcecon/comet-project (fetched)
- **Why it matters:** Open, well-paced notebooks on creating dummies from multi-category variables, interpreting their coefficients and interacting dummies with continuous variables, plus a "good regression practices" notebook. Mainly R and Stata; Python coverage could not be confirmed.
- **Use in course:** background (template for a short dummy-coding notebook in Python); free.

### Regression and Other Stories in Python (Bambi port)
- **Source:** Bambi developers (Ravin Kumar, Tomás Capretto, Osvaldo Martin and contributors), 2020 onwards, GitHub notebooks
- **Link:** https://github.com/bambinos/Bambi_resources/tree/master/ROS (fetched) and announcement https://statmodeling.stat.columbia.edu/2020/08/09/regression-and-other-stories-translated-into-python/
- **Why it matters:** Python versions of ROS examples (Earnings, KidIQ, ElectionsEconomy, Residuals, Rsquared and others) with Bambi formulas, which use the same syntax as statsmodels and lead naturally into PyMC. Coverage is partial (18 example folders).
- **Use in course:** Session 1 (worked examples on interpretation), Session 3 (bridge to Bayesian regression); free.

### A Note on the Marketing Analytics Course at Darden
- **Source:** Darden Business Publishing, University of Virginia, technical note describing a second-year MBA elective; authors and year (unverified)
- **Link:** https://www.thecasecentre.org/programmeAdmin/products/view?id=88638 (confirmed via listing)
- **Why it matters:** Describes a three-module marketing analytics elective (product analytics, customer analytics, measuring return on marketing) built on regression and experiments with large marketing databases. Useful benchmark for the course's own structure.
- **Use in course:** background (course-design benchmark); paid.

## Gaps and caveats

Almost every publisher and course host was blocked by the proxy (Wiley, Springer, INFORMS, SAGE, Cambridge, OUP, otexts.com, statlearning.com, theeffectbook.net, quantecon.org, duke.edu, nist.gov, arxiv.org, Darden and HBP stores), and the Consensus tool was out of quota, so DOIs and bibliographic details come from search listings rather than fetched landing pages; GitHub repositories (ISLP labs, Coding for Economists, Facure, Chapman/Feit notebooks, Bambi ROS port, QuantEcon source, Data 100 notes, COMET) were fetched directly. Specifically unverified: the Aiken and West SAGE URL, the Schad et al. (2020) DOI, the Keele and Kelly DOI string, the authors of the "Your MMM is Broken" paper, the authors and product numbers of the two Darden notes, chapter numbers in the Python edition of FPP and in Stock and Watson's 4th edition, and whether the free web version of The Effect already shows the 2nd edition. The requested "Kelly 2020" paper on lagged dependent variables could not be found; Keele and Kelly (2006) and Cook and Webb (2021) are listed instead, with Wilkins (2018, Political Science Research and Methods) as a further option. No peer-reviewed article on teaching regression specifically with Python in the Journal of Marketing Education or DSJIE was found; DSJIE regression pieces (Murray and Wilson 2021, Pinder 2013) use R and Excel, so Bray (2025) and Ellis and Slade (2023) are the closest matches, and the JSDSE 2025 generative-AI collection should be checked for newer items. No public Darden or HBS case with a full marketing-mix data set taught in Python was found; Pilgrim Bank and Store24 are not marketing-mix cases but are the most widely taught regression cases, and the Darden MMM note is the closest marketing fit. Hanssens, Parsons and Schultz's "Market Response Models" (2nd ed., 2001) and Mazzocchi's "Statistics for Marketing and Consumer Research" (SAGE, 2008) are relevant marketing texts but are older and were left out of the ranked list. Paywalls: Hayes, Wooldridge, Stock and Watson, Hill et al., Hair et al., Field, Fox, McElreath, the HBS and Darden cases, and most journal articles need WU library access; ISLP, ROS, FPP Pythonic, The Effect (online), Coding for Economists, UPfIE, Facure, Simonsohn 2018, Rohrer et al. 2022, Cerar et al. 2026, the ASA statements and the Google reports are free.
