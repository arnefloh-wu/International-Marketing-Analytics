# Python stack resources: software, web, video, data and real-world examples

Part 1 of the Python research brief (polars, plotnine, Great Tables, Quarto and ecosystem). Versions and dates were read from the PyPI JSON API and GitHub on 5 October 2026. Links on pypi.org, github.com and raw.githubusercontent.com were fetched; pola.rs, quarto.org, posit.co and posit-dev.github.io are blocked by the sandbox proxy, so those links are confirmed from search listings only and are marked "(unverified)" where the page itself could not be opened.

Session mapping used below: session 1 = setup and polars basics, session 2 = visualisation with plotnine, session 3 = tables and Quarto reporting, session 4 = modelling (regression, MMM-style analysis), session 5 = project reports and presentations.

## 1. Software

### polars
- **Source:** Ritchie Vink and Polars contributors, 2020 to 2026, software (Python bindings to a Rust query engine). Version 1.44.2 on PyPI, released 9 September 2026; 2.0.0-rc.2 published 20 September 2026 (new Map dtype, streaming engine as default). MIT licence, Python 3.10 or later.
- **Link:** https://pypi.org/project/polars/ and https://github.com/pola-rs/polars
- **Why it matters:** Eager `DataFrame` and lazy `LazyFrame` (`pl.scan_csv(...).filter(...).group_by(...).agg(...).collect()`), an expression API with no index, multi-threaded out of the box, `to_pandas()` via pyarrow for statsmodels and seaborn, `.plot` backed by Altair. Mature (1.x since July 2024) with a very large user base; the 2.0 release is imminent, so pin the major version in the course environment.
- **Use in course:** session 1 lab (reading CSV and parquet, select, filter, group_by, joins), session 4 (lazy pipelines on larger panel data). Free.

### plotnine
- **Source:** Hassan Kibirige (maintained with Posit support), 2017 to 2026, software. Version 0.15.8, 14 August 2026, MIT, Python 3.10 or later.
- **Link:** https://pypi.org/project/plotnine/ and https://github.com/has2k1/plotnine
- **Why it matters:** A faithful grammar-of-graphics port of ggplot2: `ggplot(df, aes(...)) + geom_*() + facet_wrap() + theme_*()`, with scales, stats, labels, built-in themes (theme_minimal, theme_bw, theme_538, theme_xkcd) and, since 0.15 (2025), plot composition with `|` and `/`, HCL colour space and better facet strips. Accepts polars frames (converted to pandas internally). Renders through matplotlib, so PNG, SVG and PDF output work in Quarto.
- **Use in course:** session 2 lab and all later sessions for figures; ggplot2 tutorials transfer almost one to one. Free.

### Great Tables
- **Source:** Rich Iannone and Michael Chow, Posit, 2023 to 2026, software. Version 1.0.0, 25 September 2026, MIT, Python 3.10 or later.
- **Link:** https://pypi.org/project/great-tables/ and https://github.com/posit-dev/great-tables/releases/tag/v1.0.0
- **Why it matters:** Python port of R's gt: header, stub, spanners, `fmt_number`, `fmt_currency`, `fmt_percent`, `tab_style`, `data_color`, nanoplots (`fmt_nanoplot`, line and bar sparklines with hover values), polars selectors in `columns=`, `pl.DataFrame.style` returning a GT, `save()` to PNG and native HTML rendering in Quarto; LaTeX output exists but nanoplots do not render to PDF yet. 1.0 added `load_dataset()`, `fmt_url`, `tab_style_body` and HTML escaping by default (breaking for anyone injecting raw HTML).
- **Use in course:** session 3 lab (summary tables for a market comparison), session 5 project reports. Free.

### Quarto CLI
- **Source:** Posit (J.J. Allaire, Carlos Scheidegger, Charlotte Wickham and others), 2022 to 2026, software. Stable v1.10.18, 24 July 2026 (also on PyPI as `quarto-cli` 1.10.18, so `uv add quarto-cli` installs it into the project); pre-release v1.11.5, 17 September 2026. MIT.
- **Link:** https://github.com/quarto-dev/quarto-cli/releases and https://pypi.org/project/quarto-cli/
- **Why it matters:** One `.qmd` (or `.ipynb`) renders to HTML, revealjs slides, pptx, docx, PDF (LaTeX or Typst), dashboards (`format: dashboard` with cards and value boxes) and manuscripts (`type: manuscript` project with notebook embedding). Python cells run through a Jupyter kernel (ipykernel), parameterised reports via the Jupyter engine, brand.yml theming since 1.6, accessibility checks in 1.8. Quarto 2, a Rust rewrite with a collaborative editor, was announced on 6 April 2026 for late 2026 and promises backward compatibility.
- **Use in course:** sessions 3 and 5 (reports, slides, GitHub Pages deployment); background for all labs since Positron edits and previews .qmd natively. Free.

### Quarto Live (r-wasm/quarto-live)
- **Source:** George Stagg, Posit, 2024 to 2026, software (Quarto extension), MIT; version not read (unverified).
- **Link:** https://github.com/r-wasm/quarto-live and https://r-wasm.github.io/quarto-live/
- **Why it matters:** Pyodide-powered `{pyodide}` code cells and graded exercises (hints, solutions, custom checks) that run in the student's browser on a static site; polars has a Pyodide build, so simple polars and plotnine exercises can be served from GitHub Pages without a server.
- **Use in course:** background; candidate for self-study pages in sessions 1 and 2. Free.

### pandas
- **Source:** pandas development team (NumFOCUS), 2008 to 2026, software. Version 3.0.6, 17 September 2026, BSD-3-Clause, Python 3.11 or later.
- **Link:** https://pypi.org/project/pandas/
- **Why it matters:** Still the interchange format: plotnine, seaborn and statsmodels formulas consume pandas frames, and polars `to_pandas()` and `pl.from_pandas()` make the round trip cheap. pandas 3.0 (2026) changed defaults (copy-on-write, string dtype), which is why older tutorials sometimes warn.
- **Use in course:** background; teach `to_pandas()` in session 4 before statsmodels. Free.

