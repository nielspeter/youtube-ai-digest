---
title: "Security Track Intro — Randall Degges, Snyk"
channel: "AI Engineer"
video_id: 2xJoimgoqBg
url: https://www.youtube.com/watch?v=2xJoimgoqBg
published: 2026-07-20T17:17:53+00:00
generated: 2026-07-20T21:20:26+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/2xJoimgoqBg/hqdefault.jpg
---
# Security Track Intro — Randall Degges, Snyk

[![Security Track Intro — Randall Degges, Snyk](https://i.ytimg.com/vi/2xJoimgoqBg/hqdefault.jpg)](https://www.youtube.com/watch?v=2xJoimgoqBg)

[Watch on YouTube](https://www.youtube.com/watch?v=2xJoimgoqBg) · **AI Engineer** · 2026-07-20

## TL;DR
Randall Degges kicks off the first-ever security track at the AI Engineer World's Fair, framing AI security as the key obstacle to fearless innovation. He highlights three core challenges—vulnerable AI-generated code, the risks of deploying autonomous agents, and geopolitical access constraints—before inviting attendees to a full day of expert sessions downstairs.

## Key Takeaways
- AI-generated code can introduce security vulnerabilities, much like human-written code, making security an essential part of the modern development lifecycle.
- Deploying autonomous agents into production presents a harder, less-solved problem: ensuring they don't go off the rails and cause harm.
- Geopolitical factors—such as restricted access to models like Fable and the newest OpenAI models—compound the challenge of building with AI confidently.
- The overarching goal is to enable developers to "use AI fearlessly" with security built in by default.
- Snyk and other leading organizations are launching a dedicated security track to address these concerns.
- The security track features presentations from NVIDIA, Anthropic, Keycard, and Snyk.
- The track runs all day in Room 2005 on the second floor, immediately following the keynote.
- Randall emphasizes the joy of shipping quality software quickly with AI, but stresses that security is what makes doing so at scale possible.

## Detailed Breakdown

### Introduction and Personal Background [00:01](https://www.youtube.com/watch?v=2xJoimgoqBg&t=1s)
Randall opens with a brief greeting and thanks Ali for the introduction. He notes that his talk will be short and focuses on the current state of AI security. He shares that he has spent his career as both a developer and security professional, and that what excites him most about generative AI is the ability to build better software faster and ship it to users.

### The Joy and Obstacles of AI-Assisted Development [00:32](https://www.youtube.com/watch?v=2xJoimgoqBg&t=32s)
Randall describes the feeling of shipping software to real users as almost a "cheat code" for productivity and joy. However, he identifies several obstacles preventing developers from innovating at scale with AI. The first is the well-known risk that AI-generated code may contain security issues—analogous to the vulnerabilities humans introduce, which simply makes security tooling a standard part of modern engineering.

### The Harder Problem: Autonomous Agents in Production [01:34](https://www.youtube.com/watch?v=2xJoimgoqBg&t=94s)
The second, more interesting challenge Randall highlights is deploying autonomous agents into production. The difficulty lies in trusting that these agents will not behave unpredictably, go off the rails, or harm the business or its users. This, he argues, is a much tougher problem than simply scanning generated code for flaws.

### Geopolitics and Model Access [02:05](https://www.youtube.com/watch?v=2xJoimgoqBg&t=125s)
The third barrier Randall discusses is what he calls "almost geopolitics." He asks the audience how many were annoyed when access to "Fable" was pulled, and how many are frustrated they can't yet use the newest OpenAI GPT-5.6 model. Both prompts draw visible audience reactions. He ties these access limitations back to the broader theme of security and the ability to use AI confidently.

### Announcing the Security Track [03:08](https://www.youtube.com/watch?v=2xJoimgoqBg&t=188s)
Randall announces that immediately after the keynote, the first security track at the World's Fair will run for the entire day in Room 2005 on the second floor. The track will feature presentations from top companies and speakers, including NVIDIA, Anthropic, Keycard (where Ali works), and Snyk. The goal is to help attendees level up their AI projects with security built in, so they can build without worry. Randall closes by inviting everyone to join him downstairs, where he will emcee the sessions all day.

## Notable Quotes
- "There's nothing more fun than shipping the things that you're working on to actual users and sparking that sense of joy, right? It almost feels like a cheat code."
- "When humans write code, we generate security issues. When AI models write code, turns out they also generate security issues."
- "How do you do that in a way that allows you to go to sleep easily and not worry that the agents you deployed are going to go off the rails?"
- "Fundamentally, the biggest problem that I feel we have to still solve in our space is being able to use AI fearlessly and have it be secure by default."

## People, Tools & References Mentioned
- **Randall Degges** — speaker, Snyk, emcee of the security track
- **Ali** — introducer, works at Keycard
- **Snyk** — Randall's company
- **NVIDIA** — security track presenter
- **Anthropic** — security track presenter
- **Keycard** — security track presenter
- **Fable** — AI model whose access was pulled (referenced as an example of geopolitical access constraints)
- **OpenAI GPT-5.6** — referenced as a model attendees wish they could use now
- **AI Engineer World's Fair** — the event hosting the security track

## Who Should Watch
Developers, security professionals, and AI engineers who are building with generative AI or deploying autonomous agents and want practical guidance on doing so securely. It's especially relevant for those concerned about balancing rapid AI-driven innovation with safety and reliability.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=2xJoimgoqBg&amp;t=1s">00:01</a></span> Hello. How&#x27;s it going everyone? I&#x27;m Randall. Thanks for the nice intro Ali. And I&#x27;m only up here for a couple minutes. This is going to be very brief. But what I wanted to talk about in the time that I have is kind of the state of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=2xJoimgoqBg&amp;t=32s">00:32</a></span> time that I have is kind of the state of AI security and the things that I&#x27;ve been thinking about quite a lot lately and maybe things that you&#x27;ve all been thinking about too. So I&#x27;ve been a developer and security professional pretty much my entire life. And even though I&#x27;ve been in the security space, the thing that makes me excited in these recent years with the rise of generative AI is being able to build better quality software more quickly. There&#x27;s nothing more fun than shipping the things that you&#x27;re working on to actual users and sparking that sense of joy, right? It almost</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=2xJoimgoqBg&amp;t=63s">01:03</a></span> that sense of joy, right? It almost feels like a cheat code. And I think that there&#x27;s really a few obstacles to allowing all of us in the room today to do these things at scale in today&#x27;s world. So the first thing is something that all of us probably learned the hard way a few years ago, which is when you&#x27;re building software using AI, uh there&#x27;s always the risk that the code the AI generates might have a security issue. Everybody knows that. It&#x27;s nothing new, right? And I think the reason that that&#x27;s not a big deal is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=2xJoimgoqBg&amp;t=94s">01:34</a></span> reason that that&#x27;s not a big deal is because first of all, everyone kind of intuitively knows that when humans write code, we generate security issues. When AI models write code, turns out they also generate security issues. And so having security as part of your development life cycle is just like a core part of like modern engineering work, no questions at all. I think the second thing though is a little more interesting. It&#x27;s when you&#x27;re trying to deploy actual autonomous agents into production, how do you do that in a way that allows you to go to sleep easily and not worry</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=2xJoimgoqBg&amp;t=125s">02:05</a></span> you to go to sleep easily and not worry that the agents you deployed are going to go off the rails, do something that they&#x27;re not supposed to do, harm your business or your users or something else, right? And that&#x27;s a much more difficult problem to solve. And then the final thing that I think is a barrier to us, you know, really innovating and moving quickly is almost geopolitics at this point. Like, I don&#x27;t know about all of you, but how many people were kind of annoyed when access to Fable got pulled? Show of hands.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=2xJoimgoqBg&amp;t=157s">02:37</a></span> to Fable got pulled? Show of hands. Yeah, a whole lot of people, right? How many people are a little annoyed they can&#x27;t use the brand new Open AI GPT-5.6 model right now? Yes, a lot of people. And I think it&#x27;s interesting because this is all related to security, right? Like, fundamentally, the biggest problem that I feel we have to still solve in our space is being able to use AI fearlessly and have it be secure by default. And so, that&#x27;s why I&#x27;m really excited to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=2xJoimgoqBg&amp;t=188s">03:08</a></span> so, that&#x27;s why I&#x27;m really excited to announce that right after this keynote, downstairs on the second floor, in room 2005, we&#x27;re going to be running the first security track at the World&#x27;s Fair for the entire day with some of the best companies and presenters in the world talking all about these problems and how we can fix them going forward. So, if security is a concern to you like it is to me, please come downstairs, join us. Again, room 2005, second floor. Uh we have presenters from Nvidia, Anthropic, Keycard, where Ali works, uh Sneak, of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=2xJoimgoqBg&amp;t=219s">03:39</a></span> Keycard, where Ali works, uh Sneak, of course. We have a ton of amazing content and it&#x27;s hopefully going to allow you to level up the stuff that you&#x27;re building and do it without any worry at all. So, that&#x27;s really the goal. So, with that being said, thank you so much for the time, and hopefully I&#x27;ll see you down there. Um I&#x27;m Randall, and I&#x27;ll be emceeing the event all day. All right. Take care, everyone.</p>

</details>
