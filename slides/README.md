# Slides

Course decks on the WU template, built and polished with the `polish-slides` skill (`.claude/skills/polish-slides`).

| File | Content |
|---|---|
| `00a_course-content-and-style_WT26-27.pptx` / `.pdf` | Course outline: content, learning outcomes, methods, roadmap, assessment, certificates, quizzes and check-ins, group project, peer rating |
| `build_course_outline.py` | Rebuilds the outline deck from the skill's template and the WT 25/26 deck in `old-slides/` (pictures are carried over) |

Rebuild and check:

```bash
python slides/build_course_outline.py .claude/skills/polish-slides/assets/template.pptx "old-slides/00a_Course Content & Style_WT25-26.pptx" slides/00a_course-content-and-style_WT26-27.pptx
python .claude/skills/polish-slides/scripts/check_deck.py slides/00a_course-content-and-style_WT26-27.pptx /tmp/qa
```

Session decks for the lectures are generated from Quarto (`sessions/0X-*/slides.qmd`, rendered to reveal.js and PowerPoint).
