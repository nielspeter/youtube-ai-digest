---
title: "Lessons Learned Building Rippling AI | Interrupt 26"
channel: "LangChain"
video_id: 3lb_4OEOykc
url: https://www.youtube.com/watch?v=3lb_4OEOykc
published: 2026-07-13T12:40:21+00:00
generated: 2026-07-16T20:29:13+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/3lb_4OEOykc/hqdefault.jpg
---
# Lessons Learned Building Rippling AI | Interrupt 26

[![Lessons Learned Building Rippling AI | Interrupt 26](https://i.ytimg.com/vi/3lb_4OEOykc/hqdefault.jpg)](https://www.youtube.com/watch?v=3lb_4OEOykc)

[Watch on YouTube](https://www.youtube.com/watch?v=3lb_4OEOykc) · **LangChain** · 2026-07-13

## TL;DR
Senthil and Akash from Rippling share lessons from building Rippling AI, an assistant layered on top of Rippling's unified "employee graph." They discuss evolving from a multi-agent architecture to a single flat agent, replacing many bespoke tools with generic SQL-backed ones, and adopting eval-driven development with a disciplined approach to repetition and statistical confidence.

## Key Takeaways
- Rippling's unified employee graph—employee data at the center with all products built around it—made adding an AI layer feel like "magic."
- An early multi-agent design (top agent + many sub-agents) failed due to context-sharing, handoff, and interrupt problems; the team replaced it with one flat agent.
- Domain context is injected declaratively via "skills and SOPs" written by product engineers, rather than encoded in agent structure.
- A large catalog of team-built tools made tool selection fragile; the team moved to fewer, generic, composable tools (e.g., one `get-data` method with entity as a parameter).
- For data queries, raw data is not stuffed into the context window; instead the LLM is given the schema and query, writes SQL, and the system executes it—reducing hallucinations.
- Caching queried data lets the LLM iterate (write query, see error, retry) efficiently, especially for follow-up questions and competing hypotheses.
- "Evals first and build next" means eval-driven development (EDD): any meaningful change (prompt, tool, skill) must be validated by evals because LLM behavior is unpredictable.
- A single eval pass proves little; Wilson's confidence interval shows that 1/1 passing could mean a lower bound of ~20% at 95% confidence. Repetitions reduce uncertainty.
- Required repetition count depends on baseline performance, the size of regression you want to detect, and your false-positive tolerance.
- There's a tradeoff triangle of cost, uncertainty, and lag—you can only optimize two of three. Rippling uses cheap "smoke evals" on every commit and more thorough "health evals" twice daily before production.
- Production data (including PII) is kept in a "vault workspace" and synthesized into representative test data; custom tooling is needed to inspect domain-specific issues.

## Detailed Breakdown

### Introduction and the HR problem [00:06](https://www.youtube.com/watch?v=3lb_4OEOykc&t=6s)
Senthil introduces himself and Akash, who build AI products at Rippling. He asks the audience if they've heard of Rippling, then sets up the core problem: an HR leader at a company with thousands of employees across countries, departments, and access controls is flooded with requests—spend reports from the CEO, payroll discrepancies from employees—and the answers are scattered across systems and spreadsheets. Getting them quickly and accurately is tedious.

### The vision: just ask your system [01:11](https://www.youtube.com/watch?v=3lb_4OEOykc&t=71s)
Senthil poses the question: what if you could just ask your system and get the answer? This sets up the motivation for Rippling AI.

### Rippling AI and the employee graph [02:10](https://www.youtube.com/watch?v=3lb_4OEOykc&t=130s)
The key enabler is Rippling's architecture from day one: employee data sits at the center (the "employee graph"), with all products connected around it. A change to an employee is reflected everywhere. Putting an AI layer on top of this already-organized data is what makes Rippling AI work. Senthil notes it's one of the most successful launches in his six and a half years at the company.

### Architecture overview [03:12](https://www.youtube.com/watch?v=3lb_4OEOykc&t=192s)
The Rippling backend (employee graph + applications + data) is represented as one block. The agent is built with LangGraph. There's a top agent handling orchestration, and three main blocks: entity resolution (resolving a first name to an employee ID), tool selection (selecting the right tools and bringing in domain context via skills and SOPs), and a flat agent with generic tools that connects to the employee graph to fetch data and operate workflows.

### From multi-agent to flat agent [04:52](https://www.youtube.com/watch?v=3lb_4OEOykc&t=292s)
Initially, with hundreds of engineers and vastly different products, the team tried a top-level assistant agent with many sub-agents (one per team). This didn't work well due to problems with context sharing, handoffs, interrupt handling, and queries spanning multiple sub-agents. The solution was to flatten everything into one agent, injecting domain context only through declarative skills and SOPs. The message history the user sees is the same as what the LLM sees, and performance improved.

### From many tools to generic, composable tools [05:58](https://www.youtube.com/watch?v=3lb_4OEOykc&t=358s)
Each team initially built its own tools, creating a large catalog that made tool selection sensitive and error-prone. The team moved toward generic tools—for example, one `get-data` method where "employee," "device," or "taxes" becomes a parameter. This echoes the Unix philosophy: do simple things well and let the agent compose them.

### Data accuracy and the SQL approach [07:00](https://www.youtube.com/watch?v=3lb_4OEOykc&t=420s)
People primarily use the assistant to ask data questions—payroll, benefits, aggregated reports—and the data cannot be wrong. Stuffing raw data into the LLM context risks hallucinations. Instead, Rippling gives the LLM the schema, the data shape, and the query; the LLM writes SQL, which the system executes. The data itself stays out of the context window.

### SQL is more powerful than bespoke tools [08:02](https://www.youtube.com/watch?v=3lb_4OEOykc&t=482s)
Senthil gives the example query: "why weren't the benefits deductions withheld for a given employee?" Under the hood this requires data about the employee (location, entitlements, HRIS), benefits, and payroll. Instead of orchestrating many tools, one generic SQL-executing tool lets the LLM write a single query to pull everything. LLMs are very good at writing SQL. This reduced the number of tools and the risk of wrong tool selection.

### Caching for iteration and follow-ups [09:05](https://www.youtube.com/watch?v=3lb_4OEOykc&t=545s)
Querying the core data lake is costly in dollars and time. Rippling caches the data once and lets the LLM explore—writing a query, seeing errors, iterating—similar to how Claude Code or other agents work. Caching is especially powerful when the same data is needed for follow-up questions or when two hypotheses are being tested.

### Evals first and build next [10:07](https://www.youtube.com/watch?v=3lb_4OEOykc&t=607s)
The team follows eval-driven development (EDD), analogous to TDD but harder due to LLM stochasticity. You don't write evals before the agent exists, but once a version is running, any meaningful change—system prompt, tool, tool description, skill—must be validated by evals. Intuition isn't enough; evals tell the truth.

### Repetitions and Wilson's confidence interval [11:09](https://www.youtube.com/watch?v=3lb_4OEOykc&t=669s)
A single passing eval doesn't prove a 100% success rate. The team uses Wilson's confidence interval: at 95% confidence, 1 out of 1 passing could mean a lower bound of ~20%, and 3 out of 3 could still be as low as ~44%. More repetitions converge toward the true pass rate. The number of reps needed depends on your baseline, how small a regression you want to detect, and your tolerance for false positives.

### The tradeoff triangle: cost, uncertainty, lag [13:18](https://www.youtube.com/watch?v=3lb_4OEOykc&t=798s)
You can only optimize two of three: cost (more reps = more money), uncertainty (more reps = more confidence), and lag (how quickly you detect a regression). Rippling runs cheap "smoke evals" on every commit (low cost, low lag, higher uncertainty) and more thorough "health evals" twice a day before production (higher lag, lower uncertainty, controlled cost). Once health evals pass, changes go to production.

### Production learnings and data handling [15:23](https://www.youtube.com/watch?v=3lb_4OEOykc&t=923s)
Every domain is different; you need custom tooling to explore your data and understand failures. Rippling keeps production data (including PII) in a "vault workspace" and synthesizes it into representative test data rather than working with customer data directly. Learnings from production feed back into improving the eval suite.

### Final recommendations [15:56](https://www.youtube.com/watch?v=3lb_4OEOykc&t=956s)
Senthil wraps up with three lessons: (1) keep agents flat and get glue code out of the LLM's way—this will keep changing as models improve; (2) build generic, composable tools and let the model query via SQL when possible; (3) practice eval-driven development, testing every change and choosing your tradeoff among cost, uncertainty, and lag.

## Notable Quotes
- "What if you could just ask your system and it would give you the answer?"
- "We eliminated the problem by keeping it flat. What we have is one flat agent today."
- "Whatever the user sees as message history, the LLM sees the same thing."
- "It's the same Unix philosophy: do simple things and do them well, and let the agent compose all these things to get any complex outcome."
- "The data itself is not part of the context window. It's basically the LLM solving the problem given the shape of the data."
- "You can go by your intuitions, but at the end of the day, evals tell you the truth."
- "You can only get two out of the three."

## People, Tools & References Mentioned
- **Senthil** — speaker, builds AI products at Rippling
- **Akash** — co-speaker, builds AI products at Rippling
- **Rippling** — workforce management platform (HR, payroll, benefits, devices, etc.)
- **Rippling AI** — the AI assistant discussed
- **Employee graph** — Rippling's central, unified employee data model
- **LangGraph** — framework used to build the agent
- **Claude Code** — referenced as an example of iterative agent behavior
- **Wilson's confidence interval** — statistical method for evaluating eval confidence with small sample sizes
- **Unix philosophy** — invoked to explain the generic-tools approach
- **Vault workspace** — Rippling's secure production data environment for PII
- **Smoke evals / health evals** — Rippling's two-tier eval strategy

## Who Should Watch
AI engineers and product builders working on LLM agents—especially in enterprise or data-rich domains—who want practical lessons on agent architecture, tool design, and eval-driven development. The talk is most valuable for teams grappling with multi-agent complexity, tool-selection failures, or the challenge of confidently shipping agent changes.


<details class="transcript">
<summary>Full transcript</summary>

<p>We can start. I have good news and bad news. The good news is this is the last talk of the day. The bad news is you have to sit through and hear us. Shall we start? Thank you. So my name is Senthil and he is Akash. We build AI products at Rippling. How many of you have heard of Rippling? OK, reasonably popular. Imagine you are running a company. You have a few thousand employees across multiple countries.</p>
<p>You have full-time, part-time, and contract employees, multiple departments, different access controls. You run payroll and benefits, and you handle payroll taxes. You manage their devices and all this stuff. And you are the HR leader at the company. And on Monday morning, in your inbox, your CEO is asking for a report around spend. An employee is asking about some discrepancy or a missing amount in payroll, and things like that.</p>
<p>So you&#x27;re filled with all these kinds of requests. You know the answers are out there somewhere, across all the systems you&#x27;re managing and all the spreadsheets you&#x27;re handling. But getting all of these things done quickly and accurately is just tedious work. It&#x27;s work. What if you could just ask your system and it would give you the answer? [upbeat music]</p>
<p>That&#x27;s Rippling AI. So this is possible because of the way</p>
<p>we&#x27;ve organized the system at Rippling from day one. Instead of multiple systems that you&#x27;re dealing with, we put employee data at the center, and then we built a lot of products around it. We call it the employee graph. So you have all the systems connected. Whenever you change something about an employee, everything is reflected everywhere. The data is already organized for you to use it. And we put an AI layer on top of it. And suddenly it feels like magic. And that&#x27;s what we did with Rippling AI.</p>
<p>We launched a few weeks ago. I&#x27;ve been with the company for six and a half years now. And this is one of the most successful launches we&#x27;ve had. And that&#x27;s possible because we have this data already organized with the employee graph. So in this talk, we&#x27;re going to talk about the Rippling AI journey, what we learned, and we thought we would share this with you. And that&#x27;s it. So let&#x27;s talk about the architecture first. Everything I spoke about — the employee graph, all the applications and the data —</p>
<p>I&#x27;m representing as one big block at the bottom called the Rippling Backend API. And now I&#x27;m going to zoom into the agent itself. We use LangGraph, of course. And we have a top agent. And then we have a deep agent, which handles the overall orchestration. The top agent handles the orchestration. There are three main blocks I&#x27;m talking about. First is entity resolution. If a user is asking about an employee by first name, that name has to be resolved to an employee record</p>
<p>living in the system, pointing to an employee ID. And then we have tool selection, which — specific to the query — selects the right tools, and also brings in domain context, which is very vast in the case of Rippling, through skills and SOP. So that&#x27;s a horizontal concern at the top. And then we have an agent which has some generic tools, and — now that it has the entity, the tools, and the domain context — it uses these, runs the agent, connects to the employee graph, brings the data, gives you the answers, and operates</p>
<p>the workflows. But we didn&#x27;t start with this. When we started this project, Rippling is a several-hundred-member engineering company. And the products are vastly different. So we started with one top-level AI assistant agent. And then we had a lot of sub-agents. Each team could build their own sub-agent. That didn&#x27;t work well. Primarily, the problem was around how to do context sharing. How do you handle handoffs across agents? Whether the top agent should fully know about the sub-agent&#x27;s</p>
<p>context or not. How do you handle interrupts? How do you handle queries that span multiple sub-agents? And then that became messy. So we eliminated the problem by keeping it flat. What we have is one flat agent today. And all the domain context of different products is injected into the agent only through declarative skills and SOPs. Our product team engineers write them. And of course, they test them. And the agent itself is one flat agent.</p>
<p>If you really think about it, we actually removed a lot of abstractions and code. We kind of flattened it in such a way that whatever the user sees as message history, the LLM sees the same thing. And the performance is much better with this approach. Moving on to the next topic. When we started, each team built a bunch of tools, and we ended up with a very large catalog of tools. The problem with that is tool selection became far more sensitive.</p>
<p>If we selected the wrong tools or missed some tools, we were not getting the right answers. So we eliminated the problem by moving towards more generic tools. Here&#x27;s an example: instead of many get-data methods, you have one get-data method, and employee, device, or taxes becomes a parameter. If you think about it, it&#x27;s the same Unix philosophy: do simple things and do them well, and let the agent compose all these things</p>
<p>to get any complex outcome. Our AI Assistant can do a lot of things. It can run payroll, hire an employee, and a lot of other operations. But primarily, people are using it to ask questions and get data. It could be an individual asking about their payroll data, their benefits data, or any data that they&#x27;re dealing with. Or it could be the company admin or HR asking for aggregated data or report data. And this data cannot be wrong.</p>
<p>And we all know that stuffing raw data into the LLM — &quot;here is the data, here is the query, answer this&quot; — kind of prompting can go wrong. It can lead to hallucinations, and we cannot afford to be wrong. So what we did is specify to the LLM the shape of the data. Here is the schema. Here is the data. And here is the query. And ask the LLM to solve that. The LLM comes up with SQL to solve it. And we execute the SQL.</p>
<p>So the data itself is not part of the context window. It&#x27;s basically the LLM solving the problem given the shape of the data. An interesting side effect we discovered is that SQL is so powerful that it&#x27;s far more powerful than building a lot of bespoke tools we might otherwise have to build. I&#x27;ll give an example. Consider a query: &quot;why weren&#x27;t the benefits deductions withheld for a given employee?&quot; Now, this looks like a very simple query. But underneath</p>
<p>the system, we need to know about the employee — their location, entitlements, and everything in HRIS. We need to know about the benefits. Then, of course, payroll. So we need to orchestrate across all these things. With multiple tools, you can get this information and compose it. But we built one generic tool to pull all the data out, and it can execute SQL. LLMs are really good at writing SQL. And the moment we expose the schema in the context, the LLMs can write SQL in one go and get</p>
<p>the information they want. And this was far more powerful. It also reduced the number of tools needed, which removes the risk of wrong tool selection and things like that. But this still has one problem. The problem is that fetching this data — querying all the core data lake — is costly, both in terms of dollars and in terms of time.</p>
<p>So what did we do? We take this data once, put it in a cache, and let the LLM say: here is the schema, here is the data, here is the query — explore and give me the answer. And you might have seen this if you&#x27;re working with Claude Code or any of the agents, right? It iterates, writes the query, figures out the problem, and if there&#x27;s an error, it iterates again and gets the final answer. It&#x27;s very helpful. We cache the data, especially when you want the same data and there are two hypotheses running,</p>
<p>and the user is asking follow-up questions. It&#x27;s very, very powerful. And this made the experience much, much better for users. So far, we&#x27;ve spoken about the &quot;what&quot; of the system. Now we&#x27;re going to switch gears and talk about how we release the system, how we iterate and improve. And that means we are going to talk about evals. So what we do at Rippling is — we say evals first and build next. Does that mean you write your evals</p>
<p>before you even have your agent running? No. That&#x27;s not what I&#x27;m talking about. Let&#x27;s say you have your agent running in production, or some version of your agent running. Now, to make any meaningful change — a system prompt change, a tool change, a tool description change, a skill change, anything — you don&#x27;t know how it&#x27;s going to behave, even if you know every single line of code, because you don&#x27;t know how the LLMs are going to behave. So it&#x27;s very important to say: you can go by your intuitions,</p>
<p>but at the end of the day, evals tell you the truth. So that&#x27;s what we call eval-driven development, and we follow this extensively. EDD — eval-driven development — is like TDD, test-driven development, but harder. Given the stochasticity of the LLM in the first place, let&#x27;s say you have an eval, you run it once, and it passes one time. Is the success rate 100%? Are you really sure? Let&#x27;s say we run it a few more times just to be sure.</p>
<p>Let&#x27;s say you run it three times, three out of three pass. Is it 100%? Are you really sure? There are scientific ways to figure out how confident you can be as you get more repetitions in your evals. You can&#x27;t run it just once and declare victory, because if you run it a few more times it might fail. There are some scientific ways. For example, there&#x27;s something called Wilson&#x27;s confidence interval. If one out of one eval passes, at a 95% confidence interval, you could be as low as 20%.</p>
<p>And at three out of three, your lower bound could still be 44%. As you increase the number of reps, it&#x27;s going to converge to your true pass rate. So the more repetitions you have, the more confident you can be in your evals. And there&#x27;s a scientific way of asking: how many reps do you need for your evals? The more repetitions you have, the more certain you can be. The fewer repetitions you have, the less certain you are. Repetitions reduce the uncertainty</p>
<p>you have in your evals. So how many repetitions do you really need? That depends on three things. One: where are you right now? What is your baseline? For example, if your eval is already at 95%, the number of repetitions you need would be very different from if your eval is performing at 85% or 75%. The second thing: how small a regression are you trying to detect? To detect something from 95% to 94%,</p>
<p>you need a lot more repetitions than to detect something from 95% to, say, 70%. Similarly, it&#x27;s very different from detecting a drop from 85% to 60%. And the last thing is: what is your tolerance toward false positives? All of these things bring us to the tradeoff triangle: cost, uncertainty, and lag. Cost: the more repetitions you have, the more money you&#x27;re going to spend on your LLMs.</p>
<p>Uncertainty: the more repetitions you have, the less uncertain you are, the more confident you are. And lag: how soon can you detect a regression from the time you&#x27;ve made a change? Say you&#x27;ve committed your PR. How quickly can you detect: there&#x27;s been a regression here? And you can only get two out of these three, which means you can get low cost and low lag, but with higher uncertainty. At Rippling, what we do is have something called smoke evals, which are very few evals</p>
<p>that we run for fewer repetitions, and we run them on every commit that goes in. This gives us some amount of confidence that nothing is majorly broken, though something could still be off. So that falls under the low cost and low lag category. And then before anything gets pushed into production, we have a pre-prod stage where we run something called health evals, where we run them twice a day with many more evals running for many more</p>
<p>repetitions, but we wait for a batch of commits to come in — meaning we&#x27;re accepting higher lag, but reducing uncertainty and cost because we don&#x27;t run on every commit. You can only get two out of the three, and once health evals pass, they go into production. Once you have it in production, there are a few things to keep in mind. Every domain, every agent is different. No matter how many generic tools you have, you have to have visibility into your data,</p>
<p>for which you need to build custom tooling to explore your data and understand what&#x27;s going wrong with your system. So we have to build custom tooling. The second thing is we have a vault workspace where all production data lives, and we handle PII. Those things we carefully synthesize into a test environment — a synthetic test — representative of customer data, but we don&#x27;t work with the customer data directly. So we have a vault workspace and we improve our eval suite</p>
<p>over time based on learnings from production. So, finally wrapping up: first, keep your agents flat. And of course, this is going to change as models improve over time. What you would have done last year is very different from what you were doing last month. And what you&#x27;re doing now is very different from what you&#x27;re doing right now. And what you&#x27;ll probably do six months from now will be very different. As models get more and more powerful, the most important thing is to get your glue code out</p>
<p>of your agents and let the LLM do its job. Get out of its way. Next: build generic, composable tools, which means if you have data that you can let your model query via SQL, let it do that. It&#x27;s much more powerful at that. And when you get things down to the most fundamental atomic pieces, your LLMs can do far more. And last: evals first. Always ensure you have eval-driven development.</p>
<p>Test each one of your changes. No matter how good your intuition is, evals tell you the truth. And you have to choose: cost, uncertainty, or lag. Two out of three. Thank you. [APPLAUSE]</p>

</details>
