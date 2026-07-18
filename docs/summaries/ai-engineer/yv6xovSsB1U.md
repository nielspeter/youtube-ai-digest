---
title: "Content Is Code - Matt Palmer, Conductor"
channel: "AI Engineer"
video_id: yv6xovSsB1U
url: https://www.youtube.com/watch?v=yv6xovSsB1U
published: 2026-07-18T16:15:06+00:00
generated: 2026-07-18T17:10:18+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/yv6xovSsB1U/hqdefault.jpg
---
# Content Is Code - Matt Palmer, Conductor

[![Content Is Code - Matt Palmer, Conductor](https://i.ytimg.com/vi/yv6xovSsB1U/hqdefault.jpg)](https://www.youtube.com/watch?v=yv6xovSsB1U)

[Watch on YouTube](https://www.youtube.com/watch?v=yv6xovSsB1U) · **AI Engineer** · 2026-07-18

## TL;DR
Matt Palmer argues that code is becoming the primary medium for technical communication and content creation, driven by AI making code generation cheap. The real bottleneck is no longer engineering skill but organizational structure and conscientiousness—maintaining clean codebases, design tokens, and disciplined workflows. He predicts 2027 will be the year of the "content engineer," when declarative content pipelines produce documentation, videos, and product updates directly from code.

## Key Takeaways
- Code is increasingly the fastest and best way to create any creative asset—videos, websites, slides, images—not just software.
- Three eras of content: handcrafted (manual), expensive code (engineers as bottleneck), and cheap code (AI-driven generation).
- AI has made code generation inexpensive, meaning the cost barrier to producing high-fidelity content assets has collapsed.
- The scarce resource is no longer engineering skill or "taste"—it is **structure**: clean codebases, design tokens, disciplined PR practices, and internal documentation.
- AI rewards conscientiousness and organizational excellence, not raw technical brilliance.
- Without structure, AI-generated content degrades into generic "purple gradient slop"; with structure, it looks professional and polished.
- Content is shifting left toward code as the source of truth, requiring disciplined engineering practices to enable content generation.
- Tools like React, TypeScript, and Remotion are becoming the default toolkit for content creators, even those without traditional frontend backgrounds.
- 2026 was the year of the "creative technologist" in DevRel; 2027 will be the year of the "content engineer."
- Declarative, robust content pipelines will soon generate walkthroughs, documentation, screenshots, and product updates from code.

## Detailed Breakdown

**[00:00] The Medium Problem and Code as Communication**
Matt opens by acknowledging the classic challenge of content creation: choosing the right medium. People default to what they already know. His central thesis is that code is increasingly becoming the way we communicate, something that would have seemed wild just a few years ago when only professional software engineers wrote code for content.

**[01:00] What "Content" Means in Technical Communication**
He defines content broadly as technical communication—documentation, change logs, product update emails, product tours, video overlays, and more. He emphasizes that accurate change logs require an accurate diff of the product, which is genuinely hard without either strong tooling or someone manually combing through PRs. Content is the act of communicating what a product solves and how it has changed.

**[02:04] A Live Example: Product Tour Built in React and Remotion**
Matt shows a product tour for Conductor built entirely with React and Remotion. He recreated the product surface and walked through a sample user flow in a Remotion scene. He admits it is still a bit buggy and the flows aren't perfect, but sees it as a preview of a coming norm where entire product surfaces and videos are generated via code.

**[03:05] Three Eras of Content Creation**
Matt frames the evolution in three eras. **Era one** is the handcrafted era—everything is manual, and your only levers are time, money, and skill; you either do it yourself or hire an expert or agency. **Era two** is the era of expensive code—cloud and code are mature, but engineering is the bottleneck and engineers are costly, so content is deprioritized. Frameworks like Remotion didn't proliferate because few had the time or incentive to invest in "content engineering." **Era three** is today: code is cheap because of AI. You can generate videos, documentation, websites, and motion graphics with tools like Claude—but quality varies, and you need an engineering mindset to get good results.

**[05:37] Code as the Fastest Way to Build Anything**
Matt reflects on preparing this presentation and realizing his favorite medium is TypeScript. Every ancillary asset—slides, images, videos—is React or TypeScript. Coming from a Python/data engineering background, he finds it remarkable that he now leans on React, TypeScript, CSS, and HTML as the best path to high-fidelity assets.

**[07:12] Structure Is the Expensive Thing**
With code being cheap, the scarce resource is structure: maintaining a clean codebase, enforcing brand guidelines, keeping design tokens consistent, separating frontend from backend code, writing clean PRs with proper descriptions and tags, and maintaining accurate internal documentation. Without these, even good AI agents cannot produce polished results. The difference between generic AI "purple gradient slop" and professional output comes down to structural discipline.

**[08:13] AI Rewards Conscientiousness**
Matt argues that AI rewards conscientiousness—being meticulous, careful, and guided by professional duty—over raw engineering skill. The highest-performing teams will be those that instill discipline and rigor into their software process and then shift content creation left toward code. He predicts 2026 was the year of the "creative technologist" in DevRel, and 2027 will be the year of the "content engineer," when declarative content pipelines produce walkthroughs, documentation, screenshots, and product updates from code.

## Notable Quotes
- "Increasingly code is becoming the way that we communicate."
- "My favorite medium is actually TypeScript. Aside from recording myself talk or writing, every ancillary asset is React or TypeScript."
- "Structure is expensive. The hard thing is maintaining a very structured code base, maintaining brand guidelines and keeping those guidelines consistent."
- "Structure often is the difference between AI purple gradient slop and something that looks professional and polished."
- "AI rewards conscientiousness. AI rewards organizational excellence. AI rewards structure."
- "2026 was the year of the creative technologist. I think 2027 is the year of the content engineer."

## People, Tools & References Mentioned
- **Matt Palmer** — speaker; former data engineer, former DevRel lead at Replit, now leads developer experience at Conductor
- **Conductor** — Matt's current company
- **Replit** — Matt's former employer
- **Remotion** — React-based framework for programmatic video creation
- **React / TypeScript / CSS / HTML** — core technologies Matt uses for content generation
- **Anthropic / OpenAI** — AI providers referenced as the "paid" entities replacing human labor for code generation
- **Claude** — Anthropic's AI, cited as a tool for creating videos, documentation, websites, and motion graphics

## Who Should Watch
DevRel professionals, developer experience engineers, technical content creators, and engineering leaders who want to understand how AI and code are reshaping content pipelines—and why organizational discipline matters more than ever.


<details class="transcript">
<summary>Full transcript</summary>

<p>So, if you&#x27;ve ever created content, you know it could be hard. And what&#x27;s often most hard is choosing a medium for how you&#x27;d like to communicate. Do you write a blog post? Do you create a video? Do you go out and speak at a conference? And even of these things, you&#x27;re likely to select something that you&#x27;re good at or you have experience doing. But the idea I want to present to you today is that increasingly code is becoming the way that we communicate. Now, this might seem obvious in 2026, but I want to point out that even a couple years ago, this was wild because the only people</p>
<p>this was wild because the only people that were writing code to create content were professional software engineers. And often professional software engineers are spending their time doing mostly engineering and are not getting that deep on content. Now, what do I mean when I say content? Well, I&#x27;m talking mostly about technical communication. That could be documentation, it could be things like change logs, emails, product marketing, it could be video, which I create a lot of. Um, and it could be other things associated with a typical DevRel motion, but it&#x27;s not restricted to DevRel, right? Content or technical</p>
<p>right? Content or technical communication is the act of communicating what a what problem a product really solves. And that can be done by anybody. That might mean really complete, accurate documentation that covers every part of the Deta X this framework. It could be change logs shipped timely um with robust assets that cover all areas of a product. This is something that&#x27;s often overlooked. This is actually really hard because to have an accurate change log, you have to have an accurate diff of your product. Or you could just have someone that spends a lot of their time combing through PRs to try to</p>
<p>time combing through PRs to try to figure out what was shipped. It could be things like timely product updates, emails, which kind of follow from a change log, right? If you understand what changed, you can then summarize that over time for your users. It could be something as simple as a home page product tour instead of a static screenshot. These are all ways that we&#x27;re communicating products, we&#x27;re communicating what this thing does or how it&#x27;s changed via either written content</p>
<p>content free via code via distinct assets. It could also be something like video overlays, right? Something like adding a bit of engaging material to the content that you create, but increasingly where I think this is headed is entire product surfaces and entire videos generated via code. And in front of me, I have a product tour for Conductor that was built entirely with React and Remotion. So, basically, I recreated the product</p>
<p>So, basically, I recreated the product surface. I used a Remotion scene to recreate the product and do a full walk-through of a sample user flow. Now, it&#x27;s not perfect. It&#x27;s a little buggy and the flows aren&#x27;t quite there yet, if I&#x27;m being honest, but I think we&#x27;re moving towards a world where this is normal. So, my name is Matt. I was previously a data engineer, then I led DevRel at Replit, and now I lead developer experience at Conductor. And today I want to talk about how content is shifting left to code as the source of</p>
<p>shifting left to code as the source of truth. And so, I think there are three distinct eras we can think about here. Era one, the handcrafted era of content. Era two, an era where code existed, but it was quite expensive. And era three, where code exists, but it&#x27;s very cheap. And that&#x27;s where we are today with AI. So, in the handcrafted era, right? Everything is manual. The only levers we really have are time and money and skill. And so, if I want something, I either need to create it myself, but there are only 24 hours in a day, so</p>
<p>there are only 24 hours in a day, so likely I&#x27;m going to go out and seek an expert, someone that does know how to create this thing. Maybe that&#x27;s an agency or someone who creates these assets professionally. If I&#x27;m thinking about like motion graphics, for example. Now, post era one, when we had expensive code, code and cloud are mature assets. These are things that have existed for a while, and most professional software engineers know how to use. Engineering is now the bottleneck. This is like Serp era, everybody&#x27;s paying a lot for</p>
<p>era, everybody&#x27;s paying a lot for engineers, and to get anything done, you really need professional software engineers. So, you&#x27;d better pay someone, maybe not an agency, but an engineer. And that included things like, you know, um robust documentation, or even just a website, right? You Back in the day, it&#x27;s hard to imagine before AI, you wanted a website, a good website, you needed a front-end engineer, or like a low-code website service, but those weren&#x27;t any good to begin with. So, you needed a professional engineer to have a really nice website. And what that meant was that content is</p>
<p>And what that meant was that content is really not the priority, right? Because if you&#x27;re a professional engineer, you have better ways of spending your time. And I think this is reflected by um libraries like Remotion, frameworks like Remotion, um not proliferating the way that they are today. Because, really, who has the time and energy to put into these things? There aren&#x27;t a ton of what I&#x27;d call content engineers. Now, in era three, most of these things, you&#x27;re not paying a human, you&#x27;re paying Anthropic, or OpenAI, or whoever, right? You can create videos with Claude. You</p>
<p>You can create videos with Claude. You can create documentation with Claude. You can design websites with Claude, and you can create motion graphics with Claude. Now, the problem is that not all of the all of these things are good, right? We&#x27;ll talk about that later, but if you know what you&#x27;re doing, if you have an engineering mindset, if you understand the systems, you can create high-quality assets with these systems. And I&#x27;m going to talk about how to do that in the rest of this presentation. So, today, code is cheap. And we talk about code as communication. So, code is communication. The fastest</p>
<p>So, code is communication. The fastest way to build an asset today is through code. And it&#x27;s not just to build software, right? It&#x27;s really to build anything. If I want a prototype a video, a website, slides, um I mean really any asset, any creative thing that I can think of, images, video, the fastest way to do that is going to be through code or code generation. And I was thinking about this presentation, I was thinking about how I was going to create all the assets for this presentation, and I realized that my</p>
<p>presentation, and I realized that my favorite medium is actually TypeScript. Aside from recording myself talk or writing, every ancillary asset is React or TypeScript. And I just want to take a moment because that is the most insane statement to hear myself say if I was thinking about this two or three years ago, right? I don&#x27;t even really know how to write that good of TypeScript, you know? My background&#x27;s in data engineering, I come from Python land. Well, I better learn TypeScript, I better learn React because the best way for me to get these high-fidelity assets is React,</p>
<p>high-fidelity assets is React, TypeScript, CSS, um and HTML. And that&#x27;s wild. That&#x27;s wild to say. So, if code is inexpensive, what is the expensive thing? Now, you might think I&#x27;m going to say taste here. I&#x27;m not going to say taste because everybody says taste. Structure is expensive. This is maybe a bit of a contrarian sta- statement here because the hard thing is maintaining a very structured code base, maintaining brand guidelines and keeping those guidelines consistent, keeping design tokens in your project, separating even front-end code from</p>
<p>separating even front-end code from back-end code from these design tokens. Merging really clean PRs, which like nobody does, right? Tagging PRs, PR descriptions, knowing what&#x27;s a feature and what&#x27;s a bug fix, knowing if you reverted a PR. How many organizations do this? I&#x27;ve worked at a number of organizations, none, right? And maintaining accurate internal documentation so that anybody can accomplish anything. Even if you have really good agents, they&#x27;re not going to know how to solve these problems if they don&#x27;t have documentation or skills, right? And so, structure often is the</p>
<p>And so, structure often is the difference between AI purple gradient slop, right? And something that looks professional and polished. And I would even go a little bit further, and I would say that this is conscientiousness. And the dictionary definition for conscientiousness is the quality of being meticulous, careful, and guided by a strong sense of moral or professional duty. And so, it&#x27;s less about comp- like software engineering skill today. It&#x27;s less about the skill of being able to create this these assets,</p>
<p>being able to create this these assets, and more about the meticulousness and care given to making sure that an outcome matches your expectations. And that, you know, increasingly with each model generation is not predicated on being the smartest person in the room, or being this the person in the room with the most technical skill. So, what does AI reward? AI rewards conscientiousness. AI rewards organizational excellence.</p>
<p>AI rewards organizational excellence. AI rewards structure. And ultimately, these are the things that go into good AI skills. There&#x27;s a lot of like not very good AI skills out there. Um and most of them are just generated without any regard for what&#x27;s in their contents or how they&#x27;re structured. And so, all the assets that I showed you at the beginning of this video are a byproduct of design tokens, structured code, um structured assets. And they get exponentially harder to create when we lack those things.</p>
<p>create when we lack those things. And so, code, again, is communication. And we&#x27;re seeing a shift left movement for content, where content is moving to code. And if code, right, is the source of truth, if our code base is the source of truth, we have to have a structured source of truth in order to create content from code. In order to communicate, we need structure and conscientiousness around the way that we create code. And again, this only works</p>
<p>create code. And again, this only works with organizational excellence. And so, I think what we&#x27;ll see in 2026 and the years beyond is that the highest performing the best communicating teams are the ones that are able to instill discipline and rigor into the process of creating software and then shift their content left towards the code through content engineering. And so, 2026, I think was the year of the creative technologist, at least in the DevRel space. This is the term that</p>
<p>the DevRel space. This is the term that got thrown around a lot. I think 2027 is the year of the content engineer. And I&#x27;ll close on that because I think what we&#x27;re going to see next year are declarative and robust content pipelines capable of producing content walkthroughs, capable of producing documentation, screenshots, product updates, all of the things that were really manual can now be created through code, through React, and ultimately because of AI. Again, I&#x27;m Matt with Conductor. Thanks</p>
<p>Again, I&#x27;m Matt with Conductor. Thanks for sticking around for my talk. I&#x27;ll catch you next time. Peace.</p>

</details>
