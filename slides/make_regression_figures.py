"""Charts and numbers for the deck "Linear regression" (01b), built on the real chocolate data.

Data: data/legacy/chocolate_dataset.csv (68 weeks; weekly sales of brand 1, prices, feature and display
activity of four chocolate brands, temperature, December and Easter weeks). Writes to slides/figures/:
  reg_scatter.png      sales against own price with the least-squares line
  reg_residuals.png    the least-squares idea: residuals as vertical distances to the line
  reg_sales_time.png   weekly sales over 68 weeks, promotion weeks (price below 1.2) marked
  reg_resid_fitted.png residuals against fitted values of the main model
  reg_resid_hist.png   histogram of the residuals of the main model
  reg_resid_time.png   residuals over time (autocorrelation)
  reg_numbers.txt      every number quoted on the slides

usage: python slides/make_regression_figures.py     (from the repository root, course .venv)
"""
from pathlib import Path

import numpy as np
import polars as pl
import statsmodels.formula.api as smf
from plotnine import (aes, element_blank, element_text, geom_col, geom_histogram, geom_hline, geom_line, geom_point,
                      geom_segment, geom_smooth, ggplot, labs, scale_color_manual, theme, theme_minimal)
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson, jarque_bera

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
NAVY, BLUE, INK = "#002350", "#0096D3", "#404040"
BASE = 11


def look(p):
    return (p + theme_minimal(base_size=BASE)
            + theme(panel_grid_minor=element_blank(), axis_title=element_text(size=BASE, color=INK),
                    axis_text=element_text(size=BASE - 1, color=INK), legend_position="top",
                    legend_title=element_blank(), legend_text=element_text(size=BASE - 1)))


choc = pl.read_csv("data/legacy/chocolate_dataset.csv")
df = choc.with_columns((pl.col("price1") < 1.2).alias("promo")).to_pandas()
notes = []

# simple and log-log models
simple = smf.ols("sales ~ price1", data=df).fit()
loglog = smf.ols("np.log(sales) ~ np.log(price1)", data=df).fit()
FORMULA = ("np.log(sales) ~ np.log(price1) + np.log(price2) + np.log(price3) + np.log(price4)"
           " + feature1 + temp + december")
main = smf.ols(FORMULA, data=df).fit()
notes += [f"n = {len(df)} weeks; mean sales {df.sales.mean():.1f}; mean price1 {df.price1.mean():.3f}",
          f"corr(sales, price1) = {df[['sales', 'price1']].corr().iloc[0, 1]:.2f}",
          f"simple: sales = {simple.params.iloc[0]:.1f} {simple.params.iloc[1]:+.1f} * price1; R2 {simple.rsquared:.3f}; "
          f"se slope {simple.bse.iloc[1]:.1f}",
          f"log-log: elasticity {loglog.params.iloc[1]:.3f}, CI {loglog.conf_int().iloc[1, 0]:.2f} to "
          f"{loglog.conf_int().iloc[1, 1]:.2f}; R2 {loglog.rsquared:.3f}",
          "main model: " + FORMULA]
for name in main.params.index:
    ci = main.conf_int().loc[name]
    notes.append(f"  {name:<16} {main.params[name]:8.4f}  se {main.bse[name]:.4f}  p {main.pvalues[name]:.3f}  "
                 f"CI {ci.iloc[0]:.3f} to {ci.iloc[1]:.3f}")
notes.append(f"  R2 {main.rsquared:.3f}, adj R2 {main.rsquared_adj:.3f}, F {main.fvalue:.1f}, p(F) {main.f_pvalue:.2e}, "
             f"RMSE {np.sqrt(np.mean(main.resid ** 2)):.3f}")
notes.append(f"  December effect {np.exp(main.params['december']) - 1:+.1%}; temperature {np.exp(main.params['temp']) - 1:+.2%} "
             f"per degree")
