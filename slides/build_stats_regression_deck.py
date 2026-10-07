"""Build the deck "Statistics refresher and linear regression" (Session 1) on the WU template (polish-slides skill).

Eleven parts in two halves. Statistics refresher (Parts 1 to 5) on a chocolate kiosk with five weeks, small enough
for a calculator: scale types; mean, median, variance, standard deviation and standard error; standardisation, normal
and standard normal distribution; covariance and correlation with the bridge to regression; the same calculations by
hand in Python with a check against the built-in functions, an exercise and quiz 1. Linear regression (Parts 6 to 11)
on real chocolate scanner data: theory, assumptions and tests, regression in the real world, the data in Python
(statsmodels and plotnine) with quiz 2, an in-class assignment and the individual coding exercise 1.
Core readings: Bojinov, Parzen & Hamilton (2025, HBS note 9-622-100) and Skiera, Reiner & Albers (2022, Handbook of
Market Research); further sources from instructor/resources/regression-resource-guide.md; two quiz questions adapted
from the quantmethods exam bank. Every number comes from make_refresher_figures.py and make_regression_figures.py
(slides/figures/ref_numbers.txt, reg_numbers.txt), which also draw the charts.

usage: python slides/build_stats_regression_deck.py TEMPLATE.pptx OUT.pptx
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




def rows_with_bar(slide, x, y, w, items, name, row_h=0.62, gap=0.08, size=12):
    for i, para in enumerate(items):
        ry = y + i * (row_h + gap)
        box(slide, x, ry, w, row_h, LIGHT, f"{name} row {i + 1}")
        box(slide, x, ry, 0.07, row_h, ACC, f"{name} bar {i + 1}")
        text(slide, x + 0.22, ry, w - 0.32, row_h, [para], f"{name} text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, size=size)


def grid(slide, rows, widths, x, y, name, row_h=0.36, size=11.5, head_fill=ACC, first_bold=True, last_bold=False,
         align=None):
    """Drawn table: header in accent1, body rows in bg2; optional bold last row (sums)."""
    for r_i, row in enumerate(rows):
        cx = x
        last = last_bold and r_i == len(rows) - 1
        for c_i, val in enumerate(row):
            w = widths[c_i]
            head_row = r_i == 0
            box(slide, cx, y + r_i * (row_h + 0.03), w - 0.03, row_h, head_fill if head_row else LIGHT,
                f"{name} {r_i + 1}-{c_i + 1}")
            col = WHITE if head_row else (NAVY if (c_i == 0 and first_bold) or last else INK)
            al = align[c_i] if align else PP_ALIGN.LEFT
            text(slide, cx + 0.1, y + r_i * (row_h + 0.03), w - 0.23, row_h,
                 [[(val, {"bold": head_row or last or (c_i == 0 and first_bold), "col": col, "size": size})]],
                 f"{name} text {r_i + 1}-{c_i + 1}", anchor=MSO_ANCHOR.MIDDLE, align=al)
            cx += w


R = PP_ALIGN.RIGHT
L_ = PP_ALIGN.LEFT


SKIERA = "Skiera, Reiner & Albers 2022"
HBS = "Bojinov, Parzen & Hamilton 2025"

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
              notes="Two halves. First a statistics refresher on a small chocolate kiosk that can be followed with a "
                    "calculator, calculated by hand in Python. Then linear regression, the workhorse of the course: every "
                    "marketing mix model is a regression with transformed variables. Theory, assumptions and tests, "
                    "real-world uses, and a first model on real chocolate scanner data. Readings: Bojinov, Parzen and "
                    "Hamilton (2025), Skiera, Reiner and Albers (2022).")
set_runs(ph(s, 0).text_frame.paragraphs[0], "International Marketing Analytics")
set_runs(ph(s, 1).text_frame.paragraphs[0], "Statistics refresher and linear regression")
set_runs(ph(s, 12).text_frame.paragraphs[0], "Session 1" + NB + "·" + NB + "WT" + NB + "2026/27")

# 2  Today
s = add_slide("Titel und Inhalt", "Today",
              notes="Two halves, eleven short parts. The refresher (Parts 1 to 5) builds the vocabulary of every "
                    "regression table: means, standard errors, z-values, correlations. Regression (Parts 6 to 11) uses it "
                    "on real chocolate data. Each half ends with a five-question quiz.")
stepper(s, 0.5, 1.35, 9.0, 0.6, ["Refresher", "Python\vby hand", "OLS\vtheory", "Tests",
                                 "Chocolate\vin Python", "In class,\vexercise"], "Plan steps", size=11)
cw2 = (9.0 - GAP) / 2
card(s, 0.5, 2.1, cw2, 2.55, "Refresher, Parts 1 to 5", [
    "Scale types: what you may calculate",
    "Mean, median, standard deviation, standard error",
    "z-scores and the normal distribution",
    "Covariance and correlation",
    "All of it by hand in Python; quiz 1"], "LuSigma", "Refresher card", head_h=0.45)
card(s, 0.5 + cw2 + GAP, 2.1, cw2, 2.55, "Regression, Parts 6 to 11", [
    "OLS, inference, fit, logs and elasticities",
    "Seven assumptions and four tests",
    "Regression in the real world",
    "statsmodels and plotnine on real data; quiz 2",
    "In-class assignment, coding exercise 1"], "LuChartLine", "Regression card", head_h=0.45)
callout(s, 4.8, 0.6, "LuBookOpen", ("Readings: ", "Bojinov, Parzen & Hamilton (2025), Linear Regression (HBS); Skiera, "
                                                 "Reiner & Albers (2022), Regression Analysis."), "Readings", dark=True,
        size=12)

# 3  Running example
s = add_slide("Titel und Inhalt", "Our example: a chocolate kiosk",
              notes="A kiosk at the university sells one chocolate bar. Over five weeks the owner tried five prices. Small "
                    "numbers on purpose: every result today can be checked with a calculator. The daily sales of one week "
                    "(right) serve for mean and median.")
text(s, 0.5, 1.35, 4.4, 0.38, [[("Five weeks, five prices", {"bold": True, "col": NAVY, "size": HEAD, "head": True})]],
     "Weeks label", anchor=MSO_ANCHOR.MIDDLE)
grid(s, [("Week", "Price (EUR)", "Bars sold"), ("1", "2.00", "110"), ("2", "2.50", "100"), ("3", "3.00", "80"),
         ("4", "3.50", "70"), ("5", "4.00", "40")], [1.2, 1.6, 1.6], 0.5, 1.8, "Weeks", row_h=0.4, size=12.5,
     align=[L_, R, R])
text(s, 5.1, 1.35, 4.4, 0.38, [[("One week, day by day", {"bold": True, "col": NAVY, "size": HEAD, "head": True})]],
     "Days label", anchor=MSO_ANCHOR.MIDDLE)
grid(s, [("Day", "Bars sold"), ("Mon", "10"), ("Tue", "12"), ("Wed", "11"), ("Thu", "13"), ("Fri (event)", "54")],
     [2.2, 2.2], 5.1, 1.8, "Days", row_h=0.4, size=12.5, align=[L_, R])
callout(s, 4.45, 0.75, "LuCalculator", ("Small on purpose: ", "every number today can be checked with a calculator, "
                                                             "then in Python."), "Kiosk calc", dark=True)

# ---------------------------------------------------------------- Part 1 -----
divider("Scale types", "Part 1 of 11" + NB + "·" + NB + "nominal, ordinal, interval, ratio",
        "The scale decides which statistics and which charts make sense.")

# 5  Four scale types
s = add_slide("Titel und Tabelle", "Four scale types",
              notes="Nominal: categories without order (brand, country, payment method): count them, report the mode. "
                    "Ordinal: ordered categories with unequal or unknown distances (star rating, size S/M/L): median and "
                    "percentiles. Interval: equal distances but no true zero (temperature in °C): differences and means "
                    "are fine, ratios are not. Ratio: true zero (price, bars sold, revenue): everything, including 'twice "
                    "as much'. Interval and ratio together are called metric; nominal and ordinal categorical.")
table(s, [("Scale", "What you can say", "Kiosk example", "Typical statistics"),
          ("Nominal", "same or different", "brand, payment method", "counts, mode"),
          ("Ordinal", "more or less", "rating 1 to 5 stars, size S/M/L", "median, percentiles"),
          ("Interval", "how much more (no true zero)", "temperature in °C", "mean, standard deviation"),
          ("Ratio", "how many times (true zero)", "price, bars sold, revenue", "all, incl. ratios")],
      [1.5, 2.6, 2.8, 2.1], "Scales table", size=12.5, top=1.35, row_margin=60000)
callout(s, 4.0, 0.7, "LuLayers", ("Two groups: ", "nominal and ordinal are categorical; interval and ratio are metric "
                                                 "(numbers you can average)."), "Scale groups", dark=True)
text(s, 0.5, 4.85, 9.0, 0.4, [[("In regression: ", {"bold": True, "col": NAVY, "size": 12}),
                               ("categorical variables enter as dummies (0/1), metric variables as they are.",
                                {"size": 12})]], "Scale reg", anchor=MSO_ANCHOR.MIDDLE)

# 6  Why it matters + quiz
s = add_slide("Titel und Inhalt", "Why the scale matters",
              notes="20 °C is not twice as warm as 10 °C (in Kelvin it is 293 versus 283). An average of star ratings "
                    "treats an ordinal scale as metric: common in practice, but a decision you should state. An 'average "
                    "brand' means nothing. Quiz answers: country nominal; satisfaction 1 to 7 ordinal (often treated as "
                    "metric); age in years ratio; store ID nominal (a number, but only a label); discount yes/no nominal "
                    "(binary, a dummy); temperature interval.")
rows_with_bar(s, 0.5, 1.35, 4.4, [("20 °C ", "is not twice as warm as 10 °C: no true zero"),
                                  ("Mean of star ratings: ", "treats ordinal as metric; say so"),
                                  ("Store ID 17: ", "a number, but only a label: nominal")], "Matter", row_h=0.78)
box(s, 5.05, 1.35, 4.45, 0.45, ACC, "Quiz head")
text(s, 5.2, 1.35, 4.15, 0.45, [[("Quick quiz: which scale?", {"bold": True, "col": WHITE, "size": HEAD, "head": True})]],
     "Quiz head text", anchor=MSO_ANCHOR.MIDDLE)
box(s, 5.05, 1.8, 4.45, 2.06, LIGHT, "Quiz body")
text(s, 5.25, 1.9, 4.1, 1.9, ["Country of the customer", "Satisfaction from 1 to 7", "Age in years", "Discount: yes or no",
                              "Temperature on the day"], "Quiz items", bullets=True, size=12, space=5)
callout(s, 4.05, 0.7, "LuTarget", ("Rule: ", "check the scale before you average, chart or put a variable into a "
                                             "model."), "Matter rule", dark=True)

# ---------------------------------------------------------------- Part 2 -----
divider("Centre and spread", "Part 2 of 11" + NB + "·" + NB + "mean, median, variance, standard deviation, standard error",
        "Where are the data, how far do they scatter, and how precise is our average?")

# 8  Mean and median
s = add_slide("Titel und Inhalt", "Mean and median",
              notes="The mean adds all values and divides by n. The median is the middle value of the sorted data (with an "
                    "even n, the average of the two middle values). One event day with 54 bars pulls the mean to 20, but "
                    "the median stays at 12, which describes a normal day much better. Use the median for skewed data "
                    "(income, basket values, sales with promotions) and for ordinal scales; the mean for symmetric metric "
                    "data, and whenever totals matter (20 x 5 = 100 bars sold).")
code_block(s, 0.5, 1.35, 4.6, 0.95, "mean    x̄ = Σ x / n = 100 / 5 = 20\nmedian  middle of 10 11 12 13 54 = 12",
           "Mean formula", size=12)
rows_with_bar(s, 0.5, 2.45, 4.6, [("Mean ", "uses every value; one event day pulls it up"),
                                  ("Median ", "is robust: half the days below, half above"),
                                  ("Use the median ", "for skewed data and ordinal scales")], "MM rows", row_h=0.62)
picture(s, "ref_mean_median.png", 5.25, 1.35, 4.25, 2.9,
        "Dot chart of five days: four between 10 and 13 bars, Friday at 54; a solid line at the mean of 20 and a dashed "
        "line at the median of 12")
callout(s, 4.75, 0.55, "LuLightbulb", ("Totals need the mean: ", "20 bars a day × 5 days = 100 bars in the week."),
        "MM totals", size=12)

# 9  Variance and SD by hand
s = add_slide("Titel und Inhalt", "Variance and standard deviation, by hand",
              notes="Step by step for weekly bars sold: subtract the mean (80), square the deviations so that plus and minus "
                    "do not cancel, add them up (3,000), divide by n - 1 = 4: the variance is 750 (bars squared). The square "
                    "root brings us back to bars: the standard deviation is 27.4 bars, the typical distance of a week from "
                    "the mean. Why n - 1: the deviations are measured from the sample mean, which sits closer to the data "
                    "than the true mean; dividing by n - 1 corrects this. polars, pandas and statsmodels use n - 1 for "
                    "samples.")
grid(s, [("Week", "Bars x", "x − x̄", "(x − x̄)²"), ("1", "110", "30", "900"), ("2", "100", "20", "400"),
         ("3", "80", "0", "0"), ("4", "70", "−10", "100"), ("5", "40", "−40", "1,600"), ("Sum", "400", "0", "3,000")],
     [1.0, 1.15, 1.15, 1.35], 0.5, 1.35, "Var table", row_h=0.38, size=12, last_bold=True, align=[L_, R, R, R])
code_block(s, 5.4, 1.35, 4.1, 1.35, "x̄  = 400 / 5 = 80\ns² = 3,000 / (5 − 1) = 750\ns  = √750 = 27.4 bars",
           "Var formula", size=12, caption="Variance and standard deviation")
rows_with_bar(s, 5.4, 2.85, 4.1, [("Variance ", "is in squared units (bars²)"),
                                  ("Standard deviation ", "is in bars: the typical distance from the mean")], "Var rows",
              row_h=0.58)
callout(s, 4.35, 0.85, "LuSigma", ("Why n − 1? ", "deviations from the sample mean are a little too small; dividing by n − 1 "
                                                 "corrects this. polars and pandas do it by default."), "Var n1",
        dark=True, size=12)

# 10  What SD tells you
s = add_slide("Titel und Inhalt", "Same mean, different spread",
              notes="Two kiosks sell 80 bars a week on average. Kiosk A varies between 75 and 85 (sd 3.8), kiosk B between "
                    "40 and 120 (sd 31.6). The mean alone hides this. For planning: kiosk B needs far more safety stock, and "
                    "a forecast for kiosk B is much less certain.")
picture(s, "ref_spread.png", 0.5, 1.35, 5.0, 2.73,
        "Two rows of five dots: kiosk A between 75 and 85, kiosk B between 40 and 120, a dashed line at the common mean of 80")
tw = 3.85
for i, (fig, lab) in enumerate([("3.8", "bars: sd of kiosk A"), ("31.6", "bars: sd of kiosk B")]):
    y = 1.35 + i * (1.0 + 0.1)
    box(s, 5.65, y, tw, 1.0, LIGHT, f"SD stat box {i + 1}")
    stat(s, 5.65, y, tw, 1.0, fig, lab, f"SD stat {i + 1}", fig_w=1.3, size=12)
callout(s, 4.3, 0.8, "LuShoppingCart", ("For the manager: ", "both sell 80 a week, but kiosk B needs much more safety stock "
                                                             "and its forecasts are less certain."), "SD manager",
        dark=True, size=12)

# 11  Standard error
s = add_slide("Titel und Inhalt", "Standard error: how precise is the mean?",
              notes="The standard deviation describes the customers; the standard error describes the precision of the "
                    "average we calculate from a sample. SE = s / square root of n. Spending per customer has sd EUR 4: with "
                    "16 customers the SE of the mean is EUR 1, with 64 customers EUR 0.50. Four times the sample halves the "
                    "standard error. A 95 % confidence interval is roughly mean plus or minus 2 SE (1.96 exactly): EUR 12 "
                    "plus or minus 1.96 gives 10.04 to 13.96. Every 'std err' in a regression table is a standard error.")
code_block(s, 0.5, 1.35, 9.0, 0.6, "SE = s / √n          95% confidence interval ≈ x̄ ± 1.96 · SE", "SE formula", size=12)
tw3 = (9.0 - GAP * 2) / 3
se = [("EUR" + NB + "1.00", "SE with 16 customers: 4 / √16"), ("EUR" + NB + "0.50", "SE with 64 customers: 4 / √64"),
      ("10.04–13.96", "95" + PCT + " interval for a mean spend of EUR 12 (n = 16)")]
for i, (fig, lab) in enumerate(se):
    x = 0.5 + i * (tw3 + GAP)
    box(s, x, 2.1, tw3, 1.25, LIGHT, f"SE box {i + 1}")
    box(s, x, 2.1, 0.07, 1.25, ACC, f"SE bar {i + 1}")
    text(s, x + 0.2, 2.15, tw3 - 0.3, 0.55, [[(fig, {"size": 24, "bold": True, "col": NAVY, "head": True})]],
         f"SE fig {i + 1}", anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 0.2, 2.7, tw3 - 0.3, 0.6, [lab], f"SE lab {i + 1}", size=12)
rows_with_bar(s, 0.5, 3.5, 9.0, [("sd ", "describes how much customers differ: spending varies by about EUR 4"),
                                 ("SE ", "describes how precise the average is: it shrinks with √n; four times the sample, "
                                         "half the SE")], "SE rows", row_h=0.5, gap=0.07)
callout(s, 4.7, 0.55, "LuTable", ("In every regression table: ", "the column 'std err' is the standard error of a "
                                                                "coefficient."), "SE reg", size=12)

# ---------------------------------------------------------------- Part 3 -----
divider("Standardisation and the normal distribution", "Part 3 of 11" + NB + "·" + NB + "z-scores, normal and standard "
        "normal distribution", "z-scores make different scales comparable; the normal distribution tells us how unusual a "
        "value is.")

# 13  Standardisation
s = add_slide("Titel und Inhalt", "Standardisation: z-scores",
              notes="A z-score says how many standard deviations a value lies above or below the mean. It removes the units, "
                    "so values on different scales become comparable. Vienna sold 140 bars in a week (mean 120, sd 10): "
                    "z = 2.0. Graz sold 75 (mean 60, sd 15): z = 1.0. Vienna's week was the more unusual one, although "
                    "Graz's increase looks large. In our kiosk, week 5 with 40 bars has z = (40 - 80) / 27.4 = -1.46. A "
                    "standardised variable always has mean 0 and standard deviation 1; standardised regression coefficients "
                    "use exactly this.")
code_block(s, 0.5, 1.35, 9.0, 0.6, "z = (x − x̄) / s        a standardised variable has mean 0 and standard deviation 1",
           "Z formula", size=12)
grid(s, [("Kiosk", "Bars this week", "Mean", "sd", "z"), ("Vienna", "140", "120", "10", "+2.0"),
         ("Graz", "75", "60", "15", "+1.0"), ("Our kiosk, week 5", "40", "80", "27.4", "−1.46")],
     [2.6, 1.7, 1.4, 1.4, 1.9], 0.5, 2.1, "Z table", row_h=0.45, size=12.5, align=[L_, R, R, R, R])
callout(s, 4.1, 0.75, "LuScale", ("Read it: ", "Vienna's week lies 2 standard deviations above normal, Graz's only 1: "
                                               "Vienna's week was the more unusual one."), "Z read", dark=True)
text(s, 0.5, 4.95, 9.0, 0.4, [[("Use: ", {"bold": True, "col": NAVY, "size": 12}),
                               ("compare across stores, countries or units; spot outliers (|z| > 3); standardised "
                                "coefficients.", {"size": 12})]], "Z use", anchor=MSO_ANCHOR.MIDDLE)

# 14  Normal distribution
s = add_slide("Titel und Inhalt", "The normal distribution",
              notes="A machine fills 100 g bars; the weights are normally distributed with mean 100 g and sd 2 g. The bell "
                    "curve is fully described by mean and standard deviation. The 68-95-99.7 rule: 68 % of bars lie within "
                    "one sd (98 to 102 g), 95 % within two (96 to 104 g; exactly 1.96 sd), 99.7 % within three (94 to "
                    "106 g). Many sums and averages are approximately normal even when single values are not (central "
                    "limit theorem): this is why means and regression coefficients can be tested with the normal curve.")
picture(s, "ref_normal.png", 0.5, 1.35, 4.6, 3.0,
        "Bell curve of bar weights centred at 100 g; the band from 98 to 102 g shaded dark (68 %), from 96 to 104 g light "
        "(95 %)")
rule = [("68" + PCT, "within ±1 sd: 98 to 102 g"), ("95" + PCT, "within ±2 sd: 96 to 104 g"),
        ("99.7" + PCT, "within ±3 sd: 94 to 106 g")]
for i, (fig, lab) in enumerate(rule):
    y = 1.35 + i * (0.8 + 0.08)
    box(s, 5.25, y, 4.25, 0.8, LIGHT, f"Rule box {i + 1}")
    stat(s, 5.25, y, 4.25, 0.8, fig, lab, f"Rule stat {i + 1}", fig_w=1.8, size=12)
callout(s, 4.5, 0.75, "LuLightbulb", ("Why it matters: ", "averages and regression coefficients are approximately normal "
                                                         "(central limit theorem), so we can test them."), "Normal why",
        dark=True, size=12)

# 15  Standard normal
s = add_slide("Titel und Inhalt", "The standard normal distribution",
              notes="Standardising any normal variable gives the standard normal distribution: mean 0, sd 1. One table (or "
                    "one line of Python) then answers every question. Share of bars below 97 g: z = (97 - 100) / 2 = -1.5, "
                    "P(Z < -1.5) = 6.7 %. The value 1.96 cuts off 2.5 % in each tail: it is the 1.96 in confidence "
                    "intervals and the critical value of a two-sided test at 5 %.")
picture(s, "ref_std_normal.png", 0.5, 1.35, 4.6, 3.0,
        "Standard normal curve from -3.5 to 3.5 with both tails beyond 1.96 shaded, each labelled 2.5 %, the centre 95 %")
grid(s, [("z", "share below z"), ("1.00", "84.1" + PCT), ("1.645", "95.0" + PCT), ("1.96", "97.5" + PCT),
         ("2.576", "99.5" + PCT)], [1.6, 2.6], 5.25, 1.35, "Z share", row_h=0.4, size=12.5, align=[L_, R])
box(s, 5.25, 3.5, 4.25, 0.85, LIGHT, "Z worked box")
box(s, 5.25, 3.5, 0.07, 0.85, ACC, "Z worked bar")
text(s, 5.45, 3.5, 4.0, 0.85, [("Bars under 97 g? ", "z = (97 − 100) / 2 = −1.5, so 6.7" + PCT + " of all bars")],
     "Z worked", anchor=MSO_ANCHOR.MIDDLE, size=12)
callout(s, 4.55, 0.7, "LuTarget", ("1.96: ", "the number behind 95" + PCT + " confidence intervals and two-sided tests at "
                                            "5" + PCT + "."), "Z196", dark=True, size=12)

# ---------------------------------------------------------------- Part 4 -----
divider("Covariance and correlation", "Part 4 of 11" + NB + "·" + NB + "do two variables move together, and how strongly?",
        "From one variable to two: price and bars sold at the kiosk.")

# 17  Covariance
s = add_slide("Titel und Inhalt", "Covariance: do price and sales move together?",
              notes="Multiply the deviation of price by the deviation of bars sold for every week. When one is above its "
                    "mean while the other is below, the product is negative (weeks 1, 2, 4 and 5); week 3 sits exactly on "
                    "both means. The sum is -85; divided by n - 1 = 4 the covariance is -21.25. The sign gives the "
                    "direction: negative, higher prices go with fewer bars. The size depends on the units (EUR x bars), so "
                    "-21.25 alone says little about strength.")
picture(s, "ref_quadrants.png", 0.5, 1.35, 4.4, 3.06,
        "Scatter plot of the five weeks, price against bars sold, split by dashed lines at the means (3.00 EUR and 80 "
        "bars); the points lie in the top-left and bottom-right quadrants, where the product of deviations is negative")
grid(s, [("Week", "p − p̄", "x − x̄", "product"), ("1", "−1.0", "30", "−30"), ("2", "−0.5", "20", "−10"),
         ("3", "0", "0", "0"), ("4", "0.5", "−10", "−5"), ("5", "1.0", "−40", "−40"), ("Sum", "", "", "−85")],
     [0.95, 1.1, 1.1, 1.3], 5.05, 1.35, "Cov table", row_h=0.36, size=12, last_bold=True, align=[L_, R, R, R])
code_block(s, 5.05, 4.05, 4.45, 0.55, "cov = −85 / (5 − 1) = −21.25", "Cov formula", size=12)
callout(s, 4.75, 0.55, "LuShuffle", ("Sign = direction; ", "the size depends on the units (EUR × bars)."), "Cov sign",
        size=12)

# 18  Correlation
s = add_slide("Titel und Inhalt", "Correlation: covariance without units",
              notes="Dividing the covariance by both standard deviations removes the units: r = -21.25 / (0.79 x 27.39) = "
                    "-0.98. r always lies between -1 and +1; -0.98 is an extremely strong negative relationship (rule of "
                    "thumb in Bojinov et al.: above 0.8 extremely strong). The gallery shows strong positive, none, strong "
                    "negative, and a U-shape where r is zero although x and y are clearly related: r only measures linear "
                    "relationships.")
code_block(s, 0.5, 1.35, 9.0, 0.6, "r = cov / (s_p · s_x) = −21.25 / (0.79 · 27.39) = −0.98          −1 ≤ r ≤ +1",
           "R formula", size=12)
picture(s, "ref_corr_gallery.png", 0.5, 2.05, 9.0, 2.3,
        "Four scatter plots: a rising cloud with r about 0.9, a shapeless cloud with r about 0, a falling cloud with r about "
        "-0.9, and a U-shaped curve with r about 0")
callout(s, 4.5, 0.7, "LuTriangleAlert", ("Two warnings: ", "r only measures straight-line relationships (the U has r ≈ 0), "
                                                          "and correlation is not causation."), "R warn", dark=True,
        size=12)
source(s, "Bojinov, Parzen & Hamilton 2025 (HBS note 9-622-100)")

# 19  Bridge to regression
s = add_slide("Titel und Inhalt", "From correlation to regression",
              notes="Ice-cream sales and sunburn correlate because sunshine drives both: correlation is not causation. The "
                    "regression slope through the five weeks is cov / var(price) = -21.25 / 0.625 = -34: each euro more, "
                    "34 bars fewer. The same building blocks (means, deviations, covariance, variance) produce the "
                    "least-squares line of Part 6.")
rows_with_bar(s, 0.5, 1.35, 9.0, [("Not causation: ", "ice-cream sales and sunburn rise together; sunshine drives both"),
                                  ("Correlation ", "says how strongly two variables move together, from −1 to +1"),
                                  ("Regression ", "says by how much y changes when x changes by one unit")],
              "Bridge rows", row_h=0.6, gap=0.08)
code_block(s, 0.5, 3.55, 9.0, 0.75, "slope b = cov(p, x) / var(p) = −21.25 / 0.625 = −34 bars per EUR\n"
                                    "line through the means: x = 80 − 34 · (p − 3)", "Slope formula", size=12)
callout(s, 4.5, 0.7, "LuChartLine", ("Next: ", "the least-squares line, built from exactly these pieces."), "Bridge next",
        dark=True)

# ---------------------------------------------------------------- Part 5 -----
divider("Python in Positron", "Part 5 of 11" + NB + "·" + NB + "mean, standard deviation, z-scores, covariance and "
        "correlation by hand, then checked", "Open sessions/01-foundations/stats_refresher.qmd and run it cell by cell "
        "with Ctrl/Cmd + Enter. Each step first calculates by hand, then checks with the built-in function.")

# 21  Step 1 mean
s = add_slide("Titel und Inhalt", "Step 1: the data and the mean",
              notes="A polars data frame from three lists. The mean by hand is the sum divided by the number of rows; "
                    "polars' mean() gives the same 80.0.")
code_block(s, 0.5, 1.35, 5.4, 3.0, """import polars as pl

