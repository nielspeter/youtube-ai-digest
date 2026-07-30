---
title: "Intelligent whole-body control with Gemini Robotics 2"
channel: "Google DeepMind"
video_id: 9MNLEAzA59o
url: https://www.youtube.com/watch?v=9MNLEAzA59o
published: 2026-07-30T14:58:07+00:00
generated: 2026-07-30T19:50:19+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/9MNLEAzA59o/hqdefault.jpg
---
# Intelligent whole-body control with Gemini Robotics 2

[![Intelligent whole-body control with Gemini Robotics 2](https://i.ytimg.com/vi/9MNLEAzA59o/hqdefault.jpg)](https://www.youtube.com/watch?v=9MNLEAzA59o)

[Watch on YouTube](https://www.youtube.com/watch?v=9MNLEAzA59o) · **Google DeepMind** · 2026-07-30

## TL;DR
Google DeepMind demonstrates Gemini Robotics 2, an embodied AI system enabling humanoid robots to perform whole-body coordinated tasks like packing sports bags. The system combines embodied reasoning with vision-language-action models to control joints from feet to fingertips in real time, maintaining balance while navigating cluttered environments.

## Key Takeaways
- The human world is designed for human bodies, making coordinated whole-body control essential for robots to be genuinely useful.
- Gemini Robotics uses an embodied reasoning model to understand natural language instructions and the visual world, then calls a Vision-Language-Action (VLA) model to generate robot actions.
- Whole-body control requires coordinating all joints and actuators from feet to fingertip while maintaining balance, with adjustments happening in fractions of a second.
- Tasks that feel simple to humans require robots to make many decisions across the entire body.
- The system is designed to generalize—navigating cluttered environments, selecting the right objects, and placing them correctly.
- The robot can recognize failures and retry tasks autonomously.
- Reactivity is stress-tested in real time, such as when a new object is unexpectedly placed on the floor for the robot to find and handle.
- The ultimate vision is a generalist robot capable of performing many useful real-world tasks.
- AI is described as the "missing piece" of the robotics puzzle.

## Detailed Breakdown

### The Human-Centric World and Robot Challenges [00:04](https://www.youtube.com/watch?v=9MNLEAzA59o&t=4s)
The video opens by highlighting that the human body has many muscles and joints, and the entire world is designed around human capabilities. Humans move in highly coordinated ways naturally, but this is not yet true for robots. The scene sets up a domestic scenario where a person asks a humanoid robot named Apollo to help pack sports equipment for two children—Jesse, who has a pickleball match at 2:00 p.m., and Jeremy, who has a baseball game at 4:00 p.m.

### How Gemini Robotics Works [00:35](https://www.youtube.com/watch?v=9MNLEAzA59o&t=35s)
A DeepMind researcher explains the architecture: the Gemini Robotics embodied reasoning model understands the world, processes visual input, and interprets natural language instructions. It then invokes a Vision-Language-Action (VLA) model to control the robot and generate the physical actions needed to accomplish complex tasks. This layered approach allows the robot to translate high-level requests into concrete motor commands.

### Whole-Body Coordination and Balance [01:06](https://www.youtube.com/watch?v=9MNLEAzA59o&t=66s)
The robot must coordinate all joints and actuators from its feet to its fingertips while maintaining balance. If the robot leans too far forward and is about to tip, it must push its legs backward to compensate. All of these adjustments need to happen in a fraction of a second. A researcher notes that even seemingly simple tasks require the robot to make many decisions across its entire body.

### Generalization, Clutter, and Failure Recovery [01:42](https://www.youtube.com/watch?v=9MNLEAzA59o&t=102s)
The team emphasizes demonstrating that the robot is general—able to navigate cluttered environments, identify the correct objects, and place them in the right locations. Crucially, the robot sometimes fails, but it can recognize its own failures and try again. In the demo, Apollo announces it will retrieve Jesse's pickleball paddle from the middle shelf and completes the packing task, then asks if further help is needed.

### Stress-Testing Reactivity [02:13](https://www.youtube.com/watch?v=9MNLEAzA59o&t=133s)
The human operator introduces an unplanned challenge: a tall bag is placed on the floor to the robot's left, and the robot is asked to search for it, pick it up, and place it on the table. This serves as a real-time stress test of the robot's reactivity and adaptability. Apollo responds enthusiastically, saying it is "absolutely ready" for the additional challenge.

### The Vision for Generalist Robots [02:35](https://www.youtube.com/watch?v=9MNLEAzA59o&t=155s)
A researcher articulates the broader vision: to develop a generalist robot capable of performing many more useful tasks in the real world. Whole-body control is described as a necessity for achieving that goal. The video closes with a researcher expressing excitement about how fast robotics is moving, calling AI "the missing piece of the entire robotics puzzle."

## Notable Quotes
- "The whole world is designed for humans. We are very used to actually move our body in a very coordinated manner, but it's not true for robots."
- "The robot need to coordinate all the joints and the actuators from feet to fingertip while maintaining balance. If it's leaning more forward and it's about to tip, then it need to push the legs backwards. And all these things need to happen in a fraction of the second."
- "Even though this feels a very simple task for us, for robots it need to make many many decisions across the entire body to achieve this."
- "Sometimes it fails and it recognizes failures and then try again."
- "The vision we have is to develop a generalist robot to do a lot more useful tasks in the real world. Whole body control is a necessity to achieve that goal."
- "AI is really the missing piece of the entire robotics puzzle."

## People, Tools & References Mentioned
- **Apollo** — the humanoid robot demonstrated in the video
- **Gemini Robotics** — DeepMind's embodied reasoning model
- **Vision-Language-Action (VLA) model** — the model called by Gemini Robotics to generate robot motor actions
- **Jesse and Jeremy** — children referenced in the demo scenario (pickleball and baseball players respectively)
- **Google DeepMind** — the research organization presenting the work

## Who Should Watch
Robotics enthusiasts, AI researchers, and engineers interested in embodied AI and whole-body control will find this video valuable for understanding how large-scale reasoning models are being integrated with physical robot control to achieve generalist, real-world task performance.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=9MNLEAzA59o&amp;t=4s">00:04</a></span> Human body has a lot of muscles and joints. The whole world is designed for humans. We are very used to actually move our body in a very coordinated manner, but it&#x27;s not true for robots. Hey Apollo, the kids are going to do some sports today. Could you help them to pack? I see on the calendar that Jesse has a pickleball match at 2:00 p.m.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=9MNLEAzA59o&amp;t=35s">00:35</a></span> pickleball match at 2:00 p.m. and Jeremy has a baseball game at 4:00 p.m. Let&#x27;s get started. The Gemini Robotics embodied reasoning model can understand the world, understand what it sees, understand the natural language instructions. Then it&#x27;s going to call the VOA vision language action model to control the robot to generate the actions in order to accomplish this more complex task. So the robot need to coordinate all the joints and the actuators from feet to fingertip while staying maintaining balance. If</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=9MNLEAzA59o&amp;t=66s">01:06</a></span> while staying maintaining balance. If it&#x27;s leaning more forward and it&#x27;s about to tip, then it need to push the legs backwards. And all these things need to happen in a fraction of the second. Even though this feels a very simple task for us, for robots it need to make a many many decisions across the entire body to achieve this. So we really want to demonstrate that robot is general and can sort of navigate on these cluttered environment and pick out the right object and put them into the right place. Sometimes it fails and it recognizes failures and then try again.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=9MNLEAzA59o&amp;t=102s">01:42</a></span> Now I will retrieve Jesse&#x27;s pickleball paddle from the middle shelf. I have finished packing. Is there anything else you need help with? Can&#x27;t throw you one more challenge. I am absolutely ready for you to throw me one more challenge. So, please let me know what it is. I just put a tall bag on the floor to your left. Can you search for it and pick it up and place it on the table? I&#x27;m going to stress test the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=9MNLEAzA59o&amp;t=133s">02:13</a></span> I&#x27;m going to stress test the reactivity of the robot. The vision we have is to develop a generalist robot to do a lot more useful tasks in the real world. Whole body control is a necessity to achieve that goal. I&#x27;m super excited about robotics. I think it&#x27;s moving really fast and AI is really the missing piece of the entire robotics puzzle.</p>

</details>
