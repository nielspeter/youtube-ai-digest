---
title: "How 11x Built a Slack-Native Bug Triage Agent with LangSmith Fleet"
channel: "LangChain"
video_id: Z4DoEXhrPC8
url: https://www.youtube.com/watch?v=Z4DoEXhrPC8
published: 2026-07-15T16:53:16+00:00
generated: 2026-07-16T20:25:58+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/Z4DoEXhrPC8/hqdefault.jpg
---
# How 11x Built a Slack-Native Bug Triage Agent with LangSmith Fleet

[![How 11x Built a Slack-Native Bug Triage Agent with LangSmith Fleet](https://i.ytimg.com/vi/Z4DoEXhrPC8/hqdefault.jpg)](https://www.youtube.com/watch?v=Z4DoEXhrPC8)

[Watch on YouTube](https://www.youtube.com/watch?v=Z4DoEXhrPC8) · **LangChain** · 2026-07-15

## TL;DR
Jason Patel, CTO at 11X, shares how his company built a Slack-native bug triage agent using LangSmith Fleet. What started as an effort to automate bug investigation and triage evolved into a general-purpose organizational agent, and the next goal is to empower the entire company to build their own agents without writing code or deploying infrastructure.

## Key Takeaways
- 11X builds AI software for go-to-market teams and wanted AI to automate bug filing and triaging.
- The original triage process was run by a PM off his own machine, which wasn't scalable.
- Jason wanted a no-code solution that included Slack integration without having to build a custom Slack app.
- LangSmith Fleet provided the capabilities he was looking for, initially seeming "too good to be true."
- Employees interact with the agent simply by tagging it in Slack channels where it's already present.
- After the bug triage agent proved successful, Jason folded in additional use cases: Datadog alert triage and general Q&A.
- The agent evolved into a single general-purpose agent powering multiple workflows across the organization.
- Sales reps even use the agent live on calls to answer product questions.
- Fleet's ease of use and power means the next phase is enabling non-engineers across the company to build their own agents.
- Jason's advice: enabling just one use case reveals Fleet's power and motivates building many more.

## Detailed Breakdown

**[00:00] — Introduction and the Bug Triage Problem**
Jason Patel introduces himself as CTO of 11X, a company that builds AI software for go-to-market teams. The initial problem was bringing AI into the bug filing and triaging process. Customer Success Managers (CSMs) file bugs, and the goal was to have AI automatically investigate and triage those issues. A PM had already created a process for this, but it was running off his personal machine, making it unsustainable. Jason wanted a solution where he could build agents without writing code or deploying infrastructure, and Slack integration was a critical requirement—he also didn't want to build his own Slack app.

**[00:31] — Discovering Fleet and Slack-Native Design**
Jason discovered LangSmith Fleet and was initially skeptical that its capabilities could be real. The agent's user experience is designed around Slack: employees simply talk to it by tagging it in channels. Everyone in the company knows the agent's identity, and it lives in all the main channels, making access frictionless.

**[01:02] — Expanding from Bug Triage to a General-Purpose Agent**
After building the bug triage agent, Jason identified two more use cases: triaging Datadog alerts that arrive in Slack, and a general Q&A agent. He realized the tools he had already built for bug triage were sufficient for these additional use cases, so he integrated them into the same agent. This revealed a broader pattern: he could keep folding new use cases into a single agent, increasing its capabilities until it became a general-purpose agent powering the entire organization. People now ask it a wide variety of questions, and salespeople even use it live on calls to answer product questions.

**[01:33] — Next Steps: Democratizing Agent Building Across the Company**
The bots and agents built so far were created by a small handful of people. Jason's next step is to enable the rest of the organization to build their own agents using Fleet, because it is both easy to use and powerful. He wants individuals and teams to automate their own workflows. He closes with a strong endorsement: if you can enable just one use case, you'll understand Fleet's power and immediately want to build ten more.

## Notable Quotes
- "I was looking for a solution where I can build agents where I didn't actually have to write code and deploy my own infrastructure and a Slack integration was a key component."
- "When I heard about its capabilities, I thought it was too good to be true."
- "I could just keep folding in more use cases into this single agent and I could increase its capabilities and it could be this general purpose agent that could just power the entire organization."
- "If you can enable one use case, you'll understand its power and you'll want to build 10 more."

## People, Tools & References Mentioned
- **Jason Patel** — CTO at 11X
- **11X** — Company building AI software for go-to-market teams
- **LangSmith Fleet** — Platform used to build and deploy Slack-native agents without custom infrastructure
- **Slack** — Primary interface where employees interact with the agent
- **Datadog** — Monitoring/alerting tool whose Slack alerts are triaged by the agent
- **CSMs (Customer Success Managers)** — Team members who file bugs that the agent triages

## Who Should Watch
This video is ideal for engineering leaders, CTOs, and operations teams who want to deploy AI agents inside Slack without building custom infrastructure or Slack apps. It's also valuable for anyone exploring how a single agent can scale from one use case into an organization-wide automation platform.


<details class="transcript">
<summary>Full transcript</summary>

<p>Hi, I&#x27;m Jason Patel. I&#x27;m CTO at 11X and we build AI software for go to market teams. We were trying to bring AI to our uh bug filing and triaging process. As our CSMs would actually file bugs, we wanted AI to actually investigate the issue and triage them. And so we had a PM that actually put together a process to do this, but he was running it off his own machine. I was looking for a solution where I can build agents where I didn&#x27;t actually have to write code and deploy my own infrastructure and a Slack integration was a key component. I also</p>
<p>integration was a key component. I also didn&#x27;t want to have to build my own Slack app. I was looking for a solution that did all of this. And then I happened to come across Fleet and when I heard about its capabilities, I was I I thought it was too good to be true. The way people find it is is real simple. They just talk to it in Slack. Everyone at the company knows the identity of the agent and it&#x27;s in all of the main channels. So they just tag it. After I built this uh the bug triaging agent, there were couple of other use cases I wanted to take on. I wanted to triage data dog alerts that were coming into</p>
<p>data dog alerts that were coming into Slack. And then I also want to build a general Q&amp;A agent. And what I realized from what I built with the about triage agent, I had all the right tools there. So I just integrated all these use cases into the same agent. And so I realized that I could just keep folding in more use cases into this single agent and I could increase its capabilities and it could be this general purpose agent that could just power the entire organization. People are asking it tons of different types of questions. We even have sales people that like pull it up on sales calls when they you know they had a they have a</p>
<p>they you know they had a they have a question about the product and they they just ask it. I think the next step is to enable the rest of the organization to build agents. with the bots and agents we&#x27;ve built so far, they were built by a handful of people on the team. Um, but Fleet is easy to use and it&#x27;s very powerful. So, I want to give that to every individual on the team and let them automate their workflows, the workflows for themselves and for their teams. If you can enable one use case, you&#x27;ll understand its power and you&#x27;ll want to build 10 more.</p>

</details>
