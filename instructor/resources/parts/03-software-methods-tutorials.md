# Part 3: Software, statistical methods, video tutorials and online courses

Compiled 5 October 2026 for the master course "International Marketing Analytics" (WU Vienna, CEMS). Session mapping used below: S1 foundations and regression, S2 MMM mechanics (adstock, saturation, Bayesian estimation), S3 budget allocation across countries and channels, S4 forecasting, S5 experiments and attribution. Adjust if the syllabus numbers differ.

Verification note: PyPI, GitHub and a handful of other domains could be fetched directly. Most vendor, course-platform and documentation domains (developers.google.com, pymc-marketing.io, getrecast.com, coursera.org, udemy.com, youtube.com and others) were blocked by the network proxy in this session, so those entries are confirmed from search-engine results only and are marked "(search-confirmed)". Anything that could not be confirmed either way is marked "(unverified)".

---

## 1. Software

**Open source (Python first)**

### PyMC-Marketing
- **Source:** PyMC Labs, 2023 to 2026, software (Python, Apache 2.0). Latest release 1.2.0, 29 September 2026; requires Python 3.12 or newer.
- **Link:** https://pypi.org/project/pymc-marketing/ and https://github.com/pymc-labs/pymc-marketing
- **Why it matters:** The most complete open Bayesian MMM in Python: pluggable adstock and saturation, lift-test calibration, time-varying intercept and media effects via Hilbert-space Gaussian processes, budget optimiser with constraints, multidimensional (geo-level) MMM, plus CLV models. Mature, actively released, excellent example notebooks.
- **Use in course:** S2 and S3 main lab tool; S5 calibration lab. Free.

### Google Meridian
- **Source:** Google, 2025 to 2026, software (Python on TensorFlow Probability, Apache 2.0). Latest release 2.1.0, 25 September 2026; Python 3.10 or newer (repo states 3.11 to 3.13).
- **Link:** https://pypi.org/project/google-meridian/ and https://github.com/google/meridian (docs: https://developers.google.com/meridian, search-confirmed)
- **Why it matters:** Geo-level hierarchical Bayesian MMM with Hill saturation, adstock, ROI priors, reach and frequency, and a fixed or flexible budget optimiser with ROI constraints. The natural "international" tool: geos (countries, regions) are first-class and partially pooled. Replaces LightweightMMM.
- **Use in course:** S3 lab (multi-country allocation) and comparison with PyMC-Marketing. Free; GPU helpful but not required for the demo data.

### Meta Robyn
- **Source:** Meta Marketing Science, 2020 to 2025, software (R primary, MIT). R 3.12.0 released 19 December 2024; Python port "robynpy" 0.3.6, 3 April 2025 (beta, LLM-translated from R 3.11.1).
- **Link:** https://github.com/facebookexperimental/Robyn and https://pypi.org/project/robynpy/
- **Why it matters:** The industry-standard frequentist alternative: ridge regression with Nevergrad evolutionary hyperparameter search over adstock (geometric or Weibull), Hill saturation and lambda, multi-objective model selection (NRMSE, DECOMP.RSSD), calibration with experiments, budget allocator. Ships a simulated demo dataset (demo.R).
- **Use in course:** S2 reading and optional R lab; useful to contrast ridge plus search against Bayesian priors. Free. Python port is not yet reliable enough for a graded lab.

### LightweightMMM (deprecated)
- **Source:** Google, 2022 to 2023, software (Python, NumPyro and JAX, Apache 2.0). Last release 0.1.9, 23 May 2023; repository archived 19 January 2026 with a notice recommending Meridian.
- **Link:** https://github.com/google/lightweight_mmm and https://pypi.org/project/lightweight-mmm/
- **Why it matters:** Still the simplest readable implementation of a geo-hierarchical Bayesian MMM (about 1,500 lines) and the basis of many tutorials. Good for reading the model code, not for new projects.
- **Use in course:** Background only; point students to Meridian for anything hands-on.

### Orbit (KTR) by Uber
- **Source:** Uber, 2020 to 2026, software (Python, Apache 2.0). Latest 1.1.5.1, 22 May 2026; Python 3.12 or newer.
- **Link:** https://pypi.org/project/orbit-ml/ and https://github.com/uber/orbit
- **Why it matters:** Bayesian time-series package whose Kernel Time-varying Regression (KTR) model is the reference implementation of the Ng, Wang and Dai (2021) time-varying coefficient MMM. Also provides ETS, LGT and DLT forecasters.
- **Use in course:** S4 (forecasting) and an advanced S2 demo of time-varying media effects. Free.

### CausalPy
- **Source:** PyMC Labs, 2022 to 2026, software (Python, Apache 2.0). Latest 0.9.0, 28 July 2026.
- **Link:** https://pypi.org/project/CausalPy/ and https://github.com/pymc-labs/CausalPy
- **Why it matters:** One API for difference-in-differences (including staggered), synthetic control, geographical lift, interrupted time series, regression discontinuity, IV and IPW, with PyMC (Bayesian) or scikit-learn (OLS) back ends. Ideal for teaching quasi-experiments without R.
- **Use in course:** S5 lab (DiD, synthetic control on a country roll-out). Free.

### GeoLift
- **Source:** Meta (facebookincubator), 2021 to 2026, software (R, GPL 2 or later; version 2.7.5 in DESCRIPTION).
- **Link:** https://github.com/facebookincubator/GeoLift
- **Why it matters:** End-to-end geo-experiment toolkit built on augmented synthetic control: power analysis and market selection, test design, lift inference and plots. Needs 25 or more pre-periods and about 20 or more geo units, which is a useful teaching constraint. R only.
- **Use in course:** S5 reading and optional R demo; pair with CausalPy or Google's Trimmed Match (https://github.com/google/trimmed_match, Python, Apache 2.0) for a Python path.