kiosk = pl.DataFrame({
    "week":  [1, 2, 3, 4, 5],
    "price": [2.0, 2.5, 3.0, 3.5, 4.0],
    "units": [110, 100, 80, 70, 40],
})

n = kiosk.height                         # 5
mean_units = kiosk["units"].sum() / n    # by hand
kiosk["units"].mean()                    # check
kiosk["units"].median()""", "Mean code", size=11, caption="Python: polars")
grid(s, [("Result", "Value"), ("n", "5"), ("mean, by hand", "80.0"), ("mean(), check", "80.0"), ("median()", "80.0")],
     [2.0, 1.45], 6.05, 1.35, "Mean out", row_h=0.4, size=12, align=[L_, R])
callout(s, 4.55, 0.6, "LuPlay", ("Run it: ", "click into a cell and press Ctrl/Cmd + Enter; the result appears in the "
                                             "Console."), "Run it", size=12)

# 22  Step 2 sd
s = add_slide("Titel und Inhalt", "Step 2: variance, standard deviation, standard error",
              notes="The same steps as on the slide by hand: deviations, squares, sum, divide by n - 1, square root. polars' "
                    "std() uses n - 1 by default (ddof=1), so it matches. The standard error of the mean is sd / sqrt(n).")
code_block(s, 0.5, 1.35, 5.4, 3.0, """dev = kiosk["units"] - mean_units
dev        # 30, 20, 0, -10, -40

