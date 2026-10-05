"""Charts and numbers for the deck "Introduction to marketing mix modelling" (02a).

Writes to slides/figures/:
  mmm_de_sales_tv.png       weekly sales and TV spend in Germany, 2023 to 2025 (Alpenglow data)
  mmm_decomposition.png     base versus media-driven sales in Germany, 2025, from a simple OLS
  mmm_adstock.png           geometric adstock of one spend pulse, decay 0.3 and 0.7 (synthetic)
  mmm_saturation.png        a Hill saturation curve with the gain from the next EUR 10k (synthetic)
  mmm_numbers.txt           every Alpenglow number quoted on the slides

The OLS models here are deliberately simple first looks (one adstock decay for all channels,
no saturation); the sessions build the proper models. Charts: theme_minimal, WU navy #002350
and blue #0096D3, base size 11 pt, saved at the size they appear on the slide.

usage: python slides/make_mmm_figures.py     (from the repository root, course .venv)
"""
from pathlib import Path

import numpy as np
import pandas as pd
import polars as pl
import statsmodels.formula.api as smf
from plotnine import (aes, annotate, element_blank, element_text, facet_wrap, geom_area, geom_col, geom_line,
                      geom_point, geom_rect, geom_segment, ggplot, labs, scale_color_manual, scale_fill_manual,
                      scale_x_continuous, scale_x_date, scale_y_continuous, theme, theme_minimal)

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
NAVY, BLUE, GREY, INK = "#002350", "#0096D3", "#BFBFBF", "#404040"
BASE = 11
CHANNELS = ["tv", "online_video", "paid_search", "paid_social", "ooh"]


def look(p):
    return (p + theme_minimal(base_size=BASE)
            + theme(panel_grid_minor=element_blank(), panel_grid_major_x=element_blank(),
                    axis_title=element_text(size=BASE, color=INK), axis_text=element_text(size=BASE - 1, color=INK),
                    legend_position="top", legend_title=element_blank(), legend_text=element_text(size=BASE - 1),
                    strip_text=element_text(size=BASE, color=NAVY, ha="left", weight="bold")))


def adstock(x, decay):
    out, carry = np.zeros(len(x)), 0.0
    for i, v in enumerate(x):
        carry = v + decay * carry
        out[i] = carry
    return out


sales = pl.read_csv("data/mmm/alpenglow_weekly.csv", try_parse_dates=True)
de = sales.filter(pl.col("country") == "DE").to_pandas()
notes = []

# --- numbers for the "next euro" slide ------------------------------------------------------
spend_cols = [f"spend_{c}_k" for c in CHANNELS]
y25 = sales.filter(pl.col("week").dt.year() == 2025)
total_2025 = float(y25.select(pl.sum_horizontal(spend_cols).sum()).item())
rev_2025 = float(y25["revenue_eur_k"].sum())
by_ch = {c: float(y25[f"spend_{c}_k"].sum()) for c in CHANNELS}
notes.append(f"2025 media spend, six countries, five channels: {total_2025:,.0f} k EUR "
             f"({y25['week'].n_unique()} weeks); revenue {rev_2025:,.0f} k EUR")
notes.append("2025 spend share by channel: " + ", ".join(f"{c} {100 * v / total_2025:.0f}%" for c, v in by_ch.items()))

# --- 1 Germany: weekly sales and TV spend, Christmas weeks shaded --------------------------
long = pd.concat([
    pd.DataFrame({"week": de.week, "value": de.sales_units_k, "panel": "Weekly sales (thousand units)"}),
    pd.DataFrame({"week": de.week, "value": de.spend_tv_k, "panel": "Weekly TV spend (thousand EUR)"})])
