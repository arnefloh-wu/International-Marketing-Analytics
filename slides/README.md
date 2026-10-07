# Slides

Course decks on the WU template, built with the `polish-slides` and `add-instructor-slide` skills (`.claude/skills/`).

| File | Content |
|---|---|
| `00a_course-content-and-style_WT26-27.pptx` / `.pdf` | Course outline: welcome, instructor profile, module content, course roadmap, learning outcomes, methods, roadmap table, assessment strategy, software and set-up, online certificates, coding exercises, written exam, case study report, contact (18 slides) |
| `01a_setup-and-registration_WT26-27.pptx` / `.pdf` | Session 1 set-up deck (45 slides, six parts): registrations; installation (Python 3.14.8, Positron 2026.09, Quarto, GitHub Desktop, the course repository, the project .venv, the check and the stack test `test_stack.qmd`, Posit Assistant); how Positron works (panes, projects, shortcuts, Posit Assistant); GitHub Desktop (the window, the everyday workflow, the group project); Quarto (how it works, the YAML header, code cells, output formats); Python packages (install, Packages pane, load, polars, plotnine, Great Tables, statsmodels); troubleshooting, checklist |
| `01b_statistics-and-regression_WT26-27.pptx` / `.pdf` | Statistics refresher and linear regression (Session 1, 66 slides, eleven parts). Refresher (Parts 1 to 5) on a chocolate kiosk with five weeks of prices and sales: scale types; mean and median; variance, standard deviation and standard error; z-scores; normal and standard normal distribution; covariance and correlation and the bridge to the regression slope; the packages and how to install and load them; the same calculations by hand in Python with checks; an exercise and quiz 1. Regression (Parts 6 to 11) on real chocolate scanner data: simple and multiple OLS, inference, fit, logs and dummies, from elasticity to price; seven assumptions with residual plots and tests (Durbin-Watson, Breusch-Pagan, Jarque-Bera, VIF, Cook's distance) and remedies; benchmarks and company uses; statsmodels and plotnine code; quiz 2; in-class assignment; coding exercise 1. Core readings Bojinov, Parzen & Hamilton (2025) and Skiera, Reiner & Albers (2022). Code: `sessions/01-foundations/stats_refresher.qmd`, `sessions/01-foundations/regression_chocolate.qmd` |
| `02a_intro-to-mmm_WT26-27.pptx` / `.pdf` | Introduction to marketing mix modelling (44 slides, seven parts), based on `instructor/resources/mmm-resource-guide.md`; examples come from the literature, charts from simulated data (Alpenglow is kept for the labs and the case study): the international brand manager's "next euro" question; what MMM is (definition, inputs and outputs, MMM versus attribution and experiments, history); why attribution is not enough (global and European ad spend, last click, six problems, switch-off tests at eBay, Uber, P&G, Airbnb, Facebook); how it works (base and incremental, the regression, adstock, saturation, seasonality, two key-terms slides); empirical generalisations (advertising and price elasticities, carryover, country differences); doing it well (data, pitfalls, validation, Bayesian priors, Robyn, Meridian, PyMC-Marketing); the reading Fantini & Narayandas 2023 (HBR) with a two-slide in-class discussion on MMM for international brand managers; MMM in this course; takeaways, further reading |
| `build_course_outline.py` | Builds the outline deck on the skill's template with the design patterns in `polish-slides/references/design-patterns.md` (icon rows, grouped bands, two-card comparisons, steppers, stat rows, native chart, session card grid) |
| `finish_profile_slides.py` | Adapts the instructor profile slides to this deck: 16 pt titles, 15 pt card headings, the two Module Convenor cards merged into one with an online office-hours link (the skill asset is unchanged) |
| `build_setup_deck.py` | Builds the set-up deck |
| `make_quarto_figures.py`, `quarto_demo/` | Renders the demo report to HTML, PDF (Typst), Word and reveal.js and saves the thumbnails for the Quarto slides |
| `make_setup_figures.py` | Runs the package code shown on the set-up slides and saves the chart, table and numbers to `figures/` |
| `build_stats_regression_deck.py`, `make_refresher_figures.py`, `make_regression_figures.py` | Build the statistics and regression deck: run `python slides/make_refresher_figures.py` and `python slides/make_regression_figures.py`, then `python slides/build_stats_regression_deck.py .claude/skills/polish-slides/assets/template.pptx slides/01b_statistics-and-regression_WT26-27.pptx` |
| `build_mmm_intro.py` | Builds the MMM introduction deck: `python slides/build_mmm_intro.py .claude/skills/polish-slides/assets/template.pptx slides/02a_intro-to-mmm_WT26-27.pptx` (run `make_mmm_figures.py` first) |
| `make_mmm_figures.py` | Draws the plotnine charts for the MMM deck from the Alpenglow data (`figures/mmm_*.png`: German sales and TV spend, a base-versus-media decomposition, adstock with decay 0.3 and 0.7, a Hill saturation curve) and writes every number quoted on the slides to `figures/mmm_numbers.txt` |
| `wu_deck.py` | Shared helpers for both builders: deck from the template, boxes, text, cards, steppers, code blocks |
| `icons/` | Lucide line icons as PNG in WU navy, blue and white; `render_icons.js` regenerates them |

Type sizes: 13 pt text, 15 pt table and card headings, 16 pt slide titles, 28 pt figures.

Rebuild and check:

```bash
python slides/build_course_outline.py .claude/skills/polish-slides/assets/template.pptx "old-slides/00a_Course Content & Style_WT25-26.pptx" /tmp/outline.pptx
python .claude/skills/add-instructor-slide/scripts/add_instructor_slides.py /tmp/outline.pptx -o slides/00a_course-content-and-style_WT26-27.pptx --after 2
python slides/finish_profile_slides.py slides/00a_course-content-and-style_WT26-27.pptx
python .claude/skills/polish-slides/scripts/check_deck.py slides/00a_course-content-and-style_WT26-27.pptx /tmp/qa

python slides/make_setup_figures.py
python slides/make_quarto_figures.py
python slides/build_setup_deck.py .claude/skills/polish-slides/assets/template.pptx slides/01a_setup-and-registration_WT26-27.pptx
python .claude/skills/polish-slides/scripts/check_deck.py slides/01a_setup-and-registration_WT26-27.pptx /tmp/qa-setup
```

Run these from the repository root with the course `.venv` active.

Session decks for the lectures are generated from Quarto (`sessions/0X-*/slides.qmd`, rendered to reveal.js and PowerPoint).
