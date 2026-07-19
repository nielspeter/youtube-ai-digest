---
title: "Anthropic Just Dropped the Biggest Subagent Upgrade Yet"
channel: "Ray Amjad"
video_id: i4fMF1pug3w
url: https://www.youtube.com/watch?v=i4fMF1pug3w
published: 2026-06-10T15:00:50+00:00
generated: 2026-07-17T21:05:54+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/i4fMF1pug3w/hqdefault.jpg
---
# Anthropic Just Dropped the Biggest Subagent Upgrade Yet

[![Anthropic Just Dropped the Biggest Subagent Upgrade Yet](https://i.ytimg.com/vi/i4fMF1pug3w/hqdefault.jpg)](https://www.youtube.com/watch?v=i4fMF1pug3w)

[Watch on YouTube](https://www.youtube.com/watch?v=i4fMF1pug3w) · **Ray Amjad** · 2026-06-10

## TL;DR
Anthropic added support for nested subagents in Claude Code, allowing subagents to spawn their own subagents up to five layers deep. This keeps the main context window clean by pushing noisy tool-calling deeper down the chain, enabling more powerful parallel workflows for research, debugging, legal analysis, and skill optimization.

## Key Takeaways
- Nested subagents allow a Claude Code subagent to spawn additional subagents, up to 5 layers deep.
- The core benefit is keeping the main context window lean and high-signal by delegating noisy tool calls away.
- Subagents can now delegate their own noisy exploration, preventing their context from degrading.
- Codex already supported this via a `max_depth` configuration parameter (default of 1).
- Practical use cases include parallel article fact-checking, legal contract blast-radius analysis, and multi-layer debugging.
- You can compare different skills (e.g., code review skills) by running them in separate subagent branches and having Claude Code judge the results.
- A Microsoft paper on skill optimization inspired a workflow where Claude Code iteratively improves skill prompts overnight using nested subagents.
- The presenter optimized the "Spec Developer" skill using Codex and plans to share enhanced skills on GitHub.
- The new "Fable-5" model is expected to be smart enough to use nested subagents autonomously, but manual prompting may still be needed for now.
- The video also promotes the presenter's paid classes, including a new course on running AI agents in loops ("Loopy AI").

## Detailed Breakdown

### Why Subagents Matter [00:00](https://www.youtube.com/watch?v=i4fMF1pug3w&t=0s)
The presenter opens by announcing that Anthropic now supports nested subagents in Claude Code, jokingly claiming credit after tweeting the suggestion. He recaps why subagents exist: agents like Claude Code call many tools, filling the main context window with noise, which degrades decision quality. Delegating noisy tool calls to subagents keeps the main context lean and high-signal.

### The Problem Nested Subagents Solve [01:30](https://www.youtube.com/watch?v=i4fMF1pug3w&t=90s)
Claude Code already delegates noisy work to subagents by default. However, if a subagent itself needs to explore a new path or verify something, doing so inside its own context can make it noisy and ineffective. Nested subagents solve this by letting a subagent spawn another subagent, keeping each layer's context clean.

### How Nesting Works, Up to 5 Layers Deep [02:00](https://www.youtube.com/watch?v=i4fMF1pug3w&t=120s)
A level 1 subagent can delegate to a level 2 subagent, which can delegate to level 3, and so on, up to 5 layers. Results bubble back up: level 2 returns to level 1, which returns to the main session. The presenter notes that powerful models like the new "Fable-5" may eventually do this automatically, but for now manual prompting or overriding may be needed.

### Codex Already Supported This [03:07](https://www.youtube.com/watch?v=i4fMF1pug3w&t=187s)
The Codex app has supported nested subagents for a while via a `max_depth` parameter in its config file, defaulting to 1. Adding the right line under the agents section enables deeper nesting.

### Use Case: Parallel Article Fact-Checking [03:50](https://www.youtube.com/watch?v=i4fMF1pug3w&t=230s)
One practical workflow is loading a folder of articles, assigning one subagent per article to extract major claims, and then having each of those spawn layer 2 subagents to verify claims by searching online or through a knowledge base. This runs in parallel across all articles, keeping noisy research out of the main context.

### Use Case: Legal Contract Blast-Radius Analysis [05:00](https://www.youtube.com/watch?v=i4fMF1pug3w&t=300s)
For legal work with multiple contracts, a layer 1 subagent per contract considers implications of a goal. Layer 2 subagents measure the "blast radius"—what else needs to change—potentially searching emails or past correspondence. If online verification is needed, a layer 3 agent can handle that. This enables second- and third-order effect analysis in parallel.

### Use Case: Multi-Layer Debugging [06:13](https://www.youtube.com/watch?v=i4fMF1pug3w&t=373s)
In a debugging flow, a layer 1 agent loads a new incident and identifies potential causes. Layer 2 agents fan out to search the codebase in parallel, and one may delegate to a layer 3 agent to cross-check server logs. This helps uncover deeper underlying problems that a single-context approach might miss, while barely consuming the main context window.

### Prompting for Nested Behavior Today [07:20](https://www.youtube.com/watch?v=i4fMF1pug3w&t=440s)
Models haven't yet fully reached the point where they automatically spawn nested subagents. Users may need to design prompts or skills explicitly to trigger this behavior until reinforcement learning environments catch up.

### Course Promotion: Loopy AI and Classes [07:30](https://www.youtube.com/watch?v=i4fMF1pug3w&t=450s)
The presenter promotes his paid classes, currently at a 30% discount, including a new "Loopy AI" course about running AI agents in loops. Subscribers get access to nearly 300 videos, a 30-day money-back guarantee, team discounts, and an MCP server integration that recommends videos based on the user's current project.

### Use Case: Comparing Skills in Parallel [08:40](https://www.youtube.com/watch?v=i4fMF1pug3w&t=520s)
You can load multiple skills that do similar jobs—such as code review—into separate layer 1 subagents, each spawning their own subagents. For example, comparing Cursor's "Thermonuclear Code Quality Review" against Claude Code's built-in `code-review` skill, then asking Claude Code to judge which produced better results.

### Use Case: Iterative Skill Optimization [10:00](https://www.youtube.com/watch?v=i4fMF1pug3w&t=600s)
Inspired by a recent Microsoft paper on automatic skill prompt optimization, the presenter describes running nested subagents to iteratively test and improve a skill overnight. Claude Code writes version 2, runs it, evaluates, and repeats—potentially arriving at a consistently better skill after many iterations.

### Real-World Skill Enhancement and Sharing [11:10](https://www.youtube.com/watch?v=i4fMF1pug3w&t=670s)
The presenter used Codex's nested subagents to optimize the Claude Code team's "Spec Developer" skill, producing an enhanced version he calls "Spec Developer Enhanced." With the new Fable-5 model and nested subagents, he plans to enhance more skills and share them on GitHub. He also mentions a free newsletter linked below.

## Notable Quotes
- "Any important decisions happen early on in the context window when it's lean and high signal."
- "It would be nice if this subagent could also delegate to another subagent if needs be."
- "We kind of have second-order and third-order effects being considered here."
- "Sometimes when it's debugging, it may actually find a problem, but there was actually a deeper underlying problem at play."
- "People have found many of the things that I teach in these classes to be way ahead of the curve."

## People, Tools & References Mentioned
- **Anthropic** — added nested subagent support to Claude Code
- **Claude Code** — the primary coding agent discussed
- **Codex** — already supported nested subagents via `max_depth` config
- **Fable-5** — new model expected to use nested subagents more autonomously
- **Cursor team's "Thermonuclear Code Quality Review"** — a code review skill
- **Claude Code's built-in `code-review` skill** — compared against the Cursor skill
- **Microsoft paper on skill optimization** — referenced for iterative skill improvement
- **Spec Developer skill** — by the Claude Code team; enhanced by the presenter
- **Loopy AI** — the presenter's upcoming course on running AI agents in loops
- **Ray Amjad's classes and newsletter** — promoted throughout the video

## Who Should Watch
Developers and AI power users who work with Claude Code or Codex and want to design more advanced, multi-layered agent workflows. It's especially useful for those interested in parallel research, debugging, or iterative skill optimization using nested subagents.


<details class="transcript">
<summary>Full transcript</summary>

<p>Okay, so Claude Code subagents became even more powerful yesterday because Anthropic added the support for nested subagents. Now I will actually take credit for this feature because I did send a tweet, &quot;Can you allow Claude Code subagents to spawn up other subagents?&quot; And they did like the tweet. So joking aside, basically I want to talk about what exactly this feature means and how you can leverage it to level up your own workflows. Now, just to make sure that we&#x27;re all on the same page, let&#x27;s quickly go over why we even need subagents to begin with. So basically</p>
<p>agents like Claude Code really like calling tools and they will call a lot of tools inside of the main context window. Now this can be quite bad because as a context window fills up, then it can make worse decisions overall and we may run out of context. So when it comes time to like editing or running bash commands, it may make worse decisions about what to edit and what edits it should make. But if we delegate everything over here on the left-hand side, into a subagent instead, and then tell the subagent to return only the most relevant results back to the main session, then we</p>
<p>will get much better outputs because any important decisions happen early on in the context window when it&#x27;s lean and high signal. So essentially any kind of noisy tool calling that may or may not return the result that we are looking for can be delegated into a separate context window that can either be thrown away or resumed later. So this can be any kind of really noisy tool calling. Like exploring the codebase or searching online or doing any kind of verification inside of a subagent by using like Claude in Chrome, for example, or another browser MCP tool. Now</p>
<p>you will find Claude Code doing this by default, delegating any noisy tool calling to subagent. But now the question becomes, what if this subagent decided that it also needed to delegate noisy tool calling because it was kind of changing paths or considering another idea? If it did it inside of a subagent&#x27;s context window, then that subagent could become even noisier and not actually lead to any useful results back for the main conversation. So it would be nice if this subagent could also delegate to another subagent if needs be. So you can kind of imagine it looks like this, what we</p>
<p>have so far, the main conversation delegating to a subagent with a tool call. It does a bunch more stuff over here, and then that result is passed back into main conversation. Now, if we take this one step further, it would look kind of like this. So we would have a level 1 subagent, which is one layer deep, and then that may decide, Okay, like maybe I should check online whether this library actually makes sense for this project or there&#x27;s no bug in the library itself. It could then delegate to another subagent that is another layer deep over here to do that task, and then</p>
<p>it could continue working whilst that task is in action. And then that result will be passed back into the Level 1 subagent once it is complete, and then that is passed back into the main session. So our Level 1 subagent will be even clearer in its final results. Now, of course, this can continue and continue up until it&#x27;s 5 layers deep. And ideally, if you&#x27;re using a really powerful model that is aware of these capabilities, like the brand new Fable-5 model, then you won&#x27;t really have to worry about this because ideally the model will be smart enough to know that it can</p>
<p>make these decisions itself. But it may still take a while for the newer models to reach their full potential in being able to use nested subagents. So you may want to manually prompt it or manually override it. Now it is quickly worth mentioning the Codex app has supported nested subagents for a while because they have a parameter that you can set, which is max_depth. And this is default to 1. So for example, if you went over to Codex and then you went over to configuration, open up the config file and then scroll down. If you add a line kind of like this to your config underneath agents in</p>
<p>Codex, your agents will be able to call other agents inside of themselves. Now overall, this can be pretty easy to understand, but you may be wondering, okay, what are some practical workflows or use cases here? Now, a lot of people in their replies to the official announcement tweet were also wondering the same thing as well. Now let&#x27;s quickly go through some examples so you can get used to thinking in this brand new way. Now you may have some kind of research flow whereby you have a folder of articles and you may tell Claude Code, hey, can you like load in all these articles</p>
<p>one per sub-agent and then verify all those claims that are made, like the biggest claims inside of the articles. So what would happen is you would have your Layer 1 subagent extract claims for like Article 1. So this would be loading Article 1 and this would happen inside of a subagent. It would then identify all the claims. And then for each of the claim that is made that it thinks is important enough, it would then like do some noisy searching either through your knowledge base, searching online and stuff to actually verify that claim. And of course, whilst this one is running,</p>
<p>it would also repeat the same flow in parallel for Article 2, Article 3, and so forth. So it&#x27;ll look kind of like this. So you can see that all our noisy tool calling would be separated into layer 2 and layer 1 would just be receiving verifications of all the big claims. Now, one way that you can also like have this as a mental model in your mind is that you can have it think about second order effects and then carry on to third order effects and so forth. So let&#x27;s say you were kind of like doing some legal work with Claude Code and you had like 10 different</p>
<p>contracts, for example. You may have some kind of result that you want from that legal proceeding. And what you can do is you can pass in All those contracts and then have one subagent per contract consider any implications that would happen to contract if we were to go for that goal. And then we can have inside of layer 2 subagents measuring the blast radius of like if we did change it in that particular way, what else would need to be changed as a result as well? So any kind of like noisy searching from like, I don&#x27;t know, previous emails that you may have exchanged back and forth</p>
<p>and so forth could be delegated into your layer 2 agent. And if during the noisy searching it wanted to verify claim by searching online, it could then do that by also like delegating to a layer 3 agent. So this would happen for like Contract 2 and Contract 3 and so forth, all in parallel. So we kind of have like second order and third order effects being considered here. And by using an approach like this, you may find that for any important work, you uncover more insights than if you just try to do everything inside of one context window or inside of one agent instead.</p>
<p>Now, as for a more technical example, you may have some kind of debugging flow whereby you have a layer 1 agent loading in a brand new incident that just happened. It identifies any potential causes and then it would fan out and verify a bunch of causes in parallel. So these layer 2 subagents would be searching through the codebase to find any relevant things. And then one of the layer 2 ones may decide to delegate to a layer 3 one to also cross-check with the server logs as well. And you may find that this approach ends up being better because sometimes when it&#x27;s debugging,</p>
<p>it may actually find a problem, but there was actually a deeper underlying problem at play. And if you don&#x27;t have the right setup, then it may miss out on the deeper underlying problem. So anyway, all of this would collapse back into the main context window, barely have used up the main context window, and then you can fix the issue inside of the main context window again, rather than starting a brand new one. Now, ideally, as the models get better, because the labs improve the reinforcement learning environments with this in mind, we will notice this behavior automatically emerging when needs be, provided you give your coding agent the right goal. But</p>
<p>you may not notice this behavior emerging right now because the models haven&#x27;t reached that level to like automatically think, okay, I got to spawn another agent inside of this agent. In which case you may want to design your prompts kind of like this, or you may want to design your skills like this as well. Now, if you do like this kind of stuff, then you may want to check out my classes. There is a 30% sale going on right now because I have a brand new class that will be released next week, all about Loopy AI, which is about running AI agents in loops to achieve even better results than you could previously. I have been planning this for the last couple of weeks,</p>
<p>and many of the ideas that will be covered, you will not find covered anywhere else on YouTube. Now, people have found many of the things that I teach in these classes to be way ahead of the curve. They learn ideas that often go mainstream many months later. By signing up, you get access to almost 300 videos that I recorded with brand new videos being added almost every single day. And if for whatever reason you don&#x27;t like it, there is a 30-day money-back guarantee as well. And if you&#x27;re part of a team, then there are bulk discounts for team plans as well. And of course, if you do have any questions about this, then you can always email me using the email you</p>
<p>can see on the screen right now. Now, one of the features that everyone loves about the class is the fact that you can connect it to Claude Code or Codex using the MCP server, and then it will automatically help you find which video videos to watch based on the project you&#x27;re working on and what you&#x27;re struggling with as well. Now, another really good use case here is to compare different skills together. So you could load in a whole bunch of skills that do a similar job and then figure out which one is better for your use case. So for example, we could have Layer 1 loading in Skill A, and Skill A is designed whereby it will spawn up other subagents to explore the</p>
<p>codebase because it&#x27;s like a code review skill, for example. And then in parallel, we could have another layer 1 subagent loading in Skill B, and then that could spawn up their own subagents as well. So for example, you may be checking out the skill, which is Thermonuclear Code Quality Review from the Cursor team. You may install that, and then you may want to compare it against the built-in skill inside of Claude Code for code review. So for example, inside of Claude Code, you could do code review, which is a default built-in code review, do max. And then do &quot;thermonuclear</p>
<p>code quality review in separate subagents.&quot; Press enter. And then each of them can spawn up their own subagents as well. And then you can say, &quot;Hey, what results do you think are better?&quot; And then Claude Code can give you an honest take by comparing these two skills together. Now, another really interesting thing you can do is iterating on skills. So one paper that I really liked recently is this one by Microsoft last month. About skill optimization, whereby you run an auto research to automatically improve the skill prompt and description to try and get even</p>
<p>better results from those skills. And this can be really handy for skills that you run on a daily basis, &#x27;cause you want to make sure that they are as good as they can be. So one way that you can do this is you could have the subagent load in the first version of the skill, and then that would spawn up a whole bunch of new subagents that may be doing some kind of code review or something. And then Claude Code is like, okay, let&#x27;s try and like see if we get different results by editing that skill. So that means Claude Code can then write a version 2 of the skill and then it would run that and it may go overnight or something and then find a really good skill that leads to</p>
<p>consistently good results after like 9 versions, for example. And because of course you are using that particular skill every single day, you may find that to be a really good use of your tokens. So because Codex supported nested subagents first, I had a folder called skill optimization and I optimized one of my favorite skills, which is the Spec Developer skill by the Claude Code team. So this is one of the skills that interviews you about a bunch of things, and I found this to be better than all the other skills out there. And basically I was wondering to myself, okay,</p>
<p>could I make this even better? So I gave it over to Codex at the very beginning. I set a goal and then I just had it continue with the help of nested subagents, and it gave me a pretty good final skill. That I found performing better than the previous one that I&#x27;m basically calling Spec Developer Enhanced. Now with the brand new Fable-5 model and nested subagents, I will be enhancing more my own skills and then slowly sharing it on my GitHub over the coming weeks. So if you want to check that out, that will be linked down below. And if you do want to stay</p>
<p>in the loop of what I&#x27;m doing and learning, then I also have a free newsletter that will be linked down below. And by signing up, you get access to many free videos from the class as well.</p>

</details>