### narwhals
- **Source:** Marco Gorelli and contributors, 2024 to 2026, software. Version 2.26.0, 8 September 2026, MIT.
- **Link:** https://pypi.org/project/narwhals/ and https://github.com/narwhals-dev/narwhals
- **Why it matters:** Thin compatibility layer that lets libraries (Altair, Plotly, marimo, scikit-lego and others) accept polars, pandas, DuckDB and pyarrow inputs without depending on any of them. Explains to students why polars "just works" in Altair and marimo.
- **Use in course:** background only. Free.

### pyarrow
- **Source:** Apache Arrow project, 2016 to 2026, software. Version 25.0.1, 10 August 2026, Apache-2.0.
- **Link:** https://pypi.org/project/pyarrow/
- **Why it matters:** Columnar memory format underneath polars, pandas 3 strings, DuckDB and parquet I/O; required for zero-copy `to_pandas()` and for reading parquet in the labs.
- **Use in course:** background dependency, mention in session 1. Free.

### DuckDB
- **Source:** DuckDB Foundation, 2019 to 2026, software. Version 1.5.6, 28 September 2026, MIT.
- **Link:** https://pypi.org/project/duckdb/
- **Why it matters:** In-process SQL engine that queries polars and pandas frames and parquet files directly (`duckdb.sql("select ... from df").pl()`); the natural bridge for students who already know SQL and for larger-than-memory panel data.
- **Use in course:** optional in session 4 for SQL-minded students. Free.

### Altair (Vega-Altair)
- **Source:** Jake VanderPlas and contributors, 2016 to 2026, software. Version 6.3.0, 15 September 2026, BSD-3-Clause, Python 3.11 or later.
- **Link:** https://pypi.org/project/altair/
- **Why it matters:** Declarative interactive charts; polars' built-in `df.plot.*` uses Altair, and Altair accepts polars frames natively via narwhals. The interactive counterpart to plotnine for HTML dashboards.
- **Use in course:** session 5 dashboards; otherwise alternative to plotnine. Free.

### matplotlib
- **Source:** matplotlib development team, 2003 to 2026, software. Version 3.11.2, 11 September 2026, PSF-style licence.
- **Link:** https://pypi.org/project/matplotlib/
- **Why it matters:** Rendering backend for plotnine (and for pandas `.plot`); needed to save figures at print resolution and to tweak the occasional detail plotnine does not expose.
- **Use in course:** background dependency. Free.

### seaborn
- **Source:** Michael Waskom, 2012 to 2024, software. Version 0.13.2, 25 January 2024 (no release since), BSD-3-Clause.
- **Link:** https://pypi.org/project/seaborn/
- **Why it matters:** Popular statistical plotting on pandas; the `seaborn.objects` interface is grammar-like. Stable but slow-moving and pandas-only, so it is the comparison point rather than the course tool; AI assistants often suggest it, which students should recognise.
- **Use in course:** background, "why not seaborn" note in session 2. Free.

### marimo
- **Source:** marimo team (Akshay Agrawal, Myles Scolnick), 2023 to 2026, software. Version 0.25.1, 1 October 2026, Apache-2.0.
- **Link:** https://pypi.org/project/marimo/ and https://github.com/marimo-team/marimo
- **Why it matters:** Reactive, git-friendly notebooks stored as .py, with built-in polars support and a documented Great Tables integration; runs as an app or in WebAssembly. Useful alternative to Jupyter for exploratory work, though Quarto remains the reporting layer.
- **Use in course:** background; possible demo in session 1. Free.

### JupyterLab and ipykernel
- **Source:** Project Jupyter, 2015 to 2026, software. JupyterLab 4.6.4, 21 September 2026, BSD-3-Clause.
- **Link:** https://pypi.org/project/jupyterlab/
- **Why it matters:** Quarto executes Python through a Jupyter kernel, so `ipykernel` (and optionally JupyterLab) must be in the project environment even when students never open a notebook; Positron handles kernels but the dependency is still required.
- **Use in course:** session 1 environment setup. Free.

### uv
- **Source:** Astral, 2024 to 2026, software. Version 0.12.23, 3 October 2026, MIT or Apache-2.0.
- **Link:** https://pypi.org/project/uv/ and https://github.com/astral-sh/uv
- **Why it matters:** Fast project and Python manager: `uv init`, `uv add polars plotnine great-tables ipykernel quarto-cli`, `uv run quarto render`, with a lock file committed to GitHub so every student reproduces the same environment.
- **Use in course:** session 1 setup and the course template repository. Free.

### statsmodels
- **Source:** statsmodels developers, 2009 to 2026, software. Version 0.15.0, 27 August 2026, BSD-3-Clause.
- **Link:** https://pypi.org/project/statsmodels/
- **Why it matters:** Formula interface (`smf.ols("sales ~ price + adstock", data=df.to_pandas()).fit().summary()`) with the regression tables marketing students expect; pandas input only, which is the main reason to teach `to_pandas()`.
- **Use in course:** session 4 regression and simple marketing-mix models. Free.

### scikit-learn
- **Source:** scikit-learn developers, 2007 to 2026, software. Version 1.9.1, 10 September 2026, BSD-3-Clause, Python 3.11 or later.
- **Link:** https://pypi.org/project/scikit-learn/
- **Why it matters:** Accepts polars frames directly and can return polars output (`set_output(transform="polars")`), so pipelines for segmentation (k-means) or churn classification stay in polars.
- **Use in course:** session 4 optional segmentation lab. Free.

### polars-ols
- **Source:** Azmy Rajab, 2024, software (polars plugin). Version 0.3.5, 25 August 2024, licence not declared on PyPI (MIT on GitHub, unverified).
- **Link:** https://pypi.org/project/polars-ols/ and https://github.com/azmyrajab/polars_ols
- **Why it matters:** OLS, WLS, ridge and rolling regressions as polars expressions with a patsy-style formula (`pl.col("y").least_squares.ols(...)`), handy for per-country regressions inside `group_by`. Little maintenance since 2024; for teaching, prefer statsmodels and mention this as an advanced option (polars-statistics is a newer alternative).
- **Use in course:** session 4 stretch material. Free.

