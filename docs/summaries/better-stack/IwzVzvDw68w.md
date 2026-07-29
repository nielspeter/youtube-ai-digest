---
title: "Homebrew 6.0 Just Changed How Your Mac Installs Software"
channel: "Better Stack"
video_id: IwzVzvDw68w
url: https://www.youtube.com/watch?v=IwzVzvDw68w
published: 2026-07-29T12:00:34+00:00
generated: 2026-07-29T14:29:20+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/IwzVzvDw68w/hqdefault.jpg
---
# Homebrew 6.0 Just Changed How Your Mac Installs Software

[![Homebrew 6.0 Just Changed How Your Mac Installs Software](https://i.ytimg.com/vi/IwzVzvDw68w/hqdefault.jpg)](https://www.youtube.com/watch?v=IwzVzvDw68w)

[Watch on YouTube](https://www.youtube.com/watch?v=IwzVzvDw68w) · **Better Stack** · 2026-07-29

## TL;DR
Homebrew 6.0 is a major release focused on a complete security overhaul rather than new features, headlined by "tap trust" which prevents arbitrary Ruby code execution from third-party taps. While the update is a significant security upgrade that most users should embrace, it introduces breaking changes for CI pipelines and automation scripts that assume silent installs or rely on untrusted third-party taps.

## Key Takeaways
- Homebrew 6.0's headline change is a complete security overhaul, not a pile of new features.
- **Tap trust** is the marquee feature: third-party taps can no longer run arbitrary Ruby code until explicitly trusted via `brew trust`.
- A new **ask mode** is on by default for developers, showing a summary of everything about to be installed and requiring confirmation before proceeding.
- The internal metadata system is now the default, making `brew update` faster by consolidating package info into a single download.
- New `brew execute` command acts like `npx` for Homebrew, letting you run a tool once without permanently installing it.
- `brew audit` (referred to as Brew VMS) scans installed packages against known security advisories.
- 6.0 patches three security holes, including one that could run code as root through the macOS installer package.
- **Tap trust is a breaking change**: CI pipelines using third-party taps will fail because `brew doctor` now errors on untrusted taps, and many GitHub Actions run `brew doctor` as a first step.
- Ask mode can also break automation scripts that expect `brew install` to proceed without prompting, leaving them hanging.
- Homebrew is **not** being rewritten in Rust; the focus remains on the Ruby codebase.
- Intel Mac support is on a retirement timeline over the next couple of years; Apple Silicon (including M5 chips) is fully supported.

## Detailed Breakdown

### Context and Motivation [00:00](https://www.youtube.com/watch?v=IwzVzvDw68w&t=0s)
The presenter previously criticized Homebrew as a "Stone Age thing" compared to Nix, but now returns to highlight Homebrew 6.0, its first major version in years. The headline isn't a batch of features but a complete security overhaul, signaling that Homebrew has "grown up."

### The Core Problem: Arbitrary Code Execution [00:33](https://www.youtube.com/watch?v=IwzVzvDw68w&t=33s)
For most of Homebrew's life, adding a third-party tap meant Homebrew would execute arbitrary Ruby code from that tap without question. In today's landscape where package managers are the top target for supply chain attacks (NPM and others repeatedly hit), this was a bad default that 6.0 aims to eliminate.

### Ask Mode: See Before You Install [01:35](https://www.youtube.com/watch?v=IwzVzvDw68w&t=95s)
A daily-felt change is the new ask mode, on by default for developers. When installing something with dependencies, Brew now presents a summary of everything it's about to install and waits for explicit confirmation, ensuring users always see the plan before anything touches their machine.

### Tap Trust: The Marquee Security Feature [02:06](https://www.youtube.com/watch?v=IwzVzvDw68w&t=126s)
When adding a third-party tap, Homebrew now stops and refuses to run any of its code until the user explicitly trusts it with `brew trust`. Official Homebrew taps are trusted out of the box, so normal usage is unaffected, but taps from unknown GitHub authors now require deliberate approval.

### Performance and New Commands [02:37](https://www.youtube.com/watch?v=IwzVzvDw68w&t=157s)
The internal metadata system is now the default, consolidating package info into a single download instead of many network trips, making `brew update` faster. A new `brew execute` command works like `npx` for Homebrew—running a tool once without permanent installation. Additionally, `brew audit` (called Brew VMS) scans installed packages against known security advisories, and 6.0 quietly patches three security vulnerabilities including a root-level code execution via the macOS installer package.

### Breaking Changes for CI and Automation [03:07](https://www.youtube.com/watch?v=IwzVzvDw68w&t=187s)
Tap trust is a breaking change. CI pipelines relying on third-party taps will fail because `brew doctor` now errors on untrusted taps, and many standard GitHub Actions run `brew doctor` as their first step. Users must manually mark taps as trusted in their config. Similarly, ask mode can hang scripts that assumed silent installs.

### What 6.0 Is and Isn't [03:39](https://www.youtube.com/watch?v=IwzVzvDw68w&t=219s)
For regular users installing apps day-to-day, little looks different—this is a security and architecture release, not a cosmetic refresh. A myth is also addressed: Homebrew is not being rewritten in Rust. That was an experiment, and the focus remains on the Ruby codebase.

### Upgrade Advice and Hardware Support [04:10](https://www.youtube.com/watch?v=IwzVzvDw68w&t=250s)
Almost everyone should upgrade; `brew update` will move users to 6.0 regardless. Those who should slow down are people running CI with third-party taps or automation expecting silent installs—handle those first. Intel Mac support is being retired over the next couple of years, while Apple Silicon (including new M5 chips) is fully supported.

### The Bigger Picture [04:41](https://www.youtube.com/watch?v=IwzVzvDw68w&t=281s)
Homebrew has evolved from a convenience tool into a checkpoint where code must prove it's trusted. The package manager has finally caught up to the threat model the rest of the industry has been living with for years—that's the real significance of 6.0, not the version number itself.

## Notable Quotes
- "The Stone Age thing that we were using just shipped its first major version in years, Homebrew 6.0. And here's the big thing. The headlines isn't a pile of new features. It's a complete security overhaul. Homebrew just grew up."
- "We'll just run whatever code the repo hands us is a bad default. And Homebrew 6.0's feature exists to kill that."
- "It says this tap isn't trusted yet and it will not run a line of its code until I explicitly say so."
- "This is a release with a spine."
- "The package manager caught up to the threat model the rest of us have been living inside for years. That's the real thing here, not the number in the box."

## People, Tools & References Mentioned
- **Homebrew 6.0** — the subject of the video
- **Nix** — referenced as a faster alternative the channel previously compared favorably to Homebrew
- **NPM** — cited as an example of package managers hit by supply chain attacks
- **`brew trust`** — new command to explicitly trust a third-party tap
- **`brew execute`** — new command analogous to `npx`, for running a tool once without installing
- **`brew doctor`** — now errors on untrusted taps, affecting CI pipelines
- **`brew audit` / Brew VMS** — scans installed packages against known security advisories
- **GitHub Actions** — many standard actions run `brew doctor` as a first step, causing breakage
- **Ruby** — Homebrew's core language; Rust rewrite was only an experiment
- **Apple Silicon / M5 chips** — fully supported in 6.0
- **Intel Macs** — support retirement timeline announced

## Who Should Watch
This video is ideal for macOS developers, DevOps engineers, and anyone managing CI pipelines that use Homebrew—especially those relying on third-party taps or silent install automation. It's a concise, practical briefing on what breaks, what improves, and what to do before upgrading to 6.0.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=0s">00:00</a></span> A few months ago on this very channel, we made a whole video that basically called homebrew this Stone Age thing we use because Nyx runs circles around it. So, it&#x27;s only fair that I circle back here and tell you this. The Stone Age thing that we were using just shipped its first major version in years, Homebrew 6.0. And here&#x27;s the big thing. The headlines isn&#x27;t a pile of new features. It&#x27;s a complete security overhaul. Homebrew just grew up.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=33s">00:33</a></span> Now, let me explain what actually changed because it&#x27;s more interesting than just a bumped version number. For basically the entire life of Homebrew, when you added a third-party tap, someone else&#x27;s package repo, Homebrew would just run their Ruby code. It would just execute their code. Any tap, arbitrary code, without really any questions asked. Now, think about that world that we&#x27;re in now. Package managers are the number one target for supply chain attacks right now. NPM, all of them getting hit over and over. We&#x27;ll</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=63s">01:03</a></span> of them getting hit over and over. We&#x27;ll just run whatever code the repo hands us is a bad default. And Homebrew 6.0&#x27;s feature exists to kill that. It&#x27;s called tap trust. If you enjoy coding tips and tricks like this, be sure to subscribe. We have videos coming out all the time. But let me start with the part you&#x27;ll actually feel every single day. Brew version. There it is. 6.0. Now watch what happens when I install something that pulls a few dependencies. Instead of silently going off and doing it, Brew now lays out a summary of everything it&#x27;s about to install and waits for me</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=95s">01:35</a></span> it&#x27;s about to install and waits for me to say yes. That&#x27;s the new ask mode and it&#x27;s on by default for devs. Now tiny change, but it means you always see the plan before Brew lays a finger on any of our machine. Now the big one, tap trust. Watch when I add a third party tap. Homebrew stops me cold. It says this tap isn&#x27;t trusted yet and it will not run a line of its code until I explicitly say so. I trust it on purpose with brew trust and only then does it actually execute. The official homebrew taps</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=126s">02:06</a></span> execute. The official homebrew taps trusted right out of the box. So your normal brew install life is the exact same. But that little sketchy tap from some GitHub stranger that you found on a readme, now that&#x27;s kind of like a locked door. You have to actually approve that. And honestly, that&#x27;s probably a pretty good decision at this point. And this isn&#x27;t the only real upgrade here. The internal metadata system is now the default, which means all your package info comes down in one clean download instead of a dozen little network trips. So, brew update is a lot quicker.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=157s">02:37</a></span> So, brew update is a lot quicker. There&#x27;s a brand new command, brew execute, which basically is MPX for homebrew. Run a tool once without permanently bolting it onto your system. There&#x27;s Brew VMS which scans packages you already have installed against known security issues advisories and 6.0 quietly patched three security holes including one that could run code as root through the Mac installer package. This is a release with the spine. Okay, now here&#x27;s the catch with all this and for some of you it&#x27;s going to be a big</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=187s">03:07</a></span> for some of you it&#x27;s going to be a big one so I&#x27;m just going to bury it on you. Tap trust is the breaking change. If you&#x27;ve got CI pipelines that lean on thirdparty taps, Brood Doctor now throws an air the moment it sees an untrusted one and a huge number of standard GitHub actions run Brute Doctor as their very first step. So people upgraded and their build just started failing. The fix is to mark those taps as trusted in your config, but you have to actually go do it yourself. Nobody&#x27;s going to do it for you. Same story with the ask mode. If</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=219s">03:39</a></span> you. Same story with the ask mode. If you&#x27;ve got scripts that quietly assumed Brew installs without asking, that new prompt can leave them hanging forever. Now, the whole framing thing, too. If you&#x27;re just a regular person installing apps day-to-day, this barely looks any different. This is a security and architecture release, not just a fresh coat of paint. One quick myth here, too. A lot of things are getting rewritten in Rust. No, homebrew is not getting rewritten in Rust. At least not now. That was a whole experiment. the focus is right back on the Ruby codebase as it</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=250s">04:10</a></span> is right back on the Ruby codebase as it always was. So, should you upgrade to Homebrew 6.0? For almost everyone, the answer is just yes. You&#x27;re getting three security fixes and frankly, Brew Update is going to walk you on to 6.0 whether you plan for it or not. Now, the people who maybe need to slow down a little bit here is anyone running CI that touches third party taps or automation that expects silent installs. Handle those first, you&#x27;re golden. And if you&#x27;re still on an Intel Mac, heads up. 6.0 spells out the timeline for retiring</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=281s">04:41</a></span> spells out the timeline for retiring Intel support over the next couple of years. Apple silicone people, the new computers, we&#x27;re completely fine. It even adds support for the new M5 chips. Here&#x27;s how I&#x27;d kind of leave this. For years, homebrew was a convenience to say the least. Just the fastest way to get software onto a Mac. With 6.0, know, it looks like it&#x27;s turned itself into more of a checkpoint, a place where the code coming onto the machine finally has to prove it&#x27;s trusted. This is a big step. The package manager caught up to the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=IwzVzvDw68w&amp;t=311s">05:11</a></span> The package manager caught up to the threat model the rest of us have been living inside for years. That&#x27;s the real thing here, not the number in the box, 6.0, 6.1. It&#x27;s what came with it. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
