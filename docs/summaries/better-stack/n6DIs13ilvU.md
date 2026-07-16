---
title: "Grok Was Caught Uploading Your Entire Codebase"
channel: "Better Stack"
video_id: n6DIs13ilvU
url: https://www.youtube.com/watch?v=n6DIs13ilvU
published: 2026-07-16T09:00:07+00:00
generated: 2026-07-16T10:21:39+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/n6DIs13ilvU/hqdefault.jpg
---
# Grok Was Caught Uploading Your Entire Codebase

[![Grok Was Caught Uploading Your Entire Codebase](https://i.ytimg.com/vi/n6DIs13ilvU/hqdefault.jpg)](https://www.youtube.com/watch?v=n6DIs13ilvU)

[Watch on YouTube](https://www.youtube.com/watch?v=n6DIs13ilvU) · **Better Stack** · 2026-07-16

## TL;DR
Grok's coding CLI was caught uploading users' entire codebases—including Git history, environment variables, and even deleted secrets—to xAI servers, regardless of whether the prompt required file access. After viral backlash, xAI implemented a server-side kill switch and added a `/privacy` command, but the upload code remains in the binary and privacy mode only controls server-side retention, not client-side transmission.

## Key Takeaways
- Grok CLI uploaded entire repositories (including full Git history and environment variables) even when explicitly told not to open any files.
- One user who ran Grok in their home directory reported that their entire user directory—including SSH keys, password manager databases, photos, and videos—was uploaded.
- The upload behavior persisted even with the "help improve this model" setting disabled; a server-side flag called `trace upload enable` was always set to `true`.
- Researcher Seriblab used MITM proxy to inspect traffic and confirmed the full-repo upload behavior, which worked even on a 12 GB repository.
- Competing tools (Claude Code, Codex, Gemini) only send files they actually read—this bulk upload is unique to Grok CLI.
- xAI's initial fix was silent: disabling the trace upload flag server-side and adding a `disable codebase upload` flag set to `true` for all accounts.
- Elon Musk tweeted that all user data uploaded before the fix would be "completely and utterly deleted," but also asked users to leave data retention on for debugging.
- The `/privacy` command added in a subsequent update only toggles server-side retention—it does not stop the client from transmitting data.
- The privacy toggle is per-session, meaning users must re-enable it every session to maintain privacy.
- The code responsible for uploading entire repos still exists in the Grok CLI binary; only a server-side flag prevents it from activating.

## Detailed Breakdown

**[00:00] Initial Discovery and Severity**
The video opens with alarming reports that Grok's coding CLI uploaded entire user directories to xAI servers, including SSH keys, password manager databases, documents, photos, and videos. The tool also uploaded full repository contents and Git history, including files it was explicitly told not to open and secrets that had been deleted from Git history. The host frames this as a serious and massive mistake by the Grok team.

**[00:31] Viral Tweet and Investigation**
The story gained traction from a tweet advising users to run a grep command on their Grok logs, warning "you will be pissed." Hundreds of users confirmed similar findings. One user who ran Grok in their home directory discovered the entire directory was uploaded. Further investigation revealed the CLI shipped what was described as a "malware-like background code collector."

**[01:01] Researcher Seriblab's MITM Proxy Analysis**
Researcher Seriblab used MITM proxy to inspect Grok CLI's network traffic. When opening Grok in a repo and sending the prompt "reply okay, do not open any files," Grok uploaded the entire repo anyway via a POST request containing the full repo bundle, Git history, and environment variables. The upload worked even on a 12 GB repository. Testing Claude Code, Codex, and Gemini showed they only send files they actually read, confirming this was unique to Grok CLI. Disabling the "help improve this model" setting did not stop the behavior; a server-side flag `trace upload enable` was always set to `true`.

**[02:03] xAI's Silent and Public Response**
After the posts went viral, xAI first made a silent fix: the `trace upload` flag was disabled and a new `disable codebase upload` flag was set to `true` for all accounts—a server-side kill switch. xAI then publicly responded on Twitter, emphasizing their commitment to privacy, noting that zero data retention teams have no trace or code data retained, and that the `/privacy` command in the CLI can disable data retention and delete previously synced data. Elon Musk tweeted that all user data uploaded before the fix would be completely deleted, though he also asked users to leave the setting on for debugging purposes.

**[03:05] Inadequacy of the Fix**
The host argues that none of xAI's responses directly address the core issue of uploading entire repos. The updated Grok CLI added a `/privacy` command but did not remove the upload code from the binary—only the server-side flag prevents it from reactivating. The `/privacy` command merely disables traces and flips a server-side toggle called `coding data retention opt out`. Seriblab's analysis showed it does nothing locally: session traces are still posted to xAI in full regardless of the setting. The only difference is the server response—200 (stored) when privacy is off, 204 (no content/discarded) when on.

**[04:07] Per-Session Privacy and Recommendations**
The privacy command is a per-session toggle, meaning users must re-enable it every session. The host recommends that anyone who used Grok CLI check their logs with the provided grep command to see which sessions triggered uploads, and rotate all keys if data was transmitted. A hardening guide is referenced for users who want to continue using Grok CLI, showing how to set `disable codebase upload` in the config to hard-stop the upload pipeline. The host closes by questioning whether viewers would trust or continue using Grok CLI after learning this.

## Notable Quotes
- "Grok has uploaded my entire user directory to XAI servers. It contains my SSH keys, my password manager database, my documents, photos, videos, everything."
- "The only prompt that they sent to it was reply okay, do not open any files. It turns out though that that instruction does not matter as Grok still uploaded the entire repo anyway."
- "All user data that was uploaded to space xAI before now will be completely and utterly deleted. Zero anything whatsoever will remain." — Elon Musk
- "Your session traces are still posted to xAI in full, whether it's on or off, and the only difference is in how the server responds."
- "It just really seems to me like this code shouldn't be in there, as no other tool uses it."

## People, Tools & References Mentioned
- **Grok CLI** — xAI's coding command-line tool at the center of the controversy
- **xAI** — Elon Musk's AI company behind Grok
- **Seriblab** — Security researcher who analyzed Grok CLI traffic using MITM proxy
- **MITM proxy** — Tool used to inspect Grok CLI's network traffic
- **Claude Code, Codex, Gemini** — Competing coding CLI tools tested for comparison; none exhibited the bulk upload behavior
- **`/privacy` command** — Grok CLI command added in update to toggle data retention
- **`trace upload enable` / `disable codebase upload`** — Server-side flags controlling the upload behavior
- **Elon Musk** — Tweeted confirmation that all previously uploaded user data would be deleted
- **Zero Data Retention** — xAI's enterprise setting ensuring no trace or code data is retained

## Who Should Watch
Developers, DevOps engineers, and security-conscious coders who use or are considering AI coding CLIs—especially Grok CLI—should watch this to understand the serious privacy implications and learn how to check their logs and harden their configuration against unwanted data uploads.


<details class="transcript">
<summary>Full transcript</summary>

<p>Grok has uploaded my entire user directory to XAI servers. It contains my SSH keys, my password manager database, my documents, photos, videos, everything. Grok&#x27;s coding CLI uploaded your whole repo and your Git history including files it was told not to open and secrets deleted from history. This is a seriously bad and massive mistake from the Grok team, so let&#x27;s break down what happened, how you can check if your code was uploaded and what XAI has done to fix this. So, I first came across this from this</p>
<p>So, I first came across this from this tweet telling people to run this grep command to read their Grok logs saying you will be pissed. It shows a photo of the logs showing it queuing up a repo upload to Grok servers. This tweet has hundreds of replies and quotes of people running this command and getting a similar result and even one user who ran Grok in his home directory reporting they uploaded all of it. Further investigation showed that it ships a malware-like background code collector. So, let&#x27;s take a look at what it was actually doing and this is a report by a researcher called Seriblab who used MITM proxy to inspect the traffic that Grok CLI was sending and receiving. And they</p>
<p>CLI was sending and receiving. And they open up Grok in a repo and the only prompt that they sent to it was reply okay, do not open any files. It turns out though that that instruction does not matter as Grok still uploaded the entire repo anyway. There was a post request that was sent containing the whole repo bundle and this bundle had all of the Git history and even environment variables. This is what I find so bad about all of this. Yes, we all know that when we&#x27;re using a remote model our code is going to be sent to their servers, but there&#x27;s normally an assumption that it&#x27;s only the code they actually needs to read that is sent to them. It&#x27;s not the entire code base even when it&#x27;s not relevant to the prompt.</p>
<p>when it&#x27;s not relevant to the prompt. They even showed that this worked when a repo was 12 gigabytes. It still uploads the whole thing. Testing this in the other tools like Claude Code, Code X, and Gemini, it shows they only sends the file that it reads. This is a unique problem to Grok CLI. They even found that if you turned off the help improve this model setting, it would still do this and fetching the user settings from the API showed that there was actually a flag called trace upload enable which was always set to true. Now, all of these tweets and this post started to go viral, so how did xAI respond? Well, first they made a bit of a silent fix. If you tried this again a day later</p>
<p>If you tried this again a day later after the post went viral, the setting showed that that trace upload flag was now disabled, and there was actually a new one called disable code base upload, which was set to true, seemingly for everyone&#x27;s account. So, they&#x27;d actually put in a server-side kill switch for the upload of code. Shortly after, they then also publicly responded on Twitter, saying, &quot;We care deeply about your privacy and respect customer choice. For teams using zero data retention, no trace and code data is ever retained. All API key use of Grok build also respects zero data retention. If zero data retention is disabled, the {slash} privacy command is available in the CLI</p>
<p>privacy command is available in the CLI to disable data retention, which also deletes previously synced data. Run the {slash} privacy command to view or change your settings at any time.&quot; Elon also tweeted, saying that as a precautionary measure, all user data that was uploaded to space xAI before now will be completely and utterly deleted. Zero anything whatsoever will remain. But, he did also ask in another tweet that you leave the setting on, as this is actually helpful for debugging issues if they can retain some amount of data, which I can believe that if we were just talking about traces. That is a pretty common practice. But, uploading an entire repo to their servers, none of</p>
<p>an entire repo to their servers, none of these responses seem to address that part. And the new Grok CLI update simply added a privacy command, but it&#x27;s worth noting that this update didn&#x27;t actually remove the code that uploads your whole repo. You can actually still find that in the binary, so it seems the only thing stopping this from turning on again is that server-side flag that is controlled by xAI. It just really seems to me like this code shouldn&#x27;t be in there, as no other tool uses it. Plus, if we take a look at that new privacy command, this actually simply disables traces and flips a server-side toggle called coding data retention opt out, and the same researcher actually analyzed this command and showed that it</p>
<p>analyzed this command and showed that it does nothing locally. Your session traces are still posted to xAI in full, whether it&#x27;s on or off, and the only difference is in how the server responds. If it&#x27;s off, it&#x27;s going to respond with a 200, meaning it&#x27;s been stored, and if privacy mode is on, it simply returns a 204 to say no content, and the data has been discarded. So, it&#x27;s actually only a server-side retention switch, and it doesn&#x27;t block it from the client-side. So, you&#x27;re still transmitting everything. You just have to trust the XAI servers are actually going to discard it instead of storing it. Even if I did trust XAI, it gets even worse because that privacy</p>
<p>gets even worse because that privacy command is actually a per-session retention toggle. So, you may have to toggle this in every session to keep your data safe. This just seems incredibly backwards to me, but this is where we are now. If you have used the Grok CLI in the past, and you want to see what may have leaked from your machine, you can check your logs. This grep command shows you exactly which sessions triggered the uploads. If you take security seriously as well, you&#x27;re probably going to want to rotate all of those keys if it does show that some of this data was sent over, unless you trust fully that XAI has deleted all of this. Finally, if you want to keep some semblance of privacy while still using</p>
<p>semblance of privacy while still using the Grok CLI, although I probably wouldn&#x27;t recommend it, there is a really good write-up here on how you can harden the Grok CLI, and it shows you where to set things like disable code base upload in your config, which should hard stop that upload pipeline. So, that&#x27;s the story. For some reason, Grok was uploading your whole repo even when it didn&#x27;t need it, and they seemingly have deleted all of that data now and walked back the feature, but I do want to know, do you trust them, and would you use the Grok CLI from now on now that you know this? Let me know in the comments down below. Wait there, subscribe, and as always, see you in the next one.</p>

</details>
