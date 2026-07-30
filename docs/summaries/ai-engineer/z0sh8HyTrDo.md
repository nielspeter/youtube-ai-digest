---
title: "Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI"
channel: "AI Engineer"
video_id: z0sh8HyTrDo
url: https://www.youtube.com/watch?v=z0sh8HyTrDo
published: 2026-07-29T06:16:07+00:00
generated: 2026-07-30T03:22:19+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/z0sh8HyTrDo/hqdefault.jpg
---
# Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI

[![Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](https://i.ytimg.com/vi/z0sh8HyTrDo/hqdefault.jpg)](https://www.youtube.com/watch?v=z0sh8HyTrDo)

[Watch on YouTube](https://www.youtube.com/watch?v=z0sh8HyTrDo) · **AI Engineer** · 2026-07-29

## TL;DR
Ramana Siddanth Emani from Auditoria AI argues that the real bottleneck in shipping production AI agents isn't the model or framework—it's the developer's own dev loop velocity. By leveraging sub-agents in parallel git work trees, organizational "skills," MCP tools, and minimal-UX dashboards, developers can remove themselves from the orchestration loop and let agents autonomously fix bugs, run tests, and ship code with humans serving only as verifiers.

## Key Takeaways
- Production bugs are inevitable because agents encounter unseen customer data once demos become pilots; swapping models or frameworks won't fix the core issue.
- The true bottleneck is human attention and dev loop velocity, not model capability or GPU speed.
- Four key primitives for 10x productivity: sub-agents, parallel git work trees, organizational "skills," and MCP tool connections.
- A single MacBook with 48 GB of RAM can run ~50 independent work trees simultaneously, each handling a separate task like a Jira bug ticket.
- In a 9-step automated bug-fix pipeline, humans are only needed at step 1 (define the task) and step 9 (validate the shipped fix).
- Minimal UX—compressing Kubernetes, logs, Jira, GitHub PRs, and cloud sessions into one pane of glass—drastically reduces context-switching overhead.
- In regulated finance environments, accountability and compliance (e.g., SOX) add constraints, making human verification even more critical.
- Recursive self-improvement lets agents analyze their own bottlenecks over days/weeks and progressively automate them away.
- Combining "goals" (set-and-forget instructions) with "loops" enables agents to autonomously investigate discrepancies, fetch logs, and ship fixes.
- "Dreaming"—agents compacting recurring customer session patterns into upgrade data points—further reduces the need for human intervention.

## Detailed Breakdown

### The Real Problem: Demos vs. Production [00:01](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=1s)
Emani opens by acknowledging the provocative title—*you* are the bottleneck—and clarifies he means the internal developer harnesses used to build production agents. He introduces himself as a data scientist at Auditoria AI, which builds production agents for finance. The talk sits at the intersection of harness engineering and AI for finance, aimed at helping developers become 10x more productive.

### Why Demos Fail in Production [01:03](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=63s)
Beautiful demos are easy to ship, but once promoted to pilots with real customers, agents encounter data they've never seen, causing high production bug rates. Emani dismisses common scapegoats—better models (e.g., "Fable 5"), faster GPUs, or new frameworks—since these arrive on predictable cadences (new models every ~3.5 months, new chips yearly) and swapping them doesn't address real-time bug fixing.

### Four Primitives for Dev Loop Velocity [02:37](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=157s)
The answer is automating the developer loop. Emani introduces four primitives: (1) **sub-agents** that can be spawned in armies; (2) **git work trees** as isolated parallel folders where agents write code independently; (3) **skills**—organizational secret recipes and workflows that ensure agents follow correct procedures; and (4) **MCP tools** for connecting to any third-party server or data system. Minimal UX ties these together because orchestrating many sub-agents creates significant overhead.

### Sub-Agents and Parallel Work Trees [03:07](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=187s)
With 48 GB of RAM on a MacBook, a developer can maintain ~50 active work trees, each with an independent sub-agent working on a different task (e.g., separate Jira bug tickets). Agents handle task queuing better than humans. Emani walks through an idealized harness: an agent parses requirements, performs root-cause analysis, pulls traces and logs, works in an isolated work tree, does TDD, implements the fix, runs local tests, creates a PR, and shepherds it through Docker builds and deployments to dev and stage environments.

### Where Humans Are Actually Needed [06:16](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=376s)
Emani asks the audience to identify which of the 9 pipeline steps require human contact. His answer: only steps 1 (initiating/defining the work) and 9 (validating after deployment to stage). Everything in between can be done better by the agent. He shows a macOS widget dashboard that consolidates Kubernetes services, pods, logs, Jira tickets, GitHub PRs, and a cloud code session into one view, drastically reducing the "neck rotations" developers perform across multiple monitors.

### Finance-Specific Constraints [07:50](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=470s)
In finance, regulation and SOX compliance require a human auditor to review code and a controller to sign off. Agent-to-agent review raises accountability questions—you can't blame "the cloud" when something breaks. This makes the human verification role even more important, even as orchestration overhead remains the bottleneck.

### Removing Yourself from the Loop [08:52](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=532s)
With recursive self-improvement and advancing model capabilities (referencing "Fable 5," "Mythos 5," and "GPT 5.6"), Emani envisions a loop where production failures become inputs. You let the agent run for 1–2 days solving bug tickets, then ask it to analyze its own bottlenecks, list them, and progressively remove them. Over a month, this yields a self-automated loop where a single sentence—"fix this bug for me"—triggers the agent to fetch logs, traces, and tickets, then ship the fix through the QA pipeline.

### Goals, Loops, and Dreaming [10:55](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=655s)
Emani highlights three advanced features: **goals** (set-and-forget instructions like "fix this data discrepancy"), **loops** (autonomous iterative investigation), and **dreaming** (agents compacting recurring customer usage patterns into data points that upgrade the system). Combining these lets developers close their laptops and monitor from their phones, effectively removing themselves from the loop.

### Summary and Philosophy [12:28](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=748s)
Emani recaps: sub-agents in parallel work trees, organizational skills, MCP tool connections, all compressed into one pane of glass for minimal UX, with goals and loops for autonomy. He emphasizes that humans should always be verifiers, never the throughput ceiling, because human attention is limited. He closes by noting that sitting at a desk 9-to-5 just writing code is no longer a valid developer workflow.

## Notable Quotes
- "Writing code is very easy. Shipping beautiful demos and showing it to a lot of people is very easy right nowadays. So what is the problem?"
- "If you wait 3 and 1/2 months, we are awarded with a new model in the market. So we can easily swap models... How do we in real time fix these production bugs? The answer is your dev loop velocity."
- "The human is only required at steps 1 and 9 because the in-between steps, the agent can do a lot better work."
- "Always have the human as a verifier, but not the throughput ceiling because human attention is very limited."
- "Sitting behind a desk from 9:00 to 5:00 and just writing code is not valid anymore."

## People, Tools & References Mentioned
- **Ramana Siddanth Emani** — Data Scientist at Auditoria AI, speaker
- **Auditoria AI** — Company building production agents for finance
- **MCP tools** — Model Context Protocol tools for third-party server connections
- **Jira** — Bug ticket tracking system
- **GitHub PRs** — Pull request workflow
- **Kubernetes** — Container orchestration (services, pods)
- **Docker** — Image building for deployment
- **SOX compliance** — Sarbanes-Oxley regulatory compliance for finance
- **Git work trees** — Isolated folders for parallel agent code generation
- **"Fable 5," "Mythos 5," "GPT 5.6"** — Referenced (possibly hypothetical/future) model names
- **macOS widget dashboard** — Minimal UX pane-of-glass interface concept

## Who Should Watch
AI engineers and developer tooling leads building production agents—especially in regulated industries like finance—who want to accelerate their dev loop and reduce human orchestration overhead. The talk is particularly valuable for those transitioning from impressive demos to reliable production systems where bug-fixing velocity matters more than model selection.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=1s">00:01</a></span> Hello everyone. Welcome to this session about your finance agent&#x27;s bottleneck is you. So, sorry for the rude title. I don&#x27;t mean to call the audience here the bottlenecks, but I&#x27;m here to talk about the harnesses that you guys are developing and using these internal harnesses to build your</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=32s">00:32</a></span> these internal harnesses to build your production agents. So, my name is Siddhant Imani and I&#x27;m a data scientist at Auditoria AI and we build production agents for finance. So, if you&#x27;re a CFO in the audience, I would love to speak to you after the session. This talk is in between the harness engineering track and AI for finance. So, this talk is mostly about identifying the bottlenecks within your developer and if you&#x27;re a developer yourself, how</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=63s">01:03</a></span> and if you&#x27;re a developer yourself, how do you be 10x productive with the agent harnesses that you&#x27;re using. So, all of us have seen, you know, beautiful demos in this AI engineer&#x27;s world fair. But, once these demos are promoted to pilots and you start onboarding new customers, the agent has never seen these future data. So, all of us know production bugs are very high</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=93s">01:33</a></span> high and production guards built by the hour. So, that&#x27;s a hard fact. And writing code is very easy. So, shipping beautiful demos and showing it to a lot of people is very easy right nowadays. So, what is the problem? And why do these demos fail in production? Is it the model? Do you need a better model? Fable 5, perhaps? Or do you need faster GPUs? Or do you need a better framework? Maybe.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=126s">02:06</a></span> do you need a better framework? Maybe. Or your RALF loops are not working properly. So, what is the answer? If you wait 3 and 1/2 months, we are awarded with a new model in the market. So, we can easily swap models. If you wait perhaps 1 year, we have new chips. We have faster GPUs. And again, writing code is easy. So, we have new from frameworks every day. So, you can swap your framework every now and then. So, how do we</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=157s">02:37</a></span> So, how do we in real time fix these production bugs? The answer is your dev loop velocity. The model capability increases very exponentially. And the developers have to spend a lot of time every day to automate your developer loop. So, I&#x27;m talking about four primitives here. All of you need to think about loops. And at the end of the session, I hope you can 10x your production code.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=187s">03:07</a></span> So, first we have sub agents. Nowadays, whatever harness you&#x27;re using, you can spawn new sub agents. You can have a You can have an army of them. And get work trees are your best friend. So, think of work trees as isolated folders. And inside these folders, the agent writes whatever code it&#x27;s generating. So, you want these work trees to be in parallel. So, the sub agents are doing independent tasks and are not fighting over the same thing.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=219s">03:39</a></span> fighting over the same thing. Second, we have skills. These are your organization secret recipes. So, make sure you have a lot of skills because these skills, once you start say giving it to your agents, the agents will always make sure to use the correct and proper workflows to solve whatever production bug you&#x27;re facing. And of course, all of us have seen a lot of MCP tools being shipped into the market right now. Everybody says we can, yeah, the agent can connect to whatever MCP tool and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=250s">04:10</a></span> can connect to whatever MCP tool and whatever third-party server there is. And your client data can live in any system you want. And at the end of the day, if you have a lot of sub-agents, you have a lot of work to orchestrate. So, minimal UX is the key here. Let&#x27;s look at the sub-agents. With you as the orchestrator, you can have, let&#x27;s say, with 48 GB of RAM on your MacBook, you can have 50 active work trees. That is 50 active sub-agents working independently on</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=282s">04:42</a></span> sub-agents working independently on different tasks. So, where do these tasks come from? So, let&#x27;s say the production software you&#x27;re going to ship has a lot of bugs that your QA is reporting. So, all the Jira tickets can be thought of in a separate different work tree. So, different work trees are handled by a separate agent, and these agents can spawn multiple sub-agents to solve that particular task. You don&#x27;t want to queue up your tasks because the agent is will do that a lot better than you.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=315s">05:15</a></span> Let&#x27;s look at, you know, um, an example harness. What if the QA reports a lot of bug tickets, and somehow magically there is an agent which parses the requirements, does a root cause analysis, pulls all the traces, pulls all the logs, puts all this in a separate work tree, does the TDD, does the, implements the fix. Because it&#x27;s in your local system, you have to do test scripts, local</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=346s">05:46</a></span> have to do test scripts, local end-to-end testing. You create a PR. You submit the PR to your team for review. And after review, you merge it into your master branch, let&#x27;s say. After merging it, obviously, you have to build a Docker image, deploy it into your development environment, test it, again ship build an image to your stage environment, test it, deploy it to stage. And then you go back to the QA saying, &quot;Here you go. You can test it now.&quot;</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=376s">06:16</a></span> &quot;Here you go. You can test it now.&quot; So, I would like to ask a question in the audience, um at what points do you think the human contact is required in this, um steps 1 to 9? So, I would say the human is only required at steps 1 and 9 because the in-between steps, the agent can do a lot better work. There needs to be a human to see what work the agent is doing. And then needs to be a human at the end to validate</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=406s">06:46</a></span> to be a human at the end to validate after the work is being shipped to stage. And obviously, we need minimal UX because humans love minimal UX. So, in the image, if um you can if you squint your eyes and see, the image shows um the production agent software that you&#x27;re building, the project dashboards which shows all your Kubernetes services, pods, examples, all the logs, system logs, all your Jira tickets, all your GitHub PRs,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=438s">07:18</a></span> all your GitHub PRs, and maybe a cloud code session at the bottom. So, this is basically a macOS widget, and you don&#x27;t need to open multiple windows to do all of this work. A developer does like variety of things in their software development life cycle. So, you can use just this one widget to do a lot of things. So, you can see from the graph also, the number of neck rotations to ship one change like reduces a lot drastically. And I imagine all of you have like two to three monitors on your table and you</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=470s">07:50</a></span> to three monitors on your table and you just keep rotating your neck orchestrating these agents. So, Auditoria works in finance. So, there&#x27;s a lot of regulation and policies happening in finance right now. So, what does it look like for orchestrating a team of sub agents in the finance sector? If we take AI out of the picture, usually what happens is you have a human auditor which reviews the code and you have a controller which signs off under your socks compliance.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=501s">08:21</a></span> off under your socks compliance. And reviewing agent to agent, it it doesn&#x27;t Where do you keep the accountability? If something goes wrong in production, you can&#x27;t say Cloud is doing this. Something is wrong. So, but let&#x27;s say you have all these sub agents and you&#x27;re using this harnesses to fix bugs in real time. What is the bottleneck? It becomes a human attention because you yourself have to orchestrate all these different tasks.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=532s">08:52</a></span> And moving fast and breaking things in sector in the finance sector is a lot different. So, let&#x27;s look at part two, which is removing yourself from the loop. Till now I&#x27;ve been saying a human is required to see what the agent is doing and at the end also to validate what the agent has done. But with the self-improvement of the agent and model capabilities these days, we get Fable 5 and Mythos 5 and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=563s">09:23</a></span> Fable 5 and Mythos 5 and GPT 5.6 also. So, what does it look like when you have this recursive self-improvement in your internal developer developer harnesses? So, all your production failures become input. So, let&#x27;s say you automate keep automating these cell developer harnesses every day and you ask the agent to upgrade itself essentially. So, you do a task. You let the loop run.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=594s">09:54</a></span> So, you do a task. You let the loop run. Let&#x27;s say one or two days. You solve five to six bug tickets. And you just tell the agent to analyze all the bottlenecks in this process. Make a list of them. And somehow slowly keep removing these bottlenecks every day. At the end of one month, let&#x27;s say, you have a really nice self-automated loop where you just type in one sentence and just say fix this bug for me. And the agent goes off, connects to all your database systems, fetches all the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=625s">10:25</a></span> your database systems, fetches all the logs, traces, tickets, and ships it and migrates it migrates it to the Jira to QA pipeline. And you can just book a vacation maybe or work from home. And what does it look like internally and what happens when you stare less and ship more? Nowadays, how many of you know you can give goals to your agents? You can just set a goal and forget about it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=655s">10:55</a></span> set a goal and forget about it. Anybody? Nice. Um so, what if you combine goals and loops? You can just set a goal saying there is some data discrepancy in this report. And in the production bug like the source data is not matching with what the agent has generated. So, you can just set a goal to fix this, look into this, set a loop. You can even close like close your laptop because you can do it from your phone nowadays. And</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=687s">11:27</a></span> And if you look at the last but one point, which is dreaming, um let&#x27;s say a lot of are using your production software and they are doing the same type of patterns and they&#x27;re facing the same type of problems. So, you let the agent dream like humans dream in the background so that it collects all the sessions that your customers are using and compacts it into a set of data points which your system can use and basically [snorts] upgrade yourself.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=717s">11:57</a></span> upgrade yourself. So, with a combination of all these features, basically you can essentially remove yourself out of the loop. But, as I said before, the developers do a lot of variety things in their software development life cycle and sitting behind a desk from 9:00 to 5:00 and just writing code is not valid anymore. So, just an overview of what I&#x27;ve covered till now in the session. You can have a team of sub agents</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=748s">12:28</a></span> You can have a team of sub agents working in parallel work trees. You can have skills, your organizational secret recipes, your customers recipes. You can give all of these to an agent. Your agent can connect to whatever third-party server there is. It can be a logging system, it can be an authentication gateway. And you just compress all of this into one pane of glass because minimal UX is the key. And you can set goals and loops for autonomy. If you think this particular work can be done by the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=780s">13:00</a></span> this particular work can be done by the agent a lot better, you can just ship it to the agent. Always have the human as a verifier, but not the throughput ceiling because human attention is very limited. So, thank you for your time and thank you for your Thank you for I hope you um learned something from the session. Thank you. [applause]</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=z0sh8HyTrDo&amp;t=820s">13:40</a></span> Hey.</p>

</details>
