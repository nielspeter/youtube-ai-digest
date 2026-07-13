---
title: "No API Key. No Cloud. Just Mac AI (Apfel)"
channel: "Better Stack"
video_id: wiQo9gayiqU
url: https://www.youtube.com/watch?v=wiQo9gayiqU
published: 2026-07-07T15:00:23+00:00
generated: 2026-07-13T06:53:37+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/wiQo9gayiqU/hqdefault.jpg
---
# No API Key. No Cloud. Just Mac AI (Apfel)

[![No API Key. No Cloud. Just Mac AI (Apfel)](https://i.ytimg.com/vi/wiQo9gayiqU/hqdefault.jpg)](https://www.youtube.com/watch?v=wiQo9gayiqU)

[Watch on YouTube](https://www.youtube.com/watch?v=wiQo9gayiqU) · **Better Stack** · 2026-07-07

## TL;DR
Apfel is a tiny open-source CLI that exposes Apple's built-in, on-device ~3-billion-parameter language model (shipped with macOS Apple Intelligence) to your terminal, shell scripts, and even an OpenAI-compatible local server. It's perfect for quick, offline micro-tasks where you'd otherwise rack up cloud API bills, but it's hard-capped by a small context window and modest reasoning ability.

## Key Takeaways
- macOS already ships a ~3B-parameter on-device language model via the Foundation Models framework; Apfel makes it usable without writing Swift.
- Apfel is MIT-licensed, installed via `brew install apfel`, and requires no model download because the model is already on the Mac.
- It offers three interfaces: a CLI (`apfel stream`), shell-friendly file input/output, and an OpenAI-compatible local server on localhost.
- Everything runs fully offline — no API keys, no cloud, no data leaving the machine.
- Best suited for small, sharp tasks: shell one-liners, commit messages from diffs, tagging, classification, short summaries.
- The model is relatively weak: ~3B parameters, "not in the same league" as GPT or Claude; it handles ~75–80% of simple shell one-liners but struggles with math and multi-step reasoning.
- The context window is under 5,000 tokens total (prompt + answer), roughly one page — too small for log files or coding sub-agents.
- Apple's safety guardrails are baked in and can't be fully disabled; a "permissive mode" softens them but control still belongs to Apple.
- The model is Apple's property, lives inside macOS, and can't be downloaded or run on non-Apple hardware.
- Compared to Ollama/MLX, Apfel offers zero choice of model but zero download; Ollama lets you swap, shrink, and fine-tune open-weight models.

## Detailed Breakdown

**[00:00] Introduction — A free model already on your Mac**
The video opens by revealing that a free AI language model sits on every eligible Mac as part of macOS, accessible offline with no API keys. Until now, reaching it basically required writing a Swift app. Apfel changes that by exposing Apple's built-in on-device model through the terminal, code, or an OpenAI-style local server. The host promises a quick demo followed by a comparison to Ollama.

**[00:34] What Apfel is and how it works**
Macs with Apple Intelligence contain an on-device language model of about 3 billion parameters, hidden behind Apple's Foundation Models framework. Apple aimed it at app developers, not end users. Apfel is a tiny, MIT-licensed, few-megabyte Swift binary that exposes this model in three ways: a CLI, a chat prompt, and — the standout feature — an OpenAI-compatible server running on localhost, all with no API key and no billing.

**[01:05] Installation and first run**
On an M4 Max Mac, installation is a single command: `brew install apfel`. There's no model to download because it's already part of Apple Intelligence. The host runs `apfel stream` with a prompt ("What can you do as a language model?") and gets an immediate response. He then kills Wi-Fi to prove it works fully offline, asking it to "Teach me the Arabic alphabet," and it streams back token by token with no internet.

**[02:08] Shell workflow integration**
Apfel can be used directly in shell workflows. The host demonstrates asking it to write a function and save the output straight to a file with a redirect. He notes it adds some extra conversational text that has to be cleaned up. He also shows feeding it an existing file (`apfel -f scriptname`) and asking questions about it — useful for quick code feedback.

**[03:12] OpenAI-compatible local server**
The feature the host likes most is Apfel's ability to run as a real OpenAI-compatible server. He takes a standard Python script using the OpenAI SDK, changes the base URL to localhost, drops in a nonsense API key (since none is needed), and runs it. It works identically to calling OpenAI — same SDK, but free and fully offline, with no data leaving the machine.

**[03:42] How Apfel differs from Ollama/MLX**
Apfel isn't running a model; it's a translator that hands prompts to Apple's Foundation Models framework and reshapes the output into what the OpenAI SDK expects. That's why there's nothing to download. Ollama and MLX, by contrast, pull down open-weight models (Llama, Qwen, etc.) that you can swap, shrink, and fine-tune. Apfel wraps the one model Apple already installed — no download, almost no disk usage, but no model choice either.

**[04:14] Where Apfel shines**
Apfel is ideal for small, sharp tasks: shell commands, commit messages from a diff, quick tagging, classification, and short summaries — the little things that would otherwise rack up a cloud bill. Because it speaks the OpenAI API, you can build and test an entire app offline against it, then switch to a real cloud provider only when you ship.

**[04:45] The ceiling — limitations and honesty**
The host is candid about the limits. The model is ~3B parameters — "not GPT, not Claude, not even in the same league." It nails maybe 75–80% of simple shell one-liners but fails on math, multi-step reasoning, and context retention. The real wall is the context window: under 5,000 tokens total (prompt + answer combined), about one page. You can't feed it log files or use it for coding sub-agents. Apple's safety guardrails are also baked in and can't be switched off, though a "permissive mode" softens them.

**[05:48] Licensing, ownership, and who should use it**
Apfel itself is open-source MIT — take it, ship it. But the model is Apple's, lives inside macOS, can't be downloaded, and can't run anywhere but an Apple machine. So it's "kind of free, kind of." For real reasoning, long documents, or production products, stay on the cloud (Claude, OpenAI) or run a bigger model via Ollama. But for the hundred tiny prompts a day, Apfel is private, offline, and already on your Mac.

## Notable Quotes
- "Think of Ollama as bringing your own equipment and Apfel as turning the key on something that's already installed."
- "It's the same SDK, just free and fully offline. No data is leaving our machine."
- "The free tier of local AI used to be a model you download and had to watch. Now it's a model that shipped inside our computer already."
- "It nails maybe 75, 80% of simple shell one-liners. And then it faceplants on math, any multi-step, any remembering context."
- "Know that 5,000 context window number before you actually build anything on it."

## People, Tools & References Mentioned
- **Apfel** — the open-source MIT-licensed CLI/tool featured in the video
- **Apple Foundation Models framework** — the macOS framework exposing the on-device ~3B-parameter model
- **Apple Intelligence** — the macOS feature set that ships the model
- **Ollama** — compared tool for running open-weight models locally
- **MLX** — Apple's machine learning framework, mentioned alongside Ollama
- **OpenAI / OpenAI SDK** — API whose format Apfel mimics for local server compatibility
- **Claude (Anthropic)** — referenced as a cloud alternative for real reasoning
- **Llama, Qwen** — open-weight models mentioned as Ollama/MLX options
- **Homebrew (`brew install apfel`)** — installation method
- **Mac M4 Max** — the host's machine used in the demo

## Who Should Watch
Developers and power users on macOS who want a zero-setup, fully offline way to handle dozens of small daily AI prompts without API costs. It's especially valuable for anyone curious about leveraging Apple's built-in Foundation Models framework from the terminal or via an OpenAI-compatible local server for prototyping.


<details class="transcript">
<summary>Full transcript</summary>

<p>There&#x27;s a free AI model sitting on your Mac right now. It works offline with no API keys and the weird part, Apple shipped it with Mac OS, but until now, getting to it basically meant writing a Swift app. This is AppFoil. It lets you talk to Apple&#x27;s built-in on-device model from your terminal, your code, or even an OpenAI style local server. I&#x27;ll show you how to talk to the model you already paid for and then I&#x27;ll stack it up against Ollama cuz you want to know how this even compares.</p>
<p>All right, now, yeah, Macs have Apple intelligence, sure. And buried inside it is an on-device language model. It&#x27;s about 3 billion parameters that lives behind a framework called Foundation Models. Apple aimed it at app developers. It was never really pointed at you until now. That&#x27;s what AppFoil changes. It&#x27;s a tiny open-source binary, MIT licensed, a few megs of Swift, and it exposes that built-in model in three different ways. It gives us a CLI, a</p>
<p>different ways. It gives us a CLI, a chat prompt, and the one that is actually really cool, an OpenAI compatible server running on localhost. All without the need for any kind of API key and racking up any bill. I&#x27;m going to run all this in about 60 seconds, then we&#x27;ll compare it to Ollama to AppFoil. If you enjoy coding tools to speed up your workflow, be sure to subscribe. We have videos coming out all the time. Now, watch how little this actually takes. I&#x27;m on my Mac M4 Max on a clean terminal, just run brew install AppFoil. That&#x27;s the entire install. It was super</p>
<p>That&#x27;s the entire install. It was super quick because no model waits to download. The model is already on your Mac as part of Apple Intelligence. Now, I can run this command here, AppFoil stream, tell it what to do, like, what can you do as a language model? Okay, cool. Now, let me kill the Wi-Fi so we&#x27;re fully offline and I&#x27;m going to run again, let&#x27;s say, at full stream. I&#x27;ll do something like &quot;Teach me the Arabic alphabet.&quot; Nice. It streams back token by token, works on a plane, it works with no internet at all. But, it doesn&#x27;t</p>
<p>internet at all. But, it doesn&#x27;t remember, so the follow-up would lack a lot of context. And here&#x27;s what really gets useful for us as devs. I can use it directly in my shell workflow. For example, I can ask it to write a function and save it straight to a file. I just need to run at full. I&#x27;m going to write out the function and then tell it which file it&#x27;s going to. Now, I have a new file with the code already written in it. Super cool. It does add all this weird text, so I have to delete that, which is kind of annoying. I can also feed it existing files. Let&#x27;s say I have</p>
<p>feed it existing files. Let&#x27;s say I have a script and I want feedback. I could run here at full F script name and then ask it questions. But, the part that I like the most is that it also runs as a real OpenAI compatible server. So, I can take the exact same few lines of Python code here I would normally send OpenAI, change the base URL and localhost, and it just works. Here&#x27;s the Python script with a nonsense API key cuz it doesn&#x27;t actually need it. I just have to drop in something. I&#x27;m going to run the file. Boom. It&#x27;s the same SDK, just free and</p>
<p>Boom. It&#x27;s the same SDK, just free and fully offline. No data is leaving our machine. So, what&#x27;s really happening here? Well, at full isn&#x27;t running a model. No. It&#x27;s just a translator. It hands your prompt to Apple&#x27;s framework and reshapes the answer into what the OpenAI SDK expects. It&#x27;s why there&#x27;s nothing to download here. It was almost instant. And that&#x27;s the clean line between this and a Llama or MLX. Those tools pull down open weight models, gigabytes of Llama or Kwen, and you can</p>
<p>gigabytes of Llama or Kwen, and you can swap them, you could shrink [snorts] them, you can fine-tune them. Those are the advantages to that. At full does the opposite. It wraps the one model Apple already installed. So, think of Ollama as bringing our own equipment and Appful as turning the key on to something that&#x27;s already installed. There&#x27;s no download, almost no disk, but no choice either. Every eligible Mac already has this. If you have Apple Intelligence, you probably have this. Nothing to install, nothing to manage, there&#x27;s nothing to update. Now, where does this</p>
<p>nothing to update. Now, where does this actually stack up? Why should I be using this, right? Small, sharp tasks like give me the show command to find something. Hit print it. Easy. You can do commit messages from a diff, quick tagging, quick classification, short summaries. The little things that are needed for us, but would really just rack up our cloud bill. This is where this would be really good. And since it speaks the OpenAI API, you can build a whole app offline against it and only switch to the real cloud when you actually ship it. That&#x27;s pretty cool. Now, here&#x27;s where I want to be honest</p>
<p>Now, here&#x27;s where I want to be honest about this cuz everything I just showed you sits under this ceiling. I&#x27;ll start with the obvious one. It&#x27;s a 3 billion parameter model. This is not GPT. This is not Claude. It&#x27;s not even in the same league, and I mean that literally. It nails maybe 75, 80% of simple shell one-liners. And then it faceplants on math, any multi-step, any remembering context. Match the task to the model and you&#x27;re fine. But the real wall is the context window of less than 5,000 tokens. Total, your prompt and its</p>
<p>tokens. Total, your prompt and its answer combined. That&#x27;s about one page. You can&#x27;t pour a log file into this thing. You can&#x27;t bolt it against coding sub agents because a real agent would just burn through everything. That budget would just be reading one small file. Know that 5,000 context window number before you actually build anything on it. Also, Apple wraps the model safety guardrails you can&#x27;t switch off. There&#x27;s a permissive mode that softens this, but the leash everything still belongs to Apple, not Appful. One last little bit here because free local</p>
<p>last little bit here because free local AI is only half of it. App full itself is actually open source MIT take it ship it. But the model is still Apple&#x27;s. It lives inside Mac OS. You can&#x27;t download it and you can&#x27;t run it anywhere but on an Apple machine. So yeah, it&#x27;s kind of free, kind of. So who should actually use this thing? Well, if you need real reasoning, you have long documents, anything you&#x27;re actually building a product on, just stay on the cloud. Claude, Open AI, it&#x27;s good. Or you can run a bigger model in a llama, that&#x27;s</p>
<p>run a bigger model in a llama, that&#x27;s fine. But for the 100 tiny prompts a day that we&#x27;re doing, you know, this is fine, right? It&#x27;s private, it&#x27;s offline, it&#x27;s already sitting on our Mac so we can just utilize this. The free tier of local AI used to be a model you download and had to watch. Now it&#x27;s a model that shipped inside our computer already. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
