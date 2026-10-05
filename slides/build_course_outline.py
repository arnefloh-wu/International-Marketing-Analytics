"""Build the WT 26/27 course outline deck on the WU template (polish-slides skill).

Design follows .claude/skills/polish-slides/references/design-patterns.md:
icon rows, grouped bands, two-card comparisons, steppers, stat rows, a native
bar chart and a session card grid, all in theme colours. Type sizes: 13 pt text,
15 pt card and table headings, 16 pt slide titles, 28 pt figures.
The instructor profile slides are added afterwards with the add-instructor-slide
skill (see slides/README.md).

usage: python slides/build_course_outline.py TEMPLATE.pptx OLD_DECK.pptx OUT.pptx
"""
import copy
import io
import sys
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.shapes import MSO_SHAPE, PP_PLACEHOLDER
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Emu, Pt

TEMPLATE, OLD, OUT = sys.argv[1:4]
ICONS = Path(__file__).resolve().parent / "icons"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NB = " "
BODY, HEAD, TITLE, FIG = 13, 15, 16, 28
FOOTER = "International Marketing Analytics" + NB + "·" + NB + "WT" + NB + "2026/27"
ACC, NAVY, LIGHT, INK, WHITE, BARS = (MSO_THEME_COLOR.ACCENT_1, MSO_THEME_COLOR.TEXT_2, MSO_THEME_COLOR.BACKGROUND_2,
                                      MSO_THEME_COLOR.TEXT_1, MSO_THEME_COLOR.BACKGROUND_1, MSO_THEME_COLOR.ACCENT_4)
GAP = 0.15


def I(x):
    return Emu(int(round(x * 914400)))


prs = Presentation(TEMPLATE)
old = Presentation(OLD)
old_slides = list(old.slides)
for sldId in list(prs.slides._sldIdLst):          # drop the template's sample slides
    prs.part.drop_rel(sldId.rId)
    prs.slides._sldIdLst.remove(sldId)
L = {l.name: l for l in prs.slide_layouts}


# ---------------------------------------------------------------- helpers ----
def set_runs(p, text):
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    if isinstance(text, tuple):
        lead, rest = text
        r1 = p.add_run(); r1.text = lead; r1.font.bold = True
        r2 = p.add_run(); r2.text = rest
    else:
        p.add_run().text = text


def ph(slide, idx):
    for sh in slide.placeholders:
        if sh.placeholder_format.idx == idx:
            return sh
    raise KeyError(idx)


def remove_shape(sh):
    sh._element.getparent().remove(sh._element)


def add_slide(layout_name, title=None, footer=FOOTER, notes=None, keep_body=False):
    s = prs.slides.add_slide(L[layout_name])
    for lph in L[layout_name].placeholders:       # python-pptx does not copy footer and slide number
        if lph.placeholder_format.type in (PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.SLIDE_NUMBER):
            s.shapes._spTree.append(copy.deepcopy(lph._element))
    for sh in list(s.placeholders):
        t = sh.placeholder_format.type
        if t == PP_PLACEHOLDER.FOOTER and footer is not None:
            set_runs(sh.text_frame.paragraphs[0], footer)
        elif t in (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE) and title is not None:
            set_runs(sh.text_frame.paragraphs[0], title)
            for r in sh.text_frame.paragraphs[0].runs:
                r.font.size = Pt(TITLE)
        elif t == PP_PLACEHOLDER.OBJECT and not keep_body and layout_name == "Titel und Inhalt":
            remove_shape(sh)                      # designed slides draw their own content
    if notes:
        s.notes_slide.notes_text_frame.text = notes
    return s


def color(fmt, c):
    if isinstance(c, str):
        fmt.rgb = RGBColor.from_string(c)
    else:
        fmt.theme_color = c


def box(slide, x, y, w, h, fill, name, shape=MSO_SHAPE.RECTANGLE, line=None):
    sh = slide.shapes.add_shape(shape, I(x), I(y), I(w), I(h))
    sh.name = name
    sh.fill.solid(); color(sh.fill.fore_color, fill)
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.theme_color = line
    sh.shadow.inherit = False
    sh.text_frame.text = ""
    return sh


