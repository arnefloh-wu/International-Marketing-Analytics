"""Build the WT 26/27 course outline deck on the WU template (polish-slides skill).

Design follows .claude/skills/polish-slides/references/design-patterns.md:
icon rows, grouped bands, two-card comparisons, steppers, stat rows, a native
bar chart and a session card grid, all in theme colours. Type sizes: 13 pt text,
15 pt card and table headings, 16 pt slide titles, 28 pt figures.
Helpers live in wu_deck.py. The instructor profile slides are added afterwards with the add-instructor-slide
skill (see slides/README.md).

usage: python slides/build_course_outline.py TEMPLATE.pptx OLD_DECK.pptx OUT.pptx
"""
import copy
import sys

from lxml import etree
from pptx import Presentation
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Pt

from wu_deck import (A, ACC, BODY, FIG, GAP, HEAD, LIGHT, NAVY, NB, TITLE, WHITE, Deck, I, box, card, color,
                     copy_pictures, icon, ph, set_runs, stepper, text)

TEMPLATE, OLD, OUT = sys.argv[1:4]
FOOTER = "International Marketing Analytics" + NB + "·" + NB + "WT" + NB + "2026/27"

deck = Deck(TEMPLATE, FOOTER)
prs, L, add_slide = deck.prs, deck.L, deck.add_slide
old_slides = list(Presentation(OLD).slides)


def old_shape(slide_no, name):
    return next(sh for sh in old_slides[slide_no - 1].shapes if sh.name == name)


# ================================================================ slides ======
# 1  Title. Empty line after the institute in this deck's copy of the contact block (layout only, template untouched)
kontakt = next(sh for sh in L["Titelfolie Kontakt"].shapes if sh.name == "Kontaktdaten")
for para in kontakt.text_frame.paragraphs:
    if "Institute for International Business" in para.text:
        blank = copy.deepcopy(para._p)
        for r in blank.findall(f"{{{A}}}r"):
            blank.remove(r)
        end = etree.SubElement(blank, f"{{{A}}}endParaRPr"); end.set("lang", "en-GB"); end.set("sz", "1200")
        para._p.addnext(blank)
        break
s = add_slide("Titelfolie Kontakt", footer=None,
              notes="Welcome. This deck explains what the course is about, how it is taught and how it is assessed.")
set_runs(ph(s, 0).text_frame.paragraphs[0], "International Marketing Analytics")
set_runs(ph(s, 1).text_frame.paragraphs[0], "Course content and style")
set_runs(ph(s, 12).text_frame.paragraphs[0], "Winter term 2026/27")

# 2  Welcome picture (the instructor profile slides follow here, added by the skill)
s = add_slide("Titel und Inhalt", "The journey begins",
              notes="Ice-breaker: who is in the room, which countries, which prior exposure to analytics.")
copy_pictures(old_shape(2, "Grafik 5"), s)

# 3  Module content: icon rows
s = add_slide("Titel und Inhalt", "Module content",
              notes="Marketing mix modelling in one breath: take the sales history, separate what would have sold anyway "
                    "from what each marketing activity added, and use that to decide where the next euro goes.")
rows = [
    ("LuChartLine", ("Marketing analytics ", "is the measurement, management and analysis of marketing performance data "
                                              "to improve marketing effectiveness and return on investment. It turns data "
                                              "into decisions and shows where the next euro should go.")),
    ("LuTarget", ("Key questions: ", "how do price, place, product features and promotion drive performance measures such "
                                     "as sales, and how should a fixed budget be split across countries and channels?")),
    ("LuLaptop", ("Tools: ", "Python in Positron, GitHub for versioning and DataCamp courses; AI assistants do most of the "
                             "typing, you check the results.")),
    ("LuBriefcase", ("Case studies: ", "Zalando and NEOH, plus a six-country teaching dataset with known answers for the labs.")),
]
rh = (4.25 - GAP * 3) / 4
for i, (ic, para) in enumerate(rows):
    y = 1.35 + i * (rh + GAP)
    box(s, 0.5, y, 9.0, rh, LIGHT, f"Content row {i + 1}")
    icon(s, ic, "navy", 0.72, y + (rh - 0.45) / 2, 0.45, f"content row {i + 1}")
    text(s, 1.45, y, 7.85, rh, [para], f"Content text {i + 1}", anchor=MSO_ANCHOR.MIDDLE)

