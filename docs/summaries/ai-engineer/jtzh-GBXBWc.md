---
title: "The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft"
channel: "AI Engineer"
video_id: jtzh-GBXBWc
url: https://www.youtube.com/watch?v=jtzh-GBXBWc
published: 2026-07-11T20:00:27+00:00
generated: 2026-07-12T21:27:45+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/jtzh-GBXBWc/hqdefault.jpg
---
# The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft

[![The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](https://i.ytimg.com/vi/jtzh-GBXBWc/hqdefault.jpg)](https://www.youtube.com/watch?v=jtzh-GBXBWc)

[Watch on YouTube](https://www.youtube.com/watch?v=jtzh-GBXBWc) · **AI Engineer** · 2026-07-11

## TL;DR

Rushabh Doshi runs Machinecraft, a 100-person thermoforming factory in India with no data science team, yet he built "Eira"—a system of 36 specialized AI agents that runs the company's entire go-to-market operation. Rather than training models, the system relies on well-organized memory (vectors + knowledge graphs), biological metaphors (senses, gut, dream cycle, immune system), and a strict "Eira drafts, human sends" rule—all built for roughly $30K instead of the $230K an agency quoted, and now forkable as "Brain OS" at forkmybrain.org.

## Key Takeaways

- **No model training required.** The system uses off-the-shelf LLMs reading chunked company history—stored as vectors and relationship graphs—rather than fine-tuning or training anything from scratch.
- **36 specialist agents beat one mega-prompt.** Each agent has exactly one job (pricing, machine specs, fact-checking, guarding corrections, etc.), and they hold "meetings" where they argue and converge on answers.
- **Memory is engineered in layers.** Working memory, pinned facts, episodic stories, relationships with warmth, and a salience gate that filters what's worth remembering—preventing the "goldfish" problem of raw LLMs.
- **A nightly "dream cycle" consolidates learning.** Eira replays the day, locks in useful information, hunts contradictions, forgets stale junk, and produces a morning dream report.
- **Every agent has a "soul file" based on Jain family-business principles.** Guardrails include cross-checking before speaking, never stating things absolutely, citing documents and dates, and reporting ugly truths.
- **The golden rule: "Eira drafts, human sends."** Nothing goes out without human approval.
- **Cost was dramatically lower than expected.** An agency quoted $230K; they built it for ~$30K, with operating costs of a couple thousand dollars per month.
- **The architecture is forkable.** Called "Brain OS," it ships as an empty nervous system—agents, memory, dream cycle, soul file—ready for any company to pour its own truth into.
- **The real expense isn't compute—it's teaching a company to remember itself.** Only the company itself can build its own brain; it can't be outsourced.
- **The system runs nine concrete go-to-market jobs daily**, from outbound emails to lead revival, qualification, quotations, and account briefs.

## Detailed Breakdown

### Introduction: A Factory That Remembers [00:00](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=0s)
Rushabh introduces himself as the operator of Machinecraft, a 100-person factory in India with no data science team or ML budget. Despite this, the company built a system of 36 AI agents (he initially says 39 in the title but clarifies 36 in the talk) that runs their entire go-to-market operation. He frames the story as both ridiculous and replicable.

### The Real Company Is Knowledge, Not Machines [00:32](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=32s)
From the outside, Machinecraft looks like machines and metal, but the actual company is the knowledge: who the customer is, what was quoted in 2019, why a machine needed a custom tweak. For three generations, all of that lived in exactly three brains—his grandfather's, his father's, and now his. He describes this as "a genuinely terrifying way to run a company."

### The Fear of Forgetting [01:02](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=62s)
People joined and left constantly, and every departure meant a chunk of the company's brain walked out the door. The fear wasn't competitors—it was forgetting, or waking up to find the entire company existed only inside "two increasingly tired heads." This motivated the idea of growing a brain that held the knowledge, not just writing documents nobody reads.

### The Messy Reality of the Business [01:32](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=92s)
Machinecraft makes thermoforming machines that heat and shape plastic sheets. The same core machine serves seven completely different worlds: hydroponic farm trays, spa bathtubs, EV car panels, medical casings, packaging, and more. Each world has totally different buyers, so the brain couldn't just memorize a brochure—it had to understand which universe a given customer lives in.

### Step One: Feed It Everything [02:03](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=123s)
They fed the system everything—years of quotes, drawings, payment schedules, timelines, email threads, hundreds of gigabytes of private company history. Not the public internet, but "our internet." The key plot twist: they never trained a model. No GPUs, no fine-tuning. They chunked the history and let off-the-shelf models read it and extract facts, storing meaning as vectors and relationships in a graph. The brain isn't a smarter model; it's "a really, really well-organized memory."

### Biological Metaphor for the Architecture [03:05](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=185s)
They stopped thinking of Eira as software and started thinking of it as something they were raising. They modeled it on biology: senses to identify who it's talking to, a gut to digest documents into facts, memory, a dream cycle, and an immune system to fight off bad information. The rationale: evolution spent a billion years solving how to stay coherent over time, so they "copied the homework."

### Why 36 Agents Instead of One Mega-Prompt [04:08](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=248s)
One prompt that does everything ends up doing everything badly. Eira is a "pantheon" of specialist agents, each with one job: Athena runs the room, Prometheus owns the sale, Plutus does pricing, Hephaestus knows machine specs, Vera fact-checks everything, and Memnon guards corrections so that once a human fixes something, it stays fixed forever. The agents hold meetings, argue, and produce a single answer—"a board room that never sleeps, never gets tired, and somehow has no ego."

### Nine Concrete Jobs Eira Runs Daily [05:09](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=309s)
Eira handles the entire front-of-business: outbound emails referencing the real world, account briefs from cross-checked truths, quotations, a "swipe left, swipe right" outreach mode, reviving dead leads ("blast from the past"), inbound replies, and qualifying whether a company is even a fit before wasting time. Nine jobs, one operator that never sleeps.

### The Stack: One Cursor Tab, Real Infrastructure [06:11](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=371s)
Everything runs in one Cursor tab. Under the hood it's a genuine stack: databases for vectors, relationship graphs, and CRM; three different model providers chosen by job; tools for Google, document ingestion, communication channels, and monitoring. All capabilities are exposed as 213 tools over one protocol. The golden rule never broken: "Eira drafts, human sends."

### Engineered Memory in Layers [06:41](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=401s)
Raw language models are "goldfish"—brilliant for 30 seconds, then they forget. Eira's memory is engineered in layers: working memory for the last few minutes, pinned facts about individuals, episodic memories stored as little stories, relationships with warmth that grows from stranger to trusted, and a salience gate acting as a bouncer that decides what's worth remembering. When two facts disagree, corrections win, ensuring continuity without fabrication.

### The Dream Cycle [07:43](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=463s)
Every night, Eira runs a sleep cycle: it replays the day, locks in useful information, hunts for contradictions, gently forgets stale junk, and turns the day's work into reusable skills. A morning "dream report" summarizes what was consolidated, what was let go, and what was figured out overnight. "The thing literally gets smarter overnight."

### Every Agent Has a Conscience: The Soul File [08:13](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=493s)
Each agent has a "soul file" based on Jain family-business principles from three generations. Five old ideas became engineering rules: no single source has the whole truth (cross-check before speaking), never say things absolutely (cite the document and date), do your own job, report the truth even when ugly, and nobody works alone. "Ancient philosophy running as guardrails in production."

### Money and the Uncomfortable Truth [08:44](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=524s)
There was zero training bill. The expensive part was never compute—it was teaching a company to remember itself. An agency quoted $230K to build this; they built it for around $30K ("cheaper than a nice watch"), running on a couple thousand dollars a month.

### Brain OS: A Forkable Architecture [09:14](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=554s)
They extracted the architecture into "Brain OS," which ships as an empty nervous system—agents, memory, dream cycle, soul file, all blank. Companies pour their own truth into it. The core message: only you can build your company's brain; it can't be outsourced. "We are not selling ours to you. We are helping you build your own." The project lives at forkmybrain.org.

## Notable Quotes

- "We weren't scared of the competitors, we were scared of forgetting."
- "The brain isn't a smarter model. It's actually a really, really well-organized memory."
- "Evolution already spent a billion years solving how do you stay coherent over time? We just copied the homework."
- "One prompt that's supposed to do everything ends up doing everything badly."
- "It's like having a board room that never sleeps, never gets tired, and somehow has no ego."
- "A raw language model is basically a goldfish. Brilliant for about 30 seconds, and then you close the tab and it forgets you ever existed."
- "The thing literally gets smarter overnight."
- "Ancient philosophy running as guardrails in production."
- "The expensive part was never compute. It was teaching a company to remember itself."
- "We are not selling ours to you. We are helping you build your own."

## People, Tools & References Mentioned

- **Rushabh Doshi** — Speaker; runs Machinecraft, a 100-person thermoforming factory in India
- **Machinecraft** — Three-generation family business making thermoforming machines
- **Eira (Ira)** — The 36-agent AI system running Machinecraft's go-to-market
- **Named agents**: Athena (runs the room), Prometheus (owns the sale), Plutus (pricing), Hephaestus (machine specs), Vera (fact-checking), Memnon (guards corrections)
- **Brain OS** — The forkable, empty-nervous-system version of the architecture
- **forkmybrain.org** — Website to access or learn about the forkable system
- **Cursor** — The single IDE tab from which the entire system is operated
- **Three model providers** — Unnamed, each chosen for the job it's best at
- **213 tools over one protocol** — How all capabilities are exposed
- **Jain family-business principles** — Source of the five guardrail rules in the "soul file"
- **Agency quote of $230K** — What an external agency estimated; actual cost was ~$30K

## Who Should Watch

Founders and operators of small-to-midsize businesses—especially those without data science teams—who want to see a practical, replicable blueprint for building an AI system that captures institutional knowledge and automates go-to-market work. It's also valuable for AI engineers interested in multi-agent architectures, memory design, and production guardrails outside the typical framework ecosystem.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=0s">00:00</a></span> Okay, I want to tell you a story about a factory that taught itself how to remember. Hi, I&#x27;m Rushabh. I run Machinecraft, a 100 people factory in India. No data science team, no ML budget, none of that. And somehow we ended up building a 36 AI agent that runs our entire go-to-market. I think that&#x27;s still a little ridiculous. Let me show you how it happened and why you can do the same thing. So, here&#x27;s the thing about our company.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=32s">00:32</a></span> So, here&#x27;s the thing about our company. From the outside it looks like machines and metal. But the actual company, the part that matters, isn&#x27;t the machines, it&#x27;s the knowledge. Who the customer is, what we quoted them in 2019, why that one machine needed that weird custom tweak. And for three generations, all of that lived in exactly three brains. Initially my grandfather&#x27;s, then my father&#x27;s, and now mine. Which is a genuinely terrifying way to run a company. When you sit with it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=62s">01:02</a></span> When you sit with it. A lot of people have joined us, people have left us, the revolving door never stopped. And every single time someone walked out, a chunk of our brain walked out with them. We weren&#x27;t scared of the competitors, we were scared of forgetting. Or waking up one day and realizing the whole company only existed inside two increasingly tired heads. So, I had an idea. I&#x27;ll be honest. Sounded insane first.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=92s">01:32</a></span> Sounded insane first. But what if instead of writing the knowledge down in some document nobody ever reads, what if we grew a brain that just held it? Not a chatbot you poke at, a twin of the company. I didn&#x27;t hire a sales team. I tried to build one. A quick detour because you need to know how messy this is. We make thermoforming machines. They heat up a plastic sheet and shape it. Same core machine, but it ends up making</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=123s">02:03</a></span> Same core machine, but it ends up making hydroponic farm trays, spa bathtubs, EV car panels, medical casings, and even packaging. Seven totally different worlds, seven totally different buyers. So, this brain couldn&#x27;t just memorize a brochure. It had to know which universe a given customer lives in. Step one was almost boringly simple. Feed it everything, and I mean everything. Years of quotes, drawings, payment schedules, timelines, email threads,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=155s">02:35</a></span> schedules, timelines, email threads, hundreds of gigabytes of our own private history. Not the public internet, our internet. And here&#x27;s the plot twist. The part that surprises every engineer I tell this to. We never trained a model. No GPUs humming in the basement, no fine-tuning. We just looked at all the history, chopped it into bite-size chunks, and let off-the-shelf models read it and pull out the facts. We stored the meaning of each chunk as</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=185s">03:05</a></span> We stored the meaning of each chunk as vectors and relationships. Who&#x27;s connected to what as a graph. The brain isn&#x27;t a smarter model. It&#x27;s actually a really, really well-organized memory. Now, this is where it gets a little weird in a good way. We stopped thinking of Era as a software and started thinking of it as something we were raising. So, we gave it a body modeled on biology. Senses to figure out who it&#x27;s talking to, a gut to digest the documents into</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=215s">03:35</a></span> to, a gut to digest the documents into facts, a memory, a dream cycle, an immune system to fight off bad information. Why biology? Well, because evolution already spent a billion years solving how do you stay coherent over time? We just copied the homework. Okay, so the big question. Why 36 agents instead of one genius mega prompt? Because, and you already know this if you&#x27;ve ever tried it, one prompt that&#x27;s supposed to do everything ends up doing everything badly. So, Ira isn&#x27;t</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=248s">04:08</a></span> doing everything badly. So, Ira isn&#x27;t one mind, it&#x27;s a pantheon. A whole cast of specialists. Each one has exactly one job. Athena runs the room. Prometheus owns the sale. Plutus does pricing. Hephaestus knows every machine spec cold. Vera fact checks everything, and Memnon, my favorite, guards corrections. So, the second a human fixes something, it stays fixed forever.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=278s">04:38</a></span> fixed forever. One agent, one job. It&#x27;s a team, not a hero. And here&#x27;s the cool part. They hold meetings. Athena pulls in specialists. They actually argue, and a single answer comes out the other side. It&#x27;s like having a board room that never sleeps, never gets tired, and somehow has no ego. So, what does all this actually run? Honestly, the whole front business. Everything between a stranger exists</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=309s">05:09</a></span> Everything between a stranger exists somewhere, and now they&#x27;re a customer. Nine concrete jobs every single day. Outbound emails that actually reference my real world. Account briefs built from cross-checked truths before a call. Quotations. A swipe left, swipe right mode for outreach. Reviving dead leads, which I call blast from the past. Inbound replies, and figuring out before we waste an hour whether a company is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=339s">05:39</a></span> we waste an hour whether a company is even a fit. Nine jobs, one operator who never sleeps. Where does all this live? One cursor tab. That&#x27;s genuinely it. You type and Eira reaches out with a dozen hands. Searches the knowledge base, reads the inbox, drafts the email, builds the code, and then shows you before anything actually goes out. Under the hood, it&#x27;s genuinely a real stack. Not a demo held together with duct tape. Databases for vectors, for relationship</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=371s">06:11</a></span> Databases for vectors, for relationship graph, for the CRM. Three different model providers, each picked for the job it&#x27;s actually best for. Tools for Google, for swallowing documents, for every communication channel, plus monitoring. So, we can see what it&#x27;s thinking. All of it, every capability exposed as 213 tools over one protocol. And the golden rule, the one we never break, Eira drafts, human sends. Now, memory. And this is the part where</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=401s">06:41</a></span> Now, memory. And this is the part where most AI quietly lies to you, because a raw language model is basically a goldfish. Brilliant for about 30 seconds, and then you close the tab and forgets you ever existed. So, we engineered memory on purpose, in layers. Working memory for the last few minutes. Pinned facts about someone who who is. Episodes, whole conversations as little stories. Relationships with warmth that grows from stranger to trusted. And a bouncer at the door.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=432s">07:12</a></span> And a bouncer at the door. A salience gate that decides what&#x27;s even worth remembering, so the brain doesn&#x27;t fill up with junk. When two facts disagree, corrections win. Continuity without making things up. And then, I genuinely love this part. At night, it dreams. Every night, Eira runs a sleep cycle. It replays the day, locks in useful stuff, hunts for contradictions, gently forgets the stale junk, and turns</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=463s">07:43</a></span> gently forgets the stale junk, and turns the day&#x27;s work into reusable skills. In the morning, there&#x27;s a little dream report waiting for me to read. Here&#x27;s what I consolidated. Here&#x27;s what I Here&#x27;s what I let go of. Here&#x27;s what I figured out while you were asleep. The thing literally gets smarter overnight. And here&#x27;s the part I care about the most. Every agent has a conscience. And it is emphatically not to be helpful, be harmless. It&#x27;s a soul file</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=493s">08:13</a></span> harmless. It&#x27;s a soul file written from the principles of a Jain family business that&#x27;s been doing this for the last three generations. Five old ideas turn into engineering rules. No single source has the whole truth. So, cross-check before you speak. Never say things absolutely. Cite the document and the date. Do your own job, not someone else&#x27;s. Report the truth even when the truth is ugly. And nobody works alone. Ancient philosophy running as guardrails in production.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=524s">08:44</a></span> production. Now, let&#x27;s talk money. Because this is the part that should make the whole industry a little uncomfortable. There was no training bill. Zero. The expensive part was never compute. It was teaching a company to remember itself. An agency quoted us 230 grand to build this. We built it for around 30. That&#x27;s cheaper than a nice watch. And it runs on a couple of thousand dollars a month. So, here&#x27;s the move. We pulled the whole architecture out and made it forkable.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=554s">09:14</a></span> made it forkable. We call it Brain OS. It ships as an empty nervous system. The agents, the memory, the dream cycle, the soul file. All there, completely blank. You pour your own company&#x27;s truth into it and from inside out. Because here&#x27;s the thing nobody can outsource for you. Only you can build your company&#x27;s brain. We are a 100 people factory with no data scientists. If we can grow a brain, you can too. We are not selling ours to you. We are helping you build your own.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jtzh-GBXBWc&amp;t=586s">09:46</a></span> helping you build your own. forkmybrain.org Go build something that remembers. Thank you.</p>

</details>
