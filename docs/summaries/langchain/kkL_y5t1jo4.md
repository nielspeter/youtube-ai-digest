---
title: "The LangChain Team Answers the Most Searched Questions About Agents"
channel: "LangChain"
video_id: kkL_y5t1jo4
url: https://www.youtube.com/watch?v=kkL_y5t1jo4
published: 2026-07-14T20:28:06+00:00
generated: 2026-07-16T20:27:13+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/kkL_y5t1jo4/hqdefault.jpg
---
# The LangChain Team Answers the Most Searched Questions About Agents

[![The LangChain Team Answers the Most Searched Questions About Agents](https://i.ytimg.com/vi/kkL_y5t1jo4/hqdefault.jpg)](https://www.youtube.com/watch?v=kkL_y5t1jo4)

[Watch on YouTube](https://www.youtube.com/watch?v=kkL_y5t1jo4) · **LangChain** · 2026-07-14

## TL;DR
Amy and Sean from LangChain answer the web's most searched questions about AI agents, covering fundamentals like what agents are, RAG, MCP, and memory, as well as practical concerns like hallucination, human-in-the-loop design, and evaluation. They frame LangChain's suite of tools—Deep Agents, Fleet, LangGraph, and LangSmith—as solutions for the full agent development lifecycle, from building to production monitoring.

## Key Takeaways
- An agent is an LLM running in a loop with the ability to call tools, iterating through a "decide, act, reason, repeat" cycle.
- RAG (Retrieval Augmented Generation) gives a model relevant context right before it answers, like an open-book test instead of memorization.
- MCP (Model Context Protocol) standardizes tool connections for agents, acting like a "USB-C cable" so you write a server once and connect it everywhere.
- Agents amplify hallucination risk because errors compound across steps; evals are essential to catch regressions.
- The agent development lifecycle has four phases: build, test, deploy, and monitor.
- Human-in-the-loop is a deliberate design pattern where agents pause for human approval on high-stakes actions; the best teams don't aim for full autonomy on day one.
- Agent evals differ from traditional software testing because inputs and outputs are non-deterministic; teams should define "what good looks like" and run evals continuously.
- LangChain has evolved from an open-source framework into a full-lifecycle platform, with LangGraph for orchestration, Deep Agents for code-based building, Fleet for no-code building, and LangSmith for testing, deployment, and monitoring.
- LangSmith is framework-agnostic and works with any model or framework, not just LangChain's own tools.
- Over 7,000 organizations—including NVIDIA, Bridgewater, and Harvey—use LangSmith to keep agents reliable in production.

## Detailed Breakdown

**[00:00] Intro & What Is an Agent?**
Amy and Sean introduce the format: answering the internet's most searched questions about agents. The first question asks what an agent actually is. Sean explains that "agent" isn't just a buzzword—at its core, an agent is an LLM running in a loop with the ability to call tools (functions). The model picks a tool, examines the result, and then either produces a final answer or calls another tool. That "decide, act, reason, repeat" loop is what defines an agent.

**[01:05] What Is RAG?**
Amy describes Retrieval Augmented Generation as giving a model an open-book test rather than requiring it to memorize everything. Since models are trained on public data, they lack context about private information like company docs or customer history. RAG retrieves relevant information and injects it into the model's context right before it answers.

**[01:35] What Is MCP?**
Sean compares MCP (Model Context Protocol) to a USB-C cable for agents. Before MCP, every tool connection had to be custom-built—one integration per database, API, or file system. MCP provides a standard plug that any compliant model can use: write the server once, connect it to everything. It has quickly become the default for how agents interact with external systems.

**[02:06] Why Do Agents Hallucinate?**
Sean clarifies that technically the model hallucinates, not the agent itself—LLMs are "glorified word guessers" that sound equally confident whether right or wrong. Agents make this more dangerous because errors compound: a hallucinated fact in step two poisons everything downstream, and the loop amplifies the mistake. This is why you can't just "vibe check" an agent; you need evals to verify it actually works.

**[02:37] What Is the Agent Development Lifecycle?**
Amy outlines four phases: build in code (using a framework like Deep Agents), test with real inputs and expected outputs, deploy into production, and monitor with tracing and evals. Sean notes they literally have this on a poster.

**[03:07] What Is Memory?**
Sean explains that memory is how agents hold onto information beyond a single run. Short-term memory is the context window—everything in scope right now, like remembering what you had for breakfast. Long-term memory persists across runs: user preferences, past decisions, and learned facts, like remembering a parent's birthday every year.

**[03:37] What Is Human in the Loop?**
Amy describes human-in-the-loop as a design pattern where the agent pauses and waits for human approval before taking a next action. The best production agents use this deliberately—letting the agent handle routine work but interrupting for high-stakes actions (like sending a message on someone's behalf). She emphasizes that the best teams aren't going for full autonomy on day one; they're building systems where humans and agents divide work intelligently.

**[04:42] How Do You Evaluate an Agent?**
Sean calls this a "spicy" topic and advocates strongly for agent evals. Unlike traditional software where specific inputs yield expected outputs, agents deal with natural language inputs and non-deterministic outputs. Instead of testing for exact matches, you define what "good" looks like for your use case, potentially using an LLM-as-judge to evaluate individual steps. You build a dataset of real-world examples and edge cases, then run those tests every time you change the agent. Amy adds that evals should run continuously—not just before shipping—so you catch regressions immediately when tweaking prompts or swapping models. Sean compares evals to a muscle: build it early and run it constantly, because the alternative is discovering your agent started recommending the wrong product three weeks ago via a customer complaint.

**[05:45] What Is LangChain?**
Amy calls this her favorite question. LangChain started as an open-source framework that predates ChatGPT, helping engineers wrangle LLMs before "prompt" was a household word. As developers wanted to build agents, LangChain released LangGraph, an agent runtime and low-level orchestration framework. Since then, the company has evolved beyond an open-source framework to serve the full agent development lifecycle: building (LangChain, LangGraph, Deep Agents), testing (evals, regression testing), deployment (LangSmith deployments), and monitoring (also through evals and LangSmith). Both Amy and Sean stress that building the agent is the fun, easy part—keeping it from going sideways in production is the hard, more important part. Over 7,000 organizations, including NVIDIA, Bridgewater, and Harvey, use LangSmith to ship agents that hold up in production.

**[07:21] How Do I Get Started Building Agents?**
Amy offers two paths. For developers comfortable with code, Deep Agents is the easiest starting point, with built-in task planning, file systems for context management, sub-agents, and long-term memory. For those new to agents or who prefer no code, Fleet lets you build agents using natural language—describe what you want, and Fleet builds it, then lets you share it across your team. Either way, you can integrate into LangSmith for testing, deploying, and monitoring. Amy highlights that LangSmith identifies where decisions went wrong and what the agent was reasoning, and it works with any framework or model—not just LangChain's own tools. The video closes with a plug for LangChain Academy for full-length courses.

## Notable Quotes
- "At its core, an agent is just an LLM running in a loop with the ability to call tools." — Sean
- "I'd think of retrieval augmented generation as giving the model an open book test instead of making it memorize everything." — Amy
- "MCP is a standard plug that any compliant model can use. You write the server once, you connect it to everything." — Sean
- "One hallucinated fact in step two poisons step three, step four, and everything downstream, and the loop sort of just amplifies this mistake." — Sean
- "The best teams sort of shipping the best agents aren't really going for full autonomy on day one. They're building systems where humans and agents can divide the work very intelligently." — Amy
- "Building the agent is really fun and kind of easy now, but actually keeping it from going completely sideways in production is the hard part." — Amy
- "The teams that really get this right treat evals sort of as a muscle. You build it early, you're running it constantly." — Sean

## People, Tools & References Mentioned
- **People:** Amy, Sean, Harrison (referenced in a human-in-the-loop example)
- **LangChain products:** LangChain (open-source framework), LangGraph (agent runtime/orchestration), Deep Agents (code-based agent builder), Fleet (no-code agent builder), LangSmith (platform for testing, deployment, monitoring, observability), LangChain Academy (courses)
- **Concepts & protocols:** Agents, RAG, MCP (Model Context Protocol), human-in-the-loop, short-term and long-term memory, agent evals, LLM-as-judge, agent development lifecycle, tracing
- **Organizations mentioned as LangSmith users:** NVIDIA, Bridgewater, Harvey (7,000+ organizations total)
- **Other references:** ChatGPT

## Who Should Watch
Developers, engineers, and technical product managers who want a concise, beginner-friendly overview of what AI agents are and how to build, evaluate, and deploy them responsibly. It's especially useful for those evaluating LangChain's ecosystem of tools for bringing agents to production.


<details class="transcript">
<summary>Full transcript</summary>

<p>Human in the loop. Hi, I&#x27;m Amy. And I&#x27;m Sean. Today we&#x27;ll answer every question about agents, from what even is an agent, all the way to-- Will this thing eat my job? The internet has lots. We have answers. Let&#x27;s get into it. [MUSIC PLAYING] Question one. What is an agent? All right, good. So we got an easy one to start. I can take this one. OK. Honestly, people get confused about this all the time. I kind of thought agent was just a marketing buzzword join me here. At its core, an agent is just an LLM running in a loop with the ability</p>
<p>to call tools. Think of those tools as functions. The model has a task to complete. So it picks a tool, looks at what comes back, and then either formulates a final response or decides it needs to call another tool. That loop, decide, act, reason, repeat. That&#x27;s what makes an agent. Nice. What do you think? I think that makes sense. Yeah. All right, you get the next one. Question number two. What is RAG? So I would think of retrieval augmented generation as giving the model an open book test instead of making it memorize everything.</p>
<p>The model was trained on, let&#x27;s say, like public data so it doesn&#x27;t have any context on your company docs, your customer history, or your internal knowledge base. What RAG does is it retrieves what&#x27;s relevant, drops it into context right before the model answers. - Nice, that was a harder one, you did good. - Yeah. - All right, next one, maybe you won&#x27;t get another easy one. What is MCP? OK, MCP or model context protocol, kind of like a USB-C cable for agents. Before it, every tool connection was custom built</p>
<p>for your agents. One integration per database, per API, per file system. MCP is a standard plug that any compliant model can use. You write the server once, you connect it to everything. It&#x27;s quickly become the default for how agents talk to the rest of the world. Why do agents hallucinate? Ooh. OK. That&#x27;s a great question. I&#x27;d say technically it&#x27;s the model that hallucinates, not the agent. LLMs are essentially glorified word guessers. When that guess is wrong, it sounds just as confident as when it&#x27;s right.</p>
<p>I think agents make this a little bit more dangerous because errors compound, and so one hallucinated fact in step two poisons step three, step four, and everything downstream, and the loop sort of just amplifies this mistake. Which is exactly why you can&#x27;t just vibe check your agent and send it out into the world. You need to actually verify the agent knows what it&#x27;s doing. I use evals for that, and that&#x27;s kind of the de facto way to do that. Yeah, evals are great. Next question, this one&#x27;s a long one. What is the agent development lifecycle? So the agent development lifecycle is the process</p>
<p>that agent engineers use to build and improve their agents. There are four phases. You can build it in code with a framework like Deep Agents, test it with real inputs and expected outputs, deploy it into production and monitor it with tracing and evals. - Feel like we need this on a poster. - We literally have this on a poster. - I get the next question, &#x27;cause it looks way shorter. What is memory? See if I remember this one. Memory is how agents hold onto information</p>
<p>beyond a single run. - Short term memory is your context window, basically everything in scope right now. For example, I remember what I had for breakfast this morning. - Long term memory is what persists, things like user preferences, decisions from last week, facts that agents learned and need to carry forward. For example, I&#x27;m supposed to remember that my mom&#x27;s birthday is in October every year. (upbeat music) Next question, mine or yours? - I&#x27;ll take this one. - Oh, confidence. - I don&#x27;t know what it is yet. - We&#x27;ll see, we&#x27;ll see. What is human in the loop? - I&#x27;m glad I don&#x27;t have this one.</p>
<p>- I should have given Sean this one. I would say that human in the loop is sort of a design pattern where the agent pauses and waits for a human to approve before sort of like taking the next action. I think the best production agents use this very deliberately. Right? So like you&#x27;ll let the agent handle the routine and you only interrupt for like a really high stakes action. For example, like, hey, Sean, is it cool if I upload this video to YouTube? Yeah. OK. Not bad. How about if I send this message on your behalf to Harrison?</p>
<p>Probably not. I&#x27;d say the best teams sort of like shipping the best agents aren&#x27;t really going for full autonomy on day one. They&#x27;re sort of like building systems where humans and agents can divide the work very intelligently. All right, let&#x27;s see. I&#x27;m getting the next one then. How do you evaluate an agent? Agent evals. This one&#x27;s controversial. Guys, this one&#x27;s spicy. I&#x27;m obviously a big proponent of agent evals. One of the big reasons that we need different evals for agents than traditional software is with traditional software you can kind of expect</p>
<p>certain outputs and certain inputs. With agents, that&#x27;s very different. Right? The input can be all natural language. And then even for the same input, you&#x27;re not going to get the same outputs. Right? So instead of testing for exact outputs, you&#x27;re going to define what good looks like in your case. Yeah. Right? You can use like an LLM-as-judge to do that. It can test certain steps. Was it right without making something up? You&#x27;re then going to build a data set of real world examples, stuff that tests your agent, like edge cases, and then run those tests every time you make a change to your agent</p>
<p>to make sure you don&#x27;t regress on any of those evals. Yeah, sure. Sean sounds like an expert. And I think with evals, you want to make sure you run these continuously, not just before you ship. Every time you sort of tweak a prompt or you swap a model out, I think you want to immediately know if something has regressed. I think the teams that really get this right treat evals sort of as a muscle. You build it early, you&#x27;re running it constantly, because I think the alternative is like finding out your agent started recommending the wrong product three weeks ago from a customer complaint.</p>
<p>Yeah. And that&#x27;s a situation nobody wants to run into. Yeah, yeah. Getting close to the end. Chugging along. We&#x27;re almost there. What is LangChain? Oh, this is a good question. This is my favorite question. Oh, okay. Just say that. So LangChain started as an open source framework that actually predates ChatGPT. Wow. It&#x27;s kind of crazy. We&#x27;re really helping engineers sort of wrangle LLMs before most people have even heard of the word prompt. And I think as the space kind of changed and we saw developers wanting to build more agents, we released LangGraph, which is an agent runtime and low-level orchestration framework.</p>
<p>But since then we&#x27;ve evolved from just an open source framework. We&#x27;re not really that anymore. We now serve the full agent development lifecycle. That&#x27;s building, obviously, LangChain, LangGraph, Deep Agents. We talked about testing, which is like evals, regression testing, deployment, which is LangSmith deployments, right? your agent getting that runtime together, then monitoring, which is also sort of evals again. Those like testing, deployments, monitoring, that&#x27;s all coming through LangSmith, which is our platform for agent reliability, observability. Turns out building the agent is really fun.</p>
<p>Super fun. And kind of easy now, but actually keeping it from going completely sideways in production is the hard part. Super hard. Yeah. And people are sometimes less interested in learning about that, but it&#x27;s way more important than having a little demo agent. How do you actually bring it to production? So more than, I think it&#x27;s like 7,000 organizations, like some big names, NVIDIA, Bridgewater, Harvey, use LangSmith to ship these agents so they can actually hold up in production in front of their customers with their brand image on the line. Final question.</p>
<p>Last one. We&#x27;re just getting into the flow of things. Guys, this is so fun. I don&#x27;t want this to end. How do I get... But-- Oh, wow. The suspense is killing me. Started building agents. Oh, this is a great-- this is a great final question, actually. It&#x27;s not-- It&#x27;s an alien dolly question. The way I think about it is, if you&#x27;re a developer who is, I&#x27;d say, pretty comfortable building agents, Deep Agents is the easiest way to start building agents. It has built-in task planning, file systems for context management. You can create sub-agents and long-term memory.</p>
<p>Or if you&#x27;re brand new to building agents and you&#x27;re not really comfortable or you don&#x27;t want to get hands on with code, you could start building agents with Fleet. That&#x27;s our no code agent builder, where you build agents using natural language. You describe what you want, Fleet builds it for you. You can then share it across your entire team. So it&#x27;s kind of cool, then. It&#x27;s like kind of flexing a little bit, like look at this cool agent I just built. - Either way, you can integrate your agent into LangSmith, which is our platform for testing, deploying, and monitoring agents. - Yeah, great. I mean, as we cover that&#x27;s way more important</p>
<p>than actually building the agent. - And I think with LangSmith, you can actually identify where decisions went wrong, what your agent was reasoning. You can use these evals that Sean&#x27;s super excited about to measure agent performance and also validate your improvements before shipping. But I think the best part is that LangSmith actually works with any framework or model you choose. Oh, so it&#x27;s not just LangChain. It&#x27;s not just Deep Agents. It&#x27;s not just Fleet. Anything. Yeah. I mean, we could get them to try out both. Because? See what they think. All right. Links to both are in the description below. Try them out and tell us which one works best for you.</p>
<p>Thanks for joining the LangChain team on answering the web&#x27;s most searched questions about agents. - If you wanna learn more about any of the topics we covered today, check out LangChain Academy for full length courses starring yours truly and other LangChain educators. - Bye for now.</p>

</details>
