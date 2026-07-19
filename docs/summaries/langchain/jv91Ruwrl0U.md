---
title: "Trace Every Codex Session in LangSmith in Minutes"
channel: "LangChain"
video_id: jv91Ruwrl0U
url: https://www.youtube.com/watch?v=jv91Ruwrl0U
published: 2026-07-14T13:19:06+00:00
generated: 2026-07-16T20:28:19+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/jv91Ruwrl0U/hqdefault.jpg
---
# Trace Every Codex Session in LangSmith in Minutes

[![Trace Every Codex Session in LangSmith in Minutes](https://i.ytimg.com/vi/jv91Ruwrl0U/hqdefault.jpg)](https://www.youtube.com/watch?v=jv91Ruwrl0U)

[Watch on YouTube](https://www.youtube.com/watch?v=jv91Ruwrl0U) · **LangChain** · 2026-07-14

## TL;DR
Amy from the LangChain Product team demonstrates how to trace Codex CLI sessions in LangSmith, capturing every turn, tool call, model metadata, and token usage as inspectable traces. With a couple of config blocks and an environment variable flag, developers can gain full visibility into Codex agent activity, including nested sub-agent hierarchies.

## Key Takeaways
- Codex CLI version 0.142 or later and a LangSmith API key are required to get started.
- A marketplace command pulls in the tracing plugin, but plugin hooks must be explicitly enabled in `~/.codex/config.toml`.
- Tracing is gated by an additional flag, `TRACE_TO_LANGSMITH`, which can be set via environment variables or config file.
- LangSmith traces capture the full accumulated conversation, assistant responses, model metadata, and token usage.
- Tool calls—function calls, shell calls, web searches, file reads—each appear with their actual inputs and outputs.
- Sub-agent invocations show up as nested children under parent turns, preserving the call hierarchy rather than flattening it.
- Traces land in a default project called "Codex" unless a custom project name is set via `LANGSMITH_CODEX_PROJECT`.
- Even cancelled runs still get uploaded once the session completes.
- Troubleshooting involves verifying `plugin_hooks = true`, the tracing plugin is enabled, `TRACE_TO_LANGSMITH = true`, and a valid API key.
- Similar tracing setups for Claude Code and Cursor are forthcoming.

## Detailed Breakdown
### Introduction and Prerequisites [00:00](https://www.youtube.com/watch?v=jv91Ruwrl0U&t=0s)
Amy introduces herself as part of the LangChain Product team and outlines the goal: wiring up Codex so that every session, turn, tool call, model metadata, and token usage lands in LangSmith as a real, inspectable trace. She notes the two prerequisites: Codex CLI version 0.142 or later and a LangSmith API key.

### Adding the Tracing Plugin via the Marketplace [00:35](https://www.youtube.com/watch?v=jv91Ruwrl0U&t=35s)
Amy runs a marketplace command from the Codex CLI that pulls in the tracing plugin. She explains that the plugin is not yet active—it still needs to be enabled. She opens her Codex config file at `~/.codex/config.toml` and adds two blocks (`features` and `plugins`) to turn the plugin on.

### Enabling Tracing with Environment Variables [01:15](https://www.youtube.com/watch?v=jv91Ruwrl0U&t=75s)
Even with the plugin enabled, tracing itself is gated by one more flag. Amy demonstrates setting this up via environment variables in her shell config. She adds three exports: `TRACE_TO_LANGSMITH`, `CODEX_API_KEY` (initially a placeholder), and `LANGSMITH_CODEX_PROJECT`. She then replaces the placeholder with her real API key.

### Running a Real Codex Task [01:50](https://www.youtube.com/watch?v=jv91Ruwrl0U&t=110s)
To exercise the tracing, Amy gives Codex a real task: look up the current top five trending GitHub repositories and build a small Python CLI tool that displays them nicely formatted in the terminal. The prompt also instructs Codex to set up the project structure, write the code, add a `requirements.txt` if needed, run the code, and fix anything that fails. This task is designed to trigger tool calls and web searches.

### Inspecting the Trace in LangSmith [02:58](https://www.youtube.com/watch?v=jv91Ruwrl0U&t=178s)
After the run completes, Amy navigates to LangSmith, where traces land in a default project called "Codex" unless a custom name was set. She walks through the trace: an LLM run shows the full accumulated conversation as input, the assistant's response as output, and metadata including model provider, model name, stop reason, and token usage. Below that, every tool call—function calls, shell calls, web searches, file reads—appears with its actual input and output. Sub-agent invocations show up as nested children under the parent turn, preserving the call hierarchy.

### Edge Cases and Troubleshooting [03:30](https://www.youtube.com/watch?v=jv91Ruwrl0U&t=210s)
Amy notes that even cancelled runs still get uploaded once the session completes. For cases where nothing shows up, she recommends checking that `plugin_hooks` is set to `true` and the tracing plugin is enabled in `config.toml`, confirming `TRACE_TO_LANGSMITH` is `true`, and verifying the API key is set and valid. If traces land in the wrong project, check the `LANGSMITH_CODEX_PROJECT` variable.

### Wrap-Up and What's Next [04:03](https://www.youtube.com/watch?v=jv91Ruwrl0U&t=243s)
Amy summarizes the setup: two config blocks and one flag turn every Codex session into a real trace with turns, tools, tokens, and sub-agents. She points to full docs linked below and mentions she is filming the same setup for other coding agents like Claude Code and Cursor, encouraging viewers to stay tuned.

## Notable Quotes
- "With two config blocks and one flag, every Codex session becomes a real trace with turns, tools, tokens, and sub-agents."
- "The hierarchy of who called what is preserved and not flattened into one long list."
- "Even if you cancel the run it should still get uploaded once the session completes."

## People, Tools & References Mentioned
- **Amy** — Presenter, LangChain Product team
- **Codex CLI** (version 0.142+) — The coding agent being traced
- **LangSmith** — Tracing and observability platform
- **`~/.codex/config.toml`** — Codex configuration file
- **Environment variables:** `TRACE_TO_LANGSMITH`, `CODEX_API_KEY`, `LANGSMITH_CODEX_PROJECT`
- **Claude Code, Cursor** — Other coding agents with similar tracing setups forthcoming
- **GitHub** — Used in the demo task (looking up trending repositories)

## Who Should Watch
Developers and AI engineers using the Codex CLI who want full observability into agent sessions—turns, tool calls, token usage, and sub-agent hierarchies—will find this a concise, practical guide to wiring up LangSmith tracing in minutes.


<details class="transcript">
<summary>Full transcript</summary>

<p>Hi, I&#x27;m Amy from the LangChain Product team, and today I&#x27;m going to show you how to trace Codex applications in LangSmith. In this video, I&#x27;ll wire up Codex, so every session along with turns, tool calls, model metadata, and token usage, all land in LangSmith as a real trace that you can inspect. To get started, you&#x27;ll need the Codex CLI with version 0.142 or later and a LangSmith API key. And so to get started, from the Codex CLI, we&#x27;re going to add the marketplace, which is essentially</p>
<p>this command. And then that should pull in the tracing plugin. But it&#x27;s not live yet. We still need to turn on plugin hooks that enable the plugin itself. And so what I&#x27;m doing here is I&#x27;m opening my Codex config file. It&#x27;s pretty much like ~/.codex/config.toml for every project. And then you add these two blocks, features and plugins. Okay, so that turns the plugin on</p>
<p>but tracing itself is still gated by one more flag. And you can either set it with environment variables or with a config file. And I&#x27;ll show you what it looks like to set it up with environment variables. And so here I&#x27;m going to add these to my shell config. And so I&#x27;m going to create like a new tab in my terminal and then add these three lines. Export TRACE_TO_LANGSMITH, export CODEX API_KEY, and export LANGSMITH_CODEX_PROJECT. Obviously this is a placeholder for my real API</p>
<p>key, but I&#x27;m going to go fill in my real API key now. So now let&#x27;s actually use it. I&#x27;m going to give Codex a real task that uses tool calls and web searches. Something like look up the current trending five repositories on GitHub right now and then build a small Python CLI tool that displays them nicely formatted in the terminal.</p>
<p>Set up the project structure, write the code, add a requirements.txt if needed, run them and then fix anything that fails. And so now we&#x27;re just going to let it run and see if we can trace it in LangSmith. Okay, so once that run finishes, I&#x27;m on LangSmith right now. And by default traces sort of land in a project, literally like called Codex unless you set your own name to it. And so as you can see in this latest trace, I get an LLM run and in this LLM run, I see</p>
<p>the full accumulated conversation as input, the assistant&#x27;s response as output, and metadata including model provider, model name, stop reason, token usage. And then below that you can see every tool call if there is one, like function calls, shell calls, web searches, file reads, each with its actual input and output. And if Codex kicks off a sub agent, it should show up as a nested child right under the parent turn. And so the hierarchy of who called what is preserved and not flattened into one long list.</p>
<p>And then, yeah, basically even if you cancel the run it should still get uploaded once the session completes. And so in the case that nothing shows up and your screen looks empty like this, I would check that plugin_hooks equals true and the tracing plugin is actually enabled in your config.toml file. And then also confirm that TRACE_TO_LANGSMITH equals true and that your API key is set and valid. If traces are landing in the wrong project, check LANGSMITH_CODEX_PROJECT.</p>
<p>And so there you go. With two config blocks and one flag, every Codex session becomes a real trace with turns, tools, tokens, and sub-agents. Full docs are linked below. I&#x27;m also filming the same setup for other coding agents like Claude Code and Cursor, so stay tuned for those videos. Thanks for watching.</p>

</details>