var_units = (dev ** 2).sum() / (n - 1)   # 750.0
sd_units = var_units ** 0.5              # 27.39
kiosk["units"].std()                     # check: n - 1

se_units = sd_units / n ** 0.5           # 12.25""", "SD code", size=11, caption="Python: by hand, then checked")
grid(s, [("Result", "Value"), ("variance", "750.0"), ("sd, by hand", "27.39"), ("std(), check", "27.39"),
         ("standard error", "12.25")], [2.0, 1.45], 6.05, 1.35, "SD out", row_h=0.4, size=12, align=[L_, R])
callout(s, 4.55, 0.6, "LuSigma", ("Note: ", "std() divides by n − 1 (ddof=1), like the formula on the slide."), "SD note",
        size=12)

# 23  Step 3 z
s = add_slide("Titel und Inhalt", "Step 3: standardise",
              notes="with_columns adds a new column; the expression subtracts the mean and divides by the standard deviation. "
                    "The z-scores have mean 0 and standard deviation 1. Week 5 lies 1.46 standard deviations below the mean.")
code_block(s, 0.5, 1.35, 5.4, 2.7, """kiosk = kiosk.with_columns(
    z_units=(pl.col("units") - pl.col("units").mean())
            / pl.col("units").std()
)
kiosk

kiosk["z_units"].mean()    # 0
kiosk["z_units"].std()     # 1""", "Z code", size=11, caption="Python: z-scores")
grid(s, [("Week", "Bars", "z"), ("1", "110", "1.10"), ("2", "100", "0.73"), ("3", "80", "0.00"), ("4", "70", "−0.37"),
         ("5", "40", "−1.46")], [1.0, 1.15, 1.3], 6.05, 1.35, "Z out", row_h=0.4, size=12, align=[L_, R, R])
