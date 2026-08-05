---
title: "OpenAI Astra Just Advanced Mathematics... 10 Times."
channel: "Better Stack"
video_id: -aCN5BMq1JI
url: https://www.youtube.com/watch?v=-aCN5BMq1JI
published: 2026-08-05T08:00:33+00:00
generated: 2026-08-05T10:45:20+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/-aCN5BMq1JI/hqdefault.jpg
---
# OpenAI Astra Just Advanced Mathematics... 10 Times.

[![OpenAI Astra Just Advanced Mathematics... 10 Times.](https://i.ytimg.com/vi/-aCN5BMq1JI/hqdefault.jpg)](https://www.youtube.com/watch?v=-aCN5BMq1JI)

[Watch on YouTube](https://www.youtube.com/watch?v=-aCN5BMq1JI) · **Better Stack** · 2026-08-05

## TL;DR
OpenAI's next major model, Astra, reportedly solved 10 significant problems in mathematics and theoretical computer science, with every result verified in the Lean proof language. The model is designed for long-horizon tasks—working on single problems for hours or days—using a multi-agent architecture that may eventually transform software engineering work like large-scale refactors.

## Key Takeaways
- OpenAI published a post titled "10 Advances in Mathematics and Theoretical Computer Science" achieved by an internal version of Astra [00:30](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=30s)
- Every result was written in Lean, a proof language that a computer checks line by line, meaning anyone can verify the proofs without trusting OpenAI [01:00](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=60s)
- A 249-page paper was released, including 62 pages of the model's own reasoning narration [00:00](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=0s)
- OpenAI is being more careful this time after a previous incident last October where GPT5 allegedly "solved" Erdős problems that turned out to already have human-published solutions [01:31](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=91s)
- The total token cost for successful solution runs was roughly $2,000 on the Sol API, though this only covers runs that worked—not failed attempts [02:01](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=121s)
- Astra is designed for long-horizon tasks, contrasting with existing models like Luna, Terror, and Sol that handle day-to-day software engineering [02:30](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=150s)
- OpenAI's chief scientist Jacob Pjaki previously discussed wanting systems that can work on problems for hours or days [03:00](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=180s)
- The reported architecture uses a root agent that creates sub-agents, assigns portions of the problem, and synthesizes results—similar to Sol Ultra's approach [04:03](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=243s)
- Splitting problems isn't free: coordination overhead and compounding errors can make multi-agent setups worse on tightly coupled work [04:33](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=273s)
- Mathematician Thomas Bloom pushed back on claims that AI is "replacing mathematicians," noting the work builds on over a century of human mathematical theory [05:03](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=303s)

## Detailed Breakdown

### OpenAI's Announcement and Verification via Lean [00:00](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=0s)
The video opens by announcing that Astra solved 10 major problems in math and computer science, with some observers claiming the model exceeds PhD-level intelligence. OpenAI published a 249-page paper including 62 pages of the model's own reasoning. The results were written in Lean, a proof language that is compiler-checked line by line, so verification doesn't require trusting OpenAI or even understanding the math—if it compiles, the proof holds.

### Past Controversy and Renewed Caution [01:31](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=91s)
OpenAI has reason to be careful. Last October, Kevin Whale posted that GPT5 had solved 10 previously unsolved Erdős problems, but it turned out the model had simply found existing papers where humans had already solved them. The current Astra claim is similar, but this time the Lean proofs allow independent verification. The speaker draws an analogy to software testing: you don't trust that a function works because someone says so—you write a test and let the machine decide.

### Cost of Intelligence and Open Questions [02:01](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=121s)
OpenAI mentioned that the total tokens needed for the successful runs cost roughly $2,000 on the Sol API, which the speaker finds shockingly low and suggestive of intelligence becoming a cheap commodity. However, this figure only covers successful runs—there's no visibility into how many failed attempts preceded them, and since the model is internal, nobody outside OpenAI can verify the full cost.

### What Astra Is and Its Design Purpose [02:30](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=150s)
Astra is likely a new family of models positioned alongside existing models like Luna, Terror, and Sol, but aimed at long-horizon tasks rather than day-to-day software engineering. OpenAI's chief scientist Jacob Pjaki previously stated on the company's podcast that current models are good at short tasks, and the goal is to build systems that can work on problems for hours or days—synthesizing huge amounts of data and performing research impractical for humans.

### The Coherence Challenge and Why Math Is a Good Test [03:00](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=180s)
The speaker explains that the real challenge over long runs isn't intelligence but coherence. In typical AI sessions, context fills up, early decisions scroll away, and the model starts repeating earlier mistakes. Open math problems are excellent tests because there's no partial credit and no feedback until the entire argument holds together. If a system can stay focused on such a problem for hours without drifting, it could likely handle large software refactors too.

### Multi-Agent Architecture and Coordination Costs [04:03](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=243s)
Much of Astra's capability comes from the harness and tools around the model, not just the model itself. The reported architecture uses a root agent that creates sub-agents, assigns each a portion of the problem, waits for results, and synthesizes them. Sol Ultra already uses a similar approach where sub-agents can communicate with each other. However, splitting problems incurs coordination costs, and on tightly coupled work like planning, overhead and compounding errors can wipe out gains. The design only works when splitting and reassembling buys more than coordination costs.

### "Replacing Mathematicians" Debate and Closing Thoughts [05:03](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=303s)
The speaker addresses claims that Astra is replacing mathematicians, citing Thomas Bloom's rebuttal: it's wrong to call it "replacing mathematicians" when the AI proves a conjecture made by a mathematician, using theories developed over a century of human work, with an AI built and trained by mathematicians on everything mathematicians have ever written. The replacement argument looks weak even if the results are promising. The speaker expresses excitement about eventually testing Astra on practical software engineering tasks.

## Notable Quotes
- "You don't just trust that a function works because someone tells you it does, at least not all of us. You write a test and let the machine decide. Lean is the same idea and the compiler either accepts the proof or it doesn't." [01:31](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=91s)
- "If we keep going at this rate, I don't see how intelligence doesn't just become a cheap commodity." [02:01](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=121s)
- "The thing that breaks over a long run isn't always intelligence. It's often coherence." [03:00](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=180s)
- "It's not right to call proving one conjecture made by a mathematician using theories developed by over a century of work by mathematicians with an AI built by mathematicians and trained by reading everything ever written by all mathematicians as replacing mathematicians." — Thomas Bloom [05:03](https://www.youtube.com/watch?v=-aCN5BMq1JI&t=303s)

## People, Tools & References Mentioned
- **Astra** — OpenAI's next major model, designed for long-horizon tasks
- **Lean** — A proof language that compilers check line by line for mathematical verification
- **Kevin Whale** — OpenAI employee who posted about GPT5 solving Erdős problems last October
- **Jacob Pjaki** — OpenAI's chief scientist, discussed long-horizon AI systems on the company podcast
- **Thomas Bloom** — Mathematician who pushed back on the "AI replacing mathematicians" narrative
- **Sol / Sol Ultra** — Existing OpenAI models; Sol Ultra uses a similar multi-agent architecture with inter-agent communication
- **Luna, Terror** — Other existing model families mentioned alongside Sol
- **Erdős problems** — Famous unsolved mathematical problems; GPT5 previously claimed to have solved some that were already solved by humans

## Who Should Watch
Software engineers and AI enthusiasts interested in the frontier of long-horizon AI reasoning and what it could mean for complex engineering tasks like large-scale refactors. The video is especially relevant for those curious about how multi-agent architectures and formal verification (via Lean) are being used to push AI beyond short-context limitations.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=0s">00:00</a></span> Open AAI&#x27;s next major model, Astra, just solved 10 major problems in maths and computer science, and people have been genuinely impressed with the results. Some saying the model is now beyond the intelligence of a PhD. They published the whole thing online for anyone to read. And there&#x27;s a 249page paper with 62 pages of the model&#x27;s own reasoning. But what does this mean for us software engineers? Because from everything we know so far, Astra is built to work on a single problem for days or hours. So if you fancy rewriting everything in Rust, I&#x27;m looking at Hub</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=30s">00:30</a></span> everything in Rust, I&#x27;m looking at Hub Bun. This might be the model you need. So in this video, we&#x27;ll go through what OpenAI actually claimed and how you can check this yourself and how a model like this runs on a problem for days without getting lost. So first, what did Open AI actually claim? They put out a post on the weekend titled 10 Advances in Mathematics and Theoretical Computer Science. The results were all achieved by an internal version of Astra, which is their next</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=60s">01:00</a></span> version of Astra, which is their next major model. And they list all 10 of the problems that they solved, which I&#x27;m not going to pretend to understand. But they didn&#x27;t just make the claim. Every result was written out in something called lean, which is a proof language a computer checks line by line. So you don&#x27;t have to trust Open AI, and you don&#x27;t even have to understand the mass because if the thing compiles, then that means the proof holds. And they also released the model&#x27;s own narration of how it got to each of the results. So if you fancy reading a 62-page PDF, then go ahead. And they&#x27;ve got a good reason to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=91s">01:31</a></span> ahead. And they&#x27;ve got a good reason to be careful because they got burned on exactly this last October. Open AAI&#x27;s Kevin Whale put out a post saying GPT5 had found solutions to 10 previously unsolved Erdos problems. And it turned out GPT5 had just found papers where humans had already solved them. So they&#x27;re making a similar claim now, but this time they&#x27;re being much more careful. And you can actually check the results yourself. It&#x27;s the same thing we do with code. You don&#x27;t just trust that a function works because someone tells you it does, at least not all of us. You write a test and let the machine decide.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=121s">02:01</a></span> write a test and let the machine decide. Lean is the same idea and the compiler either accepts the proof or it doesn&#x27;t. They also mentioned that the total number of tokens needed to find a solution to these problems would cost roughly 2,000 on sole API rights, which is shockingly low in my opinion. If we keep going at this right, I don&#x27;t see how intelligence doesn&#x27;t just become a cheap commodity. Though that number only covers the runs that actually worked. We&#x27;ve got no idea how many attempts came before them, whether it was one shot or a thousand. And since the model is internal, there&#x27;s nobody outside of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=151s">02:31</a></span> internal, there&#x27;s nobody outside of OpenAI who can go back and check. So, the 10 results are real and anyone can verify them, but the price tag is up in the air. And if you enjoy staying up to date with AI news, then subscribe to Better Stack. So, what actually is Astra? It&#x27;s likely a new family of models sat next to Luna, Terror, and Soul, but it&#x27;s aimed somewhere else. The existing models can do our day-to-day software engineering, and Astra is designed for long horizon tasks, and the rumors line up with earlier statements from Open AI. Their chief scientist,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=181s">03:01</a></span> from Open AI. Their chief scientist, Jacob Pjaki, went on the company&#x27;s own podcast last year and talked about wanting systems that can work on problems for hours or days because right now models are good at short tasks and that&#x27;s the thing they want to change. So this is a model that could potentially perform research that is completely impractical for humans, synthesizing huge amounts of data and thinking through problems for days on end. But the thing that breaks over a long run isn&#x27;t always intelligence. It&#x27;s often coherence. You probably felt this yourself. You start a session with a clear plan and 40 minutes later the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=213s">03:33</a></span> clear plan and 40 minutes later the context is full and the early decisions have scrolled off the back and then the model is just confidently repeating the same mistakes it got wrong 20 minutes ago. And this is why an open maths problem is such a good test. You can&#x27;t brute force it and you can&#x27;t cheat because there&#x27;s no partial credit and no feedback until the whole argument holds together. So if a system can stay pointed at one of those for hours without drifting, it can probably be pointed at your refactor as well. But this is the bit that I find really interesting because a lot of the gain here is coming from the harness and the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=243s">04:03</a></span> here is coming from the harness and the tools around the model rather than just the model itself. The reported architecture for this is a root agent that creates sub agents and hands each a portion of the problem, waits for the results and synthesizes them into a final answer. Now there&#x27;s a lot of complexity in coordinating those agents. It&#x27;s not just a case of hand it a problem and wait for a result. And we&#x27;ve already seen a similar architecture already shipped because Soul Ultra does the same thing. And with Sol Ultra, the sub aents can actually talk to each other when they&#x27;re doing work rather</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=273s">04:33</a></span> other when they&#x27;re doing work rather than just remaining in complete isolation. But splitting a problem up isn&#x27;t actually free. Every time you hand work to a sub agent, you pay for it in coordination because multiple agent setups can do worse on tightly coupled work like planning where the overhead and the compounding errors wipe out whatever you gained by splitting up the work in the first place. The whole design hangs on the fact that splitting a problem up and then stitching it back together buys you more results than the coordination actually costs. On these 10 problems, the results clearly paid off,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=303s">05:03</a></span> problems, the results clearly paid off, but we can&#x27;t just trust internal results. So we&#x27;ll have to wait to see how this turns out when we can get our hands on it. Now of course there&#x27;s a lot of talk saying this is now replacing mathematicians and Thomas Bloom pushed back on that. He said it&#x27;s not right to call proving one conjecture made by a mathematician using theories developed by over a century of work by mathematicians with an AI built by mathematicians and trained by reading everything ever written by all mathematicians as replacing mathematicians. So, the replacement argument looks weak to me, even if the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=-aCN5BMq1JI&amp;t=334s">05:34</a></span> argument looks weak to me, even if the results look promising. But it&#x27;ll be really interesting to finally get my own hands on Astra and try out myself and see how practical it is for software engineering tasks. But I hope you enjoyed that one, guys. And if you enjoy staying up to date on tech and AI news, then subscribe to Better Stack. Otherwise, thank you so much for watching and I&#x27;ll see you in the next one.</p>

</details>
