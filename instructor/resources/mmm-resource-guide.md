# Marketing mix modelling: resource guide

Compiled on 5 October 2026 by parallel research agents for the course International Marketing Analytics (WU Vienna). Entries are ranked best first within each section. Links marked (unverified) or search-confirmed could not be fetched from the build environment and should be checked once before use.

Total entries: 248; new relative to the existing Notion list: 237.

---

# Part 1: Books and journal articles

Scope: textbooks and practitioner books on market response and marketing mix modelling (MMM), plus the academic and industry research papers that the course should rest on. Entries are ranked best first within each section. "Verified" means the link or DOI appeared in a search result or was fetched; "(unverified)" means the detail comes from memory because the host was blocked (see Gaps and caveats).

Suggested session mapping used below: session 1 = foundations and response models; session 2 = Bayesian MMM in Python (adstock, saturation, priors); session 3 = budget allocation across channels and countries; session 4 = forecasting, experiments and calibration; session 5 = attribution and unified measurement.

## Books

### Market Response Models: Econometric and Time Series Analysis
- **Source:** Dominique M. Hanssens, Leonard J. Parsons, Randall L. Schultz, 2001, 2nd edition, Kluwer/Springer (International Series in Quantitative Marketing 12), book
- **Link:** https://books.google.com/books/about/Market_Response_Models.html?id=xZyJamKdpIsC (publisher page on link.springer.com not fetchable from here)
- **Why it matters:** Still the reference text for aggregate response modelling: sales response functions, lag structures (Koyck and adstock), elasticities, time-series methods (persistence, VAR) and how response models feed allocation decisions. Dense but exact; most Google and Meta MMM papers cite it.
- **Use in course:** Session 1 reading (chapters on response model specification and lag structures) and session 3 (decision models and allocation). Paywalled; library copy or e-book, roughly EUR 150 to 200 new.

### Modeling Markets: Analyzing Marketing Phenomena and Improving Marketing Decision Making
- **Source:** Peter S. H. Leeflang, Jaap E. Wieringa, Tammo H. A. Bijmolt, Koen H. Pauwels, 2015, Springer (International Series in Quantitative Marketing), book, DOI 10.1007/978-1-4939-2086-0 (verified via chapter link)
- **Link:** https://link.springer.com/book/10.1007/978-1-4939-2086-0
- **Why it matters:** The most teachable modern textbook on marketing models: specification, estimation, validation and use, with a full chapter of worked aggregate-demand models (chapter 7, "Examples of models for aggregate demand"). European authors, European examples.
- **Use in course:** Session 1 core reading (chapters on model building and aggregate demand), session 4 for validation chapters. WU library likely has Springer access; otherwise paywalled.

### Advanced Methods for Modeling Markets
- **Source:** Peter S. H. Leeflang, Jaap E. Wieringa, Tammo H. A. Bijmolt, Koen H. Pauwels (eds), 2017, Springer, edited book, DOI 10.1007/978-3-319-53469-5 (verified)
- **Link:** https://link.springer.com/book/10.1007/978-3-319-53469-5
- **Why it matters:** Companion volume with chapters on Bayesian analysis, time-series models, endogeneity, structural models and mixture models, each written by specialists. The Bayesian and endogeneity chapters are the academic bridge to Meridian and PyMC-Marketing.
- **Use in course:** Background for session 2 (Bayesian chapter) and session 4 (endogeneity, time series). Paywalled; Springer access needed.

### Python for Marketing Research and Analytics
- **Source:** Jason S. Schwarz, Chris Chapman, Elea McDonnell Feit, 2020, Springer, textbook with code, DOI 10.1007/978-3-030-49720-0 (verified); code at https://github.com/python-marketing-research/python-marketing-research-1ed (verified)
- **Link:** https://link.springer.com/book/10.1007/978-3-030-49720-0
- **Why it matters:** The only mainstream marketing analytics textbook written in Python (pandas, statsmodels, scikit-learn), by two Google researchers and a Penn professor. Covers data handling, linear models, model interpretation and segmentation with marketing data; no MMM chapter, but it sets the coding baseline. The R twin is Chapman and Feit, R for Marketing Research and Analytics, 2nd ed., 2019, Springer, with free slides and exercises at https://r-marketing.r-forge.r-project.org/ (verified).
- **Use in course:** Pre-course or session 1 lab warm-up (chapters on data wrangling and linear models). Paywalled book; GitHub notebooks are free.

