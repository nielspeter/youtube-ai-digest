---
title: "Trace Every Cursor Agent Turn in LangSmith"
channel: "LangChain"
video_id: Ncv5TYdY7Tg
url: https://www.youtube.com/watch?v=Ncv5TYdY7Tg
published: 2026-07-21T15:16:53+00:00
generated: 2026-07-21T17:48:25+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/Ncv5TYdY7Tg/hqdefault.jpg
---
# Trace Every Cursor Agent Turn in LangSmith

[![Trace Every Cursor Agent Turn in LangSmith](https://i.ytimg.com/vi/Ncv5TYdY7Tg/hqdefault.jpg)](https://www.youtube.com/watch?v=Ncv5TYdY7Tg)

[Watch on YouTube](https://www.youtube.com/watch?v=Ncv5TYdY7Tg) · **LangChain** · 2026-07-21

## TL;DR
Amy from the LangChain product team demonstrates how to install and configure a LangSmith tracing plugin for Cursor, enabling every Cursor agent turn to appear as a full, structured trace in LangSmith. The setup involves adding a pre-compiled plugin repo, restarting Cursor, and setting a few environment variables—after which each agent run becomes inspectable with model calls, tool runs, sub-agent activity, and attachments all visible.

## Key Takeaways
- The LangSmith tracing plugin for Cursor is installed by pasting a repo URL into Cursor's Settings → Plugins → plugin link field.
- Cursor must be restarted after adding the plugin before tracing will work.
- Three environment variables control tracing: one to toggle tracing on, one for the LangSmith API key, and one for the product/project name (defaulting to "Cursor").
- Alternatively, a `cursor-langsmith.json` config file can be used instead of shell environment variables.
- Tailing the plugin's log file is a quick way to confirm the hook is live and active.
- Each Cursor agent turn shows up in LangSmith as its own trace with a consistent structure: model run (name, token usage, input/output) at the top, followed by tool runs (e.g., file reads, shell commands).
- Sub-agent activity appears as nested task runs with their own tool calls.
- Attachments such as images or files included in prompts are recovered from Cursor's local database and rendered directly on the user message in the trace.
- The traces share a common underlying structure with those from Claude Code and Codex, allowing all three agents to be compared within the same LangSmith workspace.
- The plugin uses a built-in Node.js module to pull attachments out of Cursor's local database.

## Detailed Breakdown

### Prerequisites and Plugin Installation [00:00](https://www.youtube.com/watch?v=Ncv5TYdY7Tg&t=0s)
Amy introduces herself as part of the LangChain product team and outlines the goal: by the end of the video, every Cursor agent turn should appear as a full trace in LangSmith. She lists the prerequisites—Cursor installed, Node.js (because the hook uses a built-in Node module to extract attachments from Cursor's local database), and a LangSmith API key. She then walks through the installation: open Cursor, go to Settings, then Plugins, paste a repo URL into the plugin link field, and confirm adding "LangSmith tracing for Cursor." She notes this is the easiest install method because the repo is a pre-compiled bundle. After confirming, Cursor must be restarted before proceeding.

### Environment Variables and Configuration [01:04](https://www.youtube.com/watch?v=Ncv5TYdY7Tg&t=64s)
Amy explains that three environment variables need to be set in the shell config: one to turn tracing on, one for the LangSmith API key for authentication, and one for the product name (which determines where traces land and defaults to "Cursor" if omitted). She mentions an alternative for users who prefer not to modify their shell: a `cursor-langsmith.json` config file supports the same fields. To verify the hook is live, she recommends tailing the log file with a specific command.

### Running the Agent and Viewing Traces [01:45](https://www.youtube.com/watch?v=Ncv5TYdY7Tg&t=105s)
Amy asks the Cursor agent to perform a task and explains that once it finishes, checking the log should reveal hook activity. She then navigates to LangSmith and opens the Cursor project, showing that each agent turn is its own trace. The structure is consistent every time: the model run appears at the top (including model name, token usage, and input/output), with tool runs such as file reads or shell commands underneath. If a sub-agent was invoked, it shows up as a nested task run with its own tool calls.

### Attachments and Cross-Agent Comparison [02:17](https://www.youtube.com/watch?v=Ncv5TYdY7Tg&t=137s)
Amy explains that if a prompt included an image or file, Cursor's local database retains that attachment. The plugin recovers it and renders it directly on the user message in the trace. She recaps the entire workflow: install the plugin, restart, set environment variables, and every agent turn becomes an inspectable trace. She notes that viewers who watched the Claude Code or Codex versions of the series will find the traces share a common underlying structure, enabling comparison of all three agents within the same LangSmith workspace. She closes by pointing to the linked documentation.

## Notable Quotes
- "By the end of this video, every Cursor agent turn you run should show up as a full trace in LangSmith."
- "This is the easiest way to install since the repo is a pre-compiled bundle that you can just add."
- "Each turn is its own trace, and it's structured the same way every time."
- "If your prompt included an image or file, Cursor's local database actually holds on to that attachment. And the plugin recovers it and renders it right on the user message."
- "The traces actually share a common structure under the hood, so you can compare all three agents in the same LangSmith workspace."

## People, Tools & References Mentioned
- **Amy** — Presenter, LangChain product team
- **Cursor** — AI code editor being traced
- **LangSmith** — LangChain's tracing and observability platform
- **Node.js** — Required because Cursor's hook uses a built-in Node module
- **Claude Code** — Another agent covered in the same tracing series
- **Codex** — Another agent covered in the same tracing series
- **cursor-langsmith.json** — Alternative config file for setting tracing options without modifying shell config

## Who Should Watch
Developers and AI engineers who use Cursor's agent mode and want deep observability into what the agent is doing—model calls, tool usage, sub-agent activity, and attachments—will find this video directly useful. It's also valuable for teams evaluating or comparing multiple coding agents (Cursor, Claude Code, Codex) side by side in a single LangSmith workspace.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=Ncv5TYdY7Tg&amp;t=0s">00:00</a></span> Hi, I&#x27;m Amy from the LangChain product team, and today I&#x27;m going to show you how to trace Cursor applications in LangSmith. By the end of this video, every Cursor agent turn you run should show up as a full trace in LangSmith. To get started, you&#x27;ll need Cursor installed as well as Node.js, since Cursor&#x27;s hooks use a built-in node module to pull attachments out of Cursor&#x27;s local database and a LangSmith API key. So first, open Cursor, go to settings, then plugins,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Ncv5TYdY7Tg&amp;t=32s">00:32</a></span> and then paste this repo URL into the plugin link field. Confirm adding LangSmith tracing for Cursor. This is the easiest way to install since the repo is a pre-compiled bundle that you can just add. Now restart Cursor before we move on. Great. Now we&#x27;re going to set a few environment variables in your shell config. And so I&#x27;m going to add these three lines.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Ncv5TYdY7Tg&amp;t=64s">01:04</a></span> Trace to LangSmith turns tracing on, the API key authenticates you, and the product name is where traces will land. It defaults the name Cursor if you skip it. And if you&#x27;d rather not touch your shell, there&#x27;s also a cursor-langsmith.json config file option with the same fields. And so what I like to do to confirm the hook is actually live is to tail the log file with this command. Now I&#x27;m going to ask the Cursor agent to perform a task.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Ncv5TYdY7Tg&amp;t=105s">01:45</a></span> Great. So that should start running and once it finishes, check the log, you should see hook activity. and then head to LangSmith and open the Cursor project. You can see here that each turn is its own trace, and it&#x27;s structured the same way every time. The model run at the top, then model name, token usage, input output, then any tool runs underneath like file reads or shell commands. And if a sub agent kicked in, it should show up as nested task run</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Ncv5TYdY7Tg&amp;t=137s">02:17</a></span> with its own tool calls. If your prompt included an image or file, Cursor&#x27;s local database actually holds on to that attachment. And the plugin recovers it and renders it right on the user message. And yeah, that&#x27;s how you set up LangSmith tracing on Cursor. So to recap all of this, install the plugin, restart, set the environment variables, and every agent turn becomes an inspectable trace. If you watch the Claude Code or Codex versions of the series, you&#x27;ll notice that the traces actually share a common structure</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Ncv5TYdY7Tg&amp;t=169s">02:49</a></span> under the hood. so you can compare all three agents in the same LangSmith workspace. Docs are linked below, and thanks for watching.</p>

</details>
