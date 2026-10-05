# Positron and AI-assisted analytics: resource guide

Compiled on 5 October 2026 by parallel research agents for the course International Marketing Analytics (WU Vienna). Entries are ranked best first within each section. Links marked (unverified) or search-confirmed could not be fetched from the build environment and should be checked once before use.

Total entries: 124; new relative to the existing Notion list: 123.

---

# Positron and in-IDE AI assistants: software, docs, videos and real-world examples

Part 01 of the Positron resource search (brief: `RESEARCH_BRIEF_POSITRON.md`). Covers four categories: Software; Websites, documentation and blogs; Video tutorials and courses; Real-world examples. Searched 5 October 2026. Posit's own domains (positron.posit.co, posit.co, opensource.posit.co, assistant.posit.co) and YouTube could not be fetched directly from this environment; those links were confirmed through search results and through the GitHub source of the Positron website (posit-dev/positron-website) and are marked accordingly where detail is thin.

Landscape note (important for course rules): the AI story inside Positron changed in mid 2026. "Positron Assistant" (June 2025) and "Databot" (2025) were both superseded by **Posit Assistant**, which shipped as the default AI experience in Positron 2026.07 and also runs in RStudio 2026.04+ and as a terminal app. Anything published before April 2026 that says "Positron Assistant" describes the old tool; the concepts (session context, ask/edit/agent, bring your own key) carry over, but menus and provider set-up differ.

# Software

### Positron IDE (current release 2026.09.1-2, 4 September 2026)
- **Source:** Posit PBC, 2024-2026, software (desktop IDE; Elastic License 2.0, source-available, free for personal, academic and commercial use)
- **Link:** https://positron.posit.co/ and https://github.com/posit-dev/positron/releases
- **Why it matters:** Fork of VS Code (Code OSS) with first-class Python and R, Data Explorer, Variables pane, Plots pane, Connections pane, native Quarto and a Jupyter notebook editor (GA since 2026.07.0, 6 July 2026). Monthly date-stamped releases (there is no "1.0"; GA was declared with 2025.08.0 in August 2025). macOS, Windows and Linux. Only restriction: you may not host it as a service for third parties without Posit's consent; education hosting for your own students is explicitly allowed.
- **Use in course:** session 1 (install, tour, first Quarto document); free.

### Posit Assistant (in Positron 2026.07+, RStudio 2026.04+, terminal TUI)
- **Source:** Posit PBC, 2026, software (AI coding agent for data science; preview from Positron 2026.04.0, default since 2026.07; Posit AI Pass GA April 2026)
- **Link:** https://positron.posit.co/assistant.html and https://assistant.posit.co/docs/getting-started/
- **Why it matters:** The agent sees the live Python or R session (data frames, variables, plots, console history), runs code, has plan mode, skills, MCP servers, an `AGENTS.md` memory file and three permission modes. Bring your own key: providers listed on the getting-started page are Posit AI Pass, Anthropic, OpenAI, GitHub Copilot (preview), Amazon Bedrock, Microsoft Foundry, Snowflake Cortex, Databricks, DeepSeek, Google Gemini and Gemini Enterprise. Posit AI Pass Pro is USD 20/month (USD 5 first month) with USD 15 of model credits; it cannot draw on a personal Claude Pro or Max subscription.
- **Use in course:** sessions 1-5 (the default assistant for labs); students need either a Posit AI Pass, an Anthropic API key or a Copilot account.

