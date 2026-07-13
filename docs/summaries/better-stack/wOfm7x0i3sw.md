---
title: "Open Source Is Back. Goodbye Claude."
channel: "Better Stack"
video_id: wOfm7x0i3sw
url: https://www.youtube.com/watch?v=wOfm7x0i3sw
published: 2026-07-07T21:00:35+00:00
generated: 2026-07-13T06:52:32+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/wOfm7x0i3sw/hqdefault.jpg
---
# Open Source Is Back. Goodbye Claude.

[![Open Source Is Back. Goodbye Claude.](https://i.ytimg.com/vi/wOfm7x0i3sw/hqdefault.jpg)](https://www.youtube.com/watch?v=wOfm7x0i3sw)

[Watch on YouTube](https://www.youtube.com/watch?v=wOfm7x0i3sw) · **Better Stack** · 2026-07-07

## TL;DR
Open Code is a free, open-source terminal coding agent that rivals Claude Code with a cleaner UI, hundreds of model choices (including free and local options), and powerful custom agent configuration. It wins on cost and flexibility for API-based users, though Anthropic subscription holders may find Claude Code cheaper due to bundled discounts.

## Key Takeaways
- Open Code has surpassed 180,000 GitHub stars and positions itself as a direct, open-source replacement for Claude Code.
- It supports hundreds of models via models.dev, including free, local, and paid options from Google, Anthropic, and OpenAI.
- The terminal UI is notably cleaner than Claude Code's, with built-in tools like bash, edit, grep, web fetch, and web search.
- Agents come in two types: primary (build and plan) and sub-agents (general, explore), with support for fully custom agents.
- Custom agents can be configured via a central JSON file or individual markdown files in a `.opencode/agents` folder.
- GLM 5.2 is highlighted as a cheap, high-quality model that even beat Anthropic's models at web design benchmarks.
- Quality-of-life features include LSP integration, fuzzy file search, undo/redo for agent changes, session sharing, and project convention files.
- Cost comparison isn't straightforward: Open Code wins for API-only users, but Anthropic subscription holders get discounted Claude Code access.
- There's no auto mode for model selection based on task type, unlike some competitors like Copilot.
- The tool is recommended for developers who want flexibility, model choice, and customization without vendor lock-in.

## Detailed Breakdown

**[00:00] Introduction and Overview**
The video introduces Open Code, an open-source coding agent that has crossed 180,000 GitHub stars. It's positioned as a direct replacement for Claude Code, offering access to hundreds of models including free and local options, avoiding vendor lock-in. The host promises a comparison with paid alternatives and a test of whether free and open source holds up for production use.

**[00:31] Terminal UI and Model Flexibility**
Open Code lives in the terminal and includes tools like bash, edit, grep, web fetch, and web search—the same capabilities that made Claude Code useful. The UI is described as clean, demonstrated using the Ghostty terminal. A major differentiator is the ability to bring your own models; by default it uses a free model called "Big Pickle," but users can switch models via the `/models` command or a model picker (Ctrl+I) pulling from models.dev, including GLM 5.2 and DeepSeek 4.

**[01:32] Cost Advantages and Model Performance**
Even with paid models, Open Code can be significantly cheaper than Anthropic's API-only pricing. GLM 5.2 is highlighted as much cheaper than comparable models like "Fable 5" (likely Claude 3.5 Sonnet) and even beat it at web design according to Design Arena. However, there's no auto mode to select models based on task type, a feature found in harnesses like Copilot. Instead, users can configure custom sub-agents to use specific models for specific tasks.

**[02:04] Agent Types: Primary and Sub-Agents**
Open Code features two agent types. Primary agents are top-level and include "build" and "plan," similar to Claude Code or Copilot. Plan mode is for planning large features without making changes; build mode implements them. Sub-agents handle specialist tasks and are invoked automatically based on prompts or manually via the `@` character. Default sub-agents include "general" (for research and multi-step tasks) and "explore" (read-only, for navigating large codebases).

**[03:05] Configuring Custom Agents**
Custom agents can be configured in two ways. The first is via a central JSON config file, where default agents can be modified and new ones added (e.g., a "code review" agent using Claude Sonnet 4). The second method uses a `.opencode/agents` folder with individual markdown files per agent, such as `ui-engineer.md` or `review.md`. These markdown files specify the model, temperature, permissions, mode (sub-agent), and detailed instructions. More detailed instructions reduce hallucinations and improve task accuracy.

**[05:11] Quality-of-Life Features**
Several features improve the Open Code experience. Enabling LSP in the config auto-starts the correct language server per file, giving the model real-time errors rather than just raw text. The `@` character provides fuzzy file search to pull files into context. Undo/redo can reverse agent changes and they stack. The `share` command generates a link to the entire session for debugging or handoff. The `inits` command writes an `agents.md` file (similar to Claude Code's `CLAUDE.md`) that teaches agents project conventions.

**[06:13] Final Verdict and Cost Comparison**
The host's verdict is that Open Code's UI is considerably better than Claude Code's, with the same tools plus model flexibility and custom agent configuration. On cost, it's not black and white: for API-only users, Open Code wins due to access to cheaper models. However, Anthropic subscription holders (Pro or Max plans) cannot use third-party harnesses like Open Code, and Claude Code bundles significant discounts compared to raw API rates. The recommendation is to use Open Code if on API-only pricing, but stick with Claude Code if you have an Anthropic subscription.

## Notable Quotes
- "Open code is an open source coding agent that just crossed 180,000 stars on GitHub and it's a direct replacement for tools like Claude code without the glitchy UI and expensive subscriptions."
- "The big difference is bringing your own models."
- "GLM 5.2 even beat Fable 5 at web design according to design arena."
- "The more detail you give here, the less likely it is to do the wrong thing or hallucinate."
- "My verdict here is that the UI is considerably better than Claude code."

## People, Tools & References Mentioned
- **Open Code** — the open-source coding agent featured in the video
- **Claude Code** — Anthropic's paid coding agent, used as the primary comparison
- **GLM 5.2** — a cheap, high-quality model recommended for design tasks
- **DeepSeek 4** — another available model
- **models.dev** — a model directory officially supported by Open Code
- **Ghostty** — recommended terminal for Open Code
- **Copilot** — referenced for its auto mode feature
- **Anthropic Pro/Max plan** — subscription tiers that block third-party harnesses
- **Design Arena** — benchmark cited for GLM 5.2's web design performance
- **LSP (Language Server Protocol)** — integration for real-time code error feedback
- **Warren** — the video host, from Better Stack

## Who Should Watch
Developers who use AI coding agents and want more flexibility, model choice, and customization than Claude Code offers—especially those on API-based pricing rather than Anthropic subscriptions. It's also valuable for anyone curious about open-source alternatives to paid AI coding tools.


<details class="transcript">
<summary>Full transcript</summary>

<p>Open code is an open source coding agent that just crossed 180,000 stars on GitHub and it&#x27;s a direct replacement for tools like Claude code without the glitchy UI and expensive subscriptions. You&#x27;ll get access to hundreds of models including free and local models, which is pretty cool. So, you&#x27;re not vendor locked into one platform. Today, we&#x27;re going to pull apart open code and we&#x27;re going to compare it to some of the paid alternatives and test whether free and open source really holds up when you&#x27;re trying to push to production. And we cover a huge amount of dev content on this channel. So, if you want to stay</p>
<p>this channel. So, if you want to stay up-to-date, then subscribe.</p>
<p>Open code is a coding agent that lives in your terminal and it comes with a huge array of tools like bash, edit, grep, web fetch, and web search. These are all the things that made Claude code so useful. So, seeing them in a free and open source tool is really nice. Once installed, we can run the open code command to enter our terminal. Here, I&#x27;m using Ghosty, which is one of open code&#x27;s recommended terminals. You can</p>
<p>code&#x27;s recommended terminals. You can see immediately the terminal UI here is really clean, but the big difference is bringing your own models. By default, I&#x27;m using a free model called Big Pickle. But, using the {slash} models command, I can easily switch to other free alternatives or paid models from companies like Google, Anthropic, and OpenAI. Hitting control I, I can also see a huge list of models which come from models.dev, a directory officially supported by open code. Here, you&#x27;ll have access to models like GLM 5.2 and</p>
<p>have access to models like GLM 5.2 and Deep Seek 4. Even with paid models, this can be considerably cheaper than sticking to API only pricing with labs like Anthropic because models like GLM 5.2 are much, much cheaper with comparable results to models like Fable 5. GLM 5.2 even beat Fable 5 at web design according to design arena. At the time of recording, there is no auto mode for open code to select a suitable model based on its assigned task. Features you&#x27;d see in harnesses like Copilot, but what you can do instead is configure custom sub agents to use a specific</p>
<p>custom sub agents to use a specific model. Then call on those for specific tasks. And this is a great way to segue into configuring Open Code&#x27;s agents. In Open Code, agents come in two types, primary and sub agents. Primary are the top-level agents you&#x27;d always use. You get build and plan exactly as you would expect from harnesses like Copilot or Claude Code. You can use tab to change this or just use the slash agents command. So, plan is exactly as you would expect for planning large features without actually making those changes, and then you could switch to the build</p>
<p>and then you could switch to the build agent to actually implement that plan. Or if you just want to make changes directly, stick into the build agent. Sub agents on the other hand are for specialist tasks, and they&#x27;ll be invoked automatically depending on your prompt. But you can tag them manually by using the at character. By default, you&#x27;ll have access to the general agent for researching complex questions and executing multi-step tasks. And then we have the explore agent, which has read-only access for exploring large code bases. Now, the really interesting and powerful part of Open Code is that</p>
<p>and powerful part of Open Code is that you can configure your own custom agents. So, there are a few ways that you can set up custom agents with Open Code. You can use the JSON file which I just explained earlier. And if you want all your config in one place, this is the right way to do it. So, I&#x27;ll just enlarge this. We can see that under the agents config, we&#x27;ve got a build agent, we&#x27;ve got the plan agent. So, these are the ones that come as default, but you can change these if you like. And then we&#x27;ve got a custom agent here called code review, and this just happens to be using Claude Sonic 4. And then we got a little description of what it does, and</p>
<p>little description of what it does, and then a prompt that would automatically be injected into the agent when you ask to perform a specific task. If you don&#x27;t want all of your config in one place, instead you can have a dot open code folder with an agents folder, and inside that you can describe the specific agent that you want as a markdown. So, here we have the UI engineer.md. And the description is it handles UI component implementation, styling, and front-end engineering tasks. The mode for this would be a sub-agent. We&#x27;re using GLM 5.2 just because that is</p>
<p>We&#x27;re using GLM 5.2 just because that is very, very good at doing design based on the design benchmarks. You can also change the temperature as well to modify the sort of randomness of the output that you would get from the model. And then you can also modify any of the default permissions. So, in this case, we always want to allow edits and always allow bash commands. Within the markdown file, you then can give further instructions on exactly what this agent does. So, here we say, &quot;You&#x27;re a UI engineer specializing in front-end development. You excel at&quot; and then you can give as much detail as you like to guide your agent in the correct direction. So, next time that you</p>
<p>direction. So, next time that you trigger a prompt that requires design work, it&#x27;s going to do exactly what you want. So, here as another example, we have review.md, and this will just do code review for us. In this case, we set the temperature as a really low number because we want more of a deterministic output from the model. We provide the same sort of permissions. This time, we&#x27;re using Claude Sonic 4, and then we give a little description of what it does: review code for quality and best practices. Again, the mode is going to be sub-agent. And then again, a short or long description to explain exactly what</p>
<p>long description to explain exactly what the model does. And the more detail you give here, the less likely it is to do the wrong thing or hallucinate. Now, when I&#x27;m working on a UI task, I can tag my agent and let GLM handle all of the design work. Now, here are a few things to improve quality of life when using open code. Flip on AliceP in your config, and it will auto-start the correct language server per file. So, the model gets real-time information and errors, not just raw text. And this is off by default, so you do need to flip it on. Using the at character also gives you fuzzy file search to pull in files</p>
<p>you fuzzy file search to pull in files into context. You can use undo or redo to reverse the agent&#x27;s changes, and they do stack. Share can give you a link to the whole session for debugging or handing to a teammate. You can also use inits, which writes an agents.md, a checked-in file that teaches the agents your project&#x27;s conventions. And this is just exactly like the Claude MD file in Claude code. So, my verdict here is that the UI is considerably better than Claude code. Plus, it has access to all of the same tools with the added benefit that you can use your own models and configure custom tools and agents. On</p>
<p>configure custom tools and agents. On cost, it&#x27;s actually not black and white. If you&#x27;re on API-only pricing, then Open Code wins easily because you have access to so many more much cheaper models. But, if you&#x27;re on a subscription with Anthropic&#x27;s Pro or Max plan, for example, you cannot use third-party harnesses like Open Code because Anthropic specifically block access to them. But, if you are on that subscription, then Claude Code bundles in a huge discounts compared to raw API rates. So, if you&#x27;re on API-only pricing, then stick to Open Code. But, if you do have that subscription, then</p>
<p>if you do have that subscription, then Claude Code is the winner on pure cost. If you enjoy hearing about the latest AI tooling, then we&#x27;ve done a breakdown of GLM 5.2 you can watch here. Otherwise, I&#x27;ve been Warren from Better Stack. Thanks for watching, and I&#x27;ll see you in the next one.</p>

</details>
