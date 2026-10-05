"""Build the WT 26/27 course outline deck on the WU template shipped with the
polish-slides skill. Pictures are carried over from the WT 25/26 deck.

usage: see slides/README.md
"""
import copy
import io
import sys

from lxml import etree
from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER
from pptx.util import Emu, Pt

TEMPLATE, OLD, OUT = sys.argv[1:4]
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NB = " "
FOOTER = "International Marketing Analytics" + NB + "·" + NB + "WT" + NB + "2026/27"

prs = Presentation(TEMPLATE)
old = Presentation(OLD)
old_slides = list(old.slides)

# ---- remove the template's sample slides -------------------------------------
sldIdLst = prs.slides._sldIdLst
for sldId in list(sldIdLst):
    prs.part.drop_rel(sldId.rId)
    sldIdLst.remove(sldId)

L = {l.name: l for l in prs.slide_layouts}


def layout(name):
    return L[name]


def add_slide(layout_name, title=None, footer=FOOTER, notes=None):
    s = prs.slides.add_slide(layout(layout_name))
    lay = layout(layout_name)
    # clone footer and slide-number placeholders from the layout (python-pptx skips them)
    for lph in lay.placeholders:
        t = lph.placeholder_format.type
        if t in (PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.SLIDE_NUMBER):
            el = copy.deepcopy(lph._element)
            s.shapes._spTree.append(el)
    for sh in s.placeholders:
        t = sh.placeholder_format.type
        if t == PP_PLACEHOLDER.FOOTER and footer is not None:
            set_runs(sh.text_frame.paragraphs[0], footer)
        if t in (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE) and title is not None:
            set_runs(sh.text_frame.paragraphs[0], title)
    if notes:
        s.notes_slide.notes_text_frame.text = notes
    return s


def ph(slide, idx):
    for sh in slide.placeholders:
        if sh.placeholder_format.idx == idx:
            return sh
    raise KeyError(idx)


def remove_shape(sh):
    sh._element.getparent().remove(sh._element)


def set_runs(p, text):
    """Replace the paragraph's runs by one run (or bold lead-in + rest when text is a tuple)."""
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    if isinstance(text, tuple):
        lead, rest = text
        r1 = p.add_run()
        r1.text = lead
        r1.font.bold = True
        r2 = p.add_run()
        r2.text = rest
    else:
        r = p.add_run()
        r.text = text


def fill_body(shape, items, size=None, numbered_from=None):
    """items: list of (level, text) with text a str or (lead, rest) tuple."""
    tf = shape.text_frame
    # keep the first paragraph element as formatting base
    first = tf.paragraphs[0]
    for extra in tf.paragraphs[1:]:
        extra._p.getparent().remove(extra._p)
    n = 0
    for i, (lvl, text) in enumerate(items):
        p = first if i == 0 else tf.add_paragraph()
        set_runs(p, text)
        p.level = lvl
        if size:
            for r in p.runs:
                r.font.size = Pt(size)
        if numbered_from is not None and text != "":
            n += 1
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", "342900")
            pPr.set("indent", "-342900")
            for tag in ("buNone", "buChar", "buAutoNum", "buFont"):
                for e in pPr.findall(f"{{{A}}}{tag}"):
                    pPr.remove(e)
            buFont = etree.SubElement(pPr, f"{{{A}}}buFont")
            buFont.set("typeface", "+mj-lt")
            bu = etree.SubElement(pPr, f"{{{A}}}buAutoNum")
            bu.set("type", "arabicPeriod")
            bu.set("startAt", str(numbered_from))
        if text == "":
            pPr = p._p.get_or_add_pPr()
            for e in pPr.findall(f"{{{A}}}buAutoNum"):
                pPr.remove(e)
            etree.SubElement(pPr, f"{{{A}}}buNone")


