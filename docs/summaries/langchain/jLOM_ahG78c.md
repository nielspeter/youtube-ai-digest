---
title: "Trace Every Claude Code Session in LangSmith in Minutes"
channel: "LangChain"
video_id: jLOM_ahG78c
url: https://www.youtube.com/watch?v=jLOM_ahG78c
published: 2026-07-09T14:20:56+00:00
generated: 2026-07-16T21:16:34+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/jLOM_ahG78c/hqdefault.jpg
---
# Trace Every Claude Code Session in LangSmith in Minutes

[![Trace Every Claude Code Session in LangSmith in Minutes](https://i.ytimg.com/vi/jLOM_ahG78c/hqdefault.jpg)](https://www.youtube.com/watch?v=jLOM_ahG78c)

[Watch on YouTube](https://www.youtube.com/watch?v=jLOM_ahG78c) · **LangChain** · 2026-07-09

## TL;DR
Amy from the LangChain product team demonstrates how to integrate tracing for Claude Code applications into LangSmith using a marketplace plugin. With three CLI commands and a small JSON configuration file, developers can capture every message, tool call, token usage, and sub-agent run from their Claude Code sessions as debuggable traces in LangSmith.

## Key Takeaways
- Tracing Claude Code sessions in LangSmith requires the Claude Code CLI, Node.js, and a LangSmith API key.
- Installation involves adding a marketplace plugin and installing/reloading the tracing plugin via three simple commands.
- A project-level settings file (`.claude/settings.local.json`) controls tracing behavior with three key fields: `traceToLangSmith`, `CC-LangSmith-APIKey`, and `CC-LangSmith-Project`.
- Tracing can be toggled on or off by setting `traceToLangSmith` to `true` or `false`.
- Each user message appears as its own trace in LangSmith, containing the full picture of the interaction.
- A trace includes the user message, all tool calls, token usage, sub-agent runs, and the final response.
- The Threads tab in LangSmith groups every turn from the same Claude Code session together, enabling full conversation-level debugging.
- Upgrading the plugin later requires running `/plugin marketplace update LangSmith ClaudeCode` followed by `/reload plugins`.
- Troubleshooting primarily involves verifying the API key is correct.
- Similar tracing setups for Codex and Cursor are planned for future videos.

## Detailed Breakdown

### Introduction and Problem Statement [00:00](https://www.youtube.com/watch?v=jLOM_ahG78c&t=0s)
Amy introduces herself as a member of the LangChain product team and frames the core problem: developers building agents with Claude Code often encounter unexpected behavior with no visibility into why it happened. She notes that without tracing, it's difficult to determine which tool call triggered an issue or what a sub-agent actually returned. She promises to show how to trace every Claude Code session into LangSmith, capturing every message, tool call, and sub-agent run with minimal setup. She lists three prerequisites: the Claude Code CLI, Node.js, and a LangSmith API key (available from LangSmith settings).

### Plugin Installation [00:31](https://www.youtube.com/watch?v=jLOM_ahG78c&t=31s)
Amy walks through the installation process. Inside Claude Code, the user runs three commands: adding the marketplace plugin, installing the tracing plugin, and reloading plugins so Claude Code picks it up. She notes that for future upgrades, the process is similarly straightforward—run `/plugin marketplace update LangSmith ClaudeCode` followed by `/reload plugins` again.

### Configuration via Project Settings [01:01](https://www.youtube.com/watch?v=jLOM_ahG78c&t=61s)
The cleanest way to direct traces to LangSmith is through a project settings file. Amy instructs viewers to create `.claude/settings.local.json` in their project directory. This file contains three fields: `traceToLangSmith` (a boolean that turns tracing on or off for the project), `CC-LangSmith-APIKey` (your LangSmith API key), and `CC-LangSmith-Project` (the LangSmith project name under which traces will appear). Once configured, users simply interact with Claude Code as normal.

### Viewing Traces in LangSmith [01:38](https://www.youtube.com/watch?v=jLOM_ahG78c&t=98s)
Amy explains the LangSmith trace view. Every message sent to Claude Code shows up as its own individual trace. Inside each trace, users can see the user message, every tool call Claude makes, token usage, any sub-agent runs, and the final response. She then highlights the Threads tab, which groups every turn from the same Claude Code session under a single thread, allowing users to follow an entire conversation rather than just isolated messages.

### Wrap-Up and What's Next [02:09](https://www.youtube.com/watch?v=jLOM_ahG78c&t=129s)
Amy summarizes the entire setup as "three commands and one JSON block," after which every Claude Code session becomes a debuggable trace in LangSmith. She points viewers to pinned troubleshooting steps (primarily checking the API key) and a link to the full docs in the description. She closes by mentioning that she will film the same setup for Codex and Cursor in upcoming videos.

## Notable Quotes
- "If you are building agents with Claude Code, you've probably had a moment where your Claude Code agent did something unexpected and you had no way to see why."
- "Three commands and one JSON block, and now every Claude Code session is a debuggable trace in LangSmith."
- "Every message you send shows up as its own trace and inside it you get the full picture: the user message, every tool call Claude makes, token usage, and any sub agent runs, plus the final response."

## People, Tools & References Mentioned
- **Amy** — Presenter, LangChain product team member
- **Claude Code CLI** — Anthropic's command-line coding agent
- **LangSmith** — LangChain's tracing and observability platform
- **Node.js** — JavaScript runtime (prerequisite)
- **LangSmith Claude Code plugin** — Marketplace plugin enabling tracing
- **`.claude/settings.local.json`** — Project-level configuration file for tracing settings
- **Codex** — Mentioned as a future tracing setup target
- **Cursor** — Mentioned as a future tracing setup target

## Who Should Watch
Developers and AI engineers building agents with Claude Code who want full observability into their agent's behavior—tool calls, sub-agent runs, and token usage—will benefit most from this quick, practical setup walkthrough.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=jLOM_ahG78c&amp;t=0s">00:00</a></span> Hi, I&#x27;m Amy from the LangChain product team, and today I&#x27;m going to show you how to trace Claude Code applications in LangSmith. If you are building agents with Claude Code, you&#x27;ve probably had a moment where your Claude Code agent did something unexpected and you had no way to see why. Which tool call triggered it? What did the sub agent actually return? In this video, I&#x27;ll show you how to trace every Claude Code session straight into LangSmith, so you get a full trace of every message, tool call, and sub agent run in just a few minutes of setup. Three things you&#x27;ll need before we start.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jLOM_ahG78c&amp;t=31s">00:31</a></span> Make sure you have the Claude Code CLI installed, Node.js installed, and a LangSmith API key. You can grab that from your LangSmith settings if you don&#x27;t have one. And once you have those, we&#x27;re ready to go. First, open Claude Code and run these three commands and add the marketplace plugin. Then install the tracing plugin with this command and reload the plugin so that it picks it back up. And that&#x27;s it for installation.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jLOM_ahG78c&amp;t=61s">01:01</a></span> If you&#x27;re upgrading later, it&#x27;s just forward slash plugin marketplace update LangSmith Claude Code followed by forward slash reload plugins again. Now we tell the plugin where to send traces. The cleanest way is a project settings file. And so in your project directory, create dot claude slash settings dot local dot JSON. traceToLangSmith turns tracing on for this project. You can flip it to false anytime you want it to stop. CC-LangSmith-APIKey is your key and CC-LangSmith-Project is the project name traces will show up under</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jLOM_ahG78c&amp;t=98s">01:38</a></span> in LangSmith. Now just use Claude Code normally, ask it to do something and let it run. Once it responds, switch over to LangSmith. And so here&#x27;s how you view a trace on LangSmith. Every message you send shows up as its own trace and inside it you get the full picture. the user message, every tool call Claude makes, token usage, and any sub agent runs, plus the final response. And if you click over to the threads tab,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jLOM_ahG78c&amp;t=129s">02:09</a></span> every turn from the same Claude Code session is grouped under one thread. So you can follow a whole conversation, not just a single message. And that&#x27;s the whole setup. Three commands and one JSON block, and now every Claude Code session is a debuggable trace in LangSmith. If something breaks, check the pinned troubleshooting steps and double check that your API key is correct. Link to the full docs is below. I&#x27;ll also film the same setup for Codex and Cursor, so stay tuned for those videos.</p>

</details>
