# Session 5: Project pitches and wrap-up (Tue 3 November 2026)

The final session is the board meeting of Alpenglow. Six groups present their 2027 media budget recommendation to the board in ten minutes each and defend it for five minutes of questions. The rest of the cohort sits on the board: every student holds a role card (CFO, CEO, a country manager, the media agency, the data-protection officer, the sceptical statistician) and a question card, so every pitch gets challenged from the angles a real board uses. After the pitches the instructor reveals the data-generating process behind the Alpenglow data (true ROAS by country and channel, the true optimal allocation) and compares it with what the groups recommended. The session closes with what the course taught about analytics in international marketing, where this work is done professionally, and what to read next.

## Learning outcomes

After this session you can:

1. Present an analytical recommendation to a non-technical decision body in ten minutes: decision first, evidence second, uncertainty stated.
2. Challenge an analytics pitch as a board member: ask for the counterfactual, the interval, the assumption that would break the result.
3. Judge your own model against the truth: see where MMMs recover reality (ranking of channels, direction of reallocation) and where they do not (small markets, saturated channels).
4. Give structured peer feedback on analytical communication.

## Timing plan (4 hours, 13:00 to 17:00 as working assumption)

| Time | Block | Minutes |
|---|---|---|
| 13:00 | Welcome, rules of the board meeting, role and question cards handed out | 10 |
| 13:10 | Pitches 1 to 3 (10 min pitch + 5 min Q&A each; 2 min changeover) | 50 |
| 14:00 | Break | 10 |
| 14:10 | Pitches 4 to 6 | 50 |
| 15:00 | Board deliberation: each board role names the pitch that convinced them and why; peer feedback forms completed | 20 |
| 15:20 | Break | 10 |
| 15:30 | The reveal: how the data were made, true ROAS, true optimal allocation, where the groups landed | 40 |
| 16:10 | Lessons of the course: what MMM can and cannot do, experiments, attribution, AI-assisted analytics | 20 |
| 16:30 | Careers, tools, further reading, course evaluation | 20 |
| 16:50 | Close | 10 |

## Format of the board meeting

- **Running order** is drawn by lot at the end of Session 4 and posted on the Discussions board. Each group has 10 minutes, hard stop (a timer is visible), then 5 minutes of questions. Changeover 2 minutes: the next group's `pitch.pdf` is opened from the submitted repository, not from a laptop.
- **Every member speaks.** The board may direct a question to a named member.
- **Slides**: max 8, as submitted (`pitch.pdf`, tag `v1.0`). No live demos; the numbers on the slides are the numbers in the report.
- **The chair** (instructor) keeps time, calls board members in turn and closes each Q&A.

## Board roles and question cards

Each student who is not presenting draws one role card for the whole session and receives a stack of question cards. In each Q&A the chair calls at least three different roles. Suggested roles and the question each is expected to ask at least once during the session:

| Role | Typical question |
|---|---|
| CFO | "What is the expected gain in euro per year, with what interval, and what happens if the lower bound materialises?" |
| CEO | "Which single change do you need the board to approve today, and what is the risk?" |
| Country manager Poland (or Netherlands) | "You cut my TV to zero. What do I tell my retailers?" |
| Country manager Germany | "Your geo-lift says paid social returns 14 cents per euro at 2.5x spend. Why keep it at all?" |
| Media agency | "Your model says OOH works in France and not in Austria. Is that the data or the market?" |
| Sceptical statistician | "How many weeks of data per country? How wide are your intervals for Austria? What did the hierarchical model change?" |
| Data-protection officer | "What in your recommendation depends on user-level tracking that may not exist in 2027?" |
| Analytics lead of a competitor | "What experiment would you run in 2027 to prove your model right or wrong?" |

Question cards (printed, one question each) are in `peer_feedback_form.md` and may be used verbatim. Board members write their peer feedback on the form during the deliberation block.

## Materials in this folder

| File | Purpose |
|---|---|
| `slides.qmd` | Instructor deck: welcome, rules, scoring, the reveal (reads `instructor/ground_truth/`), wrap-up. **Render and show only after the pitches; the reveal slides contain the ground truth.** |
| `peer_feedback_form.md` | Peer feedback form for each pitch and the printable question cards |
| `group_allocations/` (instructor creates) | Copies of the six `allocation_2027.csv` files, named `group-XX.csv`, for the "where the groups landed" slide |

## Before the session (instructor checklist)

1. Pull all six repositories at tag `v1.0`; run `PROJECT_CSV=... pytest assignments/checks/test_project.py` for each.
2. Copy each `allocation_2027.csv` to `sessions/05-project-pitches/group_allocations/group-XX.csv`.
3. Render `slides.qmd` (`quarto render sessions/05-project-pitches/slides.qmd --to revealjs,pptx`).
4. Print role cards, question cards and peer feedback forms (one form per student per pitch).
5. Open the course evaluation survey.
