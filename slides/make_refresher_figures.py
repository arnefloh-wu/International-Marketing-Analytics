"""Charts and numbers for the deck "Statistics refresher" (01b).

The running example is a chocolate kiosk: five weeks of price (EUR) and units sold, small enough to calculate
by hand. Writes to slides/figures/:
  ref_mean_median.png    five days of kiosk sales with one event day: mean versus median
  ref_spread.png         two kiosks with the same mean and a different spread
  ref_normal.png         weights of 100 g bars: normal curve with the 68-95-99.7 bands
  ref_std_normal.png     the standard normal distribution with the outer 5 % shaded (|z| > 1.96)
  ref_quadrants.png      price against units sold for the five weeks, split at the means (covariance signs)
  ref_corr_gallery.png   four scatter plots: r = 0.9, 0, -0.9 and a U-shape with r = 0
  ref_numbers.txt        every number quoted on the slides

usage: python slides/make_refresher_figures.py     (from the repository root, course .venv)
"""
from math import erf, sqrt
from pathlib import Path

import numpy as np
import pandas as pd
from plotnine import (aes, annotate, element_blank, element_text, facet_wrap, geom_area, geom_hline, geom_line,
                      geom_point, geom_vline, ggplot, labs, scale_x_continuous, scale_y_continuous, theme,
                      theme_minimal)

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
NAVY, BLUE, LIGHTBLUE, INK = "#002350", "#0096D3", "#B3DDF2", "#404040"
BASE = 11
notes = []


def look(p):
    return (p + theme_minimal(base_size=BASE)
            + theme(panel_grid_minor=element_blank(), axis_title=element_text(size=BASE, color=INK),
                    axis_text=element_text(size=BASE - 1, color=INK),
                    strip_text=element_text(size=BASE, color=NAVY, ha="left", weight="bold")))


def phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


# the five weeks
price = np.array([2.0, 2.5, 3.0, 3.5, 4.0])
units = np.array([110, 100, 80, 70, 40])
n = len(units)
dp, du = price - price.mean(), units - units.mean()
var_p, var_u = (dp ** 2).sum() / (n - 1), (du ** 2).sum() / (n - 1)
cov = (dp * du).sum() / (n - 1)
r = cov / np.sqrt(var_p * var_u)
notes += [f"weeks: price {price.tolist()}, units {units.tolist()}",
          f"mean price {price.mean():.2f}, mean units {units.mean():.1f}",
          f"units deviations {du.tolist()}, squared {(du ** 2).tolist()}, sum {(du ** 2).sum():.0f}",
          f"var units {var_u:.1f}, sd units {np.sqrt(var_u):.2f}; var price {var_p:.4f}, sd price {np.sqrt(var_p):.4f}",
          f"products {(dp * du).tolist()}, sum {(dp * du).sum():.1f}, cov {cov:.2f}, r {r:.3f}",
          f"slope cov/var(price) = {cov / var_p:.1f} units per EUR; z of week 5 units {(units[4] - units.mean()) / np.sqrt(var_u):.2f}",
          f"z units all: {np.round(du / np.sqrt(var_u), 2).tolist()}",
          f"check numpy: {np.std(units, ddof=1):.2f}, {np.corrcoef(price, units)[0, 1]:.3f}"]

# mean vs median: five days with one event day
days = pd.DataFrame({"day": ["Mon", "Tue", "Wed", "Thu", "Fri"], "units": [10, 12, 11, 13, 54]})
days["day"] = pd.Categorical(days["day"], categories=days["day"], ordered=True)
notes.append(f"days: mean {days.units.mean():.1f}, median {days.units.median():.1f}")
p = (ggplot(days, aes("day", "units")) + geom_point(color=NAVY, size=4)
     + geom_hline(yintercept=days.units.mean(), color=BLUE, size=1)
     + geom_hline(yintercept=days.units.median(), color=NAVY, linetype="dashed", size=1)
     + annotate("text", x=1.0, y=days.units.mean() + 3, label="mean 20", color=BLUE, ha="left", size=BASE)
     + annotate("text", x=1.0, y=days.units.median() + 3, label="median 12", color=NAVY, ha="left", size=BASE)
     + labs(x="", y="Bars sold"))
look(p).save(OUT / "ref_mean_median.png", width=4.4, height=3.0, dpi=300, verbose=False)

# spread: same mean, different sd
spread = pd.DataFrame({"kiosk": ["Kiosk A"] * 5 + ["Kiosk B"] * 5,
                       "units": [75, 78, 80, 82, 85, 40, 60, 80, 100, 120]})
sd_a, sd_b = spread.groupby("kiosk").units.std()
notes.append(f"spread: kiosk A sd {sd_a:.1f}, kiosk B sd {sd_b:.1f}, both mean 80")
p = (ggplot(spread, aes("units", "kiosk")) + geom_vline(xintercept=80, color=BLUE, linetype="dashed")
     + geom_point(color=NAVY, size=4) + labs(x="Bars sold per week", y=""))
look(p).save(OUT / "ref_spread.png", width=4.4, height=2.4, dpi=300, verbose=False)