# 4  Course roadmap: five stops on a road, one card per session
s = add_slide("Titel und Inhalt", "Course roadmap: five sessions",
              notes="Session 1 combines the introduction with linear regression. Each session adds one method; "
                    "the last brings them together in dedicated MMM software.")
stops = [
    ("Introduction and linear regression", "MMM basics, OLS, model fit and interpretation"),
    ("Advanced regression", "Log-log, dummies, interactions, adstock, saturation"),
    ("Logistic regression", "Binary outcomes such as purchase or churn, odds ratios"),
    ("ARIMA", "Trend, seasonality, forecasting the sales baseline"),
    ("Advanced MMM tools", "Bayesian MMM, budget optimisation across channels"),
]
cg = 0.1
cw = (9.0 - cg * 4) / 5
road_y = 1.72
box(s, 0.5, road_y - 0.06, 8.75, 0.12, ACC, "Road")
end = box(s, 9.2, road_y - 0.17, 0.3, 0.34, ACC, "Road end", shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
end.rotation = 90
for i, (theme, desc) in enumerate(stops):
    x = 0.5 + i * (cw + cg)
    cx = x + cw / 2
    box(s, cx - 0.015, road_y, 0.03, 0.55, ACC, f"Stop connector {i + 1}")
    dot = box(s, cx - 0.3, road_y - 0.3, 0.6, 0.6, NAVY, f"Stop {i + 1}", shape=MSO_SHAPE.OVAL)
    tf = dot.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = str(i + 1); r.font.size = Pt(TITLE); r.font.bold = True; r.font.name = "+mj-lt"
    color(r.font.color, WHITE)
    box(s, x, 2.27, cw, 2.5, LIGHT, f"Session card {i + 1}")
    text(s, x + 0.07, 2.4, cw - 0.12, 0.95, [theme], f"Session theme {i + 1}", size=HEAD, col=NAVY, bold=True,
         head=True, space=0)
    box(s, x + 0.07, 3.42, 0.5, 0.04, ACC, f"Session rule {i + 1}")
    text(s, x + 0.07, 3.58, cw - 0.12, 1.1, [desc], f"Session text {i + 1}")
box(s, 0.5, 4.95, 5.75, 0.6, LIGHT, "Along the way")
icon(s, "LuFlag", "navy", 0.68, 5.06, 0.38, "along the way")
text(s, 1.2, 4.95, 4.95, 0.6, [("Along the way: ", "DataCamp certificates, coding exercises, guest speaker")],
     "Along the way text", anchor=MSO_ANCHOR.MIDDLE)
box(s, 6.4, 4.95, 3.1, 0.6, NAVY, "Exam box")
icon(s, "LuPencilLine", "white", 6.55, 5.06, 0.38, "exam")
text(s, 7.05, 4.95, 2.4, 0.6, [[("At the end: ", {"bold": True, "col": WHITE}), ("written exam", {"col": WHITE})]],
     "Exam text", anchor=MSO_ANCHOR.MIDDLE)


# 5  Learning outcomes: grouped bands with numbered badges, one line per outcome
def bands(slide, groups, top, height, prefix):
    for g, (ic, heading, items) in enumerate(groups):
        y = top + g * (height + GAP)
        box(slide, 0.5, y, 9.0, height, LIGHT, f"{prefix} band {g + 1}")
        box(slide, 0.5, y, 0.07, height, ACC, f"{prefix} bar {g + 1}")
        icon(slide, ic, "navy", 0.75, y + (height - 0.42) / 2, 0.42, f"{prefix} {g + 1}")
        text(slide, 1.3, y, 1.45, height, [heading], f"{prefix} heading {g + 1}", size=HEAD, col=NAVY,
             bold=True, head=True, anchor=MSO_ANCHOR.MIDDLE, space=0)
        row_h = height / len(items)
        for k, (num, lead, rest) in enumerate(items):
            ry = y + k * row_h
            badge = box(slide, 2.85, ry + (row_h - 0.34) / 2, 0.34, 0.34, NAVY, f"{prefix} number {num}",
                        shape=MSO_SHAPE.OVAL)
            tf = badge.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
            r = p.add_run(); r.text = num; r.font.size = Pt(BODY); r.font.bold = True; color(r.font.color, WHITE)
            text(slide, 3.35, ry, 6.0, row_h, [[(lead, {"bold": True, "col": NAVY}), (rest, {})]],
                 f"{prefix} outcome {num}", anchor=MSO_ANCHOR.MIDDLE, space=0)


s = add_slide("Titel und Inhalt", "Learning outcomes",
              notes="Two outcomes each for understanding, applying and transferring. Cross-sectional means many units "
                    "at one point in time (countries, stores); longitudinal means the same units over time (weekly sales).")
text(s, 0.5, 1.3, 9.0, 0.3, ["On successful completion of this module, students will be able to:"], "Outcomes intro")
bands(s, [
    ("LuLightbulb", "Understand", [
        ("1", "Explain the fundamentals of MMM, ", "its strengths and limits"),
        ("2", "Describe real-world applications ", "of MMM in marketing")]),
    ("LuCode", "Apply", [
        ("3", "Apply MMM in Python ", "to cross-sectional and longitudinal data"),
        ("4", "Interpret results ", "and turn them into marketing decisions")]),
    ("LuUsers", "Transfer", [
        ("5", "Use AI tools ", "for analysis and reporting, and check the output"),
        ("6", "Think critically ", "and work effectively in teams")]),
], 1.72, 1.18, "Outcomes")

# 6  Methods of teaching and learning: stepper, two cards, the exam
s = add_slide("Titel und Inhalt", "Methods of teaching and learning",
              notes="Each session ends with a short online quiz that is not graded; it shows you what to revise. "
                    "The written exam at the end is paper and pencil with multiple-choice questions.")
text(s, 0.5, 1.28, 9.0, 0.3, [[("Every session", {"bold": True, "col": NAVY})]], "Session rhythm label")
stepper(s, 0.5, 1.62, 9.0, 0.72, ["Concept lecture\v60" + NB + "min", "Guided lab\v90" + NB + "min",
                                  "Team exercise\v60" + NB + "min", "Online quiz\vnot graded"], "Session rhythm")
cw2 = (9.0 - 0.5) / 2
card(s, 0.5, 2.55, cw2, 2.3, "Between sessions", [
    "Read chapters and materials",
    "DataCamp courses and certificates",
    "Coding exercises",
    "Case study report in your group",
    "Q&A forum on Canvas"], "LuHouse", "Between sessions card")
box(s, 0.5 + cw2 + 0.09, 3.5, 0.32, 0.4, ACC, "Card arrow", shape=MSO_SHAPE.CHEVRON)
card(s, 0.5 + cw2 + 0.5, 2.55, cw2, 2.3, "In the classroom", [
    "Five in-person sessions",
    "Laptop with Python, Positron, GitHub",
    "AI-assisted coding, checked by you",
    "Guest speaker from industry"], "LuSchool", "In the classroom card")
box(s, 0.5, 5.0, 9.0, 0.55, NAVY, "Exam box")
icon(s, "LuPencilLine", "white", 0.7, 5.08, 0.38, "exam")
text(s, 1.25, 5.0, 8.1, 0.55, [[("At the end: ", {"bold": True, "col": WHITE}),
                                ("written exam, 60" + NB + "minutes, paper and pencil, multiple-choice questions.", {"col": WHITE})]],
     "Exam text", anchor=MSO_ANCHOR.MIDDLE)

# 7  Module roadmap: table
s = add_slide("Titel und Tabelle", "Module roadmap",
              notes="Topics follow the course roadmap; methods in detail.")
rows = [
    ("Session", "Topic", "Methods"),
    ("1", "Introduction and linear regression", "Course content and style; registration and set-up (Python, Positron, GitHub, DataCamp); MMM fundamentals; OLS, model fit and interpretation"),
    ("2", "Advanced regression", "Log-log elasticities, dummy variables, non-linear effects, moderation and mediation, adstock and saturation, diagnostics"),
    ("3", "Logistic regression", "Binary outcomes such as purchase or churn, odds ratios, model fit and classification"),
    ("4", "ARIMA", "Trend, seasonality and autocorrelation; ARIMA and ARIMAX forecasts as the sales baseline"),
    ("5", "Advanced MMM tools", "Bayesian MMM with PyMC-Marketing and Google Meridian; budget optimisation across channels and countries"),
]
gf = ph(s, 1).insert_table(len(rows), len(rows[0]))
tbl = gf.table
widths = [1.2, 2.6, 5.2]
for i, w in enumerate(widths):
    tbl.columns[i].width = I(w)
gf.width = I(sum(widths))
for r_i, row in enumerate(rows):
    for c_i, txt in enumerate(row):
        cell = tbl.cell(r_i, c_i)
        p = cell.text_frame.paragraphs[0]
        set_runs(p, txt)
        for r in p.runs:
            r.font.size = Pt(HEAD if r_i == 0 else BODY)
            if c_i == 1 and r_i > 0:
                r.font.bold = True
        if c_i == 0 and r_i > 0:
            p.alignment = PP_ALIGN.CENTER
        cell.margin_top = cell.margin_bottom = Emu(54000)

# 8  Assessment strategy: composition bar, one card per component, grading scale
s = add_slide("Titel und Inhalt", "Assessment strategy",
              notes="Three individual components (70 %) and one group component (30 %). The bar shows the shares at a "
                    "glance; the cards say what each part is.")
comps = [
    ("Online certificates", "DataCamp, 4" + NB + "×" + NB + "5" + NB + "%", 20, "Individual", "LuGraduationCap", MSO_THEME_COLOR.ACCENT_4, WHITE),
    ("Coding exercises", "4" + NB + "×" + NB + "5" + NB + "%", 20, "Individual", "LuCode", ACC, WHITE),
    ("Written exam", "60" + NB + "minutes, multiple choice", 30, "Individual", "LuPencilLine", NAVY, WHITE),
    ("Case study report", "written report, groups of max." + NB + "4", 30, "Group", "LuBriefcase", MSO_THEME_COLOR.ACCENT_6, NAVY),
]
x = 0.5
for i, (name, detail, w, who, ic, fillc, txtc) in enumerate(comps):
    seg_w = 9.0 * w / 100
    box(s, x, 1.35, seg_w - 0.04, 0.5, fillc, f"Share {i + 1}")
    text(s, x, 1.35, seg_w - 0.04, 0.5, [[(f"{w}" + NB + "%", {"bold": True, "col": txtc})]], f"Share label {i + 1}",
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    x += seg_w
cw4 = (9.0 - GAP * 3) / 4
for i, (name, detail, w, who, ic, fillc, txtc) in enumerate(comps):
    x = 0.5 + i * (cw4 + GAP)
    box(s, x, 2.05, cw4, 1.85, LIGHT, f"Component card {i + 1}")
    box(s, x, 2.05, cw4, 0.08, fillc, f"Component strip {i + 1}")
    icon(s, ic, "navy", x + 0.15, 2.25, 0.4, f"component {i + 1}")
    text(s, x + cw4 - 1.25, 2.25, 1.1, 0.4, [[(f"{w}" + NB + "%", {"size": FIG, "bold": True, "col": NAVY, "head": True})]],
         f"Component weight {i + 1}", align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 0.15, 2.8, cw4 - 0.3, 1.05, [[(name, {"bold": True, "col": NAVY})], detail,
                                              [(who, {"bold": True, "col": ACC})]], f"Component text {i + 1}", space=3)
text(s, 0.5, 4.05, 9.0, 0.3, [[("Grading scale (WU)", {"bold": True, "col": NAVY})]], "Scale label")
scale = [("1", "Excellent", "90" + NB + "% and above"), ("2", "Good", "80 to 89" + NB + "%"),
         ("3", "Satisfactory", "70 to 79" + NB + "%"), ("4", "Sufficient", "60 to 69" + NB + "%"),
         ("5", "Fail", "below 60" + NB + "%")]
sw5 = (9.0 - 0.1 * 4) / 5
for i, (g, word, rng) in enumerate(scale):
    x = 0.5 + i * (sw5 + 0.1)
    box(s, x, 4.4, sw5, 0.6, NAVY if i < 4 else LIGHT, f"Grade {g}")
    col = WHITE if i < 4 else NAVY
    text(s, x + 0.1, 4.4, sw5 - 0.2, 0.6, [[(g + "  ", {"size": HEAD, "bold": True, "col": col, "head": True}),
                                            (word, {"bold": True, "col": col})], [(rng, {"col": col})]],
         f"Grade text {g}", anchor=MSO_ANCHOR.MIDDLE, space=0)
text(s, 0.5, 5.12, 9.0, 0.4, [[("Attendance: ", {"bold": True, "col": NAVY}), ("at least 80" + NB + "% of sessions.   ", {}),
                               ("AI tools: ", {"bold": True, "col": NAVY}), ("expected; you own every number you report.", {})]],
     "Rules line", anchor=MSO_ANCHOR.MIDDLE)

# 9  Software and set-up: tool cards plus installation stepper
s = add_slide("Titel und Inhalt", "Software and set-up",
              notes="Everything is free for students. No preparation before the course: we register the accounts and install "
                    "the software together in Session 1. The check is the command in the guide that prints 'ready'.")
tools = [("LuCode", "Python", "the language for all analyses"),
         ("LuLaptop", "Positron", "the editor where you write, run and see results"),
         ("LuFileText", "Quarto", "turns code and text into reports and slides"),
         ("LuGitBranch", "GitHub", "versions and shares your work"),
         ("LuBot", "AI assistant", "GitHub Copilot, free with the student plan")]
tw5 = (9.0 - 0.12 * 4) / 5
for i, (ic, name, role) in enumerate(tools):
    x = 0.5 + i * (tw5 + 0.12)
    box(s, x, 1.35, tw5, 1.9, LIGHT, f"Tool card {i + 1}")
    icon(s, ic, "navy", x + 0.15, 1.5, 0.45, f"tool {i + 1}")
    text(s, x + 0.15, 2.05, tw5 - 0.25, 1.15, [[(name, {"bold": True, "col": NAVY})], role], f"Tool text {i + 1}", space=3)
text(s, 0.5, 3.4, 9.0, 0.3, [[("Set-up in Session 1: four steps", {"bold": True, "col": NAVY})]], "Set-up label")
stepper(s, 0.5, 3.75, 9.0, 0.75, ["Register\vaccounts", "Install\vthe software", "Clone\vthe repo", "Run the\vcheck"],
        "Set-up steps", current=3)
box(s, 0.5, 4.75, 9.0, 0.8, LIGHT, "Set-up callout")
icon(s, "LuSchool", "navy", 0.7, 4.91, 0.48, "set-up in class")
text(s, 1.4, 4.75, 7.9, 0.8, [("Together in Session 1. ", "Registration (GitHub, Copilot, DataCamp) and installation are done in class. "
                                "Just bring your laptop and charger; no preparation needed.")],
     "Set-up text", anchor=MSO_ANCHOR.MIDDLE)

# 10  Online certificates: stat rows plus a callout
s = add_slide("Titel und Inhalt", "Online certificates",
              notes="The DataCamp courses are assigned on Canvas. Each certificate counts 5 % once it is uploaded on time.")
stats = [
    ("4", ("DataCamp courses. ", "Python courses assigned on Canvas, each ending with a certificate.")),
    ("5" + NB + "%", ("Per certificate. ", "Upload each certificate on Canvas by its deadline.")),
    ("20" + NB + "%", ("In total. ", "Together the four certificates count one fifth of the final grade.")),
]
for i, (fig, para) in enumerate(stats):
    y = 1.4 + i * (0.85 + GAP)
    box(s, 0.5, y, 0.07, 0.85, ACC, f"Stat bar {i + 1}")
    text(s, 0.75, y, 1.75, 0.85, [[(fig, {"size": FIG, "bold": True, "col": NAVY, "head": True})]], f"Stat figure {i + 1}",
         anchor=MSO_ANCHOR.MIDDLE)
    text(s, 2.6, y, 6.9, 0.85, [para], f"Stat text {i + 1}", anchor=MSO_ANCHOR.MIDDLE)
box(s, 0.5, 4.5, 9.0, 1.05, LIGHT, "Deadline callout")
icon(s, "LuGraduationCap", "navy", 0.75, 4.75, 0.55, "certificates")
text(s, 1.55, 4.5, 7.75, 1.05, [("Deadlines: ", "the date for each certificate is on Canvas. The courses build the Python "
                                                "basics you need for the labs, so start early.")],
     "Deadline text", anchor=MSO_ANCHOR.MIDDLE)


# 11  Coding exercises: figures, how it works, rules
def fact_tiles(slide, facts, y, prefix):
    tw = (9.0 - GAP * (len(facts) - 1)) / len(facts)
    for i, (fig, label) in enumerate(facts):
        x = 0.5 + i * (tw + GAP)
        box(slide, x, y, tw, 1.0, LIGHT, f"{prefix} tile {i + 1}")
        box(slide, x, y, 0.07, 1.0, ACC, f"{prefix} bar {i + 1}")
        text(slide, x + 0.25, y, tw - 0.35, 1.0, [[(fig, {"size": FIG, "bold": True, "col": NAVY, "head": True})], label],
             f"{prefix} text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)


s = add_slide("Titel und Inhalt", "Coding exercises",
              notes="Each exercise takes the code from the guided lab and applies it to a similar task. AI assistants are "
                    "allowed; the prompt log shows how you used them.")
fact_tiles(s, [("4", "exercises during the course"), ("5" + NB + "%", "per exercise"), ("20" + NB + "%", "of the final grade")],
           1.35, "Coding")
text(s, 0.5, 2.55, 9.0, 0.3, [[("How it works", {"bold": True, "col": NAVY})]], "Coding label")
stepper(s, 0.5, 2.9, 9.0, 0.75, ["Guided lab\vin class", "Apply the code\vto a similar task", "Submit on\vCanvas",
                                 "Feedback\vand grade"], "Coding steps")
card(s, 0.5, 3.85, 9.0, 1.7, "Rules", [
    "Submit your Python or Quarto file; it must run from top to bottom",
    "AI assistants are allowed; add a short prompt log at the end",
    "Individual work: discuss ideas, but write and check your own code"], "LuShieldCheck", "Coding rules card", head_h=0.45)

# 12  Written exam: figures and three cards
s = add_slide("Titel und Inhalt", "Written exam",
              notes="The exam checks understanding, not coding. The non-graded online quiz at the end of each session "
                    "uses the same question format.")
fact_tiles(s, [("30" + NB + "%", "of the final grade"), ("60", "minutes exam time"),
               ("1", "exam at the end of the course"), ("MC", "multiple-choice questions")], 1.35, "Exam")
cw3 = (9.0 - GAP * 2) / 3
card(s, 0.5, 2.55, cw3, 3.0, "Format", [
    "Paper and pencil, 60" + NB + "minutes", "Multiple-choice questions", "Individual, closed book"], "LuPencilLine", "Exam format card")
card(s, 0.5 + cw3 + GAP, 2.55, cw3, 3.0, "Content", [
    "All five sessions", "Concepts and interpretation", "Reading model output, not coding"], "LuBookOpen", "Exam content card")
card(s, 0.5 + 2 * (cw3 + GAP), 2.55, cw3, 3.0, "Preparation", [
    "Online quiz after every session (not graded)", "Session materials and book chapters",
    "Q&A forum on Canvas"], "LuListChecks", "Exam preparation card")

# 13  Case study: written report (group)
s = add_slide("Titel und Inhalt", "Case study: written report",
              notes="The case and its data are published on Canvas. Online consulting hours need registration. "
                    "The report is the only group component of the grade.")
fact_tiles(s, [("1", "written report per group"), ("max." + NB + "4", "students per group"),
               ("30" + NB + "%", "of the final grade"), ("2" + NB + "weeks", "after the last session: deadline")],
           1.35, "Case")
tw = (9.0 - GAP * 2) / 3
text(s, 0.5, 2.55, 9.0, 0.3, [[("What you submit", {"bold": True, "col": NAVY})]], "Submit label")
subs = [("LuCode", "Quarto file", "your analysis and text in one reproducible document"),
        ("LuFileText", "Rendered report", "the output of the Quarto file; HTML recommended"),
        ("LuFileSpreadsheet", "Data file", "the data you analysed, so the report can be rerun")]
for i, (ic, head, body) in enumerate(subs):
    x = 0.5 + i * (tw + GAP)
    box(s, x, 2.9, tw, 1.35, LIGHT, f"Submission card {i + 1}")
    icon(s, ic, "navy", x + 0.18, 3.05, 0.4, f"submission {i + 1}")
    text(s, x + 0.75, 3.05, tw - 0.9, 1.1, [[(head, {"bold": True, "col": NAVY})], body], f"Submission text {i + 1}", space=4)
box(s, 0.5, 4.45, 9.0, 1.1, NAVY, "Task box")
text(s, 0.75, 4.45, 8.5, 1.1,
     [[("The task: ", {"bold": True, "col": WHITE}),
       ("apply marketing mix modelling to a real marketing case, interpret the results and recommend a decision "
        "to management.", {"col": WHITE})],
      [("Support: ", {"bold": True, "col": WHITE}),
       ("online consulting hours (registration needed).", {"col": WHITE})]],
     "Task text", anchor=MSO_ANCHOR.MIDDLE, space=6)

# 14  Closing contact card
add_slide("Abschlussfolie Kontakt", notes="Any questions? Contact details on the card.")

deck.save(OUT)
