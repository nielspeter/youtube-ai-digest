---
title: "A Song of Types and Agents - Roberto Stagi, Ratel"
channel: "AI Engineer"
video_id: UlFB6efYN5Q
url: https://www.youtube.com/watch?v=UlFB6efYN5Q
published: 2026-07-12T12:45:05+00:00
generated: 2026-07-12T20:00:36+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/UlFB6efYN5Q/hqdefault.jpg
---
# A Song of Types and Agents - Roberto Stagi, Ratel

[![A Song of Types and Agents - Roberto Stagi, Ratel](https://i.ytimg.com/vi/UlFB6efYN5Q/hqdefault.jpg)](https://www.youtube.com/watch?v=UlFB6efYN5Q)

[Watch on YouTube](https://www.youtube.com/watch?v=UlFB6efYN5Q) · **AI Engineer** · 2026-07-12

## TL;DR
Roberto Stagi argues that TypeScript is displacing Python as the dominant language for building AI agents and AI-powered applications, driven by the rise of coding agents, the richness of NPM, and the ability to maintain a single language and type system across the entire stack. Python remains the undisputed king of model training and inference, but the application and agentic layer increasingly belongs to TypeScript.

## Key Takeaways
- Python dominated AI for years and became the most popular language on GitHub in 2024, fueled by the post-ChatGPT AI surge.
- By August 2025, TypeScript overtook Python as the most used language on GitHub, with the same catalyst cited by GitHub: AI.
- The key shift between 2024 and 2025 was the maturation of coding agents (Cursor, Codex, Lava Cloud Code), which default to TypeScript.
- AI has moved up the stack from infrastructure/training to the application layer, which has been TypeScript's territory for years.
- Python still owns the "brain"—training, research, GPU serving, and inference—but TypeScript owns the agentic and application layer.
- Building in TypeScript lets teams use one language and one consistent type system (e.g., Zod) across the agent loop, backend, and UI, avoiding a split between Python services and a separate React frontend.
- NPM is the richest package manager, covering authentication, payments, UI, and infra, making it convenient for AI application integration.
- The AI ecosystem in TypeScript is growing fast; the Vercel AI SDK went from 1.6M to 15.1M weekly downloads in one year (~9–10x).
- Coding agents will keep getting better at TypeScript because more TypeScript code feeds their training, creating a compounding advantage.
- Jeff Atwood's law ("any application that can be written in JavaScript will eventually be written in JavaScript") extends to TypeScript, and the gap between TypeScript and Python at the application layer will widen.

## Detailed Breakdown

**[00:02] Introduction: A Song of Types and Agents**
Roberto introduces the talk as a "song of types and agents," framing it as a story of languages competing for dominance in the AI realm, with TypeScript emerging as the likely winner.

**[00:33] Python's Dominance and the ChatGPT Inflection Point**
For years, Python was the unquestioned language of AI. The release of ChatGPT in 2022 expanded AI beyond its niche, and in 2024 GitHub named Python the most popular language, attributing the rise to AI.

**[02:07] Speaker Background**
Roberto introduces himself as CTO and co-founder of Ratel, a context layer for AI agents, and EU ambassador for AI Tinkerers, a global community of AI builders. He is a long-time JavaScript and TypeScript developer.

**[02:38] AI Moves Up the Stack**
AI shifted from the infrastructure layer (training, ML ecosystem) to the application layer—AI is now something you ship inside applications. The application layer has been TypeScript's domain for a long time.

**[03:41] Python Keeps the Brain; TypeScript Takes the Application Layer**
Roberto clarifies that Python still owns training, research, and GPU serving—the "brain" of AI. What changed is the application layer: a few years ago you had to use Python to build AI into an app, but no longer. TypeScript now owns the agentic layer too.

**[04:46] TypeScript Passes Python on GitHub**
In August 2025, TypeScript passed Python as the most used language on GitHub. GitHub's reports gave the same reason both years—AI drove the language to the top. By 2025, one new developer joined GitHub every second.

**[05:18] What Changed: Coding Agents**
The difference between 2024 and 2025 was the rise of coding agents like Cursor, Codex, and Lava Cloud Code. They became the default way to build applications, and they defaulted to TypeScript. Since nearly every new app is now an agent, the demand for AI integrations falls on TypeScript, not Python. Anthropic's acquisition of the Bun JavaScript runtime is cited as further evidence.

**[07:20] Should You Build AI Agents in TypeScript?**
Roberto argues yes. First, coding agents will keep improving at TypeScript because more TypeScript code feeds their training. Second, NPM is the richest package manager, covering everything needed for application integration. Third, TypeScript enables a single language across the entire codebase—agent loop, tools, backend, and UI—whereas Python forces a split (e.g., FastAPI + Pydantic AI backend and a separate React frontend) with contracts to maintain.

**[10:01] Consistent Typing with Zod**
TypeScript allows one consistent type system across the whole application using Zod. You define a type once and use it in the backend, the model, and the UI. With Python, you hit a boundary where the frontend has its own typing that must be synchronized.

**[11:03] The TypeScript AI Ecosystem Is Surging**
The Vercel AI SDK grew from 1.6M to 15.1M weekly downloads in one year, roughly a 9–10x increase, showing the ecosystem's rapid expansion.

**[11:34] Summary of Reasons and Atwood's Law**
Roberto summarizes the five reasons to build agents in TypeScript: default language for coding agents, single language across the codebase, fast-growing AI ecosystem, consistent typing, and the richest package manager. He invokes Jeff Atwood's 20-year-old prediction that any application writable in JavaScript will eventually be written in JavaScript, extending it as a corollary to TypeScript.

**[13:08] Recommendation and Closing**
The model and inference layer stays Python (pip), but the agent and application layer ships on NPM. Roberto recommends keeping training in Python but building agents and applications in TypeScript—those who overlook TypeScript risk falling behind. He closes by inviting feedback and sharing a QR code for slides.

## Notable Quotes
- "The brain of the agent and all of the AI world is actually still owned by Python. All the training, the research, the GPU serving is all Python's. What's changing is actually the application layer."
- "In August 2025, TypeScript actually passed Python as the most used language on GitHub."
- "What changed between 2024 and 2025 was actually coding agents."
- "Since every new app pretty much every new app is an agent today... the demand to have more AI integrations doesn't fall on Python. It falls on TypeScript."
- "Any application that can be written in JavaScript will eventually be written in JavaScript." — Jeff Atwood, with Roberto's corollary: any application that could be written in JavaScript will eventually be written in TypeScript.
- "The model can still run on pip. But the agents... will probably ship on NPM."

## People, Tools & References Mentioned
- **Roberto Stagi** — CTO and co-founder of Ratel, EU ambassador for AI Tinkerers
- **Ratel** — a context layer for AI agents
- **AI Tinkerers** — global community of AI builders meeting monthly
- **GitHub** — language popularity reports (2024 Python, 2025 TypeScript)
- **ChatGPT** (2022 release) — inflection point for AI adoption
- **Coding agents:** Cursor, Codex, Lava Cloud Code
- **Anthropic** — acquired the Bun JavaScript runtime (December, per talk)
- **Bun** — JavaScript runtime acquired by Anthropic
- **NPM** — richest package manager, cited for breadth of packages
- **Zod** — TypeScript schema/type library for consistent typing
- **Vercel AI SDK** — grew from 1.6M to 15.1M weekly downloads in one year
- **FastAPI, Pydantic AI** — Python backend stack mentioned as contrast
- **React, Vue** — frontend frameworks mentioned in the Python split-stack contrast
- **Jeff Atwood** — author of the "Atwood's Law" quote about JavaScript

## Who Should Watch
AI engineers, full-stack developers, and engineering leaders deciding which language to standardize on for building AI agents and AI-powered applications—especially those currently weighing Python vs. TypeScript for their agentic stack.


<details class="transcript">
<summary>Full transcript</summary>

<p>Hello, and thank you for being here. I&#x27;m Roberto, and today I&#x27;m going to tell you this song of types and agents. Uh basically a song that speaks about languages that fight each other to conquer what&#x27;s the throne in the AI realm. And how I think that TypeScript might actually be winning this war. But let&#x27;s start from the beginning. A few years ago, whenever someone was</p>
<p>A few years ago, whenever someone was building uh in AI, they were certainly using Python. Like there was no doubt. All the other languages were bowing to Python because um because of its dominion uh over the AI world. And then, when in 2022 ChatGPT was released, everybody started wondering and starting understanding that AI was becoming something more. Was</p>
<p>that AI was becoming something more. Was going outside of the bubble that lived for years. And started to becoming something more ambitious. And together with it, Python, which was the standard language for AI, became more ambitious as well. And that&#x27;s how in 2024 uh GitHub actually claim claimed the ladder and became the most popular language on GitHub. So,</p>
<p>So, you know, everybody was happy. Python finally reached the top. But little did they know that there was another contender for the throne. Another contender that was rising to challenge the claim that Python had on the throne. And this contender, as you may have guessed by now, was indeed TypeScript. But, before talking about this, let me present myself. My name is Roberto. I&#x27;m</p>
<p>present myself. My name is Roberto. I&#x27;m the CTO and co-founder of Reto, a context layer for AI agents. And I&#x27;m also the EU ambassador for AI&#x27;s Pratic, a global community of AI builders meeting once per month to discuss the latest news in AI. I&#x27;m also a long-time JavaScript then turned TypeScript developer. And that&#x27;s basically why I am talking about TypeScript today. So, let&#x27;s begin.</p>
<p>begin. As we said, AI started moving up to the stack. It was moving from the infrastructure layer of these models, machine learning, and all related ecosystem towards the application layer. This means that AI stopped being something that you train, and it started being something that you ship inside your application. Applications started featuring AI,</p>
<p>Applications started featuring AI, starting having features powered by AI. Which basically means that we started having applications that think. And the application layer was not Python&#x27;s. The application layer has been TypeScript&#x27;s for pretty long time now. Don&#x27;t get me wrong, like I still think that Python has its own application. Like I still think that the</p>
<p>application. Like I still think that the brain of the of the agent and all the of all the AI world is actually still owned by Python. All the training, the research, the GPU serving is all Python&#x27;s. Uh Has been Python&#x27;s all along and it&#x27;s going to be Python&#x27;s for long time yet. And um what&#x27;s changing is actually the application layer. Like few years ago, if you wanted to build something with AI built in the application, you had to use Python.</p>
<p>application, you had to use Python. But today, that&#x27;s not the case anymore. And that&#x27;s all uh the shift is about. TypeScript doesn&#x27;t just own, you know, the UI or the back end. Started owning also the agentic layer of our application. And that&#x27;s why in August 2025, TypeScript TypeScript actually passed Python as the most used language on GitHub. And the funny thing is that the reason that the GitHub reports gave</p>
<p>that the GitHub reports gave was the same. Like in 2024, it said AI leads Python to the top language. While in 2025, it said AI leads TypeScript as the first language. And in both cases, as you can see, the global developers, the number of global developers were surging. In 2020 2025, we even have one new developer joining GitHub every second.</p>
<p>GitHub every second. So, what actually changed in this year? Like yeah, we were flooded from like new developers. In 2024, these newcomers were reaching for Python, or even maybe existing developers were reaching for Python. And in 2025, they reached for TypeScript instead. What changed between 2024 and 2025 was actually coding agents.</p>
<p>coding agents. The coding agents grew up like we saw established um we saw the players establishing themselves like Lava Cloud Code, Cursor, Codex. They became the default way to build applications. And the default way to uh to which these coding agents actually built the applications was TypeScript. And you know since</p>
<p>since every new app pretty much every new app is an agent today because they ship these AI and agentic capabilities, they are hungry to embed AI inside themselves. The demand to have more AI integrations, more and more AI integrations doesn&#x27;t fall on through Python.</p>
<p>[clears throat]</p>
<p>It falls on TypeScript. And pretty much all the tools that we</p>
<p>And pretty much all the tools that we use to build AI today already run on TypeScript. We even saw an AI lab acquiring a JavaScript runtime like last December Anthropic acquired Bun. But still, you know, okay, everybody use is using TypeScript because of the coding agents and we are having more and more demand to build uh AI to embed AI inside TypeScript</p>
<p>embed AI inside TypeScript application. But does this mean that we should do it? Like this is a fair question, like it&#x27;s an honest question and it&#x27;s a question worth answering. And the answer in my opinion can be yes like for several reasons. The first one is that since TypeScript is the default language for coding agents today, we can expect that they will become better and better in in TypeScript because we are having more</p>
<p>TypeScript because we are having more and more application in TypeScript, which are going to field the training of next coding agents. And then we are having uh deeper integrations and more native integrations from these coding agents towards TypeScript, and we can expect that the quality of the output in TypeScript is going to be better and better from these coding agents. Since we&#x27;re building applications, and uh we want to have like the highest quality of these applications, might make sense to build agents, which</p>
<p>might make sense to build agents, which are the new kind of applications in TypeScript. And also, if you use TypeScript, you are actually tapping into what is probably the richest package manager out there. NPM comes with everything, uh pretty much everything, like authentication, payments, UI, infra. Like it&#x27;s uh the deepest up layer tail that there is. So, since again, AI is coming towards the</p>
<p>since again, AI is coming towards the application layer, we need to integrate with all these right now. And tapping inside NPM is a very convenient way to do that. Also, you have by building in TypeScript, you can have one single language throughout all your code base. You can have one single code base for the whole application. Because you can use TypeScript for your agent loop, for the tools, for the back end service, for the UI.</p>
<p>end service, for the UI. While if you use Python, you probably have to split uh split it at least into two services. Which means, you know, one service with FastAPI, Pydantic AI, and whatever. And then another um separate React application that you need to sync between between these two with a uh with a contract, which you have to maintain and synchronize. And speaking of contracts, with TypeScript, you can have one single</p>
<p>with TypeScript, you can have one single consistent typing across all your all your application. While if you use Python instead, you at some point will stop at a boundary, cuz you will have your agent, maybe your back end, etc. with one consistent typing, and then you will have your React application or Vue or whatever with um another set of typing at which you need to synchronize between the two. So, if you use TypeScript, you can use</p>
<p>So, if you use TypeScript, you can use Zod as a single schema throughout all your application, which is very convenient. You can define a type once. You can use this type in the back end and uh in the model, and you can use the same type in your UI. One type, checked and went. Also, like it makes sense to build in TypeScript today uh also in the AI ecosystem because we are seeing a very surge in</p>
<p>because we are seeing a very surge in in the AI ecosystem as well. Like take the Versatile AI SDK, for example, you can see that in just 1 year, it went from 1.6 million to 15.1 million downloads per week, which is between 9 and 10x in just 1 year. So, finally, I&#x27;d to put everything together. In my opinion, yes, it makes sense to build AI agents in TypeScript because you have like a uh you can leverage the</p>
<p>uh you can leverage the the de facto default language for coding agent. You can have one single language for your whole application and your whole code base. You can tap into uh fast-growing AI ecosystem. You can have consistent typing uh across all your application. And you can tap into the richest package manager that there is, NPM. So, um you might ask was all this unpredictable? And the</p>
<p>was all this unpredictable? And the answer is actually no. Someone predicted this uh many years ago, almost 20 years ago. Jeff Atwood said, &quot;Any application that can be written in JavaScript will eventually be written in JavaScript.&quot; And you know, as you as you probably know in the last few years, we have a corollary of this that any application that could be written in JavaScript will eventually be written in TypeScript. And so basically, we can say that any application, even the gigantic ones,</p>
<p>application, even the gigantic ones, will be written in TypeScript. And be mindful that what I showed you today is just the beginning. Like, we are just getting started. You can project this in a few years and you can see that on the application layer, the difference between TypeScript and Python is actually going to widen from here. So, um as I said, the model can still run on</p>
<p>as I said, the model can still run on pip. But the agents, which is the application layer today, so the agent that called the models will probably ship on NPM. So, everything on the inference layer, you know, it&#x27;s going to be Python. But everything but else, probably all TypeScript. Let me leave you with one recommendation then. Um keep training in Python. As I said, I don&#x27;t see that&#x27;s one going away soon.</p>
<p>don&#x27;t see that&#x27;s one going away soon. But please consider building the agents and the applications in TypeScript. Because if you don&#x27;t do that now, if you overlook TypeScript, you are probably going to fall behind. That was all on my side today. I thank you all for your listening. And please scan the QR code for the slides. Reach out to me if you agree or if you disagree, if you have any feedback, and let&#x27;s get in touch. Thank you.</p>
<p>let&#x27;s get in touch. Thank you. Bye-bye.</p>

</details>
