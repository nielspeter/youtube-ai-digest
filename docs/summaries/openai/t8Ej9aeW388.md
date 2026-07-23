---
title: "How IT Admins can manage ChatGPT Work at scale | OpenAI"
channel: "OpenAI"
video_id: t8Ej9aeW388
url: https://www.youtube.com/watch?v=t8Ej9aeW388
published: 2026-07-23T20:50:48+00:00
generated: 2026-07-23T21:19:50+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/t8Ej9aeW388/hqdefault.jpg
---
# How IT Admins can manage ChatGPT Work at scale | OpenAI

[![How IT Admins can manage ChatGPT Work at scale | OpenAI](https://i.ytimg.com/vi/t8Ej9aeW388/hqdefault.jpg)](https://www.youtube.com/watch?v=t8Ej9aeW388)

[Watch on YouTube](https://www.youtube.com/watch?v=t8Ej9aeW388) · **OpenAI** · 2026-07-23

## TL;DR
OpenAI demonstrates how IT administrators can use ChatGPT Work alongside new admin APIs to manage ChatGPT deployments at scale. Through a conversational interface, admins can monitor adoption, track spending, and take corrective actions like setting per-user spend caps—all while maintaining control through scoped API keys and confirmation steps.

## Key Takeaways
- IT admins play an increasingly strategic role in managing AI access, spend, and value measurement across organizations.
- OpenAI's new admin APIs enable scalable workspace management through programmatic access.
- Admins can create scoped admin keys stored securely (e.g., in Keychain) to allow agents to interact with the API safely.
- ChatGPT Work surfaces adoption data, showing which groups and users are most active each day.
- Spend analysis is available per user and per group, with automatic highlighting of outliers above the workspace average.
- Admins can request spend-management recommendations, such as monthly per-user caps for high-spending groups.
- Work provides projected impact context before any change is applied, ensuring informed decision-making.
- All changes require explicit admin confirmation, keeping the human in control.
- Applied changes can be verified in the standard admin UI, bridging the agent experience with traditional controls.
- The admin APIs power the data and controls behind each workflow demonstrated in ChatGPT Work.

## Detailed Breakdown

### The Evolving Role of IT Admins [00:02](https://www.youtube.com/watch?v=t8Ej9aeW388&t=2s)
The video opens by framing the broader context: as AI tools like ChatGPT become embedded in everyday work, IT administrators are shifting into a more strategic and consequential position. Their responsibilities now extend beyond traditional IT management to include managing access, monitoring spend, and measuring the value that AI delivers to the organization. OpenAI states they are building tools specifically for admins to ease this burden, and their new admin APIs are designed to make operating at scale possible.

### Setting Up a Scoped Admin Key [00:14](https://www.youtube.com/watch?v=t8Ej9aeW388&t=14s)
The presenter begins a live demonstration using ChatGPT Work. The first step is creating a scoped admin key, which is then saved in Keychain. This setup allows a "work agent" to use the API securely, establishing the foundation for the agent to query and act on workspace data without compromising security. The scoping of the key implies least-privilege access, though the video does not elaborate on specific permission levels.

### Monitoring Adoption and Activity [00:32](https://www.youtube.com/watch?v=t8Ej9aeW388&t=32s)
With the agent connected, the presenter asks in natural language, "Which groups and users are most active each day?" ChatGPT Work summarizes adoption patterns and shows where usage is concentrated across the workspace. This gives the admin visibility into which teams are actively engaged with the tool and where additional support or enablement might be needed.

### Analyzing Spend and Identifying Outliers [00:40](https://www.youtube.com/watch?v=t8Ej9aeW388&t=40s)
The presenter then asks whether they can see average spend per user and per group, and specifically which groups are above the workspace average. Work responds by surfacing the spend data and highlighting outlier groups whose spending exceeds the norm. This visual emphasis on outliers makes it straightforward for the admin to investigate potential cost issues before they escalate.

### Recommending and Applying a Per-User Spend Cap [01:03](https://www.youtube.com/watch?v=t8Ej9aeW388&t=63s)
For the highest-spending group identified, the presenter asks Work to recommend a monthly per-user spend cap. Work responds with a clear recommendation and shows the projected impact of implementing the cap, giving the admin the context needed to evaluate the decision. After reviewing the recommendation, the admin confirms the change. Work applies the cap, and the presenter verifies the result in the admin UI—reinforcing that the admin remains in control of all modifications.

### Closing Summary [01:34](https://www.youtube.com/watch?v=t8Ej9aeW388&t=94s)
The video concludes by reiterating that ChatGPT Work offers an easier way to observe workspace activity and take action. The presenter notes that the demonstrations shown are just a few examples of everyday workspace management tasks. Behind each workflow, the admin APIs provide the underlying data and controls that make these interactions possible, positioning the APIs as the scalable backbone for enterprise AI administration.

## Notable Quotes
- "As AI becomes part of everyday work, IT admins are taking on a more strategic and consequential role, managing access, spend, and measuring value."
- "Which groups and users are most active each day?"
- "Look how it highlights the outlier, making it easy to investigate before costs become a problem."
- "I get a clear recommendation and the context to review it before anything changes."
- "Work makes everyday workspace management easier, while the admin APIs provide the data and controls behind each workflow."

## People, Tools & References Mentioned
- **ChatGPT Work** — OpenAI's workspace management interface for administering ChatGPT at an organizational level
- **Admin APIs** — OpenAI's new APIs enabling programmatic, at-scale workspace administration
- **Keychain** — Used to securely store the scoped admin key
- **Work Agent** — The AI agent within ChatGPT Work that interacts with the admin APIs on the admin's behalf
- **Admin UI** — The traditional administrative interface where applied changes can be verified

## Who Should Watch
IT administrators, workspace managers, and anyone responsible for overseeing ChatGPT deployments in an enterprise environment will find this video valuable. It provides a concise, practical look at how OpenAI's admin tools and APIs can streamline adoption monitoring, spend management, and policy enforcement at scale.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=t8Ej9aeW388&amp;t=2s">00:02</a></span> As AI becomes part of everyday work, IT admins are taking on a more strategic and consequential role, managing access, spend, and measuring value. We&#x27;re building tools specifically for admins to make that work easier. And now, our new admin APIs make it possible to operate at scale. Today, I&#x27;ll show you what that looks like using ChatGPT Work. First, I create a scoped admin key and save it in Keychain. This allows our work agent to use the API securely. Now, I can just ask, &quot;Which groups and users</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=t8Ej9aeW388&amp;t=32s">00:32</a></span> can just ask, &quot;Which groups and users are most active each day?&quot; Work summarizes adoption and shows where usage is concentrated. That helps me see which teams are engaged and where more support may be needed. Can we also see average spend per user and group? And maybe also which groups are above the workspace average? Look how it highlights the outlier, making it easy to investigate before costs become a problem.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=t8Ej9aeW388&amp;t=63s">01:03</a></span> costs become a problem. For the highest spending group, I asked Work to recommend a monthly per-user cap. It showed the projected impact. I get a clear recommendation and the context to review it before anything changes. Once I&#x27;ve reviewed it, I confirm the change, Work applies the cap, and I verify it in the admin UI so I stay in control of what changes. And that&#x27;s it. ChatGPT Work gives you an easier way to see what&#x27;s happening across your workspace and take action. And these are just a few examples. Work makes everyday workspace management</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=t8Ej9aeW388&amp;t=94s">01:34</a></span> Work makes everyday workspace management easier, while the admin APIs provide the data and controls behind each workflow.</p>

</details>
