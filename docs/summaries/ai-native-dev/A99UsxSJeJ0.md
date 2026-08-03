---
title: "The Hallway Track: Would You Trust an Agent to Send Your Email?"
channel: "AI Native Dev"
video_id: A99UsxSJeJ0
url: https://www.youtube.com/watch?v=A99UsxSJeJ0
published: 2026-08-03T15:00:38+00:00
generated: 2026-08-03T15:12:17+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/A99UsxSJeJ0/hqdefault.jpg
---
# The Hallway Track: Would You Trust an Agent to Send Your Email?

[![The Hallway Track: Would You Trust an Agent to Send Your Email?](https://i.ytimg.com/vi/A99UsxSJeJ0/hqdefault.jpg)](https://www.youtube.com/watch?v=A99UsxSJeJ0)

[Watch on YouTube](https://www.youtube.com/watch?v=A99UsxSJeJ0) · **AI Native Dev** · 2026-08-03

## TL;DR
A conference attendee discusses the critical need for observability, deterministic models, and human-in-the-loop controls as AI adoption scales. The conversation centers on a practical example: whether you'd trust an AI agent to send emails autonomously, with one participant sharing his approach of restricting agents to draft-only mode to maintain oversight before any irreversible communication goes out.

## Key Takeaways
- Observability and deterministic models are essential for building trust in AI outputs at enterprise scale
- As AI adoption grows, controlling autonomous agent loops becomes the next major challenge
- Human-in-the-loop safeguards are critical before AI agents take actions that have external, real-world consequences
- Sending emails is a non-reversible action with reputational stakes, making it a key boundary for agent autonomy
- One practical approach is to let agents draft emails but require human review before sending
- The distinction between internal tooling and outward-facing actions represents an important trust threshold
- Context matters: an agent that has read sensitive personal information raises the stakes of what it communicates on your behalf

## Detailed Breakdown

### Learning Goals: Observability and Trust [00:00](https://www.youtube.com/watch?v=A99UsxSJeJ0&t=0s)
The interviewee explains they are attending to learn about observability and deterministic models, specifically to understand how to make AI results more trustworthy. They highlight the challenge of ensuring models aren't hallucinating even in proper enterprise-scale AI adoption, and stress the importance of eval metrics that can catch problems and reveal what's happening under the hood.

### The Control Challenge [00:30](https://www.youtube.com/watch?v=A99UsxSJeJ0&t=30s)
The conversation shifts to the broader landscape: there is now enormous value and data flowing through AI harnesses, and the pressing question is how to control these systems. The interviewer notes that with many autonomous loops running, figuring out "what next" in terms of control and oversight is becoming critical.

### The Email Trust Question [00:40](https://www.youtube.com/watch?v=A99UsxSJeJ0&t=40s)
The interviewer poses a direct question: would you trust an agent to send an email on your behalf right now, sight unseen? The interviewee reveals they have actually built an app called Simon EA that can read all their emails, but they deliberately restrict it to only writing drafts. Every email is validated by a human before leaving the outbox, making it a powerful tool with a built-in safety mechanism.

### The Irreversibility of External Actions [01:01](https://www.youtube.com/watch?v=A99UsxSJeJ0&t=61s)
The interviewer underscores why this safeguard matters: the moment an AI action shifts to impacting someone's opinion of you outside your organization, it crosses an important line. The interviewee adds that sending an email is non-reversible—it's not a retaining door. This irreversibility is what makes autonomous email-sending a risky proposition.

### Context and Consent [01:20](https://www.youtube.com/watch?v=A99UsxSJeJ0&t=80s)
The interviewer offers a vivid hypothetical: if an agent had spent the day reading your diary and then wanted to send a message to your mother-in-law, you'd want to be in the loop before that happened. This illustrates how the sensitivity of context an agent has access to should raise the threshold for human oversight before it acts on your behalf.

## Notable Quotes
- "I want to be in the loop before you email my mother in law."
- "It doesn't have the send ability, so I validate every single thing that goes out my outbox."
- "That moment where it shifts to impacting somebody's opinion of you outside of your own organization—like that's an important line that it's going to cross."
- "It's non-reversible. It's not a retaining door."
- "We're now in a place where there's so much value, so much data going through our AI, our harnesses that we're going to need to figure out how do we control these things."

## People, Tools & References Mentioned
- **Simon EA** — A personal app built by the interviewee that reads emails and drafts responses, but deliberately lacks send capability to enforce human review

## Who Should Watch
AI engineers, platform builders, and anyone exploring autonomous agent workflows who needs to think carefully about where to draw the line between agent autonomy and human oversight—especially for actions that are irreversible or externally visible.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=A99UsxSJeJ0&amp;t=0s">00:00</a></span> I want to be in the loop before you email my mother in law. And what are you here to learn at AI? I&#x27;m here to learn about observability and deterministic models, just to see how to make the results of AI more trusting. And even with a proper enterprise scale adoption of AI, how do you make sure that the models are not like still hallucinating? Or if they are like the eval metrics are catching that and we&#x27;re able to determine what&#x27;s actually going on under the hood. Yeah.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=A99UsxSJeJ0&amp;t=30s">00:30</a></span> So we&#x27;re now in a place where there&#x27;s so much value, so much data going through our AI, our harnesses that we&#x27;re going to need to figure out how do we control these things? Yeah, I think that&#x27;s probably next is yes, I&#x27;ve got 20 loops going but okay, what next? I always ask this question would you trust an agent to send an email on your behalf right now, sight unseen? What I do, actually, this is a very valid question because I&#x27;ve just literally just built a nice little app called Simon EA and it can read all my emails and things like that. But what I get it to do is I get it to only write emails and leave them in draft.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=A99UsxSJeJ0&amp;t=61s">01:01</a></span> It doesn&#x27;t have the send ability, so I validate every single thing that goes out my outbox. So this like incredibly powerful tool and you have to review every email before it gets sent because that moment where it shifts to impacting, you know, somebody’s opinion of you outside of your own organization, like that&#x27;s an important line that it&#x27;s going to cross. A non reversible as well. It&#x27;s non-reversible. It&#x27;s not a retaining door. Yeah. If the agent had spent the day reading your diary, if the person it was going to send a message to was like your mother in law. Yeah. All right. You want to be able to express those circumstances. If you spent the day reading my diary, then I want to be in the loop before</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=A99UsxSJeJ0&amp;t=93s">01:33</a></span> you email my mother in law.</p>

</details>