callout(s, 4.55, 0.6, "LuScale", ("Read it: ", "week 5 lies 1.46 standard deviations below an average week."), "Z out read",
        size=12)

# 24  Step 4 cov and r
s = add_slide("Titel und Inhalt", "Step 4: covariance and correlation",
              notes="Deviations of both variables, multiplied week by week, summed and divided by n - 1: the covariance. "
                    "Divided by both standard deviations: the correlation. pl.cov and pl.corr check both in one line.")
code_block(s, 0.5, 1.35, 5.4, 3.0, """dev_p = kiosk["price"] - kiosk["price"].mean()
dev_u = kiosk["units"] - kiosk["units"].mean()

cov = (dev_p * dev_u).sum() / (n - 1)          # -21.25
r = cov / (kiosk["price"].std()
           * kiosk["units"].std())             # -0.981

kiosk.select(
    pl.cov("price", "units").alias("cov"),
    pl.corr("price", "units").alias("r"))      # check""", "Cov code", size=11, caption="Python: by hand, then checked")
grid(s, [("Result", "Value"), ("covariance", "−21.25"), ("correlation", "−0.981"), ("pl.cov, check", "−21.25"),
         ("pl.corr, check", "−0.981")], [2.0, 1.45], 6.05, 1.35, "Cov out", row_h=0.4, size=12, align=[L_, R])
