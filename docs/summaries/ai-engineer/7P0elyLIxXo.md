---
title: "What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip"
channel: "AI Engineer"
video_id: 7P0elyLIxXo
url: https://www.youtube.com/watch?v=7P0elyLIxXo
published: 2026-07-12T06:45:06+00:00
generated: 2026-07-12T21:03:08+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/7P0elyLIxXo/hqdefault.jpg
---
# What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip

[![What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip](https://i.ytimg.com/vi/7P0elyLIxXo/hqdefault.jpg)](https://www.youtube.com/watch?v=7P0elyLIxXo)

[Watch on YouTube](https://www.youtube.com/watch?v=7P0elyLIxXo) · **AI Engineer** · 2026-07-12

## TL;DR
Dotta, creator of Paperclip, argues that "done" in agentic systems is not a Boolean checkbox but a bundle of operational claims—artifact, evidence, rubric, ownership, and next steps—that must be explicitly modeled and verified. Paperclip's liveness model balances continuous work progression with structured verification through state transitions, blockers, human approval points, and harness-agnostic watchdog agents. The core message: if you want agents to produce serious, accountable work, you must define "done" as a rich object and enforce it with a proper control plane.

## Key Takeaways
- "Done" is not a single state but a bundle of claims: artifact produced, evidence provided, rubric met, owner identified, next step known, and residual risk understood.
- Agents can now generate code and documentation faster than humans can verify, creating a new failure mode: more work than humans have capacity to review.
- Exhaustive human verification at high volume degrades into "verification theater"—sign-offs without real scrutiny.
- A control plane must balance two competing forces: liveness (work keeps moving, no blockers) and verification (assurance that work is correct).
- Pure liveness without verification produces AI slop; pure verification without liveness creates unmanageable review queues.
- Three key invariants for an agentic control plane: productive work continues, only real blockers stop work, and infinite loops are bounded.
- Paperclip provides mechanisms including explicit state transitions, first-class blockers, interactive human approval with audit trails, explicit reviewers/approvers, and harness-agnostic watchdog agents.
- Watchdog agents operate in a "maximizer mode," enforcing that all agents continue working until a goal is achieved, regardless of which agent harness is used.
- Treat "done" as an object, not a Boolean—specify artifact, scope, rubric, evidence, verifier, authority, risk, and next action.
- Separate the verifier from the author, ideally using a different model (e.g., if Claude authored, have Codex verify).

## Detailed Breakdown

**[00:00] The Problem with "Done"**
Dotta opens with a scenario: an agent opens a PR, passes tests, updates docs, closes the issue, and declares "Looks done to me." But this flattens fundamentally different operational claims—done enough to merge, deploy, or announce to customers—into a single green checkmark. Most agent systems fail to distinguish these levels.

**[00:30] The New Failure Mode**
Programming is described as "solved," with agents producing code and documentation faster than any human can verify. This creates a novel problem: agents generating more work than humans have time to review. Simply letting agents check a checkbox is insufficient. Saying something is "done" is actually a bundle of claims: an artifact was produced, evidence exists that the task is complete, a rubric exists to verify against, an owner for the next step is known, and the next step itself is known.

**[01:34] Levels of Done**
Dotta outlines a progression of "done-ness": the producer claims completion, a reviewer finds no obvious issues, evidence meets a specified standard, an authorized person approves, someone stands behind the decision, and ideally the outcome survives real-world conditions. Exhaustive human verification fails at high volume, leading to "verification theater"—the appearance of review without real scrutiny.

**[02:05] The Protocol and Control Plane**
What's needed is a protocol for how tasks progress through a system—keeping them moving without falling into invalid states. A control plane must tie task execution to specific contracts and constraints, governing what the system does and which agents receive the next task. The fundamental tension is between verification (assurance of correctness, but work stops) and liveness (work continues without blockers, but no quality control).

**[03:08] The Liveness-Verification Tension**
Pure liveness without approval produces "classic AI slop"—high-volume, low-quality output that is worse than creating nothing over time. Pure peer review creates an enormous review queue humans can't keep up with. The solution requires teasing apart the bundle of claims in "done." A simple for-loop over a task manager falls apart once you introduce dependency trees, blockers, multiple agents, idempotent checkouts, and locks.

**[04:09] Three Invariants and Paperclip's Mechanisms**
Three critical invariants: productive work continues, only real blockers stop work, and infinite loops are bounded. Paperclip implements these through clear state transitions, first-class blockers enforced by the control plane, interactive human approval with audit trails, explicit reviewers and approvers, and watchdog agents. Watchdogs operate in maximizer mode, enforcing that all agents keep working until a goal is achieved, and are harness-agnostic—compatible with Py, OpenGL, Hermes, Claude Code, Codex, etc.

**[05:13] Treat Done as an Object**
Dotta's key advice: stop treating "done" as a Boolean and treat it as an object. Humans naturally paper over the details, but agentic systems require explicitness. The "done" object should capture: the artifact, scope, rubric or standard, evidence, who verified, who has authority to sign off, residual risk, and the next action.

**[05:45] The Checklist for 100x More Work**
A practical checklist: define exactly what "done" means per task, separate the verifier from the author (ideally using a different model), require agents to provide evidence rather than just claiming completion, give agents tools to verify (browser harnesses, screenshots, custom hooks, button-clicking tooling), and maintain a clear chain of custody so every agent knows who receives the work next. For serious, accountable work, vague single-line instructions are insufficient—structure and detail are essential.

## Notable Quotes
- "Agents can actually create more work than humans have time to verify."
- "Saying that something is done is actually a bundle of claims."
- "Exhaustive human verification fails at high volume... you just get a form of verification theater."
- "If you have tasks that are completely alive with no approvals, then what you get is this classic AI slop... it's worse than creating nothing after a long period of time."
- "Stop treating done as a Boolean and treat it more like an object."
- "Don't just ask them to say, 'Is this done?' But give them the tools they need to verify that the work is done."

## People, Tools & References Mentioned
- **Dotta** — Creator of Paperclip, presenter
- **Paperclip** — Agentic work orchestration system with a liveness model
- **Agent harnesses mentioned:** Py, OpenGL, Hermes, Claude Code, Codex
- **Models referenced:** Claude, Codex (used as examples of author/verifier separation)
- **Concepts:** Liveness model, verification theater, AI slop, control plane, watchdog agents, maximizer mode, chain of custody, idempotent checkouts

## Who Should Watch
Engineers and technical leaders building agentic systems who need to move beyond vibe-driven automation and establish real accountability, verification, and liveness in their agent workflows. Anyone struggling with the tension between keeping agent-produced work moving and ensuring it is actually correct will find practical, hard-earned lessons here.


<details class="transcript">
<summary>Full transcript</summary>

<p>An agent opens a pull request. It passes the tests. It updates the documentation. It closes the issue and comments, &quot;Looks done to me.&quot; But is it actually done? Is it done enough to merge? Is it done enough to deploy? Is it done enough to announce to your customers? These are fundamentally different operational claims, and most agent systems just flatten it to a single green check mark. I&#x27;m Dota. I&#x27;m the creator of Paperclip, and I&#x27;m going to give you some hard-earned lessons that we&#x27;ve learned in creating Paperclip&#x27;s liveness model. What does done even mean? Here&#x27;s the</p>
<p>What does done even mean? Here&#x27;s the thing. Programming is solved, and agents can now produce more code and documentation faster than any human can ever verify. And this actually gives us a new failure mode, is that agents can actually create more work than humans have time to verify. So we need a way to verify that our agents are done more than just letting them check a checkbox. Done doesn&#x27;t mean that an agent just changed the status of a task being done. Saying that something is done is actually a bundle of claims. You&#x27;re saying that an artifact was produced, that you have evidence that the task is</p>
<p>that you have evidence that the task is actually complete, and you have a rubric in which you can verify against. You know exactly who the owner is for the next step, and you know exactly what the next step is. There&#x27;s different levels to how done something is. The producer might claim something is complete, but you need to have a reviewer, another party that looks at it and finds no obvious issues. You want to verify and make sure that the evidence actually meets a specified standard. You want to make sure that a person who is authorized to approve it actually approves that the work is done.</p>
<p>actually approves that the work is done. And you want to make sure that there&#x27;s somebody who actually stands behind the decision. And ideally, what you want is that the outcome has actually survived real-world conditions. Because exhaustive human verification fails at high volume. You might be able to verify a few tasks per day, but essentially, if you have humans verifying all the tasks and they have to sign off on it, you eventually what you just get is a form of verification theater. What you need is a protocol for</p>
<p>theater. What you need is a protocol for defining how tasks actually progress through a system. You want to make sure that tasks are always kept moving, but they don&#x27;t get stuck into invalid states. You need a control plane that actually has the execution of the tasks being tied to specific contracts and constraints about what the system will do and what agents it will hand off your next task to. Because really what you&#x27;re trying to play against is this idea around keeping work moving, but also having it</p>
<p>work moving, but also having it verified. When a task has been reviewed by a human, you get the assurance that it&#x27;s correct. But having a human verify it means that the task is dead in its tracks. You also want to keep liveliness. Liveliness means that the work is continuing with no blockers. And you&#x27;re always trying to keep these two things in balance. If you have tasks that are completely alive with no approvals, then what you get is this classic AI slop because you&#x27;re producing a lot of things with kind of no quality control and it&#x27;s worse than creating nothing after a long period of time. But</p>
<p>nothing after a long period of time. But if you have peer review, um then you have this enormous review queue where humans can&#x27;t actually review it by hand anyway. These agents will be creating far more than you can ever actually review, and so we have to find a way to tease apart the bundle of claims that are involved in saying a task is done. With Paperclip, we have a number of mechanisms to keep this going. You might think that you can easily just write a for loop over your task manager and have your agents work, but quickly you&#x27;ll find that falls apart. As soon as you</p>
<p>find that falls apart. As soon as you start integrating task dependency trees, blockers, multiple agents, item potent checkouts, like locks on checkouts, you find that this tension between liveliness and verification actually gets quite complicated. There&#x27;s really three invariants that are extremely important when you&#x27;re thinking about what you want out of a control plane for your agentic work. You want to ensure that productive work continues. You want to make sure that only real blockers stop work. And you want to make</p>
<p>blockers stop work. And you want to make sure that infinite loops are bounded. In Paperclip, we have built a number of mechanisms to deal with this problem. So, for example, every time you have a task, there&#x27;s clear transitions to what the next state could be. We have first-class blockers between tasks, and the control plane enforces those blockers. We have moments of interactive human approval, where human choices leave an audit trail. You can set reviewers and approvers on tasks explicitly, meaning when this task completes, another agent can review it.</p>
<p>completes, another agent can review it. We also have the idea of watchdogs, which is this maximizer mode, which says, um, try as hard as you can to make sure that this happens. When you have a watchdog, it&#x27;s another agent, um, who is given a goal, and it enforces that all of your agents continue to work until that goal has been achieved. The important thing here is that the watchdog within Paperclip is harness agnostic. You can use it with Pi, OpenGL, Hermes, Claude Code, Codex, whatever you&#x27;re using, you have one consistent interface for ensuring that</p>
<p>consistent interface for ensuring that goal is complete. So, one of the best pieces of advice we have is that you stop treating done as a Boolean and treat it more like an object. This isn&#x27;t specific to Paperclip. It&#x27;s just advice on how you think about what is done. Humans automatically paper over these details, but when we&#x27;re building agentic systems, it&#x27;s important that your agents can distinguish between the different pieces of what they&#x27;re claiming when they say something is done. The artifact that they&#x27;re saying is complete, the scope, the rubric or the standard, the evidence that it&#x27;s done, who verified the work, who has the</p>
<p>done, who verified the work, who has the authority to sign off on the work, And what risk might be left? And really, what&#x27;s the next action going to be? So, you want to make sure that when you define done, it&#x27;s not just a checkbox. So, if you want to get 100 times more work done, you should steal this checklist. You need to define exactly what does done mean for this task. You definitely want to separate the verifier from the author. Often, this means you&#x27;re using a different model. So, if you&#x27;re coding using Claude, have Codex verify. You want to ask your agents to provide</p>
<p>You want to ask your agents to provide evidence. Don&#x27;t just ask them to say, &quot;Is this done?&quot; But, give them the tools they need to verify that the work is done. Write the code to have the custom browser harness. Write the code to take the screenshots. Make sure they have access to a browser. Make sure that they have custom agent hooks or custom agent tooling to actually run through and click the buttons and try it out themselves and verify that the work is truly done. Make sure you have a clear chain of custody, that every agent knows that as soon as they&#x27;re done, who they&#x27;re supposed to give the work to next.</p>
<p>supposed to give the work to next. It can be easy to just fire off a single-line instruction and vibe with whatever comes back. But, if you have serious work that you&#x27;re accountable for, it&#x27;s very important that you define what done really means in as much detail as possible, and that you have a structure for your agents, so that way they can verify that all of the claims that are involved with something being done are actually met. Thank you.</p>

</details>
