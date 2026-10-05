# Research brief: Regression analysis in Python resource search

Purpose: a curated resource guide on regression analysis taught with Python: linear regression (OLS), non-linear effects (polynomials, logs, splines, saturation curves), moderation (interaction effects, simple slopes, Johnson-Neyman), mediation (indirect effects, bootstrapping, causal mediation), dummy and effect coding of categorical variables, assumptions and diagnostics (linearity, homoscedasticity, normality, multicollinearity and VIF, influential points, robust and clustered standard errors), and time-series regression (trend, seasonality, lags, autocorrelation, Newey-West, ARIMAX, distributed lags). Audience: the instructor of "International Marketing Analytics" (WU Vienna, CEMS, 30 master students with no programming background who do AI-assisted Python analytics in Positron, Quarto and GitHub; the course builds towards marketing mix modelling). He uses it to choose readings, tutorials, cases, datasets and tools.

Write your findings as a Markdown file in instructor/resources/parts/regression-<your-part>.md. Do not commit.

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
- Teaching angle matters: material that explains these regression topics to business students, with marketing or international business examples (price and promotion elasticities, advertising response, cross-country moderation by culture or market characteristics, mediation via brand attitudes, sales over time).
- Python first (statsmodels formula API, linearmodels, scikit-learn, pingouin, patsy or formulaic, marginaleffects for Python); mention R, SPSS PROCESS or Stata only where they are the standard reference for a method (e.g. Hayes PROCESS for moderation and mediation).
- For people: public professional profiles only (LinkedIn, university pages, company pages, conference speaker pages). Give name, role, organisation, city, why relevant, and a realistic guest-speaker angle (industry MMM practice, vendor, academic). Favour Vienna, Austria, Germany, Switzerland and wider Europe for guest speakers; global for people to follow. No private contact details.
- British English. No em dashes.
- End with a short "Gaps and caveats" paragraph: what you could not verify, paywalls, anything out of date.

Network note: the sandbox proxy blocks many publisher and vendor domains; github.com, pypi.org, raw.githubusercontent.com and some documentation hosts resolve. Fetch what you can, confirm the rest from search listings, and mark anything unconfirmed "(unverified)". Search budget is limited: plan queries, do not repeat them.
