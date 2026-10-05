"""Build the Session 1 set-up and registration deck on the WU template (polish-slides skill).

Four parts: register the accounts, install the tools, how Positron works, the Python
packages of the course (polars, plotnine, Great Tables, statsmodels). The code on the
package slides is the code in make_setup_figures.py, which also renders the chart and
table pictures; run that script first.

usage: python slides/build_setup_deck.py TEMPLATE.pptx OUT.pptx
"""
import copy
import sys
from pathlib import Path

from lxml import etree
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Pt

from wu_deck import (A, ACC, BODY, FIG, GAP, HEAD, INK, LIGHT, MONO, NAVY, NB, WHITE, Deck, I, box, card,
                     code_block, color, icon, ph, set_runs, stepper, text)

TEMPLATE, OUT = sys.argv[1:3]
FIGS = Path(__file__).resolve().parent / "figures"
FOOTER = "International Marketing Analytics" + NB + "·" + NB + "WT" + NB + "2026/27"
deck = Deck(TEMPLATE, FOOTER)
add_slide, L = deck.add_slide, deck.L
STEPS = ["Accounts", "Tools", "Repo", "Project", "Check", "AI"]
WHITE_BG = "FFFFFF"


def progress(slide, current):
    """The six set-up steps across the top, current step in navy (repeated on every step slide)."""
    stepper(slide, 0.5, 1.3, 9.0, 0.42, STEPS, "Progress", current=current, size=12)


def divider(title, part, notes):
    s = add_slide("Kapitelfolie", title, notes=notes)
    set_runs(ph(s, 11).text_frame.paragraphs[0], part)
    return s


def badge(slide, x, y, num, name, d=0.34, fill=NAVY):
    b = box(slide, x, y, d, d, fill, name, shape=MSO_SHAPE.OVAL)
    tf = b.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = str(num); r.font.size = Pt(12); r.font.bold = True
    color(r.font.color, WHITE)


def numbered(slide, x, y, w, items, name, row_h=0.62, gap=0.1):
    """Numbered rows: bg2 band, navy number badge, text with a bold lead-in."""
    for i, para in enumerate(items):
        ry = y + i * (row_h + gap)
        box(slide, x, ry, w, row_h, LIGHT, f"{name} row {i + 1}")
        badge(slide, x + 0.15, ry + (row_h - 0.34) / 2, i + 1, f"{name} number {i + 1}")
        text(slide, x + 0.65, ry, w - 0.8, row_h, [para], f"{name} text {i + 1}", anchor=MSO_ANCHOR.MIDDLE)


def callout(slide, y, h, icon_name, para, name, dark=False):
    box(slide, 0.5, y, 9.0, h, NAVY if dark else LIGHT, f"{name} box")
    icon(slide, icon_name, "white" if dark else "navy", 0.72, y + (h - 0.42) / 2, 0.42, name)
    if dark:
        lead, rest = para
        para = [(lead, {"bold": True, "col": WHITE}), (rest, {"col": WHITE})]
    text(slide, 1.35, y, 7.95, h, [para], f"{name} text", anchor=MSO_ANCHOR.MIDDLE)


def tile(slide, x, y, w, h, icon_name, head, lines, name, fill=LIGHT):
    """Icon at the top left, bold navy heading, plain lines underneath."""
    box(slide, x, y, w, h, fill, f"{name} tile")
    icon(slide, icon_name, "navy", x + 0.15, y + 0.15, 0.4, name)
    text(slide, x + 0.15, y + 0.65, w - 0.3, h - 0.75, [[(head, {"bold": True, "col": NAVY})]] + lines,
         f"{name} text", space=3)


def link(t, url):
    return (t, {"link": url, "col": ACC})


# ================================================================ slides ======
# 1  Title (same spacing in the contact block as the course outline deck)
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
              notes="Today we set up every laptop together. Nothing had to be installed before this session.")
set_runs(ph(s, 0).text_frame.paragraphs[0], "International Marketing Analytics")
set_runs(ph(s, 1).text_frame.paragraphs[0], "Set-up and registration")
set_runs(ph(s, 12).text_frame.paragraphs[0], "Session 1" + NB + "·" + NB + "WT" + NB + "2026/27")

# 2  Plan for today
s = add_slide("Titel und Inhalt", "Today: from zero to a working set-up",
              notes="Six steps. Start the GitHub Education application first, because approval can take a few days; "
                    "everything else runs while it is pending.")
stepper(s, 0.5, 1.35, 9.0, 0.6, STEPS, "Plan steps", size=11)
cw = (9.0 - GAP * 2) / 3
plan = [("LuLaptop", "What you need", ["Your laptop and charger", "Windows 10/11 or a recent macOS",
                                         "About 10" + NB + "GB free disk space", "Admin rights to install software"]),
        ("LuKeyRound", "Have at hand", ["Your WU e-mail and its password", "Your phone, for two-factor sign-in",
                                        "Your student ID or enrolment confirmation"]),
        ("LuUsers", "How we work", ["One step at a time, all together", "Check your neighbour's screen",
                                    "Stuck? Raise your hand, keep going with the next step"])]
for i, (ic, head, items) in enumerate(plan):
    card(s, 0.5 + i * (cw + GAP), 2.15, cw, 2.45, head, items, ic, f"Plan card {i + 1}", head_h=0.45)
callout(s, 4.8, 0.75, "LuCircleCheck", ("Goal: ", "by the end of today the check script prints \u201cready\u201d on every laptop."),
        "Goal", dark=True)

# ---------------------------------------------------------------- Part 1 -----
divider("Register your accounts", "Part 1 of 6" + NB + "·" + NB + "GitHub, GitHub Education, DataCamp",
        "Accounts first: they need e-mail confirmations and, for GitHub Education, an approval that can take days.")

# 3  The accounts
s = add_slide("Titel und Inhalt", "Three registrations",
              notes="All three are free for students. Use the WU e-mail address everywhere, so the student benefits apply.")
progress(s, 0)
tw3 = (9.0 - GAP * 2) / 3
accounts = [("LuGithub", "GitHub", ["Stores code and its history; hosts the course and group repositories"],
             ("github.com/signup", "https://github.com/signup")),
            ("LuGraduationCap", "GitHub Education", ["Free student benefits, including GitHub Copilot"],
             ("education.github.com/pack", "https://education.github.com/pack")),
            ("LuAward", "DataCamp", ["Online Python courses; four certificates count 20" + NB + "%"],
             ("Invitation link on Canvas", None))]
for i, (ic, head, lines, (where, url)) in enumerate(accounts):
    x = 0.5 + i * (tw3 + GAP)
    tile(s, x, 1.95, tw3, 2.75, ic, head, lines, f"Account {i + 1}")
    text(s, x + 0.15, 4.2, tw3 - 0.3, 0.4, [[link(where, url) if url else (where, {"bold": True, "col": ACC})]],
         f"Account {i + 1} where", size=12, anchor=MSO_ANCHOR.BOTTOM)
callout(s, 4.9, 0.65, "LuMail", ("Same e-mail everywhere: ", "your WU student address unlocks the free plans."), "Email")

# 4  GitHub account
s = add_slide("Titel und Inhalt", "GitHub account",
              notes="Two-factor authentication is required by GitHub for accounts that contribute code. "
                    "GitHub Mobile is the easiest second factor.")
progress(s, 0)
numbered(s, 0.5, 1.95, 5.6, [
    [("Open ", {}), link("github.com/signup", "https://github.com/signup")],
    ("WU e-mail: ", "sign up with your student address"),
    ("Username: ", "short and professional, e.g. anna-berger"),
    ("Verify ", "the code GitHub sends to your inbox"),
    ("Two-factor sign-in: ", "GitHub Mobile or an authenticator app")], "GitHub steps", row_h=0.6, gap=0.1)
card(s, 6.3, 1.95, 3.2, 3.4, "Why it matters", [
    "Your username appears on every commit you make",
    "A clean GitHub profile is part of your CV",
    "You need it for the group repository of the case study",
    "The free plan is all you need"], "LuIdCard", "GitHub why card", head_h=0.45)

# 5  GitHub Education and Copilot
s = add_slide("Titel und Inhalt", "GitHub Education and Copilot",
              notes="Approval is often quick but can take several days, and benefits can take up to 72 hours more to "
                    "appear. Check the Copilot Student plan status the week before term; it was paused once in 2026.")
progress(s, 0)
stepper(s, 0.5, 1.95, 9.0, 0.6, ["Add WU e-mail\vto GitHub", "Apply for\vbenefits", "Upload\vproof",
                                 "Wait for\vapproval", "Turn on\vCopilot"], "Education steps", size=12)
cw2 = (9.0 - GAP) / 2
card(s, 0.5, 2.75, cw2, 2.0, "Apply", [
    [("Go to ", {}), link("education.github.com/pack", "https://education.github.com/pack")],
    "Your WU address must be verified in GitHub's e-mail settings",
    "Proof: a photo of your student ID or enrolment confirmation"], "LuBadgeCheck", "Apply card", head_h=0.45)
