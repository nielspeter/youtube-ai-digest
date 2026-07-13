---
title: "I Let Strix Attack My App... Here’s What It Found"
channel: "Better Stack"
video_id: vRTliPb8fjg
url: https://www.youtube.com/watch?v=vRTliPb8fjg
published: 2026-07-09T15:00:27+00:00
generated: 2026-07-13T06:41:14+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/vRTliPb8fjg/hqdefault.jpg
---
# I Let Strix Attack My App... Here’s What It Found

[![I Let Strix Attack My App... Here’s What It Found](https://i.ytimg.com/vi/vRTliPb8fjg/hqdefault.jpg)](https://www.youtube.com/watch?v=vRTliPb8fjg)

[Watch on YouTube](https://www.youtube.com/watch?v=vRTliPb8fjg) · **Better Stack** · 2026-07-09

## TL;DR
Strix is an open-source AI security tool that deploys a team of AI agents to actively break into your application, prove the exploit works, and generate a pull request with the fix. It's a fast, validated alternative to expensive manual penetration testing, though it has real limits around cost, speed, and handling complex logic chains.

## Key Takeaways
- Strix uses a crew of AI agents to perform penetration testing, with different agents handling recon, OWASP Top 10 vulnerabilities, and API attacks.
- Unlike traditional scanners that bury you in "what-ifs," Strix proves vulnerabilities by actually exploiting them and providing working proof.
- It generates pull requests with the exact fixes for the vulnerabilities it finds.
- Setup is minimal via a curl command, and it supports models like Claude, Gemini, or local Llama models.
- It runs in a Docker sandbox to ensure the agents' actions don't impact your actual systems.
- A quick scan takes about 10 minutes and costs roughly $3–$5 in tokens, depending on the project size.
- It achieves a 96% solve rate on the X bin exploitation benchmark in about 19 minutes per challenge.
- It can be integrated into CI/CD pipelines via GitHub Actions to block bad merges before they land.
- It struggles with complex logic and long chain attacks, making it better suited for routine, repeatable checks rather than replacing human penetration testers entirely.
- It should be used as one layer of a multi-layered security strategy, not as a standalone defense.

## Detailed Breakdown

**[00:00] Introduction to Strix**
The video opens with the common scenario of shipping clean code that passes tests, only to have a hidden bug cause a database breach. The host introduces Strix, an open-source, free tool with nearly 38,000 GitHub stars, designed to show exactly how a break-in could occur.

**[00:30] What Strix Does**
Strix spins up a team of AI agents that act like hackers. One agent performs reconnaissance and maps the app, while others target OWASP Top 10 vulnerabilities, APIs, SQL injection, cross-site scripting, and broken access control. The host emphasizes its value for teams without the budget for a professional penetration test, noting that unlike traditional scanners that generate a pile of "what-ifs," Strix actually breaks in, proves the exploit, and hands you a pull request.

**[01:00] Setup and Demo App**
Setting up Strix is done via a single curl command. The host demonstrates using a simple FastAPI expenses app running on a live UI. To run a scan, a single command is used: `Strix target`, pointing to the code path and live UI, with the scan mode set to "quick." The tool requires an API key from a provider like Anthropic, but it also supports Gemini or local Llama models. A key requirement is that Docker must be running, as Strix pulls a sandbox container on the first run to safely execute agent actions.

**[02:30] Reviewing the Results**
A quick scan takes about 10 minutes. The host shows that instead of just suggesting a vulnerability might exist, Strix found the endpoint, wrote a working exploit, ran it, extracted data, and provided the exact steps and the fix. The host notes that while you can change the scan mode, deeper scans take longer and consume more tokens.

**[03:05] How Strix Compares**
Strix is compared to manual penetration testing (accurate but slow and expensive) and static scanners (fast and cheap but don't run code). Strix differentiates itself by having agents communicate in chain attacks, running in a sandbox, and closing the loop with auto-fix pull requests. It boasts a 96% solve rate on the X bin exploitation benchmark, taking about 19 minutes per challenge on real break-in tasks.

**[03:37] Practical Usage and CI Integration**
Strix is a command-line tool with native GitHub Actions support, working on both open-source code and live apps. Its biggest strength is validated findings—every real bug comes with working proof, eliminating the "400 maybes" problem. It exits with an error code when it finds an issue, allowing it to block bad merges in a CI pipeline before they land.

**[04:07] Limitations and Final Thoughts**
Strix is open-source under the Apache 2.0 license with no model lock-in, but it has limitations. Its performance depends heavily on the model used; weak local models yield weak findings, while strong models cost significant tokens. Deep scans can take hours, Docker adds friction, and it struggles with complex logic and long chain attacks. The host recommends using it for pre-merge checks, side projects, and staging environments to catch obvious issues before production. It should be viewed as one layer in a multi-layered security strategy, sitting alongside existing scanners and human review.

## Notable Quotes
- "Most tools tell you your door might be unlocked. Strix found the endpoint, wrote a working exploit, ran it, pulled data out, and gave me the exact steps here."
- "You're basically renting a hacker for a minute or two or however long this takes."
- "Think of security as layers, not a single wall. Strix is one strong layer."

## People, Tools & References Mentioned
- **Strix** - The open-source AI security tool featured in the video.
- **OWASP Top 10** - A standard awareness document for web application security, referenced as a target for Strix's agents.
- **FastAPI** - The Python framework used to build the demo expenses app.
- **Docker** - Used to create a sandbox environment for Strix's agents to operate safely.
- **Anthropic (Claude), Gemini, Llama** - LLM providers supported by Strix.
- **GitHub Actions** - Mentioned for native CI/CD integration.
- **X bin exploitation benchmark** - A benchmark where Strix achieved a 96% solve rate.
- **Apache 2.0** - The open-source license under which Strix is released.

## Who Should Watch
Solo developers, small teams, and DevOps engineers without a dedicated security budget who want an automated, proof-backed way to catch common vulnerabilities before shipping code.


<details class="transcript">
<summary>Full transcript</summary>

<p>Your tests pass, the code is clean, you ship, and you&#x27;re done. Then something happens to your database through a bug you were never going to see in the first place. This thing that just shows me exactly how that break-in happened, and it isn&#x27;t some hack. It&#x27;s open source, it&#x27;s free, it&#x27;s sitting at almost 38,000 stars on GitHub, and this thing has a name. This is Strix. Let me show you what it does and where it falls apart.</p>
<p>So, what is this thing? Strix spins up a</p>
<p>So, what is this thing? Strix spins up a team of AI agents that behave as hackers, similar to some pen test tools, but not one model is taking a guess, it&#x27;s a crew of them. One agent does recon and maps your app, another goes after the OWASP top 10 and your APIs, SQL injection, cross-site scripting, broken access control, the stuff that actually gets shipped. Here&#x27;s why this matters to us, because a lot of us don&#x27;t have a team and we don&#x27;t have a bunch of money laying around for a pen test. So, we either ignore the problem or you run a scanner that buries you in a ton of</p>
<p>a scanner that buries you in a ton of what-ifs. Strix doesn&#x27;t do that. It doesn&#x27;t say this might be exploitable. It breaks in, proves it, and hands you it as a pull request. Now, let me show you all this in action. All right, now you&#x27;d expect setting up would be a lot, but in reality, this is one line. If fired up with a curl command to install it, that is what installs this. Now, here is a fast API app for expenses just built out, and it&#x27;s running on this UI, which you can see here. I added one expense, which is subscribe to the</p>
<p>expense, which is subscribe to the Better Stack channel. I put one cent, but in reality, subscribing is always free, and you learn a ton from our countless videos coming out all the time. Now that we have Strix, I can run this one command here. Strix target. I&#x27;m going to put my code path in the live UI, then I&#x27;ll add the scan mode quick. I&#x27;m just giving Strix a model to use here. I&#x27;m using my Anthropic API here, but it takes Claude, Gemini, or even a stronger Llama model if you want to keep it local. This command targets my live site and my project together. One catch</p>
<p>site and my project together. One catch here, it pulls a docker sandbox on the first run, so docker does need running. The sandbox lets the agents actually act without the blast hitting your systems. Then I pointed at a small app, my app that I built. I wrapped some off and a database to it, and that&#x27;s the one rule. You only ever run this on something that you have permission to test. Now, you think it fires back results instantly, it doesn&#x27;t. Does any pen test tool do that? A quick scan here took about 10 minutes. All right, so but I&#x27;ll speed that up for you. Let me cook this and</p>
<p>that up for you. Let me cook this and let me grab a coffee in the meantime. All right, with that coffee in hand, we can take a look at this now. Now, most tools tell you your door might be unlocked. Strix found the endpoint, wrote a working exploit, ran it, pulled data out, and gave me the exact steps here. Plus the fix, it told me what&#x27;s wrong. This is everything I got back from Strix. After a little bit of time running on the quick mode. You could change quick mode, but that&#x27;s going to take a lot longer, and it&#x27;s going to rack up more tokens. So, how is this different from many of the others</p>
<p>different from many of the others already out there? Manual pen test is accurate, but it&#x27;s slow and it&#x27;s pricey. A static scanner is fast and cheap, but it never really runs our code, and other AI tools exist. They do, right? Here&#x27;s where Strix kind of pulls ahead or changes it a little bit. The agents talk to each other in chain attacks. It&#x27;s all sandboxed, and it closes the loop with auto fix pull requests. On the X bin exploitation benchmark, it hits a 96% solve rate around 19 minutes per challenge. And those are real break-in</p>
<p>challenge. And those are real break-in tasks, not multiple-choice detection. How would you actually use this? Well, it&#x27;s a command-line tool with native GitHub actions support, and it works on open-source code and a live app. Ship Python drops right in. Now, the best part by a mile is validated findings. Every real bug here comes with working proof. So, that 400 maybes pile just disappears. See, I hook is clean. It exits with an error code when it finds something. So, you can start straight-up block a bad merge before it even lands.</p>
<p>block a bad merge before it even lands. So, open source Apache 2.0 brings your own model with no lock-in and it&#x27;s strong on APIs and web apps. And it mostly held up, but it&#x27;s got real limits as well. It leans hard on the model you give it. You&#x27;re basically renting a hacker for a minute or two or however long this takes. A weak local model gives weak findings. A strong one, it costs a lot of tokens. Budget three, maybe $5 for a quick scan. It depends on how big your project is. Deep scans are slow. They&#x27;re hours. They&#x27;re not minutes. And Docker adds friction. And</p>
<p>minutes. And Docker adds friction. And on the really messed-up stuff, complex logic, long chain attacks, it&#x27;s not quite there yet. It&#x27;s pretty cool for routine repeatable checks, but maybe not a stand-in for a human on your actual systems, depending on how big they are. So, do you actually run this? I mean, yeah, you could. Where I&#x27;d reach for it maybe is pre-merge checks, side project staging, catching the obvious stuff before production. Wired in your pipeline, let it run on real changes and see what happens. As your only defense on a critical system with a bit of setup, maybe not. Think of security as</p>
<p>setup, maybe not. Think of security as layers, not a single wall. Strix is one strong layer. Validated feedback in CI sitting next to your existing scanners for coverage and a human review for the hard calls. That&#x27;s just an idea. If you care about shipping secure code faster, this is a pretty sweet open source tool and it&#x27;s free to try with your own keys. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
