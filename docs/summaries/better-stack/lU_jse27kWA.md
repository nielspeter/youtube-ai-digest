---
title: "Harper: The Free, Private Grammarly Alternative Built in Rust"
channel: "Better Stack"
video_id: lU_jse27kWA
url: https://www.youtube.com/watch?v=lU_jse27kWA
published: 2026-07-22T12:00:35+00:00
generated: 2026-07-22T14:23:42+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/lU_jse27kWA/hqdefault.jpg
---
# Harper: The Free, Private Grammarly Alternative Built in Rust

[![Harper: The Free, Private Grammarly Alternative Built in Rust](https://i.ytimg.com/vi/lU_jse27kWA/hqdefault.jpg)](https://www.youtube.com/watch?v=lU_jse27kWA)

[Watch on YouTube](https://www.youtube.com/watch?v=lU_jse27kWA) · **Better Stack** · 2026-07-22

## TL;DR
Harper is a free, open-source grammar checker written in Rust that runs entirely offline, offering under-10-millisecond checks through ~287 deterministic, handwritten rules rather than machine learning. It trades the tone-coaching and whole-sentence rewrites of Grammarly for instant, private, predictable grammar checking that integrates directly into developer toolchains—especially code comments, commit messages, and notes.

## Key Takeaways
- Grammarly ships everything you type to its servers and stores it; Harper runs fully offline with no data leaving your machine.
- Harper uses no AI—it's a rule-based engine with ~287 handwritten Rust rules that produce deterministic, repeatable results.
- The same sentence always gets the same verdict in Harper, unlike Grammarly's ML model, which users complain changes its mind between checks.
- Harper claims sub-10-millisecond check latency with no spinner or cloud dependency.
- It integrates into developer editors via a Language Server Protocol (LSP) implementation, supporting Neovim, Zed, Helix, Emacs, and VS Code, and specifically flags typos inside code comments while ignoring actual code.
- An Obsidian plugin (200,000 downloads) checks notes and intelligently skips code fences—something Grammarly struggles with.
- The entire engine compiles to WebAssembly, allowing a zero-install test drive at writewithharper.com.
- Coverage is the trade-off: 287 rules versus Language Tool's 6,000 rules versus Grammarly's ML models. If no rule matches an error, nothing fires.
- Harper is English-only (five dialects), has ~240 open false-positive issues, and one Neovim user reported over 1 GB of RAM usage.
- Acquired by Automattic (WordPress parent company) in November 2024; some developers on Hacker News expressed reluctance to adopt anything controlled by Matt Mullenweg.

## Detailed Breakdown

### The Privacy Problem with Grammarly [00:00](https://www.youtube.com/watch?v=lU_jse27kWA&t=0s)
The video opens by framing Grammarly's cost ($140+/year) and its data practices—everything typed is shipped to servers and stored—as essentially a paid keylogger. Harper is introduced as the alternative: free, written in Rust, and functional with Wi-Fi turned off. However, the presenter immediately tempers expectations by noting Harper failed to catch a slang phrase ("I'm joshing into it"), establishing that both its strengths and limitations matter.

### Rule-Based Engine vs. Machine Learning [00:31](https://www.youtube.com/watch?v=lU_jse27kWA&t=31s)
Harper contains no AI whatsoever. Text is tagged word by word and run through approximately 287 handwritten Rust rules. Because rules are deterministic, the same sentence always yields the same verdict. This is contrasted with Grammarly's ML model, which users complain flags something at one moment and reverses itself later—a frustration Harper eliminates by never changing its mind.

### Automattic Acquisition and Installation [01:03](https://www.youtube.com/watch?v=lU_jse27kWA&t=63s)
Since November 2024, Harper has been owned by Automattic, the WordPress company, which hired its creator and kept the project under the Apache 2.0 license. Installation is straightforward: `brew install harper` or a one-click VS Code extension. It's native to Apple Silicon and works fully offline once installed.

### Live Demonstration of Speed and Accuracy [01:35](https://www.youtube.com/watch?v=lU_jse27kWA&t=95s)
With Wi-Fi disabled, the presenter demonstrates Harper flagging errors instantly: "I ate and pineapple" (wrong word), "I needthe the from the store" (doubled word), "your point is mute" (suggesting "moot"—confirmed as a handwritten rule in the source code), and various misspellings and bad punctuation. Three underlines appeared before the sentence was finished, with no spinner or cloud delay.

### Developer Toolchain Integration [02:05](https://www.youtube.com/watch?v=lU_jse27kWA&t=125s)
Harper's standout feature for developers is demonstrated in a TypeScript file: writing a comment with typos ("receive the payload") triggers flags on both misspelled words while every line of actual code is ignored. This works across essentially all programming languages. Harper ships a Language Server Protocol implementation, enabling integration into Neovim, Vim, Zed, Helix, and Emacs with one line of config. An Obsidian plugin with 200,000 downloads checks notes while skipping code fences—precisely where Grammarly trips up. The engine also compiles to WebAssembly, powering writewithharper.com as a zero-install browser-based test drive.

### How Harper Compares to Rivals [03:09](https://www.youtube.com/watch?v=lU_jse27kWA&t=189s)
Grammarly's ML offers tone clarity coaching and whole-sentence rewrites that Harper doesn't attempt. Language Tool, self-hosted, is the nearest free rival, but its context checks require a 16 GB n-gram dataset and matching RAM; without that, Hacker News users found it missing obvious errors. The presenter demonstrates Harper's ceiling by typing "me and Sally went to have seen the duck's cousin"—clearly broken English with zero flags. "What your name?" and "What day today?" also pass cleanly. If no rule matches, nothing fires.

### Limitations and Trade-offs [03:42](https://www.youtube.com/watch?v=lU_jse27kWA&t=222s)
Coverage numbers are laid out: 287 rules (Harper) vs. 6,000 rules (Language Tool) vs. ML models (Grammarly). Privacy and speed come at the cost of coverage. The repo has ~240 issues mentioning false positives—Harper flagged the word "Cloudflare" for review. Fixes ship weekly, but users will encounter false positives. No independent benchmarks exist; the speed and memory numbers are vendor-supplied. One Neovim user reported the language server consuming over 1 GB of RAM. Harper is English-only across five dialects. The Automattic acquisition raises adoption concerns among developers wary of Matt Mullenweg's control after two years of WordPress engine drama.

### Final Verdict [04:43](https://www.youtube.com/watch?v=lU_jse27kWA&t=283s)
If you pay Grammarly for tone rewrites, keep paying—Harper won't replace that. But for a free, private, instant checker inside your editor for code comments, commit messages, docs, and notes, nothing else comes close. The presenter highlights a Hacker News comment from a dyslexic writer who preferred Grammarly when it was "dumb and rule-based," arguing that when a tool fires on every keystroke, predictability isn't a compromise—it's the whole feature. The video closes with the observation that the best privacy feature ever shipped isn't a settings toggle or policy page, but software that never needed your data in the first place.

## Notable Quotes
- "A more blunt name for that would be a key logger you pay for."
- "Harper never changes its mind."
- "Grammarly is an app that watches you type. Harper is a component you install into your tool chain."
- "Coverage is what you trade for privacy and speed."
- "When a tool fires on every keystroke in your editor, predictability isn't a compromise, it's the whole feature."
- "The best privacy feature ever shipped isn't a settings toggle or a policy page. It's software that never needed your data in the first place."

## People, Tools & References Mentioned
- **Harper** — free, open-source Rust grammar checker (Apache 2.0)
- **Grammarly** — commercial ML-based grammar checker ($140+/year)
- **Language Tool** — self-hosted free grammar checker rival
- **Automattic** — WordPress parent company; acquired Harper in November 2024
- **Matt Mullenweg** — Automattic/WordPress CEO; some developers reluctant to adopt his projects
- **Editors/Tools:** VS Code, Neovim, Vim, Zed, Helix, Emacs, Obsidian
- **Technologies:** Rust, Language Server Protocol (LSP), WebAssembly
- **writewithharper.com** — browser-based zero-install test drive of Harper
- **Hacker News** — community thread cited for user feedback and comparisons

## Who Should Watch
Developers, technical writers, and privacy-conscious users who want instant grammar checking directly inside their editor for code comments, commit messages, docs, and notes—without sending any text to the cloud. Those who rely on Grammarly's tone coaching or multi-language support should watch to understand exactly what they'd be trading away.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=0s">00:00</a></span> Grammarly costs over $140 a year, and according to its own documentation, everything you type is shipped to their servers and stored there. A more blunt name for that would be a key logger you pay for. This is Harper. It&#x27;s a grammar checker that&#x27;s free, written in Rust, and works with your Wi-Fi turned off. Before you get too excited, I typed, &quot;What&#x27;s going on? I&#x27;m josh into it,&quot; and it didn&#x27;t blink. Stay with me because both halves of that are the point.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=31s">00:31</a></span> Now, with Harper, the more interesting thing about it is what&#x27;s missing. There&#x27;s no AI in it at all. It&#x27;s a rule-based engine. Your text gets tagged word by word, then ran through about 287 handwritten Rust rules. Rules are deterministic. The same sentence gets the same verdict every single time. Now, compare that to what Grammarly users keep complaining about. It tells you to delete a comment at 9 and then put it back at 10. That&#x27;s a machine learning model changing its mind about your writing. Harper never changes its mind.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=63s">01:03</a></span> writing. Harper never changes its mind. And because nothing ever leaves your machine, it&#x27;s instant. The claim is under 10 milliseconds per check. One more thing before I live run this. Since November 2024, Harper belongs to Automatic, the WordPress company, which hired its creator and kept everything Apache 2.0. Hold that thought cuz I&#x27;m going to circle back to it in just a second. If you enjoy coding tools to speed up your workflow, be sure to subscribe. We have videos coming out all the time. Now, check this out. Brew install Harper or oneclick the VS Code extension. It&#x27;s native to Apple Silicon.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=95s">01:35</a></span> extension. It&#x27;s native to Apple Silicon. And now you can switch the Wi-Fi off. You can go fully offline. If you run this, I&#x27;m going to type I ate and pineapple. Flagged instantly. If I type along the lines of I needthe the from the store, the &#x27;the&#x27; is flagged. I spell a word wrong now like your point is mute. It suggests an alternative. That correlation is literally a handwritten rule in the source code. I checked. I don&#x27;t think it&#x27;s too late. Spelled some things wrong there. Bad punctuation.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=125s">02:05</a></span> things wrong there. Bad punctuation. Three underlines before I could even finish the sentence. No spinner, no cloud. There&#x27;s nothing to wait for. And here&#x27;s the part that&#x27;s going to help us in development. I&#x27;ll open a TypeScript file and write a comment. I&#x27;m going to write receive the payload. Again, I spelled some things wrong. Harper flags both typos inside the comment. It ignores every line of actual code around it. It does this across basically every language we can write in. Harper ships a zero language server, so it drops into Neo, Vim, Zed, Helix, Emacs, one line of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=158s">02:38</a></span> Neo, Vim, Zed, Helix, Emacs, one line of config. The Obsidian plugin, 200,000 downloads, checks your notes and skips code fences, the exact thing Grammarly actually trips over. The whole engine compiles to web suddenly. So, writewithharper.com runs the full checker inside your browser tab. That&#x27;s your zeroinstalled test drive. Think of it this way. Grammarly is an app that watches you type. Harper is a component you install into your tool chain. Now, how does all this land? Grammarly&#x27;s ML does things</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=189s">03:09</a></span> this land? Grammarly&#x27;s ML does things Harper doesn&#x27;t even attempt. Tone clarity coaching, whole sentence rewrites. Language tool self-hosted is the nearest free rival. But here&#x27;s the fine print nobody&#x27;s reading. It&#x27;s good context checks need a 16 GB engram data set and the RAM to match. Skip that. And Hacker News users found it missing obvious errors. Now you need to know exactly where that baseline ends. Now, if I just write out here, me and Sally went to have seen the duck&#x27;s cousin. There&#x27;s errors, but there&#x27;s zero errors.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=222s">03:42</a></span> There&#x27;s errors, but there&#x27;s zero errors. Perfectly clean, right? Now, what your name? What day today? Also clean. That&#x27;s the ceiling of rules. If no rule matches the way a sentence is broken, nothing&#x27;s going to fire. 287 modules versus language tools 6000 rules versus Grammarly&#x27;s models. Coverage is what you trade for privacy and speed. And it cuts the other way too. 240 issues in this repo mentioned false positive. It flagged the word Cloudflare for reviewers. Fixes are shipping weekly,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=252s">04:12</a></span> reviewers. Fixes are shipping weekly, but you will hit some. Those speed and memory numbers, the vendor&#x27;s own numbers. There&#x27;s no benchmarks. They don&#x27;t exist yet. And one Neoim user clocked the language server at over a gigabyte of RAM. It&#x27;s again English only. Five dialects, nothing else. And the automatic thing I said earlier, after 2 years of WordPress engine drama, some developers on HackerNews said flat out they won&#x27;t adopt anything Matt Moldenweg controls. Fair concern. Now, if you pay Grammarly for tone rewrites,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=283s">04:43</a></span> if you pay Grammarly for tone rewrites, keep paying. Harper&#x27;s not going to replace that. If you want a free private instant checker living inside your editor for code comments, commit messages, docs, notes, nothing else comes close. This is a great hack. My favorite comment in the whole hacker news thread that I came across was from a dyslexic writer who paid for Grammarly for years. They said it actually worked better back when it was dumb and rule-based. When a tool fires on every keystroke in your editor, predictability isn&#x27;t a compromise, it&#x27;s the whole feature. Harper is free, released every</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=lU_jse27kWA&amp;t=315s">05:15</a></span> feature. Harper is free, released every week or two, and it covers precisely the surfaces Grammarly will never see, your comments and your commits. The best privacy feature ever shipped isn&#x27;t a settings toggle or a policy page. It&#x27;s software that never needed your data in the first place. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