### pins (Python)
- **Source:** Posit (Isabel Zimmerman, Michael Chow), 2022 to 2025, software. Version 0.9.1, 3 October 2025, MIT.
- **Link:** https://pypi.org/project/pins/
- **Why it matters:** Versioned sharing of dataframes to a folder, S3, Azure or Posit Connect with `board.pin_write(df, "sales")`; a simple way to distribute course datasets without committing CSVs to git.
- **Use in course:** background for the instructor. Free.

### Ibis
- **Source:** Ibis project (Voltron Data origins, now community), 2015 to 2026, software. Version 12.0.0, 7 February 2026, Apache-2.0.
- **Link:** https://pypi.org/project/ibis-framework/
- **Why it matters:** One dataframe API that compiles to DuckDB, Postgres, BigQuery, Snowflake and polars; shows students how the same expression logic scales to a warehouse.
- **Use in course:** background only. Free.

## 2. Websites, documentation and blogs

### Polars user guide, including "Coming from pandas"
- **Source:** Polars team, 2023 to 2026, website (official documentation).
- **Link:** https://docs.pola.rs/user-guide/ and https://docs.pola.rs/user-guide/migration/pandas/ (search-confirmed; host blocked in sandbox, unverified)
- **Why it matters:** The migration page is the clearest short statement of the mental model (expressions instead of index and lambdas, lazy by default, `with_columns` versus assignment) and maps pandas idioms to polars.
- **Use in course:** session 1 pre-reading (concepts, expressions, lazy API chapters). Free.

### Modern Polars (Kevin Heavey)
- **Source:** Kevin Heavey, 2023, website (online book, side-by-side polars and pandas, modelled on Modern Pandas).
- **Link:** https://kevinheavey.github.io/modern-polars/
- **Why it matters:** Each chapter (indexing, method chaining, tidy data, time series, performance) shows the same task in pandas and polars with commentary; ideal for students whose AI assistant keeps producing pandas.
- **Use in course:** session 1 and 4 reading; the tidy-data chapter pairs with plotnine. Free.

