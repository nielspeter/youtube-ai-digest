---
title: "The Hallway Track: What Even Is Harness Engineering"
channel: "AI Native Dev"
video_id: DLjarZe0Xqc
url: https://www.youtube.com/watch?v=DLjarZe0Xqc
published: 2026-07-30T16:00:19+00:00
generated: 2026-07-30T19:47:59+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/DLjarZe0Xqc/hqdefault.jpg
---
# The Hallway Track: What Even Is Harness Engineering

[![The Hallway Track: What Even Is Harness Engineering](https://i.ytimg.com/vi/DLjarZe0Xqc/hqdefault.jpg)](https://www.youtube.com/watch?v=DLjarZe0Xqc)

[Watch on YouTube](https://www.youtube.com/watch?v=DLjarZe0Xqc) · **AI Native Dev** · 2026-07-30

## TL;DR
Simon Maple roams the AI Engineer conference in San Francisco conducting a "hallway track" interview about the latest trends in AI engineering. The conversation centers on the shift toward "loop engineering" over "harness engineering," the just-released Sonnet 5 model, and how agents are evolving to handle long-running operations with proper self-healing feedback loops.

## Key Takeaways
- "Loop engineering" has emerged as the dominant paradigm, supplanting "harness engineering" as the trending term in the AI engineering community.
- Anthropic's Sonnet 5 model dropped during the conference, underscoring the rapid pace of model releases.
- The major advantage of loop-based agent design is that agents no longer interrupt users every 5–10 operations to ask for input or present multiple-choice decisions.
- Until recently, even with emerging features like channels for pushing notifications directly into agent sessions, models would circle back and request human input rather than working autonomously.
- Proper feedback loops require agents to understand what's being done and to update their memory over time.
- Memory management is critical: what an agent learns today may be valuable in the moment but irrelevant or unhelpful two days later.
- The interviewee built a self-healing Pokémon agent that trains code while playing Pokémon, initially demoed in London.
- This project has advanced to fine-tuning an open-weight model using a custom Pokémon harness.
- Fine-tuning models for this kind of work is described as "very expensive" — a cautionary note to those considering similar experiments.

## Detailed Breakdown

### Introduction and the Hallway Track Concept [00:00](https://www.youtube.com/watch?v=DLjarZe0Xqc&t=0s)
Simon Maple introduces himself from AI Native Dev, reporting from the AI Engineer conference in San Francisco. He introduces a small robotic puppy named Sunny AI and explains the plan to do a "hallway track" segment — moving through the conference venue to talk with attendees about what people are discussing, learning, and taking away from the event. Sunny has to stay behind, so Simon sets off on his own.

### Loop Engineering vs. Harness Engineering [00:31](https://www.youtube.com/watch?v=DLjarZe0Xqc&t=31s)
Simon encounters an attendee and asks whether "loop engineering" has replaced "harness engineering" as the trending term, noting he's been out of touch for the last 24 hours. The attendee confirms that loop engineering is indeed the current focus. The conversation immediately turns to breaking news: Sonnet 5 has just dropped in the last 30 minutes, highlighting the breakneck speed of model releases in the AI engineering space.

### The Advantage of Loops and Agent Autonomy [00:31](https://www.youtube.com/watch?v=DLjarZe0Xqc&t=31s)
The attendee explains that the primary advantage of a loop-based approach is that the agent doesn't return to the user asking for input every 5–10 operations. This represents a fundamental shift in how models think about long-running operations. Previously, no matter how much you encouraged an agent to continue working — even using emerging features like channels to push notifications directly into agent sessions — the agent would still circle back, saying it didn't know what was wanted or presenting multiple choices and asking the user to decide. The new loop paradigm addresses this by enabling proper feedback loops where agents truly understand the task at hand.

### Memory and Feedback Loop Management [01:03](https://www.youtube.com/watch?v=DLjarZe0Xqc&t=63s)
The discussion moves to how agents manage memory and context over time. The attendee emphasizes that a proper feedback loop must include the ability to update memory. What an agent does or learns today might be valuable in the moment but could become irrelevant or even counterproductive within a couple of days. Simon probes how the weighting and biasing of this memory works, prompting the attendee to share a concrete example.

### Self-Healing Pokémon Agent and Fine-Tuning [01:33](https://www.youtube.com/watch?v=DLjarZe0Xqc&t=93s)
The attendee describes a project they first previewed in London: a self-healing Pokémon agent that demonstrates how to train code while playing Pokémon. The project has since advanced significantly — they've built a Pokémon harness that fine-tunes an open-weight model to play the game. They caution that this kind of fine-tuning is "very expensive" and advise against trying it at home. The full details will be presented in an hour-long talk upstairs at the conference.

## Notable Quotes
- "Loop engineering is the, you know, the dream words. Is that still the case?" — Simon Maple
- "The major advantage of a loop is that the agent doesn't come back to you and ask for your input every five to ten operations." — Attendee
- "No matter how much you encourage the agent to continue working... it would still circle back and say, I don't know what you want from me, I need your input." — Attendee
- "What you're doing today might be really valuable, but in two days that might be something that's not valuable." — Attendee
- "Don't try this at home. Very expensive, people." — Attendee, on fine-tuning a model to play Pokémon

## People, Tools & References Mentioned
- **Simon Maple** — Host from AI Native Dev conducting the hallway track interviews
- **Sunny AI** — A small robotic puppy present at the start of the segment
- **Sonnet 5** — Anthropic model that dropped during the conference (referred to as "Sonnet 5" in the transcript)
- **Channels** — An emerging feature for pushing notifications directly into agent sessions
- **AI Engineer conference** — The event in San Francisco where the interviews took place
- **Self-healing Pokémon agent** — A demo project involving training code while playing Pokémon, fine-tuned on an open-weight model
- **Open-weight model** — The type of model used in the Pokémon fine-tuning experiment
- **London** — Where an earlier version of the Pokémon agent talk was first presented

## Who Should Watch
AI engineers and developers working with autonomous agents who want to understand the latest thinking on loop-based agent design, memory management, and the shift from harness engineering to loop engineering. The segment also offers a glimpse into cutting-edge experimentation with self-healing agents and fine-tuning open-weight models for complex, long-running tasks.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=DLjarZe0Xqc&amp;t=0s">00:00</a></span> Oh, boy. Hey, Simon Maple here from AI Native Dev. And I&#x27;m here at AI Engineer in San Francisco. And joining me today is a little puppy, little Sunny AI. We can actually run around and do the hallway track. Unfortunately without Sunny, because Sunny has to stay here. But we&#x27;re going to talk to people, understand what people are talking about at the hallway track, what people are trying to learn at AI Engineer and some of their takeaways. Unfortunately, this is where we have to part ways. But let&#x27;s move on and see who we can chat with.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=DLjarZe0Xqc&amp;t=31s">00:31</a></span> So it started this week. Harness engineering. And now loop engineering is the, you know, the dream words. Is that still the case? I&#x27;ve been out of touch for the last 24 hours. No, it&#x27;s definitely the case. And actually, if you didn&#x27;t see, in the last 30 minutes, Sonnet 5 dropped. Okay. What is the major advantage of a loop? The major advantage of a loop is that the agent doesn&#x27;t come back to you and ask for your input every five to tens of operations. So I think what we&#x27;ve seen is we&#x27;ve seen the models actually fundamentally change the way they think about long-running operations. Until very recently,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=DLjarZe0Xqc&amp;t=63s">01:03</a></span> no matter how much you encourage the agent to continue working, even if you use, like, emerging features like channels to push notifications directly into the agent sessions, it would still circle back and say, I don&#x27;t know what you want from me, I need your input. Or here&#x27;s three choices. I need you to help me make one of these choices. Having a proper feedback loop and making sure your agents really understand what&#x27;s being done, and also being able to update the memory. What you&#x27;re doing today might be really valuable, but in two days that might be something that&#x27;s not valuable.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=DLjarZe0Xqc&amp;t=93s">01:33</a></span> So how is it going to, you know, do the weights and the bias of it? I gave an early snippet of what I did this in London, but I built a self-healing Pokémon agent, and I showed how you can essentially train your code to while playing Pokémon. I&#x27;ve actually advanced that talk to basically training a model. Okay, so I&#x27;ve essentially built a Pokémon harness to play Pokémon that&#x27;s fine-tuned on an open-weight model. Don&#x27;t try this at home. Very expensive, people. But that&#x27;s my talk. I&#x27;ll have an hour upstairs. Amazing.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=DLjarZe0Xqc&amp;t=123s">02:03</a></span> Let&#x27;s see if we can crack it.</p>

</details>