### CausalImpact (tfcausalimpact Python port)
- **Source:** Willian Fuks (port of Google's R CausalImpact, Brodersen et al. 2015), 2020 to 2026, software (Python, Apache 2.0). Latest 0.0.19, 20 September 2026.
- **Link:** https://pypi.org/project/tfcausalimpact/ and https://github.com/WillianFuks/tfcausalimpact (R original: https://google.github.io/CausalImpact/CausalImpact.html)
- **Why it matters:** Bayesian structural time-series counterfactual for a single treated series with control series, with results documented as equivalent to the R original. Good for "what did the campaign or price change do" questions where no geo split exists.
- **Use in course:** S5 short lab. Free.

### statsmodels
- **Source:** statsmodels developers, 2009 to 2026, software (Python, BSD 3-clause). Latest 0.15.0, 27 August 2026.
- **Link:** https://pypi.org/project/statsmodels/ (VIF: https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html, search-confirmed)
- **Why it matters:** OLS and log-log elasticities with proper inference tables, HAC standard errors, VIF and condition numbers for multicollinearity diagnostics, ETS and SARIMAX for forecasting. The baseline every MMM should be compared against.
- **Use in course:** S1 lab (first MMM as OLS), S4 forecasting baselines. Free.

### linearmodels
- **Source:** Kevin Sheppard, 2017 to 2025, software (Python, NCSA licence). Latest 7.0, 21 October 2025.
- **Link:** https://pypi.org/project/linearmodels/ and https://github.com/bashtage/linearmodels
- **Why it matters:** Panel estimators that statsmodels lacks: one- and two-way fixed effects, first differences, between and pooled, plus IV and system estimators, with clustered standard errors. The frequentist counterpart to partial pooling for country-by-week panels.
- **Use in course:** S3 lab (country fixed effects versus hierarchical priors). Free.

### Prophet and StatsForecast (forecasting baselines)
- **Source:** Meta (Prophet 1.5.0, 5 October 2026, MIT) and Nixtla (StatsForecast 2.1.1, 16 July 2026, Apache 2.0), software (Python).
- **Link:** https://pypi.org/project/prophet/ ; https://pypi.org/project/statsforecast/ and https://github.com/Nixtla/statsforecast
- **Why it matters:** Prophet gives an additive trend plus Fourier seasonality plus holidays model with regressors, which doubles as an intuition builder for MMM baselines. StatsForecast gives fast AutoARIMA, AutoETS, Theta and CES with exogenous regressors across hundreds of country series at once.
- **Use in course:** S4 lab (country-level demand forecasts feeding budget scenarios). Free.

### Synthetic MMM benchmark generators
- **Source:** Niklas Heusch, 2026, software and paper (Jupyter, generator for "A Synthetic Benchmark Dataset with Endogenous Marketing Spend for Validating MMMs", arXiv 2608.21130); Meta siMMMulator (R, MIT); PyMC Labs mmm-param-recovery (Python, Apache 2.0, compares PyMC samplers and Meridian).
- **Link:** https://github.com/niklas-heusch/mmm-materials ; https://arxiv.org/abs/2608.21130 (search-confirmed) ; https://github.com/facebookexperimental/siMMMulator ; https://github.com/pymc-labs/mmm-param-recovery
- **Why it matters:** Ground-truth data is the only way to grade an MMM. Heusch's generator is the first with endogenous spend (budget feedback, promo-calendar anticipation, TV bursts, performance chasing) plus simulated go-dark geo tests, which is exactly the confounding students need to see. No licence file shown on the Heusch repo.
- **Use in course:** S2 and S3 assignments (fit a model, compare to known ROI); S5 for simulated geo tests. Free.

**Commercial and SaaS**

### Recast
- **Source:** Recast (Michael Kaminsky, Tom Vladeck), 2020 to 2026, software and vendor (Bayesian MMM in Stan, weekly refresh, forecasting and optimiser).
- **Link:** https://getrecast.com/mmm/ (search-confirmed); docs https://docs.getrecast.com/docs/model-configuration-phase (search-confirmed)
- **Why it matters:** The most technically transparent vendor: public docs on model configuration, posts on divergences, multimodality and saturation, open comparisons with Robyn and LightweightMMM. Enterprise pricing, no public free tier.
- **Use in course:** Background and S2 reading (their "3 hurdles of a Bayesian MMM" post); guest-talk candidate (US based, remote). Free educational content; platform is paid.

### Mutinex (GrowthOS)
- **Source:** Mutinex, Sydney, 2020 to 2026, software and vendor (continuous MMM, scenario planning, agency partnerships such as dentsu).
- **Link:** https://mutinex.co/product/growthos/ (search-confirmed)
- **Why it matters:** Example of "always-on" MMM delivered as a platform with confidence intervals on scenarios; strong APAC and multi-market footprint. No academic programme found.
- **Use in course:** Background; vendor-landscape slide in S3.

### Cassandra
- **Source:** Cassandra (cassandra.app), 2021 to 2026, software and vendor (no-code Bayesian MMM and geo incrementality; now offers a Meridian-based model).
- **Link:** https://cassandra.app/marketing-mix-model (search-confirmed); Meridian note https://cassandra.app/product-updates/meridian (search-confirmed)
- **Why it matters:** Shows how open-source engines (Meridian) are wrapped into SaaS. Markets a free entry tier ("Your MMM in 10 minutes"), which could give students a hands-on UI without code (terms unverified).
- **Use in course:** S3 demo of a vendor UI versus a notebook; check the free tier before class.

### Sellforte
- **Source:** Sellforte, Espoo (Finland), 2017 to 2026, software and vendor (SaaS MMM, daily forecasts, incrementality tests, "agentic" media planner).
- **Link:** https://sellforte.com/ (search-confirmed)
- **Why it matters:** European SaaS MMM with public explainer content, including a page on Meridian and a note on data granularity; clients across Nordics and Baltics (Musti Group, Finnish Design Shop) give a multi-country angle.
- **Use in course:** Background; strong European guest-talk candidate (Helsinki, remote).

### Analytic Partners (GPS Enterprise)
- **Source:** Analytic Partners, New York with European offices, 1999 to 2026, software and vendor (GPS-Enterprise platform, ROI Genome benchmarks; Gartner MMM leader).
- **Link:** https://analyticpartners.com/solutions/marketing-mix-modeling/ (search-confirmed)
- **Why it matters:** The large-enterprise "commercial analytics" model: data ingestion to optimisation, cross-market benchmarks (ROI Genome). Useful for discussing what enterprises buy versus what open source gives.
- **Use in course:** Background; S3 vendor landscape.

### Nielsen MMM (now Circana)
- **Source:** Nielsen, then Circana (acquisition completed 21 August 2025), vendor and report. Nielsen "Marketing Mix Modeling Best Practices" guide, 2022.
- **Link:** https://www.nielsen.com/wp-content/uploads/sites/2/2022/09/Marketing-Mix-Modeling-Best-Practices-EN.pdf (search-confirmed); https://www.circana.com/post/circana-completes-acquisition-of-nielsen-s-marketing-mix-modeling-business (search-confirmed)
- **Why it matters:** Decades of multi-country MMM practice; the best-practices PDF is a short, readable client-side checklist (granularity, data requirements). Note the ownership change when citing.
- **Use in course:** S1 or background reading.

### Ipsos MMA
- **Source:** Ipsos MMA, 1990s to 2026, vendor (unified marketing measurement; Gartner MMM Magic Quadrant leader 2024 and 2025).
- **Link:** https://mma.com/resources/analytic-fundamentals-what-is-marketing-mix-modeling/ (search-confirmed); product overview PDF https://mma.com/wp-content/uploads/IPSOS-MMA-Unified-Marketing-Measurement-Product-Overview-2024-FINAL.pdf (search-confirmed)
- **Why it matters:** Clear statement of "unified measurement" (MMM plus attribution plus tests in one framework), the vendor positioning students will meet in practice.
- **Use in course:** S5 reading on triangulation; background.

### Measured
- **Source:** Measured, 2017 to 2026, software and vendor (incrementality testing platform with test-calibrated MMM; pricing reported from about USD 50k per year).
- **Link:** https://www.measured.com/media-mix-modeling/ (search-confirmed); decision tree https://www.measured.com/faq/incrementality-attribution-mmm-decision-tree/ (search-confirmed)
- **Why it matters:** Good public FAQ material on when to use incrementality tests, attribution or MMM, and ten real-world MMM examples.
- **Use in course:** S5 reading; background.

### Haus
- **Source:** Haus, 2021 to 2026, software and vendor (geo incrementality experiments, "causal MMM"; USD 55m funding to 2025).
- **Link:** https://www.haus.io/incrementality-101 (search-confirmed); https://www.haus.io/blog/geo-experiments-the-fundamentals (search-confirmed)
- **Why it matters:** Their "Incrementality 101" and geo-experiment fundamentals posts are short, well written primers on design, power and synthetic control in business language.
- **Use in course:** S5 pre-reading for the geo-experiment session.

### Lifesight
- **Source:** Lifesight, Singapore and US, 2016 to 2026, software and vendor (no-code causal MMM, incrementality, attribution). Maintains the CC0 "awesome-marketing-measurement" list on GitHub.
- **Link:** https://github.com/lifesight/awesome-marketing-measurement (fetched); platform https://lifesight.io/platform/ (search-confirmed)
- **Why it matters:** The awesome list (15 sections: open-source MMM, geo experiments, attribution, datasets, papers, courses, communities) is a handy vendor-neutral index for students. Lifesight announced an open-source forecasting engine "Horizon" but no repository was visible on their GitHub organisation (unverified).
- **Use in course:** Background; give students the awesome list in week 1.

### MASS Analytics (MassTer)
- **Source:** MASS Analytics (Dr Ramla Jarrar), London and Tunis, 2010s to 2026, software and vendor (MassTer MMM desktop software, Bayesian and hierarchical options; MMM Academy).
- **Link:** https://mass-analytics.com/solutions (search-confirmed); academy https://mass-analytics.com/mmm-learning-academy/ (search-confirmed)
- **Why it matters:** One of the few vendors that packages teaching with the tool: free YouTube course, paid academy with certificate and software access, 2-week MassTer trial licences with their Udemy course. Listed price about GBP 12,000 per year; no formal academic licence found, worth asking.
- **Use in course:** S2 reading (free course videos); vendor demo candidate. Trial licence free for two weeks.

### Ekimetrics (Eki.Decisions)
- **Source:** Ekimetrics, Paris (offices in London, New York, Dubai), 2006 to 2026, vendor and consultancy (MMM core with modules; Gartner "Visionary" 2025; Meta and TikTok measurement partner).
- **Link:** https://www.ekimetrics.com/solutions/marketing-effectiveness (search-confirmed)
- **Why it matters:** European leader in multi-market MMM for FMCG and luxury; co-author of the Artefact and Meta Robyn comparison study. Their "Bayesian MMM with limited data" style posts are useful for small-country models.
- **Use in course:** Background; European guest-talk candidate (Paris).

### Keen Decision Systems
- **Source:** Keen, Durham NC, 2010 to 2026, software and vendor (adaptive Bayesian MMM with real-time scenario planning).
- **Link:** https://keends.com/news/free-access-to-mmm/ (search-confirmed)
- **Why it matters:** Announced a free-access MMM programme (scope unverified); a mid-market example of self-serve forecasting and planning.
- **Use in course:** Background; check the free-access terms for a student exercise.

### Artefact
- **Source:** Artefact, Paris, 2015 to 2026, consultancy and vendor (Google Meridian certified; custom hierarchical Bayesian and graphical causal MMM; Robyn versus GCM study with Meta on five international FMCG brands).
- **Link:** https://www.artefact.com/news/artefact-achieves-google-meridian-certification/ (search-confirmed); Robyn study https://report.artefact.com/l/597421/2023-07-18/j2kvz8 (search-confirmed)
- **Why it matters:** Shows how consultancies build on open-source engines and where they add causal structure (DAGs). The five-brand international comparison is directly relevant.
- **Use in course:** S2 or S5 reading; European guest-talk candidate.

---

## 2. Statistical methods (stat. Methoden)

### OLS and log-log (constant elasticity) response models
- **Source:** Hanssens, Parsons and Schultz, 2001, book (Market Response Models, 2nd ed., Springer, chapters on functional forms); Tellis, 2006, book chapter ("Modeling Marketing Mix", Handbook of Marketing Research, Sage).
- **Link:** https://www.springer.com/us/book/9780792378266 ; https://doi.org/10.4135/9781412973380.n24
- **Why it matters:** Defines the linear, multiplicative (log-log) and semi-log forms, elasticities and the economics behind them; Tellis is the compact 17-page primer.
- **Use in course:** S1 reading; statsmodels lab. Paywalled (library access).

### Adstock variants (geometric, delayed, Weibull)
- **Source:** Jin, Wang, Sun, Chan and Koehler, 2017, paper (Google Research technical report); Robyn documentation, "Key features" (geometric and Weibull adstock).
- **Link:** https://research.google/pubs/bayesian-methods-for-media-mix-modeling-with-carryover-and-shape-effects/ (search-confirmed) ; https://facebookexperimental.github.io/Robyn/docs/features/ (search-confirmed)
- **Why it matters:** Jin et al. formalise carryover (geometric and delayed adstock) and shape effects in one Bayesian model; Robyn's docs explain the Weibull PDF and CDF variants used in practice.
- **Use in course:** S2 core reading.

### Hill and logistic saturation
- **Source:** Jin et al., 2017 (as above, Hill shape function); Google Meridian documentation, "Media saturation and lagging".
- **Link:** https://developers.google.com/meridian/docs/advanced-modeling/media-saturation-lagging (search-confirmed)
- **Why it matters:** Hill(x; ec, slope) with half-saturation point and slope is now the default in Meridian and Robyn; the docs show how it interacts with adstock and why the two are hard to separate.
- **Use in course:** S2 lab (plot response curves, derive marginal ROI).

### Ridge regression with hyperparameter search (Robyn approach)
- **Source:** Hastie, Tibshirani and Friedman, 2009, book (Elements of Statistical Learning, 2nd ed., section 3.4 shrinkage methods, free PDF); Zhou et al., 2024, paper ("Packaging Up Media Mix Modeling: An Introduction to Robyn's Open-Source Approach", arXiv 2403.14674 and MSI working paper).
- **Link:** https://hastie.su.domains/ElemStatLearn/ (search-confirmed) ; https://arxiv.org/pdf/2403.14674 (search-confirmed)
- **Why it matters:** ESL gives the L2 penalty and bias-variance trade-off; the Robyn paper documents the Nevergrad multi-objective search over adstock, Hill and lambda and the model-selection criteria.
- **Use in course:** S2 reading; compare with Bayesian priors.

### Hierarchical Bayesian regression (geo-level MMM)
- **Source:** Sun, Wang, Jin, Chan and Koehler, 2017, paper (Geo-level Bayesian Hierarchical Media Mix Modeling, Google); Wang, Jin, Sun, Chan and Koehler, 2017, paper (hierarchical approach using category data).
- **Link:** https://research.google/pubs/geo-level-bayesian-hierarchical-media-mix-modeling/ (search-confirmed) ; https://research.google.com/pubs/archive/45999.pdf (search-confirmed)
- **Why it matters:** The basis of Meridian: sub-national or multi-country units share priors, which tightens credible intervals and protects against unsound reallocation. The category paper shows how to borrow strength across brands or markets via informative priors.
- **Use in course:** S3 core reading for cross-country allocation.

### Time-varying coefficients and Gaussian processes
- **Source:** Ng, Wang and Dai, 2021, paper (Bayesian Time Varying Coefficient Model with Applications to MMM, AdKDD 2021, arXiv 2106.03322); PyMC-Marketing notebook "MMM with time-varying parameters" (HSGP); Rasmussen and Williams, 2006, book (GPML, free PDF).
- **Link:** https://arxiv.org/pdf/2106.03322 (search-confirmed) ; https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_tvp_example.html (search-confirmed) ; https://gaussianprocess.org/gpml/ (search-confirmed)
- **Why it matters:** Media effectiveness drifts; KTR (Orbit) and HSGP (PyMC-Marketing) are the two practical ways to let coefficients or baselines move smoothly over time.
- **Use in course:** S2 advanced demo; S4 link to forecasting.

### Fourier seasonality
- **Source:** Hyndman and Athanasopoulos, 2021, book (Forecasting: Principles and Practice, 3rd ed., chapter 7 "Time series regression models", section on Fourier terms, free online); Taylor and Letham, 2018, article (Forecasting at Scale, The American Statistician 72(1), 37 to 45).
- **Link:** https://otexts.com/fpp3/useful-predictors.html (search-confirmed) ; https://doi.org/10.1080/00031305.2017.1380080 (search-confirmed)
- **Why it matters:** Fourier pairs are how Prophet, PyMC-Marketing and Meridian represent yearly seasonality with few parameters; fpp3 explains the choice of K.
- **Use in course:** S2 and S4.

### Panel fixed effects and partial pooling
- **Source:** Gelman and Hill, 2007, book (Data Analysis Using Regression and Multilevel/Hierarchical Models, Cambridge, chapter 12 on partial pooling); linearmodels documentation (PanelOLS fixed effects).
- **Link:** https://assets.cambridge.org/97805218/67061/frontmatter/9780521867061_frontmatter.pdf (search-confirmed) ; https://github.com/bashtage/linearmodels
- **Why it matters:** Makes the link between country fixed effects (no pooling), pooled OLS (complete pooling) and hierarchical priors (partial pooling), which is the central modelling decision in a multi-country MMM.
- **Use in course:** S3 reading and lab. Gelman and Hill is paywalled; chapter 12 circulates as a PDF in many course sites.

### Budget optimisation under constraints
- **Source:** PyMC-Marketing notebook "Budget Allocation with PyMC-Marketing" (SLSQP with bounds and custom constraints, plus risk assessment and multi-objective variants); Google Meridian docs "Budget optimization scenarios" (fixed versus flexible budget, minimal marginal ROI or target ROI constraints).
- **Link:** https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_budget_allocation_example.html (search-confirmed) ; https://developers.google.com/meridian/docs/user-guide/budget-optimization-scenarios (search-confirmed)
- **Why it matters:** Both docs show the same mathematics (maximise expected response subject to total budget and per-channel bounds) in code students can run, including uncertainty in the optimum.
- **Use in course:** S3 lab (allocate across countries and channels with floor and cap constraints).

### Forecasting with ETS, ARIMA and regression
- **Source:** Hyndman and Athanasopoulos, 2021, book (fpp3 chapters 8 "Exponential smoothing", 9 "ARIMA models", 10 "Dynamic regression models"); StatsForecast documentation.
- **Link:** https://otexts.com/fpp3/ (search-confirmed) ; https://github.com/Nixtla/statsforecast
- **Why it matters:** The standard, free text; dynamic regression (ARIMA errors with media regressors) is the bridge between forecasting and MMM.
- **Use in course:** S4 core reading and lab.

### Difference-in-differences
- **Source:** Roth, Sant'Anna, Bilinski and Poe, 2023, article (What's trending in difference-in-differences? Journal of Econometrics 235(2), 2218 to 2244); CausalPy documentation.
- **Link:** https://doi.org/10.1016/j.jeconom.2023.03.008 (search-confirmed; free PDF https://arxiv.org/pdf/2201.01194) ; https://github.com/pymc-labs/CausalPy
- **Why it matters:** Synthesises staggered adoption, parallel-trends violations and inference, with practitioner recommendations; CausalPy implements standard and staggered DiD.
- **Use in course:** S5 reading and lab.

