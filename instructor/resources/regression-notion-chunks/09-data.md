### Data (15)
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
		<td>Data</td>
		<td>Advertising.csv (ISLR/ISLP)</td>
		<td>James, Witten, Hastie and Tibshirani, \*An Introduction to Statistical Learning\*, dataset; 200 markets x 4 variables (TV, radio, newspaper spend in USD thousands; sales in thousand units).</td>
		<td>[https://www.statlearning.com/s/Advertising.csv](https://www.statlearning.com/s/Advertising.csv)</td>
		<td>The canonical teaching set for multiple regression, the TV x radio interaction (synergy), diminishing returns (log or square-root TV) and the "newspaper is significant alone but not jointly" lesson in omitted variables.</td>
		<td>session 1 warm-up and session 2 bridge to response curves. Free for teaching (book data).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Carseats (ISLP)</td>
		<td>ISLP package, simulated data, 400 stores x 11 variables (Sales, Price, CompPrice, Advertising, Income, ShelveLoc Bad/Medium/Good, Urban, US).</td>
		<td>[https://islp.readthedocs.io/en/latest/datasets/Carseats.html](https://islp.readthedocs.io/en/latest/datasets/Carseats.html)</td>
		<td>Ideal for dummy coding (three-level ShelveLoc and changing the reference level), price x advertising and price x US interactions, and effect coding comparisons.</td>
		<td>session 1 lab exercise. Free (BSD-style).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>OJ and Bikeshare (ISLP)</td>
		<td>ISLP package. OJ: 1,070 orange juice purchases (Citrus Hill vs Minute Maid) with prices, discounts, specials, brand loyalty and store, from Stine, Foster and Waterman, \*Business Analysis Using Regression\* (1998). Bikeshare: hourly and daily Capital Bikeshare counts 2011 to 2012 with season, holiday, weather.</td>
		<td>[https://github.com/intro-stat-learning/ISLP/tree/main/docs/source/datasets](https://github.com/intro-stat-learning/ISLP/tree/main/docs/source/datasets)</td>
		<td>OJ is a compact price-and-promotion dataset (price differences, discounts, loyalty as a moderator); Bikeshare teaches seasonal dummies, hour-of-day effects and count outcomes.</td>
		<td>sessions 1 (OJ, promotions) and 4 (Bikeshare, seasonality and time-series regression). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>dunnhumby Source Files: Breakfast at the Frat</td>
		<td>dunnhumby, dataset; 156 weeks of unit sales, spend, base and shelf price, feature (sale tag) and display for products in four categories (mouthwash, pretzels, frozen pizza, boxed cereal) across stores.</td>
		<td>[https://www.dunnhumby.com/source-files/](https://www.dunnhumby.com/source-files/)</td>
		<td>Real retail scanner data for log-log price elasticities, promotion dummies, feature x display interactions and store fixed effects, at a manageable size.</td>
		<td>session 1 extension exercise or a project alternative. Free with registration; dunnhumby terms restrict redistribution (do not commit raw files to the course repo).</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>dunnhumby: The Complete Journey (completejourney-py)</td>
		<td>dunnhumby; Python port of the R completejourney package, version 0.1.0, MIT (data under dunnhumby terms); about 2,500 households, one year of transactions, campaigns, coupons and demographics.</td>
		<td>[https://pypi.org/project/completejourney-py/](https://pypi.org/project/completejourney-py/)</td>
		<td>Household-level data for regression of spend on campaign exposure with demographic moderators (income, household size), and for discussing selection into campaigns.</td>
		<td>background or project alternative. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Dominick's Finer Foods (Kilts Center, Chicago Booth)</td>
		<td>Kilts Center for Marketing, University of Chicago Booth; about 9 years (1989 to 1997) of weekly store-level scanner data for roughly 100 Chicago stores and 3,500+ UPCs in 25+ categories, including randomised pricing experiments.</td>
		<td>[https://www.chicagobooth.edu/research/kilts/research-data/dominicks](https://www.chicagobooth.edu/research/kilts/research-data/dominicks)</td>
		<td>The classic dataset behind decades of price-elasticity and promotion research; good for log-log demand models with store and week fixed effects and for showing elasticity differences across store demographics.</td>
		<td>background or advanced project data. Free for academic research only, acknowledgement required; files are large SAS/Stata zips.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Rossmann Store Sales (Kaggle)</td>
		<td>Rossmann (German drugstore chain), Kaggle competition, 2015; daily sales for 1,115 German stores 2013 to 2015 with Promo, Promo2, school and state holidays, competitor distance and store type.</td>
		<td>[https://www.kaggle.com/datasets/pratyushakar/rossmann-store-sales](https://www.kaggle.com/datasets/pratyushakar/rossmann-store-sales)</td>
		<td>A European, marketing-relevant time series: promotion dummies, day-of-week and holiday effects, trend, lagged effects and store heterogeneity (promotion x store type moderation).</td>
		<td>session 4 (time-series regression with promotions) or session 1 promo-elasticity demo. Free with Kaggle login; competition rules govern use (check before redistributing).</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Walmart store sales and M5 (Kaggle)</td>
		<td>Walmart Recruiting Store Sales Forecasting (Kaggle, 2014): weekly sales for 45 stores by department 2010 to 2012 with holiday flags and markdowns MarkDown1 to 5. M5 (Kaggle, 2020): 3,049 products in 10 US stores over 1,941 days with prices, SNAP days and events.</td>
		<td>[https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data)</td>
		<td>Holiday dummies, promotion (markdown) effects, seasonality and hierarchical structure; M5 adds daily prices for elasticity estimation.</td>
		<td>session 4 forecasting exercise or project extension. Free with Kaggle login; competition terms apply.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Hofstede dimension data matrix</td>
		<td>Geert Hofstede / Hofstede Insights, dataset (version 2015-12-08): six dimensions (PDI, IDV, MAS, UAI, LTO, IVR) for roughly 100 countries and regions (count unverified); .csv, .xls, .sav.</td>
		<td>[https://geerthofstede.com/research-and-vsm/dimension-data-matrix/](https://geerthofstede.com/research-and-vsm/dimension-data-matrix/)</td>
		<td>The standard country-level moderator: merge with country elasticities and regress elasticity on power distance or uncertainty avoidance (as in Datta et al. 2022), or interact log price with a dimension in a pooled model.</td>
		<td>session 1 (already planned via country_meta.csv) and session 3. Free for research use; contact the owners for commercial use.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>World Bank WDI via wbgapi</td>
		<td>World Bank, World Development Indicators; wbgapi Python client version 1.0.14, 27 February 2026.</td>
		<td>[https://pypi.org/project/wbgapi/](https://pypi.org/project/wbgapi/)</td>
		<td>GDP per capita, inflation, internet penetration, Gini and population for cross-country regressions and as moderators of marketing elasticities (income inequality in Datta et al. 2022). Data are CC BY 4.0.</td>
		<td>sessions 1 and 3 (country covariates). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Eurostat via the eurostat package</td>
		<td>Eurostat; eurostat Python package version 1.1.1, 13 June 2024.</td>
		<td>[https://pypi.org/project/eurostat/](https://pypi.org/project/eurostat/)</td>
		<td>Harmonised EU retail trade volumes, HICP prices, household consumption and digital economy indicators by country and month: good for time-series regressions with seasonality and for EU cross-country panels.</td>
		<td>session 4 (monthly retail trade series) or projects. Free (Eurostat reuse policy, attribution).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Our World in Data and Gapminder</td>
		<td>Our World in Data (owid-catalog 1.2.7, 5 October 2026) and the gapminder Python package (0.1, 2018, copy of the R teaching data: 142 countries, 1952 to 2007, life expectancy, population, GDP per capita).</td>
		<td>[https://pypi.org/project/owid-catalog/](https://pypi.org/project/owid-catalog/)</td>
		<td>Gapminder is the cleanest dataset for teaching log transformations (log GDP), continent dummies and continent x GDP interactions; OWID adds hundreds of current indicators, CC BY.</td>
		<td>session 1 warm-up (logs and interactions with a non-marketing example). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>statsmodels built-in datasets and Rdatasets</td>
		<td>statsmodels sm.datasets (e.g. macrodata, longley, grunfeld) and sm.datasets.get_rdataset() access to Rdatasets (e.g. Duncan from carData, Guerry from HistData).</td>
		<td>[https://github.com/statsmodels/statsmodels/tree/main/statsmodels/datasets](https://github.com/statsmodels/statsmodels/tree/main/statsmodels/datasets)</td>
		<td>One-line loading; Duncan is the textbook case for influential observations (ministers, conductors), Guerry for cross-regional regression, macrodata for quarterly time-series regression with HAC errors.</td>
		<td>session 1 and 2 diagnostics exercises. Free (get_rdataset needs internet).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Housing datasets: caveats (Boston, California)</td>
		<td>Boston housing (Harrison and Rubinfeld 1978) in ISLP; California housing (sklearn.datasets.fetch_california_housing, 20,640 block groups).</td>
		<td>[https://github.com/intro-stat-learning/ISLP](https://github.com/intro-stat-learning/ISLP)</td>
		<td>Boston was removed from scikit-learn (1.2) because of its racially constructed B variable and data issues; avoid it or use it only to discuss data ethics. California housing is fine for non-linear effects but is not marketing.</td>
		<td>avoid in labs; mention as a caveat when students find these in AI-generated code. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Kaggle: Customer Personality Analysis (marketing campaign)</td>
		<td>Kaggle community upload (originally an iFood-style case dataset), about 2,240 customers x 29 variables: demographics, spend by category, campaign responses, web and store purchases (size from search listings, unverified).</td>
		<td>[https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)</td>
		<td>Easy cross-sectional marketing data for regression of spend on income with education and marital-status dummies, and moderation (income x kids at home).</td>
		<td>optional practice data. Free with login; licence stated as CC0 on Kaggle (unverified).</td>
		<td>neu; Link ungeprüft</td>
	</tr>
</table>