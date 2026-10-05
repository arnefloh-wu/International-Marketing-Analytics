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
