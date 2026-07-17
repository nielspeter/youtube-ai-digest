---
title: "Anthropic Just Dropped Ultra Plan for Claude Code"
channel: "Ray Amjad"
video_id: UNhA17l6CWw
url: https://www.youtube.com/watch?v=UNhA17l6CWw
published: 2026-04-06T02:02:07+00:00
generated: 2026-07-17T19:31:19+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/UNhA17l6CWw/hqdefault.jpg
---
# Anthropic Just Dropped Ultra Plan for Claude Code

[![Anthropic Just Dropped Ultra Plan for Claude Code](https://i.ytimg.com/vi/UNhA17l6CWw/hqdefault.jpg)](https://www.youtube.com/watch?v=UNhA17l6CWw)

[Watch on YouTube](https://www.youtube.com/watch?v=UNhA17l6CWw) · **Ray Amjad** · 2026-04-06

## TL;DR
Anthropic released a new Claude Code feature called Ultra Plan, triggered via `/ultraplan`, which hands off planning to a web-based UI where users can review, comment on, and approve plans before implementation. After extensive testing, the creator discovered that Ultra Plan is actually an A/B/C test of three different planning modes—simple, visual, and deep (multi-agent with critique)—assigned server-side, meaning users never know which variant they're getting.

## Key Takeaways
- Ultra Plan is triggered with `/ultraplan` in Claude Code, which offloads planning to a cloud-based web UI for review and approval.
- The web UI offers a nicer experience with inline comments, thumbs-up feedback, ASCII/Mermaid diagrams, and the ability to approve or teleport back to the terminal.
- Ultra Plan ran up to 2x faster than local planning across 10 test comparisons.
- Three hidden planning modes exist: simple plan, visual plan (adds diagrams), and deep plan (multi-agent with critique pass).
- The deep plan uses multiple subagents: one to understand code/architecture, one to find files needing modification, one to identify risks/edge cases, and one to review the plan for gaps.
- Anthropic uses remote config to assign users a planning variant server-side—users have no control over which mode they receive.
- Ultra Plan showed better blast-radius auditing for dependency upgrades (e.g., tRPC v10→v11), but was no better than local planning for simpler model swaps (e.g., Qwen 3.5 → Gemma 4).
- The creator believes Ultra Plan is essentially an A/B/C test to determine the best planning system prompt, with potential for testing unreleased models in the future.
- The creator plans to extract the deep plan prompt and use it as a custom skill instead of relying on Ultra Plan's random assignment.
- Ultra Plan is useful for multitasking—multiple plans can be spun up and reviewed in the web UI without polluting the main conversation.

## Detailed Breakdown

**[00:00] – Introducing Ultra Plan and How to Trigger It**
The video opens with the introduction of Ultra Plan, a new planning mode in Claude Code. It is triggered by typing `/ultraplan` followed by a prompt. The creator demonstrates with a real task: upgrading from Qwen 3.5 to Gemma 4 in a macOS application called HypoWhisperer. After pressing enter, Claude Code indicates it will run Ultra Plan on the cloud and provides a session URL.

**[01:03] – The Ultra Plan Web UI Experience**
Clicking the session URL opens a web version of Claude Code where the plan is displayed in a polished UI. Users can highlight sections, leave thumbs-up reactions, and add inline comments (e.g., "use the recommended sampling parameters"). Comments can be sent back to Claude to refine the plan. Users can then approve the plan and start coding in the cloud, or teleport back to the terminal. The creator notes that Ultra Plan is noticeably faster—up to 2x faster than local planning—and sometimes includes ASCII or Mermaid diagrams, though not consistently.

**[02:08] – Teleporting Back and Implementation Options**
Once the Ultra Plan is ready, the terminal displays options: stop the plan, go back, or review in the web UI. After approving in the web UI, the plan is sent back to the terminal, where the user can implement it in the current session or start a new one. The creator also notes that local plans have a "Refine with Ultra Plan" option, which transports the local plan to the web for a cloud-based validation step.

**[02:42] – Comparing Ultra Plan vs. Local Plan: Testing Methodology**
The creator ran 10 Ultra Plans and 10 local plans for identical prompts to compare quality. Differences were inconsistent. For dependency upgrades (e.g., tRPC v10→v11), Ultra Plan did a better job auditing the blast radius and flagging risks. The local plan assumed build commands would catch issues. However, for simpler tasks like swapping local models (Qwen 3.5 → Gemma 4), Ultra Plan offered no quality improvement—only a nicer review UI.

**[04:18] – Investigating the Binary: Three Hidden Planning Modes**
Curious about the inconsistency, the creator had Claude Code inspect the binary's readable strings and discovered three planning modes: simple plan, visual plan (adds ASCII/Mermaid diagrams), and deep plan (multi-agent with critique). The deep plan uses multiple subagents: one to understand relevant code and architecture, one to find files needing modification, one to identify risks/edge cases/dependencies, and one to review the plan for missing steps and mitigations.

**[05:22] – Server-Side A/B/C Testing and the Remote Config**
Anthropic uses a remote config to assign users to one of the three planning modes—entirely server-controlled. The creator realized that good plans came from being assigned "variant free" (the deep plan), while mediocre plans came from the simple or visual modes. The creator concludes that Ultra Plan is effectively an A/B/C test to measure acceptance rates of each variant and determine the best planning prompt. This infrastructure could also be used to test unreleased models for planning quality.

**[06:27] – Practical Verdict and Custom Skill Alternative**
The creator shares final takeaways: Ultra Plan is consistently faster and better for multitasking, as multiple plans can be spun up and reviewed in the web UI without polluting the main conversation. It's also handy for quick prototyping—plans can be discarded easily. However, due to the unpredictable variant assignment, the creator plans to avoid Ultra Plan and instead use the deep plan prompt directly as a custom skill. The video closes with a plug for the creator's Claude Code masterclass and newsletter.

## Notable Quotes
- "Despite the name, like Ultra being the name, you may actually be underwhelmed when using this new feature."
- "Ultra plan seemed to do a better job at auditing the blast radius and then flagging any risks compared to the local plan instead."
- "Essentially what Anthropic are doing behind the scenes is that they're using a remote config to decide which Ultra Plan mode that you will be sent to. And this is entirely server controlled, the user never actually picks this."
- "This whole ultra planning thing is like an A/B/C test for us to figure out which system prompt they should be using going forwards for planning."
- "I will stay away from Ultraplanning for now and just use the free ServAgents with a critique as a custom skill instead."

## People, Tools & References Mentioned
- **Claude Code** – Anthropic's terminal-based AI coding tool
- **Ultra Plan** – New cloud-based planning mode in Claude Code
- **HypoWhisperer** – The creator's macOS application used as a test case
- **Qwen 3.5 / Gemma 4** – Local AI models referenced in the upgrade test prompt
- **tRPC (v10 → v11)** – Dependency migration used to compare planning quality
- **Mermaid / ASCII diagrams** – Visual outputs sometimes included in plans
- **Claude Code Web** – Cloud-based UI for reviewing Ultra Plans
- **Ray Amjad's Claude Code Masterclass & Newsletter** – Creator's paid course and free newsletter

## Who Should Watch
Developers and power users of Claude Code who want to understand what Ultra Plan actually does under the hood and whether it's worth using over local planning. The video is especially valuable for those interested in Anthropic's A/B testing infrastructure and anyone looking to extract the deep plan prompt for custom use.


<details class="transcript">
<summary>Full transcript</summary>

<p>Okay, so we have a brand new planning mode inside of Claude Code known as Ultra Plan. And I&#x27;ll be going through that in this video as well as my own thoughts about this because despite the name, like Ultra being the name, you may actually be underwhelmed when using this new feature. Now essentially, if you go to Claude Code and then you do /ultraplan, then you can give it a prompt. So for my application HypoWhisperer, I basically want to upgrade Qwen 3.5 to Gemma 4 instead for the local model. So if I give it that prompt, can you upgrade Qwen 3.5 to Gemma 4 for the local</p>
<p>model in the macOS application? And then pressing enter, it will say that it will run Ultra plan on the cloud, press enter, and then it will give you a session URL so you can like watch it planning and then actually respond to the plan that it gave you. So clicking on this URL over here, it should then take you to the Claude Code web like version. And then you&#x27;ll see that the Ultra plan is in action. Now I actually made 10 Ultra Plans yesterday. So I ran this prompt before and I ran 10 different prompts for a local planning mode and 10 different prompts for Ultra Plan mode.</p>
<p>Now when the Ultra Plan is presented to you, you will see that it looks kind of like this. So they have a nice UI over here and you can select things over here and like leave a thumbs up, like emoji, smiling face. And you can leave comments in different areas over here. So like leaving a comment saying, use the recommended sampling parameters. And after reading through the plan, I could send these two comments back to Claude so I can adjust the plan on the cloud version. And I can press approve Claude&#x27;s plan and start coding on the cloud version or teleport back to the terminal instead. And you&#x27;ll actually notice two different things here.</p>
<p>Firstly, that Ultra plan is actually really fast on the cloud. So I noticed that it was up to 2 times faster than the local plan for the same prompt. And you&#x27;ll also notice that sometimes you get diagrams in your Ultra plan, kind of like this ASCII diagram or this Mermaid diagram over here, but other times you will not see any diagrams at all. And then on your terminal, once the Ultra plan is ready, you will see Ultra plan ready over here. Press down, press enter, and then you can stop the Ultra plan, go back, or review in Claude Code web. So reviewing the web version,</p>
<p>I could then press approve plan and teleport back to terminal. Now this will then send the plan back to the terminal, and then I can do implement here, like in this current session, or do start a brand new session for this plan. So starting a brand new session, it will then like move me over to that with the Ultra plan passed back in. So essentially the difference from the normal planning mode is that you use a trigger word, Ultra plan. It hands it off to a web version of Claude Code that research and drafts a plan. You can leave inline comments to the plan. And then once you&#x27;ve approved the plan to your liking, you can either run it in the cloud or teleport back to the local</p>
<p>session instead. And you will also notice that for other sessions, when you run the local plan, then you will see right over here and there&#x27;ll be another option that says no Refine with Ultra plan on Claude Code on the web. So pressing that, it will then transport your local plan to the web version and then it will do a validation step on the cloud. Okay, now the question that you probably have is that, is this Ultra plan actually better than the normal planning mode inside of Claude Code? Now yesterday I did like 10 different Ultra plans and 10 different local plans and then compared them for the same prompt. And I did notice some differences, but like I</p>
<p>couldn&#x27;t reliably get those differences. So some of the differences that I did notice is that for things that make small changes across the entire application, like updating a dependency, Ultra plan seemed to do a better job at auditing the blast radius and then flagging any risks compared to the local plan instead. Whereas the local plan just kind of assumed that any build step or build command would catch any things that missed. When upgrading a dependency. So in one particular case, I was migrating from tRPC version 10 to version 11, and the Ultra plan caught more potential</p>
<p>issues compared to the Local plan. But in other cases, removing Qwen 3.5 and using gemer4 instead, it seemed that the Ultra plan didn&#x27;t really have an impact and make the plan any better. So the only difference was that it basically presented a nicer UI for actually reviewing the plan and leaving comments at specific points. So as a short aside, I do also have a free Claude Code newsletter. So if you are interested in getting the latest from someone who is using Claude Code like 10 hours every single day, then I do share this in my newsletter. There will be a link down below if you&#x27;re interested, and signing up will give you access to a bunch of free videos</p>
<p>from my masterclass. So then I was wondering like, okay, why is Ultra Plan really good in some cases and like kind of mid or basically the same as a Local Plan in other cases? So I got Claude Code to do some digging through the binary readable strings over here, and essentially it discovered that there are 3 different planning modes inside of Ultra Plan. So there is the simple plan, the visual plan, and then free subagents with a critique plan. And this is the system prompt for each of the planning modes right over here. So the visual plan is basically the same as the</p>
<p>normal plan, but it just generates some ASCII diagrams and like Mermaid diagrams as well, which is why sometimes I notice the Ultra Planner mode like generating Mermaid diagrams kind of like this and other times not. And then this is the most interesting planning mode. So they call this the deep plan and it&#x27;s basically a multi-agent exploration with a critique pass. So they have one agent that understands relevant code and the existing architecture, another one to find all files that need modification, another one to identify potential risks, edge cases, and dependencies, and then another one to review the plan for missing steps, risks,</p>
<p>and mitigations over here. And essentially what Anthropic are doing behind the scenes is that they&#x27;re using a remote config to decide which Ultra Plan mode that you will be sent to. And this is entirely server controlled, the user never actually picks this. So I noticed that sometimes I was getting a really good plan because they assigned me variant free, which had the 3 different subagents with a critique. And other times I was getting a pretty mid plan, which was the same as a local plan. And ultimately what I think is happening here is that Anthropic want to measure how many people are accepting each variant and then deciding which planning mode,</p>
<p>planning prompt is better for users. So essentially this whole ultra planning thing is like an A/B/C test for us to figure out which system prompt they should be using going forwards for planning. But I think that this gives them the infrastructure to do other testing as well. So for example, for an upcoming model, they could use an upcoming unreleased model to generate either plan, and then they will measure how many people are accepting that plan to inform whether that prompt or that model is actually good for planning. So maybe with all this A/B testing that they&#x27;re doing with Ultraplan, they&#x27;ll get a better sense of how good planning works. But ultimately,</p>
<p>I want to know exactly which planning mode that I&#x27;m being assigned to. So I think that I will use the Ultraplan deep plan prompt directly as some kind of skill instead. So this will be down below for those of you who are interested in copying this, because just by reading through this prompt, it seems that this approach may actually be pretty good compared to the normal planning mode prompt. Anyways, that said, you will find that the Ultra Plan is actually faster. In all 10 versions that I ran, Ultra Plan finished about 2 times faster compared to the Local Plan for the same prompt. I think that it is better for multitasking as well, because you can spin up many</p>
<p>different Ultra Plans. From like your terminal and then review them all in like a nicer UI as well. And it can be quite handy for quick prototyping and iteration because you can fire off a change to the cloud version of Ultraplan and then see what that would look like. And then if the plan doesn&#x27;t look good, you can just discard it quite easily without polluting the rest of the conversation. Anyways, I think that I will stay away from Ultraplanning for now and just use the free ServAgents with a critique as a custom skill instead. Anyways, if you&#x27;re interested in diving much deeper into Claude Code, then I do have an entire masterclass about this which many people</p>
<p>from some of the world&#x27;s biggest companies have already taken. It is the first and the most comprehensive Claude Code class that you&#x27;ll find online. And there are many other ideas that are covered here that you will not find anywhere else on YouTube. I do update it every single day whenever a new feature is released or there&#x27;s a new technique that I discover. If you do have any questions about this, then you can email me using the email you can see on the screen right now.</p>

</details>
