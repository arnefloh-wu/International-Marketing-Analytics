# Research brief: Python data-analysis stack resource search (polars, plotnine, Great Tables, Quarto)

Purpose: a curated resource guide on the modern Python data-analysis stack used in the course: polars (dataframes), plotnine (grammar of graphics), Great Tables (publication tables), Quarto (reproducible reports and slides), plus the surrounding ecosystem (pandas interoperability, narwhals, Altair and matplotlib as alternatives, marimo and Jupyter, uv, statsmodels). Audience: the instructor of "International Marketing Analytics" (WU Vienna, CEMS, 30 master students with no programming background who do AI-assisted Python analytics in Positron, Quarto and GitHub). He uses it to choose readings, tutorials, cases, datasets and tools.

Write your findings as a Markdown file in instructor/resources/parts/python-<your-part>.md. Do not commit.

Format for every entry (keep it tight, 2 to 4 lines each):

### <Title>
- **Source:** author or organisation, year, type (book / article / report / website / video / case / software / person)
- **Link:** full URL (verify it resolves; prefer DOI or publisher page for articles)
- **Why it matters:** one or two sentences, concrete (what it covers, what makes it good)
- **Use in course:** session 1-5 or "background", and how (reading, lab, case, guest talk); access/cost if not free

Rules:
- Verify every link by fetching it (WebFetch) or at least confirming it in a search result; mark anything unverified with "(unverified)".
- Prefer 2019 or later for practical material; classics are welcome when they are the reference (e.g. Hanssens, Little 1979, Tellis).
- Rank within each category: best first, 5 to 15 entries per category, more only when clearly useful.
- Teaching angle matters: material that explains polars, plotnine, Great Tables and Quarto to beginners, migration guides from pandas and ggplot2, and worked marketing or business examples.
- Python first; mention the R origins (dplyr, ggplot2, gt) only where they help explain the Python package.
- For people: public professional profiles only (LinkedIn, university pages, company pages, conference speaker pages). Give name, role, organisation, city, why relevant, and a realistic guest-speaker angle (industry MMM practice, vendor, academic). Favour Vienna, Austria, Germany, Switzerland and wider Europe for guest speakers; global for people to follow. No private contact details.
- British English. No em dashes.
- End with a short "Gaps and caveats" paragraph: what you could not verify, paywalls, anything out of date.

Network note: the sandbox proxy blocks many publisher and vendor domains; github.com, pypi.org, raw.githubusercontent.com and some documentation hosts resolve. Fetch what you can, confirm the rest from search listings, and mark anything unconfirmed "(unverified)". Search budget is limited: plan queries, do not repeat them.
