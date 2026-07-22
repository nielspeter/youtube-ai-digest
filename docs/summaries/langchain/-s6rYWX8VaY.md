---
title: "/goal: Building big features with dcode"
channel: "LangChain"
video_id: -s6rYWX8VaY
url: https://www.youtube.com/watch?v=-s6rYWX8VaY
published: 2026-07-22T14:59:13+00:00
generated: 2026-07-22T15:27:44+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/-s6rYWX8VaY/hqdefault.jpg
---
# /goal: Building big features with dcode

[![/goal: Building big features with dcode](https://i.ytimg.com/vi/-s6rYWX8VaY/hqdefault.jpg)](https://www.youtube.com/watch?v=-s6rYWX8VaY)

[Watch on YouTube](https://www.youtube.com/watch?v=-s6rYWX8VaY) · **LangChain** · 2026-07-22

## TL;DR
The video introduces `/goal`, a new command in dcode (an open-source, model-agnostic coding agent) that enables agents to tackle large, complex features in a single persistent run. By establishing visible, editable acceptance criteria upfront and allowing mid-run amendments, `/goal` shifts alignment to the beginning of the process—demonstrated by implementing native Python Playwright browser control into dcode itself over roughly four hours with minimal human intervention.

## Key Takeaways
- `/goal` gives a coding agent a durable, long-running objective that persists across many agent reasoning cycles.
- The goal loop wraps the standard ReAct loop: the inner loop decides actions, the outer loop evaluates whether durable criteria are met.
- dcode converts a `/goal` prompt into short acceptance criteria, which the user can review and edit before the run begins.
- Visible, editable criteria upfront reduce the need for constant human-in-the-loop correction during long tasks.
- Users can amend active goals mid-run with `/goal amend`, and messages are interpreted in the context of the existing goal—no need to restate original requirements.
- `/goal show` displays the current goal status and original criteria; `/goal resume` restarts the agent after an interruption or amendment.
- LangSmith tracing (`/trace`) provides turn-by-turn visibility into the agent's work for debugging and workflow analysis.
- The demo implemented native Python Playwright browser control in dcode without MCP, including tests and passing CI, in one shot.
- Because dcode is open source, users can modify the agent harness itself—adding features like browser control to their own local copy.
- The presenter started the goal at 3 PM and returned around 7 PM without needing to continuously restate the task or maintain a mental checklist.

## Detailed Breakdown

### Introducing /goal and the Goal Loop [00:00](https://www.youtube.com/watch?v=-s6rYWX8VaY&t=0s)
The video opens with a recording of dcode implementing a large feature in one shot. The presenter explains that `/goal` is designed for especially large or experimental tasks, giving the agent a persistent objective over a long period. The goal loop is described as wrapping the standard ReAct loop: the inner loop reasons and acts, while the outer loop checks whether those actions satisfied the durable goal. If criteria aren't met, the goal stays active; if progress is impossible, it becomes blocked; only evidence satisfying the criteria completes it.

### Installing dcode and Issuing the First /goal [01:46](https://www.youtube.com/watch?v=-s6rYWX8VaY&t=106s)
After installing dcode via an install script from the docs, the presenter fires it up and types `/goal add native browser control compatibility to dcode without using MCP` (with some typos). dcode immediately converts this into a short set of acceptance criteria. The presenter notes these criteria mostly look right but wants to add one, so they choose "edit criteria" and add: "this is done using the Python Playwright API." Pressing Enter activates the goal. The presenter emphasizes that this visible criteria step is important and not available in some other agents like Codex.

### The Problem /goal Solves: Upfront Alignment [02:48](https://www.youtube.com/watch?v=-s6rYWX8VaY&t=168s)
The presenter explains that for substantial tasks, one-shotting usually falls short—the agent builds something that doesn't quite match intent, skips tests, or fails CI, turning the human into a bottleneck for corrections. `/goal` shifts alignment upfront, makes requirements visible, and allows tailoring mid-run. The agent is then shown working: inspecting architecture, identifying where browser support belongs, and implementing it with Python Playwright, while the goal remains active throughout.

### Monitoring, Amending, and Resuming Goals [03:50](https://www.youtube.com/watch?v=-s6rYWX8VaY&t=230s)
The presenter demonstrates `/goal show` to view detailed information including original criteria. They then use `/goal amend` to add "ensure that CI passes at the end," noting they don't need to repeat the browser control task or paste original requirements—the amendment is interpreted in the context of the active goal. This is highlighted as a major value add, enabling better product direction without extensive human-in-the-loop interaction. After amending, `/goal resume` continues the agent's work.

### Under the Hood with LangSmith Tracing [04:51](https://www.youtube.com/watch?v=-s6rYWX8VaY&t=291s)
The presenter interrupts the agent to show `/trace`, which opens the current session's trace in the LangSmith web portal (assuming LangSmith tracing is enabled). Clicking into a larger turn reveals the goal prompt submitted to the model and a breakdown of all associated work. The presenter notes this is super useful for debugging workflows and recommends checking out other LangSmith videos for more detail.

### Goal Completion and Verification [05:56](https://www.youtube.com/watch?v=-s6rYWX8VaY&t=356s)
Time has passed (visible by lighting change), and the goal


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=0s">00:00</a></span> What you&#x27;re looking at right now is dcode, my open source model agnostic coding agent implementing a feature in one shot. As you can tell from the length, this is a feature that takes a lot of code, a lot of review and a lot of time. In order to one shot this, I used a new feature in dcode, the /goal command. So what is /goal and why is it needed? It is needed whenever you want to accomplish an especially large task like a meaty or</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=31s">00:31</a></span> an experimental PR. It gives an agent a long running, persistent objective to work toward over a long period of time. And to illustrate this, imagine a react loop. A request comes in and the agent reasons about it, acts on it, observes the results and responds. The goal loop doesn&#x27;t replace the agent loop, but rather wraps it. The inner loop decides the next action, the outer loop asks whether those actions actually achieved the durable goal. If the criteria aren&#x27;t met, the goal remains active. If progress is impossible,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=66s">01:06</a></span> it becomes blocked. Only evidence satisfying the criteria completes it. We&#x27;re going to be working with dcode, the model agnostic open source coding agent built for control over your development workflows. And we&#x27;ll be dealing with source code so you can do cool things like adding native browser control. You can download dcode using the link below. For now, let&#x27;s jump in. After installing dcode using the install script found in the docs page, fire it up with dcode. Now I&#x27;ll type /goal add native browser control</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=106s">01:46</a></span> compatibility to dcode without using MCP. With some typos, by the way. Press Enter and the first thing that dcode does is turn that into a short set of acceptance criteria. Now acceptance criteria are the durable requirements which guide the agent&#x27;s work. So we have here, dcode can launch and control a browser through its native browser control interface. And these criteria mostly look right, but say I want to add a piece of criteria. I&#x27;ll choose edit criteria.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=137s">02:17</a></span> Let&#x27;s add a bullet point here and say, this is done using the Python Playwright API. Press enter and it will be accepted and the goal is now active with typos. So the visible criteria step is super important and it&#x27;s not available in some other agents like Codex. You&#x27;ve probably experienced this, but for substantial tasks, one-shotting usually just doesn&#x27;t get you all the way there.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=168s">02:48</a></span> The agent will create a solution that doesn&#x27;t quite match what you had in mind or finish the main feature without tests or CI will fail. And the net result here is that the bottleneck becomes keeping yourself in the loop throughout the entire process. You can imagine concretely, you submit the model request, the agent builds what you sort of want, and then you spend a substantial amount of time fixing and correcting things. But /goal shifts that extra alignment upfront,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=200s">03:20</a></span> makes it visible and allows you to tailor those requirements mid run, which we&#x27;ll see later. Looking back at the screen now, dcode is working on the task, doing things like inspecting the current architecture, identifying where browser support belongs, implementing it, it notes here, Python Playwright. The goal remains active throughout this thread. And we can see that in the input box. Or if I were to interrupt the agent, we can type in /goal show</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=230s">03:50</a></span> for more detailed information, including the original criteria. So let&#x27;s say that I wanna add some guidance here. I can type in /goal amend. and I will say, ensure that CI passes at the end. I don&#x27;t need to repeat the browser control task or paste the original requirements again. The message is interpreted in the context of the active goal. And I think this is a huge value add.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=261s">04:21</a></span> It allows us to direct ourselves toward a better product without needing to involve a ton of human-in-the-loop interactions following what would otherwise be an incorrect completion of work. This will now update our current goal criteria and then I can use /goal resume in order to continue making the machine work. Okay, so the agent is buzzing along, but I just want to jump in real quick because I want to show you something that I think is really cool. We&#x27;re going to take a peek under the hood. So we&#x27;ll interrupt</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=291s">04:51</a></span> the agents and we will type in /trace. Assuming that you&#x27;ve enabled LangSmith tracing for dcode, you can type /trace to open the trace for the current dcode session in the LangSmith web portal. And now here we can see what&#x27;s happening turn by turn in our conversation. So let&#x27;s click into this larger turn here and we&#x27;ll see our inputs. And this is the goal prompt that we had submitted to the model. Here we can see a breakdown of all the work associated with this goal prompt.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=326s">05:26</a></span> This is a super useful tool in debugging your workflows among a ton of other things. We have other videos on LangSmith that I recommend checking out. We don&#x27;t have enough time in this video. Now let&#x27;s get back to the agent run and hopefully it&#x27;s done. Okay, stepping back to the computer. You can probably tell that time has passed because of the change in lighting in here and we are at goal completed. Let&#x27;s scroll up. Yeah, plenty of file edits. Looks like some tests.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=356s">05:56</a></span> Implemented native Python Playwright browser controls, enabled with this browser flag. Works alongside no MCP. Okay, cool. Chrome smoke tests, code quality systems passing, full test suite passes. Okay, well, none of this really matters if it doesn&#x27;t work. So let&#x27;s try it out. So we will run dcode with this browser flag. I think it said I have to do this /browser.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=389s">06:29</a></span> Yeah, that looks like it enabled browser tools. All right. Browser tools enabled for this thread. And we&#x27;ll say visit langchain.com. Approve. And there it is. we have a browser running with langchain.com. That is really cool. Like really cool. I mean, this is sort of a huge feature that we added to our local version of dcode all with one /goal command.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=421s">07:01</a></span> And I mean, this really illustrates the power of both /goal and open source, right? We are modifying the agent, the harness itself in order to bring this into reality. That is really cool. We were able to modify our own agent because dcode is open source, meaning that you can do this right now. I started this goal at 3pm and I came back around 7 and during that time I didn&#x27;t have to continuously restate the task or maintain a mental checklist of everything dcode was</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-s6rYWX8VaY&amp;t=455s">07:35</a></span> supposed to do. Aligning early on criteria and keeping it visible kept everything in check for the length of the run. Again, we&#x27;re including the link below so that you can build out your own harness modifications or do other huge units of work using /goal. Thanks for watching and I&#x27;ll see you in the next one. [MUSIC PLAYING]</p>

</details>