eps = main.params["np.log(price1)"]
notes.append(f"  optimal price = cost x {eps / (1 + eps):.2f} (markup {eps / (1 + eps) - 1:.0%} on marginal cost)")
X = main.model.exog
vif = {n: variance_inflation_factor(X, i) for i, n in enumerate(main.model.exog_names) if n != "Intercept"}
cooks = main.get_influence().cooks_distance[0]
notes += [f"  Durbin-Watson {durbin_watson(main.resid):.2f}; Breusch-Pagan p {het_breuschpagan(main.resid, X)[1]:.3f}; "
          f"Jarque-Bera p {jarque_bera(main.resid)[1]:.3f}",
          "  VIF " + ", ".join(f"{k} {v:.2f}" for k, v in vif.items()),
          f"  Cook's distance max {cooks.max():.2f} (week {int(np.argmax(cooks)) + 1}); weeks above 4/n = {4 / len(df):.3f}: "
          f"{int((cooks > 4 / len(df)).sum())}"]
full = smf.ols(FORMULA + " + display1 + fand1 + easter", data=df).fit()
Xf = full.model.exog
vif_f = {n: variance_inflation_factor(Xf, i) for i, n in enumerate(full.model.exog_names) if n != "Intercept"}
cf = full.get_influence().cooks_distance[0]
notes.append(f"with display1, fand1, easter: VIF display1 {vif_f['display1']:.1f}, fand1 {vif_f['fand1']:.1f}; "
             f"leverage of the single Easter week {full.get_influence().hat_matrix_diag[int(np.argmax(cf))]:.2f}")
hac = main.get_robustcov_results(cov_type="HAC", maxlags=1)
notes.append(f"HAC (Newey-West, 1 lag) se of log(price1): {hac.bse[1]:.3f} vs {main.bse.iloc[1]:.3f}")

# charts
p = (ggplot(df, aes("price1", "sales")) + geom_point(color=NAVY, size=2, alpha=0.8)
     + geom_smooth(method="lm", se=False, color=BLUE, size=1)
     + labs(x="Price of brand 1", y="Weekly sales of brand 1"))
look(p).save(OUT / "reg_scatter.png", width=5.0, height=3.3, dpi=300, verbose=False)

df["fitted_s"] = simple.fittedvalues
sub = df[df.week <= 68]
p = (ggplot(sub, aes("price1", "sales")) + geom_segment(aes(xend="price1", yend="fitted_s"), color=BLUE, size=0.6)
     + geom_point(color=NAVY, size=2) + geom_line(aes(y="fitted_s"), color=NAVY, size=0.8)
     + labs(x="Price of brand 1", y="Weekly sales of brand 1"))
look(p).save(OUT / "reg_residuals.png", width=4.6, height=3.2, dpi=300, verbose=False)

p = (ggplot(df, aes("week", "sales")) + geom_line(color=NAVY, size=0.8)
     + geom_point(df[df.promo], aes("week", "sales"), color=BLUE, size=2.5)
     + labs(x="Week", y="Weekly sales of brand 1"))
look(p).save(OUT / "reg_sales_time.png", width=5.0, height=3.0, dpi=300, verbose=False)

df["fitted"], df["resid"] = main.fittedvalues, main.resid
p = (ggplot(df, aes("fitted", "resid")) + geom_hline(yintercept=0, color=INK, linetype="dashed")
     + geom_point(color=NAVY, size=2, alpha=0.8) + labs(x="Fitted values (log sales)", y="Residuals"))
look(p).save(OUT / "reg_resid_fitted.png", width=4.3, height=3.0, dpi=300, verbose=False)
p = (ggplot(df, aes("resid")) + geom_histogram(bins=15, fill=BLUE, color="white")
     + labs(x="Residuals", y="Weeks"))
look(p).save(OUT / "reg_resid_hist.png", width=4.3, height=3.0, dpi=300, verbose=False)
p = (ggplot(df, aes("week", "resid")) + geom_hline(yintercept=0, color=INK, linetype="dashed")
     + geom_col(fill=NAVY, width=0.8) + labs(x="Week", y="Residuals"))
look(p).save(OUT / "reg_resid_time.png", width=4.3, height=3.0, dpi=300, verbose=False)

(OUT / "reg_numbers.txt").write_text("\n".join(notes) + "\n")
print("\n".join(notes))
