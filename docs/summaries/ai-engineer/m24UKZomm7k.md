---
title: "Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft"
channel: "AI Engineer"
video_id: m24UKZomm7k
url: https://www.youtube.com/watch?v=m24UKZomm7k
published: 2026-07-20T06:25:18+00:00
generated: 2026-07-20T11:16:12+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/m24UKZomm7k/hqdefault.jpg
---
# Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft

[![Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft](https://i.ytimg.com/vi/m24UKZomm7k/hqdefault.jpg)](https://www.youtube.com/watch?v=m24UKZomm7k)

[Watch on YouTube](https://www.youtube.com/watch?v=m24UKZomm7k) · **AI Engineer** · 2026-07-20

## TL;DR
Ornella and Joel present Ace, a live AI voice tutor that runs full lessons reliably by keeping the LLM out of the driver's seat. The core insight is that reliability is a control-flow problem, not a prompting problem: the LLM executes narrowly scoped tasks while a deterministic harness (a state machine) governs what step the system is on, validates outputs, and decides what comes next.

## Key Takeaways
- Reliability in multi-step agents is a control problem, not a prompting problem — adding more prompt rules doesn't fix agents that skip steps or loop.
- Treat the LLM as the "talent" and the surrounding harness as the "director"; the model is great at delivering a line but terrible at tracking its own position in a multi-step flow.
- A lesson (or any multi-step workflow) should be modeled as a small state machine with discrete, well-defined steps (e.g., intro, teach, check, grade, advance, wrap).
- Each step sends the model a narrow "neural contract" — do one thing and return it — then the harness validates the output and advances state.
- The model never decides where the system is in the flow; the harness owns that decision.
- By constraining the model's responsibilities, you can use a smaller, cheaper, faster model (e.g., Haiku 4.5 instead of Opus) and still get production-quality results.
- Harness engineering saves money, reduces latency, and improves reliability simultaneously.
- The approach generalizes beyond voice tutors: coding agents, ops runbooks, onboarding flows, and any agent where reliability matters.
- A practical heuristic: if your agent's reliability feels like a coin flip, take control-flow decisions away from the model and engineer them externally.
- Let the LLM talk, but don't let it drive.

## Detailed Breakdown

### The Problem with LLM-Driven Agents [00:00](https://www.youtube.com/watch?v=m24UKZomm7k&t=0s)
Ornella opens by introducing herself and Joel and the project they built: Ace, a live AI voice tutor that runs a full lesson from start to finish reliably. She immediately names the core problem: the LLM is not in charge. She describes the familiar failure mode for anyone who has shipped a multi-step agent — it works near demo time, but real users hit cases where the agent prematurely decides it's done, skips a step, or loops. Demos never surface these issues. The first instinct — prompting harder or adding more rules — misses the point, because reliability was never a prompting problem. It's a control problem.

### Model as Talent, Harness as Director [00:30](https://www.youtube.com/watch?v=m24UKZomm7k&t=30s)
Ornella introduces the central metaphor: the model is the talent, and the harness is the director. The model excels at delivering a specific line or response but is poor at remembering its position in a sequence (e.g., "step three of six"). The solution is to stop asking the model to track state. Instead, a lesson is modeled as a small state machine with steps: intro, teach, check, grade, advance, and wrap. Each step sends the model a "neural contract" — do this one thing and return it. The harness validates the response, advances the state, and decides what's next. The model never decides where the system is.

### Harness Engineering and Model Choice [01:35](https://www.youtube.com/watch?v=m24UKZomm7k&t=95s)
Joel takes over to explain the engineering rationale. He notes that frontier models like Anthropic's Opus are often used for everything — thinking, processing, and all steps in between. While that can work, it's not always effective for a live AI tutor that needs to be reliable, cost-effective, and fast. This motivated the concept of harness engineering: rather than letting one intelligent model handle everything, they built explicit steps and provided only the input needed for each specific scenario. By constraining the model's role, they were able to use Haiku 4.5 — a much smaller model with fewer reasoning capabilities — and still achieve the expected performance level, saving money, time, and latency.

### State Machine Design and Demo Walkthrough [02:37](https://www.youtube.com/watch?v=m24UKZomm7k&t=157s)
Joel explains that they thought deeply about state machines when building Ace: what is the current step, what steps could come after, and what concrete inputs confine the model to that specific action. He then plays a recording showing logs from a live lesson. The right side of the screen displays the various harnessing activities: harnessing for a section (providing input about what to speak about and do), harnessing for drawing on the whiteboard, harnessing for clearing the queue, and steps for how to end the lesson. The goal is to incorporate every possible scenario into the state machine so the lesson remains reliable even when new situations arise. The model's only job is to receive an input, take the specified action, and return the output.

### Three Core Decisions Engineered Outside the Model [04:11](https://www.youtube.com/watch?v=m24UKZomm7k&t=251s)
Joel identifies three key questions that must not be left to the model: when is the lesson done, did the student actually learn correctly, and what comes next. All decisions and actions within these three categories are engineered outside the model. The model proposes an output, but the harness ultimately decides. Joel emphasizes this approach is broadly applicable — not just to voice models like Ace, but to coding agents, ops runbooks, and onboarding flows. The rule is the same: find a way to keep the model from thinking about control flow and instead build abstractions around it.

### When to Use This Abstraction and Closing [05:42](https://www.youtube.com/watch?v=m24UKZomm7k&t=342s)
Joel offers a practical heuristic for deciding whether to apply this abstraction: consider the reliability of your agent. If it feels like a coin flip, take control flow out of the model. Reduce the number of decisions the model makes and instead engineer those decisions externally, feeding the model simple inputs so it can easily produce outputs. He closes with the memorable line: don't let the model talk — or rather, let it talk, but don't let it drive. Ornella and Joel invite questions and wrap up.

## Notable Quotes
- "Reliability was never a prompting problem. It's a control problem."
- "The model is the talent, and the harness is the director. The model is brilliant at delivering a line, but it's really terrible at remembering if it's on step three of six."
- "The model never decide where we are. That's the design."
- "The model proposes, but ultimately it is the harness that decides."
- "If it's somewhat of a coin flip, then you want to take the control flow out of the model."
- "Let it talk, but don't let it drive."

## People, Tools & References Mentioned
- **Ornella (Onela) Bahidika** — co-presenter, co-builder of Ace at Microsoft
- **Joel Allou** — co-presenter, co-builder of Ace at Microsoft
- **Ace** — the live AI voice tutor they built
- **Anthropic Claude Opus 4.7** — referenced as an example of a large frontier model often overused for all tasks
- **Anthropic Claude Haiku 4.5** — the smaller, cheaper model they successfully used thanks to harness engineering
- **Microsoft** — the presenters' employer

## Who Should Watch
AI engineers and developers building multi-step agents or voice agents who are hitting reliability walls with prompt-driven approaches. Anyone considering whether to use a large frontier model for everything versus engineering a deterministic harness around a smaller model will find practical, actionable guidance.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=0s">00:00</a></span> Hi, I&#x27;m Onela. That&#x27;s Joel. And we built Ace, a live AI voice tutor that runs a full lesson start to finish reliably. The trick is LLM is not in charge. If you have shipped a multi-step agent, you know this moment. It&#x27;s near the demo, then a real user gets in and halfway through the agent decide it&#x27;s done. Or skip a step, or even loops. The demo never show you that.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=30s">00:30</a></span> demo never show you that. And the first fix everyone reaches for is prompt this harder, add more holes. But reliability was never a prompting problem. It&#x27;s a control problem. Think of it this way. The model is the talent, and the harness is the director. The model is brilliant at delivering a line, but it&#x27;s really terrible at remembering if it&#x27;s on step three of six. So we stop asking it to. A lesson is a small state machine with intro, teach, check, grade, advance, and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=63s">01:03</a></span> intro, teach, check, grade, advance, and wrap. Each step sends the model a neural contract. Do this one thing, return it. The harness validates what&#x27;s comes back, advance the state, and decide what&#x27;s next. The model never decide where we are. That&#x27;s the design. Joel is going to show you the harness thing. Yeah. So, when we think about the frontier models of today, let&#x27;s take for example um Opus 4.7 Cloud from Anthropic,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=95s">01:35</a></span> um Opus 4.7 Cloud from Anthropic, you see that oftentimes people leverage the model for essentially everything. For the thinking, for the processing, right? And for everything in between. While that can be good, it&#x27;s not always effective in situations like ours, where we are building a live AI tutor that is speaking back and forth with students. Right? For something like this, we had a need to actually build something that is reliable, something that is cost-effective, and something that is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=126s">02:06</a></span> cost-effective, and something that is fast. Right? So, this is where the idea of leveraging the concept of harness engineering has come in. Where instead of having a model that is really intelligent, sort of go through everything for us, we will build all of these steps that are needed and provide only the input required for the model to execute a specific scenario. So, when we were building ACE, we actually thought very deeply about state machines. Right? What is the step right now? And what is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=157s">02:37</a></span> What is the step right now? And what is the possible steps that could come after? And within each of the steps, what are concrete things that we can provide to the model so that it is confined to that specific action, it is confined to that specific step at that particular moment, and only execute what needs to be done. So, by doing this, instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn&#x27;t</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=188s">03:08</a></span> which is a much smaller model, doesn&#x27;t have as much reasoning capabilities, but because of the harnessing around it, it&#x27;s still able to perform at the level in which we expect, saving money, saving time, and saving latency. So, let&#x27;s go ahead and play this recording, which will show us logs um about a particular lesson. So, as you can see in this video, especially on the right side, we see logs on all of the different harnessing that are happening. [clears throat] Right? So, for example, we see that there&#x27;s harnessing for a section, which</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=219s">03:39</a></span> there&#x27;s harnessing for a section, which provides input to the model about exactly what to speak about, what to do. We have harnessing about drawing on the whiteboard. We have harnessing that deals with clearing the queue. We have steps to how to end the lesson and everything in between, right? So, everything that would allow us to actually build the lesson in a way that is reliable even if there&#x27;s a new scenario that comes in. We try to incorporate that in our state machine. We try to incorporate that with within</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=251s">04:11</a></span> We try to incorporate that with within the lesson, right? So, again, the model all it worries about is given an input, it knows which action to take and it provides the output of that action. Right? And so, the model never really um has to think. It proposes, but ultimately it is the harness that decides. And so, for his A specifically, there are three things that we wanted to think about. Like, when is the lesson done is one, right? Did the student actually get it right? Like, did they actually learn in the way they were supposed to? And what comes next, right?</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=281s">04:41</a></span> supposed to? And what comes next, right? And so, everything that comes within those three categories, all of the different questions, all of the different actions that the models needs to take, we have engineered that outside of the model, right? So, again, it&#x27;s an input, the model receives it and gives us an output, right? And so, this is very, very important and we have found this to be very remarkable. Right? So, again, the the this is applicable to really everything, right? It&#x27;s applicable to something like A that is a voice model. It&#x27;s applicable to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=312s">05:12</a></span> is a voice model. It&#x27;s applicable to coding agents, to Ops Run Books. Um it&#x27;s applicable to onboarding flows, right? The same rule applies, right? We want to find a way to not let the model think, but building abstractions around it. So, a good way to to remember on whether you should use this abstraction is essentially to think about the reliability of your agent, right? If it&#x27;s somewhat of a coin flip, then you want to take the control flow out of the model. You want the model to not make as</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=m24UKZomm7k&amp;t=342s">05:42</a></span> model. You want the model to not make as many decisions as it should and instead build those decisions around the model and simply feed an easy input so that the model can easily produce an output, right? So, don&#x27;t let the model talk, right? Or actually let it talk, but don&#x27;t let it drive. So, we&#x27;re Joel and Ornella. This is Ace, and if you have any questions, please let us know. Thank you. Thank you.</p>

</details>
