---
title: "The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab"
channel: "AI Engineer"
video_id: sum9DgexFRQ
url: https://www.youtube.com/watch?v=sum9DgexFRQ
published: 2026-07-12T14:00:07+00:00
generated: 2026-07-12T19:59:41+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/sum9DgexFRQ/hqdefault.jpg
---
# The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab

[![The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab](https://i.ytimg.com/vi/sum9DgexFRQ/hqdefault.jpg)](https://www.youtube.com/watch?v=sum9DgexFRQ)

[Watch on YouTube](https://www.youtube.com/watch?v=sum9DgexFRQ) · **AI Engineer** · 2026-07-12

## TL;DR
Project Nanda, an MIT Media Lab research initiative, is building open infrastructure for an "internet of AI agents"—a discovery, identity, and coordination layer that lets agents from different organizations find, trust, and transact with each other without walled gardens. The project ships the Nanda Index for agent discovery, supports self-hosted agents via Open Claw, and tests large-scale agent coordination in a sandbox simulator called Nanda Town.

## Key Takeaways
- **The "AOL to open web" analogy**: Today's agents live in closed, proprietary platforms; Project Nanda wants to move them to an open, permissionless web where any agent can talk to any other.
- **Three layers to build**: discovery (finding agents), commerce (transacting and trusting), and the "bazaar" (open coordination).
- **An agent is a model using tools in a loop**—not just a chatbot—and needs real access to tools, which makes open-source, self-hosted gateways like Open Claw important.
- **Nanda Index is the discovery layer**: it returns an "agent card" and a signed "agent facts record" so agents can verify identity, capabilities, permissions, and endpoints before connecting.
- **Adaptive resolution**: one agent can have many endpoints; the index routes traffic to the best one and can hide private details based on who is asking.
- **Onboarding is inclusive**: enterprises can register from their own domain, existing sites can use DNS AID, and individuals can use host39.org to get a hosted agent URL.
- **Hosting matters at scale**: Maritime offers sleep/wake architecture so idle agents don't burn compute, making it cheaper to run many agents.
- **Nanda Town is a simulation sandbox**: an open-source, laptop-runnable discrete-event simulator that models the full agentic economy—discovery, messaging, auctions, voting, supply chains—across 12 infrastructure layers.
- **You can plug in one layer**: Nanda Town is modular; contributors can swap in their own version of a single layer (e.g., trust, payments, registry) and test it against the rest.
- **Two simulation tiers**: tier one uses scripted agents; tier two swaps in real AI models.

## Detailed Breakdown

### Welcome and Framing [00:01](https://www.youtube.com/watch?v=sum9DgexFRQ&t=1s)
Ramesh Raskar introduces the talk as a walkthrough of open infrastructure for a "web of agents," originating from Project Nanda at MIT. By the end, viewers should know how to put their own agent on the open web independently.

### What Is Nanda and Why It Needs to Exist [00:36](https://www.youtube.com/watch?v=sum9DgexFRQ&t=36s)
Nanda stands for "Network AI Agents in a Decentralized Architecture." It addresses a concrete gap: agents lack a shared way to find each other across vendors, portable identity/trust not owned by one platform, and an open method to transact across organizations. Nanda ships the index, registries, protocol, and the Nanda Town Simulator.

### The Scale Problem: Trillions of Agents [01:39](https://www.youtube.com/watch?v=sum9DgexFRQ&t=99s)
The internet will eventually host trillions of autonomous agents that negotiate, delegate, and migrate between hosts in milliseconds. This load is fundamentally different from the human web and strains document-era systems like DNS.

### The AOL Analogy and the Coming Open Agent Web [02:10](https://www.youtube.com/watch?v=sum9DgexFRQ&t=130s)
Today's agent ecosystem resembles the late-'90s AOL era: closed networks, gated directories, proprietary stores. Just as AOL gave way to the open web—where any website could talk to any browser—the agent world needs the same transition to permissionless, cross-organizational discovery and coordination. Raskar names three layers to keep in mind: discovery, commerce, and the bazaar.

### What Is an Agent? (Maria) [03:44](https://www.youtube.com/watch?v=sum9DgexFRQ&t=224s)
Maria defines an agent as a model that uses tools in a loop: given a goal, it decides what to do, calls a tool, inspects the result, and continues until the task is done. Memory, orchestration, and multi-agent systems build on this core loop.

### Open Claw: Self-Hosted Agent Gateway [04:16](https://www.youtube.com/watch?v=sum9DgexFRQ&t=256s)
Open Claw is a self-hosted agent gateway that connects to real apps and tools. Because agents doing real work need real tool access, who controls the agent, where it runs, and how transparent it is matters—making open-source, self-hosted agents important for user control.

### The Nanda Index: Discovery Layer [04:47](https://www.youtube.com/watch?v=sum9DgexFRQ&t=287s)
With agents running in many places, the problem becomes mutual discovery. The Nanda Index is the discovery layer for the agentic web—analogous to DNS but richer. Where DNS maps a name to an address, the index returns an "agent card" describing what an agent does, its tools, rules, and how to reach it. Messages go to a "message box" first, which checks sender identity, handles access, filters spam, and holds messages until the agent is ready.

### Agent Facts Record and Adaptive Resolution [05:48](https://www.youtube.com/watch?v=sum9DgexFRQ&t=348s)
The "agent facts record" is a signed record stating who the agent is, what it can do, what it is allowed to touch, who built it, and where to reach it—enabling trust before connection. The index is not a static lookup: it can return updated facts based on the request, support multiple endpoints per agent, route traffic to the best endpoint, and hide private details. Resolution is adaptive to location, requester identity, and permissions.

### How to Get on the Index [06:49](https://www.youtube.com/watch?v=sum9DgexFRQ&t=409s)
Onboarding paths: enterprises run their own catalog and register their gateway from their own domain; existing websites use DNS AID to attach agents to domains they own; small businesses and individuals use host39.org to fill out an agent facts form and get a hosted agent URL without their own domain. The goal is universal onboarding, from large companies to solo developers.

### Where Agents Run: Local vs. Cloud Hosting [07:52](https://www.youtube.com/watch?v=sum9DgexFRQ&t=472s)
Agents must stay online and be reachable. Local hosting gives full control but puts uptime responsibility on the owner. Cloud options include general clouds like AWS (enterprise-ready) and agent-specific platforms like Maritime, which offers sleep/wake architecture so idle agents don't keep burning compute—key for running many agents affordably.

### Nanda Town: Simulating the Agentic Web [09:24](https://www.youtube.com/watch?v=sum9DgexFRQ&t=564s)
The hard problems live between agents at scale: discovery, identity, trust, and coordination with no central authority. Nanda Town is an open-source simulation sandbox that models the full agentic economy—discovery, identity, registries, messaging, coordination. It is small enough to run on a laptop and lets you watch agents on a map, see messages move in real time, compare protocol results, and replay runs step by step.

### Real Experiments in Nanda Town [10:28](https://www.youtube.com/watch?v=sum9DgexFRQ&t=628s)
Nanda Town already runs experiments: a marketplace with price negotiation, auctions with bidding, voting tests with ballot submission and counting, plus consensus and supply-chain tests. The goal is to study real coordination problems—deal-making, decision agreement, message passing, and recovery from failures.

### The 12 Layers and Modular Participation [10:58](https://www.youtube.com/watch?v=sum9DgexFRQ&t=658s)
Nanda Town decomposes the agentic web into 12 parts: transport, communication, identity, registry, auth, trust, payments, coordination, negotiation, memory, privacy, and data effects. Contributors can take one layer, add their own version, and test it within the full network. The simulator runs as a discrete-event simulation driven by a short YAML scenario file, with tier one using scripted agents and tier two swapping in real AI models.

### Summary and Resources [11:30](https://www.youtube.com/watch?v=sum9DgexFRQ&t=690s)
Project Nanda provides open infrastructure for an internet of AI agents: discovery via the index, commerce via portable identity and trust, and coordination via open protocols—all tested in Nanda Town. More information, papers, and projects are available at projectnanda.org.

## Notable Quotes
- "The internet is about to host not millions or billions, but eventually trillions of autonomous agents. They negotiate, they delegate, they migrate between hosts in milliseconds. That's a fundamental different load than the human web, and it strains the identity and discovery system we built for documents, DNS among them."
- "If you're building agents today, you're mostly building them or you're forced to build them inside walled gardens, closed platforms, proprietary agent stores, and orchestrations that only talk to itself… This is like the AOL era from the late '90s where it was a closed network."
- "An agent is a model that uses tools in a loop… you give it a goal, it decides what to do next, it calls a tool, it looks at the result, then it keeps going until the task is done."
- "If an agent is going to do real work, it needs to access your real tools and apps. And if it has access to real tools, we should care about who controls it, where it runs, and how much we can see."
- "The hard problems of the agent web live between agents at scale—how thousands of them discover each other, prove who they are, decide whom to trust, and coordinate with no central authority."

## People, Tools & References Mentioned
- **Ramesh Raskar** — Professor at MIT, director of Project Nanda
- **Maria** — Core contributor to Project Nanda
- **Project Nanda** (projectnanda.org) — Open research effort: "Network AI Agents in a Decentralized Architecture"
- **Nanda Index** — Discovery layer for the agentic web
- **Agent facts record / agent card** — Signed identity and capability records for agents
- **Open Claw** — Self-hosted agent gateway
- **host39.org** — Portal for individuals and small businesses to register agents
- **DNS AID** — Mechanism to attach agents to existing domain names
- **Maritime** — Agent hosting platform with sleep/wake architecture
- **Nanda Town** — Open-source discrete-event simulation sandbox for agentic networks
- **AOL** — Referenced as the analogy for today's closed agent platforms
- **AWS** — Mentioned as an enterprise-ready general cloud option
- **12 Nanda Town layers** — Transport, communication, identity, registry, auth, trust, payments, coordination, negotiation, memory, privacy, data effects

## Who Should Watch
AI engineers, platform builders, and researchers who want to understand how a decentralized, open infrastructure for agent discovery, trust, and coordination could work—and how to register and host their own agents on it. It's especially relevant for anyone thinking about interoperability, agent identity, or large-scale agent simulation.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=1s">00:01</a></span> Welcome everyone. Over the next few minutes, we&#x27;re going to talk about the open infrastructure being built for a web of agents. Why it&#x27;s needed, what&#x27;s already shipped, and exactly where your own agent fits into it. It comes out of Project Nanda, an open research effort that started at MIT. And by the end of this presentation, you will know how to put an agent that you build yourself on the open web all by yourself. So, let&#x27;s get into it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=36s">00:36</a></span> I&#x27;m Ramesh Raskar, professor and at MIT and director of Project Nanda. And Maria is a core contributor to Project Nanda. So, first, what is Nanda and why does it need to exist? Nanda, which stands for network AI agents in a decentralized architecture, is an open research building the infrastructure for an internet of AI agents, the way open web was built for documents. The gap it fills is concrete. Agents</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=67s">01:07</a></span> The gap it fills is concrete. Agents have no shared way to find each other across vendors, no portable identity or trust that isn&#x27;t owned by a single platform, and no open way to transact and coordinate across organizations. Nanda builds that missing layer and ships it in open. The index, the registries, the protocol, and the Nanda Town Simulator you will see later. Here&#x27;s the premise that drives it all of it. The internet is about to host not</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=99s">01:39</a></span> it. The internet is about to host not millions or billions, but eventually trillions of autonomous agents. They negotiate, they delegate, they migrate between hosts in milliseconds. That&#x27;s a fundamental different load than the human web, and it strains the identity and discovery system we built for documents, DNS among them. The web that&#x27;s coming needs infrastructure of its own. And we have been here before. If you&#x27;re</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=130s">02:10</a></span> And we have been here before. If you&#x27;re building agents today, you&#x27;re mostly building them or you&#x27;re forced to build them inside walled gardens, closed platforms, proprietary agent stores, and orchestrations that only talk to itself. And it kind of works. But, you know, it also feels similar because we have been this we have been here before. This is like the AOL era from the late &#x27;90s where it was a closed network. You know, AOL, you got the CDs and you installed it on your PC. It was a closed network. It was a gated directory. You live</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=161s">02:41</a></span> It was a gated directory. You live inside the garden created by this one company called AOL. And what came after AOL was this open web. You know, everybody&#x27;s in a permissionless manner creating websites, creating browsers, and any website can talk to any browser. And that&#x27;s the transition that&#x27;s about to happen to agents as well. So, the next era needs what the web needed, an open infrastructure where an agent from one company or one entity can discover agent from another.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=193s">03:13</a></span> entity can discover agent from another. That agent can hand off work to it, pay it, learn from it across organizational boundaries, no permissions required. There are three layers here, discovery, commerce, and what I will call the bazaar. So, hold on to those three concepts. We&#x27;ll come back to them and and discussed. So, first the basics. Hey, my name is Maria and I&#x27;m a core contributor to Project Nondo. So, let&#x27;s start with a simple definition of an agent. The way I think about it, an agent is a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=224s">03:44</a></span> The way I think about it, an agent is a model that uses tools in a loop. Right, you give it a goal, it decides what to do next, it calls a tool, it looks at the result, then it keeps going until the task is done. So, that loop is the core idea. Everything else, like memory orchestration and multi-agent systems, is built on top of it. So, you can build this agent loop in many different ways. One example is Open Claw. So, Open Claw is a self-hosted agent gateway. That means you can run it yourself and connect it to the apps and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=256s">04:16</a></span> yourself and connect it to the apps and tools you already use. This matters because agents are not just chatbots. If an agent is going to do real work, it needs to access your real tools and apps. And if it has access to real tools, we should care about who controls it, where it runs, and how much we can see. And that is why open-source self-hosted agents are super important. They give people more control over their own agents. But then, we get a new problem. If agents are running in many different</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=287s">04:47</a></span> agents are running in many different places, locally and on the clouds, on many different servers, like owned by many different people, how do they find each other? And that is the job of the index. And this is what the Nanda index is built for. Nanda index is the discovery layer for the agentic web. It gives agents a shared place to publish who they are, what they can do, and how other agents can reach them. The regular internet already has a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=318s">05:18</a></span> The regular internet already has a version of this with DNS. So, DNS maps a name to an address, so your browser knows where to go. But agents need more than an address. They need to know what another agent does, what tools it can use, what rules it follows, and how to talk to it. The index gives agents a common way to find each other and connect. So, here&#x27;s how the index works. An agent starts with the an identity like</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=348s">05:48</a></span> starts with the an identity like agent@hotmail.com. The NANDA index takes that identity and returns an agent card. So, the card says what an agent is, how to reach it, and where to send the messages. Messages do not go straight to the agent&#x27;s runtime. They go to the message box first. The message box checks who is sending the message, handles access, filters spam or bad requests, and holds the message until the agent is ready.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=379s">06:19</a></span> the message until the agent is ready. Now, the agent facts record is what makes discovery trustworthy. It is a signed record that tells other agents who this agent is, what it can do, what it is allowed to touch, who built it, and where to reach it. So, before one agent connects to another, it can check the basic facts first. Now, the index is not just a lookup table. It does not point to one name to one fixed address. It can return updated agent facts based on the request. So, that means one agent can have many</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=409s">06:49</a></span> that means one agent can have many endpoints. Traffic can be routed to the best one, and private details do not have to be exposed. So, the resolution is adaptive. It changes based on where the agent is, who&#x27;s asking, and what they are allowed to access. So, how do you put your agent on the index? You start at host39.org. So, you fill out the agent facts form, get an agent card, and publish it to the NANDA index. Once it&#x27;s listed, other agents can find it and know how to reach it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=441s">07:21</a></span> it and know how to reach it. So, there are a few ways to get onto the index, depending on who you are. Enterprises can run their own catalog and register their gateway from their own domain. Existing websites can literally use DNS AID to connect agents to domains they already own. Small businesses and individuals can use host39, fill out the agent facts form, and get a hosted agent URL without needing their own domain. Goal is to make the onboarding work for everyone, from a large company to one person with a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=472s">07:52</a></span> large company to one person with a personal agent. Now that we know how agents get listed on the index, the next question is, where does the agent actually run? To be useful, an agent needs to stay online and be reachable. You can run it locally, which gives you full control, but then you&#x27;re responsible for keeping it up. For most use cases, it makes more sense to host it on the cloud. That could be on a general cloud like AWS, which is more enterprise ready, or</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=502s">08:22</a></span> AWS, which is more enterprise ready, or on an agent hosting platform like Maritime, which is built to make hosting AI agents cheaper and simpler. So, a little bit about Maritime. Hosting one agent can be affordable, but the cost problem starts when you want to run many agents at once, for a team, a product, or a simulation. That is where per agent cost really matters. And Maritime is one way to solve this. It gives you a simple cloud default for running Open Clo or other agents with sleep and wake architecture, so idle</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=533s">08:53</a></span> sleep and wake architecture, so idle agents do not keep burning compute. And the point is to make running many agents practical, cheap, and simple. So, you can host an agent and list it on the index, but getting one agent online was always the easy part. The hard problems of the agent web live between agents at scale. So, how thousands of them discover each other, prove who they are, decide whom to trust, and coordinate with no central authority. So, you can&#x27;t just assume that protocols will hold up under the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=564s">09:24</a></span> that protocols will hold up under the load, and you have to test and run them and watch when they break. So, that&#x27;s exactly where Nanda town comes in. So, how do you prove an open agent web actually works before it&#x27;s load bearing on the real internet. You simulate it. This is Nanda Town, an open-source project from Project Nanda. The easiest way to describe it is it&#x27;s a simulation playbook for the infrastructure of the Agoric platform. So, think of it as a sandbox town where the whole Agoric economy is modeled,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=596s">09:56</a></span> the whole Agoric economy is modeled, like discovery, identity, registries, messaging, messages, coordination, all of it. So, you can run and test it on scale. Here&#x27;s what it looks like in practice. Nanda Town is a live sandbox for testing Agoric networks. You can see agents on a map, watch messages move in real time, compare protocol results, and replay a run step by step. It&#x27;s fully open source, it&#x27;s small enough to run on your own laptop, and built to make Agoric networks easier to test and understand.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=628s">10:28</a></span> test and understand. Nanda Town is already running real experiments. For example, there is a marketplace where buyers and sellers negotiate prices, an auction where agents bid on items, and and a voting test where agents submit and count ballots. There are also tests for consensus and supply chains. The point is to study real coordination problems, how agents make deals, agree on decisions, pass messages, and recover when something breaks. Under the hood, Nanda Town breaks the Agoric web into 12</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=658s">10:58</a></span> Nanda Town breaks the Agoric web into 12 parts. Transport, communication, identity, registry, auth, trust, payments, coordination, negotiation, memory, privacy, data effects. Each part is something a real Agoric platform needs. So, the registry layer is the Nanda index we just walked through, but here it is just one piece of a bigger system. And you do not need to build everything to try it. You can take one layer, add your own version, run it inside Nanda Town, and see how it works with the rest of the network. So, Nanda Town runs as a discrete event</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=690s">11:30</a></span> So, Nanda Town runs as a discrete event simulation. You define a scenario in a short YAML file, inject agents and traffic, and the test bed plays plays it out so you can measure what actually happens end-to-end. Tier one uses simple scripted agents, and tier two swaps in real AI models. So, to summarize, Project Nanda builds the open infrastructure for an internet of AI agents. Discovery through the index, commerce through portable identity and trust, and coordination through open protocols, all tested in Nanda Town.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=sum9DgexFRQ&amp;t=721s">12:01</a></span> Nanda Town. And if you want to learn more, uh you can go to projectnanda.org, read our papers, and um check out our latest projects.</p>

</details>
