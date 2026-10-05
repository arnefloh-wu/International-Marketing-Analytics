### Software (18)
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
		<td>Positron IDE (current release 2026.09.1-2, 4 September 2026)</td>
		<td>Posit PBC, 2024-2026, software (desktop IDE; Elastic License 2.0, source-available, free for personal, academic and commercial use)</td>
		<td>[https://positron.posit.co/](https://positron.posit.co/)</td>
		<td>Fork of VS Code (Code OSS) with first-class Python and R, Data Explorer, Variables pane, Plots pane, Connections pane, native Quarto and a Jupyter notebook editor (GA since 2026.07.0, 6 July 2026). Monthly date-stamped releases (there is no "1.0"; GA was declared with 2025.08.0 in August 2025). macOS, Windows and Linux. Only restriction: you may not host it as a service for third parties without P</td>
		<td>session 1 (install, tour, first Quarto document); free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Posit Assistant (in Positron 2026.07+, RStudio 2026.04+, terminal TUI)</td>
		<td>Posit PBC, 2026, software (AI coding agent for data science; preview from Positron 2026.04.0, default since 2026.07; Posit AI Pass GA April 2026)</td>
		<td>[https://positron.posit.co/assistant.html](https://positron.posit.co/assistant.html)</td>
		<td>The agent sees the live Python or R session (data frames, variables, plots, console history), runs code, has plan mode, skills, MCP servers, an \`AGENTS.md\` memory file and three permission modes. Bring your own key: providers listed on the getting-started page are Posit AI Pass, Anthropic, OpenAI, GitHub Copilot (preview), Amazon Bedrock, Microsoft Foundry, Snowflake Cortex, Databricks, DeepSeek,</td>
		<td>sessions 1-5 (the default assistant for labs); students need either a Posit AI Pass, an Anthropic API key or a Copilot account.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Positron Assistant (legacy, June 2025 to June 2026)</td>
		<td>Posit PBC, 2025, software (deprecated from Positron 2026.07)</td>
		<td>[https://github.com/posit-dev/positron/discussions/7931](https://github.com/posit-dev/positron/discussions/7931)</td>
		<td>The announcement thread (3 June 2025, Tom Mock) documents the original design: Anthropic Claude for chat via API key only (no Claude Pro OAuth, see discussion #10418), GitHub Copilot for completions, ask / edit / agent modes, and early user complaints about token cost. Useful for reading older blog posts and videos correctly.</td>
		<td>background only (do not install; the replacement is built in).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Databot (legacy exploratory data analysis agent)</td>
		<td>Posit PBC (Joe Cheng), 2025, software (deprecated from Positron 2026.07, folded into Posit Assistant)</td>
		<td>[https://positron.posit.co/databot.html](https://positron.posit.co/databot.html)</td>
		<td>Short-turn EDA loop (question, code, run, show output, suggest next question) that is the design ancestor of Posit Assistant's iterative data exploration; the "A brief and biased history" post below explains the lineage.</td>
		<td>background (explains why Posit Assistant explores data step by step instead of writing whole scripts).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>GitHub Copilot in Positron</td>
		<td>GitHub / Posit, 2025-2026, software (completions, Next Edit Suggestions and chat provider inside Posit Assistant; status "Preview")</td>
		<td>[https://positron.posit.co/assistant-completions.html](https://positron.posit.co/assistant-completions.html)</td>
		<td>Sign in via the Accounts menu; ghost-text completions in Python, R and Quarto, and Copilot can be selected as the chat model provider so students with a Copilot account avoid paying for API credits. Copilot Free gives 2,000 completions a month; the GitHub Student Developer Pack's free Copilot Student plan paused new sign-ups in April 2026 and reopened gradually from 17 June 2026 (check current sta</td>
		<td>session 1 set-up; the cheapest route for students who have a GitHub Education account.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Claude Code in the Positron terminal</td>
		<td>Anthropic, 2025-2026, software (terminal agent; requires Claude Pro/Max or API billing)</td>
		<td>[https://opensource.posit.co/blog/2026-06-08_comparing-posit-assistant-and-claude-code/](https://opensource.posit.co/blog/2026-06-08_comparing-posit-assistant-and-claude-code/)</td>
		<td>Runs unchanged in Positron's integrated terminal, and the Claude Code VS Code extension also installs in Positron (Sharon Machlis, October 2025). Posit's own comparison (8 June 2026) is honest: Claude Code edits files and runs scripts but cannot see the live session unless you add the \`btw\` package's MCP server, whereas Posit Assistant has session access built in. Issue #13603 (May 2026, milestone</td>
		<td>sessions 3-5 for students who already have Claude Pro; good for the "agent writes the whole pipeline" versus "assistant explores with me" contrast.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>OpenAI Codex CLI</td>
		<td>OpenAI, 2025-2026, software (open-source terminal agent, Apache 2.0, released 16 April 2025; IDE extension for VS Code forks)</td>
		<td>[https://github.com/openai/codex](https://github.com/openai/codex)</td>
		<td>The OpenAI equivalent of Claude Code; sandboxed command execution with suggest / auto-edit / full-auto approval modes. Works in Positron's terminal like any CLI. Needs a ChatGPT Plus/Pro or API account.</td>
		<td>background (mention as an alternative; do not support it in labs).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Posit AI Pass</td>
		<td>Posit PBC, 2026, software/subscription (invite-only beta January 2026, early release March 2026, GA April 2026; "Posit AI is Now Available to All", 5 May 2026)</td>
		<td>[https://posit.ai/](https://posit.ai/)</td>
		<td>The one-login route to Posit Assistant and Next Edit Suggestions with a monthly credit allowance; the FAQ is the clearest statement of what leaves the machine (prompts, session info, variable names and types, schema via tool calls, row-level data only if you ask for it) and of zero-data-retention agreements with model providers.</td>
		<td>session 1 and the course AI policy (privacy paragraph); USD 20/month, free trial without card.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>ellmer (R) and chatlas (Python)</td>
		<td>Posit PBC (Hadley Wickham; Carson Sievert), 2024-2026, software (ellmer 0.5.0 on CRAN 4 September 2026; chatlas on PyPI)</td>
		<td>[https://ellmer.tidyverse.org/](https://ellmer.tidyverse.org/)</td>
		<td>Identical interfaces for calling LLMs from code (OpenAI, Anthropic, Gemini, Bedrock, Azure, Ollama and more), with tool calling and structured data extraction into typed objects. This is the "use an LLM inside your analysis" layer (for example classifying open-ended survey answers), distinct from the assistant that writes your code.</td>
		<td>session 4 or 5 (optional lab: LLM-coded text data in a marketing dataset); API cost only.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Visual Studio Code with the Python Data Science extension pack and Copilot</td>
		<td>Microsoft, 2024-2026, software (free; Python, Jupyter, Data Wrangler, Copilot)</td>
		<td>[https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler)</td>
		<td>The mainstream comparison point. Data Wrangler gives a Data-Explorer-like grid with Copilot-generated pandas code; Copilot Chat has an agent mode. What it lacks is Positron's language-aware console, Variables pane and R support. Positron's own migration guide (https://positron.posit.co/migrate-vscode.html) lists the differences.</td>
		<td>background (why the course chose Positron); free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>JupyterLab 4.6 with Jupyter AI 3.x</td>
		<td>Project Jupyter, 2026, software (open source; Jupyter AI 3.0 released 31 March 2026)</td>
		<td>[https://jupyter-ai.readthedocs.io/](https://jupyter-ai.readthedocs.io/)</td>
		<td>Jupyter AI 3 stopped building its own agent and instead hosts Claude Code, Codex, Gemini and others via the Agent Client Protocol inside JupyterLab, with multi-user chats saved as files. Relevant if the school's JupyterHub is the only sanctioned platform; note Positron Server can also be launched from JupyterHub (see Real-world examples).</td>
		<td>background; free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Cursor</td>
		<td>Anysphere, 2023-2026, software (VS Code fork with built-in agent; Hobby free, Pro USD 20/month)</td>
		<td>[https://cursor.com/](https://cursor.com/)</td>
		<td>The most-used "AI-native" editor among software developers, but no data science panes and no R. The free one-year student Pro offer closed to new sign-ups on 25 June 2026; students now get the Hobby tier only.</td>
		<td>background (useful for the "vibe coding" discussion: a tool built for shipping code, not for understanding data).</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>RStudio 2026.04+ with Posit Assistant, ellmer and chattr</td>
		<td>Posit PBC, 2026, software (open source IDE; Posit Assistant private beta January 2026, public 5 March 2026)</td>
		<td>[https://docs.posit.co/ide/user/ide/guide/tools/posit-ai.html](https://docs.posit.co/ide/user/ide/guide/tools/posit-ai.html)</td>
		<td>The same assistant now lives in RStudio, so R-side colleagues are not left behind; chattr (Shiny gadget for prompting from RStudio) and ellmer remain the package-level routes. Confirms that Positron is not a forced migration for R users.</td>
		<td>background; free.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Google Colab with Gemini Data Science Agent</td>
		<td>Google, 2025-2026, software (free tier for users 18+ in supported countries; Pro from USD 9.99/month)</td>
		<td>[https://colab.research.google.com/](https://colab.research.google.com/)</td>
		<td>Describe an analysis in the Gemini side panel and it generates a complete notebook (launched March 2025). Zero install, which is tempting for a first-session fallback, but no local files, no Quarto, no Git integration and session time-outs on the free tier.</td>
		<td>background / emergency fallback only.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Deepnote</td>
		<td>Deepnote, 2020-2026, software (cloud notebook; free Education plan for verified students and teachers)</td>
		<td>[https://deepnote.com/docs/edu-verification](https://deepnote.com/docs/edu-verification)</td>
		<td>Collaborative notebook with SQL, Python and R blocks and a Deepnote Agent that is aware of the workspace; the free Education plan excludes Deepnote AI, so the AI angle costs money. Good illustration of the "AI in a hosted notebook" model versus Positron's local IDE.</td>
		<td>background.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Posit Cloud with Positron (preview)</td>
		<td>Posit PBC, 2026, software (hosted; Free plan 25 project hours/month, Student plan USD 5/month with 75 hours)</td>
		<td>[https://posit.co/blog/positron-now-available-posit-cloud-preview](https://posit.co/blog/positron-now-available-posit-cloud-preview)</td>
		<td>Browser-based Positron so nobody loses the first session to laptop troubleshooting; every plan including Free can open Positron. Posit Cloud does not bundle AI, but a student with their own Posit AI Pass can sign in inside the session (relevant for exam rules, see the forum thread under Real-world examples).</td>
		<td>session 1 fallback for students with locked-down laptops.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Positron Server on JupyterHub and Positron Pro on Posit Workbench (institutional)</td>
		<td>Posit PBC, 2026, software (free 12-month education licence for qualifying institutions; \`jupyter-positron-server\` on PyPI)</td>
		<td>[https://positron.posit.co/education.html](https://positron.posit.co/education.html)</td>
		<td>If WU already runs JupyterHub, Positron can be added as a launcher next to JupyterLab with a free education licence (request via academic-licenses@posit.co); Workbench 2026.04.0 adds Posit Assistant with institution-controlled BYOK providers. This is the route to a uniform, admin-controlled AI set-up for 30 students.</td>
		<td>background / infrastructure decision before session 1.</td>
		<td>neu; Link geprüft</td>
	</tr>
	<tr>
		<td>Software</td>
		<td>Student pricing summary (as of October 2026)</td>
		<td>compiled from vendor pages, 2026, software/pricing</td>
		<td>[https://education.github.com/pack](https://education.github.com/pack)</td>
		<td>Cheapest working combination for a student: Positron (free) + GitHub Education (Copilot Student plan when open, otherwise Copilot Free) as the Posit Assistant provider. Alternatives: Posit AI Pass USD 20/month (USD 5 first month); Anthropic API pay-as-you-go (an Anthropic console key; Claude Pro does not work in Posit Assistant but does power Claude Code in the terminal); Claude for Education is i</td>
		<td>session 1 and the syllabus "tools and costs" paragraph. Verify GitHub Copilot Student availability the week before term; it has been paused and reopened once already in 2026.</td>
		<td>neu; Link geprüft</td>
	</tr>
</table>