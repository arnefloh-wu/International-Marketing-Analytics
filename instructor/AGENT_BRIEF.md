# Shared brief for material authors

Repository: /home/user/International-Marketing-Analytics (branch claude/epic-babbage-5ihdj0). Do NOT run git commit or git push; the integrator commits.

Read first: instructor/course_design.md (sections 1, 2, 7, 8), data/README.md, assets/mma.py, syllabus/syllabus.qmd.

Environment: `source .venv/bin/activate` (all packages installed: pandas 3, numpy 2, statsmodels 0.15, scikit-learn, linearmodels 7, pymc-marketing 0.19.2, arviz, causalpy 0.9, matplotlib, seaborn, plotly, pytest). Quarto 1.7 is installed. Render checks:
  quarto render sessions/0X-.../slides.qmd --to revealjs,pptx
  quarto render sessions/0X-.../lab.qmd
Every .qmd must render without error. Labs must run end to end in under 5 minutes on a laptop (PyMC: draws=500, tune=500, chains=2, random_seed=42, progressbar=False).

Paths: labs live in sessions/0X-name/ and are rendered with that folder as the working directory, so load data with relative paths like "../../data/mmm/alpenglow_weekly.csv" and import helpers with
    import sys; sys.path.append("../../assets"); from mma import *
Slides use: format: revealjs: theme: [default, ../../assets/wu.scss], slide-number: true, footer: "International Marketing Analytics · WU Vienna", width 1280 height 720, plus a pptx format. Python chunks in slides must set echo: false unless the code itself is the teaching point. Keep each chart small (fig-width 8, fig-height 4).

Files per session folder: slides.qmd, lab.qmd, exercises.qmd, quiz.md (10 multiple-choice questions with 4 options, correct answer marked, one-line rationale, closed-book conceptual), and README.md (1-paragraph session overview + learning outcomes + timing plan for 4 hours). Instructor solutions for exercises go to instructor/solutions/session0X_solutions.qmd (must render too).

Pedagogy: students are CEMS master students with no programming background who use AI assistants (Positron Assistant / Copilot / Claude Code). Every lab section has: the decision, the code (fully written, runnable), an interpretation paragraph with the actual numbers, a "Check yourself" list, and a "Prompt pattern" box showing a good prompt to ask an AI assistant plus "what to verify". Explain every regression output the first time it appears. Decision-first framing: start each session from the manager's question.

Style: British English, "modelling". No em dashes. Slide decks: 25-40 slides, max 6 bullets, speaker notes under ::: {.notes} on every content slide. Use .decision div for the decision-of-the-day slide. Charts: matplotlib, clean, labelled axes, colour-blind friendly (tab10 is fine), one chart per slide.

Ground truth: instructor/ground_truth/ exists. Instructor solutions may compare to it; student-facing files must never read from instructor/.
