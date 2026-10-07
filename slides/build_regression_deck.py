"""Build the deck "Linear regression" (Session 1) on the WU template (polish-slides skill).

Six parts: theory (correlation, simple and multiple OLS, inference, fit, functional forms, from elasticity to
price), assumptions and tests, regression in the real world, the chocolate data in Python (statsmodels and
plotnine), an in-class assignment and the individual coding exercise 1. Core readings: Bojinov, Parzen & Hamilton
(2025, HBS note 9-622-100) and Skiera, Reiner & Albers (2022, Handbook of Market Research); further sources from
instructor/resources/regression-resource-guide.md; two quiz questions adapted from the quantmethods exam bank.
Every number comes from make_regression_figures.py (slides/figures/reg_numbers.txt), which also draws the charts.

usage: python slides/build_regression_deck.py TEMPLATE.pptx OUT.pptx
"""
import copy
import sys
from pathlib import Path

from lxml import etree
from pptx.enum.dml import MSO_LINE
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
GREY_TXT = "595959"
PCT = NB + "%"


# ---------------------------------------------------------------- helpers ----
def divider(title, part, notes):
    s = add_slide("Kapitelfolie", title, notes=notes)
    set_runs(ph(s, 11).text_frame.paragraphs[0], part)
    return s


def badge(slide, x, y, num, name, d=0.34, fill=NAVY, size=12):
    b = box(slide, x, y, d, d, fill, name, shape=MSO_SHAPE.OVAL)
    tf = b.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = str(num); r.font.size = Pt(size); r.font.bold = True
    color(r.font.color, WHITE)


def numbered(slide, x, y, w, items, name, row_h=0.62, gap=0.1, size=BODY):
    """Numbered rows: bg2 band, navy number badge, text with a bold lead-in."""
    for i, para in enumerate(items):
        ry = y + i * (row_h + gap)
        box(slide, x, ry, w, row_h, LIGHT, f"{name} row {i + 1}")
        badge(slide, x + 0.15, ry + (row_h - 0.34) / 2, i + 1, f"{name} number {i + 1}")
        text(slide, x + 0.65, ry, w - 0.8, row_h, [para], f"{name} text {i + 1}", size=size, anchor=MSO_ANCHOR.MIDDLE)


def callout(slide, y, h, icon_name, para, name, dark=False, x=0.5, w=9.0, size=BODY):
    box(slide, x, y, w, h, NAVY if dark else LIGHT, f"{name} box")
    icon(slide, icon_name, "white" if dark else "navy", x + 0.22, y + (h - 0.4) / 2, 0.4, name)
    if dark:
        lead, rest = para
        para = [(lead, {"bold": True, "col": WHITE}), (rest, {"col": WHITE})]
    text(slide, x + 0.82, y, w - 1.0, h, [para], f"{name} text", anchor=MSO_ANCHOR.MIDDLE, size=size)


def tile(slide, x, y, w, h, icon_name, head, lines, name, size=BODY):
    """Icon at the top left, bold navy heading, plain lines underneath."""
    box(slide, x, y, w, h, LIGHT, f"{name} tile")
    icon(slide, icon_name, "navy", x + 0.15, y + 0.15, 0.4, name)
    text(slide, x + 0.65, y + 0.15, w - 0.75, 0.4, [[(head, {"bold": True, "col": NAVY, "size": HEAD, "head": True})]],
         f"{name} heading", anchor=MSO_ANCHOR.MIDDLE)
    text(slide, x + 0.15, y + 0.68, w - 0.3, h - 0.75, lines, f"{name} text", space=4, size=size)


def stat(slide, x, y, w, h, fig, label, name, fig_w=1.25, size=BODY):
    """Stat row: thin accent bar, 28 pt navy figure, explanation to its right."""
    box(slide, x, y, 0.07, h, ACC, f"{name} bar")
    text(slide, x + 0.2, y, fig_w, h, [[(fig, {"size": FIG, "bold": True, "col": NAVY, "head": True})]],
         f"{name} figure", anchor=MSO_ANCHOR.MIDDLE)
    text(slide, x + 0.2 + fig_w, y, w - fig_w - 0.25, h, [label], f"{name} label", anchor=MSO_ANCHOR.MIDDLE, size=size)


def source(slide, txt, y=5.27, x=0.5, w=9.0):
    text(slide, x, y, w, 0.28, [[("Sources: " + txt, {"col": GREY_TXT, "size": 11})]], "Sources",
         anchor=MSO_ANCHOR.MIDDLE)


def picture(slide, fname, x, y, w, h, alt):
    pic = slide.shapes.add_picture(str(FIGS / fname), I(x), I(y), I(w), I(h))
    pic.name = "Chart " + fname
    pic._element.nvPicPr.cNvPr.set("descr", alt)
    return pic


def arrow(slide, x, y, name, w=0.22, h=0.36):
    box(slide, x, y, w, h, ACC, name, shape=MSO_SHAPE.CHEVRON)


def table(slide, rows, widths, name, size=BODY, head_size=HEAD, top=1.35, bold_first_col=True, row_margin=45000,
          mono_rows=()):
    gf = ph(slide, 1).insert_table(len(rows), len(rows[0]))
    gf.name = name
    tbl = gf.table
    for i, w in enumerate(widths):
        tbl.columns[i].width = I(w)
    gf.left, gf.top, gf.width = I(0.5), I(top), I(sum(widths))
    for r_i, row in enumerate(rows):
        for c_i, txt in enumerate(row):
            cell = tbl.cell(r_i, c_i)
            p = cell.text_frame.paragraphs[0]
            set_runs(p, txt)
            for r in p.runs:
                r.font.size = Pt(head_size if r_i == 0 else size)
                if c_i == 0 and r_i > 0 and bold_first_col:
                    r.font.bold = True
            cell.margin_top = cell.margin_bottom = Emu(row_margin)
    return tbl


def link(t, url):
    return (t, {"link": url, "col": ACC})



SKIERA = "Skiera, Reiner & Albers 2022"
HBS = "Bojinov, Parzen & Hamilton 2025"


def rows_with_bar(slide, x, y, w, items, name, row_h=0.62, gap=0.08, size=12):
    for i, para in enumerate(items):
        ry = y + i * (row_h + gap)
        box(slide, x, ry, w, row_h, LIGHT, f"{name} row {i + 1}")
        box(slide, x, ry, 0.07, row_h, ACC, f"{name} bar {i + 1}")
        text(slide, x + 0.22, ry, w - 0.32, row_h, [para], f"{name} text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, size=size)


def grid(slide, rows, widths, x, y, name, row_h=0.36, size=11.5, head_fill=ACC, first_bold=True):
    """Drawn table: header in accent1, body rows in bg2, works on any layout."""
    for r_i, row in enumerate(rows):
        cx = x
        for c_i, val in enumerate(row):
            w = widths[c_i]
            head_row = r_i == 0
            box(slide, cx, y + r_i * (row_h + 0.03), w - 0.03, row_h, head_fill if head_row else LIGHT,
                f"{name} {r_i + 1}-{c_i + 1}")
            col = WHITE if head_row else (NAVY if c_i == 0 and first_bold else INK)
            text(slide, cx + 0.1, y + r_i * (row_h + 0.03), w - 0.23, row_h,
                 [[(val, {"bold": head_row or (c_i == 0 and first_bold), "col": col, "size": size})]],
                 f"{name} text {r_i + 1}-{c_i + 1}", anchor=MSO_ANCHOR.MIDDLE)
            cx += w


# ================================================================ slides ======
# 1  Title
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
              notes="Linear regression is the workhorse of the course: every marketing mix model is a regression with "
                    "transformed variables. Today: the theory, the assumptions and how to test them, real-world uses, and "
                    "a first model on real chocolate scanner data in Python. Readings: Bojinov, Parzen and Hamilton "
                    "(2025), Skiera, Reiner and Albers (2022).")
