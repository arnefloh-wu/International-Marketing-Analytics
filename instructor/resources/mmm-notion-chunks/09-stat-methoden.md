### stat. Methoden (18)
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
		<td>stat. Methoden</td>
		<td>OLS and log-log (constant elasticity) response models</td>
		<td>Hanssens, Parsons and Schultz, 2001, book (Market Response Models, 2nd ed., Springer, chapters on functional forms); Tellis, 2006, book chapter ("Modeling Marketing Mix", Handbook of Marketing Research, Sage).</td>
		<td>[https://www.springer.com/us/book/9780792378266](https://www.springer.com/us/book/9780792378266)</td>
		<td>Defines the linear, multiplicative (log-log) and semi-log forms, elasticities and the economics behind them; Tellis is the compact 17-page primer.</td>
		<td>S1 reading; statsmodels lab. Paywalled (library access).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Adstock variants (geometric, delayed, Weibull)</td>
		<td>Jin, Wang, Sun, Chan and Koehler, 2017, paper (Google Research technical report); Robyn documentation, "Key features" (geometric and Weibull adstock).</td>
		<td>[https://research.google/pubs/bayesian-methods-for-media-mix-modeling-with-carryover-and-shape-effects/](https://research.google/pubs/bayesian-methods-for-media-mix-modeling-with-carryover-and-shape-effects/)</td>
		<td>Jin et al. formalise carryover (geometric and delayed adstock) and shape effects in one Bayesian model; Robyn's docs explain the Weibull PDF and CDF variants used in practice.</td>
		<td>S2 core reading.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Hill and logistic saturation</td>
		<td>Jin et al., 2017 (as above, Hill shape function); Google Meridian documentation, "Media saturation and lagging".</td>
		<td>[https://developers.google.com/meridian/docs/advanced-modeling/media-saturation-lagging](https://developers.google.com/meridian/docs/advanced-modeling/media-saturation-lagging)</td>
		<td>Hill(x; ec, slope) with half-saturation point and slope is now the default in Meridian and Robyn; the docs show how it interacts with adstock and why the two are hard to separate.</td>
		<td>S2 lab (plot response curves, derive marginal ROI).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Ridge regression with hyperparameter search (Robyn approach)</td>
		<td>Hastie, Tibshirani and Friedman, 2009, book (Elements of Statistical Learning, 2nd ed., section 3.4 shrinkage methods, free PDF); Zhou et al., 2024, paper ("Packaging Up Media Mix Modeling: An Introduction to Robyn's Open-Source Approach", arXiv 2403</td>
		<td>[https://hastie.su.domains/ElemStatLearn/](https://hastie.su.domains/ElemStatLearn/)</td>
		<td>ESL gives the L2 penalty and bias-variance trade-off; the Robyn paper documents the Nevergrad multi-objective search over adstock, Hill and lambda and the model-selection criteria.</td>
		<td>S2 reading; compare with Bayesian priors.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Hierarchical Bayesian regression (geo-level MMM)</td>
		<td>Sun, Wang, Jin, Chan and Koehler, 2017, paper (Geo-level Bayesian Hierarchical Media Mix Modeling, Google); Wang, Jin, Sun, Chan and Koehler, 2017, paper (hierarchical approach using category data).</td>
		<td>[https://research.google/pubs/geo-level-bayesian-hierarchical-media-mix-modeling/](https://research.google/pubs/geo-level-bayesian-hierarchical-media-mix-modeling/)</td>
		<td>The basis of Meridian: sub-national or multi-country units share priors, which tightens credible intervals and protects against unsound reallocation. The category paper shows how to borrow strength across brands or markets via informative priors.</td>
		<td>S3 core reading for cross-country allocation.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Time-varying coefficients and Gaussian processes</td>
		<td>Ng, Wang and Dai, 2021, paper (Bayesian Time Varying Coefficient Model with Applications to MMM, AdKDD 2021, arXiv 2106.03322); PyMC-Marketing notebook "MMM with time-varying parameters" (HSGP); Rasmussen and Williams, 2006, book (GPML, free PDF).</td>
		<td>[https://arxiv.org/pdf/2106.03322](https://arxiv.org/pdf/2106.03322)</td>
		<td>Media effectiveness drifts; KTR (Orbit) and HSGP (PyMC-Marketing) are the two practical ways to let coefficients or baselines move smoothly over time.</td>
		<td>S2 advanced demo; S4 link to forecasting.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Fourier seasonality</td>
		<td>Hyndman and Athanasopoulos, 2021, book (Forecasting: Principles and Practice, 3rd ed., chapter 7 "Time series regression models", section on Fourier terms, free online); Taylor and Letham, 2018, article (Forecasting at Scale, The American Statisticia</td>
		<td>[https://otexts.com/fpp3/useful-predictors.html](https://otexts.com/fpp3/useful-predictors.html)</td>
		<td>Fourier pairs are how Prophet, PyMC-Marketing and Meridian represent yearly seasonality with few parameters; fpp3 explains the choice of K.</td>
		<td>S2 and S4.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Panel fixed effects and partial pooling</td>
		<td>Gelman and Hill, 2007, book (Data Analysis Using Regression and Multilevel/Hierarchical Models, Cambridge, chapter 12 on partial pooling); linearmodels documentation (PanelOLS fixed effects).</td>
		<td>[https://assets.cambridge.org/97805218/67061/frontmatter/9780521867061_frontmatter.pdf](https://assets.cambridge.org/97805218/67061/frontmatter/9780521867061_frontmatter.pdf)</td>
		<td>Makes the link between country fixed effects (no pooling), pooled OLS (complete pooling) and hierarchical priors (partial pooling), which is the central modelling decision in a multi-country MMM.</td>
		<td>S3 reading and lab. Gelman and Hill is paywalled; chapter 12 circulates as a PDF in many course sites.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Budget optimisation under constraints</td>
		<td>PyMC-Marketing notebook "Budget Allocation with PyMC-Marketing" (SLSQP with bounds and custom constraints, plus risk assessment and multi-objective variants); Google Meridian docs "Budget optimization scenarios" (fixed versus flexible budget, minimal</td>
		<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_budget_allocation_example.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_budget_allocation_example.html)</td>
		<td>Both docs show the same mathematics (maximise expected response subject to total budget and per-channel bounds) in code students can run, including uncertainty in the optimum.</td>
		<td>S3 lab (allocate across countries and channels with floor and cap constraints).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Forecasting with ETS, ARIMA and regression</td>
		<td>Hyndman and Athanasopoulos, 2021, book (fpp3 chapters 8 "Exponential smoothing", 9 "ARIMA models", 10 "Dynamic regression models"); StatsForecast documentation.</td>
		<td>[https://otexts.com/fpp3/](https://otexts.com/fpp3/)</td>
		<td>The standard, free text; dynamic regression (ARIMA errors with media regressors) is the bridge between forecasting and MMM.</td>
		<td>S4 core reading and lab.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Difference-in-differences</td>
		<td>Roth, Sant'Anna, Bilinski and Poe, 2023, article (What's trending in difference-in-differences? Journal of Econometrics 235(2), 2218 to 2244); CausalPy documentation.</td>
		<td>[https://doi.org/10.1016/j.jeconom.2023.03.008](https://doi.org/10.1016/j.jeconom.2023.03.008)</td>
		<td>Synthesises staggered adoption, parallel-trends violations and inference, with practitioner recommendations; CausalPy implements standard and staggered DiD.</td>
		<td>S5 reading and lab.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Synthetic control</td>
		<td>Abadie, 2021, article (Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects, Journal of Economic Literature 59(2), 391 to 425, open access); Brodersen et al., 2015, article (CausalImpact, Annals of Applied Statistics 9</td>
		<td>[https://www.aeaweb.org/articles?id=10.1257/jel.20191450](https://www.aeaweb.org/articles?id=10.1257/jel.20191450)</td>
		<td>Abadie is the definitive guide to when synthetic control is credible (donor pool, pre-period fit, placebo tests); Brodersen gives the Bayesian state-space version used in CausalImpact.</td>
		<td>S5 reading; CausalPy and tfcausalimpact labs.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Geo experiments and power</td>
		<td>Vaver and Koehler, 2011, paper (Measuring Ad Effectiveness Using Geo Experiments, Google); Chen and Au, 2022, article (Robust causal inference for incremental return on ad spend with randomized paired geo experiments, Annals of Applied Statistics 16(</td>
		<td>[https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/)</td>
		<td>Vaver and Koehler is the original geo-based regression design; Trimmed Match adds robust paired designs and power-based pair selection. GeoLift's power tools and Haus's primers build on both.</td>
		<td>S5 core reading; power-calculation exercise with GeoLift or Trimmed Match.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Logistic (data-driven) attribution</td>
		<td>Shao and Li, 2011, paper (Data-driven multi-touch attribution models, KDD 2011, pages 258 to 264).</td>
		<td>[https://doi.org/10.1145/2020408.2020453](https://doi.org/10.1145/2020408.2020453)</td>
		<td>The first data-driven MTA: bagged logistic regression on touchpoint exposure plus a probabilistic second-order model for credit assignment; the reference point for all later MTA work.</td>
		<td>S5 reading. ACM paywall (library access).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Shapley value attribution</td>
		<td>Zhao, Mahboobi and Bagheri, 2018, paper (Shapley Value Methods for Attribution Modeling in Online Advertising, arXiv 1804.05327).</td>
		<td>[https://arxiv.org/abs/1804.05327](https://arxiv.org/abs/1804.05327)</td>
		<td>Clear derivation of ordered and unordered Shapley attribution with an efficient computation; the method behind Google Analytics' former data-driven attribution.</td>
		<td>S5 lab (compute Shapley credit on a synthetic journey dataset). Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Markov chain attribution</td>
		<td>Anderl, Becker, von Wangenheim and Schumann, 2016, article (Mapping the customer journey: Lessons learned from graph-based online attribution modeling, International Journal of Research in Marketing 33(3), 457 to 474).</td>
		<td>[https://www.sciencedirect.com/science/article/abs/pii/S0167811616300349](https://www.sciencedirect.com/science/article/abs/pii/S0167811616300349)</td>
		<td>The removal-effect Markov attribution framework, from a German research team (Passau and ETH), with first- and higher-order chains and spillover findings; the basis of the R ChannelAttribution package.</td>
		<td>S5 reading. Elsevier paywall (WU library).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Calibration with lift tests</td>
		<td>Zhang, Wurm, Li, Wakim, Kelly, Price and Liu, 2024, paper (Media Mix Model Calibration With Bayesian Priors, Google Research); PyMC-Marketing notebooks "Lift test calibration" and "Mitigating unobserved confounders with lift test likelihoods".</td>
		<td>[https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/](https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/)</td>
		<td>Reparametrising channel effects as ROI and placing experiment-informed priors on them is now the industry standard (Meridian ROI priors, Robyn calibration); the PyMC-Marketing notebooks show it in code with simulated confounding.</td>
		<td>S5 lab linking experiments back into the MMM.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>stat. Methoden</td>
		<td>Identifiability and multicollinearity diagnostics</td>
		<td>Chan and Perry, 2017, paper (Challenges and Opportunities in Media Mix Modeling, Google); Chen, Chan, Perry, Jin, Sun, Wang and Koehler, 2018, paper (Bias Correction for Paid Search in Media Mix Modeling, arXiv 1807.03292); statsmodels VIF.</td>
		<td>[https://research.google/pubs/challenges-and-opportunities-in-media-mix-modeling/](https://research.google/pubs/challenges-and-opportunities-in-media-mix-modeling/)</td>
		<td>Chan and Perry list the structural problems (collinear spend, selection bias, limited variation, ad-hoc functional forms); the paid-search paper gives a back-door correction. Together with VIF and prior-posterior checks they are the honest "what can this model not tell you" session.</td>
		<td>S2 reading and a diagnostics checklist students apply to their own model.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
</table>