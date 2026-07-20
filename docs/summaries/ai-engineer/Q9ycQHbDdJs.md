---
title: "Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio"
channel: "AI Engineer"
video_id: Q9ycQHbDdJs
url: https://www.youtube.com/watch?v=Q9ycQHbDdJs
published: 2026-07-20T06:25:01+00:00
generated: 2026-07-20T11:17:02+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/Q9ycQHbDdJs/hqdefault.jpg
---
# Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio

[![Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio](https://i.ytimg.com/vi/Q9ycQHbDdJs/hqdefault.jpg)](https://www.youtube.com/watch?v=Q9ycQHbDdJs)

[Watch on YouTube](https://www.youtube.com/watch?v=Q9ycQHbDdJs) · **AI Engineer** · 2026-07-20

## TL;DR
Armanas Povilionis argues that autonomous agents in scientific research need more than additional tools—they need a protocol for discovering, transacting with, and verifying external services across organizational boundaries. He introduces Froglet, a system that provides agents with verifiable receipts for every step of cross-organizational collaboration, enabling trustworthy, scalable scientific automation.

## Key Takeaways
- Scientific research is among the most valuable targets for agentic automation, but it depends on collaboration, not just local tool use.
- Giving agents more tools is like giving a cook better knives—it improves local efficiency but doesn't solve the supply-chain coordination problem.
- Agents need budgets and the ability to discover services, negotiate execution, and pay for work across organizations.
- Froglet is a protocol for agents to discover, transact with, and receive verifiable receipts for external data and services.
- The system integrates with existing payment rails, agent execution environments, and transport protocols without requiring a uniform software stack.
- Every Froglet node generates a cryptographic key pair used to sign an immutable chain of interactions: descriptors, offers, quotes, deals, invoices, and receipts.
- Providers register services on a marketplace; requesters discover them there but then communicate directly—no middleman required.
- Payments have two parts: a base payment to protect providers from spam requests, and a success fee to protect requesters from malicious providers.
- What once took years and millions of dollars as a bespoke enterprise project can be reduced to minutes and a few thousand tokens.
- Froglet is not itself an AI agent, but an interface designed specifically for agents to find and transact with one another.

## Detailed Breakdown

### The Problem with More Tools [00:01](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=1s)
Povilionis opens by identifying scientific research as one of the most valuable domains for agentic automation. After a decade in life sciences collaboration, he concludes that simply adding more tools will not enable research automation because science fundamentally relies on collaboration. For agents to collaborate autonomously, they need a chain of verifiable receipts proving every step and ensuring trust at scale.

### The Kitchen Metaphor [01:06](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=66s)
He contrasts two models. Giving agents more tools is like giving a cook better knives and more ovens—it boosts local speed and quality but only within one kitchen. Scientific work, however, is more like running a Michelin-starred restaurant: outcomes depend on suppliers, service quality, and consistent reproducibility. The real challenge is aligning the entire supply chain, not improving local tools.

### From Cooks to Executive Chefs [02:10](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=130s)
Today's agents already have plenty of tools, but data and specialized analytics live in silos across organizations. Povilionis predicts that as agentic automation matures, organizations will give agents budgets—not just token budgets per task, but broader budgets to manage discovery, data requests, negotiation, execution, and payment across organizational boundaries. At that point, an agent stops being a cook and becomes an executive chef: finding suppliers, ordering ingredients, coordinating work, and keeping records.

### Introducing Froglet [03:42](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=222s)
Froglet is the protocol Povilionis's company, Alithea, is building to address this need. It enables agents to discover, transact with, and receive verifiable receipts for external data and services. Froglet sits between many moving parts and integrates with existing payment rails, agent execution environments, and network transport protocols. It does not require everyone to share the same software stack—only the same interface. Interested users can visit froglet.dev to run Froglet locally with one command or try it remotely with one prompt.

### The Cost of Bespoke Collaboration [05:15](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=315s)
Povilionis notes that close scientific collaboration today often becomes a bespoke enterprise project costing millions and taking years before the first reusable workflow exists. Froglet's mission is to simplify this dramatically: once an organization deems a resource shareable, a provider exposes it via Froglet, and an agent can discover it, understand its terms, request work, and receive a verifiable receipt in minutes for a few thousand tokens.

### How the Froglet Network Works [06:18](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=378s)
The Froglet network consists of homogeneous nodes—every actor runs the same core node but plays a different role: requester, provider, or marketplace. The marketplace is simply a Froglet node running a specialized service. The system solves four problems: how requesters find providers, how they trust them, how they settle payments, and how they prove execution happened. Each node generates a cryptographic key pair for identity and signing, and every action is signed on-chain, forming an immutable sequence from descriptors to offers, quotes, deals, invoices, and receipts. Tampering with any part breaks the chain.

### Discovery, Direct Communication, and Payments [07:57](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=477s)
Providers register and describe their services on the marketplace, which indexes available services. When a requester queries the index, it then communicates directly with the chosen provider—no middleman is involved. The entire interaction—request, signing, execution, and receipt—happens in one flow. Payments, when not free, have two components: a base payment protecting providers from spam or attack, and a success fee protecting requesters from malicious providers.

### What Froglet Is—and Is Not [09:33](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=573s)
Povilionis clarifies that Froglet itself is not an AI agent. It is an interface created specifically for agents to find each other, discover data and services across borders, and execute deals directly. In summary, Froglet lets agents discover external scientific resources, execute work across organizational boundaries, and receive verifiable receipts—opening the door to autonomous scientific progress.

## Notable Quotes
- "For agents to collaborate autonomously, we need a chain of verifiable receipts."
- "Giving them more tools improves kitchen's efficiency... but it only enhances local work. Scientific work is not cooking alone in your own kitchen. It is closer to running a Michelin star restaurant."
- "The agent is no longer just a cook with a better knife. It starts acting like an executive chef, finding suppliers, ordering ingredients, coordinating kitchen work, and keeping a record of everything."
- "It does not require that everyone has the same software stack. It just requires that everyone has the same interface."
- "Close scientific collaboration often turns into a bespoke enterprise project that can take years and cost millions before even first reusable workflow exists."
- "Froglet itself is not an AI agent, but it is created specifically for agents as an interface to find each other."

## People, Tools & References Mentioned
- **Armanas Povilionis** — speaker, Alithea Bio
- **Alithea (Bio)** — the company building Froglet
- **Froglet** — protocol for agent discovery, transaction, and verifiable receipts across organizational boundaries
- **froglet.dev** — project website with documentation, local run instructions, and a walkthrough

## Who Should Watch
AI engineers, research technologists, and life sciences professionals interested in how agents can autonomously collaborate across organizational silos—and anyone exploring the infrastructure needed for trustworthy, cross-boundary agent transactions.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=1s">00:01</a></span> What is the most valuable agentic automation work? I think scientific research is quite high on that list. After a decade working in life sciences collaboration projects, I think that more tools alone will not enable automation of scientific research. Because science work relies on</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=33s">00:33</a></span> Because science work relies on collaboration. For agents to collaborate autonomously, we need a chain of verifiable receipts. We need a solution which can provide these receipts proving every step, ensuring that every result can be trusted, and enabling collaboration at scale. Let&#x27;s step back. Imagine an Imagine agents as cooks in the kitchen.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=66s">01:06</a></span> Giving them more tools improves kitchen&#x27;s efficiency. Better knives, more pans, more ovens boost the speed and quality. But it only enhances local work. Scientific work is not cooking alone in your own kitchen. It is closer to running a Michelin star restaurant. The outcomes depend on suppliers and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=97s">01:37</a></span> The outcomes depend on suppliers and their produce, the level of service that you can provide, and an ability to consistently deliver the same quality dish again and again and again. You can cannot bring everything into one kitchen. The challenge isn&#x27;t local tools. It is aligning the entire supply chain. Today we already have plenty of tools</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=130s">02:10</a></span> Today we already have plenty of tools for agents and agent automation. On other hand, we also have data and specialized analytics algorithms, which are distributed across organizations and and and live in silos. At Alifeia, our vision for Froglet is very simple. As agentic workflow automation matures,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=160s">02:40</a></span> As agentic workflow automation matures, organizations will not just give agents more tools, they will allocate them budgets. We already kind of doing it in a primitive way, allocating them token budgets per task. The next step is a bit broader. It&#x27;s allowing agents to manage their own budget for anything that they might need,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=190s">03:10</a></span> anything that they might need, discovering services, requesting data, negotiating execution, paying for work in cross-organizational boundary setting. At that point, the agent is no longer just a cook with a better knife. It starts acting like an executive chef, finding suppliers, ordering ingredients, coordinating kitchen</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=222s">03:42</a></span> coordinating kitchen the kitchen work, and keeping a record of everything what&#x27;s happening. That is why we&#x27;re building Froglet. The protocol for a agents to discover, transact with, and receive verifiable receipts for external data and services and service providers. Froglet is designed to sit in between of many moving parts.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=253s">04:13</a></span> many moving parts. And that&#x27;s why we are not replacing existing tools and protocols. We integrate with different payment rails, with different agent and harnesses, execution environments, and even network transport protocols. It does not require that everyone has the same software stack. It just requires that everyone has the same interface.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=283s">04:43</a></span> For more details, please visit froglet.dev. Where you will be able to run to see how to run Froglet locally with just one command. Or you can even try Froglet remotely with just one prompt. So, in essence, close scientific collaboration often turns into a bespoke enterprise project.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=315s">05:15</a></span> That can take years and cost millions before even first reusable workflow exists. On the other hand, the Froglet&#x27;s mission is to simplify that much more. Once your organization has deemed that the resource is shareable, a provider should be able to expose it for Froglet. An agent can discover it,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=347s">05:47</a></span> An agent can discover it, understand its terms, request the work, and receive verifiable receipt. That costs few thousand tokens and takes minutes. Let&#x27;s deep dive a bit deeper. So, here is our Froglet Dev website, and here you can see um a walkthrough button. If you click on</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=378s">06:18</a></span> a walkthrough button. If you click on it, you will have a much more detailed review of what&#x27;s happening, and you can read documentation in even more detail. So, first of all, the Froglet network consists of homogeneous nodes. Every single actor in the environment runs the same core um node. It just plays a different role. There are requesters, there are providers, and there is a marketplace, which is a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=410s">06:50</a></span> and there is a marketplace, which is a just a Froglet running the specialized service. What it solves is how to find how for a requester to find the providers, how to trust them, how to battle pay or settle, and how to prove that execution has happened. Whenever you&#x27;re generating a new node, you&#x27;re generating a key pair for</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=442s">07:22</a></span> you&#x27;re generating a key pair for identity and signing. And every time you execute anything with Froglet, it uses your keys to sign on the chain. And the chain consists of everything what you do, from descriptors to offer to quote to deal for invoice and finally receipt. Therefore, you cannot tamper with any part of this chain. Otherwise, the chain will be broken.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=477s">07:57</a></span> And to discover services, providers of services, just register and describe their services to the marketplace. Marketplace itself provides the services for providing descriptions and for indexing what&#x27;s what is existing what services existing on the marketplace. Once a requester requests an index of available services, from there on, it continues direct communication with that requester.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=509s">08:29</a></span> communication with that requester. It doesn&#x27;t need a middleman. So, the requester and provider communicates with each other directly, and it all happens in one interaction: requests, signing, execution, and receipt. On a payment side, we have a system where it where all payments, if it&#x27;s not free, has two parts. One is a base payment, and another is success fee.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=541s">09:01</a></span> payment, and another is success fee. So, base payment protects the providers that they wouldn&#x27;t be attacked by uh multiple requests. And success fee is providing the requesters from malicious providers. In essence, the Froglet [snorts] itself is not an AI agent, but it is created specifically for agents as an interface to find each other.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=573s">09:33</a></span> as an interface to find each other. As an interface to find the data and services cross borders and execute these deals directly with each other. So, coming back to recap, a froglet lets agent to discover external scientific resources, execute work across organizational boundaries, and it gives every transaction a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q9ycQHbDdJs&amp;t=605s">10:05</a></span> and it gives every transaction a verifiable receipt. Together, this opens the door to autonomous scientific progress. We hope you will join us and enjoyed this talk. Thank you.</p>

</details>
