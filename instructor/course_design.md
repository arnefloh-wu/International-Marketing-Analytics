# International Marketing Analytics — Course Design Specification

**Programme:** MSc International Management / CEMS, WU Vienna
**Course type:** CEMS Hard Skills / Exclusive / Data Analytics (in person)
**Lecturer:** Dr. Arne Floh
**Term:** Winter 2026/27, 6 October – 3 November 2026
**Cohort:** ~30 CEMS students, no prior programming or statistics beyond bachelor level
**Language:** English

> Items marked **[SYLLABUS]** must be aligned with the official WU course page
> (vvz.wu.ac.at, course 1243, 26W). The page could not be read from the build
> environment, so dates, hours, ECTS and assessment weights below are working
> assumptions.

## 1. Teaching philosophy

1. **Decision first, method second.** Every session starts from a budget or market decision an international marketing manager has to make and works backwards to the regression that answers it.
2. **AI-assisted analytics.** Students do not learn to write Python from scratch. They learn to *specify*, *run*, *read*, *check* and *communicate* analyses with an AI coding assistant inside Positron. Every lab therefore includes a "prompt pattern", a "what to check" list and a "what can go wrong" box.
3. **One running case.** Alpenglow, a fictional Vienna-based premium chocolate brand active in AT, DE, FR, IT, NL and PL. All datasets (weekly MMM panel, German geo-lift test, multi-market customer journeys) describe this company. The group project is the final decision: allocate next year's media budget across countries and channels.
4. **Reproducible, versioned work.** Everything lives in GitHub. Students fork or clone the course repo, work in Quarto, and submit the group project as a GitHub repository with a rendered report.
5. **Regression as the unifying language.** OLS, log-log, fixed effects, logistic, Bayesian hierarchical regression, regression with lags: students see that MMM, forecasting, experiments, attribution are all regressions with different design matrices.

## 2. Learning outcomes

After the course, students can:

1. Explain the logic of marketing mix modelling (MMM): carryover (adstock), saturation, baseline vs incremental sales, ROAS vs marginal ROAS.
2. Specify, estimate and diagnose regression models for marketing response data in Python (OLS, log-log elasticity models, panel fixed effects, hierarchical Bayesian models with PyMC-Marketing).
3. Translate model output into a cross-country, cross-channel budget allocation and defend it under uncertainty.
4. Produce and evaluate short-term sales forecasts and use them as the baseline for planning.
5. Design and analyse a marketing experiment (geo-lift / matched markets) and use it to calibrate an MMM.
6. Compare attribution approaches (last-touch, logistic regression, Shapley) and explain why they disagree across markets.
7. Work reproducibly with Python, Positron, Quarto and GitHub, using AI assistants responsibly: verifying outputs, documenting prompts, and recognising hallucinated or misleading results.

## 3. Schedule **[SYLLABUS]**

Assumed: five Tuesday sessions of four teaching hours each.

| # | Date | Theme | Decision of the day |
|---|------|-------|---------------------|
| 1 | Tue 6 Oct 2026 | Toolkit & regression foundations | "Is our price too high in Poland?" Price and promotion elasticities |
| 2 | Tue 13 Oct 2026 | Marketing mix modelling I: one country | "What did TV do for us in Germany?" Adstock, saturation, ROAS |
| 3 | Tue 20 Oct 2026 | MMM II: many countries, one budget | "Where should the next euro go?" Panel/hierarchical MMM, budget allocation |
| 4 | Tue 27 Oct 2026 | Forecasting, experiments, attribution | "Can we trust the model?" Forecast baseline, geo-lift test, multi-market attribution |
| 5 | Tue 3 Nov 2026 | Group project pitches & wrap-up | "Board meeting": present and defend the 2027 budget |

Session rhythm (4 h): 60 min concept lecture → 90 min guided lab → 15 min break → 60 min team exercise on the project data → 15 min debrief, quiz opens.

## 4. Assessment **[SYLLABUS]**

| Component | Weight | Individual / group | Auto-graded |
|-----------|--------|--------------------|-------------|
| Four weekly online quizzes (Sessions 1–4), best 3 of 4 | 30 % | individual | yes (Moodle/Canvas-ready question bank) |
| Two lab check-ins (Session 2, Session 4): short Quarto notebook, auto-checked with `pytest` | 20 % | individual | yes (`assignments/checks/`) |
| Group project: Alpenglow 2027 budget allocation (GitHub repo + Quarto report + 10-min pitch) | 40 % | group of 5 | rubric + automated checks |
| Peer evaluation & contribution (GitHub commit history, peer form) | 10 % | individual | partly |

Grading scale (WU): 1 (≥ 90 %), 2 (80–89 %), 3 (70–79 %), 4 (60–69 %), 5 (< 60 %). Attendance required at ≥ 80 % of sessions (WU PI rule). **[SYLLABUS]**

## 5. Tooling

- Python 3.11+ managed with `uv`; dependencies in `pyproject.toml` / `requirements.txt`.
- Positron IDE (Posit) with the Python extension and an AI assistant (Positron Assistant, GitHub Copilot, or Claude Code; any of the three is acceptable).
- Quarto for labs, reports and slides. Slides render to **reveal.js** (HTML) and **PowerPoint** from the same `.qmd`.
- GitHub: course organisation, one repo per group, GitHub Desktop for students.
- Key libraries: pandas, numpy, statsmodels, scikit-learn, linearmodels (panel FE), pymc-marketing (Bayesian MMM, budget optimiser), matplotlib/plotly.

