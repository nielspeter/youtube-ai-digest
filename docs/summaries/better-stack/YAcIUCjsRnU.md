---
title: "Ex OpenAI CTO's Open-Weight Model Processes Raw Audio"
channel: "Better Stack"
video_id: YAcIUCjsRnU
url: https://www.youtube.com/watch?v=YAcIUCjsRnU
published: 2026-07-23T16:34:35+00:00
generated: 2026-07-23T17:45:26+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/YAcIUCjsRnU/hqdefault.jpg
---
# Ex OpenAI CTO's Open-Weight Model Processes Raw Audio

[![Ex OpenAI CTO's Open-Weight Model Processes Raw Audio](https://i.ytimg.com/vi/YAcIUCjsRnU/hqdefault.jpg)](https://www.youtube.com/watch?v=YAcIUCjsRnU)

[Watch on YouTube](https://www.youtube.com/watch?v=YAcIUCjsRnU) · **Better Stack** · 2026-07-23

## TL;DR
Thinking Machines, the startup founded by ex-OpenAI CTO Mira Murati, released its first open-weight model, a 975-billion-parameter mixture-of-experts model designed specifically for fine-tuning via their Tinker platform. While it underperforms as a generalist model, it stands out by processing raw audio and images directly into token space—eliminating transcription-based data loss—and offering a granular "thinking effort" slider.

## Key Takeaways
- Thinking Machines released a 975B-parameter mixture-of-experts model (Apache 2.0), with only ~41B parameters active per token.
- The model is explicitly not designed to compete with frontier generalist models and underperforms on agentic benchmarks like Terminal Bench.
- Its primary purpose is to be fine-tuned for narrow, specific tasks using the Tinker platform.
- Unlike most multimodal models, it processes raw audio as spectrograms and images as 40×40 pixel patches directly in token space, avoiding the data loss of transcription-based approaches.
- Fine-tuning is best for teaching a model *how* to answer (tone, structure, latency reduction), not *what* to know; retrieval is better for adding new knowledge.
- Tinker uses LoRA (low-rank adaptation) for efficient, cost-effective fine-tuning rather than retraining the full model.
- Inkling is the only model on Tinker that accepts raw audio, shipping with cookbook recipes for speech recognition, speaking-style classification, and medical dictation.
- The model offers a granular "thinking effort" slider (0 to 1), unlike competitors that offer only 2–3 preset levels.
- Real-world fine-tuning examples (e.g., Harvey's legal citation tool) show small fine-tuned models matching or beating GPT-4o on narrow tasks while running faster.

## Detailed Breakdown

### Model Release and Positioning [00:00](https://www.youtube.com/watch?v=YAcIUCjsRnU&t=0s)
Thinking Machines, a $12-billion startup founded by former OpenAI CTO Mira Murati, released its first model. It is a 975-billion-parameter model, Apache 2.0 licensed, with weights available on Hugging Face. The model is not intended to compete with frontier labs but is built specifically to be fine-tuned using their platform, Tinker.

### Benchmark Performance and Architecture [01:00](https://www.youtube.com/watch?v=YAcIUCjsRnU&t=60s)
The company is transparent that the model is weaker than general models on the market. Benchmarks show it beats GLM-130B on instruction following (79.8 vs. 73.3) but loses badly on Terminal Bench (63.8 vs. 82.7), meaning it follows orders well but struggles with autonomous agentic work. Under the hood, it is a mixture-of-experts model with 256 unique experts per layer; each token activates only 6 experts, meaning roughly 41 billion parameters are active at any given time.

### Native Multimodal Processing [01:31](https://www.youtube.com/watch?v=YAcIUCjsRnU&t=91s)
The model handles multimodal input differently from standard models. Rather than using a separate speech or vision encoder to transcribe audio or describe images into text (which causes data loss), it feeds raw audio as spectrograms—chopping sound frequency bands into buckets—and images as 40×40 pixel patches directly into the same token space as text. The model processes all tokens together, theoretically reducing data loss and compression.

### When to Fine-Tune vs. Use Retrieval [02:32](https://www.youtube.com/watch?v=YAcIUCjsRnU&t=152s)
Fine-tuning teaches a model *how* to answer, not *what* to know. It is ideal for tone, rigid structured output, and cost/latency distillation where using a smaller model for a narrow task is cheaper than a large generalist model. However, if the model needs new knowledge, retrieval is better; a well-cited paper showed retrieval consistently outperforming fine-tuning for knowledge. Fine-tuning can also degrade reasoning by disrupting chain-of-thought, with smaller models suffering most.

### Real-World Fine-Tuning Results and LoRA [03:34](https://www.youtube.com/watch?v=YAcIUCjsRnU&t=214s)
Harvey, a company building AI tools for law firms, fine-tuned a small model to extract legal citations, improving F1 score from 0.56 to 0.68. The fine-tuned model beat or tied GPT-4o 93% of the time and ran faster. Thinking Machines demoed Inkling fine-tuning itself via Tinker to avoid the letter "E," automatically correcting its training data. Fine-tuning uses LoRA (low-rank adaptation), which freezes original weights and injects lightweight matrices, making the process far cheaper and faster than full retraining.

### Why Choose Inkling on Tinker [05:06](https://www.youtube.com/watch?v=YAcIUCjsRnU&t=306s)
Tinker supports multiple open models (Qwen, Kimmy, DeepSeek, Nvidia's NeMo-Tron, OpenAI's GPT-OSS), and Inkling is pricier. However, it is the only model on Tinker that accepts raw audio, shipping with cookbook recipes for speech recognition, speaking-style classification, and medical prescription dictation. It also offers a continuous "thinking effort" slider from 0 to 1, unlike GPT-OSS's low/medium/high presets.

### Final Recommendation [05:37](https://www.youtube.com/watch?v=YAcIUCjsRnU&t=337s)
If you need a model to run well out of the box, Inkling is not the right choice. But for narrow, high-volume tasks with labeled data and a way to grade output, fine-tuning a small open model via Tinker is highly recommended. If your task involves audio, Inkling is the strongest option on Tinker. For a generalist open model, the host recommends checking out Chimera 3 instead.

## Notable Quotes
- "Fine-tuning teaches a model how to answer, not what to know."
- "The audio goes straight in as a spectrogram... nothing's getting squashed down into text."
- "If you've got a narrow, high-volume job, some real label data, and a way to grade the output, fine-tuning a small open model is one of the most underrated things you can do right now."

## People, Tools & References Mentioned
- **People:** Mira Murati (ex-OpenAI CTO, founder of Thinking Machines), Warren (host)
- **Models:** Inkling (Thinking Machines), GLM-130B, GPT-4o, GPT-OSS, Qwen, Kimmy, DeepSeek, Nvidia NeMo-Tron, Chimera 3
- **Tools/Platforms:** Tinker (Thinking Machines' fine-tuning platform), Hugging Face
- **Companies:** Thinking Machines, Harvey (AI legal tools), OpenAI, Anthropic, Nvidia
- **Concepts/Techniques:** Mixture of Experts (MoE), LoRA (low-rank adaptation), spectrograms, F1 score, Terminal Bench, Apache 2.0 license
- **References:** A well-cited paper comparing retrieval against fine-tuning (retrieval won consistently)

## Who Should Watch
AI developers, ML engineers, and technical founders evaluating open-weight models for fine-tuning narrow, high-volume tasks—especially those involving raw audio processing—will find this video valuable for understanding Inkling's unique capabilities and when fine-tuning is the right approach.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=0s">00:00</a></span> Thinking Machines, the 12-billion startup from ex-OpenAI CTO Mira Murati, just dropped its first-ever model. There&#x27;s 975 billion parameters, it&#x27;s Apache 2.0 licensed, and the weights are all on Hugging Face for anyone to download. And although it&#x27;s not competing with Frontier Labs like Anthropic, its actual goal is to be fine-tuned specifically with its own platform, Tinker. So, if you need a model that&#x27;s trained on a highly specific task, then this might be exactly what you&#x27;re looking for. Today, we&#x27;ll cover why you&#x27;d want to use this</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=30s">00:30</a></span> we&#x27;ll cover why you&#x27;d want to use this model specifically and all of the reasons why you&#x27;d want to fine-tune. And there&#x27;s a super interesting way that this model processes audio and visual, which I&#x27;ve never seen before. So, stick around and we&#x27;re going to cover that as well in this video. And we cover AI topics constantly on this channel, so if you want to stay up to date, then subscribe to Better Stack. Thinking Machines are very upfront about the fact that their new model is not as strong as basically any general model on the market, and they say this in their</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=60s">01:00</a></span> the market, and they say this in their launch post. So, they&#x27;re just managing expectations, and you can see why in the benchmarks. On instruction following, it does beat GLM-130B 79.8 to 73.3, but on terminal bench, where agents go off and actually do work, it gets beaten badly with 63.8 to 82.7. So, it&#x27;s good at following orders, but much weaker at working things out on its own. However, it is a great starting point if your intention is to fine-tune. Under the hood, it&#x27;s a mixture of experts, so there&#x27;s 975 billion parameters in total, but each layer</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=91s">01:31</a></span> parameters in total, but each layer holds 256 unique experts, and each token only gets sent to six of them, which means only about 41 billion parameters are doing any work at any single time. It&#x27;s also multimodal, so images, text, and audio all go in, and the way it does this is much different to any model you would have seen before. Normally, when a model handles audio, for example, there&#x27;s a separate speech model in front of the language model that transcribes the text and then passes that transcript to the language model. Images can work in the same way. A vision encoder looks</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=122s">02:02</a></span> in the same way. A vision encoder looks at the picture and then creates a description for the image and then passes that to the language model. And of course, doing this means that there&#x27;s going to be some form of data loss along the way. Inklein doesn&#x27;t do any of that. The audio goes straight in as a spectrogram. So, the raw frequency bands of the sound are chopped up into buckets. Images also go in as 40 by 40 pixel patches. Both get dropped straight into the same space where the text tokens live and the model choose through all of them together. So, nothing&#x27;s getting squashed down into text. So, theoretically, you should get much less</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=152s">02:32</a></span> theoretically, you should get much less data loss and compression when processing things like audio and visual specifically with the Inklein model. And in fact, compared to most generalist models which don&#x27;t support raw audio at all, Inklein clearly stands out. Now, whether you should even fine-tune at all comes down to your specific goals. The rule of thumb is generally that fine-tuning teaches a model how to answer, not what to know. For example, tone of voice or rigid structured output where thousands of examples would be needed in context to guide the model&#x27;s output because passing thousands of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=183s">03:03</a></span> output because passing thousands of examples via a prompt would just be impractical. Also, cost and latency distillation where performing a narrow task with a general model would be considerably more expensive than fine-tuning a smaller model. Basically, if there&#x27;s any situation where you need thousands of examples to get decent output, then that could benefit from fine-tuning. But if you need the model to know things it doesn&#x27;t know, then don&#x27;t fine-tune. There&#x27;s actually a well-cited paper which puts retrieval up against fine-tuning and retrieval won consistently. And if you want better reasoning, then fine-tuning can actually</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=214s">03:34</a></span> reasoning, then fine-tuning can actually make it worse because it degrades the model&#x27;s chain of thought. And interestingly, smaller models suffer the most. But specifically for narrow jobs, the results from fine-tuning can be great. We take Harvey who build AI tools for law firms. They trained a small model to pull citations out of legal documents. They scored its F1, which is a metric used to evaluate the performance of a classification model, and fine-tuning took them from 0.56 to 0.68. And head-to-head against GPT-4.0,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=244s">04:04</a></span> 0.68. And head-to-head against GPT-4.0, the smaller model won or tied 93% of the time, and it even ran faster. Thinking Machines even show a demo forcing Inkling to never use the letter E, where you can literally prompt it to fine-tune itself via Tinker. It then goes off and corrects the training data set and can run the full fine-tuning process completely automatically. And the result of this is a model that has severe epsilon-phobia, and somehow their responses still make sense. But you&#x27;re not retraining the entire model here, you&#x27;re actually using something called LoRA, which stands for low-rank adaptation. Instead of training the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=276s">04:36</a></span> adaptation. Instead of training the entire model, LoRA freezes the original weights and injects lightweight smaller matrices to capture new specific data. This provides advantages of cost and speed for post-training compared to fine-tuning an entire model, which likely would just be impractical. Now, Tinker already supports a bunch of open models like Queen, Kimmy, Deep Seek, Nvidia&#x27;s NeMo-Tron, and OpenAI&#x27;s GPT-OSS. And Inkling is one of the pricier ones, so why would you even bother with it? Well, there&#x27;s two reasons, and we&#x27;ve covered them a little bit already. The first is audio. Of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=306s">05:06</a></span> bit already. The first is audio. Of every model on the platform, Inkling is the only one that takes audio at all. Plenty of them do images, Kimmy and most of the Queen models handle vision fine, but not one of them actually handles raw sound. And they&#x27;ve also shipped three cookbook recipes to go with it like speech recognition and speaking style classification. So the model can tell you how something was said, not just what was said. And there&#x27;s also a medical example trained on dictated prescriptions, teaching it drug names that most models would otherwise mangle. The second is thinking effort. Inkling lets you set how hard it thinks as a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=337s">05:37</a></span> lets you set how hard it thinks as a number from zero to one. Most models give you a switch of two to three settings, GPT-OSS gives you low, medium, and high, for example, but Inkling gives you an entire slider. So the big question is, should you actually use it? Well, if you want a model to run as it comes, then this probably isn&#x27;t it, and they&#x27;ll be explicit about that themselves. But, if you&#x27;ve got a narrow, high-volume job, some real label data, and a way to grade the output, fine-tuning a small open model is one of the most underrated things you can do right now. And with platforms like Tinker, it&#x27;s so much easier. And whether</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=YAcIUCjsRnU&amp;t=368s">06:08</a></span> Tinker, it&#x27;s so much easier. And whether Inkling is the one you train really comes down to what you&#x27;re feeding it. If there&#x27;s audio going in, Inkling is a strong choice, and nothing else on Tinker even takes raw audio right now. And if you&#x27;re looking for the best open generalist model right now, we&#x27;ve just done a video on Chimera 3 you can watch here, and that has had some incredible results. But, otherwise, thank you for watching. I&#x27;ve been Warren from Better Stack, and I&#x27;ll catch you in the next one.</p>

</details>
