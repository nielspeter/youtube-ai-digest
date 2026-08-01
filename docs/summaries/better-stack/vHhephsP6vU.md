---
title: "Apple Silicon Can Run Local AI With Just 2GB Of RAM"
channel: "Better Stack"
video_id: vHhephsP6vU
url: https://www.youtube.com/watch?v=vHhephsP6vU
published: 2026-08-01T08:00:32+00:00
generated: 2026-08-01T10:08:17+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/vHhephsP6vU/hqdefault.jpg
---
# Apple Silicon Can Run Local AI With Just 2GB Of RAM

[![Apple Silicon Can Run Local AI With Just 2GB Of RAM](https://i.ytimg.com/vi/vHhephsP6vU/hqdefault.jpg)](https://www.youtube.com/watch?v=vHhephsP6vU)

[Watch on YouTube](https://www.youtube.com/watch?v=vHhephsP6vU) · **Better Stack** · 2026-08-01

## TL;DR
Turbo Fieldfare is a Swift-and-Metal project that runs a 26-billion-parameter Gemma 4 mixture-of-experts model on Apple Silicon Macs using just ~2 GB of RAM, achieving ~23 tokens per second. It exploits Gemma 4's architecture—where only ~3.9B of 26B parameters are active per token—by keeping the always-needed components resident in memory and streaming individual experts on-demand from the SSD, made possible by Apple's unified memory architecture.

## Key Takeaways
- Gemma 4 is a mixture-of-experts (MoE) model with 128 experts per layer, but only 8 are activated per token, meaning ~85% of the model's parameters are idle at any given moment.
- Turbo Fieldfare keeps only ~1.35 GB of always-needed data (attention, router, embeddings, shared expert) resident in RAM, leaving ~12.9 GB of expert weights on the SSD.
- On an M3 Max, the system achieves 23.4 tokens per second with a memory footprint of just 2.15 GB, which is fully usable for local AI.
- Apple Silicon's unified memory is critical: the CPU and GPU share the same physical RAM, eliminating the two-copy, bus-hop bottleneck that would tank performance on a discrete-GPU PC.
- Weights are stored on disk in the exact layout the Metal kernel consumes—down to 4-bit quantized values—so reading the file *is* loading the weight, with no conversion step.
- The GPU stays busy during SSD fetches by working on a shared expert that runs for every token regardless of the router's picks, effectively hiding much of the disk I/O latency.
- Each layer keeps 16 of its 128 experts cached in memory using an LFU (Least Frequently Used) eviction policy, which outperforms LRU because expert routing is predictable and some experts are far more popular than others.
- The entire project is written in Swift and Metal, Apple's low-level GPU API, and runs as a native Mac app.
- The system design is tightly coupled to both Gemma 4's MoE architecture and Apple Silicon's hardware characteristics—it would not translate directly to traditional PC architectures.
- The project demonstrates that with architecture-aware engineering, very large models can run on modest hardware, hinting at a future where even larger models might run on ever-smaller devices.

## Detailed Breakdown

### Project Overview and Performance [00:00](https://www.youtube.com/watch?v=vHhephsP6vU&t=0s)
Turbo Fieldfare is a recently created project that runs a 26-billion-parameter Gemma 4 model on Apple Silicon using only ~2 GB of RAM. Tested locally on an M3 Max, it achieved 23.4 tokens per second with a 2.15 GB memory footprint—performance the presenter describes as "completely usable." The entire project is written in Swift and Metal, Apple's low-level GPU API, and launches as a user-friendly Mac app. The GitHub repo can be cloned and set up with a series of straightforward commands: clone, download the model, load it, and start sending messages.

### How Gemma 4's Mixture-of-Experts Architecture Works [01:32](https://www.youtube.com/watch?v=vHhephsP6vU&t=92s)
Gemma 4 differs from traditional models that use one large feed-forward neural network. Instead, each layer has 128 small feed-forward blocks (the "experts") plus a tiny router. For each token, the router selects the top 8 experts, meaning only ~3.9 billion of the 26 billion parameters actually do any work per token. This leaves 85% of the model idle at any instant, which means you don't need the full 14.3 GB in RAM—only whatever the current token touches.

### Memory Layout: Resident Pile vs. SSD Experts [02:04](https://www.youtube.com/watch?v=vHhephsP6vU&t=124s)
Turbo Fieldfare splits the model into two piles. The first (~1.35 GB) contains everything every token needs regardless: attention, the router, embeddings, and one shared expert that always runs. This is memory-mapped straight off disk and stays resident in memory the entire time the model is loaded. The second pile is the experts themselves—30 layers × 128 experts, ~3.36 MB each, totaling ~12.9 GB. This pile never gets fully loaded; it sits on the SSD and is pulled in a few megabytes at a time as requested.

### Token Generation: Attention, Routing, and the I/O Challenge [03:08](https://www.youtube.com/watch?v=vHhephsP6vU&t=188s)
When producing a token, it passes through all 30 layers in order. Each layer performs two steps: attention (looking back at what's been written to determine what matters now) and routing (selecting 8 of 128 experts). Attention runs entirely on the resident 1.35 GB. The problem is that you can't know which experts are needed until attention is already done—there's no prefetching possible because the choice depends on the current token and every token before it. This means 30 times per token, the CPU must stop and read from disk, a fraction of a millisecond before those weights are needed.

### Why Apple Silicon Makes This Possible [03:39](https://www.youtube.com/watch?v=vHhephsP6vU&t=219s)
On a PC with a discrete GPU, getting a weight to the GPU requires reading from SSD into system RAM, then pushing it across the PCI bus into the GPU's VRAM—two copies and a bus hop, which would tank performance if done thousands of times per second. Apple Silicon has unified memory where the CPU and GPU share the same physical RAM with no separate VRAM. A Metal buffer is simply memory both can see, so the CPU reads straight off the SSD into a buffer the GPU is about to use, skipping a significant amount of work.

### File Format Optimization [04:43](https://www.youtube.com/watch?v=vHhephsP6vU&t=283s)
Normally, model weights on disk sit in a storage format that requires unpacking and conversion before a GPU can use them. Turbo Fieldfare stores weights in exactly the layout the Metal kernel consumes, down to the 4-bit quantized values. The installer rearranges the data without re-encoding it, so reading the file is equivalent to loading the weight—no conversion step in between.

### Async Work Streams and Hiding Disk Latency [05:15](https://www.youtube.com/watch?v=vHhephsP6vU&t=315s)
While the CPU fetches from disk, the GPU isn't idle. It works on the shared expert from the resident pile, which runs for every token regardless of the router's selection. This means much of the disk fetch is hidden inside work the model had to do anyway. Multiple async work streams further compress the timing.

### LFU Caching Strategy [05:46](https://www.youtube.com/watch?v=vHhephsP6vU&t=346s)
Each layer keeps 16 of its 128 experts parked in memory. When the router picks an already-cached expert, it's instant; when it doesn't, the expert is pulled from SSD and evicts the least frequently used one. This LFU (Least Frequently Used) cache is chosen over LRU (Least Recently Used) because expert routing isn't random—some experts are picked constantly while others rarely appear. Counting usage frequency keeps popular experts resident better than counting recency. The design bets on routing being predictable; if every token wanted a different random 8 experts, the cache would miss nearly every time and performance would suffer.

### Future Outlook [06:18](https://www.youtube.com/watch?v=vHhephsP6vU&t=378s)
The presenter expresses excitement about how far models can be squeezed onto smaller hardware, speculating that one day a "fable-level model" might run on a watch. A companion video demonstrates running this architecture on even smaller machines. The system design is specifically tailored to exploit both Gemma 4's MoE structure and Apple Silicon's unique characteristics.

## Notable Quotes
- "This project uses Apple Silicon's architecture to run a 26 billion per model on just 2 GB of RAM and it's actually usable."
- "26 billion parameters total, but only roughly 3.9 billion actually do any work on any given token. 85% of the file is idle at any instance."
- "You can't know which experts you need until you've already done half the work on that layer. There's no reading ahead and no prefetching."
- "Apple silicon, however, has unified memory. So the CPU and the GPU are looking at the same physical RAM, and there's no VRAM to copy into."
- "Reading the file is loading the weight with no conversion step in between."
- "The disc read hides inside work the model had to do anyway. So you get most the fetch for free."
- "Some experts get picked constantly across all sorts of tokens and others hardly come up at all. So counting how often an expert gets used keeps the popular ones around better than counting how recently."

## People, Tools & References Mentioned
- **Turbo Fieldfare** — the project demonstrated, written in Swift and Metal
- **Gemma 4** — Google's mixture-of-experts model (26B parameters, 128 experts per layer, 8 active per token)
- **Apple Silicon** — specifically tested on M3 Max
- **Metal** — Apple's low-level GPU API
- **Swift** — programming language used for the project
- **GitHub** — where the project repo is hosted
- **LFU (Least Frequently Used) cache** — eviction strategy used for expert caching
- **LRU (Least Recently Used) cache** — mentioned as a contrast to LFU
- **Better Stack** — the channel producing the video

## Who Should Watch
Mac-owning developers and AI enthusiasts interested in running large language models locally on modest hardware, as well as engineers curious about how Apple Silicon's unified memory architecture can be exploited for performance gains that aren't possible on traditional discrete-GPU systems.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=0s">00:00</a></span> This project uses Apple Silicon&#x27;s architecture to run a 26 billion per model on just 2 GB of RAM and it&#x27;s actually usable. I tried it out locally and was able to get 23 tokens per second. The project created a couple of weeks ago. Turbo Fieldfare avoids the large memory footprint of Gemma 4, which is around 14 gig by keeping only a tiny fraction of the model in memory, then streaming the experts direct from SSD. The entire thing is written in Swift and Metal, which is Apple&#x27;s low-level GPU</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=31s">00:31</a></span> Metal, which is Apple&#x27;s low-level GPU API. So, you can launch it as a Mac app, which is incredibly userfriendly, and it takes advantage of the specific architecture that you get from Apple silicon chips. So, today I want to dive into how Turbo Fieldfare uses Apple Silicon specifically to squeeze incredible performance out of a 26 billion per model. So, if we head over to the GitHub repo, we can run a series of commands to clone the repo and get the app up and running. And once up and running, we need to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=62s">01:02</a></span> And once up and running, we need to download the model itself, load the model, then we can send our first message. You can see for me on an M3 Max, I&#x27;m getting 23.4 tokens per second with a memory footprint of just 2.15 GB. This feels completely usable to me. So, let&#x27;s take a deeper look at the architecture. And if you enjoy content like this, then don&#x27;t forget to subscribe to better stack. First, we need to understand how Gemma 4 works because that leads into the system design of the application itself. Gemma 4 is a mixture of experts model. Most</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=92s">01:32</a></span> 4 is a mixture of experts model. Most models use one big feed forward neural network, but Gemma is different. As ane layer, it instead has 128 small feed forward blocks. These are the experts plus a tiny routter. For each token, the routter picks the top eight experts and only those eight run. So 26 billion parameters total, but only roughly 3.9 billion actually do any work on any given token. 85% of the file is idle at any instance. You don&#x27;t need 14.3 GB in RAM. You need whatever the current token</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=124s">02:04</a></span> RAM. You need whatever the current token happens to touch. Turbo Fieldfare takes advantage of this design, keeping the always needed parts in RAM, leaving the experts on SSD and fetching them just in time. So, let&#x27;s take a look at what Turbo Fieldfare is doing with Apple Silicon. When you install the bundle, it gets split into two separate piles. The first is everything the token needs no matter what. The attention, the router, the embeddings, and one shared expert that always runs that comes to about 1.35 gig. It gets memory mapped straight off disk and it&#x27;s always resident on</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=156s">02:36</a></span> off disk and it&#x27;s always resident on memory the whole time the model is loaded. The second pile is the experts themselves. 30 layers with 128 experts each, about 3.36 megabytes a piece. So roughly 12.9 GB and that never gets loaded at all. It just sits on the SSD and gets pulled in a few megabytes at a time as and when the model asks for it. So what actually happens when you produce a token? The model has 30 layers and a token passes through every one of them in order and each layer does the same two things. First up is attention</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=188s">03:08</a></span> same two things. First up is attention and that&#x27;s the step where the model looks back over everything that&#x27;s been written so far and works out what matters right now. If it&#x27;s about to write the word after the cat sat on the attention is what makes cat count more than the and the handy thing is that attention runs entirely on that 1.35 gig that&#x27;s already in memory. though we haven&#x27;t touched the disc yet at all. Then the router takes what attention produced and it names the eight experts it wants out of the 128. And that&#x27;s where a problem lies because you can&#x27;t</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=219s">03:39</a></span> where a problem lies because you can&#x27;t know which experts you need until you&#x27;ve already done half the work on that layer. There&#x27;s no reading ahead and no prefetching since the choice depends on this token and every token before it. And it only gets made a fraction of a millisecond before those weights are needed. So 30 times per token, the CPU has to stop and go to disk. Which brings us to why this specifically is a Mac project. On a PC with a discrete GPU, getting a weight in front of the GPU means reading it off the SSD into system RAM. Then pushing it across the PCI buzz</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=252s">04:12</a></span> RAM. Then pushing it across the PCI buzz into the card&#x27;s own VRAMm. That&#x27;s two copies and a buzz hop. And doing that thousands of times a second would tank performance. Apple silicon, however, has unified memory. So the CPU and the GPU are looking at the same physical RAM, and there&#x27;s no VRAM to copy into. A metal buffer is just memory that both the CPU and the GPU can see. So the CPU reads by straight off the SSD into a buffer the GPU is about to run against, meaning we can skip a bunch of work, and they lean on these optimizations harder</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=283s">04:43</a></span> they lean on these optimizations harder with the file format. Normally, weights on discs sit in a storage format that needs to be unpacked and converted before a GPU can use them. But Turbo Fieldfet stores them in exactly the layout the metal kernel consumes right down to the 4-bit quantized values. The installer rearranges the data without ever re-encoding it. So reading the file is loading the weight with no conversion step in between. So what&#x27;s the GPU doing while the CPU is off fetching from disk? Well, remember the shared expert sitting on the resident pile that runs for every token no matter what the router picked.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=315s">05:15</a></span> token no matter what the router picked. That&#x27;s what it works on. The disc read hides inside work the model had to do anyway. So you get most the fetch for free. So we&#x27;ve got multiple work streams happening async which squeezes the time down even further. And even more so it&#x27;s not even going to disk every time either. Each lag keeps 16 of its 128 experts parked in memory. So when the router picks one that&#x27;s already there, you get it instantly. And when it doesn&#x27;t, the expert comes off the SSD and pushes out whichever one has been used least. That&#x27;s called an LFU cache,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=346s">05:46</a></span> used least. That&#x27;s called an LFU cache, which is least frequently used. This is different to an alloy u cache where you throw out whatever was touched longest ago because rooting here isn&#x27;t random. Some experts get picked constantly across all sorts of tokens and others hardly come up at all. So counting how often an expert gets used keeps the popular ones around better than counting how recently. It does mean the whole design is betting on routting being predictable because if every token wanted a different random eight, you&#x27;d miss the cash nearly every time and lose performance. So, the system design here</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=vHhephsP6vU&amp;t=378s">06:18</a></span> performance. So, the system design here is very specific to take advantage of both the architecture of Gemma 4 and Apple Silicon. You can try this out yourself and head over to the repo we&#x27;ve included in the description. And I&#x27;m excited to see how far we can squeeze these models. You know, maybe one day we&#x27;ll have a fable level model running on our watch. We&#x27;ve also filmed a video showing how you can run this type of architecture on even smaller machines. You can watch that here. Otherwise, thank you so much for watching, guys. I hope you enjoyed that one and I&#x27;ll see you in the next one.</p>

</details>
