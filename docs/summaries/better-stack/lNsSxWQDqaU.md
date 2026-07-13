---
title: "The Largest Supply Chain Attack Ever Just Infected Go"
channel: "Better Stack"
video_id: lNsSxWQDqaU
url: https://www.youtube.com/watch?v=lNsSxWQDqaU
published: 2026-07-08T11:27:36+00:00
generated: 2026-07-13T06:48:25+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/lNsSxWQDqaU/hqdefault.jpg
---
# The Largest Supply Chain Attack Ever Just Infected Go

[![The Largest Supply Chain Attack Ever Just Infected Go](https://i.ytimg.com/vi/lNsSxWQDqaU/hqdefault.jpg)](https://www.youtube.com/watch?v=lNsSxWQDqaU)

[Watch on YouTube](https://www.youtube.com/watch?v=lNsSxWQDqaU) · **Better Stack** · 2026-07-08

## TL;DR
The "Shai Hulud" NPM worm, which self-replicates by stealing tokens and publishing poisoned packages, has evolved to cross ecosystems into Go by hiding malicious JavaScript inside source archives. Instead of relying on install scripts, it now plants hooks in `.cloud` and `.vscode` folders that execute the moment you open a project, rendering traditional defenses like `--ignore-scripts` ineffective.

## Key Takeaways
- Shai Hulud is a self-replicating NPM worm that steals secrets (tokens, cloud keys, SSH keys) and uses them to publish poisoned versions of your packages automatically.
- It uses TruffleHog maliciously to find exposed keys, then leverages stolen NPM tokens to spread without any attacker in the loop.
- A new wave flagged by socket.dev at the end of June jumped ecosystems, appearing in a Go module called the Verana blockchain project.
- The malware doesn't infect Go packages directly; instead, it ships JavaScript files hidden inside a source archive containing `.cloud` and `.vscode` folders.
- It executes via a `settings.json` Cloud Code session-start hook and a `tasks.json` VS Code folder-open task that runs `node cloud.setup.mjs`.
- The `--ignore-scripts` flag no longer protects you because no install scripts run, and the malicious code lives in project config rather than `node_modules`.
- The payload stages through Bun, grabs credentials, and checks for security tools like CrowdStrike, Defender, and SentinelOne before proceeding.
- Best defenses include treating Cloud/VS Code/GitHub workflows as executable code, disabling VS Code automatic tasks, using short-lived OIDC tokens, and applying egress filtering on CI runners.

## Detailed Breakdown

**[00:00] Introduction and Overview**
The video opens by announcing that the NPM worm that caused chaos last year has done something unprecedented: it has jumped ecosystems and is now appearing in Go packages. The host outlines three topics to be covered: a recap of the worm, what changed in this new wave, and actionable steps to stay secure.

**[00:30] What Is Shai Hulud?**
Shai Hulud is described as a self-replicating worm that lives in package registries. When a victim installs a poisoned package, it runs on install and scans the machine for secrets, including NPM tokens, GitHub tokens, AWS/GCP/Azure keys, and SSH keys. It even runs TruffleHog, a tool normally used defensively to find exposed keys, but here it's used maliciously to steal credentials. The worm then uses stolen NPM tokens to publish poisoned versions of the victim's packages, infecting the next user automatically with no attacker in the loop. It first hit in September 2025, returned larger in November, and in 2026 a group called Team PCP open-sourced the entire worm and ran a contest for the biggest attack, leading to constant copycat waves.

**[02:00] The New Wave: Cross-Ecosystem Jump**
Security firm socket.dev flagged a new wave at the end of June with two major differences. First, it jumped ecosystems, appearing in a Go module called the Verana blockchain project. However, it doesn't infect Go packages directly, and nothing in Go's tooling runs it. Instead, the shipped source archive contained hidden JavaScript files with a `.cloud` folder and a `.vscode` folder designed to execute code as hooks when commands are run. Specifically, a `settings.json` file contains a Cloud Code session-start hook, and a `tasks.json` file has a VS Code folder-open task that runs `node cloud.setup.mjs`. This means the malware fires the moment you open a folder or start a coding session.

**[02:32] Why Traditional Defenses Fail**
From there, the payload decodes and stages through Bun, grabs your `.npm` file and every credential it can find, and even checks for security tools like CrowdStrike, Defender, and SentinelOne before going to work. The host emphasizes that the `--ignore-scripts` flag no longer works because no install scripts run, and `npm uninstall` doesn't help because the malicious code doesn't live in `node_modules` — it lives in your project config. The target has moved from app dependencies to the dev environment itself, and victims could unknowingly push malicious code to production or CI environments like GitHub workflows.

**[03:03] Five Things You Can Do Today**
The host provides five actionable security measures. First, don't rely solely on the `--ignore-scripts` flag, as this new attack sidesteps it completely. Second, treat Cloud, VS Code, and GitHub workflows as executable code, and inspect those files before opening a cloned repo or pulled dependency source in your editor. Third, keep VS Code automatic tasks turned off via the "Manage Automatic Tasks" command so folder-open tasks can't run without your approval. Fourth, use short-lived, least-privileged tokens and rely on OIDC rather than long-lived tokens, preventing the worm from replicating through you. Fifth, apply egress filtering on CI runners with a whitelist so that even if malicious code executes, it can't send stolen credentials to the attacker.

**[04:35] Closing Thoughts**
The host acknowledges the situation is frightening but stresses that following best practices — setting a minimum release age in `.npmrc`, using short-lived tokens, disabling automatic hooks, and storing sensitive data in password managers — greatly reduces risk. The video closes with a recommendation for a related video about a free alternative to Burp Suite.

## Notable Quotes
- "Your ignore scripts flag no longer works because no install scripts run and npm uninstall no longer works because the malicious code doesn't live in your node modules. It now lives in your project config."
- "For years, the advice has been to watch your dependencies, but now the target has moved. It's not your app's dependencies anymore, it's the dev environment itself."
- "If a token can't be stolen and reused, then that means the worm can't replicate through you."
- "Treat Cloud, VS Code, and GitHub workflows as executable code because they are."

## People, Tools & References Mentioned
- **Shai Hulud** — the self-replicating NPM worm
- **Team PCP** — group that open-sourced the worm and ran an attack contest in 2026
- **socket.dev** — security firm that flagged the new wave at the end of June
- **Verana blockchain project** — Go module where the new wave appeared
- **TruffleHog** — secret-scanning tool repurposed maliciously by the worm
- **Bun** — JavaScript runtime used to stage the payload
- **CrowdStrike, Defender, SentinelOne** — security tools the malware checks for before executing
- **VS Code, GitHub workflows, Cloud Code** — environments exploited as execution hooks
- **OIDC** — recommended token-free authentication approach
- **Burp Suite** — referenced via a related video recommendation
- **Better Stack** — the channel producing the video

## Who Should Watch
Developers, DevOps engineers, and security practitioners who work with NPM, Go, VS Code, or CI pipelines should watch this to understand how supply chain attacks have evolved beyond install scripts into dev environment configuration, and to learn practical steps to protect their credentials and build pipelines.


<details class="transcript">
<summary>Full transcript</summary>

<p>The NPM worm that everyone scrambled to fight last year just did something completely new. It jumped ecosystems and it&#x27;s now showing up in Go packages. And the nasty part is how it&#x27;s actually getting in. It&#x27;s planting malicious hooks into things like your cloud code setup and your VS code tasks. Today, we&#x27;re going to cover three things. A recap of what the worm actually is, a breakdown of what changed in this new wave, and a list of things that you can do today to stay secure. And we&#x27;ve covered the NPM supply chain attack several times on this channel, so subscribe to Better Stack if you don&#x27;t</p>
<p>subscribe to Better Stack if you don&#x27;t want to miss an important update. If you missed it the first time, Shai Hulud is a self-replicating worm that lives in package registers. Here&#x27;s how it works. You install a poison package, it runs on install, and then scans your machine for secrets. It&#x27;s looking for things like NPM tokens, GitHub tokens, AWS, GCP, and Azure keys, SSH keys. It even runs TruffleHog, a tool designed to protect organizations by finding exposed</p>
<p>protect organizations by finding exposed keys so you can rotate them. But in this case, it&#x27;s being used maliciously so the attacker can grab those secrets for themselves. Then it uses your stolen NPM tokens to publish poisoned versions of your NPM packages, which infects the next person, meaning there&#x27;s no attacker in the loop. It spreads automatically and that&#x27;s why it&#x27;s called a worm and not just malware. It first hit in September 2025, then came back bigger in November, and in 2026, a group calling themselves Team PCP open-sourced the</p>
<p>themselves Team PCP open-sourced the whole thing and run a contest for the biggest attack. So now, there are copycat waves constantly. Now, there&#x27;s a brand new wave which the security firm socket.dev flagged at the end of June, and two things are different. First off, it jumped ecosystems. It didn&#x27;t just appear in another NPM package, it actually appeared in a Go module called the Verana blockchain project. But this is not actually infecting Go packages directly. Nothing in Go&#x27;s tooling actually run it. What actually shipped was a source archive with a bunch of</p>
<p>was a source archive with a bunch of JavaScript files hidden within it. It contained a dot cloud folder and a dot VS code folder to execute code as hooks when other commands are run. There&#x27;s a settings.json with a cloud code session start hook and also a tasks.json with a VS code folder open task that runs node cloud.setup.mjs. So, the malware can fire the moment you open a folder or start a coding session. From there, it decodes and stages its real payload through Bun. It grabs your dot M file and then every credential it</p>
<p>dot M file and then every credential it can find and even checks if you&#x27;re running things like CrowdStrike, Defender, and SentinelOne before it goes to work. Just sit with that for a second. Your ignore scripts flag no longer works because no install scripts run and npm uninstall no longer works because the malicious code doesn&#x27;t live in your node modules. It now lives in your project config. For years, the advice has been to watch your dependencies, but now the target has moved. It&#x27;s not your app&#x27;s dependencies anymore, it&#x27;s the dev environment itself. And if you don&#x27;t notice, you could be pushing malicious code to</p>
<p>could be pushing malicious code to production to run in CI environments like GitHub workflows. So, of course, that all sounds terrifying, but here are the things you can actually do today to remain safe and secure. Don&#x27;t just lean on the ignore scripts flag as your safety net. That only covers install hooks and this new way sidesteps that completely. Treat Cloud, VS Code, and GitHub workflows as executable code because they are. When you clone a repo or pull a dependency source, actually look at those files before you open your project in your coding editor. Three is</p>
<p>project in your coding editor. Three is in VS Code, keep automatic tasks turned off. That&#x27;s the task manage automatic task command, so a folder open task can&#x27;t run without you saying yes. Four is to use short-lived and least privileged tokens and relying on things like OIDC rather than having long-lived tokens in your environment. If a token can&#x27;t be stolen and reused, then that means the worm can&#x27;t replicate through you. And five is in your CI to put egress filtering on your runners. So, if some malicious code does execute, it at</p>
<p>some malicious code does execute, it at least cannot send those credentials to the attacker. And for those not familiar, using GitHub as an example CI, egress refers to sending data out of GitHub&#x27;s networks. So, you would set up a white list and only allow requests to go to where you permit. This would stop the malicious code in its tracks. Now, I know all of this sounds pretty terrifying, but if we all just follow best practices like setting a minimum release age in .npmrc, only using short-lived tokens, disabling automatic hooks, and storing sensitive data in things like password managers, then</p>
<p>things like password managers, then we&#x27;re far less likely to fall victim. If you want to learn more about security, then we&#x27;ve just released a video covering a free alternative to Burp Suite. I&#x27;ve been Warren from Better Stack. Thanks for watching, and I&#x27;ll see you in the next one.</p>

</details>
