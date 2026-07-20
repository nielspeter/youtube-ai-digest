---
title: "Anthropic Just Dropped the Feature Nobody Knew They Needed"
channel: "Ray Amjad"
video_id: OnQ4BGN8B-s
url: https://www.youtube.com/watch?v=OnQ4BGN8B-s
published: 2026-03-24T08:57:59+00:00
generated: 2026-07-20T11:22:38+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/OnQ4BGN8B-s/hqdefault.jpg
---
# Anthropic Just Dropped the Feature Nobody Knew They Needed

[![Anthropic Just Dropped the Feature Nobody Knew They Needed](https://i.ytimg.com/vi/OnQ4BGN8B-s/hqdefault.jpg)](https://www.youtube.com/watch?v=OnQ4BGN8B-s)

[Watch on YouTube](https://www.youtube.com/watch?v=OnQ4BGN8B-s) · **Ray Amjad** · 2026-03-24

## TL;DR
Anthropic has quietly added an unannounced feature to Claude Code called "Auto Dream," which consolidates and cleans up the agent's auto-generated memories—mirroring how human REM sleep organizes short-term experiences into long-term memory. The feature reviews past session transcripts, removes stale/contradictory memories, and reorganizes the memory index, all while running in the background without disrupting active coding.

## Key Takeaways
- Auto Dream is a secret, unannounced Claude Code feature discovered by inspecting the binary and system prompts via a proxy.
- It addresses the problem of "memory bloat" from the existing Auto Memory feature, where accumulated memories become noisy and contradictory over many sessions.
- The feature is inspired by human REM sleep: consolidating what matters, deleting what doesn't, and organizing into long-term memory.
- It can be toggled on/off via the `/memory` command; the `/dream` command itself isn't fully rolled out yet but can be triggered by telling Claude Code to "dream" or "autodream."
- The dreaming process has four phases: Orientation, Gathering Signal, Consolidating, and Pruning & Indexing.
- It reviews locally stored JSONL session transcripts to find user feedback, corrections, important decisions, and recurring themes.
- The main `MEMORY.md` file is intended to serve as an index referencing other memory files, not to store memories directly.
- Auto Dream triggers only after 24 hours have passed AND more than five sessions have occurred since the last consolidation.
- It runs in read-only mode on project code but has write access to memory files; a lock file prevents concurrent dream instances.
- The background process doesn't block normal Claude Code usage while it runs.

## Detailed Breakdown

### Discovery of the Hidden Feature [00:00](https://www.youtube.com/watch?v=OnQ4BGN8B-s&t=0s)
While doing "vibe coding," the presenter noticed Claude Code displayed "improved six memories"—a message not mentioned in any changelog. After digging through the binary file and having Claude Code self-inspect, he discovered a secret, unannounced feature called Auto Dream.

### The Problem with Auto Memory [00:35](https://www.youtube.com/watch?v=OnQ4BGN8B-s&t=35s)
Claude Code's existing Auto Memory feature, added roughly two months ago, automatically writes notes to a `.claude/projects` memory folder based on corrections and preferences. However, over many sessions, memories accumulate noise and contradictions—by session 20, the memory is cluttered and degrades model performance. System prompt instructions to verify memory accuracy proved insufficient.

### Auto Dream: Inspired by Human Sleep [01:39](https://www.youtube.com/watch?v=OnQ4BGN8B-s&t=99s)
The new Auto Dream feature is accessible via `/memory`, where it shows "Auto-dream: on." The presenter draws a parallel to human REM sleep: the brain replays the day's events, strengthens important memories, discards irrelevant ones, and organizes everything into long-term memory. Until now, Claude Code was effectively "sleep-deprived," accumulating unfiltered short-term memories.

### Triggering and Watching the Dream Process [02:43](https://www.youtube.com/watch?v=OnQ4BGN8B-s&t=163s)
After enabling Auto Dream via `/memory`, the `/dream` command doesn't yet work for everyone, but simply telling Claude Code to "dream" or "autodream" triggers it. Using `/tasks`, the presenter shows the process in action: "Memory Consolidation, reviewing 913 sessions," searching for user feedback, corrections, important decisions, and recurring themes across session transcripts.

### The Four Phases Behind the Scenes [03:47](https://www.youtube.com/watch?v=OnQ4BGN8B-s&t=227s)
The presenter used a proxy to extract the exact system prompts, revealing four phases:
1. **Orientation** — reads the current memory directory to assess what exists and determine what to search for.
2. **Gathering Signal** — scans JSONL session transcripts stored locally to find relevant new information and identify drifted or stale memories.
3. **Consolidating** — merges new information into existing topics, converts relative dates like "today" or "yesterday" to exact dates, and resolves contradictions.
4. **Pruning and Indexing** — ensures the main `MEMORY.md` file serves as an index referencing other memory files rather than storing memories directly.

### Running Conditions and Safety Mechanisms [05:26](https://www.youtube.com/watch?v=OnQ4BGN8B-s&t=326s)
Auto Dream does not run constantly. It checks two conditions: at least 24 hours must have passed since the last consolidation, and more than five sessions must have occurred. It operates in read-only mode on project code (preventing accidental file changes) but has write access to memory files. A lock file prevents two instances from running simultaneously on the same project. The process doesn't block normal Claude Code usage.

### Results and Meta-Reflection [06:33](https://www.youtube.com/watch?v=OnQ4BGN8B-s&t=393s)
After 8–9 minutes, the consolidation completed, producing organized memory files: one about the user's role, one about recent project activity, the main index file, and an unchanged previous file. The presenter reflects on a broader trend: AI agents are increasingly modeled after human behavior and organizations—sub-agent teams interact like colleagues, and now agents "dream" like people to consolidate memories. He notes the feature is functional but unannounced, so changes may come.

## Notable Quotes
- "Until now, even though Claude Code had an auto-memory feature, it was kind of sleep-deprived, where it kept adding random things to memory that may have not been relevant."
- "It gathers all the memories together, and then figures out what is relevant, adds new things to the memories, and then deletes old, stale memories that are not relevant."
- "The main MEMORY.md file for your project should be an index referencing other types of memories rather than being the memories itself."
- "When making agents, we've kind of been modeling it after human behavior and human organizations: so sub-agent teams and sub-agents can interact with each other, kind of like an organization would. And now we have this whole idea of agents dreaming, kind of like people, to consolidate their memories."

## People, Tools & References Mentioned
- **Claude Code** — Anthropic's CLI coding agent; the central subject of the video
- **Anthropic** — the company behind Claude Code
- **Auto Memory** — Claude Code's existing memory feature (added ~2 months prior)
- **Auto Dream** — the newly discovered, unannounced memory consolidation feature
- **`.claude` folder / projects / memory folder** — local directory structure where memories are stored
- **`MEMORY.md`** — the main project memory index file
- **JSONL files** — locally stored session transcripts that Auto Dream scans
- **`/memory`, `/dream`, `/tasks` commands** — Claude Code commands referenced during the demo
- **REM sleep** — the biological process that inspired the feature's design
- **Ray Amjad's Claude Code newsletter and masterclass** — promoted resources at the end of the video

## Who Should Watch
Heavy Claude Code users and AI agent builders who want to understand the tool's evolving memory system and stay ahead of unannounced features. It's also valuable for anyone interested in the broader design philosophy of modeling AI agent behavior after human cognitive processes like sleep and memory consolidation.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=0s">00:00</a></span> Okay, so I was just doing some vibe coding and I noticed that Claude Code did something really weird that I had never seen before, whereby it randomly said improved six memories. And I was like, what is going on here? Because I follow the changelog pretty aggressively and there was no mention of anything like this anywhere recently. So I did some digging with Claude Code and I got it to look through the binary file and do some like self-inspection. And it turns out there&#x27;s a secret new feature that Anthropic added to Claude Code that they haven&#x27;t yet announced but is working. And that feature is essentially called Auto Dream. Now if you have been using Claude Code</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=35s">00:35</a></span> for a long time like me, then you probably ran into an issue whereby you would start a brand new session, and the agent just wouldn&#x27;t quite remember what you did yesterday. It didn&#x27;t really have a memory. And then the Claude Code team added something called Auto Memory about two months ago, whereby Claude could automatically write notes for itself based on your corrections and preferences. So you would have noticed this if you went to your .claude folder, went to projects, and in all your projects there would be a memory folder with memories about that particular project. And these memories would automatically be inserted into the context window whenever you&#x27;re working.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=68s">01:08</a></span> But then this introduced a brand new problem, whereby in Session 1 you would have a pretty fresh, clean, and relevant memory. And then as you go on, you would notice that Claude Code decides to add more and more stuff to its memory, and you get noise and contradictions and stuff like that. And then by Session 20, you notice your memory is just full of noise, has a bunch of contradictions, and it is kind of making the model perform worse. And Claude did have some instructions in the system prompt telling it to verify that the memory is still correct and up-to-date. But that didn&#x27;t really do a good job.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=99s">01:39</a></span> But then the Claude Code team added a brand new feature that they haven&#x27;t yet announced, called Auto Dream. So if you do /memory in your project, then you&#x27;ll notice it says Auto-dream: on over here, and you can turn this off and on. And then you can also open your project&#x27;s memory folder from here as well. And I think that by naming the feature, they were kind of inspired by humans. Because if you&#x27;re a human watching the video, not an AI agent, then throughout your day, your brain is taking in a lot of new information: conversations, decisions, things that you read. And all of this goes into a short-term memory. And if everything just stayed there in the short-term</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=132s">02:12</a></span> memory, you&#x27;d quickly become overwhelmed. But when you sleep, at least during REM sleep, your brain can replay the day&#x27;s events and consolidate them and strengthens what matters, and then also deletes what doesn&#x27;t matter and organizes everything into long-term memory. And that is the reason why people who don&#x27;t sleep enough literally can&#x27;t form long-term memories. Their short-term memory fills up, and then they start confusing things and making contradictory decisions. And until now, even though Claude Code had an auto-memory feature, it was kind of sleep-deprived, where it kept adding random things to memory that may have</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=163s">02:43</a></span> not been relevant. But now with this Auto Dream mode, essentially what Claude Code is doing is it gathers all the memories together, and then figures out what is relevant, adds new things to the memories, and then deletes old, stale memories that are not relevant. And you can see this in action by first enabling Auto-Dream by doing /memory and making sure that is on. And right now, the /dream command doesn&#x27;t work because it hasn&#x27;t officially been rolled out to everyone, this particular skill. But if you just kind of tell Claude Code like &quot;dream auto</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=194s">03:14</a></span> dream autodream&quot;, then you can see right here it started dreaming. So if I do /tasks, there I can see that dreaming in action. So you can see it says Memory Consolidation, reviewing 913 sessions. So it&#x27;s saying starting memory consolidation dream. Let me orient first. So maybe if you&#x27;re watching this later on, the /dream thing will actually work. Now you can see what it&#x27;s doing is it&#x27;s going through all the previous sessions. So it says, &quot;Let me gather recent signal from the transcripts. I&#x27;ll search for key patterns across the 913 sessions.&quot; So it&#x27;s searching for user</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=227s">03:47</a></span> feedback, corrections, important decisions, and recurring themes automatically in the background. So whilst we&#x27;re waiting for this to complete, I&#x27;ll quickly explain what&#x27;s happening behind the scenes. So we essentially have three different phases of this Auto Dreaming process. Phase 1: Orientation, which you can see that it&#x27;s currently doing, where it said, &quot;I will orient myself first.&quot; And essentially what it does is it reads through the current memory directory to kind of figure out, like, &quot;okay, what do we have so far?&quot; And then kind of figures out what it needs to be searching based on previous sessions. And then it starts to gather recent signal. So it starts to go through the session transcripts of all your</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=262s">04:22</a></span> previous Claude Code sessions, which are stored locally on your computer in these JSONL files. And it basically starts searching for all of them to try and find any relevant signal, new information, and identify drifted or stale memories that it can then remove. And then Phase 3 is the Consolidation phase, whereby it merges new information into existing topics. It writes any dates as well. So for example, if the memory says the words &quot;today&quot; or &quot;yesterday&quot;, then it would get the exact date, and it would remove and organize any contradictions.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=295s">04:55</a></span> And the reason I know that this is happening behind the scenes is because I used a proxy to extract the exact system prompts that are being used. And it kind of looks like this over here. So we have Phase 1: Orientation, Phase 2: Gathering Signal, Phase 3: Consolidating, and then we have one more phase called Pruning and Indexing. Because the main MEMORY.md file for your project should be an index referencing other types of memories rather than being the memories itself. Six minutes later, it&#x27;s still underway reviewing the memories. And do bear in</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=326s">05:26</a></span> mind that during this process, we can be using Claude Code normally, and it will be dreaming in the background. So this dreaming does not actually stop you from using Claude Code. Now, before continuing, if you spend all day in Claude Code like me, then you may want to sign up to my free Claude Code newsletter. I send it out every time I find something interesting in Claude Code, and signing up does give you access to a bunch of free videos covering ideas that you won&#x27;t find anywhere else on YouTube. Now, this Auto Dream feature does not run constantly behind the scenes. It checks two conditions. Firstly, has 24 hours passed since the last consolidation? And secondly, have more than</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=361s">06:01</a></span> five sessions happened since then? And you don&#x27;t have to worry about it accidentally making changes to your project&#x27;s files because it runs in a read-only mode when it comes to your project code, but has write access to the memory files themselves. And secondly, there is a lock file, which means that two instances of Auto Dream can&#x27;t run at the same time on the same project. Anyway, we can see that after about 8-9 minutes, it consolidated those memories behind the scenes. And then I can see the consolidated files here. So there&#x27;s one about me and my own role, there&#x27;s another one about any recent activity inside the project,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=393s">06:33</a></span> and then there&#x27;s the main index file, and then a previous file that didn&#x27;t need changing. Now, as a meta-point, what I&#x27;ve been finding interesting is that when making agents, we&#x27;ve kind of been modeling it after human behavior and human organizations: so sub-agent teams and sub-agents can interact with each other, kind of like an organization would. And now we have this whole idea of agents dreaming, kind of like people, to consolidate their memories. Now, it is worth bearing in mind that even though the feature is working inside of Claude Code, it hasn&#x27;t officially been announced, so they may make changes to it in some way. And finally,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=OnQ4BGN8B-s&amp;t=423s">07:03</a></span> if you want to learn to become a Claude Code power user, because this is increasingly the best tool to be using in 2026, then I do have a masterclass all about this. It is the most comprehensive and the first class all about Claude Code. Many people from some of the world&#x27;s biggest organizations have taken this and have gone on to be the best Claude Code users at their companies. So if you want to learn to master the most important tool of 2026, then there will be a link down below to sign up.</p>

</details>