def copy_pictures(src_shape, dst_slide):
    """Deep-copy a picture or group of pictures from the old deck, re-linking image parts."""
    src_part = src_shape.part
    el = copy.deepcopy(src_shape._element)
    for blip in el.iter(f"{{{A}}}blip"):
        old_rid = blip.get(f"{{{R}}}embed")
        if not old_rid:
            continue
        blob = src_part.related_part(old_rid).blob
        image_part, new_rid = dst_slide.part.get_or_add_image_part(io.BytesIO(blob))
        blip.set(f"{{{R}}}embed", new_rid)
    dst_slide.shapes._spTree.append(el)
    return el


def old_shape(slide_no, name):
    for sh in old_slides[slide_no - 1].shapes:
        if sh.name == name:
            return sh
    raise KeyError(name)


# =============================================================================
# 1  Title
s = add_slide("Titelfolie Kontakt", footer=None,
              notes="Welcome. This deck explains what the course is about, how it is taught and how it is assessed.")
set_runs(ph(s, 0).text_frame.paragraphs[0], "International Marketing Analytics")
set_runs(ph(s, 1).text_frame.paragraphs[0], "Course content and style")
set_runs(ph(s, 12).text_frame.paragraphs[0], "Winter term 2026/27")

# 2  The journey begins (welcome picture)
s = add_slide("Titel und Inhalt", "The journey begins",
              notes="Ice-breaker: who is in the room, which countries, which prior exposure to analytics.")
remove_shape(ph(s, 1))
copy_pictures(old_shape(2, "Grafik 5"), s)

# 3  Instructor: text left, portrait right
s = add_slide("Inhalt und Bild mit Logo", "Instructor: Dr Arne Floh",
              notes="Contact me by e-mail first; office hours are booked through the calendar link on the closing slide.")
fill_body(ph(s, 1), [
    (0, ("Position: ", "Senior Lecturer in International Marketing, Institute for International Business, WU Vienna")),
    (0, ("Also: ", "Deputy Programme Director, Export and Internationalisation Management")),
    (0, ("Teaching: ", "International Marketing, Marketing Analytics, Digital Marketing and Social Media, Entrepreneurial Marketing")),
    (0, ("Research: ", "Consumer behaviour, relationship marketing, electronic marketing and social media")),
    (0, ("Contact: ", "arne.floh@wu.ac.at, office hours by appointment (see closing slide)")),
], size=14)
portrait = old_shape(3, "Picture 2")
ph(s, 2).insert_picture(io.BytesIO(portrait.image.blob))
remove_shape(ph(s, 13))  # no logo

# 4  Instructor: background collage
s = add_slide("Zwei Inhalte", "Instructor: background",
              notes="Twenty years of teaching across WU, Emory, Surrey and JKU; industry background; the private side.")
fill_body(ph(s, 1), [
    (0, ("Experience: ", "international and industry background, more than 20 years of teaching")),
    (0, ("Supervision: ", "BSc, MSc and PhD theses")),
    (0, ("Private: ", "football, electronic gadgets, Austrian wine")),
], size=16)
remove_shape(ph(s, 2))
collage = copy_pictures(old_shape(4, "Gruppieren 6"), s)

# 5  Module content
s = add_slide("Titel und Inhalt", "Module content",
              notes="Frame the course as one budget decision studied from five angles. Alpenglow is fictional; the data are synthetic with a known truth revealed in Session 5.")
fill_body(ph(s, 1), [
    (0, ("Marketing analytics ", "turns marketing data into decisions: which markets to invest in, how to price, how much to spend on which channel, and whether it worked.")),
    (0, ("One question dominates ", "international marketing budgets today: how should a fixed media budget be split across countries and channels?")),
    (0, ("Marketing mix modelling (MMM) ", "is back at the centre of this debate since privacy changes made user-level tracking unreliable. Managers who can read, challenge and commission these models hold the budget conversation.")),
    (0, ("One running case: ", "Alpenglow, a Vienna-based premium chocolate brand active in six European markets (AT, DE, FR, IT, NL, PL).")),
    (0, ("Python with AI assistants: ", "the assistant does most of the typing; you learn to specify, run, check and communicate analyses.")),
], size=14)

# 6  Decision of the day per session
s = add_slide("Titel und Inhalt", "Five sessions, five decisions",
              notes="Each session starts from a manager's question and works backwards to the regression that answers it.")