set_runs(ph(s, 0).text_frame.paragraphs[0], "International Marketing Analytics")
set_runs(ph(s, 1).text_frame.paragraphs[0], "Linear regression")
set_runs(ph(s, 12).text_frame.paragraphs[0], "Session 1" + NB + "·" + NB + "WT" + NB + "2026/27")

# 2  Plan
s = add_slide("Titel und Inhalt", "Today",
              notes="Six blocks. Theory and assumptions in the lecture; the chocolate data live in Positron; then an "
                    "in-class assignment in groups and the instructions for the first individual coding exercise.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["Theory", "Tests", "Practice", "Python", "In class", "Exercise"], "Plan steps", size=11)
cw3 = (9.0 - GAP * 2) / 3
plan = [("LuSigma", "Understand", ["What OLS does and what a coefficient means",
                                            "t-test, p-value, confidence interval, R²", "Logs and elasticities"]),
        ("LuShieldCheck", "Check", ["Seven assumptions behind OLS", "Residual plots and four tests",
                                             "What to do when a test fails"]),
        ("LuCode", "Code", ["A first regression with statsmodels", "Simple charts with plotnine",
                                     "A pricing recommendation from data"])]
for i, (ic, head, items) in enumerate(plan):
    card(s, 0.5 + i * (cw3 + GAP), 2.15, cw3, 2.4, head, items, ic, f"Plan card {i + 1}", head_h=0.45)
callout(s, 4.72, 0.6, "LuBookOpen", ("Readings: ", "Bojinov, Parzen & Hamilton (2025), Linear Regression (HBS); Skiera, "
                                                  "Reiner & Albers (2022), Regression Analysis."), "Readings", dark=True,
        size=12)

# 3  The business question
s = add_slide("Titel und Inhalt", "The question: what does a price cut sell?",
              notes="Real weekly scanner data for one chocolate brand (brand 1) and three competitors: 68 weeks of unit "
                    "sales, prices, feature ads and in-store displays, plus temperature and holiday weeks. Brand 1 cut its "
                    "price from about 1.50 to about 1.03 in seven weeks (blue dots); sales jumped to up to five times the "
                    "normal level. The brand manager wants to know how strongly sales respond to price, and whether the "
                    "regular price is right.")
picture(s, "reg_sales_time.png", 0.5, 1.35, 5.0, 3.0,
        "Line chart of weekly sales of brand 1 over 68 weeks: mostly between 60 and 120, with seven spikes up to about "
        "530 in price-cut weeks, marked with blue dots")
text(s, 0.5, 4.4, 5.0, 0.3, [[("Weekly sales of brand 1; blue: weeks with a price cut (price below 1.20).",
                               {"col": GREY_TXT, "size": 11})]], "Sales caption", anchor=MSO_ANCHOR.MIDDLE)
rows_with_bar(s, 5.65, 1.35, 3.85, [
    ("Data: ", "68 weeks of real scanner data, 4 brands"),
    ("Normal week: ", "price about 1.50, sales about 100"),
    ("Price-cut week: ", "price about 1.03, sales up to 530"),
    ("Also in the data: ", "competitor prices, features, displays, temperature, holidays")], "Question", row_h=0.68,
    gap=0.08)
callout(s, 4.8, 0.6, "LuTarget", ("The manager asks: ", "how much does 1" + PCT + " lower price sell, and is the regular "
                                                        "price right?"), "Manager question", dark=True)

# ---------------------------------------------------------------- Part 1 -----
divider("Theory", "Part 1 of 6" + NB + "·" + NB + "correlation, simple and multiple regression, inference, fit, logs, "
        "from elasticity to price", "Concepts first, each shown on the chocolate data. Bojinov et al. (2025) and Skiera "
        "et al. (2022) cover the same steps in more depth.")

# 5  Correlation
s = add_slide("Titel und Inhalt", "Correlation: direction and strength",
              notes="The correlation r lies between -1 and +1 and measures the direction and strength of a linear "
                    "relationship. The rule of thumb in the HBS note: below 0.2 very weak, up to 0.4 weak to moderate, up "
                    "to 0.6 medium to substantial, up to 0.8 very strong, above extremely strong. Sales and own price of "
                    "brand 1 correlate at -0.94. Two warnings: r only measures linear association (a perfect U-shape has "
                    "r = 0), and correlation is not causation.")
text(s, 0.5, 1.35, 4.4, 0.35, [[("Rule of thumb for |r|", {"bold": True, "col": NAVY, "size": HEAD, "head": True})]],
     "r label", anchor=MSO_ANCHOR.MIDDLE)
grid(s, [("|r|", "Interpretation"), ("0 to 0.2", "very weak"), ("0.2 to 0.4", "weak to moderate"),
         ("0.4 to 0.6", "medium to substantial"), ("0.6 to 0.8", "very strong"), ("0.8 to 1.0", "extremely strong")],
     [1.5, 2.9], 0.5, 1.8, "r table", row_h=0.38, size=12)
box(s, 5.1, 1.35, 4.4, 1.25, LIGHT, "r stat box")
stat(s, 5.1, 1.35, 4.4, 1.25, "−0.94", "sales and own price of brand 1: an extremely strong negative relationship",
     "r stat", fig_w=1.4, size=12)
rows_with_bar(s, 5.1, 2.75, 4.4, [("Linear only: ", "a perfect U-shape has r = 0"),
                                  ("Not causation: ", "ice cream and sunburn rise together; the sun drives both")],
              "r warn", row_h=0.6)
callout(s, 4.4, 0.75, "LuTriangleAlert", ("Correlation describes; ", "regression quantifies: how many units does one "
                                                                     "euro of price cost?"), "r next", dark=True, x=0.5,
        w=9.0, size=12)
source(s, HBS + " (HBS note 9-622-100)")

# 6  Simple linear regression
s = add_slide("Titel und Inhalt", "Simple linear regression",
              notes="The line sales = 1,110 - 669 x price1 is the least-squares line for brand 1. The slope says: one "
                    "unit (one euro) more price, 669 units fewer per week; more useful, 10 cents more price, about 67 units "
                    "fewer. R-squared is 0.88. But look at the chart: the points curve. The line overshoots in the middle "
                    "and misses the promotion weeks, a first hint that a straight line is the wrong form (logs follow).")
picture(s, "reg_scatter.png", 0.5, 1.35, 4.9, 3.25,
        "Scatter plot of weekly sales against price of brand 1 with a falling straight line; most points sit near a price "
        "of 1.5 and sales of 100, seven points near a price of 1.03 with sales of 290 to 530")
code_block(s, 5.55, 1.35, 3.95, 0.6, "sales = b0 + b1 · price1 + e", "Simple formula", size=12)
rows_with_bar(s, 5.55, 2.1, 3.95, [("b0 = 1,110: ", "intercept, sales at price 0 (not meaningful here)"),
                                   ("b1 = −669: ", "10 cents more price, about 67 units fewer a week"),
                                   ("e: ", "residual, what the line does not explain")], "Simple rows", row_h=0.72)
callout(s, 4.75, 0.55, "LuEye", ("Look at the chart: ", "the points curve, so a straight line misses the price-cut weeks."),
        "Simple look", size=12)

# 7  Least squares
s = add_slide("Titel und Inhalt", "Least squares: the line with the smallest squared errors",
              notes="Each residual is the vertical distance between an observed week and the line. Ordinary least "
                    "squares (OLS) chooses intercept and slope so that the sum of squared residuals is as small as "
                    "possible. Squaring makes positive and negative misses count equally and weighs large misses more, "
                    "which is also why single extreme weeks can pull the line (outliers, Part 2).")
picture(s, "reg_residuals.png", 0.5, 1.35, 4.6, 3.2,
        "The same scatter plot with the regression line and thin blue vertical segments from each point to the line, the "
        "residuals")
code_block(s, 5.25, 1.35, 4.25, 0.95, "residual:  e_i = y_i − ŷ_i\nOLS:       minimise Σ e_i²", "LS formula",
           size=12)
rows_with_bar(s, 5.25, 2.45, 4.25, [("Squared: ", "misses above and below do not cancel"),
                                    ("Large misses ", "count much more than small ones"),
                                    ("One line: ", "the unique best fit for these data")], "LS rows", row_h=0.6)
source(s, SKIERA + "; " + HBS, y=4.75)

# 8  Multiple regression
s = add_slide("Titel und Inhalt", "Multiple regression: holding other things constant",
              notes="With several explanatory variables each coefficient measures the effect of one variable while the "
                    "others are held constant (ceteris paribus). This is exactly the marketing mix question: what does a "
                    "price cut do if feature ads, competitor prices and the season stay the same? A variable left out of "
                    "the model hands its effect to the variables that are in it (omitted variable bias).")
code_block(s, 0.5, 1.35, 9.0, 0.75, "ln sales = b0 + b1·ln price1 + b2·ln price2 + b3·ln price3 + b4·ln price4\n"
                                    "           + b5·feature1 + b6·temp + b7·december + e", "Multiple formula", size=12)
cw3 = (9.0 - GAP * 2) / 3
mix = [("LuSlidersHorizontal", "Own mix", ["Price of brand 1", "Feature ads, displays"]),
       ("LuUsers", "Competitors", ["Prices of brands 2 to 4", "Their features and displays"]),
       ("LuCalendarDays", "Context", ["Temperature", "December and Easter weeks"])]
for i, (ic, head, lines) in enumerate(mix):
    tile(s, 0.5 + i * (cw3 + GAP), 2.25, cw3, 1.65, ic, head, lines, f"Mix {i + 1}", size=12)
callout(s, 4.05, 0.7, "LuScale", ("Each b: ", "the effect of one variable with all others held constant (ceteris "
                                             "paribus)."), "Ceteris", dark=True)
text(s, 0.5, 4.85, 9.0, 0.4, [[("Left out ", {"bold": True, "col": NAVY, "size": 12}),
                               ("a relevant variable? Its effect ends up in the others (omitted variable bias).",
                                {"size": 12})]], "Omitted note", anchor=MSO_ANCHOR.MIDDLE)

# 9  Inference
s = add_slide("Titel und Inhalt", "Is the effect real? t-test, p-value, interval, F-test",
              notes="Every coefficient comes with a standard error. t = b / se tests whether the true coefficient is zero; "
                    "the p-value is the probability of a t this extreme if it were zero; below 0.05 we call it significant. "
                    "The 95 % confidence interval is about b plus or minus two standard errors. The F-test asks whether "
                    "all slopes together are zero. For brand 1: own-price elasticity -3.64, se 0.30, t -12.1, interval "
                    "-4.24 to -3.04; F = 59.5, p < 0.001.")
tw2 = (9.0 - GAP) / 2
inf = [("LuSigma", "t-test", ["t = b / se", "Own price: −3.64 / 0.30 = −12.1"]),
       ("LuGauge", "p-value", ["Below 0.05: significant", "Own price: p < 0.001; brand 4: p = 0.86"]),
       ("LuSlidersHorizontal", "95" + PCT + " confidence interval", ["About b ± 2 se", "Own price: −4.24 to −3.04"]),
       ("LuLayers", "F-test", ["Are all slopes together zero?", "F = 59.5, p < 0.001"])]
for i, (ic, head, lines) in enumerate(inf):
    tile(s, 0.5 + (i % 2) * (tw2 + GAP), 1.35 + (i // 2) * (1.55 + GAP), tw2, 1.55, ic, head, lines, f"Inf {i + 1}",
         size=12)
callout(s, 4.75, 0.55, "LuTriangleAlert", ("Significant is not important: ", "read the size of b and its interval, not "
                                                                            "just the stars."), "Inf warn", dark=True,
        size=12)
source(s, HBS + "; " + SKIERA)

# 10  Fit
s = add_slide("Titel und Inhalt", "How well does the model fit?",
              notes="R-squared is the share of the variation in the outcome that the model explains; it never falls when "
                    "a variable is added, so adjusted R-squared penalises extra variables. The residual standard error "
                    "(or RMSE) is the typical miss in the units of the outcome: in a log model, 0.169 means about 17 % per "
                    "week. Compare R-squared only between models with the same outcome: the simple model (sales) has 0.88, "
                    "the log model (log sales) 0.87, and these are not comparable.")
fits = [("0.874", "R²: the model explains 87" + PCT + " of the weekly variation in log sales"),
        ("0.859", "adjusted R²: R² with a penalty for each extra variable"),
        ("0.169", "RMSE: the typical weekly miss, about 17" + PCT + " in a log model")]
for i, (fig, lab) in enumerate(fits):
    y = 1.35 + i * (0.8 + 0.08)
    box(s, 0.5, y, 5.4, 0.8, LIGHT, f"Fit row {i + 1}")
    stat(s, 0.5, y, 5.4, 0.8, fig, lab, f"Fit stat {i + 1}", fig_w=1.45, size=12)
card(s, 6.05, 1.35, 3.45, 2.56, "Careful", ["R² never falls when you add a variable",
                                            "Compare R² only for the same outcome (sales vs log sales)",
                                            "High R² does not mean causal"], "LuTriangleAlert", "Fit card", head_h=0.45)
callout(s, 4.1, 0.6, "LuTarget", ("Main model for brand 1: ", "log-log, own and competitor prices, feature, temperature, "
                                                             "December; 68 weeks."), "Fit model", size=12)
source(s, HBS + "; " + SKIERA, y=4.85)

# 11  Functional forms and dummies
s = add_slide("Titel und Tabelle", "Functional forms and dummy variables",
              notes="Logs turn a multiplicative sales response function into a linear regression (Skiera et al. 2022): in "
                    "the log-log form the coefficient is an elasticity, the per cent change in sales for a 1 % change in "
                    "the driver. A dummy (0/1) in a log model shifts sales by exp(b) - 1 per cent: December -0.385 means "
                    "exp(-0.385) - 1 = -32 %. For small b, b x 100 is a good approximation.")
table(s, [("Model", "Equation", "b means", "Brand 1"),
          ("Linear", "sales = a + b·price", "+1 unit price: b units", "b = −669 units"),
          ("Log-log", "ln sales = a + b·ln price", "+1" + PCT + " price: b" + PCT, "b = −3.64 (elasticity)"),
          ("Log-linear", "ln sales = a + b·temp", "+1 °C: about 100·b" + PCT, "b = −0.0066: −0.66" + PCT),
          ("Dummy in log model", "ln sales = a + b·december", "e^b − 1, vs other weeks", "b = −0.385: −32" + PCT)],
      [1.9, 2.6, 2.4, 2.1], "Forms table", size=12, top=1.35)
callout(s, 4.25, 0.75, "LuLightbulb", ("Why logs? ", "sales respond in per cent, not in units, and the elasticity can be "
                                                     "compared across brands and countries."), "Forms why", dark=True)
source(s, SKIERA + "; Wooldridge 2025, ch. 6 to 7", y=5.1)

# 12  From elasticity to price
s = add_slide("Titel und Inhalt", "From elasticity to a pricing decision",
              notes="With a constant elasticity e below -1, the profit-maximising price is marginal cost times e / (1 + e) "
                    "(the Amoroso-Robinson relation). Skiera et al. estimate e = -2.34 with unit cost $30, which gives about "
                    "$52. For brand 1 e = -3.64 gives a price 1.38 times marginal cost, a 38 % markup. Caveats: this is a "
                    "short-term, promotion-driven elasticity; regular-price elasticities are usually smaller, competitors "
                    "react, and the retailer takes a margin.")
code_block(s, 0.5, 1.35, 9.0, 0.6, "optimal price  p* = marginal cost × ε / (1 + ε)        (valid for ε < −1)",
           "Price formula", size=12)
tw2 = (9.0 - GAP) / 2
box(s, 0.5, 2.1, tw2, 1.35, LIGHT, "Skiera box")
stat(s, 0.5, 2.1, tw2, 1.35, "$52", "Skiera et al.: ε = −2.34, unit cost $30 → p* = 30 × 2.34 / 1.34", "Skiera stat",
     fig_w=1.25, size=12)
box(s, 0.5 + tw2 + GAP, 2.1, tw2, 1.35, LIGHT, "Brand box")
stat(s, 0.5 + tw2 + GAP, 2.1, tw2, 1.35, "×1.38", "Brand 1: ε = −3.64 → price 38" + PCT + " above marginal cost",
     "Brand stat", fig_w=1.35, size=12)
rows_with_bar(s, 0.5, 3.6, 9.0, [("Short term: ", "promotion weeks inflate the elasticity; regular-price elasticities are "
                                                  "smaller"),
                                 ("Competitors react, ", "and the retailer takes its margin")], "Price caveats",
              row_h=0.5, gap=0.07)
source(s, SKIERA + "; Hanssens, Parsons & Schultz 2001", y=4.75)

# ---------------------------------------------------------------- Part 2 -----
divider("Assumptions and tests", "Part 2 of 6" + NB + "·" + NB + "what OLS assumes, how to look, how to test, what to do",
        "Look first (residual plots), then test, then decide. Skiera et al. (2022) recommend checking multicollinearity, "
        "autocorrelation and heteroscedasticity in every model.")

# 14  Assumptions overview
s = add_slide("Titel und Tabelle", "Seven assumptions behind OLS",
              notes="Linearity and no omitted variables protect the coefficients themselves; homoscedasticity, no "
                    "autocorrelation and normal residuals protect the standard errors and therefore the t- and F-tests. "
                    "Normality matters least: with enough observations (Skiera et al.: even 10 to 20) the tests still work. "
                    "Skiera et al. recommend at least three, better five times as many observations as coefficients. "
                    "Exogeneity is the one no test can prove: it needs a good design (next slides).")
table(s, [("Assumption", "If violated", "Look or test (statsmodels)"),
          ("1 Linear form", "biased coefficients", "residuals vs fitted; try logs"),
          ("2 Exogeneity, no omitted variables", "biased, not causal", "theory, controls, experiments"),
          ("3 Constant error variance", "wrong standard errors", "funnel in plot; Breusch-Pagan"),
          ("4 No autocorrelation", "standard errors too small", "residuals over time; Durbin-Watson ≈ 2"),
          ("5 Normal residuals", "tests unreliable in small samples", "histogram; Jarque-Bera"),
          ("6 No multicollinearity", "unstable b, large se", "correlations; VIF below 10 (better 5)"),
          ("7 Enough data, no dominant week", "fragile results", "n ≥ 3 to 5 × coefficients; Cook's distance")],
      [3.1, 2.6, 3.3], "Assumption table", size=11.5, head_size=13, top=1.35, row_margin=36000)
source(s, SKIERA + "; Hair et al. 2019; Wooldridge 2025", y=5.2)

# 15  Look first
s = add_slide("Titel und Inhalt", "Look first: two residual plots",
              notes="Left: residuals against fitted values for the main brand-1 model. No curve and no funnel, so the "
                    "linear log form and constant variance look acceptable; a few price-cut weeks sit to the right. Right: "
                    "the histogram is roughly bell-shaped with slightly heavy tails.")
picture(s, "reg_resid_fitted.png", 0.5, 1.35, 4.35, 3.04,
        "Residuals against fitted values: a cloud around zero between -0.5 and 0.5, most fitted values near 4.5, a few "
        "near 6, no curve or funnel")
picture(s, "reg_resid_hist.png", 5.15, 1.35, 4.35, 3.04,
        "Histogram of the residuals: roughly bell-shaped around zero, a few residuals around 0.4 to 0.6")
text(s, 0.5, 4.42, 4.35, 0.5, [("Look for: ", "a curve (wrong form) or a funnel (unequal variance)")], "Look left",
     size=12, anchor=MSO_ANCHOR.MIDDLE)
text(s, 5.15, 4.42, 4.35, 0.5, [("Look for: ", "a rough bell shape, no extreme weeks")], "Look right", size=12,
     anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.95, 0.5, "LuEye", ("Brand 1: ", "no curve, no funnel, a roughly bell-shaped histogram."), "Look verdict",
        size=12)

# 16  Then test
s = add_slide("Titel und Inhalt", "Then test: four numbers for the brand 1 model",
              notes="Durbin-Watson 1.41: below 2, some positive autocorrelation between neighbouring weeks, which makes "
                    "the usual standard errors a little too small; Newey-West (HAC) standard errors correct this (0.32 "
                    "instead of 0.30 for own price). Breusch-Pagan p = 0.14 and Jarque-Bera p = 0.07: no evidence against "
                    "constant variance and normal residuals at 5 %. Largest VIF 2.4: no multicollinearity.")
tw2 = (9.0 - GAP) / 2
tests = [("1.41", "Durbin-Watson: below 2, some autocorrelation between weeks"),
         ("0.14", "Breusch-Pagan p: no evidence of unequal variance"),
         ("0.07", "Jarque-Bera p: residuals roughly normal"),
         ("2.4", "largest VIF: no multicollinearity")]
for i, (fig, lab) in enumerate(tests):
    x = 0.5 + (i % 2) * (tw2 + GAP)
    y = 1.35 + (i // 2) * (1.0 + GAP)
    box(s, x, y, tw2, 1.0, LIGHT, f"Test box {i + 1}")
    stat(s, x, y, tw2, 1.0, fig, lab, f"Test stat {i + 1}", fig_w=1.2, size=12)
picture(s, "reg_resid_time.png", 0.5, 3.6, 2.6, 1.6, "Bar chart of residuals by week: runs of positive and negative "
                                                     "residuals, e.g. positive from week 35 to 50")
callout(s, 3.6, 1.6, "LuShieldCheck", ("Verdict: ", "usable. Report Newey-West (HAC) standard errors because of the "
                                                    "autocorrelation: 0.32 instead of 0.30 for own price."), "Test verdict",
        dark=True, x=3.25, w=6.25, size=12)

# 17  When tests fail
s = add_slide("Titel und Tabelle", "When a test fails: what to do",
              notes="Most fixes are one argument in statsmodels: cov_type='HC3' for heteroscedasticity-robust standard "
                    "errors, cov_type='HAC' with maxlags for autocorrelation (Newey-West). Multicollinearity has no "
                    "econometric cure: more variation in the data, combine variables, or run an experiment (Skiera et al.). "
                    "Outliers: check the data first, report results with and without, never delete silently. Endogeneity "
                    "needs design: experiments, instruments, panel data.")
table(s, [("Problem", "Remedy", "In statsmodels"),
          ("Curve in residuals", "logs, squares, interactions", "np.log(x), I(x**2)"),
          ("Unequal variance", "robust standard errors", "fit(cov_type=\"HC3\")"),
          ("Autocorrelation", "HAC standard errors; lags; ARIMA errors (Session 4)",
           "fit(cov_type=\"HAC\", cov_kwds={\"maxlags\": 1})"),
          ("Multicollinearity", "more variation, combine variables, experiments", "variance_inflation_factor"),
          ("Dominant weeks", "check data, report with and without", "get_influence().cooks_distance"),
          ("Endogeneity", "experiments, instruments, fixed effects", "Sessions 2 to 5")],
      [2.2, 3.4, 3.4], "Remedy table", size=11.5, head_size=13, top=1.35, row_margin=40000)
source(s, SKIERA + "; statsmodels documentation", y=5.15)

# 18  Two warnings from the data
s = add_slide("Titel und Inhalt", "Three warnings from real data",
              notes="Multicollinearity: brand 1 ran displays in only four weeks, mostly together with features and price "
                    "cuts; adding display1 and fand1 gives VIFs of 11.4 and 10.9. Influence: there is a single Easter week; "
                    "an Easter dummy fits that week perfectly (leverage 1.00), so its coefficient says nothing. Skiera et "
                    "al.: mailings and salespersons correlate at 0.989; with both in the model the VIF is 53 and the "
                    "salesperson coefficient turns negative and insignificant.")
cw3 = (9.0 - GAP * 2) / 3
warn = [("LuShuffle", "Displays", ["Only 4 display weeks", "VIF 11.4 and 10.9",
                                                      "Effects cannot be separated"]),
        ("LuCrosshair", "One Easter week", ["A dummy for one week fits it exactly", "Leverage 1.00",
                                            "No real estimate of Easter"]),
        ("LuTriangleAlert", "Mailings", ["Skiera et al.: mailings and salespersons r = 0.989", "VIF 53",
                                                        "Salesperson effect flips sign"])]
for i, (ic, head, items) in enumerate(warn):
    card(s, 0.5 + i * (cw3 + GAP), 1.35, cw3, 2.75, head, items, ic, f"Warn {i + 1}", head_h=0.45)
callout(s, 4.3, 0.8, "LuFlaskConical", ("The real fix: ", "vary the marketing instruments independently, ideally in a "
                                                          "field experiment."), "Warn fix", dark=True)
source(s, SKIERA + "; own calculation on the chocolate data", y=5.2)

# 19  Endogeneity
s = add_slide("Titel und Inhalt", "Endogeneity: when marketing follows demand",
              notes="OLS assumes that the explanatory variables are unrelated to the error. Marketing breaks this whenever "
                    "managers spend more where they expect success: then high spend and high unexplained sales go "
                    "together and the coefficient is too large (Skiera et al.). Price cuts are often timed with features "
                    "and displays, so the price coefficient also carries their effect. Gordon et al. (2019) compared 15 "
                    "Facebook experiments with regression-based estimates: the observational methods often overstated the "
                    "lift, sometimes by a factor of three or more.")
rows_with_bar(s, 0.5, 1.35, 9.0, [
    ("The assumption: ", "explanatory variables are unrelated to the error term"),
    ("Marketing breaks it: ", "budgets go where managers expect success, so spend and unexplained sales rise together"),
    ("Brand 1: ", "price cuts come with features, so the price effect partly measures the feature"),
    ("Evidence: ", "in 15 Facebook experiments, regression often overstated the true lift, sometimes 3 times")],
    "Endo", row_h=0.6, gap=0.08)
callout(s, 4.25, 0.85, "LuFlaskConical", ("Remedies: ", "experiments (A/B, geo tests), instrumental variables such as "
                                                       "cost shifters, panel data with fixed effects."), "Endo fix",
        dark=True)
source(s, SKIERA + "; Gordon, Zettelmeyer, Bhargava & Chapsky 2019", y=5.2)

# ---------------------------------------------------------------- Part 3 -----
divider("Regression in the real world", "Part 3 of 6" + NB + "·" + NB + "benchmarks, companies, what transfers to MMM",
        "Regression is everywhere in marketing practice, usually with a different name.")

# 21  Benchmarks
s = add_slide("Titel und Inhalt", "Benchmarks from decades of regressions",
              notes="Bijmolt, van Heerde and Pieters (2005) pool 1,851 price elasticities: mean -2.62. Sethuraman, Tellis "
                    "and Briesch (2011): short-term advertising elasticity 0.12 on average. Datta et al. (2022): across 14 "
                    "Asia-Pacific countries the average price elasticity is -0.42 and lower where power distance is high. "
                    "Brand 1's -3.64 is more price-sensitive than the average brand: chocolate has many close substitutes "
                    "and the estimate is driven by promotion weeks.")
bm = [("−2.62", "mean price elasticity, 1,851 estimates (Bijmolt et al. 2005)"),
      ("0.12", "mean short-term advertising elasticity (Sethuraman et al. 2011)"),
      ("−0.42", "mean price elasticity in 14 Asia-Pacific countries, lower with high power distance (Datta et al. 2022)"),
      ("−3.64", "brand 1, chocolate: promotion-driven, many substitutes")]
for i, (fig, lab) in enumerate(bm):
    y = 1.35 + i * (0.78 + 0.07)
    box(s, 0.5, y, 9.0, 0.78, LIGHT, f"Bench row {i + 1}")
    stat(s, 0.5, y, 9.0, 0.78, fig, lab, f"Bench stat {i + 1}", fig_w=1.6, size=12)
callout(s, 4.82, 0.45, "LuScale", ("Use benchmarks ", "to judge whether your own estimate is plausible."), "Bench use",
        dark=True, size=12)

# 22  Companies
s = add_slide("Titel und Inhalt", "Where companies use regression",
              notes="Meta's Robyn is a ridge regression on adstocked and saturated media variables: MMM in production. "
                    "Microsoft and Booking.com add the pre-period metric as a covariate in A/B tests (CUPED), which cuts "
                    "the sample size needed. Google estimates ad effectiveness from geo experiments with regressions of "
                    "test on control regions. Walmart's M5 competition showed that forecasts need price, promotion and "
                    "event regressors. statworx (Frankfurt) estimates price elasticities from retail sales with log-log "
                    "regressions. Bayer reallocated its budget across countries with estimated elasticities (Fischer et "
                    "al. 2011).")
tw3 = (9.0 - GAP * 2) / 3
uses = [("LuChartArea", "Meta Robyn", ["MMM in production:", "ridge regression on media"]),
        ("LuFlaskConical", "Booking.com", ["With Microsoft: CUPED,", "regression makes A/B tests faster"]),
        ("LuMap", "Google", ["Geo experiments: test vs", "control regions by regression"]),
        ("LuShoppingCart", "Walmart (M5)", ["Sales forecasts need price,", "promotion and event regressors"]),
        ("LuCoins", "statworx", ["Frankfurt consultancy: price", "elasticities, log-log"]),
        ("LuEarth", "Bayer", ["Budget across countries", "from estimated elasticities"])]
for i, (ic, head, lines) in enumerate(uses):
    x = 0.5 + (i % 3) * (tw3 + GAP)
    y = 1.35 + (i // 3) * (1.62 + 0.1)
    tile(s, x, y, tw3, 1.62, ic, head, [[(ln, {})] for ln in lines], f"Use {i + 1}", size=12)
callout(s, 4.82, 0.42, "LuLightbulb", ("Session 2: ", "the marketing mix model is this regression with adstock and "
                                                     "saturation."), "Use next", size=12)
source(s, "Robyn docs; Deng et al. 2013; Vaver & Koehler 2011; Makridakis et al. 2022; Fischer et al. 2011", y=5.27)

# ---------------------------------------------------------------- Part 4 -----
divider("The chocolate data in Python", "Part 4 of 6" + NB + "·" + NB + "load and plot, the first regression, the log-log "
        "model, the checks", "Live in Positron. The code on the next slides is complete: copy it into a Quarto file "
        "and run it cell by cell.")

# 24  The data
s = add_slide("Titel und Tabelle", "The data: 68 weeks of chocolate scanner data",
              notes="data/legacy/chocolate_dataset.csv in the course repository (also as the original .xlsx). Feature, "
                    "display and fand (feature and display) are shares of stores between 0 and 1. Sales and prices are "
                    "for brand 1 unless numbered otherwise; units are as delivered by the data provider.")
table(s, [("Column", "Meaning"),
          ("week", "1 to 68"),
          ("sales", "weekly unit sales of brand 1"),
          ("price1 to price4", "prices of brands 1 to 4"),
          ("feature1 to feature4", "share of stores with a feature ad, 0 to 1"),
          ("display1 to display4", "share of stores with an in-store display"),
          ("fand1, fand3, fand4", "share with feature and display together"),
          ("temp", "temperature, °C"),
          ("december, easter", "1 in December and Easter weeks")],
      [2.9, 6.1], "Data table", size=12, head_size=13, top=1.35, row_margin=34000)
text(s, 0.5, 5.0, 9.0, 0.35, [[("File: ", {"bold": True, "col": NAVY, "size": 12}),
                               ("data/legacy/chocolate_dataset.csv", {"font": MONO, "col": NAVY, "size": 12})]],
     "Data file", anchor=MSO_ANCHOR.MIDDLE)

# 25  Step 1 load and plot
s = add_slide("Titel und Inhalt", "Step 1: load and look",
              notes="polars reads the CSV; describe() gives counts, means and ranges. plotnine draws the scatter plot "
                    "with the least-squares line in three lines of code. Always look before you model.")
code_block(s, 0.5, 1.35, 4.6, 3.3, """import polars as pl
from plotnine import (ggplot, aes, geom_point,
                      geom_smooth, labs)

choc = pl.read_csv(
    "data/legacy/chocolate_dataset.csv")
choc.select("sales", "price1",
            "price2").describe()

(ggplot(choc, aes("price1", "sales"))
 + geom_point()
 + geom_smooth(method="lm")
 + labs(x="Price of brand 1",
        y="Weekly sales"))""", "Load code", size=10.5, caption="Python: polars and plotnine")
picture(s, "reg_scatter.png", 5.25, 1.35, 4.25, 2.81,
        "The scatter plot of sales against price of brand 1 with the least-squares line")
callout(s, 4.8, 0.55, "LuEye", ("Look before you model: ", "ranges, outliers, the shape of the relationship."),
        "Load look", size=12)

# 26  Step 2 first regression
s = add_slide("Titel und Inhalt", "Step 2: the first regression",
              notes="statsmodels takes a pandas data frame, so .to_pandas() converts the polars frame (pyarrow does the "
                    "work in the background). The formula reads like the equation. summary() prints the full table; "
                    "params, bse, pvalues and rsquared give single numbers for the text.")
code_block(s, 0.5, 1.35, 4.9, 2.4, """import statsmodels.formula.api as smf

df = choc.to_pandas()
simple = smf.ols("sales ~ price1",
                 data=df).fit()
print(simple.summary())

simple.params      # b0, b1
simple.rsquared    # 0.884""", "Simple code", size=10.5, caption="Python: statsmodels")
grid(s, [("", "coef", "std err", "P>|t|"), ("Intercept", "1,110.0", "44.0", "0.000"),
         ("price1", "−668.8", "29.8", "0.000")], [1.1, 0.95, 0.95, 0.9], 5.55, 1.35, "Simple out", row_h=0.42,
     size=12)
text(s, 5.55, 2.75, 3.95, 0.4, [[("R² = 0.884, n = 68", {"bold": True, "col": NAVY, "size": 12})]], "Simple r2",
     anchor=MSO_ANCHOR.MIDDLE)
rows_with_bar(s, 0.5, 3.95, 9.0, [("Read it: ", "10 cents more price, about 67 units fewer per week; the price "
                                                 "explains 88" + PCT + " of the weekly variation.")], "Simple read",
              row_h=0.55)
callout(s, 4.7, 0.55, "LuTriangleAlert", ("But: ", "the residuals curve. Next: the log-log model with the marketing mix."),
        "Simple next", dark=True, size=12)

# 27  Step 3 log-log model
s = add_slide("Titel und Inhalt", "Step 3: the log-log model with the marketing mix",
              notes="np.log inside the formula transforms the variables; numpy comes with statsmodels. Own price: "
                    "elasticity -3.64, highly significant. Competitor prices are not significant at 5 %; the sign for brand "
                    "2 is negative, which would mean a complement and is not plausible, so we do not interpret it. "
                    "December -0.385: exp(-0.385) - 1 = -32 %. Temperature: -0.66 % per degree.")
code_block(s, 0.5, 1.35, 4.6, 2.7, """import numpy as np

model = smf.ols(
    "np.log(sales) ~ np.log(price1)"
    " + np.log(price2) + np.log(price3)"
    " + np.log(price4) + feature1"
    " + temp + december",
    data=df).fit()
print(model.summary())""", "Loglog code", size=10.5, caption="Python: statsmodels")
grid(s, [("", "coef", "p"), ("ln price1", "−3.64", "0.000"), ("ln price2", "−0.80", "0.076"),
         ("ln price3", "0.36", "0.109"), ("ln price4", "−0.03", "0.855"), ("feature1", "0.18", "0.307"),
         ("temp", "−0.007", "0.045"), ("december", "−0.38", "0.009")], [1.6, 1.15, 1.15], 5.25, 1.35, "Loglog out",
     row_h=0.3, size=11.5)
text(s, 5.25, 4.12, 4.25, 0.35, [[("R² = 0.874, adjusted 0.859, n = 68", {"bold": True, "col": NAVY, "size": 12})]],
     "Loglog r2", anchor=MSO_ANCHOR.MIDDLE)
callout(s, 4.6, 0.65, "LuLightbulb", ("Read it: ", "1" + PCT + " higher price, 3.6" + PCT + " fewer sales; December weeks "
                                                   "32" + PCT + " lower; each degree warmer 0.7" + PCT + " lower."),
        "Loglog read", dark=True, size=12)

# 28  Step 4 checks
s = add_slide("Titel und Inhalt", "Step 4: check the assumptions",
              notes="Four functions, four numbers. Then refit with HAC standard errors because Durbin-Watson is below 2. "
                    "The residual plot uses the same plotnine grammar as before.")
code_block(s, 0.5, 1.35, 5.3, 3.05, """from statsmodels.stats.stattools import (
    durbin_watson, jarque_bera)
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import (
    variance_inflation_factor)

durbin_watson(model.resid)                     # 1.41
het_breuschpagan(model.resid, model.model.exog)[1]  # 0.14
jarque_bera(model.resid)[1]                    # 0.07
X = model.model.exog
[variance_inflation_factor(X, i) for i in range(1, 8)]

hac = model.model.fit(cov_type="HAC",
                      cov_kwds={"maxlags": 1})""", "Check code", size=10, caption="Python: tests and robust errors")
code_block(s, 5.95, 1.35, 3.55, 1.7, """from plotnine import geom_hline
df["fit"] = model.fittedvalues
df["res"] = model.resid
(ggplot(df, aes("fit", "res"))
 + geom_point()
 + geom_hline(yintercept=0))""", "Plot code", size=10, caption="Residual plot")
picture(s, "reg_resid_fitted.png", 5.95, 3.12, 1.85, 1.29, "Small residual plot of the main model")
picture(s, "reg_resid_hist.png", 7.85, 3.12, 1.65, 1.15, "Small residual histogram of the main model")
callout(s, 4.6, 0.65, "LuShieldCheck", ("Decide: ", "report the HAC result; the own-price elasticity stays −3.64, its "
                                                   "standard error rises to 0.32."), "Check decide", dark=True, size=12)

# 29  In-class quiz
s = add_slide("Titel und Inhalt", "In-class quiz: five questions",
              notes="Three minutes alone, then compare with your neighbour; reveal the answers one by one. Answers: 1 C (the "
                    "sum of squared residuals). 2 B (log-log: an elasticity, 1 % higher price, 3.6 % fewer sales). 3 B "
                    "(multicollinearity; VIF above 10 is a warning). 4 A (below 2: positive autocorrelation between "
                    "neighbouring weeks, so the usual standard errors are too small; report HAC errors). 5 B (R-squared never "
                    "falls when a variable is added; compare adjusted R-squared or test the coefficient). Questions 1 and 3 "
                    "adapted from the quantmethods exam bank.")
quiz = [("1 What does OLS minimise?", "A the sum of residuals · B the sum of absolute residuals · C the sum of squared "
                                      "residuals"),
        ("2 In ln sales = a + b · ln price, b = −3.64 means …",
         "A 1 EUR more, 3.64 units fewer · B 1" + PCT + " higher price, 3.6" + PCT + " fewer sales · C 3.64 fewer per week"),
        ("3 A VIF of 11 signals …", "A autocorrelation · B multicollinearity · C heteroscedasticity"),
        ("4 Weekly data, Durbin-Watson = 1.41. This suggests …",
         "A positive autocorrelation · B no problem · C unequal variance"),
        ("5 R² rises from 0.85 to 0.86 after adding a variable. This shows …",
         "A the variable matters · B nothing: R² never falls · C the model is causal")]
for i, (q, opts) in enumerate(quiz):
    y = 1.35 + i * (0.64 + 0.08)
    box(s, 0.5, y, 9.0, 0.64, LIGHT, f"Quiz row {i + 1}")
    box(s, 0.5, y, 0.07, 0.64, ACC, f"Quiz bar {i + 1}")
    text(s, 0.72, y, 8.7, 0.64, [[(q, {"bold": True, "col": NAVY})], [(opts.replace(" · ", "     "), {})]],
         f"Quiz text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, size=12, space=1)
callout(s, 5.0, 0.5, "LuListChecks", ("3 minutes alone, ", "then compare with your neighbour. Same format as the online "
                                                          "quiz and the exam."), "Quiz how", dark=True, size=12)

# ---------------------------------------------------------------- Part 5 -----
divider("In-class assignment", "Part 5 of 6" + NB + "·" + NB + "groups of 3, 25 minutes, on the chocolate data",
        "Run the code from Part 4, then answer the four questions. One group presents per question.")

# 31  In-class assignment
s = add_slide("Titel und Inhalt", "In-class assignment: pricing brand 1",
              notes="Expected answers. 1 A falling cloud is weak for brands 3 and 4; brand 2 shows little relation: weak "
                    "competition at the price level in these data. 2 With display1 and fand1 the VIFs exceed 10 and the "
                    "display coefficients swing and lose significance: the four display weeks cannot separate the effects. "
                    "3 With marginal cost 0.80: p* = 0.80 x 1.38 = 1.10; the actual regular price is about 1.50, because "
                    "the -3.64 is a short-term promotion elasticity, the retailer adds its margin and competitors would "
                    "react. 4 For example: 'Promotions sell, but a permanent price cut to 1.10 would rest on a promotion "
                    "elasticity; test it in a few stores first.'")
stepper(s, 0.5, 1.35, 9.0, 0.5, ["Groups of 3:\v20 minutes", "Plenary:\v5 minutes"], "Inclass steps", size=12)
numbered(s, 0.5, 2.0, 9.0, [
    ("Competition: ", "plot sales against price2, price3 and price4. Which brand competes most?"),
    ("Displays: ", "add display1 and fand1 to the log-log model. What happens to the VIFs and coefficients, and why?"),
    ("Price: ", "marginal cost is 0.80. What price does ε = −3.64 suggest? Why is the real price about 1.50?"),
    ("The manager: ", "write one sentence for the brand manager, with a number and one caveat.")],
    "Inclass q", row_h=0.66, gap=0.08, size=12)
text(s, 0.5, 5.0, 9.0, 0.35, [[("File: ", {"bold": True, "col": NAVY, "size": 12}),
                               ("sessions/01-foundations/regression_chocolate.qmd", {"font": MONO, "col": NAVY, "size": 12}),
                               ("  (the code of Part 4 and these questions)", {"size": 12})]], "Inclass file", anchor=MSO_ANCHOR.MIDDLE)

# ---------------------------------------------------------------- Part 6 -----
divider("Coding exercise 1", "Part 6 of 6" + NB + "·" + NB + "individual, 5" + PCT + " of the grade",
        "The first of four coding exercises. It applies the code of this session to a similar task.")

# 33  Exercise tasks
s = add_slide("Titel und Inhalt", "Coding exercise 1: what to do",
              notes="Individual work. The exercise reuses the data of this session with a different specification "
                    "(display1 added, marginal cost 0.90), so the in-class code transfers but the answers differ. The file "
                    "must render from top to bottom; deadline and upload on Canvas. AI assistants are allowed; the prompt "
                    "log at the end shows how they were used.")
numbered(s, 0.5, 1.35, 9.0, [
    ("Explore: ", "a great_tables summary and two plotnine charts: sales over time, sales against price1"),
    ("Simple model: ", "sales ~ price1; interpret the slope for a 10-cent price change"),
    ("Log-log model: ", "own and competitor prices, feature1, display1, temp, december; interpret 3 coefficients"),
    ("Assumptions: ", "residual plot, histogram, Durbin-Watson, Breusch-Pagan, Jarque-Bera, VIF; one sentence each"),
    ("Robust errors: ", "refit with HAC standard errors; what changes and what does not?"),
    ("Recommend: ", "the optimal price for marginal cost 0.90, with two caveats, in at most 100 words")],
    "Ex tasks", row_h=0.56, gap=0.07, size=12)
text(s, 0.5, 5.15, 9.0, 0.35, [[("Brief: ", {"bold": True, "col": NAVY, "size": 12}),
                                ("exercises/exercise-1.qmd", {"font": MONO, "col": NAVY, "size": 12}),
                                ("  in the course repository and on Canvas", {"size": 12})]],
     "Ex data", anchor=MSO_ANCHOR.MIDDLE)

# 34  Exercise rules and grading
s = add_slide("Titel und Inhalt", "Coding exercise 1: submission and grading",
              notes="Grading on 20 points, scaled to 5 % of the final grade. Interpretation counts most, because the AI "
                    "writes much of the code. Deadline: see Canvas.")
cw2 = (9.0 - GAP) / 2
card(s, 0.5, 1.35, cw2, 2.75, "Submit on Canvas", [
    "exercise1_lastname.qmd and the rendered .html",
    "Renders from top to bottom without errors",
    "Every number in the text from code",
    "Prompt log at the end: what you asked, what you changed",
    "Deadline: see Canvas"], "LuFileText", "Ex submit", head_h=0.45)
grid(s, [("Criterion", "Points"), ("Code runs, charts and tables clean", "5"), ("Interpretation of the coefficients", "6"),
         ("Assumption checks and conclusion", "5"), ("Recommendation with caveats", "2"), ("Prompt log", "2"),
         ("Total (5" + PCT + " of the grade)", "20")], [3.35, 1.08], 0.5 + cw2 + GAP, 1.35, "Ex grid", row_h=0.36,
     size=12)
callout(s, 4.3, 0.8, "LuShieldCheck", ("Individual work: ", "discuss ideas, but write and check your own code. AI "
                                                           "assistants are allowed; you own every number."), "Ex rules",
        dark=True, size=12)

# 35  Takeaways
s = add_slide("Titel und Inhalt", "Key takeaways",
              notes="If students remember one thing: in a log-log model the coefficient is an elasticity, and an elasticity "
                    "turns into a price with one formula, but only if the assumptions hold and the data vary enough.")
numbered(s, 0.5, 1.35, 9.0, [
    ("OLS ", "draws the line with the smallest squared errors; each b holds the other variables constant"),
    ("Logs ", "turn coefficients into elasticities: brand 1, −3.64"),
    ("Look, then test: ", "residual plots, Durbin-Watson, Breusch-Pagan, Jarque-Bera, VIF"),
    ("Fix what fails: ", "robust or HAC errors, better form, more variation; experiments for causality"),
    ("Decide: ", "p* = cost × ε / (1 + ε), with the caveats")], "Takeaways", row_h=0.64, gap=0.09, size=12)
callout(s, 5.0, 0.5, "LuWallet", ("Next session: ", "the marketing mix model, a regression with adstock and saturation."),
        "Takeaway next", dark=True, size=12)

# 36  References
s = add_slide("Titel und Inhalt", "References",
              notes="Core readings first. All sources are listed with notes in instructor/resources/"
                    "regression-resource-guide.md.")
refs_l = [("Bojinov, I. I., Parzen, M. & Hamilton, P. J. (2025). ", "Linear Regression. HBS note 9-622-100 (Canvas)."),
          ("Skiera, B., Reiner, J. & Albers, S. (2022). ", "Regression analysis. In Homburg et al. (eds), Handbook of "
                                                          "Market Research, 299–327. Springer."),
          ("Wooldridge, J. M. (2025). ", "Introductory Econometrics, 8th ed. Cengage."),
          ("Hanssens, D. M., Parsons, L. J. & Schultz, R. L. (2001). ", "Market Response Models. Kluwer."),
          ("Bijmolt, T., van Heerde, H. & Pieters, R. (2005). ", "Journal of Marketing Research 42(2)."),
          ("Gordon, B. R. et al. (2019). ", "Marketing Science 38(2).")]
refs_r = [("James, G. et al. (2023). ", "ISLP, ch. 3 and the Python lab (free)."),
          ("Schwarz, Chapman & Feit (2020). ", "Python for Marketing Research and Analytics, ch. 7. Springer."),
          ("statsmodels. ", "Documentation and example notebooks."),
          ("Turrell, A. ", "Coding for Economists: regression and diagnostics (free)."),
          ("StatQuest. ", "Linear regression, clearly explained (video)."),
          ("DataCamp. ", "Introduction to Regression with statsmodels in Python.")]
cw2 = (9.0 - GAP) / 2
for k, (head, ic, refs) in enumerate([("Academic", "LuBookOpen", refs_l), ("Learning resources", "LuCode", refs_r)]):
    x = 0.5 + k * (cw2 + GAP)
    box(s, x, 1.35, cw2, 0.45, ACC, f"Ref {k + 1} header")
    text(s, x + 0.15, 1.35, cw2 - 0.75, 0.45, [head], f"Ref {k + 1} heading", size=HEAD, col=WHITE, bold=True, head=True,
         anchor=MSO_ANCHOR.MIDDLE)
    icon(s, ic, "white", x + cw2 - 0.48, 1.4, 0.34, f"ref {k + 1}")
    box(s, x, 1.8, cw2, 3.75, LIGHT, f"Ref {k + 1} body")
    text(s, x + 0.18, 1.9, cw2 - 0.33, 3.6, [[(lead, {"bold": True, "col": NAVY}), (rest, {})] for lead, rest in refs],
         f"Ref {k + 1} text", size=11, space=5)

# 37  Closing
add_slide("Abschlussfolie Kontakt", notes="Questions? Contact details on the card; office hours via the booking link.")

deck.save(OUT)
