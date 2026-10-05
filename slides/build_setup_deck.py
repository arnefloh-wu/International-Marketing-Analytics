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

from wu_deck import (A, ACC, BODY, FIG, GAP, HEAD, LIGHT, MONO, NAVY, NB, WHITE, Deck, I, box, card,
                     code_block, color, icon, ph, set_runs, stepper, text)

TEMPLATE, OUT = sys.argv[1:3]
FIGS = Path(__file__).resolve().parent / "figures"
FOOTER = "International Marketing Analytics" + NB + "·" + NB + "WT" + NB + "2026/27"
deck = Deck(TEMPLATE, FOOTER)
add_slide, L = deck.add_slide, deck.L
STEPS = ["Accounts", "Tools", "Repo", "Python", "Check", "AI"]
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
stepper(s, 0.5, 1.35, 9.0, 0.6, STEPS, "Plan steps", size=12)
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
divider("Register your accounts", "Part 1 of 4" + NB + "·" + NB + "GitHub, GitHub Education, DataCamp",
        "Accounts first: they need e-mail confirmations and, for GitHub Education, an approval that can take days.")

# 3  The accounts
s = add_slide("Titel und Inhalt", "Four registrations",
              notes="All four are free for students. Use the WU e-mail address everywhere, so the student benefits apply.")
progress(s, 0)
tw4 = (9.0 - GAP * 3) / 4
accounts = [("LuGithub", "GitHub", ["Stores code and its history; hosts the course and group repositories"],
             ("github.com/signup", "https://github.com/signup")),
            ("LuGraduationCap", "GitHub Education", ["Free student benefits, including GitHub Copilot"],
             ("education.github.com", "https://education.github.com/pack")),
            ("LuAward", "DataCamp", ["Online Python courses; four certificates count 20" + NB + "%"],
             ("Invitation link on Canvas", None)),
            ("LuClipboardCheck", "Canvas survey", ["Tell us your GitHub username so we can give you access"],
             ("Course page on Canvas", None))]
