---
title: "Your Agents Need a Save Button - Hamza Tahir, ZenML"
channel: "AI Engineer"
video_id: bZISsg7H7DA
url: https://www.youtube.com/watch?v=bZISsg7H7DA
published: 2026-07-18T07:00:06+00:00
generated: 2026-07-18T09:46:36+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/bZISsg7H7DA/hqdefault.jpg
---
# Your Agents Need a Save Button - Hamza Tahir, ZenML

[![Your Agents Need a Save Button - Hamza Tahir, ZenML](https://i.ytimg.com/vi/bZISsg7H7DA/hqdefault.jpg)](https://www.youtube.com/watch?v=bZISsg7H7DA)

[Watch on YouTube](https://www.youtube.com/watch?v=bZISsg7H7DA) · **AI Engineer** · 2026-07-18

## TL;DR
Hamza Tahir argues that AI agents lack a fundamental capability the software world has had for decades: a save button. By pairing agent frameworks with durable runtimes that checkpoint full execution state—not just telemetry traces—teams can replay production runs, ask "what if" questions (e.g., swapping models or mocking tools), and evaluate changes across cohorts before shipping.

## Key Takeaways
- Traces alone are insufficient: they capture emitted telemetry but lose runtime context like in-flight variables, file system state, and actual code decisions.
- A "save button" for agents means checkpointing full execution state at runtime, enabling replay and what-if analysis.
- Replay lets you swap models, mock/override tools, or intentionally degrade behavior to see how outcomes change.
- Production runs already contain the data needed to build meaningful cohorts (expensive, slow, or risky runs) for evaluation.
- The core methodology is: checkpoint → replay → diff → decide → route/ship.
- DoorDash reduced simulation time from hours to 5 minutes using replay-based what-if scenarios, achieving 90% fewer hallucinations.
- Naive model swaps can create a false economy: cheaper/faster on paper may mean worse resolution and less value.
- A single replay is just an anecdote; cohort-level analysis is necessary because model self-consistency is low.
- Kitaru (by ZenML) is an open-source runtime layer that checkpoints agent state, connects to traces, and supports replay and diffing.
- Using MCP servers and LLMs to analyze replay reports at scale is practical when dealing with thousands of runs.

## Detailed Breakdown

**[00:00] The Missing Save Button for Agents**
Tahir opens by noting that while document auto-save (Control-S, Command-S) has been standard since the 1980s, agents have no equivalent. The closest thing today is a trace, which captures emitted telemetry (tool calls, inputs, outputs) but is disconnected from the actual runtime—losing variables, file system state, code decisions, and environment context.

**[01:35] Why a Save Button Matters: Replay and What-If**
A save button enables replay: going back in history to ask what-if questions. Examples include swapping to a cheaper open-source model, mocking a tool's return value, or intentionally degrading a tool to test failure behavior. These questions are only answerable if full state is persisted.

**[02:06] An Emerging Stack Category**
A new layer is emerging in the agent stack: durable runtimes that sit below harnesses/frameworks, augment traces with actual code execution and environment state, and complete the picture of the system. Production already has the traces and (ideally) checkpoints needed to ask improvement questions.

**[03:11] Closing the Loop on Evals**
With checkpointed state, you can build cohorts of runs (e.g., expensive, slow, risky), replay a change, diff against the baseline, and decide whether to ship. Tahir frames this as "checkpoint, replay, diff, decide"—closing the loop by evaluating against production checkpoints rather than synthetic data.

**[04:14] DoorDash Case Study**
DoorDash published a blog post (June 1) describing a simulated environment where they replayed customer bot interactions. They reduced simulation time from hours to 5 minutes, ran hundreds of simulations, cut hallucinations by 90%, and stayed within two points of production results—demonstrating that simulations grounded in real runs are highly representative.

**[05:16] Demo: Kitaru by ZenML**
Tahir introduces Kitaru, a new open-source tool from ZenML (where he is co-founder). Kitaru provides a runtime layer below the harness, connects to traces, and checkpoints state. In the demo, a support agent handles customer requests and escalates to humans when needed. Each checkpoint shows configuration, where it ran, the code, and artifacts in/out, plus the environment (Docker image or sandbox).

**[06:20] Replay Scenario: Swapping the Model**
Tahir replays an execution from a specific checkpoint, changing the model to GPT-5 Nano (cheaper). Kitaru skips the first three checkpoints (already persisted) and resumes execution from the change point. The replayed run looks similar to the original.

**[07:52] Replay Scenario: Mocking a Tool**
Next, he mocks the `lookup_policy` tool with a different function from his codebase, holding the model constant. Because Kitaru is connected to the actual code, modifying tool behavior is straightforward. The replay produces a slightly different artifact and outcome.

**[08:54] Diffing Runs Side by Side**
Kitaru's diff command generates a URL to a UI comparing the original run and two forks. The baseline checkpoints are identical (skipped), but divergence appears after the change point. In the third replay (changed policy), the final decision shifts from "needs review" to "safe to answer"—a potentially significant behavioral change.

**[10:59] Cohort-Level Replay**
Tahir extends the approach from single runs to cohorts—e.g., all expensive runs sorted by cost. He uses the `replay many` command to apply one change (model swap or tool change) across the entire cohort, emitting results to JSON.

**[12:02] Analyzing Cohorts with MCP and LLMs**
Manually diffing thousands of runs is impractical. Tahir uses the Kitaru MCP server to have an LLM read the JSON report and analyze the cohort, flagging red flags and recommending whether to ship the change.

**[13:38] The False Economy of Naive Model Swaps**
Tahir cautions against single-dimensional cost analysis. A BrainTrust study showed that naive model swaps can look cheaper and faster on paper but reduce value if the support bot stops resolving requests. He also cites the tau-bench finding that a model passing 60% of the time is only self-consistent ~25% of the time—meaning a single replay is an anecdote, and cohort analysis is essential.

**[15:10] The Production Playbook**
The recommended playbook: start from real production runs (not synthetic), build meaningful cohorts (expensive, long, risky), never ship based on one or two replays, do this at scale, and automate the loop with a human in the loop at the end.

**[16:11] Conclusion and Cohort Verdict**
The cohort analysis concludes "don't ship"—the cheaper model, despite looking good in a single replay, underperformed across the broader set of support cases. Tahir reiterates that modeling agents with a harness on a checkpointing, replayable runtime is the key to answering what-if questions, and points to Kitaru as an open-source tool to do so.

## Notable Quotes
- "Agents, they don't have [a save button] today. The only thing we have which is closest is a trace."
- "Save allows you to replay. You can go back in history and ask the what if question."
- "Checkpoint, replay, diff, decide."
- "One replay is just an anecdote and having a cohort analysis is way, way, way better."
- "Never ship anything by just replaying one or two things."

## People, Tools & References Mentioned
- **Hamza Tahir** — Co-founder of ZenML, presenter
- **ZenML** — Orchestration platform, been around for years
- **Kitaru** — New open-source runtime layer by ZenML for checkpointing, replay, and diffing agent executions
- **DoorDash** — Referenced for a June 1 blog post on simulated replay environments for customer bots
- **BrainTrust** — Referenced for a study on false economies in naive model swaps
- **tau-bench** — Referenced regarding model self-consistency statistics
- **GPT-5 Nano** — Used as a cheaper model in the replay demo
- **MCP server** — Kitaru's MCP server used for LLM-driven cohort analysis
- **Otel (OpenTelemetry)** — Mentioned in context of observability spans

## Who Should Watch
AI engineers and platform teams building production agents who want to move beyond read-only traces toward replayable, evaluable execution state. It's especially relevant for those responsible for cost optimization, reliability, and safe model or tool changes in production agent systems.


<details class="transcript">
<summary>Full transcript</summary>

<p>Have you ever looked at your agent execution and asked yourself the question, why did it do that? What if it had done a different thing? Would it have been cheaper? Would it have been faster? Well, you can do all these things if your agents have a save button. We&#x27;ve had the save button for documents for decades now. Since the 1980s, people have been used to pressing control S, command S uh or auto saving while you&#x27;re working</p>
<p>uh or auto saving while you&#x27;re working to have a persistent state. But agents, they don&#x27;t have that today. The only thing we have which is closest is a trace. A trace gives you the emitted telemetry data of how an agent calls tools in the input and output of that state. Now, while this is a good start, it is actually very disconnected from the runtime in which these agents actually execute. So, all the variables that are in state, all the file system that is in in flight, um the decisions that it makes in the code, uh the actual</p>
<p>that it makes in the code, uh the actual code itself, all of that is lost and it is only stamped as a read-only trace by the end, which is sitting in another tool far away from where the actual code is. And I think this is what&#x27;s missing today in the industry is that we don&#x27;t have a clear connection between the observability spans that are emitted with Odel and the execution. And maybe at this point you might be wondering, but why even bother? Why do I need to have a save button?</p>
<p>need to have a save button? Well, save allows you to replay. You can go back in history and ask the what if question. What are the types of questions you might want to ask? Well, you might want to swap the model. Maybe you use a an open-source model that is cheaper. Maybe you mock a tool and you override the what it returns. Maybe you degrade it intentionally to see what would happen if things are wrong. And these sorts of questions are only possible if you have that state. And there is a category of the stack</p>
<p>there is a category of the stack emerging which actually allows that. And this sit on top of the harness sit on top of the frameworks that allow you to create agents. And put a durable runtime below that. Um and augments the traces that are emitted with actually the code execution and the things that are around it to actually complete the state of this of the of the system. And the good news is that once you have such a system in production, you already have the</p>
<p>in production, you already have the information you need to ask those questions that are relevant to making your system better, cheaper, and faster. Production already has the traces. It already has these state checkpoints ideally from the runtime that can allow you to go back in time and ask those questions. For example, let&#x27;s take an agent example which does a customer resolution and refunds after a chargeback dispute. Well, you can then see if the order status is changing languages or whether</p>
<p>status is changing languages or whether the request should have been escalated or maybe a smaller model would have handled it if the runtime is checkpointing each of the state as it goes along. Almost like an auto save, a command S, a control S in your agent. And once you have that, you can even close the loop. Uh this conference is all about loops. So, this is nothing different. You have a cohort of runs that you think maybe matter because maybe they&#x27;re too expensive, they took too long. You replay a change, you diff it, you see</p>
<p>replay a change, you diff it, you see what would have happened when you have the baseline, which you know what happened in the first place, and then you decide and you route and you ship back. That&#x27;s closing the loop on your e-vals. It&#x27;s It&#x27;s It&#x27;s basically evaluating using your production traces. So, it&#x27;s basically evaluating using your production checkpoints. So, checkpoint replay diff decide. And this is really the methodology that that</p>
<p>this is really the methodology that that I&#x27;ve seen and I&#x27;ve seen others do, uh which has really scaled. For example, DoorDash. DoorDash has a a blog post on the 1st of June where they talk about having a simulated environment where they replayed customer bots. And they&#x27;ve done what-if scenarios and seeing how they could have made it better. And where And where it used to take them hours and hours to to do this, now they&#x27;ve reduced it to 5 minutes uh with hundreds of simulations, have 90% less hallucinations, and they&#x27;re</p>
<p>90% less hallucinations, and they&#x27;re still two points within what they&#x27;ve seen in production. So, the simulations are pretty good because they&#x27;re grounded in what&#x27;s already happened. So, we&#x27;re going to just walk through this um in an example, and we&#x27;re going to see how this works. Uh for this demo, we&#x27;re going to be using a tool called Kitaru. Kitaru is a very new tool that is launched by the team at uh ZenML. ZenML is has been around for many years and is a player in</p>
<p>around for many years and is a player in the orchestration space. I&#x27;m one of the co-founders. And Kitaru is something we&#x27;ve launched recently, which allows you to have a runtime layer below your harness layer, and also connect to your traces. Um and do all the checkpointing that we were just talking about and then running replay scenarios. So, you can see here I have all of my I have a support uh agent which looks at my customer requests and escalates it when it needs to to humans. You can see various things as you might expect. Um, every tool call</p>
<p>expect. Um, every tool call uh can see a timeline view if I wanted. And here the difference is that if I if I click on a particular um um checkpoint like a tool call, I can see the configuration, where it ran, uh the code it it took um and the artifacts which came in and out of it. Um and this combination of code and the artifacts that it created and the environment in which it ran in, whether it was a Docker image or a sandbox, those are all snapshotted in state here between the checkpoints.</p>
<p>between the checkpoints. And you can see that here in this particular example, there was a few tool calls every time it went to the LLM, and I can actually see um you know, how long it took. But imagine I wanted to do something different. Imagine I wanted to change the model if I maybe at this point I wanted to use a cheaper model. Would it have done the same stuff afterwards? So, to do this in Kitaro, it&#x27;s quite easy. All you have to do Now, to do this in Kitaro is quite easy.</p>
<p>Now, to do this in Kitaro is quite easy. All you have to do is you have to take your execution and replay it at a particular point. So, I&#x27;m just going to copy this over and I&#x27;m going to put it in my terminal and see what happens. So, here what I&#x27;m doing is essentially I am saying, &quot;Okay, after this particular tool call, change the model to GPT-5 Nano, which is obviously a bit cheaper.&quot; Um and then what&#x27;s going to happen here is</p>
<p>is there&#x27;s going to be a new execution that&#x27;s launched from 71 and you can see the first three checkpoints are skipped. So, they&#x27;re all skipped because Kitaro already has the state of all the checkpoints before that. All it needs to do is just change this particular checkpoint and then execute start executing from here. And this is really cool because now I can see what would have happened in this scenario if there was a cheaper model. So this looks pretty similar to me, but what if I had wanted to do a even</p>
<p>what if I had wanted to do a even different change? What if I wanted to mock a tool or or or if I wanted to change a tool call? Well, in order to do that, you can mock up for example the lookup policy tool. And here it&#x27;s also very easy. I can just go back here. Replay. And this time, rather than changing the model, I am changing the lookup policy. And I&#x27;m mocking it with another function in my code base, which returns a different lookup policy. And I&#x27;m just trying to understand if the</p>
<p>And I&#x27;m just trying to understand if the policy had changed, what would have happened. This time I&#x27;m holding the model constant. Now, the interesting thing here is that because I have the code, it&#x27;s very easy for me to do tool calls and to change these particular things and do more experiments than I would have had if I was completely disconnected from the code base. And here you can see that the code base is a little bit different, so I see my logs here. They look a little bit different. And here you can see that I got a slightly different artifact maybe from the tool call, and it published the thing. So now again, I have three runs.</p>
<p>thing. So now again, I have three runs. I have the original run and I have the two replays. Now, what if I wanted to see them side by side, right? So Kitaro actually has this very handy diff command that lets me give an original ID of an execution and then allows me on the other side to actually see them side by side. So I can see what happened. So there&#x27;s a few warnings here about some artifacts, but in a second it will go and give me a URL.</p>
<p>it will go and give me a URL. I can copy this URL and I can actually put it directly here. And now I have a very nice um comparison of the original and the two forks. Um I can see a bunch of things here, but I think what&#x27;s really interesting is this view. So, in this view, you can see that the first part of the the baseline is the same, right? So, these things were skipped. They were exactly as it is. The state is exactly where it was. Um but now, right after that, in the third replay, it&#x27;s a little bit different, right? The tool call happened</p>
<p>different, right? The tool call happened a bit differently because we used a different policy, and then something changed after here. Um here, it took a little bit longer. And you can really start looking at the final result. And if I click on the final result, I can actually see the artifacts side by side. I can see what decision um it actually ended up making. So, you can see that it uh here, it restricted the count charge. Here, it also restricted it. Here, it also restricted it. In the first two, it actually needs review. In the third, because we changed the policy, it&#x27;s safe</p>
<p>because we changed the policy, it&#x27;s safe to answer. So, this might or might not be good in your scenario, but if is this is what you expected to see? Well, maybe. Because the these two were cheaper at the end of the day. For for for the number of tokens consumed, uh they were cheaper. Input and output. And you can see a bunch of detail here uh in the in the UI, which might be useful for these for these analyses. Okay, but this is just one point, right? What if I wanted to do this across a cohort? What if I wanted to have a bunch</p>
<p>cohort? What if I wanted to have a bunch of runs, right? Which actually um maybe sorted by cost. So, maybe I took all of my expensive ones. Then I wanted to do one change across the entire cohort. So, change the change all the tool calls that happened uh that happened for this particular set of configurations across the cohort. Or change the model itself um and use a cheaper model across the cohort. So, this gives me a bigger distribution of information and replays that I can use.</p>
<p>that I can use. Um and now, I can just this. Um, and the way you would replay it is you can use the replay mini command where you actually um, start from a particular point and you do the same as you did before just across the cohort. Um, this is going to take a while, so I&#x27;m not going to do it now. But once you execute it, in this particular case, I just emitted it to JSON, so I have a very nice, uh, JSON here, and this JSON gives me a bunch of</p>
<p>here, and this JSON gives me a bunch of things. So, this is a bit hard to do the UI, right? So, there&#x27;s a lot of things going on. You can&#x27;t just do the many, many, many comparisons here. Um, but what you could do, and what I love to do personally, is use the Kitaru MCP server. And here what you do is you can just say, &quot;Hey, read this you read this JSON report and do an analysis on what you think I should be doing across the cohort.&quot; And I think this is what What is really important is to be using agents and LLMs</p>
<p>important is to be using agents and LLMs to analyze these cohorts across a plethora of data because at some point uh, I mean, 10 is probably easy to do, but what if you have thousands? Um, and doing thousands and thousands is hard, and this is where skills and MCP servers get really relevant and having the runtime be queryable and go into your execution and fetch the artifacts is very important. So, it&#x27;s going to be it&#x27;s going to be uh, doing a lot of things. So, it&#x27;s it&#x27;s it&#x27;s trying to, you know, um, run an analysis around these decisions and it&#x27;s going to flag</p>
<p>these decisions and it&#x27;s going to flag any um, red flags that that happen. So. While this is going on, um, maybe we can go back and continue our presentation. So, um, Here you can see, yeah. Yes, if you change the model, it can get very cheap. And of course, you don&#x27;t want to do it across just one sample, but across many because then you can see a bigger variation. I think one thing which is</p>
<p>variation. I think one thing which is important here is and to be very honest is that while we&#x27;ve been doing it this with our users and customers, what I&#x27;ve personally seen is that having a naive model swap usually or often times doesn&#x27;t work. So just changing for example to a cheaper model and just looking at the cost one single dimensionally, obviously it could be that you&#x27;re you&#x27;re spending a lot less money, but what happens if your support board is not resolving the requests, right? So this is a study from BrainTrust. Excellent study where they</p>
<p>BrainTrust. Excellent study where they actually looked at that and they saw that there could be a false economy if you do a naive model swap because it might look on paper that you&#x27;re faster and you&#x27;re cheaper, but at the end of the day you have to look at the value created, right? So it&#x27;s a trade-off between how much money you want to spend and and yeah, the result. And also, if you look at the towel bench, what we must understand is that a model that passes 60% of the time is only self-consistent about a quarter of the time. So which basically means that one</p>
<p>time. So which basically means that one replay is just an anecdote and having a cohort analysis is way way way better. Um and because then you can really see across a population and across scale what would have happened not just looking at one estimate. This can get very expensive of course and this is where you have to be really smart about what you replay and have tooling that really helps you. And this you can really bake into your production process as well, right? So</p>
<p>production process as well, right? So again, if you if you take a step back and look at the playbook, you can start from real runs, not synthetic, but real runs, real production uh state. Build cohorts that matter. Um maybe take the expensive ones, maybe take the long ones, maybe take the risky ones. Um never ship anything by just replaying one or two things. Um and just do this at scale and uh ship, route, and hold, and try to automate that loop as much as possible. Maybe there&#x27;s an agent that&#x27;s doing that</p>
<p>Maybe there&#x27;s an agent that&#x27;s doing that for you. Um that&#x27;s even better. But you just have a human in the loop at the end. But you just have a human in the loop at the end. Now, let&#x27;s see where our cohort analysis has gotten us. Okay, so we&#x27;re done. So, the verdict is don&#x27;t ship. So, even though it looked like from a single replay that it was cheaper to do and we reached the same result, across a bunch of those support cases, you actually saw that our agent concludes that you shouldn&#x27;t be using a cheaper model in this particular case</p>
<p>cheaper model in this particular case for your data. But this might be different for your data. In conclusion, um if you want to be replaying your agent executions and answering the questions what if I had done something different while designing this agent or what if the agent could be driven to do something different? Well, you can do this if you model your agent with your harness in a runtime that can</p>
<p>with your harness in a runtime that can checkpoint state and is able to replay that state from code with different scenarios. If you want to use Guitar Ru, the the the tool that I showed that allows you to do it, um you can scan the repo. It&#x27;s open source, free to use, and uh we&#x27;d appreciate the feedback and love. Thank you so much, and see you guys on the next one.</p>

</details>