def text(slide, x, y, w, h, paras, name, size=BODY, col=INK, bold=False, head=False, anchor=MSO_ANCHOR.TOP,
         align=PP_ALIGN.LEFT, bullets=False, space=4, lead_col=NAVY, margin=0.0):
    """paras: list of str, (lead, rest) tuples or lists of (text, {bold, col}) runs."""
    tb = slide.shapes.add_textbox(I(x), I(y), I(w), I(h))
    tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = I(margin)
    tf.vertical_anchor = anchor
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space)
        runs = para if isinstance(para, list) else ([(para[0], {"bold": True, "col": lead_col}), (para[1], {})]
                                                     if isinstance(para, tuple) else [(para, {})])
        for t, fmt in runs:
            r = p.add_run(); r.text = t
            r.font.size = Pt(fmt.get("size", size))
            r.font.bold = fmt.get("bold", bold)
            color(r.font.color, fmt.get("col", col))
            if head or fmt.get("head"):
                r.font.name = "+mj-lt"
        if bullets:
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(I(0.2))); pPr.set("indent", str(-I(0.2)))
            clr = etree.SubElement(pPr, f"{{{A}}}buClr"); sc = etree.SubElement(clr, f"{{{A}}}schemeClr"); sc.set("val", "accent1")
            etree.SubElement(pPr, f"{{{A}}}buFont").set("typeface", "Arial")
            etree.SubElement(pPr, f"{{{A}}}buChar").set("char", "▪")
    return tb


def icon(slide, name, tone, x, y, size, label):
    pic = slide.shapes.add_picture(str(ICONS / f"{name}-{tone}.png"), I(x), I(y), I(size), I(size))
    pic.name = f"Icon {label}"
    pic._element.nvPicPr.cNvPr.set("descr", "")      # decorative
    return pic


def card(slide, x, y, w, h, heading, items, icon_name, name, head_h=0.5, stat=None):
    """Card with a solid accent1 header band, white icon at its right corner and a bg2 body."""
    box(slide, x, y + head_h, w, h - head_h, LIGHT, f"{name} body")
    box(slide, x, y, w, head_h, ACC, f"{name} header")
    text(slide, x + 0.15, y, w - 0.75, head_h, [heading], f"{name} heading", size=HEAD, col=WHITE, bold=True,
         head=True, anchor=MSO_ANCHOR.MIDDLE)
    icon(slide, icon_name, "white", x + w - 0.48, y + (head_h - 0.34) / 2, 0.34, name)
    body_h = h - head_h - 0.3 - (0.75 if stat else 0)
    text(slide, x + 0.18, y + head_h + 0.15, w - 0.33, body_h, items, f"{name} text", bullets=True, space=6)
    if stat:
        fig, label = stat
        text(slide, x + 0.18, y + h - 0.8, w - 0.33, 0.65,
             [[(fig, {"size": FIG, "bold": True, "col": NAVY, "head": True}), ("  " + label, {"col": INK})]],
             f"{name} stat", anchor=MSO_ANCHOR.BOTTOM)


def stepper(slide, x, y, w, h, steps, name, current=None, size=BODY):
    n = len(steps)
    overlap = 0.12
    sw = (w + overlap * (n - 1)) / n
    for i, label in enumerate(steps):
        shape = MSO_SHAPE.PENTAGON if i == 0 else MSO_SHAPE.CHEVRON
        is_cur = current is not None and i == current
        sh = box(slide, x + i * (sw - overlap), y, sw, h, NAVY if is_cur else LIGHT, f"{name} step {i + 1}", shape=shape)
        sh.adjustments[0] = 0.28
        tf = sh.text_frame
        tf.word_wrap = True
        tf.margin_left = I(0.26 if i else 0.1); tf.margin_right = I(0.14)
        tf.margin_top = tf.margin_bottom = I(0.02)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        p.text = label
        for r in p.runs:
            r.font.size = Pt(size); r.font.bold = True
            color(r.font.color, WHITE if is_cur else NAVY)


