# Part 4: People, communities and datasets

Scope: (1) people to follow and realistic guest speakers, (2) communities, conferences and events, (3) public datasets for MMM teaching beyond the course's own Alpenglow data. Compiled 5 October 2026 for the winter term 2026/27 run (6 October to 3 November 2026). Links were checked by fetch where the network allowed it; links that could only be confirmed through a search result, or not at all, are flagged "(unverified)". See "Gaps and caveats" at the end.

---

## 1. People to follow and potential guest speakers

### 1a. Global thought leaders to follow (LinkedIn, X, blogs)

Ranked by how directly their public output maps onto the course (Bayesian MMM in Python, calibration with experiments, cross-market allocation).

### Juan Camilo Orduz
- **Source:** VP Marketing Analytics, PyMC Labs; Berlin; person (core author of PyMC-Marketing's MMM module)
- **Link:** https://www.pymc-labs.com/blog-posts/mmm_roas_lift (lift-test calibration post); personal blog https://juanitorduz.github.io/ (unverified: proxy blocked)
- **Why it matters:** Writes the most detailed public worked examples of Bayesian MMM, hierarchical geo models and lift-test calibration in Python; his notebooks are the closest public analogue to Session 3's lab.
- **Use in course:** Session 3 background reading; strong remote guest-talk candidate (Berlin, same time zone) on calibrating an MMM with experiments.

### Thomas Wiecki
- **Source:** CEO and co-founder, PyMC Labs; co-author of PyMC; Berlin area; person
- **Link:** https://cd.linkedin.com/posts/twiecki_pymc-marketing-activity-7049716496519811072-Ojbv (LinkedIn); PyData talk "Bayesian Marketing Science" referenced at https://www.pymc-labs.com/blog-posts/marketing-mix-modeling-a-complete-guide
- **Why it matters:** The public voice of Bayesian MMM; frequent posts on priors, identifiability and why Bayesian beats ridge for MMM; case studies with HelloFresh and Bolt.
- **Use in course:** Session 2-3 motivation; guest-talk candidate (vendor and open-source angle), realistic by video.

### Michael Kaminsky
- **Source:** Co-founder, Recast; USA; person
- **Link:** https://www.linkedin.com/posts/michael-the-data-guy-kaminsky_should-you-model-all-external-factors-in-activity-7163517252598775808-HtRO (LinkedIn); Recast blog https://getrecast.com/
- **Why it matters:** Sharpest practitioner writing on MMM validation: hold-out accuracy, long-term brand effects, "MER is a road to ruin", when not to add control variables. Good counterweight to vendor hype.
- **Use in course:** Session 2 diagnostics and Session 4 forecasting; short posts work as pre-reads.

### Gufeng Zhou
- **Source:** Marketing Science, Meta; creator of Robyn; London; person
- **Link:** https://uk.linkedin.com/in/gufeng-zhou-96401721 (LinkedIn, confirmed in search); Robyn repo https://github.com/facebookexperimental/Robyn
- **Why it matters:** Author of the most used open-source MMM in industry; his Medium and LinkedIn pieces on experiment calibration explain Robyn's design choices (ridge, Nevergrad, calibration).
- **Use in course:** Session 2 (Robyn as the R and ridge benchmark); vendor-side guest talk angle (Meta Marketing Science Europe).

### Igor Skokan
- **Source:** Marketing Science Director, open source, Meta; co-author of Robyn; person
- **Link:** https://github.com/facebookexperimental/Robyn (named in README); paper https://arxiv.org/pdf/2403.14674
- **Why it matters:** Co-author of "Packaging Up Media Mix Modeling" (with Runge, Zhou, Pauwels), the best short bridge between academic MMM and Robyn.
- **Use in course:** Background; Session 2 reading.

### Google Meridian team
- **Source:** Google Meridian Marketing Mix Modeling Team (the README cites the team, not individuals); person/team
- **Link:** https://github.com/google/meridian (verified); blog https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/
- **Why it matters:** Meridian is the reference implementation of geo-level hierarchical Bayesian MMM with reach and frequency, exactly the structure used in Session 3; their docs on geo selection are directly reusable.
- **Use in course:** Session 3 (geo hierarchy); follow via the GitHub repo and the Think with Google measurement pages. No single named person to follow; see JSM 2025 talk "Meridian: Google's Open-Source Marketing Mix Model" (https://ww2.amstat.org/meetings/jsm/2025/onlineprogram/abstract.cfm?sid=2361&tid=2363, unverified).

### Julian Runge
- **Source:** Assistant Professor, Northwestern University Medill; previously Meta marketing science; person
- **Link:** https://www.linkedin.com/posts/julian-runge_dear-digital-first-advertisers-are-you-media-activity-7100870821962764289-PASj (LinkedIn); MSI working paper https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_24-147.pdf
- **Why it matters:** Bridges academia and platform marketing science; co-author of the Robyn paper and of a 2026 Customer Needs and Solutions overview of open-source MMM (https://link.springer.com/article/10.1007/s40547-026-00161-4, unverified: proxy blocked).
- **Use in course:** Session 2 and 4 readings; remote guest-talk candidate on "media vs marketing mix modelling".

### Koen Pauwels
- **Source:** Distinguished Professor of Marketing, Northeastern University (DATA Initiative); Boston; person
- **Link:** https://www.researchgate.net/profile/Koen-Pauwels-3 ; personal site https://marketingandmetrics.com/
- **Why it matters:** Long-run marketing effectiveness, VAR models, dashboards; co-author of the Robyn paper and of the Yildirim and Kübler book; very active on LinkedIn and YouTube with plain-language explanations.
- **Use in course:** Session 2 and 3 background; "Marketing and Metrics" videos as optional viewing.

### Dominique Hanssens
- **Source:** Distinguished Research Professor of Marketing, UCLA Anderson; person
- **Link:** https://www.anderson.ucla.edu/faculty-and-research/marketing/faculty/hanssens
- **Why it matters:** The reference on market response models and long-term marketing effects (Hanssens, Parsons and Schultz); his MSI "Empirical Generalizations about Marketing Impact" is the best one-page summary of what elasticities to expect.
- **Use in course:** Session 1 and 2 classic reading; sanity-check priors in Session 3 against his elasticity generalisations.

### Harald van Heerde
- **Source:** Research Professor of Marketing, UNSW Sydney; Fellow, Tilburg University; person
- **Link:** https://www.unsw.edu.au/staff/harald-van-heerde
- **Why it matters:** Leading author on promotion response, decomposition of sales lifts, and marketing effectiveness across business cycles; essential for the baseline vs incremental logic.
- **Use in course:** Session 2 background (promotion decomposition), Session 1 elasticities.

### Marnik Dekimpe
- **Source:** Research Professor of Marketing, Tilburg University, and Professor, KU Leuven; person
- **Link:** https://www.researchgate.net/scientific-contributions/Marnik-G-Dekimpe-80951987
- **Why it matters:** Persistence modelling and long-run effects; cross-country work on private labels and retail in Europe fits the international angle.
- **Use in course:** Session 3 background (cross-country heterogeneity); realistic academic guest from the Benelux.

### Peter Danaher
- **Source:** Professor of Marketing and Econometrics, Monash University; Melbourne; person
- **Link:** https://research.monash.edu/en/persons/peter-danaher/
- **Why it matters:** Media exposure, reach and frequency modelling and multichannel attribution with field tests; directly relevant to Meridian's reach and frequency extension.
- **Use in course:** Session 4 attribution background.

### Jan-Benedict Steenkamp
- **Source:** C. Knox Massey Distinguished Professor of Marketing, UNC Kenan-Flagler; Editor in Chief, Journal of Marketing; person
- **Link:** https://www.kenan-flagler.unc.edu/faculty/directory/jan-benedict-steenkamp/ ; https://www.linkedin.com/in/jan-benedict-steenkamp-bb535ab/
- **Why it matters:** The international marketing reference (global brands, emerging markets, private label); frames why effects differ across the six Alpenglow markets.
- **Use in course:** Session 3 (cross-country) and Session 5 framing.

### Raoul Kübler
- **Source:** Professor of Marketing, ESSEC Business School; Cergy/Paris; German, previously Münster; person
- **Link:** https://faculty.essec.edu/en/cv/kubler-raoul/ ; https://www.raoulkuebler.de/ ; LinkedIn post on MMM manipulation https://www.linkedin.com/posts/raoul-k%C3%BCbler-a8365a49_demystifying-the-manipulation-of-marketing-activity-7156012239114682369-XpcC
- **Why it matters:** Co-author of "Applied Marketing Analytics Using R" (SAGE, with Yildirim), teaches MMM hands-on; posts on how MMM results get manipulated are perfect critical-thinking material.
- **Use in course:** Session 2 reading; realistic academic guest speaker (German speaker, European time zone, teaches exactly this material).

### Gokhan Yildirim
- **Source:** Associate Professor of Marketing, Imperial College Business School; London; person
- **Link:** https://www.researchgate.net/scientific-contributions/Gokhan-Yildirim-2006570428 ; book https://www.waterstones.com/book/applied-marketing-analytics-using-r/gokhan-yildirim/raoul-k-bler/9781529768725
- **Why it matters:** MMM and multichannel budget allocation research (direct mail vs email field tests, JAMS 2023); co-author of the applied R textbook.
- **Use in course:** Session 3 budget allocation background.

### Nicolas Padilla
- **Source:** Assistant Professor of Marketing, London Business School; person
- **Link:** https://www.london.edu/faculty-and-research/faculty-profiles/n/nicolas-padilla ; CV http://www.columbia.edu/~np2506/CV/PadillaCVweb.pdf
- **Why it matters:** Works explicitly on "modern marketing mix models" with first-party data and machine learning; one of few academics engaging with the Bayesian MMM revival.
- **Use in course:** Session 3 background; remote guest candidate (London).

### Bernd Skiera
- **Source:** Professor, Chair of Electronic Commerce, Goethe University Frankfurt; person
- **Link:** https://www.marketing.uni-frankfurt.de/de/professoren/skiera/prof-dr-bernd-skiera/publikationen.html
- **Why it matters:** Online advertising economics, attribution, and the GDPR tracking study (https://arxiv.org/pdf/2411.06862); the German-speaking reference on why attribution breaks and MMM returns.
- **Use in course:** Session 4 attribution; realistic guest (Frankfurt, two hours from Vienna by air).

### Christian Schulze
- **Source:** Associate Professor of Marketing, Frankfurt School of Finance and Management; person
- **Link:** https://scholar.google.com/citations?user=bt2edqYAAAAJ&hl=en
- **Why it matters:** Digital marketing and customer analytics with a strong quantitative bent; co-author with Skiera on marketing ROI and attribution.
- **Use in course:** Session 4 background; Frankfurt-based guest candidate.

### Martin Spann
- **Source:** Professor and Director, Institute of Electronic Commerce and Digital Markets, LMU Munich; person
- **Link:** https://ieeexplore.ieee.org/author/37086629306 (author page); LMU institute page (unverified: proxy blocked)
- **Why it matters:** Pricing, mobile and digital markets; useful for the price elasticity and digital channel parts.
- **Use in course:** Session 1 background; Munich guest candidate.

### Mike Taylor
- **Source:** Independent, co-founder of Ladder (marketing agency), author; London; person
- **Link:** https://getrecast.com/author/miketaylor/ ; https://www.linkedin.com/posts/mjt145_after-months-drowning-in-data-its-such-a-activity-6981023895956942848-S95I
- **Why it matters:** Practitioner tutorials comparing Robyn, LightweightMMM and PyMC-Marketing from a marketer's view; also writes on AI-assisted analysis, matching the course's AI-coding approach.
- **Use in course:** Session 2 optional reading.

### Eric Seufert
- **Source:** Heracles Media, author of Mobile Dev Memo; person
- **Link:** https://mobiledevmemo.com/ (unverified: proxy blocked); collaboration with Runge referenced via https://muckrack.com/julian-runge/articles
- **Why it matters:** Explains the privacy-driven revival of MMM (ATT, cookie loss) better than anyone; good for the "why now" argument.
- **Use in course:** Session 1 motivation.

### Jim Gianoglio
- **Source:** Founder, Cauzle Analytics and MMM Hub; USA; person
- **Link:** https://www.linkedin.com/in/jimgianoglio/ ; https://www.mmmhub.org (unverified: proxy blocked)
- **Why it matters:** Runs the MMM Hub newsletter, Slack and podcast; curates practically every new MMM resource. Marketing Analytics Summit talk "Cracking the Code: Mastering Modern MMM" https://www.youtube.com/watch?v=FEG-Vtj7Y9Q
- **Use in course:** Point students to MMM Hub in Session 1; the YouTube talk is a 40-minute overview for Session 2.

### Kevin Hartman
- **Source:** Director of Analytics, Google; author of "Digital Marketing Analytics: In Theory and in Practice"; person
- **Link:** https://www.goodreads.com/book/show/53490687-digital-marketing-analytics (book page); LinkedIn profile not confirmed (unverified)
- **Why it matters:** Accessible textbook framing of measurement choices; useful for students without a statistics background.
- **Use in course:** Background.

### Dominik Papies
- **Source:** Professor of Marketing, University of Tübingen; person
- **Link:** https://www.linkedin.com/in/dominik-papies-6aa204183/ ; https://scholar.google.com/citations?user=34_x4OcAAAAJ&hl=de
- **Why it matters:** Market response models and the standard reference chapter on endogeneity in marketing models; exactly the "why is media spend endogenous" problem in Session 2 and 3.
- **Use in course:** Session 2 reading on endogeneity; German guest candidate.

### Jochen Hartmann
- **Source:** Professor of Digital Marketing, TUM School of Management, Munich; person
- **Link:** https://www.mgt.tum.de/professors-1/info/prof-dr-jochen-hartmann
- **Why it matters:** Generative AI, multimodal ad analytics and unstructured data; complements MMM with creative-quality covariates.
- **Use in course:** Session 4 or 5 extension; Munich guest candidate.

### 1b. Realistic guest speakers reachable from Vienna

All are public professional pages (company, university, LinkedIn company or profile pages surfaced in search). Where a named person's current role could not be confirmed, the entry is company-level with the name flagged. Ranked by fit and practicality.

### Thomas Reutterer, WU Vienna
- **Source:** Professor of Marketing, Head of Institute for Marketing and Customer Analytics, WU Vienna; academic
- **Link:** https://www.wu.ac.at/en/mca/institute/meet-our-team ; https://www.reutterer.com/bio.html
- **Why them:** In-house WU colleague with a long record in marketing analytics and Bayesian methods; zero travel cost.
- **Speaker angle:** Academic: "What MMM can and cannot tell you about customers", or a joint Q&A in Session 5.

### Nils Wlömert and Nadia Abou Nabout, WU Vienna
- **Source:** Professors, Retailing and Data Science (Wlömert) and AI in Marketing Analytics (Abou Nabout), WU Department of Marketing; academic
- **Link:** https://www.wu.ac.at/en/marketing/about-us/department-struktur/ ; https://www.wu.ac.at/fileadmin/wu/d/i/imsm/Dokumente/Nadia_Abou_Nabout.pdf
- **Why them:** Abou Nabout works on online advertising auctions and attribution, Wlömert on retail data science; both are on campus.
- **Speaker angle:** Academic: attribution vs MMM (Session 4), retail scanner data (Session 1).

### Analytic Partners, Hamburg and Munich
- **Source:** Analytic Partners GmbH (Gartner MMM Magic Quadrant leader 2025); Hamburg office opened 2017 under Achim Schoeneich (Managing Director Germany, role as of 2017); vendor
- **Link:** https://analyticpartners.com/news-blog/2017/09/welcome-achim-schoeneich-lead-new-office-germany/ ; offices https://analyticpartners.com/contact-us/
- **Why them:** The largest commercial MMM shop with a German-speaking team; they run multi-country models for DACH brands.
- **Speaker angle:** Vendor: "Commercial analytics at scale: what a 20-country MMM programme looks like" (Session 3).

### Adtriba (now part of Funnel), Hamburg
- **Source:** János Moldvay, founder and CEO, Adtriba; acquired by Funnel in 2024; vendor
- **Link:** https://funnel.io/press-releases/marketing-intelligence-platform-funnel-acquires-measurement-firm-adtriba ; https://www.anyscale.com/blog/adtriba-accelerates-and-advances-media-mix-modeling-using-the-anyscale-fully
- **Why them:** German start-up that combined MMM, multi-touch attribution and incrementality for clients such as FlixBus; the Anyscale post describes their Bayesian MMM engineering.
- **Speaker angle:** Vendor and founder: "Unified measurement: MMM plus attribution plus experiments" (Session 4).

### Nexoya, Zurich
- **Source:** Nexoya AG, Zurich-based AI marketing budget optimisation platform active in CH, DE, AT, IT, UK; vendor
- **Link:** https://www.nexoya.com/press/ ; https://www.venturelab.swiss/nexoya-Meet-the-Venture-Leader-Technology-optimizing-marketing-decisions-with-predictive-AI
- **Why them:** Regression-based cross-channel attribution and automated budget reallocation for brands such as Zurich Insurance, Generali, Swisscom; a Swiss example of operationalised allocation.
- **Speaker angle:** Vendor: "From model to weekly budget decision" (Session 3 budget allocation).

### Mediaplus Austria (Serviceplan Group), Vienna
- **Source:** Mediaplus Austria GmbH and Co KG, Vienna media agency; group Data and AI unit in Munich; agency
- **Link:** https://at.linkedin.com/company/mediaplus-austria ; https://medianet.at/markets/mediaagenturen/mediaplus-austria-gmbh-co-kg-5516.html ; group page https://www.house-of-communication.com/int/en/brands/mediaplus/about-mediaplus.html
- **Why them:** Largest independent media agency in DACH with an in-house modelling offer; Vienna office means an in-person visit is realistic.
- **Speaker angle:** Agency: "How a media agency builds and sells an MMM to an Austrian client" (Session 2). Named modelling lead not public; ask via the Vienna office.

### dentsu Austria and Merkle, Vienna
- **Source:** dentsu Austria GmbH, Vienna; Merkle (dentsu) runs a Marketing Measurement and Optimisation practice and is a Google Meridian partner (partner status unverified); agency
- **Link:** https://medianet.at/markets/mediaagenturen/dentsu-austria-gmbh-5524.html
- **Why them:** Network agency with a Vienna office and a Meridian-based measurement practice in the group.
- **Speaker angle:** Agency: "Running Meridian for a client" (Session 3).

### GroupM Austria (WPP), Vienna
- **Source:** GroupM Austria, about 350 staff in Vienna; agency
- **Link:** https://www.linkedin.com/company/groupm-austria
- **Why them:** WPP's media investment arm; GroupM's global analytics units (Choreograph, [m]Science) run MMM for Austrian clients.
- **Speaker angle:** Agency: media planning meets MMM; a planner's view of response curves (Session 2).

### e-dialog, Vienna
- **Source:** e-dialog GmbH, Vienna performance marketing and analytics agency listing Marketing Mix Modelling among its services; agency (unverified: site blocked by proxy, mention from search summary only)
- **Link:** https://www.e-dialog.at/ (unverified)
- **Why them:** Small Vienna agency doing Google-stack analytics and MMM for mid-sized Austrian advertisers; practical scale for student projects.
- **Speaker angle:** Agency: "MMM for a mid-sized Austrian brand with limited data" (Session 2).

### Red Bull, Salzburg (Global Brand Marketing, marketing data science)
- **Source:** Red Bull GmbH, Fuschl am See; public job posting "Marketing Data Science Specialist" describing in-house MMM work in R and Python; brand
- **Link:** https://builtin.com/job/marketing-data-science-specialist/3710572 ; https://jobs.redbull.com/za-en/locations/red-bull-global-headquarters?lang=en
- **Why them:** Austria's most international brand runs MMM in-house across markets; a textbook case for Session 3's cross-country allocation.
- **Speaker angle:** Brand: "In-house MMM at a global Austrian brand". No named lead is public; approach via WU alumni or the Global Brand Marketing team.

### Sellforte (clients in DACH: bonprix, Hamburg)
- **Source:** Sellforte, Helsinki-based MMM SaaS for retail and ecommerce; bonprix case; vendor
- **Link:** https://sellforte.com/customer-news/bonprix ; https://sellforte.com/about
- **Why them:** European SaaS MMM with a published multi-country retail case (bonprix across Europe); contrasts with consultancy-style MMM.
- **Speaker angle:** Vendor: "Always-on MMM for a European retailer" (Session 3); remote.

### Ekimetrics (Paris, London; DACH projects)
- **Source:** Ekimetrics, Gartner MMM Magic Quadrant Visionary 2025, Forrester Wave leader Q1 2026; consultancy
- **Link:** https://www.ekimetrics.com/articles/ekimetrics-recognized-in-the-2025-gartner-magic-quadrant-for-marketing-mix-modeling
- **Why them:** Runs global measurement programmes with branding, local activation and structural variables; strong on the "holistic MMM" argument.
- **Speaker angle:** Consultancy: "Global MMM governance across countries" (Session 3); remote from Paris. No German office confirmed.

### Kantar (LIFT ROI), Munich and Vienna offices
- **Source:** Kantar, Gartner MMM Magic Quadrant Visionary 2025; LIFT ROI MMM product; research vendor
- **Link:** https://www.kantar.com/Campaigns/LIFT-ROI ; https://www.kantar.com/solutions/decision-intelligence/media
- **Why them:** Combines brand tracking with MMM; useful to show how brand equity enters a mix model.
- **Speaker angle:** Vendor: "Brand effects in MMM" (Session 2). Named DACH lead not public.

### Beiersdorf, Hamburg (Commercial Mix Modelling)
- **Source:** Beiersdorf AG; a public LinkedIn profile (Christian Jähnert, role unverified) describes media data analytics and "Commercial Mix Modeling (econometrics)" in-house; brand
- **Link:** https://www.linkedin.com/in/christian-jaehnert/ (unverified)
- **Why them:** FMCG brand owner (Nivea) with in-house econometrics across many countries; comparable category dynamics to Alpenglow.
- **Speaker angle:** Brand: "Owning the model in-house vs buying it" (Session 3).

### Henkel, Düsseldorf (Meridian adopter)
- **Source:** Henkel AG; search results indicate Henkel introduced Google Meridian for MMM (unverified; named profile Gabriel Marambaia, role unverified); brand
- **Link:** https://www.linkedin.com/in/gabrielmarambaia/ (unverified)
- **Why them:** A large DACH brand using the same open-source stack as the course.
- **Speaker angle:** Brand: "Moving from vendor MMM to open-source Meridian" (Session 3).

### Raoul Kübler, ESSEC (German academic abroad)
- **Source:** See 1a; German-speaking professor teaching MMM in R; academic
- **Link:** https://faculty.essec.edu/en/cv/kubler-raoul/
- **Why them:** Teaches the same material at master level and has written on MMM manipulation; fluent German.
- **Speaker angle:** Academic: "How MMM results get gamed and how to audit them" (Session 2 or 5).

### Dominik Papies, Tübingen
- **Source:** Professor of Marketing, University of Tübingen; academic
- **Link:** https://www.linkedin.com/in/dominik-papies-6aa204183/
- **Why them:** The German reference on endogeneity in market response models.
- **Speaker angle:** Academic: "Endogeneity in MMM: when your spend reacts to your sales" (Session 2 or 3).

### Bernd Skiera, Frankfurt
- **Source:** Professor, Goethe University Frankfurt; academic
- **Link:** https://www.marketing.uni-frankfurt.de/de/professoren/skiera/prof-dr-bernd-skiera/publikationen.html
- **Why them:** Attribution and privacy regulation research; close to Vienna.
- **Speaker angle:** Academic: "Attribution after GDPR and ATT: what is left and why MMM is back" (Session 4).

### Markus Christen, HEC Lausanne
- **Source:** Full Professor of Marketing, HEC Lausanne (ex INSEAD, ETH engineering background); academic
- **Link:** https://hecnet.unil.ch/hec/recherche/fiche?pnom=mchristen&dyn_lang=en ; https://www.unil.ch/news/en/1502973967830
- **Why them:** Marketing models and value-of-information research; Swiss academic voice on how much a model is worth to a decision maker.
- **Speaker angle:** Academic: "The value of information from an MMM" (Session 5 wrap-up).

### Jochen Hartmann, TUM Munich
- **Source:** Professor of Digital Marketing, TUM; academic
- **Link:** https://www.mgt.tum.de/professors-1/info/prof-dr-jochen-hartmann
- **Why them:** Generative AI and ad creative analytics; one flight from Vienna.
- **Speaker angle:** Academic: "Adding creative quality to the mix model with AI-extracted features" (Session 4 or 5 extension).

---

## 2. Communities, conferences and events

Ranked by usefulness to a Python-first MMM course. Course runs 6 October to 3 November 2026, so events in late 2026 and 2027 are the ones students can still attend.

### MMM Hub (newsletter, Slack community, podcast)
- **Source:** Jim Gianoglio (Cauzle Analytics), ongoing since 2023; website and community
- **Link:** https://www.mmmhub.org (unverified: proxy blocked; confirmed in search results and linked from the PyMC-Marketing README)
- **Why it matters:** The de facto practitioner hub: weekly newsletter, Slack workspace, curated resources and a podcast; PyMC-Marketing points its own users there.
- **Use in course:** Session 1 onboarding; students join the Slack and newsletter.

### PyMC Discourse, pymc-marketing category, and the Bayesian Discord
- **Source:** PyMC community, ongoing; forum
- **Link:** https://discourse.pymc.io/t/getting-started-with-pymc-marketing-questions-and-doubts/14447 ; https://discourse.pymc.io/t/hierarchical-mmm-channel-hierarchy-structure/17006 ; repo links https://github.com/pymc-labs/pymc-marketing
- **Why it matters:** Where PyMC-Marketing maintainers answer modelling questions (hierarchical channel structures, priors, sampling problems); the threads above are directly about Session 3 models.
- **Use in course:** Session 3 lab support channel; encourage students to search before asking.

### Robyn GitHub Discussions and Facebook group
- **Source:** Meta Marketing Science, ongoing; GitHub Discussions (Announcements, General, Ideas, Polls, Q&A, Show and tell)
- **Link:** https://github.com/facebookexperimental/Robyn/discussions (verified)
- **Why it matters:** Active Q&A on calibration, budget allocation and hyperparameters; the Facebook group linked from the README is where Meta's team interacts with users.
- **Use in course:** Session 2 (R benchmark) reference.

### Google Meridian GitHub and developer docs
- **Source:** Google, 2025 onward; repository and documentation
- **Link:** https://github.com/google/meridian (verified); docs https://developers.google.com/meridian/docs/pre-modeling/geo-selection-national-data
- **Why it matters:** Issues and docs are the practical community for geo-hierarchical MMM; the geo-selection guidance maps onto choosing markets in Session 3.
- **Use in course:** Session 3 reading.

### ISMS Marketing Science Conference
- **Source:** INFORMS Society for Marketing Science; annual academic conference
- **Link:** 2026: Nova SBE, Carcavelos, Portugal, 11 to 13 June 2026, https://www.informs.org/Meetings-Conferences/INFORMS-Conference-Calendar/2026-ISMS-Marketing-Science-Conference ; 2027: Seattle, 24 to 26 June 2027, https://www.informs.org/Meetings-Conferences/INFORMS-Conference-Calendar/2027-ISMS-Marketing-Science-Conference
- **Why it matters:** The main quantitative marketing conference; MMM, attribution and experiment sessions every year.
- **Use in course:** Background; for students considering a PhD or research-based thesis.

### EMAC Annual and Fall Conferences
- **Source:** European Marketing Academy; annual (spring) and regional (fall) conferences
- **Link:** EMAC 2026 Bath, 2 to 5 June 2026 https://www.emac2026conference.org/ ; EMAC Fall 2026 Bremen, 16 to 18 September 2026 https://www.uni-bremen.de/en/markstones/emac-fall-conference-2026 ; EMAC 2027 Rome (Luiss), 23 to 28 May 2027 https://emac2027.org/
- **Why it matters:** Europe's marketing academic community; the Rome 2027 meeting is the realistic one for WU students and the instructor.
- **Use in course:** Background; thesis supervision pipeline.

### PyData Amsterdam and PyCon DE and PyData
- **Source:** NumFOCUS PyData; annual conferences
- **Link:** PyData Amsterdam 10 to 11 September 2026 (tutorials 12 September), NDSM Loods, https://amsterdam.pydata.org/ ; PyCon DE and PyData 14 to 16 April 2026 (location per search result, unverified) https://pydata.org/past-events/
- **Why it matters:** PyMC Labs and PyMC-Marketing talks appear at PyData regularly (Wiecki's "Bayesian Marketing Science" was a PyData talk); the recordings are free on YouTube.
- **Use in course:** Session 3 video pre-read; next in-person editions are 2027.

### Meta Marketing Mix Modeling Summit
- **Source:** Meta Marketing Science, recurring practitioner summit (invitation-based); event
- **Link:** Recap by Recast https://getrecast.com/meta-mmm-summit/ (unverified: proxy blocked; confirmed in search); Ekimetrics recap https://ekimetrics.com/news-and-events/exploring-the-links-between-creative-execution-and-marketing-effectiveness-mmmsummit/
- **Why it matters:** Where Meta, vendors (Nielsen, Accenture, Ekimetrics) and brands compare MMM practice; recaps are a good snapshot of industry consensus.
- **Use in course:** Session 2 background; 2026 date not public.

### Marketing Analytics Summit
- **Source:** Marketing Analytics Summit (formerly eMetrics), annual practitioner conference, USA; event
- **Link:** https://marketinganalyticssummit.com/session/cracking-the-code-mastering-modern-marketing-mix-modeling/ ; speaker page https://marketinganalyticssummit.com/speaker/jim-gianoglio/
- **Why it matters:** Practitioner-level MMM talks with recordings on YouTube.
- **Use in course:** Session 2 video; 2027 dates unverified.

### Marketing Mix Modeling GitHub organisation
- **Source:** Community-curated GitHub organisation consolidating Meridian, Robyn, PyMC-Marketing, LightweightMMM, Unified-MMM and a Papers repo; website
- **Link:** https://github.com/marketing-mix-modeling (verified)
- **Why it matters:** One place to compare the open-source MMM stacks and find the papers list.
- **Use in course:** Session 2 reference.

### Measure Up and Funnel Reboot podcasts
- **Source:** Measure Up (podcast on marketing measurement) and Funnel Reboot episode 170 with Jim Gianoglio; audio
- **Link:** https://www.measureup.show/ (unverified: proxy blocked); https://funnelreboot.com/episode-170-marketing-mix-modelling-with-jim-gianoglio/
- **Why it matters:** Interview format makes trade-offs (cost, data needs, calibration) accessible for non-statisticians.
- **Use in course:** Optional listening, Session 1 or 2.

### Marketing Science Institute (MSI) working papers
- **Source:** MSI, ongoing; report series
- **Link:** https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_24-147.pdf ; https://thearf-org-unified-admin.s3.amazonaws.com/MSI/2026/MSI_Report_26-106.pdf
- **Why it matters:** Practitioner-facing academic papers on MMM (Runge and co-authors); free PDFs.
- **Use in course:** Session 2 and 4 readings.

---

## 3. Datasets for teaching

Ranked by fit to the course's Python stack and the multi-country theme. Sizes were measured locally where the file could be downloaded.

### Google Meridian simulated geo-level data
- **Source:** Google, 2025, dataset in the Meridian repo; Apache 2.0
- **Link:** https://raw.githubusercontent.com/google/meridian/refs/heads/main/meridian/data/simulated_data/csv/geo_all_channels.csv (verified by download); folder https://github.com/google/meridian/tree/main/meridian/data/simulated_data/csv
- **Why it matters:** 6,240 rows: 40 geos x 156 weeks (25 January 2021 to 15 January 2024), 5 paid channels with impressions and spend, 1 organic channel, 2 controls, promo flag, conversions, revenue per conversion and population (20 columns, about 1 MB). Sibling files add reach and frequency, national-level and a "hypothetical" future scenario for budget optimisation.
- **Use in course:** Session 3 lab alternative (hierarchical geo model and allocation); the geos can be relabelled as countries.

### PyMC-Marketing example data (mmm_example.csv)
- **Source:** PyMC Labs, 2023 onward, dataset in the pymc-marketing repo; Apache 2.0
- **Link:** https://raw.githubusercontent.com/pymc-labs/pymc-marketing/main/data/mmm_example.csv (verified by download); notebook https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html
- **Why it matters:** 179 weekly rows (2 April 2018 to 30 August 2021), 2 media channels, 2 event dummies, trend and seasonality helpers (8 columns, 12 KB). Tiny, so sampling is fast; matches the library's own tutorial.
- **Use in course:** Session 2 warm-up before the Alpenglow Germany data.

### Robyn demo data (dt_simulated_weekly)
- **Source:** Meta Marketing Science, 2021 onward, dataset shipped with Robyn (R and Python); MIT
- **Link:** https://raw.githubusercontent.com/facebookexperimental/Robyn/main/python/src/robyn/tutorials/resources/dt_simulated_weekly.csv (verified by download); documentation https://rdrr.io/cran/Robyn/man/dt_simulated_weekly.html (unverified: proxy blocked)
- **Why it matters:** 208 weekly rows (23 November 2015 to 11 November 2019), 12 columns: revenue, TV, OOH, print, Facebook (impressions and spend), search (clicks and spend), competitor sales, events, newsletter. The most widely used MMM demo, so students can compare their Python results with countless Robyn write-ups.
- **Use in course:** Session 2 lab or exercise (reproduce a Robyn-style decomposition in PyMC-Marketing).

### Synthetic benchmark with endogenous marketing spend
- **Source:** arXiv 2608.21130, 2026, paper plus seeded generator and reference instance with notebooks; licence stated in the repository (unverified)
- **Link:** https://arxiv.org/html/2608.21130 (unverified: proxy blocked; confirmed in search)
- **Why it matters:** Unlike Robyn and Meridian simulations, spend here reacts to seasons, promotions and past performance, so it tests whether a model survives endogeneity; ground truth is known.
- **Use in course:** Session 3 or 5 stretch exercise: fit the course model and check recovery of true ROAS.

### siMMMulator and PySiMMMulator (simulation packages)
- **Source:** Meta Marketing Science (R, MIT, author Jessica Nguyen) and PySiMMMulator (Python port, PyPI 0.6.2, 2024, Ryan Duecker); software
- **Link:** https://github.com/facebookexperimental/siMMMulator (verified); https://pypi.org/project/pysimmmulator/ (verified)
- **Why it matters:** Generate MMM data from first principles (baseline, spend, impressions, conversions) with user-chosen true ROI, so students can make their own ground-truth tests.
- **Use in course:** Session 5 project option: build a simulator for a seventh market.

### Meta GeoLift sample data
- **Source:** Meta, 2021 onward, datasets in the GeoLift R package (GeoLift_PreTest, GeoLift_Test, GeoLift_Test_MultiCell); MIT
- **Link:** https://github.com/facebookincubator/GeoLift/tree/main/data (verified)
- **Why it matters:** Daily sales by location for pre-test and test periods, built for synthetic-control geo experiments; the pre-test file is the standard power-analysis example.
- **Use in course:** Session 4 geo-lift lab (load the .rda files with pyreadr).

### Kaggle: Sample Media Spends Data
- **Source:** Kaggle user yugagrawal95, dataset; licence not visible from here (unverified)
- **Link:** https://www.kaggle.com/datasets/yugagrawal95/sample-media-spends-data (confirmed in search; page blocked by proxy)
- **Why it matters:** 3,051 rows, 9 columns, 113 weeks (January 2018 to February 2020), 8 digital channels (Facebook, Google search, email, YouTube, affiliate and more) plus sales; channel-week long format is good practice for reshaping.
- **Use in course:** Session 2 exercise; requires a Kaggle account.

### Kaggle: MMM demo dataset (bike sales)
- **Source:** Kaggle user mattwalentosky, dataset; licence not visible from here (unverified)
- **Link:** https://www.kaggle.com/datasets/mattwalentosky/mmmdemodataset (confirmed in search)
- **Why it matters:** Five years of fictitious weekly bike sales driven by Google Trends plus marketing spend; useful for showing how a search-interest covariate can absorb media effects.
- **Use in course:** Session 4 forecasting exercise.

### Dunnhumby: The Complete Journey and Breakfast at the Frat
- **Source:** dunnhumby Source Files, retail transaction and promotion datasets; free download under dunnhumby terms (non-commercial; permission needed to publish results, per search summary; unverified)
- **Link:** https://www.dunnhumby.com/source-files/ (confirmed in search; page blocked by proxy); Kaggle mirror https://www.kaggle.com/datasets/frtgnn/dunnhumby-the-complete-journey
- **Why it matters:** Complete Journey: 2,500 households over two years with transactions, coupons and campaigns. Breakfast at the Frat: 156 weeks of store-product sales with base price, shelf price and display/feature flags across four categories, the cleanest free data for price and promotion elasticities.
- **Use in course:** Session 1 elasticity lab (Breakfast at the Frat); Session 4 attribution background.

### Dominick's Finer Foods scanner data
- **Source:** Kilts Center, Chicago Booth, store-level weekly scanner data 1989 to 1997; free for academic use with registration. Eurostat's cleaned version and code: EUPL 1.2
- **Link:** https://www.chicagobooth.edu/research/kilts/research-data/dominicks (confirmed in search); cleaned files and R code https://github.com/eurostat/dff (verified)
- **Why it matters:** About 100 million observations, 18,000 UPCs, 29 categories, 90+ stores, almost 400 weeks; the classic for store-level price response and a reasonable stand-in for a "geo" panel.
- **Use in course:** Session 1 or 3 (treat stores as geos); subset one category before class.

### NielsenIQ via the Kilts Center (Consumer Panel, Retail Scanner, Ad Intel)
- **Source:** Kilts Center, Chicago Booth; academic subscription, US data only
- **Link:** https://www.chicagobooth.edu/research/kilts/research-data/nielseniq/pricing ; Ad Intel https://www.chicagobooth.edu/research/kilts/research-data/nielsen-ad-intel
- **Why it matters:** Weekly retail scanner data since 2006 from 90+ chains plus advertising occurrences by media type: the only large public-to-academics source that combines sales and advertising.
- **Use in course:** Background and thesis work only. Cost USD 3,000 for three years for one dataset (faculty subscription; up to two PhD students free); not usable for a 30-student class.

### Google Trends
- **Source:** Google, ongoing; web tool and unofficial Python access (pytrends)
- **Link:** https://trends.google.com/trends/ (unverified: proxy blocked; standard URL)
- **Why it matters:** Free weekly search-interest indices by country, the standard proxy for demand and for organic interest in all six Alpenglow markets; index values (0 to 100) are relative, not volumes.
- **Use in course:** Session 3 and 4 covariate; mind rate limits and the terms of service.

### Eurostat
- **Source:** European Commission, ongoing; database and API (Python package eurostat); CC BY 4.0
- **Link:** https://ec.europa.eu/eurostat/web/main/data/database (unverified: proxy blocked; standard URL)
- **Why it matters:** Monthly HICP, retail trade volume, consumer confidence and unemployment for AT, DE, FR, IT, NL, PL; the natural macro controls for a cross-country MMM and the source for PPP price-level adjustments.
- **Use in course:** Session 3 (controls and price-level normalisation).

### World Bank World Development Indicators
- **Source:** World Bank, ongoing; API (Python package wbgapi); CC BY 4.0
- **Link:** https://data.worldbank.org/ (unverified: proxy blocked; standard URL)
- **Why it matters:** Annual GDP per capita, PPP conversion factors, population and internet penetration for every country; needed when extending the model to emerging markets or scaling spend across currencies.
- **Use in course:** Session 3 and 5 (emerging-market extension in projects).

### LightweightMMM simulate_dummy_data (legacy)
- **Source:** Google, 2022 to 2025, archived January 2026; Apache 2.0
- **Link:** https://github.com/google/lightweight_mmm (verified; archived, Google recommends Meridian)
- **Why it matters:** A one-line simulator for national or geo MMM data with configurable channels and geos; still handy for quick demos even though the library is unmaintained.
- **Use in course:** Instructor-only for generating quiz data; do not teach the library.

---

## Gaps and caveats

- Network limits: the session's web search budget ran out and the egress proxy blocked most non-GitHub domains (Springer, arXiv, PyMC Labs, Kaggle, dunnhumby, LinkedIn, university sites, INFORMS, EMAC, PyData). Links from those domains were confirmed only through search results and are marked "(unverified)"; GitHub repositories, raw CSVs and PyPI were fetched directly.
- Named DACH practitioners: agencies and vendors do not publish their MMM leads. Analytic Partners' German managing director is cited from a 2017 announcement and may have changed; the Beiersdorf and Henkel LinkedIn profiles surfaced in search but their exact roles could not be read. Zalando, HelloFresh, Douglas, adidas, Puma, BMW, Mercedes, Swarovski, Spar, A1, Erste, Raiffeisen and Austrian Airlines returned no public MMM-specific person or page and were left out; the HelloFresh and Bolt case studies on the PyMC Labs blog are the best route to those brands.
- Accenture Song, Artefact, Publicis, Omnicom (Annalect), Ipsos and Nielsen have DACH offices but no public MMM contact or page specific to Austria or Germany was found.
- Conference dates: ISMS 2026, EMAC 2026 (spring and fall) and PyData Amsterdam 2026 are before the course starts; 2027 editions (EMAC Rome, ISMS Seattle) are the ones to point students to. Meta's MMM Summit, Marketing Analytics Summit and a PyData Vienna meetup could not be dated for 2026/27. No verifiable MMM LinkedIn group was found; MMM Hub's Slack fills that role.
- Datasets: Kaggle licences could not be read (typically CC0 or "other"); Dunnhumby's terms restrict publication; NielsenIQ is paid, US-only and faculty-gated; Google Trends is an index, not volume, and its API access is unofficial. The arXiv benchmark's repository URL and licence are in the paper, which could not be fetched. Sizes for Meridian, PyMC-Marketing and Robyn files were measured from the downloaded CSVs on 5 October 2026.
