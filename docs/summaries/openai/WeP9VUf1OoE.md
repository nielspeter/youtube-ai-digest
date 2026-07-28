---
title: "Introducing gpt-transcribe and gpt-live-transcribe"
channel: "OpenAI"
video_id: WeP9VUf1OoE
url: https://www.youtube.com/watch?v=WeP9VUf1OoE
published: 2026-07-28T21:49:18+00:00
generated: 2026-07-28T23:13:47+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/WeP9VUf1OoE/hqdefault.jpg
---
# Introducing gpt-transcribe and gpt-live-transcribe

[![Introducing gpt-transcribe and gpt-live-transcribe](https://i.ytimg.com/vi/WeP9VUf1OoE/hqdefault.jpg)](https://www.youtube.com/watch?v=WeP9VUf1OoE)

[Watch on YouTube](https://www.youtube.com/watch?v=WeP9VUf1OoE) · **OpenAI** · 2026-07-28

## TL;DR
OpenAI introduces two new transcription models: **gpt-transcribe** for processing complete audio files and **gpt-live-transcribe** for streaming audio in real time. Both support 57 languages, handle accents and background noise more robustly, and allow developers to supply custom vocabulary to improve accuracy on domain-specific terms.

## Key Takeaways
- **Two models for two workflows**: gpt-transcribe handles completed files and returns a full transcript; gpt-live-transcribe maintains an open connection and returns text as audio arrives.
- **57 languages supported**, with automatic multilingual switching within a single session.
- Improved accuracy on historically difficult elements: accents, multilingual speech, very short answers, names, and numbers.
- Developers can supply a custom vocabulary list (proper nouns, code terms, domain jargon) to ensure important words are transcribed correctly.
- Better background-noise handling reduces false transcription of side conversations or ambient music.
- gpt-transcribe is optimized for accuracy and throughput on larger files like call archives, podcasts, and batch jobs.
- gpt-live-transcribe is optimized for low-latency use cases such as captions, dictation, and voice interfaces.
- A half-hour meeting recording takes under a minute to process with gpt-transcribe.

## Detailed Breakdown

### Introducing the Two New Models [00:00](https://www.youtube.com/watch?v=WeP9VUf1OoE&t=0s)
OpenAI announces gpt-transcribe and gpt-live-transcribe, designed for two distinct transcription workflows. gpt-transcribe accepts a completed audio file and returns the entire transcript at once. gpt-live-transcribe keeps a live connection open and streams text as audio arrives. Both models support 57 languages and are specifically improved at elements that commonly break transcription systems: accents, multilingual speech, very short answers, names, and numbers.

### Custom Vocabulary and Background Noise Handling [00:30](https://www.youtube.com/watch?v=WeP9VUf1OoE&t=30s)
Developers can provide the model with a list of important words, proper nouns, or code terms to improve accuracy. The presenter demonstrates this with a vocabulary containing domain-specific terms—"phishing" (cybersecurity), "ARR" (sales), and "A1C" (healthcare)—that are easy for generic transcribers to miss. The models also handle background noise better, so side conversations or ambient music are less likely to be incorrectly transcribed as speech, whether recording in a loud café, a busy conference hall, or near a chatty coworker.

### Live Multilingual Demonstration [01:02](https://www.youtube.com/watch?v=WeP9VUf1OoE&t=62s)
The presenter highlights language hints developers can provide, but notes the model can follow multilingual speech automatically by default. He demonstrates by switching from English to Spanish mid-session—"Y también puedo cambiar al español en la misma sesión"—and then back to English. The live transcript follows the language switch in both directions within the same session.

### gpt-transcribe File Processing Demo [01:32](https://www.youtube.com/watch?v=WeP9VUf1OoE&t=92s)
The presenter uploads a roughly half-hour meeting recording to gpt-transcribe. The model processes it in under a minute, after which the full transcript is ready for downstream use. This model is positioned as ideal for call archives, podcasts, and larger batch jobs where waiting for a complete file is acceptable and accuracy and throughput are the priority.

### When to Use gpt-live-transcribe [02:03](https://www.youtube.com/watch?v=WeP9VUf1OoE&t=123s)
In contrast to the file-based model, gpt-live-transcribe is optimized for scenarios where latency meaningfully impacts the experience: captions, dictation, and voice interfaces. The video closes with a brief "Happy building" sign-off.

## Notable Quotes
- "gpt-transcribe takes a completed file and returns the full transcript. gpt-live-transcribe keeps a live open connection and returns text as the audio arrives."
- "Developers can also give the models a list of words, proper nouns, or code terms that are especially important to get right."
- "And because they're better at handling background noise, a side conversation or ambient music is less likely to show up as speech."
- "Y también puedo cambiar al español en la misma sesión… And now I'm back to English. Same session and the transcript followed the switch in both directions."

## People, Tools & References Mentioned
- **gpt-transcribe** — file-based transcription model
- **gpt-live-transcribe** — streaming transcription model
- **Custom vocabulary feature** — developer-supplied word lists for improved accuracy
- **Example vocabulary terms**: phishing (cybersecurity), ARR (sales), A1C (healthcare)

## Who Should Watch
Developers and product builders integrating speech-to-text into applications—especially those working with multilingual users, noisy environments, or domain-specific terminology—will find this a concise, practical overview of which model to choose and why.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=WeP9VUf1OoE&amp;t=0s">00:00</a></span> Today we&#x27;re introducing two new transcription models, gpt-transcribe and gpt-live-transcribe. These models give you two different ways to build with transcription. gpt-transcribe takes a completed file and returns the full transcript. gpt-live-transcribe keeps a live open connection and returns text as the audio arrives. Both models support 57 languages and they&#x27;re much better at the parts of transcription that tend to break accents, multilingual speech, very short answers, names, and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WeP9VUf1OoE&amp;t=30s">00:30</a></span> numbers. Developers can also give the models a list of words, proper nouns, or code terms that are especially important to get right. For this session, I provided a prompt mentioning transcription models plus a vocabulary with terms like phishing, ARR, and A1C from cybersecurity, sales, and healthcare domains that can be easy to miss. And because they&#x27;re better at handling background noise, a side conversation or ambient music is less likely to show up as speech. So whether you&#x27;re recording in a loud cafe,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WeP9VUf1OoE&amp;t=62s">01:02</a></span> a busy conference hall, or next to a very chatty coworker, the transcript can stay focused on what you&#x27;re actually saying. You can give the model language hints to improve accuracy, but by default it can follow multilingual speech automatically. So I can switch languages right here in the same session. Y también puedo cambiar al español en la misma sesión. El modelo sigue transcribiendo en tiempo real y ahora vuelvo al inglés. And now I&#x27;m back to English. Same session and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WeP9VUf1OoE&amp;t=92s">01:32</a></span> the transcript followed the switch in both directions. Now let&#x27;s take a look at gpt-transcribe. I&#x27;ve uploaded a meeting recording that&#x27;s about half an hour long. The model will take a little less than a minute to process it, and then the transcript is ready for whatever comes next. It&#x27;s great for call archives, podcasts, and larger batch jobs where you can wait for a complete file and optimize for accuracy and throughput. In contrast to the streaming model,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WeP9VUf1OoE&amp;t=123s">02:03</a></span> which excels at captions, dictation, and voice interfaces, where latency meaningfully impacts the experience. Happy building.</p>

</details>
