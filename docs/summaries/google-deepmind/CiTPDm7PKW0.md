---
title: "Multi-robot collaboration with Gemini Robotics 2"
channel: "Google DeepMind"
video_id: CiTPDm7PKW0
url: https://www.youtube.com/watch?v=CiTPDm7PKW0
published: 2026-07-30T14:58:03+00:00
generated: 2026-07-30T17:49:34+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/CiTPDm7PKW0/hqdefault.jpg
---
# Multi-robot collaboration with Gemini Robotics 2

[![Multi-robot collaboration with Gemini Robotics 2](https://i.ytimg.com/vi/CiTPDm7PKW0/hqdefault.jpg)](https://www.youtube.com/watch?v=CiTPDm7PKW0)

[Watch on YouTube](https://www.youtube.com/watch?v=CiTPDm7PKW0) · **Google DeepMind** · 2026-07-30

## TL;DR
Google DeepMind demonstrates multi-robot collaboration in Gemini Robotics 2, where an Apollo humanoid robot and a Duo bi-arm robot work together to tidy a garage. Each robot runs its own neural network and coordinates through natural language reasoning, enabling them to divide tasks, communicate, and assist each other to complete complex real-world chores.

## Key Takeaways
- Gemini Robotics 2 introduces a multi-robot collaboration feature allowing different robots to work simultaneously on the same task.
- An Apollo humanoid robot and a Duo bi-arm robot demonstrate the system by tidying a garage and organizing tools into kits.
- A high-level reasoning model breaks down tasks, determines what to do, where to go, and identifies when a task is complete.
- Apollo handles broad-stroke actions and delegates precise work to Duo, handing over control mid-task.
- Each robot runs its own independent copy of the same neural network stack rather than sharing a single controller.
- The robots communicate with each other and with humans through natural language to coordinate assistance.
- Precision matters significantly for tasks like kitting—putting tools into bins and closing kits—where the "last centimeter" is critical.
- The system maintains fine motor precision even across a high-degree-of-freedom humanoid platform.
- Multi-robot communication and collaboration greatly expands the range of tasks robots can accomplish.
- The ultimate goal is deploying robots into the real world to assist people in their daily lives.

## Detailed Breakdown

### Introduction to Multi-Robot Collaboration [00:01](https://www.youtube.com/watch?v=CiTPDm7PKW0&t=1s)
The video opens by noting that many real-world tasks are difficult for a single person—or a single robot—to accomplish alone. Gemini Robotics 2 addresses this by adding a feature that enables multiple robots to collaborate on the same task simultaneously. The demonstration scenario involves a user asking an Apollo humanoid robot to help tidy a garage and organize tools back into their kit.

### Task Breakdown and Robot Handover [00:32](https://www.youtube.com/watch?v=CiTPDm7PKW0&t=32s)
The high-level reasoning model decomposes the task into steps, determining what to do and where to go. A key capability is identifying not just the next action but also when a task is complete. Apollo begins by moving objects—specifically a scrubbing mitt and a white transparent spray bottle—to a transparent bin on the top shelf. Apollo then hands over control to Duo, asking it to handle the final, more precise portion of the task: kitting all tools in the bin, closing the kit, and placing it back.

### Precision and Fine Motor Control [01:03](https://www.youtube.com/watch?v=CiTPDm7PKW0&t=63s)
The narrator emphasizes that while the last centimeter of motion may not matter for simple bin-placement tasks, it is critical here. The demonstration showcases that the system can control broad, high-degree-of-freedom humanoid movements while still maintaining precision on tasks involving grippers and bi-arm robots. Duo performs the delicate kitting and organization work.

### Independent Neural Networks Coordinating Through Reasoning [01:35](https://www.youtube.com/watch?v=CiTPDm7PKW0&t=95s)
Each robot runs its own copy of the same software stack. Rather than a single neural network controlling both robots, each robot performs its own individual thinking and orchestrates collaboration through reasoning. The robots talk to each other and to the human, deciding when it is the right moment to help. After all tasks are complete, Apollo acknowledges the work and credits Duo for the precise kitting.

### Vision for the Future [02:05](https://www.youtube.com/watch?v=CiTPDm7PKW0&t=125s)
The narrator explains that enabling robots to communicate and collaborate with other robots will greatly expand the number of tasks they can perform. The hope is that these robots can eventually enter the real world and help people in their daily lives.

## Notable Quotes
- "In the real world, there's a lot of tasks that's very hard for one person to do. It's similar in the robot world."
- "Something that's important in this task is actually identifying not just what to do next, but also when you're done."
- "Each of these two robots is running that same stack, and so rather than having one neural network that controls both robots, each have their own copy, and they're each doing their own individual thinking, and they're actually orchestrating through reasoning."
- "If they can communicate with other robots and collaborate with other robots, that is going to greatly expand the amount of tasks it can do."

## People, Tools & References Mentioned
- **Gemini Robotics 2** — Google DeepMind's robotics platform featuring multi-robot collaboration
- **Apollo** — A humanoid robot that handles high-level reasoning and broad-stroke actions
- **Duo** — A bi-arm robot that performs precise manipulation tasks such as kitting and organization
- **Google DeepMind** — The research organization behind the demonstration

## Who Should Watch
Robotics researchers, AI engineers, and enthusiasts interested in multi-agent collaboration, embodied AI, and natural-language-driven robot control will find this a concise and compelling demonstration of how independent robot agents can coordinate through reasoning to complete real-world tasks.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=CiTPDm7PKW0&amp;t=1s">00:01</a></span> In real world, there&#x27;s a lot of tasks that&#x27;s very hard for one person to do. It&#x27;s similar in the robot world. Spectacular work duo, you&#x27;re a machine. In Gemini Robotics 2, we add a feature that enables multiple robots to collaborate to accomplish the same task simultaneously. Hey Apollo, can you help me tidy up my garage? And when you&#x27;re done, I want to put all the tools back in their kit. Let&#x27;s grab the scrubbing mitt and the white transparent spray bottle</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=CiTPDm7PKW0&amp;t=32s">00:32</a></span> the white transparent spray bottle together and take them to the rightmost transparent bin on the top shelf. The high-level reasoning model is breaking down what to do, where to go. And so, something that&#x27;s important in this task is actually identifying not just what to do next, but also when you&#x27;re done. Our Apollo humanoid will actually hand over control to the duo and say, &quot;Hey, can you help with the last part of this task?&quot; And so, we can see it actually pulling duo in uh for assistance right there. Hey duo, kit all tools in the bin, close the kit, and put the kit back into the bin.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=CiTPDm7PKW0&amp;t=63s">01:03</a></span> into the bin. On it. For tasks like putting objects in bins, that last centimeter matters a little bit less, but here it&#x27;s actually relatively important to completion of the task. It&#x27;s one of the things that we tried to demonstrate in this release is that not only can we control kind of broad strokes actions across a very high degree of freedom humanoid, we can still maintain that precision of motion on tasks that involve grippers and bi-arm robots. Awesome precision duo, keep going.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=CiTPDm7PKW0&amp;t=95s">01:35</a></span> Awesome precision duo, keep going. Each of these two robots is running that same stack, and so rather than having one neural network that controls both robots, each have their own copy, and they&#x27;re each doing their own individual thinking, and they&#x27;re actually orchestrating through reasoning. All tasks are fully complete. Mission accomplished. That was a fantastic job, Apollo. You should be really proud. You&#x27;re very welcome, but please don&#x27;t forget duo. Duo did a fantastic job with all the precise kitting and organization. Each robot is actually talking to us, talking to each other, and kind of deciding when it&#x27;s the right moment for them to help.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=CiTPDm7PKW0&amp;t=125s">02:05</a></span> for them to help. If they can communicate with other robots and collaborate with other robots, so that is going to greatly expand the amount of tasks it can do. We hope that the robot can enter the real world and help all of us in our daily lives.</p>

</details>
