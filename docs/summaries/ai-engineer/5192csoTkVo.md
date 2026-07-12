---
title: "remobi.app: Don't change your terminal workflow for mobile"
channel: "AI Engineer"
video_id: 5192csoTkVo
url: https://www.youtube.com/watch?v=5192csoTkVo
published: 2026-07-12T08:47:17+00:00
generated: 2026-07-12T21:01:44+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/5192csoTkVo/hqdefault.jpg
---
# remobi.app: Don't change your terminal workflow for mobile

[![remobi.app: Don't change your terminal workflow for mobile](https://i.ytimg.com/vi/5192csoTkVo/hqdefault.jpg)](https://www.youtube.com/watch?v=5192csoTkVo)

[Watch on YouTube](https://www.youtube.com/watch?v=5192csoTkVo) · **AI Engineer** · 2026-07-12

## TL;DR
Connor Adams presents Remoby, an open-source progressive web app that mirrors your local tmux terminal sessions on a mobile phone, letting you monitor and steer AI coding agents remotely without changing your existing workflow. Rather than relying on agent-specific mobile apps or cumbersome SSH setups, Remoby simply connects to your tmux session over a secure tunnel like Tailscale.

## Key Takeaways
- Remoby lets you view and control your existing tmux terminal sessions from a phone, so you don't need to adopt a new workflow or use agent-specific mobile apps.
- It works as a progressive web app (PWA) on both iOS and Android, with a server running on your local dev machine.
- Existing alternatives (e.g., Happy, Claude's built-in handoff, SSH terminal apps) are limited to specific agents, require manual handoffs, or involve painful SSH key management.
- tmux acts as a terminal window manager, enabling multiple panes, windows, custom key bindings, and tools like lazygit or critique for code review.
- Remoby installs a "skill" that helps you set up tmux and generates touch-friendly key bindings automatically.
- Security is handled via networking tools like Tailscale (the default), Cloudflare Tunnels, or ngrok — exposing the server directly to the public internet would be dangerous.
- The UI is described as "minimally functional" rather than polished, supporting gestures like double-click to zoom into panes and scrolling within them.
- The project is open source, and Connor encourages the audience to star it on GitHub.
- Connor frames the motivation partly humorously: a compulsion to check on agents during family time, what he calls "AI psychosis."
- The talk also serves as a mini-primer on tmux and custom terminal workflows for AI agent development.

## Detailed Breakdown

**[00:07] Introduction and Motivation**
Connor Adams introduces himself and notes a schedule change. He asks the audience how many people currently check on their AI agents from their phones — few do, but many would like to. He admits ambivalence about the habit, describing a compulsion to check on agents while out with friends and family, but notes that enough people want this capability that several apps already exist.

**[01:10] Why Build Another App? Surveying Existing Options**
Connor explains he built Remoby because the tool he wanted didn't exist. He reviews existing options: Happy (a native mobile app for Claude Code, but limited to Claude and reliant on a relay server he doesn't fully trust), Claude's built-in manual handoff to mobile (which requires explicit action and doesn't support tools like Codex or Pi), and generic terminal/SSH apps for phones (which involve annoying SSH key management and don't integrate well with tmux-based workflows).

**[02:11] tmux Primer and Terminal Workflow**
Connor polls the audience for tmux users and finds few. He explains his own shift from VS Code to a terminal-based, portable setup on a remote dev machine. He then demonstrates tmux as a "window manager for your terminal," showing multiple panes running different coding agents simultaneously, switchable windows (tabs along the bottom), and custom status bar elements like CPU usage. He highlights custom key commands — for example, a shortcut to split the screen into a chosen number of panes — and admits he "vibed" (AI-generated) most of this configuration rather than learning it manually.

**[04:14] Custom Tools Inside tmux**
Beyond running agents, Connor shows how tmux supports a broader workflow: opening lazygit to review diffs, using a tool called "critique" to scroll through code changes before committing, and killing stray processes (like an agent browser occupying a port). The point is that tmux lets you build a personalized, highly customized toolkit — even if, he jokes, you still don't ship anything users actually use.

**[05:18] The Mobile Experience with Remoby**
Connor transitions to the phone demo. Remoby is a progressive web app running on iOS and Android, connected to a server on his dev machine. He opens it and shows the same tmux session from the desktop, now on mobile. He demonstrates switching an agent into plan mode via a "shift tab" control, opening git and critique views, and using touch gestures — double-click to zoom into a pane, scroll within panes, zoom out. He candidly admits the UI "looks like shit" and isn't winning design awards, but argues it is minimally functional and gets the job done.

**[06:51] Setup, Open Source, and Installation**
Remoby is open source. Rather than asking users to blindly paste a random shell script, the installer guides you through setup: it installs a "skill" that helps configure tmux if you don't have it, and if you do, it generates touch-screen-friendly key bindings for your existing setup. You can also just install the skill and NPM package directly. Connor closes by asking for GitHub stars even from those who won't use it.

**[07:54] Q&A: How It Works Under the Hood**
During Q&A, an audience member asks how tmux is controlled remotely. Connor clarifies that Remoby simply calls tmux and logs you into your existing session — tmux itself handles the pane/window management. A second question probes the phone-to-machine communication: Connor admits he didn't cover this, but explains it's just over the internet, using Tailscale by default (Cloudflare Tunnels or ngrok also work). He warns that exposing the server directly to the public internet would effectively "pwn your computer," so Tailscale is the recommended default.

## Notable Quotes
- "I've got AI psychosis, of course, and you just must build apps."
- "Now I want to go and ruin my family time. Now I can do that."
- "It's not winning any design awards, right? It looks like shit, but you can actually — it's minimally functional, or maybe functional."
- "If you just put it on the public internet, you've pwned your computer."
- "I should have called my talk 'tmux talk.'"

## People, Tools & References Mentioned
- **Connor Adams** — presenter and creator of Remoby
- **Remoby** — the open-source progressive web app presented
- **tmux** — terminal multiplexer / window manager for the terminal
- **Claude Code** — AI coding agent
- **Happy** — mobile app for Claude Code (mentioned as an alternative)
- **Codex / Pi** — other coding tools mentioned as not supported by Claude's handoff
- **lazygit** — terminal git UI
- **critique** — a diff/code review tool shown in tmux
- **Conductor** — another tool mentioned as an alternative workflow app
- **Tailscale** — default networking/tunnel solution for Remoby
- **Cloudflare Tunnels / ngrok** — alternative tunneling options
- **VS Code** — mentioned as Connor's previous editor
- **GitHub** — where Remoby is hosted (stars requested)
- **Mari** — referenced briefly regarding the "fuck around and find out" stage

## Who Should Watch
Developers who run AI coding agents in terminal-based workflows (especially tmux) and want to monitor or steer them from a phone without adopting agent-specific mobile apps or managing SSH keys. It's also useful for anyone curious about building a custom, portable terminal setup for remote AI agent development.


<details class="transcript">
<summary>Full transcript</summary>

<p>Hello everyone. Um So yeah, my name&#x27;s My name&#x27;s Connor Adams and I&#x27;m here to present to you Remoby, a little change of schedule here, so you might might not be expecting this. Um So Who here uses checks on their agents on their phone? Okay. Who here would like to</p>
<p>Who here would like to but it doesn&#x27;t. Okay, yeah. I I&#x27;m always actually torn about whether or not it&#x27;s a great idea or not. I&#x27;m thinking I&#x27;m out, you know, out and about. May might be some nice weather. Uh out with my friends and family and then I get this sort of compulsion to check on my agents. Are they Are they working well? Do I need to steer them? Do they need me? And so rightly or wrongly, that there are plenty of apps for it. So, before I show you mine, why have I built one? Well, one because I&#x27;ve got AI psychosis, of course, and you just must build apps.</p>
<p>course, and you just must build apps. But the thing I wanted didn&#x27;t really exist. So, there&#x27;s there&#x27;s Claude uh there&#x27;s Happy, which does Claude code. And it&#x27;s got a nice native motor mobile app. But it only works with uh Claude code. And also it has some relay server that I&#x27;m not sure I really trust. Um Fine. Uh what other options do we have? Another Claude code option. Well, you can use the inbuilt thing and it will uh you press a manual handoff and it will hand</p>
<p>press a manual handoff and it will hand off your session to the mobile app. That&#x27;s cool. Um but it means that you have to manually hand over and also it means that you can&#x27;t use code X or something else. Or Pi. Um Or there&#x27;s just what about just having a a like terminal app for your um for your phone. And these are also good. The The annoying things I find with it is like managing SSH keys and setting all that up. Also having uh touch controls and having it work with your existing workflows that you</p>
<p>with your existing workflows that you may have uh in something like tmux. So, another question. Tmux users. Buddy? Only a couple and that was unsure face as well. Okay, so if we don&#x27;t use tmux, that&#x27;s fine. So, I used to be I used to be a big VS code man and then now I just maybe cuz I think it&#x27;s cool, I use the terminal. But also it&#x27;s nice because it&#x27;s a portable setup and I can I&#x27;ve got a remote dev machine I can SSH into it. It&#x27;s got all my same stuff on it. So, before we get onto the mobile</p>
<p>it. So, before we get onto the mobile bit, I will just show you um tmux. So, this is my terminal and why not have four different coding agents on there at the same time? And so, what tmux is is essentially like a window manager for your terminal, so you&#x27;re able to have these panes like this and you&#x27;re also able to have um windows that you can switch between. You see the tabs along the bottom. But you can also like customize it. It&#x27;s probably a bit hard to read on the screen, but I&#x27;ve got stuff in the bottom</p>
<p>screen, but I&#x27;ve got stuff in the bottom that says, &quot;Oh, this is the CPU usage.&quot; And all this sort of stuff like I can press buttons and then I can see like how the computer&#x27;s going or whatever. CPU blah blah blah. Um and I can uh set up all custom key commands. So, for example, I press this and then how how agent maxing how token maxing you&#x27;re feeling. Do you think you can manage 16? Probably not. Four, let&#x27;s say, and then you just press that and then it does that. And I didn&#x27;t know how to do any of this and I probably still</p>
<p>to do any of this and I probably still don&#x27;t cuz obviously I vibed it. It knows how to use tmux. So, you just have like a vision in your head like, &quot;I want to be able to do this.&quot; And there are apparently other cool apps that people use, you know, like conductor and stuff and I think it&#x27;s all great, but at this moment, as Mari said, the the [ __ ] around and find out stage, I&#x27;d rather sort of own what I&#x27;m doing and find my own workflows for now, but we&#x27;ll see. And so uh that&#x27;s a bit of tmux. A bit little bit more of tmux, actually. I&#x27;m just should have called my talk tmux talk.</p>
<p>should have called my talk tmux talk. But um So, let&#x27;s say I&#x27;m I I&#x27;ve done something on Claude code and it&#x27;s done some work and then I want to see the diff. Well, I can uh load up lazy get in a in a window by just pressing some buttons and then I can scroll through it and I can see all my get stuff. Or there&#x27;s other ones, there&#x27;s a thing called critique and then I can scroll through the diff there cuz we&#x27;re checking our code, of course, before we&#x27;re committing it. Um and other like random things is like sometimes you have some</p>
<p>sometimes you have some you have some random port being used and you&#x27;re like, &quot;Why Why isn&#x27;t my dev server running? Oh, it&#x27;s there&#x27;s agent browser running on here. Let&#x27;s kill it.&quot; And you can do that. And you can create all these little tools and create your own workflow. Um And then still not ship anything that users use anyway. But anyway, um</p>
<p>[snorts]</p>
<p>the point is you can customize stuff. So, that&#x27;s that and then from there, I&#x27;ve got all my custom workflows that make me incredibly productive, of course. And then I&#x27;m like, &quot;Okay,</p>
<p>course. And then I&#x27;m like, &quot;Okay, now I want to go and ruin my family time.&quot; Now I can do that. So, here&#x27;s my Here&#x27;s my phone and I can open up here. So, it&#x27;s a progressive web app, so it works on iOS and Android and you&#x27;re I&#x27;m running a server on my machine. And I press we&#x27;ve got a Pi version or we got This is the machine we&#x27;re just in. Um and so that&#x27;s where we were. We&#x27;re exactly there and it&#x27;s it&#x27;s you can If I scroll back, oh it doesn&#x27;t work. It usually shrinks, but it&#x27;s cuz I&#x27;m switching. Anyway,</p>
<p>switching. Anyway, um and so I can do all that same stuff. So, say I need to put it into plan mode or whatever, there&#x27;s a little shift tab thing here that I can switch it into plan mode. If I want to load up get, I&#x27;ve got a little thing for that. If I want to open up the critique thing, I can scroll. It&#x27;s all got the just all the gesture stuff. Um and so if we look at this, it&#x27;s not winning any design awards, right? It looks like [ __ ] but you can actually it&#x27;s I&#x27;d argue it&#x27;s like it&#x27;s minimally</p>
<p>it&#x27;s I&#x27;d argue it&#x27;s like it&#x27;s minimally functional or or maybe functional. So, you can uh I&#x27;ve got like a touch So, you can like double click and it will zoom into each pane and then you can scroll on the panes or whatever. Um as you please. There&#x27;s nothing to scroll there. We can scroll on this one. So, you know, I can scroll on there or I can zoom in, zoom out. Um all that stuff. And so uh that&#x27;s that&#x27;s basically it. So, the idea is you have your workflow. You might like tmux and if you don&#x27;t already, you might get into it. And then you can set it up. And talking of which,</p>
<p>you can set it up. And talking of which, so yeah, it&#x27;s an open source thing. I&#x27;ll put a QR code. But it&#x27;s called Remoby. Um and so uh you know what the best idea is? Is when you see a command that just runs a random shell script, you copy and you paste that into your terminal because you know it&#x27;s going to lead to good results. And so, if you do this, you don&#x27;t have to do that. It will It will guide you through it and it installs a skill that helps you set up tmux if you haven&#x27;t got it already. Or if you&#x27;ve got tmux, it turns it into key bindings that you for your setup in the little touch</p>
<p>you for your setup in the little touch screen mode on Remoby and it just helps you set up. But you can just install the skill and install the uh NPM package and have fun. Um And I think that&#x27;s basically it. So, even if you&#x27;re not going to do it, give us a few stars, would you, on the old GitHub? Um and I think I think that&#x27;s it. Um Thank you very much.</p>
<p>[applause]</p>
<p>Yeah, yeah, you can.</p>
<p>Yeah, yeah, you can. How how do you control tmux remotely? Is it just Is that Is that just a feature of tmux kind of that you&#x27;re using? Yeah, yeah, so uh yeah, tmux is just the thing that makes it all like the panes and stuff. Uh so, you&#x27;re just jumping. So, when you set up Remoby, basically don&#x27;t even have to think about it. It just run It just calls tmux. And then you just like log straight into your session. So, you don&#x27;t you don&#x27;t really have to do anything. Yeah, yeah. A follow-up on his question, what&#x27;s the communication between the phone</p>
<p>communication between the phone Yeah. Is it just a website? I didn&#x27;t I didn&#x27;t touch on this at all, which is very very key point. So, yeah, it&#x27;s just it&#x27;s just over the internet. But so I use Tailscale to do it, but you could use Cloudflare tunnels, ngrok, whatever you like. And yeah, and security is your concern of that thing. Yeah, if you If you If you If you just put it on the public internet, you&#x27;ve pwned your computer. So. Is Is Tailscale the default process of setting that up? Yes, yeah, yeah, yeah. Yeah. So, yeah, if not, I&#x27;d be a little worried. Yeah, yeah, yes. Yeah, it&#x27;s the default</p>
<p>Yeah, yeah, yes. Yeah, it&#x27;s the default thing. Yeah, yeah, yeah. But yeah. All right. Thank you very much.</p>
<p>[applause]</p>

</details>