def copy_pictures(src_shape, dst_slide):
    el = copy.deepcopy(src_shape._element)
    for blip in el.iter(f"{{{A}}}blip"):
        rid = blip.get(f"{{{R}}}embed")
        if rid:
            _, new = dst_slide.part.get_or_add_image_part(io.BytesIO(src_shape.part.related_part(rid).blob))
            blip.set(f"{{{R}}}embed", new)
    dst_slide.shapes._spTree.append(el)


def old_shape(slide_no, name):
    return next(sh for sh in old_slides[slide_no - 1].shapes if sh.name == name)


# ================================================================ slides ======
# 1  Title
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
              notes="Frame the course as one budget decision studied from five angles. Alpenglow is fictional; "
                    "the data are synthetic with a known truth revealed in Session 5.")
rows = [
    ("LuChartLine", ("Marketing analytics ", "turns marketing data into decisions on markets, prices, channels and budgets, and checks whether they worked.")),
    ("LuEuro", ("One budget question: ", "how should a fixed media budget be split across countries and channels?")),
    ("LuScale", ("Marketing mix modelling ", "is back at the centre since privacy rules weakened user-level tracking. Managers who can read and challenge it own the budget debate.")),
    ("LuCandy", ("One running case: ", "Alpenglow, a Vienna-based premium chocolate brand selling in Austria, Germany, France, Italy, the Netherlands and Poland.")),
    ("LuBot", ("Python with AI assistants: ", "the assistant does most of the typing; you specify, run, check and communicate the analysis.")),
]
rh = (4.25 - GAP * 4) / 5
for i, (ic, para) in enumerate(rows):
    y = 1.35 + i * (rh + GAP)
    box(s, 0.5, y, 9.0, rh, LIGHT, f"Content row {i + 1}")
    icon(s, ic, "navy", 0.72, y + (rh - 0.42) / 2, 0.42, f"content row {i + 1}")
    text(s, 1.4, y, 7.9, rh, [para], f"Content text {i + 1}", anchor=MSO_ANCHOR.MIDDLE)

# 4  Five sessions, five decisions: card grid plus the central question
s = add_slide("Titel und Inhalt", "Five sessions, five decisions",
              notes="Each session starts from a decision an international marketing manager has to take and works "
                    "backwards to the model that answers it. Session 5 is the board meeting where groups defend their budget.")
sessions = [
    ("Session 1", "Tue 6" + NB + "Oct", "Is our price too high in Poland?", "Price and promotion elasticities"),
    ("Session 2", "Tue 13" + NB + "Oct", "What did TV do for us in Germany?", "Adstock, saturation and ROAS"),
    ("Session 3", "Tue 20" + NB + "Oct", "Where should the next euro go?", "Budget allocation across countries and channels"),
    ("Session 4", "Tue 27" + NB + "Oct", "Can we trust the model?", "Forecasts, geo-lift tests and attribution"),
    ("Session 5", "Tue 3" + NB + "Nov", "Board meeting", "Groups pitch and defend their 2027 budget"),
]
cw = (9.0 - GAP * 4) / 5
for i, (head, date, q, method) in enumerate(sessions):
    x = 0.5 + i * (cw + GAP)
    box(s, x, 1.35, cw, 2.95, LIGHT, f"Session card {i + 1}")
    box(s, x, 1.35, cw, 0.45, NAVY if i < 4 else ACC, f"Session header {i + 1}")
    text(s, x + 0.1, 1.35, cw - 0.2, 0.45, [head], f"Session heading {i + 1}", size=HEAD, col=WHITE, bold=True,
         head=True, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 0.12, 1.92, cw - 0.22, 2.3,
         [[(date, {"col": NAVY})], [(q, {"bold": True, "col": NAVY})], [("→ " + method, {"col": ACC})]],
         f"Session text {i + 1}", space=8)
box(s, 0.5, 4.5, 9.0, 1.05, NAVY, "Central question box")
text(s, 0.75, 4.5, 8.5, 1.05,
     [[("The question behind all five sessions: ", {"bold": True, "col": WHITE}),
       ("how should Alpenglow split a fixed media budget across six countries and five channels?", {"col": WHITE})]],
     "Central question", size=HEAD, head=True, anchor=MSO_ANCHOR.MIDDLE)