fill_body(ph(s, 1), [
    (0, "Each session starts from a decision an international marketing manager has to take and works backwards to the model that answers it."),
    (0, ""),
    (0, ("Session 1: ", "Is our price too high in Poland? Price and promotion elasticities across countries")),
    (0, ("Session 2: ", "What did TV do for us in Germany? Carryover, saturation and return on ad spend")),
    (0, ("Session 3: ", "Where should the next euro go? Budget allocation across six countries and five channels")),
    (0, ("Session 4: ", "Can we trust the model? Sales forecasts, geo-lift experiments and multi-market attribution")),
    (0, ("Session 5: ", "Board meeting: the groups pitch and defend their 2027 budget")),
], size=14)

# 7 and 8  Learning outcomes
s = add_slide("Titel und Inhalt", "Learning outcomes",
              notes="Outcomes 1 to 6 are the analytical core; 7 to 11 are the working skills.")
fill_body(ph(s, 1), [
    (0, "On successful completion of this module, students will be able to:"),
    (0, ""),
    (0, ("Explain marketing mix modelling: ", "carryover (adstock), saturation, baseline versus incremental sales, ROAS versus marginal ROAS.")),
    (0, ("Estimate market response models: ", "specify, estimate and diagnose regression models in Python, from OLS and log-log elasticities to panel fixed effects and hierarchical Bayesian MMM.")),
    (0, ("Allocate budgets across markets: ", "translate model output into a cross-country, cross-channel allocation and defend it under uncertainty.")),
    (0, ("Forecast sales: ", "produce and evaluate short-term forecasts as the baseline for planning.")),
    (0, ("Design experiments: ", "design and analyse a geo-lift test and use it to validate and calibrate an MMM.")),
    (0, ("Compare attribution approaches: ", "explain why last-touch, regression-based and Shapley attribution disagree across markets.")),
], size=13)
# number only the outcome paragraphs
tf = ph(s, 1).text_frame
for k, p in enumerate(tf.paragraphs):
    if k >= 2:
        pPr = p._p.get_or_add_pPr()
        pPr.set("marL", "342900"); pPr.set("indent", "-342900")
        for e in list(pPr):
            if e.tag in (f"{{{A}}}buNone", f"{{{A}}}buChar", f"{{{A}}}buAutoNum", f"{{{A}}}buFont"):
                pPr.remove(e)
        etree.SubElement(pPr, f"{{{A}}}buFont").set("typeface", "+mj-lt")
        bu = etree.SubElement(pPr, f"{{{A}}}buAutoNum"); bu.set("type", "arabicPeriod")
    elif k == 1:
        pPr = p._p.get_or_add_pPr(); etree.SubElement(pPr, f"{{{A}}}buNone")
    else:
        pPr = p._p.get_or_add_pPr(); pPr.set("marL", "0"); pPr.set("indent", "0"); etree.SubElement(pPr, f"{{{A}}}buNone")

s = add_slide("Titel und Inhalt", "Learning outcomes (continued)")
fill_body(ph(s, 1), [
    (0, ("Work reproducibly: ", "use Python, Positron, Quarto and GitHub to build analyses that colleagues can rerun and audit.")),
    (0, ("Use AI assistants responsibly: ", "direct an AI coding assistant, verify its output and document the prompts behind an analysis.")),
    (0, ("Communicate: ", "present analytical findings to a board audience in a written report and a pitch.")),
    (0, ("Work in teams: ", "collaborate in version-controlled analytical work and take collective data-driven decisions.")),
    (0, ("Think critically: ", "evaluate data sources, model assumptions and findings in the context of international marketing.")),
], size=14, numbered_from=7)

# 9  Methods of teaching and learning (comparison layout)
s = add_slide("Zwei Inhalte Vergleich", "Methods of teaching and learning",
              notes="In person, five Tuesdays. Bring your own laptop with the environment installed; a setup clinic runs at the start of Session 1.")
