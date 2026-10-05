### Software (20)
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
		<td>Software</td>
		<td>polars</td>
		<td>Ritchie Vink and Polars contributors, 2020 to 2026, software (Python bindings to a Rust query engine). Version 1.44.2 on PyPI, released 9 September 2026; 2.0.0-rc.2 published 20 September 2026 (new Map dtype, streaming engine as default). MIT licence, Python 3.10 or later.</td>
		<td>[https://pypi.org/project/polars/](https://pypi.org/project/polars/)</td>
		<td>Eager DataFrame and lazy LazyFrame (pl.scan_csv(...).filter(...).group_by(...).agg(...).collect()), an expression API with no index, multi-threaded out of the box, to_pandas() via pyarrow for statsmodels and seaborn, .plot backed by Altair. Mature (1.x since July 2024) with a very large user base; the 2.0 release is imminent, so pin the major version in the course environment.</td>
		<td>session 1 lab (reading CSV and parquet, select, filter, group_by, joins), session 4 (lazy pipelines on larger panel data). Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>plotnine</td>
		<td>Hassan Kibirige (maintained with Posit support), 2017 to 2026, software. Version 0.15.8, 14 August 2026, MIT, Python 3.10 or later.</td>
		<td>[https://pypi.org/project/plotnine/](https://pypi.org/project/plotnine/)</td>
		<td>A faithful grammar-of-graphics port of ggplot2: ggplot(df, aes(...)) + geom_\*() + facet_wrap() + theme_\*(), with scales, stats, labels, built-in themes (theme_minimal, theme_bw, theme_538, theme_xkcd) and, since 0.15 (2025), plot composition with \| and /, HCL colour space and better facet strips. Accepts polars frames (converted to pandas internally). Renders through matplotlib, so PNG, SVG and PDF output work in Quarto.</td>
		<td>session 2 lab and all later sessions for figures; ggplot2 tutorials transfer almost one to one. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Great Tables</td>
		<td>Rich Iannone and Michael Chow, Posit, 2023 to 2026, software. Version 1.0.0, 25 September 2026, MIT, Python 3.10 or later.</td>
		<td>[https://pypi.org/project/great-tables/](https://pypi.org/project/great-tables/)</td>
		<td>Python port of R's gt: header, stub, spanners, fmt_number, fmt_currency, fmt_percent, tab_style, data_color, nanoplots (fmt_nanoplot, line and bar sparklines with hover values), polars selectors in columns=, pl.DataFrame.style returning a GT, save() to PNG and native HTML rendering in Quarto; LaTeX output exists but nanoplots do not render to PDF yet. 1.0 added load_dataset(), fmt_url, tab_style_body and HTML escaping by default (breaking for anyone injecting raw HTML).</td>
		<td>session 3 lab (summary tables for a market comparison), session 5 project reports. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Quarto CLI</td>
		<td>Posit (J.J. Allaire, Carlos Scheidegger, Charlotte Wickham and others), 2022 to 2026, software. Stable v1.10.18, 24 July 2026 (also on PyPI as quarto-cli 1.10.18, so uv add quarto-cli installs it into the project); pre-release v1.11.5, 17 September 2026. MIT.</td>
		<td>[https://github.com/quarto-dev/quarto-cli/releases](https://github.com/quarto-dev/quarto-cli/releases)</td>
		<td>One .qmd (or .ipynb) renders to HTML, revealjs slides, pptx, docx, PDF (LaTeX or Typst), dashboards (format: dashboard with cards and value boxes) and manuscripts (type: manuscript project with notebook embedding). Python cells run through a Jupyter kernel (ipykernel), parameterised reports via the Jupyter engine, brand.yml theming since 1.6, accessibility checks in 1.8. Quarto 2, a Rust rewrite with a collaborative editor, was announced on 6 April 2026 for late 2026 and promises backward compatibility.</td>
		<td>sessions 3 and 5 (reports, slides, GitHub Pages deployment); background for all labs since Positron edits and previews .qmd natively. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Quarto Live (r-wasm/quarto-live)</td>
		<td>George Stagg, Posit, 2024 to 2026, software (Quarto extension), MIT; version not read (unverified).</td>
		<td>[https://github.com/r-wasm/quarto-live](https://github.com/r-wasm/quarto-live)</td>
		<td>Pyodide-powered \{pyodide\} code cells and graded exercises (hints, solutions, custom checks) that run in the student's browser on a static site; polars has a Pyodide build, so simple polars and plotnine exercises can be served from GitHub Pages without a server.</td>
		<td>background; candidate for self-study pages in sessions 1 and 2. Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>pandas</td>
		<td>pandas development team (NumFOCUS), 2008 to 2026, software. Version 3.0.6, 17 September 2026, BSD-3-Clause, Python 3.11 or later.</td>
		<td>[https://pypi.org/project/pandas/](https://pypi.org/project/pandas/)</td>
		<td>Still the interchange format: plotnine, seaborn and statsmodels formulas consume pandas frames, and polars to_pandas() and pl.from_pandas() make the round trip cheap. pandas 3.0 (2026) changed defaults (copy-on-write, string dtype), which is why older tutorials sometimes warn.</td>
		<td>background; teach to_pandas() in session 4 before statsmodels. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>narwhals</td>
		<td>Marco Gorelli and contributors, 2024 to 2026, software. Version 2.26.0, 8 September 2026, MIT.</td>
		<td>[https://pypi.org/project/narwhals/](https://pypi.org/project/narwhals/)</td>
		<td>Thin compatibility layer that lets libraries (Altair, Plotly, marimo, scikit-lego and others) accept polars, pandas, DuckDB and pyarrow inputs without depending on any of them. Explains to students why polars "just works" in Altair and marimo.</td>
		<td>background only. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>pyarrow</td>
		<td>Apache Arrow project, 2016 to 2026, software. Version 25.0.1, 10 August 2026, Apache-2.0.</td>
		<td>[https://pypi.org/project/pyarrow/](https://pypi.org/project/pyarrow/)</td>
		<td>Columnar memory format underneath polars, pandas 3 strings, DuckDB and parquet I/O; required for zero-copy to_pandas() and for reading parquet in the labs.</td>
		<td>background dependency, mention in session 1. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>DuckDB</td>
		<td>DuckDB Foundation, 2019 to 2026, software. Version 1.5.6, 28 September 2026, MIT.</td>
		<td>[https://pypi.org/project/duckdb/](https://pypi.org/project/duckdb/)</td>
		<td>In-process SQL engine that queries polars and pandas frames and parquet files directly (duckdb.sql("select ... from df").pl()); the natural bridge for students who already know SQL and for larger-than-memory panel data.</td>
		<td>optional in session 4 for SQL-minded students. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Altair (Vega-Altair)</td>
		<td>Jake VanderPlas and contributors, 2016 to 2026, software. Version 6.3.0, 15 September 2026, BSD-3-Clause, Python 3.11 or later.</td>
		<td>[https://pypi.org/project/altair/](https://pypi.org/project/altair/)</td>
		<td>Declarative interactive charts; polars' built-in df.plot.\* uses Altair, and Altair accepts polars frames natively via narwhals. The interactive counterpart to plotnine for HTML dashboards.</td>
		<td>session 5 dashboards; otherwise alternative to plotnine. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>matplotlib</td>
		<td>matplotlib development team, 2003 to 2026, software. Version 3.11.2, 11 September 2026, PSF-style licence.</td>
		<td>[https://pypi.org/project/matplotlib/](https://pypi.org/project/matplotlib/)</td>
		<td>Rendering backend for plotnine (and for pandas .plot); needed to save figures at print resolution and to tweak the occasional detail plotnine does not expose.</td>
		<td>background dependency. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>seaborn</td>
		<td>Michael Waskom, 2012 to 2024, software. Version 0.13.2, 25 January 2024 (no release since), BSD-3-Clause.</td>
		<td>[https://pypi.org/project/seaborn/](https://pypi.org/project/seaborn/)</td>
		<td>Popular statistical plotting on pandas; the seaborn.objects interface is grammar-like. Stable but slow-moving and pandas-only, so it is the comparison point rather than the course tool; AI assistants often suggest it, which students should recognise.</td>
		<td>background, "why not seaborn" note in session 2. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>marimo</td>
		<td>marimo team (Akshay Agrawal, Myles Scolnick), 2023 to 2026, software. Version 0.25.1, 1 October 2026, Apache-2.0.</td>
		<td>[https://pypi.org/project/marimo/](https://pypi.org/project/marimo/)</td>
		<td>Reactive, git-friendly notebooks stored as .py, with built-in polars support and a documented Great Tables integration; runs as an app or in WebAssembly. Useful alternative to Jupyter for exploratory work, though Quarto remains the reporting layer.</td>
		<td>background; possible demo in session 1. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>JupyterLab and ipykernel</td>
		<td>Project Jupyter, 2015 to 2026, software. JupyterLab 4.6.4, 21 September 2026, BSD-3-Clause.</td>
		<td>[https://pypi.org/project/jupyterlab/](https://pypi.org/project/jupyterlab/)</td>
		<td>Quarto executes Python through a Jupyter kernel, so ipykernel (and optionally JupyterLab) must be in the project environment even when students never open a notebook; Positron handles kernels but the dependency is still required.</td>
		<td>session 1 environment setup. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>uv</td>
		<td>Astral, 2024 to 2026, software. Version 0.12.23, 3 October 2026, MIT or Apache-2.0.</td>
		<td>[https://pypi.org/project/uv/](https://pypi.org/project/uv/)</td>
		<td>Fast project and Python manager: uv init, uv add polars plotnine great-tables ipykernel quarto-cli, uv run quarto render, with a lock file committed to GitHub so every student reproduces the same environment.</td>
		<td>session 1 setup and the course template repository. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>statsmodels</td>
		<td>statsmodels developers, 2009 to 2026, software. Version 0.15.0, 27 August 2026, BSD-3-Clause.</td>
		<td>[https://pypi.org/project/statsmodels/](https://pypi.org/project/statsmodels/)</td>
		<td>Formula interface (smf.ols("sales \~ price + adstock", data=df.to_pandas()).fit().summary()) with the regression tables marketing students expect; pandas input only, which is the main reason to teach to_pandas().</td>
		<td>session 4 regression and simple marketing-mix models. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>scikit-learn</td>
		<td>scikit-learn developers, 2007 to 2026, software. Version 1.9.1, 10 September 2026, BSD-3-Clause, Python 3.11 or later.</td>
		<td>[https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)</td>
		<td>Accepts polars frames directly and can return polars output (set_output(transform="polars")), so pipelines for segmentation (k-means) or churn classification stay in polars.</td>
		<td>session 4 optional segmentation lab. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>polars-ols</td>
		<td>Azmy Rajab, 2024, software (polars plugin). Version 0.3.5, 25 August 2024, licence not declared on PyPI (MIT on GitHub, unverified).</td>
		<td>[https://pypi.org/project/polars-ols/](https://pypi.org/project/polars-ols/)</td>
		<td>OLS, WLS, ridge and rolling regressions as polars expressions with a patsy-style formula (pl.col("y").least_squares.ols(...)), handy for per-country regressions inside group_by. Little maintenance since 2024; for teaching, prefer statsmodels and mention this as an advanced option (polars-statistics is a newer alternative).</td>
		<td>session 4 stretch material. Free.</td>
		<td>neu; Link ungeprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>pins (Python)</td>
		<td>Posit (Isabel Zimmerman, Michael Chow), 2022 to 2025, software. Version 0.9.1, 3 October 2025, MIT.</td>
		<td>[https://pypi.org/project/pins/](https://pypi.org/project/pins/)</td>
		<td>Versioned sharing of dataframes to a folder, S3, Azure or Posit Connect with board.pin_write(df, "sales"); a simple way to distribute course datasets without committing CSVs to git.</td>
		<td>background for the instructor. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Ibis</td>
		<td>Ibis project (Voltron Data origins, now community), 2015 to 2026, software. Version 12.0.0, 7 February 2026, Apache-2.0.</td>
		<td>[https://pypi.org/project/ibis-framework/](https://pypi.org/project/ibis-framework/)</td>
		<td>One dataframe API that compiles to DuckDB, Postgres, BigQuery, Snowflake and polars; shows students how the same expression logic scales to a warehouse.</td>
		<td>background only. Free.</td>
		<td>neu; Link geprüft</td>
	</tr>
</table>