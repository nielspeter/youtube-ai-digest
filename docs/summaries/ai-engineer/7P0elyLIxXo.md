---
title: "What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip"
channel: "AI Engineer"
video_id: 7P0elyLIxXo
url: https://www.youtube.com/watch?v=7P0elyLIxXo
published: 2026-07-12T06:45:06+00:00
generated: 2026-07-12T21:19:21+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/7P0elyLIxXo/hqdefault.jpg
---
# What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip

[![What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip](https://i.ytimg.com/vi/7P0elyLIxXo/hqdefault.jpg)](https://www.youtube.com/watch?v=7P0elyLIxXo)

[Watch on YouTube](https://www.youtube.com/watch?v=7P0elyLIxXo) · **AI Engineer** · 2026-07-12

## TL;DR
Dotta, creator of Paperclip, argues that "done" is not a Boolean checkbox but a bundle of operational claims—artifact, evidence, rubric, ownership, and next steps—that must be explicitly modeled in agentic systems. Because agents now produce code faster than humans can verify, Paperclip's liveness model balances continuous workflow progress (liveness) with structured verification, using mechanisms like blockers, human approval gates, reviewers, and harness-agnostic watchdog agents.

## Key Takeaways
- "Done" is not a single state; it is a bundle of claims including artifact produced, evidence of completion, rubric/standard, verifier identity, authority to approve, residual risk, and next action.
- Agents can create more work than humans have time to verify, introducing a new failure mode: verification theater at high volume.
- There are different levels of "done"—producer claim, reviewer finding no obvious issues, evidence meeting a specified standard, authorized approval, and surviving real-world conditions.
- Two competing forces must be balanced: liveness (work continuing without blockers) and verification (assurance of correctness).
- All-liveness/no-verification produces AI slop; all-verification/no-liveness creates an unmanageable human review queue.
- A control plane for agentic work must maintain three invariants: productive work continues, only real blockers stop work, and infinite loops are bounded.
- Paperclip provides mechanisms including state transitions, first-class blockers, interactive human approval with audit trails, explicit reviewers/approvers, and watchdog agents.
- Watchdogs are harness-agnostic maximizer agents that enforce goal completion across any agent framework (Claude Code, Codex, etc.).
- Treat "done" as an object, not a Boolean—explicitly define artifact, scope, rubric, evidence, verifier, authority, risk, and next action.
- Separate the verifier from the author, ideally using a different model (e.g., code with Claude, verify with Codex).

## Detailed Breakdown

### The Problem with "Done" [00:00](https://www.youtube.com/watch?v=7P0elyLIxXo&t=0s)
Dotta opens with a scenario: an agent opens a PR, passes tests, updates docs, closes the issue, and declares "Looks done to me." But done enough to merge? To deploy? To announce to customers? These are fundamentally different operational claims, yet most agent systems flatten them to a single green checkmark. Dotta introduces himself as the creator of Paperclip and frames the talk around lessons learned building Paperclip's liveness model.

### A New Failure Mode [00:30](https://www.youtube.com/watch?v=7P0elyLIxXo&t=30s)
Programming is effectively solved in the sense that agents can now produce code and documentation faster than any human can verify. This creates a new failure mode: agents generating more work than humans have time to review. Simply letting an agent check a box is insufficient. Saying something is "done" is actually a bundle of claims—an artifact was produced, there is evidence the task is complete, and there is a rubric to verify against.

### Levels of Done [01:02](https://www.youtube.com/watch?v=7P0elyLIxXo&t=62s)
Dotta enumerates progressive levels of doneness: the producer claims completion; a separate reviewer finds no obvious issues; evidence is verified against a specified standard; an authorized person approves the work; someone stands behind the decision; and ideally, the outcome survives real-world conditions. Exhaustive human verification fails at high volume—if humans must sign off on every task, you get verification theater rather than real assurance.

### The Need for a Protocol and Control Plane [02:05](https://www.youtube.com/watch?v=7P0elyLIxXo&t=125s)
What is needed is a protocol for how tasks progress through a system, keeping work moving without allowing tasks to enter invalid states. A control plane must tie task execution to specific contracts and constraints, governing what the system will do and which agents receive the next task. The core tension is between keeping work moving (liveness) and keeping it verified.

### Liveness vs. Verification [02:36](https://www.youtube.com/watch?v=7P0elyLIxXo&t=156s)
Liveness means work continues with no blockers. When a human reviews a task, you get correctness assurance, but the task is dead in its tracks. Balancing these two forces is the central challenge. All liveness and no approval produces classic AI slop—high-volume, low-quality output that is worse than creating nothing. But all peer review creates an enormous review queue that humans cannot keep up with. The solution is to tease apart the bundle of claims embedded in "done."

### Why a Simple Loop Falls Apart [03:39](https://www.youtube.com/watch?v=7P0elyLIxXo&t=219s)
You might think you can just write a for loop over your task manager and let agents work, but this quickly falls apart when you introduce task dependency trees, blockers, multiple agents, idempotent checkouts, and checkout locks. The liveness-verification tension becomes quite complicated. Dotta identifies three critical invariants for a control plane: ensure productive work continues, ensure only real blockers stop work, and ensure infinite loops are bounded.

### Paperclip's Mechanisms [04:09](https://www.youtube.com/watch?v=7P0elyLIxXo&t=249s)
Paperclip addresses these challenges with several mechanisms: clear state transitions for tasks; first-class blockers enforced by the control plane; interactive human approval moments that leave audit trails; explicit reviewers and approvers on tasks; and watchdogs. Watchdogs operate in a "maximizer mode"—another agent is given a goal and enforces that all agents continue working until that goal is achieved. Crucially, watchdogs are harness-agnostic, working with any framework (Pi, OpenGL, Hermes, Claude Code, Codex) through one consistent interface.

### Treat Done as an Object, Not a Boolean [05:13](https://www.youtube.com/watch?v=7P0elyLIxXo&t=313s)
Dotta's key advice: stop treating "done" as a Boolean and treat it as an object. Humans automatically paper over the details, but agentic systems require agents to distinguish between the different claims involved: the artifact, the scope, the rubric or standard, the evidence, who verified the work, who has authority to sign off, what risk remains, and what the next action will be.

### The Checklist for 100x More Work [05:45](https://www.youtube.com/watch?v=7P0elyLIxXo&t=345s)
Dotta offers a concrete checklist: define exactly what "done" means for each task; separate the verifier from the author (ideally using a different model—code with Claude, verify with Codex); require agents to provide evidence rather than just asserting completion; give agents the tools to verify—custom browser harnesses, screenshots, button-clicking, custom agent hooks; and maintain a clear chain of custody so every agent knows who receives the work next. For serious, accountable work, define "done" in maximum detail and structure your agents so all claims of completion are actually met.

## Notable Quotes
- "Agents can actually create more work than humans have time to verify."
- "Saying that something is done is actually a bundle of claims."
- "If you have humans verifying all the tasks and they have to sign off on it, you eventually just get a form of verification theater."
- "If you have tasks that are completely alive with no approvals, then what you get is this classic AI slop... it's worse than creating nothing after a long period of time."
- "Stop treating done as a Boolean and treat it more like an object."
- "Don't just ask them to say, 'Is this done?' Give them the tools they need to verify that the work is done."

## People, Tools & References Mentioned
- **Dotta** — Creator of Paperclip, presenter
- **Paperclip** — Agentic work control plane with a liveness model
- **Watchdogs** — Paperclip's harness-agnostic maximizer agents for goal enforcement
- **Agent harnesses/frameworks mentioned:** Pi, OpenGL, Hermes, Claude Code, Codex
- **Concepts:** Liveness model, verification theater, AI slop, control plane, task dependency trees, idempotent checkouts, chain of custody

## Who Should Watch
Engineers and engineering managers building or operating multi-agent systems who need to move beyond "vibe-coded" single prompts and establish real accountability, verification, and workflow control for autonomous agent output at scale.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=0s">00:00</a></span> An agent opens a pull request. It passes the tests. It updates the documentation. It closes the issue and comments, &quot;Looks done to me.&quot; But is it actually done? Is it done enough to merge? Is it done enough to deploy? Is it done enough to announce to your customers? These are fundamentally different operational claims, and most agent systems just flatten it to a single green check mark. I&#x27;m Dota. I&#x27;m the creator of Paperclip, and I&#x27;m going to give you some hard-earned lessons that we&#x27;ve learned in creating Paperclip&#x27;s liveness model. What does done even mean? Here&#x27;s the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=30s">00:30</a></span> What does done even mean? Here&#x27;s the thing. Programming is solved, and agents can now produce more code and documentation faster than any human can ever verify. And this actually gives us a new failure mode, is that agents can actually create more work than humans have time to verify. So we need a way to verify that our agents are done more than just letting them check a checkbox. Done doesn&#x27;t mean that an agent just changed the status of a task being done. Saying that something is done is actually a bundle of claims. You&#x27;re saying that an artifact was produced, that you have evidence that the task is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=62s">01:02</a></span> that you have evidence that the task is actually complete, and you have a rubric in which you can verify against. You know exactly who the owner is for the next step, and you know exactly what the next step is. There&#x27;s different levels to how done something is. The producer might claim something is complete, but you need to have a reviewer, another party that looks at it and finds no obvious issues. You want to verify and make sure that the evidence actually meets a specified standard. You want to make sure that a person who is authorized to approve it actually approves that the work is done.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=94s">01:34</a></span> actually approves that the work is done. And you want to make sure that there&#x27;s somebody who actually stands behind the decision. And ideally, what you want is that the outcome has actually survived real-world conditions. Because exhaustive human verification fails at high volume. You might be able to verify a few tasks per day, but essentially, if you have humans verifying all the tasks and they have to sign off on it, you eventually what you just get is a form of verification theater. What you need is a protocol for</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=125s">02:05</a></span> theater. What you need is a protocol for defining how tasks actually progress through a system. You want to make sure that tasks are always kept moving, but they don&#x27;t get stuck into invalid states. You need a control plane that actually has the execution of the tasks being tied to specific contracts and constraints about what the system will do and what agents it will hand off your next task to. Because really what you&#x27;re trying to play against is this idea around keeping work moving, but also having it</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=156s">02:36</a></span> work moving, but also having it verified. When a task has been reviewed by a human, you get the assurance that it&#x27;s correct. But having a human verify it means that the task is dead in its tracks. You also want to keep liveliness. Liveliness means that the work is continuing with no blockers. And you&#x27;re always trying to keep these two things in balance. If you have tasks that are completely alive with no approvals, then what you get is this classic AI slop because you&#x27;re producing a lot of things with kind of no quality control and it&#x27;s worse than creating nothing after a long period of time. But</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=188s">03:08</a></span> nothing after a long period of time. But if you have peer review, um then you have this enormous review queue where humans can&#x27;t actually review it by hand anyway. These agents will be creating far more than you can ever actually review, and so we have to find a way to tease apart the bundle of claims that are involved in saying a task is done. With Paperclip, we have a number of mechanisms to keep this going. You might think that you can easily just write a for loop over your task manager and have your agents work, but quickly you&#x27;ll find that falls apart. As soon as you</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=219s">03:39</a></span> find that falls apart. As soon as you start integrating task dependency trees, blockers, multiple agents, item potent checkouts, like locks on checkouts, you find that this tension between liveliness and verification actually gets quite complicated. There&#x27;s really three invariants that are extremely important when you&#x27;re thinking about what you want out of a control plane for your agentic work. You want to ensure that productive work continues. You want to make sure that only real blockers stop work. And you want to make</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=249s">04:09</a></span> blockers stop work. And you want to make sure that infinite loops are bounded. In Paperclip, we have built a number of mechanisms to deal with this problem. So, for example, every time you have a task, there&#x27;s clear transitions to what the next state could be. We have first-class blockers between tasks, and the control plane enforces those blockers. We have moments of interactive human approval, where human choices leave an audit trail. You can set reviewers and approvers on tasks explicitly, meaning when this task completes, another agent can review it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=281s">04:41</a></span> completes, another agent can review it. We also have the idea of watchdogs, which is this maximizer mode, which says, um, try as hard as you can to make sure that this happens. When you have a watchdog, it&#x27;s another agent, um, who is given a goal, and it enforces that all of your agents continue to work until that goal has been achieved. The important thing here is that the watchdog within Paperclip is harness agnostic. You can use it with Pi, OpenGL, Hermes, Claude Code, Codex, whatever you&#x27;re using, you have one consistent interface for ensuring that</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=313s">05:13</a></span> consistent interface for ensuring that goal is complete. So, one of the best pieces of advice we have is that you stop treating done as a Boolean and treat it more like an object. This isn&#x27;t specific to Paperclip. It&#x27;s just advice on how you think about what is done. Humans automatically paper over these details, but when we&#x27;re building agentic systems, it&#x27;s important that your agents can distinguish between the different pieces of what they&#x27;re claiming when they say something is done. The artifact that they&#x27;re saying is complete, the scope, the rubric or the standard, the evidence that it&#x27;s done, who verified the work, who has the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=345s">05:45</a></span> done, who verified the work, who has the authority to sign off on the work, And what risk might be left? And really, what&#x27;s the next action going to be? So, you want to make sure that when you define done, it&#x27;s not just a checkbox. So, if you want to get 100 times more work done, you should steal this checklist. You need to define exactly what does done mean for this task. You definitely want to separate the verifier from the author. Often, this means you&#x27;re using a different model. So, if you&#x27;re coding using Claude, have Codex verify. You want to ask your agents to provide</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=375s">06:15</a></span> You want to ask your agents to provide evidence. Don&#x27;t just ask them to say, &quot;Is this done?&quot; But, give them the tools they need to verify that the work is done. Write the code to have the custom browser harness. Write the code to take the screenshots. Make sure they have access to a browser. Make sure that they have custom agent hooks or custom agent tooling to actually run through and click the buttons and try it out themselves and verify that the work is truly done. Make sure you have a clear chain of custody, that every agent knows that as soon as they&#x27;re done, who they&#x27;re supposed to give the work to next.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=7P0elyLIxXo&amp;t=408s">06:48</a></span> supposed to give the work to next. It can be easy to just fire off a single-line instruction and vibe with whatever comes back. But, if you have serious work that you&#x27;re accountable for, it&#x27;s very important that you define what done really means in as much detail as possible, and that you have a structure for your agents, so that way they can verify that all of the claims that are involved with something being done are actually met. Thank you.</p>

</details>
