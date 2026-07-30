---
title: "Gemini Robotics 2 brings whole body intelligence to robots"
channel: "Google DeepMind"
video_id: 4lSQnrMC6nY
url: https://www.youtube.com/watch?v=4lSQnrMC6nY
published: 2026-07-30T14:57:57+00:00
generated: 2026-07-30T19:53:53+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/4lSQnrMC6nY/hqdefault.jpg
---
# Gemini Robotics 2 brings whole body intelligence to robots

[![Gemini Robotics 2 brings whole body intelligence to robots](https://i.ytimg.com/vi/4lSQnrMC6nY/hqdefault.jpg)](https://www.youtube.com/watch?v=4lSQnrMC6nY)

[Watch on YouTube](https://www.youtube.com/watch?v=4lSQnrMC6nY) · **Google DeepMind** · 2026-07-30

## TL;DR
Google DeepMind introduces Gemini Robotics 2, a generalist AI model designed to give humanoid robots "whole body intelligence" for navigating the physical world. Unlike specialized robots that perform single impressive feats, this model enables coordinated whole-body control, dexterous hand manipulation of complex objects, and even multi-robot collaboration through shared reasoning.

## Key Takeaways
- Gemini Robotics 2 is a **generalist robotics model** — one AI controlling one robot that can perform many different tasks, rather than a specialized robot built for a single purpose.
- The model acts as the "brain" controlling the **entire body** of humanoid robots, including delicate hand movements and gripper operations.
- The release focuses on **three main capabilities**: whole body control, dexterous manipulation, and multi-robot collaboration.
- Whole body control requires the AI to make many coordinated decisions across the entire robot body — something humans do intuitively but is extremely difficult for robots.
- Dexterous manipulation goes well beyond simple "pick and place," tackling hard problems like screwing in a light bulb or handling a trash bag.
- The trash bag task was initially considered impossible by some team members, highlighting the ambition of the project.
- Multi-robot collaboration is enabled by giving each robot its own copy of the same AI stack; they coordinate through reasoning rather than being controlled by a single central network.
- Reactivity and adaptability to changing scenes is a core measure of the intelligence the team is pursuing.
- AI is described as "the missing piece of the entire robotics puzzle."

## Detailed Breakdown

### The Challenge of Physical-World Intelligence [00:00](https://www.youtube.com/watch?v=4lSQnrMC6nY&t=0s)
The video opens with a humanoid robot named Apollo expressing nervousness about being recorded. A DeepMind researcher frames the core problem: navigating the physical world is "borderline impossible" for robots, yet humans do it so naturally and intuitively that they barely consider it a form of intelligence. This contrast sets up the motivation for the work.

### Generalist vs. Specialized Robots [00:33](https://www.youtube.com/watch?v=4lSQnrMC6nY&t=33s)
The team distinguishes Gemini Robotics 2 from specialized humanoid robots that perform impressive single tasks like running, jumping, or backflipping. Instead, the goal is a **generalist robotics model** — one robot capable of handling many different tasks, which the team believes adds far more value. AI models are presented as the key to navigating the "messy complexity" of human environments. Gemini Robotics is described as the "brain" that controls the whole body of the humanoid, including delicate hand movements and the grippers of a robot called Duo.

### Three Focus Areas: Whole Body Control and Dexterity [01:03](https://www.youtube.com/watch?v=4lSQnrMC6nY&t=63s)
The release centers on three main pillars. The first is **whole body control**: humans move in a coordinated manner effortlessly, but robots must make many decisions across the entire body to achieve even simple tasks. The second is **dexterous hands and manipulation** that goes beyond basic pick-and-place operations. A researcher notes the field is "humbled" by tasks like screwing in a light bulb, which involve interacting with smaller objects — genuinely hard problems the team is tackling. The trash bag task is highlighted as one that several people initially thought was impossible. The key insight is that humans don't think about driving individual finger joints, but that is exactly what the AI models must learn to do.

### Multi-Robot Collaboration [02:04](https://www.youtube.com/watch?v=4lSQnrMC6nY&t=124s)
The third focus area is **multi-robot collaboration**. A voice command is given to Duo — a dual-armed robot — to gather tools into a bin, close a kit, and place the kit back. Duo responds, "On it." Critically, each robot runs its own copy of the same AI stack; there is no single central network controlling both. Each robot performs its own individual thinking and orchestrates cooperation through reasoning. After the task, Duo receives verbal praise: "Awesome precision, duo."

### Intelligence, Generality, and the Future [02:35](https://www.youtube.com/watch?v=4lSQnrMC6nY&t=155s)
The team emphasizes that the real goal is **intelligence and generality** — the ability to react when the scene changes, which is where true intelligence manifests. A researcher expresses excitement about how fast robotics is moving and calls AI "the missing piece of the entire robotics puzzle." The video closes with a researcher reflecting that it is exciting to be in the spotlight at this moment in the field.

## Notable Quotes
- "For the robot, dealing with challenges of the actual physical world is borderline impossible. But for us humans, it comes so naturally and so intuitively that we almost don't even think of it as intelligence."
- "We aim to build a generalist robotics model that's going to add a lot more value if one robot can do a lot of different tasks."
- "As a field, we're humbled by things like screwing a light bulb where you're interacting with smaller objects, and those are really hard problems that we are trying to solve."
- "When we first came up with the trash bag task in particular, several people did think it was impossible."
- "Each of these two robots is running that same stack, and so rather than having one robot network that controls both robots, they have their own copy, and they're each doing their own individual thinking, and they're actually orchestrating through reasoning."
- "Being able to react to the scene changing — that is where the intelligence comes in."
- "AI is really the missing piece of the entire robotics puzzle."

## People, Tools & References Mentioned
- **Apollo** — a humanoid robot featured at the start of the video
- **Duo** — a dual-armed robot that demonstrates multi-robot collaboration and responds to voice commands
- **Gemini Robotics 2** — the generalist robotics AI model released by Google DeepMind
- **Google DeepMind** — the organization behind the research

## Who Should Watch
Robotics engineers, AI researchers, and technology enthusiasts who want to understand how generalist foundation models are being applied to physical-world robotics — especially whole-body control, dexterous manipulation, and multi-robot collaboration — will find this a concise and inspiring overview of the state of the art.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=4lSQnrMC6nY&amp;t=0s">00:00</a></span> How are you today, Apollo? I&#x27;m a little nervous. Is that a microphone? For the robot, dealing with challenges of the actual physical world is borderline impossible. But for us humans, it comes so naturally and so intuitively that we almost don&#x27;t even think of it as intelligence.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=4lSQnrMC6nY&amp;t=33s">00:33</a></span> You probably have seen all these amazing videos of specialized humanoid robots running, jumping, backflipping. The key difference in Gemini Robotics 2 is we aim to build a generalist robotics model that&#x27;s going to add a lot more value if one robot can do a lot of different tasks. AI models offer a way to navigate the messy complexity of our human environment. The way to think about it is the brain Gemini Robotics is what controls the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=4lSQnrMC6nY&amp;t=63s">01:03</a></span> Gemini Robotics is what controls the whole body of the humanoid, the delicate movements of the sharp hand and the grippers of the dual. We focus on three main things for this release. The first one is whole body control. We are very used to move our body in a very coordinated manner, but it&#x27;s not true for robots. Even though this feels a very simple task for us, but for robots, I need to make a many, many decisions across the entire body to achieve this. The second thing is about dexterous hands and particular manipulations of objects way beyond just</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=4lSQnrMC6nY&amp;t=94s">01:34</a></span> manipulations of objects way beyond just pick and place. As a field, we&#x27;re humbled by things like screwing a light bulb where you&#x27;re interacting with smaller objects, and those are really hard problems that we are trying to solve. When we first came up with the trash bag task in particular, several people did think it was impossible. You don&#x27;t think about how to drive separate joints when you operate your hand, but that&#x27;s what we&#x27;re asking these AI models to do. And for a thing is being Gemini</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=4lSQnrMC6nY&amp;t=124s">02:04</a></span> And for a thing is being Gemini Robotics too, we add a feature that enables multiple robots to collaborate to accomplish the same task simultaneously. Hey duo, get all tools in the bin, close the kit, and put the kit back into the bin. On it. Each of these two robots is running that same stack, and so rather than having one robot network that controls both robots, they have their own copy, and they&#x27;re each doing their own individual thinking, and they&#x27;re actually orchestrating through reasoning. Awesome precision, duo. Keep going. We&#x27;re really after intelligence and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=4lSQnrMC6nY&amp;t=155s">02:35</a></span> We&#x27;re really after intelligence and generality. Being able to react to the scene changing, that is where the intelligence comes in. I&#x27;m super excited about robotics. I think uh it&#x27;s moving really fast, and AI is really the missing piece of the entire robotics puzzle. It is quite exciting to be in the spotlight.</p>

</details>
