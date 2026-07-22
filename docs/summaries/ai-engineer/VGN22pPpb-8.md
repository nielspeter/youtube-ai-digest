---
title: "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j"
channel: "AI Engineer"
video_id: VGN22pPpb-8
url: https://www.youtube.com/watch?v=VGN22pPpb-8
published: 2026-07-22T17:00:38+00:00
generated: 2026-07-22T17:38:35+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/VGN22pPpb-8/hqdefault.jpg
---
# Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j

[![Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j](https://i.ytimg.com/vi/VGN22pPpb-8/hqdefault.jpg)](https://www.youtube.com/watch?v=VGN22pPpb-8)

[Watch on YouTube](https://www.youtube.com/watch?v=VGN22pPpb-8) · **AI Engineer** · 2026-07-22

## TL;DR
Emil Eifrem of Neo4j outlines a growing problem in enterprise AI: agents built independently each manually wire into data sources, leading to duplicated effort, fragile maintenance, and no cross-agent learning. He proposes a blueprint of "thin agents on a smarter shared substrate"—an ontology-based semantic layer combining a business-facing ontology, a technical ontology with mappings, and runtime execution traces—that lets agents discover, trust, and learn from data sources dynamically.

## Key Takeaways
- Enterprise agents typically consist of business logic (intent/plan/act) plus manually wired data sources—a model that breaks down at scale.
- In large organizations, every new agent team must rediscover where data lives, which version is trustworthy, and whether access is permitted.
- The "DRY" (Don't Repeat Yourself) principle is violated: when data sources change, every agent must be manually rewired.
- Markdown-file "skills" alone are insufficient; they are part of the solution but not the whole solution.
- The proposed pattern is **thin agents on a smarter shared substrate**, built on three pillars: a business-facing ontology, a technical ontology (with mappings between the two), and runtime execution traces.
- A **business-facing ontology** captures key organizational concepts (e.g., customers, accounts, transactions) in human-understandable terms.
- A **technical ontology** catalogs all enterprise data assets (Oracle, Neo4j, Snowflake, S3, etc.) including schemas and locations, mapped to the business concepts.
- **Execution traces** record what agents tried, whether it worked, and outcomes—enabling both individual and cross-agent self-learning.
- Together, these pillars solve discovery, trust, governance, reuse, and continuous learning across agents.
- Neo4j offers resources including documentation, a graph/AI track at the conference, and a startup program with free credits and dedicated solution engineering support.

## Detailed Breakdown

### The Enterprise Agent Problem [00:12](https://www.youtube.com/watch?v=VGN22pPpb-8&t=12s)
Eifrem opens by describing Neo4j's work helping large companies prepare data for AI agents. He frames the talk around a problem emerging over the past six to nine months and uses a simplified example: an agent that automates opening a bank account at a large bank.

### Anatomy of an Agent [00:43](https://www.youtube.com/watch?v=VGN22pPpb-8&t=43s)
An agent has two main pieces: business logic (interpreting intent, planning, acting, looping) and data source wiring. For the bank-account-opening example, the agent might need identity validation via the DMV registry and a passport verification service. This works in isolation, but other teams build similar agents with similar needs.

### Why Manual Wiring Breaks at Scale [02:16](https://www.youtube.com/watch?v=VGN22pPpb-8&t=136s)
In a startup with one Postgres database, finding data is trivial. In an enterprise with a hundred databases, Snowflake, Databricks, and S3 buckets, every team must manually rediscover where data sits. Problems include data duplication (which version is correct?), trust, access permissions, violation of the DRY principle (changes cascade across all agents), and no learning—agents don't get smarter over time, and there's no cross-agent learning because the business-to-data wiring lives in code and prompts.

### Skills Files: Part of the Solution, Not the Whole Solution [03:18](https://www.youtube.com/watch?v=VGN22pPpb-8&t=198s)
Eifrem acknowledges the audience may be thinking "skills files to the rescue" but says markdown files alone are insufficient. He cites a recent Latent Space podcast comment by Swyx: "You got to learn your databases. You cannot vibe code with just markdown files."

### The Emerging Pattern: Thin Agents on a Smarter Shared Substrate [04:19](https://www.youtube.com/watch?v=VGN22pPpb-8&t=259s)
Based on work with a Fortune 20 global bank, a massive Bay Area tech platform, and a leading fintech, Eifrem identifies an emerging pattern for agents at scale: thin agents sitting on a smarter shared substrate. This rests on three pillars.

### Pillar One: Business-Facing Ontology [04:49](https://www.youtube.com/watch?v=VGN22pPpb-8&t=289s)
A business-facing ontology captures the key concepts in an organization—customers, accounts, debit cards, checks, transactions—and how they relate. Critically, these are expressed in terms that make sense to all humans in the organization (e.g., "customer has a first name," not a database column called `f_name`).

### Pillar Two: Technical Ontology and Mapping [05:22](https://www.youtube.com/watch?v=VGN22pPpb-8&t=322s)
The technical ontology is the metadata of all data sources and assets in the enterprise: Oracle databases, Neo4j databases, Snowflake, Databricks, S3 buckets, their schemas, and locations. A mapping connects business concepts to technical assets—for example, the business concept "first name" maps to an Oracle column called `F_name` in a system of record.

### Pillar Three: Runtime Execution Traces [06:24](https://www.youtube.com/watch?v=VGN22pPpb-8&t=384s)
When agents walk the ontology graph and execute, they leave traces: what they tried, whether it succeeded, the outcome, and ultimately a score. These traces feed back into future decisions—for instance, if the DMV lookup was consistently successful, the agent is more likely to choose it in the right context next time.

### Putting It Together: The Bank Account Example [06:56](https://www.youtube.com/watch?v=VGN22pPpb-8&t=416s)
Eifrem walks through a simplified graph combining business concepts (checks, accounts, credit history) and an encoded business process. At the "check compliance" node, the graph flips to the technical ontology, showing that compliance requires resolving a government-issued ID, with two data sources available: motor vehicle records and passport verification. Agents discover these options, execute, and leave execution traces that inform future invocations.

### How the Three Pillars Solve the Four Problems [08:30](https://www.youtube.com/watch?v=VGN22pPpb-8&t=510s)
The ontology-based semantic layer solves all four original problems: easy data source discovery; trustworthiness determined both top-down (human curation) and bottom-up (execution traces); a single governed mapping eliminating repetition so changes cascade automatically; and self-learning both within and across agents.

### From Thick Agents to Thin Agents [09:01](https://www.youtube.com/watch?v=VGN22pPpb-8&t=541s)
Eifrem contrasts the old world—thick agents with manually wired data sources—with the new world of thin agents on a smarter shared ontology-based semantic layer, enabling many more agents without re-engineering each time.

### Resources and Conference Plug [09:33](https://www.youtube.com/watch?v=VGN22pPpb-8&t=573s)
He points to documentation (via a QR code), invites attendees to visit Neo4j's booth at Expo P3, and highlights a graph track in Room 2005 featuring talks from the Gates Foundation, Monday.com, JP Morgan Chase, Berkeley, and the New York Times. He closes by promoting Neo4j's startup program, which offers free credits and a dedicated solution engineering team.

## Notable Quotes
- "In order to do agents at scale, we need thin agents on a smarter shared substrate."
- "You don't say `f_name`—no, you have a customer and they have a first name."
- "You cannot vibe code with just markdown files." — Swyx, quoted by Eifrem
- "We're moving from a world of thick agents with manually wired data sources into a world where we have thin agents on a smarter shared ontology-based semantic layer."

## People, Tools & References Mentioned
- **Emil Eifrem** — speaker, Neo4j
- **Neo4j** — graph database company; sponsor of the talk
- **Swyx** — quoted from the Latent Space podcast
- **Palantir** — credited with helping popularize the term "ontology"
- **Tools/platforms mentioned:** Postgres, Oracle, Snowflake, Databricks, S3, Neo4j
- **Organizations cited as Neo4j customers/use cases:** a Fortune 20 global bank, a massive Bay Area tech platform company, a leading fintech company
- **Conference graph track speakers:** Gates Foundation, Monday.com, JP Morgan Chase, UC Berkeley, New York Times

## Who Should Watch
Enterprise architects, AI engineers, and data leaders building multiple AI agents across complex data landscapes who want to reduce duplicated integration work and enable cross-agent learning. The talk is especially relevant for teams at large organizations struggling with data discovery, trust, and governance for agentic AI.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=12s">00:12</a></span> All right. At Neo Forj, we work with some of the largest companies in the world to help make their data ready for AI agents. And today I want to talk to you about a problem that we saw emerging over the last call it six to nine months and propose a solution blueprint for that. So let&#x27;s say that we work at a big organization a big bank and we want to write an agent. Let&#x27;s say that agent is helping automate the opening of a bank account. Right? You can imagine that&#x27;s</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=43s">00:43</a></span> account. Right? You can imagine that&#x27;s very ripe for automation. You want to be able to orchestrate that process. And I&#x27;m going to use the powers bestowed upon me by a short keynote slot to grossly simplify what that agent looks like. I&#x27;m going to say there&#x27;s two pieces. The first one is let&#x27;s call it the business logic. Some version of interpreting intent and plan act and we loop around that. It&#x27;s what your agent does. And we know that when an agent act, it doesn&#x27;t always operate on data. But we equally know that in order for agents to be successful a huge part of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=74s">01:14</a></span> agents to be successful a huge part of that is giving it access to the right data at the right time. So the second big bucket is let&#x27;s call it the data sources need to identify figure out okay in order to solve my problem I need access to these few things and wire them up and make them available to the agent. In the example of our account opening agent maybe we can imagine that we need to be able to validate identity and so we might look at two data sources for that. the Department of Motor Vehicles, the DMV registry, and maybe some kind of passport verification service. So, we</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=106s">01:46</a></span> passport verification service. So, we wire that up into our agent and it works. It&#x27;s great. It&#x27;s fantastic. And at the same time, you and other teams in your organization are building other agents and conceptually they look very similar. So, that&#x27;s great. It&#x27;s fantastic. It works. But it has a few problems. So first of all, every single time a team has to build an agent, they have to figure out from scratch where the data that they require for that agent to operate, where it sits, which if you work at a startup and you have</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=136s">02:16</a></span> if you work at a startup and you have one application, it sits on top of one Postgress database. That&#x27;s not hard. The data is in that Postgress database. But in an enterprise ecosystem, you don&#x27;t have one database. You have a hundred databases and you have snowflake and data bricks probably and you have S3 buckets and so on and so forth. You have to do that work manually from scratch every single time. And then when you&#x27;ve found the data sources, you know, in an enterprise there&#x27;s lots of duplication of data. So then you need to figure out like is this the right data? Is it the right version? Can I trust it? Am I allowed to access it? So on and so</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=167s">02:47</a></span> allowed to access it? So on and so forth. It also violates one of the core principles of software engineering, the dry principle. Don&#x27;t repeat yourself. So when something change that cascades across all of your agents, you have to kind of manually rewire all of them. all the time, which works, but it&#x27;s just a lot of work. And then finally, there&#x27;s no learning around the data sources and how your agents operate on them. So when your agent wake up wakes up tomorrow, it&#x27;s not smarter than it was today. And there certainly isn&#x27;t any cross agent</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=198s">03:18</a></span> there certainly isn&#x27;t any cross agent learning because all of that wiring between business intent and the data sources is encoded in a combination of code and prompts. So I know what you&#x27;re all thinking. work on files skills to the rescue and yes and no. Um you can come talk to me afterwards for kind of the full version of this but we&#x27;ve seen a ton of team that try to solve this problem using just markdown files and the summary is it is part of the solution but it is not the solution. Uh but don&#x27;t take it from</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=228s">03:48</a></span> the solution. Uh but don&#x27;t take it from me, take it from Switz. A week ago on the latent space podcast, he said, &quot;Hey guys, you got to learn your databases. You cannot vibe code with just markdown files.&quot; So we&#x27;ve been solving this problem at scale for some really massive organizations recently, including a Fortune 20 global bank, a massive tech platform company based here in the Bay Area, and a leading fintech company. And the pattern that is emerging is that in</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=259s">04:19</a></span> the pattern that is emerging is that in order to do agents at scale, we need thin agents on a smarter shared substrate. Thin agents on a smarter shared substrate. And what does that look like in practice? There are three pillars to that. The first pillar is a businessfacing ontology. And the word ontology like I grew up in this world. People talked about ontologies forever. More recently, it&#x27;s become very hype. probably thanks to Palunteer but also the rise of AI and there&#x27;s a lot of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=289s">04:49</a></span> the rise of AI and there&#x27;s a lot of people that want to make ontologies really complex but the core concepts are actually super simple what are the key concepts in your organization in our banking example customers accounts um debit cards checks transactions and how do they all relate but very importantly they are expressed in a way that makes sense to all the human beings working in your universe right all the people working in your company it&#x27;s expressed in that name in that way in other words you don&#x27;t say f_name</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=322s">05:22</a></span> you don&#x27;t say f_name no you have a customer and they have a first name so that&#x27;s the first a businessf facing ontology the second pillar is a technical ontology this is all the metadata of all the data sources and data assets in your enterprise ecosystem I have 14 Oracle databases I have 15 neo forj databases I have snowflake and data bricks and I have s3 buckets and all of that kind of stuff. Where do they sit? What are the schemas? All of that kind of good stuff. You com you construct that technical ontology in</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=353s">05:53</a></span> you construct that technical ontology in three key ways that we can talk about later though not in this in this talk. And then you have a mapping between the two. So that customer that has a first name that first name has a system of record and over there there&#x27;s an Oracle database with a column called F_name the mapping between the two. And then the third pillar is the runtime signals out of your agents. When they walk this graph and they execute, they leave the traces around what have I tried? Was I successful? What was the outcome? The</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=384s">06:24</a></span> successful? What was the outcome? The execution traces those three pillars. Okay. So let&#x27;s look at that in the context of our bank account opening agent. This is a simplified view, but you can see this graph here. It has a combination of business concept like checks and accounts and credit history and stuff like that. This is a process following agent or a process guided agent. We want this type of agent to actually follow a process. So we&#x27;ve also encoded that in the ontology, a business process. And then if you look at the node that is surrounded by green the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=416s">06:56</a></span> node that is surrounded by green the check compliance one we flip to the technical ontology and we&#x27;ve put in the graph here we&#x27;ve discovered and encoded that in order to do a compliance check you might imagine that you need to resolve a governmentissued ID and then we say that in this particular organization there are two data sources that can help us with that. It&#x27;s the motor vehicle records and the passport verification one. Okay so that&#x27;s really great. So then when our agents come in here and they realize I&#x27;m going to check compliance, I need a governmentissued</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=446s">07:26</a></span> compliance, I need a governmentissued ID. Here are the two ways that I can resolve that. When they execute and they try that, they leave the third pillar, the execution traces for that. And they&#x27;re more sophisticated than what&#x27;s on this simplified slide, but involves things like, okay, where was I? What did I do? What is my context? And was I successful? And ultimately, it leads out to some kind of a score. and you use that as input. It&#x27;s like, okay, I&#x27;ve been very successful using the DMV lookup, for example, then I&#x27;m more likely to choose one if I&#x27;m in the right</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=477s">07:57</a></span> likely to choose one if I&#x27;m in the right context in my next invocation. Three pillars of the ontology based semantic layer, a business ontology, a technical ontology, the execution traces taken together, they solve all four of the problems. We now have a very easy way to discover the data sources. We know if they&#x27;re trustworthy or not. We know that top down by some kind of human curated knowledge, right? An administrator of some sort saying it. We also know it bottom up through the execution traces. This is what actually worked in reality in practice. We have a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=510s">08:30</a></span> worked in reality in practice. We have a single governed place that maps business intent and the concepts to those data sources so we don&#x27;t repeat ourselves. If something changes that cascades across all my agents, right? And we have self-arning. So my agent that wakes up tomorrow is slightly smarter than it was today. And not just self-learning on an individual agent, but across agents as well. So we&#x27;re moving from this world, a world of thick agents with manually wired data sources into this world where we have</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=541s">09:01</a></span> sources into this world where we have thin agents on a smarter shared ontology based semantic layer. And this allows us to do a ton more agents without having to re-engineer them every time. Thin agents on top of a smarter shared substrate. If you think this is interesting, there&#x27;s a documentation, a web page that outlines more information about this. If you see the QR code here, you can also come and talk to us at the booth. We have a big booth here at the expo P3. We love</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=573s">09:33</a></span> booth here at the expo P3. We love talking about this this kind of stuff. But not just that, this is one pattern, a very exciting pattern that we see a lot of traction around right now for using graphs in AI. But there&#x27;s hundreds of more interesting patterns that combines graphs and AI. 10 of them is actually in the graph track that is kicking off right now in room 2005. And you have some really amazing talks from organizations like the Gates Foundation, Monday.com, JP Morgan Chase, Berkeley,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=605s">10:05</a></span> Monday.com, JP Morgan Chase, Berkeley, New York Times, and so on and so forth. So go check out that thing. And then finally, this was primarily center around organizations where you deal with many data sources and many agents. But if you&#x27;re a startup building on Neo forj, love you. There is a startup program for Neo Forj that is phenomenal. You get access to free credit, but more importantly, we&#x27;ve built up a dedicated solution engineering team that spend every day working with startups for free, helping them model their data in</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=VGN22pPpb-8&amp;t=636s">10:36</a></span> free, helping them model their data in Neo Forj, tune it for performance, and so on and so forth. So, please sign up for our startup program. Thank you very much. Enjoy the conference. Have a good day, everyone.</p>

</details>
