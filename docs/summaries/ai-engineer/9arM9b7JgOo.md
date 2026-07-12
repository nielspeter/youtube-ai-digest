---
title: "Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat"
channel: "AI Engineer"
video_id: 9arM9b7JgOo
url: https://www.youtube.com/watch?v=9arM9b7JgOo
published: 2026-07-11T14:45:18+00:00
generated: 2026-07-12T21:40:29+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/9arM9b7JgOo/hqdefault.jpg
---
# Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat

[![Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://i.ytimg.com/vi/9arM9b7JgOo/hqdefault.jpg)](https://www.youtube.com/watch?v=9arM9b7JgOo)

[Watch on YouTube](https://www.youtube.com/watch?v=9arM9b7JgOo) · **AI Engineer** · 2026-07-11

## TL;DR
Jeffrey Lee-Chan demonstrates how he uses Open Claw to accelerate development at "idea velocity," combining it with tmux terminals and agent orchestrators to parallelize AI coding workflows. He showcases real projects built with this stack and discusses the conceptual advantages of separating planning/context from code execution.

## Key Takeaways
- **Open Claw vs. direct Claude**: Open Claw specializes in task specification and context (specs, goals, history), while Claude Code handles implementation details — keeping these separate prevents context pollution.
- **Frictionless communication** is a core concept: being able to briefly message your AI agent (even via Slack) without re-explaining context, because it retains memory of prior requests.
- **Parallelization via work trees and tmux**: Multiple agents work simultaneously using git work trees, managed through tmux terminal sessions.
- **Manager-worker architecture**: Open Claw acts as an orchestrator/manager, spawning worker agents that run Claude Code, which can themselves spawn sub-agents — creating a hierarchical agent structure.
- **Reduced bias through separation**: When the manager agent reviews worker output, it provides less biased assessments than a single agent reviewing its own work.
- **Practical demos**: An AI RPG with D&D-style dice mechanics, and a multi-AI analysis website that queries multiple models and synthesizes answers.
- **Model selection is budget-driven**: Uses Codex 53 as default orchestrator, switching to MiniMax when token budgets run low, noting GPT 54 consumes more tokens.
- **Sandbox/staging setups** can increase token usage but provide reliability for integration testing before production deployment.

## Detailed Breakdown

**[00:01] Workshop Setup and Agenda**
Jeffrey outlines the workshop structure: helping newcomers install Open Claw, offering advanced users an experimental staging environment for running two Open Claw instances, 10-minute Q&A segments, and periodic discussion breaks every 5 minutes.

**[01:02] Personal Workflow Overview**
He describes his setup where, roughly 70% of the time, he briefly describes a task and Open Claw executes it using retained context. Example: saying "fix the skeptic agent" works because Open Claw remembers prior conversations about a custom code review tool. He uses multiple agents with git work trees for parallelization and notes that his own responses to agents are simple enough that "an agent could replace me" — his current goal.

**[03:08] Core Concepts of Open Claw**
Jeffrey presents two key concepts: **frictionless communication** (easily messaging your AI rather than remote-desktopping in) and the **central axis of control** — a spectrum from "cowboy mode" (giving agents full autonomy) to personal control via tmux terminals. He uses a forked agent orchestrator framework to manage workers, and notes that once Claude Code takes over, it can spawn its own sub-agents, creating a layered managed-agent hierarchy.

**[04:42] Q&A: Why Open Claw Over Direct Claude?**
A participant asks why use Open Claw instead of Claude directly. Jeffrey explains **specialization**: when Claude opens, it reads CLAUDE.md files, skills, and MCPs — consuming ~25% of context with implementation details. Open Claw keeps context focused on specs, goals, and task history. He also notes browser testing has improved dramatically — agents that struggled with pop-ups and passwords a year ago now handle these reliably.

**[07:53] Demo: AI RPG and Multi-AI Analysis Website**
He shows two projects: an AI RPG with a D&D dice-roll system that prevents players from always "winning" (unlike raw ChatGPT/Gemini chats), and a multi-AI analysis site that queries multiple models and synthesizes their answers — yielding better results than single-model queries. The site features vertical tabs and notifications for completed tasks.

**[09:30] Manager-Worker Dynamics and Bias Reduction**
Jeffrey explains that using terminals as a manager rather than a coder reduces bias. A worker agent working on its own PR might declare it "amazing," but a manager agent with different context can objectively assess that another PR should supersede it. He credits tmux for significantly improving his efficiency.

**[11:04] tmux Discussion with Austin**
Austin, a tmux creator, joins briefly to mention new features: Cloud Code Teams integration (auto-spawning terminals), Cmux SSH for remote work, and encourages feedback via email. Jeffrey endorses tmux as a power user.

**[13:07] Sandbox and Model Selection Q&A**
A participant asks about sandbox usage and token concerns. Jeffrey clarifies two types of "sandbox": Docker isolation vs. his staging environment (running a second Open Claw instance). The latter increases token usage but enables local development with integration testing on staging before production deployment. On models: he uses Codex 53 as the default orchestrator (finding GPT 54 consumes more tokens) and switches to MiniMax when budget runs low — a financial rather than preference-driven choice.

## Notable Quotes
- "I actually think an agent could replace me. So that's kind of what I'm working on right now to get things even more autonomous." [02:38]
- "When Open Claw makes a decision, I want that context to be more about the spec or the goals or the history of what I want in the task rather than the code." [05:14]
- "As soon as you open up Claude, it reads CLAUDE.md, it reads skills, it reads MCPs. A lot of those things are sort of independent of the actual task." [05:46]
- "When I code with these directly, I usually feel like there's a bias, where it wants to say things are really working. Versus the manager has a different context than the workers." [10:01]

## People, Tools & References Mentioned
- **Open Claw** — AI agent orchestration framework
- **Claude Code** — Anthropic's coding agent (runs within Open Claw workers)
- **tmux / Cmux** — Terminal multiplexer; Austin (creator) mentioned new features including Cloud Code Teams integration and Cmux SSH
- **Agent Orchestrator** — Open-source framework Jeffrey forked for managing worker agents
- **Git work trees** — Used for parallelization across multiple agents
- **MCP (Model Context Protocol)** — Referenced as context-consuming integration layer
- **Codex 53** — Default orchestrator model
- **GPT 54** — Noted as consuming more tokens
- **MiniMax** — Budget fallback model
- **Docker** — Mentioned in context of sandbox isolation
- **Tailscale** — Referenced for SSH networking
- **Mac minis** — Mentioned as potential hosts for Open Claw instances
- **Skeptic Agent** — Jeffrey's custom code review tool, used as an example throughout

## Who Should Watch
AI engineers and developers interested in multi-agent orchestration workflows, particularly those exploring how to separate planning/specification from code execution using Open Claw, tmux, and Claude Code. The talk is most valuable for practitioners seeking practical patterns for parallelizing AI-assisted development and reducing context pollution in agent interactions.


<details class="transcript">
<summary>Full transcript</summary>

<p>workshop setup, so um there are some people who kind of have like never installed open claw, and I want to kind of get them set up. And then the other people like want to try an experimental thing, which I haven&#x27;t even fully gotten working, but I think for more advanced people that&#x27;ll be cool um to get like a sort of staging environment and run two open claws. So, I think if I&#x27;m not, you know, too busy helping new people set up, then I&#x27;ll try to help people like finish debugging the last part, or maybe someone else will get it.</p>
<p>get it. And I think uh 10 minutes Q&amp;A, 10 minutes some more advanced topics, and then just more Q&amp;A. And uh probably after every 5 minutes or so, we can do a bit of a few minutes of discussion. So, I&#x27;ll just set some timers to make sure I don&#x27;t go off track. All right. Let me start.</p>
<p>All right. Can everyone see this presentation?</p>
<p>Yes.</p>
<p>All right, cool.</p>
<p>Yeah.</p>
<p>So, this kind of describes like my setup. Um I&#x27;ll just keep it really high level for this part where when everything works, you know, maybe like 70% of the time, you describe your task. And then what&#x27;s nice is open claw will have like context and memory about what you&#x27;re talking about. So, for example, like let&#x27;s say I&#x27;m</p>
<p>So, for example, like let&#x27;s say I&#x27;m like, &quot;All right, fix this thing.&quot; It&#x27;s a very brief Slack message, but open claw can remember like what I&#x27;ve asked it to do before. So, for example, I&#x27;m working on this thing I&#x27;m calling a skeptic agent, and it&#x27;s a custom code review thing. But if I&#x27;m like, &quot;All right, fix the skeptic agent.&quot; or whatever, right? It kind of knows what that is, which is nice. You don&#x27;t have to re-explain a lot. Um I use multiple agents with work trees, that&#x27;s very key for parallelization. Uh, CI code</p>
<p>good integration. But you can kind of see you can talk to it and be pretty brief and then, you know, usually get reasonable outcomes, but sometimes you&#x27;ll have to debug it. So, then it&#x27;s like, all right, there&#x27;s some time out thing. I&#x27;m like, give it a longer time out, right? And then I asked that here like like uh, you know, what are the priorities and what we&#x27;re working on. And I&#x27;m reading it here. And then I might have just said like, uh, I just made code for it, right?</p>
<p>I just made code for it, right? So, another interesting thing about this is you can kind of see from like, um,</p>
<p>[clears throat]</p>
<p>the types of responses I give, they&#x27;re not that like, um, special. As in I I actually think an agent could replace me. So, that&#x27;s kind of what I&#x27;m working on right now to like get things even more autonomous. You know, and you and you&#x27;ll see this with LLMs like you&#x27;re working with them and they&#x27;ll be like, &quot;Hey, I&#x27;ve got this thing ready.&quot; And I&#x27;m like, &quot;Okay, we&#x27;ll run the test, right?&quot; Uh, all right. So, I&#x27;ll share the next</p>
<p>Uh, all right. So, I&#x27;ll share the next slide now. Oops. Okay. We&#x27;re going to some concepts right now. Like, what is Open Claw? So, I think what&#x27;s cool about Open Claw is it&#x27;s not just about a particular repo or the code, but more of the concept. So, you know, I&#x27;ve got this cool super diagram, but first concept is frictionless communication. So, I know we have other things like Claude co-work or whatever, but I think</p>
<p>Claude co-work or whatever, but I think they still have a similar concept where it&#x27;s like, can you like easily talk to your AI versus like you&#x27;ve got a, um, remote desktop into your computer or you have to go sit down. So, that kind of enables certain really higher level of velocity. Um then I think the central axis is very important. So, you know, there&#x27;s a spectrum like I kind of go like a little more cowboy and I give it act.</p>
<p>Open Claw has these agent orchestrator managers that manage your workers for you. Uh or sometimes when I want more personal control, I use tmux terminals. So tmux is like a terminal program, but it&#x27;s pretty good for parallelization and AI development. Then I use the open source framework that I forked agent orchestrator to do the workers. And then once it gets to here, this part is like not really controlled by me as much anymore. Um so, I&#x27;m calling them managed agents, but basically like</p>
<p>basically like you have a worker that runs Claude code and Claude code itself can run agents and those can have sub agents. So once you get to this Claude code part, right? This part is not exactly my stack, just stuff I use, but this part of the stack I&#x27;m changing a lot more. Um I&#x27;ll pause here to see if anyone has any questions or thoughts.</p>
<p>Um can you hear me? So I I have a question. So the the real question is, you know, why why use Open Claw versus</p>
<p>why use Open Claw versus directly use Claude?</p>
<p>So yeah, that&#x27;s that&#x27;s definitely a good question. Um</p>
<p>[clears throat]</p>
<p>The reason I use Open Claw as specialization. So when Open Claw makes a decision, I want that context to be more about like the spec or the goals or like the history of what I want in the task rather than the code. And you can just imagine this, right? As soon as you open up Claude, it reads Claude MDs, it reads skills, it reads um MCPs.</p>
<p>MCPs. A lot of those things are sort of independent of like the actual task. It&#x27;s more about how to do the task. Um so imagine like 25% of your context already taken up by implementation. Versus like when you think about open claw, you&#x27;re like, okay. I want to think about exactly what I want to do and how it relates to all the other slacks Jeffrey sent me in the last 2 weeks and put it all together and give me like a reasonable spec. Does every single thing a player does,</p>
<p>Does every single thing a player does, but it does it without a browser, right? So you could use MCP, which usually is JSON or whatever or HTTP. Doesn&#x27;t really matter actually. And then the final thing is the browser test. So some things like are visual. I mean, maybe you could even have CSS tests or JS tests, right? And that kind of goes here. But then the final thing is visual. So I would recommend you like try um similar approaches to this and be like, okay, like which problems truly needed that human or not. Um and I think what&#x27;s kind of cool is like</p>
<p>like every quarter or you maybe even every month like it improves. So before like I had to really manually test a lot because like you know, this worked fine, right? But these things didn&#x27;t work that well with agents like last year but like a year ago even 6 months ago. But now like um agents are pretty good at like nailing down a lot of browser tests for me. Versus like when I started my agent would have a lot of problems, you know, finding a pop-up and entering a password. Now no problem. Um that was a little long, but does that kind of address the theme of your</p>
<p>kind of address the theme of your question?</p>
<p>Yeah, I think this is good. Good. Thank you.</p>
<p>Okay.</p>
<p>Thank you very</p>
<p>Just just remind me for all these slash commands. I&#x27;ll put um links here instead. All right, cool. Anyone have any other questions related to some of that stuff? All right. If not, I will go here. All right. So, here&#x27;s a two websites that I&#x27;ve built.</p>
<p>[clears throat]</p>
<p>Yeah, while that loads, I&#x27;ll show this one. So, this is like a AI RPG. Um what&#x27;s cool about this is you can I&#x27;ve got a default campaign, for example. Um</p>
<p>[clears throat]</p>
<p>Yeah, pick some options. You&#x27;ve got a avatar. And uh what&#x27;s cool about this is it builds a custom world for you that reacts to you. So, you can like kind of say whatever you want, do whatever you want, you&#x27;ll get a story back. Um the main difference between playing this versus like um you know, you could</p>
<p>this versus like um you know, you could just always go into the Gemini chat or or chat GPT or whatever is that um I have like a D&amp;D system. So, if you play your own like games or novels, like you kind of just win too much. Versus like with this, you&#x27;ll actually do like dice rolls and be like, you know, did the person actually um did you actually succeed in your action or not? All right. So, while this is going, I&#x27;ll also um show this thing. Yeah, so this is funny. Um this website is like a multi-AI</p>
<p>Um this website is like a multi-AI analysis website. Um so, what I found was like whenever I was doing research or or whatever, I would go to multiple models and I&#x27;d be like, what&#x27;s the answer? Then I copy and paste them all. I put them into one model. Um so, pretty simple concept, but this does it for you. So, usually I like these answers better than like asking one model. And I&#x27;m like, okay, how do I do this workshop? So, I can be like, okay, what&#x27;s the status?</p>
<p>Uh what&#x27;s the latest PR now? And um what I like about this is it has that sort of vertical tab type of thing. Cuz when you go horizontal, it&#x27;s really easy to lose track of your tabs. Um but we&#x27;ve got notifications, too. So, when this thing is finished or this is finished and I need to look, it&#x27;ll give me a notification. And I can just focus on clearing the notifications. So, here um the way of using these terminals, usually it&#x27;s more like a manager rather than a coder. Um and it&#x27;s kind of</p>
<p>than a coder. Um and it&#x27;s kind of interesting, but it gives you a certain benefit where I feel I feel like the work is not biased anymore. So, when I when I code with these directly, um I usually feel like there&#x27;s a bias, where it wants to say things are really working or whatever, right? Versus like, you know, um I&#x27;ll show this. Let&#x27;s look. If this had been working on PR 294 by itself, I think it would have been like, &quot;This PR is amazing. Like, we got to merge it, right?&quot; But then this one was like, &quot;No, like, there&#x27;s another PR that</p>
<p>like, &quot;No, like, there&#x27;s another PR that should supersede it, and probably we should just close this PR.&quot; Right? So, that&#x27;s kind of the benefit you get, where the manager has a different context um than the workers.</p>
<p>[snorts]</p>
<p>Uh let&#x27;s see. All right, so this is compacting whatever. So, it will take some time to complete. Don&#x27;t want to wait for it, but when it completes, you see these notifications, and I think my efficiency has improved a lot with tmux. Um I think is Austin or someone from tmux here?</p>
<p>here?</p>
<p>Yeah, here. What&#x27;s up? Go.</p>
<p>Yeah, so Austin is uh</p>
<p>[clears throat]</p>
<p>one of the guys behind tmux. Um you know, big fan of it, and I&#x27;m not I&#x27;m not paid to say this or anything, but big fan of tmux. Uh been using it a lot. I don&#x27;t know, you can spend a minute if you want to talk about anything cool about tmux.</p>
<p>Yeah, so yeah, one of the creators of tmux. Really happy to have Jeff as one of our power users. And also like kind of endorsing it for free. But yeah, lots of uh yeah, lots of things that we&#x27;re</p>
<p>uh yeah, lots of things that we&#x27;re shipping. We shipped a Cloud Code Teams integration. So, if anyone is using Cloud Code Teams and wants to actually see what the salvations are doing, we&#x27;ll automatically spawn terminals for that. We also shipped Cmux SSH. So, if you do any SSH work, you can use our native Cmux SSH to you know, do your tailscale and etc. To other computers. You can even use it to run your own open claw in your Mac minis. But yeah, just one of the creators.</p>
<p>But yeah, just one of the creators. Please feel free to email me if you have anything that you think is a bug or any feedback, feature requests. I&#x27;m always available and yeah, just love seeing people using Cmux and always want to take as much feedback as I can to like get them as get them</p>
<p>Okay, so just download that.</p>
<p>Yeah. They actually have an app too. So, the</p>
<p>They actually have an app too. So, the app might be nice.</p>
<p>Yeah. Okay. And then use that to help me get back in and set set up.</p>
<p>Exactly. Yeah.</p>
<p>Okay. Okay, cool. Thanks.</p>
<p>All right. Is using the sandbox, it should not. Where would you Have you had Have you run into any troubles Aaron about sandbox token usage?</p>
<p>Uh no. I&#x27;m just I&#x27;m not technical at all. I have open claw installed, so I&#x27;m</p>
<p>Okay.</p>
<p>very newbie questions.</p>
<p>No no</p>
<p>No no no bad questions. All good. Yeah. Uh they&#x27;re not the sandbox wouldn&#x27;t do that. I think if if everything&#x27;s working well for you, you know, keep using the sandbox. For me, I just you know, don&#x27;t use a sandbox and so so far nothing bad has happened. But I think if I had an external bot, then I would use a sandbox too.</p>
<p>You changing the model testing a new model like it&#x27;ll go down then I have to figure out how to get it back up again. So I think I want to set up this sandbox because</p>
<p>Oh, sorry. Sorry. Um okay, wait. There&#x27;s two kinds of things. Okay.</p>
<p>two kinds of things. Okay. The sandbox that most people talk about means like they run it in Docker or they like have it running in isolated part of their system. But the other one was the one where I made the staging instructions where I was like oh</p>
<p>Yeah.</p>
<p>Okay. So that could double your token usage if you send the same work to both of them. If you have two of them, right? Um but I think the way I would use it is not like that. Like I think I would do local development and then I would run integration tests on the um sandbox or staging one, right? So</p>
<p>the um sandbox or staging one, right? So I have two of them. And then once like everything&#x27;s good, then I would merge the code and deploy to the production one.</p>
<p>I see.</p>
<p>It wouldn&#x27;t double your usage, but it would definitely increase it. But then the benefit is you might have some more reliability. So</p>
<p>Yeah.</p>
<p>I I made some instructions and I was kind of in the middle of setting it up, but then, you know, it&#x27;s like competing with the other one, so I got to debug it.</p>
<p>Yeah.</p>
<p>But I think, you know, it&#x27;s it&#x27;s worth trying out though. So I had that for more advanced people to give it a give it a try.</p>
<p>Cool. Thanks. What</p>
<p>Or if you&#x27;re not as advanced, if you</p>
<p>Or if you&#x27;re not as advanced, if you want it, you know, you can try it.</p>
<p>Yeah, I&#x27;m definitely going to play around. But what a what model do you use? Like do you have a something that like a default orchestrator model and then you say for this you use</p>
<p>use Codex 53. Um I found I found uh GPT 54 to just use more tokens. Um and even 53 like like I I just get destroyed all the time, right? So I might have to adjust that. Um so basically I use this until</p>
<p>that. Um so basically I use this until like this is getting low and then I just switch to MiniMax, which is not as good, but it kind of gets the job done. And then this is more about money than like preference, but some some work I can still kind of just do um um here. So, I don&#x27;t always have to</p>

</details>