### Synthetic control
- **Source:** Abadie, 2021, article (Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects, Journal of Economic Literature 59(2), 391 to 425, open access); Brodersen et al., 2015, article (CausalImpact, Annals of Applied Statistics 9(1), 247 to 274).
- **Link:** https://www.aeaweb.org/articles?id=10.1257/jel.20191450 (search-confirmed) ; https://projecteuclid.org/journals/annals-of-applied-statistics/volume-9/issue-1/Inferring-causal-impact-using-Bayesian-structural-time-series-models/10.1214/14-AOAS788.full (search-confirmed)
- **Why it matters:** Abadie is the definitive guide to when synthetic control is credible (donor pool, pre-period fit, placebo tests); Brodersen gives the Bayesian state-space version used in CausalImpact.
- **Use in course:** S5 reading; CausalPy and tfcausalimpact labs.

### Geo experiments and power
- **Source:** Vaver and Koehler, 2011, paper (Measuring Ad Effectiveness Using Geo Experiments, Google); Chen and Au, 2022, article (Robust causal inference for incremental return on ad spend with randomized paired geo experiments, Annals of Applied Statistics 16(1); Trimmed Match, arXiv 1908.02922) and Trimmed Match Design (arXiv 2105.07060).
- **Link:** https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/ (search-confirmed) ; https://projecteuclid.org/journals/annals-of-applied-statistics/volume-16/issue-1/Robust-causal-inference-for-incremental-return-on-ad-spend-with/10.1214/21-AOAS1493.pdf (search-confirmed)
- **Why it matters:** Vaver and Koehler is the original geo-based regression design; Trimmed Match adds robust paired designs and power-based pair selection. GeoLift's power tools and Haus's primers build on both.
- **Use in course:** S5 core reading; power-calculation exercise with GeoLift or Trimmed Match.