# 5 and 6  Learning outcomes: grouped bands
def bands(slide, groups, top, height, prefix):
    for g, (ic, heading, items) in enumerate(groups):
        y = top + g * (height + GAP)
        box(slide, 0.5, y, 9.0, height, LIGHT, f"{prefix} band {g + 1}")
        box(slide, 0.5, y, 0.07, height, ACC, f"{prefix} bar {g + 1}")
        icon(slide, ic, "navy", 0.75, y + (height - 0.42) / 2, 0.42, f"{prefix} {g + 1}")
        text(slide, 1.3, y, 1.4, height, [heading], f"{prefix} heading {g + 1}", size=HEAD, col=NAVY,
             bold=True, head=True, anchor=MSO_ANCHOR.MIDDLE, space=0)
        paras = [[(num + NB + NB, {"bold": True, "col": ACC}), (lead, {"bold": True, "col": NAVY}), (rest, {})]
                 for num, lead, rest in items]
        text(slide, 2.85, y + 0.1, 6.45, height - 0.2, paras, f"{prefix} outcomes {g + 1}", space=6,
             anchor=MSO_ANCHOR.MIDDLE)


s = add_slide("Titel und Inhalt", "Learning outcomes",
              notes="Outcomes 1 to 6 are the analytical core of the course; 7 to 11 on the next slide are the working skills.")
text(s, 0.5, 1.3, 9.0, 0.3, ["On successful completion of this module, students will be able to:"], "Outcomes intro")
bands(s, [
    ("LuChartLine", "Model the market", [
        ("1", "Explain marketing mix modelling: ", "carryover, saturation, baseline versus incremental sales, ROAS versus marginal ROAS."),
        ("2", "Estimate response models ", "in Python, from OLS and log-log elasticities to fixed effects and Bayesian MMM.")]),
    ("LuEuro", "Decide on budgets", [
        ("3", "Allocate budgets ", "across countries and channels and defend the allocation under uncertainty."),
        ("4", "Forecast sales ", "and evaluate the forecasts as the baseline for planning.")]),
    ("LuFlaskConical", "Test the evidence", [
        ("5", "Design experiments: ", "analyse a geo-lift test and use it to validate and calibrate an MMM."),
        ("6", "Compare attribution: ", "explain why last-touch, regression-based and Shapley attribution disagree across markets.")]),
], 1.72, 1.18, "Outcomes")

s = add_slide("Titel und Inhalt", "Learning outcomes (continued)")
bands(s, [
    ("LuCode", "Work with tools", [
        ("7", "Work reproducibly: ", "use Python, Positron, Quarto and GitHub to build analyses that colleagues can rerun and audit."),
        ("8", "Use AI assistants responsibly: ", "direct an AI coding assistant, verify its output and document the prompts behind an analysis.")]),
    ("LuUsers", "Work with people", [
        ("9", "Communicate: ", "present analytical findings to a board audience in a written report and a pitch."),
        ("10", "Work in teams: ", "collaborate in version-controlled projects and take collective, data-driven decisions."),
        ("11", "Think critically: ", "evaluate data sources, model assumptions and findings in an international marketing context.")]),
], 1.35, 2.0, "Outcomes II")

# 7  Methods of teaching and learning: stepper plus two cards
s = add_slide("Titel und Inhalt", "Methods of teaching and learning",
              notes="In person, five Tuesdays. Bring your own laptop with the environment installed; a setup clinic runs "
                    "at the start of Session 1. Between sessions: read, take the quiz, work on the project.")
text(s, 0.5, 1.28, 9.0, 0.3, [[("Every session", {"bold": True, "col": NAVY})]], "Session rhythm label")
stepper(s, 0.5, 1.62, 9.0, 0.72, ["Concept lecture\v60" + NB + "min", "Guided lab\v90" + NB + "min",
                                  "Team exercise\v60" + NB + "min", "Debrief\vand quiz"], "Session rhythm")
cw2 = (9.0 - 0.5) / 2
card(s, 0.5, 2.55, cw2, 3.0, "Between sessions", [
    "Read the book chapters and materials in advance",
    "Online quiz after Sessions 1 to 4",
    "Lab check-ins after Sessions 2 and 4",
    "Group project in your team repository",
    "Q&A forum on Canvas; consulting hours on request"], "LuHouse", "Between sessions card")
