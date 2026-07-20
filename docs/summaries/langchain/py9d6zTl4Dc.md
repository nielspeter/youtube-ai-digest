---
title: "How Coinbase Builds Developer Support Agents | Interrupt 26"
channel: "LangChain"
video_id: py9d6zTl4Dc
url: https://www.youtube.com/watch?v=py9d6zTl4Dc
published: 2026-07-20T12:40:58+00:00
generated: 2026-07-20T14:33:47+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/py9d6zTl4Dc/hqdefault.jpg
---
# How Coinbase Builds Developer Support Agents | Interrupt 26

[![How Coinbase Builds Developer Support Agents | Interrupt 26](https://i.ytimg.com/vi/py9d6zTl4Dc/hqdefault.jpg)](https://www.youtube.com/watch?v=py9d6zTl4Dc)

[Watch on YouTube](https://www.youtube.com/watch?v=py9d6zTl4Dc) · **LangChain** · 2026-07-20

## TL;DR
Coinbase's developer support engineering team transformed their developer support from a basic Discord-hosted chatbot into a self-improving, agentic system powered by Python services, LangSmith tracing, and MCP tools. Evan Kormos shares the technical architecture, development workflow, and key lessons learned in scaling AI support for crypto developers while maintaining high customer satisfaction.

## Key Takeaways
- Coinbase's developer platform supports a community building on crypto APIs, wallets, payments, and staking infrastructure, originally relying on manual Discord support.
- The team moved from a hosted chat service with no visibility into usage to a full agentic system with observability built in from the start.
- Python services were elevated to first-class infrastructure, paired with self-hosted LangSmith for tracing and evaluation.
- A remote MCP server for developer documentation serves as the primary tool, with a RAG fallback acting as both a safety net and an A/B testing mechanism.
- Three showcased agents include Discord AI Chat, Slack Triage, and a Support Engineer Assistant — each addressing different parts of the support workflow.
- Guardrails combine deterministic safeguards with lightweight LLM-based judgment to evaluate responses for accuracy and risk.
- The team's development workflow is entirely intent-based, using Claude Code with MCP tools for tech grooming, research, planning, and execution.
- Trace analysis ("back-testing") is used to discover signals for system improvement, profiling chat turns both randomly and deterministically.
- Multilingual conversations emerged immediately in Discord, highlighting the need to consider multilingual adversaries in security testing.
- Three core lessons: treat agent engineering as its own discipline, build observability ("the glass box") before the agent, and recognize that team alignment is the true multiplier.

## Detailed Breakdown

### Introduction and Agenda [00:06](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=6s)
Evan Kormos introduces himself as a builder and manager of engineering teams at Coinbase. He frames the talk as the story of the developer support engineering team's transformation from zero to one on a self-improving, customer-facing agentic system. The agenda covers the support challenge, agent behavior monitoring, technical capabilities, and team contributions.

### Coinbase Developer Platform and Support Challenge [01:11](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=71s)
The Coinbase developer platform powers developers building on crypto APIs, wallets, payments, staking, and infrastructure for the on-chain economy. The original support model was people posting and answering questions in a Discord server. The team needed to scale while keeping customer satisfaction high and increasing automation levels, with PM Harry shaping and prioritizing the work.

### Version One Discord Chat and Its Limitations [02:47](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=167s)
The first version integrated a hosted chat service that answered developer questions but had significant shortcomings: docs could go stale, there was no visibility into how people used it, and quality assessment required manually tallying thumbs up and thumbs down. The team had no real idea what was happening — a familiar problem when standing up a new service.

### System Design and Infrastructure [03:50](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=230s)
The system meets customers where they are (Discord and web) while providing quality backend tools for support engineers. The agentic foundation enables future expansion to partner Slack channels, new MCP channels, and generative UX. A major unlock was making Python services first-class infrastructure — the team's first service of this type — paired with self-hosted LangSmith for tracing, driven by team member Caesar.

### MCP Server, RAG Fallback, and Internal Services [04:52](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=292s)
A remote MCP server provides developer documentation to the agent. Because remote MCP tools can be unreliable for customer-facing agents, the team added a RAG fallback fed by a basic knowledge pipeline into a vector DB. This also serves as an A/B testing mechanism for the MCP tool. The system also connects to various internal services — some event-driven, some proxying external services — supporting both on-demand and ambient agent flows.

### Showcased Agents Overview [05:54](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=354s)
Three agents are showcased: Discord AI Chat, Slack Triage, and the Support Engineer Assistant. Additional compliance, risk reduction, and service quality agents are being built. The Discord Support bot offers a menu to launch AI Chat, open a case, or access case management, with automatic channel responses coming soon.

### Discord AI Chat and Guardrails [06:57](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=417s)
The Discord AI Chat provides expert responses guiding developers with technical documentation or further support paths. Significant care went into detecting and preventing misuse despite the agent lacking transaction or sensitive data access. Guardrails include deterministic safeguards, the developer documentation MCP tool, and lightweight LLM judgment evaluating responses for accuracy and risk — forming the foundation for public auto-response.

### Discord Support Triage in Slack [08:07](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=487s)
The Slack Triage channel surfaces Discord messages internally, with links directly into LangSmith trace data. As classifiers are tuned, this surface can serve as a lens and control plane to flag improvement signals and track agents in motion as part of the team's workflow.

### Support Engineer Assistant [08:38](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=518s)
An AI Support Assistant runs internally on a locally hosted React site within the service console. It allows users to control chat context based on underlying system access permissions. Initially read-only, it has building blocks for human-in-the-loop functionality, with "send customer response" capability planned. The pop-out window enables a responsive, controllable UX.

### Intent-Based Development Workflow [09:09](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=549s)
Everything the team does is intent-based, using a Linear Slack bot to convert conversational context into intent-based work. Once intent is defined, the team uses Claude Code with multiple MCP tools for tech grooming, deep research, planning, and execution. Code artifacts (including system prompts) go through rigorous testing, cross-model review, evaluation, and human approval before reaching production.

### Back-Testing and Trace Analysis [10:45](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=645s)
The team calls trace analysis "back-testing" — using natural language to investigate the working system and improve starter evals. For Discord Chat, they built a process to profile chat turns both randomly and deterministically. A recent security dashboard review uncovered signals applicable beyond just security, enabling system hardening.

### Security Testing and Multilingual Challenges [11:48](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=708s)
Generating adversarial datasets proved difficult due to dev tooling terms and conditions. The team immediately encountered multilingual conversations in Discord — something they weren't prepared for — highlighting the need to account for multilingual adversaries. Automation numbers still need improvement, and adding human-in-the-loop will drive efficiency and enable tracking metrics like token cost per resolved case.

### Customer Impact and Three Key Lessons [12:18](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=738s)
A customer testimonial confirmed the system is helping customers build. Kormos emphasizes that the hard part is making AI work for the customer through a balanced combination of human and machine effort. Three takeaways: (1) treat agent engineering as its own discipline requiring a balance of product engineering and ML mindsets across the team; (2) build the "glass box" (observability) before building the agent — it's the base layer, not a feature added later; (3) the team is the multiplier — AI lets a small team do extraordinary things only if aligned for collective execution.

## Notable Quotes
- "Observability isn't a feature you add later. It's really the base layer and the starting point for everything else to materialize afterward."
- "The team is the multiplier. AI lets a small team do extraordinary things, but only if they are aligned for collective execution."
- "It's incredible what AI enables a small team to build, truly. The hard part — making it work for the customer in a balanced system — is the combination of human and machine effort."
- "Treat agent engineering as its own discipline... We really need a balance of product engineering and ML mindset strengths across the group of people, not just an individual."

## People, Tools & References Mentioned
- **Evan Kormos** — speaker, builder and manager of engineering teams at Coinbase
- **Harry** — PM who shapes and prioritizes the team's work
- **Caesar** — agent engineer who set up the Python/LangSmith proof of concept
- **Harrison** — referenced for emphasizing agent engineering as a discipline at a prior Interrupt event
- **Coinbase Developer Platform** — crypto APIs, wallets, payments, staking, infrastructure
- **LangSmith** — self-hosted tracing and evaluation infrastructure (operated by Coinbase's AI platform team)
- **LangSmith CLI** — used with Claude Code to inspect traces and find improvement signals
- **Claude Code** — used with MCP tools for tech grooming, research, planning, and execution
- **Remote MCP Server** — provides developer documentation to the agent
- **RAG fallback** — vector DB knowledge pipeline behind the MCP tool
- **Linear Slack bot** — converts conversational context to intent-based work
- **Coinbase Engineering blog** — referenced for more stories
- **Interrupt (LangChain event)** — the conference where this talk was delivered

## Who Should Watch
Engineering leaders and practitioners building customer-facing AI agents — especially those scaling support for developer platforms — will find practical value in Coinbase's architecture decisions, observability-first philosophy, and intent-based development workflow. The talk is particularly relevant for teams navigating the transition from basic chatbots to self-improving agentic systems with human-in-the-loop controls.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=6s">00:06</a></span> Hello, Interrupt. What a great event so far. I want to try to set up a strong finish with the story of one of our teams. My name is Evan Kormos. I&#x27;m a builder and manager of engineering teams at Coinbase. Today I&#x27;m excited to talk about our developer support engineering team and describe the transformation of what and how we shipped to scale AI support for crypto developers. It&#x27;s a story of how a small team was able to go from 0 to 1 on a self-improving, customer- facing agentic system.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=39s">00:39</a></span> Onto the agenda. First, we&#x27;ll frame up the support challenge and how we&#x27;re scaling for Coinbase developers. Next, I&#x27;ll discuss our approach for monitoring agent behavior. Then we&#x27;ll dive into some technical details and describe and show some of the capabilities and how they were produced. Throughout, I&#x27;ll be referencing team members — our agent engineers — to describe how this transformation unfolded, supported by Coinbase infrastructure, leadership,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=71s">01:11</a></span> and partners. First, a bit of setup so you know where we&#x27;re coming from. The Coinbase developer platform powers a community of developers building on crypto APIs, wallets, payments, staking, infrastructure — powering the on-chain economy. For a long time, our support model was people posting in our Discord server, and people answering in the Discord server. We added AI chat, and we&#x27;ll talk a little bit more about that.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=104s">01:44</a></span> Of course, this team is building with AI. I know there&#x27;s a lot of attention around this, especially with our company. But this is great, and I think it demonstrates our conviction to increase product velocity and quality. OK, let&#x27;s dive into the challenge. In order to scale, we needed to keep being great for a developer who was working to ship a side project or a trading bot. But now we have new challenges as we have new markets</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=135s">02:15</a></span> and new expectations entering into our scope. For this team working together on a common goal to serve the customer is focused by our PM, Harry, who helps shape this work and prioritize. So to recap: our goal was to keep customer satisfaction high while increasing automation levels. Let&#x27;s get into the story. As I mentioned, we started with our version one Discord chat. We started like a lot of teams and integrated a hosted chat service.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=167s">02:47</a></span> And honestly, the first version was fine. It answered developer questions. Sometimes the docs got stale. We had no way of knowing how people were using it. If it was doing a good job, we sort of had to manually tally the downvotes and the thumbs up and thumbs down. If you guys have done that before, you know where I&#x27;m coming from. So we really had no idea what was going on. A familiar situation. How do you stand up a new service that&#x27;s as good as the one that you have —</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=198s">03:18</a></span> or ideally better — and gets better over time? It did require some new capabilities I&#x27;ll talk about, paired with our existing paved roads. But the goal was to harness agent behavior. Here&#x27;s where we landed on system design. For delivery channels, we still meet customers where they are — in Discord and on the web — and on the backend, provide quality tools for support engineers.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=230s">03:50</a></span> With an agentic foundation, we could build more: partner Slack channels, new MCP channels, generative UX — a lot is possible with this setup. A huge unlock for us was including Python services as first-class infrastructure. This was the team&#x27;s first service of this type. We paired it with self-hosted LangSmith for tracing. A big driver of this transformation was Caesar, who is here today — you can chat with him.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=262s">04:22</a></span> Where are you? Raise your hand. There he is. All right. [laughs] A big driver. He set this up from proof of concept and brought these skills onto the team. For more stories like this, I&#x27;ll give a plug for the Coinbase Engineering blog. Also a big thank you to our AI platform team who operates LangSmith and other infrastructure for our team and others to use. Finally, we have our own set of shared tools.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=292s">04:52</a></span> A remote MCP server for developer documentation was used by the agent. For customer-facing agents, a remote MCP tool can be a bit unreliable. So what we did was add a RAG fallback. This is also a way for us to A/B test our own tool. So behind the MCP, we have a pretty basic knowledge pipeline feeding the vector DB, which is the RAG fallback.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=323s">05:23</a></span> Lastly, we hooked up to a variety of internal services, some event-driven, some proxying to external services. Bringing it all together. You have on-demand and ambient agent flows with our overall pulse on agent behavior. Building full stack and now adding AI — this team has already shipped agents within this framework, with more coming.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=354s">05:54</a></span> The first three we&#x27;ll showcase start with Discord AI Chat and Slack Triage. You&#x27;ll see how both of these are helping shape progress toward Discord public auto-response. The Support Engineer Assistant is an exciting new surface for helping customers. We&#x27;ll take a look at that if you promise not to judge. We&#x27;ve also built or are building a handful of compliance, risk reduction, and service quality related agents. OK, so this is our Discord Support bot, and there&#x27;s a menu where users can launch</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=387s">06:27</a></span> AI Chat, open a case, or open case management and other things. Soon the bot will be automatically able to respond on the channel when needed. Starting an AI Chat, a Discord developer can get expert responses to guide them with technical documentation or how to get further agent support.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=417s">06:57</a></span> He is our team member that picked these skills up and built a wonderful starting point for the Discord AI Chat you just saw. So we&#x27;ll dive a little bit more into the detail of how we handle customer inquiries safely. So even though our agent doesn&#x27;t have access to tools to transact or access sensitive data, you can see there was still a lot of care that went into detecting and preventing misuse. So when you hear the term guardrails, you can see there are deterministic safeguards in place. You can also see the developer documentation tool that we mentioned, which is needed for</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=453s">07:33</a></span> the initial version. LLM judgment was applied to the output using a lightweight model to evaluate the response for both accuracy and risk. This design was our starting point for public auto-response, and is also a way for us to safely handle customer inquiries going forward. So, onto our next agent: the Discord Support Triage in Slack. I&#x27;ll give you a second to check out the screenshots, but you can see within a Slack Triage channel,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=487s">08:07</a></span> we have messages surfaced internally based on what&#x27;s happening in Discord. We also have links that the team can provide directly into the LangSmith trace data on the initial version, as the classifiers are tuned. In the future, this can also serve as a lens and control plane to flag signals for improvement as part of the team&#x27;s workflow, or to view and keep track of the agents in motion.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=518s">08:38</a></span> All right. Onto our AI Assistant. You can see here, within our service console, we have a new Support Assistant that we&#x27;re trying out. It runs internally on a locally hosted React site. It allows the user to control the chat context based on what they can access in the underlying system. Initially read-only, we&#x27;ve set up the building blocks for human-in-the-loop and are excited to add functions like &quot;send customer response&quot; in the near future.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=549s">09:09</a></span> Because this can be popped out in a new window, we can have a responsive UX and really control the experience very well. I&#x27;m excited to see where this goes and the potential for broader adoption and impact. OK. So everything we do is intent-based. This is a little bit about the way we work. I&#x27;ll give a plug for the Linear Slack bot.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=580s">09:40</a></span> It does a great job of converting our conversational context to intent-based work. These tools may vary across teams. This is the way our team works. But everything we do is intent-based, like I said. Once we get the intent defined, we then go through a tech grooming process using Claude Code with a number of MCP tools to do deep research and begin planning and executing</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=610s">10:10</a></span> the work. We produce a number of code artifacts. Some could be system prompts and things like that. They go through a rigorous testing, cross-model review, and evaluation step, and human approval, before outputting and resulting in a production system. From the production system, we get traces and real-time evals, as we showed from the prior graph. We can then use the LangSmith CLI and Claude Code to look at the traces, find signals for</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=645s">10:45</a></span> improvement, and drive more intent from that. So let&#x27;s dive deeper. I&#x27;m calling it back-testing. Well, just looking at the traces. I think it&#x27;s a great way to begin to improve starter evals — go live — and is a great way to use natural language to investigate your working system. For us to perform a signal search in our Discord Chat, we built a basic process to look at the turns of the chat</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=678s">11:18</a></span> in a certain way — profiling them both randomly and deterministically. One example: we recently double-checked our security dashboards. What we found was applicable beyond just security. Deep-diving on specific threads, we were able to discover signals to improve or harden the system in various ways. On the topic of security testing, we thought an adversarial dataset would be good to have, but it turns out they&#x27;re not easy to generate — due to the terms and conditions of some of the dev tooling.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=708s">11:48</a></span> Also an observation: we almost immediately had multilingual conversations going on in our Discord — something we weren&#x27;t prepared for. But with regard to adversaries, consider multilingual adversaries. We still have some work to do on our automation numbers. Adding human-in-the-loop will really drive efficiency and provide more detailed levels of tracking, including how many tokens</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=738s">12:18</a></span> we&#x27;re spending to resolve a customer case. Looking at this customer testimonial, I was excited to learn that we&#x27;re helping customers build. It&#x27;s incredible what AI enables a small team to build, truly. The hard part — making it work for the customer in a balanced system — is the combination of human and machine effort. I&#x27;d really take three things away. One: treat agent engineering as its own discipline.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=773s">12:53</a></span> This was something Harrison really hit home on at last year&#x27;s Interrupt, and something we took to heart. We really need a balance of product engineering and ML mindset strengths across the group of people, not just an individual. Hiring and growing to balance these is super important. Two: build the glass box before you build the agent. Observability isn&#x27;t a feature you add later. It&#x27;s really the base layer and the starting point for everything else to materialize afterward.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=py9d6zTl4Dc&amp;t=806s">13:26</a></span> Three: the team is the multiplier. The team is the multiplier. AI lets a small team do extraordinary things, but only if they are aligned for collective execution. All right. I&#x27;d like to say thank you to everyone at LangChain and all the Interrupt sponsors for this great event. Thank you. [APPLAUSE]</p>

</details>
