### Data (14)
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
		<td>Google Meridian simulated geo-level data</td>
		<td>Google, 2025, dataset in the Meridian repo; Apache 2.0</td>
		<td>[https://raw.githubusercontent.com/google/meridian/refs/heads/main/meridian/data/simulated_data/csv/geo_all_channels.csv](https://raw.githubusercontent.com/google/meridian/refs/heads/main/meridian/data/simulated_data/csv/geo_all_channels.csv)</td>
		<td>6,240 rows: 40 geos x 156 weeks (25 January 2021 to 15 January 2024), 5 paid channels with impressions and spend, 1 organic channel, 2 controls, promo flag, conversions, revenue per conversion and population (20 columns, about 1 MB). Sibling files add reach and frequency, national-level and a "hypothetical" future scenario for budget optimisation.</td>
		<td>Session 3 lab alternative (hierarchical geo model and allocation); the geos can be relabelled as countries.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>PyMC-Marketing example data (mmm_example.csv)</td>
		<td>PyMC Labs, 2023 onward, dataset in the pymc-marketing repo; Apache 2.0</td>
		<td>[https://raw.githubusercontent.com/pymc-labs/pymc-marketing/main/data/mmm_example.csv](https://raw.githubusercontent.com/pymc-labs/pymc-marketing/main/data/mmm_example.csv)</td>
		<td>179 weekly rows (2 April 2018 to 30 August 2021), 2 media channels, 2 event dummies, trend and seasonality helpers (8 columns, 12 KB). Tiny, so sampling is fast; matches the library's own tutorial.</td>
		<td>Session 2 warm-up before the Alpenglow Germany data.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Robyn demo data (dt_simulated_weekly)</td>
		<td>Meta Marketing Science, 2021 onward, dataset shipped with Robyn (R and Python); MIT</td>
		<td>[https://raw.githubusercontent.com/facebookexperimental/Robyn/main/python/src/robyn/tutorials/resources/dt_simulated_weekly.csv](https://raw.githubusercontent.com/facebookexperimental/Robyn/main/python/src/robyn/tutorials/resources/dt_simulated_weekly.csv)</td>
		<td>208 weekly rows (23 November 2015 to 11 November 2019), 12 columns: revenue, TV, OOH, print, Facebook (impressions and spend), search (clicks and spend), competitor sales, events, newsletter. The most widely used MMM demo, so students can compare their Python results with countless Robyn write-ups.</td>
		<td>Session 2 lab or exercise (reproduce a Robyn-style decomposition in PyMC-Marketing).</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Synthetic benchmark with endogenous marketing spend</td>
		<td>arXiv 2608.21130, 2026, paper plus seeded generator and reference instance with notebooks; licence stated in the repository (unverified)</td>
		<td>[https://arxiv.org/html/2608.21130](https://arxiv.org/html/2608.21130)</td>
		<td>Unlike Robyn and Meridian simulations, spend here reacts to seasons, promotions and past performance, so it tests whether a model survives endogeneity; ground truth is known.</td>
		<td>Session 3 or 5 stretch exercise: fit the course model and check recovery of true ROAS.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>siMMMulator and PySiMMMulator (simulation packages)</td>
		<td>Meta Marketing Science (R, MIT, author Jessica Nguyen) and PySiMMMulator (Python port, PyPI 0.6.2, 2024, Ryan Duecker); software</td>
		<td>[https://github.com/facebookexperimental/siMMMulator](https://github.com/facebookexperimental/siMMMulator)</td>
		<td>Generate MMM data from first principles (baseline, spend, impressions, conversions) with user-chosen true ROI, so students can make their own ground-truth tests.</td>
		<td>Session 5 project option: build a simulator for a seventh market.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Meta GeoLift sample data</td>
		<td>Meta, 2021 onward, datasets in the GeoLift R package (GeoLift_PreTest, GeoLift_Test, GeoLift_Test_MultiCell); MIT</td>
		<td>[https://github.com/facebookincubator/GeoLift/tree/main/data](https://github.com/facebookincubator/GeoLift/tree/main/data)</td>
		<td>Daily sales by location for pre-test and test periods, built for synthetic-control geo experiments; the pre-test file is the standard power-analysis example.</td>
		<td>Session 4 geo-lift lab (load the .rda files with pyreadr).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Kaggle: Sample Media Spends Data</td>
		<td>Kaggle user yugagrawal95, dataset; licence not visible from here (unverified)</td>
		<td>[https://www.kaggle.com/datasets/yugagrawal95/sample-media-spends-data](https://www.kaggle.com/datasets/yugagrawal95/sample-media-spends-data)</td>
		<td>3,051 rows, 9 columns, 113 weeks (January 2018 to February 2020), 8 digital channels (Facebook, Google search, email, YouTube, affiliate and more) plus sales; channel-week long format is good practice for reshaping.</td>
		<td>Session 2 exercise; requires a Kaggle account.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Kaggle: MMM demo dataset (bike sales)</td>
		<td>Kaggle user mattwalentosky, dataset; licence not visible from here (unverified)</td>
		<td>[https://www.kaggle.com/datasets/mattwalentosky/mmmdemodataset](https://www.kaggle.com/datasets/mattwalentosky/mmmdemodataset)</td>
		<td>Five years of fictitious weekly bike sales driven by Google Trends plus marketing spend; useful for showing how a search-interest covariate can absorb media effects.</td>
		<td>Session 4 forecasting exercise.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Dunnhumby: The Complete Journey and Breakfast at the Frat</td>
		<td>dunnhumby Source Files, retail transaction and promotion datasets; free download under dunnhumby terms (non-commercial; permission needed to publish results, per search summary; unverified)</td>
		<td>[https://www.dunnhumby.com/source-files/](https://www.dunnhumby.com/source-files/)</td>
		<td>Complete Journey: 2,500 households over two years with transactions, coupons and campaigns. Breakfast at the Frat: 156 weeks of store-product sales with base price, shelf price and display/feature flags across four categories, the cleanest free data for price and promotion elasticities.</td>
		<td>Session 1 elasticity lab (Breakfast at the Frat); Session 4 attribution background.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Dominick's Finer Foods scanner data</td>
		<td>Kilts Center, Chicago Booth, store-level weekly scanner data 1989 to 1997; free for academic use with registration. Eurostat's cleaned version and code: EUPL 1.2</td>
		<td>[https://www.chicagobooth.edu/research/kilts/research-data/dominicks](https://www.chicagobooth.edu/research/kilts/research-data/dominicks)</td>
		<td>About 100 million observations, 18,000 UPCs, 29 categories, 90+ stores, almost 400 weeks; the classic for store-level price response and a reasonable stand-in for a "geo" panel.</td>
		<td>Session 1 or 3 (treat stores as geos); subset one category before class.</td>
		<td>neu; in Suchergebnis bestätigt</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>NielsenIQ via the Kilts Center (Consumer Panel, Retail Scanner, Ad Intel)</td>
		<td>Kilts Center, Chicago Booth; academic subscription, US data only</td>
		<td>[https://www.chicagobooth.edu/research/kilts/research-data/nielseniq/pricing](https://www.chicagobooth.edu/research/kilts/research-data/nielseniq/pricing)</td>
		<td>Weekly retail scanner data since 2006 from 90+ chains plus advertising occurrences by media type: the only large public-to-academics source that combines sales and advertising.</td>
		<td>Background and thesis work only. Cost USD 3,000 for three years for one dataset (faculty subscription; up to two PhD students free); not usable for a 30-student class.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Google Trends</td>
		<td>Google, ongoing; web tool and unofficial Python access (pytrends)</td>
		<td>[https://trends.google.com/trends/](https://trends.google.com/trends/)</td>
		<td>Free weekly search-interest indices by country, the standard proxy for demand and for organic interest in all six Alpenglow markets; index values (0 to 100) are relative, not volumes.</td>
		<td>Session 3 and 4 covariate; mind rate limits and the terms of service.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>Eurostat</td>
		<td>European Commission, ongoing; database and API (Python package eurostat); CC BY 4.0</td>
		<td>[https://ec.europa.eu/eurostat/web/main/data/database](https://ec.europa.eu/eurostat/web/main/data/database)</td>
		<td>Monthly HICP, retail trade volume, consumer confidence and unemployment for AT, DE, FR, IT, NL, PL; the natural macro controls for a cross-country MMM and the source for PPP price-level adjustments.</td>
		<td>Session 3 (controls and price-level normalisation).</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Data</td>
		<td>World Bank World Development Indicators</td>
		<td>World Bank, ongoing; API (Python package wbgapi); CC BY 4.0</td>
		<td>[https://data.worldbank.org/](https://data.worldbank.org/)</td>
		<td>Annual GDP per capita, PPP conversion factors, population and internet penetration for every country; needed when extending the model to emerging markets or scaling spend across currencies.</td>
		<td>Session 3 and 5 (emerging-market extension in projects).</td>
		<td>neu; Link ungeprüft</td>
	</tr>
</table>