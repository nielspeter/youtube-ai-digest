---
title: "\"The best thing since OpenClaw\" (Hermes Tutorial)"
channel: "Matthew Berman"
video_id: TML-0HmxWCE
url: https://www.youtube.com/watch?v=TML-0HmxWCE
published: 2026-06-28T14:00:35+00:00
generated: 2026-07-13T08:43:12+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/TML-0HmxWCE/hqdefault.jpg
---
# "The best thing since OpenClaw" (Hermes Tutorial)

[!["The best thing since OpenClaw" (Hermes Tutorial)](https://i.ytimg.com/vi/TML-0HmxWCE/hqdefault.jpg)](https://www.youtube.com/watch?v=TML-0HmxWCE)

[Watch on YouTube](https://www.youtube.com/watch?v=TML-0HmxWCE) · **Matthew Berman** · 2026-06-28

## TL;DR
Matthew Berman demonstrates how to quickly install and configure Hermes, an AI agent platform he considers the best thing since OpenClaw. Hosted via Hostinger, Hermes stands out with preconfigured skills, self-healing capabilities, scheduled tasks, memory/profiles, extensive model routing, plugins, and easy gateway connections to chat apps like Telegram.

## Key Takeaways
- Hermes can be installed in under 2 minutes through Hostinger's hosted agent platform, requiring only an OpenAI API key to get started.
- Unlike OpenClaw, Hermes comes preconfigured with a large library of skills and plugins out of the box, all toggleable with a click.
- Hermes can self-heal: if a skill runs into an error or missing dependency, it attempts to diagnose and patch the problem automatically.
- Users can install custom skills by copying a `skill.md` file from GitHub and pasting it into Hermes's skills tab.
- A "Tasks" feature lets users create scheduled automations (e.g., a daily calendar brief) that run on recurring intervals.
- Hermes builds memory automatically over time and supports an editable "agent soul" document, similar to OpenClaw's `identity.md` or `soul.md` files.
- Multiple agent profiles can be created to silo different use cases (e.g., a marketing agent vs. a development agent).
- Hermes supports a wide range of inference providers (OpenAI, Anthropic, Deepseek, Gemini, LM Studio, Mistral, Nvidia Nims, etc.) with per-task model routing.
- Built-in plugins like browser use, Firecrawl, Discord, Google Chat, and Google Meet provide end-to-end workflows.
- Connecting Hermes to Telegram (or Slack, WhatsApp, Signal, etc.) is straightforward via the `Hermes gateway setup` command and BotFather.

## Detailed Breakdown

### Quick Install via Hostinger [00:00](https://www.youtube.com/watch?v=TML-0HmxWCE&t=0s)
Berman begins with a speed-install challenge. He walks through signing up for Hermes Agent Hosting on Hostinger, selecting a plan (defaulting to 24 months for maximum savings), applying the promo code "Matthew B" for an extra 10% off, and paying. He then creates an OpenAI API key at platform.openai.com, names it "Hermes-hostinger," copies it, and pastes it into Hostinger. Hostinger handles the rest of the setup automatically, completing the installation in under two minutes.

### Initial Configuration [01:03](https://www.youtube.com/watch?v=TML-0HmxWCE&t=63s)
Berman walks through the Hermes initial setup wizard: skipping provider config (already done), selecting a workspace, and opening Hermes. He tests the agent by switching the default model from GPT-4o to GPT-4 Mini, sends a "hello," and receives a response, confirming everything works.

### Preconfigured Skills [01:34](https://www.youtube.com/watch?v=TML-0HmxWCE&t=94s)
A major differentiator from OpenClaw is Hermes's large library of pre-enabled skills. Berman shows the Skills tab, which includes skills for Claude Code, codec, Asky Art, Asky Video, and Excalidraw diagramming. Each skill is viewable as markdown, and users can toggle them on or off. He highlights the Excalidraw skill as a personal favorite.

### Installing a Custom Skill [02:35](https://www.youtube.com/watch?v=TML-0HmxWCE&t=155s)
Berman demonstrates installing a new skill from GitHub. He finds a "last 30 days" skill, copies the raw `skill.md` file, returns to Hermes, clicks the Skills button, adds a new skill via the plus button, names it, categorizes it as "search," and pastes the markdown. He invokes it in chat using a slash command. When the skill requires additional code that wasn't installed, Hermes self-heals by fetching the skill's repo into a temporary directory and running from there. It also intelligently disambiguates "Hermes" to mean the Hermes agent (not the fashion brand or mythology) based on chat context.

### Self-Healing Capability [04:38](https://www.youtube.com/watch?v=TML-0HmxWCE&t=278s)
Berman emphasizes that if Hermes encounters an unfamiliar error while using a skill, it will investigate the cause and apply a patch to itself. This is designed to make the platform accessible to non-technical users.

### Tasks (Scheduled Automations) [05:09](https://www.youtube.com/watch?v=TML-0HmxWCE&t=309s)
The Tasks feature allows users to create scheduled automations or loops. Berman creates a "daily brief" job that runs every 24 hours with a prompt to review his calendar and summarize each meeting. Output is delivered to the chat window. Skills can optionally be attached to tasks. Saved jobs are listed and run on schedule.

### Memory and Agent Soul [05:40](https://www.youtube.com/watch?v=TML-0HmxWCE&t=340s)
Hermes automatically generates memory about the user over time. Users can also manually add facts. The "agent soul" document—comparable to OpenClaw's `identity.md` or `soul.md`—is editable. Berman adds a pirate-speaking instruction and personal details (name, company, newsletter URL) to the memory, saves it, and the agent adopts that persona immediately.

### Profiles [06:43](https://www.youtube.com/watch?v=TML-0HmxWCE&t=403s)
Profiles allow users to maintain multiple specialized agents (e.g., a marketing agent and a development agent) rather than one bloated agent with all skills enabled. This effectively silos capabilities for different use cases.

### Insights [07:15](https://www.youtube.com/watch?v=TML-0HmxWCE&t=435s)
The Insights tab displays usage metrics including daily token usage, number of messages, and number of sessions. Berman shows his own stats: 73,000 tokens.

### Settings and Model Routing [07:47](https://www.youtube.com/watch?v=TML-0HmxWCE&t=467s)
Hermes supports a broad range of inference providers: OpenAI, Anthropic, Copilot, Deepseek, Gemini, Kimmy, LM Studio (for local inference), Mistral, Nexos, Nouse Portal, and Nvidia Nims. It offers built-in model routing, allowing users to assign specific models to specific tasks (vision, compression, web extraction, session search, approval). Berman leaves everything on "auto" for simplicity.

### Plugins [08:18](https://www.youtube.com/watch?v=TML-0HmxWCE&t=498s)
Plugins are described as end-to-end workflows—more comprehensive than individual skills. Built-in plugins include browser use, Firecrawl (web scraping), Discord, Google Chat, and Google Meet. Users can also build and install their own plugins.

### Connecting to Telegram [08:49](https://www.youtube.com/watch?v=TML-0HmxWCE&t=529s)
Berman demonstrates connecting Hermes to Telegram via the Hostinger command line. He runs `Hermes gateway setup`, selects Telegram from a list of options (Slack, Matrix, Mattermost, WhatsApp, Signal, Email, etc.), and provides a bot token created through Telegram's BotFather (`/newbot`). He retrieves his user ID via the "user infobot," pastes it as an allowed user, sets it as the home channel, and restarts the gateway. He tests the bot in Telegram and it responds—in pirate speak, retaining the earlier memory context.

### Manim Video Demo [10:52](https://www.youtube.com/watch?v=TML-0HmxWCE&t=652s)
Berman showcases a built-in skill called "man video" (referring to Manim, a language for mathematical motion graphics). He prompts Hermes to create a video explaining how exponentials work. Within a couple of minutes, Hermes generates a 58-second animated MP4, which Berman plays back.

### Final Thoughts and Sponsorship Recap [11:24](https://www.youtube.com/watch?v=TML-0HmxWCE&t=684s)
Berman recaps Hermes's strengths: self-healing, preconfigured skills and plugins, extensive configurability, broad provider support, and a 2-minute install via Hostinger. Because it's hosted on an isolated server, there's no need to maintain a dedicated local machine, and the agent only accesses what the user explicitly provides. He thanks Hostinger for sponsoring the video and directs viewers to links below.

## Notable Quotes
- "Self-healing. That is what I'm talking about. Very, very nice."
- "Since Hermes is ambiguous, I'm scoping it to Hermes agent based on this chat context, not the fashion brand or mythology, which is exactly what I was talking about."
- "It is really that easy. Now I can take my Hermes agent anywhere with me on the go."
- "Because it's hosted on Hostinger, I don't have to worry about keeping an isolated laptop or Mac Mini or anything like that. It is on an isolated server, so it won't have access to anything that I haven't explicitly given to it."

## People, Tools & References Mentioned
- **Hermes** — AI agent platform by Nouse Research; the main subject of the video
- **OpenClaw** — Prior agent platform used for comparison
- **Hostinger** — Hosting provider sponsoring the video and offering Hermes Agent Hosting
- **OpenAI** — Inference provider used for the demo (GPT-4 Mini, referred to as GPT 5.4 Mini in the transcript)
- **Anthropic, Copilot, Deepseek, Gemini, Kimmy, LM Studio, Mistral, Nexos, Nouse Portal, Nvidia Nims** — Other supported inference providers
- **Telegram, BotFather, user infobot** — Telegram messaging app and tools used to create and configure the bot gateway
- **Slack, Matrix, Mattermost, WhatsApp, Signal, Email** — Other gateway options
- **Excalidraw** — Diagramming tool with a preinstalled Hermes skill
- **Firecrawl** — Web scraping plugin
- **Manim (referred to as "man video")** — Mathematical animation engine used to generate an explanatory video
- **GitHub** — Source for finding and copying custom skills
- **Forward Future** — Berman's company; newsletter at forwardfuture.ai

## Who Should Watch
This video is ideal for non-technical users and developers alike who want a fast, hosted AI agent platform with rich out-of-the-box functionality and minimal setup friction. It's especially valuable for those interested in comparing Hermes to OpenClaw or who want a self-healing, highly configurable agent that connects easily to messaging apps like Telegram.


<details class="transcript">
<summary>Full transcript</summary>

<p>In this video, I am going to show you how to use Hermes, how to get it set up, why it&#x27;s different from OpenClaw and why everybody seems to be talking about it right now. But first, let me show you how fast we can get it installed. Timer starts now. All right, so I&#x27;m going to drop a link down below where you can get to this page. You get 73% off Hermes Agent Hosting if you use this link. So, please do. So, you&#x27;re going to click choose plan. Come right here. Choose the most popular plan. And if that one fits your needs, click choose plan again. 24</p>
<p>your needs, click choose plan again. 24 months is the default. That&#x27;s how you get the biggest savings. And use code Matthew B for an extra 10% off. And pay. Then you&#x27;re good to go. We&#x27;re going to select our provider. We&#x27;re going to be using OpenAI for this. You&#x27;re going to come to platform.opai.com. You&#x27;re going to click on API keys. We&#x27;re going to create a new API key. We&#x27;re going to call this Hermes-hostinger. Create secret key. We&#x27;re going to copy the key right here. We&#x27;re going to paste it in. And then we&#x27;re going to click next. And now Hostinger literally does</p>
<p>next. And now Hostinger literally does all the work for us. It&#x27;s going to set up Hermes. And that&#x27;s it. We&#x27;re done under 2 minutes. And now we&#x27;re ready to configure it to our needs. All right. So, let me show you how to go through the Hermes initial setup. So, we&#x27;re going to choose provider config. We already did that. We&#x27;re going to leave this blank because we already have a key. We put that in the first step. Continue. Here, we&#x27;re going to select a workspace. Again, you really don&#x27;t need to customize any of this. a password. We&#x27;ll leave that for later. And open Hermes. And so here we go. We have Hermes up and running. Let&#x27;s just test it out to make sure it works. It says</p>
<p>it out to make sure it works. It says GPT40 by default, but we&#x27;re going to go ahead and switch that to GPT 5.4 Mini. Okay. So there we said hello and it says hello back. All right. So there are a few things that really set Hermes apart and make it very different from OpenClaw. The first thing you&#x27;re going to notice is it comes preconfigured with a lot of things out of the box, especially skills. It gives you a ton of different skills. So right here, if we click the skills tab, look at all of these skills that come enabled out of the box. All of these different skills.</p>
<p>the box. All of these different skills. So here&#x27;s a cloud code skill, a codec skill, Hermes agent, we have asy art, Asky video, all of these cool skills. And of course, you can always add more. And you just disable them right here by clicking it off or clicking it back on. So if you click on any of these, you can actually read the full skill just like this. This is just markdown. It is a full skill for claude code. We have one of my favorite skills, the Excaladraw skill, which allows you to create diagrams with Excal very easily. So,</p>
<p>diagrams with Excal very easily. So, here is the skill for that. Very, very useful. So, I want to show you how to install a new skill. I already showed you that Hermes comes with a bunch of pre-installed skills, but of course, you may want to create or install ones of your own. So, you go to GitHub, you find a skill that you really like. You can also just create your own manually, but today I&#x27;m going to show you how to install this last 30 days skill. So, you find the skill.md file within the repo, and you click this little copy raw file button right here. Once you&#x27;ve done</p>
<p>button right here. Once you&#x27;ve done that, you&#x27;re going to switch back over to Hermes. You&#x27;re going to click the skills button over here on the left side. You&#x27;re going to click the plus button right here. We&#x27;re going to name it last 30 days. Category, we&#x27;ll call it search. And you just paste it in here. You click this little check mark up in the top right. And now the skill is created. Now we have access to this skill from Hermes. Let me show you. So to invoke the skill from within Hermes, go to Hermes chat, type slash, and then you get a list of all the skills and slash commands. Type last and then you</p>
<p>slash commands. Type last and then you can see right there last 30 days skill. Research what people are actually saying about any topic. Okay. Hit enter. And we can type in Hermes. And then we&#x27;ll hit enter. And now it&#x27;s going to use that skill for us. It was really that easy. And this skill actually has some code that was required with it that I didn&#x27;t know. And of course, Hermes is good enough to understand that. And it said it right here. The skills instruction file is installed, but it&#x27;s required last 30 days. file is missing. So what did it do? I&#x27;ll fetch a fresh copy of the skill repo into a temporary</p>
<p>the skill repo into a temporary directory and run the engine from there. Self-healing. That is what I&#x27;m talking about. Very, very nice. And look how smart this is. Since Hermes is ambiguous, I&#x27;m scoping it to Hermes agent based on this chat context, not the fashion brand or mythology, which is exactly what I was talking about. Here we go. We have the answer. Hermes agent has a real but still early community pulse mie. And of course, that&#x27;s because I made it talk like a pirate earlier. And this is perfect. Using the skill, I got a bunch of information about Hermes agent. And so, that&#x27;s how you install skills. It is dead simple. The second</p>
<p>skills. It is dead simple. The second thing that makes Hermes very unique is its ability to selfheal. For example, if you&#x27;re using a skill and you run into some error that Hermes hasn&#x27;t seen before, it&#x27;s actually going to go figure out what caused it and apply a patch to itself. It&#x27;s really cool. And again, this is all in the spirit of making it very easy for non-technical people to use this. Next, we have this feature called tasks, which are basically automations or scheduled things. You can call them loops even. And you come in</p>
<p>call them loops even. And you come in here, you give it a name. We&#x27;ll call it a daily brief here. In schedule, you can say every 24 hours. Prompt. This is where obviously you describe what you actually want accomplished. So, look at my calendar for the day. Give me a summary of each meeting I have coming for that day. So, deliver the output locally to basically the chat window. And everything else we can just leave blank. You can also add skills to this if you need it, but we don&#x27;t. So, let&#x27;s go ahead and click save. And the job is created. All of our scheduled jobs are going to be listed here. And this is going to run every 24 hours. Just like</p>
<p>going to run every 24 hours. Just like that. very easy to create a bunch of scheduled automations. All right, next is memory. Hermes starts to generate memory about you over time. It does so automatically. You can also tell it things about yourself. This is also where the agent soul document will be located and you can edit it from right here. If you&#x27;ve worked with OpenClaw, you know it has files like identity.md, soul.md. Those types of files are exactly what you&#x27;re going to find in Hermes. Here it is. So, you&#x27;re a Hermes agent, an intelligent AI assistant created by Nouse Research, etc. So, you can put</p>
<p>Nouse Research, etc. So, you can put anything you want in here. Click the little edit button and you can say, you know, only talk like a pirate. And so, from now on, obviously, we&#x27;ll only talk like a pirate. Now, you can add different parts of your memory. The user&#x27;s name is Matthew Berman and his company is Forward Future. Matthew&#x27;s newsletter can be found at forward future.ai, but seriously, it can be. Go check it out. And so, let&#x27;s hit save. And there we go. Now we&#x27;ve given it memory and it is that easy. Another cool thing it allows you to do is have profiles and this is a way to have</p>
<p>profiles and this is a way to have different agents available at your disposal at any time. So rather than just having a single agent with a single way of running a single set of skills, you can have a bunch. So you can have a marketing agent and you can have a development agent. And so they&#x27;re not just completely bloated agents all the time. You can actually silo them really effectively. Under the insights tab, it tells you how much usage you&#x27;ve been getting out of Hermes, including your token usage, obviously. Here&#x27;s mine. Daily token usage, as you can see right here. Number of tokens, 73,000. Number</p>
<p>here. Number of tokens, 73,000. Number of messages right there. Number of sessions, all of this really useful information that you can see at any time. All right, now let&#x27;s go through settings because another thing that Hermes does incredibly well is just give you all the options. All the options in the whole world. Look at how many providers it has out of the box. obviously OpenAI and Anthropic, but also Copilot, Deepseek, Gemini, Kimmy, LM Studio if you want to run things completely locally. Shout out to LM Studio, Mistral, Nexos, Nouse Portal, Nvidia Nims, just basically every single</p>
<p>Nvidia Nims, just basically every single option you can ever need for inference providers. And what&#x27;s really cool is it has model routing out of the box, very easily set up. So for all of the different tasks that you might need, you can actually set a specific model. Here&#x27;s if you need vision. Here&#x27;s if you need compression, web extraction, session search, approval. And if you click right here, you get a drop down of models that you can select. Now, it&#x27;s only going to be using auto for me across the board. I&#x27;ll let it decide. Again, in the spirit of keeping things as simple as possible. Plugins is also</p>
<p>as simple as possible. Plugins is also something that can be incredibly useful. Very similar to how it has a bunch of skills out of the box. It also has a bunch of plugins. You can think of plugins as more endto-end workflows. Not just a skill, not just a tool, but an entire feature set available to you with one click. So here we have browser use. Here we have fire crawl. So if you want to scrape the web, here&#x27;s a discord plugin, Google chat, Google meet. You can also build your own plugins. You can install your own plugins and it&#x27;s fully</p>
<p>install your own plugins and it&#x27;s fully configurable. All right. And then of course, one of the most important things about OpenClaw was being able to connect it to your chat application. Mine was Telegram. For many, it was Telegram. Others it can be WhatsApp or Slack. And you can do it all with Hermes. Let me show you how easy this is. So from within Hostinger, you&#x27;re going to click right here, open command line. And this is going to open a CLI directly into your Hermes agent. If you&#x27;re not familiar with command lines, it might seem a little scary, but I promise it&#x27;s quite easy. So, all you&#x27;re going to type is Hermes gateway setup. A gateway is</p>
<p>is Hermes gateway setup. A gateway is like Telegram or Slack or any of those systems. So, hit enter and there you go. You have a ton of different options. Telegram, Slack, Matrix, Mattermost, WhatsApp, Signal, Emails, all the way down the list. So many. What we&#x27;re going to do is we&#x27;re going to hit the up arrow. We&#x27;re going to go all the way up to Telegram and we&#x27;re going to hit enter. Now, it&#x27;s going to ask for a Telegram bot token. And the only way to get that is from within Telegram. So you&#x27;re going to search for the user called bot father. This is the official bot from telegram. So you come here and</p>
<p>bot from telegram. So you come here and you&#x27;re going to type / newbot. Then hit enter. How are we going to call it? Let&#x27;s call it Hermes. And then it&#x27;s asking for a username. And the name does have to end in bot. Let&#x27;s try this. There we go. All right. Then we&#x27;re going to paste in our bot token right there. Hit enter. And then it&#x27;s going to ask for allowed user IDs. This just means you or whoever you select are the only ones that are allowed to message your bot, your Hermes agent. To get your user ID, you&#x27;re going to message user infobot. Start a conversation. And there</p>
<p>infobot. Start a conversation. And there we go. Click it. Copy to clipboard. We&#x27;re going to paste it in here. Hit enter. And we&#x27;re going to use it as our home channel. Yes. And then we hit done. Restart the gateway. Yes. And we should be good to go now. So you&#x27;re going to take the bot name. You&#x27;re gonna search for it. Click it. Start. And let&#x27;s just see. Hello. And let&#x27;s see if it types back. And hopefully it talks like a pirate because it still should have that context. Ohoy Matthew. What can I do for you today? There we go. And we&#x27;re done.</p>
<p>you today? There we go. And we&#x27;re done. It is really that easy. Now I can take my Hermes agent anywhere with me on the go. So here&#x27;s a demo of something you can do with Hermes. I&#x27;m going to use the built-in skill man video. Man is a coding language that allows you to create really cool motion graphics and visuals for explaining difficult topics. So man video make a cool video explaining how exponentials work. Hit enter and it is going to use that skill. All right. And there we go. Just a couple minutes later are done. I made you a 58 second animated MP4 explaining</p>
<p>you a 58 second animated MP4 explaining exponentials. Let&#x27;s open it up and watch. So there we go. It&#x27;s showing where the exponential is going. The engine repeated multiplication. So yeah, it&#x27;s just a full graphical way to explain difficult topics. And again, this was completely made by Hermes Agent using the Manom skill powered by GPT 5.5. So self-healing, lots of skills out of the box, plugins out of the box. Plenty of configurability, just making it super easy to bring in your favorite inference provider. Plus, it only took 2</p>
<p>inference provider. Plus, it only took 2 minutes to install with Hostinger. And because it&#x27;s hosted on Hostinger, I don&#x27;t have to worry about keeping an isolated laptop or Mac Mini or anything like that. It is on an isolated server, so it won&#x27;t have access to anything that I haven&#x27;t explicitly given to it. So, thanks to Hostinger for sponsoring this video. Go try out Hermes. I&#x27;m going to drop a link down below. I&#x27;ll also drop a link for Hostinger so you can go get it down below. And thanks again. And if you want to know which model is best to use with Hermes, check out this video right</p>

</details>
