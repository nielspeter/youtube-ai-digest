---
title: "Opus 5 Is Exhausting. Anthropic Reveals The Fix."
channel: "Ray Amjad"
video_id: szjakRcw7V0
url: https://www.youtube.com/watch?v=szjakRcw7V0
published: 2026-08-05T15:37:08+00:00
generated: 2026-08-05T17:53:40+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/szjakRcw7V0/hqdefault.jpg
---
# Opus 5 Is Exhausting. Anthropic Reveals The Fix.

[![Opus 5 Is Exhausting. Anthropic Reveals The Fix.](https://i.ytimg.com/vi/szjakRcw7V0/hqdefault.jpg)](https://www.youtube.com/watch?v=szjakRcw7V0)

[Watch on YouTube](https://www.youtube.com/watch?v=szjakRcw7V0) · **Ray Amjad** · 2026-08-05

## TL;DR
Opus 5's default output has become increasingly verbose, jargon-dense, and confusing to read. The fix, recommended by Anthropic's own Claude Code team, is to use **output styles** — a per-project configuration feature in Claude Code that lets you control how the model communicates, from "explain like I'm 5" to simplified technical English.

## Key Takeaways
- Opus 5's default text output is widely perceived as overly verbose, jargon-heavy, and hard to parse.
- A viral blog post highlighted that reading AI output now feels like "extra effort," with dense, plausible-sounding nonsense.
- The Claude Code team recommends using **output styles** to make output more comprehensible.
- Output styles can be added by pasting a style definition, tagging `@cloud code guide`, and asking Claude to add it.
- Switch styles via `/config` → search "output style" → select the desired one.
- Built-in styles include "explain like I'm 5," a "learning" style (asks you to write code), and an "exploratory/explanatory" style (explains architecture and codebase as it works).
- The Claude Code team has new hires use the exploratory style when onboarding into unfamiliar repos.
- You can use `/branch` to spin off a conversation and experiment with generating multiple alternative output styles.
- One effective custom style is based on **ASD-STE100**, a standard for simplified technical English.
- Output styles persist **per project** via `settings.local.json` in the `.claude` folder, so different projects can use different styles.

## Detailed Breakdown

### The Problem: Opus 5's Confusing Output [00:00](https://www.youtube.com/watch?v=szjakRcw7V0&t=0s)
Ray opens by describing a common frustration: Opus 5's text output is hard to understand. He shares an example where the model produced jargon-dense text ("the corpus is an engine angles come from what you've already ingested") that left him unsure what it meant. He references a viral blog post arguing that reading AI output has become "extra effort" — verbose, dense, and full of plausible nonsense. The author had to look up nearly every word in one Claude response.

### The Recommended Fix: Output Styles [00:30](https://www.youtube.com/watch?v=szjakRcw7V0&t=30s)
Someone from the Claude Code team recommended using **output styles** as the solution. Ray notes he originally covered this feature 8–9 months ago in his agent coding school but hadn't used it much until now. He highlights that Anthropic team members use different styles for different projects, tasks, or even times of day depending on their energy and engagement level — it's not a one-and-done setting.

### How to Set Up an Output Style [01:31](https://www.youtube.com/watch?v=szjakRcw7V0&t=91s)
Ray walks through the setup: copy an output style definition, go to Claude Code, tag `@cloud code guide`, paste the style, and say "add this output style for me." Once added, run `/config`, search for "output style," select one (e.g., "explain like I'm 5"), and press escape. Rewind to a previous message and re-enter the same prompt to see the improved output.

### Built-in Styles: Learning and Exploratory [02:32](https://www.youtube.com/watch?v=szjakRcw7V0&t=152s)
Beyond "explain like I'm 5," there's a **learning** output style that asks you to write code yourself, and an **exploratory/explanatory** style. Ray shares that the Claude Code team has new hires enable the exploratory style (`/config output style equals exploratory`) when joining, so the model explains architecture, language conventions, and codebase structure with every change — helping them learn as they work.

### Experimenting with Custom Styles via /branch [03:04](https://www.youtube.com/watch?v=szjakRcw7V0&t=184s)
Ray emphasizes this isn't one-size-fits-all. When you encounter confusing output, use `/branch` to fork the conversation into a new chat, then ask Claude to generate five alternative output styles and show how the previous output would look in each. He reviews options like "kid mode" (too basic), "Slack DM" (still confusing), and ultimately lands on a style based on **ASD-STE100**, a simplified technical English standard, which produces significantly clearer output.

### Iterating and Refining Your Style [04:07](https://www.youtube.com/watch?v=szjakRcw7V0&t=247s)
Over time you may want to adjust a style — for example, making it more technical if it's too simple. Ray demonstrates tagging `@cloud code guide` and asking it to turn a preferred communication style into a formal output style. He notes you can dial the technical level up or down as your preferences evolve.

### Per-Project Persistence [04:37](https://www.youtube.com/watch?v=szjakRcw7V0&t=277s)
Output styles persist per project. In `settings.local.json` inside the `.claude` folder, each project stores its own active style. Ray shows one project set to "explain like I'm 5" while another is set to the STE100 simplified technical English style — changing one doesn't affect the other. He plans to use the explanatory style for a new agent-sandbox project he's learning, and shorter styles for familiar projects.

### Closing Thoughts and Newsletter [05:08](https://www.youtube.com/watch?v=szjakRcw7V0&t=308s)
Ray predicts that as models' default outputs grow more confusing, using output styles will become increasingly necessary. He encourages viewers to experiment and subscribe, and promotes his email newsletter, which includes free videos from his agent coding school and direct reply access.

## Notable Quotes
- "Reading AI output is extra effort. It's verbose, frequently contains all too plausible nonsense, and it is increasingly jargon dense." — referencing a viral blog post
- "Whenever any new engineer joins our team, we tell them to use the exploratory output style." — Claude Code team member
- "This is something we will need to do more going forwards as models are getting slightly more confusing in their default outputs."

## People, Tools & References Mentioned
- **Claude Code** — Anthropic's coding tool where output styles are configured
- **Opus 5** — The model producing the confusing output discussed
- **`@cloud code guide`** — A tagged resource within Claude Code for adding output styles
- **ASD-STE100** — A simplified technical English standard used as the basis for a custom output style
- **`/config`** — Claude Code command for switching output styles
- **`/branch`** — Claude Code command to fork a conversation
- **`settings.local.json`** — File in the `.claude` folder storing per-project output style settings
- **Viral blog post** on AI output being verbose and jargon-dense (referenced but not named)
- **Ray's Agent Coding School** — His paid course, with a free preview via newsletter signup

## Who Should Watch
Developers and teams using Claude Code with Opus 5 who find the model's output verbose or hard to parse. This video provides a practical, immediately actionable fix — output styles — that can dramatically improve readability and be tailored per project or experience level.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=0s">00:00</a></span> Okay, so one of the biggest problems that you&#x27;ve likely been facing with Opus 5 recently is the fact it&#x27;s really confusing when outputting any text. So for example over here I was chatting about some ideas and it basically said the corpus is an engine angles come from what you&#x27;ve already ingested and I read through a lot of this output and I&#x27;m kind of like what on earth does this even mean? I have no idea. It feels like my English has become weaker or it&#x27;s speaking another language. And I know I&#x27;m not the only one feeling this way because there&#x27;s a pretty recent viral blog post where basically the author</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=30s">00:30</a></span> blog post where basically the author says reading AI output is extra effort. It&#x27;s verbose frequently contains all too plausible nonsense and it is increasingly jargon dense. And recently they got this output from claude which I would not even try reading. And it said I had to look up every single word to make sense of this. And basically the solution that someone from the cloud code team recommended is using output styles. And I actually did make a video about this inside of my Aenta coding school almost like eight nine months ago now back in October when it was released, but I haven&#x27;t really used it</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=61s">01:01</a></span> released, but I haven&#x27;t really used it since. So if I go over to output styles over here, I basically start out the video by saying that this is a feature that I don&#x27;t use much, but it does exist. But I&#x27;ve been using it more and more because this helps get around the fact that Opus 5 is really annoying when it comes to outputting. So I&#x27;m going to quickly go through how we can set this up over here. So this will be down below. So you can literally just copy the text. But she essentially says that she likes to use this after a long day honestly helps so much. And it seems that some of the team members like using different output styles for either different projects, different tasks, or</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=91s">01:31</a></span> different projects, different tasks, or even at different times of the day depending on how tired they&#x27;re feeling or how engaged in the process they want to be. So it&#x27;s not a case of you make one output style, then you set it once. You will be switching back and forth between them over time. So anyways, I&#x27;ll quickly go through how you can set this up. Basically, this will be down below. You can literally just copy the text. Then go over to cloud code. Tag the cloud code guide by doing at@cloud code guide. Paste in the output style and say and say add this output style for me. Press enter and then it will go ahead and do that. And then once it is done,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=122s">02:02</a></span> and do that. And then once it is done, you can do /config inside of cloud code. Search for output style over here and then switch over to explain like M5 and then press escape. And then you can just rewind uh to go back earlier one message and then basically enter in the same prompt again. And then after entering the same prompt again like the explain like five output style it made much more sense. Now you will have noticed there are other output styles as well. So there is a learning output style where it will ask you to write some code yourself. There is also the explanatory output style which I know the cloud code</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=152s">02:32</a></span> output style which I know the cloud code team likes to use because they mentioned it in an interview where they get new hires to basically enable that when they&#x27;re working inside of a brand new repo. Whenever any new engineer joins our team, we tell them to use the exploratory output style. So this is just like /config output style equals exploratory. You run this in quad code or you can ask quad to set this for you. And what it does is anytime Quad will make a change, it&#x27;ll explain to you, hey, here&#x27;s how the architecture works. Here&#x27;s how this language works if you haven&#x27;t used it before. Here&#x27;s how this part of the codebase works. It&#x27;ll explain to you so that you can learn. Now, of course, this is not a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=184s">03:04</a></span> Now, of course, this is not a one-sizefits-all output style. You may want to kind of experiment around and find a better one for your liking. And one way that you can do this is that anytime you come across some really confusing or annoying output, kind of like I have in this chat over here, you can basically do slash branch and then it will branch from the existing conversation onto brand new chats. And then I can basically paste in the existing output style and say, &quot;Hey, so can you basically generate me like five other output styles and how your previous output would look like in that brand new style?&quot; Essentially, my goal here is to find a style of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=215s">03:35</a></span> here is to find a style of communication, which I understand. And now I can see there&#x27;s a bunch of Apple styles. So there is a kid mode which I will not be using. That&#x27;s way too basic. There&#x27;s also the Slack DM over here which looks a bit better. But honestly when I&#x27;m reading for it then it&#x27;s like still pretty confusing. And if you find that doesn&#x27;t work for you then you can ask it to make a output style based on ASD ST 100 which is a language standard which is for simplified technical English. And if I were to basically rewind and then say like, okay, can you explain explain in this instead, then it</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=247s">04:07</a></span> explain explain in this instead, then it will give a much better style. And you may want to adjust this slightly. And if I were to make this into a brand new output style, then I may find over time, actually, I want it to be a bit more technical. And now reading through this, I can be like, okay, wow, this is significantly better. I want to turn this into output style. Tag the cloud code guide and say, turn this into a output style. and I may notice over time like hey I&#x27;m getting more tentacle or something like that in which case I may want to bump up the level of the output style in some way. Now one of the nice built-in features into cloud code is the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=277s">04:37</a></span> built-in features into cloud code is the fact that the output styles persist per project. So you can see for agent stack over here when I go to settings.local.json inside thecloud folder then I have outpost style set to explain like M5. But if I now set the output style for this other project to the ST 100 uh in simple tentacle English, then I can see that the previous project&#x27;s output style has not changed. But this new one over here has changed to ST 100. So this is really good because you can have different output styles for different projects. Anyways, for me personally, I will be</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=308s">05:08</a></span> Anyways, for me personally, I will be using it for different projects, different output styles. So for example, recently I have been working on a new project of building really good agent sandboxes. So I can do /config and set that to explanatory to understand more about agent sandboxes. But for projects I&#x27;m very familiar with I can have it be way shorter instead. Anyways, I would basically recommend playing around because I think this is something we will need to do more going forwards as a models are getting slightly more confusing in their default outputs. Anyways, if you do like this kind of stuff, then do subscribe to the channel and if you do want to get more tips from</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=szjakRcw7V0&amp;t=338s">05:38</a></span> and if you do want to get more tips from me on a regular basis, then do check out my email newsletter. It will be linked down below. By signing up, you will also get access to a bunch of free videos from my agent coding school class as well. And you&#x27;re also welcome to reply to any of the issues and I will try to get back to you as well because I really like hearing from people replying to newsletters.</p>

</details>
