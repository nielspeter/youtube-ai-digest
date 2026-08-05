---
title: "How Madrigal Pharmaceuticals Cut Time to Production From 12 Weeks to 2 with LangChain & LangSmith"
channel: "LangChain"
video_id: D-SByYTJxUA
url: https://www.youtube.com/watch?v=D-SByYTJxUA
published: 2026-08-05T18:11:08+00:00
generated: 2026-08-05T19:54:58+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/D-SByYTJxUA/hqdefault.jpg
---
# How Madrigal Pharmaceuticals Cut Time to Production From 12 Weeks to 2 with LangChain & LangSmith

[![How Madrigal Pharmaceuticals Cut Time to Production From 12 Weeks to 2 with LangChain & LangSmith](https://i.ytimg.com/vi/D-SByYTJxUA/hqdefault.jpg)](https://www.youtube.com/watch?v=D-SByYTJxUA)

[Watch on YouTube](https://www.youtube.com/watch?v=D-SByYTJxUA) · **LangChain** · 2026-08-05

## TL;DR
Madrigal Pharmaceuticals leveraged LangChain and LangSmith to scale AI across departments with robust retrieval, context engineering, and observability. By adopting these tools, they reduced their time to production for agentic use cases from 12 weeks to just 2 weeks, while maintaining enterprise reliability and full deployment control.

## Key Takeaways
- Madrigal treats AI as a scalable capability, emphasizing infrastructure and system engineering over interfaces alone.
- LangSmith provides observability and traceability, described as "neuroimaging for agents," enabling fine-tuning of retrieval and analysis behavior.
- Deploying AI agents at scale is a major challenge; LangSmith simplifies this with one-click deployment, GitHub integration, and branch control.
- Teams can test agents in LangSmith Studio before connecting them to their own UI.
- LangChain offers modular agent-building blocks that accelerate development significantly.
- Madrigal values the combination of open-source community innovation with enterprise-grade reliability.
- The partnership with LangChain goes beyond a vendor relationship—they collaborate with developers who understand the pain points of building AI systems.
- Time to production for agentic use cases dropped from 12 weeks to 2 weeks.
- Multiple datasets and use cases across departments are served by a unified, observable infrastructure.
- Engineers can inspect and adjust granular agent behaviors, such as how many documents are retrieved and how they are analyzed.

## Detailed Breakdown

### AI as a Scalable Capability [00:00](https://www.youtube.com/watch?v=D-SByYTJxUA&t=0s)
Madrigal views AI not as a single tool but as a broad capability that must scale across the organization. This requires large-scale retrieval, synthesis, and context engineering. The speaker stresses that infrastructure compounds in value over time, while interfaces alone do not scale—system engineering is essential.

### LangSmith for Observability and Traceability [00:30](https://www.youtube.com/watch?v=D-SByYTJxUA&t=30s)
With many datasets and use cases across departments, Madrigal needs accuracy and scalability. LangSmith's observability, traceability, and deployment features make this seamless. The speaker vividly describes looking at a LangSmith trace as "peering into the brain of our AI agent," allowing them to change how the agent works and verify it behaves as intended. Fine-tuning extends to granular details like document retrieval counts and analysis methods.

### Simplified Deployment at Scale [01:01](https://www.youtube.com/watch?v=D-SByYTJxUA&t=61s)
Deploying AI agents at scale is notoriously difficult, often requiring custom orchestration. LangSmith changes this: the speaker was surprised by how easy it was to click "deploy" and have the agent go live. Agents can be tested in LangSmith Studio, then connected to a custom UI. Deployment control includes GitHub repo integration, with support for dev and production branches—offering both simplicity and full version control.

### Open Source Innovation with Enterprise Reliability [01:31](https://www.youtube.com/watch?v=D-SByYTJxUA&t=91s)
Madrigal benefits from open-source community-driven innovation without sacrificing the reliability that enterprise AI demands. LangChain unites iterative development with full visibility across the process, bridging the gap between rapid prototyping and production-grade stability.

### Dramatic Reduction in Time to Production [02:03](https://www.youtube.com/watch?v=D-SByYTJxUA&t=123s)
Thanks to LangChain's modular architecture for building agents at scale, Madrigal's time to production for agentic use cases dropped from 12 weeks to 2 weeks. The speaker highlights the value of partnering with LangChain developers who understand the challenges of building such systems—not just buying a product, but collaborating with a team that shares their mindset and pain points.

## Notable Quotes
- "The first time I looked at a trace in LangSmith, I felt like I was peering into the brain of our AI agent."
- "It's really like neuroimaging for agents. You can fine-tune everything down to how many documents they're retrieving, how they're analyzing, everything about what an agent does."
- "I was honestly surprised with how easy it was to just click the deploy button on LangSmith and have the agent live."
- "Our time to production of agentic use case has dropped from 12 weeks to two weeks."
- "We're able to work with someone that has a similar mindset and knows the similar pains of bringing something like this to life."

## People, Tools & References Mentioned
- **Madrigal Pharmaceuticals** — the organization featured in the video
- **LangChain** — modular framework for building AI agents at scale
- **LangSmith** — platform for observability, traceability, testing, and deployment of AI agents
- **LangSmith Studio** — environment for testing agents before connecting to a custom UI
- **GitHub** — integrated with LangSmith for deployment branch control

## Who Should Watch
AI engineers, platform leads, and pharma/enterprise technology decision-makers who want to understand how observability and modular agent frameworks can dramatically accelerate production deployment while maintaining enterprise-grade reliability.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=D-SByYTJxUA&amp;t=0s">00:00</a></span> So, at Madrigal, our focus is to really think about AI overall as a capability. Scaling force also means how do we leverage large-scale retrieval, large-scale synthesis, large-scale context engineering. Infrastructure for us, you know, compounds over time, and uh interfaces, unfortunately, alone doesn&#x27;t scale. So, you need infrastructure and system engineering overall to scale. We have a lot of different data sets and a lot of different use cases across departments. Um to be able to deploy</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=D-SByYTJxUA&amp;t=30s">00:30</a></span> departments. Um to be able to deploy that at scale, have accuracy, and um meet the business needs, LangSmith uh observability, traceability, and deployments have made that extremely seamless. The first time I looked at a trace in LangSmith, I felt like I was peering into the brain of our AI agent. And the upshot of that is you can change how it&#x27;s working, and then make sure that it&#x27;s doing exactly what you want it to. It&#x27;s really like neuroimaging for agents. You can fine-tune everything down to how many documents they&#x27;re retrieving, how they&#x27;re analyzing, everything about what an agent does. One of the most</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=D-SByYTJxUA&amp;t=61s">01:01</a></span> an agent does. One of the most difficult things about building AI agents in any company is deploying it at scale. One choice is to build custom deployments, orchestrate everything on your own. That&#x27;s very difficult and time-consuming. I was honestly surprised with how easy it was to just click the deploy button on LangSmith and have the agent live. You can test it in LangSmith Studio. You can then connect it to your own UI. It&#x27;s extremely easy to have multiple deployments. It just connects to your GitHub repo for that project. You can have a dev and a production branch. You can have all the control</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=D-SByYTJxUA&amp;t=91s">01:31</a></span> branch. You can have all the control that you want of deployments, but it&#x27;s extremely easy and simple. We have access to the community-driven innovation of the open source community without sacrificing the enterprise reliability that um you enterprise AI really needs. And that unites the iterative developments with the full visibility throughout the entire process. Because of LangChain&#x27;s innate modular nature of building agents at scale. Our time to production of agentic use case has dropped from 12 weeks to two weeks. Our strong team of engineers</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=D-SByYTJxUA&amp;t=123s">02:03</a></span> two weeks. Our strong team of engineers is able to take a very sophisticated tool and make the most out of it. And that&#x27;s the value add that we see in partnering with Launch Chain. We are not just working in isolation, we&#x27;re working with a team of developers that knows what they&#x27;re building. Rather than just buying a product, we&#x27;re able to work with someone that has a similar mindset and knows the similar pains of bringing something like this to life.</p>

</details>