card(s, 0.5 + cw2 + GAP, 2.75, cw2, 2.0, "After approval", [
    [("Turn on Copilot at ", {}), link("github.com/settings/copilot", "https://github.com/settings/copilot")],
    "Copilot Student is free while you study",
    "Until then, Copilot Free works with monthly limits"], "LuSparkles", "Approval card", head_h=0.45)
callout(s, 4.9, 0.65, "LuClock", ("Do this first: ", "approval can take a few days, so apply today, then carry on."),
        "Education", dark=True)

# 6  DataCamp
s = add_slide("Titel und Inhalt", "DataCamp classroom",
              notes="DataCamp for the Classroom gives students free premium access for six months. Nobody needs to pay.")
progress(s, 0)
numbered(s, 0.5, 1.95, 5.6, [
    ("Open ", "the invitation link on Canvas"),
    ("Sign up ", "with your WU e-mail, or log in"),
    ("Join ", "the classroom International Marketing Analytics"),
    ("Find ", "the four assigned courses under Assignments"),
    ("Upload ", "each certificate to Canvas by its deadline")], "DataCamp steps", row_h=0.6, gap=0.1)
box(s, 6.3, 1.95, 3.2, 3.4, LIGHT, "DataCamp facts")
facts = [("6", "months free premium access"), ("4", "courses with certificates"), ("20" + NB + "%", "of the final grade")]
for i, (fig, lab) in enumerate(facts):
    y = 2.1 + i * 1.07
    box(s, 6.45, y, 0.07, 0.9, ACC, f"DataCamp bar {i + 1}")
    text(s, 6.7, y, 2.7, 0.9, [[(fig, {"size": FIG, "bold": True, "col": NAVY, "head": True})], lab],
         f"DataCamp fact {i + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)

# ---------------------------------------------------------------- Part 2 -----
divider("Install the tools", "Part 2 of 6" + NB + "·" + NB + "Python, Positron, Quarto, GitHub Desktop, the course repository",
        "Show the overview first, so students know why each tool is there before they install it.")

# 7  How the pieces fit together
s = add_slide("Titel und Inhalt", "How the pieces fit together",
              notes="GitHub is the shared cloud copy. GitHub Desktop syncs it with a folder on the laptop. "
                    "Positron is where students work on that folder, using Python, Quarto and an AI assistant.")
cloud = box(s, 3.25, 1.35, 3.5, 0.6, ACC, "GitHub box")
icon(s, "LuCloud", "white", 3.4, 1.43, 0.44, "cloud")
text(s, 3.95, 1.35, 2.75, 0.6, [[("GitHub.com", {"bold": True, "col": WHITE})], [("course and group repositories", {"col": WHITE, "size": 11})]],
     "GitHub text", anchor=MSO_ANCHOR.MIDDLE, space=0)
arr = box(s, 4.82, 1.97, 0.36, 0.5, NAVY, "Sync arrow", shape=MSO_SHAPE.UP_DOWN_ARROW)
box(s, 0.5, 2.5, 9.0, 2.85, LIGHT, "Laptop area")
text(s, 0.65, 2.55, 3.0, 0.3, [[("Your laptop", {"bold": True, "col": NAVY, "size": 12})]], "Laptop label")
bw = 2.6
row1 = [("LuFolderGit2", "GitHub Desktop", "clone, pull and push"),
        ("LuFolderOpen", "Course folder", "data, code, requirements.txt"),
        ("LuMonitor", "Positron", "where you write and run code")]
xs = [0.75, 3.7, 6.65]
for i, (ic, head, sub) in enumerate(row1):
    box(s, xs[i], 2.95, bw, 0.85, WHITE_BG, f"Laptop box {i + 1}")
    icon(s, ic, "navy", xs[i] + 0.12, 3.15, 0.45, f"laptop {i + 1}")
    text(s, xs[i] + 0.7, 2.95, bw - 0.8, 0.85, [[(head, {"bold": True, "col": NAVY})], [(sub, {"size": 11})]],
         f"Laptop text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)
for i in range(2):
    text(s, xs[i] + bw, 2.95, 0.35, 0.85, [[("\u2194", {"bold": True, "col": ACC, "size": 22})]], f"Laptop arrow {i + 1}",
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
text(s, 0.75, 3.95, 8.5, 0.3, [[("Inside Positron you use", {"bold": True, "col": NAVY, "size": 12})]], "Inside label")
row2 = [("LuTerminal", "Python + packages", "in a private .venv folder"),
        ("LuFileText", "Quarto", "turns .qmd files into reports"),
        ("LuBot", "AI assistant", "writes and explains code")]
for i, (ic, head, sub) in enumerate(row2):
    box(s, xs[i], 4.3, bw, 0.85, WHITE_BG, f"Inside box {i + 1}")
    icon(s, ic, "navy", xs[i] + 0.12, 4.5, 0.45, f"inside {i + 1}")
    text(s, xs[i] + 0.7, 4.3, bw - 0.8, 0.85, [[(head, {"bold": True, "col": NAVY})], [(sub, {"size": 11})]],
         f"Inside text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)

# 8  Python from python.org
PY = "3.14.8"
s = add_slide("Titel und Inhalt", "Step 2: install Python " + PY,
              notes="Python 3.14.8 (30 September 2026) is the latest release; every course package installs and runs on it. "
                    "Windows and macOS do not come with Python, so it is always installed once. On Windows, python.org now "
                    "distributes Python through the Python install manager, which installs and updates Python itself. "
                    "Positron can also install Python for you: Command Palette, Python: Install Python via uv.")
progress(s, 1)
cw2 = (9.0 - GAP) / 2
for k, (osname, ic, steps, check) in enumerate([
        ("Windows", "LuMonitor",
         [[("Download: ", {"bold": True, "col": NAVY}), ("Python install manager", {})],
          "Install it with a double-click", "Start menu \u2192 Terminal: py install 3.14"], "py -3.14 --version"),
        ("macOS", "LuLaptop",
         [[("Download: ", {"bold": True, "col": NAVY}), ("macOS installer (Python 3.14.8)", {})],
          "Open the .pkg and click through", "Apple silicon and Intel"], "python3.14 --version")]):
    x = 0.5 + k * (cw2 + GAP)
    card(s, x, 1.95, cw2, 2.05, osname, steps, ic, f"{osname} card", head_h=0.45)
    code_block(s, x, 4.1, cw2, 0.62, check, f"{osname} check", size=11.5, caption=None)
box(s, 0.5, 4.87, 9.0, 0.68, LIGHT, "Python link box")
icon(s, "LuDownload", "navy", 0.72, 4.99, 0.42, "download")
text(s, 1.35, 4.87, 8.0, 0.68, [[("Both downloads: ", {"bold": True, "col": NAVY}),
                                 link("python.org/downloads", "https://www.python.org/downloads/")],
                                [("Or let Positron install it: Command Palette \u2192 Python: Install Python via uv", {"size": 12})]],
     "Python link text", anchor=MSO_ANCHOR.MIDDLE, space=0)

# 9  Positron, Quarto, GitHub Desktop
s = add_slide("Titel und Inhalt", "Step 2: install Positron, Quarto and GitHub Desktop",
              notes="Install Python first, then these three. Current Positron: 2026.09 (September 2026); it updates "
                    "monthly and offers updates itself. Its welcome page checks whether Python is ready. GitHub Desktop "
                    "brings its own Git.")
progress(s, 1)
tw3 = (9.0 - GAP * 2) / 3
tools = [("LuMonitor", "Positron", "positron.posit.co/download", "https://positron.posit.co/download",
          ["The editor for code, data and charts", "Version 2026.09, free", "Welcome page checks that Python is ready"]),
         ("LuFileText", "Quarto", "quarto.org/docs/get-started", "https://quarto.org/docs/get-started/",
          ["Turns text and code into reports and slides", "Check in a terminal: quarto --version"]),
         ("LuFolderGit2", "GitHub Desktop", "desktop.github.com", "https://desktop.github.com",
          ["Clone, pull and push with clicks", "Installs Git for you", "Sign in with your GitHub account"])]
for i, (ic, head, where, url, items) in enumerate(tools):
    x = 0.5 + i * (tw3 + GAP)
    card(s, x, 1.95, tw3, 3.0, head, items, ic, f"Tool card {i + 1}", head_h=0.45)
    text(s, x + 0.18, 4.45, tw3 - 0.33, 0.35, [[link(where, url)]], f"Tool link {i + 1}", size=12,
         anchor=MSO_ANCHOR.BOTTOM)
callout(s, 5.05, 0.5, "LuRefreshCw", ("Restart Positron ", "after installing Quarto, so it finds it."), "Restart")

# 10  Course repository
s = add_slide("Titel und Inhalt", "Step 3: get the course repository",
              notes="The course repository is public: anyone can clone it without sign-in or access rights. Students pull "
                    "updates before each session. The cloned folder is the project they open in Positron.")
progress(s, 2)
stepper(s, 0.5, 1.95, 9.0, 0.6, ["Copy the URL\v(below)", "GitHub Desktop:\vClone repository", "Pick a folder\vwithout spaces",
                                 "Positron:\vOpen Folder"], "Clone steps", size=12)
code_block(s, 0.5, 2.75, 4.4, 1.05, "https://github.com/arnefloh-wu/\n  international-marketing-analytics-teaching",
           "Repo URL code", size=10.5, caption="Course repository (public)")
text(s, 0.5, 3.9, 4.4, 0.85, [("Folder: ", "e.g. C:\\Users\\anna\\wu\\ima or ~/wu/ima. Avoid spaces, umlauts and "
                                           "OneDrive or iCloud folders.")], "Folder note", size=12)
words = [("Clone", "your own copy of a repository; a public one needs no sign-in"),
         ("Pull", "get the latest materials; do it before every session"),
         ("Commit and push", "save and upload your changes (group repository)")]
for i, (w, d) in enumerate(words):
    y = 2.75 + i * 0.68
    box(s, 5.1, y, 4.4, 0.58, LIGHT, f"Git word {i + 1}")
    box(s, 5.1, y, 0.07, 0.58, ACC, f"Git word bar {i + 1}")
    text(s, 5.32, y, 4.08, 0.58, [(w + ": ", d)], f"Git word text {i + 1}", size=12, anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.9, 0.65, "LuFolderOpen", ("In Positron: ", "File \u2192 Open Folder. The cloned folder is now your project."),
        "Open folder")

# 11  The project's Python: a .venv made by Positron
s = add_slide("Titel und Inhalt", "Step 4: set up the project's Python",
              notes="Python: Create Environment makes a .venv inside the open project folder with the chosen Python, offers "
                    "to install the packages from requirements.txt, and selects the new interpreter. The first install "
                    "takes a few minutes because PyMC is large. If packages were not installed, the console line does it, "
                    "on Windows and macOS alike.")
progress(s, 3)
stepper(s, 0.5, 1.95, 9.0, 0.6, ["Create\vEnvironment", "Venv", "Python\v3.14.8",
                                 "Install\vpackages", ".venv\vselected"], "Env steps", size=12)
card(s, 0.5, 2.75, 4.3, 2.05, "Positron then", [
    "Start: Command Palette \u2192 Python: Create Environment",
    "Creates .venv inside the project",
    "Installs all course packages",
    "Starts Python from .venv"], "LuFolderOpen", "Env card", head_h=0.45)
box(s, 4.95, 2.75, 4.55, 0.95, LIGHT, "Interpreter panel")
text(s, 5.1, 2.75, 1.6, 0.95, [[("Interpreter picker", {"bold": True, "col": NAVY, "size": 12})], [("top right", {"size": 11})]],
     "Interpreter head", anchor=MSO_ANCHOR.MIDDLE, space=0)
pill = box(s, 6.65, 3.02, 2.7, 0.42, WHITE_BG, "Interpreter pill", shape=MSO_SHAPE.ROUNDED_RECTANGLE, line=ACC)
text(s, 6.72, 3.02, 2.6, 0.42, [[("Python 3.14.8 (.venv) \u25be", {"font": MONO, "col": NAVY, "size": 11})]], "Pill text",
     anchor=MSO_ANCHOR.MIDDLE)
code_block(s, 4.95, 3.85, 4.55, 0.95, "%pip install -r requirements.txt", "Env console", size=11,
           caption="Packages missing? Positron console")
callout(s, 4.95, 0.6, "LuRefreshCw", ("Once per project: ", "Positron remembers the .venv and starts it whenever you open "
                                                         "the folder."), "Once note")

# 12  The check
s = add_slide("Titel und Inhalt", "Step 5: run the check",
              notes="The script lives in setup/check_setup.py. Every line marked !! says what to fix. test_stack.qmd "
                    "then runs polars, plotnine and statsmodels on the course data and renders with Quarto. "
                    "Alternatively open the file and press the Run button at the top right of the editor.")
progress(s, 4)
code_block(s, 0.5, 1.95, 9.0, 0.75, "%run setup/check_setup.py", "Check command", size=11,
           caption="Positron console (Windows and macOS)")
out = """Packages
  [ok] polars           1.44.2     data wrangling
  [ok] plotnine         0.15.8     charts
  [ok] great_tables     1.0.0      tables
  [ok] statsmodels      0.15.0     regression
  ...
ready"""
code_block(s, 0.5, 2.85, 5.6, 2.1, out, "Check output", caption="Example output (shortened)")
card(s, 6.3, 2.85, 3.2, 2.1, "Reading it", [
    "[ok]: in place",
    "[!!]: the line says what to fix",
    "Ends with \u201cready\u201d: done"], "LuCircleCheck", "Check card", head_h=0.45)
callout(s, 5.05, 0.5, "LuPlay", ("Next: ", "the full test with test_stack.qmd (next slide)."), "Run button")

# 13  The stack test: test_stack.qmd
s = add_slide("Titel und Inhalt", "Step 5: test the whole stack",
              notes="test_stack.qmd sits at the top of the course repository. Open it and press Preview: Quarto runs the "
                    "three cells with the project's .venv and shows a report with a table, a chart and the regression "
                    "coefficients. The text under it says the model explains 43 % of the weekly variation.")
code_block(s, 0.5, 1.35, 4.5, 3.05, """# polars: sum 2025 revenue by country
import polars as pl

sales = pl.read_csv(
    "data/mmm/alpenglow_weekly.csv",
    try_parse_dates=True)
summary = (
    sales
    .filter(pl.col("week").dt.year() == 2025)
    .group_by("country")
    .agg(pl.col("revenue_eur_k").sum())
    .sort("revenue_eur_k", descending=True)
)
summary""", "Test polars", size=10, caption="test_stack.qmd · cell 1")
code_block(s, 5.15, 1.35, 4.35, 1.55, """# plotnine: weekly sales, AT and DE
from plotnine import ggplot, aes, geom_line
two = sales.filter(
    pl.col("country").is_in(["AT", "DE"]))
ggplot(two, aes("week", "sales_units_k",
                color="country")) + geom_line()""", "Test plotnine", size=10, caption="cell 2")
code_block(s, 5.15, 3.0, 4.35, 2.0, """# statsmodels: regression for Austria
import statsmodels.formula.api as smf
at = (sales.filter(pl.col("country") == "AT")
      .to_pandas())
model = smf.ols(
    "sales_units_k ~ price_eur + spend_tv_k"
    " + spend_paid_search_k", data=at).fit()
model.params.round(2)""", "Test statsmodels", size=10, caption="cell 3")
box(s, 0.5, 4.5, 4.5, 0.5, LIGHT, "Test result box")
text(s, 0.65, 4.5, 4.3, 0.5, [("Result: ", "a table, a chart and four coefficients")], "Test result", size=12,
     anchor=MSO_ANCHOR.MIDDLE)
callout(s, 5.1, 0.45, "LuPlay", ("Run it: ", "open test_stack.qmd in Positron and press Preview (Ctrl/Cmd + Shift + K)."),
        "Test run")

# 14  AI assistant
s = add_slide("Titel und Inhalt", "Step 6: connect your AI assistant",
              notes="Posit Assistant replaced Positron Assistant and Databot in Positron 2026.07; older videos show the "
                    "old menus. GitHub Copilot gives chat and code completions and is the cheapest provider for students; "
                    "in Positron it is still marked Preview.")
progress(s, 5)
numbered(s, 0.5, 1.95, 5.0, [
    ("Command Palette: ", "Configure Language Model Providers"),
    ("Choose GitHub Copilot ", "and sign in with GitHub"),
    ("Open the chat: ", "View: Show Posit Assistant")], "AI steps", row_h=0.62, gap=0.1)
rows = [("GitHub Copilot", "chat and completions; free with Copilot Student or Copilot Free"),
        ("Posit AI Pass", "chat and completions; about USD" + NB + "20 a month"),
        ("Anthropic API key", "chat; pay as you go")]
box(s, 5.7, 1.95, 3.8, 2.06, LIGHT, "Options panel")
text(s, 5.9, 2.0, 3.4, 0.35, [[("Providers", {"bold": True, "col": NAVY})]], "Options head")
text(s, 5.9, 2.35, 3.5, 1.6, [(a + ": ", b) for a, b in rows], "Options text", size=12, space=4)
callout(s, 4.25, 1.2, "LuShieldCheck", ("Our rule: ", "the AI writes, you check. Run the code, read the output and keep "
                                                   "a short prompt log for each submission."), "AI rule", dark=True)

# ---------------------------------------------------------------- Part 3 -----
divider("How Positron works", "Part 3 of 6" + NB + "·" + NB + "panes, running code, projects, shortcuts, Posit Assistant",
        "Positron 2026.09. A five-minute tour with the live application next to the slides works best.")

# 15  Positron at a glance: a schematic window (names as in the Positron 2026.09 docs)
s = add_slide("Titel und Inhalt", "Positron at a glance",
              notes="Names as in the Positron documentation: Activity Bar and Primary Side Bar on the left, Editor in "
                    "the middle with the Panel (Console, Terminal) below, Secondary Side Bar on the right with the "
                    "Session pane (Variables, Plots). The Top Bar holds the project switcher and the Interpreter picker.")
box(s, 0.5, 1.35, 9.0, 0.36, NAVY, "Top Bar")
text(s, 0.65, 1.35, 3.0, 0.36, [[("New ▾   Open ▾", {"col": WHITE, "size": 11})]], "Top Bar left",
     anchor=MSO_ANCHOR.MIDDLE)
box(s, 5.0, 1.39, 1.65, 0.28, WHITE_BG, "Project switcher", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 5.05, 1.39, 1.55, 0.28, [[("case-study ▾", {"col": NAVY, "size": 10.5})]], "Project switcher text",
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
box(s, 6.75, 1.39, 2.65, 0.28, WHITE_BG, "Window pill", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 6.8, 1.39, 2.55, 0.28, [[("Python 3.14.8 (.venv) ▾", {"font": MONO, "col": NAVY, "size": 10.5})]],
     "Window pill text", anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
box(s, 0.5, 1.71, 0.3, 3.84, ACC, "Activity bar")
panes = [  # x, y, w, h, name, description, sample
    (0.84, 1.75, 1.86, 3.8, "Explorer", "files of the open folder", "data/\nanalysis.py\nreport.qmd\nrequirements.txt"),
    (2.74, 1.75, 3.86, 2.08, "Editor", "write .py and .qmd files", "# %%\nsales = pl.read_csv(...)\nsales.head()"),
    (2.74, 3.87, 3.86, 1.68, "Console and Terminal", "the Panel: code runs, results print", ">>> sales.height\n936"),
    (6.64, 1.75, 2.86, 1.73, "Variables", "Session pane: what is in memory", None),
    (6.64, 3.52, 2.86, 2.03, "Plots", "Session pane: your charts", None),
]
for i, (x, y, w, h, head, desc, sample) in enumerate(panes):
    box(s, x, y, w, h, LIGHT, f"Pane {head}")
    badge(s, x + 0.1, y + 0.1, i + 1, f"Pane number {i + 1}", d=0.3, fill=ACC)
    text(s, x + 0.5, y + 0.08, w - 0.6, 0.6, [[(head, {"bold": True, "col": NAVY, "size": 12})], [(desc, {"size": 11})]],
         f"Pane text {i + 1}", space=0)
    if sample:
        text(s, x + 0.15, y + 0.85, w - 0.3, h - 0.95,
             [[(ln, {"font": MONO, "col": NAVY, "size": 11})] for ln in sample.split("\n")], f"Pane sample {i + 1}", space=0)
vars_ = [("sales", "936 × 18"), ("summary", "6 × 3"), ("model", "OLS results")]
for j, (n, v) in enumerate(vars_):
    text(s, 6.79, 2.45 + j * 0.3, 2.6, 0.3, [[(n, {"font": MONO, "col": NAVY, "size": 11}), ("   " + v, {"size": 11})]],
         f"Variable {j + 1}", space=0)
pic = s.shapes.add_picture(str(FIGS / "plotnine_example.png"), I(6.79), I(4.18), I(2.56), I(1.3653))
pic.name = "Plot thumbnail"
pic._element.nvPicPr.cNvPr.set("descr", "Example line chart of weekly sales for Austria and Germany")

# 16  From code to result
s = add_slide("Titel und Inhalt", "From code to result",
              notes="Show it live: write one line, press Ctrl+Enter, point at the console, the Variables pane and the plot. "
                    "%view df opens a table in the Data Explorer from the console.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["Write code\vin the editor", "Ctrl/Cmd\v+ Enter", "It runs in\vthe console",
                                 "Objects in\vVariables", "Charts in\vPlots"], "Run steps", size=12)
cw2 = (9.0 - GAP) / 2
card(s, 0.5, 2.15, cw2, 2.3, "Run code", [
    "Ctrl/Cmd + Enter: the selection or current statement",
    "Ctrl/Cmd + Shift + Enter: the whole file, or the current cell",
    "# %% starts a cell in a .py file"], "LuPlay", "Run card", head_h=0.45)
card(s, 0.5 + cw2 + GAP, 2.15, cw2, 2.3, "Look at results", [
    "Variables: every object, its type and size",
    "Data Explorer: click a table, or type %view sales",
    "Plots: earlier charts, zoom, save as PNG"], "LuEye", "Results card", head_h=0.45)
callout(s, 4.65, 0.9, "LuSquareTerminal", ("Console or terminal? ", "The console speaks Python. The terminal speaks to "
                                                                  "your computer: pip, git and quarto commands go there."),
        "Console", dark=True)

# 17  Projects: one folder for everything
s = add_slide("Titel und Inhalt", "Projects in Positron: one folder for everything",
              notes="In Positron a project is simply a folder opened with File > Open Folder (a workspace). Positron finds "
                    "the .venv at the folder root and remembers the interpreter for that folder. Open folders, not single files.")
tree = """case-study/
├── .venv/            private Python + packages
├── .git/             version history
├── .gitignore        what Git leaves out
├── data/             raw data, never edit by hand
├── analysis.py       code, split into # %% cells
├── report.qmd        text, code and results
└── requirements.txt  packages and versions"""
code_block(s, 0.5, 1.35, 5.4, 2.75, tree, "Project tree", size=11, caption="A project is a folder")
prow = [("Open the folder, ", "not single files: File → Open Folder"),
        ("Positron remembers ", "the interpreter and open files per folder"),
        ("Relative paths: ", "data/sales.csv works on every laptop"),
        ("Switch projects ", "with the project switcher, top right")]
for i, para in enumerate(prow):
    y = 1.35 + i * (0.62 + 0.09)
    box(s, 6.1, y, 3.4, 0.62, LIGHT, f"Project row {i + 1}")
    box(s, 6.1, y, 0.07, 0.62, ACC, f"Project bar {i + 1}")
    text(s, 6.3, y, 3.12, 0.62, [para], f"Project text {i + 1}", size=11.5, anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.3, 1.25, "LuFolderGit2", (".venv stays on your laptop: ", ".gitignore keeps it out of GitHub. "
                                       "requirements.txt travels instead, so your group rebuilds the same environment "
                                       "with one command."), "Venv note", dark=True)

# 18  New project from a template
s = add_slide("Titel und Inhalt", "Start a new project from a template",
              notes="New Folder from Template sets up the folder, a .venv, Git and a running session in one dialog. "
                    "Open it from the New menu (top left), the project switcher or the Command Palette "
                    "(Workspaces: New Folder from Template).")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["New Folder\vfrom Template", "Python\vProject", "Name and\vlocation",
                                 "Python 3.14\v+ venv", "Create"], "Template steps", size=12)
card(s, 0.5, 2.15, 4.3, 2.35, "Positron sets up", [
    "The folder with a .venv inside",
    "Git: .git and a .gitignore",
    "A running Python session",
    "An empty file to start with"], "LuFolderOpen", "Template card", head_h=0.45)
code_block(s, 4.95, 2.15, 4.55, 2.35,
           "%pip install polars plotnine great-tables\n\n%pip freeze > requirements.txt",
           "Template code", size=11, caption="Then, in the Positron console")
text(s, 5.1, 3.55, 4.3, 0.9, [[("Line 1 installs packages, line 2 writes their versions to requirements.txt.",
                                {"col": WHITE, "size": 11})]], "Template code note")
callout(s, 4.7, 0.85, "LuSearch", ("Where: ", "New ▾ (top left), the project switcher, or Command Palette → "
                                              "Workspaces: New Folder from Template."), "Template where")

# 19  Shortcuts
s = add_slide("Titel und Tabelle", "Shortcuts worth knowing",
              notes="Positron-specific shortcuts from the Positron documentation, plus the Quarto preview. On macOS, Cmd "
                    "replaces Ctrl except where noted. The Command Palette finds every other command by name.")
rows = [("Action", "Windows", "macOS"),
        ("Run selection or current statement", "Ctrl + Enter", "Cmd + Enter"),
        ("Run the file or current cell", "Ctrl + Shift + Enter", "Cmd + Shift + Enter"),
        ("Insert a code cell (# %%)", "Ctrl + Shift + I", "Cmd + Shift + I"),
        ("Restart the Python session", "Ctrl + Shift + 0", "Cmd + Shift + 0"),
        ("Clear the console", "Ctrl + L", "Ctrl + L"),
        ("Preview a Quarto document", "Ctrl + Shift + K", "Cmd + Shift + K"),
        ("Command Palette", "Ctrl + Shift + P", "Cmd + Shift + P"),
        ("Help for the word under the cursor", "F1", "F1"),
        ("Accept an AI suggestion", "Tab", "Tab")]
gf = ph(s, 1).insert_table(len(rows), 3)
tbl = gf.table
for i, w in enumerate([4.0, 2.5, 2.5]):
    tbl.columns[i].width = I(w)
gf.width = I(9.0)
for r_i, row in enumerate(rows):
    for c_i, txt in enumerate(row):
        cell = tbl.cell(r_i, c_i)
        p = cell.text_frame.paragraphs[0]
        set_runs(p, txt)
        for r in p.runs:
            r.font.size = Pt(HEAD if r_i == 0 else BODY)
            if r_i > 0 and c_i > 0:
                r.font.name = MONO
        cell.margin_top = cell.margin_bottom = Emu(45000)

# 20  Posit Assistant: what it is
s = add_slide("Titel und Inhalt", "Posit Assistant: the AI inside Positron",
              notes="Posit Assistant has been Positron's built-in AI since 2026.07, replacing Positron Assistant and "
                    "Databot. It uses session context (variable names and types, plots, console history). Permission "
                    "modes: Normal asks before acting, Restricted allows less, YOLO runs without asking; we use Normal.")
tw3 = (9.0 - GAP * 2) / 3
pa = [("LuEye", "What it sees", ["Your open files and project", "Loaded data, variables and plots", "Console history"]),
      ("LuBot", "What it does", ["Explains, writes and fixes code", "Runs code after you approve",
                                 "Fix and Explain on any error"]),
      ("LuSettings", "How you steer it", ["/plan: a plan before any code", "@file: point it to a file",
                                          "Permission mode: keep Normal"])]
for i, (ic, head, items) in enumerate(pa):
    card(s, 0.5 + i * (tw3 + GAP), 1.35, tw3, 2.35, head, items, ic, f"Assistant card {i + 1}", head_h=0.45)
text(s, 0.5, 3.85, 9.0, 0.3, [[("Open it", {"bold": True, "col": NAVY})]], "Open label")
code_block(s, 0.5, 4.2, 4.4, 0.6, "View: Show Posit Assistant", "Open command", size=11.5)
text(s, 5.05, 4.2, 4.45, 0.6, [[("Command Palette, or the Assistant icon in the Activity Bar", {"size": 12})]],
     "Open note", anchor=MSO_ANCHOR.MIDDLE)
text(s, 0.5, 4.95, 9.0, 0.6, [[("Memory: ", {"bold": True, "col": NAVY}),
                               ("an AGENTS.md file in your project tells it your conventions, for example "
                                "“use polars and plotnine”.", {})]], "Memory note", size=12, anchor=MSO_ANCHOR.MIDDLE)

# 21  Working with AI
s = add_slide("Titel und Inhalt", "Working with AI in Positron",
              notes="Export a conversation (Markdown) and attach it as the prompt log. Posit's FAQ: prompts and session "
                    "information such as variable names and types go to the model provider; row-level data only when "
                    "you ask for it.")
cw2 = (9.0 - GAP) / 2
card(s, 0.5, 1.35, cw2, 1.85, "Completions: ghost text", [
    "Grey suggestions appear as you type",
    "Tab accepts, Ctrl/Cmd + → word by word",
    "Esc or keep typing to dismiss"], "LuSparkles", "Ghost card", head_h=0.45)
card(s, 0.5 + cw2 + GAP, 1.35, cw2, 1.85, "Chat: Posit Assistant", [
    "Ask in plain English, one step at a time",
    "Check every result it reports",
    "Export the chat: your prompt log"], "LuMessagesSquare", "Assistant chat card", head_h=0.45)
text(s, 0.5, 3.35, 9.0, 0.3, [[("Good prompts", {"bold": True, "col": NAVY})]], "Prompt label")
code_block(s, 0.5, 3.7, 9.0, 0.8,
           '"Sum revenue by country for 2025 with polars and sort it."\n'
           '"Explain this error in two sentences, then fix it."', "Prompt code", size=11.5)
callout(s, 4.7, 0.85, "LuShieldCheck", ("Privacy: ", "prompts, variable names and types go to the model provider; rows of "
                                                     "data only if you ask. Never paste personal data."), "Privacy")

# ---------------------------------------------------------------- Part 4 -----
divider("Work with GitHub Desktop", "Part 4 of 6" + NB + "·" + NB + "the window, the everyday workflow, your group project",
        "GitHub Desktop is the bridge between the folder on the laptop and GitHub. Show it live with the course repository.")

# 22  GitHub Desktop at a glance
s = add_slide("Titel und Inhalt", "GitHub Desktop at a glance",
              notes="Names as in GitHub Desktop: the toolbar shows Current repository, Current branch and the sync button, "
                    "which reads Fetch origin, Pull origin or Push origin depending on what is waiting. The Changes tab "
                    "lists edited files; the diff on the right shows removed lines in red and added lines in green.")
box(s, 0.5, 1.35, 5.8, 0.6, NAVY, "GD toolbar")
segs = [(0.6, 2.35, "Current repository", "ima-teaching ▾"), (3.0, 1.5, "Current branch", "main ▾"),
        (4.55, 1.7, "Fetch origin", "↻ now")]
for j, (x, w, a, b) in enumerate(segs):
    text(s, x + 0.35, 1.35, w - 0.35, 0.6, [[(a, {"col": WHITE, "size": 10.5})], [(b, {"col": WHITE, "bold": True, "size": 10.5})]],
         f"GD seg {j + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)
    badge(s, x, 1.5, j + 1, f"GD badge {j + 1}", d=0.3, fill=ACC)
box(s, 0.5, 2.0, 2.4, 2.95, LIGHT, "GD left")
text(s, 0.95, 2.05, 1.9, 0.35, [[("Changes (2)", {"bold": True, "col": NAVY, "size": 11}), ("   History", {"size": 11})]],
     "GD tabs", anchor=MSO_ANCHOR.MIDDLE)
badge(s, 0.58, 2.07, 4, "GD badge 4", d=0.3, fill=ACC)
for j, f in enumerate(["analysis.py", "report.qmd"]):
    y = 2.5 + j * 0.38
    box(s, 0.65, y + 0.07, 0.2, 0.2, ACC, f"GD check {j + 1}")
    text(s, 0.95, y, 1.9, 0.34, [[(f, {"font": MONO, "col": NAVY, "size": 11})]], f"GD file {j + 1}", anchor=MSO_ANCHOR.MIDDLE)
box(s, 0.6, 3.45, 2.2, 0.42, WHITE_BG, "GD summary")
text(s, 0.68, 3.45, 2.1, 0.42, [[("Add Austria sales chart", {"size": 10.5})]], "GD summary text", anchor=MSO_ANCHOR.MIDDLE)
btn = box(s, 0.6, 4.0, 2.2, 0.42, ACC, "GD commit", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 0.6, 4.0, 2.2, 0.42, [[("Commit to main", {"bold": True, "col": WHITE, "size": 11})]], "GD commit text",
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
badge(s, 0.58, 4.5, 5, "GD badge 5", d=0.3, fill=ACC)
text(s, 0.95, 4.45, 1.9, 0.4, [[("summary, then commit", {"size": 10.5})]], "GD commit note", anchor=MSO_ANCHOR.MIDDLE)
box(s, 2.95, 2.0, 3.35, 2.95, WHITE_BG, "GD diff", line=ACC)
badge(s, 3.03, 2.07, 6, "GD badge 6", d=0.3, fill=ACC)
text(s, 3.4, 2.05, 2.8, 0.35, [[("report.qmd", {"font": MONO, "bold": True, "col": NAVY, "size": 11})]], "GD diff head",
     anchor=MSO_ANCHOR.MIDDLE)
for j, (sign, code, fill, ink) in enumerate([(" ", "at = sales.filter(...)", None, None),
                                             ("-", "at.head()", "FBE3E3", "9F1D1D"),
                                             ("+", "ggplot(at, aes(\"week\",", "E3F4E8", "146C2E"),
                                             ("+", "  \"sales_units_k\"))", "E3F4E8", "146C2E"),
                                             ("+", "  + geom_line()", "E3F4E8", "146C2E")]):
    y = 2.55 + j * 0.36
    if fill:
        box(s, 3.0, y, 3.25, 0.34, fill, f"GD diff bg {j + 1}")
    text(s, 3.08, y, 3.15, 0.34, [[(sign + " " + code, {"font": MONO, "size": 10.5, "col": ink or INK})]],
         f"GD diff line {j + 1}", anchor=MSO_ANCHOR.MIDDLE)
legend = [("Current repository", "which project you work on"), ("Current branch", "main is all we need"),
          ("Fetch / Pull / Push origin", "sync with GitHub"),
          ("Changes", "files edited since last commit"), ("Summary + Commit", "save a snapshot with a message"),
          ("Diff", "red removed, green added")]
for j, (a, b) in enumerate(legend):
    y = 1.35 + j * 0.61
    box(s, 6.45, y, 3.05, 0.55, LIGHT, f"GD legend {j + 1}")
    badge(s, 6.55, y + 0.12, j + 1, f"GD legend badge {j + 1}", d=0.3, fill=ACC)
    text(s, 6.95, y, 2.5, 0.55, [[(a, {"bold": True, "col": NAVY, "size": 11})], [(b, {"size": 10.5})]],
         f"GD legend text {j + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)
text(s, 0.5, 5.05, 9.0, 0.45, [[("Course repository: ", {"bold": True, "col": NAVY}),
                               ("you only pull. Your own work goes in your files or in your group repository.", {})]],
     "GD note", size=12, anchor=MSO_ANCHOR.MIDDLE)

# 23  The everyday workflow
s = add_slide("Titel und Inhalt", "The everyday workflow",
              notes="Pull before you start, commit small steps, push when you stop. A merge conflict happens when two people "
                    "change the same lines; GitHub Desktop lists the files, and Posit Assistant can explain the markers.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["Fetch, then\vPull origin", "Work in\vPositron", "Review\vChanges",
                                 "Summary +\vCommit", "Push\vorigin"], "Flow steps", size=12)
tw3 = (9.0 - GAP * 2) / 3
flow = [("LuRefreshCw", "Course repository", ["Pull before every session", "Read-only for you: copy files into your own folder before editing"]),
        ("LuUsers", "Group repository", ["Pull, work, commit, push", "One person per file where you can", "Push before others start"]),
        ("LuGitBranch", "Good commits", ["Small steps, often", "Summary says what changed: “Add AT sales chart”",
                                         "Push when you stop"])]
for i, (ic, head, items) in enumerate(flow):
    card(s, 0.5 + i * (tw3 + GAP), 2.15, tw3, 2.45, head, items, ic, f"Flow card {i + 1}", head_h=0.45)
callout(s, 4.75, 0.8, "LuTriangleAlert", ("Merge conflict? ", "Open the file, keep the lines you want, delete the conflict "
                                                            "markers (<<< === >>>), then commit and push."), "Conflict",
        dark=True)

# 24  Group project
s = add_slide("Titel und Inhalt", "Your case study as a shared project",
              notes="GitHub in the browser is where the repository is created and the group is invited; GitHub Desktop "
                    "keeps each laptop's copy in sync; Positron is where the work happens.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["github.com:\vnew repository", "Invite\vthe group", "Desktop:\vclone",
                                 "Positron:\vOpen Folder", "Create\v.venv"], "Group steps", size=12)
tw3 = (9.0 - GAP * 2) / 3
groups = [("LuGlobe", "github.com", ["One member creates the repository: Python .gitignore, README",
                                                 "Settings → Collaborators: invite the group"]),
          ("LuFolderGit2", "GitHub Desktop", ["Pull before you start", "Commit small steps with a clear message",
                                              "Push when you stop"]),
          ("LuMonitor", "Positron", ["Open the cloned folder", "Create Environment from requirements.txt (Step 4)",
                                     "Work, save, then back to Desktop"])]
for i, (ic, head, items) in enumerate(groups):
    card(s, 0.5 + i * (tw3 + GAP), 2.15, tw3, 2.45, head, items, ic, f"Group card {i + 1}", head_h=0.45)
callout(s, 4.8, 0.75, "LuUsers", ("Fewer conflicts: ", "pull first, push often, and one person per file where you can."),
        "Group rule", dark=True)

# ---------------------------------------------------------------- Part 5 -----
divider("Write reports with Quarto", "Part 5 of 6" + NB + "·" + NB + "how it works, the YAML header, code cells, output formats",
        "All labs and the case study report are Quarto documents. One file holds text, code and results.")

# 25  How Quarto works
s = add_slide("Titel und Inhalt", "Quarto: text, code and results in one file",
              notes="Quarto runs the Python cells through Jupyter, writes the results into Markdown and lets Pandoc turn it "
                    "into HTML, PDF, Word or slides. Since Positron 2026.08 cell output also shows inline in the editor, "
                    "with Fix and Explain buttons on errors.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["report.qmd", "Python runs\vthe cells", "Markdown\v+ results", "Pandoc\vconverts",
                                 "HTML, PDF,\vWord, slides"], "Quarto steps", size=12)
code_block(s, 0.5, 2.1, 5.0, 2.85, """---
title: "Alpenglow: sales in Austria"
author: "Anna Berger"
format: html
---

## Weekly sales

```{python}
at = sales.filter(pl.col("country") == "AT")
at.head()
```

Austria is our smallest market.""", "Anatomy code", size=10, caption="report.qmd")
parts = [("1  YAML header: ", "settings between the two --- lines"), ("2  Markdown: ", "headings (##), **bold**, lists, links"),
         ("3  Code cells: ", "```{python} … ``` run Python; the output lands under the cell")]
for i, para in enumerate(parts):
    y = 2.1 + i * 0.98
    box(s, 5.65, y, 3.85, 0.88, LIGHT, f"Anatomy row {i + 1}")
    box(s, 5.65, y, 0.07, 0.88, ACC, f"Anatomy bar {i + 1}")
    text(s, 5.85, y, 3.55, 0.88, [para], f"Anatomy text {i + 1}", size=12, anchor=MSO_ANCHOR.MIDDLE)
callout(s, 5.05, 0.5, "LuEye", ("Preview: ", "Ctrl/Cmd + Shift + K in Positron.   Render: quarto render report.qmd"),
        "Quarto preview")

# 26  The YAML header
s = add_slide("Titel und Inhalt", "The YAML header: settings for the whole document",
              notes="YAML is key: value pairs. Nesting is done by indentation, two spaces per level, never tabs. Options for "
                    "one format sit under that format's name.")
code_block(s, 0.5, 1.35, 4.3, 3.35, """---
title: "Alpenglow: sales in Austria"
author: "Anna Berger"
date: today
format:
  html:
    toc: true
    code-fold: true
execute:
  warning: false
---""", "YAML code", size=11.5, caption="Top of report.qmd")
keys = [("title, author", "shown at the top"), ("date: today", "the day you render"),
        ("format: html", "the output; its options indented below"), ("toc: true", "table of contents"),
        ("code-fold: true", "code hidden behind a “Code” button"), ("warning: false", "no warnings in the output")]
for i, (k, v) in enumerate(keys):
    y = 1.35 + i * 0.56
    box(s, 4.95, y, 4.55, 0.5, LIGHT, f"YAML row {i + 1}")
    text(s, 5.1, y, 2.15, 0.5, [[(k, {"font": MONO, "bold": True, "col": NAVY, "size": 11})]], f"YAML key {i + 1}",
         anchor=MSO_ANCHOR.MIDDLE)
    text(s, 7.25, y, 2.2, 0.5, [[(v, {"size": 11})]], f"YAML value {i + 1}", anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.85, 0.7, "LuTriangleAlert", ("Indentation matters: ", "two spaces per level, no tabs, and a space after "
                                                                 "every colon."), "YAML rule", dark=True)

# 27  Code cells
s = add_slide("Titel und Inhalt", "Code cells: options and numbers in the text",
              notes="Cell options start with #| at the top of a cell. A label starting with fig- makes the chart a numbered "
                    "figure that @fig-sales refers to. Inline code puts a computed number into the sentence, so the text "
                    "updates when the data change.")
code_block(s, 0.5, 1.35, 5.3, 2.75, """```{python}
#| label: fig-sales
#| fig-cap: "Weekly sales in Austria"
#| echo: false
ggplot(at, aes("week", "sales_units_k")) + geom_line()
```

The chart covers `{python} at.height` weeks (@fig-sales).""", "Cell code", size=10.5, caption="Inside report.qmd")
opts = [("#| label: fig-sales", "names the cell; fig- makes it a figure"), ("#| fig-cap:", "the caption under the chart"),
        ("#| echo: false", "show the result, hide the code"), ("`{python} …`", "a computed number in the text"),
        ("@fig-sales", "“Figure 1”, with a link")]
for i, (k, v) in enumerate(opts):
    y = 1.35 + i * 0.56
    box(s, 5.95, y, 3.55, 0.5, LIGHT, f"Opt row {i + 1}")
    text(s, 6.08, y, 3.4, 0.5, [[(k, {"font": MONO, "bold": True, "col": NAVY, "size": 10.5})], [(v, {"size": 10.5})]],
         f"Opt text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)
callout(s, 4.3, 1.2, "LuLightbulb", ("Why it matters: ", "when the data change, you render again and every chart, table "
                                                       "and number in the text updates. No copy and paste into Word."),
        "Cell why", dark=True)

# 28  Output formats
s = add_slide("Titel und Inhalt", "One source, many output formats",
              notes="The four pictures are the same report.qmd rendered four ways (slides/quarto_demo/report.qmd). Typst "
                    "makes PDFs without installing LaTeX. Positron's Preview shows the first format listed.")
thumbs = [("html", 1500 / 1125, "html", "web page (default)"), ("revealjs", 1500 / 938, "revealjs", "slides in the browser"),
          ("pdf", 680 / 880, "typst", "PDF, no LaTeX needed"), ("docx", 680 / 880, "docx", "Word, to edit further")]
th = 1.8
widths = [th * r for _, r, _, _ in thumbs]
gap = (9.0 - sum(widths)) / 3
x = 0.5
for f, r, key, desc in thumbs:
    w = th * r
    pic = s.shapes.add_picture(str(FIGS / f"quarto_{f}.png"), I(x), I(1.35), I(w), I(th))
    pic.name = f"Quarto {key} thumbnail"
    pic.line.color.theme_color = ACC
    pic.line.width = Pt(0.75)
    pic._element.nvPicPr.cNvPr.set("descr", f"The demo report rendered as {desc}")
    text(s, x, 3.2, w + 0.1, 0.5, [[(key, {"font": MONO, "bold": True, "col": NAVY, "size": 11})], [(desc, {"size": 10.5})]],
         f"Quarto {key} label", space=0)
    x += w + gap
code_block(s, 0.5, 3.85, 4.4, 1.7, """format:
  html: default
  revealjs: default
  typst: default
  docx: default""", "Formats code", size=11, caption="YAML: several formats")
code_block(s, 5.05, 3.85, 4.45, 1.7, """quarto render report.qmd
quarto render report.qmd --to docx""", "Render code", size=11, caption="Terminal: all formats, or one")
text(s, 5.2, 4.9, 4.2, 0.6, [[("Also: pptx, dashboard, pdf (LaTeX)", {"col": WHITE, "size": 11})]], "Formats also")

# ---------------------------------------------------------------- Part 6 -----
divider("Python packages for this course", "Part 6 of 6" + NB + "·" + NB + "install and load; polars, plotnine, Great Tables, statsmodels",
        "Install and load first, then one slide per package with code that runs on the course data.")

# 29  Install packages: code for Windows and macOS
s = add_slide("Titel und Inhalt", "Install packages: three ways",
              notes="All three install into the course .venv. The terminal lines call the Python inside .venv directly, "
                    "so no activation is needed. %pip in the Positron console installs into the running session; "
                    "restart the session afterwards if Positron asks.")
def two(prefix):
    a, b = prefix + " -m pip install -r requirements.txt", prefix + " -m pip install polars"
    return f"{a.ljust(58)}# all course packages\n{b.ljust(58)}# one package"


code_block(s, 0.5, 2.15, 9.0, 0.95, two(".venv\\Scripts\\python"),
           "Install win", size=11, caption="2  Windows: Positron terminal")
code_block(s, 0.5, 3.22, 9.0, 0.95, two(".venv/bin/python"),
           "Install mac", size=11, caption="3  macOS: Positron terminal")
code_block(s, 0.5, 1.35, 9.0, 0.7, "%pip install polars plotnine great-tables", "Install console", size=11,
           caption="1  Windows and macOS: Positron console (easiest)")
callout(s, 4.35, 1.2, "LuPackage", ("Install name and import name can differ: ",
                                    "pip install great-tables → import great_tables; scikit-learn → sklearn; "
                                    "pymc-marketing → pymc_marketing."), "Names")

# 30  Packages pane
s = add_slide("Titel und Inhalt", "The Packages pane: install without code",
              notes="The Packages pane arrived in Positron 2026.07. It works on the active session's environment, uses the "
                    "workspace requirements.txt to keep versions consistent, flags outdated packages and known security "
                    "issues, and prompts for a session restart after changes.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["Packages icon\v(Activity Bar)", "Install\vPackage", "Search name,\vpick version",
                                 "Restart session\vwhen asked"], "Pane steps", size=12)
box(s, 0.5, 2.15, 4.4, 3.4, LIGHT, "Pane mock")
text(s, 0.65, 2.22, 4.1, 0.35, [[("PACKAGES", {"bold": True, "col": NAVY, "size": 11}),
                                 ("     Python 3.14.8 (.venv)", {"size": 11})]], "Pane mock head", anchor=MSO_ANCHOR.MIDDLE)
mock = [("great-tables", "1.0.0", ""), ("pandas", "3.0.6", "● attached"), ("plotnine", "0.15.8", ""),
        ("polars", "1.44.2", "● attached"), ("statsmodels", "0.15.0", "● attached"), ("…", "", "")]
for j, (n, v, a) in enumerate(mock):
    y = 2.65 + j * 0.45
    box(s, 0.65, y, 4.1, 0.38, WHITE_BG, f"Pane row {j + 1}")
    text(s, 0.78, y, 1.9, 0.38, [[(n, {"font": MONO, "col": NAVY, "size": 11})]], f"Pane name {j + 1}", anchor=MSO_ANCHOR.MIDDLE)
    text(s, 2.55, y, 0.9, 0.38, [[(v, {"font": MONO, "size": 11})]], f"Pane version {j + 1}", anchor=MSO_ANCHOR.MIDDLE)
    text(s, 3.45, y, 1.25, 0.38, [[(a, {"col": ACC, "size": 10.5})]], f"Pane attached {j + 1}", anchor=MSO_ANCHOR.MIDDLE)
card(s, 5.05, 2.15, 4.45, 3.4, "What else it does", [
    "Shows which packages are loaded (attached)",
    "Update one, or Update All Packages",
    "Flags known security issues",
    "Keeps versions in line with requirements.txt",
    "Offers to install a missing package after an error"], "LuPackage", "Pane card", head_h=0.45)

# 31  Load packages
s = add_slide("Titel und Inhalt", "Load packages: import at the top of every file",
              notes="Loading is the same on Windows and macOS. Installing happens once per laptop; importing in every "
                    "file and every new session.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["Install once\vper laptop", "Import in every\vfile and session",
                                 "Use the short\vname: pl.read_csv()"], "Package steps", size=12)
code_block(s, 0.5, 2.15, 5.3, 2.05, """import polars as pl
import statsmodels.formula.api as smf
from plotnine import ggplot, aes, geom_line
from great_tables import GT

print(pl.__version__)    # 1.44.2""", "Import code", size=11, caption="Windows and macOS: the same code")
card(s, 6.0, 2.15, 3.5, 2.05, "Conventions", [
    "pl and smf are the usual short names",
    "Imports go at the top",
    "Import only what you use"], "LuBookOpen", "Conventions card", head_h=0.45)
callout(s, 4.35, 1.2, "LuTriangleAlert", ("ModuleNotFoundError? ", "Either the wrong interpreter is selected (pick the one "
                                                                 "in .venv) or the package is missing: %pip install it."),
        "Error", dark=True)

# 32  Toolkit map
s = add_slide("Titel und Inhalt", "Your toolkit, from data to report",
              notes="The four stages repeat in every lab and in the case study.")
tw4 = (9.0 - GAP * 3) / 4
kit = [("1  Wrangle", "LuDatabase", [("polars ", "fast tables"), ("pandas ", "for model packages")]),
       ("2  Visualise", "LuChartColumn", [("plotnine ", "charts by grammar")]),
       ("3  Model", "LuSigma", [("statsmodels ", "regression"), ("pymc-marketing ", "Bayesian MMM")]),
       ("4  Report", "LuPresentation", [("great_tables ", "tables"), ("Quarto ", "documents")])]
for i, (head, ic, items) in enumerate(kit):
    x = 0.5 + i * (tw4 + GAP)
    card(s, x, 1.35, tw4, 1.95, head, [[(a, {"bold": True, "col": NAVY, "font": MONO}), (b, {})] for a, b in items],
         ic, f"Kit card {i + 1}", head_h=0.5, bullets=False)
    if i < 3:
        box(s, x + tw4 - 0.02, 2.2, 0.19, 0.3, ACC, f"Kit arrow {i + 1}", shape=MSO_SHAPE.CHEVRON)
fact = [("22", "packages pinned in requirements.txt"), ("1", "command installs them all"), ("0", "euros: all open source")]
for i, (fig, lab) in enumerate(fact):
    x = 0.5 + i * ((9.0 - GAP * 2) / 3 + GAP)
    w = (9.0 - GAP * 2) / 3
    box(s, x, 3.45, w, 1.1, LIGHT, f"Kit fact {i + 1}")
    box(s, x, 3.45, 0.07, 1.1, ACC, f"Kit fact bar {i + 1}")
    text(s, x + 0.25, 3.45, w - 0.35, 1.1, [[(fig, {"size": FIG, "bold": True, "col": NAVY, "head": True})], lab],
         f"Kit fact text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)

callout(s, 4.75, 0.8, "LuBookOpen", ("Online you will also meet pandas and matplotlib: ", "older but common; "
                                                                                    "the ideas carry over."), "Older tools")

# 33  polars
s = add_slide("Titel und Inhalt", "polars: data wrangling",
              notes="Read the chain top to bottom: keep 2025, group by country, sum two columns, sort. "
                    "statsmodels and PyMC expect pandas, so convert at the end with .to_pandas().")
code_block(s, 0.5, 1.35, 5.4, 3.1, '''import polars as pl

sales = pl.read_csv("data/mmm/alpenglow_weekly.csv",
                    try_parse_dates=True)
summary = (
    sales
    .filter(pl.col("week").dt.year() == 2025)
    .group_by("country")
    .agg(pl.col("revenue_eur_k").sum().alias("revenue"),
         pl.col("spend_tv_k").sum().alias("tv"))
    .sort("revenue", descending=True)
)''', "Polars code", size=10.5, caption="Revenue and TV spend per country, 2025")
prow = [("DataFrame: ", "a table with typed columns"),
        ("Expressions: ", "pl.col(\"tv\").sum() says what to compute"),
        ("Chaining: ", "one step per line, read top to bottom"),
        ("Fast: ", "multi-threaded, written in Rust")]
for i, para in enumerate(prow):
    y = 1.35 + i * (0.7 + 0.1)
    box(s, 6.1, y, 3.4, 0.7, LIGHT, f"Polars row {i + 1}")
    box(s, 6.1, y, 0.07, 0.7, ACC, f"Polars bar {i + 1}")
    text(s, 6.3, y, 3.1, 0.7, [para], f"Polars text {i + 1}", size=12, anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.6, 0.95, "LuTable", ("Result: ", "six rows, one per country. Germany leads with about EUR" + NB + "131" + NB +
                                  "million revenue in 2025. Need pandas? Add .to_pandas()."), "Polars result")

# 34  plotnine
s = add_slide("Titel und Inhalt", "plotnine: charts with the grammar of graphics",
              notes="Same grammar as ggplot2 in R, so R tutorials transfer almost one to one. Each + adds one layer.")
code_block(s, 0.5, 1.35, 4.6, 2.6, '''(ggplot(sales.filter(
         pl.col("country").is_in(["AT", "DE"])),
        aes(x="week", y="sales_units_k"))
 + geom_line(color="#0096D3")
 + facet_wrap("country")
 + scale_x_date(date_breaks="1 year",
                date_labels="%Y")
 + labs(x="", y="Sales (k units)")
 + theme_minimal())''', "Plotnine code", size=10.5, caption="Weekly sales, Austria and Germany")
pic = s.shapes.add_picture(str(FIGS / "plotnine_example.png"), I(5.25), I(1.35), I(4.25), I(2.2667))
pic.name = "Plotnine chart"
pic._element.nvPicPr.cNvPr.set("descr", "Line chart of weekly sales in thousand units, 2023 to 2025, Austria (about 100 to "
                                        "200) and Germany (about 500 to 1,700), with a Christmas peak every year")
text(s, 5.25, 3.65, 4.25, 0.3, [[("The output of the code on the left", {"size": 11, "col": "595959"})]], "Chart caption")
gram = [("ggplot()", "the data"), ("aes()", "columns to x, y"), ("geom_", "the marks"),
        ("facet_", "one panel per group"), ("theme_", "the look")]
gw = (9.0 - 0.1 * 4) / 5
for i, (a, b) in enumerate(gram):
    x = 0.5 + i * (gw + 0.1)
    box(s, x, 4.15, gw, 0.85, LIGHT, f"Grammar chip {i + 1}")
    text(s, x + 0.1, 4.15, gw - 0.2, 0.85, [[(a, {"font": MONO, "bold": True, "col": NAVY})], [(b, {"size": 12})]],
         f"Grammar text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, space=0)
text(s, 0.5, 5.1, 9.0, 0.45, [[("Data + mapping + marks + panels + theme: ", {"bold": True, "col": NAVY}),
                               ("each + adds one layer.", {})]], "Grammar note", anchor=MSO_ANCHOR.MIDDLE)

# 35  Great Tables
s = add_slide("Titel und Inhalt", "Great Tables: tables for reports",
              notes="GT takes the polars summary from the polars slide directly. In a Quarto HTML report the table "
                    "renders by itself; .save() writes a PNG.")
code_block(s, 0.5, 1.35, 5.2, 2.0, '''from great_tables import GT

(GT(summary)
 .tab_header(title="Revenue and TV spend, 2025")
 .fmt_number(columns=["revenue", "tv"], decimals=0)
 .cols_label(country="Country",
             revenue="Revenue (k EUR)",
             tv="TV spend (k EUR)"))''', "GT code", size=10.5, caption="The polars summary as a table")
pic = s.shapes.add_picture(str(FIGS / "great_tables_example.png"), I(6.0), I(1.35), I(3.2), I(3.2 * 590 / 714))
pic.name = "Great Tables output"
pic._element.nvPicPr.cNvPr.set("descr", "Table of revenue and TV spend in 2025 by country, Germany first with 130,650 "
                                        "thousand euros revenue")
gtrows = [("Header and labels: ", "readable names instead of column codes"),
          ("Number formats: ", "thousands separators, currency, percent"),
          ("Works with polars ", "and pandas; renders in Quarto reports")]
for i, para in enumerate(gtrows):
    y = 3.55 + i * 0.68
    box(s, 0.5, y, 5.2, 0.58, LIGHT, f"GT row {i + 1}")
    box(s, 0.5, y, 0.07, 0.58, ACC, f"GT bar {i + 1}")
    text(s, 0.72, y, 4.9, 0.58, [para], f"GT text {i + 1}", size=12, anchor=MSO_ANCHOR.MIDDLE)

# 36  statsmodels
s = add_slide("Titel und Inhalt", "statsmodels: regression",
              notes="A first look only: Sessions 1 and 2 explain how to read, check and improve such a model. "
                    "The formula reads: sales explained by price, TV spend and paid search spend.")
code_block(s, 0.5, 1.35, 5.4, 2.4, '''import statsmodels.formula.api as smf

at = sales.filter(pl.col("country") == "AT").to_pandas()
model = smf.ols(
    "sales_units_k ~ price_eur + spend_tv_k"
    " + spend_paid_search_k",
    data=at).fit()
print(model.summary())''', "OLS code", size=10.5, caption="Weekly sales in Austria, 2023 to 2025")
coef = [("Coefficient", "Estimate"), ("Intercept", "250.63"), ("price_eur", "\u221248.31"), ("spend_tv_k", "0.41"),
        ("spend_paid_search_k", "4.03"), ("R\u00b2  (n" + NB + "=" + NB + "156)", "0.43")]
box(s, 6.1, 1.35, 3.4, 2.4, LIGHT, "Coefficient panel")
for i, (a, b) in enumerate(coef):
    y = 1.45 + i * 0.37
    hd = i == 0
    text(s, 6.25, y, 2.2, 0.37, [[(a, {"font": None if hd else MONO, "bold": hd, "col": NAVY, "size": 11 if not hd else 12})]],
         f"Coef name {i + 1}", anchor=MSO_ANCHOR.MIDDLE)
    text(s, 8.35, y, 1.0, 0.37, [[(b, {"bold": hd, "col": NAVY, "size": 12})]], f"Coef value {i + 1}",
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)
callout(s, 3.95, 0.8, "LuLightbulb", ("Reading it: ", "EUR" + NB + "1,000 more paid search in a week goes with about "
                                                    "4,000 more units sold, holding price and TV constant."), "OLS reading")
text(s, 0.5, 4.9, 9.0, 0.65, [[("Later in the course: ", {"bold": True, "col": NAVY}),
                               ("scikit-learn for logistic regression and pymc-marketing for Bayesian MMM.", {})]],
     "Later note", anchor=MSO_ANCHOR.MIDDLE)

# ---------------------------------------------------------------- wrap-up ----
# 37  Troubleshooting
s = add_slide("Titel und Tabelle", "When something goes wrong",
              notes="Most problems are an old terminal window or the wrong interpreter.")
rows = [("Problem", "Fix"),
        ("Windows: python or py is not recognised", "Reinstall the Python install manager, then run py install 3.14"),
        ("No .venv in the Interpreter picker", "Open the course folder, not a single file; then pick Python 3.14.8 (.venv)"),
        ("ModuleNotFoundError", "Select the .venv interpreter, then %pip install the package"),
        ("macOS: externally-managed-environment", "You used the system Python: select the project's .venv first"),
        ("Quarto preview does not start", "Restart Positron; run quarto check in the terminal"),
        ("Clone fails in GitHub Desktop", "Sign in again under Accounts in the settings; check the URL"),
        ("Copilot is not offered", "GitHub Education still pending: use Copilot Free meanwhile")]
gf = ph(s, 1).insert_table(len(rows), 2)
tbl = gf.table
for i, w in enumerate([3.4, 5.6]):
    tbl.columns[i].width = I(w)
gf.width = I(9.0)
for r_i, row in enumerate(rows):
    for c_i, txt in enumerate(row):
        cell = tbl.cell(r_i, c_i)
        p = cell.text_frame.paragraphs[0]
        set_runs(p, txt)
        for r in p.runs:
            r.font.size = Pt(HEAD if r_i == 0 else BODY)
            if c_i == 0 and r_i > 0:
                r.font.bold = True
        cell.margin_top = cell.margin_bottom = Emu(54000)

# 38  Checklist
s = add_slide("Titel und Inhalt", "Checklist: before you leave today",
              notes="Students tick these off. Anything still open goes to the Q&A forum on Canvas before Session 2.")
cw2 = (9.0 - GAP) / 2
for k, (head, ic, items) in enumerate([
        ("Accounts", "LuUserPlus", ["GitHub account with two-factor sign-in", "GitHub Education application sent",
                                    "DataCamp classroom joined"]),
        ("Laptop", "LuLaptop", ["Python 3.14, Positron, Quarto, GitHub Desktop", "Course repository cloned and open",
                                ".venv created and selected", "\u201cready\u201d and the test report renders",
                                "Posit Assistant connected"])]):
    x = 0.5 + k * (cw2 + GAP)
    box(s, x, 1.35 + 0.45, cw2, 3.0, LIGHT, f"Checklist {head} body")
    box(s, x, 1.35, cw2, 0.45, ACC, f"Checklist {head} header")
    text(s, x + 0.15, 1.35, cw2 - 0.75, 0.45, [head], f"Checklist {head} heading", size=HEAD, col=WHITE, bold=True,
         head=True, anchor=MSO_ANCHOR.MIDDLE)
    icon(s, ic, "white", x + cw2 - 0.48, 1.4, 0.34, f"checklist {head}")
    for j, item in enumerate(items):
        y = 1.95 + j * 0.55
        box(s, x + 0.2, y + 0.08, 0.26, 0.26, WHITE_BG, f"Checkbox {head} {j + 1}", line=NAVY)
        text(s, x + 0.6, y, cw2 - 0.75, 0.45, [item], f"Checklist {head} item {j + 1}", size=12, anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.95, 0.6, "LuLifeBuoy", ("Not ready yet? ", "Post the failing step in the Q&A forum on Canvas before Session 2."),
        "Help", dark=True)

# 39  Closing contact card
add_slide("Abschlussfolie Kontakt", notes="Questions? Contact details on the card.")

deck.save(OUT)
