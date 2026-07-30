---
title: "This is basically an X-ray for your codebase..."
channel: "Better Stack"
video_id: Y_7_rbtQXcs
url: https://www.youtube.com/watch?v=Y_7_rbtQXcs
published: 2026-07-30T12:00:11+00:00
generated: 2026-07-30T14:35:02+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/Y_7_rbtQXcs/hqdefault.jpg
---
# This is basically an X-ray for your codebase...

[![This is basically an X-ray for your codebase...](https://i.ytimg.com/vi/Y_7_rbtQXcs/hqdefault.jpg)](https://www.youtube.com/watch?v=Y_7_rbtQXcs)

[Watch on YouTube](https://www.youtube.com/watch?v=Y_7_rbtQXcs) · **Better Stack** · 2026-07-30

## TL;DR
Mindwalk is an early-stage tool that renders your codebase as a 3D city and replays AI coding-agent sessions over it, showing which files the agent looked at, read, and edited. It adds an AI "judge" that grades the agent's exploration and discipline, offering a new lens for understanding how agents reason across a repo—though for small changes, a plain git diff is still faster.

## Key Takeaways
- Mindwalk visualizes a codebase as a 3D "city" where every file is a building, with height representing code volume.
- It replays AI agent sessions (from Claude Code and Codeex logs) over the 3D scene, lighting files by interaction type: green for a glance, blue for a read, amber for an edit.
- The timeline is annotated with symbols for sub-agent spin-ups, context-window compactions, and user-injected instructions.
- An `analyze` command runs a local "judge" model over the session, grading whether the agent explored enough, stayed in scope, wandered, or verified its work; each finding links to the exact timeline moment.
- A separate `map` command can render any repo as a 3D city without needing a session replay.
- It's a single Go binary that reads session logs already written to disk, plus a three.js scene in the browser.
- At launch on Hacker News, the top reaction was "cool, but would I actually use this?"—some called it purposeless fun; others noted git diff is faster for small changes.
- It's version 0.3, rough and early, and currently only supports Claude Code and Codeex logs—not Cursor.
- Best use cases: comparing how different models explore the same task, or reviewing large, sprawling agent changes where a flat diff lacks "shape."
- It's not meant to replace review tools, but to reveal the agent's reasoning path that existing tools were never built to show.

## Detailed Breakdown

### The Problem with Agent Transparency [00:00](https://www.youtube.com/watch?v=Y_7_rbtQXcs&t=0s)
The video opens by framing a modern pain point: for two years, developers have handed codebases to AI agents that rewrite freely, with review limited to scrolling walls of code. Agent logs say *what* was done—ran a command, edited a file—but never *how* the agent understood the job: which files it considered relevant, where it looked before editing, whether it stayed in scope or wandered through half the repo. That thinking is invisible in a transcript.

### Installing and Launching Mindwalk [01:03](https://www.youtube.com/watch?v=Y_7_rbtQXcs&t=63s)
The presenter demonstrates installing Mindwalk inside a Claude Code session. Running a command fires up the tool, rendering the entire codebase as a dark 3D city where each file is a building and taller buildings mean more code. Pressing play on a recorded session begins the replay.

### The Color Language and Timeline [01:35](https://www.youtube.com/watch?v=Y_7_rbtQXcs&t=95s)
Mindwalk's core visual trick is its color coding: mossy green when the agent merely glances at a file, blue when it reads the file, and amber when it edits it—cool colors mean looking, warm colors mean changing. The timeline is marked with symbols indicating where sub-agents spun up, where the context window was compacted, and where the user injected a new instruction, letting you trace the agent's path precisely.

### The Analyze Command and Judge Report [02:08](https://www.youtube.com/watch?v=Y_7_rbtQXcs&t=128s)
Beyond the visual replay, an `analyze` command runs a judge over the whole session using your own local Claude or Codeex model. It grades the run: did the agent explore enough before editing, stay in scope, wander, or verify its work? Each finding is a clickable link to the exact moment on the timeline—effectively a code review of the agent's behavior. A `map` command can also render any repo as a 3D city standalone, no session needed.

### Hacker News Reception and Honest Skepticism [03:10](https://www.youtube.com/watch?v=Y_7_rbtQXcs&t=190s)
When Mindwalk launched on Hacker News, the top comment was blunt: "This is very cool, but would I actually use this?" Some users admitted it serves no real purpose and is just fun. A fair jab noted that for a small change, a plain git diff is faster than watching a 3D tour. The presenter acknowledges the tool is version 0.3, only reads Claude Code and Codeex logs, and doesn't yet support Cursor.

### Who It's Genuinely For [03:41](https://www.youtube.com/watch?v=Y_7_rbtQXcs&t=221s)
Mindwalk is useful if you're comparing models—seeing how Claude explores a task versus Codeex—offering a lens unavailable elsewhere. It's also valuable for large, sprawling agent changes where a flat diff doesn't convey the "shape" of what happened; the 3D flythrough plus judge report breaks that down. But for a two-line fix, the presenter concedes: just read a diff. Mindwalk won't replace review tools but aims to reveal the feel of a run that existing tools were never built to show.

## Notable Quotes
- "We taught our machines to write our code way faster than we ever built a way to understand what they wrote."
- "The agent's actual thinking is kind of invisible in a transcript. It's just gone."
- "Cool colors mean the agent was looking. Warm colors mean the agent was changing."
- "This is very cool, but would I actually use this? What would I actually use this for?"
- "It's rough, it's early, and it's aimed at the exact right problem."

## People, Tools & References Mentioned
- **Mindwalk** — the featured 3D agent-session visualization tool (version 0.3)
- **Graphify / Graphy** — another codebase visualization tool mentioned for comparison
- **Claude Code** — AI coding agent whose logs Mindwalk can read
- **Codeex** — another AI coding agent whose logs Mindwalk can read
- **Cursor** — AI coding IDE noted as not yet supported by Mindwalk
- **Hacker News** — where Mindwalk launched and received candid feedback
- **three.js** — browser 3D library used for Mindwalk's scene rendering
- **Go** — language the Mindwalk binary is written in
- **git diff** — cited as the faster alternative for reviewing small changes

## Who Should Watch
Developers and engineering leads who regularly use AI coding agents (especially Claude Code or Codeex) and want deeper insight into how those agents explore and modify a codebase. It's also relevant for anyone comparing model behavior or reviewing large, sprawling agent-generated changes where a standard diff feels insufficient.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=0s">00:00</a></span> For two years, we&#x27;ve been handing our code bases to AI agents and letting them rewrite whatever they please and then reviewing that by just scrolling a wall of code. Somebody finally got fed up with that and built the opposite. A way to actually watch an agent move through your code in 3D. It&#x27;s called Mindwalk. Now, this might even be a better way to visualize our code and bring it to life. We have tools like Graphify. So, how does this even compare?</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=32s">00:32</a></span> Now, here&#x27;s the real problem. Mindwalk is aimed at our agents log tells us what it did, ran this, edited that. What it never tells us is how it understood the job. Which files did it decide were relevant. Where did it go looking around before it changed a single line? Did it stay in its lane or quietly just go through half the repo? All of that. The agent&#x27;s actual thinking is kind of invisible in a transcript. It&#x27;s just gone. If you enjoy coding tools to speed up your workflow, be sure to subscribe. We have videos coming out all the time. So, let me show you what it looks like</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=63s">01:03</a></span> So, let me show you what it looks like when it&#x27;s not gone. I&#x27;ve got a project here in a Cloud Code session I ran earlier. I can go install this go, no pun intended, and then build it out. Now, I can fire up Mindwalk with this command here, and my whole codebase renders as this dark 3D city. Every file is a building and the more code it has, the taller it stands. Then I press play on the session. Watch the lights here. A file glows green, mossish green when the agent just</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=95s">01:35</a></span> green, mossish green when the agent just glances at it. Blue when it actually sits down and reads it, and amber when it makes an edit. And I can drag the timeline back and forth and literally trace the path the agent walked through this code. It&#x27;s one go binary that just reads the session logs cla code and codecs are already writing to your disk plus a 3JS scene in your browser for the 3D. That color language is the real trick here. Cool colors mean the agent was looking. Warm colors mean it was changing. The timelines marked up, too.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=128s">02:08</a></span> changing. The timelines marked up, too. Little symbols show you exactly where a sub agent spun up, where the context window got compacted, and where you barged in with a new instruction. So now you always know where you are going. But here&#x27;s the piece I actually think matters. Once you&#x27;re past this looks cool, right? There is an analyze command that runs a judge over the whole session using your own local cloud or codeex and it grades the run it just went through. Did the agent explore enough before it started editing? Okay. Did it stay in</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=158s">02:38</a></span> started editing? Okay. Did it stay in scope? Did it wander? Did it bother to verify its own work? And every one of those findings is a clickable link straight to that moment on the timeline. That&#x27;s a code review of the agent. And if you&#x27;ve got no session replay at all, there&#x27;s a map command that&#x27;ll render any repos as a 3D city on its own without any setup, which is just a really cool trick. Okay, now here we go. When this thing launched on Hacker News, the number one comment was pretty honest because you&#x27;re probably asking it too. This is very cool, but would I actually</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=190s">03:10</a></span> This is very cool, but would I actually use this? What would I actually use this for? And some people didn&#x27;t even fight back on that. They said things like, &quot;It serves no real purpose. It&#x27;s fun and not everything needs a reason.&quot; Someone else eventually landed a fair jab for a small change. A plain old git diff. It&#x27;s just faster than watching an agent go through this 3D tour. I get it. So, this is way too fresh. It&#x27;s version.3. It only reads Claude code and codeex logs. If you live in cursor, you can&#x27;t replay your sessions yet. Which brings me to the question, who&#x27;s this genuinely for? Is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=221s">03:41</a></span> question, who&#x27;s this genuinely for? Is it just fun? Well, if you&#x27;re comparing models, you want to see how Claude explores a task versus how Codeex does. This is a really cool lens you can&#x27;t really get anywhere else. If you&#x27;re staring down a huge sprawling agent change and a flat diff just isn&#x27;t giving you the shape of what happened, this 3D flythrough plus the judge report is pretty cool. It breaks that down. But for a two-line fix, come on, just read a diff. I don&#x27;t think Minewalk is going to replace any of our review tools, but it&#x27;s here maybe to give you a feel for</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=252s">04:12</a></span> it&#x27;s here maybe to give you a feel for the run that your tools were never built to actually show us. And that&#x27;s the part that we can actually play around with here. We taught our machines to write our code way faster than we ever built a way to understand what they wrote. Minewalk like graphy graphy graphy. Okay, I think I&#x27;m saying that right. This could be a first serious swing at the gap, letting you see how an agent actually reasons across the codebase, not just the keystrokes it left building it out. It&#x27;s rough, it&#x27;s early, and it&#x27;s aimed at the exact right problem, but</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Y_7_rbtQXcs&amp;t=284s">04:44</a></span> aimed at the exact right problem, but play around with it. See if it even helps you. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