set_runs(ph(s, 13).text_frame.paragraphs[0], "In the classroom")
set_runs(ph(s, 17).text_frame.paragraphs[0], "Between sessions")
fill_body(ph(s, 1), [
    (0, "Five in-person sessions on Tuesdays, 6 October to 3" + NB + "November 2026"),
    (0, "Concept lecture (60" + NB + "min), guided lab in Positron (90" + NB + "min), team exercise on the project data (60" + NB + "min), debrief"),
    (0, "Coding is AI-assisted: your laptop, your assistant, your checks"),
    (0, "Everything lives in GitHub: pull, commit and push from Session 1"),
], size=14)
fill_body(ph(s, 2), [
    (0, "Read the book chapters and session materials in advance"),
    (0, "Online quiz after each of Sessions 1 to 4"),
    (0, "Lab check-ins after Sessions 2 and 4"),
    (0, "Group project work in your team repository; consulting hours on request"),
    (0, "Q&A forum on Canvas"),
], size=14)

# 10  Roadmap table
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
tph = ph(s, 1)
gf = tph.insert_table(len(rows), len(rows[0]))
tbl = gf.table
widths = [Emu(int(1.1 * 914400)), Emu(int(1.05 * 914400)), Emu(int(2.45 * 914400)), Emu(int(2.75 * 914400)), Emu(int(1.1 * 914400))]
for i, w in enumerate(widths):
    tbl.columns[i].width = w
gf.width = sum(widths)
for r_i, row in enumerate(rows):
    for c_i, txt in enumerate(row):
        cell = tbl.cell(r_i, c_i)
        p = cell.text_frame.paragraphs[0]
        set_runs(p, txt)
        for r in p.runs:
            r.font.size = Pt(12)
        if c_i in (0, 1, 4) and r_i > 0:
            from pptx.enum.text import PP_ALIGN
            p.alignment = PP_ALIGN.CENTER
        cell.margin_top = Emu(36000); cell.margin_bottom = Emu(36000)

# 11  Assessment (comparison layout)
s = add_slide("Zwei Inhalte Vergleich", "Assessment strategy",
              notes="Six components. The group project is the centrepiece; quizzes and check-ins keep everyone on track between sessions.")
set_runs(ph(s, 13).text_frame.paragraphs[0], "Components")
set_runs(ph(s, 17).text_frame.paragraphs[0], "Rules")
fill_body(ph(s, 1), [
    (0, ("5" + NB + "% ", "Online certificates Python and GitHub (individual)")),
    (0, ("5" + NB + "% ", "Self-reflection (individual)")),
    (0, ("20" + NB + "% ", "Online quizzes, 4" + NB + "×" + NB + "5" + NB + "% (individual)")),
    (0, ("20" + NB + "% ", "Lab check-ins, 2" + NB + "×" + NB + "10" + NB + "% (individual)")),
    (0, ("40" + NB + "% ", "Group project: report, repository and pitch")),
    (0, ("10" + NB + "% ", "Peer review")),
], size=14)
fill_body(ph(s, 2), [
    (0, ("Groups: ", "5 students, enrol on Canvas by the end of Session 1")),
    (0, ("Grades: ", "WU scale, 1 from 90" + NB + "%, 2 from 80" + NB + "%, 3 from 70" + NB + "%, 4 from 60" + NB + "%")),
    (0, ("Attendance: ", "at least 80" + NB + "% of sessions")),
    (0, ("Late submissions: ", "minus 10 percentage points per day unless agreed in advance")),
    (0, ("AI tools: ", "expected for coding; you remain responsible for every number you report")),
], size=14)

# 12  Online certificates
s = add_slide("Titel und Inhalt", "Online certificates",
              notes="Both courses are free. The installation check is the command in the setup guide that prints 'ready'.")
fill_body(ph(s, 1), [
    (0, "Complete two free online courses before the second session:"),
    (1, ("Kaggle Learn: Python ", "(about 5" + NB + "hours, certificate on completion)")),
    (1, ("GitHub Skills: Introduction to GitHub ", "(about 1" + NB + "hour)")),
    (0, "Install the course environment with the setup guide: Python via uv, Positron, Quarto, GitHub Desktop, and run the installation check"),
    (0, ("Upload ", "both certificates and a screenshot of the passing installation check on Canvas by Mon 12" + NB + "Oct, 11:59" + NB + "pm")),
], size=16)

