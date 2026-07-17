---
title: "Claude Code Ultrareview Is Here: What You Need to Know"
channel: "Ray Amjad"
video_id: EhiJX0WvRz4
url: https://www.youtube.com/watch?v=EhiJX0WvRz4
published: 2026-04-09T11:03:54+00:00
generated: 2026-07-17T21:06:27+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/EhiJX0WvRz4/hqdefault.jpg
---
# Claude Code Ultrareview Is Here: What You Need to Know

[![Claude Code Ultrareview Is Here: What You Need to Know](https://i.ytimg.com/vi/EhiJX0WvRz4/hqdefault.jpg)](https://www.youtube.com/watch?v=EhiJX0WvRz4)

[Watch on YouTube](https://www.youtube.com/watch?v=EhiJX0WvRz4) · **Ray Amjad** · 2026-04-09

## TL;DR
Anthropic is developing a new "ultra review" feature for Claude Code that deploys multiple sub-agents to find, verify, and deduplicate bugs in large pull requests. The feature runs in the cloud, takes 10-20 minutes, and introduces a crucial verification step that filters out false positives—something the standard `/review` command lacks.

## Key Takeaways
- **Ultra review** is an upcoming Claude Code feature hidden under the codename "bug hunter" in the binary file.
- It is invoked via `/ultra review` and runs on the cloud version of Claude Code, taking roughly 10-20 minutes per review.
- The process has four stages: **setup**, **find**, **verify**, and **dedupe**.
- The finding stage spins up five independent sub-agents (default fleet size of 5, max 20), each likely using different personas and starting positions to uncover bugs.
- The verify stage independently checks each candidate bug to filter out false positives, preventing unnecessary code changes.
- The dedupe stage merges duplicate findings from multiple sub-agents into unique issues.
- Users on the $200/month plan get a limited number of free ultra reviews (the host saw three available).
- The standard `/review` command runs locally in 3-4 minutes, spins up sub-agents without a verification step, and acts more like a quick audit.
- Ultra review behaves more like an "attacker," finding race conditions and lifecycle bugs by holding many files in context simultaneously.
- The host built a custom "fleet review" combining Claude Code and ChatGPT Codex sub-agents with cross-verification to replicate the pattern.

## Detailed Breakdown

**[00:00] — Introduction and Accessing Ultra Review**
The host introduces the upcoming ultra review feature for Claude Code, which he accessed early through reverse engineering. Unlike the existing `/review` command, `/ultra review` runs on the cloud and takes 10-20 minutes. He tests it on PR #16, a complex voice calling feature with roughly 11,000 lines of code added.

**[01:03] — The Four Stages of Ultra Review**
Running the command spins up a web session with four stages: setup, find, verify, and dedupe. The finding stage deploys five independent sub-agents on the "hard version" of Claude Code. These sub-agents start at different positions in the codebase and follow different paths, because the order in which context is loaded can reveal or hide bugs. The host references his Claude Code masterclass, noting these sub-agents likely have distinct personas (e.g., billing, security).

**[02:06] — "Bug Hunter" and Fleet Size**
By inspecting the Claude Code binary, the host discovered the feature is internally called "bug hunter," with a default fleet size of 5 and a maximum of 20 (possibly reserved for enterprise). The fleet size is not currently configurable. The finding stage surfaced 64 candidate bugs, each with a brief description.

**[03:08] — The Verify and Dedupe Stages**
The verify stage uses independent sub-agents to confirm or refute each candidate bug, addressing the common problem of AI review tools producing false positives. At the time of recording, one bug was confirmed and nine were refuted. The final dedupe stage consolidates duplicate findings from different sub-agents into a single unique issue.

**[04:10] — Why Verification Matters**
The host highlights the verification step as the most valuable innovation. Traditional review tools often flag false positives or miss real issues. By verifying bugs before presenting them, ultra review prevents unnecessary changes. Even if users can't access the feature flag, the host encourages applying this verification-and-synthesis pattern to any multi-agent review workflow, especially for large PRs.

**[05:12] — Comparing Local Review vs. Ultra Review**
The standard `/review` runs locally in 3-4 minutes, spins up sub-agents to find bugs, and presents a combined list without verification. Ultra review ran for about 17 minutes and was still underway. The host speculates Anthropic may be A/B testing different sub-agent configurations, prompts, and possibly unreleased models (such as "Mythus") in the cloud.

**[06:15] — Custom "Fleet Review" with Claude Code and Codex**
Inspired by ultra review, the host built a custom fleet review that spins up three Claude Code sub-agents and three Codex sub-agents (via Codex CLI headless mode), then passes findings through both a Claude verifier and a Codex verifier. Cross-verification is valuable because each model sometimes catches or refutes bugs the other misses.

**[07:17] — Final Comparison and Recommendations**
ChatGPT Codex compared the two review outputs. The standard `/review` acts like a quick audit, flagging deviations from the norm. Ultra review behaves like an attacker, finding race conditions and lifecycle bugs by holding many files in context. Given only three free ultra reviews are available, the host recommends using `/review` for quick checks, Codex for a second pass, and `/ultra review` for large or critical features once it is publicly released.

## Notable Quotes
- "It's likely that these sub-agents have personas. So, one could be focused on billing, and another could be focused on security."
- "Stage three is basically this independent verifier... to verify that these are actually bugs independently."
- "Your current reviewing tool may just be flagging things and just leading to a lot of false positives instead."
- "Slash review is kind of doing a quick audit of the entire code base... the second review is kind of like an attacker instead. So, it's trying to pick one path of this entire PR and breaking it anyway."

## People, Tools & References Mentioned
- **Claude Code** — Anthropic's CLI tool; the core subject of the video
- **Ultra review / "bug hunter"** — The new feature under review
- **ChatGPT Codex / Codex CLI** — Used in the host's custom fleet review for cross-verification
- **Claude Code Masterclass** — The host's educational course, referenced and linked
- **Free newsletter** — The host's newsletter for Claude Code power users
- **PR #16** — An 11,000-line voice calling feature used as the test case
- **"Mythus" model** — Speculated as a possible unreleased model used in ultra review
- **$200/month plan** — The host's subscription tier, which included three free ultra reviews

## Who Should Watch
Power users and developers working with Claude Code—especially those handling large or complex pull requests—who want to understand upcoming multi-agent review capabilities and how to apply verification patterns to their own AI-assisted code review workflows.


<details class="transcript">
<summary>Full transcript</summary>

<p>Okay, so there&#x27;s a brand new feature coming soon to Cloud Code known as ultra review. And while this feature will not be available to everyone right now, I did a bit of reverse engineering so I could get access to it early. Now, as the name would suggest, you would expect this to be a really good like review feature, much better than the default like {slash} review built into Cloud Code. So, bear in mind we already have a {slash} review to review a pull request. But now, with this new feature enabled, if you do {slash} ultra review, then you can see that it says roughly 10 to 20</p>
<p>can see that it says roughly 10 to 20 minutes, finds and verifies bugs in your branch for either like your local changes or a PR, and it runs in Cloud Code on the cloud. So, if I do {slash} ultra review and then pass in a PR that I&#x27;m working on, which is uh number 16, this has about 11,000 lines added to the code base because it&#x27;s like a pretty complicated voice calling feature. So, running this command, this will then spin up a ultra reviewing session on the Cloud Code web version. So, you can see it say is that it&#x27;s running on the cloud, and it says this is free ultra</p>
<p>cloud, and it says this is free ultra review two out of free. So, I&#x27;m on the $200 month plan, and it seems that we get a couple free ultra reviews right now. Anyways, going over to web session, this is what it looks like on the Cloud Code web. So, it seems that we have a couple different stages running. We have the setup stage, the find stage, the verify stage, and the dedupe stage. So, essentially what&#x27;s happening is that after running ultra review, then it essentially spins out five independent subagents on the hard version of Cloud Code in the finding stage, and you can see it found 47 candidates over here to</p>
<p>see it found 47 candidates over here to find bugs throughout the entire code base. So, imagine what&#x27;s happening is that each of them is starting in a different position of the code base, and then following a different path for any recent changes that have happened because the order in which things are loaded into context window can reveal a bug, but if that order is swapped, then that bug can be like hidden to model or harder for the model to spot. And as I previously talked about in my Cloud Code masterclass, linked down below if you are interested, it&#x27;s likely that these sub-agents have personas. So, one could be focused on billing, and another could be focused on security. And the more</p>
<p>be focused on security. And the more sub-agents this ultra review is running behind the scenes, it&#x27;s likely that even more personas are running. And the reason I know that five sub-agents have been spun up is that when you look through the binary file of Cloud Code, then you essentially find that this feature is hidden under the word bug hunter, and there is a default bug hunter fleet size of five with a maximum up to 20. And this 20 may be for like enterprise organizations who are paying for like extra reviews or something like that. But as far as I know, this is not configurable right now. It&#x27;s only on the</p>
<p>configurable right now. It&#x27;s only on the Infobip servers. So, we can see that these sub-agents have found 64 candidates for potential bugs, and these are all the bugs that are listed right over here. And a brief description of each of the bugs and what potentially may be the problem. Now, this uh verifying stage is pretty interesting because essentially you may have found with certain reviewing tools, they give you a bug and then you check and it&#x27;s not actually a real bug, it just made something up instead. So, stage three is basically this independent verifier where we have another sub-agent or a set of</p>
<p>another sub-agent or a set of sub-agents, it&#x27;s not entirely clear, to verify that these are actually bugs independently. So, right now we have one confirmed bug and one refuted, and it seems to be going in order one by one trying to verify each of these bugs. It&#x27;s not exactly clear if this is happening each time in a brand new session or within the same like sub-agent instead. And finally at the very end, we will have a dedupe stage whereby it may be the case that many of these sub-agents have found that these bugs actually found the same bug but like from two different angles or two</p>
<p>like from two different angles or two different forms. And the dedupe stage basically combines it all into one unique finding instead. So, as I mentioned over here, this may take between 10 to 20 minutes on the cloud version of Cloud Code. So, I will come back to this later in the video once it is done, so we can see the final stages. Now, as a short aside, if you are interested in all things Cloud Code from a power user, then I do have a free newsletter all about this. There&#x27;s a link down below. And by signing up, you get access to a bunch of free videos from my masterclass as well. So, we can see that the verifying stage has refuted nine bugs so far.</p>
<p>nine bugs so far. But essentially, what I find interesting about this approach is that maybe with your traditional Cloud Code Review so far, your current reviewing tool may just be flagging things and just leading to a lot of false positives instead, or potentially doing the reverse and ignoring a bunch of issues. But what I find interesting about this ultra review approach that the Infropic team created, whereby it&#x27;s a verifying which bugs are actually bugs, it kind of prevents Cloud Code from making unnecessary changes for false positives. So, I think that has been like the most unique part about this approach that I want to be integrating into my own workflows going</p>
<p>integrating into my own workflows going forwards. And I think that really matters, especially if you have a lot of different sub-agents trying to find bugs from different angles, because many of those issues may actually be non-issues, or combined into an existing issue already. Now, whilst this feature is hidden behind a feature flag, and you may not be able to reverse engineer it to get access to a feature, but the same pattern still applies. Whereby, if you&#x27;re making a multi-agent review, you want to have a verification synthesizing step, whereby it&#x27;s actually making sure that those things that were flagged are serious issues, especially for really</p>
<p>serious issues, especially for really big PRs, kind of like this one, which has 11,000 lines. So, you can still be applying this verification pattern to whichever review that you&#x27;re doing. So, for example, I also use the built-in review, which reviews a pull request locally, for the same pull request, which we&#x27;ll be doing a comparison at the end to see which one is better. But essentially, the normal review built into Cloud Code, not the ultra review, does not have a verification step, because it just spins up a bunch of sub-agents to find bugs, each of them being a solid sub-agent instead, and then it just gives me the list from all</p>
<p>then it just gives me the list from all the sub-agents combined. So, so far, the ultra review has been running for about 17 minutes and it&#x27;s still underway. Whereas the local review ran for about 3 to 4 minutes instead. And I think one of the reasons they added this brand new feature is because they may want to be testing this AB testing this going forwards with different sub-agent configurations and different sub-agent prompts that they have running in the cloud and potentially mixing different models including unreleased models as well. So, I made a fleet review scale myself based on this idea whereby essentially what this fleets review</p>
<p>essentially what this fleets review scale is doing is that it spins up three Claude Code sub-agents to try and find bugs and also three CodeX sub-agents so via the CodeX CLI headless mode to try and find those bugs as well. And then it passes it through a verify stage. So, there will be a Claude Code verifier and then also a CodeX verifier to make sure those bugs are actually real bugs. And this stage is pretty important because sometimes you will find that CodeX says that a bug that Claude Code found isn&#x27;t actually a real bug and the reverse also happens whereby CodeX finds a bug and</p>
<p>happens whereby CodeX finds a bug and then Claude says it&#x27;s not a bug. So, I think that by combining these two verification stages you may get a better output. So, then I got ChatGPT CodeX to compare the local review which is review one with the ultra review. So, the way that I would kind of describe it is that {slash} review is kind of doing a quick audit of the entire code base and everything that deviates from the mean slightly it&#x27;s just flagging as an issue. And the second review is kind of like an attacker instead. So, it&#x27;s trying to pick one path of this entire PR and breaking it anyway. So, it kind of found</p>
<p>breaking it anyway. So, it kind of found some race conditions and life cycle bugs that the first review completely missed, did a better job at holding like many different files in its minds together. So, anyways because it seems that we&#x27;re only going to be getting three free ultra reviews it may be the case that like this is just much more expensive for them to run like on that cloud or they may be using a different model in some way. Maybe they would be using some elements of the Mythus model that&#x27;s coming up in the ultra review. So, it seems that you would want to do a quick {slash} review for a PR or a new feature, and then maybe use Codex as</p>
<p>feature, and then maybe use Codex as well to find any more bugs with another review. And if the feature is really important or really big, you may want to do a {slash} ultra review as well once it is released. Anyways, if you do like this kind of stuff, then do subscribe to the channel because I do make the most in-depth videos on Cloud Code on YouTube. And if you&#x27;re interested in learning more about Cloud Code, then I have a whole masterclass all about this linked down below.</p>

</details>