callout(s, 4.55, 0.6, "LuShuffle", ("Same numbers ", "as by hand: the computer only saves the typing."), "Cov same",
        size=12)

# 25  Step 5 chart
s = add_slide("Titel und Inhalt", "Step 5: look at it",
              notes="plotnine takes the polars data frame directly. Always plot two variables before you trust a correlation: "
                    "the U-shape on the correlation slide had r = 0.")
code_block(s, 0.5, 1.35, 4.6, 2.2, """from plotnine import (ggplot, aes,
                      geom_point, labs)

(ggplot(kiosk, aes("price", "units"))
 + geom_point(size=3)
 + labs(x="Price (EUR)",
        y="Bars sold per week"))""", "Plot code", size=11, caption="Python: plotnine")
picture(s, "ref_quadrants.png", 5.25, 1.35, 4.25, 2.96, "The scatter plot of price against bars sold for the five weeks")
callout(s, 4.5, 0.75, "LuEye", ("Plot first: ", "a correlation can hide a curve, an outlier or two groups."), "Plot first",
        dark=True)

# 26  Your turn
s = add_slide("Titel und Inhalt", "Your turn: by hand, then in Python",
              notes="Answers: 1 day nominal-ordinal (weekday order), temperature interval, bars sold ratio. 2 mean 48, "
                    "median 50. 3 deviations 12, 7, 2, -8, -13; squares sum 430; variance 107.5; sd 10.37. 4 z of the "
                    "hottest day: (35 - 48) / 10.37 = -1.25. 5 temperature deviations -10, -5, 0, 5, 10; products -120, -35, "
                    "0, -40, -130, sum -325; covariance -81.25; sd temperature 7.91; r = -0.99. Warmer days, fewer "
                    "chocolate bars.")