### Logistic (data-driven) attribution
- **Source:** Shao and Li, 2011, paper (Data-driven multi-touch attribution models, KDD 2011, pages 258 to 264).
- **Link:** https://doi.org/10.1145/2020408.2020453 (search-confirmed)
- **Why it matters:** The first data-driven MTA: bagged logistic regression on touchpoint exposure plus a probabilistic second-order model for credit assignment; the reference point for all later MTA work.
- **Use in course:** S5 reading. ACM paywall (library access).

### Shapley value attribution
- **Source:** Zhao, Mahboobi and Bagheri, 2018, paper (Shapley Value Methods for Attribution Modeling in Online Advertising, arXiv 1804.05327).
- **Link:** https://arxiv.org/abs/1804.05327 (search-confirmed)
- **Why it matters:** Clear derivation of ordered and unordered Shapley attribution with an efficient computation; the method behind Google Analytics' former data-driven attribution.
- **Use in course:** S5 lab (compute Shapley credit on a synthetic journey dataset). Free.

### Markov chain attribution
- **Source:** Anderl, Becker, von Wangenheim and Schumann, 2016, article (Mapping the customer journey: Lessons learned from graph-based online attribution modeling, International Journal of Research in Marketing 33(3), 457 to 474).
- **Link:** https://www.sciencedirect.com/science/article/abs/pii/S0167811616300349 (search-confirmed)
- **Why it matters:** The removal-effect Markov attribution framework, from a German research team (Passau and ETH), with first- and higher-order chains and spillover findings; the basis of the R ChannelAttribution package.
- **Use in course:** S5 reading. Elsevier paywall (WU library).

