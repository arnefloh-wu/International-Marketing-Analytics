# Slides

Course decks on the WU template, built with the `polish-slides` and `add-instructor-slide` skills (`.claude/skills/`).

| File | Content |
|---|---|
| `00a_course-content-and-style_WT26-27.pptx` / `.pdf` | Course outline: welcome, instructor profile, module content, course roadmap, learning outcomes, methods, roadmap table, assessment, certificates and set-up, coding exercises and written exam, contact |
| `build_course_outline.py` | Builds the outline deck on the skill's template with the design patterns in `polish-slides/references/design-patterns.md` (icon rows, grouped bands, two-card comparisons, steppers, stat rows, native chart, session card grid) |
| `finish_profile_slides.py` | Adapts the instructor profile slides to this deck: 16 pt titles, 15 pt card headings, the two Module Convenor cards merged into one with an online office-hours link (the skill asset is unchanged) |
| `icons/` | Lucide line icons as PNG in WU navy, blue and white; `render_icons.js` regenerates them |

Type sizes: 13 pt text, 15 pt table and card headings, 16 pt slide titles, 28 pt figures.

Rebuild and check:

```bash
python slides/build_course_outline.py .claude/skills/polish-slides/assets/template.pptx "old-slides/00a_Course Content & Style_WT25-26.pptx" /tmp/outline.pptx
python .claude/skills/add-instructor-slide/scripts/add_instructor_slides.py /tmp/outline.pptx -o slides/00a_course-content-and-style_WT26-27.pptx --after 2
python slides/finish_profile_slides.py slides/00a_course-content-and-style_WT26-27.pptx
python .claude/skills/polish-slides/scripts/check_deck.py slides/00a_course-content-and-style_WT26-27.pptx /tmp/qa
```

Session decks for the lectures are generated from Quarto (`sessions/0X-*/slides.qmd`, rendered to reveal.js and PowerPoint).
