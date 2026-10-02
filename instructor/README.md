# Instructor area

Not for students. Contents:

| Path | Purpose |
|---|---|
| `course_design.md` | Design specification: outcomes, schedule, assessment, session blueprints, style guide |
| `AGENT_BRIEF.md` | Conventions used when (re)generating materials with AI assistance |
| `ground_truth/` | True parameters of the synthetic data generator, true contributions, true optimal allocation. Reveal in Session 5 only. |
| `solutions/` | Worked solutions for every session's exercises, with comparisons to ground truth |

## Before the term

1. Align every **[SYLLABUS]** / **[to align]** item in `course_design.md` and `syllabus/syllabus.qmd` with the WU course catalogue entry (dates, room, hours, ECTS, assessment weights, attendance rule).
2. Create a GitHub organisation for the term, push this repository as the course repo (consider a public student mirror without `instructor/`), and create six group repositories from `assignments/group-project/template/`.
3. Import quizzes: `python assignments/quizzes/convert_quiz.py` produces GIFT files for Canvas or Moodle.
4. Render everything: `quarto render`. Slides: `quarto render sessions/*/slides.qmd --to revealjs,pptx`.
5. Check the lab runtime on a typical student laptop (target under 5 minutes per lab; PyMC compiles once).

## Regenerating data

`python data/generate_data.py` regenerates all datasets deterministically (seed 2026). Change the seed to produce a fresh variant for a new cohort; the ground-truth files are rewritten accordingly. Re-run `python assignments/checks/make_example_submission.py` afterwards.

## Publishing a student mirror

```bash
git subtree split --prefix . -b student-mirror
# or simply: copy the repo and delete instructor/ before pushing to the student organisation
```

`.gitignore` already excludes rendered outputs and the virtual environment.
