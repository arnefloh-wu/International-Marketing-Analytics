### Software (23)
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
		<td>PyMC-Marketing</td>
		<td>PyMC Labs, 2023 to 2026, software (Python, Apache 2.0). Latest release 1.2.0, 29 September 2026; requires Python 3.12 or newer.</td>
		<td>[https://pypi.org/project/pymc-marketing/](https://pypi.org/project/pymc-marketing/)</td>
		<td>The most complete open Bayesian MMM in Python: pluggable adstock and saturation, lift-test calibration, time-varying intercept and media effects via Hilbert-space Gaussian processes, budget optimiser with constraints, multidimensional (geo-level) MMM, plus CLV models. Mature, actively released, excellent example notebooks.</td>
		<td>S2 and S3 main lab tool; S5 calibration lab. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Google Meridian</td>
		<td>Google, 2025 to 2026, software (Python on TensorFlow Probability, Apache 2.0). Latest release 2.1.0, 25 September 2026; Python 3.10 or newer (repo states 3.11 to 3.13).</td>
		<td>[https://pypi.org/project/google-meridian/](https://pypi.org/project/google-meridian/)</td>
		<td>Geo-level hierarchical Bayesian MMM with Hill saturation, adstock, ROI priors, reach and frequency, and a fixed or flexible budget optimiser with ROI constraints. The natural "international" tool: geos (countries, regions) are first-class and partially pooled. Replaces LightweightMMM.</td>
		<td>S3 lab (multi-country allocation) and comparison with PyMC-Marketing. Free; GPU helpful but not required for the demo data.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Orbit (KTR) by Uber</td>
		<td>Uber, 2020 to 2026, software (Python, Apache 2.0). Latest 1.1.5.1, 22 May 2026; Python 3.12 or newer.</td>
		<td>[https://pypi.org/project/orbit-ml/](https://pypi.org/project/orbit-ml/)</td>
		<td>Bayesian time-series package whose Kernel Time-varying Regression (KTR) model is the reference implementation of the Ng, Wang and Dai (2021) time-varying coefficient MMM. Also provides ETS, LGT and DLT forecasters.</td>
		<td>S4 (forecasting) and an advanced S2 demo of time-varying media effects. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>CausalPy</td>
		<td>PyMC Labs, 2022 to 2026, software (Python, Apache 2.0). Latest 0.9.0, 28 July 2026.</td>
		<td>[https://pypi.org/project/CausalPy/](https://pypi.org/project/CausalPy/)</td>
		<td>One API for difference-in-differences (including staggered), synthetic control, geographical lift, interrupted time series, regression discontinuity, IV and IPW, with PyMC (Bayesian) or scikit-learn (OLS) back ends. Ideal for teaching quasi-experiments without R.</td>
		<td>S5 lab (DiD, synthetic control on a country roll-out). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>GeoLift</td>
		<td>Meta (facebookincubator), 2021 to 2026, software (R, GPL 2 or later; version 2.7.5 in DESCRIPTION).</td>
		<td>[https://github.com/facebookincubator/GeoLift](https://github.com/facebookincubator/GeoLift)</td>
		<td>End-to-end geo-experiment toolkit built on augmented synthetic control: power analysis and market selection, test design, lift inference and plots. Needs 25 or more pre-periods and about 20 or more geo units, which is a useful teaching constraint. R only.</td>
		<td>S5 reading and optional R demo; pair with CausalPy or Google's Trimmed Match (https://github.com/google/trimmed_match, Python, Apache 2.0) for a Python path.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>CausalImpact (tfcausalimpact Python port)</td>
		<td>Willian Fuks (port of Google's R CausalImpact, Brodersen et al. 2015), 2020 to 2026, software (Python, Apache 2.0). Latest 0.0.19, 20 September 2026.</td>
		<td>[https://pypi.org/project/tfcausalimpact/](https://pypi.org/project/tfcausalimpact/)</td>
		<td>Bayesian structural time-series counterfactual for a single treated series with control series, with results documented as equivalent to the R original. Good for "what did the campaign or price change do" questions where no geo split exists.</td>
		<td>S5 short lab. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>statsmodels</td>
		<td>statsmodels developers, 2009 to 2026, software (Python, BSD 3-clause). Latest 0.15.0, 27 August 2026.</td>
		<td>[https://pypi.org/project/statsmodels/](https://pypi.org/project/statsmodels/)</td>
		<td>OLS and log-log elasticities with proper inference tables, HAC standard errors, VIF and condition numbers for multicollinearity diagnostics, ETS and SARIMAX for forecasting. The baseline every MMM should be compared against.</td>
		<td>S1 lab (first MMM as OLS), S4 forecasting baselines. Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>linearmodels</td>
		<td>Kevin Sheppard, 2017 to 2025, software (Python, NCSA licence). Latest 7.0, 21 October 2025.</td>
		<td>[https://pypi.org/project/linearmodels/](https://pypi.org/project/linearmodels/)</td>
		<td>Panel estimators that statsmodels lacks: one- and two-way fixed effects, first differences, between and pooled, plus IV and system estimators, with clustered standard errors. The frequentist counterpart to partial pooling for country-by-week panels.</td>
		<td>S3 lab (country fixed effects versus hierarchical priors). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Prophet and StatsForecast (forecasting baselines)</td>
		<td>Meta (Prophet 1.5.0, 5 October 2026, MIT) and Nixtla (StatsForecast 2.1.1, 16 July 2026, Apache 2.0), software (Python).</td>
		<td>[https://pypi.org/project/prophet/](https://pypi.org/project/prophet/)</td>
		<td>Prophet gives an additive trend plus Fourier seasonality plus holidays model with regressors, which doubles as an intuition builder for MMM baselines. StatsForecast gives fast AutoARIMA, AutoETS, Theta and CES with exogenous regressors across hundreds of country series at once.</td>
		<td>S4 lab (country-level demand forecasts feeding budget scenarios). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Synthetic MMM benchmark generators</td>
		<td>Niklas Heusch, 2026, software and paper (Jupyter, generator for "A Synthetic Benchmark Dataset with Endogenous Marketing Spend for Validating MMMs", arXiv 2608.21130); Meta siMMMulator (R, MIT); PyMC Labs mmm-param-recovery (Python, Apache 2.0, compa</td>
		<td>[https://github.com/niklas-heusch/mmm-materials](https://github.com/niklas-heusch/mmm-materials)</td>
		<td>Ground-truth data is the only way to grade an MMM. Heusch's generator is the first with endogenous spend (budget feedback, promo-calendar anticipation, TV bursts, performance chasing) plus simulated go-dark geo tests, which is exactly the confounding students need to see. No licence file shown on the Heusch repo.</td>
		<td>S2 and S3 assignments (fit a model, compare to known ROI); S5 for simulated geo tests. Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Mutinex (GrowthOS)</td>
		<td>Mutinex, Sydney, 2020 to 2026, software and vendor (continuous MMM, scenario planning, agency partnerships such as dentsu).</td>
		<td>[https://mutinex.co/product/growthos/](https://mutinex.co/product/growthos/)</td>
		<td>Example of "always-on" MMM delivered as a platform with confidence intervals on scenarios; strong APAC and multi-market footprint. No academic programme found.</td>
		<td>Background; vendor-landscape slide in S3.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Cassandra</td>
		<td>Cassandra (cassandra.app), 2021 to 2026, software and vendor (no-code Bayesian MMM and geo incrementality; now offers a Meridian-based model).</td>
		<td>[https://cassandra.app/marketing-mix-model](https://cassandra.app/marketing-mix-model)</td>
		<td>Shows how open-source engines (Meridian) are wrapped into SaaS. Markets a free entry tier ("Your MMM in 10 minutes"), which could give students a hands-on UI without code (terms unverified).</td>
		<td>S3 demo of a vendor UI versus a notebook; check the free tier before class.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Sellforte</td>
		<td>Sellforte, Espoo (Finland), 2017 to 2026, software and vendor (SaaS MMM, daily forecasts, incrementality tests, "agentic" media planner).</td>
		<td>[https://sellforte.com/](https://sellforte.com/)</td>
		<td>European SaaS MMM with public explainer content, including a page on Meridian and a note on data granularity; clients across Nordics and Baltics (Musti Group, Finnish Design Shop) give a multi-country angle.</td>
		<td>Background; strong European guest-talk candidate (Helsinki, remote).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Analytic Partners (GPS Enterprise)</td>
		<td>Analytic Partners, New York with European offices, 1999 to 2026, software and vendor (GPS-Enterprise platform, ROI Genome benchmarks; Gartner MMM leader).</td>
		<td>[https://analyticpartners.com/solutions/marketing-mix-modeling/](https://analyticpartners.com/solutions/marketing-mix-modeling/)</td>
		<td>The large-enterprise "commercial analytics" model: data ingestion to optimisation, cross-market benchmarks (ROI Genome). Useful for discussing what enterprises buy versus what open source gives.</td>
		<td>Background; S3 vendor landscape.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Nielsen MMM (now Circana)</td>
		<td>Nielsen, then Circana (acquisition completed 21 August 2025), vendor and report. Nielsen "Marketing Mix Modeling Best Practices" guide, 2022.</td>
		<td>[https://www.nielsen.com/wp-content/uploads/sites/2/2022/09/Marketing-Mix-Modeling-Best-Practices-EN.pdf](https://www.nielsen.com/wp-content/uploads/sites/2/2022/09/Marketing-Mix-Modeling-Best-Practices-EN.pdf)</td>
		<td>Decades of multi-country MMM practice; the best-practices PDF is a short, readable client-side checklist (granularity, data requirements). Note the ownership change when citing.</td>
		<td>S1 or background reading.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Ipsos MMA</td>
		<td>Ipsos MMA, 1990s to 2026, vendor (unified marketing measurement; Gartner MMM Magic Quadrant leader 2024 and 2025).</td>
		<td>[https://mma.com/resources/analytic-fundamentals-what-is-marketing-mix-modeling/](https://mma.com/resources/analytic-fundamentals-what-is-marketing-mix-modeling/)</td>
		<td>Clear statement of "unified measurement" (MMM plus attribution plus tests in one framework), the vendor positioning students will meet in practice.</td>
		<td>S5 reading on triangulation; background.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Measured</td>
		<td>Measured, 2017 to 2026, software and vendor (incrementality testing platform with test-calibrated MMM; pricing reported from about USD 50k per year).</td>
		<td>[https://www.measured.com/media-mix-modeling/](https://www.measured.com/media-mix-modeling/)</td>
		<td>Good public FAQ material on when to use incrementality tests, attribution or MMM, and ten real-world MMM examples.</td>
		<td>S5 reading; background.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Haus</td>
		<td>Haus, 2021 to 2026, software and vendor (geo incrementality experiments, "causal MMM"; USD 55m funding to 2025).</td>
		<td>[https://www.haus.io/incrementality-101](https://www.haus.io/incrementality-101)</td>
		<td>Their "Incrementality 101" and geo-experiment fundamentals posts are short, well written primers on design, power and synthetic control in business language.</td>
		<td>S5 pre-reading for the geo-experiment session.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Lifesight</td>
		<td>Lifesight, Singapore and US, 2016 to 2026, software and vendor (no-code causal MMM, incrementality, attribution). Maintains the CC0 "awesome-marketing-measurement" list on GitHub.</td>
		<td>[https://github.com/lifesight/awesome-marketing-measurement](https://github.com/lifesight/awesome-marketing-measurement)</td>
		<td>The awesome list (15 sections: open-source MMM, geo experiments, attribution, datasets, papers, courses, communities) is a handy vendor-neutral index for students. Lifesight announced an open-source forecasting engine "Horizon" but no repository was visible on their GitHub organisation (unverified).</td>
		<td>Background; give students the awesome list in week 1.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>MASS Analytics (MassTer)</td>
		<td>MASS Analytics (Dr Ramla Jarrar), London and Tunis, 2010s to 2026, software and vendor (MassTer MMM desktop software, Bayesian and hierarchical options; MMM Academy).</td>
		<td>[https://mass-analytics.com/solutions](https://mass-analytics.com/solutions)</td>
		<td>One of the few vendors that packages teaching with the tool: free YouTube course, paid academy with certificate and software access, 2-week MassTer trial licences with their Udemy course. Listed price about GBP 12,000 per year; no formal academic licence found, worth asking.</td>
		<td>S2 reading (free course videos); vendor demo candidate. Trial licence free for two weeks.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Ekimetrics (Eki.Decisions)</td>
		<td>Ekimetrics, Paris (offices in London, New York, Dubai), 2006 to 2026, vendor and consultancy (MMM core with modules; Gartner "Visionary" 2025; Meta and TikTok measurement partner).</td>
		<td>[https://www.ekimetrics.com/solutions/marketing-effectiveness](https://www.ekimetrics.com/solutions/marketing-effectiveness)</td>
		<td>European leader in multi-market MMM for FMCG and luxury; co-author of the Artefact and Meta Robyn comparison study. Their "Bayesian MMM with limited data" style posts are useful for small-country models.</td>
		<td>Background; European guest-talk candidate (Paris).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Keen Decision Systems</td>
		<td>Keen, Durham NC, 2010 to 2026, software and vendor (adaptive Bayesian MMM with real-time scenario planning).</td>
		<td>[https://keends.com/news/free-access-to-mmm/](https://keends.com/news/free-access-to-mmm/)</td>
		<td>Announced a free-access MMM programme (scope unverified); a mid-market example of self-serve forecasting and planning.</td>
		<td>Background; check the free-access terms for a student exercise.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Artefact</td>
		<td>Artefact, Paris, 2015 to 2026, consultancy and vendor (Google Meridian certified; custom hierarchical Bayesian and graphical causal MMM; Robyn versus GCM study with Meta on five international FMCG brands).</td>
		<td>[https://www.artefact.com/news/artefact-achieves-google-meridian-certification/](https://www.artefact.com/news/artefact-achieves-google-meridian-certification/)</td>
		<td>Shows how consultancies build on open-source engines and where they add causal structure (DAGs). The five-brand international comparison is directly relevant.</td>
		<td>S2 or S5 reading; European guest-talk candidate.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
</table>