# 13  Quizzes and lab check-ins (comparison layout)
s = add_slide("Zwei Inhalte Vergleich", "Quizzes and lab check-ins",
              notes="Quizzes test concepts, not code. Check-ins replicate a lab for another country and are auto-checked before grading.")
set_runs(ph(s, 13).text_frame.paragraphs[0], "Online quizzes (individual)")
set_runs(ph(s, 17).text_frame.paragraphs[0], "Lab check-ins (individual)")
fill_body(ph(s, 1), [
    (0, "After each of Sessions 1 to 4"),
    (0, "Open Wednesday 9" + NB + "am, close Monday 11:59" + NB + "pm"),
    (0, "10 multiple-choice questions in 10" + NB + "minutes"),
    (0, "Closed book: concepts, not code"),
    (0, "5" + NB + "% each"),
], size=16)
fill_body(ph(s, 2), [
    (0, "After Sessions 2 and 4"),
    (0, "Replicate the lab for another country or dataset with your AI assistant"),
    (0, "Submit the Quarto notebook, rendered HTML, result files and a short prompt log on Canvas"),
    (0, "Auto-checked for plausibility, reviewed for interpretation"),
    (0, "10" + NB + "% each"),
], size=16)

# 14  Group project
s = add_slide("Titel und Inhalt", "Group project",
              notes="The brief, rubric and starter repository are in the course GitHub organisation.")
fill_body(ph(s, 1), [
    (0, ("The task: ", "as Alpenglow's analytics team, recommend to the board how the 2027 media budget should be split across six countries and five channels.")),
    (0, ("Deliverables: ", "GitHub repository with a Quarto report (max 12" + NB + "pages), allocation_2027.csv, a pitch deck (max 8" + NB + "slides) and a prompt log.")),
    (0, ("Milestones: ", "repository and data exploration before Session 2; first model table before Session 4.")),
    (0, ("Support: ", "online consulting hours (registration needed).")),
    (0, ("Deadline: ", "Mon 2" + NB + "Nov 2026, 6" + NB + "pm. Pitches in Session 5 on Tue 3" + NB + "Nov 2026.")),
], size=16)

# 15  Peer rating: text left, form on the right
s = add_slide("Inhalt und Bild mit Logo", "Peer rating",
              notes="The peer rating form is on Canvas. Each member rates the others; self-ratings are not allowed.")
fill_body(ph(s, 1), [
    (0, "Every group member rates the other members on a 0 to 10 scale"),
    (0, "Six criteria: tasks carried out, deadlines met, quality of work, communication and respect, attendance, pre-agreed rules"),
    (0, "Kept in strict confidence; feeds the peer review component (10" + NB + "%)"),
    (0, "Submit on Canvas with the final project"),
], size=14)
form = old_shape(15, "Grafik 6")
box = ph(s, 2)
bx, by, bw, bh = box.left, box.top, box.width, box.height
remove_shape(box)
remove_shape(ph(s, 13))
from PIL import Image as _Image
iw, ih = _Image.open(io.BytesIO(form.image.blob)).size
scale = min(bw / iw, bh / ih)
pw, phh = int(iw * scale), int(ih * scale)
s.shapes.add_picture(io.BytesIO(form.image.blob), bx + (bw - pw) // 2, by, pw, phh)

# 16  Closing contact card
s = add_slide("Abschlussfolie Kontakt", notes="Any questions? Contact details on the card.")

# ---- language tag on every run -------------------------------------------------
for slide in prs.slides:
    for sh in slide.shapes:
        frames = []
        if sh.has_text_frame:
            frames.append(sh.text_frame)
        if sh.has_table:
            for row in sh.table.rows:
                for cell in row.cells:
                    frames.append(cell.text_frame)
        for tf in frames:
            for p in tf.paragraphs:
                for r in p.runs:
                    r._r.get_or_add_rPr().set("lang", "en-GB")

prs.save(OUT)
print("saved", OUT, "slides:", len(prs.slides))
