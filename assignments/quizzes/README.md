# Quiz banks

Each session folder holds a `quiz.md` with **10 closed-book multiple-choice questions** (four options, one correct, one-line rationale). The quizzes open online after Sessions 1 to 4 and are auto-graded; each quiz counts 5 % of the grade (20 % in total).

## Source format (`sessions/0X-*/quiz.md`)

```markdown
# Quiz 2: Marketing mix modelling I

1. What does geometric adstock model?
   a) Diminishing returns to spend within a week
   b) Carryover of advertising effects into later weeks
   c) Seasonality of demand
   d) Competitor reactions
   Answer: b
   Rationale: Adstock spreads the effect of one week's spend over the following weeks with geometric decay.

2. ...
```

Rules the converter relies on:

- questions start with a number and a dot (`1.`), optionally bold or as a heading (`**1.**`, `### 1.`); the question text may run over several lines until the first option;
- options are the lines starting with `a)`, `b)`, `c)`, `d)` (also `a.`, `(a)`, `A)` or a list dash in front);
- a line `Answer: b` (letter only, or letter followed by the option text) marks the correct option;
- a line `Rationale: ...` gives the one-line feedback shown after the attempt;
- anything before the first question (title, instructions) is ignored.

## Converting to GIFT (Moodle, Canvas via plugin)

```bash
python assignments/quizzes/convert_quiz.py                      # all sessions/0X-*/quiz.md -> assignments/quizzes/session0X.gift
python assignments/quizzes/convert_quiz.py --input assignments/quizzes/sample_quiz.md --output assignments/quizzes/sample_quiz.gift
python assignments/quizzes/convert_quiz.py --check              # parse only, report problems, write nothing
```

Each question becomes a GIFT item named `S0X Q01`, with the rationale as general feedback and options shuffled by the platform. The converter aborts with a clear message if a question has fewer than four options, no answer line or an answer letter that does not match an option. Special GIFT characters (`~ = # { } :`) are escaped.

Import in Moodle: *Question bank -> Import -> GIFT format*, choose the `.gift` file, then build the quiz from the category. In Canvas, use the GIFT importer plugin or convert with Respondus.

`sample_quiz.md` is a three-question sample used to test the converter.