### Calibration with lift tests
- **Source:** Zhang, Wurm, Li, Wakim, Kelly, Price and Liu, 2024, paper (Media Mix Model Calibration With Bayesian Priors, Google Research); PyMC-Marketing notebooks "Lift test calibration" and "Mitigating unobserved confounders with lift test likelihoods".
- **Link:** https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/ (search-confirmed) ; https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_lift_test.html (search-confirmed) ; https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_roas.html (search-confirmed)
- **Why it matters:** Reparametrising channel effects as ROI and placing experiment-informed priors on them is now the industry standard (Meridian ROI priors, Robyn calibration); the PyMC-Marketing notebooks show it in code with simulated confounding.
- **Use in course:** S5 lab linking experiments back into the MMM.

### Identifiability and multicollinearity diagnostics
- **Source:** Chan and Perry, 2017, paper (Challenges and Opportunities in Media Mix Modeling, Google); Chen, Chan, Perry, Jin, Sun, Wang and Koehler, 2018, paper (Bias Correction for Paid Search in Media Mix Modeling, arXiv 1807.03292); statsmodels VIF.
- **Link:** https://research.google/pubs/challenges-and-opportunities-in-media-mix-modeling/ (search-confirmed) ; https://arxiv.org/pdf/1807.03292 (search-confirmed)
- **Why it matters:** Chan and Perry list the structural problems (collinear spend, selection bias, limited variation, ad-hoc functional forms); the paid-search paper gives a back-door correction. Together with VIF and prior-posterior checks they are the honest "what can this model not tell you" session.
- **Use in course:** S2 reading and a diagnostics checklist students apply to their own model.

