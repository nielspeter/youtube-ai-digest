---
title: "remobi.app: Don't change your terminal workflow for mobile"
channel: "AI Engineer"
video_id: 5192csoTkVo
url: https://www.youtube.com/watch?v=5192csoTkVo
published: 2026-07-12T08:47:17+00:00
generated: 2026-07-12T21:18:31+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/5192csoTkVo/hqdefault.jpg
---
# remobi.app: Don't change your terminal workflow for mobile

[![remobi.app: Don't change your terminal workflow for mobile](https://i.ytimg.com/vi/5192csoTkVo/hqdefault.jpg)](https://www.youtube.com/watch?v=5192csoTkVo)

[Watch on YouTube](https://www.youtube.com/watch?v=5192csoTkVo) · **AI Engineer** · 2026-07-12

## TL;DR
Connor Adams presents Remobi, an open-source progressive web app that mirrors your existing terminal and tmux workflows on a mobile phone, letting you monitor and steer coding agents remotely without adopting a new tool or relying on a third-party relay server. The talk covers why he built it, how it works with tmux, and how to get started.

## Key Takeaways
- Remobi lets you access your existing terminal/tmux sessions from a phone instead of forcing you into a new mobile-specific workflow.
- Existing mobile options for monitoring coding agents are limited—Happy only works with Claude Code and uses a relay server; Claude's built-in mobile handoff is manual and tool-specific; standalone SSH terminal apps require managing keys and don't integrate well with tmux workflows.
- tmux acts as a terminal window manager, supporting panes, windows, custom key bindings, and status displays (e.g., CPU usage), enabling a portable, remote-friendly dev setup.
- Connor runs multiple coding agents simultaneously in tmux panes and has vibed custom key bindings (e.g., spawning 4 agent panes at once) despite not knowing tmux deeply.
- Remobi is a progressive web app that works on iOS and Android by connecting to a server running on your dev machine.
- The app supports touch interactions: double-click to zoom into panes, scroll within panes, and gestures for navigation, plus a shift-tab-style toggle for plan mode.
- Security is handled via Tailscale by default; alternatives like Cloudflare tunnels or ngrok work, but exposing the server publicly would compromise your machine.
- Setup is guided: installing the skill helps configure tmux if needed and generates key bindings tailored for the mobile touch interface.
- The project is open source, and Connor encourages GitHub stars even from non-users.
- Connor acknowledges the UI isn't polished but emphasizes it's "minimally functional"—the priority is preserving your workflow, not winning design awards.

## Detailed Breakdown

### Intro and Motivation [00:07](https://www.youtube.com/watch?v=5192csoTkVo&t=7s)
Connor Adams introduces himself and asks the audience how many people check on their coding agents from their phones. He admits ambivalence about the habit—feeling a compulsion to check on agents while out with family and friends—but notes there's clearly demand for mobile agent monitoring.

### Why Build Another Mobile Agent App? [01:10](https://www.youtube.com/watch?v=5192csoTkVo&t=70s)
He explains existing options fall short. Happy is a native mobile app but only supports Claude Code and relies on a relay server he doesn't fully trust. Claude's built-in mobile handoff requires a manual step and locks you into Claude Code (no Codex or other tools). Generic terminal apps for phones work but managing SSH keys and integrating with existing tmux workflows is cumbersome.

### tmux as the Foundation [02:11](https://www.youtube.com/watch?v=5192csoTkVo&t=131s)
Connor surveys the audience for tmux users (finding few) and explains his shift from VS Code to a terminal-based setup. He values the portability: a remote dev machine accessible via SSH with all his tools. He introduces tmux as a terminal window manager supporting panes, tabs/windows, and customization.

### Custom tmux Workflows [03:13](https://www.youtube.com/watch?v=5192csoTkVo&t=193s)
He demonstrates running multiple coding agents in separate panes simultaneously. tmux can display system info (CPU usage) and support custom key commands—e.g., pressing a key sequence to spawn a chosen number of agent panes. He admits he vibed these configs with AI assistance rather than learning tmux manually, and mentions alternatives like Conductor but prefers owning his workflow for now.

### Reviewing Diffs and Managing Sessions [04:14](https://www.youtube.com/watch?v=5192csoTkVo&t=254s)
Connor shows how he loads lazygit or "critique" in a tmux window to review diffs before committing. He also describes ad-hoc utilities, like killing a rogue process occupying a port (e.g., an agent browser blocking his dev server). The broader point: tmux lets you build custom tools and workflows tailored to your needs.

### Remobi Demo on Phone [05:18](https://www.youtube.com/watch?v=5192csoTkVo&t=318s)
He switches to his phone and opens Remobi, a progressive web app running on his dev machine's server. The app mirrors the exact tmux session from his desktop. He can scroll through output, toggle plan mode via a shift-tab equivalent, and open tools like git or critique with touch-friendly gestures. He candidly admits the UI "looks like shit" but argues it's functional.

### Touch Interactions [06:20](https://www.youtube.com/watch?v=5192csoTkVo&t=380s)
Connor details the touch controls: double-clicking zooms into individual panes, scrolling works within panes, and you can zoom in and out. The emphasis is on minimal but functional mobile interaction with your existing terminal setup.

### Setup and Open Source [06:51](https://www.youtube.com/watch?v=5192csoTkVo&t=411s)
Remobi is open source. Rather than asking users to blindly paste a random shell script, the installer guides you through setup. It installs a skill that helps configure tmux if you don't have it, and generates key bindings optimized for the mobile touch interface. You can also just install the NPM package directly. He asks for GitHub stars regardless of whether people use it.

### Q&A: tmux Control and Security [07:54](https://www.youtube.com/watch?v=5192csoTkVo&t=474s)
An audience member asks how Remobi controls tmux remotely—Connor explains it simply calls tmux and logs into your existing session. Another asks about the phone-to-machine communication. Connor clarifies it runs over the internet, with Tailscale as the default secure tunnel (Cloudflare tunnels or ngrok are alternatives). He warns that exposing the server publicly would "pwn your computer," so Tailscale is the default setup path.

## Notable Quotes
- "I've got AI psychosis, of course, and you just must build apps."
- "I'd rather sort of own what I'm doing and find my own workflows for now."
- "It's not winning any design awards, right? It looks like shit but you can actually—it's minimally functional or maybe functional."
- "If you just put it on the public internet, you've pwned your computer."
- "The best idea is when you see a command that just runs a random shell script, you copy and you paste that into your terminal because you know it's going to lead to good results."

## People, Tools & References Mentioned
- **Connor Adams** — presenter and creator of Remobi
- **Remobi** — the open-source progressive web app presented
- **tmux** — terminal multiplexer / window manager for the terminal
- **Claude Code** — Anthropic's coding agent
- **Happy** — a native mobile app for Claude Code (noted limitations: Claude-only, relay server)
- **Codex** — another coding agent mentioned as unsupported by Claude's mobile handoff
- **lazygit** — terminal UI for git, used within tmux
- **critique** — a diff review tool used in tmux
- **Conductor** — another tool for managing agent workflows, mentioned as an alternative
- **Tailscale** — default secure tunnel for Remobi's phone-to-machine communication
- **Cloudflare tunnels / ngrok** — alternative tunneling options
- **VS Code** — Connor's previous editor before switching to terminal-based dev
- **Mari** — referenced briefly regarding the "fuck around and find out stage"

## Who Should Watch
Developers who already use (or are curious about) tmux and terminal-based workflows with AI coding agents, and want to monitor or steer those agents from their phone without abandoning their existing setup. It's especially relevant for people dissatisfied with tool-specific mobile apps or the overhead of managing SSH keys on mobile.


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
