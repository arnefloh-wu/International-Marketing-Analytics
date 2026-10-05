"""Run the package examples shown in the set-up deck and save their output as pictures.

The code blocks below are the ones printed on the slides (polars, plotnine, Great Tables,
statsmodels), so every snippet in the deck is known to run on the course data.
Writes slides/figures/plotnine_example.png, great_tables_example.png and
example_output.txt (numbers quoted on the slides).

usage: python slides/make_setup_figures.py     (from the repository root, course .venv)
The Great Tables picture is a headless-Chromium screenshot; set CHROMIUM if it is not
at /opt/pw-browsers/chromium.
"""
import os
import subprocess
import tempfile
from pathlib import Path

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)

# --- polars (slide: polars) ------------------------------------------------------------
import polars as pl

sales = pl.read_csv("data/mmm/alpenglow_weekly.csv", try_parse_dates=True)

summary = (
    sales
    .filter(pl.col("week").dt.year() == 2025)
    .group_by("country")
    .agg(pl.col("revenue_eur_k").sum().alias("revenue"),
         pl.col("spend_tv_k").sum().alias("tv"))
    .sort("revenue", descending=True)
)

# --- plotnine (slide: plotnine) --------------------------------------------------------
from plotnine import aes, facet_wrap, geom_line, ggplot, labs, scale_x_date, theme_minimal

chart = (
    ggplot(sales.filter(pl.col("country").is_in(["AT", "DE"])),
           aes(x="week", y="sales_units_k"))
    + geom_line(color="#0096D3")
    + facet_wrap("country")
    + scale_x_date(date_breaks="1 year", date_labels="%Y")
    + labs(x="", y="Sales (k units)")
    + theme_minimal()
)
chart.save(OUT / "plotnine_example.png", width=4.5, height=2.4, dpi=300, verbose=False)

# --- Great Tables (slide: Great Tables) ------------------------------------------------
from great_tables import GT

table = (
    GT(summary)
    .tab_header(title="Revenue and TV spend, 2025")
    .fmt_number(columns=["revenue", "tv"], decimals=0)
    .cols_label(country="Country", revenue="Revenue (k EUR)", tv="TV spend (k EUR)")
)
html = "<html><body style='margin:0;padding:12px;background:white'>" + table.as_raw_html() + "</body></html>"
with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
    f.write(html)
chromium = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
shot = OUT / "great_tables_example.png"
subprocess.run([chromium, "--headless", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=2",
                "--window-size=560,520", f"--screenshot={shot}", f"file://{f.name}"],
               check=True, capture_output=True)
from PIL import Image, ImageChops  # crop the white margin around the table

img = Image.open(shot).convert("RGB")
box = ImageChops.difference(img, Image.new("RGB", img.size, "white")).getbbox()
img.crop((box[0] - 16, box[1] - 16, box[2] + 16, box[3] + 16)).save(shot)

# --- statsmodels (slide: statsmodels) ---------------------------------------------------
import statsmodels.formula.api as smf

at = sales.filter(pl.col("country") == "AT").to_pandas()
model = smf.ols(
    "sales_units_k ~ price_eur + spend_tv_k"
    " + spend_paid_search_k",
    data=at).fit()

with open(OUT / "example_output.txt", "w") as f:
    f.write(str(summary) + "\n\n")
    f.write(model.params.round(2).to_string() + f"\nR-squared {model.rsquared:.2f}  n {int(model.nobs)}\n")
print((OUT / "example_output.txt").read_text())
