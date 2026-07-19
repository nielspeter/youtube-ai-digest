---
title: "An initiative to secure the world's software | Project Glasswing"
channel: "Anthropic"
video_id: INGOC6-LLv0
url: https://www.youtube.com/watch?v=INGOC6-LLv0
published: 2026-04-07T18:03:51+00:00
generated: 2026-07-13T15:15:12+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/INGOC6-LLv0/hqdefault.jpg
---
# An initiative to secure the world's software | Project Glasswing

[![An initiative to secure the world's software | Project Glasswing](https://i.ytimg.com/vi/INGOC6-LLv0/hqdefault.jpg)](https://www.youtube.com/watch?v=INGOC6-LLv0)

[Watch on YouTube](https://www.youtube.com/watch?v=INGOC6-LLv0) · **Anthropic** · 2026-04-07

## TL;DR
Anthropic has developed a new, highly capable code-and-cybersecurity model, Claude Mythos Preview, which can autonomously find and chain together complex software vulnerabilities. Because these capabilities could be dangerous if released publicly, Anthropic is launching Project Glasswing, a private partnership giving critical open-source maintainers and government collaborators early access to the model to find and patch bugs before adversaries can exploit them.

## Key Takeaways
- Most software bugs go unnoticed by everyday users, but single vulnerabilities in widely shared code can have massive, global consequences.
- Historically, finding and patching vulnerabilities has been slow, expensive, and time-consuming.
- Claude Mythos Preview represents a significant jump in cybersecurity capability, emerging as a side effect of being trained to be good at code.
- The model performs at roughly the level of a professional human security researcher in identifying bugs.
- It can autonomously chain together multiple minor vulnerabilities—sometimes three to five—to create sophisticated exploits.
- Due to dual-use risks, Anthropic will not release this model widely.
- Project Glasswing partners Anthropic with organizations powering the world's most critical code, giving defenders a head start.
- The model has already found long-standing bugs in major operating systems, including a 27-year-old bug in OpenBSD and privilege escalation vulnerabilities in Linux.
- Anthropic is also engaging with U.S. government officials to assess and defend against the risks posed by such models.
- Securing the world's software is a long-term, cross-industry effort essential to the security of modern society.

## Detailed Breakdown

### The hidden reality of software bugs [00:00](https://www.youtube.com/watch?v=INGOC6-LLv0&t=0s)
The video opens by contrasting the average person's experience of software—largely oblivious to bugs—with the daily reality of developers who must constantly manage flaws and vulnerabilities. Most bugs are minor and quietly fixed, but occasionally a single vulnerability in widely shared software can magnify out and cause severe global impact.

### The historical cost of vulnerability discovery [00:30](https://www.youtube.com/watch?v=INGOC6-LLv0&t=30s)
Finding and patching vulnerabilities has traditionally been a slow, expensive, and labor-intensive process. The video then pivots to the transformative potential of large language models (LLMs): if they can write code at a world-class level, they can also find bugs and exploit software with comparable effectiveness, raising the bar for both defenders and adversaries.

### Introducing Claude Mythos Preview [01:02](https://www.youtube.com/watch?v=INGOC6-LLv0&t=62s)
Anthropic developed a new model, Claude Mythos Preview, which showed early on that it was meaningfully better at cybersecurity tasks. The model was not specifically trained for cyber work; rather, its cyber capabilities emerged as a side effect of being trained to be good at code. Anthropic describes this as a significant jump along an accelerating exponential curve of capability.

### Professional-level bug finding and vulnerability chaining [01:33](https://www.youtube.com/watch?v=INGOC6-LLv0&t=93s)
The model is described as being roughly as good as a professional human at identifying bugs. A standout capability is its ability to chain together multiple vulnerabilities—sometimes three to five—that individually do little, but in sequence produce sophisticated exploit outcomes. This is attributed to the model's autonomy and its ability to pursue long-range tasks similar to a human security researcher's daily workflow.

### Why the model won't be released widely [02:35](https://www.youtube.com/watch?v=INGOC6-LLv0&t=155s)
Because these capabilities could cause harm in the wrong hands, Anthropic has decided not to release the model publicly. Acknowledging that even more powerful models will come from Anthropic and others, the company argues that a proactive plan is needed to respond to the emerging cybersecurity landscape.

### Launch of Project Glasswing [03:07](https://www.youtube.com/watch?v=INGOC6-LLv0&t=187s)
To address the risks, Anthropic is launching Project Glasswing, partnering with organizations that maintain some of the world's most critical code. By giving these developers advanced tools before anyone else, Anthropic aims to provide a collective head start—finding and fixing vulnerabilities faster than would otherwise be possible.

### Early results: bugs across major platforms [03:39](https://www.youtube.com/watch?v=INGOC6-LLv0&t=219s)
Working with partners, the model has found vulnerabilities across essentially every major platform. One Anthropic researcher reports finding more bugs in a couple of weeks than in the rest of their life combined. The team first scanned open-source operating systems—the code underlying internet infrastructure—and found a 27-year-old bug in OpenBSD that could crash any server, plus privilege escalation vulnerabilities in Linux allowing a user with no permissions to become an administrator.

### Responsible disclosure and patching [04:13](https://www.youtube.com/watch?v=INGOC6-LLv0&t=253s)
For each bug found, Anthropic notified the maintainers, who fixed the issues and deployed patches so that users are no longer vulnerable. The video emphasizes how invaluable such a tool is for developers who tirelessly maintain software, allowing them to discover and fix vulnerabilities before exploitation.

### Government collaboration and societal stakes [04:47](https://www.youtube.com/watch?v=INGOC6-LLv0&t=287s)
Anthropic has spoken with officials across the U.S. government, offering to collaborate on assessing the risks of these models and defending against them. The video underscores that software now underpins nearly every aspect of daily life—"Software ate the world"—making cybersecurity essential to the security of society itself.

### A long-term, cross-industry effort [05:18](https://www.youtube.com/watch?v=INGOC6-LLv0&t=318s)
No single organization can see the whole picture or tackle the problem alone. The effort will span months or years, not weeks. Anthropic's hope is that, through collective action, the world's software, customer data, financial transactions, and critical infrastructure will ultimately be safer than before.

## Notable Quotes
- "If LLMs are now able to write code, at the level of some of the greatest software developers in the world, it can also be used to find bugs and exploit that software equally effectively."
- "We haven't trained it specifically to be good at cyber. We trained it to be good at code, but as a side effect of being good at code, it's also good at cyber."
- "I found more bugs in the last couple of weeks than I found in the rest of my life combined."
- "For OpenBSD, we found a bug that's been present for 27 years, where I can send a couple of pieces of data to any OpenBSD server and crash it."
- "Software ate the world. Every analog aspect of our life is somehow represented in the digital domain."

## People, Tools & References Mentioned
- **Claude Mythos Preview** — Anthropic's new experimental model with advanced code and cybersecurity capabilities.
- **Project Glasswing** — Anthropic's initiative to partner with critical-code organizations for early defensive use of the model.
- **OpenBSD** — Open-source operating system in which a 27-year-old crash-inducing bug was found.
- **Linux** — Open-source operating system in which privilege escalation vulnerabilities were discovered.
- **U.S. government officials** — Engaged by Anthropic for collaboration on risk assessment and defense.

## Who Should Watch
Software developers, security researchers, open-source maintainers, and policymakers interested in how frontier AI models are transforming cybersecurity—both the risks they pose and the defensive opportunities they create—will find this video essential viewing.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=0s">00:00</a></span> Most people who use software every day don&#x27;t think about bugs. They don&#x27;t think about what can happen if the software that they depend upon suddenly is less secure. That&#x27;s something that software developers have to deal with every single day. Software has always had flaws and vulnerabilities. That&#x27;s not new. For an average person, the bugs are, by and large, not something they notice on a daily basis, because if they do,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=30s">00:30</a></span> they get fixed. But then every so often, there are vulnerabilities that have real severe impacts. Like one single bug that works its way into shared software that many, many, many different products or websites use. One issue just gets magnified out around the world. Historically, finding and patching vulnerabilities has been a slow, time-consuming, and expensive process. If LLMs are now able to write code, at the level of some of the greatest</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=62s">01:02</a></span> software developers in the world, it can also be used to find bugs and exploit that software equally effectively. These models have capabilities which are raising the bar from a cybersecurity point of view with their ability to help defenders as well as potentially help adversaries. We recently developed a new model, Claude Mythos Preview. Early on, it was clear to us that this model was going to be meaningfully better at cybersecurity capabilities.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=93s">01:33</a></span> There&#x27;s a high accelerating exponential, but along that exponential, there are points of significance. Claude Mythos Preview is a particularly big jump along that point. We haven&#x27;t trained it specifically to be good at cyber. We trained it to be good at code, but as a side effect of being good at code, it&#x27;s also good at cyber. The model that we&#x27;re experimenting with is by and large as good as a professional human at identifying bugs. It&#x27;s good for us because we can find</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=124s">02:04</a></span> more vulnerabilities sooner and we can fix them. It has the ability to chain together vulnerabilities. What this means is you find two vulnerabilities, either of which doesn&#x27;t really get you very much independently, but this model is able to create exploits out of three, four, sometimes five vulnerabilities that in sequence give you some very sophisticated end outcome. And we think that this model can do this really well because we noticed that this model is very autonomous. It&#x27;s just generally better at pursuing really long-range tasks</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=155s">02:35</a></span> that are kind of like the tasks that a human security researcher would do throughout the course of an entire day. Obviously, capabilities in a model like this could do harm if in the wrong hands, and so we won&#x27;t be releasing this model widely. More powerful models are going to come from us and from others, and so we do need a plan to respond to this. That&#x27;s why we&#x27;re launching what we&#x27;re calling Project Glasswing, where we partner with a number of the organizations that power some of the world&#x27;s most critical code to put the model into their hands to allow them</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=187s">03:07</a></span> to look at how they can use models like this to bring down risk and protect everyone. And by giving these software developers advanced tools before anyone else, it gives all of us a collective headstart. It allows us to find things that we couldn&#x27;t find before, and it helps us fix these things much more quickly. Working with our partners, we&#x27;ve been finding vulnerabilities across essentially every major platform. I found more bugs in the last couple of weeks than I found</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=219s">03:39</a></span> in the rest of my life combined. We used the model to scan a bunch of open-source code and the thing that we went for first was operating systems because this is the code that underlies the entire internet infrastructure. For OpenBSD, we found a bug that&#x27;s been present for 27 years, where I can send a couple of pieces of data to any OpenBSD server and crash it. On Linux, we found a number of vulnerabilities where, as a user with no permissions, I can elevate myself to the administrator</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=253s">04:13</a></span> by just running some binary on my machine. For each of these bugs, we told the maintainers who actually run the software about them, and they went and fixed them and have deployed the patches so that anyone who runs this software is no longer vulnerable to these attacks. For a developer who tirelessly maintains software, a model that can help them discover vulnerabilities in their own code and fix them before they can be exploited, that is an invaluable tool. We&#x27;ve spoken to officials across the US government, and we&#x27;ve offered to work with them and collaborate to assess the risks</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=287s">04:47</a></span> of these models and to help defend against the risks of these models. Everything that we do in our lives now depends on software. Software ate the world. Every analog aspect of our life is somehow represented in the digital domain. And so all of our daily lives run on the idea that we can rely on the systems that power them. Cybersecurity is the security of our society. It is essential that we come together and work together across industry to help build better defensive capabilities.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=INGOC6-LLv0&amp;t=318s">05:18</a></span> No single organization sees the whole picture and can tackle this on their own. This is not going to be done as part of a few week program. This is going to be the work of certainly months, perhaps years. But what I do hope is at the end of this, we can be in a position where the world&#x27;s software, its customer data, its financial transactions, its critical infrastructure are safer than they were before.</p>

</details>