---

## 3. Video tutorials and online courses

### Thomas Wiecki, "Bayesian Marketing Science: Solving Marketing's 3 Biggest Problems" (PyCon DE and PyData Berlin 2023)
- **Source:** PyMC Labs, 2023, video (YouTube, about 30 minutes, free, intermediate).
- **Link:** https://www.youtube.com/watch?v=RY-M0tvN77s (search-confirmed)
- **Why it matters:** Introduces PyMC-Marketing (MMM and CLV) and CausalPy in one talk with code, from the PyMC founder. A good conceptual opener before the lab.
- **Use in course:** S2 pre-class viewing.

### PyMC Labs, "Bayesian Marketing Mix Models: State of the Art and their Future" (online meetup, September 2022)
- **Source:** PyMC Labs with Juan Orduz, Luca Fiaschi and guests, 2022, video (recording linked from PyMC Discourse; about 60 to 90 minutes, free, intermediate).
- **Link:** https://discourse.pymc.io/t/online-meetup-bayesian-marketing-mix-models-state-of-the-art-and-their-future-sep-21-2022/10432 (search-confirmed; recording link unverified)
- **Why it matters:** Practitioner panel on what works in Bayesian MMM at companies such as HelloFresh and Bolt; useful as a "voices from industry" segment.
- **Use in course:** Background.

### PyData NYC 2024, "PyMC-Marketing: Customer and Marketing Analytics the Easy Way" (Christian Luhmann)
- **Source:** PyData, November 2024, talk (40 minutes; recording expected on the PyData YouTube channel, unverified).
- **Link:** https://pydata.org/nyc2024/schedule/talk/BF3GQ7/ (search-confirmed)
- **Why it matters:** Most recent conference walk-through of the library's MMM and CLV APIs.
- **Use in course:** S2 optional viewing.

### Google Ads DevCast, episode 6: "The What and Why on Meridian" (May 2026)
- **Source:** Google Advertising and Measurement Developers, 2026, video podcast (YouTube playlist, about 30 minutes, free, introductory).
- **Link:** https://ads-developers.googleblog.com/2026/05/the-what-and-why-on-meridian-ads.html (search-confirmed); playlist https://www.youtube.com/playlist?list=PLKByxjzUC-N8t_n0JnP6PTETY6b7yg2q4 (search-confirmed)
- **Why it matters:** Official overview of Meridian and the new surfaces (Google Analytics, Studio, GeoX) from the product team; up to date as of 2026.
- **Use in course:** S3 pre-class viewing.

