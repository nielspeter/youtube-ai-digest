---
title: "Anthropic Just Dropped the Biggest Subagent Upgrade Yet"
channel: "Ray Amjad"
video_id: _QGgk9F9CSM
url: https://www.youtube.com/watch?v=_QGgk9F9CSM
published: 2026-04-23T11:42:28+00:00
generated: 2026-07-17T19:27:50+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/_QGgk9F9CSM/hqdefault.jpg
---
# Anthropic Just Dropped the Biggest Subagent Upgrade Yet

[![Anthropic Just Dropped the Biggest Subagent Upgrade Yet](https://i.ytimg.com/vi/_QGgk9F9CSM/hqdefault.jpg)](https://www.youtube.com/watch?v=_QGgk9F9CSM)

[Watch on YouTube](https://www.youtube.com/watch?v=_QGgk9F9CSM) · **Ray Amjad** · 2026-04-23

## TL;DR
Anthropic introduced "forked subagents" for Claude Code, a feature that allows subagents to inherit the full conversation history and nuance of the main session rather than receiving a compressed summary. This enables richer, more context-aware parallel task execution while keeping the main context window clean and leveraging prompt caching to reduce costs.

## Key Takeaways
- **Forked subagents inherit full history:** Unlike standard subagents that receive a compressed summary, forked subagents get the entire prior conversation, preserving nuance and detail.
- **Cost efficiency via prompt caching:** Forked subagents share the same prompt cache as the main session, making the transfer of large conversation histories cheaper.
- **Cleaner main context:** Noisy tool calling and multi-step research can be offloaded to forks, keeping the main session's context window lean for better decision-making.
- **Interactive and parallel:** Forks run in the background, can be monitored, and even accept follow-up messages while running.
- **When to use forks:** Use forked subagents when the accumulated nuance of the main conversation is useful to the subagent; avoid them when prior context could bias the subagent (e.g., code reviews).
- **Built-in features already use forks:** Anthropic has quietly used forked subagents behind features like `/recap`, `/bytheway`, and the auto-dream memory consolidation.
- **Enabling the feature:** Forked subagents can be enabled via an environment variable or by configuring `settings.json` for persistent use.
- **Parallel decision convergence:** You can mix forked and non-forked subagents to compare conclusions from full-context vs. blank-context perspectives.

## Detailed Breakdown

### The Problem with Standard Subagents [00:00](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=0s)
Subagents exist to delegate noisy tool calling into separate context windows, returning only relevant results to the main session. This prevents the main context from filling with unnecessary output, which degrades Claude Code's decision-making. However, standard subagents receive only a compressed summary of the main conversation, which can lose critical nuance.

### Introducing Forked Subagents [01:03](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=63s)
Forked subagents solve the compression problem by inheriting the entire prior conversation history and instructions from the main session. They can continue down a specific path and pass results back. Because they use the same prompt cache as the main session, they are cheaper than re-sending the full history from scratch.

### Real-World Example: Design Variations [02:06](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=126s)
The speaker describes a scenario where they discussed design choices (fonts, colors) with Claude Code, accumulating ~50,000 tokens of nuance. Asking for three parallel design variations with standard subagents compressed this into ~2,000 tokens per subagent, resulting in worse output. Forked subagents preserve the full nuance, leading to better design decisions.

### Existing Features Using Forked Subagents [03:41](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=221s)
Anthropic already uses forked subagents behind the scenes in features like the auto-dream memory consolidation, the `/recap` command, and the `/bytheway` (`/btw`) command. This demonstrates the feature's utility for context-rich background tasks.

### Enabling and Using Forked Subagents [04:12](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=252s)
To enable forked subagents, set an environment variable before launching Claude Code, or add it to your project's `settings.json` for persistent use. Once enabled, the `/fork` command spawns a background agent that inherits the full conversation.

### Example: Parallel Research with Full Context [04:45](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=285s)
The speaker demonstrates asking Claude Code to spawn two forked subagents: one to create a Mermaid diagram of changes made so far, and another to search online (via Exa MCP) to verify the approach. Both forks start with ~180,000 tokens, inheriting the full conversation. The speaker shows how to monitor forks, send follow-up messages (e.g., "use a light theme"), and view results passed back to the main session.

### Use Case: MCP Server Recommendations [06:56](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=416s)
The speaker uses a forked subagent to query their "Agentic Coding School" MCP server, asking it to recommend videos based on the current session. The fork performs noisy tool calls in the background and returns tailored recommendations to the main session without cluttering it.

### Additional Use Cases [08:53](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=533s)
- **Tangent containment:** Forks can handle multi-step side questions without derailing the main conversation.
- **Opposing views:** A fork can explore whether the main conversation's premise is wrong, using full context.
- **Log verification:** Forks can check logs to verify work done so far.
- **Parallel decision convergence:** Combine forked and non-forked subagents to compare conclusions from full-context vs. blank-context perspectives.

### When NOT to Use Forked Subagents [10:07](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=607s)
Code reviews are a common case where forks are counterproductive. A forked subagent would see the code it wrote earlier and be biased toward approving it. A standard subagent with a blank context provides a more objective review.

### Closing and Masterclass Promotion [10:39](https://www.youtube.com/watch?v=_QGgk9F9CSM&t=639s)
The speaker expresses excitement about exploring more use cases and shares them in their Claude Code Masterclass. They promote the lifetime plan (being removed soon), noting it includes access to all future agentic coding classes, with a 14-day money-back guarantee and a refund rate under 0.2%.

## Notable Quotes
- "The whole reason for us to have subagents is so we can delegate any noisy tool calling into a separate context window and only get the most relevant results back into the main session."
- "During this compression, we lost a lot of nuance from the main conversation that would have been handy for the subagent to make better decisions."
- "The key here is to essentially think to yourself, is a nuance of the main conversation so far useful to the subagent? If so, tell it to spin up a forked subagent. If it's not useful and could hinder or bias the subagent anyway, then don't use a forked subagent."
- "By forking, you'd probably get a worse review compared to having a separate subagent do that review instead. Because Claude Code would see the code that it wrote earlier inside of the fork and be like, 'Oh, I wrote that code. Of course it's like good.'"

## People, Tools & References Mentioned
- **Anthropic** — Creator of Claude Code; introduced forked subagents.
- **Claude Code** — The agentic coding tool being discussed.
- **Exa MCP** — An MCP server used for online search within a forked subagent.
- **Mermaid** — Diagramming tool used by a fork to visualize changes.
- **`/recap`, `/bytheway` (`/btw`), `/fork`, `/rewind`** — Claude Code commands leveraging or related to forked subagents.
- **Auto-dream feature** — Anthropic's memory consolidation feature that uses forked subagents.
- **Agentic Coding School MCP** — The speaker's MCP server for recommending course videos.
- **Claude Code Masterclass** — The speaker's comprehensive course; lifetime plan being discontinued.
- **`settings.json`** — Project configuration file for persistently enabling forked subagents.

## Who Should Watch
Developers and power users of Claude Code who want to optimize their agentic workflows by leveraging full-context parallel task execution. This video is especially valuable for those doing complex, multi-step work where conversation nuance is critical to subagent output quality.


<details class="transcript">
<summary>Full transcript</summary>

<p>Okay, so yesterday Anthropic solved what I found to be the biggest problem with Claude Code subagents, and that is by introducing this new feature called forked subagents. And I&#x27;ll be going through exactly what this means and how you can be leveraging this to improve your own workflows. So just to make sure that we&#x27;re all on the same page, the whole reason for us to have subagents is so we can delegate any noisy tool calling into a separate context window and only get the most relevant results back into the main session. So if you were to do everything inside of the main session, it would fill up with a bunch of random</p>
<p>noise and like output that Claude Code did not need. And that would lead you to use your context window of the main session faster. And we know that as a context window fills up, then Claude Code makes worse decisions. So to keep our context window lean, we usually delegate to subagents like Explore subagents to look through the codebase or research subagent to search online, which once it is done, will return the most relevant things back into the main session. And whilst in this example, it happens at the start of the conversation, it can also happen in the middle of the conversation. So your main Claude Code session may</p>
<p>be doing some stuff. It then decides it needs to call a subagent, and then a summary of everything that the main session has done so far alongside instructions will be passed over to that subagent. It will then do whatever it needs to do, and that result will be passed back into the main session. Now, this can be handy in many situations whereby that blank context was helpful for Claude Code to get a different perspective. But in many situations, you actually want everything that you&#x27;ve accumulated so far in the main conversation to also go over to the subagent. And that is what forked subagents allow you to do. So</p>
<p>the forked subagent has the entire prior history of the main conversation and instructions as well. And then that can basically continue down a certain path and then pass that result back over into the main session. And one of the benefits here is that when you are using a forked subagent, it will be using the same prompt cache as well as the main session, which means that it can be cheaper. So essentially the main difference between normal subagents and forked subagents is that forked subagents inherit the entire conversation history. Of the main session. Okay, so before going over how you can actually use the</p>
<p>feature, I&#x27;ll go over a recent situation in which this would have been handy for me. So essentially before forked subagents, there were instances where I would be doing some kind of design work with Claude Code and I would basically chat with Claude Code back and forth of, hey, we&#x27;re gonna choose these fonts, like what colors do you think are handy and so forth. And this main conversation would accumulate a lot of nuance and nuance is a key word here. And then I would say to Claude Code, okay, let&#x27;s design 3 different variations of this in parallel with subagents. So it&#x27;s faster and the variations remain isolated from</p>
<p>one another so they&#x27;re not biased by one another. And Claude Code would then essentially give a summary of everything we&#x27;ve done so far with instructions over to 3 different subagents. They would do the design and then give it back to me, like 3 different HTML webpages, for example. And the main problem is that these 50,000 tokens I&#x27;ve accumulated so far in the main conversation to come up with some kind of design has now been compressed into 2,000-ish tokens for the prompt of each subagent. And this was like too much compression for me, and it actually meant the subagents did a worse job because they couldn&#x27;t remember all</p>
<p>the details that we had talked about so far in the conversation. So essentially, during this compression, we lost a lot of nuance from the main conversation that would have been handy for the subagent to make better decisions. But now with the brand new forked subagent, I can then use all the nuance that we&#x27;ve accumulated so far in the main conversation have each of the subagents keep that in mind when designing each variation. And the fact that for each forked subagent, it will be using the same prompt cache as a main session means that it won&#x27;t be that much more expensive to send all that history again and over time.</p>
<p>Now Anthropic have been using this idea of forked subagents inside of the recent new features that they added. So for example, my video about the Claude Code auto-dream feature, they also use forked subagents to do the memory consolidation. I&#x27;d recommend watching that video as well. And it&#x27;s also used inside of the recent recap feature inside of Claude Code. This is using a forked subagent behind the scenes. So doing /recap, that will trigger a forked subagent. Doing /bytheway, /btw, which I made a previous video about, also uses</p>
<p>a forked subagent behind the scenes. Okay, so let&#x27;s go ahead and use this feature. So we have to make sure we have this environment variable set inside of Claude Code. So we can either copy that over, go back to Claude Code, and then paste that in into our terminal and then run Claude kind of like this. And that will enable the fork subagent. And you can see that in action because if I do /fork, then it will say fork spawn a background agent that inherits the full conversation. Alternatively, you can go to your settings.json for your project and put this in at the very top so that if you were to run Claude normally, then</p>
<p>that would be enabled for every session going forwards. So doing /fork, you can see that in action again. Okay, now let&#x27;s go for a few examples. So in this project, I was adding some pre-warming for connections so that when the connection is needed, it would happen faster. And I basically don&#x27;t know if the premise here is correct and I want to know what changes have happened so far. So I can tell Claude Code, hey, can you spawn up two forked subagents? One of them should make a Mermaid diagram of all the changes that we made so far and another one should search online with the Exa MCP to check if everything we&#x27;ve done so</p>
<p>far is correct. So pressing enter, these two forked subagents will inherit the entire previous conversation, have all of that context and nuance, and it can lead to a better decision. And it also keeps a main conversation clean as well, because we don&#x27;t need all this information of generating a Mermaid diagram in the main conversation. That can just go over to a forked conversation. It can like use all the context so far to make one and then pass in the URL back into the main conversation. So I can actually see these two forks running right now at the very bottom. And how many tokens they&#x27;re using. And you can see they</p>
<p>immediately started out with about 180,000 tokens, which is how much I used in this conversation so far. So if I click on this one, I can see what this fork is doing. See what this fork is doing. Going up, I can go back to the main conversation. So this is really handy because then I can give a fork a follow-up question as well. I can press Escape, go over to the text input over here, and then give that fork an additional like prompt. So I can say, use a light theme instead, press enter. And that would go over to that fork with that message</p>
<p>queued. So this kind of feels like agent teams in Claude Code, if you are aware of that. So our verification fork is done and it passed this information back into main session. And this information is much richer and like more nuanced because the fork had the nuance that we accumulated so far. And now the Mermaid diagram fork is done as well. So I can open up this. And then see the light theme mermaid diagram that it made me over here. So the key here is to essentially think to yourself, is a nuance of the main conversation so far useful to the subagent? If so, tell it to spin up a forked subagent. If it&#x27;s not</p>
<p>useful and could hinder or bias the subagent anyway, then don&#x27;t use a forked subagent. Now another pretty interesting use case is for my Claude Code Masterclass, which is the most comprehensive Claude Code class that you will find on the internet. By the way, I will be removing the lifetime plan for the masterclass at the end of the week. So if you want to buy the lifetime plan before it disappears, then now is a chance to do so. There is a discount as well if you are interested. And you&#x27;re probably thinking, why would I buy the lifetime plan if in one year from now, I don&#x27;t know if we&#x27;ll still be using</p>
<p>Claude Code? And that is a point because like a year from now, there will likely be a better tool available, in which case I will make a class about that as well. And you will get lifetime access to all future Agentic Coding classes that I make. Now my class also has a MCP server, which is a really good use case for forked subagents. So if you add like the MCP server to Claude Code, I can basically tell Claude Code, with a forked subagent, can you use the Agentic Coding School MCP and recommend me any videos to watch that you think would be</p>
<p>most helpful based on the session that we&#x27;ve just done together? Pressing enter, Claude Code will use all the nuance and detail of the current conversation with a forked subagent. It will do all the noisy tool calling in the fork to gather all that information and then just return that back to the main session. So we can see this fork in action by going down, pressing enter on this. It&#x27;s doing all the noisy tool calling inside of the fork, and then it will pass those recommendations back into the main session. So you can see Claude Code now recommended me some videos from my masterclass. Based on this session that I</p>
<p>haven&#x27;t seen yet and why they would be helpful. So yeah, a lot of people have found this MCP server helpful to help them decide what they should watch next inside of the class. Now to quickly go over some other use cases, you may want to use this for some kind of tangent containment. So a fork can do multi-steps. So if you use /bytheway, that is a single-step turn, whereas a fork is a multi-step turn and it can use tool calls, like MCP servers, for example. So you can ask side questions without derailing the main conversation. And if you get</p>
<p>an answer back and you don&#x27;t think the answer is helpful, then of course you can do /rewind to go back to before you spun up that fork. It can also be handy to do things like considering an opposing view with all the context so far. So you could do something like getting a forked subagent to explore if the premise that you have in the main conversation is wrong. So the fork would take the opposite of our working assumption. Like I showed as well, we can use it for any noisy tool calls. So any like throwaway research. And if you don&#x27;t find the outcome of that research to be helpful, we can rewind the conversation. We could also be</p>
<p>like, okay, can you actually check the logs inside of a fork to verify everything we&#x27;ve done so far? Another interesting approach that I will be trying more of is parallel decision convergence. So what if you combined forks and non-forks in interesting ways to kind of see where they would agree and disagree. So you can actually do this as well because I just asked Claude Code, can you spin up two subagents to do further research? One should be a fork and one should not be a fork. So you can see at the bottom here, one of them is a fork because it already has 200,000 tokens so far. And one of them is not a fork</p>
<p>because it only has 35. And I can check up on each of them to actually see what they are doing behind the scenes. And a pretty common situation for not wanting to use a fork would be for a code review of sorts. Because by forking, you&#x27;d probably get a worse review compared to having a separate subagent do that review instead. Because Claude Code would see the code that it wrote earlier inside of the fork and be like, &quot;Oh, I wrote that code. Of course it&#x27;s like good.&quot; So it wouldn&#x27;t do as detailed of a review compared to having a review done inside of a blank subagent. Anyways, I&#x27;m really excited by the feature and</p>
<p>I will be playing around with it much more and trying to find more interesting ways of using it to get better results. And I will be sharing all of that inside of my Claude Code Masterclass as I discover those use cases. So if you do want to take advantage of the lifetime offer before it is removed, then there will be a link down below. There&#x27;s also a 14-day money-back guarantee if you&#x27;re not satisfied for whatever reason, but I&#x27;m sure that you will be satisfied because so far less than 0.2% of people have asked for a refund. Anyways, there will be a link down below if you&#x27;re interested, and if you want to email me about it and ask me any more questions, there will be my email down below as well.</p>

</details>
