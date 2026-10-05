### Data (12)
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
		<td>Palmer penguins (palmerpenguins, also bundled in plotnine)</td>
		<td>Allison Horst, Alison Hill and Kristen Gorman (R package), Python port by Muhammad Chenariyan Nakhaee, 2020 to 2026, dataset package (0.1.6, 1 February 2026). CC0. 344 rows, 8 columns.</td>
		<td>[https://pypi.org/project/palmerpenguins/](https://pypi.org/project/palmerpenguins/)</td>
		<td>The standard first dataset for aesthetics, facets and group-by; plotnine.data.penguins means no extra install. Not marketing, but ideal for the first plotnine lab.</td>
		<td>session 2 warm-up. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Gapminder (gapminder Python package)</td>
		<td>Jennifer Bryan (R), Python port by Jeff Stafford, 2018, dataset package (0.1, BSD-3-Clause). 1,704 rows, 6 columns (country, continent, year, life expectancy, population, GDP per capita, 1952 to 2007).</td>
		<td>[https://pypi.org/project/gapminder/](https://pypi.org/project/gapminder/)</td>
		<td>International by construction; perfect for facets by continent, log scales and animated or faceted time series, and for a first Great Tables country comparison.</td>
		<td>sessions 1 and 2 labs, session 3 table demo. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>plotnine built-in datasets</td>
		<td>plotnine (plotnine.data), 2017 to 2026, 18 datasets ported from ggplot2: mpg, diamonds (about 54,000 rows), economics and economics_long, txhousing (8,602 rows), midwest, msleep, mtcars, penguins, presidential, anscombe_quartet and others. MIT with the package.</td>
		<td>[https://github.com/has2k1/plotnine/tree/main/plotnine/data](https://github.com/has2k1/plotnine/tree/main/plotnine/data)</td>
		<td>Every plotnine example and most ggplot2 tutorials use these, so students can follow any ggplot2 material directly; diamonds (prices by quality) and txhousing (sales by city and month) have a pricing and sales feel.</td>
		<td>session 2 exercises. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Great Tables bundled datasets</td>
		<td>Posit, 2024 to 2026, 16 datasets via great_tables.data or load_dataset() (pandas or polars): gtcars (47 deluxe cars, 15 columns, prices and specs by country of origin), sza (solar zenith angles, 816 rows), towny (414 Ontario municipalities, population 1996 to 2021), countrypops (13,545 rows, country populations 1960 to 2022), sp500 (16,607 daily rows), pizzaplace (49,574 pizza sales rows), metro, films, peeps, exibble. MIT with the package.</td>
		<td>[https://github.com/posit-dev/great-tables/blob/main/great_tables/data/__init__.py](https://github.com/posit-dev/great-tables/blob/main/great_tables/data/__init__.py)</td>
		<td>gtcars (car prices by manufacturer country) and pizzaplace (a year of sales by category and size) are natural marketing tables; countrypops gives nanoplot time series per country.</td>
		<td>session 3 lab. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>nycflights13 (Python port)</td>
		<td>Hadley Wickham (R), Python port by Michael Chow, 2020, dataset package (0.0.3, CC0). Five tables: flights (336,776 rows), airlines, airports, planes, weather.</td>
		<td>[https://pypi.org/project/nycflights13/](https://pypi.org/project/nycflights13/)</td>
		<td>The classic relational dataset for joins and lazy pipelines at a size where polars' speed is noticeable; many dplyr tutorials use it.</td>
		<td>session 1 or 4 joins lab. Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Kaggle: Customer Personality Analysis (marketing campaign)</td>
		<td>Akash Patel (Kaggle), 2021, dataset (2,240 customers, 29 columns: demographics, spend by product category, campaign responses, channel usage). CC0.</td>
		<td>[https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)</td>
		<td>Small, clean, genuinely marketing (campaign acceptance, RFM-style spend) and widely used for segmentation tutorials; good for group_by and scikit-learn clustering.</td>
		<td>session 4 segmentation lab. Free (Kaggle account needed).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>UCI Online Retail II</td>
		<td>Daqing Chen, London South Bank University, UCI Machine Learning Repository, 2019 (data 2009 to 2011), dataset (about 1 million transaction lines, UK gift wholesaler, customers in over 40 countries). CC BY 4.0 at UCI; Kaggle mirrors.</td>
		<td>[https://archive.ics.uci.edu/datasets?search=Online+Retail](https://archive.ics.uci.edu/datasets?search=Online+Retail)</td>
		<td>International transactions by country with invoices, quantities and prices: ideal for revenue by country tables, time series by month and a "lazy pipeline on a million rows" demonstration.</td>
		<td>sessions 1, 3 and 4. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Dunnhumby: The Complete Journey (completejourney-py)</td>
		<td>dunnhumby, 2014, dataset (2,500 households, two years, eight tables: transactions of about 2.6 million lines, demographics, products, campaigns, coupons, redemptions, causal data); Python package completejourney-py 0.1.0 (November 2025, MIT, mirrors the R package). Data under dunnhumby's source-files terms (free for non-commercial use).</td>
		<td>[https://pypi.org/project/completejourney-py/](https://pypi.org/project/completejourney-py/)</td>
		<td>The best free retail loyalty-card dataset: campaign and coupon effects, basket analysis, household panels. US only, so pair with Eurostat or Online Retail II for the international angle.</td>
		<td>session 4 case on promotion effects. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Eurostat via the eurostat package</td>
		<td>Eurostat (data, CC BY 4.0) and Noemi Emanuela Cazzaniga's eurostat package 1.1.1 (June 2024, MIT), API client (get_data_df("prc_hicp_manr") returns a pandas frame; wrap with pl.from_pandas).</td>
		<td>[https://pypi.org/project/eurostat/](https://pypi.org/project/eurostat/)</td>
		<td>Live European data (retail trade volumes, e-commerce usage, HICP by country, tourism nights) for country-comparison tables and faceted plots; sizes range from a few hundred to millions of rows depending on the table.</td>
		<td>sessions 2 and 3 international comparisons. Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>World Bank via wbgapi</td>
		<td>World Bank (World Development Indicators, CC BY 4.0) and Tim Herzog's wbgapi 1.0.14 (February 2026, MIT), API client (wb.data.DataFrame("NY.GDP.PCAP.CD", time=range(2000, 2024))).</td>
		<td>[https://pypi.org/project/wbgapi/](https://pypi.org/project/wbgapi/)</td>
		<td>Market-sizing variables (GDP per capita, internet users, urban population) for 200+ economies, directly as wide or long pandas frames.</td>
		<td>session 4 market attractiveness exercise. Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Our World in Data: Chart API and owid-catalog</td>
		<td>Our World in Data, 2024 to 2026, data API (append .csv to any grapher URL, e.g. https://ourworldindata.org/grapher/life-expectancy.csv) and Python package owid-catalog 1.2.7 (October 2026, MIT). Data CC BY 4.0 (underlying sources vary).</td>
		<td>[https://docs.owid.io/projects/etl/api/chart-api/](https://docs.owid.io/projects/etl/api/chart-api/)</td>
		<td>One-line pl.read_csv(url) for thousands of curated country-year series with metadata; the simplest live international data source for a beginner lab.</td>
		<td>session 1 (reading data from a URL) and session 2. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Kaggle: Marketing Campaign Performance Dataset</td>
		<td>Manisha Bhatt (Kaggle), 2023, dataset (200,000 rows: campaign type, channel, target audience, impressions, clicks, conversion rate, acquisition cost, ROI, location, language). Synthetic; licence as listed on Kaggle (unverified).</td>
		<td>[https://www.kaggle.com/datasets/manishabhatt22/marketing-campaign-performance-dataset](https://www.kaggle.com/datasets/manishabhatt22/marketing-campaign-performance-dataset)</td>
		<td>Large enough to show polars speed and has channel and language fields for cross-market tables; because it is synthetic, use it for mechanics, not for substantive conclusions.</td>
		<td>session 1 or 3 mechanics demo. Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
</table>