# normal distribution: bar weights
x = np.linspace(92, 108, 400)
dens = np.exp(-0.5 * ((x - 100) / 2) ** 2) / (2 * np.sqrt(2 * np.pi))
nd = pd.DataFrame({"x": x, "d": dens})
p = (ggplot(nd, aes("x", "d"))
     + geom_area(nd[(nd.x >= 96) & (nd.x <= 104)], fill=LIGHTBLUE)
     + geom_area(nd[(nd.x >= 98) & (nd.x <= 102)], fill=BLUE, alpha=0.7)
     + geom_line(color=NAVY, size=1)
     + annotate("text", x=100, y=0.08, label="68 %", color="white", size=BASE)
     + annotate("text", x=103.0, y=0.03, label="95 %", color=NAVY, size=BASE)
     + scale_x_continuous(breaks=[94, 96, 98, 100, 102, 104, 106]) + scale_y_continuous(breaks=[])
     + labs(x="Weight of a 100 g bar (g)", y=""))
look(p).save(OUT / "ref_normal.png", width=4.6, height=3.0, dpi=300, verbose=False)
notes.append(f"bars: P(weight < 97 g) = P(z < -1.5) = {phi(-1.5):.4f}; 95 % between {100 - 1.96 * 2:.2f} and "
             f"{100 + 1.96 * 2:.2f} g")

# standard normal
z = np.linspace(-3.5, 3.5, 400)
sd_ = pd.DataFrame({"z": z, "d": np.exp(-0.5 * z ** 2) / np.sqrt(2 * np.pi)})
p = (ggplot(sd_, aes("z", "d"))
     + geom_area(sd_[sd_.z <= -1.96], fill=BLUE) + geom_area(sd_[sd_.z >= 1.96], fill=BLUE)
     + geom_line(color=NAVY, size=1)
     + annotate("text", x=-2.6, y=0.06, label="2.5 %", color=NAVY, size=BASE)
     + annotate("text", x=2.6, y=0.06, label="2.5 %", color=NAVY, size=BASE)
     + annotate("text", x=0, y=0.15, label="95 %", color=NAVY, size=BASE)
     + scale_x_continuous(breaks=[-3, -1.96, -1, 0, 1, 1.96, 3], labels=["-3", "-1.96", "-1", "0", "1", "1.96", "3"])
     + scale_y_continuous(breaks=[]) + labs(x="z", y=""))
look(p).save(OUT / "ref_std_normal.png", width=4.6, height=3.0, dpi=300, verbose=False)
notes.append("standard normal: " + ", ".join(f"P(Z<{v}) = {phi(v):.3f}" for v in (1, 1.645, 1.96, 2.576)))

# quadrants for covariance
wk = pd.DataFrame({"price": price, "units": units, "week": [f"W{i}" for i in range(1, 6)]})
p = (ggplot(wk, aes("price", "units"))
     + geom_vline(xintercept=price.mean(), color=BLUE, linetype="dashed")
     + geom_hline(yintercept=units.mean(), color=BLUE, linetype="dashed")
     + geom_point(color=NAVY, size=4)
     + annotate("text", x=wk.price + 0.12, y=wk.units + 4, label=wk.week, color=NAVY, size=BASE - 1)
     + annotate("text", x=2.35, y=119, label="price −, units +  →  −", color=BLUE, size=BASE - 1)
     + annotate("text", x=3.65, y=118, label="+", color=INK, size=BASE + 2)
     + annotate("text", x=2.3, y=40, label="+", color=INK, size=BASE + 2)
     + annotate("text", x=3.67, y=31, label="price +, units −  →  −", color=BLUE, size=BASE - 1)
     + scale_x_continuous(limits=(1.8, 4.3)) + scale_y_continuous(limits=(28, 122))
     + labs(x="Price (EUR)", y="Bars sold per week"))
look(p).save(OUT / "ref_quadrants.png", width=4.6, height=3.2, dpi=300, verbose=False)

# correlation gallery
rng = np.random.default_rng(7)
xs = rng.normal(size=120)
noise = rng.normal(size=120)
zero = rng.normal(size=120)
zero = zero - np.polyval(np.polyfit(xs, zero, 1), xs)          # remove any linear trend: r = 0
xu = np.linspace(-2, 2, 120)                                    # symmetric x: the U has r = 0
gal = pd.concat([
    pd.DataFrame({"x": xs, "y": 0.9 * xs + 0.44 * noise, "panel": "r ≈ +0.9"}),
    pd.DataFrame({"x": xs, "y": zero, "panel": "r ≈ 0"}),
    pd.DataFrame({"x": xs, "y": -0.9 * xs + 0.44 * noise, "panel": "r ≈ −0.9"}),
    pd.DataFrame({"x": xu, "y": xu ** 2 + 0.3 * rng.normal(size=120), "panel": "U-shape: r ≈ 0"})])
gal["panel"] = pd.Categorical(gal["panel"], categories=["r ≈ +0.9", "r ≈ 0", "r ≈ −0.9", "U-shape: r ≈ 0"], ordered=True)
rs = {k: np.corrcoef(g.x, g.y)[0, 1] for k, g in gal.groupby("panel", observed=True)}
notes.append("gallery r: " + ", ".join(f"{k} {v:.2f}" for k, v in rs.items()))
p = (ggplot(gal, aes("x", "y")) + geom_point(color=NAVY, size=1.2, alpha=0.7) + facet_wrap("panel", ncol=4, scales="free_y")
     + labs(x="", y="") + theme(axis_text=element_blank()))
look(p).save(OUT / "ref_corr_gallery.png", width=9.0, height=2.3, dpi=300, verbose=False)

(OUT / "ref_numbers.txt").write_text("\n".join(notes) + "\n")
print("\n".join(notes))