for i, (ic, head, lines, (where, url)) in enumerate(accounts):
    x = 0.5 + i * (tw4 + GAP)
    tile(s, x, 1.95, tw4, 2.75, ic, head, lines, f"Account {i + 1}")
    text(s, x + 0.15, 4.2, tw4 - 0.3, 0.4, [[link(where, url) if url else (where, {"bold": True, "col": ACC})]],
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
divider("Install the tools", "Part 2 of 4" + NB + "·" + NB + "uv, Positron, Quarto, GitHub Desktop, the course repository",
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
row2 = [("LuTerminal", "Python + packages", "in a .venv made by uv"),
        ("LuFileText", "Quarto", "turns .qmd files into reports"),
        ("LuBot", "AI assistant", "writes and explains code")]
for i, (ic, head, sub) in enumerate(row2):
    box(s, xs[i], 4.3, bw, 0.85, WHITE_BG, f"Inside box {i + 1}")
    icon(s, ic, "navy", xs[i] + 0.12, 4.5, 0.45, f"inside {i + 1}")
    text(s, xs[i] + 0.7, 4.3, bw - 0.8, 0.85, [[(head, {"bold": True, "col": NAVY})], [(sub, {"size": 11})]],
         f"Inside text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, space=0)

# 8  uv and Python
s = add_slide("Titel und Inhalt", "Step 2: install uv, which installs Python",
              notes="uv replaces pip, venv and pyenv with one fast tool. It downloads Python itself, so students do not "
                    "need the installer from python.org. Close and reopen the terminal after installing.")
progress(s, 1)
code_block(s, 0.5, 1.95, 5.6, 1.05,
           'powershell -ExecutionPolicy ByPass -c "irm\n  https://astral.sh/uv/install.ps1 | iex"',
           "Windows code", caption="Windows: PowerShell (one line)")
code_block(s, 0.5, 3.15, 5.6, 0.8, "curl -LsSf https://astral.sh/uv/install.sh | sh", "Mac code",
           caption="macOS: Terminal")
code_block(s, 0.5, 4.1, 5.6, 0.8, "uv --version", "Check code", caption="Then, in a new terminal window: check")
card(s, 6.3, 1.95, 3.2, 2.95, "What uv does", [
    "Installs Python for you",
    "Creates a private environment per project",
    "Installs packages in seconds",
    "Replaces pip, venv and pyenv"], "LuPackage", "uv card", head_h=0.45)
text(s, 0.5, 5.05, 9.0, 0.45, [[("Windows: ", {"bold": True, "col": NAVY}),
                                ("type the command on one line; the line break above is only for the slide.", {})]],
     "Windows note", size=12, anchor=MSO_ANCHOR.MIDDLE)

# 9  Positron, Quarto, GitHub Desktop
s = add_slide("Titel und Inhalt", "Step 2: install Positron, Quarto and GitHub Desktop",
              notes="Install in this order. Positron detects Quarto and Python automatically. GitHub Desktop brings Git "
                    "with it, so there is no separate Git installer.")
progress(s, 1)
tw3 = (9.0 - GAP * 2) / 3
tools = [("LuMonitor", "Positron", "positron.posit.co/download", "https://positron.posit.co/download",
          ["The editor for code, data and charts", "Free, from Posit", "macOS: drag it to Applications"]),
         ("LuFileText", "Quarto", "quarto.org/docs/get-started", "https://quarto.org/docs/get-started/",
          ["Turns text and code into reports and slides", "Check: quarto --version"]),
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
              notes="The course repository is read-only for students: they pull updates before each session. "
                    "Group repositories for the case study come later and use the same clicks plus commit and push.")
progress(s, 2)
stepper(s, 0.5, 1.95, 9.0, 0.6, ["Copy the URL\vfrom Canvas", "GitHub Desktop:\vClone repository", "Pick a folder\vwithout spaces",
                                 "Positron:\vOpen Folder"], "Clone steps", size=12)
code_block(s, 0.5, 2.75, 4.4, 1.05, "C:\\Users\\anna\\wu\\ima\n~/wu/ima", "Folder code", caption="Good folder names")
text(s, 0.5, 3.9, 4.4, 0.85, [("Avoid ", "spaces, umlauts and cloud folders such as OneDrive or iCloud: they break "
                                         "paths and syncing.")], "Folder note", size=12)
words = [("Clone", "your own copy of the repository, linked to GitHub"),
         ("Pull", "get the latest materials; do it before every session"),
         ("Commit and push", "save and upload your changes (group repository)")]
for i, (w, d) in enumerate(words):
    y = 2.75 + i * 0.68
    box(s, 5.1, y, 4.4, 0.58, LIGHT, f"Git word {i + 1}")
    box(s, 5.1, y, 0.07, 0.58, ACC, f"Git word bar {i + 1}")
    text(s, 5.32, y, 4.08, 0.58, [(w + ": ", d)], f"Git word text {i + 1}", size=12, anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.9, 0.65, "LuFolderOpen", ("In Positron: ", "File \u2192 Open Folder and choose the cloned folder."), "Open folder")

# 11  Python environment
s = add_slide("Titel und Inhalt", "Step 4: create the Python environment",
              notes="The first install downloads several hundred megabytes (PyMC is large), so it takes a few minutes on "
                    "WU Wi-Fi. Positron usually offers the new .venv interpreter by itself.")
progress(s, 3)
code_block(s, 0.5, 1.95, 5.0, 1.1, "uv venv --python 3.12\nuv pip install -r requirements.txt", "Env code",
           caption="Positron: Terminal \u2192 New Terminal, then")
numbered(s, 0.5, 3.25, 5.0, [
    ("Creates .venv: ", "a private Python just for this folder"),
    ("Installs ", "the packages and versions in requirements.txt"),
    ("Select it: ", "click the interpreter at the top right")], "Env steps", row_h=0.55, gap=0.1)
box(s, 5.7, 1.95, 3.8, 3.15, LIGHT, "Interpreter panel")
text(s, 5.9, 2.05, 3.4, 0.35, [[("The interpreter selector", {"bold": True, "col": NAVY})]], "Interpreter head")
pill = box(s, 6.05, 2.55, 3.1, 0.45, WHITE_BG, "Interpreter pill", shape=MSO_SHAPE.ROUNDED_RECTANGLE, line=ACC)
text(s, 6.2, 2.55, 2.9, 0.45, [[("Python 3.12 (.venv)  \u25be", {"font": MONO, "col": NAVY, "size": 12})]], "Pill text",
     anchor=MSO_ANCHOR.MIDDLE)
text(s, 5.9, 3.15, 3.4, 1.85, [
    "Shows which Python runs your code",
    "Pick the one that ends in .venv",
    "Once per folder; Positron remembers it"], "Interpreter text", size=12, bullets=True, space=6)
text(s, 0.5, 5.15, 9.0, 0.4, [[("First time: ", {"bold": True, "col": NAVY}),
                               ("a few minutes, because PyMC is large. After that you only pull and open the folder.", {})]],
     "Env note", size=12, anchor=MSO_ANCHOR.MIDDLE)

# 12  The check
s = add_slide("Titel und Inhalt", "Step 5: run the check",
              notes="The script lives in setup/check_setup.py. Every line marked !! says what to fix. "
                    "Alternatively open the file and press the Run button at the top right of the editor.")
progress(s, 4)
code_block(s, 0.5, 1.95, 9.0, 0.75, "uv run --no-project python setup/check_setup.py", "Check command",
           caption="In the Positron terminal")
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
callout(s, 5.05, 0.5, "LuPlay", ("No terminal? ", "Open setup/check_setup.py in Positron and press Run."), "Run button")

# 13  AI assistant
s = add_slide("Titel und Inhalt", "Step 6: connect your AI assistant",
              notes="Posit Assistant replaced Positron Assistant in Positron 2026.07; older videos show the old menus. "
                    "GitHub Copilot is the cheapest provider for students.")
progress(s, 5)
numbered(s, 0.5, 1.95, 5.0, [
    ("Accounts menu ", "in Positron (bottom left): sign in with GitHub"),
    ("Copilot ", "now suggests code as you type"),
    ("Posit Assistant: ", "open the chat, choose GitHub Copilot")], "AI steps", row_h=0.62, gap=0.1)
rows = [("Copilot Student", "free, after GitHub Education approval"),
        ("Copilot Free", "free, with monthly limits"),
        ("Posit AI Pass", "about USD" + NB + "20 a month"),
        ("Anthropic API key", "pay as you go")]
box(s, 5.7, 1.95, 3.8, 2.06, LIGHT, "Options panel")
text(s, 5.9, 2.0, 3.4, 0.35, [[("Options", {"bold": True, "col": NAVY})]], "Options head")
text(s, 5.9, 2.35, 3.5, 1.6, [(a + ": ", b) for a, b in rows], "Options text", size=12, space=4)
callout(s, 4.25, 1.2, "LuShieldCheck", ("Our rule: ", "the AI writes, you check. Run the code, read the output and keep "
                                                   "a short prompt log for each submission."), "AI rule", dark=True)

# ---------------------------------------------------------------- Part 3 -----
divider("How Positron works", "Part 3 of 4" + NB + "·" + NB + "panes, running code, Quarto, shortcuts",
        "A five-minute tour with the live application next to the slides works best.")

# 14  Positron at a glance: a schematic window
s = add_slide("Titel und Inhalt", "Positron at a glance",
              notes="Left: files. Middle: editor above, console below. Right: what is in memory and the charts. "
                    "The interpreter selector sits at the top right.")
box(s, 0.5, 1.35, 9.0, 0.36, NAVY, "Window bar")
text(s, 0.65, 1.35, 4.0, 0.36, [[("ima \u2014 Positron", {"col": WHITE, "size": 11})]], "Window title",
     anchor=MSO_ANCHOR.MIDDLE)
box(s, 6.95, 1.39, 2.45, 0.28, WHITE_BG, "Window pill", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 7.0, 1.39, 2.35, 0.28, [[("Python 3.12 (.venv) \u25be", {"font": MONO, "col": NAVY, "size": 10.5})]],
     "Window pill text", anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
box(s, 0.5, 1.71, 0.3, 3.84, ACC, "Activity bar")
panes = [  # x, y, w, h, name, description, sample
    (0.84, 1.75, 1.86, 3.8, "Explorer", "the files of the course folder", "data/\nsessions/\nsetup/\nrequirements.txt"),
    (2.74, 1.75, 3.86, 2.08, "Editor", "write .py and .qmd files", 'sales = pl.read_csv(...)\nsales.head()'),
    (2.74, 3.87, 3.86, 1.68, "Console and Terminal", "code runs here, results print", ">>> sales.height\n936"),
    (6.64, 1.75, 2.86, 1.73, "Variables", "what is in memory; click a table to explore it", None),
    (6.64, 3.52, 2.86, 2.03, "Plots", "charts appear here", None),
]
for i, (x, y, w, h, head, desc, sample) in enumerate(panes):
    box(s, x, y, w, h, LIGHT, f"Pane {head}")
    badge(s, x + 0.1, y + 0.1, i + 1, f"Pane number {i + 1}", d=0.3, fill=ACC)
    text(s, x + 0.5, y + 0.08, w - 0.6, 0.6, [[(head, {"bold": True, "col": NAVY, "size": 12})], [(desc, {"size": 11})]],
         f"Pane text {i + 1}", space=0)
    if sample:
        text(s, x + 0.15, y + 0.85, w - 0.3, h - 0.95,
             [[(ln, {"font": MONO, "col": NAVY, "size": 11})] for ln in sample.split("\n")], f"Pane sample {i + 1}", space=0)
vars_ = [("sales", "936 \u00d7 18"), ("summary", "6 \u00d7 3"), ("model", "OLS results")]
for j, (n, v) in enumerate(vars_):
    text(s, 6.79, 2.45 + j * 0.3, 2.6, 0.3, [[(n, {"font": MONO, "col": NAVY, "size": 11}), ("   " + v, {"size": 11})]],
         f"Variable {j + 1}", space=0)
pic = s.shapes.add_picture(str(FIGS / "plotnine_example.png"), I(6.79), I(4.18), I(2.56), I(1.3653))
pic.name = "Plot thumbnail"
pic._element.nvPicPr.cNvPr.set("descr", "Example line chart of weekly sales for Austria and Germany")

# 15  From code to result
s = add_slide("Titel und Inhalt", "From code to result",
              notes="Show it live: write one line, press Ctrl+Enter, point at the console, the Variables pane and the plot.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["Write code\vin the editor", "Ctrl/Cmd\v+ Enter", "It runs in\vthe console",
                                 "Objects in\vVariables", "Charts in\vPlots"], "Run steps", size=12)
cw2 = (9.0 - GAP) / 2
card(s, 0.5, 2.15, cw2, 2.3, "Run code", [
    "Ctrl/Cmd + Enter: the line or selection",
    "Ctrl/Cmd + Shift + Enter: the current cell of a .qmd file",
    "Run button (top right): the whole file"], "LuPlay", "Run card", head_h=0.45)
card(s, 0.5 + cw2 + GAP, 2.15, cw2, 2.3, "Look at results", [
    "Variables: every object, its type and size",
    "Data Explorer: sort, filter and summarise a table without code",
    "Plots: earlier charts, zoom, save as PNG"], "LuEye", "Results card", head_h=0.45)
callout(s, 4.65, 0.9, "LuSquareTerminal", ("Console or terminal? ", "The console speaks Python. The terminal speaks to "
                                                                  "your computer: uv, git and quarto commands go there."),
        "Console", dark=True)

# 16  Quarto in Positron
s = add_slide("Titel und Inhalt", "Quarto documents in Positron",
              notes="All labs and the case study report are Quarto files. Text, code and results stay in one file, "
                    "so the report can be rerun when the data change.")
qmd = '''---
title: "Sales by country"
format: html
---

## Revenue in 2025

```{python}
import polars as pl
sales = pl.read_csv("data/mmm/alpenglow_weekly.csv")
```

Germany has the highest revenue.'''
code_block(s, 0.5, 1.35, 5.3, 3.25, qmd, "Qmd code", size=10.5, caption="report.qmd")
qrows = [("LuFileText", ("Text ", "in Markdown: headings, bold, lists")),
         ("LuCode", ("Code cells ", "run one by one, like a notebook")),
         ("LuEye", ("Preview: ", "Ctrl/Cmd + Shift + K shows the report next to your code")),
         ("LuPresentation", ("Render ", "to HTML, PDF, Word or slides"))]
for i, (ic, para) in enumerate(qrows):
    y = 1.35 + i * (0.73 + 0.1)
    box(s, 6.0, y, 3.5, 0.73, LIGHT, f"Quarto row {i + 1}")
    icon(s, ic, "navy", 6.15, y + 0.16, 0.4, f"quarto {i + 1}")
    text(s, 6.72, y, 2.7, 0.73, [para], f"Quarto text {i + 1}", size=12, anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.8, 0.75, "LuNotebookPen", ("One file, rerun any time: ", "the labs and your case study report are Quarto "
                                                                   "documents."), "Quarto use")

# 17  Shortcuts
s = add_slide("Titel und Tabelle", "Shortcuts worth knowing",
              notes="On macOS, Cmd replaces Ctrl, except for the new-terminal shortcut. The command palette finds every "
                    "other command by name.")
rows = [("Action", "Windows", "macOS"),
        ("Run line or selection", "Ctrl + Enter", "Cmd + Enter"),
        ("Run current cell (.qmd)", "Ctrl + Shift + Enter", "Cmd + Shift + Enter"),
        ("Preview a Quarto document", "Ctrl + Shift + K", "Cmd + Shift + K"),
        ("Find any command", "Ctrl + Shift + P", "Cmd + Shift + P"),
        ("Open a file by name", "Ctrl + P", "Cmd + P"),
        ("Comment or uncomment lines", "Ctrl + /", "Cmd + /"),
        ("New terminal", "Ctrl + Shift + `", "Ctrl + Shift + `"),
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
        cell.margin_top = cell.margin_bottom = Emu(54000)

# 18  AI inside Positron
s = add_slide("Titel und Inhalt", "Working with AI in Positron",
              notes="Posit's FAQ: prompts, session information and variable names and types are sent to the model "
                    "provider; row-level data only when you ask for it. Do not paste personal data.")
cw2 = (9.0 - GAP) / 2
card(s, 0.5, 1.35, cw2, 1.85, "Copilot: ghost text", [
    "Grey suggestions appear as you type",
    "Tab accepts, Esc rejects",
    "Best for short, routine lines"], "LuSparkles", "Ghost card", head_h=0.45)
card(s, 0.5 + cw2 + GAP, 1.35, cw2, 1.85, "Posit Assistant: chat", [
    "Sees your data, variables and plots",
    "Writes, explains and fixes code",
    "You approve each step it runs"], "LuBot", "Assistant card", head_h=0.45)
text(s, 0.5, 3.35, 9.0, 0.3, [[("Good prompts", {"bold": True, "col": NAVY})]], "Prompt label")
code_block(s, 0.5, 3.7, 9.0, 0.8,
           '"Sum revenue by country for 2025 with polars and sort it."\n'
           '"Explain this error in two sentences, then fix it."', "Prompt code", size=11.5)
callout(s, 4.7, 0.85, "LuShieldCheck", ("Privacy: ", "prompts, variable names and types go to the model provider; rows of "
                                                     "data only if you ask. Never paste personal data."), "Privacy")

# ---------------------------------------------------------------- Part 4 -----
divider("Python packages for this course", "Part 4 of 4" + NB + "·" + NB + "polars, plotnine, Great Tables, statsmodels",
        "Each package gets one slide with code that runs on the course data.")

# 19  Install once, import every time
s = add_slide("Titel und Inhalt", "Packages: install once, import every time",
              notes="Python itself is small; packages add the tools. Versions are pinned so everybody's results match.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["requirements.txt\vlists packages", "uv pip install\vonce per laptop",
                                 "import\vin every file"], "Package steps", size=12)
code_block(s, 0.5, 2.15, 5.3, 1.95, """import polars as pl
import statsmodels.formula.api as smf
from plotnine import ggplot, aes, geom_line
from great_tables import GT""", "Import code", caption="Top of every script")
card(s, 6.0, 2.15, 3.5, 1.95, "Conventions", [
    "pl and smf are the usual short names",
    "Imports go at the top",
    "Import only what you use"], "LuBookOpen", "Conventions card", head_h=0.45)
callout(s, 4.3, 1.2, "LuTriangleAlert", ("ModuleNotFoundError? ", "The wrong interpreter is selected (pick .venv) or the "
                                                                "package is missing (run uv pip install -r requirements.txt)."),
        "Error", dark=True)

# 20  Toolkit map
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

# 21  polars
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

# 22  plotnine
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

# 23  Great Tables
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

# 24  statsmodels
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
# 25  Troubleshooting
s = add_slide("Titel und Tabelle", "When something goes wrong",
              notes="Most problems are an old terminal window or the wrong interpreter.")
rows = [("Problem", "Fix"),
        ("uv: command not found", "Close and reopen the terminal, or restart Positron"),
        ("PowerShell: running scripts is disabled", "Use the exact uv command; it includes -ExecutionPolicy ByPass"),
        ("ModuleNotFoundError", "Select the .venv interpreter; run uv pip install -r requirements.txt again"),
        ("Quarto preview does not start", "Restart Positron; run quarto check in the terminal"),
        ("Clone fails in GitHub Desktop", "Sign in again; check the URL; is your username in the Canvas survey?"),
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

# 26  Checklist
s = add_slide("Titel und Inhalt", "Checklist: before you leave today",
              notes="Students tick these off. Anything still open goes to the Q&A forum on Canvas before Session 2.")
cw2 = (9.0 - GAP) / 2
for k, (head, ic, items) in enumerate([
        ("Accounts", "LuUserPlus", ["GitHub account with two-factor sign-in", "GitHub Education application sent",
                                    "DataCamp classroom joined", "GitHub username in the Canvas survey"]),
        ("Laptop", "LuLaptop", ["uv, Positron, Quarto and GitHub Desktop installed", "Course repository cloned and open",
                                ".venv created and selected", "Check script prints \u201cready\u201d",
                                "AI assistant signed in"])]):
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

# 27  Closing contact card
add_slide("Abschlussfolie Kontakt", notes="Questions? Contact details on the card.")

deck.save(OUT)
