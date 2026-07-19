---
title: "Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua"
channel: "AI Engineer"
video_id: ZSQb5fzRFPw
url: https://www.youtube.com/watch?v=ZSQb5fzRFPw
published: 2026-07-15T22:45:06+00:00
generated: 2026-07-15T23:10:41+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/ZSQb5fzRFPw/hqdefault.jpg
---
# Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua

[![Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](https://i.ytimg.com/vi/ZSQb5fzRFPw/hqdefault.jpg)](https://www.youtube.com/watch?v=ZSQb5fzRFPw)

[Watch on YouTube](https://www.youtube.com/watch?v=ZSQb5fzRFPw) · **AI Engineer** · 2026-07-15

## TL;DR
Francesco Bonacci and his Cua team present "Computer-Use 2.0," a new paradigm for AI agents that operate in the background without hijacking the user's screen. They introduce three key projects—CU Driver (background control infrastructure), CUA Bench (evaluation framework), and CUA Fleet (GPU-efficient RL training infrastructure)—that together enable more trustworthy, measurable, and cost-effective computer-using agents.

## Key Takeaways
- **Computer-Use 1.0 vs 2.0**: Old agents took over the screen via a screenshot-reason-act loop; the new paradigm runs agents in the background without disrupting the user.
- **CU Driver** works across macOS, Windows, and Linux using undocumented Apple framework APIs, accessibility trees, and pixel-level background clicks.
- **Fallback strategy**: Agents first attempt actions via accessibility trees; if that fails, CU Driver falls back to pixel-level background clicking.
- **CUA Bench** is an evaluation framework with 130+ verifiable tasks across 42 environments and 5 platforms, authored via a single Python file.
- **CUA Bench Kyad**, built with Snorkel AI, tests agents on real electrical engineering software—the top agent passed only 6/25 tasks, with 0% success on blank-schematic tasks.
- **Switching to CU Driver** improved agent pass rates from 62% to 80% while using 34% fewer tokens, primarily by focusing on windows rather than entire desktops.
- **Reward hacking prevention**: Before tasks enter the dataset, a matrix of agents attempts to break the environment; only surviving tasks are admitted.
- **World model measurement**: Every recorded run can be forked at any trajectory point to probe a model's understanding of the computer's state, making "world models" measurable.
- **GPU idle cost problem**: During RL training, GPUs sit idle while waiting for sandboxes to spin up or reset—pure wasted cost.
- **CUA Fleet** uses a demand-based autoscaling warm pool of sandboxes so GPUs maintain full utilization, with infrastructure absorbing startup latency.

## Detailed Breakdown

### Introduction and Vision [00:01](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=1s)
Francesco Bonacci, CEO of Cua, opens the talk alongside his co-founders—CTO Dylan and Chief Infra Officer Rob. He gauges audience familiarity with computer-using agents, noting that a year ago many people didn't know what computer use meant. The team's experience traces back to Microsoft, where they worked on GUI agents.

### Computer-Use 1.0: The Old-Fashioned Loop [01:36](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=96s)
Francesco describes the traditional agent loop: take a screenshot, reason and plan, then execute actions (clicking, typing, scrolling). This "Computer-Use 1.0" approach takes over the user's screen, which is the core limitation the team set out to solve.

### CU Driver: Background Computer Use [03:14](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=194s)
Released as open source roughly two months ago, CU Driver was motivated by Codex releasing their computer-use model. Built over a weekend, it uses undocumented APIs in Apple's framework to let agents operate without taking over the screen. It spans macOS, Windows, and Linux. Agents get a window state snapshot (accessibility tree + screenshot), attempt background execution via the accessibility tree, and fall back to pixel-level background clicks if needed. Francesco notes cross-platform behavior isn't uniform, so CU Driver does "heavy lifting" to normalize the experience. Eight application harnesses are used for regression testing across releases.

### CUA Bench: Measuring Agent Intelligence [06:24](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=384s)
CTO Dylan takes the stage to address trust. CUA Bench tasks consist of three parts: a setup function (initial machine state), an oracle function (golden GUI trajectory), and an evaluator (probes for success). Unlike Terminal Bench, the oracle is GUI actions. The SDK lets anyone author tasks in a single Python file that works across all five targeted desktop platforms. The dataset currently has 130+ verifiable tasks across 42 environments.

### CUA Bench Kyad: Electrical Engineering Benchmark [08:29](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=509s)
Built in collaboration with Snorkel AI, this dataset tests agents on professional electrical engineering software with evaluators that simulate circuits. Results are humbling: the best agent passed only 6/25 tasks, all involving editing existing schematics. Starting from a blank schematic, success dropped to 0%. No model exceeded 30% reward.

### CU Driver Improves Agent Performance [09:04](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=544s)
On the CUA Bench basic dataset at 4K resolution, switching the agent's computer tool from the built-in one to CU Driver raised the pass rate from 62% to 80% while using 34% fewer tokens. The improvement comes from CU Driver focusing on a window rather than the entire desktop.

### Trust Pipeline and World Model Measurement [09:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s)
Before tasks enter the dataset, a matrix of agents attempts reward hacking and environment-breaking. Surviving tasks get a code-review-style report. Dylan also introduces "world model" measurement: any recorded run can be forked at any point in its trajectory, letting researchers probe the model's prediction of reward, internal state, or observations and compare against the actual forked state.

### CUA Fleet: GPU Infrastructure Efficiency [10:47](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=647s)
Rob (Chief Infra Officer) addresses the cost of idle GPUs during RL training. When a sandbox finishes a task, GPUs wait for a new sandbox to spin up or reset—pure wasted cost, especially with large (e.g., 40GB) environments. CUA Fleet solves this with a demand-based autoscaler that maintains a warm pool of sandboxes sized to current GPU demand. The pool size adjusts dynamically over multi-day training runs. Since sandboxes are 2–4x cheaper than GPUs, the redundancy still saves money. Infrastructure absorbs startup latency, keeping GPUs at full utilization. Instant sandboxes are available for Windows, Linux, and Android, with macOS coming.

### Q&A: Android Background Computer Use [15:18](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=918s)
Asked about Android, Francesco explains there's more flexibility than iOS. The team works with the ARM team's harness and can containerize workloads (e.g., Ubuntu or GUI Docker containers) within Android. However, Android background computer use leans more toward tool use than full GUI control, leveraging the activity framework.

## Notable Quotes
- "The trick here is really not having your agents take over your screen." — Francesco Bonacci
- "With CU Driver we gave an agent hands, but then the question becomes how can you trust the agent to use those hands correctly and not leave anything broken behind." — Dylan
- "The results are humbling. The top agent that we tested only got a full pass on six out of 25 of these tasks." — Dylan
- "If you ask us how we trust that agent, the answer is that it's just evals all the way down." — Dylan
- "That prediction is the world model of the agent made measurable." — Dylan
- "You're probably leaving a lot of money on the table with idle GPUs if you do RL training for computer use agents." — Rob

## People, Tools & References Mentioned
- **Francesco Bonacci** — CEO of Cua
- **Dylan** — CTO of Cua
- **Rob** — Chief Infra Officer of Cua
- **CU Driver** — Open-source background computer-use driver
- **CUA Bench** — Evaluation framework for computer-use agents
- **CUA Bench Kyad** — Electrical engineering benchmark (built with Snorkel AI)
- **CUA Fleet** — GPU-efficient RL training infrastructure
- **Snorkel AI** — Collaborator on the Kyad dataset
- **Terminal Bench / Harbor** — Referenced evaluation benchmarks
- **Codex** — Their computer-use model release motivated CU Driver
- **Microsoft** — Where the team originally worked on GUI agents
- **ARM team** — Collaborating on Android harness
- **Early adopters**: Clicky, Mass, Queno, H Company, Droid Factory
- **Platforms**: macOS, Windows, Linux, Android

## Who Should Watch
AI engineers and researchers building or evaluating computer-using agents, especially those focused on background execution, cross-platform GUI automation, RL training infrastructure, or benchmark design. The talk is practical for teams seeking to reduce GPU training costs and improve agent reliability without disrupting end users.


<details class="transcript">
<summary>Full transcript</summary>

<p>Thank you for taking the time for coming over here. Um I&#x27;m Franchesco. I&#x27;m the CEO of the company. Uh alongside me, a couple of other folks. Um my co Dylan and my chief of infra Rob. They&#x27;re going to walk on the stage in a while. Uh but before we do that, who&#x27;s excited for some computer using agent talk happening</p>
<p>some computer using agent talk happening now? Are you guys excited? Lovely. Um if I were to ask like what what was a computer using agent like one year ago, probably half the crowd would say I don&#x27;t have any idea what really computer use mean. Um so um today I&#x27;m going to take you to a journey. Um basically like from our vision where um we come from so far on computer user um like this new shape of like agents are talking um and uh up to model</p>
<p>talking um and uh up to model intelligence um so we&#x27;re going to start like with the vision of uh quad driver where we&#x27;re coming from and uh if you how many of you guys been been working with computer use for one year. How about like two years? Lovely. Okay. So, our team has plenty of experience like we go all the way back uh our time on Microsoft. We were working on this type of guey agents we were calling them uh back in the days.</p>
<p>were calling them uh back in the days. Um and uh there is a um there&#x27;s an example of like old-fashioned human uh agent loop. Um we basically refer um refer this as a human uh loop where you will have like an agent loop. You will have a um uh you will take a screenshot that the agents will have to reason and plan through and then um you will basically work with an action space in terms of like clicking, typing, scrolling around. So this is</p>
<p>typing, scrolling around. So this is what we refer as as um um the old fashioned like computer use 1.0 you know, just to set the tone for for um for this talk and uh we come like a long um a long like way since this type of like um computer using agents. So this is this again like I&#x27;m going to skim over these slides but that&#x27;s like the old fashioned way of like representing these agents loop as a human would do. Um we um</p>
<p>um here we go. Um over like two months ago we released a project in open source. It&#x27;s called quad driver and uh um we um we made it working like in the background. That means that your computer user will will not take over your uh screen as like the computer use 1.0 um kind of like agent loop was doing back in the days. And uh um it all like started from uh um from like uh um from</p>
<p>started from uh um from like uh um from Codex releasing their computer use um model two months ago. So we kind of like take the challenge because we were already like working with this uh this type of background computer user. So over one weekend we act something together. And uh the trick here is really um not like having your agents like take over your screen. So there is a lot of like dark magic like happening behind the wood just to uh give you some context. Uh there are like some undocumented API um living in u um in</p>
<p>undocumented API um living in u um in the Apple framework that basically ships with your laptop and as you can see here like is in the demo you have like an I agent that is not taking over uh control of your over your laptop. Um we made it working not only for Mac OS but also spanning like across Windows and Linux. where uh this is like the very first like driver that is uh living on your um laptop and uh it lets uh really any agents connect to the underlying operating system uh either like using</p>
<p>operating system uh either like using accessibility trees or like a screenshot level approach. We kind of like take all um this is what really the agents see for what it concerns. Um you will have to install quad driver. Um the agents will uh will take a snapshot of the window state and uh you will have to observe um and uh we really like take take like one uh uh like different like action path to really make the ground computer use happening. So you really um</p>
<p>computer use happening. So you really um have um to observe the space in this case just by calling like get window state you get a an accessibility tree representation plus a screenshot and then you will go and uh um try a background execution using accessibility tree and if that doesn&#x27;t work we go all the way and uh make the heavy lifting for you and just try a pixel background click. This is like uh kind of like best step for background at this stage. It&#x27;s not like behaving in</p>
<p>this stage. It&#x27;s not like behaving in the same way Mac OS, Windows and Linux. So uh we we do like some of the lifting for you so that your AI agent can uh can run and disturb on your uh on your MacBook. um how we manage like to not break anything between like release cycles. We have ex we have like a lot of investment happening uh behind the scene uh when we test like new releases. uh we have about like eight different</p>
<p>like eight different uh application harnesses that are um that that that we that we use for making sure that we don&#x27;t break anything uh among different releases. Um among our early adopters you can see like clicky mass queno h company and droid factory. uh like huge thanks to them for using quad driver and like um basically releasing a lot of like upstream contribution back in in our framework. Um without further ado, I&#x27;m</p>
<p>framework. Um without further ado, I&#x27;m just going to move to the next part of the presentation which is going to be intelligence. Um and I&#x27;m going to have our CTO Don cover that.</p>
<p>Hello. So thank you Franchesco. Um with cooler driver we gave an agent hands but then the question becomes how can you trust the agent to use those hands correctly and not leave anything broken behind and to answer that we had to build kuab bench so for a show of hands who here has heard of terminal bench or harbor</p>
<p>heard of terminal bench or harbor yeah so a few few of you have heard of it and uh if you&#x27;ve ever authored a task for terminal bench then this might look familiar but in kuabench a task is made of three pieces the setup setup function which sets up the machine to initial state. The oracle function which provides a golden trajectory for the task and the evaluator which probes the environment to check if the agent successfully completed the task. Uh unlike terminal bench the oracle here is</p>
<p>unlike terminal bench the oracle here is guey actions. So it looks kind of like pile of gooey when you write that and writing environments takes scale and expertise. On desktop there&#x27;s more than uh five platforms that we target and um we try to collapse that into a single Python file. So using the Kubaben SDK you can write a guey that works across every desktop platform in a single Python file and use the same SDK to probe that GUI to get usable agent data. Anyone or any agent can author one of</p>
<p>Anyone or any agent can author one of these tasks and when you put that to work you get a real catalog. We have currently over 130 verifiable tasks, 42 environments, and across five platforms. And each of these are easily reproducible using our CLI. And the latest addition to our data sets is one that we&#x27;re proud of. Uh with collaboration with Snorkel AI, we built KUBench Kyad, which tests computer use agents on electrical engineering tasks using software by real professionals and</p>
<p>using software by real professionals and evaluator functions that actually simulate the circuits. But the results are humbling. The top agent that we tested only got a full pass on six out of 25 of these tasks. Of those six, 100% of them involved editing an existing schematic. And when we start the task from a blank schematic, the success rate drops to 0%. And across all the models that we tested, the leaderboard is flat. No model has achieved more than 30% reward.</p>
<p>But once you can score something, you can improve it. If we take a look at the Kua bench basic data set scaled up to 4K resolution uh testing an agent they typically get around 62% pass rate but when you switch the agent computer tool from the built-in one to KU driver the pass rate jumps from 62% to 80% using 34% less tokens and this is primarily because KU driver focuses on a window rather than the entire desktop but our evals might say you can trust</p>
<p>but our evals might say you can trust model XYZ at task whatever. But how can you know that the task how can you know that the eval can be trusted? So before we test a task against any agent, we first try to break the environment ourselves. We have a matrix of agents attempt to do reward hacking and attempting to break the environment and we take all that data and we compile it into a nice code rabbit style code review and only tasks that survive our pipeline can enter the data set. And if you ask us how we trust that agent, the</p>
<p>you ask us how we trust that agent, the answer is that it&#x27;s just evows all the way down. But to measure the intelligence of an agent, you can&#x27;t just measure its ability to successfully perform actions. You also have to measure its ability to understand the world that it&#x27;s operating in. Every run that we record can be forked through any moment in its trajectory to give you the state of the computer at that moment. From there we can probe a model asking to predict the reward, the internal state or any other observation of the computer and compare</p>
<p>observation of the computer and compare it against the fork. And that prediction is the world model of the agent made measurable. And with that um I&#x27;ll let Robert take the stage.</p>
<p>Thank you Dylan. Uh hello everybody. Uh I am the chief infra officer at Kua and I&#x27;m here to talk to you about um how you&#x27;re probably leaving a lot of money on the table uh with idle GPUs if you do RL training uh for computer use agents. So I kind of want to introduce this uh diagram to</p>
<p>want to introduce this uh diagram to y&#x27;all. Uh could I get like is is there like general familiarity with this diagram or this like something that most of us haven&#x27;t seen before like any anyone? Awesome. Very niche. Um Almost everything on this is not really important for what we&#x27;re talking about, but the blue portions are um and what those basically represent are GPUs uh generating tokens for um RL uh training. And if you zoom in on this a little bit,</p>
<p>And if you zoom in on this a little bit, you can kind of see like how this typically looks like with a sandbox environment is you&#x27;re going to be generating some tokens um and then you finish your task on a sandbox and then you&#x27;re waiting for either like a new sandbox to spin up or for your existing one to reset. Uh the problem here is that like this is just pure cost. um your GPU really isn&#x27;t doing anything useful here and you know I don&#x27;t know if you&#x27;ve heard but GPU time is pretty expensive right now. So um as you&#x27;re</p>
<p>expensive right now. So um as you&#x27;re scaling this cost really compounds a lot and you really want to focus on minimizing this if possible. So one thing that you might try to do is uh minimize the startup time of your sandbox. And I mean you should do that like that&#x27;s a great thing to do but uh you know especially for computer use style environments sometimes this can be a little bit impractical. Um you know your researchers might give you like a 40 gigabyte environment and that might just be necessary and it takes a long</p>
<p>just be necessary and it takes a long time to pull that down and start it up. So you know how do you how do you design your training infrastructure so that you can minimize the GPU startup or the minimize the startup time of the sandbox? uh even when the sandbox is like not well designed to be start up quickly. Um so the way we do the oh man is it not so the way we do this is a pool and this is supposed to be animated but it&#x27;s not</p>
<p>is supposed to be animated but it&#x27;s not animating. So um I guess I&#x27;ll just explain to you orally and what what that is is uh so we have like a a set of GPUs here which all want to use a sandbox and what we will do is that we use a demandbased autoscaler to detect um how many GPUs like currently need a sandbox and we can grow the pool to be that size uh on demand. And what that means is that uh if you have let&#x27;s say like you</p>
<p>that uh if you have let&#x27;s say like you have a warm pool that you want to allocate to your GPU cluster, you don&#x27;t actually need to know upfront what that warm pool size is. We can figure out what that warm pool size should be for you um on demand. And that might even change over the course of your multi-day training run. Uh you might start needing a lot of sandboxes, but then as your generations get longer, you might need less. So these also could be like, you know, easily uh two to four times cheaper than your GPUs. So having a</p>
<p>cheaper than your GPUs. So having a little bit of redundancy here, uh you still wind up saving money because you&#x27;re maximizing the use of your GPU time. Um yeah, come see me after if you want to see the animation because it&#x27;s it&#x27;s cool. Um so yeah so now when you have like this like uh redundancy in your pool you&#x27;re paying the cost of that startup time on the infrastructure side not on the GPU side so your GPU workers have full utilization um yeah and then because we use this we</p>
<p>um yeah and then because we use this we can give you instant sandboxes for your GPUs for Windows Windows Linux Android uh and Mac OS is coming up Um, and I&#x27;m going to hand it back to Franchesco to uh close it out for us.</p>
<p>Lovely. Uh, thank you Don, thank you Rob for taking this over. Um, we do have like plenty of time for Q&amp;A. So if you guys like have any questions like happy to um take them either for quad driver qua bench basically what Dylan presented</p>
<p>qua bench basically what Dylan presented or qua fleet uh which is like what uh Robert covered any questions otherwise we can wrap this up. Oh, I see.</p>
<p>Um, so the story for mobile Android there is very far you can go. Um, we are</p>
<p>there is very far you can go. Um, we are talking with the arm team because they do have like an arness that runs on Android. I guess like if you&#x27;re talking about background there is some level of like background that can happen if you containerize a workload and basically on Android you can even like run your own container or like sort of like Ubuntu or like GUI docker container uh within Android um but yeah the Android ecosystem especially compared to iOS is more inclined to that form of like background uh computer use but it&#x27;s more</p>
<p>background uh computer use but it&#x27;s more towards like tool use than really like controlling GUI interface. Um we work with the activity framework and uh do tool use in the background.</p>
<p>Cool. Thank you guys.</p>

</details>
