# Slides

Course decks on the WU template, built with the `polish-slides` and `add-instructor-slide` skills (`.claude/skills/`).

| File | Content |
|---|---|
| `00a_course-content-and-style_WT26-27.pptx` / `.pdf` | Course outline: welcome, instructor profile, module content, course roadmap, learning outcomes, methods, roadmap table, assessment strategy, software and set-up, online certificates, coding exercises, written exam, case study report, contact (16 slides) |
| `01a_setup-and-registration_WT26-27.pptx` / `.pdf` | Session 1 set-up deck (31 slides): plan for the day; Part 1 registrations (GitHub, GitHub Education and Copilot, DataCamp, Canvas survey); Part 2 installation (how the tools fit together, uv, Positron, Quarto, GitHub Desktop, cloning, the `.venv`, the check script, the AI assistant); Part 3 how Positron works (panes, running code, Quarto, shortcuts, AI); Part 4 packages (polars, plotnine, Great Tables, statsmodels with code that runs on the course data); troubleshooting, checklist |
| `build_course_outline.py` | Builds the outline deck on the skill's template with the design patterns in `polish-slides/references/design-patterns.md` (icon rows, grouped bands, two-card comparisons, steppers, stat rows, native chart, session card grid) |
| `finish_profile_slides.py` | Adapts the instructor profile slides to this deck: 16 pt titles, 15 pt card headings, the two Module Convenor cards merged into one with an online office-hours link (the skill asset is unchanged) |
| `build_setup_deck.py` | Builds the set-up deck |
| `make_setup_figures.py` | Runs the package code shown on the set-up slides and saves the chart, table and numbers to `figures/` |
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
python slides/build_setup_deck.py .claude/skills/polish-slides/assets/template.pptx slides/01a_setup-and-registration_WT26-27.pptx
python .claude/skills/polish-slides/scripts/check_deck.py slides/01a_setup-and-registration_WT26-27.pptx /tmp/qa-setup
```

Run these from the repository root with the course `.venv` active.

Session decks for the lectures are generated from Quarto (`sessions/0X-*/slides.qmd`, rendered to reveal.js and PowerPoint).
