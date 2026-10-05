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
