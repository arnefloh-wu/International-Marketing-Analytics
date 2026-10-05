### Software (18)
<table fit-page-width="true" header-row="true">
	<tr>
		<td>Kategorie</td>
		<td>Titel / Name</td>
		<td>Autor / Quelle / Firma</td>
		<td>Link</td>
		<td>Notiz</td>
		<td>Verwendung im Kurs</td>
		<td>Status</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>statsmodels (formula API, OLS/WLS/GLS, robust covariance, diagnostics)</td>
		<td>statsmodels developers (Josef Perktold, Kevin Sheppard and others), 2009 to 2026, software. Version 0.15.0, released 27 August 2026, BSD-3-Clause, Python 3.10 or later.</td>
		<td>[https://pypi.org/project/statsmodels/](https://pypi.org/project/statsmodels/)</td>
		<td>The reference for teaching regression in Python: smf.ols("np.log(sales) \~ np.log(price) + C(country) + promo:C(country)", df).fit(cov_type="HC3") gives R-style output, cov_type="cluster" and "HAC" (Newey-West), variance_inflation_factor, het_breuschpagan, acorr_breusch_godfrey, OLSInfluence (Cook's distance, leverage), plot_regress_exog, and statsmodels.stats.mediation.Mediation. Release 0.15 abstracts the formula engine so either patsy or formulaic can be the backend and accepts polars DataFrames directly.</td>
		<td>sessions 1 to 4 lab workhorse (elasticity models, MMM OLS, diagnostics, HAC errors); pin 0.15 in requirements.txt. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>statsmodels.tsa (SARIMAX, ARDL, distributed lags)</td>
		<td>statsmodels developers, part of statsmodels 0.15.0 (27 August 2026), software.</td>
		<td>[https://github.com/statsmodels/statsmodels/tree/main/examples/notebooks](https://github.com/statsmodels/statsmodels/tree/main/examples/notebooks)</td>
		<td>SARIMAX(endog, exog=...) is regression with ARIMA errors (ARIMAX), ARDL and UECM estimate distributed-lag models of advertising carry-over, seasonal_decompose/STL and acf/pacf plots diagnose residual autocorrelation; 0.15 adds Diebold-Mariano and Pesaran-Timmermann forecast tests.</td>
		<td>session 2 (residual autocorrelation in the MMM, distributed lags as a bridge to adstock) and session 4 lab (forecast baseline). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>PyFixest</td>
		<td>Alexander Fischer, Styfen Schär and the py-econometrics team, 2023 to 2026, software. Version 0.60.0, 11 June 2026, MIT.</td>
		<td>[https://pypi.org/project/pyfixest/](https://pypi.org/project/pyfixest/)</td>
		<td>Port of R's fixest: pf.feols("log_sales \~ log_price \| country + week", data=df, vcov=\{"CRV1": "country"\}) with fast high-dimensional fixed effects, IV and Poisson, wild cluster bootstrap (important with only 6 to 8 countries), randomisation inference, DiD and event-study estimators, multiple-estimation syntax, and etable() regression tables rendered with Great Tables. Integrates with marginaleffects.</td>
		<td>session 3 (country and week fixed effects), session 4 (DiD on the geo-lift data). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>marginaleffects (Python)</td>
		<td>Vincent Arel-Bundock and contributors, 2023 to 2026, software. Version 0.6.1, 5 July 2026, GPL-3.0-or-later, Python 3.12 or later. The Python package now lives in the joint R/Python repository (the old pymarginaleffects repo was archived on 15 August 2026).</td>
		<td>[https://pypi.org/project/marginaleffects/](https://pypi.org/project/marginaleffects/)</td>
		<td>One consistent grammar (predictions, comparisons, slopes, hypotheses, plot_slopes) for interpreting interactions and non-linear terms: conditional slopes of price at each level of a cultural moderator, average marginal effects, contrasts between countries, delta-method or bootstrap intervals. Works on statsmodels formula models and pyfixest. The companion book \*Model to Meaning\* (CRC Press, 2026) is free online.</td>
		<td>session 1 (interpreting an interaction with a Hofstede moderator), session 2 (slopes of non-linear response curves). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>linearmodels</td>
		<td>Kevin Sheppard, 2017 to 2025, software. Version 7.0, 21 October 2025, NCSA licence.</td>
		<td>[https://pypi.org/project/linearmodels/](https://pypi.org/project/linearmodels/)</td>
		<td>PanelOLS with entity and time effects and clustered covariance, RandomEffects, BetweenOLS, FirstDifferenceOLS, IV2SLS/IVGMM (price endogeneity), and a compare() table. Needs a (entity, time) MultiIndex, which is a useful lesson in panel data structure.</td>
		<td>session 3 lab (panel OLS with country fixed effects, as named in the course design). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>formulaic and patsy (formulas, dummy and effect coding)</td>
		<td>formulaic: Matthew Wardrop, version 1.2.2, 2 June 2026, MIT. patsy: Nathaniel Smith, now maintained by Wardrop and Tomás Capretto, version 1.0.3, 29 August 2026, BSD-2.</td>
		<td>[https://pypi.org/project/formulaic/](https://pypi.org/project/formulaic/)</td>
		<td>These build the design matrix behind every formula: C(country, Treatment(reference="DE")), C(region, Sum) for effect (deviation) coding, Helmert, polynomial contrasts, bs()/cr() splines and I(price\*\*2). The patsy README says it is no longer actively developed and recommends migrating to formulaic, which statsmodels 0.15 now supports as a backend.</td>
		<td>session 1 (dummy vs effect coding of countries and seasons); background for the formula syntax students and AI assistants generate. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>scikit-learn (linear models, splines, pipelines)</td>
		<td>scikit-learn developers (Inria and community), 2007 to 2026, software. Version 1.9.1, 10 September 2026, BSD-3-Clause, Python 3.11 or later.</td>
		<td>[https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)</td>
		<td>LinearRegression, Ridge (the estimator inside Meta's Robyn MMM), HuberRegressor, SplineTransformer and PolynomialFeatures for non-linear effects, OneHotEncoder(drop="first") for dummies, Pipeline, TimeSeriesSplit for rolling-origin evaluation. No p-values or standard errors, which is a teachable contrast with statsmodels (prediction vs inference).</td>
		<td>session 1 (out-of-sample fit), session 2 (ridge, holdout), session 4 (time-series cross-validation). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>pingouin</td>
		<td>Raphael Vallat, 2018 to 2026, software. Version 0.7.0, 26 September 2026, GPL-3.0, Python 3.11 or later.</td>
		<td>[https://pypi.org/project/pingouin/](https://pypi.org/project/pingouin/)</td>
		<td>pg.mediation_analysis(data, x, m, y, covar, n_boot, seed) returns a tidy table of a, b, total, direct and indirect paths with bias-corrected bootstrap intervals and supports parallel mediators; pg.linear_regression gives tidy OLS output with relative importance. No dedicated moderation function: moderation is a product term in linear_regression or statsmodels.</td>
		<td>session 1 or background (simple mediation demo, e.g. advertising to brand attitude to sales). Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>PyProcessMacro (Python PROCESS)</td>
		<td>Quentin André, 2017 to 2026, software. Version 2.2.0, 29 September 2026, MIT (distributed with Andrew Hayes's permission, not endorsed by him), Python 3.11 or later. Revived in September 2026 after years without releases.</td>
		<td>[https://pypi.org/project/pyprocessmacro/](https://pypi.org/project/pyprocessmacro/)</td>
		<td>Reimplements all PROCESS models 1 to 76 (moderation, mediation, moderated mediation, serial mediation with model 6), tested against PROCESS 2.16 and, for the 42 models still defined, PROCESS for R 5.0; 2.2 adds multicategorical X and moderators (indicator, Helmert, effect coding), percentile spotlight values as in PROCESS 3+, negative binomial outcomes, tidy()/glance() outputs and to_statsmodels(). Note that its defaults follow PROCESS 2; percent=True, spotlight="percentiles" reproduces PROCESS 3 to 5.</td>
		<td>background and optional lab for students who know PROCESS from SPSS courses; useful when a thesis supervisor expects PROCESS model numbers. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>pyGAM</td>
		<td>Daniel Servén Marín, Charlie Brummitt and contributors, 2018 to 2025, software. Version 0.12.0, 18 December 2025, Apache-2.0.</td>
		<td>[https://pypi.org/project/pygam/](https://pypi.org/project/pygam/)</td>
		<td>Generalised additive models (LinearGAM(s(0) + f(1) + te(2, 3))) with penalised splines, factor terms, tensor interactions, monotonic and concave constraints and partial-dependence plots: a data-driven way to show students what a saturating spend-response curve looks like before imposing Hill or logistic forms.</td>
		<td>session 2 (exploring the shape of the response curve). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Bambi</td>
		<td>Tomás Capretto, Ravin Kumar, Osvaldo Martin and contributors (PyMC ecosystem), 2020 to 2026, software. Version 0.21.0, 10 September 2026, MIT, Python 3.12 or later.</td>
		<td>[https://pypi.org/project/bambi/](https://pypi.org/project/bambi/)</td>
		<td>Bayesian regression with R-style formulas, including hierarchical terms (1 + log_price \| country); its interpret module (plot_predictions, plot_comparisons, plot_slopes) is modelled on marginaleffects. A gentle step from OLS to the partial pooling used in PyMC-Marketing.</td>
		<td>session 3 (partial pooling of elasticities across countries before PyMC-Marketing). Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>DoWhy and CausalML (causal mediation)</td>
		<td>DoWhy: PyWhy (originally Microsoft Research), version 0.14, 8 November 2025, MIT. CausalML: Uber, version 0.17.0, 4 July 2026, Apache-2.0.</td>
		<td>[https://github.com/py-why/dowhy](https://github.com/py-why/dowhy)</td>
		<td>DoWhy estimates natural direct and natural indirect effects from an explicit causal graph (and its GCM module quantifies causal influence), which shows students that mediation needs causal assumptions, not just a product of coefficients. CausalML focuses on uplift and heterogeneous treatment effects for marketing campaigns.</td>
		<td>background; session 4 discussion of experiments vs observational estimates. Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>semopy</td>
		<td>Georgy Meshcheryakov and Anastasia Igolkina, 2019 to 2024, software. Version 2.3.11, 4 January 2024, licence not stated on PyPI.</td>
		<td>[https://pypi.org/project/semopy/](https://pypi.org/project/semopy/)</td>
		<td>lavaan-style SEM syntax in Python (attitude \~ a\*ad; sales \~ b\*attitude + c\*ad; ind := a\*b), so mediation with latent constructs (brand attitude measured by several items) can be estimated. No release since January 2024, so treat as stable but low-maintenance.</td>
		<td>background only (thesis students with survey data). Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>StatsForecast and sktime (time-series regression and forecasting)</td>
		<td>StatsForecast: Nixtla, version 2.1.1, 16 July 2026, Apache-2.0. sktime: sktime community, version 1.2.0, 22 September 2026, BSD-3-Clause. pmdarima 2.1.1 (17 November 2025, MIT) as an older auto-ARIMA option.</td>
		<td>[https://pypi.org/project/statsforecast/](https://pypi.org/project/statsforecast/)</td>
		<td>StatsForecast fits AutoARIMA (with exogenous regressors, i.e. ARIMAX), ETS and seasonal baselines quickly across many series (one per country) and is the engine used in the Python edition of \*Forecasting: Principles and Practice\*; sktime offers a scikit-learn-like interface with reduction (regression on lags) and pipelines.</td>
		<td>session 4 lab (country-level forecasts, rolling-origin evaluation). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Regression tables: summary_col, PyFixest etable, stargazer and Great Tables</td>
		<td>statsmodels summary_col (0.15.0); PyFixest etable (0.60.0); stargazer (Pietro Battiston and Matthew Burke), version 0.0.7, 4 April 2024, GPLv2; Great Tables (Posit), version 1.0.0, 25 September 2026, MIT.</td>
		<td>[https://github.com/StatsReporting/stargazer](https://github.com/StatsReporting/stargazer)</td>
		<td>Side-by-side model tables (coefficients, standard errors, stars, R², N) for comparing pooled, fixed-effects and interaction models. etable already outputs Great Tables objects that render in Quarto HTML; stargazer mimics R's stargazer for statsmodels OLS but is barely maintained.</td>
		<td>sessions 1 and 3 (model comparison table in the project repo milestone). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>seaborn and Yellowbrick (diagnostic plots)</td>
		<td>seaborn (Michael Waskom), version 0.13.2, 25 January 2024, BSD; Yellowbrick (District Data Labs), version 1.5, 21 August 2022, Apache-2.0.</td>
		<td>[https://pypi.org/project/seaborn/](https://pypi.org/project/seaborn/)</td>
		<td>sns.regplot(order=2 / logx=True / lowess=True), sns.residplot and sns.lmplot(hue="country") make linearity, heteroscedasticity and group-specific slopes (moderation) visible in one line; Yellowbrick adds ResidualsPlot, PredictionError and CooksDistance for scikit-learn models. Yellowbrick has had no release since 2022.</td>
		<td>sessions 1 and 2 (diagnostic plots in the lab). Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>ISLP (package)</td>
		<td>James, Witten, Hastie, Tibshirani and Taylor, 2023 to 2026, software. Version 0.4.1, 3 February 2026, BSD-style licence.</td>
		<td>[https://pypi.org/project/ISLP/](https://pypi.org/project/ISLP/)</td>
		<td>Ships the textbook datasets (Carseats, OJ, Bikeshare, Credit, Wage and others) via load_data() plus ModelSpec, poly(), bs(), ns() helpers that make interaction and spline design matrices explicit; the companion Chapter 3 lab is a complete statsmodels regression walk-through.</td>
		<td>session 1 warm-up data and exercises. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Reference points outside Python: R lm/fixest/marginaleffects and SPSS/R PROCESS</td>
		<td>R Core (lm), Laurent Bergé (fixest), Arel-Bundock (marginaleffects for R), Jacob Long (interactions, Johnson-Neyman plots); Andrew F. Hayes, PROCESS macro for SPSS, SAS and R (current major release 5).</td>
		<td>[http://processmacro.org/](http://processmacro.org/)</td>
		<td>R remains the reference for regression teaching material, and most Python packages above are ports (pyfixest of fixest, marginaleffects, bambi of brms, pyprocessmacro of PROCESS). PROCESS is the de facto standard in marketing and consumer research for moderation and mediation, so students will meet "Model 4" and "Model 7" language in papers; pyprocessmacro lets them reproduce it without an SPSS licence.</td>
		<td>background; one slide mapping SPSS PROCESS and R syntax to the Python equivalents.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
</table>