long["panel"] = pd.Categorical(long.panel, ["Weekly sales (thousand units)", "Weekly TV spend (thousand EUR)"])
xmas = de[de.xmas == 1].groupby(de.week.dt.year).week.agg(["min", "max"]).reset_index(drop=True)
xmas["max"] = xmas["max"] + pd.Timedelta(days=7)
p = (ggplot()
     + geom_rect(xmas, aes(xmin="min", xmax="max"), ymin=-np.inf, ymax=np.inf, fill=GREY, alpha=0.45)
     + geom_line(long[long.panel == "Weekly sales (thousand units)"], aes("week", "value"), color=NAVY, size=0.7)
     + geom_col(long[long.panel == "Weekly TV spend (thousand EUR)"], aes("week", "value"), fill=BLUE, width=5)
     + facet_wrap("panel", ncol=1, scales="free_y")
     + scale_x_date(date_breaks="6 months", date_labels="%b %Y")
     + scale_y_continuous(labels=lambda v: [f"{x:,.0f}" for x in v])
     + labs(x="", y=""))
look(p).save(OUT / "mmm_de_sales_tv.png", width=5.6, height=3.4, dpi=300, verbose=False)
notes.append(f"DE correlation weekly sales vs TV spend: {de.sales_units_k.corr(de.spend_tv_k):.2f}")
notes.append("DE TV spend in Christmas weeks vs other weeks (mean k EUR): "
             f"{de[de.xmas == 1].spend_tv_k.mean():.0f} vs {de[de.xmas == 0].spend_tv_k.mean():.0f}")

# --- 2 Germany: decomposition into base and media (simple additive OLS) --------------------
d = de.copy()
for c in CHANNELS:
    d[f"a_{c}"] = adstock(d[f"spend_{c}_k"].to_numpy(), 0.5)
d["t"] = np.arange(len(d))
controls = "price_eur + promo_share + distribution + xmas + easter + valentine + temperature_c + consumer_confidence + competitor_spend_k + t"
ols = smf.ols("sales_units_k ~ " + controls + " + " + " + ".join(f"a_{c}" for c in CHANNELS), data=d).fit()
d["media"] = sum(ols.params[f"a_{c}"] * d[f"a_{c}"] for c in CHANNELS)
d["base"] = ols.fittedvalues - d["media"]
d25 = d[d.week.dt.year == 2025]
area = pd.concat([pd.DataFrame({"week": d25.week, "value": d25.base, "part": "Base"}),
                  pd.DataFrame({"week": d25.week, "value": d25.media, "part": "Media (five channels)"})])
area["part"] = pd.Categorical(area.part, ["Media (five channels)", "Base"])
p = (ggplot(area, aes("week", "value", fill="part"))
     + geom_area(position="stack", alpha=0.95)
     + geom_line(d25, aes("week", "sales_units_k"), inherit_aes=False, color=INK, size=0.5, linetype="dashed")
     + annotate("text", x=pd.Timestamp("2025-05-15"), y=float(d25.sales_units_k.max()) * 0.97,
                label="dashed: actual sales", size=BASE - 1, color=INK, ha="left")
     + scale_fill_manual(values={"Base": NAVY, "Media (five channels)": BLUE},
                         breaks=["Base", "Media (five channels)"])
     + scale_x_date(date_breaks="2 months", date_labels="%b")
     + scale_y_continuous(labels=lambda v: [f"{x:,.0f}" for x in v])
     + labs(x="2025", y="Weekly sales (thousand units)"))
look(p).save(OUT / "mmm_decomposition.png", width=5.4, height=3.5, dpi=300, verbose=False)
share = float(d25.media.sum() / (d25.base.sum() + d25.media.sum()))
notes.append(f"DE illustrative additive OLS (adstock 0.5 all channels): R2 {ols.rsquared:.2f}, "
             f"media share of fitted 2025 sales {100 * share:.0f}%")

# --- first log-log look: price versus TV elasticity in Germany -----------------------------
loglog = smf.ols("np.log(sales_units_k) ~ np.log(price_eur) + promo_share + distribution + xmas + easter + valentine"
                 " + temperature_c + consumer_confidence + competitor_spend_k + t + "
                 + " + ".join(f"np.log1p(a_{c})" for c in CHANNELS), data=d).fit()
notes.append(f"DE log-log OLS: price elasticity {loglog.params['np.log(price_eur)']:.2f}, "
             f"TV elasticity {loglog.params['np.log1p(a_tv)']:.2f}, R2 {loglog.rsquared:.2f}")
notes.append("DE log-log media elasticities: " + ", ".join(f"{c} {loglog.params[f'np.log1p(a_{c})']:.2f}" for c in CHANNELS))

