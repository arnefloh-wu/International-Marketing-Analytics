# Regression analysis with Python: books, journal articles, reports, teaching cases and course examples

Part 02 of the regression resource search (brief: `RESEARCH_BRIEF_REGRESSION.md`). Covers four categories: Books; Journal articles; Reports; Teaching cases and course examples. Searched 5 October 2026. The Consensus tool was out of quota (30 of 30 searches used), so every DOI below comes from web search listings (publisher, JSTOR, RePEc, SSRN or university repository pages). The sandbox proxy blocked almost every publisher and course host (Wiley, Springer, INFORMS, SAGE, Cambridge, otexts.com, statlearning.com, theeffectbook.net, quantecon.org, duke.edu, nist.gov, arxiv.org, Darden store, Crossref API); GitHub pages could be fetched and were used to confirm book code, notebooks and course repositories. Entries resting on a search listing alone for a detail are marked "(unverified)" at that detail.

Session map used below (from `instructor/course_design.md`): Session 1 regression foundations (coefficients, log-log elasticities, dummies, interactions, multicollinearity, cross-country comparison with Hofstede/GDP); Session 2 MMM I (adstock, saturation, residual autocorrelation, VIF); Session 3 MMM II (pooled vs fixed effects vs hierarchical, clustering); Session 4 forecasting as regression (trend, seasonality, lags), experiments, attribution; Session 5 pitches. Mediation is not a scheduled topic, so mediation material is tagged "background" or optional Session 1 extension.

## Books

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
