---
title: "This Free CLI Tool Beats Every Paid File Transfer App (croc)"
channel: "Better Stack"
video_id: o_psX5meBo8
url: https://www.youtube.com/watch?v=o_psX5meBo8
published: 2026-07-19T21:49:23+00:00
generated: 2026-07-19T23:07:15+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/o_psX5meBo8/hqdefault.jpg
---
# This Free CLI Tool Beats Every Paid File Transfer App (croc)

[![This Free CLI Tool Beats Every Paid File Transfer App (croc)](https://i.ytimg.com/vi/o_psX5meBo8/hqdefault.jpg)](https://www.youtube.com/watch?v=o_psX5meBo8)

[Watch on YouTube](https://www.youtube.com/watch?v=o_psX5meBo8) · **Better Stack** · 2026-07-19

## TL;DR
Croc is a free, open-source CLI file transfer tool that achieves speed, security, and simplicity simultaneously—three pillars that most existing tools only manage to hit two of at a time. It uses a relay server for full-duplex transfer, PAKE-based encryption for security, and requires no accounts or server configuration, making cross-platform file sharing as easy as typing a single code phrase.

## Key Takeaways
- Most file transfer tools fail because they only optimize for two of three pillars: fast, secure, and simple—Croc is built to deliver all three.
- Traditional link-based tools (upload-then-download) are mathematically slower than full-duplex transfer, which sends and receives data simultaneously.
- Croc uses PAKE (Password Authenticated Key Exchange) instead of static shared passwords, generating a stronger encryption key on the fly via a disposable code phrase.
- The tool works through NATs and firewalls via a relay server, requiring no port forwarding or server setup—just a single binary.
- By default, transfers route through a public relay run by Croc's creator, but the relay only sees encrypted bytes and connection metadata, never file contents.
- For corporate environments with data residency concerns, Croc includes a built-in command and Docker image to self-host your own relay in about five minutes.
- Croc detects when both machines are on the same LAN and transfers locally for even faster speeds.
- Transfers can be resumed if a connection breaks mid-transfer, picking up where they left off rather than starting over.
- The user experience is minimal: one command to send, one code phrase to receive—no accounts, browser tabs, or servers required.

## Detailed Breakdown

### The File Transfer Problem [00:00](https://www.youtube.com/watch?v=o_psX5meBo8&t=0s)
The video opens with a bold claim: Croc is the best file transfer tool the presenter has ever used. It sets up the central question of why, despite dozens of available tools (AirDrop, WeTransfer, Dropbox, Google Drive, SCP, even USB sticks), people still struggle to send files quickly and reliably between computers.

### Why Existing Tools Fail [01:37](https://www.youtube.com/watch?v=o_psX5meBo8&t=97s)
The presenter explains that most tools fail because they don't satisfy all three pillars of a good file transfer system: fast, secure, and simple. Link-based tools like WeTransfer are simple but slow (sequential upload-then-download creates an effective rate slower than either individual speed) and only as secure as their link. Secure tools like SCP are fast and secure but require server setup and port forwarding—unreasonable for casual users. Most tools pick two pillars and miss the third.

### How Croc Is Different [03:43](https://www.youtube.com/watch?v=o_psX5meBo8&t=223s)
Croc is introduced as an open-source, Go-based CLI tool designed to hit all three pillars without compromise. For speed, it uses a relay server enabling full-duplex communication—both sides send and receive simultaneously—and can detect local area networks to transfer locally. For security, it uses PAKE (Password Authenticated Key Exchange) with a disposable code phrase that facilitates a cryptographic exchange to generate a stronger key on the fly; incorrect phrases cause the transfer to fail before any data moves. For simplicity, it's a single binary with no server configuration, no port forwarding, and works through NATs and firewalls via the relay.

### The Relay and Self-Hosting [05:16](https://www.youtube.com/watch?v=o_psX5meBo8&t=316s)
The video addresses who runs the relay: by default, transfers go through a public relay operated by Croc's creator, Zack. Because files are end-to-end encrypted via PAKE before leaving the sender's machine, the relay only ever sees encrypted bytes and metadata. For organizations with data residency rules or policies against third-party infrastructure, Croc includes a built-in relay command with a Docker image, allowing self-hosting in about five minutes.

### Live Demonstration [06:17](https://www.youtube.com/watch?v=o_psX5meBo8&t=377s)
The presenter demonstrates Croc between a Windows machine and a MacBook. Installation is a one-line command per platform. On the sending side, `croc send <file>` generates a random code phrase. On the receiving end, running `croc` and entering the phrase, then typing `y` to accept, completes the transfer. The presenter also demonstrates resume capability by killing the connection mid-transfer and showing it pick up where it left off. The entire experience requires no account, browser tab, or server.

## Notable Quotes
- "I think this is the best file transfer tool I've ever used. There you go. I said it."
- "Almost everyone has a story about transferring files that should have taken 30 seconds and instead ate their whole afternoon."
- "A good file transfer system needs three pillars. It needs to be fast, secure, and simple. All three at the same time without giving up on any of them."
- "One command to send, one code phrase to receive, no account, no browser tab, no server to spin up. How cool is that?"
- "Honestly, it's hard to go back once you've used it."

## People, Tools & References Mentioned
- **Croc** — the open-source Go-based CLI file transfer tool featured in the video
- **Zack Schaw** — creator of Croc
- **PAKE (Password Authenticated Key Exchange)** — cryptographic method Croc uses instead of static passwords
- **Tools compared:** AirDrop, WeTransfer, Dropbox, Google Drive, SCP, FTP, SSH, Discord, USB sticks
- **Docker** — mentioned for self-hosting a Croc relay
- **Andres** — presenter, from Better Stack

## Who Should Watch
Developers, sysadmins, and anyone who frequently transfers files between machines—especially across platforms like Windows and macOS—who wants a fast, secure, no-frills alternative to cloud upload services or SSH-based tools. It's particularly valuable for those in corporate environments who need end-to-end encryption and the option to self-host a relay.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=0s">00:00</a></span> This is Croc and it&#x27;s one of the coolest tools I&#x27;ve recently stumbled upon. I&#x27;m just going to put it out there and say it. I think this is the best file transfer tool I&#x27;ve ever used. There you go. I said it. Croc is not just a file transfer tool. It is genuinely different in the way it&#x27;s built and how it works. So, in this video, we&#x27;ll take a look at Croc, see how it works, and I&#x27;ll show you how extremely easy it is to use it. It&#x27;s going to be a lot of fun. So, let&#x27;s dive into it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=34s">00:34</a></span> So, here&#x27;s a question worth asking. How many ways can you think of right now of sending a large file to someone else&#x27;s computer? So, there&#x27;s AirDrop, Wii Transfer, Dropbox, Google Drive, SCP, Discord if you&#x27;re desperate, a USB stick if you&#x27;re really desperate, mailing a USB stick to someone if you&#x27;re absolutely insane. So, there are dozens of tools for this and yet almost everyone has a story about transferring</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=65s">01:05</a></span> everyone has a story about transferring files that should have taken 30 seconds and instead aid their whole afternoon. So, for example, your colleague tries to airdrop something to you, but sadly you&#x27;re on Windows. In another scenario, the Wii transfer link expired before the other person got around it. The file was too big for email. the other person doesn&#x27;t have a Dropbox account and doesn&#x27;t want to make one. And honestly, I don&#x27;t judge them. So, here&#x27;s the real question. With so many tools out there, why does this keep happening? And the answer is because frankly, none of these</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=97s">01:37</a></span> answer is because frankly, none of these solutions use the three-pillar strategy that makes a great file transfer solution. So, Croc was created by Zack Schaw and on his website, he explains in great detail what a good file transfer solution architecture should look like. And honestly, it makes so much sense. A good file transfer system needs three pillars. It needs to be fast, secure, and simple. All three at the same time without giving up on any of them. And most tools out there pick two and can&#x27;t</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=128s">02:08</a></span> most tools out there pick two and can&#x27;t seem to hit the sweet spot of that vin diagram. So, let&#x27;s look at each pillar separately. The way most linkbased tools work is you upload the file to a server, then the other person downloads it. Sounds fine, but this is actually mathematically slower than it needs to be. If you&#x27;re uploading at 5 megabits per second and downloading at 8 megabits per second, sequential upload then download gives you an effective rate of about 3.1 megabits per second. And that&#x27;s slower than either speed on its</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=160s">02:40</a></span> that&#x27;s slower than either speed on its own. That&#x27;s just what happens when you do things one after the other instead of at the same time. Let&#x27;s talk about secure. A lot of secure transfer tools rely on you setting a single shared password to encrypt the file, which is fine, except passwords are only as strong as the password you actually pick. And if the password gets guessed or leaked, well then that&#x27;s it. Game over. And three, it needs to be simple. At the moment, we&#x27;ve got amazing tools out there like SSH or FTP, genuinely</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=192s">03:12</a></span> out there like SSH or FTP, genuinely fast and genuinely very secure, but they require one computer to be running a server with port forwarding enabled, which is a completely reasonable setup for a data center or a techsavvy person and a completely unreasonable ask for two laptops in a coffee shop. So, look at the pattern. We transfer is simple but slow and only as secure as its link. SCP is fast and secure, but nobody&#x27;s non-technical friend is going to know how to use SCP right off the bat. So</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=223s">03:43</a></span> how to use SCP right off the bat. So almost nothing hits all three pillars. But how is Croc different? Well, Croc is an open-source gobbased CLI tool built specifically to not compromise on any of these three pillars. So first of all, fast. Instead of the upload then download model, Croc uses a relay server to set up a full duplex conversation between both computers. Both sides are sending and receiving data at the same time. So you&#x27;re not bottlenecked by the sequential upload download math from</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=253s">04:13</a></span> sequential upload download math from earlier. And if both machines happen to be on the same local area network, Croc will actually detect that and transfer locally instead, which is faster still. Next, secure. Instead of a static shared password, Croc uses something called Pake, password authenticated key exchange. It uses a disposable code phrase, but it&#x27;s not an encryption key by itself. Both sides use this phrase in a back and forth cryptographic exchange to generate a much stronger key on the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=285s">04:45</a></span> to generate a much stronger key on the fly. If someone tries to intercept that exchange with the wrong phrase, the whole thing just fails. So, no data moves and everyone knows something&#x27;s wrong. And finally, it&#x27;s simple. Single binary, no server to configure, no port forwarding, works straight through NATS and firewalls via the relay server. And on the receiving end, you just have to type CROC followed by the code phrase when it asks and then accept the transfer and it&#x27;s done. But wait, who&#x27;s actually running that relay? Well, by</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=316s">05:16</a></span> actually running that relay? Well, by default, Croc routes your transfer through a public relay run by the tool&#x27;s own creator, Zach himself. Now, because the file itself is encrypted end to end via PIG before it even leaves your machine, that relay only ever sees encrypted bytes and connection metadata. It physically can&#x27;t read your file contents. But it&#x27;s still a third-party server sitting in the middle of a transfer by default. And if you&#x27;re at a company with data residency rules or you have a policy against routing traffic through infrastructure you don&#x27;t</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=347s">05:47</a></span> through infrastructure you don&#x27;t control, that&#x27;s going to be a blocker. But the good news is that Croc accounts for this. There&#x27;s a built-in Croc relay command that spins up your own relay with a Docker image included and then you just point your transfers at it with the relay command with the relay flag instead of the default. So the public relay is the convenient default for personal use, but for anything in a corporate environment, self-hosting the relay is a 5minut setup and not a dealbreaker. But now I want to show you</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=377s">06:17</a></span> dealbreaker. But now I want to show you how extremely easy and convenient it is to use Croc. I&#x27;ve personally been using Croc a lot these past days and it&#x27;s so convenient since I have two workstations here. One is a Windows machine and another one is a MacBook. And check out how easy it is to send large files from one to the other using Croc. Installing Croc is super easy. It&#x27;s just a oneline command for both Windows and Mac. And the GitHub page has instructions for all sorts of setups. And once we have it installed, on the sending side, you need</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=408s">06:48</a></span> installed, on the sending side, you need to type croc send followed by the file and it spits out a randomly generated code phrase. And on the receiving end, run croc. Type in the code phrase when prompted. Type y to accept it. And boom, magic. It&#x27;s that easy, that fast. And here&#x27;s another thing. It also has the ability to resume transfers when the connection breaks. Let&#x27;s kill the connection mid transfer, then resume it from the sending side. And as you can see, it picks up where it left off instead of starting over. So that&#x27;s it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=439s">07:19</a></span> instead of starting over. So that&#x27;s it. That is the entire user experience. One command to send, one code phrase to receive, no account, no browser tab, no server to spin up. How cool is that? So there you have it, folks. That is Croc in a nutshell. It&#x27;s fast because of a full duplex relay transfer. It&#x27;s secure because of pake instead of using static passwords. And it&#x27;s super simple to use. And once you actually try it against the alternative, like texting someone a Wii transfer link and hoping it doesn&#x27;t</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=o_psX5meBo8&amp;t=470s">07:50</a></span> transfer link and hoping it doesn&#x27;t expire, it&#x27;s honestly hard to go back once you&#x27;ve used it. So, what do you think about Croc? Do you like it? Is it going to be in your toolkit? Let us know in the comments down below. And folks, if you like these types of technical breakdowns, please let me know by smashing that like button underneath the video. And also, don&#x27;t forget to subscribe to our channel. This has been Andres from Better Stack and I will see you in the next videos.</p>

</details>
