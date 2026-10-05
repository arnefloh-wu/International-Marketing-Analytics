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
