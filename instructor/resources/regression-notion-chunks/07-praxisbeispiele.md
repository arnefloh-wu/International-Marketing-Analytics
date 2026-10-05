### Praxisbeispiele (9)
<table fit-page-width="true" header-row="true">
	<tr>
		<td>Kategorie</td>
		<td>Titel / Name</td>
		<td>Autor / Quelle / Firma</td>
		<td>Link</td>
		<td>Notiz</td>
		<td>Verwendung im Kurs</td>
		<td>Status</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>Cross-national differences in market response (Datta, van Heerde, Dekimpe and Steenkamp 2022)</td>
		<td>Hannes Datta, Harald J. van Heerde, Marnik G. Dekimpe and Jan-Benedict E. M. Steenkamp, \*Journal of Marketing Research\* 59(2), 2022, article.</td>
		<td>[https://doi.org/10.1177/00222437211058102](https://doi.org/10.1177/00222437211058102)</td>
		<td>1,600+ brands, 14 categories, 14 Indo-Pacific Rim countries over 10+ years: average price elasticity -0.42, line-length 0.46, distribution 0.37, with elasticities explained by brand, category and country factors; high power distance (Hofstede) and income inequality lower price and distribution elasticities. A direct model for the course's "elasticity moderated by culture" exercise.</td>
		<td>session 1 case (second-stage regression of elasticities on Hofstede and GDP) and session 3. Paywalled; check WU library access.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>CUPED: regression adjustment in A/B tests at Microsoft and Booking.com</td>
		<td>Alex Deng, Ya Xu, Ron Kohavi and Toby Walker, WSDM 2013, paper (Microsoft); Simon Jackson, Booking.com, 2018, engineering blog.</td>
		<td>[https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf](https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf)</td>
		<td>Adding the pre-period metric as a covariate (essentially regression adjustment) cuts variance and required sample size; Booking.com explains why tiny conversion effects across 1.5 million room nights a day need it. Shows students that "controls" in regression matter even in randomised experiments.</td>
		<td>session 4 (experiments and geo-lift). Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>DoorDash CUPAC and Glovo covariate adjustment</td>
		<td>DoorDash Engineering, 2020 (date unverified), blog; Glovo Engineering (Barcelona), Medium blog (date unverified).</td>
		<td>[https://careersatdoordash.com/blog/improving-experimental-power-through-control-using-predictions-as-covariate-cupac/](https://careersatdoordash.com/blog/improving-experimental-power-through-control-using-predictions-as-covariate-cupac/)</td>
		<td>Extends CUPED by using a machine-learned prediction of the outcome as the regression covariate (CUPAC); Glovo, a European delivery platform, compares covariate-adjustment estimators in practice.</td>
		<td>session 4 extension reading; Glovo is a possible European guest-speaker lead. Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>Uber Labs: mediation modelling and causal inference</td>
		<td>Uber Engineering blog (Uber Labs: Totte Harinen, Bonnie Li and colleagues), 2019, engineering blog posts.</td>
		<td>[https://www.uber.com/us/en/blog/causal-inference-at-uber/](https://www.uber.com/us/en/blog/causal-inference-at-uber/)</td>
		<td>Uses mediation analysis to explain why a product change moved an outcome (for example, how delivery delays affect future Uber Eats engagement) and to promote a proven mediator to a short-term KPI. A business example of mediation beyond survey research, with the causal caveats spelled out.</td>
		<td>session 1 or 4 example of mediation (marketing action to intermediate metric to sales). Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>Google geo experiments: geo-based and time-based regression</td>
		<td>Jon Vaver and Jim Koehler, Google, 2011, white paper; Jouni Kerman, Peng Wang and Jon Vaver, Google, 2017, white paper.</td>
		<td>[https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/)</td>
		<td>Ad effectiveness (iROAS) estimated by weighted regression of post-period response on pre-period response across geos (GBR), and by a time-series regression of treated on control markets (TBR). Exactly the bridge from regression to the geo-lift test in session 4.</td>
		<td>session 4 reading and lab rationale for geolift_germany.csv. Free.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>Facebook advertising RCTs vs observational regression (Gordon, Zettelmeyer, Bhargava and Chapsky 2019)</td>
		<td>Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava and Dan Chapsky, \*Marketing Science\* 38(2), 2019, article.</td>
		<td>[https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf](https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf)</td>
		<td>15 Facebook campaigns run as RCTs (500 million user-experiment observations): matching and regression-based observational methods often overstated lift, sometimes by a factor of three or more. The strongest evidence for why regression coefficients on ad exposure are not automatically causal.</td>
		<td>session 4 case (experiments vs models). Free working-paper PDF.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>Walmart and the M5 forecasting competition</td>
		<td>Spyros Makridakis, Evangelos Spiliotis and Vassilios Assimakopoulos, \*International Journal of Forecasting\*, 2022, article; Walmart forecasting team (Brian Seaman and colleagues; authorship unverified), "Applicability of the M5 to Forecasting at Walmart", IJF 2022, commentary.</td>
		<td>[https://www.sciencedirect.com/science/article/pii/S0169207021001874](https://www.sciencedirect.com/science/article/pii/S0169207021001874)</td>
		<td>Forecasting Walmart unit sales showed that pure extrapolation fails without price, promotion, holiday and event regressors; Walmart's own commentary explains what transfers to production forecasting.</td>
		<td>session 4 reading (forecasting as regression with promotion covariates). Results paper open access (unverified); commentary paywalled.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>Meta Robyn: ridge regression MMM in production</td>
		<td>Meta Marketing Science (facebookexperimental), 2021 to 2026, open-source software and documentation (R stable; Python version in beta).</td>
		<td>[https://github.com/facebookexperimental/Robyn](https://github.com/facebookexperimental/Robyn)</td>
		<td>A widely used industry MMM that is, at its core, a ridge regression on adstocked and saturated media variables with trend and seasonality decomposed by Prophet: the clearest real-world proof that MMM is time-series regression with transformed regressors.</td>
		<td>session 2 (link OLS MMM to industry practice). Free, MIT.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Praxisbeispiele</td>
		<td>statworx: Food for Regression, price elasticity from sales data</td>
		<td>statworx (Frankfurt data-science consultancy), blog post (date unverified).</td>
		<td>[https://www.statworx.com/en/content-hub/blog/food-for-regression-using-sales-data-to-identify-price-elasticity](https://www.statworx.com/en/content-hub/blog/food-for-regression-using-sales-data-to-identify-price-elasticity)</td>
		<td>A German consultancy's worked example of estimating price elasticity with log-log regression on retail sales, including the pitfalls (promotions, endogeneity, too little price variation). statworx is a realistic DACH guest-speaker lead.</td>
		<td>session 1 reading alongside the "Is our price too high in Poland?" exercise. Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
</table>