### Meridian Python tutorials on YouTube
- **Source:** Third-party creators, 2025, videos: "Meridian Marketing Mix Modeling: Python Tutorial" and "Meridian Tutorial: Building a National MMM for eCommerce" (each roughly 20 to 40 minutes, free, intermediate; channels unverified).
- **Link:** https://www.youtube.com/watch?v=dWWaY4dZPYQ (search-confirmed) ; https://www.youtube.com/watch?v=QJJtrMobx4I (search-confirmed)
- **Why it matters:** Step-by-step runs of the official Meridian demo notebook, useful for students who get stuck installing TensorFlow Probability.
- **Use in course:** S3 lab support material. Google's own "Meridian Self-starter Guide for CMOs" PDF (Think with Google, search-confirmed) is a non-technical companion.

### Recast, "How to Build a Media Mix Model (MMM)" series with Tom Vladeck
- **Source:** Recast, 2024 to 2025, YouTube playlist (multi-episode, 15 to 30 minutes each, free, intermediate; episode 2 covers DAGs in MMM) plus "How to Use Lift Tests to Calibrate Your MMM".
- **Link:** https://www.youtube.com/playlist?list=PLICC447esbJliT9rATTVZGU9Ii-hQ_PYa (search-confirmed) ; https://www.youtube.com/watch?v=-v0NR8rZsFQ (search-confirmed)
- **Why it matters:** Statistician-led, vendor-neutral in tone, explicit about causal assumptions and validation; complements the code-centric talks.
- **Use in course:** S2 and S5 viewing.

### Recast MMM Academy
- **Source:** Recast, 2024 to 2026, web course (free, self-paced text and video modules: incrementality basics, building a model, validation, open-source packages).
- **Link:** https://getrecast.com/mmm-academy/ (search-confirmed)
- **Why it matters:** Structured, free, and written for analysts who will build their own model; the "validation" module is a good assignment rubric source.
- **Use in course:** Background reading list; S2.

### MASS Analytics free MMM course on YouTube (Dr Ramla Jarrar)
- **Source:** MASS Analytics, 2023 to 2026, YouTube playlists (eleven "Packs" A to K following a real project order; dozens of short videos, free, beginner to intermediate).
- **Link:** https://mass-analytics.com/marketing-mix-modeling-blogs/the-free-marketing-mix-modeling-course/ (search-confirmed); course hub https://mass-analytics.com/marketing-mix-modeling-course (search-confirmed)
- **Why it matters:** The only free end-to-end MMM project curriculum (data splitting, transformations, modelling, optimisation, reporting) from a practising vendor; tool-agnostic in the concepts.
- **Use in course:** S1 to S3 self-study; assign specific packs.

### MASS Analytics MMM Academy (Fundamentals and End-to-End courses)
- **Source:** MASS Analytics, 2025 to 2026, paid online courses (2 courses, 9 modules, real datasets, certificate, access to MassTer software; price not public, search-confirmed).
- **Link:** https://mass-analytics.com/mmm-learning-academy/ (search-confirmed)
- **Why it matters:** Covers Bayesian and hierarchical models and board-level reporting; one of the few MMM certificates. Worth asking about an academic bundle for 30 students.
- **Use in course:** Optional for ambitious students; vendor contact.

### PyMC Labs, "Bayesian Marketing Analytics" live course
- **Source:** PyMC Labs, 2025 to 2026, live online course (four weeks, cohort based, paid; price and next dates not retrievable in this session).
- **Link:** https://www.pymc-labs.com/courses/bayesian-marketing-analytics (search-confirmed)
- **Why it matters:** Taught by the PyMC-Marketing authors; covers MMM, causal inference, CLV, product adoption and budget optimisation, so it mirrors this course almost module by module.
- **Use in course:** Instructor preparation; possible guest lecture by a PyMC Labs instructor.

### Meta Robyn walkthroughs
- **Source:** Gufeng Zhou (Robyn creator) interview "Robyn's Creation to Controversy, Decomposition Distance and MMM Politics" (2024, about 60 minutes, free); "Ep. 1 to Ep. 8 Marketing Mix Modeling with Facebook Robyn" tutorial series (third party, 2022 to 2023, 10 to 25 minutes each, free, intermediate R).
- **Link:** https://www.youtube.com/watch?v=QX8ATifkyA4 (search-confirmed) ; https://www.youtube.com/watch?v=l1Q42qx8z9I (search-confirmed) ; https://www.youtube.com/watch?v=3DOozIRwohw (calibration episode, search-confirmed)
- **Why it matters:** The interview explains design choices (DECOMP.RSSD, ridge, Nevergrad) and their critics from the author himself; the episode series is the practical R walkthrough. Meta's own 15-minute demo video is hosted on Google Drive via the Robyn repo (unverified).
- **Use in course:** S2 optional viewing.

### Posit, "Strategic Budget Optimization through Marketing Mix Modeling" (February 2026)
- **Source:** Posit Open Source (Isabella Velasquez and Daniel Chen), 2026, video (about 60 minutes, free, intermediate; R and Python).
- **Link:** https://opensource.posit.co/resources/videos/2026-02-25_strategic-budget-optimization-through-marketing-mix-modeling-mmm/ (search-confirmed)
- **Why it matters:** Recent, tool-focused session on turning MMM output into a constrained budget plan.
- **Use in course:** S3 viewing.

### Coursera, "Forecasting Models for Marketing Decisions" (Emory University)
- **Source:** Emory University on Coursera, 2023, MOOC (4 modules, roughly 10 to 15 hours, beginner to intermediate, free to audit, certificate paid; part of Foundations of Marketing Analytics specialisation).
- **Link:** https://www.coursera.org/learn/forecasting-models-marketing-decisions (search-confirmed)
- **Why it matters:** Regression-based forecasting for marketing mix decisions in a business-school framing; closest MOOC match to S4.
- **Use in course:** S4 supplementary.

