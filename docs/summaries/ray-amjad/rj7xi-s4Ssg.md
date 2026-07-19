---
title: "Anthropic Just Dropped the Feature That Makes Sonnet Feel Like Opus"
channel: "Ray Amjad"
video_id: rj7xi-s4Ssg
url: https://www.youtube.com/watch?v=rj7xi-s4Ssg
published: 2026-04-09T23:46:24+00:00
generated: 2026-07-17T19:30:37+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/rj7xi-s4Ssg/hqdefault.jpg
---
# Anthropic Just Dropped the Feature That Makes Sonnet Feel Like Opus

[![Anthropic Just Dropped the Feature That Makes Sonnet Feel Like Opus](https://i.ytimg.com/vi/rj7xi-s4Ssg/hqdefault.jpg)](https://www.youtube.com/watch?v=rj7xi-s4Ssg)

[Watch on YouTube](https://www.youtube.com/watch?v=rj7xi-s4Ssg) · **Ray Amjad** · 2026-04-09

## TL;DR
Anthropic has added a new `/advisor` command to Claude Code that lets a primary model (like Sonnet) consult a stronger model (like Opus) when it needs help with complex decisions. The feature automatically forwards the full conversation history to the advisor model, which returns feedback that is added back into the shared context—offering slightly better performance and lower cost on benchmarks, and likely foreshadowing how the upcoming "Myphos" model will be made accessible despite expected high pricing.

## Key Takeaways
- The `/advisor` command in Claude Code lets a weaker/cheaper main model consult a stronger advisor model on demand.
- Currently the only advisor options are Opus 4.6 and Sonnet 4.6.
- The advisor receives the entire conversation transcript automatically—no manual parameters are needed.
- The advisor is called before committing to an approach, when stuck, or when the model believes the task is complete.
- Short, trivial tasks (e.g., changing colors) skip the advisor entirely.
- If empirical results contradict advisor advice, the model is instructed to surface the conflict with another advisor call rather than silently ignoring the advice.
- Advisor feedback is added to shared context, so future advisor calls can see prior advice.
- The advisor cannot read extra files on your machine—it only sees the chat history.
- Benchmarking shows this approach is slightly cheaper in raw API tokens, consumes less of your Claude Code plan usage, and yields slightly better performance.
- The presenter expects that once "Myphos" launches, users will run Opus as the main executor and use Myphos as the advisor to manage costs.

## Detailed Breakdown

### Introducing the `/advisor` Command [00:00](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=0s)
The video opens with the new `/advisor` slash command in Claude Code, which the presenter suggests is preparation for the upcoming "Myphos" model release. When invoked, `/advisor` lets you configure an advisor tool. Currently the available advisor models are Sonnet and Opus. The recommended setup is to run Sonnet as your main model and use Opus as the advisor.

### How Advisor Works with Sonnet and Opus [00:31](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=31s)
The presenter explains the workflow: you code with Sonnet, and when Sonnet gets stuck, it calls the advisor tool to ask Opus a question. This is compared to the existing `/model opusplan` approach, where Sonnet handles execution but Opus handles planning. Combining both would give you an Opus-generated plan upfront, Sonnet execution, and Opus advisor intervention when needed.

### Current Model Options and Future Myphos Integration [01:01](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=61s)
Right now `/advisor` only shows Opus 4.6 and Sonnet 4.6. If you're already on Opus, using Opus as advisor offers little benefit over a subagent. If you're on Haiku, Sonnet 4.6 as advisor makes sense. The presenter predicts that Myphos will eventually appear here, and because it's expected to be expensive, most users will keep a cheaper model as the main executor and call Myphos as the advisor for hard problems.

### Behind the Scenes: How the Advisor Tool Works [01:38](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=98s)
The tool description says the advisor acts as a "stronger reviewer" who sees your full conversation transcript. There are no parameters—calling `advisor()` automatically forwards the entire history: task, tool calls, results, and reasoning. The advisor is called before substantive work (writing, committing to an interpretation, building assumptions) and when the model believes the task is complete. It's also called when stuck, when errors recur, when approaches aren't converging, or when considering a change of approach.

### When the Advisor Is and Isn't Called [02:08](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=128s)
On tasks longer than a few steps, the advisor is called at least once before committing to an approach and once when declaring the task done. On short reactive tasks—like changing some colors—the advisor is skipped because the task is too simple.

### How to Weigh Advisor Advice [02:41](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=161s)
The tool instructs the model to give advisor feedback serious weight. If empirical results contradict the advisor's advice, the model should surface the conflict with another advisor call rather than silently switching approaches. A passing self-test alone is not considered evidence that the advisor's advice was wrong. The full tool description is available in the pinned comment.

### Live Demo of Calling the Advisor [03:14](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=194s)
The presenter demonstrates the feature using a previous session involving a billing logic bug. He asks Claude Code to call the advisor to verify the proposed solution. The interface shows "advising using Opus 4.6," and the advisor flags two things for the Sonnet model to consider. A key limitation is noted: the advisor can't consult extra files on your machine—it only sees the chat history.

### Shared Context and How Advisor Feedback Accumulates [03:46](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=226s)
A diagram from Twitter illustrates the architecture: Sonnet is the main executor, shared context accumulates the conversation and tool history, and the executor can call the advisor on demand. The advisor's feedback is added back into shared context, meaning future advisor calls can see previous advice given.

### Benchmarking, Cost, and the Presenter's Personal Take [04:17](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=257s)
Benchmarking shows the advisor approach is slightly cheaper in raw API tokens and consumes less of your Claude Code plan usage limits, with slightly better performance on some benchmarks. The presenter says he won't use it much right now because he already runs Opus full-time and sees more value in subagents with independent context. However, he envisions using it once Myphos launches—running Opus as the main executor and consulting Myphos as the advisor.

### Channel Plug and Newsletter [04:47](https://www.youtube.com/watch?v=rj7xi-s4Ssg&t=287s)
The presenter closes by encouraging subscriptions, noting he makes comprehensive Claude Code videos. He also promotes a Claude Code newsletter where he shares strategies and techniques, and mentions that signing up provides access to free videos from his masterclass.

## Notable Quotes
- "Consults a stronger reviewer who sees your full conversation transcript. There are no parameters."
- "If the empirical results contradict advisor advice, surface the conflict with another advisor call rather than silently switching."
- "A passing self-test is not evidence that the advice is wrong."
- "I'd rather get advice from a subagent that has an independent context."
- "I would have the main executor being Opus because it's still a very capable model. And then getting advice from Myphos instead."

## People, Tools & References Mentioned
- **Claude Code** — Anthropic's CLI coding tool
- **`/advisor`** — New slash command for consulting a stronger model
- **`/model opusplan`** — Existing mode where Opus handles planning and Sonnet handles execution
- **Opus 4.6** — Anthropic model, currently available as an advisor
- **Sonnet 4.6** — Anthropic model, recommended as the main executor
- **Haiku** — Anthropic model, mentioned as a potential main executor
- **Myphos** — Upcoming Anthropic model, expected to be expensive
- **Twitter/X** — Referenced for Anthropic's shared diagram of the advisor architecture

## Who Should Watch
Developers and power users of Claude Code who want to understand the new `/advisor` feature, how it fits into multi-model workflows, and how it may shape access to future high-end models like Myphos.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=0s">00:00</a></span> Okay, so we have a brand new slash command added to Claude Code, which is likely preparing us for when Claude Myphos releases. So it&#x27;s /advisor. So when you do /advisor, you can configure the advisor tool and it should take you to something like this. And essentially this is a tool that&#x27;s built into Claude Code for when it requires stronger judgment about a particular problem. Now you can see right now we only have Sonnet and Opus. So if you&#x27;re on Opus, ideally you want your main model in Claude Code to be on Sonnet. So you do /model and then pick Sonnet. And essentially</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=31s">00:31</a></span> when you&#x27;re coding with the Sonnet model and it ends up getting stuck, then it would call the advisor tool to ask Opus a question. This is kind of similar to /model opusplan whereby Sonnet is used all the time except for when you&#x27;re in planning mode, in which case Opus is used. So if you were to combine the two together, you would have a really good plan at the very beginning, then it would switch over to Sonnet for the actual execution. And if Sonnet ends up getting stuck with something, then it would call the advisor tool to ask Opus what the deal is here. Now</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=61s">01:01</a></span> right now with /advisor, you can only see that we have Opus 4.6 and Sonnet 4.6. So if you&#x27;re already on Opus and you&#x27;re using Opus as advisor, you&#x27;d probably not see much benefit to doing that over using a subagent of sorts. And if you&#x27;re in Haiku, then you may want to use Sonnet 4.6. Now what they will likely be adding here in the future is like Myphos for their upcoming model, because chances are since it&#x27;s so expensive, we won&#x27;t be able to afford it most of the time. Until like prices come down and stuff in the future. So I imagine what many people will be doing in Claude Code is sticking to Opus and then having the advisor call Myphos with the entire like chat</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=98s">01:38</a></span> history and log to help it work around like a particularly hard problem. Now the way that it works behind the scenes is that essentially the tool description consults a stronger reviewer who sees your full conversation transcript. There are no parameters. When you call advisor(), your entire history — task, every tool call and result, your reasoning — is automatically forwarded. The advisor sees exactly what you&#x27;ve done. Now, of course, you can tell Claude Code to call this tool when you&#x27;re stuck, but it says it will be called before any substantive work. So before writing,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=128s">02:08</a></span> before committing to an interpretation, before building an assumption. And it&#x27;s also called when the model believes the task is complete. So it&#x27;s told to first make deliverable durable first and then actually call the advisor. When stuck, errors recurring, approaches not converging, results don&#x27;t fit, or when considering a change of approach. Now guidance on frequency says, on tasks longer than a few steps, call it at least once before committing to an approach, and once declaring done. On short reactive tasks, skip it. Which means that if you ask Claude Code to change some colors around, then it will not call the advisor because it&#x27;s too simple of a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=161s">02:41</a></span> task. Now this is a part that&#x27;s interesting. So how to weigh the advice. Give it serious weight, as you would expect. And if the empirical results contradict advisor advice, surface the conflict with another advisor call rather than silently switching. So I find this part particularly interesting. I&#x27;d like to see that in action. And now it&#x27;s like a passing self-test is not evidence that the advice is wrong. Now this is a summary of the tool description. If you want to read the full one, then it will be down below in the pinned comment. Now let&#x27;s see this in action. If I go to previous session and this is some bug that Claude Code found with the billing logic,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=194s">03:14</a></span> if I wanted to call the advisor, I could either like tell it directly or Claude Code during the execution may realize that it needs to call the advisor. So we already have it set over here with Opus. And I will just say, hey, can you call the advisor to check that this will be the solution here? And then pressing enter, it now says advising using Opus 4.6. And the advisor basically flagged two things over here that we would want our Sonnet model to consider. Now it seems that there are some things to bear in mind when doing this. Firstly, it seems that the advisor like can&#x27;t actually consult extra files on your machine. The entire</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=226s">03:46</a></span> chat history is being passed to the advisor. And then that result is being passed back into your session. So as they showed on Twitter, this is what it looks like. You have the main executor being Sonnet. You have the shared context that has been accumulated so far in the history, which is a conversation, tools, and so forth. And then the executor can call the advisor on demand. That advisor would send feedback and that would be added to shared context, which likely means that any future advisor can see any previous advice that previous advisors have given. Now, when it comes to benchmarking, they found that using this approach is slightly cheaper if you</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=257s">04:17</a></span> were paying for raw API tokens, but it would mean that it consumes less usage limits on your Claude Code plan as well. And you also do get slightly better performance on some of these benchmarks. Now I will personally not be using this that much because I use Opus all the time and I don&#x27;t see any benefit in getting another Opus advisor with the same chat history so far to give advice. I&#x27;d rather get advice from a subagent that has an independent context. But I would see myself using this in the future whereby if Myphos is released, basically swapping this all around,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=287s">04:47</a></span> I would have the main executor being Opus because it&#x27;s still a very capable model. And then getting advice from Myphos instead. And this is probably one of the ways they&#x27;re planning on making Myphos accessible to us once it is released, because apparently it will be really expensive. Now, if you do like this kind of stuff, then do subscribe to the channel because I do make the most comprehensive Claude Code videos here on YouTube. And if you want to stay ahead of the curve, then I also have a Claude Code newsletter whereby I share some of my own strategies and techniques like on a regular basis. Signing up will give you access to some free videos in my masterclass</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=rj7xi-s4Ssg&amp;t=318s">05:18</a></span> that you may find helpful as well. There will be a link down below if you are interested.</p>

</details>
