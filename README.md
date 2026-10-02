# International Marketing Analytics

Course repository for **International Marketing Analytics**, MSc International Management / CEMS, WU Vienna (Dr. Arne Floh). Winter term 2026/27, 6 October to 3 November 2026.

The course teaches marketing mix modelling (MMM), forecasting, experiments and attribution for a brand operating in six European markets, using Python, Positron, Quarto and GitHub with AI-assisted coding.

## Start here

| You are | Go to |
|---|---|
| A student preparing for Session 1 | [`setup/setup-guide.qmd`](setup/setup-guide.qmd), then [`syllabus/syllabus.qmd`](syllabus/syllabus.qmd) |
| A student in a session | `sessions/0X-.../lab.qmd` |
| A group working on the project | [`assignments/group-project/brief.qmd`](assignments/group-project/brief.qmd) |
| The instructor | [`instructor/course_design.md`](instructor/course_design.md) (design spec, solutions, ground truth) |

## Sessions

| # | Folder | Theme |
|---|---|---|
| 1 | `sessions/01-foundations` | Toolkit (Positron, Quarto, GitHub, AI assistants) and regression foundations: price and promotion elasticities across countries |
| 2 | `sessions/02-mmm-one-country` | MMM I: adstock, saturation, baseline vs incremental, ROAS, diagnostics (Germany) |
| 3 | `sessions/03-mmm-multi-country` | MMM II: panel fixed effects, hierarchical Bayesian MMM with PyMC-Marketing, budget allocation across countries and channels |
| 4 | `sessions/04-forecasting-experiments-attribution` | Forecasting as regression, geo-lift experiments and causal inference, multi-market attribution |
| 5 | `sessions/05-project-pitches` | Group project pitches, ground-truth reveal, wrap-up |

Each session folder contains `slides.qmd` (renders to reveal.js and PowerPoint), `lab.qmd` (guided, executable), `exercises.qmd` and `quiz.md`.

## Data

All datasets describe **Alpenglow**, a fictional Vienna-based premium chocolate brand in AT, DE, FR, IT, NL and PL. See [`data/README.md`](data/README.md) for the data dictionary. The data are synthetic with known ground truth, which the instructor reveals in Session 5.

## Quick start (instructor or advanced student)

```bash
uv venv && uv pip install -r requirements.txt
quarto render                                    # all student-facing material to _site/
quarto render sessions/02-mmm-one-country/slides.qmd --to revealjs,pptx
pytest assignments/checks                        # auto-checks for lab check-ins
```

## Repository layout

```
syllabus/        syllabus (HTML, DOCX)
setup/           installation and GitHub guide
data/            datasets, generator, data dictionary
sessions/        slides, labs, exercises, quizzes per session
assignments/     group project brief and rubric, auto-checks, quiz banks
assets/          Quarto theme and helper module (mma.py)
instructor/      design spec, solutions, ground truth, grading (not for students)
```

## Licence

Teaching materials © Arne Floh, WU Vienna. Code under the MIT licence. Legacy datasets in `data/legacy/` retain their original licences (Kaggle, Inside Airbnb).
