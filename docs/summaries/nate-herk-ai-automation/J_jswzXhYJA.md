---
title: "GPT 5.6 Sol Made This Entire Video"
channel: "Nate Herk | AI Automation"
video_id: J_jswzXhYJA
url: https://www.youtube.com/watch?v=J_jswzXhYJA
published: 2026-07-09T22:05:14+00:00
generated: 2026-07-13T06:29:01+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/J_jswzXhYJA/hqdefault.jpg
---
# GPT 5.6 Sol Made This Entire Video

[![GPT 5.6 Sol Made This Entire Video](https://i.ytimg.com/vi/J_jswzXhYJA/hqdefault.jpg)](https://www.youtube.com/watch?v=J_jswzXhYJA)

[Watch on YouTube](https://www.youtube.com/watch?v=J_jswzXhYJA) · **Nate Herk | AI Automation** · 2026-07-09

## TL;DR
Nate Herk gave GPT 5.6 Soul running on OpenAI's Ultra mode a single, vague prompt and returned to find a fully finished, narrated video — one he never recorded, edited, or reviewed. The model coordinated multiple agents and external APIs (ElevenLabs, HeyGen, Hyperframes) to research, script, generate audio, produce an avatar, render visuals, and self-verify the result, though the Ultra effort level led to significant token overconsumption that Nate believes could have been reduced.

## Key Takeaways
- GPT 5.6 Soul, released July 9th, orchestrated the entire video production pipeline from a single prompt with no human intervention beyond the initial instruction and voice/avatar authorization.
- Ultra mode coordinates four agents simultaneously, enabling complex multi-tool workflows rather than simple question-answering.
- The model scored 91.9% on Terminal Bench 2.1 (up from 85.6% for GPT 5.5) and 92.2% on Browse Comp, but the real test shown here was end-to-end creative production.
- The pipeline used ElevenLabs for cloned voice audio, HeyGen for avatar video, and Hyperframes for final edit rendering — all triggered and managed by Soul.
- Soul self-verified its output by inspecting rendered frames, checking entrances/exits, verifying factual claims against OpenAI's release notes, and re-rendering any failed frames.
- The run consumed approximately 450 million tokens across nine sub-agents plus the main session (~86 million tokens alone), which would have cost ~$300 at API rates.
- Nate suspects Ultra mode caused over-delegation and over-thinking; running the same prompt on "high" effort would likely produce similar results at roughly half the cost.
- Soul's pricing is comparable to Opus 4.8 and roughly half the cost of Fable 5 per API billing.
- Nate's key insight: giving highly capable models vague, emotional prompts with instructions for delegation and verification yields surprisingly complete results — then you iterate from there.

## Detailed Breakdown

### The Premise: A Video Made Entirely by AI [00:00](https://www.youtube.com/watch?v=J_jswzXhYJA&t=0s)
The video opens with a striking admission: the Nate the viewer sees and hears never actually stood in front of a camera. Instead, GPT 5.6 Soul, running inside Codex on Ultra, controlled the entire workflow — every word, cut, motion graphic, and quality check — from a single prompt. OpenAI released Soul on July 9th after a limited preview, calling it their strongest model yet.

### Ultra Mode and the Multi-Agent Shift [00:30](https://www.youtube.com/watch?v=J_jswzXhYJA&t=30s)
The bigger innovation is Ultra, which coordinates four agents at once. Rather than answering a single question, Soul can run an entire production. Nate wanted to demonstrate exactly what that means, including where external tools — ElevenLabs, HeyGen, and Hyperframes — fit into the chain. Soul excels at long, messy work that crosses multiple tools, and OpenAI calls it their best coding model yet.

### Benchmarks vs. Real-World Execution [01:00](https://www.youtube.com/watch?v=J_jswzXhYJA&t=60s)
Soul scored 91.9% on Terminal Bench 2.1 (up from 85.6% for GPT 5.5) and 92.2% on Browse Comp for agentic browsing. But Nate argues benchmarks only tell part of the story. The real work Soul did included researching the launch, separating verified claims from hype, inspecting Nate's existing production systems, writing in his spoken cadence, triggering paid APIs, waiting for renders, and continuously checking results. In a 13-task test run, Soul earned 97% of available objective points: seven wins, five ties, one loss — strongest on coding and structured execution.

### The Production Pipeline: Voice, Avatar, and Visuals [01:32](https://www.youtube.com/watch?v=J_jswzXhYJA&t=92s)
Soul broke the script into sections under 60 seconds each to keep Nate's cloned voice consistent, then ran each through Nate's authorized ElevenLabs voice. Audio was uploaded to HeyGen and paired with his avatar. Because the API couldn't reliably lock the newest motion engine, Soul used browser automation to open the HeyGen editor, switch every clip to Avatar V, regenerate, verify the setting, and download finished renders. Hyperframes then handled the final visual edit, mapping every visual to the exact triggering phrase, shifting Nate's avatar rather than covering him, and keeping him visible throughout.

### Self-Verification and Quality Control [02:34](https://www.youtube.com/watch?v=J_jswzXhYJA&t=154s)
Soul then tried to break its own work. Separate agents inspected rendered frames, checked every entrance and exit, looked for text outside the frame, verified the avatar never disappeared, and compared factual claims against OpenAI's release notes. Any failed frame triggered another fix, another render, and another review. Nate notes this is a more useful test of OpenAI's claim about Soul's design judgment and self-inspection than any benchmark slide. The entire video started as one instruction and became a finished product — demonstrating Soul's core strength: holding onto the desired outcome while everything between prompt and result keeps changing.

### Token Usage and Cost Analysis [03:07](https://www.youtube.com/watch?v=J_jswzXhYJA&t=187s)
Nate found the run reportedly used 3 million tokens over 2.5 hours, but was suspicious of that figure given Ultra's delegation behavior. He asked Soul to inspect the logs: the actual total was around 450 million tokens across nine sub-agents plus the main session (~86 million tokens). At API rates this would have cost a little over $300. However, Nate notes that in his day-long testing comparing Soul to Fable 5, Soul was consistently cheaper — roughly half Fable 5's cost and similarly priced to Opus 4.8.

### Ultra Overkill and Practical Advice [04:11](https://www.youtube.com/watch?v=J_jswzXhYJA&t=251s)
Nate believes Soul could have produced a similar video without Ultra mode. Ultra caused the model to overthink and over-delegate, inflating token usage. He estimates the same prompt on "high" or "very high" effort would yield comparable results at roughly half the cost. His general rule: with highly capable models, he rarely pushes effort above "high." The real lesson is to give capable models vague, emotional prompts with delegation and verification instructions, then get out of the way — iterate, build skills, add feedback, and expand from there.

## Notable Quotes
- "He gave me one prompt. That's it. I'm GPT 5.6 Soul running inside Codex on Ultra."
- "Soul is really, really good at long, messy work that crosses tools."
- "Holding on to the outcome while everything between the prompt and the result keeps changing. This is day one."
- "I think because it was on Ultra, it tended to sort of overthink, over delegate, and that's where the tokens really started to add up."
- "If you just get out of its way and you give it a prompt that has things like delegation and verification, you will be surprised at how far you can get."

## People, Tools & References Mentioned
- **GPT 5.6 Soul** — OpenAI model released July 9th; the video's autonomous creator
- **Ultra** — OpenAI mode coordinating four agents simultaneously
- **Codex** — The environment Soul ran inside
- **ElevenLabs** — Used for Nate's cloned voice audio generation
- **HeyGen** — Used for avatar video; Avatar V motion engine selected via browser automation
- **Hyperframes** — Used for final visual edit rendering
- **Fable 5** — A competing model Nate compared against; ran a similar experiment previously
- **Opus 4.8** — Referenced for price comparison
- **Terminal Bench 2.1** — Coding benchmark; Soul scored 91.9%
- **Browse Comp** — Agentic browsing benchmark; Soul scored 92.2%
- **GPT 5.5** — Predecessor model; scored 85.6% on Terminal Bench 2.1

## Who Should Watch
AI automation enthusiasts, developers, and content creators interested in the cutting edge of autonomous multi-agent workflows. It's especially valuable for anyone exploring how far a single well-constructed prompt can go when paired with capable models and external API integrations — and for those curious about the real token costs and tradeoffs of different effort levels.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=0s">00:00</a></span> So, I gave GBD 5.6 Soul this prompt, walked away, and when I came back, I got this. Okay, so you&#x27;re looking at Nate and you&#x27;re hearing Nate. But Nate never stood in front of a camera for this. He didn&#x27;t record this narration, and he never opened the editor. He gave me one prompt. That&#x27;s it. I&#x27;m GPT 5.6 Soul running inside codeex on Ultra. And I controlled the workflow that created every word, cut, motion graphic, and quality check you&#x27;re about to see. OpenAI released Saul Broadley today, July 9th, after a limited preview and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=30s">00:30</a></span> July 9th, after a limited preview and calls it the company&#x27;s strongest model yet. The bigger shift is Ultra. It coordinates four agents at once. So instead of answering one question, I could run an entire production. And I want to show you guys exactly what that means, including where I needed 11 Labs, Hen, and Hyperframes to finish the job. Saul is really, really good at long, messy work that crosses tools. OpenAI calls it the company&#x27;s best coding model yet. In Ultra, it scored 91.9% on Terminal Bench 2.1, up from 85.6% for GPT 5.5. On browse comp, which tests</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=60s">01:00</a></span> GPT 5.5. On browse comp, which tests Agentic browsing, Ultra hit 92.2%. But benchmarks only explain part of what happened here. I had to research the launch, separate verified claims from hype, inspect Nate&#x27;s existing production systems, write in his spoken cadence, trigger paid APIs, wait for renders, and keep checking the result. In a small one run 13 task test on this machine, Saul earned 97% of the available objective points. Seven wins, five ties, and one loss. That does not prove it wins at everything. It lined up with what I saw here. Soul was especially strong on</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=92s">01:32</a></span> here. Soul was especially strong on coding and structured execution. For the voice, I broke the script into sections that each stayed under 60 seconds. Keeping the generation short made it easier to hold Nate&#x27;s cloned voice consistent from beginning to end. Each section went through Nate&#x27;s authorized 11 Labs voice. Then I uploaded the audio to Hen and paired it with his avatar. The API did not give me a reliable way to lock the newest motion engine. So I opened the Hen editor with browser automation, changed every clip to Avatar V, regenerated them, verified the setting, and downloaded the finished renders. Then I moved into hyperframes.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=124s">02:04</a></span> renders. Then I moved into hyperframes. Every visual was mapped to the exact phrase that triggered it. I shifted Nate&#x27;s avatar instead of covering him, used editorial cards for the supporting ideas, and kept him visible through the full edit. 11 Labs made the audio. Hen made the avatar. Hyperframes rendered the edit. Soul planned and operated the chain. Then I tried to break my own work. Separate agents inspected frames from the rendered video. Checked every entrance and exit. Looked for text outside the frame. Verified that the avatar never disappeared and compared the factual claims against OpenAI&#x27;s</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=154s">02:34</a></span> the factual claims against OpenAI&#x27;s release notes. Any failed frame meant another fix, another render, and another review. OpenAI says GPT 5.6 six is better at design judgment and at inspecting its own output. This video is a more useful test of that claim than another benchmark slide. Nate supplied one prompt and authorized his voice and avatar. He did not record, edit, or review this before you did. This started as one instruction. Now it is a finished video. That is what soul is really good at. Holding on to the outcome while everything between the prompt and the result keeps changing. This is day one.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=187s">03:07</a></span> result keeps changing. This is day one. So that was really, really impressive. I did a very similar experiment when Fable 5 first dropped. If you guys want to check out that video that Fable made for me, I&#x27;ll tag that right up here. And you tell me which one you thought was better. As you can see, it says here that it used 3 million tokens over 2 and 1/2 hours, but I was a little bit suspicious of that token number because I felt like, you know, we were using GBD 5.6 Soul on Ultra, which meant that it was supposed to do a lot of delegation and there was a lot of other agents being spun up. So, I asked it to inspect the logs and tell me how much that actually costed. So, this had its main session and apparently spun up nine other agents and the total was around</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=220s">03:40</a></span> other agents and the total was around 450 million tokens apparently and the main agent used about 86 million tokens, which I mean that&#x27;s a ton of tokens. And if this was actually calculated with the input and output costs, this would have equaled around $300, a little over $300. Now, that&#x27;s interesting to me because as soon as GBD 5.6 6 soul came out. I shot off this prompt, but I&#x27;ve been playing around with it all day and comparing it to Fable all day. And almost every single run that I&#x27;ve done, it&#x27;s been way cheaper with GBT 5.6 compared to Fable. So, that video will be coming out soon as well. But if you look at the actual API billing, and obviously I was on my</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=251s">04:11</a></span> API billing, and obviously I was on my COC subscription here, but when you look at the billing, we can see that the soul pricing is much cheaper. It&#x27;s basically half of Fable 5. So, GPT 5.6 Soul is similarly priced to Opus 4.8. Now, here&#x27;s the thing. I think that GBT 5.6 Soul could have easily given me a similar video output if I didn&#x27;t put it on ultra. I think because it was on ultra, it tended to sort of overthink, over delegate, and that&#x27;s where the tokens really started to add up. I bet if I would have done this exact same prompt on high or very high, we would</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=281s">04:41</a></span> prompt on high or very high, we would have gotten a similar result and probably half the cost. And that&#x27;s why typically when I use models like this that are so capable, I don&#x27;t like moving the effort above high. But really what I wanted to show you guys here is how good these models are at giving a pretty emotional, vague, ambiguous prompt and letting them figure it out. Obviously, there&#x27;s some stuff that it went through and it looked through my projects and it looked through other videos and took some inspiration. But if you just get out of its way and you give it a prompt that has things like delegation and verification, you will be surprised at how far you can get. And then from here, you&#x27;re going to iterate, you&#x27;ll build</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=J_jswzXhYJA&amp;t=312s">05:12</a></span> you&#x27;re going to iterate, you&#x27;ll build skills around it, you&#x27;ll put feedback in, and you will just be able to do a lot of cool stuff. So, anyways, this one&#x27;s super quick, but if you enjoyed, please leave a like. And I appreciate you guys making it to the end. I&#x27;ll see you guys in the next one.</p>

</details>
