---
title: "Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft"
channel: "AI Engineer"
video_id: fnLBmfsI_Fg
url: https://www.youtube.com/watch?v=fnLBmfsI_Fg
published: 2026-07-20T06:25:15+00:00
generated: 2026-07-20T07:25:06+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/fnLBmfsI_Fg/hqdefault.jpg
---
# Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft

[![Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](https://i.ytimg.com/vi/fnLBmfsI_Fg/hqdefault.jpg)](https://www.youtube.com/watch?v=fnLBmfsI_Fg)

[Watch on YouTube](https://www.youtube.com/watch?v=fnLBmfsI_Fg) · **AI Engineer** · 2026-07-20

## TL;DR
Ornella and Joel, builders of Ace—a live AI voice tutor—argue that voice agents should run on small, fast models rather than frontier reasoning models. By extracting all logic, state management, and reasoning into a state machine built in code, the model is left to do only what it does best: speak. The result is sub-second response times (~900ms) that feel natural in conversation, achieved with a cost-effective small model like Haiku 4.5 instead of a slower frontier model.

## Key Takeaways
- **Latency is the real budget for voice agents, not IQ.** A frontier model that reasons for a full second has already lost the user's attention, no matter how good the answer is.
- **The target response time is roughly 950 milliseconds.** Beyond that, silence makes the brain perceive the agent as broken.
- **Small models can outperform frontier models in voice** when paired with proper scaffolding—state machines, reasoning logic, and scenario handling built in code.
- **Ace's architecture offloads all "thinking" from the model.** The model doesn't decide lesson flow, track student mastery, or determine what happens next; external systems handle that and hand the model a summary each turn.
- **The model's only job is speaking.** Everything else—logic, reasoning, state transitions—is handled outside the model.
- **Scaffolding has a cost, but you pay it once in code**, not on every conversational turn like you would with per-call reasoning from a frontier model.
- **Small models without scaffolding tend to drift** on long structured interactions, so strict rules and external logic are essential.
- **The guiding rule: pick the fastest model your latency budget allows**, then invest the rest of your time building the scaffolding around it.
- **This approach generalizes beyond voice** to any real-time, high-volume application where latency is a priority.
- **The model is the smallest part of the system** in these architectures—the surrounding code and logic are where the real engineering happens.

## Detailed Breakdown

### Introduction and the Latency Problem [00:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s)
Ornella introduces herself and Joel as the builders of Ace, a live AI voice tutor that deliberately runs on a small model. She frames the core problem with a relatable example: the silence on a voice call that makes a listener's brain decide the agent is "dead." Even a one-second pause breaks the illusion of a live tutor. The budget for voice agents isn't intelligence—it's milliseconds, with a target of about 950ms for the model to start talking.

### Extracting Thinking from the Model [01:04](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=64s)
Ornella explains the core design philosophy: they made the model small and removed the hardest parts of the job from it. The model doesn't decide what happens in the lesson, track what the student knows, or explain what comes next. A system handles all of that and feeds the model a summary each turn. What remains for the model is the one thing it's genuinely good at: talking.

### The Frontier Model Problem [01:35](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=95s)
Joel adds context, using Anthropic's Claude (referred to as "Claude 4.7" in the transcript, likely meaning a current frontier model) as an example. Frontier models excel at reasoning—they can work through a lesson problem and a student's question to produce a strong answer. But that reasoning takes several seconds, which is precisely the problem for voice. Those seconds are too valuable to spend on thinking when the user is waiting for a spoken response.

### The State Machine Architecture [02:05](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=125s)
Joel describes the solution: extract all thinking into a state machine. For Ace, they mapped out every scenario needed for a lesson and built a state machine that coordinates each step to the next. An intelligent layer on top derives student mastery levels needed for lesson completion. Everything—what happens next, what to display, how to answer a question—is computed outside the model. The model simply receives that output and speaks it.

### Live Demonstration and Comparison [03:08](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=188s)
Joel walks through two video examples. The first shows a frontier model (Opus, referred to as "4.7") handling a simple question—visible reasoning takes a couple of seconds before the answer returns. The second shows the same question handled by Haiku 4.5 (a much smaller model) with Ace's full implementation. The answer comes back in about 900 milliseconds, feeling nearly instant. Joel attributes this speed to removing all thinking, logic, and reasoning from the model and placing it in code.

### The Cost of Scaffolding and the Guiding Rule [04:09](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=249s)
Joel is candid about the trade-off: this approach isn't free. A small model like Haiku 4.5, without scaffolding, tends to drift on long structured interactions and needs strict rules to stay organized. The scaffolding is the price you pay—but crucially, you pay it once, in code, rather than on every turn. Joel states the guiding rule: pick the fastest model your latency budget allows, then spend the rest of your time building the scaffolding. This means building state machines, reasoning processes, scenario planning, and logic outside the model so it can focus solely on speaking.

### Broader Applicability and Closing [05:12](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=312s)
Joel extends the principle beyond voice: it applies to any real-time application where latency is a priority and to any high-volume use case. In these systems, the model is the smallest part—the surrounding architecture is what matters. They close by reintroducing themselves as the builders of Ace and inviting questions.

## Notable Quotes
- "In voice, that instant is actually a backward. Because our budget was never IQ, it's milliseconds."
- "A frontier model that thinks for a full second has already lost the room, no matter how good the answer is."
- "We made the model small and took the hardest part jobs away from it… What's left for the model is one thing it's really good at: talking."
- "The reasoning can take a couple of seconds and those seconds are really valuable when you are building voice applications."
- "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
- "The scaffolding piece is the price. But the good thing is you pay it once and in code, not on every single turn."
- "In those cases, the model is the smallest part of the system."

## People, Tools & References Mentioned
- **Ace** — the live AI voice tutor built by Ornella and Joel
- **Anthropic Claude (referred to as "Claude 4.7" / "Opus 4.7")** — example of a frontier reasoning model that is too slow for real-time voice
- **Anthropic Haiku 4.5** — the small, fast model used by Ace for spoken output
- **State machine** — the architectural pattern used to manage lesson flow, scenarios, and logic outside the model

## Who Should Watch
Engineers and product builders working on real-time voice agents, conversational AI, or any latency-sensitive, high-volume application who want to understand why smaller models paired with robust external logic can outperform frontier models—and how to architect that scaffolding effectively.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=0s">00:00</a></span> Hi, I&#x27;m Ornella, and that&#x27;s Joel, and we built Ace, a live AI voice tutor. It run on a small model on purpose, and I want to tell you more why that&#x27;s not a compromise. Quick gut check. That silence on a voice call, that the difference between a tutor and a broken up. When a voice agent pause for even a second, your brain says it&#x27;s dead.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=31s">00:31</a></span> second, your brain says it&#x27;s dead. So, when the answer fit a leader of every instant stay, which for the smallest, biggest model. In voice, that instant is actually a backward. Because our budget was never IQ, it&#x27;s millisecond. The AI model need to start talking in about 950 milliseconds. A frontier model that think for a full second has already lost the room, no matter how good the answer is.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=64s">01:04</a></span> So, we made the model small and took the hardest part jobs away from it. It doesn&#x27;t decide when happen what&#x27;s happen in the lesson. It had It doesn&#x27;t track what the student knows. It doesn&#x27;t explain what&#x27;s next. We have a system in place to do that, and they hand the model a summary every turn. What&#x27;s left for the model is one thing it&#x27;s really good at, talking. And that&#x27;s the theory. Joel, go on and show them what it actually feel like.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=95s">01:35</a></span> show them what it actually feel like. Yeah, if maybe I can add some color to what Ornella was mentioning. So, if you think about the models of today, especially the frontier model, let&#x27;s take Claude 4.7, which is uh from Anthropic. The model is really good at reasoning. You can give it a problem, in this case a lesson, and it can reason through it, it can reason through what the student asking and it can come up with the answer. But that is actually precisely the problem. Because the reasoning can take couple of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=125s">02:05</a></span> Because the reasoning can take couple of seconds and those seconds are really valuable when you are building voice applications. So what we are doing is saying, &quot;Hey, let&#x27;s extract all of the thinking away from the model so that the model focuses on only what matters, which is speaking in our case.&quot; So all of the thinking is extracted into a state machine. So for Ace, we have thought about all the scenarios that are needed for a lesson. We have built a state machine that is able to coordinate</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=157s">02:37</a></span> state machine that is able to coordinate each step to the next and we also added intelligent layer on top to derive some of the mastery that a student might need for the lesson to be complete. So everything when it comes to what happens next, when it comes to what needs to be displayed, when it comes to how to actually answer a question, it&#x27;s all done outside of the model. And we simply feed that output to the model to speak out. And so let&#x27;s go ahead and look at an</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=188s">03:08</a></span> And so let&#x27;s go ahead and look at an example and see how that works in real time. So the first video here is without the implementation we&#x27;ve done. So it&#x27;s a simple Opus 4.7. We ask a very simple question and as you can see the model is thinking, it&#x27;s reasoning and it takes couple of seconds to return the answer back to the user. Hey, what In this video, we&#x27;ve added all everything we just talked about on Haiku 4.5, which is a much smaller model. Same question, but now you see that the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=218s">03:38</a></span> Same question, but now you see that the answer comes in about 900 milliseconds. And so that&#x27;s the beauty of building around the model. So by removing all of the thinking, all of the logic, all of the reasoning from the model and actually putting it within the code, we actually saves a lot of time and allows us to use smaller models which are cost effective and actually better at real-time voice applications. And as you can see, this feels almost instant and again that&#x27;s because all of the smart</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=249s">04:09</a></span> again that&#x27;s because all of the smart parts have already happened prior to the model actually speaking. But I have to be honest because this isn&#x27;t necessarily free. It has a cost, right? A small model like the Haiku 4.5, if it doesn&#x27;t have any scaffolding, tend to drift on long structure and really needs strict rules in order to be able to stay organized. So the scaffolding piece is the price. But the good thing is you pay it once and in code, right?</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=281s">04:41</a></span> is you pay it once and in code, right? Not on every single turn. So here&#x27;s a rule. Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding. So [snorts] in our case, right? Maybe you build a state machine, you build a reasoning process, you think about scenarios, what happens if this happens, how should your model handle it? Everything that comes with the logic, everything that comes with the harnessing, you do that outside of the model and then allowing the model to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=fnLBmfsI_Fg&amp;t=312s">05:12</a></span> model and then allowing the model to focus on that one thing that is really good at. And so that&#x27;s true for voice applications like A is, that&#x27;s true for real-time applications where latency is of priority and that&#x27;s really true for anything that is high volume, right? In those cases, the model is the smallest part of the system. So this is Joel and Ornella and we are building A is again and if you have any questions, let us know. Thank you. Thank you.</p>

</details>