### Python Polars: The Definitive Guide (companion site)
- **Source:** Jeroen Janssens and Thijs Nieuwdorp, O'Reilly, February 2025, book with free companion website; foreword by Ritchie Vink.
- **Link:** https://polarsguide.com/ and https://www.oreilly.com/library/view/python-polars-the/9781098156077/
- **Why it matters:** The reference text for polars 1.x; chapter 16 covers visualisation including plotnine, and the authors use polars with Quarto. Posit announced it on its blog.
- **Use in course:** background and recommended purchase (about EUR 50; O'Reilly subscription). Free site, paid book.

### Polars Cookbook (Yuki Kakegawa) and Effective Polars (Matt Harrison)
- **Source:** Yuki Kakegawa, Packt, August 2024, book (394 pages, 60+ recipes for polars 1.x); Matt Harrison, self-published, July 2024 edition for polars 1.0, book.
- **Link:** https://www.packtpub.com/en-us/product/polars-cookbook-9781805121152 and https://www.goodreads.com/book/show/216178997-effective-polars (both unverified)
- **Why it matters:** Recipe-style alternatives to the Definitive Guide: the Cookbook is task oriented (joins, reshaping, time series, I/O), Effective Polars is opinionated and exercise driven. Both are intermediate.
- **Use in course:** background; lab solution sources. Paid (roughly EUR 35 to 45).

### plotnine.org documentation and gallery
- **Source:** Hassan Kibirige, 2024 to 2026, website (reference, guide, gallery rebuilt in Quarto in 2024).
- **Link:** https://plotnine.org/ and https://plotnine.org/gallery/index.html
- **Why it matters:** Gallery entries are executable notebooks (including winners of the 2024 Plotnine Contest), the reference mirrors ggplot2 naming, and the "Three major updates to the Plotnine website" post (Posit blog) explains the layout.
- **Use in course:** session 2 lab reference. Free.

### Announcing Plotnine 0.15.0 (Posit blog)
- **Source:** Hassan Kibirige, Posit blog, 2025, article.
- **Link:** https://posit.co/blog/plotnine-0-15-0 (search-confirmed, unverified)
- **Why it matters:** Introduces plot composition (`|`, `/`), text alignment and facet improvements with examples; the best short "what is new" for anyone with ggplot2 habits.
- **Use in course:** session 2 optional reading. Free.

### Jeroen Janssens: Plotnine cheatsheet and "Plotnine: Grammar of Graphics for Python"
- **Source:** Jeroen Janssens (Posit), October 2025 (cheatsheet) and 2024 update of a 2019 post, website.
- **Link:** https://jeroenjanssens.com/plotnine-cheatsheet/ and https://jeroenjanssens.com/plotnine/
- **Why it matters:** The post rebuilds a classic ggplot2 walkthrough with polars 1.0 and plotnine 0.13, exactly the course pairing; the cheatsheet is a printable one-page summary.
- **Use in course:** session 2 handout. Free.

### Great Tables documentation, Get Started and Examples
- **Source:** Posit (Iannone and Chow), 2024 to 2026, website.
- **Link:** https://posit-dev.github.io/great-tables/ and https://posit-dev.github.io/great-tables/examples/ (host blocked in sandbox, unverified)
- **Why it matters:** Get Started walks the component model (header, stub, spanners, formatting, styling, nanoplots); the examples page shows finished tables built from the bundled datasets, several with a business flavour (gtcars, sp500, pizzaplace).
- **Use in course:** session 3 lab reference. Free.

### The Design Philosophy of Great Tables
- **Source:** Rich Iannone and Michael Chow, Great Tables blog, 4 April 2024, article.
- **Link:** https://posit-dev.github.io/great-tables/blog/design-philosophy/ (unverified)
- **Why it matters:** Argues from 5,000 years of table history why structure (stub, spanners, notes) matters and why computational tables should expose it; a readable "why tables deserve design" piece for business students.
- **Use in course:** session 3 pre-reading. Free.

### Great Tables blog: polars posts
- **Source:** Michael Chow and Rich Iannone, Great Tables blog, 2024 to 2025, articles: "Great Tables: the Polars DataFrame styler of your dreams" (January 2024), "Great Tables is now BYODF" (April 2024), "Nanoplots and more, v0.4.0" (March 2024), "Becoming the Polars .style property" (April 2025), "Generating LaTeX output for PDF".
- **Link:** https://posit-dev.github.io/great-tables/blog/ (unverified)
- **Why it matters:** Shows polars expressions driving conditional formatting (`tab_style(locations=loc.body(rows=pl.col("x") > 0))`), which is the course's main table idiom, plus honest notes on PDF limitations.
- **Use in course:** session 3 reading. Free.

### Posit blog: Level Up Your Python Tables and What we did with publication-quality tables in 2024
- **Source:** Posit, 2024 to 2025, articles with a companion video series.
- **Link:** https://posit.co/blog/level-up-great-tables and https://posit.co/blog/what-we-did-with-publication-quality-tables-in-2024 (unverified)
- **Why it matters:** Structure, style and clarity walkthroughs with videos; the year-in-review post lists gt and Great Tables features side by side, useful for R-trained colleagues.
- **Use in course:** session 3 background. Free.

### Quarto guide: Using Python, Presentations, Dashboards, Manuscripts
- **Source:** Posit, 2022 to 2026, website (official guide).
- **Link:** https://quarto.org/docs/computations/python.html, https://quarto.org/docs/presentations/revealjs/, https://quarto.org/docs/dashboards/, https://quarto.org/docs/manuscripts/ (host blocked in sandbox, unverified)
- **Why it matters:** The guide pages are the canonical reference for the Jupyter engine, cell options (`#| echo: false`, `#| fig-cap`), revealjs and pptx output, dashboards and parameterised reports; the Quarto blog moved to opensource.posit.co in 2025 (https://opensource.posit.co/blog/q/quarto/).
- **Use in course:** sessions 3 and 5 reference. Free.

### Quarto Live documentation
- **Source:** George Stagg, Posit, 2024 to 2026, website.
- **Link:** https://r-wasm.github.io/quarto-live/
- **Why it matters:** Setup, `{pyodide}` cells, exercises with grading and OJS integration; the Tidyverse blog post "WebAssembly roundup part 3: Quarto Live 0.1.1" (October 2024) is the readable introduction.
- **Use in course:** background for building self-study pages. Free.

### Real Python: Python Polars tutorial and Using ggplot in Python with plotnine
- **Source:** Real Python, 2023 to 2025, website tutorials (with optional video course "Working With Python Polars").
- **Link:** https://realpython.com/polars-python/ and https://realpython.com/ggplot-python/
- **Why it matters:** Beginner-paced, well edited, with runnable code on GitHub (https://github.com/realpython/materials/tree/master/python-polars); the plotnine tutorial starts from the grammar itself. Real Python Podcast episode 260 (August 2025) interviews the Definitive Guide authors.
- **Use in course:** session 1 and 2 self-study. Articles free; video courses by subscription.

### Polars Academy and PyData talk pages on pola.rs
- **Source:** Polars (company), 2023 to 2026, website (learning hub plus posts summarising conference talks with slides and video links).
- **Link:** https://pola.rs/academy/ and https://pola.rs/posts/ (host blocked in sandbox, unverified)
- **Why it matters:** Official short courses (expressions, lazy API, plugins) and the canonical index of Ritchie Vink's PyData talks (Amsterdam, NYC, Eindhoven 2023).
- **Use in course:** background. Free.

### awesome-polars and awesome-quarto
- **Source:** Damien Dotta (awesome-polars) and Mickaël Canouil (awesome-quarto), 2022 to 2026, GitHub lists.
- **Link:** https://github.com/ddotta/awesome-polars and https://github.com/mcanouil/awesome-quarto
- **Why it matters:** Curated, actively updated indexes of talks, books, plugins, courses and example sites (awesome-quarto lists Python-specific items such as "Quarto for the Python user" by Jumping Rivers and Charlotte Wickham's parameterised-report talks).
- **Use in course:** background for the instructor. Free.

### Coding for Economists and Python for Data Science (Arthur Turrell)
- **Source:** Arthur Turrell, 2021 to 2026, website (two free Quarto-style online books).
- **Link:** https://aeturrell.github.io/coding-for-economists/vis-plotnine.html and https://aeturrell.github.io/python4DS/
- **Why it matters:** Coding for Economists has a full chapter "Data visualisation using the grammar of graphics with plotnine" and discusses polars; python4DS mirrors R for Data Science in Python and ends with Quarto reporting. Written for beginners with no programming background.
- **Use in course:** session 2 reading (plotnine chapter), background for the rest. Free.

### Calmcode: Python Polars vs. pandas
- **Source:** Vincent Warmerdam, Calmcode, 2022 to 2024, website with short videos.
- **Link:** https://calmcode.io/course/polars/introduction
- **Why it matters:** Eight videos of two to five minutes each (introduction, read_csv, with_columns, pipe, sort and filter, sessionise, over expressions, eager versus lazy) using a clickstream-style dataset; calm, beginner friendly.
- **Use in course:** session 1 pre-lab viewing. Free.

## 3. Video tutorials and courses

### Ritchie Vink: Polars, DataFrames in the multi-core era (PyData NYC 2023) and Polars and a peek into the expression engine (PyData Amsterdam 2023)
- **Source:** Ritchie Vink (Polars creator), PyData, 2023, conference talks (about 35 to 40 minutes each, intermediate).
- **Link:** https://www.youtube.com/watch?v=NJbBWDzZuWs (Amsterdam) and https://nyc2023.pydata.org/cfp/talk/WZJWL3/ (NYC abstract); 2021 origin talk https://www.youtube.com/watch?v=iwGIuGk5nCE
- **Why it matters:** The creator explains why polars is built around expressions and a query optimiser; good for the "why not pandas" question without benchmark hype.
- **Use in course:** session 1 optional viewing. Free.

### Marco Gorelli: Understanding Polars expressions when you are used to pandas; Polars and time series (PyCon DE and PyData Berlin 2024); How Narwhals brings Polars, DuckDB, PyArrow and pandas together (PyData London 2025)
- **Source:** Marco Gorelli (Quansight Labs, Narwhals author, pandas and Polars contributor), 2023 to 2025, conference talks, 29 to 36 minutes, beginner to intermediate.
- **Link:** https://www.youtube.com/watch?v=qz-zAHBz6Ks (time series) and https://www.youtube.com/watch?v=r2PxJlO7_QA (Narwhals)
- **Why it matters:** The expressions talk is the single best bridge for pandas-trained viewers; the time-series talk covers date handling needed for weekly sales data.
- **Use in course:** session 1 (expressions) and session 4 (time series). Free.

### Hassan Kibirige: Grammar of Graphics in Python with Plotnine (posit::conf 2023)
- **Source:** Hassan Kibirige (plotnine creator), Posit, 2023, conference talk (about 20 minutes, beginner).
- **Link:** https://www.youtube.com/watch?v=q816IZuqVNo
- **Why it matters:** The author's own explanation of layers, aesthetics and facets with plotnine code; the Mode blog interview "Who's behind the numbers?" (https://mode.com/blog/whos-behind-the-numbers-hassan-kibirige/) adds background.
- **Use in course:** session 2 pre-viewing. Free.

### Rich Iannone: Adequate Tables? No, We Want Great Tables (posit::conf 2024) and Making Things Nice in Python (posit::conf 2025)
- **Source:** Rich Iannone (Posit), 2024 and 2025, conference talks (about 20 minutes each, beginner).
- **Link:** https://pyvideo.org/positconf-2024/adequate-tables-no-we-want-great-tables.html and https://www.youtube.com/watch?v=J6e2BKjHyPg
- **Why it matters:** Live-coded table building from a dataframe to a publication table, nanoplots included; the 2025 talk adds Pointblank for data validation.
- **Use in course:** session 3 pre-viewing. Free.

### Talk Python episode 492: Great Tables (Iannone and Chow)
- **Source:** Michael Kennedy with Rich Iannone and Michael Chow, Talk Python To Me, 2024, podcast with video (about 1 hour, beginner).
- **Link:** https://www.youtube.com/watch?v=15ICWSJ0sGk and https://talkpython.fm/episodes/show/492/great-tables
- **Why it matters:** Conversational tour of the design, polars integration and Quarto rendering; good commute listening before the tables session.
- **Use in course:** session 3 optional. Free.

### Jeroen Janssens: Python Polars, the Definitive Crash Course (PyData Global 2025)
- **Source:** Jeroen Janssens (Posit), PyData Global, December 2025, tutorial recording (long form, beginner to intermediate).
- **Link:** https://opensource.posit.co/resources/videos/2026-01-09_jeroen-janssens-python-polars-the-definitive-crash-course-pydata-global-2025/ (unverified)
- **Why it matters:** Condenses the O'Reilly book into one session, with polars 1.x syntax and plotnine figures.
- **Use in course:** session 1 and 4 self-study. Free.

### Keith Galli: Quarto with Python Crash Course (Posit YouTube series)
- **Source:** Keith Galli for Posit, 2024 to 2025, video series (six videos; crash course 96 minutes, parameterised reports 26 minutes, plus slides, dashboards and portfolio site; beginner).
- **Link:** https://www.youtube.com/playlist?list=PL9HYL-VRX0oQZPzhJR022G_bV4vynT4Ol and https://github.com/KeithGalli/quarto-crash-course
- **Why it matters:** Python-only Quarto teaching from zero: reports, PDFs, revealjs slides, dashboards and "100s of custom reports in minutes" with parameters; the companion repo is a ready template.
- **Use in course:** session 3 pre-viewing (crash course), session 5 (parameterised reports). Free.

### Mine Çetinkaya-Rundel: Quarto Dashboards video series and Build-a-Dashboard workshop
- **Source:** Mine Çetinkaya-Rundel (Duke University and Posit), November 2024, three videos (first dashboard, components, theming; about 20 minutes each) with R and Python starter code; posit::conf(2024) full-day workshop materials.
- **Link:** https://www.youtube.com/watch?v=KdsQgwaY950, https://www.youtube.com/watch?v=NigWSB-jG4Y, https://github.com/mine-cetinkaya-rundel/olympicdash and https://posit-conf-2024.github.io/workshops/workshops/quarto_dashboards.html
- **Why it matters:** Builds an Olympic medals dashboard in Python or R step by step; "Teaching (with) Quarto" (https://mine-cetinkaya-rundel.github.io/teach-with-quarto/) covers course websites and slides.
- **Use in course:** session 5 dashboards; background for the course site. Free.

### Albert Rapp: How to Automate Data Reports with Quarto (Beginner's Guide)
- **Source:** Albert Rapp (3 Minutes Wednesdays), 2024 to 2025, YouTube videos and newsletter (10 to 20 minutes, beginner; R-based code but Quarto features are language independent).
- **Link:** https://www.youtube.com/watch?v=KCpuUF4vi5g and https://3mw.albert-rapp.de/p/creating-beautiful-pdf-reports-with-typst-and-quarto
- **Why it matters:** Short, polished explanations of parameterised reports, Typst PDFs and revealjs styling; translate the R cells to Python and the rest carries over.
- **Use in course:** session 5 optional. Free (newsletter free, paid tier exists).

### Charlotte Wickham: From one notebook to many reports, automating with Quarto (SciPy 2025)
- **Source:** Charlotte Wickham (Posit, Quarto team), SciPy, 2025, conference talk (about 25 minutes, beginner to intermediate).
- **Link:** listed in https://github.com/mcanouil/awesome-quarto (direct video URL unverified)
- **Why it matters:** Parameterised Python notebooks rendered to many PDFs, exactly the "one report per country" pattern for an international marketing project.
- **Use in course:** session 5. Free.

### Udemy: Data Analysis with Polars (Liam Brannigan)
- **Source:** Liam Brannigan, Udemy, 2022 to 2025 (updated for polars 1.x), paid course (60 Jupyter notebooks, roughly 8 hours, beginner to intermediate; 4.7 rating, endorsed by Ritchie Vink).
- **Link:** https://www.udemy.com/course/data-analysis-with-polars/ and https://github.com/braaannigan/data-analysis-with-polars
- **Why it matters:** The most complete structured polars course; the public GitHub repo gives free sample notebooks and datasets.
- **Use in course:** background; recommend to students who want depth. Paid (Udemy pricing, typically EUR 15 to 90 with frequent discounts).

### DataCamp: Introduction to Polars
- **Source:** DataCamp, updated May 2026, online course (3 hours, 12 videos, 42 exercises, beginner).
- **Link:** https://www.datacamp.com/courses/introduction-to-polars
- **Why it matters:** Browser-based exercises on selecting, filtering, group-by, pivots; no setup needed, so it suits students who struggle with environments. DataCamp has no plotnine course; the only plotnine MOOC found is a 1.5-hour Coursera guided project "Data Visualization using Plotnine and ggplot" (https://www.coursera.org/projects/data-visualization-using-plotnine).
- **Use in course:** session 1 optional practice. First chapter free, rest by subscription (DataCamp Classroom is free for instructors and students).

### Real Python video course: Working With Python Polars
- **Source:** Real Python, 2024, video course (about 1 hour, beginner).
- **Link:** https://realpython.com/courses/working-with-python-polars/
- **Why it matters:** Video version of the written tutorial: dataframes, expressions, reading data, group-by, lazy API.
- **Use in course:** session 1 optional. Subscription (free article alternative above).

### Posit Academy and posit::conf(2023) Introduction to Data Science with Python
- **Source:** Posit, 2023 to 2026; Academy Apprenticeships are six-to-eight-week mentored cohorts for organisations (price on request); a free open library of courses, labs and workshops launched in 2025. The 2023 workshop (plotnine, pandas, functions, Quarto) has public materials.
- **Link:** https://academy.posit.co/, https://posit.co/blog/announcing-expanded-posit-academy (unverified) and https://github.com/chendaniely/positconf2023-academy_python
- **Why it matters:** The workshop repo is a tested beginner curriculum in the same stack (plotnine plus Quarto), easy to adapt to polars.
- **Use in course:** background; lab material source. Free materials; apprenticeships paid.

### Polars Code Academy and martinbel Polars tutorials (YouTube)
- **Source:** Polars Code Academy channel (feature-by-feature short videos) and Martin Bel's playlist "Polars: the main alternative to pandas" (about 57 minutes total), 2023 to 2025, beginner.
- **Link:** https://www.youtube.com/channel/UCFaPNTDJga0Ebwvftju9jMQ/about and https://github.com/martinbel/polars-tutorial
- **Why it matters:** Short topic videos that students can look up when stuck on one function.
- **Use in course:** background. Free.

## 4. Data

### Palmer penguins (palmerpenguins, also bundled in plotnine)
- **Source:** Allison Horst, Alison Hill and Kristen Gorman (R package), Python port by Muhammad Chenariyan Nakhaee, 2020 to 2026, dataset package (0.1.6, 1 February 2026). CC0. 344 rows, 8 columns.
- **Link:** https://pypi.org/project/palmerpenguins/ and https://github.com/mcnakhaee/palmerpenguins
- **Why it matters:** The standard first dataset for aesthetics, facets and group-by; `plotnine.data.penguins` means no extra install. Not marketing, but ideal for the first plotnine lab.
- **Use in course:** session 2 warm-up. Free.

### Gapminder (gapminder Python package)
- **Source:** Jennifer Bryan (R), Python port by Jeff Stafford, 2018, dataset package (0.1, BSD-3-Clause). 1,704 rows, 6 columns (country, continent, year, life expectancy, population, GDP per capita, 1952 to 2007).
- **Link:** https://pypi.org/project/gapminder/ and https://github.com/jstaf/gapminder
- **Why it matters:** International by construction; perfect for facets by continent, log scales and animated or faceted time series, and for a first Great Tables country comparison.
- **Use in course:** sessions 1 and 2 labs, session 3 table demo. Free.

### plotnine built-in datasets
- **Source:** plotnine (`plotnine.data`), 2017 to 2026, 18 datasets ported from ggplot2: mpg, diamonds (about 54,000 rows), economics and economics_long, txhousing (8,602 rows), midwest, msleep, mtcars, penguins, presidential, anscombe_quartet and others. MIT with the package.
- **Link:** https://github.com/has2k1/plotnine/tree/main/plotnine/data
- **Why it matters:** Every plotnine example and most ggplot2 tutorials use these, so students can follow any ggplot2 material directly; diamonds (prices by quality) and txhousing (sales by city and month) have a pricing and sales feel.
- **Use in course:** session 2 exercises. Free.

### Great Tables bundled datasets
- **Source:** Posit, 2024 to 2026, 16 datasets via `great_tables.data` or `load_dataset()` (pandas or polars): gtcars (47 deluxe cars, 15 columns, prices and specs by country of origin), sza (solar zenith angles, 816 rows), towny (414 Ontario municipalities, population 1996 to 2021), countrypops (13,545 rows, country populations 1960 to 2022), sp500 (16,607 daily rows), pizzaplace (49,574 pizza sales rows), metro, films, peeps, exibble. MIT with the package.
- **Link:** https://github.com/posit-dev/great-tables/blob/main/great_tables/data/__init__.py
- **Why it matters:** gtcars (car prices by manufacturer country) and pizzaplace (a year of sales by category and size) are natural marketing tables; countrypops gives nanoplot time series per country.
- **Use in course:** session 3 lab. Free.

### nycflights13 (Python port)
- **Source:** Hadley Wickham (R), Python port by Michael Chow, 2020, dataset package (0.0.3, CC0). Five tables: flights (336,776 rows), airlines, airports, planes, weather.
- **Link:** https://pypi.org/project/nycflights13/ (GitHub repo link on PyPI returns 404, unverified)
- **Why it matters:** The classic relational dataset for joins and lazy pipelines at a size where polars' speed is noticeable; many dplyr tutorials use it.
- **Use in course:** session 1 or 4 joins lab. Free.

### Kaggle: Customer Personality Analysis (marketing campaign)
- **Source:** Akash Patel (Kaggle), 2021, dataset (2,240 customers, 29 columns: demographics, spend by product category, campaign responses, channel usage). CC0.
- **Link:** https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis
- **Why it matters:** Small, clean, genuinely marketing (campaign acceptance, RFM-style spend) and widely used for segmentation tutorials; good for group_by and scikit-learn clustering.
- **Use in course:** session 4 segmentation lab. Free (Kaggle account needed).

### UCI Online Retail II
- **Source:** Daqing Chen, London South Bank University, UCI Machine Learning Repository, 2019 (data 2009 to 2011), dataset (about 1 million transaction lines, UK gift wholesaler, customers in over 40 countries). CC BY 4.0 at UCI; Kaggle mirrors.
- **Link:** https://archive.ics.uci.edu/datasets?search=Online+Retail and https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci
- **Why it matters:** International transactions by country with invoices, quantities and prices: ideal for revenue by country tables, time series by month and a "lazy pipeline on a million rows" demonstration.
- **Use in course:** sessions 1, 3 and 4. Free.

### Dunnhumby: The Complete Journey (completejourney-py)
- **Source:** dunnhumby, 2014, dataset (2,500 households, two years, eight tables: transactions of about 2.6 million lines, demographics, products, campaigns, coupons, redemptions, causal data); Python package completejourney-py 0.1.0 (November 2025, MIT, mirrors the R package). Data under dunnhumby's source-files terms (free for non-commercial use).
- **Link:** https://pypi.org/project/completejourney-py/ and https://www.kaggle.com/datasets/frtgnn/dunnhumby-the-complete-journey
- **Why it matters:** The best free retail loyalty-card dataset: campaign and coupon effects, basket analysis, household panels. US only, so pair with Eurostat or Online Retail II for the international angle.
- **Use in course:** session 4 case on promotion effects. Free.

### Eurostat via the eurostat package
- **Source:** Eurostat (data, CC BY 4.0) and Noemi Emanuela Cazzaniga's `eurostat` package 1.1.1 (June 2024, MIT), API client (`get_data_df("prc_hicp_manr")` returns a pandas frame; wrap with `pl.from_pandas`).
- **Link:** https://pypi.org/project/eurostat/ and https://ec.europa.eu/eurostat/web/main/data/database (unverified)
- **Why it matters:** Live European data (retail trade volumes, e-commerce usage, HICP by country, tourism nights) for country-comparison tables and faceted plots; sizes range from a few hundred to millions of rows depending on the table.
- **Use in course:** sessions 2 and 3 international comparisons. Free.

### World Bank via wbgapi
- **Source:** World Bank (World Development Indicators, CC BY 4.0) and Tim Herzog's `wbgapi` 1.0.14 (February 2026, MIT), API client (`wb.data.DataFrame("NY.GDP.PCAP.CD", time=range(2000, 2024))`).
- **Link:** https://pypi.org/project/wbgapi/ and https://blogs.worldbank.org/opendata/introducing-wbgapi-new-python-package-accessing-world-bank-data (unverified)
- **Why it matters:** Market-sizing variables (GDP per capita, internet users, urban population) for 200+ economies, directly as wide or long pandas frames.
- **Use in course:** session 4 market attractiveness exercise. Free.

### Our World in Data: Chart API and owid-catalog
- **Source:** Our World in Data, 2024 to 2026, data API (append `.csv` to any grapher URL, e.g. https://ourworldindata.org/grapher/life-expectancy.csv) and Python package owid-catalog 1.2.7 (October 2026, MIT). Data CC BY 4.0 (underlying sources vary).
- **Link:** https://docs.owid.io/projects/etl/api/chart-api/ and https://pypi.org/project/owid-catalog/
- **Why it matters:** One-line `pl.read_csv(url)` for thousands of curated country-year series with metadata; the simplest live international data source for a beginner lab.
- **Use in course:** session 1 (reading data from a URL) and session 2. Free.

### Kaggle: Marketing Campaign Performance Dataset
- **Source:** Manisha Bhatt (Kaggle), 2023, dataset (200,000 rows: campaign type, channel, target audience, impressions, clicks, conversion rate, acquisition cost, ROI, location, language). Synthetic; licence as listed on Kaggle (unverified).
- **Link:** https://www.kaggle.com/datasets/manishabhatt22/marketing-campaign-performance-dataset
- **Why it matters:** Large enough to show polars speed and has channel and language fields for cross-market tables; because it is synthetic, use it for mechanics, not for substantive conclusions.
- **Use in course:** session 1 or 3 mechanics demo. Free.

## 5. Real-world examples

### Polars at Decathlon: Ready to Play? (Spark to polars)
- **Source:** Arnaud Vennin (Decathlon Digital), Polars blog, 15 September 2025, case (also on Medium and covered by InfoQ, December 2025).
- **Link:** https://pola.rs/posts/case-decathlon/ (unverified) and https://medium.com/decathlondigital/polars-at-decathlon-ready-to-play-6abc4328d06c
- **Why it matters:** A European sports retailer replacing Spark jobs with single-machine polars to cut cost and complexity; a retail analytics story students recognise.
- **Use in course:** session 1 motivation slide. Free.

### BMLL, Citizens, Double River, Vydia, Rabobank and La Mobilière case studies (Polars blog)
- **Source:** Polars, 2024 to 2026, cases: BMLL (1.5 TB of market data in under four minutes, 48x faster than pandas), Citizens bank (analyst empowerment), Double River Investments (plugins), Vydia (music CSV processing), Rabobank (window functions), La Mobilière (Swiss insurer).
- **Link:** https://pola.rs/posts/case-bmll/ and https://pola.rs/posts/case-citizens/ (unverified)
- **Why it matters:** Short, concrete production stories including two European financial firms (Rabobank, La Mobilière); the Citizens case is about analysts, not engineers, which matches the course audience.
- **Use in course:** background; one or two quoted in session 1. Free.

### KS&R: hundreds of personalised PDF reports weekly with Quarto (Posit customer story)
- **Source:** Posit customer story, 2024 to 2025, case (KS&R Decision Sciences and Innovation team, a market research firm).
- **Link:** https://posit.co/about/customer-stories (unverified; story confirmed from search listing)
- **Why it matters:** A market research company replacing a legacy reporting pipeline with parameterised Quarto reports; the closest documented match to what marketing analysts do.
- **Use in course:** session 5 case for parameterised reports. Free.

### Bay FC: weekly match reports with Quarto and Posit Connect
- **Source:** Posit customer story with Arielle Dror (Director of Data and Analytics, Bay FC, NWSL), 2025, case.
- **Link:** https://posit.co/about/customer-stories (unverified)
- **Why it matters:** Sports marketing adjacent: automated weekly reports for coaches and recruitment, showing Quarto as the delivery layer rather than a notebook.
- **Use in course:** session 5 example. Free.

### University of Connecticut, Introduction to Data Science (STAT 3255/5255) taught in Python with Quarto
- **Source:** Jun Yan, University of Connecticut, 2025, course website and book built with Quarto, Python throughout; chapter "Reproducible data science" explains Quarto for homework, notes and presentations.
- **Link:** https://statds.github.io/ids-s25/quarto.html
- **Why it matters:** A full university course where students submit Quarto documents via GitHub; a template for assessment workflow.
- **Use in course:** background for course design. Free.

### Teaching (with) Quarto (Mine Çetinkaya-Rundel, Duke)
- **Source:** Mine Çetinkaya-Rundel, 2023 to 2024, talk and website on building course sites, slides and assignments with Quarto, plus "Using Quarto to make and organise teaching materials" (Maria Tackett, JSM).
- **Link:** https://mine-cetinkaya-rundel.github.io/teach-with-quarto/ and https://maria.quarto.pub/teach-with-quarto-jsm/
- **Why it matters:** The reference pattern for a Quarto course website with GitHub Classroom; the author also leads the Python-inclusive dashboard workshop above.
- **Use in course:** background for course design. Free.

### Coding for Economists (Bank of England economist, plotnine chapter)
- **Source:** Arthur Turrell (economist, formerly Bank of England and ONS Data Science Campus), 2021 to 2026, free online book built with Jupyter Book.
- **Link:** https://aeturrell.github.io/coding-for-economists/vis-plotnine.html
- **Why it matters:** A practising economist teaching plotnine to non-programmers with economic data; the closest documented analogue to a business-school plotnine course.
- **Use in course:** session 2 reading. Free.

### Great Tables for scientific publishing and Great Tables + marimo
- **Source:** Posit Great Tables blog, 2024 to 2025, articles ("Great Tables for scientific publishing"; Jerry Wu, "Great Tables + marimo = interactive tables").
- **Link:** https://posit-dev.github.io/great-tables/blog/tables-for-scientific-publishing/ and https://posit-dev.github.io/great-tables/blog/marimo-and-great-tables/ (unverified)
- **Why it matters:** Worked, real tables (not toy data) and a reactive-notebook integration that shows how far the HTML table model stretches.
- **Use in course:** session 3 background. Free.

### Why a University of Pittsburgh professor standardised his teaching on marimo
- **Source:** marimo blog, 2025, case (University of Pittsburgh "Writing Machines" course; also Utrecht University WASM apps and a Stanford course).
- **Link:** https://marimo.io/blog/case-study-pitt
- **Why it matters:** Documented classroom use of reactive Python notebooks with no-install WebAssembly delivery; relevant if the course wants in-browser exercises beyond Quarto Live.
- **Use in course:** background. Free.

### Plotnine Contest 2024 gallery and tashapiro's python-plotnine workshop
- **Source:** Posit (2024 Plotnine Contest entries now in the plotnine gallery) and Tanya Shapiro's workshop for R-Ladies Cologne and Paris and PyLadies Tunis and Munich, 2023 to 2024, examples.
- **Link:** https://plotnine.org/gallery/index.html and https://github.com/tashapiro/python-plotnine-workshop
- **Why it matters:** The closest thing to data-journalism-grade plotnine work: polished, annotated charts with full code, including Economist-style themes that students can copy.
- **Use in course:** session 2 inspiration and theme templates. Free.

### Jeroen Janssens: Plotnine with Polars 1.0 (worked example)
- **Source:** Jeroen Janssens (Posit), 2024, blog post rebuilding a classic ggplot2 tutorial with polars and plotnine.
- **Link:** https://jeroenjanssens.com/plotnine/
- **Why it matters:** A documented end-to-end example in exactly the course stack, by the author of the polars reference book.
- **Use in course:** session 2 worked example. Free.

## Gaps and caveats

The sandbox proxy blocks pola.rs, quarto.org, posit.co, posit-dev.github.io, docs.pola.rs, plotnine.org, realpython.com, YouTube and Kaggle, so every link on those hosts is confirmed from search listings only and is marked "(unverified)"; none of the YouTube lengths were read from the videos themselves. Package versions, dates and licences for the software section come from the PyPI JSON API on 5 October 2026 and are reliable; GitHub star counts were not available because the GitHub API was gated. Polars 2.0 is at release-candidate stage (rc.2, 20 September 2026) with breaking changes, so the course environment should pin `polars>=1.44,<2` until materials are checked. Great Tables 1.0 (25 September 2026) now HTML-escapes cell values, which breaks older examples that injected HTML. Quarto 2 (Rust rewrite) is due late 2026; everything here refers to Quarto 1.10. polars-ols has had no release since August 2024 and its licence is not declared on PyPI. DataCamp has no plotnine course; the Coursera guided project is the only MOOC found. I could not find a documented newsroom (data journalism) use of plotnine, only Economist-style tutorials and contest entries. Posit Academy apprenticeship pricing is not public. The nycflights13 Python package's GitHub link returns 404 although the PyPI package installs. The Kaggle "Marketing Campaign Performance" dataset is synthetic and its licence was not checked; the Dunnhumby data are free only for non-commercial use.
