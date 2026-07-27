---
title: "How Credit Genie Debugs Thousands of Agent Traces with LangSmith"
channel: "LangChain"
video_id: s2mZ_vKNOfI
url: https://www.youtube.com/watch?v=s2mZ_vKNOfI
published: 2026-07-27T16:19:47+00:00
generated: 2026-07-27T17:52:34+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/s2mZ_vKNOfI/hqdefault.jpg
---
# How Credit Genie Debugs Thousands of Agent Traces with LangSmith

[![How Credit Genie Debugs Thousands of Agent Traces with LangSmith](https://i.ytimg.com/vi/s2mZ_vKNOfI/hqdefault.jpg)](https://www.youtube.com/watch?v=s2mZ_vKNOfI)

[Watch on YouTube](https://www.youtube.com/watch?v=s2mZ_vKNOfI) · **LangChain** · 2026-07-27

## TL;DR
Credit Genie built AskGenie, an AI financial assistant, using LangGraph for agent orchestration and LangSmith for observability and debugging. By leveraging LangSmith's traceability and insights features, they were able to diagnose agent confusion between similar tools, segment thousands of traces by use case, and build targeted test suites to improve performance at scale.

## Key Takeaways
- AskGenie is an AI financial assistant built on LangGraph, designed to help users understand their spending and achieve long-term financial stability through natural conversation.
- LangSmith serves as the observability platform for tracing, monitoring, and alerts across the agent's multi-step processes.
- The agent uses multiple tools, and similar tools (e.g., two customer support tools) could be confused or mixed by the AI, requiring careful evaluation of user intent.
- Traceability in LangSmith allowed the team to break down agent runs into individual steps and inspect the agent's reasoning.
- Manually reviewing thousands of traces proved difficult at scale, prompting the use of LangSmith's insights feature to automate segmentation.
- The insights feature enabled the team to group traces by use case, such as isolating customer support-related traces for deeper analysis.
- Questions extracted from segmented traces were turned into structured test suites of 100–200 questions, each targeting a specific behavior.
- The LangChain team provided highly responsive support, feeling more like an internal team than an external vendor.

## Detailed Breakdown

### What AskGenie Is and How It's Built [00:00](https://www.youtube.com/watch?v=s2mZ_vKNOfI&t=0s)
Credit Genie developed AskGenie, an AI financial assistant that acts as a "personal accountant" to help users achieve long-term financial stability. It is built on LangGraph as the agent orchestration layer, with LangSmith handling tracing, monitoring, and alerts. Users interact with it through natural language, asking questions like where their money is going and receiving conversational answers.

### Tool Confusion and Intent Evaluation [00:30](https://www.youtube.com/watch?v=s2mZ_vKNOfI&t=30s)
The agent involves multiple steps and tools, some of which are similar in nature. A key example is two customer support tools—one for answering general questions and another for connecting users to a live agent. The AI sometimes confused these, prompting the team to design two separate evaluators to correctly identify and act on customer intent.

### Using Traceability to Understand Agent Reasoning [01:02](https://www.youtube.com/watch?v=s2mZ_vKNOfI&t=62s)
LangSmith's traceability feature was critical for breaking down agent runs into their constituent steps. This allowed the team to see how the agent was reasoning at each stage and make targeted changes to improve performance. However, doing this manually across thousands of traces was not scalable.

### Scaling Debug with LangSmith Insights [01:36](https://www.youtube.com/watch?v=s2mZ_vKNOfI&t=96s)
To address the scale challenge, the team used LangSmith's insights feature, which automatically breaks down traces into different use cases. They were able to segment traces specifically related to customer support issues, then use the questions within those traces to construct focused test suites of 100–200 questions, each designed to verify a specific behavior.

### Collaboration with the LangChain Team [02:09](https://www.youtube.com/watch?v=s2mZ_vKNOfI&t=129s)
The team highlighted the responsiveness of the LangChain team, noting that communication felt like working with an internal team rather than an external company. Questions and issues were addressed within minutes, making the partnership feel like having LangChain as an embedded part of their organization.

## Notable Quotes
- "I like to think of as my personal accountant, sometimes it tells me I'm overspending which is another story."
- "We've noticed that sometimes the AI would mix and confuse the two. So we had to design two different evaluators to make sure that we got the intent of the customer right."
- "Doing this manually at a very large scale over thousands of traces, that proved to be hard."
- "Let's create a list of 100 to 200 questions, each aimed at trying to get one specific behavior."
- "It feels more similar to working with an internal team than an external company."

## People, Tools & References Mentioned
- **Credit Genie** — the company building AskGenie
- **AskGenie** — AI financial assistant for long-term financial stability
- **LangGraph** — agent orchestration layer
- **LangSmith** — observability platform for tracing, monitoring, alerts, and insights
- **LangChain** — the team/company behind LangSmith, noted for close collaboration

## Who Should Watch
AI engineers and product teams building multi-step LLM agents—especially those struggling with tool selection confusion, trace debugging at scale, or building behavioral test suites from production data—will find practical, directly applicable insights in this short case study.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=s2mZ_vKNOfI&amp;t=0s">00:00</a></span> We are building AskGenie, an AI financial assistant that helps users achieve long-term financial stability. So we built AskGenie on top of LangGraph, which we used as our agent orchestration layer. For tracing and monitoring as well as alerts, we used LangSmith as our observability platform. So if you&#x27;re able to interact with AskGenie, which I like to think of as my personal accountant, sometimes it tells me I&#x27;m overspending which is another story.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=s2mZ_vKNOfI&amp;t=30s">00:30</a></span> But it just facilitates the interaction using natural conversation of &quot;Hey, I wonder where my money is going, can you please tell me what those stories are?&quot; Our agent has multiple steps and processes. So a lot of the times where you have tools that the agent is supposed to use and some of your tools might be similar, for instance you have two customer support tools, one answering general customer support questions, and another one connecting the user to an actual customer support agent.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=s2mZ_vKNOfI&amp;t=62s">01:02</a></span> We&#x27;ve noticed that sometimes the AI would mix and confuse the two. So we had to design two different evaluators to make sure that we got the intent of the customer right. One of the most important things that we use was a combination of things that the LangSmith platform offers. Number one was just traceability. that allow us to break down our agent run into its multiple steps. And we were able to see how the agent was reasoning. And based on that, we were able to make a lot of the changes</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=s2mZ_vKNOfI&amp;t=96s">01:36</a></span> that allow us to improve its performance. But doing this manually at a very large scale over thousands of traces, that proved to be hard. But one of the things that helped us expedite the process was using the insights feature that allow us to basically break down all of our traces into its different use cases. And we were able to segment the traces that were directly related to customer support issues. And inside those, then we were able to use those questions</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=s2mZ_vKNOfI&amp;t=129s">02:09</a></span> to create tests. Let&#x27;s create a list of 100 to 200 questions, each aimed at trying to get one specific behavior. and let&#x27;s make sure that more often than not, we can get the results. One thing we like about working with the LangChain team is that it feels more similar to working with an internal team than an external company. Whether we were having questions of what was the best approach or we were running into certain issues, we were able to text them and get an answer back</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=s2mZ_vKNOfI&amp;t=161s">02:41</a></span> from them within minutes. So it really felt as having them as an early team within the company.</p>

</details>