### Coursera, "Data Analytics Methods for Marketing" (Meta)
- **Source:** Meta on Coursera, 2022, MOOC (about 20 hours, beginner, free to audit; module on marketing mix modelling and attribution).
- **Link:** https://www.coursera.org/learn/data-analytics-methods-for-marketing (search-confirmed)
- **Why it matters:** Platform-side view of MMM, incrementality and attribution; useful for students without a stats background.
- **Use in course:** Background for weaker students.

### LinkedIn Learning, "Marketing Attribution and Mix Modeling" (Michael Taylor) and "Introduction to Attribution and Mix Modeling" (Corey Koberg)
- **Source:** LinkedIn Learning, 2023 to 2024, video courses (1 h 38 min and 1 h 41 min, intermediate, subscription or free trial; certificates).
- **Link:** https://www.linkedin.com/learning/marketing-attribution-and-mix-modeling (search-confirmed) ; https://www.linkedin.com/learning/introduction-to-attribution-and-mix-modeling (search-confirmed)
- **Why it matters:** Taylor's course does a simple MMM with diminishing-returns transformations and scenario forecasting in a spreadsheet; Koberg's covers how MTA and MMM fit together. Short enough to assign fully.
- **Use in course:** S5 (attribution) pre-reading. WU may have LinkedIn Learning access via the library.

### Udemy, "MMM Masterclass: Facebook Robyn Tutorial for Marketing" and "Fundamentals of Marketing Mix Modeling: Learn by Doing" (MASS Analytics)
- **Source:** Udemy, 2022 to 2025, video courses (typically 3 to 6 hours, intermediate; paid, often discounted to under EUR 20; MASS course includes a 2-week MassTer licence).
- **Link:** https://www.udemy.com/course/mmm-masterclass-facebook-robyn-tutorial-for-marketing/ (search-confirmed) ; https://www.udemy.com/course/fundamentals-of-mmm/ (search-confirmed)
- **Why it matters:** Cheapest structured hands-on routes into Robyn (R) and a GUI MMM tool respectively. A Japanese-language "Excel x Python MMM" course also exists for complete beginners.
- **Use in course:** Optional self-study.

### DataCamp, "Building Response Models in R"
- **Source:** DataCamp, 2019, interactive course (4 hours, intermediate, subscription; DataCamp Classrooms gives free access to university instructors and their students).
- **Link:** https://www.datacamp.com/courses/building-response-models-in-r (search-confirmed)
- **Why it matters:** Market response modelling with price and promotion effects, the closest DataCamp has to MMM; no Python MMM course exists there, though their "Decoding Marketing Mix Modeling" tutorial is a short free read.
- **Use in course:** S1 supplementary; apply for DataCamp Classrooms if the cohort wants R.

### edX, "Fundamentals of Digital Marketing" (University of Maryland)
- **Source:** University of Maryland on edX, 2021 to 2024, MOOC (about 4 weeks, beginner, free to audit).
- **Link:** https://www.edx.org/learn/digital-marketing/the-university-of-maryland-college-park-fundamentals-of-digital-marketing (search-confirmed)
- **Why it matters:** Only edX course found that explicitly covers attribution and MMM; conceptual, not quantitative.
- **Use in course:** Background only.

### Industry conference content: Meta MMM Summit highlights and JSM 2025 Meridian session
- **Source:** Recast summary of Meta's Marketing Mix Modeling Summit (panels with Nielsen, Accenture, Ekimetrics), 2024; American Statistical Association JSM 2025 session "Meridian: Google's Open-Source MMM" (abstract only).
- **Link:** https://getrecast.com/meta-mmm-summit/ (search-confirmed) ; https://ww2.amstat.org/meetings/jsm/2025/onlineprogram/abstract.cfm?sid=2361&tid=2363 (search-confirmed)
- **Why it matters:** No dedicated "MMM conference" with public video archive exists; these two are the best proxies for what vendors and statisticians are debating (granularity, calibration, reach and frequency).
- **Use in course:** Background; discussion prompts.

---

## Gaps and caveats

The session's network proxy blocked direct fetches of most non-GitHub and non-PyPI domains (Google developer docs, pymc-marketing.io, research.google, getrecast.com, mass-analytics.com, coursera.org, udemy.com, linkedin.com, youtube.com, otexts.com, vendor sites), so those links are confirmed from search-engine result listings rather than page loads and are marked "(search-confirmed)"; the web-search budget was also exhausted before every course could be checked for current length, price and date. Version numbers and dates for all Python packages were read from PyPI on 5 October 2026 and are reliable; Robyn R 3.12.0 is from the GitHub releases page. Not verified: the GitHub repository for Lifesight's "Horizon" engine (announced but not visible on their organisation page), the licence of the Heusch mmm-materials repo, the exact scope of Keen's and Cassandra's free-access offers, the recording link for the 2022 PyMC Labs MMM meetup and the PyData NYC 2024 talk, and the channels behind the two third-party Meridian YouTube tutorials. CXL has no dedicated MMM course (only general analytics and growth tracks), and DataCamp has no Python MMM course. Paywalled items: Hanssens et al. (Springer), Tellis (Sage), Gelman and Hill (Cambridge), Shao and Li (ACM), Anderl et al. (Elsevier); everything from Google Research, arXiv, AEA (JEL) and Project Euclid is free. Commercial pricing figures (Measured from about USD 50k per year, MassTer about GBP 12k per year) come from third-party listings and change often. Session numbers (S1 to S5) assume the mapping stated at the top of this file.
