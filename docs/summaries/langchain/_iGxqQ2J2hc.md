---
title: "NemoClaw + dcode: A governed blueprint for AI coding agents"
channel: "LangChain"
video_id: _iGxqQ2J2hc
url: https://www.youtube.com/watch?v=_iGxqQ2J2hc
published: 2026-07-08T19:22:49+00:00
generated: 2026-07-16T21:17:01+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/_iGxqQ2J2hc/hqdefault.jpg
---
# NemoClaw + dcode: A governed blueprint for AI coding agents

[![NemoClaw + dcode: A governed blueprint for AI coding agents](https://i.ytimg.com/vi/_iGxqQ2J2hc/hqdefault.jpg)](https://www.youtube.com/watch?v=_iGxqQ2J2hc)

[Watch on YouTube](https://www.youtube.com/watch?v=_iGxqQ2J2hc) · **LangChain** · 2026-07-08

## TL;DR
This video demonstrates how to run LangChain Deep Agents Code (dcode), a terminal-based AI coding agent, inside a governed NemoClaw OpenShell sandbox. By using Nemotron 3 Ultra served via Baseten's OpenAI-compatible endpoint, developers get a familiar coding workflow while organizations gain auditability, policy control, and an isolated execution environment around the agent.

## Key Takeaways
- **dcode** is a terminal-based AI coding agent from LangChain that can inspect projects, write code, run tests, and summarize changes.
- **NemoClaw** provides a governed OpenShell sandbox that wraps the dcode runtime, giving organizations control and auditability over where the agent runs and what it can access.
- **Nemotron 3 Ultra** is the underlying LLM, served from **Baseten** through an OpenAI-compatible API endpoint.
- NemoClaw's installer handles CLI setup and drops users into an onboarding flow where they select the dcode integration and inference provider.
- The sandbox is configured with a resource profile (OpenShell defaults) and a policy tier (balanced), which keeps the environment governed while remaining practical for coding tasks.
- The demo shows dcode fixing a failing Python unit test by creating a missing subtraction function, then validating the fix by running tests.
- NemoClaw provides governance commands like `policy explain`, `policy list`, and `logs` to inspect policy context and audit agent activity.
- The workflow preserves the normal developer experience of using a terminal coding agent while adding enterprise-grade controls around it.

## Detailed Breakdown

### Overview of the NemoClaw + dcode Workflow [00:00](https://www.youtube.com/watch?v=_iGxqQ2J2hc&t=0s)
The presenter introduces the integration: dcode (a terminal-based coding agent) uses Nemotron 3 Ultra served from Baseten via an OpenAI-compatible endpoint, and runs inside a NemoClaw-managed OpenShell sandbox. The goal is to give developers their familiar coding agent workflow while providing organizations auditability and control over the environment.

### Installing NemoClaw and Starting Onboarding [00:35](https://www.youtube.com/watch?v=_iGxqQ2J2hc&t=35s)
The presenter installs NemoClaw using the public installer from the NVIDIA docs. The installer sets up the CLI and launches an onboarding menu. From the menu, the presenter selects option three, "LangChain Deep Agents Code," which is the dcode integration.

### Configuring the Inference Provider and Model [01:07](https://www.youtube.com/watch?v=_iGxqQ2J2hc&t=67s)
NemoClaw prompts for an inference provider. The presenter selects option three, "Other OpenAI compatible endpoint," since Baseten exposes an OpenAI-compatible model API. He pastes the Baseten base URL, his Baseten API key, and the Nemotron 3 Ultra model slug from the Baseten documentation. This configures the model route so dcode's model calls go to Nemotron 3 Ultra through Baseten.

### Sandbox Configuration and Provisioning [01:39](https://www.youtube.com/watch?v=_iGxqQ2J2hc&t=99s)
The presenter names the sandbox "dcode demo" and reviews the configuration shown by NemoClaw. For resource profile, he selects option six, OpenShell defaults, which are sufficient for an average demo workload. For policy tier, he chooses "balanced" because it provides a practical default for coding agent work while keeping the sandbox governed. NemoClaw then provisions the OpenShell sandbox and prepares the dcode runtime.

### Connecting to the Sandbox and Setting Up the Workspace [02:40](https://www.youtube.com/watch?v=_iGxqQ2J2hc&t=160s)
The presenter verifies the sandbox is live with `NemoClaw dcode status`, then connects using `NemoClaw dcode demo connect`. Inside the terminal environment, he confirms dcode is installed, creates a new folder, and builds a tiny Python project with a basic `add` function and unit tests that expect a `subtract` function that does not yet exist. Running the tests shows a failure, which gives dcode a real task to fix.

### Running dcode to Fix the Failing Test [03:44](https://www.youtube.com/watch?v=_iGxqQ2J2hc&t=224s)
The presenter starts dcode by typing `dcode` and skips setup steps. He pastes a natural-language task: inspect the project, fix the failing test with the smallest reasonable change, run the tests, and summarize what changed. dcode proposes creating a `subtract` function, which the presenter approves. dcode then runs the tests, which the presenter also approves. Both tests pass. The presenter exits dcode, runs the same Python unit test command himself, and confirms both tests pass. He verifies the subtraction function is now in the file.

### Exploring NemoClaw's Governance and Auditing Features [05:26](https://www.youtube.com/watch?v=_iGxqQ2J2hc&t=326s)
The presenter emphasizes that this is not just a coding agent running directly on a laptop—NemoClaw provides a governed OpenShell sandbox around the dcode runtime. He exits the sandbox terminal and demonstrates three governance commands. `NemoClaw dcode demo policy explain` shows the policy context, including active presets, approval and remediation behavior, and support boundaries. `policy list` shows which policy presets are configured. `logs tail 80` displays the last 80 log lines, giving teams a more auditable environment for running coding agents.

### Summary and Closing [06:29](https://www.youtube.com/watch?v=_iGxqQ2J2hc&t=389s)
The presenter wraps up by summarizing the full workflow: dcode running inside a NemoClaw OpenShell sandbox with Baseten inference. Developers get a familiar terminal coding agent experience, while teams get a governed, auditable environment around it.

## Notable Quotes
- "Developers get their familiar coding agent workflow they expect, while organizations get more auditability and control around the environment."
- "This is not just a coding agent running directly on my laptop. NemoClaw gives us a governed OpenShell sandbox around the dcode runtime."
- "The agent can understand the workspace, make a code change, validate it, and summarize what happened."
- "Developers get a familiar terminal coding agent while teams get a governed, auditable environment around it."

## People, Tools & References Mentioned
- **NemoClaw** — governance and sandbox management tool; installed via public installer from NVIDIA docs
- **dcode (LangChain Deep Agents Code)** — terminal-based AI coding agent
- **Nemotron 3 Ultra** — LLM model used for inference
- **Baseten** — inference provider exposing an OpenAI-compatible model API
- **OpenShell** — sandbox environment managed by NemoClaw
- **NVIDIA docs** — source of the NemoClaw public installer
- **Policy tiers** — "balanced" was chosen as a practical default for coding agent work
- **Governance commands** — `policy explain`, `policy list`, `logs`

## Who Should Watch
DevOps engineers, platform teams, and engineering managers who want to deploy AI coding agents in a controlled, auditable enterprise environment. It's also useful for developers interested in how dcode works with governed sandboxes and OpenAI-compatible inference endpoints.


<details class="transcript">
<summary>Full transcript</summary>

<p>Today, I&#x27;m going to show you how to write code with LangChain Deep Agents Code, or dcode, inside a governed NemoClaw OpenShell sandbox. The flow is simple. You write code using dcode, a terminal-based coding agent. Dcode uses Nemotron 3 Ultra, served from Baseten, through an OpenAI-compatible endpoint. And then the agent runs inside a NemoClaw-managed OpenShell sandbox, so teams get a controlled environment around where the agent runs and what it can access. That means developers get their familiar coding agent workflow they expect, while organizations</p>
<p>get more auditability and control around the environment. First, I&#x27;ll install NemoClaw using the public installer from the NVIDIA docs. The installer handles the CLI setup and then drops it directly into onboarding. When the onboarding menu appears, I&#x27;ll choose option number three, LangChain Deep Agents Code. That is the dcode integration we want for this walkthrough. Next, NemoClaw asks for the inference provider. For this video, we&#x27;re using Baseten for inference, so I&#x27;ll choose three.</p>
<p>Other OpenAI compatible endpoint. Baseten exposes an OpenAI compatible model API, so first I&#x27;ll paste the Baseten base URL from their documentation. I&#x27;ll paste my Baseten API key and finally I&#x27;ll paste the Nemotron 3 Ultra model slug from the Baseten docs as well. Now the model route is configured, dcode will run inside the sandbox and the model calls will go to Nemotron 3</p>
<p>Ultra through Baseten. Next I&#x27;ll choose the sandbox name for this. We&#x27;ll do dcode demo. Now, NemoClaw shows the configuration before provisioning. Everything seems to look good. I will confirm this. For resource profile, I&#x27;ll choose option number six, OpenShell defaults. For an average demo workload, the defaults are enough. Next, it&#x27;ll ask you for the policy tier for which I&#x27;ll choose balanced, because it gives us</p>
<p>a practical default for coding agent work while still keeping the sandbox governed. On this screen, I just need the balanced defaults are enough. Once that is set, NemoClaw provisions the OpenShell sandbox and prepares the dcode runtime. Now that the deep agents code sandbox is live, I&#x27;ll first just want to verify its status. I&#x27;ll do NemoClaw dcode status. It looks like everything is good to go.</p>
<p>Now I&#x27;ll connect to the sandbox with this command. NemoClaw, dcode demo, connect. Now we&#x27;re on this screen, which means we&#x27;re in the terminal inside the environment. I&#x27;ll quickly check that dcode is available. Just making sure it looks like it&#x27;s installed. Then now I&#x27;ll create a small workspace for the coding tasks that we&#x27;re about to test. So I&#x27;ll go ahead and make a new folder and CD into that folder as well.</p>
<p>Once inside this folder, I&#x27;m going to create a tiny Python project with a basic add function. In addition, I will add some unit tests where it expects a subtraction function that does not exist yet. So we have both those things. And now let&#x27;s just run our unit tests to see how it works. We can see that there&#x27;s a failure. This failing test gives dcode something real to fix.</p>
<p>Now, I&#x27;ll start dcode from inside the sandbox, which is as simple as typing dcode. We can skip the setup steps for now. And now, instead of pasting one giant command into the terminal, I&#x27;ll use it how a developer normally would. Open dcode and then paste the task. So for the purposes of this, I will say, hey, inspect this tiny Python project, fix the failing test by making the smallest reasonable change, run the test, and summarize what changed.</p>
<p>So we&#x27;re going to let dcode, with Nemotron 3 Ultra, do what it wants. It wants to create the subtract function, which I&#x27;m going to approve. It&#x27;s going to test. So I&#x27;ll approve that as well. This is the actual model round trip and how a developer would normally be engaging with the terminal-based coding agent. Both tests ran and passed. We could see the whole execution process of dcode. Now I want to run the test suite myself to verify the results. So first</p>
<p>let&#x27;s exit dcode and go back to our terminal. Here let&#x27;s run the same Python unit test command and there we go. We ran both our tests and both of them passed, which means that the new code that dcode added has the code we need in order to pass. And just to verify the code itself, we can now see the subtraction function in that file. This is a tiny example, but it proves the workflow. The agent can understand the workspace, make a code change, validate it, and summarize</p>
<p>what happened. The other important part is the environment around the agent. This is not just a coding agent running directly on my laptop. NemoClaw gives us a governed OpenShell sandbox around the dcode runtime. So let&#x27;s explain this further. First I want to exit out of my terminal and back to my running terminal. And first the command that I&#x27;d like to show is NemoClaw dcode demo policy explain.</p>
<p>To policy explain, we can inspect the policy context for this sandbox. It shows us things like the active presets, approval and remediation behavior, and support boundaries. And the next command, policy list, which I&#x27;ve shown here, can show us which policy presets are configured, which we took care of when we did the onboarding process. Finally, with logs, (typing)</p>
<p>(typing) Logs, tail 80, just want to see the last 80. And with logs, teams get a more auditable environment for running coding agents. To summarize, that is dcode running inside a NemoClaw OpenShell Sandbox with Baseten inference. Developers get a familiar terminal coding agent while teams get a governed, auditable environment around it. Thank you.</p>

</details>
