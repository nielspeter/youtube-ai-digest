---
title: "This $8 Microcontroller Is Running a Language Model Locally!"
channel: "Better Stack"
video_id: 0qXVMt3pIjU
url: https://www.youtube.com/watch?v=0qXVMt3pIjU
published: 2026-07-31T09:00:07+00:00
generated: 2026-07-31T10:49:50+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/0qXVMt3pIjU/hqdefault.jpg
---
# This $8 Microcontroller Is Running a Language Model Locally!

[![This $8 Microcontroller Is Running a Language Model Locally!](https://i.ytimg.com/vi/0qXVMt3pIjU/hqdefault.jpg)](https://www.youtube.com/watch?v=0qXVMt3pIjU)

[Watch on YouTube](https://www.youtube.com/watch?v=0qXVMt3pIjU) · **Better Stack** · 2026-07-31

## TL;DR
A Ukrainian developer named Slava S. managed to run a 28.9 million parameter language model on an $8 ESP32S3 microcontroller with only 512 KB of SRAM by using per-layer embeddings to store the bulk of the model in flash memory. The model, trained on Microsoft's "tiny stories" dataset, generates about nine tokens per second but is limited to producing simple stories and tends to drift back to a default narrative regardless of the prompt.

## Key Takeaways
- A 28.9 million parameter language model runs locally on an $8 ESP32S3 microcontroller with no Wi-Fi or server dependency.
- The ESP32S3 has only 512 KB of SRAM, yet the model is 110 times larger than the previous record (260,000 parameters) for a chip like this.
- The key technique is "per layer embeddings," an idea from Google's Gemma, which stores the massive embedding table in cheap flash memory rather than SRAM.
- Only about 450 bytes of data (six rows for six layers) are pulled from flash into SRAM at a time for computation.
- The model is trained on Microsoft's "tiny stories" dataset, designed so even models with a few million parameters can write coherent simple stories.
- The implementation runs in plain C with no operating system or Python interpreter, inspired by Andrej Karpathy's Llama2.c project.
- The specific hardware required is the ESP32S3 N16R8 variant with 16 MB of flash and 8 MB of PSRAM.
- The model achieves roughly nine tokens per second but tends to loop back to a default story about a little girl regardless of the prompt given.
- Changing the prompt requires reflashing the ESP32, as only one pre-flashed prompt can be used at a time.
- The project is an impressive but limited proof of concept, not capable of code generation or answering complex questions.

## Detailed Breakdown

### The Impossible Feat [00:00](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=0s)
The video opens by demonstrating a 28.9 million parameter language model generating text one word at a time on an $8 ESP32S3 microcontroller. There is no Wi-Fi connection and no server communication — everything happens locally on a chip with less RAM than a 1990s computer.

### The Memory Problem [00:31](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=31s)
The ESP32S3 provides only 512 KB of SRAM, which is the fast memory the chip uses for computation. Previously, the largest language model anyone had running on a chip like this topped out at 260,000 parameters, making this new model roughly 110 times larger. The breakthrough was achieved by Ukrainian developer Slava S.

### Per Layer Embeddings [01:34](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=94s)
The workaround borrows an idea from Google's Gemma called per layer embeddings. Most of a language model's parameters do not actually compute anything — they sit in an embedding table that only gets read from. Since these parameters are only looked up, they do not need fast memory and can remain in slow, cheap flash memory. Only the attention head and feed-forward components, which actually compute the next token, need to stay in SRAM.

### Fitting the Model on the Chip [02:05](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=125s)
The 25 million row embedding table, which is the biggest chunk of the model's 28.9 million parameters, lives in flash memory. The ESP32S3 has 16 MB of flash, which is more than enough. At inference time, only about six rows are pulled from the table — one for each of the model's six layers — totaling roughly 450 bytes.

### Training on Tiny Stories [02:36](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=156s)
The presenter cautions that this is a very simple model, not a GPT-style LLM. A normally trained 28 million parameter model would produce gibberish. Instead, this model is trained on "tiny stories," a dataset created by Microsoft researchers and deliberately written simply enough that a model of just a few million parameters can learn to write coherently.

### The Llama2.c Blueprint [03:08](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=188s)
The approach of running inference in plain C on a chip with no operating system and no Python interpreter comes from Andrej Karpathy's Llama2.c project. Karpathy demonstrated that a small language model could be trained and run using only a few hundred lines of portable C code, forming the foundation for this ESP32 project.

### Hardware Requirements [03:40](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=220s)
To build this project, the specific hardware needed is an ESP32S3 with 16 MB of flash and 8 MB of PSRAM — the N16R8 variant. This is critical because the trained and exported embedding table comes to about 15 MB, meaning boards with only four or eight MB of flash will not work.

### A One-Shot Build Script [04:11](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=251s)
The presenter created a single one-shot script to replace the project's scattered instructions. The script checks the board, installs the toolchain, prepares the data, trains the model, exports it, verifies it, builds it, and flashes it to the ESP32 — all in one go. The entire process takes about 25 minutes, with most of the time spent on training the tiny stories model (approximately 30 minutes on a MacBook).

### Running the Model [05:12](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=312s)
Once training completes, LEDs on the panel flash to indicate the model is being loaded. The first example generates a story about a little girl at approximately nine tokens per second. The model eventually loops and restarts the story. A sample script is included for custom prompts, though changing the prompt requires reflashing the ESP32 each time.

### Prompt Limitations [05:43](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=343s)
Testing a custom prompt about a robot produces a different story that mentions the robot, but after the first paragraph the model drifts back to the little girl narrative. A Star Wars opening phrase prompt also immediately drifts back to the little girl story, likely because the model is too small to understand what a galaxy is. No matter the prompt, the model always returns to storytelling because that is its sole training data.

### Final Assessment [07:17](https://www.youtube.com/watch?v=0qXVMt3pIjU&t=437s)
The experiment is genuinely mind-blowing — seeing nine tokens per second on a tiny microchip is impressive — but it remains a very limited proof of concept. The presenter credits Slava for the project and points viewers to a related video about running a real LLM on a first-generation Raspberry Pi.

## Notable Quotes
- "This is a 28.9 million parameter language model generating text right now, one word at a time on a chip that costs about $8."
- "Most of a language model's parameters do not compute anything. They sit in an embedding table that just gets read from."
- "Without Karpathy this probably wouldn't even be possible."
- "No matter what you ask the model, it will always drift back to storytelling because that's what it's trained on."

## People, Tools & References Mentioned
- **Slava S.** — Ukrainian developer who achieved the 28.9M parameter model on the ESP32S3
- **Andrej Karpathy** — Creator of the Llama2.c project that provided the blueprint for running small language models in C
- **Google Gemma** — Source of the per-layer embeddings technique
- **Microsoft researchers** — Creators of the "tiny stories" dataset
- **ESP32S3 (N16R8 variant)** — The microcontroller used, with 16 MB flash and 8 MB PSRAM
- **Llama2.c** — Karpathy's project demonstrating small LLM inference in portable C
- **Tiny Stories dataset** — Microsoft dataset designed for training very small language models
- **Raspberry Pi (first generation)** — Subject of a related video by the same channel

## Who Should Watch
Embedded systems enthusiasts and AI hobbyists who want to understand how language models can be optimized to run on extremely constrained hardware. It is also valuable for anyone interested in the intersection of edge computing and machine learning, even if the current implementation is more of a proof of concept than a practical tool.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=0s">00:00</a></span> This is a 28.9 million parameter language model generating text right now, one word at a time on a chip that costs about $8. There&#x27;s no Wi-Fi. Nothing is being sent to a server. Everything is happening inside an ESP32S3, a microcontroller with less RAM than a computer from the &#x27;90s. This is insane. How is this actually possible? What&#x27;s the magic behind it? and how can we build something similar? Well, those are</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=31s">00:31</a></span> build something similar? Well, those are all good questions that we&#x27;re going to look at in today&#x27;s video. It&#x27;s going to be a lot of fun. So, let&#x27;s dive into it. So, the ESP32S3 is a chip that gives you 512 kilob of SRAMM. And that is the amount of fast memory this chip can compute with. Normally, if you would attempt to run an LLM inside of it, the whole model would have to fit right in there. The last language model anyone got running on a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=63s">01:03</a></span> language model anyone got running on a chip like this topped out at 260,000 parameters. So, this one holds about 110 times more. And the person who pulled it off is a Ukrainian developer, Slava S. So, what&#x27;s the magic trick? How did they do it? How did they fit a 28.9 million parameter model on an eight chip? Well, the workaround comes from an idea Google used in Gemma. It&#x27;s called per layer embeddings. Most of a language model&#x27;s parameters do not compute anything. They</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=94s">01:34</a></span> parameters do not compute anything. They sit in an embedding table that just gets read from. If most of your parameters are only ever looked up, they don&#x27;t need fast memory. So you can get away with leaving that table sitting in a slow cheap flash memory and only pull the rows the current token needs and the small part that actually computes and thinks about the next token the attention head and feed forward stays in SRAMM. Okay, that&#x27;s the compute part. But the question still remains, how do we fit such a big model onto such a tiny</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=125s">02:05</a></span> we fit such a big model onto such a tiny chip? So, the 25 million row table lives in flash memory, and that&#x27;s the biggest chunk of the model&#x27;s whole 28.9 million parameters. And flash is cheap and huge on this particular chip. It has 16 megabytes of it. So, instead of trying to squeeze that table into the same 512 kilob of SRAM, it just stays parked in flash. We pull out about six rows from it, one for each of the model six layers. That&#x27;s roughly 450 bytes total.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=156s">02:36</a></span> layers. That&#x27;s roughly 450 bytes total. Now, before you get too excited, I do have to address the fact that this is a very dumb simple model. This won&#x27;t be your typical GPT style LLM. It won&#x27;t give you code generation or answer questions about difficult topics because if you tried to train a normal model this size on a normal data set, 28 million parameters would just give you gibberish. But this model itself is trained on tiny stories. A data set built by researchers at Microsoft written deliberately simple enough that</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=188s">03:08</a></span> written deliberately simple enough that even a tiny model a few million parameters can learn to write them coherently and running it in plain C on a chip with no operating system and no Python interpreter. That idea comes from the famous Andre Karpathy&#x27;s Llama 2.C C project which showed us that you could train a small language model and run inference on it using nothing but a few hundred lines of portable C and that is the blueprint this entire project is built on without Karpathy this probably wouldn&#x27;t even be possible. So that&#x27;s how</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=220s">03:40</a></span> wouldn&#x27;t even be possible. So that&#x27;s how it works in a nutshell. Now let&#x27;s actually try to build it on our own and run it on the chip to see how it performs. To actually build this ourselves, the first thing you need is the right hardware. Specifically, an ESP32S3 with 16 MGB of flash and 8 MGB of PS RAM. That&#x27;s the N16R8 variant. And this is really important because remember when we talked about that 25 million row table living in flash? Well, by itself, once trained and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=251s">04:11</a></span> flash? Well, by itself, once trained and exported, it comes to about 15 megabytes. But boards with four or eight megabytes of flash simply won&#x27;t hold it. So, if you&#x27;re shopping for a board to follow along, that&#x27;s the one spec you should check first. Now, when I first went through the project&#x27;s actual instructions, the setup was scattered across a few different files and it assumed a fair amount of context I didn&#x27;t have going into it. So instead of walking you through it exactly as written, I put together a single oneshot script that does everything. Checks the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=282s">04:42</a></span> script that does everything. Checks the board, installs the tool chain, prepares the data, trains it, exports it, verifies, builds, and flashes it all in one go. So let&#x27;s go ahead and run that script. And one quick heads up, if you&#x27;re following along, the whole script takes about 25 minutes to finish. And probably that&#x27;s the same time it would take you doing it step by step. It&#x27;s just because there are so many separate commands you have to babysit. And most of the time is actually spent on training the tiny stories model. That</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=312s">05:12</a></span> training the tiny stories model. That takes about 30 minutes on my MacBook. And once the training is done, you&#x27;ll see the LEDs on the panel start flashing. And that&#x27;s an indication that we&#x27;re about to load the model. And once it&#x27;s loaded, here we can see the first basic example of a story of a little girl. And indeed, we&#x27;re getting those nine tokens a second. But you&#x27;ll notice that at a certain point, it will restart the story again. So the model is going in some kind of a loop. And if you want to give it a custom prompt, I&#x27;ve also included a sample script you can use to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=343s">05:43</a></span> included a sample script you can use to run your own custom prompts. So for this example, let&#x27;s start a story about a robot. And another thing to note is that if you change the prompt, you will have to reflash the ESP32 again. And that&#x27;s a limitation of this method. It can only play back one prompt that is pre-flashed at a time. And as you can see, we do get a mention of the robot in the story, and the story is indeed a bit different this time. But notice what happens after the end of the paragraph. We get back to the story of the little girl. So, I have no</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=375s">06:15</a></span> story of the little girl. So, I have no idea why this is happening, but clearly the model tends to steer back to that one specific story about that little girl. And let&#x27;s do another example. And this time, let&#x27;s use the famous phrase that is written at the very beginning of every Star Wars movie. and let&#x27;s see where that takes us. So, this is an interesting one. We can see that the model immediately drifts back to the little girl narrative again. And I&#x27;m assuming that for a model of this size, it doesn&#x27;t even understand what a galaxy is. So, probably that&#x27;s why it&#x27;s ignoring our specific prompt in this</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=407s">06:47</a></span> ignoring our specific prompt in this case. And once again, we see that the next paragraph starts the same story. So although this experiment is impressive and seeing a model produce nine tokens per second on a tiny microchip is genuinely mind-blowing, it&#x27;s still very much a very limited proof of concept. As we saw, no matter what you ask the model, it will always drift back to storytelling because that&#x27;s what it&#x27;s trained on. But if you found this test interesting, I also did another video in a similar realm where I tested out if a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=437s">07:17</a></span> a similar realm where I tested out if a firstg Raspberry Pi could actually run a real LLM locally. So go check out that video if you&#x27;re interested. So there you have it, folks. That&#x27;s how you run a 28.9 million parameter language model on an ESP32 chip. We tested it. It works. So kudos to Slava for making this project. But what are your thoughts on this experiment? Do you see any realworld examples where such an implementation might be useful? Give us your thoughts in the comment section down below. And folks, if you like these types of technical breakdowns, please</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=0qXVMt3pIjU&amp;t=468s">07:48</a></span> types of technical breakdowns, please let me know by smashing that like button underneath the video. And also don&#x27;t forget to subscribe to our channel. This has been Andress from Better Stack, and I will see you in the next videos.</p>

</details>
