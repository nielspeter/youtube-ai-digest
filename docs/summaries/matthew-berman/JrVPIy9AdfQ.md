---
title: "Did Kimi K3 really beat Fable?"
channel: "Matthew Berman"
video_id: JrVPIy9AdfQ
url: https://www.youtube.com/watch?v=JrVPIy9AdfQ
published: 2026-07-18T06:14:32+00:00
generated: 2026-07-18T09:49:31+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/JrVPIy9AdfQ/hqdefault.jpg
---
# Did Kimi K3 really beat Fable?

[![Did Kimi K3 really beat Fable?](https://i.ytimg.com/vi/JrVPIy9AdfQ/hqdefault.jpg)](https://www.youtube.com/watch?v=JrVPIy9AdfQ)

[Watch on YouTube](https://www.youtube.com/watch?v=JrVPIy9AdfQ) · **Matthew Berman** · 2026-07-18

## TL;DR
Moonshot AI released Kimi K3, a 2.8-trillion-parameter open-weights model that tops Arena AI's front-end development benchmark, beating Fable 5 and GPT 5.6. While it delivers frontier-level coding and writing performance at roughly half the per-token price, it consumes roughly twice as many tokens—making its effective cost similar to closed-source rivals. The release underscores the competitive pressure Chinese open-source labs are placing on US frontier labs, though Matthew Berman argues US closed-source leaders likely remain 8–10 months ahead internally.

## Key Takeaways
- Kimi K3 is the largest open-source model to date at 2.8 trillion parameters, with a one-million-token context window, designed for long-horizon coding, knowledge work, and reasoning.
- It ranks #1 on Arena AI's front-end development benchmark at 76%, ahead of Fable 5 (63%) and GPT 5.6.
- Pricing is $3 per million input tokens and $15 per million output tokens—about half of GPT 5.6 Soul's price.
- However, Deep Suite's analysis shows Kimi K3 uses roughly twice as many tokens per task, making its effective cost comparable to GPT 5.6 Soul at ~$4.70 per task.
- Kimi K3 also claims #1 on an internal writing benchmark (2840 ELO), surpassing Claude Fable 5, and tops Verscell's Next.js evals at 92% success rate.
- Caveats apply: some benchmarks are saturated, and Anthropic previously accused Moonshot of distillation attacks (training on Anthropic's data).
- Berman believes US closed-source labs (OpenAI, Anthropic) are still roughly 8–10 months ahead because they hold back finished models for safety and post-training optimization.
- Open-source releases from Chinese labs benefit the entire AI stack—cheaper models, more tokens consumed (Jevons' paradox), better applications, more inference revenue, and more Nvidia chip sales.
- The geopolitical risk is that if US enterprise builds on Chinese open-source models optimized for Chinese chips, it could create dependency on Chinese hardware.
- Berman's hands-on Rubik's Cube simulator test succeeded: the model built a working 3D cube with reflections, correct scrambling, and a perfect solve, though it took over 30 minutes.

## Detailed Breakdown

### Introduction and the "DeepSeek Moment" Claim [00:00](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=0s)
Berman opens by calling Kimi K3's release potentially "the next DeepSeek moment," positioning it as the best open-source/open-weights model available and competitive with Fable 5 and GPT 5.6 on certain metrics. He teases a Rubik's Cube simulator test running in the background.

### The Arena AI Front-End Development Benchmark [00:31](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=31s)
The headline result: Kimi K3 tops Arena AI's front-end development benchmark at 76%, beating Fable 5 (63%) and GPT 5.6. Berman emphasizes the margin is not small and calls it remarkable that an open-source model leads the world in this category.

### Model Specs and Context Window [01:33](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=93s)
Kimi K3 is a 2.8-trillion-parameter model—the largest open-source model to date—requiring data-center-grade hardware to run. It features a one-million-token context window and is designed for long-horizon coding, knowledge work, and reasoning. Berman contrasts it with Thinking Machines' 975-billion-parameter model, noting Kimi K3 is both larger and more intelligent.

### Demo Video and 3D Asset Creation [02:37](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=157s)
Berman shows a one-minute demo that Kimi K3 itself edited. The demo features real-time reflections, dynamic daylight cycles, and a Red Dead Redemption-style simulated world, highlighting the model's strength in 3D asset creation and design.

### Pricing and the Intelligence-Density Question [03:08](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=188s)
At $3/M input and $15/M output, Kimi K3 is roughly half the price of GPT 5.6 Soul. But Berman introduces the concept of "intelligence density"—cost per unit of intelligence—warning that if a model uses twice the tokens for the same output, the effective price is identical.

### Deep Suite Cost-vs-Performance Analysis [03:39](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=219s)
On Deep Suite's scatter plot (cost per task vs. completion success rate), Kimi K3 Max sits just below GPT 5.6 Soul at roughly the same ~$4.70 per-task cost. This confirms that Kimi K3's lower per-token price is offset by higher token consumption. GPT 5.6 Soul Max remains #1 overall but at roughly double the price.

### David Sacks and the Geopolitical Angle [05:13](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=313s)
US AI czar David Sacks flagged Kimi K3's #1 ranking as a concerning first for a Chinese model. Berman tempers the alarm, noting GPT 5.6 and Fable 5 remain more generalized models that perform better across the board. He also argues that US regulatory patchwork slows domestic frontier labs, while Chinese labs face fewer such constraints.

### Verscell's Next.js Evals and Writing Benchmark [06:45](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=405s)
Verscell CEO Guo Lush reports Kimi K3 is the best-performing model on Next.js.org evals at 92% success, the first time an open model has beaten all proprietary ones on that web-engineering benchmark. Separately, an internal writing benchmark places Kimi K3 #1 at 2840 ELO, jumping from place 21 over its predecessor Kimi K2.6, and five times cheaper than the model it displaced.

### Caveats: Benchmark Saturation and Distillation Allegations [07:47](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=467s)
Berman adds significant caveats: many benchmarks are saturated, and Anthropic previously accused Moonshot of distillation attacks—training Kimi K3 on data derived from Anthropic's models. He notes the model is genuinely open-source with revealed algorithmic unlocks, but real validation requires production-environment testing.

### Why US Closed-Source Labs Are Still Ahead [08:49](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=529s)
Berman argues Chinese open-source labs release models the moment they're baked, whereas US labs like Anthropic and OpenAI hold finished models for months of safety evaluation and post-training (citing Mythos, which Anthropic had in January before public release). He estimates US closed-source labs remain 8–10 months ahead internally.

### Who Wins When Open Source Gets Better [10:23](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=623s)
Berman frames the release as broadly positive: cheaper, better models trigger Jevons' paradox (more tokens consumed), better applications get built, inference providers earn more, and Nvidia sells more chips. The one risk is strategic dependency on Chinese chips if US enterprise standardizes on Chinese open-source models optimized for that hardware.

### The Rubik's Cube Test Result [10:53](https://www.youtube.com/watch?v=JrVPIy9AdfQ&t=653s)
After roughly 30 minutes of generation—slower than expected and a noted criticism of Kimi K3—the simulator completed successfully. The 3D cube featured side reflections, correct scrambling, and a perfect solve, confirming Kimi K3 can handle complex interactive 3D tasks.

## Notable Quotes
- "This might be the next DeepSeek moment."
- "Kimmy K3 at the top above Fable 5, above GPT 5.6. That means in front-end development, Kimmy K3 is the best model on the planet right now."
- "If you're using twice as many tokens for the same amount of intelligence, then the price is effectively the same."
- "I still think that Anthropic is probably 8 to 10 months ahead of open source."
- "Ultimately when there's really good open-source models, every part of the AI stack wins, maybe with the exception of the closed source labs."

## People, Tools & References Mentioned
- **Moonshot AI** — developer of Kimi K3
- **Kimi K3** — 2.8T-parameter open-weights model; 1M-token context window
- **Fable 5 / Claude Fable 5** — Anthropic frontier model used as comparison
- **GPT 5.6 / GPT 5.6 Soul / GPT 5.6 Soul Max** — OpenAI frontier models used as comparisons
- **Thinking Machines** — released a 975B-parameter open-source model
- **Arena AI** — front-end development benchmark
- **Deep Suite** — cost-vs-performance benchmarking tool
- **Verscell / Guo Lush** — Next.js.org web-engineering evals
- **David Sacks** — US AI czar
- **Anthropic** — accused Moonshot of distillation attacks; referenced re: Mythos model timeline
- **OpenAI** — referenced re: GPT 6 internal testing
- **forwardfuture.com** — Berman's newsletter and original essays
- **Jevons' paradox** — economic concept referenced re: token consumption
- **Nvidia** — chip sales beneficiary of broader open-source adoption

## Who Should Watch
AI developers, engineers, and observers tracking the open-source-vs-closed-source frontier race—especially those interested in coding and front-end development benchmarks, cost-per-intelligence tradeoffs, and the US-China AI dynamic. The video balances benchmark hype with practical caveats about token efficiency and geopolitical risk.


<details class="transcript">
<summary>Full transcript</summary>

<p>Moonshot AI just dropped Kimmy K3 and I&#x27;m out here baking in the 100 degree heat to tell you about it. This might be the next deepseek moment. This Chinese AI lab just dropped the best open-source open weights model on the planet. And it&#x27;s actually competitive with Fable 5 and GPT 5.6, at least on some measurements. But there&#x27;s more to this story than just a really good model. And if you like when I review open-source models, hit the like button, subscribe</p>
<p>models, hit the like button, subscribe to the channel. It very much does help. Thank you in advance. And also, I just kicked off the Rubik&#x27;s Cube simulator with Kimmy K3. It&#x27;s being built right now. Stick around to the end of the video. I&#x27;ll reveal how it actually did. So, this is the benchmark that everybody is pointing at and saying, &quot;Wow, China and specifically open- source has finally reached the frontier.&quot; And in fact, it actually beat the frontier. This is Arena AI&#x27;s front-end development benchmark. And what do we see? Kimmy K3</p>
<p>benchmark. And what do we see? Kimmy K3 at the top above Fable 5, above GPT 5.6. That means in front-end development, Kimmy K3 is the best model on the planet right now. And that is wild. And by the way, it&#x27;s not by a small margin. Here it is. 76% versus number two, Fable 5 at 63%. All right, so let me get into the details for a minute before I show you the bigger picture of this story. First, this is Kimmy K3. This is a 2.8 trillion</p>
<p>this is Kimmy K3. This is a 2.8 trillion parameter model that is the biggest open-source model to date. And no, you probably cannot run this on your home computer. This is one of those models that&#x27;s going to need to be served by a data center. It also has a million token context window, which is excellent. It is designed for long horizon coding, knowledge work, and reasoning. Now, I know I&#x27;ve talked a lot about US versus China in the AI race. And I made an entire video about how the economics around US open- source are not favorable</p>
<p>around US open- source are not favorable to building the best open source models on the planet. And what do we see? Look at this. Thinking Machines, which just released what is their bestin-class open- source model, 975 billion parameters, and really pales in comparison to Kimmy K3, coming in at 2.8 trillion. And yes, size is not everything. But Kimmy K3 is also just significantly better on the intelligence scale. All right, let&#x27;s watch this one minute demo video from Kimmy K3. And as</p>
<p>minute demo video from Kimmy K3. And as you watch it, I want you to keep something in mind. Kimmy K3 was the model that actually edited the video. Check this out. So, create a new character. Let&#x27;s see. There we go. By the way, I keep hearing it is incredible at design. It is incredible at 3D asset creation. And that&#x27;s what we&#x27;re seeing here with that entire simulated world. Add real-time reflections, dynamic daylight cycled. It&#x27;s basically building a video game. And it looks really good. This is like Red Dead Redemption style. So, you get the picture. Well, what is open source really known for? It is</p>
<p>open source really known for? It is known for efficiency and cost. If you&#x27;re using an open source model, you should expect to pay far less than going with a Fable 5 or a GPT 5.6. And it&#x27;s kind of the case. Let me show you. So, for the million tokens, Kim K3 input price with a cash mix, $3 per million input, $15 per million output. To put that in perspective, that is about half the price of GPT 5.6 six soul, which sounds inexpensive, but that&#x27;s not all there is</p>
<p>inexpensive, but that&#x27;s not all there is to the picture. You also have to factor in the intelligence density. What is the intelligence per token? Because if you&#x27;re using twice as many tokens for the same amount of intelligence, then the price is effectively the same. I&#x27;m going to show you that in a second. All right. So, currently my favorite benchmark out there, Deep Suite, which really has just nailed what kind of the public perception of all of these models are. Here&#x27;s what it has to say about Kimmy K3. Now, on the X-axis, over here on the bottom, we have average cost per</p>
<p>on the bottom, we have average cost per task. The more to the right, the better. That&#x27;s cheaper. Over here on the Yaxis, we have the completion success rate. So, what you&#x27;re looking for is up here. The farther up it is, and the farther to the right it is, the better. Now, what we&#x27;re seeing here is Kimmy K3 Max sits right there, right under GPT 5.6 Soul. However, it&#x27;s effectively the same price. They&#x27;re both about $4.70. Now, what does that actually mean? That means Kimmy K3, given that it is half</p>
<p>means Kimmy K3, given that it is half the price, takes twice the amount of tokens for the same exact task. And the number one model on this right now is GPT 5.6 Soul Max right there. But then you&#x27;re basically doubling the price. And here&#x27;s Fable if you were wondering. And by the way, if you want to learn more about open source, we actually have a number of incredible original essays on forwardfuture.com. Go to forwardfuture.com, subscribe to our newsletter, and really stay uptodate on the latest on all things artificial</p>
<p>on the latest on all things artificial intelligence. Now, here is David Saxs, the AI ZAR of the United States. This is concerning. For the first time, a Chinese model Kimmy Kade 3 has taken number one on the front-end code arena and is scoring at or near the frontier on other benchmarks. Now, I don&#x27;t know if that&#x27;s actually true. It&#x27;s probably fairing pretty well, but still GPT 5.6 and Fable are more generalized models. They do better across the board than Kimmy K3. Now, I don&#x27;t want to go too</p>
<p>Kimmy K3. Now, I don&#x27;t want to go too deep into the politics in this video. I&#x27;ve already covered China versus the United States plenty, but what David Sax is pointing out here is as we continue, we as the United States regulate our AI industry, have kind of this patchwork of AI regulation across all of the states in the United States. It really slows down our frontier labs. And don&#x27;t forget, Fable was released, pulled down, GPT 5.6 was delayed for weeks. This all</p>
<p>GPT 5.6 was delayed for weeks. This all allows China to continue to release incredible models much more quickly because they don&#x27;t have to follow our rules. And I&#x27;m not saying China is bad here. I&#x27;m not saying these Chinese AI labs are bad. In fact, quite the opposite. Look at what they&#x27;re doing. They are releasing insanely good models for free, open sourcing them, and open weighting them. I can&#x27;t say anything negative about that. I am grateful that they&#x27;re doing this, and I&#x27;m going to touch more on that later in the video. Now, here&#x27;s GMO Roush, the CEO and co-founder of Verscell. Kim K3 is the</p>
<p>co-founder of Verscell. Kim K3 is the best performing model on Nex.js.org. Evals, ahead of Fable, reaching a comparable success rate in less time. This is the first time that an open model is ahead of all proprietary ones for this comprehensive web engineering benchmark. And if you see me sweating, it&#x27;s not because I&#x27;m getting nervous about Chinese AI. It is literally 100° out here. Yeah. So, here&#x27;s the success rate coming in at 92% on the agent performance results. Success with agents.md, the number one model on the planet right now. Here&#x27;s another one.</p>
<p>planet right now. Here&#x27;s another one. Turns out Kimmy K3 is also really good at writing. So, big news from our internal writing benchmark early results. Kimmy K3 is our now number one for writing in our editorial voice 2840 ELO, surpassing Claude Fable 5. That jump is from place 21 to number one over its predecessor Kimk 2.6. five times cheaper than the model it just displaced at the top. So, it&#x27;s it&#x27;s much much cheaper at writing. Now, here&#x27;s where we have to add caveats left and right. Can</p>
<p>have to add caveats left and right. Can we actually trust these benchmarks? A lot of these benchmarks have been completely saturated. And remember, Anthropic did accuse Moonshot of distillation attacking their models, meaning they basically stole data from Anthropic to train the Kimmy K3 model. That is Anthropic&#x27;s claim. Now, whether they stole enough data to be meaningful, who knows? But here&#x27;s the thing, it&#x27;s open source. You can actually go look at exactly how they built the model. You can replicate it. Technically, it&#x27;s open</p>
<p>can replicate it. Technically, it&#x27;s open source and open weights. They revealed all of their algorithmic unlocks, which thank you. Amazing. But we won&#x27;t know until we actually test it thoroughly, actually in production environments. But what have I been saying for a while? It turns out you don&#x27;t need the absolute frontier for the vast majority of work, especially in the enterprise. I know you&#x27;re probably sick of me saying that by now, but it&#x27;s awesome that Moonshot released this open source, but it&#x27;s also definitely a threat to the United States</p>
<p>definitely a threat to the United States and it is a threat to the Frontier Labs. Those are two different things, by the way. Now, here&#x27;s the thing. You might be thinking, &quot;Wow, China and open source in general is at the frontier along with the closed source US labs.&quot; That is not true. What happens with these open source labs, especially the Chinese labs, is the minute they&#x27;re done baking the model, they release it to the world. However, Fable 5.1, Fable 5.2 has probably already been baked. Anthropic is just testing it. So I still think</p>
<p>is just testing it. So I still think that Anthropic is probably 8 to 10 months ahead of open source because remember we found out Anthropic had Mythos way back in January, 5 months before they actually released it publicly. That&#x27;s probably what both of the major labs, OpenAI and Anthropic are doing right now. GPT6 is probably being tested thoroughly internally at OpenAI right now. They&#x27;ve probably had it for months. They&#x27;re just doing all of their safety evaluations. They&#x27;re making sure that they&#x27;re doing kind of the post training properly, extracting the most</p>
<p>training properly, extracting the most they can out of the model. So, I still think US closed source labs are far in the lead. We&#x27;re still way out there. And again, I want to say it&#x27;s awesome that these Chinese labs are open sourcing their models because guess what? It helps everybody, including US Open source and open AI and Enthropic. It helps everybody. and they have all of these incredible algorithmic discoveries with Kimmy K3 and they just give it away for free. It&#x27;s incredible and it puts a lot of pressure and increased competition on the US closed source</p>
<p>competition on the US closed source labs. And here&#x27;s the thing, ultimately when there&#x27;s really good open-source models, every part of the AI stack wins, maybe with the exception of the closed source labs. That&#x27;s it. Every other part of the stack wins because models get better. they get cheaper which means Javon&#x27;s paradox more tokens get used better applications get built on top of it the inference providers make more money and of course Nvidia sells more chips so it&#x27;s kind of good across the</p>
<p>chips so it&#x27;s kind of good across the board that China is open-sourcing these models the risk which I&#x27;ve detailed thoroughly in other videos is that if US enterprise gets built on top of Chinese open source models and then these Chinese open source models are optimized for Chinese chips that will make us dependent on Chinese chips. That is a big problem. Now, by the way, I kicked off the Rubik&#x27;s Cube experiment 30 minutes ago and it is still going. And this is one of the criticisms I&#x27;ve heard about Kimmy K3. It is quite slow. So, it is token hungry</p>
<p>is quite slow. So, it is token hungry and slow and hopefully it finishes soon. And in fact, right after this, I&#x27;m just going to show you a quick demo of it. But for now, it hasn&#x27;t finished after about 30 minutes. And by the way, here we go. The Rubik&#x27;s Cube finished. Let&#x27;s check it out. It looks really good. I can see the reflections on the side of the cube right there. Let&#x27;s try scrambling it. Scramble looks correct. Everything looks really good there. And let&#x27;s see what happens when we solve it. It looks like it&#x27;s going to solve it.</p>
<p>It looks like it&#x27;s going to solve it. There it is. Perfect. So, works really well. This is another model that can absolutely crush the Rubik&#x27;s Cube. And by the way, I detailed my thoughts on the AI race between China and the US.</p>

</details>