### Positron Assistant (legacy, June 2025 to June 2026)
- **Source:** Posit PBC, 2025, software (deprecated from Positron 2026.07)
- **Link:** https://github.com/posit-dev/positron/discussions/7931
- **Why it matters:** The announcement thread (3 June 2025, Tom Mock) documents the original design: Anthropic Claude for chat via API key only (no Claude Pro OAuth, see discussion #10418), GitHub Copilot for completions, ask / edit / agent modes, and early user complaints about token cost. Useful for reading older blog posts and videos correctly.
- **Use in course:** background only (do not install; the replacement is built in).

### Databot (legacy exploratory data analysis agent)
- **Source:** Posit PBC (Joe Cheng), 2025, software (deprecated from Positron 2026.07, folded into Posit Assistant)
- **Link:** https://positron.posit.co/databot.html and https://posit.co/blog/introducing-databot
- **Why it matters:** Short-turn EDA loop (question, code, run, show output, suggest next question) that is the design ancestor of Posit Assistant's iterative data exploration; the "A brief and biased history" post below explains the lineage.
- **Use in course:** background (explains why Posit Assistant explores data step by step instead of writing whole scripts).

### GitHub Copilot in Positron
- **Source:** GitHub / Posit, 2025-2026, software (completions, Next Edit Suggestions and chat provider inside Posit Assistant; status "Preview")
- **Link:** https://positron.posit.co/assistant-completions.html and https://docs.posit.co/ide/user/ide/guide/tools/copilot.html
- **Why it matters:** Sign in via the Accounts menu; ghost-text completions in Python, R and Quarto, and Copilot can be selected as the chat model provider so students with a Copilot account avoid paying for API credits. Copilot Free gives 2,000 completions a month; the GitHub Student Developer Pack's free Copilot Student plan paused new sign-ups in April 2026 and reopened gradually from 17 June 2026 (check current status at https://education.github.com/pack).
- **Use in course:** session 1 set-up; the cheapest route for students who have a GitHub Education account.

### Claude Code in the Positron terminal
- **Source:** Anthropic, 2025-2026, software (terminal agent; requires Claude Pro/Max or API billing)
- **Link:** https://opensource.posit.co/blog/2026-06-08_comparing-posit-assistant-and-claude-code/ and https://github.com/posit-dev/positron/issues/13603
- **Why it matters:** Runs unchanged in Positron's integrated terminal, and the Claude Code VS Code extension also installs in Positron (Sharon Machlis, October 2025). Posit's own comparison (8 June 2026) is honest: Claude Code edits files and runs scripts but cannot see the live session unless you add the `btw` package's MCP server, whereas Posit Assistant has session access built in. Issue #13603 (May 2026, milestone 2026.10) proposes routing console "Fix / Explain" links to Claude Code for Claude subscribers.
- **Use in course:** sessions 3-5 for students who already have Claude Pro; good for the "agent writes the whole pipeline" versus "assistant explores with me" contrast.

### OpenAI Codex CLI
- **Source:** OpenAI, 2025-2026, software (open-source terminal agent, Apache 2.0, released 16 April 2025; IDE extension for VS Code forks)
- **Link:** https://github.com/openai/codex
- **Why it matters:** The OpenAI equivalent of Claude Code; sandboxed command execution with suggest / auto-edit / full-auto approval modes. Works in Positron's terminal like any CLI. Needs a ChatGPT Plus/Pro or API account.
- **Use in course:** background (mention as an alternative; do not support it in labs).

### Posit AI Pass
- **Source:** Posit PBC, 2026, software/subscription (invite-only beta January 2026, early release March 2026, GA April 2026; "Posit AI is Now Available to All", 5 May 2026)
- **Link:** https://posit.ai/ and https://docs.posit.co/posit-ai/user/faq/
- **Why it matters:** The one-login route to Posit Assistant and Next Edit Suggestions with a monthly credit allowance; the FAQ is the clearest statement of what leaves the machine (prompts, session info, variable names and types, schema via tool calls, row-level data only if you ask for it) and of zero-data-retention agreements with model providers.
- **Use in course:** session 1 and the course AI policy (privacy paragraph); USD 20/month, free trial without card.

### ellmer (R) and chatlas (Python)
- **Source:** Posit PBC (Hadley Wickham; Carson Sievert), 2024-2026, software (ellmer 0.5.0 on CRAN 4 September 2026; chatlas on PyPI)
- **Link:** https://ellmer.tidyverse.org/ and https://posit-dev.github.io/chatlas/
- **Why it matters:** Identical interfaces for calling LLMs from code (OpenAI, Anthropic, Gemini, Bedrock, Azure, Ollama and more), with tool calling and structured data extraction into typed objects. This is the "use an LLM inside your analysis" layer (for example classifying open-ended survey answers), distinct from the assistant that writes your code.
- **Use in course:** session 4 or 5 (optional lab: LLM-coded text data in a marketing dataset); API cost only.

### Visual Studio Code with the Python Data Science extension pack and Copilot
- **Source:** Microsoft, 2024-2026, software (free; Python, Jupyter, Data Wrangler, Copilot)
- **Link:** https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler
- **Why it matters:** The mainstream comparison point. Data Wrangler gives a Data-Explorer-like grid with Copilot-generated pandas code; Copilot Chat has an agent mode. What it lacks is Positron's language-aware console, Variables pane and R support. Positron's own migration guide (https://positron.posit.co/migrate-vscode.html) lists the differences.
- **Use in course:** background (why the course chose Positron); free.

### JupyterLab 4.6 with Jupyter AI 3.x
- **Source:** Project Jupyter, 2026, software (open source; Jupyter AI 3.0 released 31 March 2026)
- **Link:** https://jupyter-ai.readthedocs.io/ and https://github.com/jupyterlab/jupyter-ai
- **Why it matters:** Jupyter AI 3 stopped building its own agent and instead hosts Claude Code, Codex, Gemini and others via the Agent Client Protocol inside JupyterLab, with multi-user chats saved as files. Relevant if the school's JupyterHub is the only sanctioned platform; note Positron Server can also be launched from JupyterHub (see Real-world examples).
- **Use in course:** background; free.

### Cursor
- **Source:** Anysphere, 2023-2026, software (VS Code fork with built-in agent; Hobby free, Pro USD 20/month)
- **Link:** https://cursor.com/
- **Why it matters:** The most-used "AI-native" editor among software developers, but no data science panes and no R. The free one-year student Pro offer closed to new sign-ups on 25 June 2026; students now get the Hobby tier only.
- **Use in course:** background (useful for the "vibe coding" discussion: a tool built for shipping code, not for understanding data).

### RStudio 2026.04+ with Posit Assistant, ellmer and chattr
- **Source:** Posit PBC, 2026, software (open source IDE; Posit Assistant private beta January 2026, public 5 March 2026)
- **Link:** https://docs.posit.co/ide/user/ide/guide/tools/posit-ai.html and https://posit.co/blog/introducing-ai-in-rstudio
- **Why it matters:** The same assistant now lives in RStudio, so R-side colleagues are not left behind; chattr (Shiny gadget for prompting from RStudio) and ellmer remain the package-level routes. Confirms that Positron is not a forced migration for R users.
- **Use in course:** background; free.

### Google Colab with Gemini Data Science Agent
- **Source:** Google, 2025-2026, software (free tier for users 18+ in supported countries; Pro from USD 9.99/month)
- **Link:** https://colab.research.google.com/
- **Why it matters:** Describe an analysis in the Gemini side panel and it generates a complete notebook (launched March 2025). Zero install, which is tempting for a first-session fallback, but no local files, no Quarto, no Git integration and session time-outs on the free tier.
- **Use in course:** background / emergency fallback only.

### Deepnote
- **Source:** Deepnote, 2020-2026, software (cloud notebook; free Education plan for verified students and teachers)
- **Link:** https://deepnote.com/docs/edu-verification
- **Why it matters:** Collaborative notebook with SQL, Python and R blocks and a Deepnote Agent that is aware of the workspace; the free Education plan excludes Deepnote AI, so the AI angle costs money. Good illustration of the "AI in a hosted notebook" model versus Positron's local IDE.
- **Use in course:** background.

### Posit Cloud with Positron (preview)
- **Source:** Posit PBC, 2026, software (hosted; Free plan 25 project hours/month, Student plan USD 5/month with 75 hours)
- **Link:** https://posit.co/blog/positron-now-available-posit-cloud-preview and https://posit.cloud/plans/student
- **Why it matters:** Browser-based Positron so nobody loses the first session to laptop troubleshooting; every plan including Free can open Positron. Posit Cloud does not bundle AI, but a student with their own Posit AI Pass can sign in inside the session (relevant for exam rules, see the forum thread under Real-world examples).
- **Use in course:** session 1 fallback for students with locked-down laptops.

### Positron Server on JupyterHub and Positron Pro on Posit Workbench (institutional)
- **Source:** Posit PBC, 2026, software (free 12-month education licence for qualifying institutions; `jupyter-positron-server` on PyPI)
- **Link:** https://positron.posit.co/education.html and https://pypi.org/project/jupyter-positron-server/
- **Why it matters:** If WU already runs JupyterHub, Positron can be added as a launcher next to JupyterLab with a free education licence (request via academic-licenses@posit.co); Workbench 2026.04.0 adds Posit Assistant with institution-controlled BYOK providers. This is the route to a uniform, admin-controlled AI set-up for 30 students.
- **Use in course:** background / infrastructure decision before session 1.

### Student pricing summary (as of October 2026)
- **Source:** compiled from vendor pages, 2026, software/pricing
- **Link:** https://education.github.com/pack ; https://www.anthropic.com/education ; https://posit.ai/ ; https://posit.cloud/plans/student
- **Why it matters:** Cheapest working combination for a student: Positron (free) + GitHub Education (Copilot Student plan when open, otherwise Copilot Free) as the Posit Assistant provider. Alternatives: Posit AI Pass USD 20/month (USD 5 first month); Anthropic API pay-as-you-go (an Anthropic console key; Claude Pro does not work in Posit Assistant but does power Claude Code in the terminal); Claude for Education is institution-level only, with no individual student discount.
- **Use in course:** session 1 and the syllabus "tools and costs" paragraph. Verify GitHub Copilot Student availability the week before term; it has been paused and reopened once already in 2026.

# Websites, documentation and blogs

### Positron documentation: Python in Positron, Data Explorer, Connections, Quarto
- **Source:** Posit PBC, 2024-2026, website (official docs, source on GitHub at posit-dev/positron-website)
- **Link:** https://positron.posit.co/guide-python.html ; https://positron.posit.co/data-explorer.html ; https://positron.posit.co/connections-pane.html ; https://positron.posit.co/jupyter-notebooks.html
- **Why it matters:** Concise, screenshot-led pages; the Python guide covers venv, uv, conda and interpreter selection, which is where beginners get stuck. The Data Explorer page is the best two-minute explanation of filter, sort and summary statistics without code.
- **Use in course:** session 1 pre-reading; sessions 2-3 (Data Explorer as a no-code first look at the data).

### Posit Assistant documentation (positron.posit.co and assistant.posit.co)
- **Source:** Posit PBC, 2026, website
- **Link:** https://positron.posit.co/assistant.html ; https://positron.posit.co/assistant-getting-started.html ; https://assistant.posit.co/docs/getting-started/providers/
- **Why it matters:** Defines the modes, permission levels, `/plan` and `/savememory` commands, skills and the `AGENTS.md` memory file; the providers page is the authoritative list of what students can sign in with. The permission-mode section is directly usable as course rules ("approve every code change in lab 1 and 2").
- **Use in course:** session 1 (set-up); the AI policy appendix.

### Tutorial: "Collaborate with AI on a Python analysis"
- **Source:** Posit PBC, 2026, website (step-by-step tutorial in the Positron docs)
- **Link:** https://positron.posit.co/tutorial-ai-notebooks.html
- **Why it matters:** The closest thing to a ready-made lab for this course: clone a repo, inspect `retail_sales.xlsx` (about 9,800 orders) in the Data Explorer, set up a venv, ask Posit Assistant for quarterly sales aggregation and a chart, export the chat to a notebook, use one-click error fixes and ghost cells, convert to Quarto and publish a dashboard.
- **Use in course:** session 2 lab (swap in a marketing dataset); free.

### "Your first Python project in Positron" (Sara Altman)
- **Source:** Posit blog, March 2026, article with companion video
- **Link:** https://posit.co/blog/first-python-project-in-positron
- **Why it matters:** Folder, virtual environment, Git init, install pandas and matplotlib, Quarto document, commit, push, deploy. Written by a former Stanford data science instructor for beginners; matches the course's Positron + Quarto + GitHub stack exactly.
- **Use in course:** session 1 homework (follow along before class).

### "A brief and biased history of Posit data science agents"
- **Source:** Posit Open Source blog, 11 June 2026, article
- **Link:** https://opensource.posit.co/blog/2026-06-11_history-of-posit-data-science-agents/
- **Why it matters:** Explains why Positron Assistant, Databot and Posit Assistant exist, which ideas survived (short turns, human approval, session context) and why the first two were retired. Essential for reading anything older than April 2026.
- **Use in course:** background for the instructor; optional reading in session 1.

### "Posit Assistant is specialized for data work" (Posit Assistant versus Claude Code)
- **Source:** Posit Open Source blog (Sara Altman, Simon Couch), 8 June 2026, article (companion to the 13 April 2026 video)
- **Link:** https://opensource.posit.co/blog/2026-06-08_comparing-posit-assistant-and-claude-code/
- **Why it matters:** Three concrete differences: built-in session access, iterative exploration with summaries, and plot handling; fair about where Claude Code is stronger (multi-file projects, package development). Good basis for a class discussion on "assistant that explores with me" versus "agent that ships code".
- **Use in course:** session 3 reading.

### "Positron Assistant: GitHub Copilot and Claude-Powered Agentic Coding in R" (Stephen Turner)
- **Source:** Stephen D. Turner, Paired Ends (Substack), September 2025, article (reposted on R-bloggers)
- **Link:** https://blog.stephenturner.us/p/positron-assistant-copilot-chat-agent
- **Why it matters:** An independent bioinformatician's hands-on test of agent mode with Copilot and Claude, including what it got wrong. R examples, but the workflow and cautions transfer. Describes the legacy assistant; read with the history post.
- **Use in course:** background.

### "Posit Assistant: Is it worth the switch?" (Jumping Rivers)
- **Source:** Jumping Rivers (UK training company), August 2026, article (also on R-bloggers)
- **Link:** https://www.jumpingrivers.com/blog/posit-assistant-is-it-worth-the-switch/
- **Why it matters:** Independent review of the new assistant: it answers by writing and running code, which makes its reasoning auditable; the authors compare it with running the Claude Code extension in Positron and note that session context arrives with zero configuration. Grew out of their "Improving Your Workflow with Positron and Claude" workshop at AI in Production 2026.
- **Use in course:** session 3 reading (short, practitioner view).

### "RStudio vs VS Code vs Positron: Best R IDE" and "Positron vs RStudio: Should You Switch?"
- **Source:** r-statistics.co, March 2026, articles
- **Link:** https://r-statistics.co/RStudio-vs-VSCode-vs-Positron.html and https://r-statistics.co/Positron-vs-RStudio.html
- **Why it matters:** Plain-language comparison with a one-line verdict (R only: RStudio; Python only: VS Code or Jupyter; both: Positron) and performance notes (large files, Data Explorer with 100k+ rows). Also https://www.datanovia.com/learn/programming/setup/choosing-an-ide for a four-way comparison that includes Jupyter.
- **Use in course:** background; the verdict line is quotable in session 1.

### Positron migration guides (from RStudio, from VS Code)
- **Source:** Posit PBC, 2025-2026, website and blog
- **Link:** https://posit.co/blog/positron-migration-guides ; https://positron.posit.co/migrate-vscode.html ; https://positron.posit.co/migrate-rstudio.html
- **Why it matters:** Side-by-side tables of what is the same, what moved and what is missing; in-product walkthroughs exist too. Students who already know VS Code from a bachelor course can read the VS Code page in ten minutes.
- **Use in course:** session 1 (optional, for students with prior IDE experience).

### "Privacy and AI Assistants" and the Posit AI FAQ
- **Source:** Posit blog (2025) and docs.posit.co (2026), article and website
- **Link:** https://posit.co/blog/trust-llm-tools and https://docs.posit.co/posit-ai/user/faq/
- **Why it matters:** States plainly that the assistant can execute arbitrary code and read files, that Posit does not store queries, and that the trust relationship is with the model provider. The FAQ lists exactly what context is sent (variable names and types, schemas, and row-level values only if prompted). The GitHub discussion "Handling Sensitive Data with Positron Assistant" (#9508) adds user questions.
- **Use in course:** course AI policy (data handling rule for any client or survey data).

### "Responsible by Design: Building AI That Works With You"
- **Source:** Posit blog (Nick Rohrbaugh), August 2025, article
- **Link:** https://posit.co/blog/positron-ai-product-announcement-aug-2025
- **Why it matters:** Posit's design principles for AI in the IDE: correct, transparent, reproducible; a human expert who can read the code must stay in the loop. A one-page statement that doubles as a course value statement on AI-assisted analysis.
- **Use in course:** session 1 reading (frames the course rules on AI use).

### Whitepaper "A guide to Positron: the data science code editor"
- **Source:** Posit PBC, 2025, report (PDF, free with form; mirror PDF on bookdown.org)
- **Link:** https://posit.co/whitepaper/a-guide-to-positron-the-data-science-code-editor (mirror: https://bookdown.org/jtkulas/12_23_25/Positron-Whitepaper-2025.pdf)
- **Why it matters:** The single most complete written overview: four-pane workflow, polyglot sessions, Data Explorer, Connections, Quarto, AI, Workbench. Marketing tone but accurate.
- **Use in course:** background reading for the instructor and for the syllabus tool section.

### Positron for Education (institutional options)
- **Source:** Posit PBC, 2026, website
- **Link:** https://positron.posit.co/education.html
- **Why it matters:** Lays out the three ways to run Positron for a class (desktop, Positron Server on JupyterHub, Positron Pro on Workbench), the free 12-month education licence, eligibility rider and the e-mail to request a key.
- **Use in course:** background (infrastructure decision with WU IT).

### "10 tips for getting better R code from your AI coding agent" (Sharon Machlis)
- **Source:** InfoWorld, 17 June 2026, article
- **Link:** https://www.infoworld.com/article/4184642/10-tips-for-getting-better-r-code-from-your-ai-coding-agent.html
- **Why it matters:** Covers Claude Code, Codex and Posit Assistant alike: knowledge files (`CLAUDE.md`, `AGENTS.md`), skills, plan mode before coding, having the agent write tests, and budget management with local models. R-flavoured but every tip applies to Python in Positron.
- **Use in course:** session 3 or 4 reading (turns "prompting" into a reproducible workflow with memory files, which is also a good artefact to assess).

### "Posit's AI Packages Explained: A Decision Map for R and Python Developers" (Appsilon)
- **Source:** Appsilon (Vedha Viyash), 9 April 2026, article
- **Link:** https://www.appsilon.com/post/posits-ai-packages-explained-a-decision-map-for-r-and-python-developers
- **Why it matters:** Sorts ellmer, chatlas, querychat, shinychat, ragnar, vitals, mcptools and the assistants into "which do I need for what". Saves a confused hour.
- **Use in course:** background; session 5 if the LLM-in-analysis lab is run.

### Community reviews: Kasey Zapatka (2025), Andrew Heiss (2024), Peter Hahn (Medium), Erik Gahner (2024), Posit Community thread "Moving from Python development to Positron"
- **Source:** independent academics and practitioners, 2024-2026, blog posts and forum thread
- **Link:** https://www.kaseyzapatka.com/blog/2025/positron/ ; https://www.andrewheiss.com/blog/2024/07/08/fun-with-positron/ ; https://kphahn57.medium.com/from-rstudio-to-positron-707d3f6d2776 ; https://erikgahner.dk/2024/notes-on-positron/ ; https://forum.posit.co/t/moving-from-python-development-to-positron/210963
- **Why it matters:** Honest first-person accounts from social scientists and analysts; Zapatka on mixed R/Python academic work with multiple consoles, Heiss on what RStudio users gain, Gahner the sceptic (2024: "if you already use VS Code you gain little"). Pre-2026 posts predate the notebook editor and Posit Assistant.
- **Use in course:** background; one or two make good discussion prompts on tool choice.

### "Customize Positron with these community-curated resources"
- **Source:** Posit Open Source blog, 28 April 2026, article
- **Link:** https://opensource.posit.co/blog/2026-04-28_positron-community-resources/
- **Why it matters:** Curated list of settings, keybindings, themes and workflow posts (including Andrew Heiss's "Switching to Positron full-time" thread); a shortcut to a sane default configuration for a classroom.
- **Use in course:** session 1 (distribute a recommended `settings.json`).

# Video tutorials and courses

### "A quick tour of Positron" (Sara Altman)
- **Source:** Posit, 28 July 2025, video (6 min)
- **Link:** https://www.youtube.com/watch?v=4Ir_HX4riHw (blog: https://posit.co/blog/a-quick-tour-of-positron)
- **Why it matters:** The six-minute orientation: editor, console, Variables, Data Explorer, Plots, Help, R and Python side by side. Short enough to play in class.
- **Use in course:** session 1 (play in class or assign before).

### "Getting Started with Positron: A Quick Tour"
- **Source:** Posit, 24 September 2025, video
- **Link:** https://www.youtube.com/watch?v=mru9z50IOhI
- **Why it matters:** Set-up and layout walkthrough aimed at first-time users; complements the six-minute tour with interpreter selection and settings.
- **Use in course:** session 1 pre-work. Length not confirmed (unverified).

### "Your First Python Project in Positron" (Sara Altman)
- **Source:** Posit, March 2026, video
- **Link:** https://www.youtube.com/watch?v=Dw04bDgUTmg
- **Why it matters:** Video version of the blog post above: folder, venv, Git, pandas, matplotlib, Quarto, commit, deploy. The whole course stack in one sitting.
- **Use in course:** session 1 homework. Length not confirmed (unverified).

### "Introducing Posit AI for Positron and RStudio" (Tom Mock)
- **Source:** Posit live demo, 29 April 2026, video (29 min)
- **Link:** https://posit.co/workflow-demo/introducing-posit-ai-positron-and-rstudio (also https://opensource.posit.co/resources/videos/2026-04-29_introducing-posit-ai-for-positron-and-rstudio/)
- **Why it matters:** The official first demo of Posit Assistant with live session context: debugging, reshaping data, explaining code, in both IDEs. Current product, current UI.
- **Use in course:** session 2 (watch 10 minutes in class before the first AI lab).

### "Comparing Posit Assistant and Claude Code" (Sara Altman, Simon Couch)
- **Source:** Posit, 13 April 2026, video (21 min)
- **Link:** https://www.youtube.com/watch?v=7GI6-4J0AXA
- **Why it matters:** Same task done with both tools; shows the `btw::btw_mcp_session()` workaround for Claude Code and the assistant's iterative exploration style. Pairs with the June blog post.
- **Use in course:** session 3.

### "Comparing Posit Assistant and Positron Assistant"
- **Source:** Posit, 21 May 2026, video (23 min)
- **Link:** https://www.youtube.com/watch?v=Y9P2nlFXKnQ
- **Why it matters:** Explains tool coverage, built-in skills, OS-level sandboxing and cache efficiency of the new assistant; the clearest explanation of why the old one was retired.
- **Use in course:** background for the instructor.

### "Building Posit Assistant: An AI Agent for Data Science and Analysis" (The Test Set)
- **Source:** Posit (Michael Chow with Simon Couch, George Stagg, Sara Altman, Winston Chang), 24 April 2026, video (8 min)
- **Link:** https://www.youtube.com/watch?v=A2samrgWZyo
- **Why it matters:** Engineers on thinking effort, the terminal UI, predictive modelling and image data extraction; a short peek under the bonnet that demystifies "the agent" for non-programmers.
- **Use in course:** session 2 or 3 (8 minutes, in class).

### "Data analysis with Posit AI-assistants" (Data Science Lab)
- **Source:** Posit Data Science Lab (Libby Heeren with Sara Altman and Simon Couch), 12 March 2026, video (54 min)
- **Link:** https://opensource.posit.co/resources/videos/2026-03-12_data-analysis-with-posit-ai-assistants-sara-altman-simon-couch-data-science-lab/
- **Why it matters:** Long-form live analysis with the assistants plus a demo of the `reviewer` package (AI code review); shows what a realistic hour of AI-assisted EDA looks like, including dead ends.
- **Use in course:** background; clip 10-15 minutes for session 3.

### "Positron: The First Five Minutes" (Isabella Velásquez, posit::conf 2025)
- **Source:** Posit, posit::conf(2025), published 7 November 2025, video (44 min)
- **Link:** https://www.youtube.com/watch?v=MOpJYbhLgyc
- **Why it matters:** What to do in the first five minutes of opening a project in Positron, by a developer-relations lead; good for the "set-up anxiety" of beginners. The full posit::conf(2025) playlist is https://www.youtube.com/playlist?list=PL9HYL-VRX0oTixlfDPCS5RW_F1pccERRe (Stephen Turner's curated index: https://blog.stephenturner.us/p/posit-conf-2025-youtube-playlist).
- **Use in course:** session 1 optional.

### "Introducing Positron, a new data science IDE" (posit::conf 2024)
- **Source:** Posit (Julia Silge, Isabel Zimmerman, Tom Mock, Jonathan McPherson, Lionel Henry, Davis Vaughan, Jenny Bryan), posit::conf(2024), video
- **Link:** https://www.youtube.com/watch?v=8uRcB34Hhsw (Jenny Bryan's slides: https://speakerdeck.com/jennybc/positron-for-r-and-rstudio-users)
- **Why it matters:** The design rationale from the team that built it: why a VS Code fork, why a dedicated console and Data Explorer, what should feel familiar from RStudio. Dated UI, timeless reasoning.
- **Use in course:** background. Length not confirmed (unverified).

### "A First Look at Positron and Posit Assistant" (Jumping Rivers webinar, Kia Mack)
- **Source:** Jumping Rivers, 13 August 2026, video (recorded webinar)
- **Link:** https://www.youtube.com/watch?v=7tBlsBjpEBI (blog: https://www.jumpingrivers.com/blog/first-look-positron-posit-assistant/)
- **Why it matters:** Independent, European (Newcastle) trainer demonstrating Positron versus RStudio, R and Python side by side and Posit Assistant on everyday tasks, live rather than scripted.
- **Use in course:** session 2 optional viewing. Length not confirmed (unverified).

### "AI-Powered Data Science in Positron" (Ryan Johnson)
- **Source:** Posit, 2025-2026, video
- **Link:** https://www.youtube.com/watch?v=Ve7cNChzq5Q
- **Why it matters:** Marketing-level overview of Positron as an "AI-ready" IDE with Posit Assistant and Next Edit Suggestions; useful as a two-minute motivator, not as a tutorial.
- **Use in course:** background. Date and length not confirmed (unverified).

### Posit Academy: "Introduction to Positron" path and "Positron AI Workshop"
- **Source:** Posit Academy, 2025-2026, online courses (Navigating the Positron Interface 28 min; Working with Data in Positron 25 min; Running and Managing Code in Positron 24 min; Positron AI Workshop 20 min; on-demand, free account)
- **Link:** https://academy.posit.co/path/introduction-to-positron and https://academy.posit.co/page/all-courses (workshop materials: https://github.com/posit-dev/positron-ai-workshop)
- **Why it matters:** Short self-paced modules with a hosted Positron on Workbench, so students can practise before installing. The AI workshop repo has R and Python scripts, notebooks and Quarto files on a happiness dataset plus a pharma example; it still names Positron Assistant and Databot, so expect UI differences.
- **Use in course:** session 1 homework (first two modules, under an hour).

### "Modern R Workflow (ft. Positron and AI)" (Hadley Wickham, Jenny Bryan; posit::conf 2026 workshop)
- **Source:** Posit, September 2026, one-day workshop materials (CC-BY 4.0; recordings expected on YouTube per Posit's practice)
- **Link:** https://github.com/posit-conf-2026/modern-r-workflow (site: https://posit-conf-2026.github.io/modern-r-workflow/)
- **Why it matters:** The two most influential R educators teaching functions, testing and Claude Code and Positron Assistant skills together; the repo includes ready-made assistant skill files. R, but the "how to work with an agent responsibly" material is language-neutral.
- **Use in course:** background for the instructor; skill files as templates for a course `AGENTS.md`.

### "Human-in-the-Loop AI: Using Posit Assistant in Positron" (Garrett Grolemund, R/Pharma 2026)
- **Source:** Posit (Garrett Grolemund, Director of Learning), 28 September 2026, 3-hour workshop materials
- **Link:** https://github.com/posit-dev/human-in-the-loop-ai-r-pharma-2026
- **Why it matters:** Workshop built around approving every line the model proposes, keeping data local and setting methodology yourself; slides (PDF), specs and a house style guide are in the repo. The structure is a template for a regulated-industry-grade AI lab.
- **Use in course:** sessions 2-4 (adapt the approval-at-every-step exercise to a marketing dataset).

### Julia Silge on Positron (The Test Set podcast; SuperDataScience 817; "A first look at Positron")
- **Source:** Posit / SuperDataScience, 2024-2025, videos and podcast
- **Link:** https://www.youtube.com/watch?v=8E2p5o07-EI ; https://www.superdatascience.com/podcast/sds-817-the-positron-ide-tidy-nlp-and-mlops-with-dr-julia-silge ; https://www.youtube.com/watch?v=aKSrptGegeo
- **Why it matters:** The engineering manager explaining why data science needs an IDE that is not a software-engineering IDE; good listening for the instructor and for curious students.
- **Use in course:** background. Lengths not confirmed (unverified).

### "Exploratory Data Analysis with R in Positron" (Mine Çetinkaya-Rundel)
- **Source:** Mine Çetinkaya-Rundel (Duke), 2025, video
- **Link:** https://www.youtube.com/watch?v=ndq2Mm3Dju8
- **Why it matters:** A leading statistics educator doing EDA in Positron the way she teaches it; R, but the console-plus-Quarto rhythm is exactly what the course wants in Python.
- **Use in course:** background. Date and length not confirmed (unverified).

### Udemy: "Créer un site web personnel avec Quarto, Positron et GitHub" (French)
- **Source:** Savoir-faire Digital, 2025-2026, online course (paid, about 75 enrolled, 4.5 rating; free YouTube summary at https://www.youtube.com/watch?v=DphbTu5jovU)
- **Link:** https://www.udemy.com/course/creer-un-site-web-personnel-avec-quarto-positron-et-github/
- **Why it matters:** One of very few third-party courses built on Positron; the Quarto website plus GitHub Pages workflow is the same one a student portfolio or course project site would use.
- **Use in course:** background (for French-speaking students; optional project add-on).

# Real-world examples

### Cornell INFO 4940 / INFO 5001 (Benjamin Soltoff): Positron, Quarto and GitHub as the course workflow
- **Source:** Cornell University, Bowers CIS, 2025-2026, course websites (case)
- **Link:** https://info4940.infosci.cornell.edu/hw/hw-05.html and https://info5001.infosci.cornell.edu/hw/hw-00.html
- **Why it matters:** Students clone homework repos into Positron workspaces, write in Quarto, render, commit and push with meaningful messages; HW 00 is a "hello" computing-workflow assignment. A working template for assessment logistics in a Positron + GitHub course.
- **Use in course:** session 1 (borrow the HW 00 structure); background for the GitHub workflow. Positron mention in INFO 5001 HW 00 not directly confirmed (unverified).

### positron.tutorials and Kane's free Data Science Course (David Kane, formerly Harvard)
- **Source:** David Kane, 2025-2026, CRAN package (v0.2.1, May 2026) and free 8-week online course (case)
- **Link:** https://ppbds.github.io/positron.tutorials/ and https://bootcamp.davidkane.info/
- **Why it matters:** Tutorials for Positron, Quarto, Git, GitHub and "using AI" written for absolute beginners; the r4ds.tutorials maintainers now tell teachers to use Positron rather than RStudio. The summer course (next cohort from 15 June 2026) promises that beginners will "use generative AI to do data science" by week 8. R-based, but the only documented beginner curriculum built on Positron plus AI.
- **Use in course:** background; the AI tutorials are a model for a Python equivalent.

### "Getting Started with Positron" short course at SDSS 2026 (Mine Çetinkaya-Rundel)
- **Source:** American Statistical Association SDSS 2026, half-day short course (case)
- **Link:** https://ww2.amstat.org/meetings/sdss/2026/shortcourses.cfm and https://opensource.posit.co/events/sdss-2026/
- **Why it matters:** A leading data science educator teaching Positron to statisticians coming from both RStudio and VS Code; signals that Positron is now the IDE statistics educators train each other on.
- **Use in course:** background (credibility argument in the syllabus).

### Universities deploying Positron Server through JupyterHub
- **Source:** Jupyter blog / Posit, 2026, article (case)
- **Link:** https://blog.jupyter.org/positron-server-available-for-academic-use-via-jupyterhub-ae4e406f9444
- **Why it matters:** Describes the institution-level pattern: Positron appears as a launcher next to JupyterLab, students log in with their usual JupyterHub account, shared environments are pre-loaded, no laptop installs. Free education licence by e-mail.
- **Use in course:** background (WU infrastructure option).

### NHS Strategy Unit: "Positron for Product Owners" (Claire Welsh)
- **Source:** Posit blog / NHS-R Community, 2026, article (case)
- **Link:** https://posit.co/blog/positron-for-product-owners (mirror: https://nhsrcommunity.com/blog/positron_for_product.html)
- **Why it matters:** Lead data scientist of an internal NHS consultancy on using Positron for backlog reviews, Quarto documentation, test debugging and fast project switching; a non-coder-manager perspective that business students will recognise.
- **Use in course:** session 5 (short case on how analytics teams actually work).

### Pharma analysts: R/Pharma 2026 workshop on Posit Assistant with clinical data (ADaM, SDTM)
- **Source:** Posit (Garrett Grolemund), 28 September 2026, workshop (case)
- **Link:** https://github.com/posit-dev/human-in-the-loop-ai-r-pharma-2026
- **Why it matters:** Documents how a regulated industry is being taught to use an in-IDE agent: approved model providers, data never leaves the machine, every line approved. Governance template for a course policy on client or survey data.
- **Use in course:** session 2 (policy discussion); sessions 3-4 (lab structure).

### Practitioner testimonials on the Positron product page (Pfizer, Bath & Body Works, Memorial Sloan Kettering)
- **Source:** Posit PBC, 2025-2026, website (vendor-curated quotes)
- **Link:** https://posit.co/products/ide/positron
- **Why it matters:** Sam Parmar (statistical data scientist, Pfizer), Jeffrey Sumner (Bath & Body Works, a retailer) and Meghan Harris (MSKCC) on switching between R and Python and on the AI assistant. Vendor-selected, so treat as colour, not evidence.
- **Use in course:** background.

### Alex Zajichek: "Trying AI-assisted development in the Positron IDE"
- **Source:** Alex Zajichek (independent biostatistician), 29 October 2025, blog case
- **Link:** https://www.zajichekstats.com/post/ai-assisted-shiny-development-in-positron/
- **Why it matters:** Step-by-step record of adding features to a Shiny app with the (legacy) assistant, including what had to be corrected; a realistic log of human-AI collaboration that could serve as an example "prompt log" for assessment.
- **Use in course:** session 4 (example of a documented AI workflow).

### Raymond Hunter: "An Introduction to Positron Assistant"
- **Source:** Raymond Hunter (environmental data scientist), 30 October 2025, blog case
- **Link:** https://ramhunte.github.io/blogs/positron_assitant/
- **Why it matters:** Beginner-friendly walkthrough of setting up Claude and Copilot providers and using chat and inline completions for an analysis; written by a recent graduate for peers.
- **Use in course:** background (student-level voice). Describes the legacy assistant.

### Instructor concern: "Academic integrity with Posit's AI integration in Posit Cloud" (Posit Community)
- **Source:** Posit Community forum thread with Posit staff reply, 2026, case
- **Link:** https://forum.posit.co/t/academic-integrity-with-posits-ai-integration-in-posit-cloud/211566
- **Why it matters:** An intro-R instructor asks whether AI can be disabled for exams; Posit's answer is that Cloud does not bundle AI but cannot stop a student signing into their own Posit AI subscription. Concrete evidence for designing assessment that assumes AI is available rather than trying to block it.
- **Use in course:** the assessment design and AI policy (background for the instructor).

### Andrew Heiss (Georgia State): "Switching to Positron full-time" and "Fun with Positron"
- **Source:** Andrew Heiss, 2024-2026, blog and GitHub discussion (case)
- **Link:** https://www.andrewheiss.com/blog/2024/07/08/fun-with-positron/ (full-time switch thread indexed at https://opensource.posit.co/blog/2026-04-28_positron-community-resources/)
- **Why it matters:** A public-policy professor who teaches data analysis to non-programmers documents his full move to Positron and the settings he uses; a close analogue to a business-school instructor.
- **Use in course:** background (configuration ideas for session 1).

# Gaps and caveats

- Network restrictions in this environment blocked direct fetching of positron.posit.co, posit.co, opensource.posit.co, assistant.posit.co, docs.posit.co, blog.stephenturner.us and YouTube. Those links were confirmed through search-engine results and, for Positron's docs, through the GitHub source repository posit-dev/positron-website; video lengths and dates marked "(unverified)" could not be read from the player. Re-check the handful of YouTube IDs before putting them on slides.
- Moving target: Positron ships monthly and Posit Assistant only replaced Positron Assistant and Databot in July 2026. Most independent blog posts and all Posit videos before April 2026 show the old assistant; menus, provider sign-in and some commands differ. The Posit Academy "Positron AI Workshop" and its GitHub repo also still describe the old tools.
- Provider lists are inconsistent across Posit pages: the Posit Assistant getting-started page lists eleven providers (including OpenAI, Gemini and Copilot in preview), while the Posit AI Pass FAQ says Anthropic Claude is currently the sole provider for AI Pass credits. Treat the getting-started page as authoritative for BYO-key, and AI Pass as Claude-only for now.
- Student pricing changes quickly: GitHub paused and then reopened the free Copilot Student plan in 2026, Cursor ended its free student year on 25 June 2026, and Claude for Education is institution-level with no individual student discount. Posit AI Pass (USD 20/month, USD 5 first month) and pay-as-you-go Anthropic keys are the stable options; all prices are in USD from vendor pages and were not checked for EU VAT.
- No peer-reviewed study of Positron or Posit Assistant in teaching exists yet; the "real-world" entries are course websites, workshop repos, vendor case posts and practitioner blogs. The academic-integrity evidence is a forum thread, not a policy document. I found no business-school course that documents switching to Positron, and no European university case beyond the NHS and Jumping Rivers (UK) items.
- The Posit whitepaper and some Posit blog posts sit behind a form or are vendor-authored; the independent material is weighted towards R users (R-bloggers, Jumping Rivers, r-statistics.co). Python-first beginner material on Positron is still thin outside Posit's own tutorials.

# Positron and AI-assisted analytics: books, journal articles, reports, teaching cases

Part 02 of the Positron resource search. Scope: AI-assisted coding and data analysis in (business) education, with Positron, Positron Assistant, GitHub Copilot, Claude Code and similar assistants as the tool context. Entries are ranked best first within each section. Links were confirmed through publisher, DOI or repository pages surfacing in search results; direct fetching was blocked for most domains in this session (see "Gaps and caveats"). Date of search: 5 October 2026.

## Books

### Learn AI-Assisted Python Programming, Second Edition
- **Source:** Leo Porter and Daniel Zingaro, Manning, 2024, book
- **Link:** https://www.manning.com/books/learn-ai-assisted-python-programming-second-edition
- **Why it matters:** The only mainstream textbook that teaches Python from zero with Copilot and ChatGPT as the default workflow: problem decomposition, reading and testing generated code, prompt refinement, debugging. Written by the two CS-education researchers whose CS1-LLM course is the best-documented evidence base. Includes data-analysis and automation projects.
- **Use in course:** Core reading, sessions 1 to 3 (chapters 1 to 5 on prompting, testing and decomposition). Paid (about EUR 40, Manning liveBook subscription or print); first edition chapters are sometimes free as Manning previews.

### Teaching with AI: A Practical Guide to a New Era of Human Learning (2nd edition)
- **Source:** José Antonio Bowen and C. Edward Watson, Johns Hopkins University Press, 2025 (1st ed. 2024), book
- **Link:** https://www.hfsbooks.com/books/teaching-with-ai-2nd-edition-bowen-watson/
- **Why it matters:** The standard instructor handbook on AI-era course design: assignment redesign, assessment, integrity, "AI-use statements" and prompt disclosure. The 2nd edition (December 2025) adds reasoning models, agents and an ethics chapter.
- **Use in course:** Background for the instructor when writing the course AI policy and rubric; not a student reading. Paid (about EUR 30).

### Co-Intelligence: Living and Working with AI
- **Source:** Ethan Mollick, Portfolio/Penguin, 2024, book
- **Link:** https://books.google.com/books/about/Co_intelligence.html?id=LS2N0AEACAAJ
- **Why it matters:** Short, readable framing of the "jagged frontier", "centaur vs cyborg" work styles and the four rules (always invite AI to the table, be the human in the loop, treat AI like a person but tell it what kind, assume this is the worst AI you will ever use). Business-school voice, so it lands with CEMS students.
- **Use in course:** Optional pre-reading for session 1 (chapters 1 to 4); gives students a shared vocabulary for reflecting on their AI use in prompt logs. Paid (about EUR 20), widely available in WU library e-book collections (check).

### AI-Assisted Programming: Better Planning, Coding, Testing, and Deployment
- **Source:** Tom Taulli, O'Reilly, 2024, book
- **Link:** https://www.oreilly.com/library/view/ai-assisted-programming/9781098164553/
- **Why it matters:** Tool-agnostic survey of Copilot, ChatGPT, Claude, Cursor and friends across the full development cycle, with a useful chapter on prompt patterns for code and on the limits of generated code. Practitioner rather than pedagogical.
- **Use in course:** Background for the instructor; chapters on prompting and testing can be excerpted for session 2. Paid; available via O'Reilly Learning if WU subscribes.

### Beyond Vibe Coding: From Coder to AI-Era Developer
- **Source:** Addy Osmani (Google Chrome team), O'Reilly, 2025, book
- **Link:** https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/
- **Why it matters:** The clearest practitioner critique of "vibe coding": it distinguishes throwaway prompting from AI-assisted engineering, insists on reviewing AI output like a junior colleague's pull request, and gives review, testing and version-control habits. Simon Willison's review (https://simonwillison.net/2025/Sep/4/beyond-vibe-coding/) is a good two-page summary.
- **Use in course:** Chapter 1 ("What is vibe coding?") as a session 1 reading to set the norm that students must understand what they commit. Paid.

### Vibe Coding: Building Production-Grade Software with GenAI, Chat, Agents, and Beyond
- **Source:** Gene Kim and Steve Yegge, IT Revolution, 2025, book (foreword by Dario Amodei)
- **Link:** https://www.simonandschuster.com/books/Vibe-Coding/Gene-Kim/9781966280026
- **Why it matters:** The optimistic counterpart to Osmani: agentic coding as the future of software work, with workflow advice for chat-and-agent development. Pair with The Register's sceptical review (https://www.theregister.com/2025/10/21/book_review_vibe_coding/) for a balanced debate.
- **Use in course:** Background; one chapter plus the review make a good debate prompt in session 5 on "what should a marketing analyst still know?". Paid.

### R for Data Science (2nd edition)
- **Source:** Hadley Wickham, Mine Çetinkaya-Rundel and Garrett Grolemund, O'Reilly, 2023, book (free online)
- **Link:** https://r4ds.hadley.nz/
- **Why it matters:** The reference for the tidy, Quarto-based reproducible workflow that Positron inherits from RStudio. Even for a Python-first course, the chapters on Quarto, workflow and data tidying are the best explanation of why notebooks plus version control matter. Pair with the Quarto guide (https://quarto.org/docs/guide/).
- **Use in course:** Background, and the Quarto chapters (Communicate section) as a session 1 lab reference. Free online, print about EUR 60.

### Python for Data Analysis (3rd edition)
- **Source:** Wes McKinney, O'Reilly, 2022, book (open-access online edition)
- **Link:** https://wesmckinney.com/book/
- **Why it matters:** The pandas creator's own text, updated for pandas 2.0 and Python 3.10. Not about AI, but it is the look-up reference students need when an assistant produces pandas code they cannot read: indexing, groupby, reshaping, time series.
- **Use in course:** Reference for all lab sessions; chapters 5, 8 and 10 as "read when stuck" material. Free online.

### Python for MBAs
- **Source:** Mattan Griffel and Daniel Guetta (Columbia Business School), Columbia Business School Publishing, 2021, book
- **Link:** https://www.amazon.com/Python-MBAs-Mattan-Griffel/dp/0231193939
- **Why it matters:** Written for business students with no prior coding, by the people who teach the Columbia MBA Python course; business-flavoured examples (sales data, customer tables) rather than CS toy problems. Pre-dates LLM assistants, so pair with Porter and Zingaro.
- **Use in course:** Optional background for students who want a gentler Python on-ramp; chapters 1 to 4. Paid (about EUR 35).

## Journal articles

### Generative AI for Data Science 101: Coding Without Learning to Code
- **Source:** Jacob Bien and Gourab Mukherjee (USC Marshall), Journal of Statistics and Data Science Education 33(2), 129 to 142, 2025, article
- **Link:** https://doi.org/10.1080/26939169.2024.2432397 (preprint: https://arxiv.org/abs/2401.17647)
- **Why it matters:** The closest published analogue to this course: a required MBA data-science course where students with no coding background wrote English prompts for GitHub Copilot that became R code. Reports the design, what students could and could not do, and what the instructors would change.
- **Use in course:** Instructor reading before session 1; the "what students struggled with" section informs the lab scaffolding. Open access.

### CS1-LLM: Integrating LLMs into CS1 Instruction
- **Source:** Annapurna Vadaparty, Daniel Zingaro, David H. Smith IV, Mounika Padala, Christine Alvarado, Jamie Gorson Benario and Leo Porter, ITiCSE 2024, article
- **Link:** https://doi.org/10.1145/3649217.3653584
- **Why it matters:** The published course design and first-offering evaluation behind the Porter and Zingaro book: 550+ mostly non-CS first-years learning Python with Copilot from day one, with assessment built around decomposition, testing and code reading rather than code writing.
- **Use in course:** Background for the course design; its assessment ideas (explain-and-test tasks) transfer directly to session 5 grading. ACM paywall; author version via UCSD.

### The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers
- **Source:** James Prather, Brent N. Reeves, Juho Leinonen, Stephen MacNeil et al., ICER 2024, article
- **Link:** https://doi.org/10.1145/3632620.3671116 (open version: https://arxiv.org/abs/2405.17739)
- **Why it matters:** Think-aloud study showing that strong students accelerate with GenAI while struggling students' metacognitive problems persist or worsen (illusion of competence, accepting wrong code). The best single paper for justifying guard-rails and reflection prompts.
- **Use in course:** Instructor reading; one-paragraph summary for students in session 1 to explain why prompt logs and "explain your code" checks exist. Open access.

### Prompt Problems: A New Programming Exercise for the Generative AI Era
- **Source:** Paul Denny, Juho Leinonen, James Prather, Andrew Luxton-Reilly, Thezyrie Amarouche, Brett A. Becker and Brent N. Reeves, SIGCSE 2024, article
- **Link:** https://doi.org/10.1145/3626252.3630909 (open version: https://arxiv.org/abs/2311.05943)
- **Why it matters:** Introduces an exercise type where students see a visual problem and must write a prompt that makes an LLM produce correct code; code is auto-tested. Directly reusable as an assessment format that rewards specification skill rather than syntax.
- **Use in course:** Lab exercise template for sessions 2 to 4 (e.g. "write the prompt that produces the churn table"). Open access.

### Studying the Effect of AI Code Generators on Supporting Novice Learners in Introductory Programming
- **Source:** Majeed Kazemitabaar, Justin Chow, Carl Ka To Ma, Barbara J. Ericson, David Weintrop and Tovi Grossman, CHI 2023, article
- **Link:** https://doi.org/10.1145/3544548.3580919
- **Why it matters:** Controlled study (69 novices, Codex vs none): the AI group completed more tasks and scored higher on code authoring without harming later manual coding, though learners over-relied on the tool. Frequently cited as the main "no harm" evidence.
- **Use in course:** Background evidence for the course AI policy. ACM paywall; author PDF at https://www.terpconnect.umd.edu/~weintrop/papers/Kazemitabaar_et_al_CHI_2023.pdf

### How Beginning Programmers and Code LLMs (Mis)read Each Other
- **Source:** Sydney Nguyen, Hannah McLean Babe, Yangtian Zi, Arjun Guha, Carolyn Jane Anderson and Molly Q Feldman, CHI 2024, article
- **Link:** https://doi.org/10.1145/3613904.3642706 (open version: https://arxiv.org/abs/2401.15232)
- **Why it matters:** 120 beginners across three institutions writing prompts for code LLMs: students struggle to describe problems precisely and models misread vague descriptions. Strong evidence that prompt specification is a teachable skill, not a given.
- **Use in course:** Instructor reading; informs the session 2 "specify before you prompt" exercise. Open access.

### AI Meets the Classroom: When Do Large Language Models Harm Learning?
- **Source:** Matthias Lehmann, Philipp B. Cornelius and Fabian J. Sting (European business-school authors), working paper, 2024 (revised 2025), article
- **Link:** https://arxiv.org/abs/2409.09047
- **Why it matters:** Two pre-registered lab experiments plus observational data from university Python courses: LLM use did not change average learning, but students who used the model as a tutor (asking for explanations) learned more, those who used it as a solution generator learned less, and all over-estimated the benefit. The closest evidence base for a business-school Python course in Europe.
- **Use in course:** Instructor reading; cite in the AI policy as the reason for "ask for explanation, then generate" prompting rules. Open access preprint; journal status to check.

### Generative AI Without Guardrails Can Harm Learning: Evidence from High School Mathematics
- **Source:** Hamsa Bastani, Osbert Bastani, Alp Sungu, Haosen Ge, Özge Kabakcı and Rei Mariman (Wharton), PNAS 122(26), 2025, article
- **Link:** https://doi.org/10.1073/pnas.2422633122
- **Why it matters:** Large field experiment (about 1,000 students): unrestricted GPT-4 raised practice performance by 48 per cent but lowered unassisted exam scores by 17 per cent; a tutor version with hints-only guard-rails removed the harm. School maths, not coding, but the cleanest causal evidence that interface design matters.
- **Use in course:** Instructor reading; justifies configuring Positron Assistant or Copilot in "explain and hint" mode for early labs. Open access.

### The Robots Are Coming: Exploring the Implications of OpenAI Codex on Introductory Programming
- **Source:** James Finnie-Ansley, Paul Denny, Brett A. Becker, Andrew Luxton-Reilly and James Prather, ACE 2022, article
- **Link:** https://doi.org/10.1145/3511861.3511863
- **Why it matters:** The paper that started the field: Codex out-scored most students on real CS1 exam questions. Mainly historical now, but the reference point for "assessment must change".
- **Use in course:** Background only. ACM paywall; author versions on ResearchGate.

### Programming Is Hard, Or at Least It Used to Be: Educational Opportunities and Challenges of AI Code Generation
- **Source:** Brett A. Becker, Paul Denny, James Finnie-Ansley, Andrew Luxton-Reilly, James Prather and Eddie Antonio Santos, SIGCSE 2023, article
- **Link:** https://doi.org/10.1145/3545945.3569759 (open version: https://arxiv.org/abs/2212.01020)
- **Why it matters:** Position paper listing opportunities (lower barriers, better error messages, more time for design) and challenges (integrity, over-reliance, bias) and arguing that educators must adapt rather than ban. Good agenda-setter.
- **Use in course:** Background. Open access.

### From "Ban It Till We Understand It" to "Resistance is Futile": How University Programming Instructors Plan to Adapt
- **Source:** Sam Lau and Philip J. Guo (UC San Diego), ICER 2023, article
- **Link:** https://doi.org/10.1145/3568813.3600138 (author PDF: https://lau.ucsd.edu/pubs/cs-instructors-adapting-to-chatgpt-copilot-ai-tools_ICER-2023.pdf)
- **Why it matters:** Interviews with 20 instructors in nine countries on how they planned to respond to Copilot and ChatGPT: short-term integrity measures versus long-term curriculum change. Useful typology for positioning the course's own stance.
- **Use in course:** Background for the AI policy. Open author PDF.

### The Robots Are Here: Navigating the Generative AI Revolution in Computing Education (ITiCSE Working Group report)
- **Source:** James Prather, Paul Denny, Juho Leinonen, Brett A. Becker et al. (15 authors), ITiCSE-WGR 2023, report-length article
- **Link:** https://doi.org/10.1145/3623762.3633499 (open version: https://arxiv.org/abs/2310.00658)
- **Why it matters:** 50-page synthesis: literature review, student and instructor surveys, and concrete recommendations on assessment, policy and tooling. The best one-stop reference if only one computing-education source is read.
- **Use in course:** Background; the recommendations section informs the course rules. Open access.

### Teaching CS50 with AI: Leveraging Generative Artificial Intelligence in Computer Science Education
- **Source:** Rongxin Liu, Carter Zenke, Charlie Liu, Andrew Holmes, Patrick Thornton and David J. Malan (Harvard), SIGCSE 2024, article
- **Link:** https://doi.org/10.1145/3626252.3630938
- **Why it matters:** How Harvard's largest course deployed a guard-railed assistant (the CS50 Duck) that explains and hints rather than solves, with usage data and student perceptions. The reference design for "pedagogically constrained" assistants.
- **Use in course:** Background; model for a system prompt students can paste into Positron Assistant or Claude. ACM paywall; Harvard author PDF available.

### The Impact of AI on Developer Productivity: Evidence from GitHub Copilot
- **Source:** Sida Peng, Eirini Kalliamvakou, Peter Cihon and Mert Demirer, arXiv working paper, 2023, article
- **Link:** https://arxiv.org/abs/2302.06590
- **Why it matters:** The original Copilot RCT (95 developers, HTTP server task): treatment group 55.8 per cent faster, with larger gains for less experienced developers. The number everyone quotes; students should learn how narrow the task was.
- **Use in course:** Session 1 discussion ("what does 56 per cent faster actually mean?"). Open access.

### The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers
- **Source:** Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng and Tobias Salz, Management Science, 2025/2026 (online first), article
- **Link:** https://doi.org/10.1287/mnsc.2025.00535 (draft: https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf)
- **Why it matters:** RCTs at Microsoft, Accenture and a Fortune 100 firm (4,867 developers): about 26 per cent more completed tasks, with the largest gains and adoption among less experienced developers. The strongest field evidence on Copilot in real work.
- **Use in course:** Session 1 or 5 reading on what AI assistance does to skill premia; pairs with METR below. Paywall at INFORMS; MIT draft open.

### Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity
- **Source:** Joel Becker, Nate Rush, Beth Barnes and David Rein (METR), 2025, report-style article
- **Link:** https://arxiv.org/abs/2507.09089 (summary and PDF: https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf)
- **Why it matters:** RCT with 16 experienced open-source developers using Cursor and Claude 3.5/3.7 Sonnet: tasks took 19 per cent longer with AI, while developers believed they were 20 per cent faster. The essential corrective on perceived versus measured productivity.
- **Use in course:** Session 5 discussion on self-assessment bias; ask students to compare their own prompt-log time estimates. Open access.

### Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality
- **Source:** Fabrizio Dell'Acqua, Edward McFowland III, Ethan Mollick, Hila Lifshitz-Assaf, Katherine Kellogg, Saran Rajendran, Lisa Krayer, François Candelon and Karim Lakhani, Harvard Business School Working Paper 24-013, 2023, article
- **Link:** https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
- **Why it matters:** 758 BCG consultants: GPT-4 raised quality and speed on tasks inside the frontier and lowered accuracy on a task outside it (a data-driven business problem). Introduces "centaur" and "cyborg" work patterns. The business-school reference point for analysts, not coders.
- **Use in course:** Session 1 reading (executive summary) to frame when to trust the assistant in analysis. Open access working paper (SSRN 4573321).

### Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence
- **Source:** Shakked Noy and Whitney Zhang (MIT), Science 381, 187 to 192, 2023, article
- **Link:** https://doi.org/10.1126/science.adh2586
- **Why it matters:** 453 professionals on writing tasks: ChatGPT cut time by 40 per cent and raised quality by 18 per cent, compressing inequality between workers. Short, clean and widely taught.
- **Use in course:** Background; one-slide summary in session 1. Science paywall; SSRN preprint open.

### What Should Data Science Education Do With Large Language Models?
- **Source:** Xinming Tu, James Zou, Weijie Su and Linjun Zhang, Harvard Data Science Review 6(1), 2024, article
- **Link:** https://doi.org/10.1162/99608f92.bff007ab
- **Why it matters:** Argues that LLMs shift the data scientist's job from hands-on coding to specifying, assessing and managing analyses, and proposes curriculum changes (more problem framing, verification, communication). The conceptual anchor for a "manager of analyses" learning goal.
- **Use in course:** Session 1 reading for students (short, open access).

### Generative AI and Marketing Education: What the Future Holds
- **Source:** Abhijit Guha, Dhruv Grewal and Stephen Atlas, Journal of Marketing Education 46(1), 6 to 17, 2024, article
- **Link:** https://doi.org/10.1177/02734753231215436
- **Why it matters:** Literature survey plus interviews and surveys of marketing educators and managers on how generative AI should enter the marketing curriculum, including analytics skills. The discipline-specific framing for a marketing analytics course.
- **Use in course:** Background for the instructor; cite in the syllabus rationale. SAGE paywall (WU access likely).

### Generative AI in Higher Education Assessments: Examining Risk and Tech-Savviness on Students' Adoption
- **Source:** Yusuf Oc, Chahna Gonsalves and Lashawn Toussaint Quamina, Journal of Marketing Education 47(2), 138 to 155, 2024 (online), article
- **Link:** https://doi.org/10.1177/02734753241302459
- **Why it matters:** Survey evidence on what drives marketing students to use GenAI in assessed work (perceived risk, tech confidence), with implications for assessment design and disclosure rules.
- **Use in course:** Background for the AI policy and the prompt-log requirement. SAGE paywall.

### Transformative Teaching in Management Statistics: Integrating Real-World Experiences and Artificial Intelligence
- **Source:** Williams, Decision Sciences Journal of Innovative Education, 2026 (online first), teaching brief
- **Link:** https://onlinelibrary.wiley.com/doi/full/10.1111/dsji.70019
- **Why it matters:** Scaffolded lessons in an undergraduate operations management course where students compared Excel and ChatGPT for the same statistical analyses, with industry guests and a site visit; reports higher interest in analytics. A transferable "tool comparison" lab design.
- **Use in course:** Lab idea for session 2 (Excel versus Positron-plus-assistant on the same data). Wiley paywall. Author first name not confirmed in the search result.

### A New Era of Learning: Considerations for ChatGPT as a Tool to Enhance Statistics and Data Science Education
- **Source:** Amanda R. Ellis and Emily Slade, Journal of Statistics and Data Science Education 31(2), 128 to 133, 2023, article
- **Link:** https://doi.org/10.1080/26939169.2023.2223609
- **Why it matters:** Early, practical guidance on prompting students to use ChatGPT responsibly in statistics courses; part of JSDSE's generative AI collection, which also has a 2025 call for classroom-experience papers (https://doi.org/10.1080/26939169.2025.2473300).
- **Use in course:** Background. Open access.

### The Use of Generative AI in Statistical Data Analysis and Its Impact on Teaching Statistics at Universities of Applied Sciences
- **Source:** Schwarz, Teaching Statistics, 2025, article
- **Link:** https://doi.org/10.1111/test.12398
- **Why it matters:** German-language-region applied-university perspective on what GenAI changes in teaching statistical analysis, including what still needs to be learned by hand. Useful regional counterpoint to US CS-education literature. Related: Xing (2024) in the same journal, https://doi.org/10.1111/test.12367.
- **Use in course:** Background. Wiley; open-access status to check.

### The Effect of Generative AI-Based Tool Use on Students' Computational Thinking Skills, Programming Self-Efficacy and Motivation
- **Source:** Ramazan Yilmaz and Fatma Gizem Karaoglan Yilmaz, Computers and Education: Artificial Intelligence 4, 100147, 2023, article
- **Link:** https://doi.org/10.1016/j.caeai.2023.100147
- **Why it matters:** Quasi-experiment with 45 undergraduates: ChatGPT use raised computational-thinking scores, self-efficacy and motivation. Small sample, but one of the few studies with affective outcomes, which matter for non-programmers.
- **Use in course:** Background. Open access.

### Your Brain on ChatGPT: Accumulation of Cognitive Debt When Using an AI Assistant for Essay Writing Task
- **Source:** Nataliya Kosmyna et al. (MIT Media Lab), arXiv preprint 2506.08872, 2025, article (not peer-reviewed)
- **Link:** https://www.media.mit.edu/publications/your-brain-on-chatgpt/
- **Why it matters:** Widely cited EEG study (54 participants) finding weaker neural engagement and lower recall for LLM-assisted essay writers. Included because students will have seen the headlines; it is small, essay-based, and contested, so it is a good object for a critical-reading exercise.
- **Use in course:** Optional session 5 discussion on how to read AI-and-learning evidence. Open access.

## Reports

### Guidance for Generative AI in Education and Research
- **Source:** UNESCO (Fengchun Miao and Wayne Holmes), 2023, report
- **Link:** https://unesdoc.unesco.org/ark:/48223/pf0000386693 (unverified exact link; title and authors confirmed via https://discovery.ucl.ac.uk/id/eprint/10176438/)
- **Why it matters:** First global policy guidance: human-centred principles, data protection, age limits, teacher training and a framework for institutional GenAI policies. The reference most national guidelines cite.
- **Use in course:** Background for the policy section of the syllabus. Free.

### OECD Digital Education Outlook 2023: Towards an Effective Digital Education Ecosystem
- **Source:** OECD, 2023, report (chapter "Opportunities, guidelines and guardrails for effective and equitable use of AI in education")
- **Link:** https://www.oecd.org/en/publications/oecd-digital-education-outlook-2023_c74f03de-en/full-report/opportunities-guidelines-and-guardrails-for-effective-and-equitable-use-of-ai-in-education_2f0862dc.html
- **Why it matters:** Cross-country comparison of how (little) governments had regulated or guided GenAI in education, plus the OECD's guidelines-and-guardrails framework. A 2026 edition exists (https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/01/oecd-digital-education-outlook-2026_940e0dd8/062a7394-en.pdf).
- **Use in course:** Background. Free.

### 2025 EDUCAUSE AI Landscape Study: Into the Digital AI Divide
- **Source:** EDUCAUSE, February 2025, report
- **Link:** https://library.educause.edu/resources/2025/2/2025-educause-ai-landscape-study
- **Why it matters:** Survey of 788 higher-education professionals: 57 per cent see AI as a strategic priority, 39 per cent have acceptable-use policies, and teaching-and-learning use focuses on academic integrity (74 per cent) and assessment (54 per cent). Benchmarks for where WU sits.
- **Use in course:** Background. Free.

### Jisc National Centre for AI: Assessment Menu and Generative AI Primer
- **Source:** Jisc, 2023 (menu, updated) and 2026 (primer update), reports and toolkit
- **Link:** https://nationalcentreforai.jiscinvolve.org/wp/2023/09/12/designing-assessment-in-an-ai-enabled-world/ and https://nationalcentreforai.jiscinvolve.org/wp/2026/01/27/generative-ai-primer/
- **Why it matters:** The Assessment Menu is 40 cards of assessment designs that either embed AI or resist it, each rated for authenticity, challenge and staff time. The most practical assessment-redesign tool available; the primer is a short, current explainer for staff.
- **Use in course:** Instructor tool when designing the session 5 assessment and prompt-log grading. Free.

### Reconsidering Assessment for the ChatGPT Era (and related QAA advice)
- **Source:** Quality Assurance Agency for Higher Education (UK), 2023, guidance
- **Link:** https://www.qaa.ac.uk/sector-resources/generative-artificial-intelligence/qaa-advice-and-resources
- **Why it matters:** Sector guidance on assessment validity when students have GenAI: shift to process evidence, oral components, reflective accounts and disclosure. Explicitly notes the principles apply to code generation.
- **Use in course:** Background for grading rules (process evidence through GitHub history and prompt logs). Free.

### Russell Group Principles on the Use of Generative AI Tools in Education
- **Source:** Russell Group (24 UK research universities), July 2023, policy brief
- **Link:** https://www.russellgroup.ac.uk/sites/default/files/2025-01/Russell%20Group%20principles%20on%20generative%20AI%20in%20education.pdf
- **Why it matters:** Five principles (AI literacy, staff support, adapt teaching and assessment, uphold integrity, collaborate) that moved the sector from banning to teaching with AI. A one-page model for a course policy preamble.
- **Use in course:** Quote in the syllabus AI policy. Free.

### WU Vienna: AI and Your Academic Practice (Code of Conduct) and AI in Teaching pages
- **Source:** WU Wirtschaftsuniversität Wien, 2024 to 2025, institutional guidelines
- **Link:** https://www.wu.ac.at/en/students/wu-campus/code-of-conduct/ai-and-your-academic-practice and https://www.wu.ac.at/en/staff/information-for-teachers/ai-in-teaching/wissenschaftliches-arbeiten-und-ki
- **Why it matters:** WU's own rule set: the course instructor decides whether and for what AI may be used, AI-generated content must be transparently identified, and students are advised to keep and document their prompts. Turnitin's AI check runs on a trial basis for English texts. Institute-level examples exist (Institute for Social Policy: https://www.wu.ac.at/en/institute-for-social-policy/lehre/institute-guidelines-for-the-use-of-ai; Institute for Nonprofit Management: https://www.wu.ac.at/en/institute-for-nonprofit-management-and-governance/lehre/ai-und-software-policy).
- **Use in course:** Session 1: the course AI rules must sit inside this framework; the prompt-documentation advice maps directly onto a prompt-log deliverable. Free. (Pages confirmed in search results; direct fetch blocked in this session.)

### Guidelines der Universität Wien zum Umgang mit Künstlicher Intelligenz in der Lehre (2nd edition)
- **Source:** Universität Wien, Center for Teaching and Learning, September 2024, handbook
- **Link:** https://phaidra.univie.ac.at/detail/o:1876016 (1st ed.); 2nd ed. reported at https://doi.org/10.25365/phaidra.544 (unverified)
- **Why it matters:** The most detailed Austrian university handbook: legal basis (Austrian university law, exam regulations), disclosure templates, checklists for students and teachers, and sample course-policy wording in German. FH Joanneum's Leitfaden (https://cdn3.fh-joanneum.at/media/2024/10/KI-Leitfaden_v_08_2024.pdf) is a shorter Austrian alternative.
- **Use in course:** Background for the instructor; the student checklist can be adapted for the WU course. Free.

### Künstliche Intelligenz: Grundlagen für das Handeln in der Hochschullehre (HFD Arbeitspapier Nr. 86) and HRK resolution "Digitale Hochschule"
- **Source:** Hochschulforum Digitalisierung, 2024, working paper; Hochschulrektorenkonferenz, November 2023, resolution
- **Link:** https://hochschulforumdigitalisierung.de/publikationen/arbeitspapier-nr-86-kuenstliche-intelligenz-grundlagen-fuer-das-handeln-in-der-hochschullehre/ and https://www.hrk.de/positionen/beschluss/detail/digitale-hochschule-herausforderungen-und-kooperationsmoeglichkeiten/
- **Why it matters:** The German-language sector framing: HRK names AI competence as a core need and has since launched the KI-LOTSE service centre; the HFD paper gives practical teaching guidance. Useful for German-speaking CEMS students and for aligning with DACH norms.
- **Use in course:** Background. Free.

### Anthropic Education Report: How University Students Use Claude
- **Source:** Anthropic, April 2025, report
- **Link:** https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude
- **Why it matters:** Privacy-preserving analysis of about 574,000 student conversations: computer-science students dominate, business students under-use, and roughly half of interactions are "direct" answer-seeking rather than collaborative. Gives students a mirror for their own usage patterns.
- **Use in course:** Session 1 short reading; ask students to classify their own prompt-log entries using the four interaction styles. Free.

### Stanford AI Index Report 2025, Chapter 7: Education
- **Source:** Stanford Institute for Human-Centered AI, April 2025, report
- **Link:** https://hai.stanford.edu/ai-index/2025-ai-index-report/education
- **Why it matters:** Data on AI and CS education worldwide, teacher preparedness gaps and degree trends; the other chapters give the macro numbers (investment, capability benchmarks) for a session 1 context slide. A 2026 edition is now out.
- **Use in course:** Background. Free.

### GitHub Octoverse 2025
- **Source:** GitHub, October 2025, report
- **Link:** https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- **Why it matters:** TypeScript overtook Python as most-used language on GitHub, driven by AI-assisted development, while Python stays dominant in data and AI work (2.6 million contributors); 80 per cent of new developers use Copilot in their first week. Context for why GitHub and Copilot are in the course toolchain.
- **Use in course:** Session 1 context slide. Free.

### Stack Overflow Developer Survey 2025, AI section
- **Source:** Stack Overflow, July 2025, survey report (49,000+ respondents)
- **Link:** https://survey.stackoverflow.co/2025/
- **Why it matters:** 84 per cent use or plan to use AI tools but only 29 per cent trust their accuracy; the top frustration (66 per cent) is "almost right but not quite" code and 45 per cent say debugging AI code takes longer. Exactly the failure mode novices must learn to detect.
- **Use in course:** Session 1 discussion; revisit in session 5 against students' own logs. Free.

### HEPI / Kortext Student Generative AI Survey 2025
- **Source:** Higher Education Policy Institute (UK), February 2025, report
- **Link:** https://www.hepi.ac.uk/reports/student-generative-ai-survey-2025/
- **Why it matters:** 92 per cent of UK students use AI (66 per cent a year earlier), 88 per cent in assessments; top worries are misconduct accusations and hallucinations; a gender and subject divide in use. Useful to normalise disclosure and to design for the anxious half of the class.
- **Use in course:** Background; one slide in session 1. Free.

## Teaching cases and course examples

### USC Marshall MBA "Data Science 101" with GitHub Copilot and R
- **Source:** Jacob Bien and Gourab Mukherjee, 2023 course design, published 2025 (see Journal articles), course example; CAUSE webinar recording 2025
- **Link:** https://doi.org/10.1080/26939169.2024.2432397 and https://www.causeweb.org/cause/webinar/jsdse/2025-02
- **Why it matters:** The best-documented business-school precedent: non-coding MBA students doing real analysis by prompting Copilot inside an IDE, with the instructors' candid list of what worked and what did not. The webinar adds the practical details (set-up, grading).
- **Use in course:** Instructor model for the whole course; watch the webinar before session 1. Free.

### STA 199 Introduction to Data Science and Statistical Thinking (Duke), AI policy and Quarto/GitHub workflow
- **Source:** Mine Çetinkaya-Rundel and team, Duke University, autumn 2025 offering, course website
- **Link:** https://sta199-f25.github.io/course-syllabus.html (course hub: https://mine-cr.com/teaching/)
- **Why it matters:** A mature, fully open course (R, Quarto, GitHub, Posit tools) with a two-principle AI policy: a cognitive dimension (AI must not reduce your thinking) and an ethical dimension (be transparent, cite AI output), plus "attempt first, never copy-paste, cite explicitly" rules for code help. All materials are reusable under CC licences.
- **Use in course:** Lift the AI-policy wording for session 1 and reuse the GitHub-classroom lab structure. Free.

### Andrew Heiss's AI/LLM policy for writing and coding courses
- **Source:** Andrew Heiss (Georgia State University), 2024 onward, course policy page
- **Link:** https://www.andrewheiss.com/ai/ (course sites at https://classes.andrewheiss.com/)
- **Why it matters:** A widely copied two-rule policy for R-based data courses: everything human-facing must be human-generated, and the student is responsible for understanding, verifying and citing everything an LLM produces. Written in plain language students actually read, with separate sections for writing and for code.
- **Use in course:** Adapt the two rules for the session 1 code-of-conduct discussion. Free. (Confirmed via search results; direct fetch blocked.)

### UC San Diego CS1-LLM course (Porter and Zingaro model)
- **Source:** Leo Porter and colleagues, UC San Diego, 2023 onward, course and institutional roll-out
- **Link:** https://www.microsoft.com/en/customers/story/26539-university-of-california-san-diego-github-copilot (paper: https://doi.org/10.1145/3649217.3653584; ACM TechTalk by the authors: https://learning.acm.org/techtalks/llmprogramming)
- **Why it matters:** The CS1-LLM course redesigned introductory programming around Copilot for a largely non-CS cohort, with assessment built on problem decomposition, testing and explaining code. The Microsoft case study and the authors' talk describe the institutional mechanics (licences, labs, grading).
- **Use in course:** Background; the TechTalk is a good 45-minute instructor primer. Free.

### Harvard CS50 with the CS50 Duck (cs50.ai)
- **Source:** David J. Malan and CS50 team, Harvard, 2023 onward, course and tool
- **Link:** https://cs50.readthedocs.io/cs50.ai/ (paper: https://doi.org/10.1145/3626252.3630938)
- **Why it matters:** A production example of a pedagogically constrained assistant: the Duck explains errors and code and gives hints but refuses to hand over solutions, available in VS Code and on the web. Shows that "AI on, answers off" is feasible at scale.
- **Use in course:** Model for a system prompt students use with Positron Assistant or Claude in early labs ("act as the CS50 Duck"). Free for CS50 learners; docs public.

### Wharton Generative AI Labs: Prompt Library and "Assigning AI" / "Instructors as Innovators"
- **Source:** Ethan Mollick and Lilach Mollick, Wharton, 2023 to 2025, teaching resources and working papers
- **Link:** https://gail.wharton.upenn.edu/prompt-library/ (papers: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4475995 and https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802463)
- **Why it matters:** Ready-to-use, tested prompts for tutor, coach, simulator and team-mate roles, plus two papers that explain seven ways to assign AI to students and how instructors can build their own exercises. The simulation and "AI as student" prompts translate well to analytics (e.g. have the model critique a regression interpretation).
- **Use in course:** Sessions 3 to 5: give students the "AI tutor" and "AI critic" prompts for reviewing their own analyses. Free.

### Solve It With Code (answer.ai / fast.ai)
- **Source:** Jeremy Howard and Johno Whitaker, answer.ai, 2024 onward (platform "Solveit" launched October 2025), live online course
- **Link:** https://si.answer.ai/course_info (launch posts: https://www.answer.ai/posts/2024-11-07-solveit.html and https://www.answer.ai/posts/2025-10-01-solveit-full.html)
- **Why it matters:** A five-week course for people who have generated code with ChatGPT or Claude but cannot modify it: tiny iterative steps, AI "in small doses", understanding before generating. The most explicit anti-vibe-coding pedagogy available, aimed at exactly this course's audience.
- **Use in course:** Instructor background; the "small steps, always run and inspect" discipline is a good lab norm from session 2. Paid course (about USD 400 to 500; check), posts free.

### AI Python for Beginners
- **Source:** Andrew Ng, DeepLearning.AI, 2024, short online course (four parts, about 11 hours)
- **Link:** https://www.deeplearning.ai/courses/ai-python-for-beginners
- **Why it matters:** Teaches Python from zero with an AI chatbot companion built into the lessons, explicitly designed for people who will code with AI help. Lightweight, free, and a sensible pre-course assignment for students with no programming background.
- **Use in course:** Pre-course or session 1 homework (parts 1 and 2). Free (certificate paid on Coursera).

### Posit Academy and posit::conf workshop materials
- **Source:** Posit PBC, 2022 onward, mentor-led cohort programme (paid) and open workshop repositories
- **Link:** https://posit.co/products/enterprise/academy (free workshop example: https://posit-conf-2023.github.io/workshops/workshops/intro-ds-python/)
- **Why it matters:** Posit's own teaching model for Python and R data science (daily lessons, weekly projects, live mentor sessions) and the open posit::conf workshop repos that show how Posit staff teach pandas and Quarto in their tools. Closest to a "Positron-native" curriculum, though Academy itself is for teams.
- **Use in course:** Background; borrow lab structure and the intro-ds-python repo exercises for sessions 2 to 3. Academy paid; workshop repos free.

### Copilot(s): Generative AI at Microsoft and GitHub (HBS case 624-010)
- **Source:** Frank Nagle, Shane Greenstein, Maria P. Roche, Nataliya Langburd Wright and Sarah Mehta, Harvard Business School, 2023 (teaching note revised 2024), case
- **Link:** https://store.hbr.org/product/copilot-s-generative-ai-at-microsoft-and-github/624010 (also https://www.thecasecentre.org/products/view?id=197525)
- **Why it matters:** A classic teaching case on the launch decisions for GitHub Copilot (timing, targeting, pricing, code ownership, developer reception). Lets marketing students discuss the tool they are using as a product and a market, not only as a utility.
- **Use in course:** Session 4 or 5 case discussion (60 minutes); ties AI-assisted coding to go-to-market and pricing. Paid (about USD 9 per student via HBP Education, with a free educator copy).

## Gaps and caveats

The Consensus academic search tool had exhausted its monthly quota, so the journal section was built with web search and publisher pages rather than a systematic literature query; coverage of 2026 papers is therefore thinner than of 2023 to 2025. Direct fetching was blocked by the network proxy for nearly every domain (wu.ac.at, hbs.edu, doi.org, arxiv.org, github.io, unesco.org and others), so links were confirmed by their appearance in search results from publisher or repository pages, not by loading them; two are flagged "(unverified)" (the UNESDOC record and the Universität Wien 2nd-edition DOI). WU Vienna's AI pages were confirmed to exist and their key rules were visible in search snippets, but the full current wording should be re-read on wu.ac.at before it is quoted in the syllabus. Several ACM, SAGE, Wiley and INFORMS articles are paywalled; open author versions are listed where found. Posit's assistant line-up is moving quickly (Databot deprecated in Positron 2026.07, Positron Assistant being superseded by Posit Assistant), so course examples here describe assistants generically; the tool-specific details belong to the tooling part of this guide. No published business-school syllabus was found that uses Positron by name; the USC Marshall course (RStudio plus Copilot) and the Duke STA 199 course (Posit tools, Quarto, GitHub) are the closest documented designs. The "Vibe Coding" book and the METR study are both from late 2025 and have attracted criticism; they are included as debate material rather than settled evidence.
