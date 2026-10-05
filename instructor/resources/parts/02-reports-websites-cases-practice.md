# Part 2: Reports, websites and blogs, teaching cases, practice examples

Scope: industry and vendor reports on MMM and measurement; practitioner websites, blogs and newsletters; teaching cases and free case-style datasets; documented real-world MMM implementations. Entries are ranked best first within each section. Verification note: in this session the network proxy blocked direct fetching of almost every publisher domain (only github.com resolved), so most links are confirmed through search-engine results rather than by opening the page; those are marked "(confirmed in search results)". Links opened directly are marked "(fetched)". Anything else is marked "(unverified)".

---

## 1. Reports

### Marketing Mix Modeling Best Practices (Nielsen with Google and Meta)
- **Source:** Nielsen, Google and Meta, 2022, report (PDF, about 20 pages)
- **Link:** https://www.nielsen.com/wp-content/uploads/sites/2/2022/09/Marketing-Mix-Modeling-Best-Practices-EN.pdf (confirmed in search results)
- **Why it matters:** The most-cited vendor-neutral checklist for model specification: model at the most granular geography available, include non-marketing drivers (a media-only MMM overstated ad ROI by 68 per cent in Nielsen's comparison), handle digital granularity and reach. Companion Nielsen note analyses 19 Japanese models to show regional beats national data.
- **Use in course:** Session 2 (data and model specification) required reading; pairs with the geo-hierarchy lab. Free.

### Modernizing MMM: Best Practices for Marketers (IAB)
- **Source:** IAB (US) with MMM vendors, December 2025, report (PDF)
- **Link:** https://www.iab.com/guidelines/modernizing-mmm-best-practices-for-marketers/ and PDF https://www.iab.com/wp-content/uploads/2025/12/IAB_Modernizing_MMM_Best_Practices_for_Marketers_December_2025.pdf (confirmed in search results)
- **Why it matters:** Newest vendor-neutral industry guide; frames "timely, auditable, decision-ready" MMM, covers calibration with experiments, cadence, governance and includes cross-industry case studies.
- **Use in course:** Session 1 (measurement landscape) and Session 5 (from model to decision); free.

### Modern Measurement Playbook (Google)
- **Source:** Google / Think with Google, 2023 (updated 2024), report (PDF, 44 pages)
- **Link:** https://www.thinkwithgoogle.com/_qs/documents/18393/For_pub_on_TwG___External_Playbook_Modern_Measurement.pdf (confirmed in search results); landing page https://business.google.com/us/think/measurement/drive-business-goals-modern-measurement/
- **Why it matters:** Sets out the "measurement tripod" (attribution, incrementality experiments, MMM) and how to triangulate them; concise and well illustrated, so it works as a framing text for the whole course.
- **Use in course:** Session 1 pre-reading; Session 5 for the triangulation discussion. Free.

### The MMM Handbook: A Guide for Developing Impactful Marketing Mix Models (Google)
- **Source:** Google (Think with Google, EMEA), 2023, report (PDF, "a CMO's handbook")
- **Link:** https://www.thinkwithgoogle.com/_qs/documents/18104/Marketing_Mix_Modelling_-_A_CMOs_handbook.pdf (confirmed in search results)
- **Why it matters:** Short management-level guide: start with the right business questions, pick KPIs, capture all drivers, validate, act. Good contrast to the technical Nielsen document.
- **Use in course:** Session 1 or background; free.

### Meridian Playbook (Google)
- **Source:** Google, 2025, report (PDF)
- **Link:** https://www.thinkwithgoogle.com/_qs/documents/18498/Meridian_Playbook_1s4EUSU.pdf (confirmed in search results)
- **Why it matters:** Step-by-step guidance on running Google's open-source Bayesian MMM (data requirements, geo-level set-up, priors from experiments, budget optimiser). Directly transferable to a Python lab.
- **Use in course:** Session 3 (Bayesian MMM lab) or Session 4 (budget allocation); free.

### ROI Genome (Analytic Partners)
- **Source:** Analytic Partners, ongoing series 2020 to 2025, reports and briefs
- **Link:** https://analyticpartners.com/roi-genome/report-marketing-through-crisis-and-beyond/ and newsroom summaries such as https://analyticpartners.com/knowledge-hub/newsroom/report-roi-genome-adopt-scenario-planning-increases-roi/ (confirmed in search results)
- **Why it matters:** Meta-analysis across 1,000+ brands and 50 countries of MMM results: brand versus performance messaging, recession spend, CTV, scenario planning (25 to 70 per cent ROI gains). Rare cross-country benchmark material.
- **Use in course:** Session 4 (cross-country budget allocation) as discussion input; Session 5. Free summaries, full reports gated behind registration.

### Marketing Mix Modelling: A How-To Guide for Marketers (WARC and Magic Numbers)
- **Source:** Dr Grace Kite (Magic Numbers) with WARC, 2023, report (PDF, five chapters)
- **Link:** https://magicworks.training/wp-content/uploads/2024/04/Marketing-Mix-Modelling-A-How-To-Guide-for-Marketers-FINAL.pdf (confirmed in search results; original on WARC is paywalled)
- **Why it matters:** Practical and candid on choosing suppliers, embedding MMM in an organisation, reading results and common failure modes; includes UK case studies. Written by an econometrician who runs models for a living.
- **Use in course:** Session 5 (using MMM in management) reading; free mirror, WARC version paywalled.

### Profit Ability 2: The New Business Case for Advertising (Ebiquity and Thinkbox)
- **Source:** Ebiquity for Thinkbox with Gain Theory, EssenceMediacom, Mindshare and Wavemaker, May 2024, report (PDF)
- **Link:** https://ebiquity.com/news-insights/press/profit-ability-2-the-new-business-case-for-advertising/ and PDF https://assets.ctfassets.net/ptzdhtf6t0jg/KkqtmmsDkxlGl0wlE72TF/178b9f6af6d3af215154e12455485e92/Profit_Ability_2_The_new_business_case_for_advertising_report.pdf (confirmed in search results)
- **Why it matters:** Pooled MMM across GBP 1.8bn of UK media, 141 brands and 10 channels; shows short-term versus sustained profit ROI by channel (TV 5.61, online video 3.86, generic PPC 3.52) and that about 60 per cent of effect lands after 13 weeks. A clean example of what adstock and long-term effects mean commercially.
- **Use in course:** Session 2 (adstock and carry-over) and Session 4; free.

### Paid Media Effectiveness Handbook (WFA and Ebiquity)
- **Source:** World Federation of Advertisers with Ebiquity, 2026, report
- **Link:** https://wfanet.org/leadership/marketing/media-effectiveness (confirmed in search results); related WFA benchmark of MMM partners in EMEA https://wfanet.org/knowledge/item/2025/03/31/benchmark-marketing-mix-modelling-(mmm)-partners-in-emea
- **Why it matters:** Based on research with advertisers controlling about USD 40bn of paid media; explains how MMM, attribution, experiments and brand metrics fit together and reports that 80 per cent use MMM but only 13 per cent turn data into insight quickly. The EMEA vendor benchmark is useful for a European vendor-selection discussion.
- **Use in course:** Session 5 and background; WFA members only (summary articles free).

### Magic Quadrant for Marketing Mix Modeling Solutions (Gartner)
- **Source:** Gartner, November 2024 (first edition) and 2025 edition, analyst report; preceded by the Market Guide for MMM Solutions (April 2024)
- **Link:** Gartner topic page https://www.gartner.com/en/marketing/topics/marketing-mix-modeling and Market Guide https://www.gartner.com/en/documents/5389963 (confirmed in search results); free vendor reprints via Analytic Partners, Ipsos MMA, Ekimetrics press pages
- **Why it matters:** The reference map of the commercial MMM vendor landscape (Leaders: Analytic Partners, Ipsos MMA, Ekimetrics, Nielsen and others) with Gartner's 2024 survey finding that 64 per cent of senior marketing leaders have adopted MMM. Useful to show students what "commercial tool" means versus open source.
- **Use in course:** Session 1 or 5, short discussion; paywalled, use vendor reprints.

### The Forrester Wave: Marketing Measurement and Optimization
- **Source:** Forrester, Q3 2023 (solutions) and Q1 2026 (services), analyst reports
- **Link:** Q3 2023 reprint PDF https://cdn.prod.website-files.com/66e2d4967d2fc7095ce820ef/66fd6a0e18d00d2ed1d06c79_The-Forrester-Wave_Marketing-Measurement-And-Optimization_Q3-2023.pdf and Q1 2026 summary https://gaintheory.com/forrester/ (confirmed in search results)
- **Why it matters:** Nine providers scored on 38 criteria including global capabilities, unified measurement and model operations; complements Gartner.
- **Use in course:** Background for vendor comparison; reprints free, original paywalled.

### Six Steps to More Effective Marketing Measurement (BCG)
- **Source:** Boston Consulting Group, 2025, article/report
- **Link:** https://www.bcg.com/publications/2025/six-steps-to-more-effective-marketing-measurement (confirmed in search results); related https://www.bcg.com/x/the-multiplier/four-legged-approach-to-understanding-marketing-roi
- **Why it matters:** Consultancy view with survey data: 39 per cent of leading marketers run MMM monthly, 40 per cent calibrate with incrementality tests, growing use of brand metrics in MMM. Good for the "MMM as a management system" angle.
- **Use in course:** Session 5 reading; free.

### MMM adoption study (Kantar and Meta)
- **Source:** Kantar with Meta, 2025, report (PDF)
- **Link:** https://s3.amazonaws.com/media.mediapost.com/uploads/Kantar___META_Thought_Leadership.pdf (fetched; PDF resolves)
- **Why it matters:** Global survey of 1,935 measurement professionals at companies spending over USD 1m a year on digital; adoption dynamics, barriers and what "good" looks like. Kantar's own MMM pages add the long-term brand-effect angle.
- **Use in course:** Session 1 background; free.

### Market Mix Modelling Landscape Report 2025 (IAB Australia)
- **Source:** IAB Australia Ad Effectiveness Council, September 2025 (updated December 2025), report
- **Link:** https://www.iabaustralia.com.au/resource/market-mix-modelling-landscape-report-2025/ (confirmed in search results)
- **Why it matters:** Directory of twelve MMM vendors (classical econometrics to Bayesian and ML), a marketer's checklist and plain-language method comparison; a handy template for a vendor-evaluation exercise.
- **Use in course:** Session 5 exercise (evaluate a vendor pitch); free.

### The Essential Guide to Marketing Mix Modeling and Multi-Touch Attribution (IAB and MMA Global)
- **Source:** IAB with MMA Global, November 2019, guidebook (PDF)
- **Link:** https://www.iab.com/wp-content/uploads/2019/11/IAB_MMA_MTA-Guidebook_Nov-2019.pdf (confirmed in search results)
- **Why it matters:** Older but still the clearest side-by-side of MMM and MTA (data, granularity, use cases, limitations). Meta's own note "Considerations for creating modern marketing mix models" (https://www.facebook.com/business/news/insights/considerations-for-creating-modern-marketing-mix-models) is a short complement.
- **Use in course:** Session 5 (attribution versus MMM); free.

---

## 2. Websites, blogs and newsletters

### PyMC Labs blog
- **Source:** PyMC Labs (authors include Thomas Wiecki, Juan Orduz, Carlos Trujillo, Will Dean), 2021 to 2026, blog
- **Link:** https://www.pymc-labs.com/blog-posts (confirmed in search results); key posts: https://www.pymc-labs.com/blog-posts/bayesian-media-mix-modeling-for-marketing-optimization , https://www.pymc-labs.com/blog-posts/modelling-changes-marketing-effectiveness-over-time , https://www.pymc-labs.com/blog-posts/full-funnel-mmm-optimization
- **Why it matters:** The home of PyMC-Marketing thinking: Bayesian MMM, time-varying effectiveness, funnel-aware models, lift-test calibration, the HelloFresh case. Python code throughout.
- **Use in course:** Sessions 2 to 4 lab readings; free.

### Google Meridian documentation and repository
- **Source:** Google, 2025 to 2026, website and software (Python, Apache 2.0)
- **Link:** https://developers.google.com/meridian (confirmed in search results); https://github.com/google/meridian (fetched)
- **Why it matters:** Reference docs for a hierarchical geo-level Bayesian MMM with reach and frequency, experiment priors and budget optimiser; Colab tutorial with sample data; superseded LightweightMMM (https://github.com/google/lightweight_mmm, archived, fetched).
- **Use in course:** Session 3 and 4 labs; free.

### Meta Robyn site and repository
- **Source:** Meta Marketing Science (Gufeng Zhou and others), 2021 to 2026, website and software (R primary, Python beta, MIT)
- **Link:** https://facebookexperimental.github.io/Robyn/ (confirmed in search results); https://github.com/facebookexperimental/Robyn (fetched); case studies https://facebookexperimental.github.io/Robyn/docs/case-studies/
- **Why it matters:** Ridge regression plus evolutionary hyperparameter search, calibration with lift tests, simulated weekly demo data; the most used open-source MMM in practice and the natural contrast to the Bayesian tools.
- **Use in course:** Session 3 comparison (R versus Python), optional lab; free.

### Recast blog and MMM Academy
- **Source:** Recast (Michael Kaminsky, Thomas Vladeck), 2021 to 2026, blog and newsletter
- **Link:** https://getrecast.com/mmm-academy/building-a-media-mix-model/ , https://getrecast.com/integrating-geo-testing-with-marketing-mix-modeling/ , https://getrecast.com/mmm-examples/ (confirmed in search results)
- **Why it matters:** The most opinionated practitioner writing on MMM identification problems, geo-test calibration, long-term brand effects and vendor hype; the "who is talking about MMM" page lists public brand examples.
- **Use in course:** Session 3 (calibration) and Session 5; free.

### Dr Juan Camilo Orduz, personal blog
- **Source:** Juan Camilo Orduz (PyMC Labs, Berlin), 2021 to 2026, blog
- **Link:** https://juanitorduz.github.io/pymc_mmm/ and https://juanitorduz.github.io/orbit_mmm/ (confirmed in search results)
- **Why it matters:** Fully reproducible PyMC notebooks on adstock, saturation, time-varying coefficients, Orbit's KTR model and hierarchical MMM; ideal lab scaffolding. Berlin-based, so also a realistic guest-speaker lead for the people part.
- **Use in course:** Sessions 2 and 3 lab material; free.

### Aryma Labs Substack
- **Source:** Venkat Raman and Ridhima Kumar (Aryma Labs, India), 2023 to 2026, newsletter
- **Link:** https://arymalabs.substack.com/p/marketing-mix-modeling-mmm-101 , https://arymalabs.substack.com/p/marketing-mix-modeling-mmm-is-just , https://arymalabs.substack.com/p/learning-from-og-mmm-fmcg-cpg-mmm (confirmed in search results)
- **Why it matters:** Critical, statistically careful posts ("is MMM just linear regression?", "one true MMM?", lessons from FMCG econometrics); good for teaching scepticism towards automated tools.
- **Use in course:** Session 2 discussion reading; free.

### Measured learning centre
- **Source:** Measured (US), 2020 to 2026, website
- **Link:** https://www.measured.com/resources/ , https://www.measured.com/faq/incrementality-attribution-mmm-decision-tree/ , https://www.measured.com/faq/real-life-media-mix-modeling-mmm-examples-true-incrementality/ (confirmed in search results)
- **Why it matters:** Decision tree for when to use incrementality tests, attribution or MMM; a "how to QA an MMM" checklist; ten named brand examples. Vendor site but unusually instructive.
- **Use in course:** Session 5; free.

### Haus blog and Incrementality School
- **Source:** Haus (US; founders from Netflix and Google experimentation teams), 2023 to 2026, blog
- **Link:** https://www.haus.io/blog/why-incrementality-testing-belongs-with-your-mmm-and-where-to-start and https://www.haus.io/blog/incrementality-experiments-a-comprehensive-guide (confirmed in search results)
- **Why it matters:** Clear explanations of geo experiments, synthetic control and "causal MMM" built on experiments; the experiments-first counterweight to model-first vendors.
- **Use in course:** Session 3 or the experiments session; free.

### Sellforte blog
- **Source:** Sellforte (Helsinki), 2022 to 2026, blog
- **Link:** https://sellforte.com/blog/what-is-causal-marketing-mix-modeling-mmm and https://sellforte.com/blog/marketing-mix-modeling-rfp-retail (confirmed in search results)
- **Why it matters:** European SaaS vendor writing on retail and e-commerce MMM, causal MMM and a procurement/RFP guide that students can use in a vendor-selection exercise.
- **Use in course:** Session 5 exercise; free.

### Mutinex (Henry Innis) and Madison and Wall interviews
- **Source:** Mutinex (Sydney) and Madison and Wall Substack (Brian Wieser), 2024 to 2026, blog and newsletter
- **Link:** https://mutinex.co/the-power-of-mmm-to-unlock-true-growth/ , https://madisonandwall.substack.com/p/mutinex-on-mmms-mtas-and-more , https://www.beet.tv/2026/09/mmm-must-plug-directly-into-bidding-systems-to-stay-competitive-mutinex-ceo-says.html (confirmed in search results)
- **Why it matters:** The "always-on MMM feeding bidding systems" thesis and a sceptical industry analyst's questioning of it; good for a debate on MMM cadence and over-use of incrementality tests.
- **Use in course:** Session 5 debate; free.

### Cassandra resources
- **Source:** Cassandra (European MMM SaaS), 2023 to 2026, website
- **Link:** https://cassandra.app/resources/a-dee-dive-into-the-algorithm-behind-media-mix-modeling-and-optimization (confirmed in search results)
- **Why it matters:** Readable walk-through of the algorithm behind a commercial MMM and optimiser, written for marketers rather than statisticians.
- **Use in course:** Session 4 background; free.

### Ebiquity Insights blog
- **Source:** Ebiquity (London), 2022 to 2026, blog
- **Link:** https://ebiquity.com/news-insights/blog/bayesian-media-mix-modelling/ , https://ebiquity.com/news-insights/blog/automation-marketing-mix-modelling/ , https://ebiquity.com/news-insights/blog/from-measurement-to-management-the-emerging-role-of-mmm/ (confirmed in search results)
- **Why it matters:** The classical econometrics view: "Bayesian MMM: cure-all or caveat emptor?", pros and cons of always-on automation, MMM as a management discipline; strong European advertiser perspective.
- **Use in course:** Session 3 counter-reading; free.

### MASS Analytics blog and Measure Up podcast
- **Source:** MASS Analytics (Tunis and London), 2020 to 2026, blog and podcast
- **Link:** https://mass-analytics.com/marketing-mix-modeling-blogs/learn-marketing-mix-modeling/ and https://mass-analytics.com/marketing-mix-modeling-blogs/how-geo-experiments-measure-incrementality/ (confirmed in search results); podcast https://creators.spotify.com/pod/show/measure-up
- **Why it matters:** Structured "learn MMM" curriculum, masterclasses and an interview podcast with practitioners; the geo-experiment explainer is concise.
- **Use in course:** Background self-study; free.

### Hands-On Data: "The hard thing about Marketing Mix Models"
- **Source:** Hands-On Data (independent data scientist), 2024, Substack post
- **Link:** https://handsondata.substack.com/p/the-hard-thing-about-marketing-mix (confirmed in search results)
- **Why it matters:** Honest practitioner account of identification, data and organisational problems in MMM; short and quotable.
- **Use in course:** Session 2 warm-up; free.

### Vexpower MMM learning path (Mike Taylor)
- **Source:** Mike Taylor (Vexpower, former Ladder agency), 2022 to 2025, simulator-based courses
- **Link:** https://www.vexpower.com/paths/marketing-mix-modeling and https://app.vexpower.com/sim/can-we-try-uber-orbit/ (confirmed in search results)
- **Why it matters:** Scenario-style exercises (Robyn, LightweightMMM, Orbit) that mimic client briefs; a model for how to write lab assignments.
- **Use in course:** Inspiration for assignments; paid subscription, some free content.

---

## 3. Teaching cases (Cases for Teaching)

### Multiple Regression and Marketing-Mix Models (Darden technical note)
- **Source:** Rajkumar Venkatesan and Shea Gibbs, Darden Business Publishing, 2013, case/technical note; Darden UVA-M-0855, HBP UV6764, Case Centre 118828
- **Link:** https://store.hbr.org/product/multiple-regression-and-marketing-mix-models/UV6764 , https://store.darden.virginia.edu/multiple-regression-and-marketing-mix-models , https://www.thecasecentre.org/products/view?id=118828 (confirmed in search results)
- **Why it matters:** The standard classroom note on regression-based MMM (omitted-variable bias, interpretation of coefficients, elasticities); used in Darden's Big Data in Marketing elective.
- **Use in course:** Session 2 pre-reading; paid (about USD 5 to 9 per student via HBP or Case Centre).

### Note on Marketing Mix Models: Evaluating "Bang for the Buck" (Darden)
- **Source:** Paul W. Farris, Darden Business Publishing, 1987, technical note M-0339
- **Link:** https://store.darden.virginia.edu/note-on-marketing-mix-models-evaluating-bang-for-the-buck (confirmed in search results)
- **Why it matters:** The classic resource-allocation framing of MMM (marginal returns, response curves) that today's optimisers still implement; short and still assigned.
- **Use in course:** Session 4 background; paid, low cost.

### Digital Marketing at HBS Online (HBS case 521-027)
- **Source:** Sunil Gupta and Rajiv Lal, Harvard Business School, 2020 (revised 2024), case; Case Centre 174588
- **Link:** https://www.hbs.edu/faculty/Pages/item.aspx?num=58780 and https://www.thecasecentre.org/products/view?id=174588 (confirmed in search results)
- **Why it matters:** Management must allocate a digital budget across channels and course portfolios using channel performance data; raises attribution versus incrementality and portfolio trade-offs with real numbers.
- **Use in course:** Session 4 or 5 case discussion; paid (HBP, about USD 9 per student plus teaching note).

### Amperity: First-Party Data at a Crossroads (HBS case 524-017)
- **Source:** Elie Ofek, Hema Yoganarasimhan and Alexis Lefort, Harvard Business School, 2024, case
- **Link:** https://www.hbs.edu/faculty/research/publications/Pages/default.aspx?topic=Digital+Marketing (confirmed in search results; case number from HBS listing)
- **Why it matters:** Sets the signal-loss and privacy context (cookie deprecation, first-party data) that explains why MMM is back; good opener before the technical sessions.
- **Use in course:** Session 1 case; paid (HBP).

### Cutting-Edge Marketing Analytics: Real World Cases and Data Sets (Darden casebook)
- **Source:** Rajkumar Venkatesan, Paul Farris and Ronald Wilcox, FT Press, 2014, book of cases with datasets; successor "Marketing Analytics: Essential Tools for Data-Driven Decisions", UVA Press, 2021
- **Link:** https://www.amazon.com/Cutting-Edge-Marketing-Analytics-Learning/dp/0133552527 and https://www.amazon.com/Marketing-Analytics-Essential-Data-Driven-Decisions/dp/0813945151 (confirmed in search results); individual cases sold via Darden Business Publishing
- **Why it matters:** Each chapter is a real company case with downloadable data (regression-based marketing-mix, resource allocation, experiments, CLV); the cases can be run in Python rather than the book's Excel/R.
- **Use in course:** Sessions 2 and 4 labs; book purchase or per-case licences.

### Advertising measurement at Facebook and eBay (research-based mini-cases, Kellogg and Berkeley)
- **Source:** Brett Gordon, Florian Zettelmeyer, Neha Bhargava and Dan Chapsky, Marketing Science 2019 (SSRN 2017); Thomas Blake, Chris Nosko and Steven Tadelis, Econometrica 2015; Gordon, Moakler and Zettelmeyer, Marketing Science 2023, articles usable as cases
- **Link:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3033144 , https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA12423 , https://ideas.repec.org/a/inm/ormksc/v42y2023i4p768-793.html ; free teaching slides https://www.ftc.gov/system/files/documents/public_events/945353/zettelmeyer_fb_fcc_11-3-2016_fz_slides_0.pdf (confirmed in search results)
- **Why it matters:** No formal Kellogg case on MMM was found, but these are the canonical "observational methods versus experiments" teaching materials: eBay paid-search returns were a fraction of non-experimental estimates; Facebook's 15 RCTs show how far attribution and matching stray from lift.
- **Use in course:** Session 5 (attribution versus incrementality) as a structured discussion; journal access via WU library, slides free.

### Resident and Robyn (Meta Marketing Science case)
- **Source:** Meta, 2021, published case study (free)
- **Link:** https://facebookexperimental.github.io/Robyn/docs/case-studies/ (confirmed in search results)
- **Why it matters:** E-commerce company (Nectar, DreamCloud) runs its in-house MMM alongside Robyn, uses DMA-level data and lift-test calibration, reports 20 per cent revenue growth; the same page lists Central Retail Group (Thailand) and Lemonade. A free case with a reproducible open-source tool.
- **Use in course:** Session 3 case plus Robyn demo data; free.

### Marketing Mix Modeling in Lemonade (arXiv paper as case)
- **Source:** Lemonade data science team, 2025, working paper arXiv 2501.01276
- **Link:** https://arxiv.org/abs/2501.01276 (confirmed in search results)
- **Why it matters:** Candid account of building a Bayesian MMM for an insurtech, combining it with Robyn and geo tests for calibration; reads like a teaching case with methods detail.
- **Use in course:** Session 3 reading; free.

### Advertising incrementality using controlled geo-experiments: the Universal App Campaign case (Uber)
- **Source:** Joel Barajas and colleagues (Uber), AdKDD 2020, conference paper
- **Link:** http://papers.adkdd.org/2020/papers/adkdd20-barajas-advertising.pdf (confirmed in search results)
- **Why it matters:** A full geo-experiment case: market pairing, Bayesian structural time series counterfactual, a 6.57 per cent conversion drop when Google UAC spend is paused; reusable as a lab on geo tests that feed MMM priors.
- **Use in course:** Session 3 or experiments session lab; free.

### Structural estimation of MMM parameters from geo-experiments (Zalando researcher)
- **Source:** Niklas Heusch (Zalando), 2026, working paper arXiv 2608.21128
- **Link:** https://arxiv.org/abs/2608.21128 and press summary https://ppc.land/mmm-overstates-paid-search-roas-by-2-5-times-zalando-researcher-finds/ (confirmed in search results)
- **Why it matters:** Shows a standard MMM reporting 10.61x ROAS for paid search whose experimental truth was 4.20x, and how geo-experiment time series recover the right parameters; a Berlin e-commerce example students will recognise.
- **Use in course:** Session 3 case; free.

### Free datasets usable as cases
- **Source:** various, 2020 to 2026, open data
- **Link:** PyMC-Marketing data folder https://github.com/pymc-labs/pymc-marketing/tree/main/data (fetched: mmm_example.csv, mmm_multidimensional_example.csv, mmm_roas_data.csv, credibility_* lift-test files, funnel_data.csv); Meridian simulated geo-level data https://github.com/google/meridian/tree/main/meridian/data (fetched: simulated_data directory) and Colab sample data; Robyn simulated weekly demo data in https://github.com/facebookexperimental/Robyn (fetched); GeoLift sample data https://github.com/facebookincubator/GeoLift (fetched, R); Google GeoexperimentsResearch https://github.com/google/GeoexperimentsResearch (fetched, archived R); Kaggle DT MART https://www.kaggle.com/datasets/datatattle/dt-mart-market-mix-modeling and bike-sales MMM demo https://www.kaggle.com/datasets/mattwalentosky/mmmdemodataset (confirmed in search results); synthetic benchmark with endogenous spend https://arxiv.org/pdf/2608.21130 (unverified content)
- **Why it matters:** The multidimensional PyMC-Marketing example and Meridian's simulated data are geo-level, so they support a cross-country or cross-region assignment; the credibility files let students calibrate against lift tests.
- **Use in course:** Sessions 2 to 4 labs and the group project; all free.

---

## 4. Practice examples (Praxisbeispiele)

### HelloFresh: Bayesian MMM across 15 markets (PyMC Labs)
- **Source:** PyMC Labs, 2022 to 2025, case study and blog posts
- **Link:** https://www.pymc-labs.com/case-studies/hellofresh and https://www.pymc-labs.com/blog-posts/reducing-customer-acquisition-costs-how-we-helped-optimizing-hellofreshs-marketing-budget (confirmed in search results)
- **Why it matters:** Berlin-based meal-kit company replaces black-box attribution with a Bayesian MMM over TV, social, podcasts and partners; reported 60 per cent lower prediction variance, 10x faster inference and about 30 per cent ROAS uplift across 15 markets, with a what-if budget simulator. The best multi-country Python example available.
- **Use in course:** Session 4 anchor example and guest-talk target; free.

### Heineken: MMM lighthouse markets Spain and Brazil (Meta)
- **Source:** Meta Business, 2021 to 2023, case study; AudienceProject cross-media case 2023
- **Link:** https://www.facebook.com/business/measurement/case-studies/heineken and https://audienceproject.com/cases/heineken-documents-reach-and-brand-outcomes-of-cross-media-campaign-to-identify-media-mix-optimisations/ (confirmed in search results)
- **Why it matters:** Global brewer uses two lighthouse markets to test measurement questions before rolling out; MMM showed Facebook ROI 2.3x the total media ROI in Spain and 3.5x the average in Brazil, now used as a "compass" for ongoing media decisions. Platform-sponsored, so discuss source bias.
- **Use in course:** Session 4 cross-country example; free.

### Zalando: experiments first, then MMM (engineering blog and research)
- **Source:** Zalando Engineering, 2019, blog; Niklas Heusch, 2026, arXiv paper
- **Link:** https://engineering.zalando.com/posts/2019/02/effectiveness-online-marketing.html and https://arxiv.org/abs/2608.21128 (confirmed in search results)
- **Why it matters:** Europe's largest fashion platform runs geo-based and audience-based randomised tests across 25 markets to measure incremental revenue, profit and acquisition, and its researchers now publish on reconciling MMM with those tests.
- **Use in course:** Session 3 and 5; free.

### Uber: Orbit, in-house Bayesian MMM and geo experiments
- **Source:** Uber Marketing Data Science (Edwin Ng, Zhishi Wang, Athena Dai), 2021, paper and open-source library; Barajas et al., AdKDD 2020
- **Link:** https://arxiv.org/pdf/2106.03322 , https://getrecast.com/uber-orbit/ , http://papers.adkdd.org/2020/papers/adkdd20-barajas-advertising.pdf (confirmed in search results)
- **Why it matters:** Time-varying-coefficient Bayesian MMM built from zero in-house, with lift tests ingested as priors; documents how a global platform company operationalises measurement.
- **Use in course:** Session 3 (time-varying effects) example; free.

### Bayer: unifying MMM and multi-touch attribution (TransUnion)
- **Source:** TransUnion, 2023, vendor case study
- **Link:** https://www.transunion.com/case-study/bayer-marketing-unification (confirmed in search results)
- **Why it matters:** Leverkusen-based pharma and consumer-health group had conflicting MMM and MTA numbers; case describes aligning the two into one measurement programme. Short but a real DACH-headquartered example of the "unified measurement" problem.
- **Use in course:** Session 5 discussion; free.

### Resident, Central Retail Group and Lemonade (Meta Robyn adopters)
- **Source:** Meta Marketing Science, 2021 to 2024, case studies
- **Link:** https://facebookexperimental.github.io/Robyn/docs/case-studies/ (confirmed in search results)
- **Why it matters:** Three documented open-source MMM deployments: a US DTC group (+20 per cent revenue), a Thai retail conglomerate (budget reallocation worth up to 28 per cent revenue) and an insurtech using geo tests for calibration. Shows what adoption looks like outside the big consultancies.
- **Use in course:** Session 3; free.

### Kellogg's: faster MMM turnaround (MASS Analytics)
- **Source:** MASS Analytics, 2022, vendor case study
- **Link:** https://mass-analytics.com/marketing-mix-modeling-use-case/marketing-mix-modeling-use-case-faster-marketing-mix-modeling-kelloggs/ (confirmed in search results)
- **Why it matters:** FMCG example that treats media and trade spend together and focuses on speed of model refresh, which is the practical bottleneck in most MMM programmes.
- **Use in course:** Session 5; free.

### Akulaku, Suntory Wellness and Finder: Meridian in APAC (Think with Google)
- **Source:** Google / Think with Google APAC, 2025, case articles
- **Link:** https://business.google.com/us/think/measurement/marketing-mix-modelling-growth-engine/ and https://business.google.com/en-all/think/measurement/google-meridian-marketing-mix-modelling/ (confirmed in search results)
- **Why it matters:** Early Meridian deployments in Indonesia, Japan and Australia; Akulaku's optimiser suggested 16 per cent more GMV at constant budget. Emerging-market angle, with the usual caveat that the platform publishes the results.
- **Use in course:** Session 4 international examples; free.

### Nielsen and TikTok MMM case study
- **Source:** Nielsen, 2022, case study (PDF)
- **Link:** https://www.nielsen.com/wp-content/uploads/sites/2/2022/03/Nielsen-TikTok-MMM-Case-Study.pdf (confirmed in search results)
- **Why it matters:** Shows how a new channel gets measured inside a commercial MMM and how platform data partnerships shape results.
- **Use in course:** Session 2 (channel data) example; free.

### Caritas Switzerland and Swiss Post: cross-media MMM for a fundraising campaign (Exactag)
- **Source:** Swiss Post Advertising / Exactag, 2023, case summary in German
- **Link:** https://www.directpoint.ch/de/kampagnenprozess/erfolgskontrolle/marketing-mix-modeling-welche-kanaele-wirken-wirklich (confirmed in search results)
- **Why it matters:** A DACH example: MMM on the "Welt ohne Armut" Christmas campaign attributed over half of donations to advertising, with direct mail most effective, then OOH and DOOH. Useful for students who read German and for the non-profit angle.
- **Use in course:** Session 2 or 4 short example; free.

### Measured: ten named brand MMM examples
- **Source:** Measured, 2025, vendor article
- **Link:** https://www.measured.com/faq/real-life-media-mix-modeling-mmm-examples-true-incrementality/ (confirmed in search results)
- **Why it matters:** Ten retail and DTC brands with one-paragraph outcomes from incrementality-calibrated MMM; a quick source of discussion vignettes. Search results also state that Unilever uses Measured for media measurement at scale (unverified detail).
- **Use in course:** Session 5 warm-up; free.

### Volkswagen: cross-media measurement across Germany, France and the UK (TikTok and Kantar)
- **Source:** TikTok for Business with Kantar, 2023, case study
- **Link:** https://ads.tiktok.com/business/en/inspiration/volkswagen-cross-media-case-study (confirmed in search results)
- **Why it matters:** Not an MMM, but a three-country cross-media study for the ID. range that shows how brand-lift and reach studies feed into mix decisions; no public VW MMM was found.
- **Use in course:** Session 4 side example; free.

### Anonymised vendor cases from Gain Theory and Ipsos MMA
- **Source:** Gain Theory (WPP), 2023, case study; Ipsos MMA, 2024, case study
- **Link:** https://gaintheory.com/case-study/optimizing-marketing-investments/ and https://mma.com/case-study-establishing-a-unified-marketing-mix-modeling-and-attribution-program/ (confirmed in search results)
- **Why it matters:** A multinational alcoholic-beverages company and a large financial-services firm; useful to show how consultancies present MMM programmes (governance, scenario planning), even if client names are withheld.
- **Use in course:** Session 5 background; free.

### Austrian and German market context
- **Source:** Trending Topics (Vienna), 2025, article; ad agents and directpoint articles, 2024 to 2025
- **Link:** https://www.trendingtopics.eu/marketing-trends-2025-ki-mix-modeling-und-neue-einkaufsassistenten/ and https://www.ad-agents.com/so-bringt-marketing-mix-modelling-mehr-effizienz-fuer-deine-werbespendings/ (confirmed in search results)
- **Why it matters:** German-language coverage of MMM adoption in DACH (one source cites about a quarter of companies using MMM regularly; unverified figure). No public, named MMM implementation from an Austrian brand (Red Bull, Swarovski, Spar, A1) was found.
- **Use in course:** Background; free.

---

## Gaps and caveats

- Verification: the session's network proxy blocked direct fetching of nearly all publisher domains (only github.com and one PDF mirror resolved), and the search budget ran out before every blog could be double-checked. All non-GitHub links were confirmed as appearing in search-engine results with matching titles, but page content, dates and prices should be re-checked before the syllabus is finalised.
- Paywalls: Gartner Magic Quadrant and Market Guide, Forrester Waves, the WFA handbook and EMEA vendor benchmark, and WARC's original of the Magic Numbers guide are paywalled or members only; free vendor reprints or mirrors are listed instead. HBP, Darden and Case Centre cases cost roughly USD 5 to 10 per student.
- Teaching cases: no formal Ivey, INSEAD, Kellogg, Stanford GSB or Case Centre case titled "Marketing Mix Modeling at ..." was found, and no HBS or Darden case on Unilever, P&G, Coca-Cola, Nestlé, Heineken or Mattel marketing mix modelling surfaced; the section therefore mixes the Darden notes and HBS budget-allocation case with free research-based and vendor-published cases. Direct catalogue searches on iveypublishing.ca, thecasecentre.org and hbsp.harvard.edu are recommended.
- McKinsey: no McKinsey MMM-specific piece could be located; BCG is included instead.
- Practice examples: Spotify, Booking.com, Douglas, Nestlé, Red Bull, Swarovski and Austrian brands have no public, named MMM write-ups that could be found; Unilever appears only as a Measured client mention; Volkswagen appears only in a cross-media study. Platform- and vendor-published cases (Meta, Google, TransUnion, MASS Analytics, Measured) carry obvious selection and sponsorship bias and should be taught as such.
- Dates: several "2026" items (IAB December 2025, Forrester Q1 2026, WFA handbook 2026, Heusch 2026, PyMC Labs 2026 posts) are very recent and may be revised; the Robyn demo dataset name and the Darden note "A Resource-Allocation Perspective for Marketing Analytics" product number were not verified.
