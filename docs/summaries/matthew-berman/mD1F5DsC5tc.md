---
title: "GPT-5.6 is FINALLY HERE (WOAH)"
channel: "Matthew Berman"
video_id: mD1F5DsC5tc
url: https://www.youtube.com/watch?v=mD1F5DsC5tc
published: 2026-07-09T18:00:10+00:00
generated: 2026-07-13T06:40:16+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/mD1F5DsC5tc/hqdefault.jpg
---
# GPT-5.6 is FINALLY HERE (WOAH)

[![GPT-5.6 is FINALLY HERE (WOAH)](https://i.ytimg.com/vi/mD1F5DsC5tc/hqdefault.jpg)](https://www.youtube.com/watch?v=mD1F5DsC5tc)

[Watch on YouTube](https://www.youtube.com/watch?v=mD1F5DsC5tc) · **Matthew Berman** · 2026-07-09

## TL;DR
GPT-5.6 is a massive, under-marketed leap from GPT-5.5, squeezing every drop of capability from its training run to deliver exceptional browser, computer use, and long-running coding performance. Paired with Codex, it cloned Excel and Minecraft over multi-day runs, while also offering better pricing, tiered model sizes (Luna, Terra, Sol), and reasoning levels—though OpenAI's separate "Fable" model hints at even greater untapped potential.

## Key Takeaways
- GPT-5.6 feels far more capable than a typical point release, representing the pinnacle of the GPT-5 training run.
- Codex + GPT-5.6 ran an 8-word prompt ("make an Excel clone continue until feature parity") for over 5 days, producing a functional single-page HTML Excel clone with formulas, sorting, conditional formatting, and pivot tables.
- The model used computer use during the Excel clone, opening real desktop Excel to reference features and then recreating them.
- Browser and computer use are standout capabilities; the presenter uses Codex's browser as a daily driver for tasks like sorting Gmail and making complex DNS changes.
- A Minecraft clone prompt ran for ~7 days, producing a surprisingly full 3D world with mining, mobs, biomes, farming, inventory, and seed generation.
- Box enterprise benchmarks show GPT-5.6 Sol dominating GPT-5.5 in public sector, life sciences, and healthcare knowledge-work tasks.
- Pricing is significantly improved: $5 vs. $10 per million input tokens and $30 vs. $50 per million output tokens compared to the prior model (Fable).
- GPT-5.6 ships in three sizes—Luna (small), Terra (medium), Sol (large)—each with multiple reasoning levels (up to "Ultra" for Sol).
- Model routing is now practical: plan with Sol, implement with Terra, offload low-requirement work to Luna.
- "Fable" is a distinct, more experimental model that feels like a fresh training run with higher long-term potential, whereas 5.6 is the optimized peak of the existing architecture.

## Detailed Breakdown

**[00:00] A Massive Leap in Capability**
The presenter opens by stressing that GPT-5.6 is a dramatic improvement over GPT-5.5, far beyond what a dot upgrade would suggest. It represents the absolute peak of what the GPT-5 training run can produce.

**[00:31] The Excel Clone Experiment**
Using Codex, the presenter issued a simple 8-word prompt: "/goal make an Excel clone continue until feature parity." The process ran for over five days before being manually stopped. The resulting single-page HTML app includes sorting, formulas, data validation, conditional formatting, tables, find-and-replace, and functional pivot tables. The presenter notes it used computer use—opening the real desktop Excel to reference features and then recreating them in the clone.

**[03:06] Browser and Computer Use**
GPT-5.6's browser and computer use are described as phenomenal. The presenter has adopted Codex's browser as a default driver, using it to sort Gmail and execute complex DNS record changes with a single prompt.

**[03:39] The Minecraft Clone**
A similar prompt—"/goal create a clone of Minecraft, feature parity"—ran for about seven days. Within one day it had a recognizable Minecraft-like world; over subsequent days it expanded with mobs, biomes, mining, farming, inventory, seed generation, and 3D animations. The presenter calls it the best AI-generated Minecraft he has ever produced.

**[05:16] Box Enterprise Benchmarks**
Partner Box ran an "AI complex work eval" covering real knowledge tasks like document reading, number reconciliation, due diligence, and expert-output review. GPT-5.6 Sol outperformed GPT-5.5, Terra, and Luna overall, and dominated across public sector, life sciences, and healthcare subsets. Luna matched Terra's accuracy at lower cost and speed. A link to the full Box benchmark is provided.

**[06:19] Pricing and Token Efficiency**
GPT-5.6 is cheaper and more token-efficient than the prior model (Fable): $5 vs. $10 per million input tokens and $30 vs. $50 per million output tokens. The presenter notes 5.6 has a more direct line of sight to task completion.

**[06:51] GPT-5.6 vs. Fable**
Fable is framed as a fundamentally different, next-generation model. The analogy: GPT-5.6 is a fully optimized, souped-up Honda Civic, whereas Fable is an untouched Ferrari with far higher potential. The presenter links to a separate full review with additional demos.

**[07:56] Model Sizes, Reasoning Levels, and Routing**
GPT-5.6 comes in three sizes—Luna (small), Terra (medium), Sol (large)—each with multiple reasoning levels; Sol reaches "Ultra," described as a quota burner. The presenter advocates model routing: plan with Sol, implement with Terra, deploy with Luna. He wrote a custom Codex skill to automate this delegation and shared a GitHub link.

## Notable Quotes
- "It does not seem like they should have just done a dot upgrade. They have effectively squeezed every drop of juice out of the GPT 5 training run."
- "Just a simple prompt which is effectively eight words long ran for over five days before I manually stopped it."
- "5.6 feels like the absolute pinnacle of an existing model, where Fable feels like we're just scratching the surface on what's possible on a brand new training run."
- "GPT 5.6 is the most souped-up Honda Civic you've ever seen... and Fable is like a Ferrari that hasn't been touched yet."

## People, Tools & References Mentioned
- **Models:** GPT-5.6 (Luna, Terra, Sol), GPT-5.5, Fable
- **Tools / Platforms:** Codex, Codex browser, Claude Code, GitHub, Excel, Minecraft
- **Partners / Services:** Box (Box AI complex work eval), hear.now (demo hosting)
- **Benchmarks:** Box AI complex work eval (public sector, life sciences, healthcare)
- **Custom resources:** Presenter's Codex model-routing skill (GitHub link mentioned)

## Who Should Watch
Developers, AI power users, and anyone evaluating frontier models for long-running agentic coding or enterprise knowledge work will get the most value here, especially those interested in practical model routing and the trade-offs between optimized mature models and next-generation alternatives.


<details class="transcript">
<summary>Full transcript</summary>

<p>Here&#x27;s the thing about GPT 5.6. It is truly a massive leap from GPT 5.5. It does not seem like they should have just done a dot upgrade. They have effectively squeezed every drop of juice out of the GPT 5 training run that they possibly could and the result is one of the most effective models and capable models that I have ever used. One of the first loops that I gave it was super simple. Look at this. /goal make an</p>
<p>simple. Look at this. /goal make an Excel clone continue until feature parity. Here is the thing about 5.6 plus Codex. It has all the tools in its tool belt to do this really well. Just a simple prompt which is effectively eight words long ran for over five days before I manually stopped it. And here is what it created. This is the Excel clone and it has a lot of the features that Excel has. And if I would have let Codex keep churning through tokens it probably would have gotten even further. All</p>
<p>would have gotten even further. All right. So here very simple we have a list of numbers. You can easily sort it by ascending descending. If I add another number in there, same thing. And everything is just super fast, works really well. We have all the formulas. So let&#x27;s say equals this plus this nine. And if you double click into it, you get the formula up in this input bar up here like normal. We can add another one minus 43. Hit enter and everything just</p>
<p>minus 43. Hit enter and everything just works. So we have a bunch of standard Excel features. We have data validation conditional formatting. We have tables, find and replace, obviously toggling and sorting very easy. We have all of these different formula that you can use right from this single page HTML app. Remember, Excel is a massive piece of software and a lot of the functionality has been condensed down into this very simple app. You can go try this out, which I&#x27;ll drop a link down below for that. Shout out to hear.now for hosting</p>
<p>that. Shout out to hear.now for hosting all of the demos you&#x27;re going to see today. It also has really deep analysis capabilities, including pivot tables. Look at how easy this is. Simply select some data with headers. You get all the rows sorted out. You get filters. You can create the pivot table. And look at that. We actually have a full pivot table. Done. And again, this ran for 5 days. Imagine how long it took to actually create Excel. Took years and years and years to get it to where it is. And obviously this is a subset of the total functionality. And obviously</p>
<p>the total functionality. And obviously as you can see here, there are some rough edges. But again, I stopped it after 5 days. And it was not anywhere close to being done. And here&#x27;s the interesting bit. It used computer use. It opened up Excel on my desktop and would just go back and forth between doing something in Excel, the actual Excel, and then recreating it in this new cloned version. And that is one of the things that GPT 5.6 is so incredible at. Browser use and computer use.</p>
<p>at. Browser use and computer use. It is phenomenal at browser use. I really cannot overstate that. Codex&#x27;s browser has increasingly become my default, my main driver browser because I can just get stuff done with it. I can open up Gmail and have it sort through my emails. I&#x27;ve done complex DNS record changes easily with just one prompt with Codex browser use. And of course I had it clone Minecraft. I did {slash} goal once again and I just said, &quot;Create a clone of Minecraft, feature parity.&quot; And</p>
<p>clone of Minecraft, feature parity.&quot; And it went for something like 7 days before I finally stopped it. And it took only about 1 day to get what looked like actual Minecraft. But what it kept doing was going deep and would build out parts of the world that didn&#x27;t exist before. Would build out mobs that came straight from the actual game of Minecraft, different biomes, and it would just continue churning and just trying to get to feature parity. And it was just so impressive. And watch this. This is definitely the best version of Minecraft</p>
<p>definitely the best version of Minecraft that I&#x27;ve ever created using AI. All right, so here we go. You can see the shadowing is really nice. Here I can mine the grass blocks pretty easily. Really cool 3D animation when you do that. You can pick up all the blocks that you just mined. Here we have miniature carrots. There&#x27;s some carrots. We have farmland. And yeah, and it just works really, really well. Here&#x27;s a tabby cat. Here I broke the glass. And so it is just incredibly impressive. It is a very full world, more full, more realistic than any other Minecraft that</p>
<p>realistic than any other Minecraft that I&#x27;ve ever created. You can generate different seeds. Here it is. Here&#x27;s that new world I just created. Here is my full inventory. Very easy to use. Very, very cool. And of course our friends and partner on this video, Box, has put together their own benchmarks on enterprise-grade work. Let&#x27;s take a look. We have Box AI complex work eval for GPT 5.6, Soul, Terra, and Luna. And Box&#x27;s benchmark tests real knowledge work, like reading documents, reconciling numbers, doing due diligence, and reviewing expert output</p>
<p>diligence, and reviewing expert output for errors. We have GPT 5.5 on the accuracy. 63.3, Terra at 59%. So obviously a drop from Soul, even a drop from 5.5. We have 5.6 Luna basically getting the same score as Terra, but much faster and much less expensive. Here we have industry subsets. We have the public sector, life sciences, and healthcare. All three Soul dominated GPT 5.5. Thanks to our partners at Box for</p>
<p>5.5. Thanks to our partners at Box for putting together this awesome benchmark. I&#x27;m going to drop a link down below where you can read more about their benchmark and specifically how GPT 5.6 did on it. All three of these models are coming soon to Box AI, so go check them out. I&#x27;ll drop a link down below. The pricing is also much better for GPT 5.6. Not only is it less expensive, but it uses less tokens to get to the same result. So, $5 per million input tokens versus $10 for Fable, much cheaper on cash hits, and 30 versus 50 dollars per</p>
<p>cash hits, and 30 versus 50 dollars per million output tokens. So, again, you&#x27;re just paying less, and it just feels like 5.6 has a more direct line of sight to accomplishing the task versus Fable. Now, with all of that said, Fable is something else. It feels much more like a brand new model, something that I hadn&#x27;t used ever before, and it is very impressive. It sees around corners better than GPT 5.6. Here&#x27;s the best way to explain it. 5.6 feels like the absolute pinnacle of an existing model,</p>
<p>absolute pinnacle of an existing model, where Fable feels like we&#x27;re just scratching the surface on what&#x27;s possible on a brand new training run. That&#x27;s the difference. Here&#x27;s an analogy for you. It&#x27;s kind of like GPT 5.6 is the most souped-up Honda Civic you&#x27;ve ever seen. Every single horsepower has been squeezed out of it. The tires are optimized for speed. There&#x27;s a spoiler, everything. And Fable is like a Ferrari that hasn&#x27;t been touched yet, fresh [snorts] off the manufacturing line, unoptimized, and the potential is just</p>
<p>unoptimized, and the potential is just so much higher there. So, I put together a full review. I have a bunch of demos of things that I&#x27;ve built, including an actual operating system. We have a Rube Goldberg lab that you can use. All of this is available on it. I&#x27;m going to drop a link to the full review down below. And here&#x27;s the other thing that is very different about GPT 5.6 versus Fable. It comes in three different model sizes, Luna the smallest, Terra the medium, and Sol the largest. But even within those, you have multiple levels of reasoning. And if we choose Sol, you</p>
<p>of reasoning. And if we choose Sol, you get all the way up to Ultra, which is, you know, basically a quota burner. And so we&#x27;ve been talking a lot about model routing lately, where maybe you&#x27;re using Fable for planning, and then you can actually call Codex from within Claude Code and delegate off to GPT-5.5. And now you can kind of just do everything with the GPT series of models. You plan with Sol, maybe you do most of the implementation with Terra on, you know, high reasoning, and then for stuff like deploying or other kind of low requirement work, you offload to Luna.</p>
<p>requirement work, you offload to Luna. And so now you have all these different sizes, all these different thinking effort settings for these different models, and you can come up with a really nice skill to delegate between them. And by the way, I wrote a skill just for that. And if you want it, I&#x27;m going to drop a GitHub link down below, so you can delegate all within Codex, and save yourself a bunch of your quota, and get basically the same quality performance.</p>

</details>