# --- 3 Adstock: one pulse of EUR 100k in week 1, decay 0.3 and 0.7 -------------------------
weeks = np.arange(1, 13)
pulse = np.where(weeks == 1, 100.0, 0.0)
hl = {lam: np.log(0.5) / np.log(lam) for lam in (0.3, 0.7)}
lab = {lam: f"decay {lam}: half-life {hl[lam]:.1f} weeks" for lam in hl}
ad = pd.concat([pd.DataFrame({"week": weeks, "value": adstock(pulse, lam), "series": lab[lam]}) for lam in hl])
ad["series"] = pd.Categorical(ad.series, [lab[0.3], lab[0.7]])
p = (ggplot()
     + geom_col(pd.DataFrame({"week": weeks, "value": pulse}), aes("week", "value"), fill=GREY, width=0.6)
     + annotate("text", x=1.45, y=100, label="spend: EUR 100k in week 1", ha="left", size=BASE - 1, color=INK)
     + geom_line(ad, aes("week", "value", color="series"), size=0.9)
     + geom_point(ad, aes("week", "value", color="series"), size=2.2)
     + scale_color_manual(values=[BLUE, NAVY])
     + scale_x_continuous(breaks=list(range(1, 13)))
     + labs(x="Week", y="Advertising pressure (adstock, k EUR)"))
(look(p) + theme(legend_position=(0.97, 0.78), legend_justification=(1, 1), legend_direction="vertical",
                 legend_background=element_blank())).save(OUT / "mmm_adstock.png", width=5.2, height=3.3, dpi=300, verbose=False)
notes.append(f"Adstock half-life: decay 0.3 -> {hl[0.3]:.2f} weeks, decay 0.7 -> {hl[0.7]:.2f} weeks; "
             f"total effect multiplier 1/(1-decay): {1 / (1 - 0.3):.2f} and {1 / (1 - 0.7):.2f}")

# --- 4 Saturation: Hill curve, the next EUR 10k at low and at high spend --------------------
K, S, TOP = 60.0, 2.0, 120.0


def hill(x):
    return TOP * x ** S / (x ** S + K ** S)


x = np.linspace(0, 200, 401)
curve = pd.DataFrame({"spend": x, "resp": hill(x)})
steps = [(30.0, 40.0), (150.0, 160.0)]
seg = pd.DataFrame([{"x0": a, "x1": b, "y0": hill(a), "y1": hill(b)} for a, b in steps])
gains = [hill(b) - hill(a) for a, b in steps]
p = (ggplot(curve, aes("spend", "resp"))
     + geom_line(color=NAVY, size=1.0)
     + annotate("point", x=K, y=hill(K), color=NAVY, fill="white", size=3, stroke=1.2)
     + annotate("text", x=K + 6, y=hill(K) - 5, label="half-saturation: EUR 60k", ha="left", size=BASE - 1, color=INK)
     + geom_segment(seg, aes(x="x0", xend="x1", y="y0", yend="y1"), color=BLUE, size=3.2, inherit_aes=False)
     + annotate("text", x=steps[0][1] + 5, y=hill(steps[0][1]) - 14,
                label=f"next EUR 10k: +{gains[0]:.0f}k units", ha="left", size=BASE - 1, color=BLUE)
     + annotate("text", x=200, y=hill(steps[1][0]) - 18,
                label=f"next EUR 10k: +{gains[1]:.1f}k units", ha="right", size=BASE - 1, color=BLUE)
     + scale_x_continuous(breaks=[0, 50, 100, 150, 200])
     + scale_y_continuous(limits=(0, 125))
     + labs(x="Weekly spend in one channel (k EUR)", y="Extra sales (thousand units)"))
look(p).save(OUT / "mmm_saturation.png", width=5.2, height=3.3, dpi=300, verbose=False)
notes.append(f"Hill curve (K {K:.0f}, slope {S:.0f}, max {TOP:.0f}): next 10k at 30k -> +{gains[0]:.1f}k units, "
             f"at 150k -> +{gains[1]:.1f}k units")

(OUT / "mmm_numbers.txt").write_text("\n".join(notes) + "\n")
print("\n".join(notes))