arrow = box(s, 0.5 + cw2 + 0.09, 3.85, 0.32, 0.4, ACC, "Card arrow", shape=MSO_SHAPE.CHEVRON)
card(s, 0.5 + cw2 + 0.5, 2.55, cw2, 3.0, "In the classroom", [
    "Five Tuesdays, 6 October to 3" + NB + "November 2026",
    "Bring your laptop with Python, Positron, Quarto and GitHub",
    "AI-assisted coding: you direct, the assistant types, you check",
    "Pull, commit and push from Session 1"], "LuSchool", "In the classroom card")

# 8  Module roadmap: table
s = add_slide("Titel und Tabelle", "Module roadmap", footer="Chapters: Yildirim and Kübler (2025), SAGE",
              notes="Chapter numbers refer to the 2025 Python edition of Yildirim and Kübler. Times and rooms are on Canvas.")
rows = [
    ("Session", "Date", "Topic", "Methods", "Chapter"),
    ("1", "Tue 6" + NB + "Oct", "Course content and style, toolkit, regression foundations", "Descriptive statistics, OLS, log-log elasticities, dummies and interactions", "1, 11"),
    ("2", "Tue 13" + NB + "Oct", "Marketing mix modelling I: one country", "Adstock, saturation, decomposition, ROAS, diagnostics", "3"),
    ("3", "Tue 20" + NB + "Oct", "Marketing mix modelling II: many countries, one budget", "Panel fixed effects, hierarchical Bayesian MMM, budget optimisation", "3"),
    ("4", "Tue 27" + NB + "Oct", "Forecasting, experiments and attribution", "Time series regression, difference-in-differences, logistic regression, Shapley values", "9, 4"),
    ("5", "Tue 3" + NB + "Nov", "Group project pitches and wrap-up", "Board presentation, ground-truth reveal", "11"),
]
gf = ph(s, 1).insert_table(len(rows), len(rows[0]))
tbl = gf.table
widths = [1.3, 1.05, 2.2, 2.65, 1.25]
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
        if c_i in (0, 1, 4) and r_i > 0:
            p.alignment = PP_ALIGN.CENTER
        cell.margin_top = cell.margin_bottom = Emu(36000)

# 9  Assessment: native bar chart of the weights plus a rules card
s = add_slide("Titel und Inhalt", "Assessment strategy",
              notes="Six components. The group project is the centrepiece; quizzes and check-ins keep everyone on track "
                    "between sessions. Certificates and self-reflection are small but required.")
text(s, 0.5, 1.28, 5.0, 0.35, [[("Weight in the final grade", {"bold": True, "col": NAVY, "size": HEAD, "head": True})]],
     "Weights heading")
cd = CategoryChartData()
cats = ["Self-reflection", "Online certificates", "Peer review", "Lab check-ins (2" + NB + "×" + NB + "10" + NB + "%)",
        "Online quizzes (4" + NB + "×" + NB + "5" + NB + "%)", "Group project"]
cd.categories = cats
cd.add_series("Weight", (5, 5, 10, 20, 20, 40))
gfc = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, I(0.5), I(1.7), I(5.0), I(3.85), cd)
gfc.name = "Grade weights chart"
ch = gfc.chart
ch.has_legend = False
ch.has_title = False
ch.font.size = Pt(BODY)
ch.font.name = "+mn-lt"
plot = ch.plots[0]
plot.gap_width = 45
plot.has_data_labels = True
dl = plot.data_labels
dl.number_format = '0" %"'
dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END
dl.font.size = Pt(BODY); dl.font.bold = True; dl.font.color.theme_color = NAVY
ser = plot.series[0]
ser.format.fill.solid(); ser.format.fill.fore_color.theme_color = BARS
va = ch.value_axis
va.visible = False
va.has_major_gridlines = False
va.maximum_scale = 48
va.minimum_scale = 0
ca = ch.category_axis
ca.format.line.fill.background()
ca.tick_labels.font.size = Pt(BODY)
ca.tick_labels.font.color.theme_color = INK
card(s, 5.75, 1.35, 3.75, 4.2, "Rules", [
    ("Groups: ", "5 students; enrol on Canvas by the end of Session 1"),
    ("Grades: ", "WU scale, 1 from 90" + NB + "%, 2 from 80" + NB + "%, 3 from 70" + NB + "%, 4 from 60" + NB + "%"),
    ("Attendance: ", "at least 80" + NB + "% of sessions"),
    ("Late work: ", "minus 10 points per day unless agreed"),
    ("AI tools: ", "expected; you own every number you report"),
], "LuShieldCheck", "Rules card")

