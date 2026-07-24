---
title: "The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI"
channel: "AI Engineer"
video_id: q2JrUKBMf0w
url: https://www.youtube.com/watch?v=q2JrUKBMf0w
published: 2026-07-24T07:43:04+00:00
generated: 2026-07-24T21:21:41+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/q2JrUKBMf0w/hqdefault.jpg
---
# The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI

[![The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](https://i.ytimg.com/vi/q2JrUKBMf0w/hqdefault.jpg)](https://www.youtube.com/watch?v=q2JrUKBMf0w)

[Watch on YouTube](https://www.youtube.com/watch?v=q2JrUKBMf0w) · **AI Engineer** · 2026-07-24

## TL;DR
Aparna Dhinakaran of Arize AI argues that classical "LLM as a judge" evaluations are insufficient for today's complex, agentic AI systems, which feature tool calls, reasoning, and long-horizon tasks. She introduces "Agent as a Judge"—a new evaluation paradigm where an adaptive agent dynamically analyzes traces, discovers subtle failure patterns, and can even propose fixes—announcing Arize's release of "Signal," a long-running agent built for this purpose.

## Key Takeaways
- Arize AI runs over 100 million evaluations per month, with top teams running more than 3,800 different evaluators across offline and online contexts.
- The nature of what teams are evaluating has fundamentally shifted: from simple prompt-response systems in 2023 to complex agents with tool calls, reasoning, and sub-agents on long-horizon tasks in 2024.
- Each leap in agent capability (memory, dynamic UIs, multi-step reasoning) created a qualitatively different, harder problem—not just a harder version of the same problem.
- Classical "LLM as a judge" evals rely on fixed rubrics and deterministic scoring, which fail to capture the dynamic, non-deterministic trajectories of modern agents.
- Arize's own internal agent, "Alex," exposed these limitations firsthand: it would forget context, get stuck in loops, and produce a unique UI trajectory per user interaction.
- "Agent as a Judge" is proposed as a complementary new paradigm: using an adaptive agent to evaluate other agents, enabling dynamic analysis rather than static rubric scoring.
- Arize announced the release of "Signal," a long-running agent that reads traces, discovers issue patterns (e.g., repeated tool calls, inefficient trajectories), and can even open pull requests with fixes.
- The future of evals involves all three layers: deterministic evals, LLM-as-a-judge, and agent-as-a-judge.

## Detailed Breakdown

### Introduction and Context [00:01](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=1s)
Aparna Dhinakaran, co-founder of Arize AI, opens by welcoming attendees to the evals track at the AI Engineer event. She notes the track features speakers from Term Bench, Uber, and Snorkel, and frames her talk around the future of evals—a capability that has evolved from a niche skill into a core practice for serious AI teams.

### Scale and Importance of Evals [00:31](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=31s)
Drawing on Arize's work with leading AI teams, Aparna shares that the platform runs over 100 million evals per month. The average team runs about 12 evaluation jobs, while top teams run more than 3,800 distinct evaluators. She emphasizes that online evals run on live production traces are especially valuable because they help teams identify what's working, catch failures, and feed data into continual learning loops. She cites industry consensus, including Garry Tan and CPOs from Anthropic and OpenAI, affirming that "evals are everything."

### The Problem: What We Evaluate Has Changed [02:04](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=124s)
Aparna identifies the core tension: while first-generation evals were being built, the underlying systems being evaluated transformed. In 2023, evaluation meant assessing a model's response to a single prompt. By 2024, frontier models incorporated tool calls, reasoning, and deep research, and teams began deploying agents with sub-agents on long-horizon tasks over real-world data. Each of these shifts represented not just an increase in difficulty but a fundamentally different type of problem, meaning the ways systems fail also became more complex.

### Arize's Internal Agent "Alex" as a Case Study [02:34](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=154s)
To illustrate the pain, Aparna describes Arize's own agent, "Alex," which lives in their UI. As frontier labs added capabilities, Arize added them to Alex—longer memory, dynamic UI creation, and cross-trace search. However, Alex also exhibited failures: forgetting context, not knowing when a task was done, and getting stuck in loops. Critically, every user interaction could produce a different UI trajectory, making classical LLM-as-a-judge evals inadequate for catching the full range of failures.

### The Revelation: Agent as a Judge [03:36](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=216s)
This experience led to a key insight: the best way to evaluate an agent may be with another agent. Aparna clarifies that this does not invalidate deterministic evals or LLM-as-a-judge approaches; rather, it adds a new tool for a new class of problem. LLM-as-a-judge applies fixed rubrics and fixed scores, which works for deterministic flows. Agent-as-a-judge, by contrast, performs adaptive, dynamic analysis suited to agents whose trajectories vary with every user input.

### Release of "Signal" and Closing [04:09](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=249s)
Aparna announces the release of "Agent as a Judge" and a product called Signal, a long-running agent that reads traces, discovers patterns of issues, and identifies subtle failures—such as a tool being called repeatedly or an inefficient trajectory—that deterministic rubrics would miss. Because Signal performs deep analysis, it can even open a pull request with a proposed fix. She closes by inviting attendees to visit Arize's booth (near OpenAI's), attend the evals track in room 2005, and join a World Cup viewing party.

## Notable Quotes
- "Evals have gone from the new skill that every PM and every AI engineer has to learn to the thing that every serious AI team is betting on."
- "We didn't just make the problem harder, we actually got a fundamentally different type of problem."
- "What if the best way to evaluate an agent was actually with an agent?"
- "Agent as a judge is about adaptive dynamic analysis. LLM as a judge just gives you a fixed rubric with these fixed scores."
- "My take is that most teams today are doing the first two, but the future of evals is actually having all three."

## People, Tools & References Mentioned
- **Aparna Dhinakaran** — Co-founder of Arize AI; speaker.
- **Arize AI** — Company building evaluation tooling; runs 100M+ evals/month.
- **Alex** — Arize's internal agent used in their UI; used as a case study for agent failure modes.
- **Signal** — Newly released Arize product; a long-running agent that analyzes traces, discovers issue patterns, and can open PRs with fixes.
- **Garry Tan** — Quoted saying "Evals are everything you need."
- **Anthropic, OpenAI** — Referenced as frontier labs whose CPOs emphasize the importance of evals.
- **Term Bench, Uber, Snorkel** — Organizations with speakers in the evals track at the event.
- **Room 2005** — Location of the evals track at the venue.

## Who Should Watch
AI engineers, PMs, and platform teams building or evaluating agentic systems who want to understand why classical LLM-as-a-judge evals fall short for multi-step agents and how an "agent as a judge" approach can surface subtle failures and even propose fixes.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=1s">00:01</a></span> Awesome. Well, hey everyone. My name is Aparna, one of the founders of Arize. We work with some amazing teams to help them build evals. Um, and we have an incredible lineup of talks for you all today at the evals track. Um, it&#x27;s happening in room 2005 and there&#x27;s going to be amazing speakers</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=31s">00:31</a></span> and there&#x27;s going to be amazing speakers from Term Bench and Uber and Snorkel kind of all happening after this. Um, but today I&#x27;m here to talk to you about the future of evals. Evals have gone from the new skill that every PM and every AI engineer has to learn to the thing that every serious AI team is betting on. We&#x27;ve been really fortunate to get to work with some of the best AI teams in the world. So, we get a front row seat into not just what&#x27;s happening when they&#x27;re building their actual agents and before they actually ship, but</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=62s">01:02</a></span> and before they actually ship, but actually the evals that teams are running on their live production agent via their traces. Little bit of some stats for you guys. We run over 100 million evals every month. The average team runs about 12 different eval jobs with the top teams running over 3,800 different evaluators. And offline evals, online evals, they each have their own place, but today what I&#x27;m actually going to talk to you about is the teams that are running evals on their traces. This is actually what&#x27;s helping teams</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=93s">01:33</a></span> This is actually what&#x27;s helping teams figure out what&#x27;s working, catch their failures, and that&#x27;s the type of data you need to fuel your continual learning loops. And the industry kind of agrees. I mean, all the CPOs of Anthropic, OpenAI, all you know, GDB, you have Garry Tan saying, &quot;Evals are everything you need.&quot; And the whole industry kind of agrees. So, we added evals, they catch all the failures, right? Here&#x27;s the problem. When we were building all of these first-gen evals,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=124s">02:04</a></span> building all of these first-gen evals, the thing that we were actually evaluating has changed underneath us. In 2023, it was about just answering a prompt. In 2024, we started to see all the frontier models. They&#x27;ve added tool calls, they&#x27;ve added reasoning, they&#x27;ve added deep research. Now, what we have is teams running loops on real-world data with sub-agents kicked off on long-horizon tasks. Every one of these was actually a massive jump in complexity, and we</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=154s">02:34</a></span> massive jump in complexity, and we didn&#x27;t just make the problem harder, we actually got a fundamentally different type of problem. What that meant is that as these systems got more complex, so did the way that they actually fail. We&#x27;re really lucky cuz we have our own agent that we&#x27;ve built, Alex, that lives in our UI, and we get our kind of get to feel this pain ourselves. Every time the frontier labs added new functionality, we added it to our agent. And now Alex can has much longer memory. It has the ability to create dynamic UIs.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=185s">03:05</a></span> has the ability to create dynamic UIs. It can go search across an enormous volume of traces. But, we also realized that it would forget context. It wouldn&#x27;t know when something was done. Um sometimes it would just get stuck in these loops. And the key thing here is that the classical LLM as a judge evals, that probably many of you have written in this room, just weren&#x27;t for us to be able to catch all the types of failures that we were experiencing. I mean, it&#x27;s just fundamentally different, right? You have a deterministic flow, and now what</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=216s">03:36</a></span> have a deterministic flow, and now what we have is literally every time a user interacted with Alex, it would create a new UI. That&#x27;s a fundamentally different trajectory. So, this led to our really big revelation. What if the best way to an evaluate an agent was actually with an agent. Doesn&#x27;t mean that all of the ways that we did evals, with deterministic evals, with LLM as a judge, classic evals, doesn&#x27;t matter anymore, but it just means that we have a different type of tool to solve a different type of problem. Agent as a judge is about</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=249s">04:09</a></span> problem. Agent as a judge is about adaptive dynamic analysis. LLM as a judge just gives you a fixed rubric with these fixed scores. It&#x27;s what everyone&#x27;s doing, but when your agent&#x27;s doing completely different trajectories every time a user puts in data, it just means that you need a fundamentally different type of eval. My take is that most teams today are doing the first two, but the future of evals is actually having all three. And today I&#x27;m actually excited to share we&#x27;ve released agent as a judge</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=279s">04:39</a></span> we&#x27;ve released agent as a judge to help our teams on their eval journey. We&#x27;ve released signal. Signal&#x27;s actually a long-running agent that can read traces sent in, discover patterns of issues. Um, it can figure out types of problems that a classical LLM as a judge eval just would never be able to do with these deterministic rubrics. It&#x27;s helped us figure out very subtle failures that you wouldn&#x27;t even think of doing, such as something going on in a loop for multiple times, it was calling the same tool</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=310s">05:10</a></span> it was calling the same tool for repeatedly long time, the trajectory was inefficient. And actually what this does is because it has all that analysis, it can go put up a PR and put up a fix. So, if you want to learn more, come to our come to our booth. We&#x27;re right by the OpenAI booth. We&#x27;ll give you a demo, we&#x27;ll show you a bit more about it. We&#x27;re also, like I said, taking over the evals track, so come to room 2005. We&#x27;re going to be talking a lot about the future of evals and what they look like. And if you just want to hang out with our team, we&#x27;re throwing a viewing party</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=q2JrUKBMf0w&amp;t=340s">05:40</a></span> our team, we&#x27;re throwing a viewing party for the USA World Cup game tonight, so check out the Luma and register to come join us. Awesome. Thank you all so much.</p>

</details>
