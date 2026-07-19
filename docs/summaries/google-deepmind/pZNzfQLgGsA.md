---
title: "Reimagining the mouse pointer with AI"
channel: "Google DeepMind"
video_id: pZNzfQLgGsA
url: https://www.youtube.com/watch?v=pZNzfQLgGsA
published: 2026-05-13T09:07:06+00:00
generated: 2026-07-16T22:09:53+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/pZNzfQLgGsA/hqdefault.jpg
---
# Reimagining the mouse pointer with AI

[![Reimagining the mouse pointer with AI](https://i.ytimg.com/vi/pZNzfQLgGsA/hqdefault.jpg)](https://www.youtube.com/watch?v=pZNzfQLgGsA)

[Watch on YouTube](https://www.youtube.com/watch?v=pZNzfQLgGsA) · **Google DeepMind** · 2026-05-13

## TL;DR
Google DeepMind researcher Adrian presents an experimental AI-enabled mouse pointer powered by Gemini that understands what a user is pointing at, why it matters, and how to act on it. By combining pointing, voice, and on-screen visual understanding, the prototype creates a fluid, collaborative interaction model that feels less like operating a computer and more like working alongside another person.

## Key Takeaways
- The mouse pointer has been a constant in digital interfaces for over 50 years, making it a powerful anchor for reimagining human-computer interaction.
- The experimental system embeds an AI model (Gemini) "behind" the pointer, allowing it to listen, observe the screen, and interpret user intent.
- A core design goal is understanding *fluid* user intent — not just what is pointed at, but why it matters and what action is desired.
- Early prototypes used deictic keywords like "this," "that," "here," and "there" to connect speech to whatever the pointer hovered over.
- The pointer can access data layers behind UI elements (text, images, app content) and incorporate them into prompts on the fly.
- Gemini can generate code in response to user intent as the pointer moves across different apps and windows.
- The system supports multimodal input: voice, text, image understanding, and even head tracking.
- Demonstrated use cases include updating calendar drafts, generating directions between two pointed locations, and creating images by combining menu content with a reference image's style.
- The vision is a new kind of operating system where AI surfaces useful content, the user points back, and both share attention on a common canvas.
- The interaction model is likened to collaborating with another person rather than operating a machine.

## Detailed Breakdown

### Rethinking the pointer as a collaborative anchor [00:00](https://www.youtube.com/watch?v=pZNzfQLgGsA&t=0s)
The video opens by framing pointing as fundamental to human collaboration. The narrator notes that the mouse pointer has remained a constant across websites, documents, and workflows for more than half a century. The central question is posed: what if an AI model like Gemini sat behind the pointer, listening and interpreting user intent the way another person would?

### Meet the researcher and the project's goal [00:32](https://www.youtube.com/watch?v=pZNzfQLgGsA&t=32s)
Adrian, a researcher at Google DeepMind, introduces himself and his work, which involves prototyping and user experimentation to build systems that satisfy real human needs. He explains that the research project centers on an experimental AI-enabled pointer capable of understanding not only what the user points at, but also why it matters and how to act on it. The first focus was building a system that can grasp fluid user intent.

### The keyword-based prototype and "this/that" pointing [01:02](https://www.youtube.com/watch?v=pZNzfQLgGsA&t=62s)
The initial prototype worked by letting users say keywords like "this," "that," "here," or "there" while hovering over an element. For example, saying "Could you get these two ingredients and also this one and add them to my shopping list here?" triggers the pointer to resolve each reference. Typing or saying "this" while hovering on a note inserts that note's actual text into the AI prompt, grounding the instruction in the pointed-at data.

### Digging through data layers and cross-app actions [01:33](https://www.youtube.com/watch?v=pZNzfQLgGsA&t=93s)
Adrian explains that the pointer can dig through all layers of data behind the interface — voice, text, and image understanding all come into play. He demonstrates by asking to change a draft time to 8:00 p.m., and the system updates it. Another example involves asking for directions from "this place to that place," and Gemini generates directions between the two hovered locations. The pointer effectively communicates with multiple windows, assembling the prompt on the fly, and Gemini writes code to satisfy the intent as the pointer moves across apps.

### Head tracking, image generation, and multimodal magic [02:03](https://www.youtube.com/watch?v=pZNzfQLgGsA&t=123s)
Adrian shows a head-tracking interaction and asks Gemini to generate an image based on a hovered menu while using the style from a separate reference image. Gemini combines the menu's content and the bird image's style into a newly generated image. Adrian highlights how mixing voice, pointing, and visual understanding simultaneously feels magical.

### Vision for a new AI-native operating system [02:33](https://www.youtube.com/watch?v=pZNzfQLgGsA&t=153s)
The video closes with Adrian imagining a new type of operating system: the AI surfaces content the user might find useful, the user points back at it, and both share attention and a canvas — as if working with another person. This collaborative, shared-attention model is positioned as the future paradigm for human-computer interaction.

## Notable Quotes
- "What if behind the pointer there was an AI model like Gemini actually listening to us, paying attention to the screen, and trying to interpret whatever we're saying like another person would?"
- "The focus of this research project is an experimental AI-enabled pointer with the ability to understand not only what you're pointing at, but also why it matters to you and how to act upon it."
- "We can really have the pointer dig through all of the layers of data. We can have voice, we can have text, we can have image understanding."
- "It's really magical what you can do when we mix voice and pointing and visual understanding at the same time."
- "I imagine a new type of operating system, AI showing me content I might find useful, me pointing back at the content, sharing attention, and sharing the canvas like if I was working with another person."

## People, Tools & References Mentioned
- **Adrian** — Researcher at Google DeepMind leading the AI-enabled pointer project
- **Gemini** — Google's AI model used to interpret intent and generate responses/code
- **Mouse pointer** — The 50+ year-old interaction paradigm being reimagined
- **Head tracking** — Demonstrated as an input modality within the prototype

## Who Should Watch
Designers, HCI researchers, and AI product builders interested in multimodal, intent-driven interfaces will find this a compelling glimpse at how pointing, voice, and visual understanding could converge into a more collaborative operating system paradigm.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=pZNzfQLgGsA&amp;t=0s">00:00</a></span> Pointing is really at the core of a lot of the interactions we have when we collaborate with other people. For more than half a century, the mouse pointer has been the one constant across every website, digital documents, and workflow we use. What if behind the pointer there was an AI model like Gemini actually listening to us, paying attention to the screen, and trying to interpret whatever we&#x27;re saying like another person would? I&#x27;m Adrian. I am a researcher at Google</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=pZNzfQLgGsA&amp;t=32s">00:32</a></span> I&#x27;m Adrian. I am a researcher at Google DeepMind. My job involves doing a lot of prototyping, a lot of experiment with users, and really trying to understand people and how to create systems that actually satisfy their needs. The focus of this research project is an experimental AI-enabled pointer with the ability to understand not only what you&#x27;re pointing at, but also why it matters to you and how to act upon it. Our first focus was really how can we build a system that can really understand fluid user intent?</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=pZNzfQLgGsA&amp;t=62s">01:02</a></span> really understand fluid user intent? Could you get these two ingredients and also this one and add them to my shopping list here? Done. The way we actually made this work in our initial prototype was by saying keywords like this, that, here, or there. If I hover on the note the AI-enabled pointer knows the data that&#x27;s behind the scene. Make this orange. By typing the word this it added this actual text note to the prompt.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=pZNzfQLgGsA&amp;t=93s">01:33</a></span> actual text note to the prompt. We can really have the pointer dig through all of the layers of data. We can have voice, we can have text, we can have image understanding. Can you make this 8:00 p.m.? I&#x27;ve updated the draft to start at 8:00 p.m. And then have Gemini write code to satisfy the user intent whenever they&#x27;re moving the pointer across different apps. Can you show me how to go from this place to that place? Here are the directions between the two locations. All of those windows are going to be communicating with the pointer, creating</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=pZNzfQLgGsA&amp;t=123s">02:03</a></span> communicating with the pointer, creating the prompt on the fly. I am using head tracking here. Hey Gemini. So, can you generate an image based on this whole menu here? I would like you to use the style in this image. Okay, I&#x27;m generating the image now. Beautiful. Gemini transferred the content of the menu here, as well as the style from the bird, into the new image. It&#x27;s really magical what you can do when we mix voice and pointing and visual understanding at the same time. I imagine a new type of operating</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=pZNzfQLgGsA&amp;t=153s">02:33</a></span> I imagine a new type of operating system, AI showing me content I might find useful, me pointing back at the content, sharing attention, and sharing the canvas like if I was working with another person.</p>

</details>
