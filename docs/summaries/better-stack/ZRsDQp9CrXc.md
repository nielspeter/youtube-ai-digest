---
title: "Stop Paying for Dictation! This App Is Better and Free. (handy)"
channel: "Better Stack"
video_id: ZRsDQp9CrXc
url: https://www.youtube.com/watch?v=ZRsDQp9CrXc
published: 2026-07-30T20:10:06+00:00
generated: 2026-07-30T21:20:32+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/ZRsDQp9CrXc/hqdefault.jpg
---
# Stop Paying for Dictation! This App Is Better and Free. (handy)

[![Stop Paying for Dictation! This App Is Better and Free. (handy)](https://i.ytimg.com/vi/ZRsDQp9CrXc/hqdefault.jpg)](https://www.youtube.com/watch?v=ZRsDQp9CrXc)

[Watch on YouTube](https://www.youtube.com/watch?v=ZRsDQp9CrXc) · **Better Stack** · 2026-07-30

## TL;DR
Handy is a free, open-source, offline speech-to-text dictation app built with Rust and React that lets you choose your own transcription model. In testing, it significantly outperformed Google Docs voice typing and came very close to the commercial Whisper Flow, while offering full privacy and zero subscription costs.

## Key Takeaways
- Handy runs completely offline with no cloud, no account, and no subscription.
- It is MIT-licensed and designed to be the most "forkable" dictation app rather than necessarily the "best" one.
- The app uses Rust for the backend and React/TypeScript for the settings UI.
- Handy supports multiple model families, including Whisper (via Transcribe CPP) and Parakeet (via Transcribe RS).
- A built-in utility called Silero VAD filters out silence so compute isn't wasted transcribing dead air.
- Users can drop their own fine-tuned Whisper GGML models into the app's folder for custom use.
- In testing, Handy correctly punctuated text and recognized technical terms, vastly outperforming Google Docs voice typing.
- The commercial Whisper Flow still edged out Handy slightly in accuracy, but not by a wide margin.
- Privacy is a major advantage: all audio stays on the user's machine and isn't used to train other models.
- The presenter found the Parakeet 0.6B model ideal because it's CPU-optimized and runs efficiently even in the background.

## Detailed Breakdown

### Introduction to Handy [00:00](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=0s)
The video introduces Handy, an open-source speech recognition and dictation app that runs entirely offline. The host highlights that it requires no cloud, subscription, or account, and allows users to select their preferred dictation model. He notes it has become his favorite speech-to-text tool and sets up a comparison against commercial options like Whisper Flow.

### Overcoming Skepticism [00:31](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=31s)
The host admits he was previously skeptical of dictation apps, not wanting to pay for commercial products or risk high CPU usage from local open-source models. Handy changed his mind on both fronts, prompting a deeper look into how the app is built and operates.

### Architecture and Tech Stack [01:02](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=62s)
Handy was built by developer CJ Pace with Tari. The backend is written in Rust, while the settings UI uses React and TypeScript. Transcribe CPP runs Whisper family models (in GGM and GGUF formats), and Transcribe RS runs Parakeet. The CPAL library handles cross-platform audio input, RDEV manages global keyboard shortcuts, and a library called Robboto handles real-time audio streaming and resampling. This combination makes the app lightweight even on a MacBook.

### User Workflow and Model Selection [01:33](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=93s)
The user experience is straightforward: you set a custom keyboard shortcut to toggle dictation or use push-to-talk. While speaking, Silero VAD filters out background silence to save compute. Upon release, Handy sends audio to the chosen model and pastes text into the focused input. The app lists available models with speed and accuracy meters, letting users prioritize which metric matters most—likened to choosing a character in Mario Kart.

### Model Performance and Custom Models [02:35](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=155s)
The host found the Parakeet unified 0.6B model works well for him because it is CPU-optimized, running at around five times real-time speed on a mid-range i5. His M2 Max handles it effortlessly. Handy also offers language-specific models (e.g., Russian, Ukrainian) and supports dropping custom fine-tuned Whisper GGML models into the app's models folder, which then appear as selectable options after a restart.

### Privacy and Licensing [03:07](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=187s)
Handy's mission statement is honest: it isn't trying to be the best speech-to-text app, but the most forkable one. The host emphasizes that Handy's biggest advantage over Whisper Flow is that it works offline, requires no account or subscription, and keeps all audio local—ensuring samples aren't secretly used to train other voice models. He praises the fact that it is MIT-licensed.

### Testing Against Google Docs Voice Typing [03:38](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=218s)
To test performance, the host simultaneously activates Google Docs voice typing and Handy's shortcut, then speaks a paragraph containing technical terms (SQLite, Cobalt, GPU cluster, Grock, ChatGPT). Google's transcription fails to add punctuation, misrecognizes "Cobalt" and "SQLite," transcribes "Grock" as "rock," and hilariously renders "ChatGPT" as "Chad GPT." Handy, by contrast, adds punctuation and gets most technical terms correct.

### Testing Against Whisper Flow [05:13](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=313s)
The host repeats the same passage using the commercial Whisper Flow app. Whisper Flow performs the best overall, separating sentences correctly and recognizing all terms accurately. However, the host notes the difference between Handy and Whisper Flow is minimal, and he still prefers Handy because it is free, private, and open source—though he acknowledges Whisper Flow is a solid service.

### Conclusion [07:20](https://www.youtube.com/watch?v=ZRsDQp9CrXc&t=440s)
The host reiterates that Handy has become his favorite dictation tool, joking that he might forget how to type if he overuses it. He invites viewer feedback in the comments, asks for likes and subscriptions, and signs off as Andress from Better Stack.

## Notable Quotes
- "Handy isn't trying to be the best speech-to-text application. It's trying to be the most forkable one."
- "I know for sure that all my dictation audio samples stay on my machine and they're not being secretly used to train other voice models."
- "It's kind of like choosing your favorite character in Mario Kart. You can decide which metric is the priority for you."
- "Chad GPT. Nice."
- "I wasn't joking when I said that this has truly become my favorite dictation tool. And I'm honestly afraid that I might forget how to type on my keyboard if I start overusing it too much."

## People, Tools & References Mentioned
- **Handy** — the open-source dictation app reviewed
- **CJ Pace with Tari** — developer(s) of Handy
- **Whisper Flow** — commercial dictation app used for comparison
- **Google Docs Voice Typing** — Google's transcription service used for comparison
- **Transcribe CPP / Transcribe RS** — libraries for running Whisper and Parakeet models
- **Silero VAD** — silence-filtering utility
- **CPAL** — cross-platform audio input library
- **RDEV** — global keyboard shortcuts library
- **Robboto** — real-time audio streaming and resampling library
- **Parakeet unified 0.6B** — CPU-optimized speech recognition model
- **Whisper (GGM/GGUF/GGML)** — speech recognition model family
- **Grock, ChatGPT, SQLite, Cobalt** — technical terms used in the dictation test
- **Rust, React, TypeScript** — technologies used to build Handy
- **MIT license** — Handy's open-source license

## Who Should Watch
Developers, privacy-conscious users, and anyone tired of paying subscriptions for dictation software will find this video valuable. It's especially relevant for those who want a lightweight, offline, open-source alternative to commercial speech-to-text tools and are curious about how it stacks up in real-world testing.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=0s">00:00</a></span> This is Handy. It&#x27;s an open-source speech recognition and dictation app that runs completely offline with no cloud, no subscription, no account, and it lets you choose your own favorite dictation model. And I honestly think that this has now become my favorite speechtoext dictation tool. So, in this video, we&#x27;ll take a look at Handy, see how it works, and we&#x27;ll run a few tests to see how it performs and how it ranks up against heavy weights like the commercial whisper flow. It&#x27;s going to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=31s">00:31</a></span> commercial whisper flow. It&#x27;s going to be a lot of fun. So, let&#x27;s dive into it. Up until now, I was kind of skeptical of speech dictation apps, and I just couldn&#x27;t find one that I wanted to use. I didn&#x27;t want to use any commercial products and pay for dictation. And I was also worried about the fact that using an open- source tool with a local dictation model might hog up my CPU. But Handy actually changed my mind on both of those issues. So first off, let&#x27;s talk about how Handy is actually built</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=62s">01:02</a></span> talk about how Handy is actually built and how it works. Handy was built by the developer CJ Pace with Tari. So it uses Rust for the back end and React and TypeScript for handling the settings UI on top. Transcribe CPP runs the Whisper family models in GGM and GGUF format. Transcribe RS runs Parakeet. The CPAL library handles the cross-platform audio input. RDEV owns the global keyboard shortcuts. And it uses a library called Robboto, which provides real-time audio</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=93s">01:33</a></span> Robboto, which provides real-time audio streaming and takes care of resampling. And this combination makes it super easy and super lightweight to use it even on my MacBook. And the flow itself is dead simple from the user side. You set a custom keyboard shortcut and then either toggle it on or off or hold it down for pushto talk. And while you&#x27;re holding it, there&#x27;s a utility called Silero VAD which is quietly filtering out the silence in the background so you&#x27;re not burning compute transcribing complete silence. And when you let go, Handy sends the audio to whichever model you</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=125s">02:05</a></span> sends the audio to whichever model you picked and then pastes the transcribed text directly into whatever input is focused at that moment. And to be fair, Handy is not unique in this way. A lot of other dictation applications on the market work in a similar way. But the thing I love the most is that you can choose your own preferred model. And each of the models listed in the model section has a speed and accuracy meter. So it&#x27;s kind of like choosing your favorite character in Mario Kart. You can decide which metric is the priority for you. In my case, I found that using</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=155s">02:35</a></span> for you. In my case, I found that using the Parakeet unified 0.6 billion parameter model works very well for me because Parakeet is a CPUon model and by their own numbers, it runs at around five times real-time speed on a mid-range i5 chip and my M2 Max is way past that spec. So, I don&#x27;t even notice it when I&#x27;m running it in the background. And there are so many other options to choose from. They even have models that are specific to one language. For example, we have some Russian ones, some Ukrainian ones, and I love the honesty coming from Hi&#x27;s</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=187s">03:07</a></span> love the honesty coming from Hi&#x27;s mission statement. Handy isn&#x27;t trying to be the best speechtoext application. It&#x27;s trying to be the most forkable one. And you can even drop your own fine-tuned Whisper GGML models into the apps models folder, restart it, and then it just shows up as a custom option. And I think the biggest reason why I would choose Handy over something like Whisperflow any time of the day is because Handy just works offline and I don&#x27;t need to set up an account and there&#x27;s no subscription and I know for sure that all my dictation audio samples</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=218s">03:38</a></span> sure that all my dictation audio samples stay on my machine and they&#x27;re not being secretly used to train other voice models. So, I&#x27;m super happy that we now have an MIT licensed dictation tool like this. So, all that sounds great, but let&#x27;s actually put Handy up to the test and see how it performs. I&#x27;ll be comparing Hiy&#x27;s performance against Whisperflow and also against Google&#x27;s own transcription service, which is available here in Google Docs. So, here on the Google Docs page, I&#x27;m going to activate Google&#x27;s own voice typing mode.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=249s">04:09</a></span> activate Google&#x27;s own voice typing mode. And at the same time, I will be holding down Handy&#x27;s transcription shortcut. And then I&#x27;m just going to go on a random tangent. And by the end of it, we&#x27;ll see what kind of result each of the service gives us and compare the two. Um, so um, yesterday I went to pick up some groceries and on my way back home I suddenly remembered that I have to head back and hook up my SQLite database to a Cobalt service that is running on my</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=281s">04:41</a></span> Cobalt service that is running on my custom GPU cluster. I didn&#x27;t actually know how to do this. So, um, I had to ask for help and the only tool I could think of which could help me was an LLM called Grock. And then I also got a bit of help from chat GPT. And by the end of it, we got a working application running, but it was a really big hassle. Let&#x27;s separate these two. So, as you can</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=313s">05:13</a></span> Let&#x27;s separate these two. So, as you can see here, the Google voice typing service is a lot worse. It doesn&#x27;t add any punctuations. It doesn&#x27;t know how to split your sentences. It didn&#x27;t get cobalt correctly. It didn&#x27;t get the SQLite database correctly. Um, it didn&#x27;t even get the word LLM correctly. It thought that Grock was rock. And this is my favorite one. It thought that Chad GPT was Chad GPT. Chad GPT nice. Um, so yeah, so you can</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=345s">05:45</a></span> Chad GPT nice. Um, so yeah, so you can clearly see that handy is a lot better because it does give you punctuation. It does recognize certain terms and it got most of the technical terms correctly. And now let&#x27;s also compare this result with Whisper Flow. So I&#x27;m going to try to repeat the same text as closely as possible to be fair to this test. Um, so, um, yesterday I went to pick up some groceries. Um, and on my way back I suddenly remembered that I have to head</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=376s">06:16</a></span> suddenly remembered that I have to head back home and hook up my SQLite database to a Cobalt service that is running on my custom GPU cluster. Now, I didn&#x27;t actually know how to do this, so I had to ask for help. And the only tool I could think of which could help me was an LLM called Grock. And then I also got a bit of help from Chad GPT. And by the end of it, we got a working application running, but it was a really big hassle.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=408s">06:48</a></span> running, but it was a really big hassle. Okay. And you can clearly see that Whisper Flow did the best job. It separated the sentences correctly and it got all of the terms right. So, because this is a commercial application, you would expect that it&#x27;s going to be better than the open-source tool, but honestly, there isn&#x27;t that much of a difference between this result and Whisper Flows. So, I still kind of prefer using Handy just because it&#x27;s free and private and open source, but</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=440s">07:20</a></span> free and private and open source, but Whisper Flow did a very good job here. So, it is a solid service nonetheless. So, there you have it, folks. That is handy in a nutshell. I wasn&#x27;t joking when I said that this has truly become my favorite dictation tool. And I&#x27;m honestly afraid that I might forget how to type on my keyboard if I start overusing it too much. But those are just my thoughts and my observations. But what do you think about Handy? Have you tried it? Will you use it? Let us know in the comments section down below. And folks, if you like these types of technical breakdowns, please let me know</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=ZRsDQp9CrXc&amp;t=472s">07:52</a></span> technical breakdowns, please let me know by smashing that like button underneath the video. And also don&#x27;t forget to subscribe to our channel. This has been Andress from Better Stack and I will see you in the next videos.</p>

</details>
