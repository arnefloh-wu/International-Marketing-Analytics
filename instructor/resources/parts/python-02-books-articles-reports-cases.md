# Modern Python data-analysis stack: books, journal articles, reports, teaching cases and course examples

Part 02 of the Python stack resource search (brief: `RESEARCH_BRIEF_PYTHON.md`). Covers four categories: Books; Journal articles; Reports; Teaching cases and course examples. Searched 5 October 2026. The sandbox proxy blocked most publisher, GitHub Pages and Posit domains (oreilly.com, quarto.org, posit.co, quarto.pub, *.github.io, wesmckinney.com, clauswilke.com, ggplot2-book.org, pypistats.org, pepy.tech). Those links were confirmed through search listings and, where possible, through the GitHub source repository of the site; entries that rest on a search listing alone are marked "(unverified)". The Consensus tool was not used; DOIs come from web search listings and were cross-checked against the journal landing pages that appeared in those listings.

# Books

### Python Polars: The Definitive Guide
- **Source:** Jeroen Janssens and Thijs Nieuwdorp, O'Reilly, April 2025, book (501 pages)
- **Link:** https://www.oreilly.com/library/view/python-polars-the/9781098156077/ and companion site https://polarsguide.com/ (unverified, companion site not fetched)
- **Why it matters:** The reference text for the course stack. Janssens (Posit) and Nieuwdorp cover expressions, eager and lazy APIs, data types, joins and reshaping, and, unusually, a full part on visualising Polars data with Altair, hvPlot, plotnine and Great Tables, plus pandas interoperability. The only book that treats the polars plus plotnine plus Great Tables combination as one workflow.
- **Use in course:** sessions 1-3 (chapters on expressions, reading data and visualisation as background reading for labs); paid (about EUR 60 print, or via an institutional O'Reilly Learning subscription if WU has one).

### Modern Polars
- **Source:** Kevin Heavey, 2022-2024 (rolling), free online book (GitHub, built with Quarto)
- **Link:** https://kevinheavey.github.io/modern-polars/ (site blocked by proxy; source confirmed at https://github.com/kevinheavey/modern-polars)
- **Why it matters:** Side-by-side pandas and polars code for the same tasks (indexing, method chaining, tidy data, time series, scaling), modelled on Tom Augspurger's "Modern Pandas". The fastest way for a student or an AI assistant that already "thinks in pandas" to see the polars idiom.
- **Use in course:** session 1-2 (reading, a pandas-to-polars migration reference for students who arrive with pandas snippets from ChatGPT); free.

### Effective Polars: Optimized Data Manipulation for Polars 1.0
- **Source:** Matt Harrison (with Anique Khawar and Thomas M. Ahern), self-published (Treading on Python series), March 2024, updated edition for Polars 1.0 July 2024, book (368 pages)
- **Link:** https://github.com/mattharrison/effective_polars_book (code and materials); Amazon listing https://www.amazon.com/Effective-Polars-Optimized-Data-Manipulation/dp/B0D911QH19
- **Why it matters:** Opinionated, chain-first style from the author of Effective Pandas; short chapters on columns, joins, strings, dates, group-by and lazy evaluation with real datasets, and a clear argument for why method chaining produces readable, debuggable analysis code. Harrison also runs corporate training, so the examples are built for people who learn by doing.
- **Use in course:** session 2 (lab reference for group-by and reshaping); paid (about EUR 40 print or PDF).

### Polars Cookbook
- **Source:** Yuki Kakegawa, Packt, August 2024, book (394 pages, over 60 recipes for Polars 1.x)
- **Link:** https://www.packtpub.com/en-us/product/polars-cookbook-9781805125150 and https://www.oreilly.com/library/view/polars-cookbook/9781805121152/
- **Why it matters:** Recipe format (reading CSV, Parquet and databases; aggregations, window functions, string handling, missing values, pivots and joins, time series, pandas and PyArrow interop). Good when a student needs "how do I do X" rather than a narrative; weaker on visualisation and reporting.
- **Use in course:** background (lab troubleshooting reference); paid (about EUR 45, Packt subscription or O'Reilly Learning).

### Python for Data Analysis, 3rd edition
- **Source:** Wes McKinney, O'Reilly, 2022, book, free online (open-access HTML of the full text)
- **Link:** https://wesmckinney.com/book/ (site blocked by proxy; confirmed at https://github.com/wesm/pydata-book)
- **Why it matters:** The pandas author's own textbook, free online with notebooks. Still the clearest introduction to the dataframe mental model (tidy columns, group-by, joins, reshaping, time series) that polars inherits and tightens. Use it to explain the concepts, then show the polars equivalent.
- **Use in course:** session 1-2 (background reading, chapters 5, 8 and 10); free.

### Python Data Science Handbook, 2nd edition
- **Source:** Jake VanderPlas, O'Reilly, 2022 (2e), book, free online as Jupyter notebooks
- **Link:** https://jakevdp.github.io/PythonDataScienceHandbook/ (site blocked by proxy; confirmed at https://github.com/jakevdp/PythonDataScienceHandbook)
- **Why it matters:** Free, notebook-based coverage of NumPy, pandas, matplotlib and scikit-learn with Colab and Binder launch buttons. The matplotlib chapters are the best short explanation of why a grammar of graphics (plotnine) is easier for beginners than imperative plotting.
- **Use in course:** background (students who want the matplotlib and scikit-learn layer under plotnine and statsmodels); free.

### Effective Pandas 2: Opinionated Patterns for Data Manipulation
- **Source:** Matt Harrison, self-published (Treading on Python), January 2024, book (580 pages)
- **Link:** https://www.amazon.co.uk/Effective-Pandas-Opinionated-Patterns-Manipulation/dp/B0CSRGH8R3 (unverified beyond search listings)
- **Why it matters:** Updated for pandas 2 (PyArrow-backed dtypes, copy-on-write). Its chaining style is the pandas counterpart of the polars idiom, so it is the right pandas book to recommend if a student must read legacy pandas code or a dataset only ships with pandas examples.
- **Use in course:** background (optional for students who meet pandas in internships); paid (about EUR 45).

### Fundamentals of Data Visualization
- **Source:** Claus O. Wilke, O'Reilly, 2019, book, free online (CC BY-NC-ND)
- **Link:** https://clauswilke.com/dataviz/ (site blocked by proxy; confirmed at https://github.com/clauswilke/dataviz)
- **Why it matters:** Tool-agnostic principles (which chart for which question, colour, redundancy, uncertainty, "ugly, bad and wrong" figures) written by a ggplot2 power user; the figures are built with the grammar-of-graphics logic plotnine implements. The best text for grading student charts.
- **Use in course:** session 2-3 (reading before the visualisation lab; chapters 1-5 and 29 "Telling a story"); free.

### ggplot2: Elegant Graphics for Data Analysis, 3rd edition
- **Source:** Hadley Wickham, Danielle Navarro and Thomas Lin Pedersen, Springer, 3e online 2023-2024, book, free online
- **Link:** https://ggplot2-book.org/ (site blocked by proxy; confirmed at https://github.com/hadley/ggplot2-book)
- **Why it matters:** plotnine is a near one-to-one port of ggplot2, so this is effectively the plotnine theory book: layers, aesthetics, scales, facets, themes, "the grammar" chapter. Students translate `aes()`, `geom_*`, `facet_wrap` and `theme` almost unchanged.
- **Use in course:** session 2 (background reading; part II "The grammar"); free.

### Python for Marketing Research and Analytics
- **Source:** Jason S. Schwarz, Chris Chapman and Elea McDonnell Feit, Springer, 2020, book (283 pages)
- **Link:** https://doi.org/10.1007/978-3-030-49720-0 and companion code https://github.com/python-marketing-research/python-marketing-research-1ed
- **Why it matters:** Python port of the well-known R for Marketing Research and Analytics: segmentation, choice, satisfaction drivers, marketing-mix style regressions, all on simulated marketing datasets, written for readers "with little programming background". pandas and seaborn based, so students need to translate to polars and plotnine, which is itself a useful exercise.
- **Use in course:** sessions 3-4 (case data and worked examples; the GitHub notebooks are Apache 2.0); book paid (Springer, about EUR 60; often free via university SpringerLink access).

### Applied Marketing Analytics Using Python
- **Source:** Gokhan Yildirim (Imperial College Business School) and Raoul V. Kübler (ESSEC), SAGE, July 2025, textbook (384 pages)
- **Link:** https://uk.sagepub.com/en-gb/eur/applied-marketing-analytics-using-python/book288563 (unverified beyond search listings)
- **Why it matters:** The first marketing-analytics textbook written for Python by European marketing academics: segmentation, marketing mix modelling, attribution, user-generated content and text mining, churn prediction, demand forecasting, image analytics, plus a chapter on data project management. Comes with datasets, code, slides, teaching guide and test bank.
- **Use in course:** sessions 3-5 (MMM and attribution chapters as reading; datasets for cases); paid (about GBP 45 paperback; instructor resources via SAGE).

### Quarto: The Practical Guide
- **Source:** Mine Çetinkaya-Rundel and Charlotte Wickham, in progress 2025-2026 (print edition planned), book, free online
- **Link:** https://quarto-tdg.org/ (site blocked by proxy; confirmed through search listings of chapter pages such as https://quarto-tdg.org/extensions)
- **Why it matters:** A concept-first Quarto guide (getting started, computation, documents, websites, slides, extensions) by the two people who teach Quarto most, and language-neutral with Python and R examples. Fills the gap between the reference docs and a course handout. Nick Tierney's "Quarto for Scientists" (https://qmd4sci.njtierney.com/, R-leaning) is the shorter alternative.
- **Use in course:** session 1 (reading before the first Quarto report) and session 5 (slides and websites); free.

### Coding for Economists and Python for Data Science (python4DS)
- **Source:** Arthur Turrell (Bank of England), 2020-2026 (rolling), two free online books built with Quarto
- **Link:** https://aeturrell.github.io/coding-for-economists (source https://github.com/aeturrell/coding-for-economists) and https://aeturrell.github.io/python4DS (source https://github.com/aeturrell/python4DS)
- **Why it matters:** python4DS is a chapter-by-chapter Python port of R for Data Science; Coding for Economists adds reproducible workflows, Quarto, uv, plotnine and lets-plot, regression and text. Both are written for social-science students without a programming background and are maintained with uv and GitHub Actions, so they model the exact tooling the course uses.
- **Use in course:** sessions 1-3 (reading, especially the Quarto, data tidying and visualisation chapters); free.

### Think Python, 3rd edition
- **Source:** Allen B. Downey, O'Reilly / Green Tea Press, 2024, book, free online (HTML and Jupyter notebooks)
- **Link:** https://allendowney.github.io/ThinkPython/ (site blocked by proxy; confirmed at https://github.com/AllenDowney/ThinkPython)
- **Why it matters:** The gentlest full Python introduction, rewritten for the 3rd edition around notebooks and with a chapter on using AI assistants to learn programming. For students who need the language basics (functions, lists, dictionaries) under the dataframe layer.
- **Use in course:** background (pre-course self-study for students with zero coding); free.

# Journal articles

### A layered grammar of graphics
- **Source:** Hadley Wickham, 2010, article, Journal of Computational and Graphical Statistics 19(1), 3-28
- **Link:** https://doi.org/10.1198/jcgs.2009.07098 (open preprint at https://vita.had.co.nz/papers/layered-grammar.html)
- **Why it matters:** The paper that defines the layer, aesthetic, geom, stat, scale and facet model plotnine implements. Twelve readable pages; the worked examples translate directly into plotnine code.
- **Use in course:** session 2 (short reading before the visualisation lab); open preprint.

### The Grammar of Graphics, 2nd edition
- **Source:** Leland Wilkinson, Springer, 2005, book (the original reference)
- **Link:** https://doi.org/10.1007/0-387-28695-0
- **Why it matters:** The source of the idea; Wickham 2010 and plotnine are its practical descendants. Dense, so cite rather than assign; the introduction chapter (10.1007/0-387-28695-0_1) is enough for students.
- **Use in course:** background; paywalled (SpringerLink, usually available via WU library).

### Tidy data
- **Source:** Hadley Wickham, 2014, article, Journal of Statistical Software 59(10)
- **Link:** https://doi.org/10.18637/jss.v059.i10
- **Why it matters:** Defines the "one variable per column, one observation per row" convention that polars `unpivot` and `pivot`, plotnine aesthetics and Great Tables all assume. The cleanest explanation of why reshaping matters before plotting.
- **Use in course:** session 2 (reading, 10 pages); open access.

### Literate programming
- **Source:** Donald E. Knuth, 1984, article, The Computer Journal 27(2), 97-111
- **Link:** https://doi.org/10.1093/comjnl/27.2.97
- **Why it matters:** The origin of "code and prose in one document" that runs through Sweave, knitr, R Markdown, Jupyter and Quarto. Two pages of the introduction are enough to show students that Quarto is not a gimmick but a 40-year-old idea.
- **Use in course:** session 1 (one-paragraph excerpt in the Quarto lecture); paywalled, widely available copies.

### Reproducible research in computational science
- **Source:** Roger D. Peng, 2011, article, Science 334(6060), 1226-1227
- **Link:** https://doi.org/10.1126/science.1213847
- **Why it matters:** The standard two-page statement of the reproducibility spectrum (publication only, to code and data, to linked executable code and data). Gives the course a vocabulary for why a Quarto report with embedded polars code is the deliverable rather than a PowerPoint.
- **Use in course:** session 1 (reading); paywalled (Science), author version circulates widely.

### R Markdown: integrating a reproducible analysis tool into introductory statistics
- **Source:** Ben Baumer, Mine Çetinkaya-Rundel, Andrew Bray, Linda Loi and Nicholas J. Horton, 2014, article, Technology Innovations in Statistics Education 8(1)
- **Link:** https://doi.org/10.5070/T581020118 (open access; preprint https://arxiv.org/abs/1402.1894)
- **Why it matters:** The first classroom study of literate documents with beginners: students who hand in rendered reports make fewer copy-paste errors and understand the analysis better. Everything it says about R Markdown applies to Quarto with Python.
- **Use in course:** background (justifies the "every assignment is a rendered .qmd" rule); open access.

### Tools and recommendations for reproducible teaching
- **Source:** Mine Dogucu and Mine Çetinkaya-Rundel, 2022, article, Journal of Statistics and Data Science Education 30(3), 251-260 (special issue on teaching reproducibility)
- **Link:** https://doi.org/10.1080/26939169.2022.2138645
- **Why it matters:** Practical guidance on building course materials reproducibly (version control, literate documents, GitHub Classroom, a public course website); the companion paper Çetinkaya-Rundel and Rundel 2018, "Infrastructure and tools for teaching computing throughout the statistical curriculum", The American Statistician 72(1), https://doi.org/10.1080/00031305.2017.1397549, covers the infrastructure side.
- **Use in course:** background (instructor reading for course design); open access.

### Reproducibility in the classroom
- **Source:** Mine Dogucu, 2025, review article, Annual Review of Statistics and Its Application 12, 89-105
- **Link:** https://doi.org/10.1146/annurev-statistics-112723-034436
- **Why it matters:** The most recent synthesis of what teaching reproducibility means in statistics and data science courses (tools, assessment, Quarto and notebooks, open materials). A good single citation for the syllabus.
- **Use in course:** background; paywalled (Annual Reviews), preprint on ResearchGate.

### A fresh look at introductory data science
- **Source:** Mine Çetinkaya-Rundel and Victoria Ellison, 2021, article, Journal of Statistics and Data Science Education 29(S1), S16-S26
- **Link:** https://doi.org/10.1080/10691898.2020.1804497 (preprint https://arxiv.org/abs/2008.00315)
- **Why it matters:** Describes the Duke STA 199 design (data first, modelling late, GitHub from week one, literate reports throughout) that most modern Python-and-Quarto courses copy. Useful for the sequencing of a five-session course.
- **Use in course:** background (course design); open access.

### Innovative and interactive statistics teaching using Quarto
- **Source:** Evans, 2026, article, Teaching Statistics (Wiley), early view
- **Link:** https://doi.org/10.1111/test.12409 (unverified beyond the Wiley search listing)
- **Why it matters:** The first journal article specifically about Quarto in the classroom (interactive documents, slides and exercises). Recent enough to reflect Quarto 1.6 and later.
- **Use in course:** background; paywalled (Wiley), check WU access.

### Jupyter Notebooks: a publishing format for reproducible computational workflows
- **Source:** Thomas Kluyver, Benjamin Ragan-Kelley, Fernando Pérez et al., 2016, conference paper, Positioning and Power in Academic Publishing (ELPUB 2016), 87-90
- **Link:** https://doi.org/10.3233/978-1-61499-649-1-87 (open access; also https://escholarship.org/uc/item/08b3d4s2)
- **Why it matters:** The canonical citation for the notebook format Quarto renders with Python (Quarto executes .qmd files through Jupyter kernels). Four pages, explains kernels, cells and nbconvert, which demystifies what Positron does when it renders.
- **Use in course:** session 1 (citation in the Quarto lecture); open access.

### Exploration and explanation in computational notebooks, and Ten simple rules for Jupyter notebooks
- **Source:** Adam Rule, Aurélien Tabard and James D. Hollan, 2018, CHI 2018 paper; Adam Rule, Amanda Birmingham et al., 2019, article, PLOS Computational Biology 15(7)
- **Link:** https://doi.org/10.1145/3173574.3173606 and https://doi.org/10.1371/journal.pcbi.1007007
- **Why it matters:** The 2018 study of a million GitHub notebooks shows how messy exploratory notebooks become (one in four has no prose); the 2019 "ten rules" paper is the fix (tell a story, document the process, modularise, record dependencies, share). Together they explain why the course asks for Quarto reports rather than raw notebooks.
- **Use in course:** session 1 and 5 (the ten rules as a grading checklist); CHI paywalled, PLOS open access.

### Towards scalable dataframe systems
- **Source:** Devin Petersohn, Stephen Macke, Doris Xin, William Ma, Doris Lee, Xiangxi Mo, Joseph E. Gonzalez, Joseph M. Hellerstein, Anthony D. Joseph and Aditya Parameswaran, 2020, article, Proceedings of the VLDB Endowment 13(12), 2033-2046
- **Link:** https://doi.org/10.14778/3407790.3407807 (open access PDF https://www.vldb.org/pvldb/vol13/p2033-petersohn.pdf)
- **Why it matters:** The first formal dataframe algebra and a critique of pandas (ordered rows, mixed types, eager execution) that reads like a design brief for polars (lazy plans, strict schemas, query optimisation). Sections 1-3 are accessible to non-engineers.
- **Use in course:** background (instructor reading; one slide on why polars is lazy); open access.

### Evaluation of dataframe libraries for data preparation on a single machine
- **Source:** Angelo Mozzillo, Luca Zecchini, Luca Gagliardelli, Adeel Aslam, Sonia Bergamaschi and Giovanni Simonini, 2025, conference article, EDBT 2025 (preprint 2023)
- **Link:** https://openproceedings.org/2025/conf/edbt/paper-96.pdf and https://doi.org/10.48550/arXiv.2312.11122
- **Why it matters:** Independent benchmark of pandas, Polars, Modin, Dask, Vaex, cuDF and PySpark on data-preparation tasks; conclusion is that pandas has the richest API for tiny data, polars is the default when data fits in RAM, Spark only beyond that. Gives the course an evidence-based answer to "why polars and not pandas".
- **Use in course:** session 1 (one figure in the tooling lecture); open access.

### The composable data management system manifesto
- **Source:** Pedro Pedreira, Orri Erling, Konstantinos Karanasos, Scott Schneider, Wes McKinney, Satya R. Valluri, Mohamed Zait and Jacques Nadeau, 2023, article, Proceedings of the VLDB Endowment 16(10), 2679-2685
- **Link:** https://doi.org/10.14778/3603581.3603604 (open access PDF https://www.vldb.org/pvldb/vol16/p2679-pedreira.pdf)
- **Why it matters:** Co-written by the pandas and Arrow creator; explains Apache Arrow as the shared columnar memory layer that lets polars, pandas 2, DuckDB and Parquet exchange data without copying. The background to why `pl.from_pandas` and `.to_pandas()` are cheap and why narwhals exists.
- **Use in course:** background; open access.

### Ten guidelines for better tables
- **Source:** Jonathan A. Schwabish, 2020, article, Journal of Benefit-Cost Analysis 11(2), 151-178
- **Link:** https://doi.org/10.1017/bca.2020.11
- **Why it matters:** The practical rulebook for presentation tables (right-align numbers, remove gridlines, group and highlight, put units in headers). Great Tables' design philosophy post (https://posit-dev.github.io/great-tables/blog/design-philosophy/, Iannone and Chow, April 2024) explicitly builds on this tradition, and each guideline maps to a `GT` method.
- **Use in course:** session 3 (reading before the Great Tables lab, with the design-philosophy post); paywalled (Cambridge), free summaries widely available.

### A new era of learning: considerations for ChatGPT as a tool to enhance statistics and data science education
- **Source:** Amanda R. Ellis and Emily Slade, 2023, article, Journal of Statistics and Data Science Education 31(2), 128-133
- **Link:** https://doi.org/10.1080/26939169.2023.2223609
- **Why it matters:** Early, balanced discussion of generative AI in data-analysis courses (calculator analogy, assessment design, where the tools fail). Short and open access; sets the tone for a course that is explicitly AI-assisted.
- **Use in course:** session 1 (reading alongside the course AI policy); open access.

### The use of generative AI in statistical data analysis and its impact on teaching statistics at universities of applied sciences
- **Source:** Schwarz, 2025, article, Teaching Statistics (Wiley)
- **Link:** https://doi.org/10.1111/test.12398
- **Why it matters:** A European (German-speaking) applied-university perspective on students using LLMs to write analysis code: what they get right, where they stop checking, and how to redesign tasks. Close to the CEMS setting.
- **Use in course:** background (instructor reading on assessment design); open access status not confirmed.

### Is GPT-4 a good data analyst?
- **Source:** Liying Cheng, Xingxuan Li and Lidong Bing, 2023, conference article, Findings of EMNLP 2023, 9496-9514
- **Link:** https://doi.org/10.18653/v1/2023.findings-emnlp.637 (code and data https://github.com/DAMO-NLP-SG/GPT4-as-DataAnalyst)
- **Why it matters:** Benchmarks GPT-4 against professional analysts on question-to-SQL-to-chart-to-insight tasks and finds comparable performance with characteristic errors (plausible but wrong aggregations, over-confident narratives). Good evidence for the "verify the dataframe, not the prose" habit. For the current state of LLM data-science agents see the 2025 survey at https://doi.org/10.48550/arXiv.2510.04023.
- **Use in course:** session 1 or 4 (discussion reading on AI-assisted analysis); open access.

### Teaching Python for data science: collaborative development of a modular and interactive curriculum
- **Source:** Multiple authors (author list on the JOSE page), 2021, article, Journal of Open Source Education 4(37), 138
- **Link:** https://doi.org/10.21105/jose.00138
- **Why it matters:** Describes an open, modular Python data-science curriculum (notebooks, autograded exercises, Binder) and the lessons from running it with beginners. Useful for borrowing exercise design patterns; also worth reading next to the business-school pieces in the Journal of Information Systems Education, for example "A foundation course in business analytics: design and implementation at two universities" (2020, https://eric.ed.gov/?id=EJ1281524).
- **Use in course:** background (course design); open access.

# Reports

### Python Developers Survey 2024 (JetBrains and Python Software Foundation)
- **Source:** JetBrains and PSF, December 2024 (eighth edition, over 30,000 respondents), report
- **Link:** https://lp.jetbrains.com/python-developers-survey-2024/ and the companion analysis "The state of data science 2024" https://blog.jetbrains.com/pycharm/2024/12/the-state-of-data-science/
- **Why it matters:** The best yearly census of Python tooling. 51 percent of respondents do data exploration; among them pandas 80 percent, NumPy 75 percent, Spark 16 percent, Polars 15 percent, Dask 7 percent; uv, Ruff and Polars are singled out as the Rust-based tooling wave. Gives students a realistic picture: polars is growing fast but pandas is what they will meet in most firms.
- **Use in course:** session 1 (one slide on the tooling landscape); free. Check for the 2025 edition, due late 2025 or early 2026 (not found in search).

### Stack Overflow Developer Survey 2025
- **Source:** Stack Overflow, July 2025 (about 49,000 respondents), report
- **Link:** https://survey.stackoverflow.co/2025/ and technology section https://survey.stackoverflow.co/2025/technology
- **Why it matters:** Python usage rose seven percentage points year on year, the largest jump of any major language, driven by AI and data work; the AI section documents how many developers use assistants daily and how much they trust them. Useful for the "why Python" and "why AI-assisted" framing.
- **Use in course:** session 1 (background slide); free.

### Polars adoption statistics: GitHub and PyPI
- **Source:** pola-rs/polars repository (GitHub) and PyPI download trackers (pypistats.org, ClickPy, pepy.tech), live, websites
- **Link:** https://github.com/pola-rs/polars (39.9k stars, 3.2k forks on 5 October 2026; 2.0 release candidates on the releases page) and https://clickpy.clickhouse.com/dashboard/polars (unverified; pypistats.org and pepy.tech blocked by proxy)
- **Why it matters:** Hard numbers for the "is this mainstream" question. Search listings cite about 24 million PyPI downloads a month and over 250 million total in September 2025, and over 675 million total by 2026 (figures from Wikipedia and blog listings, unverified). Also note the Polars 2.0 line: check that course material and the AI assistants' snippets match the version installed.
- **Use in course:** session 1 (tooling slide); free.

### Posit 2024 Year in Review and Public Benefit Corporation report
- **Source:** Posit PBC, December 2024 and 2025, company reports (both written in Quarto)
- **Link:** https://posit.co/blog/2024-posit-year-in-review and https://posit.co/about/pbc-report-2024 (unverified; posit.co blocked by proxy)
- **Why it matters:** The only official statements on Quarto's scale: about five full-time engineers on Quarto, three releases in 2024, Quarto Live, and the Python-side investments (Positron, Great Tables, plotnine, pointblank) that make the stack coherent. Posit does not publish Quarto download counts, so adoption claims elsewhere are anecdotal.
- **Use in course:** background; free.

### NumFOCUS annual and impact reports
- **Source:** NumFOCUS, 2023-2025, non-profit reports
- **Link:** https://numfocus.org/community/mission/annual-reports and https://www.nfimpact25.org/ (unverified beyond search listings)
- **Why it matters:** Lists the sponsored and affiliated projects behind the stack (pandas, NumPy, Jupyter, Arrow, matplotlib and others; 62 sponsored and 93 affiliated projects in 2024) and the small development grants that keep them alive. A reminder that the open-source stack has an institutional home, which matters when students ask "who maintains this".
- **Use in course:** background; free.

### Kaggle State of Data Science and Machine Learning 2022
- **Source:** Kaggle (Google), 2022 (sixth and last edition, 23,997 responses), report with full raw data
- **Link:** https://www.kaggle.com/kaggle-survey-2022 (executive summary PDF and dataset)
- **Why it matters:** Python and SQL as the dominant skills, VS Code overtaking Jupyter as the IDE, scikit-learn as the standard modelling library. Out of date on polars (not yet asked about) but the raw survey data is an excellent teaching dataset: students can replicate the report's charts in polars and plotnine.
- **Use in course:** session 2 (lab dataset for group-by and faceted charts); free (Kaggle account needed).

### Anaconda State of Data Science 2024 and 2025
- **Source:** Anaconda, 2024 (seventh edition) and 2025 (eighth edition), vendor reports
- **Link:** https://www.anaconda.com/resources/report/state-of-data-science-report-2024 and the 2025 key findings https://www.anaconda.com/blog/state-of-data-science-2024-key-findings (unverified beyond search listings)
- **Why it matters:** Practitioner survey on AI adoption in data work: 87 percent increasing AI use, 59 percent of work done on local laptops, and in 2025 only 22 percent of organisations calling their AI deployment strategic. Vendor-funded, so read as marketing-adjacent, but useful for the AI-assisted analysis framing.
- **Use in course:** background; free (registration wall).

# Teaching cases and course examples

### From Jupyter notebooks to websites with Quarto (PyData workshop) and Teaching Quarto in introductory data science courses
- **Source:** Mine Çetinkaya-Rundel (Duke University and Posit), 2024, workshop site and conference talk
- **Link:** https://mine.quarto.pub/quarto-pydata/ and https://mine-cetinkaya-rundel.github.io/teach-with-quarto/talks/2-intro-ds/ (both blocked by proxy, confirmed in search listings)
- **Why it matters:** The Python-specific Quarto workshop from the person who designed the modern intro data science course: notebook to document to website to slides, with GitHub Pages publishing. The "teach with Quarto" talk explains how she structures lectures, labs and homework as Quarto projects in STA 199 (R, https://mine.quarto.pub/sta-199/), which is the template to port.
- **Use in course:** session 1 (adapt the workshop as the first lab) and session 5 (publishing the final project); free.

### LSE DS105 Data for Data Science (and the Quarto course-website template)
- **Source:** Jon Cardoso-Silva, LSE Data Science Institute, 2022-2026 (rolling), public course website and GitHub template
- **Link:** https://lse-dsi.github.io/DS105/ (blocked by proxy, confirmed in listings) and https://github.com/jonjoncardoso/quarto-template-for-university-courses
- **Why it matters:** A full undergraduate Python course for coding beginners in a social-science school, built entirely in Quarto and GitHub Pages: pandas, lets-plot (grammar of graphics, a plotnine sibling), Jupyter and Quarto notebooks, Git and GitHub, weekly labs with public solutions. The template repository documents the Python environment set-up and is reused for DS101, DS202 and ME204.
- **Use in course:** sessions 1-2 (borrow lab structure; the week 2 and 3 labs on loading and reshaping data are the closest analogue); free.

### Posit Academy: Foundations of Python for Data Science
- **Source:** Posit PBC, 2024-2026, mentor-led course with public project repositories
- **Link:** https://academy.posit.co/ and https://github.com/rstudio/academy-python-solar-power (also academy-python-foreign-aid and academy-python-ide-tutorials)
- **Why it matters:** The closest commercial analogue to the course stack: Positron IDE, Quarto .qmd milestones, uv environments, pandas, plotnine, statsmodels and scikit-learn, organised around one real dataset per project with weekly mentor sessions. The public repos show how Posit scaffolds a beginner project (data folder, milestone files, environment file).
- **Use in course:** session 1-2 (copy the milestone structure for the group project); course paid (enterprise pricing), repos free.

### UConn STAT 3255/5255 Introduction to Data Science (Python, Quarto)
- **Source:** Jun Yan and students, University of Connecticut Department of Statistics, Spring 2025 (editions back to 2022), open course notes
- **Link:** https://statds.github.io/ids-s25/ (blocked by proxy; source confirmed at https://github.com/statds/ids-s25)
- **Why it matters:** A Python data science course whose entire textbook is a Quarto book written and extended by the students themselves (each student contributes a chapter via pull request): Python basics, pandas, visualisation (a plotnine section exists in earlier editions), SQL, modelling, with a chapter on reproducible data science with Quarto. A worked example of Quarto plus GitHub as the course infrastructure.
- **Use in course:** background (model for the "students contribute to a shared Quarto site" assignment); free.

### Data Science: A First Introduction (Python edition)
- **Source:** Tiffany Timbers, Trevor Campbell, Melissa Lee, Joel Ostblom and Lindsey Heagy, University of British Columbia, 2023-2025, open textbook (CC BY-NC-SA)
- **Link:** https://python.datasciencebook.ca/ (blocked by proxy; source confirmed at https://github.com/UBC-DSCI/introduction-to-datascience-python)
- **Why it matters:** A full first-year data science textbook in Python with Jupyter, pandas and Altair, a direct port of the R edition (tidyverse, ggplot2). Chapters on wrangling, visualisation, classification, regression and clustering are each a lab with worksheets, and the book's "reading, wrangling, visualising, communicating" arc matches a five-session structure.
- **Use in course:** sessions 2-4 (lab readings; translate Altair to plotnine); free.

### BYU-Idaho CSE 250 Data Science Programming
- **Source:** J. Hathaway and colleagues, Brigham Young University-Idaho, 2021-2026 (rolling), public course site
- **Link:** https://byuistats.github.io/CSE250-Course/ and the "Quarto for Data Science" page https://byuistats.github.io/CSE250-Course/course-materials/quarto-for-data-science/ (blocked by proxy, confirmed in listings)
- **Why it matters:** A project-based Python course for non-computer-science students that teaches the grammar of graphics, pandas and Altair, and requires every project to be a rendered Quarto document; includes a Python port of R for Data Science and a baseball database project. Good source of small graded projects with public rubrics.
- **Use in course:** sessions 2-3 (project templates and rubrics); free.

### Penn MUSA 550 Geospatial Data Science in Python: "From notebooks to the web: Quarto and GitHub Pages"
- **Source:** Nick Hand, University of Pennsylvania Weitzman School, Fall 2023, public course site and lecture
- **Link:** https://musa-550-fall-2023.github.io/content/week-9/lecture-9A.html (unverified; GitHub Pages blocked by proxy)
- **Why it matters:** A single, well-structured lecture that takes a Python Jupyter workflow to a published Quarto website with interactive charts on GitHub Pages, exactly the publishing step students struggle with. The whole course is itself a Quarto site built from notebooks.
- **Use in course:** session 5 (lab on publishing the final report); free.

### Practical Data Science with Python (Duke MIDS IDS 720)
- **Source:** Nick Eubank, Duke University, 2019-2026 (rolling), public course site and textbook
- **Link:** https://www.practicaldatascience.org/ (blocked by proxy, confirmed in listings) and https://www.nickeubank.com/teaching-2/
- **Why it matters:** Flipped, exercise-heavy course on wrangling messy real data with pandas, git and GitHub, written for students from social science and policy backgrounds; includes a "welcome non-Duke students" page that makes it usable as self-study. Its "defensive programming" and "what to do when you are stuck" pages are directly reusable for an AI-assisted course. Quarto use not confirmed.
- **Use in course:** sessions 1-2 (reading on data cleaning habits); free.

### Companion notebooks for Python for Marketing Research and Analytics, and SAGE resources for Applied Marketing Analytics Using Python
- **Source:** Schwarz, Chapman and Feit (GitHub, Apache 2.0, 2020-2024) and Yildirim and Kübler (SAGE instructor resources, 2025)
- **Link:** https://github.com/python-marketing-research/python-marketing-research-1ed and https://uk.sagepub.com/en-gb/eur/applied-marketing-analytics-using-python/book288563
- **Why it matters:** The two ready-made sets of marketing teaching cases in Python: segmentation, satisfaction drivers and choice (Schwarz et al.) and MMM, attribution, churn and forecasting (Yildirim and Kübler), each with datasets and notebooks. Both are pandas-based, so the natural assignment is "rewrite this analysis in polars and plotnine and present it as a Great Tables report".
- **Use in course:** sessions 3-4 (cases); GitHub free, SAGE resources require instructor registration.

### Business-school cases with datasets: "Applying Data Science and Analytics at P&G" and the HBP cases-with-datasets collection
- **Source:** Harvard Business School (case) and Harvard Business Publishing Education (collection), 2020-2025, teaching cases
- **Link:** https://www.hbs.edu/faculty/Pages/item.aspx?num=58380 and https://hbsp.harvard.edu/catalog/collections/cases-with-datasets-in-multiple-disciplines (unverified beyond search listings)
- **Why it matters:** The P&G case covers how a consumer-goods marketer built dashboards and analytics teams, a good discussion frame for "what a report should do for a manager". The HBP collection filters cases that ship with a dataset, which is what a polars and Quarto lab needs; Ivey Publishing has an equivalent filter.
- **Use in course:** session 5 (discussion case on reporting and dashboards); paid (HBP, about USD 5 to 9 per student copy).

### Quarto dashboards with Python (official guide) and a business-school example
- **Source:** Posit (Quarto documentation, 2023-2026) and Wake Forest School of Business ("Create your own data blog with Quarto and Python", class listing, 2024)
- **Link:** https://quarto.org/docs/dashboards/ (blocked by proxy; source confirmed at https://github.com/quarto-dev/quarto-web/tree/main/docs/dashboards, with Python requirements.txt) and https://career.business.wfu.edu/classes/create-your-own-data-blog-with-quarto-and-python/ (unverified)
- **Why it matters:** Quarto dashboards turn a .qmd with polars, plotnine or Plotly cells into a static dashboard (value boxes, tabsets, sidebars) deployable on GitHub Pages, so students can produce a manager-facing dashboard without Shiny or Tableau. The Wake Forest listing shows a business school already teaching Quarto with Python as a career skill.
- **Use in course:** session 5 (lab: convert the group report into a dashboard); free.

### University of Edinburgh "Introduction to Data Analysis" course repositories
- **Source:** University of Edinburgh School of Mathematics (edinburgh-data-science GitHub organisation), 2016-2024, course repositories
- **Link:** https://github.com/edinburgh-data-science
- **Why it matters:** Second-year undergraduate data analysis course built around McKinney's Python for Data Analysis, plus a first-year Foundations of Data Science course; useful mainly as an example of a mathematics department teaching Python data analysis from a free textbook. Little recent activity and no Quarto, so a weaker example than the others; the Carpentries at Edinburgh (https://edcarp.github.io/) run current Python workshops.
- **Use in course:** background; free.

# Gaps and caveats

The proxy blocked every publisher and most documentation and course hosts (O'Reilly, SAGE, Springer, Wiley, Cambridge, quarto.org, posit.co, quarto.pub, all GitHub Pages sites, pypistats.org and pepy.tech), so book details, course contents and download figures were confirmed from search listings and from the GitHub source repositories rather than the rendered pages; entries marked "(unverified)" rest on listings alone. The Polars download numbers (about 24 million a month in September 2025, over 675 million total in 2026) come from Wikipedia and blog listings and should be re-checked on ClickPy or pepy.tech before use on a slide. The Polars GitHub releases page shows 2.0 release candidates, so some books (Effective Polars for 1.0, Polars Cookbook for 1.x, the Definitive Guide written against 1.x) will have small API differences; the Definitive Guide's companion site may carry errata. Posit publishes no Quarto adoption numbers, so claims about Quarto's reach are qualitative. No published, Python-based "Data Science in a Box" port was found; the Python-first analogues are LSE DS105, UBC's Python edition and BYU-I CSE 250, and none of them yet uses polars or Great Tables in the public materials (pandas with lets-plot or Altair is the norm), so the course will be ahead of most public courses on the dataframe and table layers. The Stanford DATASCI 112 site (Dennis Sun) and the Edinburgh materials were checked but offer little Quarto or grammar-of-graphics content and were left out or downgraded. The Journal of Information Systems Education business-analytics pieces have no DOIs and were cited through ERIC. Paywalls: Wilkinson, Knuth, Peng, Rule 2018, Schwabish, Dogucu 2025 and the two Teaching Statistics articles need library access; everything else listed is open access or free online.