## 6. Repository layout

```
.
├── README.md                     # course landing page
├── syllabus/                     # syllabus.qmd → HTML/DOCX
├── setup/                        # installation and GitHub guide
├── data/                         # all datasets + generator + data dictionary
│   ├── mmm/                      # Alpenglow weekly panel, country metadata
│   ├── experiments/              # German geo-lift test
│   ├── attribution/              # multi-market journeys
│   └── legacy/                   # older datasets used in Session 1 warm-ups
├── sessions/
│   ├── 01-foundations/           # slides.qmd, lab.qmd, exercises.qmd, quiz.md
│   ├── 02-mmm-one-country/
│   ├── 03-mmm-multi-country/
│   ├── 04-forecasting-experiments-attribution/
│   └── 05-project-pitches/
├── assignments/
│   ├── group-project/            # brief, rubric, template repo
│   ├── checks/                   # pytest auto-checks for lab check-ins
│   └── quizzes/                  # question banks (Markdown + GIFT export)
├── instructor/                   # solutions, ground truth, grading, this file
└── _quarto.yml
```

## 7. Session blueprints

### Session 1 — Toolkit & regression foundations
- **Concepts:** analytics workflow; why regression; interpreting coefficients; log-log elasticities; dummies and interactions; multicollinearity; R² and out-of-sample fit; what AI assistants get wrong.
- **Lab:** Positron tour; clone the repo; load `data/legacy/Video_Games_Sales.csv` for regional sales descriptives; then Alpenglow panel: price elasticity by country (log-log with promo and seasonality dummies). Compare elasticities with Hofstede/GDP from `country_meta.csv`.
- **Team exercise:** "Is our price too high in Poland?" one-slide answer.
- **Deliverables:** quiz 1; GitHub: first commit in group repo.

### Session 2 — MMM I: one country
- **Concepts:** MMM history and use cases; baseline vs incremental; geometric adstock; saturation (Hill, logistic); flighting; seasonality and holiday controls; confounding between budget and seasonality; ROAS vs mROAS; model diagnostics (residual autocorrelation, VIF); holdout validation.
- **Lab:** Germany only. Build an OLS MMM step by step: raw spend → adstock → saturation → controls. Grid search over decay. Decompose sales into baseline + channel contributions. Compute ROAS and response curves.
- **Team exercise:** replicate for another country; compare TV ROAS across countries.
- **Deliverables:** quiz 2; lab check-in 1 (`assignments/checks/check_session2.py`).

### Session 3 — MMM II: many countries, one budget
- **Concepts:** pooled vs country-by-country vs fixed effects vs hierarchical models; partial pooling as the solution for small markets (AT, PL); Bayesian MMM with priors; PyMC-Marketing workflow; budget optimisation under saturation and adstock; constraints (minimum spend, country floors); uncertainty in allocation.
- **Lab:** panel OLS with country fixed effects (linearmodels / statsmodels), then PyMC-Marketing `MMM` per country and a hierarchical variant; `BudgetOptimizer` for one country; manual scipy optimiser across countries using fitted response curves.
- **Team exercise:** first draft of the 2027 allocation.
- **Deliverables:** quiz 3; project milestone (model table in repo).

### Session 4 — Forecasting, experiments, attribution
- **Concepts:** forecasting as regression (trend, seasonality, lags), ETS/ARIMA briefly, rolling-origin evaluation, forecast as baseline for budget planning; experiments as the gold standard; geo-lift / matched markets; difference-in-differences and synthetic control; calibrating MMM with a lift test; attribution: last touch vs logistic regression vs Shapley; why attribution differs by market.
- **Lab:** forecast 2026 Q1 sales for each country; analyse `geolift_germany.csv` with diff-in-differences and a synthetic control (CausalPy optional); compare attribution methods on `journeys.csv`.
- **Deliverables:** quiz 4; lab check-in 2.

### Session 5 — Project pitches
- 6 groups × 10 min pitch + 5 min Q&A; board-meeting format; instructor reveals ground truth and compares with group allocations; course wrap-up and career pointers (MMM vendors, open-source tools, analytics roles).

## 8. Style guide for materials

- Slides: Quarto `revealjs` + `pptx`, `theme: [default, ../../assets/wu.scss]`, 16:9, max 6 bullets, one chart per slide, speaker notes under `::: {.notes}`. Every session deck: title → decision of the day → concepts → method → lab bridge → recap → quiz reminder.
- Labs: Quarto `html` with `code-fold: false`, executable, run end-to-end in < 5 min on a laptop (PyMC sampling: `draws=500, tune=500, chains=2` with fixed seed). Each lab has sections: Setup → Decision → Data → Model → Interpretation → Checks → Your turn → Prompt patterns.
- Exercises: short, with hidden solutions in `instructor/solutions/`.
- Language: British English; "modelling".
- All code uses the project virtual environment (`.venv`) and relative paths from repo root.