# 10  Online certificates: stat rows plus a deadline callout
s = add_slide("Titel und Inhalt", "Online certificates and set-up",
              notes="Both courses are free. The installation check is the command in the setup guide that prints 'ready'. "
                    "Bring problems to the setup clinic at the start of Session 1.")
stats = [
    ("5" + NB + "h", ("Kaggle Learn: Python. ", "Free course with a certificate on completion.")),
    ("1" + NB + "h", ("GitHub Skills: Introduction to GitHub. ", "Free, runs in the browser.")),
    ("45" + NB + "min", ("Course environment. ", "Install Python (via uv), Positron, Quarto and GitHub Desktop with the setup guide, then run the installation check.")),
]
for i, (fig, para) in enumerate(stats):
    y = 1.4 + i * (0.85 + GAP)
    box(s, 0.5, y, 0.07, 0.85, ACC, f"Stat bar {i + 1}")
    text(s, 0.75, y, 1.75, 0.85, [[(fig, {"size": FIG, "bold": True, "col": NAVY, "head": True})]], f"Stat figure {i + 1}",
         anchor=MSO_ANCHOR.MIDDLE)
    text(s, 2.6, y, 6.9, 0.85, [para], f"Stat text {i + 1}", anchor=MSO_ANCHOR.MIDDLE)
box(s, 0.5, 4.5, 9.0, 1.05, LIGHT, "Deadline callout")
icon(s, "LuClock", "navy", 0.75, 4.75, 0.55, "deadline")
text(s, 1.55, 4.5, 7.75, 1.05, [("Deadline: ", "upload both certificates and a screenshot of the passing installation check on Canvas by "
                                               "Mon 12" + NB + "Oct, 11:59" + NB + "pm.")],
     "Deadline text", anchor=MSO_ANCHOR.MIDDLE)

# 11  Quizzes and lab check-ins: two cards with figures
s = add_slide("Titel und Inhalt", "Quizzes and lab check-ins",
              notes="Quizzes test concepts, not code. Check-ins replicate a lab for another country and are auto-checked "
                    "for plausibility before grading.")
cw3 = (9.0 - 0.2) / 2
card(s, 0.5, 1.35, cw3, 3.25, "Online quizzes", [
    "After each of Sessions 1 to 4",
    "Open Wednesday 9" + NB + "am, close Monday 11:59" + NB + "pm",
    "10 multiple-choice questions in 10" + NB + "minutes",
    "Closed book: concepts, not code"], "LuListChecks", "Quiz card", stat=("5" + NB + "%", "per quiz, 20" + NB + "% in total"))
card(s, 0.7 + cw3, 1.35, cw3, 3.25, "Lab check-ins", [
    "After Sessions 2 and 4",
    "Replicate the lab for another country or dataset",
    "Submit notebook, HTML, result files and prompt log",
    "Auto-checked for plausibility, reviewed for interpretation"], "LuNotebookPen", "Check-in card",
     stat=("10" + NB + "%", "per check-in, 20" + NB + "% in total"))
box(s, 0.5, 4.8, 9.0, 0.75, NAVY, "Takeaway box")
text(s, 0.75, 4.8, 8.5, 0.75, [[("Both are individual: ", {"bold": True, "col": WHITE}),
                               ("quizzes check that you understand the concepts, check-ins that you can run, check and "
                                "explain an analysis on your own.", {"col": WHITE})]],
     "Takeaway text", anchor=MSO_ANCHOR.MIDDLE)