stepper(s, 0.5, 1.35, 9.0, 0.5, ["Pairs, paper:\v10 minutes", "Python check:\v10 minutes"], "Turn steps", size=12)
grid(s, [("Day", "Temp. °C", "Bars"), ("Mon", "10", "60"), ("Tue", "15", "55"), ("Wed", "20", "50"), ("Thu", "25", "40"),
         ("Fri", "30", "35")], [0.95, 1.2, 1.0], 0.5, 2.0, "Turn data", row_h=0.4, size=12, align=[L_, R, R])
numbered(s, 3.85, 2.0, 5.65, [
    ("Scales: ", "which scale is each column?"),
    ("Centre: ", "mean and median of bars sold"),
    ("Spread: ", "variance and sd of bars, by hand"),
    ("z: ", "z-score of the hottest day's sales"),
    ("Together: ", "covariance and r of temperature and bars; then check all in Python")],
    "Turn q", row_h=0.5, gap=0.07, size=12)

# 27  In-class quiz
s = add_slide("Titel und Inhalt", "Quiz 1: statistics in five questions",
              notes="Three minutes alone, then compare with your neighbour; reveal the answers one by one. Answers: 1 B "
                    "(ordinal: ordered, but the distances between stars are unknown). 2 B (the median, 12; the event day "
                    "pulls the mean to 20). 3 A (SE = sd / square root of n: four times the sample halves it). 4 B (z counts "
                    "standard deviations; about 2.3 % of weeks lie that low in a normal distribution, so C is wrong). 5 B "
                    "(r measures the strength of a straight-line relationship; it says nothing about cause, and the slope "
                    "per euro is the regression coefficient, -34 bars here).")