### Forecasting: Principles and Practice (3rd edition)
- **Source:** Rob J. Hyndman, George Athanasopoulos, 2021, OTexts, open textbook (R; a Python edition is in progress at https://otexts.com/fpppy/ (unverified, site blocked here))
- **Link:** https://otexts.com/fpp3/ (confirmed via https://github.com/robjhyndman/fpp3)
- **Why it matters:** Free, rigorous and readable; the standard text for the forecasting half of the course (decomposition, ETS, ARIMA, regression with ARIMA errors, hierarchical and grouped forecasting across countries and products).
- **Use in course:** Session 4 reading (chapters on time series regression, ARIMA and hierarchical forecasting). Free.

### Bayesian Modeling and Computation in Python
- **Source:** Osvaldo A. Martin, Ravin Kumar, Junpeng Lao, 2021, Chapman and Hall/CRC, textbook, free online
- **Link:** https://bayesiancomputationbook.com (confirmed via https://github.com/BayesianModelingandComputationInPython/BookCode_Edition1)
- **Why it matters:** Written by PyMC and ArviZ core developers; covers priors, MCMC diagnostics, hierarchical models and time series in exactly the stack PyMC-Marketing uses. The practical companion for anyone fitting a Bayesian MMM.
- **Use in course:** Session 2 background (chapters on Bayesian inference, hierarchical models, model comparison). Free online; print edition paywalled.

### The Effect: An Introduction to Research Design and Causality
- **Source:** Nick Huntington-Klein, 2022, Chapman and Hall/CRC, textbook, free online with R, Stata and Python code
- **Link:** https://theeffectbook.net (site blocked from here; code and data verified at https://github.com/NickCH-K/causalbook and https://github.com/NickCH-K/causaldata)
- **Why it matters:** The friendliest serious causal-inference text; the chapters on difference-in-differences, synthetic control and event studies are exactly the toolkit behind geo experiments, GeoLift and CausalImpact.
- **Use in course:** Session 4 reading (difference-in-differences, synthetic control chapters) before the experiment lab. Free.

### Causal Inference for the Brave and True
- **Source:** Matheus Facure, 2022 onward, open online book in Python (the author's O'Reilly book Causal Inference in Python, 2023, is the paid version (unverified))
- **Link:** https://matheusfacure.github.io/python-causality-handbook/ (link verified via the awesome-marketing-measurement list)
- **Why it matters:** Python-first, notebook-based treatment of potential outcomes, regression, DiD, synthetic control and uplift, written by a practitioner; students can run every chapter.
- **Use in course:** Session 4 lab companion (synthetic control and DiD chapters). Free.

### Causal Inference: The Mixtape
- **Source:** Scott Cunningham, 2021, Yale University Press, textbook, free online with R, Stata and Python code
- **Link:** https://mixtape.scunning.com/ (link verified)
- **Why it matters:** Clear, example-driven treatment of DAGs, matching, DiD and synthetic control; the DAG chapter is the best short preparation for Meridian's causal-graph framing of MMM.
- **Use in course:** Background for session 4; assign the DAG and synthetic control chapters. Free online.

### Effective Advertising: Understanding When, How, and Why Advertising Works
- **Source:** Gerard J. Tellis, 2004, Sage, book
- **Link:** https://sk.sagepub.com/book/mono/effective-advertising/toc (verified)
- **Why it matters:** Synthesises decades of econometric and experimental evidence on advertising response: elasticities, carryover, wear-in and wear-out, and the comparison of field experiments with econometric estimates. The qualitative counterpart to the elasticity meta-analyses.
- **Use in course:** Session 1 background (chapters on advertising carryover and market-level effects). Paywalled; a scanned copy is on the Internet Archive lending library.

### Empirical Generalizations about Marketing Impact (2nd edition)
- **Source:** Dominique M. Hanssens (ed.), 2015, Marketing Science Institute (Relevant Knowledge Series), book
- **Link:** https://www.msi.org/events/empirical-generalizations-about-marketing-impact/ (verified)
- **Why it matters:** About 120 one-page empirical generalisations (advertising elasticity, price elasticity, carryover, long-term effects, cross-country patterns), each with references. Ideal for setting Bayesian priors and for sanity-checking student MMM output.
- **Use in course:** Session 2 (prior elicitation exercise) and session 3. Paid MSI publication (about USD 40 as e-book); short extracts are quotable.

### Principles of Marketing Engineering and Analytics (3rd edition)
- **Source:** Gary L. Lilien, Arvind Rangaswamy, Arnaud De Bruyn, 2017, DecisionPro, textbook with Excel tools (unverified)
- **Link:** https://www.decisionpro.biz (unverified)
- **Why it matters:** The classic "marketing engineering" treatment of response functions and resource allocation (ADBUDG-style curves, allocation across segments and regions) with managerial cases; useful to show the pre-Bayesian logic of budget optimisation.
- **Use in course:** Background for session 3. Paywalled, with a student software licence.

## Journal articles

**Foundations and classics**

### Aggregate Advertising Models: The State of the Art
- **Source:** John D. C. Little, 1979, Operations Research 27(4), 629 to 667, article
- **Link:** https://doi.org/10.1287/opre.27.4.629 (verified)
- **Why it matters:** The founding statement of what an advertising response model must capture: carryover, diminishing returns, competition, interaction and dynamics. Every adstock-plus-Hill MMM is a descendant.
- **Use in course:** Session 1 required reading (sections 1 to 4). Paywalled (INFORMS).

### Econometric Measurement of the Duration of Advertising Effect on Sales
- **Source:** Darral G. Clarke, 1976, Journal of Marketing Research 13(4), 345 to 357, article
- **Link:** https://doi.org/10.2307/3151017 (verified)
- **Why it matters:** Shows that implied carryover depends heavily on the data interval (the data-interval bias), which is still the main reason weekly MMMs and annual studies disagree on decay rates.
- **Use in course:** Session 1 or 2 reading when introducing adstock decay. Paywalled (Sage/JSTOR).

### The Persistence of Marketing Effects on Sales
- **Source:** Marnik G. Dekimpe, Dominique M. Hanssens, 1995, Marketing Science 14(1), 1 to 21, article
- **Link:** https://doi.org/10.1287/mksc.14.1.1 (DOI unverified)
- **Why it matters:** Introduces persistence modelling (unit roots, VAR, impulse responses) to separate short-run from long-run marketing effects; the methodological root of "long-term effects" claims in MMM.
- **Use in course:** Session 1 background; session 4 for time-series thinking. Paywalled.

### How Well Does Advertising Work? Generalizations from Meta-Analysis of Brand Advertising Elasticities
- **Source:** Raj Sethuraman, Gerard J. Tellis, Richard A. Briesch, 2011, Journal of Marketing Research 48(3), 457 to 471, article
- **Link:** https://doi.org/10.1509/jmkr.48.3.457 (verified); open copy https://gwern.net/doc/economics/advertising/2011-sethuraman.pdf (found in search, not fetched)
- **Why it matters:** Mean short-term advertising elasticity 0.12, long-term 0.24, with moderators (durables, life-cycle stage, data interval, GRPs versus money, Europe versus US). The best single source of priors for a Bayesian MMM.
- **Use in course:** Session 2 required reading (use the moderator table to set priors). Paywalled, open PDF available.

### A Meta-Analysis of Marketing Communication Carryover Effects
- **Source:** Christine Köhler, Murali K. Mantrala, Sönke Albers, Vamsi K. Kanuri, 2017, Journal of Marketing Research 54(6), article
- **Link:** https://doi.org/10.1509/jmr.13.0580 (verified)
- **Why it matters:** Meta-analysis of carryover (decay) estimates across media and countries; gives defensible ranges for adstock parameters and shows how data interval and model type bias them.
- **Use in course:** Session 2 (adstock priors); pairs with Clarke 1976. Paywalled.

### Demonstrating the Value of Marketing
- **Source:** Dominique M. Hanssens, Koen H. Pauwels, 2016, Journal of Marketing 80(6), 173 to 190, article
- **Link:** https://doi.org/10.1509/jm.15.0417 (verified); open copy https://www.anderson.ucla.edu/sites/default/files/documents/areas/fac/marketing/Dominique/2016%20JM%20Hanssens%20Pauwels.pdf (found in search, not fetched)
- **Why it matters:** Frames marketing accountability as a chain from spend to metrics to financial value and reviews what response models, attribution and experiments can and cannot show. A good opening reading for managers-in-training.
- **Use in course:** Session 1 reading. Paywalled, open PDF available.

### How T.V. Advertising Works: A Meta-Analysis of 389 Real World Split Cable T.V. Advertising Experiments
- **Source:** Leonard M. Lodish, Magid Abraham, Stuart Kalmenson, Jeanne Livelsberger, Beth Lubetkin, Bruce Richardson, Mary Ellen Stevens, 1995, Journal of Marketing Research 32(2), 125 to 139, article
- **Link:** https://doi.org/10.1177/002224379503200204 (DOI unverified)
- **Why it matters:** The classic experimental benchmark: about half of TV weight tests show no significant sales effect, and effects are larger for new products. Sets expectations before students see MMM ROI claims.
- **Use in course:** Session 4 background (experiments versus models). Paywalled.

**Bayesian and modern MMM**

### Bayesian Methods for Media Mix Modeling with Carryover and Shape Effects
- **Source:** Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan, Jim Koehler, 2017, Google research white paper
- **Link:** https://research.google/pubs/pub46001/ (verified); PDF https://storage.googleapis.com/gweb-research2023-media/pubtools/pdf/b20467a5c27b86c08cceed56fc72ceadb875184a.pdf (fetched)
- **Why it matters:** The canonical modern MMM specification: geometric or delayed adstock plus a Hill saturation curve, estimated with Bayesian methods, with ROAS and marginal ROAS derived from the posterior. LightweightMMM, PyMC-Marketing and Meridian all implement it.
- **Use in course:** Session 2 required reading; reproduce its simulated example in the PyMC-Marketing lab. Free.

### Geo-level Bayesian Hierarchical Media Mix Modeling
- **Source:** Yunting Sun, Yueqing Wang, Yuxue Jin, David Chan, Jim Koehler, 2017, Google research white paper
- **Link:** https://research.google/pubs/pub46000/ (verified)
- **Why it matters:** Pooling sub-national (geo) data in a hierarchical model gives tighter credible intervals than national data alone. This is the statistical justification for the country-by-region hierarchies in Meridian and for multi-country MMM.
- **Use in course:** Session 3 required reading (geo hierarchies across countries). Free.

### Challenges and Opportunities in Media Mix Modeling
- **Source:** David Chan, Michael Perry, 2017, Google research white paper
- **Link:** https://research.google/pubs/pub45998/ (verified)
- **Why it matters:** Short, honest list of why MMM is hard: limited variation, collinearity, selection bias (ads follow demand), funnel effects, paid search, and the need for experiments. Excellent framing paper.
- **Use in course:** Session 1 or 2 reading; discussion piece. Free.

### A Hierarchical Bayesian Approach to Improve Media Mix Models Using Category Data
- **Source:** Yueqing Wang, Yuxue Jin, Yunting Sun, David Chan, Jim Koehler, 2017, Google research white paper
- **Link:** https://research.google.com/pubs/archive/45999.pdf (found in search; host blocked from here)
- **Why it matters:** Uses category-level data across brands as a hierarchical prior to stabilise a single brand's MMM; a practical answer to short series, and the same logic applies to pooling across countries.
- **Use in course:** Session 3 background. Free.

### Introduction to the Aggregate Marketing System Simulator
- **Source:** Stephanie Zhang, Jon Vaver, 2017, Google research white paper; R package https://github.com/google/amss (verified, archived 2022)
- **Link:** https://research.google/pubs/introduction-to-the-aggregate-marketing-system-simulator/ (verified)
- **Why it matters:** A simulator that generates realistic aggregate marketing data with known ground-truth ROAS, so MMM methods can be tested. Ideal for teaching: students fit models to data where the true answer is known.
- **Use in course:** Session 2 or 4 lab (simulate, fit, compare to truth). Free, R.

### Bayesian Hierarchical Media Mix Model Incorporating Reach and Frequency Data
- **Source:** Yingxiang Zhang, Mike Wurm, Alexander Wakim, Eddie Li, Ying Liu, 2023, Google research white paper
- **Link:** https://research.google/pubs/bayesian-hierarchical-media-mix-model-incorporating-reach-and-frequency-data/ (verified)
- **Why it matters:** Extends the geo-hierarchical MMM to use reach and frequency instead of impressions, enabling optimal-frequency recommendations; this is the model inside Google Meridian (https://github.com/google/meridian, Apache-2.0, Python, verified).
- **Use in course:** Session 2 or 3 reading for the Meridian lab. Free.

### Packaging Up Media Mix Modeling: An Introduction to Robyn's Open-Source Approach
- **Source:** Julian Runge, Igor Skokan, Gufeng Zhou, Koen Pauwels, 2024, arXiv 2403.14674 (Meta Marketing Science and academia), working paper
- **Link:** https://arxiv.org/abs/2403.14674 (verified); package https://github.com/facebookexperimental/Robyn (MIT, R with Python beta, verified)
- **Why it matters:** The authoritative description of Robyn: ridge regression, evolutionary hyperparameter search, Prophet decomposition, calibration with experiments and budget allocation, and the organisational reasons for the design. Good contrast to the Bayesian school.
- **Use in course:** Session 2 reading (compare with Jin et al. 2017). Free.

### PyMC-Marketing: Bayesian marketing analytics in Python (JOSS)
- **Source:** PyMC Labs team, 2026 (year inferred from DOI series, unverified), Journal of Open Source Software, software paper
- **Link:** https://doi.org/10.21105/joss.10805 (DOI verified via the repository README); package https://github.com/pymc-labs/pymc-marketing (Apache-2.0, verified)
- **Why it matters:** The citable reference for the Python library the course will most likely use: adstock and saturation transforms, lift-test calibration, time-varying effects, multidimensional (geo) models and budget optimisation.
- **Use in course:** Session 2 lab citation. Free, open access.

### Bayesian Time Varying Coefficient Model with Applications to Marketing Mix Modeling
- **Source:** Edwin Ng, Zhishi Wang, Athena Dai (Uber), 2021, arXiv 2106.03322, working paper
- **Link:** https://arxiv.org/abs/2106.03322 (verified)
- **Why it matters:** Lets channel effectiveness drift over time via kernel-weighted regression, which matters for multi-year series and for markets in transition; also the basis of Uber's Orbit library.
- **Use in course:** Session 4 background (time-varying effects). Free.

### Hierarchical Marketing Mix Models with Sign Constraints
- **Source:** Hao Chen, Minguang Zhang, Lanshan Han, Alvin Lim (Google), 2021, Journal of Applied Statistics (DOI 10.1080/02664763.2021.1946020 unverified); preprint arXiv 2008.12802
- **Link:** https://arxiv.org/abs/2008.12802 (verified)
- **Why it matters:** Multi-region hierarchical MMM with sign constraints on media coefficients, estimated with a scalable algorithm; directly relevant to multi-country models where naive regression gives negative media effects.
- **Use in course:** Session 3 background. Free preprint.

### Your MMM is Broken: Identification of Nonlinear and Time-varying Effects in Marketing Mix Models
- **Source:** Ryan Dew, Nicolas Padilla, Anya Shchetkina (authors from memory, unverified), 2024, arXiv 2408.07678, working paper
- **Link:** https://arxiv.org/abs/2408.07678 (listing verified)
- **Why it matters:** Academic critique showing that standard MMMs cannot separately identify nonlinearity (saturation) from time variation without extra structure; a useful counterweight to vendor enthusiasm.
- **Use in course:** Session 2 or 4 discussion reading for stronger students. Free.

**Calibration with experiments and causal inference**

### A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook
- **Source:** Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava, Dan Chapsky, 2019, Marketing Science 38(2), 193 to 225, article
- **Link:** https://doi.org/10.1287/mksc.2018.1135 (verified); open copy https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf (listed, not fetched)
- **Why it matters:** Fifteen large Facebook experiments show that observational methods (matching, regression, last click) often miss true lift by a wide margin. The paper students should read before trusting any attribution or uncalibrated model.
- **Use in course:** Session 4 required reading. Paywalled, open PDF available.

### Close Enough? A Large-Scale Exploration of Non-Experimental Approaches to Advertising Measurement
- **Source:** Brett R. Gordon, Robert Moakler, Florian Zettelmeyer, 2023, Marketing Science 42(4), 768 to 793, article
- **Link:** https://doi.org/10.1287/mksc.2022.1413 (verified)
- **Why it matters:** Follow-up on 663 experiments: even with rich data, non-experimental estimates are frequently far off, which motivates calibrating MMM with lift tests.
- **Use in course:** Session 4 reading (pairs with Gordon et al. 2019). Paywalled.

### TV Advertising Effectiveness and Profitability: Generalizable Results from 288 Brands
- **Source:** Bradley T. Shapiro, Günter J. Hitsch, Anna E. Tuchman, 2021, Econometrica 89(4), 1855 to 1879, article
- **Link:** https://doi.org/10.3982/ECTA17674 (verified); open working paper https://economics.sas.upenn.edu/system/files/2021-02/Ad-Effects-Generalizable-Robust-Revision-3-Jan-29.pdf (listed, not fetched)
- **Why it matters:** Panel-based causal estimates of TV elasticities for 288 brands; median elasticity is small and marginal ROI is negative for most brands. A sobering benchmark for MMM ROI outputs and budget recommendations.
- **Use in course:** Session 3 reading (budget allocation reality check). Paywalled, open PDF available.

### Measuring Ad Effectiveness Using Geo Experiments
- **Source:** Jon Vaver, Jim Koehler, 2011, Google research white paper
- **Link:** https://research.google/pubs/pub38355/ (verified); R package https://github.com/google/GeoexperimentsResearch (verified, archived)
- **Why it matters:** The original geo-experiment design and geo-based regression (GBR) analysis; the template for every geo-lift test now used to calibrate MMMs.
- **Use in course:** Session 4 required reading before the geo-experiment lab. Free.

### Estimating Ad Effectiveness Using Geo Experiments in a Time-Based Regression Framework
- **Source:** Jouni Kerman, Peng Wang, Jon Vaver, 2017, Google research white paper
- **Link:** https://research.google/pubs/pub45950/ (verified)
- **Why it matters:** Time-based regression (TBR) for geo tests with few regions, estimating the cumulative causal effect from a counterfactual time series; the method behind many European geo tests where countries have few media regions.
- **Use in course:** Session 4 reading. Free.

### Robust Causal Inference for Incremental Return on Ad Spend with Randomized Paired Geo Experiments
- **Source:** Aiyou Chen, Timothy C. Au, 2022, Annals of Applied Statistics 16(1), article; preprint arXiv 1908.02922; Python package https://github.com/google/trimmed_match (verified)
- **Link:** https://doi.org/10.1214/21-AOAS1493 (verified via search listing)
- **Why it matters:** Trimmed Match estimator for paired geo experiments that is robust to outlier regions; with the companion design paper (Chen, Longfils, Remy 2021, arXiv 2105.07060, verified) it gives a complete, open workflow for iROAS experiments.
- **Use in course:** Session 4 lab (trimmed_match on synthetic data). Free preprint; journal version paywalled.

### Inferring Causal Impact Using Bayesian Structural Time-Series Models
- **Source:** Kay H. Brodersen, Fabian Gallusser, Jim Koehler, Nicolas Remy, Steven L. Scott, 2015, Annals of Applied Statistics 9(1), 247 to 274, article; package https://github.com/google/CausalImpact (verified)
- **Link:** https://doi.org/10.1214/14-AOAS788 (DOI unverified; publication confirmed via the package README)
- **Why it matters:** The CausalImpact method: a Bayesian structural time-series counterfactual for a single treated market, widely used to read campaign launches and quasi-experiments in single countries.
- **Use in course:** Session 4 lab (tfcausalimpact in Python). Open access.

### The Unfavorable Economics of Measuring the Returns to Advertising
- **Source:** Randall A. Lewis, Justin M. Rao, 2015, Quarterly Journal of Economics 130(4), 1941 to 1973, article
- **Link:** https://doi.org/10.1093/qje/qjv023 (DOI unverified)
- **Why it matters:** Shows why even huge experiments are underpowered for advertising ROI: sales variance dwarfs plausible ad effects. Essential for teaching power analysis of geo tests and the limits of calibration.
- **Use in course:** Session 4 reading. Paywalled; working-paper versions circulate.

**Attribution and the MMM-attribution relationship**

### Attributing Conversions in a Multichannel Online Marketing Environment: An Empirical Model and a Field Experiment
- **Source:** Hongshuang (Alice) Li, P. K. Kannan, 2014, Journal of Marketing Research 51(1), 40 to 56, article
- **Link:** https://doi.org/10.1509/jmr.13.0050 (verified)
- **Why it matters:** The reference academic multi-touch attribution model (consideration, visit, purchase stages with carryover and spillover), validated with a field experiment; shows how last-click misallocates credit.
- **Use in course:** Session 5 required reading. Paywalled.

### Beyond the Last Touch: Attribution in Online Advertising
- **Source:** Ron Berman, 2018, Marketing Science 37(5), 771 to 792, article
- **Link:** https://doi.org/10.1287/mksc.2018.1104 (verified)
- **Why it matters:** Game-theoretic analysis of attribution rules showing how last-touch distorts publisher incentives and why Shapley-type rules behave better; the theory behind data-driven attribution products.
- **Use in course:** Session 5 reading. Paywalled; SSRN version available.

### The Path to Purchase and Attribution Modeling: Introduction to Special Section
- **Source:** P. K. Kannan, Werner Reinartz, Peter C. Verhoef, 2016, International Journal of Research in Marketing 33(3), 449 to 456, editorial article
- **Link:** https://doi.org/10.1016/j.ijresmar.2016.07.001 (DOI unverified)
- **Why it matters:** Concise map of attribution research and of the gap between user-level attribution and aggregate MMM; the whole IJRM special section (de Haan, Wiesel, Pauwels; Anderl et al.; Kireyev, Pauwels, Gupta) is worth assigning.
- **Use in course:** Session 5 overview reading. Paywalled.

### The Effectiveness of Different Forms of Online Advertising for Purchase Conversion in a Multiple-Channel Attribution Framework
- **Source:** Evert de Haan, Thorsten Wiesel, Koen Pauwels, 2016, International Journal of Research in Marketing 33(3), 491 to 507, article
- **Link:** https://doi.org/10.1016/j.ijresmar.2015.12.001 (DOI unverified)
- **Why it matters:** Uses a VAR-based, aggregate time-series approach to attribute conversions across online channels, which is in effect an MMM applied to attribution; shows content-integrated ads and search outperform banners.
- **Use in course:** Session 5 reading (bridge between MMM and attribution). Paywalled.

### Mapping the Customer Journey: Lessons Learned from Graph-Based Online Attribution Modeling
- **Source:** Eva Anderl, Ingo Becker, Florian von Wangenheim, Jan Hendrik Schumann, 2016, International Journal of Research in Marketing 33(3), 457 to 474, article
- **Link:** https://doi.org/10.1016/j.ijresmar.2016.03.001 (DOI unverified)
- **Why it matters:** Markov-graph attribution (removal effects) on real clickstream data from German firms; the method behind many "data-driven attribution" tools, written by authors at ETH Zurich and Passau.
- **Use in course:** Session 5 lab (Markov attribution in Python). Paywalled.

### Data-Driven Multi-Touch Attribution Models
- **Source:** Xuhui Shao, Lexin Li, 2011, Proceedings of KDD 2011, conference paper
- **Link:** https://doi.org/10.1145/2020408.2020453 (DOI unverified)
- **Why it matters:** The first widely cited algorithmic MTA (bagged logistic regression and a simple probabilistic model); short and easy to implement in a lab.
- **Use in course:** Session 5 lab reference. Paywalled (ACM), author copies circulate.

### Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM
- **Source:** authors not captured (unverified), 2026, arXiv 2606.16878, working paper
- **Link:** https://arxiv.org/abs/2606.16878 (listing verified)
- **Why it matters:** One of the first papers to formalise "unified measurement": granular attribution constrained to reconcile with an MMM's channel totals, in a privacy-safe setting after cookie loss. Timely for the MMM-versus-attribution debate.
- **Use in course:** Session 5 discussion reading. Free.

**International and multi-market**

### Dynamic Marketing Budget Allocation Across Countries, Products, and Marketing Activities
- **Source:** Marc Fischer, Sönke Albers, Nils Wagner, Monika Frie, 2011, Marketing Science 30(4), 568 to 585 (INFORMS Practice Prize winner), article
- **Link:** https://doi.org/10.1287/mksc.1100.0627 (verified)
- **Why it matters:** The Bayer case: a decision-support model that allocates marketing budgets across countries, products and activities using response elasticities and dynamics, with a claimed profit improvement of about EUR 500 million. The single best academic match for the course's international allocation theme.
- **Use in course:** Session 3 required reading and case discussion; rebuild the allocation heuristic in Python. Paywalled.

### Marketing Mix and Brand Sales in Global Markets: Examining the Contingent Role of Country-Market Characteristics
- **Source:** S. Cem Bahadir, Sundar G. Bharadwaj, Rajendra K. Srivastava, 2015, Journal of International Business Studies 46(5), 596 to 619, article
- **Link:** https://doi.org/10.1057/jibs.2014.69 (verified)
- **Why it matters:** Hierarchical linear model across 14 emerging and developed markets: advertising and product innovation matter more in emerging markets, distribution and price differ by country type. Gives students priors for how elasticities shift across countries.
- **Use in course:** Session 3 reading (international angle). Paywalled.

### A Global Perspective on the Marketing Mix across Time and Space
- **Source:** Julian Wichmann, Abhinav Uppal, Amalesh Sharma, Marnik G. Dekimpe, 2022, International Journal of Research in Marketing 39(2), 502 to 521, article
- **Link:** https://doi.org/10.1016/j.ijresmar.2021.09.001 (verified)
- **Why it matters:** Reviews cross-country marketing-mix effectiveness research and sets a research agenda on heterogeneity across markets and over time; the most recent academic overview of the international MMM question.
- **Use in course:** Session 3 background reading. Paywalled.

### Determinants of Advertising Effectiveness: The Development of an International Advertising Elasticity Database and a Meta-Analysis
- **Source:** Sina Henningsen, Rebecca Heuke, Michel Clement, 2011, Business Research 4(2), 193 to 239, article (open access)
- **Link:** https://doi.org/10.1007/BF03342755 (verified)
- **Why it matters:** Meta-analysis of advertising elasticities built on an explicitly international database (mean current-period elasticity 0.09) with country and method moderators; complements Sethuraman et al. 2011 and is free.
- **Use in course:** Session 2 or 3 (priors by country). Open access.

### The Role of National Culture in Advertising's Sensitivity to Business Cycles: An Investigation Across Continents
- **Source:** Barbara Deleersnyder, Marnik G. Dekimpe, Jan-Benedict E. M. Steenkamp, Peter S. H. Leeflang, 2009, Journal of Marketing Research 46(5), 623 to 636, article
- **Link:** https://doi.org/10.1509/jmkr.46.5.623 (DOI unverified)
- **Why it matters:** 37 countries over 25 years: advertising is procyclical, and the degree depends on national culture (uncertainty avoidance, long-term orientation). Shows why macro controls and country effects belong in a multi-market MMM.
- **Use in course:** Session 3 background. Paywalled.

### Price and Advertising Effectiveness over the Business Cycle
- **Source:** Harald J. van Heerde, Maarten J. Gijsenberg, Marnik G. Dekimpe, Jan-Benedict E. M. Steenkamp, 2013, Journal of Marketing Research 50(2), 177 to 193, article
- **Link:** https://doi.org/10.1509/jmr.10.0414 (DOI unverified); open copy https://cdr.lib.unc.edu/downloads/3n204669g (listed in search, not fetched)
- **Why it matters:** Time-varying elasticities over 25 years show price sensitivity rises and advertising effectiveness falls in contractions; a concrete reason to model time-varying coefficients and macro conditions.
- **Use in course:** Session 4 reading (time-varying effects). Paywalled, open PDF available.

### Financial Development and Country-Level Advertising Spending: The Moderating Role of Economic Development and National Culture
- **Source:** Berrak Bahadir, S. Cem Bahadir, 2020, Journal of International Marketing 28(4), article
- **Link:** https://doi.org/10.1177/1069031X20936278 (verified)
- **Why it matters:** Country-level panel on what drives advertising intensity across economies; useful context when students compare budgets and media prices across markets.
- **Use in course:** Session 3 background. Paywalled.

**Reviews and practitioner-oriented academic papers**

### Open-Source Media and Marketing Mix Modeling: Practice-Oriented Overview, Challenges, Opportunities
- **Source:** authors not captured from the blocked publisher page (unverified), 2026, Customer Needs and Solutions 13 (Springer), published 22 April 2026, review article, open access
- **Link:** https://doi.org/10.1007/s40547-026-00161-4 (verified)
- **Why it matters:** The first peer-reviewed comparison of Meridian, Robyn and PyMC-Marketing (LightweightMMM is noted as deprecated and archived in January 2026): Bayesian versus ridge-regression designs, who each package suits, and open challenges. Exactly the tool-selection reading the course needs.
- **Use in course:** Session 2 required reading before choosing the lab stack. Open access.

### Optimizable and Implementable Aggregate Response Modeling for Marketing Decision Support
- **Source:** Sönke Albers, 2012, International Journal of Research in Marketing 29(2), 111 to 122, article
- **Link:** https://doi.org/10.1016/j.ijresmar.2012.03.001 (verified); SSRN open copy listed in search
- **Why it matters:** Argues that response models must be both optimisable (concave, interpretable elasticities) and implementable (simple enough for managers), and shows how to go from elasticities to allocation rules. The academic underpinning of the budget optimisers in Robyn and Meridian.
- **Use in course:** Session 3 required reading. Paywalled, SSRN copy available.

### The Value of Empirical Generalizations in Marketing
- **Source:** Dominique M. Hanssens, 2018, Journal of the Academy of Marketing Science 46, 6 to 8, editorial
- **Link:** https://doi.org/10.1007/s11747-017-0567-0 (verified)
- **Why it matters:** Three-page argument for using generalisations (elasticity ranges, carryover) as priors and sanity checks; a quick companion to the MSI book above.
- **Use in course:** Session 2 short reading. Paywalled; open PDF on the UCLA Anderson site (listed in search).

### Marketing's Impact on Firm Value: Generalizations from a Meta-Analysis
- **Source:** Alexander Edeling, Marc Fischer, 2016, Journal of Marketing Research 53(4), 515 to 534, article
- **Link:** https://doi.org/10.1509/jmr.14.0046 (verified)
- **Why it matters:** Meta-analysis linking advertising, brand and other marketing assets to firm value; provides the "so what" for MMM results at board level and a Cologne-based author who fits the DACH guest-speaker focus.
- **Use in course:** Session 1 or 3 background. Paywalled.

### How Advertising Works: What Do We Really Know?
- **Source:** Demetrios Vakratsas, Tim Ambler, 1999, Journal of Marketing 63(1), 26 to 43, review article
- **Link:** https://doi.org/10.1177/002224299906300103 (verified)
- **Why it matters:** Reviews 250 studies on advertising response and frameworks (hierarchy of effects, carryover, wear-out); the best short literature map before reading MMM papers.
- **Use in course:** Session 1 background. Paywalled.

### Marvelous Advertising Returns? A Meta-Analysis of Advertising Elasticities in the Entertainment Industry
- **Source:** authors not captured (unverified), 2022, Journal of the Academy of Marketing Science, article
- **Link:** https://doi.org/10.1007/s11747-022-00916-0 (verified)
- **Why it matters:** Recent, industry-specific meta-analysis of advertising elasticities; a template for how students can derive sector priors for their own MMM.
- **Use in course:** Session 2 optional reading. Paywalled (check for Springer open access).

## Gaps and caveats

- Tooling limits during this search: the Consensus academic search quota was exhausted (30 of 30 searches used; resets 1 November), the session web-search budget ran out, and the network proxy blocked doi.org, Crossref, OpenAlex, Semantic Scholar, arXiv, Springer, Elsevier, Sage, INFORMS, Wiley and research.google. Only github.com and one Google storage host answered. Everything marked verified was confirmed from search-result listings, GitHub READMEs (lifesight awesome-marketing-measurement, LightweightMMM, trimmed_match, CausalImpact, GeoexperimentsResearch, AMSS, PyMC-Marketing) or the one fetched PDF (Jin et al. 2017). DOIs marked "(DOI unverified)" are from memory and should be checked once with doi.org before going into a syllabus.
- Authors could not be captured for three items: the 2026 Springer open-source MMM overview, the 2026 "Integrated Marketing Attribution" arXiv paper, and the 2022 JAMS entertainment meta-analysis. The "Your MMM is Broken" authors are from memory.
- Paywalls: almost all journal articles (JMR, Marketing Science, JM, IJRM, JAMS, JIBS, Econometrica, QJE) require library access; open copies exist for Sethuraman et al., Hanssens and Pauwels, Gordon et al. 2019, Shapiro et al., van Heerde et al., Albers and Hanssens 2018. All Google and Meta white papers, arXiv preprints, Henningsen et al. and the Springer 2026 overview are free.
- Books: no dedicated MMM textbook exists; the course has to combine Hanssens et al. or Leeflang et al. (theory) with the Google 2017 papers and the open Python books (Martin et al.; Huntington-Klein; Facure). Lilien et al. and the Python edition of Hyndman's book are unverified. Hanssens et al. (2001) and Tellis (2004) are old but remain the references.
- Not covered here but worth a look by whoever handles tools and reports: MSI Working Paper 24-147 (appears to concern Robyn; content unverified), MSI Report 26-106 (2026, unverified), Google's "NNN: Next-Generation Neural Networks for Marketing Mix Modeling" (arXiv 2504.06212, 2025), the 2025 to 2026 arXiv papers on geo-experiment design (Supergeo, arXiv 2301.12044 and 2506.20499), "Structural Estimation of MMM Parameters from Geo-Experiments" (arXiv 2608.21128) and the synthetic benchmark dataset with endogenous spend (arXiv 2608.21130), and Meridian's own methodology pages on developers.google.com, which were blocked here.
- Journal of Advertising Research and Management Science yielded no verified MMM-specific entries in this search; the Journal of Advertising Research in particular may hold practitioner MMM papers (2019 onward) that a library search should pick up.

# Part 2: Reports, websites and blogs, teaching cases, practice examples

Scope: industry and vendor reports on MMM and measurement; practitioner websites, blogs and newsletters; teaching cases and free case-style datasets; documented real-world MMM implementations. Entries are ranked best first within each section. Verification note: in this session the network proxy blocked direct fetching of almost every publisher domain (only github.com resolved), so most links are confirmed through search-engine results rather than by opening the page; those are marked "(confirmed in search results)". Links opened directly are marked "(fetched)". Anything else is marked "(unverified)".

---

## 1. Reports

### Marketing Mix Modeling Best Practices (Nielsen with Google and Meta)
- **Source:** Nielsen, Google and Meta, 2022, report (PDF, about 20 pages)
- **Link:** https://www.nielsen.com/wp-content/uploads/sites/2/2022/09/Marketing-Mix-Modeling-Best-Practices-EN.pdf (confirmed in search results)
- **Why it matters:** The most-cited vendor-neutral checklist for model specification: model at the most granular geography available, include non-marketing drivers (a media-only MMM overstated ad ROI by 68 per cent in Nielsen's comparison), handle digital granularity and reach. Companion Nielsen note analyses 19 Japanese models to show regional beats national data.
- **Use in course:** Session 2 (data and model specification) required reading; pairs with the geo-hierarchy lab. Free.

### Modernizing MMM: Best Practices for Marketers (IAB)
- **Source:** IAB (US) with MMM vendors, December 2025, report (PDF)
- **Link:** https://www.iab.com/guidelines/modernizing-mmm-best-practices-for-marketers/ and PDF https://www.iab.com/wp-content/uploads/2025/12/IAB_Modernizing_MMM_Best_Practices_for_Marketers_December_2025.pdf (confirmed in search results)
- **Why it matters:** Newest vendor-neutral industry guide; frames "timely, auditable, decision-ready" MMM, covers calibration with experiments, cadence, governance and includes cross-industry case studies.
- **Use in course:** Session 1 (measurement landscape) and Session 5 (from model to decision); free.

### Modern Measurement Playbook (Google)
- **Source:** Google / Think with Google, 2023 (updated 2024), report (PDF, 44 pages)
- **Link:** https://www.thinkwithgoogle.com/_qs/documents/18393/For_pub_on_TwG___External_Playbook_Modern_Measurement.pdf (confirmed in search results); landing page https://business.google.com/us/think/measurement/drive-business-goals-modern-measurement/
- **Why it matters:** Sets out the "measurement tripod" (attribution, incrementality experiments, MMM) and how to triangulate them; concise and well illustrated, so it works as a framing text for the whole course.
- **Use in course:** Session 1 pre-reading; Session 5 for the triangulation discussion. Free.

### The MMM Handbook: A Guide for Developing Impactful Marketing Mix Models (Google)
- **Source:** Google (Think with Google, EMEA), 2023, report (PDF, "a CMO's handbook")
- **Link:** https://www.thinkwithgoogle.com/_qs/documents/18104/Marketing_Mix_Modelling_-_A_CMOs_handbook.pdf (confirmed in search results)
- **Why it matters:** Short management-level guide: start with the right business questions, pick KPIs, capture all drivers, validate, act. Good contrast to the technical Nielsen document.
- **Use in course:** Session 1 or background; free.

### Meridian Playbook (Google)
- **Source:** Google, 2025, report (PDF)
- **Link:** https://www.thinkwithgoogle.com/_qs/documents/18498/Meridian_Playbook_1s4EUSU.pdf (confirmed in search results)
- **Why it matters:** Step-by-step guidance on running Google's open-source Bayesian MMM (data requirements, geo-level set-up, priors from experiments, budget optimiser). Directly transferable to a Python lab.
- **Use in course:** Session 3 (Bayesian MMM lab) or Session 4 (budget allocation); free.

### ROI Genome (Analytic Partners)
- **Source:** Analytic Partners, ongoing series 2020 to 2025, reports and briefs
- **Link:** https://analyticpartners.com/roi-genome/report-marketing-through-crisis-and-beyond/ and newsroom summaries such as https://analyticpartners.com/knowledge-hub/newsroom/report-roi-genome-adopt-scenario-planning-increases-roi/ (confirmed in search results)
- **Why it matters:** Meta-analysis across 1,000+ brands and 50 countries of MMM results: brand versus performance messaging, recession spend, CTV, scenario planning (25 to 70 per cent ROI gains). Rare cross-country benchmark material.
- **Use in course:** Session 4 (cross-country budget allocation) as discussion input; Session 5. Free summaries, full reports gated behind registration.

### Marketing Mix Modelling: A How-To Guide for Marketers (WARC and Magic Numbers)
- **Source:** Dr Grace Kite (Magic Numbers) with WARC, 2023, report (PDF, five chapters)
- **Link:** https://magicworks.training/wp-content/uploads/2024/04/Marketing-Mix-Modelling-A-How-To-Guide-for-Marketers-FINAL.pdf (confirmed in search results; original on WARC is paywalled)
- **Why it matters:** Practical and candid on choosing suppliers, embedding MMM in an organisation, reading results and common failure modes; includes UK case studies. Written by an econometrician who runs models for a living.
- **Use in course:** Session 5 (using MMM in management) reading; free mirror, WARC version paywalled.

### Profit Ability 2: The New Business Case for Advertising (Ebiquity and Thinkbox)
- **Source:** Ebiquity for Thinkbox with Gain Theory, EssenceMediacom, Mindshare and Wavemaker, May 2024, report (PDF)
- **Link:** https://ebiquity.com/news-insights/press/profit-ability-2-the-new-business-case-for-advertising/ and PDF https://assets.ctfassets.net/ptzdhtf6t0jg/KkqtmmsDkxlGl0wlE72TF/178b9f6af6d3af215154e12455485e92/Profit_Ability_2_The_new_business_case_for_advertising_report.pdf (confirmed in search results)
- **Why it matters:** Pooled MMM across GBP 1.8bn of UK media, 141 brands and 10 channels; shows short-term versus sustained profit ROI by channel (TV 5.61, online video 3.86, generic PPC 3.52) and that about 60 per cent of effect lands after 13 weeks. A clean example of what adstock and long-term effects mean commercially.
- **Use in course:** Session 2 (adstock and carry-over) and Session 4; free.

### Paid Media Effectiveness Handbook (WFA and Ebiquity)
- **Source:** World Federation of Advertisers with Ebiquity, 2026, report
- **Link:** https://wfanet.org/leadership/marketing/media-effectiveness (confirmed in search results); related WFA benchmark of MMM partners in EMEA https://wfanet.org/knowledge/item/2025/03/31/benchmark-marketing-mix-modelling-(mmm)-partners-in-emea
- **Why it matters:** Based on research with advertisers controlling about USD 40bn of paid media; explains how MMM, attribution, experiments and brand metrics fit together and reports that 80 per cent use MMM but only 13 per cent turn data into insight quickly. The EMEA vendor benchmark is useful for a European vendor-selection discussion.
- **Use in course:** Session 5 and background; WFA members only (summary articles free).

### Magic Quadrant for Marketing Mix Modeling Solutions (Gartner)
- **Source:** Gartner, November 2024 (first edition) and 2025 edition, analyst report; preceded by the Market Guide for MMM Solutions (April 2024)
- **Link:** Gartner topic page https://www.gartner.com/en/marketing/topics/marketing-mix-modeling and Market Guide https://www.gartner.com/en/documents/5389963 (confirmed in search results); free vendor reprints via Analytic Partners, Ipsos MMA, Ekimetrics press pages
- **Why it matters:** The reference map of the commercial MMM vendor landscape (Leaders: Analytic Partners, Ipsos MMA, Ekimetrics, Nielsen and others) with Gartner's 2024 survey finding that 64 per cent of senior marketing leaders have adopted MMM. Useful to show students what "commercial tool" means versus open source.
- **Use in course:** Session 1 or 5, short discussion; paywalled, use vendor reprints.

### The Forrester Wave: Marketing Measurement and Optimization
- **Source:** Forrester, Q3 2023 (solutions) and Q1 2026 (services), analyst reports
- **Link:** Q3 2023 reprint PDF https://cdn.prod.website-files.com/66e2d4967d2fc7095ce820ef/66fd6a0e18d00d2ed1d06c79_The-Forrester-Wave_Marketing-Measurement-And-Optimization_Q3-2023.pdf and Q1 2026 summary https://gaintheory.com/forrester/ (confirmed in search results)
- **Why it matters:** Nine providers scored on 38 criteria including global capabilities, unified measurement and model operations; complements Gartner.
- **Use in course:** Background for vendor comparison; reprints free, original paywalled.

### Six Steps to More Effective Marketing Measurement (BCG)
- **Source:** Boston Consulting Group, 2025, article/report
- **Link:** https://www.bcg.com/publications/2025/six-steps-to-more-effective-marketing-measurement (confirmed in search results); related https://www.bcg.com/x/the-multiplier/four-legged-approach-to-understanding-marketing-roi
- **Why it matters:** Consultancy view with survey data: 39 per cent of leading marketers run MMM monthly, 40 per cent calibrate with incrementality tests, growing use of brand metrics in MMM. Good for the "MMM as a management system" angle.
- **Use in course:** Session 5 reading; free.

### MMM adoption study (Kantar and Meta)
- **Source:** Kantar with Meta, 2025, report (PDF)
- **Link:** https://s3.amazonaws.com/media.mediapost.com/uploads/Kantar___META_Thought_Leadership.pdf (fetched; PDF resolves)
- **Why it matters:** Global survey of 1,935 measurement professionals at companies spending over USD 1m a year on digital; adoption dynamics, barriers and what "good" looks like. Kantar's own MMM pages add the long-term brand-effect angle.
- **Use in course:** Session 1 background; free.

### Market Mix Modelling Landscape Report 2025 (IAB Australia)
- **Source:** IAB Australia Ad Effectiveness Council, September 2025 (updated December 2025), report
- **Link:** https://www.iabaustralia.com.au/resource/market-mix-modelling-landscape-report-2025/ (confirmed in search results)
- **Why it matters:** Directory of twelve MMM vendors (classical econometrics to Bayesian and ML), a marketer's checklist and plain-language method comparison; a handy template for a vendor-evaluation exercise.
- **Use in course:** Session 5 exercise (evaluate a vendor pitch); free.

### The Essential Guide to Marketing Mix Modeling and Multi-Touch Attribution (IAB and MMA Global)
- **Source:** IAB with MMA Global, November 2019, guidebook (PDF)
- **Link:** https://www.iab.com/wp-content/uploads/2019/11/IAB_MMA_MTA-Guidebook_Nov-2019.pdf (confirmed in search results)
- **Why it matters:** Older but still the clearest side-by-side of MMM and MTA (data, granularity, use cases, limitations). Meta's own note "Considerations for creating modern marketing mix models" (https://www.facebook.com/business/news/insights/considerations-for-creating-modern-marketing-mix-models) is a short complement.
- **Use in course:** Session 5 (attribution versus MMM); free.

---

## 2. Websites, blogs and newsletters

### PyMC Labs blog
- **Source:** PyMC Labs (authors include Thomas Wiecki, Juan Orduz, Carlos Trujillo, Will Dean), 2021 to 2026, blog
- **Link:** https://www.pymc-labs.com/blog-posts (confirmed in search results); key posts: https://www.pymc-labs.com/blog-posts/bayesian-media-mix-modeling-for-marketing-optimization , https://www.pymc-labs.com/blog-posts/modelling-changes-marketing-effectiveness-over-time , https://www.pymc-labs.com/blog-posts/full-funnel-mmm-optimization
- **Why it matters:** The home of PyMC-Marketing thinking: Bayesian MMM, time-varying effectiveness, funnel-aware models, lift-test calibration, the HelloFresh case. Python code throughout.
- **Use in course:** Sessions 2 to 4 lab readings; free.

### Google Meridian documentation and repository
- **Source:** Google, 2025 to 2026, website and software (Python, Apache 2.0)
- **Link:** https://developers.google.com/meridian (confirmed in search results); https://github.com/google/meridian (fetched)
- **Why it matters:** Reference docs for a hierarchical geo-level Bayesian MMM with reach and frequency, experiment priors and budget optimiser; Colab tutorial with sample data; superseded LightweightMMM (https://github.com/google/lightweight_mmm, archived, fetched).
- **Use in course:** Session 3 and 4 labs; free.

### Meta Robyn site and repository
- **Source:** Meta Marketing Science (Gufeng Zhou and others), 2021 to 2026, website and software (R primary, Python beta, MIT)
- **Link:** https://facebookexperimental.github.io/Robyn/ (confirmed in search results); https://github.com/facebookexperimental/Robyn (fetched); case studies https://facebookexperimental.github.io/Robyn/docs/case-studies/
- **Why it matters:** Ridge regression plus evolutionary hyperparameter search, calibration with lift tests, simulated weekly demo data; the most used open-source MMM in practice and the natural contrast to the Bayesian tools.
- **Use in course:** Session 3 comparison (R versus Python), optional lab; free.

### Recast blog and MMM Academy
- **Source:** Recast (Michael Kaminsky, Thomas Vladeck), 2021 to 2026, blog and newsletter
- **Link:** https://getrecast.com/mmm-academy/building-a-media-mix-model/ , https://getrecast.com/integrating-geo-testing-with-marketing-mix-modeling/ , https://getrecast.com/mmm-examples/ (confirmed in search results)
- **Why it matters:** The most opinionated practitioner writing on MMM identification problems, geo-test calibration, long-term brand effects and vendor hype; the "who is talking about MMM" page lists public brand examples.
- **Use in course:** Session 3 (calibration) and Session 5; free.

### Dr Juan Camilo Orduz, personal blog
- **Source:** Juan Camilo Orduz (PyMC Labs, Berlin), 2021 to 2026, blog
- **Link:** https://juanitorduz.github.io/pymc_mmm/ and https://juanitorduz.github.io/orbit_mmm/ (confirmed in search results)
- **Why it matters:** Fully reproducible PyMC notebooks on adstock, saturation, time-varying coefficients, Orbit's KTR model and hierarchical MMM; ideal lab scaffolding. Berlin-based, so also a realistic guest-speaker lead for the people part.
- **Use in course:** Sessions 2 and 3 lab material; free.

### Aryma Labs Substack
- **Source:** Venkat Raman and Ridhima Kumar (Aryma Labs, India), 2023 to 2026, newsletter
- **Link:** https://arymalabs.substack.com/p/marketing-mix-modeling-mmm-101 , https://arymalabs.substack.com/p/marketing-mix-modeling-mmm-is-just , https://arymalabs.substack.com/p/learning-from-og-mmm-fmcg-cpg-mmm (confirmed in search results)
- **Why it matters:** Critical, statistically careful posts ("is MMM just linear regression?", "one true MMM?", lessons from FMCG econometrics); good for teaching scepticism towards automated tools.
- **Use in course:** Session 2 discussion reading; free.

### Measured learning centre
- **Source:** Measured (US), 2020 to 2026, website
- **Link:** https://www.measured.com/resources/ , https://www.measured.com/faq/incrementality-attribution-mmm-decision-tree/ , https://www.measured.com/faq/real-life-media-mix-modeling-mmm-examples-true-incrementality/ (confirmed in search results)
- **Why it matters:** Decision tree for when to use incrementality tests, attribution or MMM; a "how to QA an MMM" checklist; ten named brand examples. Vendor site but unusually instructive.
- **Use in course:** Session 5; free.

### Haus blog and Incrementality School
- **Source:** Haus (US; founders from Netflix and Google experimentation teams), 2023 to 2026, blog
- **Link:** https://www.haus.io/blog/why-incrementality-testing-belongs-with-your-mmm-and-where-to-start and https://www.haus.io/blog/incrementality-experiments-a-comprehensive-guide (confirmed in search results)
- **Why it matters:** Clear explanations of geo experiments, synthetic control and "causal MMM" built on experiments; the experiments-first counterweight to model-first vendors.
- **Use in course:** Session 3 or the experiments session; free.

### Sellforte blog
- **Source:** Sellforte (Helsinki), 2022 to 2026, blog
- **Link:** https://sellforte.com/blog/what-is-causal-marketing-mix-modeling-mmm and https://sellforte.com/blog/marketing-mix-modeling-rfp-retail (confirmed in search results)
- **Why it matters:** European SaaS vendor writing on retail and e-commerce MMM, causal MMM and a procurement/RFP guide that students can use in a vendor-selection exercise.
- **Use in course:** Session 5 exercise; free.

### Mutinex (Henry Innis) and Madison and Wall interviews
- **Source:** Mutinex (Sydney) and Madison and Wall Substack (Brian Wieser), 2024 to 2026, blog and newsletter
- **Link:** https://mutinex.co/the-power-of-mmm-to-unlock-true-growth/ , https://madisonandwall.substack.com/p/mutinex-on-mmms-mtas-and-more , https://www.beet.tv/2026/09/mmm-must-plug-directly-into-bidding-systems-to-stay-competitive-mutinex-ceo-says.html (confirmed in search results)
- **Why it matters:** The "always-on MMM feeding bidding systems" thesis and a sceptical industry analyst's questioning of it; good for a debate on MMM cadence and over-use of incrementality tests.
- **Use in course:** Session 5 debate; free.

### Cassandra resources
- **Source:** Cassandra (European MMM SaaS), 2023 to 2026, website
- **Link:** https://cassandra.app/resources/a-dee-dive-into-the-algorithm-behind-media-mix-modeling-and-optimization (confirmed in search results)
- **Why it matters:** Readable walk-through of the algorithm behind a commercial MMM and optimiser, written for marketers rather than statisticians.
- **Use in course:** Session 4 background; free.

### Ebiquity Insights blog
- **Source:** Ebiquity (London), 2022 to 2026, blog
- **Link:** https://ebiquity.com/news-insights/blog/bayesian-media-mix-modelling/ , https://ebiquity.com/news-insights/blog/automation-marketing-mix-modelling/ , https://ebiquity.com/news-insights/blog/from-measurement-to-management-the-emerging-role-of-mmm/ (confirmed in search results)
- **Why it matters:** The classical econometrics view: "Bayesian MMM: cure-all or caveat emptor?", pros and cons of always-on automation, MMM as a management discipline; strong European advertiser perspective.
- **Use in course:** Session 3 counter-reading; free.

### MASS Analytics blog and Measure Up podcast
- **Source:** MASS Analytics (Tunis and London), 2020 to 2026, blog and podcast
- **Link:** https://mass-analytics.com/marketing-mix-modeling-blogs/learn-marketing-mix-modeling/ and https://mass-analytics.com/marketing-mix-modeling-blogs/how-geo-experiments-measure-incrementality/ (confirmed in search results); podcast https://creators.spotify.com/pod/show/measure-up
- **Why it matters:** Structured "learn MMM" curriculum, masterclasses and an interview podcast with practitioners; the geo-experiment explainer is concise.
- **Use in course:** Background self-study; free.

### Hands-On Data: "The hard thing about Marketing Mix Models"
- **Source:** Hands-On Data (independent data scientist), 2024, Substack post
- **Link:** https://handsondata.substack.com/p/the-hard-thing-about-marketing-mix (confirmed in search results)
- **Why it matters:** Honest practitioner account of identification, data and organisational problems in MMM; short and quotable.
- **Use in course:** Session 2 warm-up; free.

### Vexpower MMM learning path (Mike Taylor)
- **Source:** Mike Taylor (Vexpower, former Ladder agency), 2022 to 2025, simulator-based courses
- **Link:** https://www.vexpower.com/paths/marketing-mix-modeling and https://app.vexpower.com/sim/can-we-try-uber-orbit/ (confirmed in search results)
- **Why it matters:** Scenario-style exercises (Robyn, LightweightMMM, Orbit) that mimic client briefs; a model for how to write lab assignments.
- **Use in course:** Inspiration for assignments; paid subscription, some free content.

---

## 3. Teaching cases (Cases for Teaching)

### Multiple Regression and Marketing-Mix Models (Darden technical note)
- **Source:** Rajkumar Venkatesan and Shea Gibbs, Darden Business Publishing, 2013, case/technical note; Darden UVA-M-0855, HBP UV6764, Case Centre 118828
- **Link:** https://store.hbr.org/product/multiple-regression-and-marketing-mix-models/UV6764 , https://store.darden.virginia.edu/multiple-regression-and-marketing-mix-models , https://www.thecasecentre.org/products/view?id=118828 (confirmed in search results)
- **Why it matters:** The standard classroom note on regression-based MMM (omitted-variable bias, interpretation of coefficients, elasticities); used in Darden's Big Data in Marketing elective.
- **Use in course:** Session 2 pre-reading; paid (about USD 5 to 9 per student via HBP or Case Centre).

### Note on Marketing Mix Models: Evaluating "Bang for the Buck" (Darden)
- **Source:** Paul W. Farris, Darden Business Publishing, 1987, technical note M-0339
- **Link:** https://store.darden.virginia.edu/note-on-marketing-mix-models-evaluating-bang-for-the-buck (confirmed in search results)
- **Why it matters:** The classic resource-allocation framing of MMM (marginal returns, response curves) that today's optimisers still implement; short and still assigned.
- **Use in course:** Session 4 background; paid, low cost.

### Digital Marketing at HBS Online (HBS case 521-027)
- **Source:** Sunil Gupta and Rajiv Lal, Harvard Business School, 2020 (revised 2024), case; Case Centre 174588
- **Link:** https://www.hbs.edu/faculty/Pages/item.aspx?num=58780 and https://www.thecasecentre.org/products/view?id=174588 (confirmed in search results)
- **Why it matters:** Management must allocate a digital budget across channels and course portfolios using channel performance data; raises attribution versus incrementality and portfolio trade-offs with real numbers.
- **Use in course:** Session 4 or 5 case discussion; paid (HBP, about USD 9 per student plus teaching note).

### Amperity: First-Party Data at a Crossroads (HBS case 524-017)
- **Source:** Elie Ofek, Hema Yoganarasimhan and Alexis Lefort, Harvard Business School, 2024, case
- **Link:** https://www.hbs.edu/faculty/research/publications/Pages/default.aspx?topic=Digital+Marketing (confirmed in search results; case number from HBS listing)
- **Why it matters:** Sets the signal-loss and privacy context (cookie deprecation, first-party data) that explains why MMM is back; good opener before the technical sessions.
- **Use in course:** Session 1 case; paid (HBP).

### Cutting-Edge Marketing Analytics: Real World Cases and Data Sets (Darden casebook)
- **Source:** Rajkumar Venkatesan, Paul Farris and Ronald Wilcox, FT Press, 2014, book of cases with datasets; successor "Marketing Analytics: Essential Tools for Data-Driven Decisions", UVA Press, 2021
- **Link:** https://www.amazon.com/Cutting-Edge-Marketing-Analytics-Learning/dp/0133552527 and https://www.amazon.com/Marketing-Analytics-Essential-Data-Driven-Decisions/dp/0813945151 (confirmed in search results); individual cases sold via Darden Business Publishing
- **Why it matters:** Each chapter is a real company case with downloadable data (regression-based marketing-mix, resource allocation, experiments, CLV); the cases can be run in Python rather than the book's Excel/R.
- **Use in course:** Sessions 2 and 4 labs; book purchase or per-case licences.

### Advertising measurement at Facebook and eBay (research-based mini-cases, Kellogg and Berkeley)
- **Source:** Brett Gordon, Florian Zettelmeyer, Neha Bhargava and Dan Chapsky, Marketing Science 2019 (SSRN 2017); Thomas Blake, Chris Nosko and Steven Tadelis, Econometrica 2015; Gordon, Moakler and Zettelmeyer, Marketing Science 2023, articles usable as cases
- **Link:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3033144 , https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA12423 , https://ideas.repec.org/a/inm/ormksc/v42y2023i4p768-793.html ; free teaching slides https://www.ftc.gov/system/files/documents/public_events/945353/zettelmeyer_fb_fcc_11-3-2016_fz_slides_0.pdf (confirmed in search results)
- **Why it matters:** No formal Kellogg case on MMM was found, but these are the canonical "observational methods versus experiments" teaching materials: eBay paid-search returns were a fraction of non-experimental estimates; Facebook's 15 RCTs show how far attribution and matching stray from lift.
- **Use in course:** Session 5 (attribution versus incrementality) as a structured discussion; journal access via WU library, slides free.

### Resident and Robyn (Meta Marketing Science case)
- **Source:** Meta, 2021, published case study (free)
- **Link:** https://facebookexperimental.github.io/Robyn/docs/case-studies/ (confirmed in search results)
- **Why it matters:** E-commerce company (Nectar, DreamCloud) runs its in-house MMM alongside Robyn, uses DMA-level data and lift-test calibration, reports 20 per cent revenue growth; the same page lists Central Retail Group (Thailand) and Lemonade. A free case with a reproducible open-source tool.
- **Use in course:** Session 3 case plus Robyn demo data; free.

### Marketing Mix Modeling in Lemonade (arXiv paper as case)
- **Source:** Lemonade data science team, 2025, working paper arXiv 2501.01276
- **Link:** https://arxiv.org/abs/2501.01276 (confirmed in search results)
- **Why it matters:** Candid account of building a Bayesian MMM for an insurtech, combining it with Robyn and geo tests for calibration; reads like a teaching case with methods detail.
- **Use in course:** Session 3 reading; free.

### Advertising incrementality using controlled geo-experiments: the Universal App Campaign case (Uber)
- **Source:** Joel Barajas and colleagues (Uber), AdKDD 2020, conference paper
- **Link:** http://papers.adkdd.org/2020/papers/adkdd20-barajas-advertising.pdf (confirmed in search results)
- **Why it matters:** A full geo-experiment case: market pairing, Bayesian structural time series counterfactual, a 6.57 per cent conversion drop when Google UAC spend is paused; reusable as a lab on geo tests that feed MMM priors.
- **Use in course:** Session 3 or experiments session lab; free.

### Structural estimation of MMM parameters from geo-experiments (Zalando researcher)
- **Source:** Niklas Heusch (Zalando), 2026, working paper arXiv 2608.21128
- **Link:** https://arxiv.org/abs/2608.21128 and press summary https://ppc.land/mmm-overstates-paid-search-roas-by-2-5-times-zalando-researcher-finds/ (confirmed in search results)
- **Why it matters:** Shows a standard MMM reporting 10.61x ROAS for paid search whose experimental truth was 4.20x, and how geo-experiment time series recover the right parameters; a Berlin e-commerce example students will recognise.
- **Use in course:** Session 3 case; free.

### Free datasets usable as cases
- **Source:** various, 2020 to 2026, open data
- **Link:** PyMC-Marketing data folder https://github.com/pymc-labs/pymc-marketing/tree/main/data (fetched: mmm_example.csv, mmm_multidimensional_example.csv, mmm_roas_data.csv, credibility_* lift-test files, funnel_data.csv); Meridian simulated geo-level data https://github.com/google/meridian/tree/main/meridian/data (fetched: simulated_data directory) and Colab sample data; Robyn simulated weekly demo data in https://github.com/facebookexperimental/Robyn (fetched); GeoLift sample data https://github.com/facebookincubator/GeoLift (fetched, R); Google GeoexperimentsResearch https://github.com/google/GeoexperimentsResearch (fetched, archived R); Kaggle DT MART https://www.kaggle.com/datasets/datatattle/dt-mart-market-mix-modeling and bike-sales MMM demo https://www.kaggle.com/datasets/mattwalentosky/mmmdemodataset (confirmed in search results); synthetic benchmark with endogenous spend https://arxiv.org/pdf/2608.21130 (unverified content)
- **Why it matters:** The multidimensional PyMC-Marketing example and Meridian's simulated data are geo-level, so they support a cross-country or cross-region assignment; the credibility files let students calibrate against lift tests.
- **Use in course:** Sessions 2 to 4 labs and the group project; all free.

---

## 4. Practice examples (Praxisbeispiele)

### HelloFresh: Bayesian MMM across 15 markets (PyMC Labs)
- **Source:** PyMC Labs, 2022 to 2025, case study and blog posts
- **Link:** https://www.pymc-labs.com/case-studies/hellofresh and https://www.pymc-labs.com/blog-posts/reducing-customer-acquisition-costs-how-we-helped-optimizing-hellofreshs-marketing-budget (confirmed in search results)
- **Why it matters:** Berlin-based meal-kit company replaces black-box attribution with a Bayesian MMM over TV, social, podcasts and partners; reported 60 per cent lower prediction variance, 10x faster inference and about 30 per cent ROAS uplift across 15 markets, with a what-if budget simulator. The best multi-country Python example available.
- **Use in course:** Session 4 anchor example and guest-talk target; free.

### Heineken: MMM lighthouse markets Spain and Brazil (Meta)
- **Source:** Meta Business, 2021 to 2023, case study; AudienceProject cross-media case 2023
- **Link:** https://www.facebook.com/business/measurement/case-studies/heineken and https://audienceproject.com/cases/heineken-documents-reach-and-brand-outcomes-of-cross-media-campaign-to-identify-media-mix-optimisations/ (confirmed in search results)
- **Why it matters:** Global brewer uses two lighthouse markets to test measurement questions before rolling out; MMM showed Facebook ROI 2.3x the total media ROI in Spain and 3.5x the average in Brazil, now used as a "compass" for ongoing media decisions. Platform-sponsored, so discuss source bias.
- **Use in course:** Session 4 cross-country example; free.

### Zalando: experiments first, then MMM (engineering blog and research)
- **Source:** Zalando Engineering, 2019, blog; Niklas Heusch, 2026, arXiv paper
- **Link:** https://engineering.zalando.com/posts/2019/02/effectiveness-online-marketing.html and https://arxiv.org/abs/2608.21128 (confirmed in search results)
- **Why it matters:** Europe's largest fashion platform runs geo-based and audience-based randomised tests across 25 markets to measure incremental revenue, profit and acquisition, and its researchers now publish on reconciling MMM with those tests.
- **Use in course:** Session 3 and 5; free.

### Uber: Orbit, in-house Bayesian MMM and geo experiments
- **Source:** Uber Marketing Data Science (Edwin Ng, Zhishi Wang, Athena Dai), 2021, paper and open-source library; Barajas et al., AdKDD 2020
- **Link:** https://arxiv.org/pdf/2106.03322 , https://getrecast.com/uber-orbit/ , http://papers.adkdd.org/2020/papers/adkdd20-barajas-advertising.pdf (confirmed in search results)
- **Why it matters:** Time-varying-coefficient Bayesian MMM built from zero in-house, with lift tests ingested as priors; documents how a global platform company operationalises measurement.
- **Use in course:** Session 3 (time-varying effects) example; free.

### Bayer: unifying MMM and multi-touch attribution (TransUnion)
- **Source:** TransUnion, 2023, vendor case study
- **Link:** https://www.transunion.com/case-study/bayer-marketing-unification (confirmed in search results)
- **Why it matters:** Leverkusen-based pharma and consumer-health group had conflicting MMM and MTA numbers; case describes aligning the two into one measurement programme. Short but a real DACH-headquartered example of the "unified measurement" problem.
- **Use in course:** Session 5 discussion; free.

### Resident, Central Retail Group and Lemonade (Meta Robyn adopters)
- **Source:** Meta Marketing Science, 2021 to 2024, case studies
- **Link:** https://facebookexperimental.github.io/Robyn/docs/case-studies/ (confirmed in search results)
- **Why it matters:** Three documented open-source MMM deployments: a US DTC group (+20 per cent revenue), a Thai retail conglomerate (budget reallocation worth up to 28 per cent revenue) and an insurtech using geo tests for calibration. Shows what adoption looks like outside the big consultancies.
- **Use in course:** Session 3; free.

### Kellogg's: faster MMM turnaround (MASS Analytics)
- **Source:** MASS Analytics, 2022, vendor case study
- **Link:** https://mass-analytics.com/marketing-mix-modeling-use-case/marketing-mix-modeling-use-case-faster-marketing-mix-modeling-kelloggs/ (confirmed in search results)
- **Why it matters:** FMCG example that treats media and trade spend together and focuses on speed of model refresh, which is the practical bottleneck in most MMM programmes.
- **Use in course:** Session 5; free.

### Akulaku, Suntory Wellness and Finder: Meridian in APAC (Think with Google)
- **Source:** Google / Think with Google APAC, 2025, case articles
- **Link:** https://business.google.com/us/think/measurement/marketing-mix-modelling-growth-engine/ and https://business.google.com/en-all/think/measurement/google-meridian-marketing-mix-modelling/ (confirmed in search results)
- **Why it matters:** Early Meridian deployments in Indonesia, Japan and Australia; Akulaku's optimiser suggested 16 per cent more GMV at constant budget. Emerging-market angle, with the usual caveat that the platform publishes the results.
- **Use in course:** Session 4 international examples; free.

### Nielsen and TikTok MMM case study
- **Source:** Nielsen, 2022, case study (PDF)
- **Link:** https://www.nielsen.com/wp-content/uploads/sites/2/2022/03/Nielsen-TikTok-MMM-Case-Study.pdf (confirmed in search results)
- **Why it matters:** Shows how a new channel gets measured inside a commercial MMM and how platform data partnerships shape results.
- **Use in course:** Session 2 (channel data) example; free.

### Caritas Switzerland and Swiss Post: cross-media MMM for a fundraising campaign (Exactag)
- **Source:** Swiss Post Advertising / Exactag, 2023, case summary in German
- **Link:** https://www.directpoint.ch/de/kampagnenprozess/erfolgskontrolle/marketing-mix-modeling-welche-kanaele-wirken-wirklich (confirmed in search results)
- **Why it matters:** A DACH example: MMM on the "Welt ohne Armut" Christmas campaign attributed over half of donations to advertising, with direct mail most effective, then OOH and DOOH. Useful for students who read German and for the non-profit angle.
- **Use in course:** Session 2 or 4 short example; free.

### Measured: ten named brand MMM examples
- **Source:** Measured, 2025, vendor article
- **Link:** https://www.measured.com/faq/real-life-media-mix-modeling-mmm-examples-true-incrementality/ (confirmed in search results)
- **Why it matters:** Ten retail and DTC brands with one-paragraph outcomes from incrementality-calibrated MMM; a quick source of discussion vignettes. Search results also state that Unilever uses Measured for media measurement at scale (unverified detail).
- **Use in course:** Session 5 warm-up; free.

### Volkswagen: cross-media measurement across Germany, France and the UK (TikTok and Kantar)
- **Source:** TikTok for Business with Kantar, 2023, case study
- **Link:** https://ads.tiktok.com/business/en/inspiration/volkswagen-cross-media-case-study (confirmed in search results)
- **Why it matters:** Not an MMM, but a three-country cross-media study for the ID. range that shows how brand-lift and reach studies feed into mix decisions; no public VW MMM was found.
- **Use in course:** Session 4 side example; free.

### Anonymised vendor cases from Gain Theory and Ipsos MMA
- **Source:** Gain Theory (WPP), 2023, case study; Ipsos MMA, 2024, case study
- **Link:** https://gaintheory.com/case-study/optimizing-marketing-investments/ and https://mma.com/case-study-establishing-a-unified-marketing-mix-modeling-and-attribution-program/ (confirmed in search results)
- **Why it matters:** A multinational alcoholic-beverages company and a large financial-services firm; useful to show how consultancies present MMM programmes (governance, scenario planning), even if client names are withheld.
- **Use in course:** Session 5 background; free.

### Austrian and German market context
- **Source:** Trending Topics (Vienna), 2025, article; ad agents and directpoint articles, 2024 to 2025
- **Link:** https://www.trendingtopics.eu/marketing-trends-2025-ki-mix-modeling-und-neue-einkaufsassistenten/ and https://www.ad-agents.com/so-bringt-marketing-mix-modelling-mehr-effizienz-fuer-deine-werbespendings/ (confirmed in search results)
- **Why it matters:** German-language coverage of MMM adoption in DACH (one source cites about a quarter of companies using MMM regularly; unverified figure). No public, named MMM implementation from an Austrian brand (Red Bull, Swarovski, Spar, A1) was found.
- **Use in course:** Background; free.

---

## Gaps and caveats

- Verification: the session's network proxy blocked direct fetching of nearly all publisher domains (only github.com and one PDF mirror resolved), and the search budget ran out before every blog could be double-checked. All non-GitHub links were confirmed as appearing in search-engine results with matching titles, but page content, dates and prices should be re-checked before the syllabus is finalised.
- Paywalls: Gartner Magic Quadrant and Market Guide, Forrester Waves, the WFA handbook and EMEA vendor benchmark, and WARC's original of the Magic Numbers guide are paywalled or members only; free vendor reprints or mirrors are listed instead. HBP, Darden and Case Centre cases cost roughly USD 5 to 10 per student.
- Teaching cases: no formal Ivey, INSEAD, Kellogg, Stanford GSB or Case Centre case titled "Marketing Mix Modeling at ..." was found, and no HBS or Darden case on Unilever, P&G, Coca-Cola, Nestlé, Heineken or Mattel marketing mix modelling surfaced; the section therefore mixes the Darden notes and HBS budget-allocation case with free research-based and vendor-published cases. Direct catalogue searches on iveypublishing.ca, thecasecentre.org and hbsp.harvard.edu are recommended.
- McKinsey: no McKinsey MMM-specific piece could be located; BCG is included instead.
- Practice examples: Spotify, Booking.com, Douglas, Nestlé, Red Bull, Swarovski and Austrian brands have no public, named MMM write-ups that could be found; Unilever appears only as a Measured client mention; Volkswagen appears only in a cross-media study. Platform- and vendor-published cases (Meta, Google, TransUnion, MASS Analytics, Measured) carry obvious selection and sponsorship bias and should be taught as such.
- Dates: several "2026" items (IAB December 2025, Forrester Q1 2026, WFA handbook 2026, Heusch 2026, PyMC Labs 2026 posts) are very recent and may be revised; the Robyn demo dataset name and the Darden note "A Resource-Allocation Perspective for Marketing Analytics" product number were not verified.

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

# Part 4: People, communities and datasets

Scope: (1) people to follow and realistic guest speakers, (2) communities, conferences and events, (3) public datasets for MMM teaching beyond the course's own Alpenglow data. Compiled 5 October 2026 for the winter term 2026/27 run (6 October to 3 November 2026). Links were checked by fetch where the network allowed it; links that could only be confirmed through a search result, or not at all, are flagged "(unverified)". See "Gaps and caveats" at the end.

---

## 1. People to follow and potential guest speakers

### 1a. Global thought leaders to follow (LinkedIn, X, blogs)

Ranked by how directly their public output maps onto the course (Bayesian MMM in Python, calibration with experiments, cross-market allocation).

### Juan Camilo Orduz
- **Source:** VP Marketing Analytics, PyMC Labs; Berlin; person (core author of PyMC-Marketing's MMM module)
- **Link:** https://www.pymc-labs.com/blog-posts/mmm_roas_lift (lift-test calibration post); personal blog https://juanitorduz.github.io/ (unverified: proxy blocked)
- **Why it matters:** Writes the most detailed public worked examples of Bayesian MMM, hierarchical geo models and lift-test calibration in Python; his notebooks are the closest public analogue to Session 3's lab.
- **Use in course:** Session 3 background reading; strong remote guest-talk candidate (Berlin, same time zone) on calibrating an MMM with experiments.

### Thomas Wiecki
- **Source:** CEO and co-founder, PyMC Labs; co-author of PyMC; Berlin area; person
- **Link:** https://cd.linkedin.com/posts/twiecki_pymc-marketing-activity-7049716496519811072-Ojbv (LinkedIn); PyData talk "Bayesian Marketing Science" referenced at https://www.pymc-labs.com/blog-posts/marketing-mix-modeling-a-complete-guide
- **Why it matters:** The public voice of Bayesian MMM; frequent posts on priors, identifiability and why Bayesian beats ridge for MMM; case studies with HelloFresh and Bolt.
- **Use in course:** Session 2-3 motivation; guest-talk candidate (vendor and open-source angle), realistic by video.

### Michael Kaminsky
- **Source:** Co-founder, Recast; USA; person
- **Link:** https://www.linkedin.com/posts/michael-the-data-guy-kaminsky_should-you-model-all-external-factors-in-activity-7163517252598775808-HtRO (LinkedIn); Recast blog https://getrecast.com/
- **Why it matters:** Sharpest practitioner writing on MMM validation: hold-out accuracy, long-term brand effects, "MER is a road to ruin", when not to add control variables. Good counterweight to vendor hype.
- **Use in course:** Session 2 diagnostics and Session 4 forecasting; short posts work as pre-reads.

### Gufeng Zhou
- **Source:** Marketing Science, Meta; creator of Robyn; London; person
- **Link:** https://uk.linkedin.com/in/gufeng-zhou-96401721 (LinkedIn, confirmed in search); Robyn repo https://github.com/facebookexperimental/Robyn
- **Why it matters:** Author of the most used open-source MMM in industry; his Medium and LinkedIn pieces on experiment calibration explain Robyn's design choices (ridge, Nevergrad, calibration).
- **Use in course:** Session 2 (Robyn as the R and ridge benchmark); vendor-side guest talk angle (Meta Marketing Science Europe).

### Igor Skokan
- **Source:** Marketing Science Director, open source, Meta; co-author of Robyn; person
- **Link:** https://github.com/facebookexperimental/Robyn (named in README); paper https://arxiv.org/pdf/2403.14674
- **Why it matters:** Co-author of "Packaging Up Media Mix Modeling" (with Runge, Zhou, Pauwels), the best short bridge between academic MMM and Robyn.
- **Use in course:** Background; Session 2 reading.

### Google Meridian team
- **Source:** Google Meridian Marketing Mix Modeling Team (the README cites the team, not individuals); person/team
- **Link:** https://github.com/google/meridian (verified); blog https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/
- **Why it matters:** Meridian is the reference implementation of geo-level hierarchical Bayesian MMM with reach and frequency, exactly the structure used in Session 3; their docs on geo selection are directly reusable.
- **Use in course:** Session 3 (geo hierarchy); follow via the GitHub repo and the Think with Google measurement pages. No single named person to follow; see JSM 2025 talk "Meridian: Google's Open-Source Marketing Mix Model" (https://ww2.amstat.org/meetings/jsm/2025/onlineprogram/abstract.cfm?sid=2361&tid=2363, unverified).

### Julian Runge
- **Source:** Assistant Professor, Northwestern University Medill; previously Meta marketing science; person
- **Link:** https://www.linkedin.com/posts/julian-runge_dear-digital-first-advertisers-are-you-media-activity-7100870821962764289-PASj (LinkedIn); MSI working paper https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_24-147.pdf
- **Why it matters:** Bridges academia and platform marketing science; co-author of the Robyn paper and of a 2026 Customer Needs and Solutions overview of open-source MMM (https://link.springer.com/article/10.1007/s40547-026-00161-4, unverified: proxy blocked).
- **Use in course:** Session 2 and 4 readings; remote guest-talk candidate on "media vs marketing mix modelling".

### Koen Pauwels
- **Source:** Distinguished Professor of Marketing, Northeastern University (DATA Initiative); Boston; person
- **Link:** https://www.researchgate.net/profile/Koen-Pauwels-3 ; personal site https://marketingandmetrics.com/
- **Why it matters:** Long-run marketing effectiveness, VAR models, dashboards; co-author of the Robyn paper and of the Yildirim and Kübler book; very active on LinkedIn and YouTube with plain-language explanations.
- **Use in course:** Session 2 and 3 background; "Marketing and Metrics" videos as optional viewing.

### Dominique Hanssens
- **Source:** Distinguished Research Professor of Marketing, UCLA Anderson; person
- **Link:** https://www.anderson.ucla.edu/faculty-and-research/marketing/faculty/hanssens
- **Why it matters:** The reference on market response models and long-term marketing effects (Hanssens, Parsons and Schultz); his MSI "Empirical Generalizations about Marketing Impact" is the best one-page summary of what elasticities to expect.
- **Use in course:** Session 1 and 2 classic reading; sanity-check priors in Session 3 against his elasticity generalisations.

### Harald van Heerde
- **Source:** Research Professor of Marketing, UNSW Sydney; Fellow, Tilburg University; person
- **Link:** https://www.unsw.edu.au/staff/harald-van-heerde
- **Why it matters:** Leading author on promotion response, decomposition of sales lifts, and marketing effectiveness across business cycles; essential for the baseline vs incremental logic.
- **Use in course:** Session 2 background (promotion decomposition), Session 1 elasticities.

### Marnik Dekimpe
- **Source:** Research Professor of Marketing, Tilburg University, and Professor, KU Leuven; person
- **Link:** https://www.researchgate.net/scientific-contributions/Marnik-G-Dekimpe-80951987
- **Why it matters:** Persistence modelling and long-run effects; cross-country work on private labels and retail in Europe fits the international angle.
- **Use in course:** Session 3 background (cross-country heterogeneity); realistic academic guest from the Benelux.

### Peter Danaher
- **Source:** Professor of Marketing and Econometrics, Monash University; Melbourne; person
- **Link:** https://research.monash.edu/en/persons/peter-danaher/
- **Why it matters:** Media exposure, reach and frequency modelling and multichannel attribution with field tests; directly relevant to Meridian's reach and frequency extension.
- **Use in course:** Session 4 attribution background.

### Jan-Benedict Steenkamp
- **Source:** C. Knox Massey Distinguished Professor of Marketing, UNC Kenan-Flagler; Editor in Chief, Journal of Marketing; person
- **Link:** https://www.kenan-flagler.unc.edu/faculty/directory/jan-benedict-steenkamp/ ; https://www.linkedin.com/in/jan-benedict-steenkamp-bb535ab/
- **Why it matters:** The international marketing reference (global brands, emerging markets, private label); frames why effects differ across the six Alpenglow markets.
- **Use in course:** Session 3 (cross-country) and Session 5 framing.

### Raoul Kübler
- **Source:** Professor of Marketing, ESSEC Business School; Cergy/Paris; German, previously Münster; person
- **Link:** https://faculty.essec.edu/en/cv/kubler-raoul/ ; https://www.raoulkuebler.de/ ; LinkedIn post on MMM manipulation https://www.linkedin.com/posts/raoul-k%C3%BCbler-a8365a49_demystifying-the-manipulation-of-marketing-activity-7156012239114682369-XpcC
- **Why it matters:** Co-author of "Applied Marketing Analytics Using R" (SAGE, with Yildirim), teaches MMM hands-on; posts on how MMM results get manipulated are perfect critical-thinking material.
- **Use in course:** Session 2 reading; realistic academic guest speaker (German speaker, European time zone, teaches exactly this material).

### Gokhan Yildirim
- **Source:** Associate Professor of Marketing, Imperial College Business School; London; person
- **Link:** https://www.researchgate.net/scientific-contributions/Gokhan-Yildirim-2006570428 ; book https://www.waterstones.com/book/applied-marketing-analytics-using-r/gokhan-yildirim/raoul-k-bler/9781529768725
- **Why it matters:** MMM and multichannel budget allocation research (direct mail vs email field tests, JAMS 2023); co-author of the applied R textbook.
- **Use in course:** Session 3 budget allocation background.

### Nicolas Padilla
- **Source:** Assistant Professor of Marketing, London Business School; person
- **Link:** https://www.london.edu/faculty-and-research/faculty-profiles/n/nicolas-padilla ; CV http://www.columbia.edu/~np2506/CV/PadillaCVweb.pdf
- **Why it matters:** Works explicitly on "modern marketing mix models" with first-party data and machine learning; one of few academics engaging with the Bayesian MMM revival.
- **Use in course:** Session 3 background; remote guest candidate (London).

### Bernd Skiera
- **Source:** Professor, Chair of Electronic Commerce, Goethe University Frankfurt; person
- **Link:** https://www.marketing.uni-frankfurt.de/de/professoren/skiera/prof-dr-bernd-skiera/publikationen.html
- **Why it matters:** Online advertising economics, attribution, and the GDPR tracking study (https://arxiv.org/pdf/2411.06862); the German-speaking reference on why attribution breaks and MMM returns.
- **Use in course:** Session 4 attribution; realistic guest (Frankfurt, two hours from Vienna by air).

### Christian Schulze
- **Source:** Associate Professor of Marketing, Frankfurt School of Finance and Management; person
- **Link:** https://scholar.google.com/citations?user=bt2edqYAAAAJ&hl=en
- **Why it matters:** Digital marketing and customer analytics with a strong quantitative bent; co-author with Skiera on marketing ROI and attribution.
- **Use in course:** Session 4 background; Frankfurt-based guest candidate.

### Martin Spann
- **Source:** Professor and Director, Institute of Electronic Commerce and Digital Markets, LMU Munich; person
- **Link:** https://ieeexplore.ieee.org/author/37086629306 (author page); LMU institute page (unverified: proxy blocked)
- **Why it matters:** Pricing, mobile and digital markets; useful for the price elasticity and digital channel parts.
- **Use in course:** Session 1 background; Munich guest candidate.

### Mike Taylor
- **Source:** Independent, co-founder of Ladder (marketing agency), author; London; person
- **Link:** https://getrecast.com/author/miketaylor/ ; https://www.linkedin.com/posts/mjt145_after-months-drowning-in-data-its-such-a-activity-6981023895956942848-S95I
- **Why it matters:** Practitioner tutorials comparing Robyn, LightweightMMM and PyMC-Marketing from a marketer's view; also writes on AI-assisted analysis, matching the course's AI-coding approach.
- **Use in course:** Session 2 optional reading.

### Eric Seufert
- **Source:** Heracles Media, author of Mobile Dev Memo; person
- **Link:** https://mobiledevmemo.com/ (unverified: proxy blocked); collaboration with Runge referenced via https://muckrack.com/julian-runge/articles
- **Why it matters:** Explains the privacy-driven revival of MMM (ATT, cookie loss) better than anyone; good for the "why now" argument.
- **Use in course:** Session 1 motivation.

### Jim Gianoglio
- **Source:** Founder, Cauzle Analytics and MMM Hub; USA; person
- **Link:** https://www.linkedin.com/in/jimgianoglio/ ; https://www.mmmhub.org (unverified: proxy blocked)
- **Why it matters:** Runs the MMM Hub newsletter, Slack and podcast; curates practically every new MMM resource. Marketing Analytics Summit talk "Cracking the Code: Mastering Modern MMM" https://www.youtube.com/watch?v=FEG-Vtj7Y9Q
- **Use in course:** Point students to MMM Hub in Session 1; the YouTube talk is a 40-minute overview for Session 2.

### Kevin Hartman
- **Source:** Director of Analytics, Google; author of "Digital Marketing Analytics: In Theory and in Practice"; person
- **Link:** https://www.goodreads.com/book/show/53490687-digital-marketing-analytics (book page); LinkedIn profile not confirmed (unverified)
- **Why it matters:** Accessible textbook framing of measurement choices; useful for students without a statistics background.
- **Use in course:** Background.

### Dominik Papies
- **Source:** Professor of Marketing, University of Tübingen; person
- **Link:** https://www.linkedin.com/in/dominik-papies-6aa204183/ ; https://scholar.google.com/citations?user=34_x4OcAAAAJ&hl=de
- **Why it matters:** Market response models and the standard reference chapter on endogeneity in marketing models; exactly the "why is media spend endogenous" problem in Session 2 and 3.
- **Use in course:** Session 2 reading on endogeneity; German guest candidate.

### Jochen Hartmann
- **Source:** Professor of Digital Marketing, TUM School of Management, Munich; person
- **Link:** https://www.mgt.tum.de/professors-1/info/prof-dr-jochen-hartmann
- **Why it matters:** Generative AI, multimodal ad analytics and unstructured data; complements MMM with creative-quality covariates.
- **Use in course:** Session 4 or 5 extension; Munich guest candidate.

### 1b. Realistic guest speakers reachable from Vienna

All are public professional pages (company, university, LinkedIn company or profile pages surfaced in search). Where a named person's current role could not be confirmed, the entry is company-level with the name flagged. Ranked by fit and practicality.

### Thomas Reutterer, WU Vienna
- **Source:** Professor of Marketing, Head of Institute for Marketing and Customer Analytics, WU Vienna; academic
- **Link:** https://www.wu.ac.at/en/mca/institute/meet-our-team ; https://www.reutterer.com/bio.html
- **Why them:** In-house WU colleague with a long record in marketing analytics and Bayesian methods; zero travel cost.
- **Speaker angle:** Academic: "What MMM can and cannot tell you about customers", or a joint Q&A in Session 5.

### Nils Wlömert and Nadia Abou Nabout, WU Vienna
- **Source:** Professors, Retailing and Data Science (Wlömert) and AI in Marketing Analytics (Abou Nabout), WU Department of Marketing; academic
- **Link:** https://www.wu.ac.at/en/marketing/about-us/department-struktur/ ; https://www.wu.ac.at/fileadmin/wu/d/i/imsm/Dokumente/Nadia_Abou_Nabout.pdf
- **Why them:** Abou Nabout works on online advertising auctions and attribution, Wlömert on retail data science; both are on campus.
- **Speaker angle:** Academic: attribution vs MMM (Session 4), retail scanner data (Session 1).

### Analytic Partners, Hamburg and Munich
- **Source:** Analytic Partners GmbH (Gartner MMM Magic Quadrant leader 2025); Hamburg office opened 2017 under Achim Schoeneich (Managing Director Germany, role as of 2017); vendor
- **Link:** https://analyticpartners.com/news-blog/2017/09/welcome-achim-schoeneich-lead-new-office-germany/ ; offices https://analyticpartners.com/contact-us/
- **Why them:** The largest commercial MMM shop with a German-speaking team; they run multi-country models for DACH brands.
- **Speaker angle:** Vendor: "Commercial analytics at scale: what a 20-country MMM programme looks like" (Session 3).

### Adtriba (now part of Funnel), Hamburg
- **Source:** János Moldvay, founder and CEO, Adtriba; acquired by Funnel in 2024; vendor
- **Link:** https://funnel.io/press-releases/marketing-intelligence-platform-funnel-acquires-measurement-firm-adtriba ; https://www.anyscale.com/blog/adtriba-accelerates-and-advances-media-mix-modeling-using-the-anyscale-fully
- **Why them:** German start-up that combined MMM, multi-touch attribution and incrementality for clients such as FlixBus; the Anyscale post describes their Bayesian MMM engineering.
- **Speaker angle:** Vendor and founder: "Unified measurement: MMM plus attribution plus experiments" (Session 4).

### Nexoya, Zurich
- **Source:** Nexoya AG, Zurich-based AI marketing budget optimisation platform active in CH, DE, AT, IT, UK; vendor
- **Link:** https://www.nexoya.com/press/ ; https://www.venturelab.swiss/nexoya-Meet-the-Venture-Leader-Technology-optimizing-marketing-decisions-with-predictive-AI
- **Why them:** Regression-based cross-channel attribution and automated budget reallocation for brands such as Zurich Insurance, Generali, Swisscom; a Swiss example of operationalised allocation.
- **Speaker angle:** Vendor: "From model to weekly budget decision" (Session 3 budget allocation).

### Mediaplus Austria (Serviceplan Group), Vienna
- **Source:** Mediaplus Austria GmbH and Co KG, Vienna media agency; group Data and AI unit in Munich; agency
- **Link:** https://at.linkedin.com/company/mediaplus-austria ; https://medianet.at/markets/mediaagenturen/mediaplus-austria-gmbh-co-kg-5516.html ; group page https://www.house-of-communication.com/int/en/brands/mediaplus/about-mediaplus.html
- **Why them:** Largest independent media agency in DACH with an in-house modelling offer; Vienna office means an in-person visit is realistic.
- **Speaker angle:** Agency: "How a media agency builds and sells an MMM to an Austrian client" (Session 2). Named modelling lead not public; ask via the Vienna office.

### dentsu Austria and Merkle, Vienna
- **Source:** dentsu Austria GmbH, Vienna; Merkle (dentsu) runs a Marketing Measurement and Optimisation practice and is a Google Meridian partner (partner status unverified); agency
- **Link:** https://medianet.at/markets/mediaagenturen/dentsu-austria-gmbh-5524.html
- **Why them:** Network agency with a Vienna office and a Meridian-based measurement practice in the group.
- **Speaker angle:** Agency: "Running Meridian for a client" (Session 3).

### GroupM Austria (WPP), Vienna
- **Source:** GroupM Austria, about 350 staff in Vienna; agency
- **Link:** https://www.linkedin.com/company/groupm-austria
- **Why them:** WPP's media investment arm; GroupM's global analytics units (Choreograph, [m]Science) run MMM for Austrian clients.
- **Speaker angle:** Agency: media planning meets MMM; a planner's view of response curves (Session 2).

### e-dialog, Vienna
- **Source:** e-dialog GmbH, Vienna performance marketing and analytics agency listing Marketing Mix Modelling among its services; agency (unverified: site blocked by proxy, mention from search summary only)
- **Link:** https://www.e-dialog.at/ (unverified)
- **Why them:** Small Vienna agency doing Google-stack analytics and MMM for mid-sized Austrian advertisers; practical scale for student projects.
- **Speaker angle:** Agency: "MMM for a mid-sized Austrian brand with limited data" (Session 2).

### Red Bull, Salzburg (Global Brand Marketing, marketing data science)
- **Source:** Red Bull GmbH, Fuschl am See; public job posting "Marketing Data Science Specialist" describing in-house MMM work in R and Python; brand
- **Link:** https://builtin.com/job/marketing-data-science-specialist/3710572 ; https://jobs.redbull.com/za-en/locations/red-bull-global-headquarters?lang=en
- **Why them:** Austria's most international brand runs MMM in-house across markets; a textbook case for Session 3's cross-country allocation.
- **Speaker angle:** Brand: "In-house MMM at a global Austrian brand". No named lead is public; approach via WU alumni or the Global Brand Marketing team.

### Sellforte (clients in DACH: bonprix, Hamburg)
- **Source:** Sellforte, Helsinki-based MMM SaaS for retail and ecommerce; bonprix case; vendor
- **Link:** https://sellforte.com/customer-news/bonprix ; https://sellforte.com/about
- **Why them:** European SaaS MMM with a published multi-country retail case (bonprix across Europe); contrasts with consultancy-style MMM.
- **Speaker angle:** Vendor: "Always-on MMM for a European retailer" (Session 3); remote.

### Ekimetrics (Paris, London; DACH projects)
- **Source:** Ekimetrics, Gartner MMM Magic Quadrant Visionary 2025, Forrester Wave leader Q1 2026; consultancy
- **Link:** https://www.ekimetrics.com/articles/ekimetrics-recognized-in-the-2025-gartner-magic-quadrant-for-marketing-mix-modeling
- **Why them:** Runs global measurement programmes with branding, local activation and structural variables; strong on the "holistic MMM" argument.
- **Speaker angle:** Consultancy: "Global MMM governance across countries" (Session 3); remote from Paris. No German office confirmed.

### Kantar (LIFT ROI), Munich and Vienna offices
- **Source:** Kantar, Gartner MMM Magic Quadrant Visionary 2025; LIFT ROI MMM product; research vendor
- **Link:** https://www.kantar.com/Campaigns/LIFT-ROI ; https://www.kantar.com/solutions/decision-intelligence/media
- **Why them:** Combines brand tracking with MMM; useful to show how brand equity enters a mix model.
- **Speaker angle:** Vendor: "Brand effects in MMM" (Session 2). Named DACH lead not public.

### Beiersdorf, Hamburg (Commercial Mix Modelling)
- **Source:** Beiersdorf AG; a public LinkedIn profile (Christian Jähnert, role unverified) describes media data analytics and "Commercial Mix Modeling (econometrics)" in-house; brand
- **Link:** https://www.linkedin.com/in/christian-jaehnert/ (unverified)
- **Why them:** FMCG brand owner (Nivea) with in-house econometrics across many countries; comparable category dynamics to Alpenglow.
- **Speaker angle:** Brand: "Owning the model in-house vs buying it" (Session 3).

### Henkel, Düsseldorf (Meridian adopter)
- **Source:** Henkel AG; search results indicate Henkel introduced Google Meridian for MMM (unverified; named profile Gabriel Marambaia, role unverified); brand
- **Link:** https://www.linkedin.com/in/gabrielmarambaia/ (unverified)
- **Why them:** A large DACH brand using the same open-source stack as the course.
- **Speaker angle:** Brand: "Moving from vendor MMM to open-source Meridian" (Session 3).

### Raoul Kübler, ESSEC (German academic abroad)
- **Source:** See 1a; German-speaking professor teaching MMM in R; academic
- **Link:** https://faculty.essec.edu/en/cv/kubler-raoul/
- **Why them:** Teaches the same material at master level and has written on MMM manipulation; fluent German.
- **Speaker angle:** Academic: "How MMM results get gamed and how to audit them" (Session 2 or 5).

### Dominik Papies, Tübingen
- **Source:** Professor of Marketing, University of Tübingen; academic
- **Link:** https://www.linkedin.com/in/dominik-papies-6aa204183/
- **Why them:** The German reference on endogeneity in market response models.
- **Speaker angle:** Academic: "Endogeneity in MMM: when your spend reacts to your sales" (Session 2 or 3).

### Bernd Skiera, Frankfurt
- **Source:** Professor, Goethe University Frankfurt; academic
- **Link:** https://www.marketing.uni-frankfurt.de/de/professoren/skiera/prof-dr-bernd-skiera/publikationen.html
- **Why them:** Attribution and privacy regulation research; close to Vienna.
- **Speaker angle:** Academic: "Attribution after GDPR and ATT: what is left and why MMM is back" (Session 4).

### Markus Christen, HEC Lausanne
- **Source:** Full Professor of Marketing, HEC Lausanne (ex INSEAD, ETH engineering background); academic
- **Link:** https://hecnet.unil.ch/hec/recherche/fiche?pnom=mchristen&dyn_lang=en ; https://www.unil.ch/news/en/1502973967830
- **Why them:** Marketing models and value-of-information research; Swiss academic voice on how much a model is worth to a decision maker.
- **Speaker angle:** Academic: "The value of information from an MMM" (Session 5 wrap-up).

### Jochen Hartmann, TUM Munich
- **Source:** Professor of Digital Marketing, TUM; academic
- **Link:** https://www.mgt.tum.de/professors-1/info/prof-dr-jochen-hartmann
- **Why them:** Generative AI and ad creative analytics; one flight from Vienna.
- **Speaker angle:** Academic: "Adding creative quality to the mix model with AI-extracted features" (Session 4 or 5 extension).

---

## 2. Communities, conferences and events

Ranked by usefulness to a Python-first MMM course. Course runs 6 October to 3 November 2026, so events in late 2026 and 2027 are the ones students can still attend.

### MMM Hub (newsletter, Slack community, podcast)
- **Source:** Jim Gianoglio (Cauzle Analytics), ongoing since 2023; website and community
- **Link:** https://www.mmmhub.org (unverified: proxy blocked; confirmed in search results and linked from the PyMC-Marketing README)
- **Why it matters:** The de facto practitioner hub: weekly newsletter, Slack workspace, curated resources and a podcast; PyMC-Marketing points its own users there.
- **Use in course:** Session 1 onboarding; students join the Slack and newsletter.

### PyMC Discourse, pymc-marketing category, and the Bayesian Discord
- **Source:** PyMC community, ongoing; forum
- **Link:** https://discourse.pymc.io/t/getting-started-with-pymc-marketing-questions-and-doubts/14447 ; https://discourse.pymc.io/t/hierarchical-mmm-channel-hierarchy-structure/17006 ; repo links https://github.com/pymc-labs/pymc-marketing
- **Why it matters:** Where PyMC-Marketing maintainers answer modelling questions (hierarchical channel structures, priors, sampling problems); the threads above are directly about Session 3 models.
- **Use in course:** Session 3 lab support channel; encourage students to search before asking.

### Robyn GitHub Discussions and Facebook group
- **Source:** Meta Marketing Science, ongoing; GitHub Discussions (Announcements, General, Ideas, Polls, Q&A, Show and tell)
- **Link:** https://github.com/facebookexperimental/Robyn/discussions (verified)
- **Why it matters:** Active Q&A on calibration, budget allocation and hyperparameters; the Facebook group linked from the README is where Meta's team interacts with users.
- **Use in course:** Session 2 (R benchmark) reference.

### Google Meridian GitHub and developer docs
- **Source:** Google, 2025 onward; repository and documentation
- **Link:** https://github.com/google/meridian (verified); docs https://developers.google.com/meridian/docs/pre-modeling/geo-selection-national-data
- **Why it matters:** Issues and docs are the practical community for geo-hierarchical MMM; the geo-selection guidance maps onto choosing markets in Session 3.
- **Use in course:** Session 3 reading.

### ISMS Marketing Science Conference
- **Source:** INFORMS Society for Marketing Science; annual academic conference
- **Link:** 2026: Nova SBE, Carcavelos, Portugal, 11 to 13 June 2026, https://www.informs.org/Meetings-Conferences/INFORMS-Conference-Calendar/2026-ISMS-Marketing-Science-Conference ; 2027: Seattle, 24 to 26 June 2027, https://www.informs.org/Meetings-Conferences/INFORMS-Conference-Calendar/2027-ISMS-Marketing-Science-Conference
- **Why it matters:** The main quantitative marketing conference; MMM, attribution and experiment sessions every year.
- **Use in course:** Background; for students considering a PhD or research-based thesis.

### EMAC Annual and Fall Conferences
- **Source:** European Marketing Academy; annual (spring) and regional (fall) conferences
- **Link:** EMAC 2026 Bath, 2 to 5 June 2026 https://www.emac2026conference.org/ ; EMAC Fall 2026 Bremen, 16 to 18 September 2026 https://www.uni-bremen.de/en/markstones/emac-fall-conference-2026 ; EMAC 2027 Rome (Luiss), 23 to 28 May 2027 https://emac2027.org/
- **Why it matters:** Europe's marketing academic community; the Rome 2027 meeting is the realistic one for WU students and the instructor.
- **Use in course:** Background; thesis supervision pipeline.

### PyData Amsterdam and PyCon DE and PyData
- **Source:** NumFOCUS PyData; annual conferences
- **Link:** PyData Amsterdam 10 to 11 September 2026 (tutorials 12 September), NDSM Loods, https://amsterdam.pydata.org/ ; PyCon DE and PyData 14 to 16 April 2026 (location per search result, unverified) https://pydata.org/past-events/
- **Why it matters:** PyMC Labs and PyMC-Marketing talks appear at PyData regularly (Wiecki's "Bayesian Marketing Science" was a PyData talk); the recordings are free on YouTube.
- **Use in course:** Session 3 video pre-read; next in-person editions are 2027.

### Meta Marketing Mix Modeling Summit
- **Source:** Meta Marketing Science, recurring practitioner summit (invitation-based); event
- **Link:** Recap by Recast https://getrecast.com/meta-mmm-summit/ (unverified: proxy blocked; confirmed in search); Ekimetrics recap https://ekimetrics.com/news-and-events/exploring-the-links-between-creative-execution-and-marketing-effectiveness-mmmsummit/
- **Why it matters:** Where Meta, vendors (Nielsen, Accenture, Ekimetrics) and brands compare MMM practice; recaps are a good snapshot of industry consensus.
- **Use in course:** Session 2 background; 2026 date not public.

### Marketing Analytics Summit
- **Source:** Marketing Analytics Summit (formerly eMetrics), annual practitioner conference, USA; event
- **Link:** https://marketinganalyticssummit.com/session/cracking-the-code-mastering-modern-marketing-mix-modeling/ ; speaker page https://marketinganalyticssummit.com/speaker/jim-gianoglio/
- **Why it matters:** Practitioner-level MMM talks with recordings on YouTube.
- **Use in course:** Session 2 video; 2027 dates unverified.

### Marketing Mix Modeling GitHub organisation
- **Source:** Community-curated GitHub organisation consolidating Meridian, Robyn, PyMC-Marketing, LightweightMMM, Unified-MMM and a Papers repo; website
- **Link:** https://github.com/marketing-mix-modeling (verified)
- **Why it matters:** One place to compare the open-source MMM stacks and find the papers list.
- **Use in course:** Session 2 reference.

### Measure Up and Funnel Reboot podcasts
- **Source:** Measure Up (podcast on marketing measurement) and Funnel Reboot episode 170 with Jim Gianoglio; audio
- **Link:** https://www.measureup.show/ (unverified: proxy blocked); https://funnelreboot.com/episode-170-marketing-mix-modelling-with-jim-gianoglio/
- **Why it matters:** Interview format makes trade-offs (cost, data needs, calibration) accessible for non-statisticians.
- **Use in course:** Optional listening, Session 1 or 2.

### Marketing Science Institute (MSI) working papers
- **Source:** MSI, ongoing; report series
- **Link:** https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_24-147.pdf ; https://thearf-org-unified-admin.s3.amazonaws.com/MSI/2026/MSI_Report_26-106.pdf
- **Why it matters:** Practitioner-facing academic papers on MMM (Runge and co-authors); free PDFs.
- **Use in course:** Session 2 and 4 readings.

---

## 3. Datasets for teaching

Ranked by fit to the course's Python stack and the multi-country theme. Sizes were measured locally where the file could be downloaded.

### Google Meridian simulated geo-level data
- **Source:** Google, 2025, dataset in the Meridian repo; Apache 2.0
- **Link:** https://raw.githubusercontent.com/google/meridian/refs/heads/main/meridian/data/simulated_data/csv/geo_all_channels.csv (verified by download); folder https://github.com/google/meridian/tree/main/meridian/data/simulated_data/csv
- **Why it matters:** 6,240 rows: 40 geos x 156 weeks (25 January 2021 to 15 January 2024), 5 paid channels with impressions and spend, 1 organic channel, 2 controls, promo flag, conversions, revenue per conversion and population (20 columns, about 1 MB). Sibling files add reach and frequency, national-level and a "hypothetical" future scenario for budget optimisation.
- **Use in course:** Session 3 lab alternative (hierarchical geo model and allocation); the geos can be relabelled as countries.

### PyMC-Marketing example data (mmm_example.csv)
- **Source:** PyMC Labs, 2023 onward, dataset in the pymc-marketing repo; Apache 2.0
- **Link:** https://raw.githubusercontent.com/pymc-labs/pymc-marketing/main/data/mmm_example.csv (verified by download); notebook https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html
- **Why it matters:** 179 weekly rows (2 April 2018 to 30 August 2021), 2 media channels, 2 event dummies, trend and seasonality helpers (8 columns, 12 KB). Tiny, so sampling is fast; matches the library's own tutorial.
- **Use in course:** Session 2 warm-up before the Alpenglow Germany data.

### Robyn demo data (dt_simulated_weekly)
- **Source:** Meta Marketing Science, 2021 onward, dataset shipped with Robyn (R and Python); MIT
- **Link:** https://raw.githubusercontent.com/facebookexperimental/Robyn/main/python/src/robyn/tutorials/resources/dt_simulated_weekly.csv (verified by download); documentation https://rdrr.io/cran/Robyn/man/dt_simulated_weekly.html (unverified: proxy blocked)
- **Why it matters:** 208 weekly rows (23 November 2015 to 11 November 2019), 12 columns: revenue, TV, OOH, print, Facebook (impressions and spend), search (clicks and spend), competitor sales, events, newsletter. The most widely used MMM demo, so students can compare their Python results with countless Robyn write-ups.
- **Use in course:** Session 2 lab or exercise (reproduce a Robyn-style decomposition in PyMC-Marketing).

### Synthetic benchmark with endogenous marketing spend
- **Source:** arXiv 2608.21130, 2026, paper plus seeded generator and reference instance with notebooks; licence stated in the repository (unverified)
- **Link:** https://arxiv.org/html/2608.21130 (unverified: proxy blocked; confirmed in search)
- **Why it matters:** Unlike Robyn and Meridian simulations, spend here reacts to seasons, promotions and past performance, so it tests whether a model survives endogeneity; ground truth is known.
- **Use in course:** Session 3 or 5 stretch exercise: fit the course model and check recovery of true ROAS.

### siMMMulator and PySiMMMulator (simulation packages)
- **Source:** Meta Marketing Science (R, MIT, author Jessica Nguyen) and PySiMMMulator (Python port, PyPI 0.6.2, 2024, Ryan Duecker); software
- **Link:** https://github.com/facebookexperimental/siMMMulator (verified); https://pypi.org/project/pysimmmulator/ (verified)
- **Why it matters:** Generate MMM data from first principles (baseline, spend, impressions, conversions) with user-chosen true ROI, so students can make their own ground-truth tests.
- **Use in course:** Session 5 project option: build a simulator for a seventh market.

### Meta GeoLift sample data
- **Source:** Meta, 2021 onward, datasets in the GeoLift R package (GeoLift_PreTest, GeoLift_Test, GeoLift_Test_MultiCell); MIT
- **Link:** https://github.com/facebookincubator/GeoLift/tree/main/data (verified)
- **Why it matters:** Daily sales by location for pre-test and test periods, built for synthetic-control geo experiments; the pre-test file is the standard power-analysis example.
- **Use in course:** Session 4 geo-lift lab (load the .rda files with pyreadr).

### Kaggle: Sample Media Spends Data
- **Source:** Kaggle user yugagrawal95, dataset; licence not visible from here (unverified)
- **Link:** https://www.kaggle.com/datasets/yugagrawal95/sample-media-spends-data (confirmed in search; page blocked by proxy)
- **Why it matters:** 3,051 rows, 9 columns, 113 weeks (January 2018 to February 2020), 8 digital channels (Facebook, Google search, email, YouTube, affiliate and more) plus sales; channel-week long format is good practice for reshaping.
- **Use in course:** Session 2 exercise; requires a Kaggle account.

### Kaggle: MMM demo dataset (bike sales)
- **Source:** Kaggle user mattwalentosky, dataset; licence not visible from here (unverified)
- **Link:** https://www.kaggle.com/datasets/mattwalentosky/mmmdemodataset (confirmed in search)
- **Why it matters:** Five years of fictitious weekly bike sales driven by Google Trends plus marketing spend; useful for showing how a search-interest covariate can absorb media effects.
- **Use in course:** Session 4 forecasting exercise.

### Dunnhumby: The Complete Journey and Breakfast at the Frat
- **Source:** dunnhumby Source Files, retail transaction and promotion datasets; free download under dunnhumby terms (non-commercial; permission needed to publish results, per search summary; unverified)
- **Link:** https://www.dunnhumby.com/source-files/ (confirmed in search; page blocked by proxy); Kaggle mirror https://www.kaggle.com/datasets/frtgnn/dunnhumby-the-complete-journey
- **Why it matters:** Complete Journey: 2,500 households over two years with transactions, coupons and campaigns. Breakfast at the Frat: 156 weeks of store-product sales with base price, shelf price and display/feature flags across four categories, the cleanest free data for price and promotion elasticities.
- **Use in course:** Session 1 elasticity lab (Breakfast at the Frat); Session 4 attribution background.

### Dominick's Finer Foods scanner data
- **Source:** Kilts Center, Chicago Booth, store-level weekly scanner data 1989 to 1997; free for academic use with registration. Eurostat's cleaned version and code: EUPL 1.2
- **Link:** https://www.chicagobooth.edu/research/kilts/research-data/dominicks (confirmed in search); cleaned files and R code https://github.com/eurostat/dff (verified)
- **Why it matters:** About 100 million observations, 18,000 UPCs, 29 categories, 90+ stores, almost 400 weeks; the classic for store-level price response and a reasonable stand-in for a "geo" panel.
- **Use in course:** Session 1 or 3 (treat stores as geos); subset one category before class.

### NielsenIQ via the Kilts Center (Consumer Panel, Retail Scanner, Ad Intel)
- **Source:** Kilts Center, Chicago Booth; academic subscription, US data only
- **Link:** https://www.chicagobooth.edu/research/kilts/research-data/nielseniq/pricing ; Ad Intel https://www.chicagobooth.edu/research/kilts/research-data/nielsen-ad-intel
- **Why it matters:** Weekly retail scanner data since 2006 from 90+ chains plus advertising occurrences by media type: the only large public-to-academics source that combines sales and advertising.
- **Use in course:** Background and thesis work only. Cost USD 3,000 for three years for one dataset (faculty subscription; up to two PhD students free); not usable for a 30-student class.

### Google Trends
- **Source:** Google, ongoing; web tool and unofficial Python access (pytrends)
- **Link:** https://trends.google.com/trends/ (unverified: proxy blocked; standard URL)
- **Why it matters:** Free weekly search-interest indices by country, the standard proxy for demand and for organic interest in all six Alpenglow markets; index values (0 to 100) are relative, not volumes.
- **Use in course:** Session 3 and 4 covariate; mind rate limits and the terms of service.

### Eurostat
- **Source:** European Commission, ongoing; database and API (Python package eurostat); CC BY 4.0
- **Link:** https://ec.europa.eu/eurostat/web/main/data/database (unverified: proxy blocked; standard URL)
- **Why it matters:** Monthly HICP, retail trade volume, consumer confidence and unemployment for AT, DE, FR, IT, NL, PL; the natural macro controls for a cross-country MMM and the source for PPP price-level adjustments.
- **Use in course:** Session 3 (controls and price-level normalisation).

### World Bank World Development Indicators
- **Source:** World Bank, ongoing; API (Python package wbgapi); CC BY 4.0
- **Link:** https://data.worldbank.org/ (unverified: proxy blocked; standard URL)
- **Why it matters:** Annual GDP per capita, PPP conversion factors, population and internet penetration for every country; needed when extending the model to emerging markets or scaling spend across currencies.
- **Use in course:** Session 3 and 5 (emerging-market extension in projects).

### LightweightMMM simulate_dummy_data (legacy)
- **Source:** Google, 2022 to 2025, archived January 2026; Apache 2.0
- **Link:** https://github.com/google/lightweight_mmm (verified; archived, Google recommends Meridian)
- **Why it matters:** A one-line simulator for national or geo MMM data with configurable channels and geos; still handy for quick demos even though the library is unmaintained.
- **Use in course:** Instructor-only for generating quiz data; do not teach the library.

---

## Gaps and caveats

- Network limits: the session's web search budget ran out and the egress proxy blocked most non-GitHub domains (Springer, arXiv, PyMC Labs, Kaggle, dunnhumby, LinkedIn, university sites, INFORMS, EMAC, PyData). Links from those domains were confirmed only through search results and are marked "(unverified)"; GitHub repositories, raw CSVs and PyPI were fetched directly.
- Named DACH practitioners: agencies and vendors do not publish their MMM leads. Analytic Partners' German managing director is cited from a 2017 announcement and may have changed; the Beiersdorf and Henkel LinkedIn profiles surfaced in search but their exact roles could not be read. Zalando, HelloFresh, Douglas, adidas, Puma, BMW, Mercedes, Swarovski, Spar, A1, Erste, Raiffeisen and Austrian Airlines returned no public MMM-specific person or page and were left out; the HelloFresh and Bolt case studies on the PyMC Labs blog are the best route to those brands.
- Accenture Song, Artefact, Publicis, Omnicom (Annalect), Ipsos and Nielsen have DACH offices but no public MMM contact or page specific to Austria or Germany was found.
- Conference dates: ISMS 2026, EMAC 2026 (spring and fall) and PyData Amsterdam 2026 are before the course starts; 2027 editions (EMAC Rome, ISMS Seattle) are the ones to point students to. Meta's MMM Summit, Marketing Analytics Summit and a PyData Vienna meetup could not be dated for 2026/27. No verifiable MMM LinkedIn group was found; MMM Hub's Slack fills that role.
- Datasets: Kaggle licences could not be read (typically CC0 or "other"); Dunnhumby's terms restrict publication; NielsenIQ is paid, US-only and faculty-gated; Google Trends is an index, not volume, and its API access is unofficial. The arXiv benchmark's repository URL and licence are in the paper, which could not be fetched. Sizes for Meridian, PyMC-Marketing and Robyn files were measured from the downloaded CSVs on 5 October 2026.
