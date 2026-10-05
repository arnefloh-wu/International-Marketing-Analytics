### Bücher (15)
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
		<td>Bücher</td>
		<td>An Introduction to Statistical Learning, with Applications in Python (ISLP)</td>
		<td>James, Witten, Hastie, Tibshirani and Taylor, Springer, 2023, book (free PDF on the book website)</td>
		<td>[https://www.statlearning.com/](https://www.statlearning.com/)</td>
		<td>Chapter 3 (linear regression) uses the Advertising data (sales on TV, radio, newspaper), covers qualitative predictors, the TV x radio interaction, polynomial terms and residual diagnostics; Chapter 7 covers polynomials, step functions and splines. The Ch03-linreg-lab.ipynb notebook is maintained and uses statsmodels. The cleanest marketing-flavoured, free, Python-native regression text available.</td>
		<td>Session 1 (Ch. 3 as core reading and lab warm-up), Session 2 (Ch. 7 sections on non-linear fits as background to saturation curves); free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Python for Marketing Research and Analytics</td>
		<td>Jason S. Schwarz, Chris Chapman and Elea McDonnell Feit, Springer, 2020, book (283 pp.)</td>
		<td>[https://doi.org/10.1007/978-3-030-49720-0](https://doi.org/10.1007/978-3-030-49720-0)</td>
		<td>The only Python regression text written for marketers. Chapter 7 "Identifying Drivers of Outcomes: Linear Models" (doi 10.1007/978-3-030-49720-0_7) runs a satisfaction-drivers regression with statsmodels formulas, standardisation, factor (dummy) coding, interactions and a short marketing-mix example; Chapter 8 "Additional Linear Modeling Topics" covers collinearity/VIF, logistic regression and hierarchical models. All examples are Colab notebooks with simulated marketing data.</td>
		<td>Session 1 (Ch. 7 as reading; notebooks as lab), Session 2 (Ch. 8 on collinearity); paid (Springer, often free via WU SpringerLink licence).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Regression and Other Stories</td>
		<td>Andrew Gelman, Jennifer Hill and Aki Vehtari, Cambridge University Press, 2020 (corrected online version), book; free PDF for personal use</td>
		<td>[https://users.aalto.fi/\~ave/ROS.pdf](https://users.aalto.fi/~ave/ROS.pdf)</td>
		<td>The best modern teaching text on interpreting regression. Ch. 10 (multiple predictors, indicator variables, interactions), Ch. 11 (assumptions, diagnostics, model evaluation, with a clear ranking of which assumptions matter most), Ch. 12 (log transformations and elasticity-style interpretation, standardising) and Chs. 18 to 21 (causal inference with regression) map directly onto Session 1. Simulation-first style suits AI-assisted coding.</td>
		<td>Session 1 (Chs. 10 and 12 as reading), Session 2 (Ch. 11 on diagnostics); free PDF; examples are R/rstanarm, Python port partial.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Introduction to Mediation, Moderation, and Conditional Process Analysis (3rd ed.)</td>
		<td>Andrew F. Hayes, Guilford Press, January 2022, book (732 pp.)</td>
		<td>[https://www.routledge.com/Introduction-to-Mediation-Moderation-and-Conditional-Process-Analysis-Third-Edition-A-Regression-Based-Approach/Hayes/p/book/9781462549030](https://www.routledge.com/Introduction-to-Mediation-Moderation-and-Conditional-Process-Analysis-Third-Edition-A-Regression-Based-Approach/Hayes/p/book/9781462549030)</td>
		<td>The PROCESS reference used by almost every consumer-behaviour paper students will read. Parts on mediation, moderation (simple slopes, Johnson-Neyman, multicategorical moderators) and conditional process (moderated mediation) are all OLS-based; the 3rd edition adds PROCESS for R next to SPSS and SAS. Use it to give students the vocabulary, then reproduce the models in statsmodels.</td>
		<td>background (instructor reference for moderation in Session 1 and any student project with survey data); paid (about EUR 80).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Coding for Economists</td>
		<td>Arthur Turrell, 2021 to present, free online book (Python, Quarto/Jupyter)</td>
		<td>[https://aeturrell.github.io/coding-for-economists](https://aeturrell.github.io/coding-for-economists)</td>
		<td>Python-only, current and practical. The econmt-regression chapter shows statsmodels and pyfixest with formulas, fixed effects, robust and clustered standard errors and regression tables; econmt-diagnostics covers residual and influence diagnostics; time-series covers lags and autocorrelation. Closest in spirit to the course stack.</td>
		<td>Session 1 and Session 3 (regression and fixed-effects chapters as lab reference), Session 4 (time-series chapter); free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Introductory Econometrics: A Modern Approach (8th ed.) with Using Python for Introductory Econometrics (2nd ed.)</td>
		<td>Jeffrey M. Wooldridge, Cengage, January 2025, book; Florian Heiss and Daniel Brunner, 2024, free open-access Python companion</td>
		<td>[https://www.cengage.com/c/introductory-econometrics-a-modern-approach-8e-wooldridge/9780357900161/](https://www.cengage.com/c/introductory-econometrics-a-modern-approach-8e-wooldridge/9780357900161/)</td>
		<td>The standard applied econometrics text: Ch. 6 (logs, quadratics, interactions), Ch. 7 (dummy variables, interactions with dummies, Chow tests), Ch. 8 (heteroskedasticity-robust inference), Chs. 10 to 12 (time-series regression, trends, seasonality, serial correlation, HAC errors). Heiss and Brunner reproduce every example in Python with statsmodels and the wooldridge data package, chapter for chapter.</td>
		<td>Session 1 (Chs. 6 to 7), Session 4 (Chs. 10 to 12); Wooldridge paid (about EUR 70 to 90), UPfIE free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Forecasting: Principles and Practice, the Pythonic Way</td>
		<td>Rob J. Hyndman, George Athanasopoulos, Azul Garza, Cristian Challu, Max Mergenthaler and Kin G. Olivares, OTexts, 2025 (print May 2026), free online book</td>
		<td>[https://otexts.com/fpppy/](https://otexts.com/fpppy/)</td>
		<td>Python (Nixtla) edition of fpp3. The time-series regression chapter (trend, seasonal dummies, Fourier terms, lagged predictors, residual autocorrelation checks) and the dynamic regression chapter (regression with ARIMA errors, distributed lags) are the clearest free treatment of forecasting as regression. First 13 chapters follow fpp3 numbering (Ch. 7 time-series regression, Ch. 10 dynamic regression, unverified for the Python edition).</td>
		<td>Session 4 (core reading for forecasting as regression), Session 2 (seasonality controls); free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>The Effect: An Introduction to Research Design and Causality (2nd ed.)</td>
		<td>Nick Huntington-Klein, Chapman and Hall/CRC (Routledge), July 2025, book; free online edition</td>
		<td>[https://theeffectbook.net/](https://theeffectbook.net/)</td>
		<td>Ch. 13 "Regression" explains controls, polynomial terms, logs, interactions, robust and clustered standard errors with R, Stata and Python code side by side; the causal-diagram chapters explain why "controlling for" a mediator distorts a marketing effect. Written for students with no maths background.</td>
		<td>Session 1 (Ch. 13), Session 4 (difference-in-differences and synthetic control chapters); free online, print about EUR 60.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Causal Inference for the Brave and True</td>
		<td>Matheus Facure, 2020 to present, free online book (Python)</td>
		<td>[https://matheusfacure.github.io/python-causality-handbook/landing-page.html](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)</td>
		<td>Short, humorous Python chapters on regression as a causal tool, omitted-variable bias, good and bad controls, dummy-variable regression, fixed effects and difference-in-differences, all in statsmodels. A good bridge from Session 1 elasticities to Session 4 experiments.</td>
		<td>Session 1 and Session 4 (optional readings); free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Introduction to Econometrics (4th ed.)</td>
		<td>James H. Stock and Mark W. Watson, Pearson, 2019 (Global Edition ISBN 9781292264455), book</td>
		<td>[https://www.pearson.com/en-gb/subject-catalog/p/introduction-to-econometrics-global-edition/P200000005500/9781292740652](https://www.pearson.com/en-gb/subject-catalog/p/introduction-to-econometrics-global-edition/P200000005500/9781292740652)</td>
		<td>The "nonlinear regression functions" chapter (polynomials, logs, interactions between binary and continuous regressors) is the best textbook chapter on log-log versus log-linear interpretation; the time-series chapters cover distributed lags and HAC standard errors. Clear, intuitive, widely available in European libraries.</td>
		<td>background (Session 1 for log specifications, Session 4 for dynamic causal effects); paid.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Principles of Econometrics (5th ed.)</td>
		<td>R. Carter Hill, William E. Griffiths and Guay C. Lim, Wiley, 2018, book (912 pp.)</td>
		<td>[https://www.wiley.com/en-us/Principles+of+Econometrics,+5th+Edition-p-9781119320944](https://www.wiley.com/en-us/Principles+of+Econometrics,+5th+Edition-p-9781119320944)</td>
		<td>More gentle and example-heavy than Wooldridge, with chapters on indicator variables, heteroskedasticity and time-series regression (lags, serial correlation, HAC errors). Data sets are downloadable in several formats, which makes it easy to port examples to Python.</td>
		<td>background (alternative textbook for students needing more worked examples); paid.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Multivariate Data Analysis (8th ed.)</td>
		<td>Joseph F. Hair, William C. Black, Barry J. Babin and Rolph E. Anderson, Cengage, 2019, book (832 pp.)</td>
		<td>[https://www.cengageasia.com/TitleDetails/isbn/9781473756540](https://www.cengageasia.com/TitleDetails/isbn/9781473756540)</td>
		<td>The marketing-research classic; Ch. 5 "Multiple Regression" walks through design, assumptions, VIF thresholds, dummy coding and validation in the step-by-step style business students and reviewers expect. Software-neutral (no Python), and some rules of thumb (VIF cut-offs) are more conservative than current practice.</td>
		<td>background (Ch. 5 as a checklist for the project report); paid.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Discovering Statistics Using IBM SPSS Statistics (6th ed.)</td>
		<td>Andy Field, SAGE, February 2024, book (1,144 pp.)</td>
		<td>[https://uk.sagepub.com/en-gb/eur/discovering-statistics-using-ibm-spss-statistics/book285130](https://uk.sagepub.com/en-gb/eur/discovering-statistics-using-ibm-spss-statistics/book285130)</td>
		<td>Ch. 11 (moderation and mediation with PROCESS, including a two-mediator example new in this edition) and Ch. 12 (categorical predictors and dummy coding) are the friendliest explanations for students with no maths background. SPSS-based, so use for concepts only.</td>
		<td>background (students who need an intuitive explanation of interactions or dummy coding); paid.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Statistical Rethinking (2nd ed.) with the PyMC port</td>
		<td>Richard McElreath, CRC Press, 2020, book; PyMC port by the PyMC developers</td>
		<td>[https://github.com/pymc-devs/pymc-resources/tree/main/Rethinking_2](https://github.com/pymc-devs/pymc-resources/tree/main/Rethinking_2)</td>
		<td>Ch. 4 (linear regression, polynomials, splines), Ch. 5 (multiple regression, categorical variables, spurious association), Ch. 6 (causal diagrams, post-treatment bias) and Ch. 8 (interactions) give the Bayesian view students need before PyMC-Marketing in Session 3. The PyMC notebooks reproduce the code in Python.</td>
		<td>Session 3 (background for Bayesian and hierarchical regression); book paid, notebooks free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Bücher</td>
		<td>Applied Regression Analysis and Generalized Linear Models (3rd ed.)</td>
		<td>John Fox, SAGE, 2016 (published 2015), book</td>
		<td>[https://us.sagepub.com/en-us/nam/applied-regression-analysis-and-generalized-linear-models/book237254](https://us.sagepub.com/en-us/nam/applied-regression-analysis-and-generalized-linear-models/book237254)</td>
		<td>The reference for diagnostics: dummy-variable regression (Ch. 7), unusual and influential data (Ch. 11), non-normality, non-constant variance and non-linearity (Ch. 12), collinearity (Ch. 13). Graduate level; use for instructor preparation and for answering "is this outlier a problem?" questions.</td>
		<td>background (Session 2 diagnostics); paid.</td>
		<td>neu; Link geprüft</td>
	</tr>
</table>