# 12  Group project: timeline stepper, deliverable cards, the task
s = add_slide("Titel und Inhalt", "Group project",
              notes="The brief, rubric and starter repository are in the course GitHub organisation. Online consulting "
                    "hours need registration.")
text(s, 0.5, 1.28, 9.0, 0.3, [[("Timeline", {"bold": True, "col": NAVY})]], "Timeline label")
stepper(s, 0.5, 1.62, 9.0, 0.72, ["Session" + NB + "1\vform groups", "By S2\vrepo and data",
                                  "By S4\vfirst model", "Mon 2" + NB + "Nov\vsubmit", "Tue 3" + NB + "Nov\vpitch"],
        "Project timeline", current=4)
deliv = [
    ("LuFileText", "Quarto report", "max 12 pages, rendered to HTML"),
    ("LuFileSpreadsheet", "Allocation file", "CSV with weekly spend per country and channel"),
    ("LuPresentation", "Pitch deck", "max 8 slides for a 10-minute pitch"),
    ("LuGitBranch", "Repository", "code, data pipeline and a prompt log"),
]
dw = (9.0 - GAP * 3) / 4
for i, (ic, head, body) in enumerate(deliv):
    x = 0.5 + i * (dw + GAP)
    box(s, x, 2.55, dw, 1.75, LIGHT, f"Deliverable card {i + 1}")
    icon(s, ic, "navy", x + 0.15, 2.7, 0.4, f"deliverable {i + 1}")
    text(s, x + 0.15, 3.18, dw - 0.3, 1.05, [[(head, {"bold": True, "col": NAVY})], body], f"Deliverable text {i + 1}", space=4)
box(s, 0.5, 4.5, 9.0, 1.05, NAVY, "Task box")
text(s, 0.75, 4.5, 8.5, 1.05,
     [[("The task: ", {"bold": True, "col": WHITE}),
       ("as Alpenglow's analytics team, recommend to the board how the 2027 media budget should be split across "
        "six countries and five channels.", {"col": WHITE})]], "Task text", size=HEAD, head=True, anchor=MSO_ANCHOR.MIDDLE)

# 13  Peer rating: text left, form right
s = add_slide("Inhalt und Bild mit Logo", "Peer rating",
              notes="The peer rating form is on Canvas. Each member rates the others; self-ratings are not allowed.")
body = ph(s, 1)
tf = body.text_frame
items = [("Who: ", "every group member rates the other members on a 0 to 10 scale"),
         ("Criteria: ", "tasks carried out, deadlines met, quality of work, communication and respect, attendance, pre-agreed rules"),
         ("Confidential: ", "feeds the peer review component (10" + NB + "%)"),
         ("When: ", "submit on Canvas with the final project")]
for i, it in enumerate(items):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    set_runs(p, it)
    for r in p.runs:
        r.font.size = Pt(BODY)
    p.runs[0].font.color.theme_color = NAVY
form = old_shape(15, "Grafik 6")
pb = ph(s, 2)
bx, by, bw, bh = pb.left, pb.top, pb.width, pb.height
remove_shape(pb); remove_shape(ph(s, 13))
from PIL import Image
iw, ih = Image.open(io.BytesIO(form.image.blob)).size
sc = min(bw / iw, bh / ih)
pic = s.shapes.add_picture(io.BytesIO(form.image.blob), bx + (bw - int(iw * sc)) // 2, by, int(iw * sc), int(ih * sc))
pic.name = "Peer rating form"
pic._element.nvPicPr.cNvPr.set("descr", "Peer rating form: criteria list and a grade table for five group members")

# 14  Closing contact card
add_slide("Abschlussfolie Kontakt", notes="Any questions? Contact details on the card.")

# ---- language tag on every run ----------------------------------------------
for slide in prs.slides:
    for sh in slide.shapes:
        frames = [sh.text_frame] if sh.has_text_frame else []
        if sh.has_table:
            frames += [c.text_frame for row in sh.table.rows for c in row.cells]
        for tf in frames:
            for p in tf.paragraphs:
                for r in p.runs:
                    r._r.get_or_add_rPr().set("lang", "en-GB")

prs.save(OUT)
print("saved", OUT, "slides:", len(prs.slides))
