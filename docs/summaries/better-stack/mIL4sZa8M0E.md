---
title: "Open-Source Dictation Is Here… Goodbye Subscriptions"
channel: "Better Stack"
video_id: mIL4sZa8M0E
url: https://www.youtube.com/watch?v=mIL4sZa8M0E
published: 2026-07-10T12:00:12+00:00
generated: 2026-07-12T21:44:29+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/mIL4sZa8M0E/hqdefault.jpg
---
# Open-Source Dictation Is Here… Goodbye Subscriptions

[![Open-Source Dictation Is Here… Goodbye Subscriptions](https://i.ytimg.com/vi/mIL4sZa8M0E/hqdefault.jpg)](https://www.youtube.com/watch?v=mIL4sZa8M0E)

[Watch on YouTube](https://www.youtube.com/watch?v=mIL4sZa8M0E) · **Better Stack** · 2026-07-10

## TL;DR
Fluid Voice is a free, open-source Mac dictation app that runs entirely locally, using a Parakeet speech model and a "Fluid Intelligence" editor model to transcribe and clean up your voice into formatted text. It offers a compelling, subscription-free, privacy-preserving alternative to paid cloud tools like Whisper Flow, though it's currently Mac-only (best on Apple Silicon) and requires a sizable model download.

## Key Takeaways
- Fluid Voice is a free, open-source dictation app for Mac that processes everything locally—no audio is sent to the cloud.
- It uses two local models: Parakeet for transcription and Fluid Intelligence for editing/cleanup (capitalization, punctuation, structure).
- A single hotkey lets you speak, and cleaned-up text drops directly into whatever app your cursor is in (Cursor, Claude, notes, etc.).
- It's roughly four times faster than other dictation options and produces well-formatted, punctuated text without any waiting spinners.
- The built-in Mac dictation is free but inadequate for commit messages, docs, or anything someone else will read.
- Paid alternatives like Whisper Flow and Super Whisper cost money and often send audio to the cloud, which can be a dealbreaker for privacy-conscious developers.
- Fluid Voice is best on Apple Silicon (M-series) machines; it runs on Intel Macs but is slower.
- Downsides: Mac-only (Windows and iOS are on a waitlist), the editor model is a ~3.5 GB download, and non-English dictation may require tuning.
- The recommended setup is to use Fluid Voice as your everyday Mac dictation tool and keep a cross-platform option around for when you're not on Mac.

## Detailed Breakdown
### The Problem with Existing Dictation Tools [00:00](https://www.youtube.com/watch?v=mIL4sZa8M0E&t=0s)
The video opens by acknowledging the appeal of talking to your computer instead of typing, but notes that existing solutions often fall short. Apple's built-in Mac dictation is free but not good enough for serious use, while paid options like Whisper Flow add yet another monthly subscription to your stack.

### Introducing Fluid Voice and Its Local-First Approach [00:32](https://www.youtube.com/watch?v=mIL4sZa8M0E&t=32s)
Fluid Voice is presented as a free, open-source Mac app that handles all voice-to-text processing on your own machine. The presenter highlights two key benefits: privacy (your voice and dictated content—potentially code—never leave your Mac) and cost (no subscription fees).

### How It Works: Two Local Models [01:05](https://www.youtube.com/watch?v=mIL4sZa8M0E&t=65s)
Fluid Voice uses a model called Parakeet to transcribe speech, then a second local model called Fluid Intelligence acts as an editor, fixing capitalization, punctuation, and structure. You set a hotkey, speak, and the cleaned-up text is inserted wherever your cursor currently is—whether that's Cursor, Claude, or a notes app.

### Quick Demo and Setup [01:36](https://www.youtube.com/watch?v=mIL4sZa8M0E&t=96s)
Setup is a one-line install, after which you grant mic and accessibility permissions (standard for Mac apps). You can choose a custom hotkey or use the built-in one. In the demo, the presenter holds the key and speaks a code-review request; the app instantly produces properly capitalized, punctuated, and formatted text with no spinner or cloud delay.

### How It Compares to the Competition [02:07](https://www.youtube.com/watch?v=mIL4sZa8M0E&t=127s)
Fluid Voice is described as four times faster than other options. The free Mac dictation is fine for text messages but not for commit messages or docs. Whisper Flow is paid and cloud-based, which is a dealbreaker for many before price is even considered. Super Whisper and similar tools are good but still cost money and don't match Fluid Voice's local cleanup quality. Fluid Voice stands out as the only free, open-source option that does smart formatting on-device.

### Limitations and Caveats [03:09](https://www.youtube.com/watch?v=mIL4sZa8M0E&t=189s)
Before recommending it, the presenter lists drawbacks: it's Mac-only (Windows and iOS are waitlisted), the editor model is a ~3.5 GB download, it's best on Apple Silicon (slower on Intel), and non-English dictation may need tuning. These are framed as things to know upfront rather than after a frustrating download.

### Final Verdict and Practical Advice [03:40](https://www.youtube.com/watch?v=mIL4sZa8M0E&t=220s)
For most Mac developers, Fluid Voice is worth trying—especially if you want to avoid another monthly payment. It's great for emails, docs, code comments, Slack messages, and even talking to Claude. On an M4 Pro Mac, it's fast and fully local. If you need Windows or iOS support, it's not ready yet. The practical recommendation: use Fluid Voice as your everyday Mac tool and keep a cross-platform option for when you're off Mac. Links and the brew command are in the video description.

## Notable Quotes
- "Nothing ever gets shipped off to a server somewhere, which is a huge win."
- "A model called Parakeet listens and writes down what you say. Then a second local model called Fluid Intelligence acts like an editor sitting right next to you fixing your capitalization, punctuation and structure as you talk."
- "No spinner, no waiting because there's no cloud to actually wait on here."
- "The free one that was supposed to be the weakest, it's the only one that's free, open-source, and does the smart formatting right there on our machine."
- "It's worth it if you don't want another monthly payment just to dictate things for you, which come on, who does want that?"

## People, Tools & References Mentioned
- **Fluid Voice** – Free, open-source local dictation app for Mac
- **Whisper Flow** – Paid, cloud-based dictation tool
- **Super Whisper** – Another paid dictation tool
- **Parakeet** – Local speech-to-text model used by Fluid Voice
- **Fluid Intelligence** – Local editor model used by Fluid Voice for cleanup and formatting
- **Apple Silicon (M-series, M4 Pro)** – Hardware referenced as ideal for running Fluid Voice
- **Intel Macs** – Supported but slower
- **Cursor, Claude, Slack** – Example apps where dictated text can be inserted
- **Homebrew (brew)** – Installation method referenced in the description

## Who Should Watch
Mac-based developers and power users who want a private, subscription-free alternative to cloud dictation tools and are curious whether a fully local solution can match paid options in speed and formatting quality.


<details class="transcript">
<summary>Full transcript</summary>

<p>just to talk to your computer instead of typing it all out. You end up with another subscription to something like Whisper Flow. And yeah, it&#x27;s good. You&#x27;d think the free thing we already have on Mac would be good enough, but it&#x27;s not. This is Fluid Voice. It runs completely on your own machine, and it&#x27;s growing in popularity as a strong competitor to Whisper Flow and all the others. Fluid Voice is a free open-source Mac app that turns your voice into text and</p>
<p>app that turns your voice into text and every part of that happens on your own computer. Nothing ever gets shipped off to a server somewhere, which is a huge win. Two reasons this is good for us. And there are the exact two things devs complain about. First, your voice and whatever you&#x27;re dictating might be code or private and this never leaves your Mac. Second, you&#x27;re not paying another monthly bill to do it. Here&#x27;s how simple this is. A model called parakeet listens and writes down what you say. Then a second local model called fluid intelligence acts like an editor sitting</p>
<p>intelligence acts like an editor sitting right next to you fixing your capitalization, punctuation and structure as you talk. You hit one hotkey that you set speak and the cleaned up text drops into whatever your cursor is already at into cursor cla notes. Doesn&#x27;t really care which one. Now, this is super [snorts] simple to spin up, so I&#x27;ll keep the demo short, too. It&#x27;s a oneline install. You open it, give it mic and accessibility permissions. Every Mac app makes you do this, so you have to do it anyways. And then you can choose a hotkey or use the</p>
<p>then you can choose a hotkey or use the one builtin. So, there&#x27;s no real difference here. Now, watch this. I hold the key and I just talk normally here. Can you check over my code and make sure it&#x27;s set up with some good practices to prevent bugs? And it didn&#x27;t just collapse. Look at what it just did. It capitalized the line, punctuated it, kept my technical word spelled right, and formatted it like an actual comment. I didn&#x27;t fix one thing. No spinner, no waiting because there&#x27;s no cloud to actually wait on here. So, where does this actually sit</p>
<p>here. So, where does this actually sit next to everything else? Well, this is actually four times faster than using other ones already out there. And on top of that, this is where it gets interesting. The dictation already on your Mac is free, and for a text message, it&#x27;s fine. for a commit message or a doc, someone actually going to read that. It&#x27;s probably not so great. Whisper flow is the paid, so you&#x27;d expect it just wins here. But it&#x27;s subscription, your audio goes to a cloud. For a lot of us, that second part is a deal breaker before we even get to the price. Super whisper and the rest are good tools. Still cost money. They</p>
<p>are good tools. Still cost money. They don&#x27;t quite match the local cleanup Fluid Voice is actually doing. So, the free one that was supposed to be the weakest, it&#x27;s the only one that&#x27;s free, open- source, and does the smart formatting right there on our machine. On Apple Silicon, it&#x27;s fast enough that you can forget it&#x27;s even thinking. Now, before you run off and install this, it&#x27;s great that it&#x27;s free, right? There&#x27;s no subscription. It&#x27;s great that it&#x27;s private. Our voice stays on our Mac. On M series machines, it&#x27;s fast and the formatting is actually pretty good, and it&#x27;s open source and actively worked</p>
<p>and it&#x27;s open source and actively worked on, so problems are getting fixed. But on the flip side of things, it&#x27;s Mac only right now. iOS and Windows are on the wait list. So if you live on Windows, this isn&#x27;t your tool just yet. The editor model is about 3 and 1/2 gigs, so it&#x27;s a real download. It&#x27;s not a quick one. It&#x27;s best, like I said, on the silicone chips. It does run on Intel. It&#x27;s just slower. And if you dictate in a language other than English, you might have to tune it to get it just right. But you should know all that now, not after you spend 10 minutes trying to download this the hard</p>
<p>minutes trying to download this the hard way. You&#x27;d probably expect me to say it&#x27;s worth it now, but I won&#x27;t. For most Mac devs, yeah, okay, this might be worth giving a shot. It&#x27;s worth it if you don&#x27;t want another monthly payment just to dictate things for you, which come on, who does want that? Use it for boring typing, email, docs, code comments, Slack messages. Heck, talk to Claude. On a Mac M4 Pro, it&#x27;s really nice because it&#x27;s all local and it&#x27;s quick. If you need Windows or iOS right now, sorry, but this can&#x27;t help you. So, here&#x27;s what you could actually do. Run it as your everyday tool in Mac and keep</p>
<p>it as your everyday tool in Mac and keep something crossplatform around for when you&#x27;re not on Mac. You get the best of both worlds and it costs you nothing you&#x27;re using Mac. The GitHub link and the brew command are both in the description below. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