quiz = [("1 Satisfaction from 1 to 5 stars is measured on which scale?", "A nominal · B ordinal · C ratio"),
        ("2 Daily sales 10, 12, 11, 13, 54: what describes a typical day best?",
         "A the mean (20) · B the median (12) · C the standard deviation"),
        ("3 You survey four times as many customers. The standard error of the mean …",
         "A halves · B falls to a quarter · C stays the same"),
        ("4 A week's sales have z = −2. That week was …",
         "A 2 bars below the mean · B 2 standard deviations below the mean · C 2" + PCT + " below the mean"),
        ("5 Price and bars sold have r = −0.98. What does this mean?",
         "A higher prices cause lower sales · B opposite directions, nearly linear · "
         "C 0.98 bars fewer per EUR")]
for i, (q, opts) in enumerate(quiz):
    y = 1.35 + i * (0.64 + 0.08)
    box(s, 0.5, y, 9.0, 0.64, LIGHT, f"Quiz row {i + 1}")
    box(s, 0.5, y, 0.07, 0.64, ACC, f"Quiz bar {i + 1}")
    text(s, 0.72, y, 8.7, 0.64, [[(q.strip(), {"bold": True, "col": NAVY})], [(opts.replace(" · ", "     "), {})]],
         f"Quiz text {i + 1}", anchor=MSO_ANCHOR.MIDDLE, size=12, space=1)
callout(s, 5.0, 0.5, "LuListChecks", ("3 minutes alone, ", "then compare with your neighbour. Same format as the online "
                                                          "quiz and the exam."), "Quiz how", dark=True, size=12)

# 28  Takeaways
s = add_slide("Titel und Inhalt", "Refresher: key takeaways",
              notes="The vocabulary for the rest of the course: every regression table reports means, standard errors, "
                    "z- or t-values and builds on covariances.")
numbered(s, 0.5, 1.35, 9.0, [
    ("Scale ", "first: it decides which statistics make sense"),
    ("Mean and median: ", "the median resists outliers; totals need the mean"),
    ("sd ", "describes the data; SE = sd / √n describes the precision of the mean"),
    ("z = (x − x̄) / s ", "makes values comparable; 95" + PCT + " of a normal lies within ±1.96 sd"),
    ("Covariance ", "gives the direction, correlation the strength (−1 to +1), regression the size")],
    "Takeaways", row_h=0.64, gap=0.09, size=12)
callout(s, 5.0, 0.5, "LuChartLine", ("Next: ", "linear regression on real chocolate scanner data, Parts 6 to 11."), "Take next", dark=True, size=12)
# ---------------------------------------------------------------- Part 1 -----
divider("Linear regression: theory", "Part 6 of 11" + NB + "·" + NB + "real data, simple and multiple regression, "
        "inference, fit, logs, from elasticity to price", "From the kiosk to real scanner data. Concepts first, each shown on the chocolate data. Bojinov et al. (2025) and Skiera "
        "et al. (2022) cover the same steps in more depth.")
# 30  The business question
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

# 31  Correlation
s = add_slide("Titel und Inhalt", "Correlation on real data: how strong is strong?",
              notes="The correlation r lies between -1 and +1 and measures the direction and strength of a linear "
                    "relationship. The rule of thumb in the HBS note: below 0.2 very weak, up to 0.4 weak to moderate, up "
                    "to 0.6 medium to substantial, up to 0.8 very strong, above extremely strong. Sales and own price of "
                    "brand 1 correlate at -0.94 over 68 real weeks, close to the kiosk's -0.98 from five made-up weeks. "
                    "Real data are never a perfect line: competitors, features and the season also move sales, which is "
                    "why we need multiple regression. The warnings from Part 4 still hold: linear only, not causal.")
text(s, 0.5, 1.35, 4.4, 0.35, [[("Rule of thumb for |r|", {"bold": True, "col": NAVY, "size": HEAD, "head": True})]],
     "r label", anchor=MSO_ANCHOR.MIDDLE)
grid(s, [("|r|", "Interpretation"), ("0 to 0.2", "very weak"), ("0.2 to 0.4", "weak to moderate"),
         ("0.4 to 0.6", "medium to substantial"), ("0.6 to 0.8", "very strong"), ("0.8 to 1.0", "extremely strong")],
     [1.5, 2.9], 0.5, 1.8, "r table", row_h=0.38, size=12)
box(s, 5.1, 1.35, 4.4, 1.25, LIGHT, "r stat box")
stat(s, 5.1, 1.35, 4.4, 1.25, "−0.94", "sales and own price of brand 1: an extremely strong negative relationship",
     "r stat", fig_w=1.4, size=12)
