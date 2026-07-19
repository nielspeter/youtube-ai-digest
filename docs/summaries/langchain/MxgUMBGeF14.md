---
title: "How to use dcode + Nemotron 3 Ultra"
channel: "LangChain"
video_id: MxgUMBGeF14
url: https://www.youtube.com/watch?v=MxgUMBGeF14
published: 2026-07-08T17:22:45+00:00
generated: 2026-07-16T21:17:28+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/MxgUMBGeF14/hqdefault.jpg
---
# How to use dcode + Nemotron 3 Ultra

[![How to use dcode + Nemotron 3 Ultra](https://i.ytimg.com/vi/MxgUMBGeF14/hqdefault.jpg)](https://www.youtube.com/watch?v=MxgUMBGeF14)

[Watch on YouTube](https://www.youtube.com/watch?v=MxgUMBGeF14) · **LangChain** · 2026-07-08

## TL;DR
This video demonstrates how to use Deep Agents Code (dcode), an open-source, model-agnostic coding agent, with Nemotron 3 Ultra—a 550 billion parameter open model hosted on Baseten. It walks through installation, setup, and running tasks, while highlighting dcode's features like goal-oriented sessions and first-class observability through LangSmith tracing.

## Key Takeaways
- Nemotron 3 Ultra is a 550 billion parameter open model offering frontier-model-comparable intelligence at 3–6 times the speed of other open models, reaching up to 300 tokens per second.
- While tools like Claude Code or Codex are provider-specific, dcode (Deep Agents Code) is a model-agnostic terminal coding agent optimized for Nemotron 3 and other open models.
- dcode offers a familiar terminal-based coding agent experience with skills, sub-agents, and MCP support.
- LangSmith integration provides first-class tracing, giving users complete visibility into what the agent is doing under the hood.
- dcode includes unique features like `/goal`, which declares a session objective and drafts acceptance criteria to guide the agent.
- Baseten is used as the model provider, requiring an API key for integration.
- For enterprise use, NVIDIA's newly released NemoClaw Deep Agents Blueprint offers a secure, governed reference stack for running open models.
- Open models, when paired with the right harness and stack, are a first-class choice for teams wanting control over their inference.

## Detailed Breakdown

### The Case for Open Models and Nemotron 3 Ultra [00:00](https://www.youtube.com/watch?v=MxgUMBGeF14&t=0s)
The video opens by highlighting a new era in agent engineering where open models are solving previously out-of-reach problems economically. It introduces Nemotron 3 Ultra, a 550 billion parameter model with strong reasoning performance that runs up to 300 tokens per second at a fraction of the cost of frontier models. On the Artificial Analysis Intelligence Index, Nemotron 3 Ultra sits in a quadrant of its own, displaying comparable intelligence at 3 to 6 times the speed of other open models.

### Introducing Deep Agents Code (dcode) [00:31](https://www.youtube.com/watch?v=MxgUMBGeF14&t=31s)
The presenter explains that a model is only as good as the harness driving it. Tools like Claude Code or Codex are excellent but built for provider-specific models. To maximize Nemotron 3's performance, you need dcode (Deep Agents Code)—an open-source, model-agnostic coding agent with built-in optimizations for Nemotron 3 and other open models. dcode offers a terminal-based experience similar to Claude Code, with skills, sub-agents, and MCP support, plus first-class tracing through LangSmith.

### Installation and Setup [01:34](https://www.youtube.com/watch?v=MxgUMBGeF14&t=94s)
The walkthrough begins at the Deep Agents Code docs website, where users copy an install script and paste it into the terminal. After installation, typing `dcode` launches the agent, which runs through an initialization process. Users select their model by typing "Nemotron" to find Baseten Nemotron. The setup prompts for an API key for web search (which the presenter skips) and then installs the Baseten integration, requiring a Baseten API key. Users can obtain a key from Baseten.co by logging in or creating an account.

### Running Tasks and Exploring Features [03:09](https://www.youtube.com/watch?v=MxgUMBGeF14&t=189s)
With setup complete, the presenter kicks off a long-running task: building an LLM chat app powered by deep agents. While that runs, a second dcode session is opened to explore features. The presenter authenticates with LangSmith via `/auth` for observability. Other features highlighted include `/threads` to browse and resume prior conversations, `/offload` to free up context, and `/mcp` to configure MCP servers.

### The `/goal` Feature [04:19](https://www.youtube.com/watch?v=MxgUMBGeF14&t=259s)
A standout feature is `/goal`, which declares an objective for the session. The presenter types "please help me write a song," and dcode drafts acceptance criteria (e.g., topic and theme defined, user confirmed the song's central subject). Users can edit or accept the criteria, after which the agent works toward the goal, asking questions as needed.

### Observability with LangSmith [05:25](https://www.youtube.com/watch?v=MxgUMBGeF14&t=325s)
The presenter checks the long-running task by visiting localhost:8000, revealing a working chat app. The focus then shifts to LangSmith, the observability platform providing complete visibility into agent behavior. Because LangSmith tracing was enabled earlier, traces from the dcode conversation are visible. Clicking a trace shows a turn-by-turn breakdown from input to output. The "details" view reveals token counts at different granularity levels, including chat invocations and tool calls like `read file`.

### Enterprise Deployment with NVIDIA NemoClaw [06:50](https://www.youtube.com/watch?v=MxgUMBGeF14&t=410s)
For enterprise use beyond local testing, the video highlights NVIDIA's newly released NemoClaw Deep Agents Blueprint—an open-source reference stack for building secure, governed agents. This collaboration enables running open models in a secure environment. The presenter notes that with the right harness and stack, open models are a first-class choice for teams wanting control over inference, and invites viewers to request more content on open models and dcode.

## Notable Quotes
- "A model is only as good as the harness driving it."
- "Nemotron 3 Ultra sits in a quadrant of its own, displaying a comparable intelligence at 3 to 6 times the speed of other open models."
- "With the right harness and stack behind them, open models can be a first class choice for teams that want control over their inference."

## People, Tools & References Mentioned
- **Nemotron 3 Ultra** — 550B parameter open model
- **Baseten** — Model provider used for hosting Nemotron 3 Ultra
- **Deep Agents Code (dcode)** — Open-source, model-agnostic coding agent
- **LangSmith** — Observability platform for tracing agent behavior
- **Claude Code / Codex** — Provider-specific coding agents mentioned for comparison
- **NVIDIA NemoClaw Deep Agents Blueprint** — Open-source enterprise reference stack for secure, governed agents
- **Artificial Analysis Intelligence Index** — Benchmark plotting model intelligence against speed
- **MCP (Model Context Protocol)** — Supported in dcode for server configuration

## Who Should Watch
This video is ideal for developers and engineering teams interested in using powerful open models like Nemotron 3 Ultra for coding agents, especially those who want model-agnostic tooling with strong observability. It's also valuable for enterprise teams exploring secure, governed deployments of open-source agent stacks.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=0s">00:00</a></span> We&#x27;re entering a new era in agent engineering, where open models are solving problems that used to be out of reach, running capable agents at a scale that just wasn&#x27;t economical before. In this video, you&#x27;ll see how to get rolling with one such model, Nemotron 3 Ultra, using Baseten as our model provider. Nemotron 3 Ultra is a 550 billion parameter model with strong reasoning performance running up to a blazing 300 tokens per second at a fraction of the cost of frontier models.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=31s">00:31</a></span> On an Artificial Analysis Intelligence Index plotting model intelligence against speed, Nemotron 3 Ultra sits in a quadrant of its own, displaying a comparable intelligence at 3 to 6 times the speed of other open models. But a model is only as good as the harness driving it. Tools like Claude Code or Codex are excellent. However, they&#x27;re built to run provider-specific models. To get maximum performance out of Nemotron 3, you need a coding agent which isn&#x27;t just</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=63s">01:03</a></span> provider agnostic but tuned to perform with Nemotron. That&#x27;s where Deep Agents Code comes in, or dcode for short. It&#x27;s the open source, model agnostic coding agent with optimizations built in for Nemotron 3 and other open models. Dcode has a similar experience to Claude Code. a terminal based coding agent with skills, sub agents and MCP support. Later in the video, we&#x27;ll see that it also has first class tracing through LangSmith. So you can see exactly</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=94s">01:34</a></span> what&#x27;s going on with your agent under the hood. With that said, let&#x27;s get up and running with dcode and Nemotron 3 Ultra. Okay, so to begin with head over to the Deep Agents Code docs website. We&#x27;ll include the link below and then copy this install script. over to terminal, paste that in and press enter. It&#x27;ll install pretty quickly. And once it&#x27;s done, you can type in dcode. And now we&#x27;re in. So Deep Agents Code, or dcode, for</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=128s">02:08</a></span> short will run you through the initialization process. You can enter your name. I&#x27;m going to skip this for now. And then we can select our model. We have a lot of options here, Let&#x27;s type in Nemotron and there we will see Baseten Nemotron. Press enter, dcode will ask us for our API key to enable web search for Nemotron. We&#x27;re going to skip this for now too though. Now we&#x27;ll install the Baseten integration,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=158s">02:38</a></span> restart the server and in a second it will prompt us for our API key for Baseten. Now if you don&#x27;t already have an API key for Baseten, you can go to Baseten .co and login if you already have an account or get started if you don&#x27;t. I already have my API key handy, so I&#x27;ll just type that in, press enter, and we&#x27;re ready to get to work. You can use Deep Agents Code with Nemotron, just like Claude or Codex or any other coding</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=189s">03:09</a></span> agent. So let&#x27;s go ahead and kickstart a long running task. Let&#x27;s do build an LLM chat app powered by deep agents. And the agent will go to work. And this will give us an opportunity to check out some of the other features in dcode. So we will open a new tab and fire up a new dcode session. And once we&#x27;re in dcode again, let&#x27;s type /auth. So here</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=222s">03:42</a></span> we can authenticate with a bunch of different integrations, let&#x27;s scroll down to LangSmith. So we&#x27;re going to talk much more about LangSmith later in the video, but what you need to know now is that it gives complete visibility into what&#x27;s going on under the hood with your dcode agent. So enter your API key, press enter, and then escape to get back. And so Nemotron inherits all of the features that you would expect from a first class coding agent. /threads to browse and resume prior conversations. /offload to free up some</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=259s">04:19</a></span> context. And /mcp to configure MCP servers. But one cool new feature that I&#x27;m really excited about is the /goal feature. So we&#x27;ll type /goal. And I will say, please help me write a song. So what this does is it declares an objective for the session. Dcode will draft acceptance criteria like topic and theme is defined, users confirmed the song&#x27;s central</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=290s">04:50</a></span> subject and so on and so forth. And then we can optionally move forward or edit the criteria, but I&#x27;ll go ahead and move forward with it. And the agent will get to work. It might ask questions, it will help guide our session toward the goal. Really looking forward to a longer, more in-depth video on this in the future, but for now, let&#x27;s check back in with our long-running task by opening up the browser and visiting localhost:8000. And we have</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=325s">05:25</a></span> a chat app. Let&#x27;s take a peek under the hood now. What you&#x27;re looking at here is LangSmith. This is our observability platform that gives you complete visibility into your agent behavior. And so because we enabled LangSmith tracing earlier, we can see traces from our conversation in dcode. I&#x27;ll click on to a trace and then we see a turn by turn breakdown starting from when I said, please build me a chat app powered by deep agents.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=357s">05:57</a></span> That of course is our input, and then we can see some outputs here. Once again broken down turn by turn. We can get more information here though by clicking on details at the top right. Once again we see our inputs and our outputs, but we can also hover our cursor over the first turn, where we see a token breakdown of inputs, outputs in total, and then we can see that at different levels of granularity. So here&#x27;s a chat invocation with a lot of the same information or a read file tool</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=393s">06:33</a></span> call. There&#x27;s a lot more that I could talk about with LangSmith and observability, but if you&#x27;re interested, check out some of our other videos on LangSmith. So we just ran Deep Agents locally with Nemotron. That may be fine for testing, but for enterprise use, you may want to run it in a secure, governed environment. That&#x27;s exactly what our collaboration with NVIDIA enables. Just today, NVIDIA released their NemoClaw Deep Agents Blueprint, the open source reference stack for enterprises to build secure, governed agents.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=MxgUMBGeF14&amp;t=426s">07:06</a></span> We dig into that blueprint in another video, but the through line here is that with the right harness and stack behind them, open models can be a first class choice for teams that want control over their inference. I think there&#x27;s a really exciting future for open models, and there&#x27;s so much more that we can talk about here. If you want to hear more about open models and dcode, let us know in the comments or on X. See you in the next one.</p>

</details>
