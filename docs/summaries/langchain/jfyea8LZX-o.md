---
title: "How Salesforce Standardizes Agent Evals with LangSmith"
channel: "LangChain"
video_id: jfyea8LZX-o
url: https://www.youtube.com/watch?v=jfyea8LZX-o
published: 2026-07-23T18:43:14+00:00
generated: 2026-07-23T19:42:08+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/jfyea8LZX-o/hqdefault.jpg
---
# How Salesforce Standardizes Agent Evals with LangSmith

[![How Salesforce Standardizes Agent Evals with LangSmith](https://i.ytimg.com/vi/jfyea8LZX-o/hqdefault.jpg)](https://www.youtube.com/watch?v=jfyea8LZX-o)

[Watch on YouTube](https://www.youtube.com/watch?v=jfyea8LZX-o) · **LangChain** · 2026-07-23

## TL;DR
Salesforce's Agent Force team uses LangSmith to standardize and scale evaluations for the MCP tools that power their enterprise "vibe coding" product. By running thousands of test cases against shared metrics—instruction following, coherence, factuality, and deployability—they catch quality issues before reaching customers and have recently surpassed 100 million lines of accepted generated code.

## Key Takeaways
- Agent Force is Salesforce's enterprise "vibe coding" product, launched in October 2025, for building app components and metadata.
- Before LangSmith, individual teams built their own MCP tools and each struggled independently to validate tool outputs.
- LangSmith enables at-scale evaluation and trace inspection so the team can diagnose unexpected outputs and make improvements before customer impact.
- It amplifies internal expertise by letting teams reuse the same evaluation structures and tests rather than reinventing the wheel.
- LangSmith sets a shared standard across teams with metrics including instruction following, coherence, factuality, and deployability.
- The team runs thousands and thousands of test cases through LangSmith.
- Agent Force recently crossed a milestone of over 100 million lines of accepted code.
- LangSmith serves as the single evaluation tool ensuring the quality of all generated code.

## Detailed Breakdown

### Agent Force and the Pre-LangSmith Problem [00:00](https://www.youtube.com/watch?v=jfyea8LZX-o&t=0s)
The speaker introduces their team as one of the groups building Agent Force, Salesforce's enterprise "vibe coding" product launched in October 2025. Prior to adopting LangChain, various teams were independently building MCP tools to generate metadata and components for the app-building process. The core challenge was ensuring those tools produced expected outputs, and every team was trying to solve this validation problem on their own.

### Finding LangSmith and Scaling Evaluations [00:32](https://www.youtube.com/watch?v=jfyea8LZX-o&t=32s)
The team discovered LangChain and, specifically, LangSmith as the solution to their fragmented evaluation problem. LangSmith allowed them to evaluate tool outputs at scale and inspect traces to understand why unexpected outputs occurred. This trace visibility helped them make targeted improvements before any code reached customers, effectively amplifying their internal expertise by enabling thousands of test cases.

### Standardizing Metrics Across Teams [01:02](https://www.youtube.com/watch?v=jfyea8LZX-o&t=62s)
Beyond running tests, LangSmith helped establish a common evaluation standard across all teams. Instead of each team reinventing the wheel, they could reuse the same structure and tests. The shared metrics include instruction following, coherence, factuality, and deployability, ensuring every team evaluates its work against the same criteria.

### 100 Million Lines of Accepted Code [01:34](https://www.youtube.com/watch?v=jfyea8LZX-o&t=94s)
Agent Force recently passed a significant milestone: over 100 million lines of accepted code. LangSmith plays a critical role as the single evaluation tool that ensures all of that generated code meets quality standards.

## Notable Quotes
- "Before LangChain, teams were building their own MCP tools to generate metadata, generate components, basically all the pieces of the app building process. And the problem is, how do you make sure that those tools that teams were building were outputting what you expect."
- "LangSmith helps us to amplify our internal expertise, allowing us to run thousands and thousands of test cases. It makes it so that teams don't have to reinvent the wheel every time."
- "LangSmith makes it easier for everyone to evaluate against the same criteria."
- "Recently, Agent Force 5's just passed an amazing milestone. We've hit over 100 million lines of accepted code."

## People, Tools & References Mentioned
- **Agent Force** — Salesforce's enterprise vibe coding product, launched October 2025
- **LangChain** — Framework adopted by the team for evaluation
- **LangSmith** — LangChain's evaluation and tracing tool, used as the single eval tool
- **MCP tools** — Tools teams built to generate metadata and app components
- **Evaluation metrics mentioned:** instruction following, coherence, factuality, deployability

## Who Should Watch
Engineering leaders and developers building LLM-powered code generation or agent products—especially those scaling evaluation across multiple teams—will find this a concise, practical case study on standardizing evals and ensuring output quality before customer delivery.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=jfyea8LZX-o&amp;t=0s">00:00</a></span> We&#x27;re one of the teams building Agent Force vibes, which is Salesforce&#x27;s enterprise vibe coding product that we launched in October of 2025. Before LangChain, teams were building their own MCP tools to generate metadata, generate components, basically all the pieces of the app building process. And the problem is, how [snorts] do you make sure that those tools that teams were building were outputting what you expect. Every team</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jfyea8LZX-o&amp;t=32s">00:32</a></span> outputting what you expect. Every team was sort of trying to figure this out all on their own. And that&#x27;s when we found LangChain and specifically LangSmith, we can evaluate these at scale. We can look at the traces to see why are things outputting something that we might not expect. How do we make improvements to those? And we do this all at scale prior to this hitting our customers. LangSmith helps us to amplify our internal expertise,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jfyea8LZX-o&amp;t=62s">01:02</a></span> expertise, allowing us to run thousands and thousands of test cases. It makes it so that teams don&#x27;t have to reinvent the wheel every time. They can use the same structure and tests to see that what they&#x27;re building is actually doing what they expect. LangSmith also helps us to set a standard across what teams are scoring on, including instruction following, coherence, factuality, deployability. We have a lot of metrics that we want to make sure each team is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=jfyea8LZX-o&amp;t=94s">01:34</a></span> that we want to make sure each team is using, and LangSmith makes it easier for everyone to evaluate against the same criteria. Recently, Agent Force 5&#x27;s just passed an amazing milestone. We&#x27;ve hit over 100 million lines of accepted code. And that&#x27;s where LangSmith comes in as a single eval tool that we can use to make sure that all that code that we&#x27;re generating is of quality.</p>

</details>