rows_with_bar(s, 5.1, 2.75, 4.4, [("Kiosk: ", "r = −0.98, five made-up weeks (Part 4)"),
                                  ("Both: ", "extremely strong, yet far from a perfect line")],
              "r warn", row_h=0.6)
callout(s, 4.4, 0.75, "LuTriangleAlert", ("Real data are never a perfect line: ", "competitors, features and the season "
                                                                                 "move sales too."), "r next", dark=True,
        x=0.5, w=9.0, size=12)
source(s, HBS + " (HBS note 9-622-100)")

# 32  Simple linear regression
s = add_slide("Titel und Inhalt", "Simple linear regression",
              notes="The line sales = 1,110 - 669 x price1 is the least-squares line for brand 1, built from the same pieces as the kiosk slope in Part 4 (cov / var). The slope says: one "
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

# 33  Least squares
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

# 34  Multiple regression
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

# 35  Inference
s = add_slide("Titel und Inhalt", "Is the effect real? t-test, p-value, interval, F-test",
              notes="Every coefficient comes with a standard error (Part 2). t = b / se tests whether the true coefficient is zero; "
                    "the p-value is the probability of a t this extreme if it were zero; below 0.05 we call it significant. "
                    "The 95 % confidence interval is about b plus or minus two standard errors. The F-test asks whether "
                    "all slopes together are zero. For brand 1: own-price elasticity -3.64, se 0.30, t -12.1, interval "
                    "-4.24 to -3.04; F = 59.5, p < 0.001. The 1.96 from Part 3 is behind the 'about 2'.")
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

# 36  Fit
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

# 37  Functional forms and dummies
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

# 38  From elasticity to price
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
divider("Assumptions and tests", "Part 7 of 11" + NB + "·" + NB + "what OLS assumes, how to look, how to test, what to do",
        "Look first (residual plots), then test, then decide. Skiera et al. (2022) recommend checking multicollinearity, "
        "autocorrelation and heteroscedasticity in every model.")

# 40  Assumptions overview
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

# 41  Look first
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

# 42  Then test
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

# 43  When tests fail
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

# 44  Two warnings from the data
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

# 45  Endogeneity
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
divider("Regression in the real world", "Part 8 of 11" + NB + "·" + NB + "benchmarks, companies, what transfers to MMM",
        "Regression is everywhere in marketing practice, usually with a different name.")

# 47  Benchmarks
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

# 48  Companies
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
divider("The chocolate data in Python", "Part 9 of 11" + NB + "·" + NB + "load and plot, the first regression, the log-log "
        "model, the checks", "Live in Positron. The code on the next slides is complete: copy it into a Quarto file "
        "and run it cell by cell.")

# 50  The data
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

# 51  Step 1 load and plot
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

# 52  Step 2 first regression
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

# 53  Step 3 log-log model
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

# 54  Step 4 checks
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

# 55  In-class quiz
s = add_slide("Titel und Inhalt", "Quiz 2: regression in five questions",
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
divider("In-class assignment", "Part 10 of 11" + NB + "·" + NB + "groups of 3, 25 minutes, on the chocolate data",
        "Run the code from Part 4, then answer the four questions. One group presents per question.")

# 57  In-class assignment
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
divider("Coding exercise 1", "Part 11 of 11" + NB + "·" + NB + "individual, 5" + PCT + " of the grade",
        "The first of four coding exercises. It applies the code of this session to a similar task.")

# 59  Exercise tasks
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

# 60  Exercise rules and grading
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

# 61  Takeaways
s = add_slide("Titel und Inhalt", "Regression: key takeaways",
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

# 62  References
s = add_slide("Titel und Inhalt", "References: statistics refresher",
              notes="Field is the friendliest textbook for students without a statistics background; Seeing Theory and "
                    "StatQuest visualise every concept of today.")
refs_l = [("Field, A. (2024). ", "Discovering Statistics Using IBM SPSS Statistics, 6th ed. SAGE. Chapters 1 to 2 and 8."),
          ("Hair, J. F. et al. (2019). ", "Multivariate Data Analysis, 8th ed. Cengage. Chapter 2."),
          ("Stock, J. H. & Watson, M. W. (2019). ", "Introduction to Econometrics, 4th ed. Pearson. Chapters 2 to 3.")]
refs_r = [("Seeing Theory. ", "Brown University: interactive visual introduction to probability and statistics (free)."),
          ("StatQuest. ", "Videos on the normal distribution, standard deviation vs standard error, covariance and "
                          "correlation (free)."),
          ("polars documentation. ", "mean, median, std, cov, corr."),
          ("Gelman, Hill & Vehtari (2020). ", "Regression and Other Stories, ch. 3 to 4 (free PDF).")]
cw2 = (9.0 - GAP) / 2
for k, (head, ic, refs) in enumerate([("Books and readings", "LuBookOpen", refs_l), ("Online", "LuCode", refs_r)]):
    x = 0.5 + k * (cw2 + GAP)
    box(s, x, 1.35, cw2, 0.45, ACC, f"Ref {k + 1} header")
    text(s, x + 0.15, 1.35, cw2 - 0.75, 0.45, [head], f"Ref {k + 1} heading", size=HEAD, col=WHITE, bold=True, head=True,
         anchor=MSO_ANCHOR.MIDDLE)
    icon(s, ic, "white", x + cw2 - 0.48, 1.4, 0.34, f"ref {k + 1}")
    box(s, x, 1.8, cw2, 3.75, LIGHT, f"Ref {k + 1} body")
    text(s, x + 0.18, 1.9, cw2 - 0.33, 3.6, [[(lead, {"bold": True, "col": NAVY}), (rest, {})] for lead, rest in refs],
         f"Ref {k + 1} text", size=11.5, space=6)

# 63  References
s = add_slide("Titel und Inhalt", "References: linear regression",
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

# 64  Closing
add_slide("Abschlussfolie Kontakt", notes="Questions? Contact details on the card; office hours via the booking link.")

deck.save(OUT)