---
title: "Run Claude Code with Ollama for 99% Cheaper AI"
channel: "Better Stack"
video_id: LPDWUWP9SCk
url: https://www.youtube.com/watch?v=LPDWUWP9SCk
published: 2026-07-16T11:00:34+00:00
generated: 2026-07-16T14:18:17+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/LPDWUWP9SCk/hqdefault.jpg
---
# Run Claude Code with Ollama for 99% Cheaper AI

[![Run Claude Code with Ollama for 99% Cheaper AI](https://i.ytimg.com/vi/LPDWUWP9SCk/hqdefault.jpg)](https://www.youtube.com/watch?v=LPDWUWP9SCk)

[Watch on YouTube](https://www.youtube.com/watch?v=LPDWUWP9SCk) · **Better Stack** · 2026-07-16

## TL;DR
Ollama is a popular headless LLM server that lets you run open-source models through tools like Claude Code by simply changing environment variables, unlocking access to hundreds of models instead of just a few. The video demonstrates how to configure Claude Code to use local models like Gemma, compares Ollama to alternatives like vLLM and LM Studio, and highlights performance considerations and Docker deployment options.

## Key Takeaways
- Ollama has over 176,000 GitHub stars and acts as a headless LLM server compatible with tools like Claude Code, CodeX, and Open Claw.
- You can point Claude Code at an Ollama server by changing the base URL and auth token environment variables, then continue using Claude Code exactly as before — but with open-source models.
- Popular available models include GLM, DeepSeek, Gemma, Qwen, and MiniMax, accessible via `ollama.com/search`.
- Ollama's CLI lets you launch agent harnesses (like Claude Code) directly, or you can chat to models without any third-party tool.
- Local model performance depends heavily on available VRAM: less than 24 GB yields 4K context, 28–48 GB yields 32K, and 48+ GB yields 256K context.
- Ollama ported to Apple's MLX framework in March, improving time-to-first-token and generation speed on Apple Silicon by leveraging unified memory and GPU neural accelerators.
- Ollama can run inside Docker with CPU-only or Nvidia/AMD GPU support, and you can curl requests directly to its API.
- vLLM is better suited for hosted server deployments with higher throughput, while Ollama is more oriented toward local CLI workflows.
- LM Studio is a close competitor with a GUI, though Ollama also offers an official GUI option.

## Detailed Breakdown

### What Is Ollama and Why It Matters [00:00](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=0s)
Ollama is introduced as a headless LLM server with over 176,000 GitHub stars. It lets you run open models through any app or agent — including Claude Code, CodeX, and Open Claw. You can point your existing tools at an Ollama server, which manages local models or routes traffic to hosted models. In Claude Code's case, you simply change the base URL environment variable to point to your Ollama server, and everything works the same — but you unlock access to hundreds of models instead of just four.

### Available Models and the Big Unlock [00:31](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=31s)
The video highlights models like GLM, DeepSeek, Gemma, and Qwen as examples of what becomes available. The core value proposition is that you can keep using all the tools you already like, in exactly the same way, but now with access to virtually any model you can think of. The host notes they'll test Ollama against competitors like vLLM and LM Studio.

### Launching via the Ollama CLI and Environment Variables [01:03](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=63s)
The Ollama CLI offers options to launch other CLI tools like Claude Code or OpenCode, then select your preferred model. The demo shows OpenCode running Gemma 4 via Ollama. Alternatively, you don't need to go through the Ollama CLI at all — with Claude Code, you can just set environment variables (base URL and auth token) and run Claude Code directly, pointing at whichever model you like.

### Running Models Directly and Entering the Harness [01:35](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=95s)
Ollama also lets you run models directly — for example, running Gemma 4 (a multimodal model) and asking it to identify contents of an image. You can even enter Ollama's own harness to chat with models directly, no third-party tool required. The host demonstrates typing `ollama` in the terminal to see a menu of agents/harnesses, then selects Claude Code with Gemma 4 as the default model.

### Demo: Claude Code Running Gemma 4 [02:05](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=125s)
Inside Claude Code, the interface shows Gemma 4 at high effort. Although it says "API usage billing," because it's a local model it costs nothing. The host types "Hello," and the model responds, "Hello, I'm Claude Code, your assistant for all things software engineering." This demonstrates that Claude Code still thinks it's Claude Code, but is actually running a local open-source model behind the scenes.

### Browsing Available Models [02:35](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=155s)
The host visits `ollama.com/search`, showing many available models including Qwen 3.6, MiniMax, and the DeepSeek family. Running a new model is as simple as typing a command like `ollama run qwen 3.6`, which downloads the model if it isn't already available, then runs it locally.

### Image Detection Demo [03:07](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=187s)
The host demonstrates multimodal capability by running `ollama run gemma 4` with a prompt asking "What's inside this image?" pointed at an image in the downloads folder. The model quickly responds correctly, identifying a tabby cat lying down. The host confirms the analysis is accurate by showing the source image.

### VRAM, Context Windows, and macOS Performance [03:38](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=218s)
Available memory and system performance matter significantly for local models. Less than 24 GB VRAM gives 4K context; 28–48 GB gives 32K context; 48+ GB gives 256K context. In March, Ollama ported to MLX for Apple Silicon, Apple's machine learning framework, allowing models to use unified memory and GPU neural accelerators for faster time-to-first-token and generation speed.

### Docker Deployment and API [04:10](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=250s)
Ollama can also run inside Docker, enabling self-hosted services that rely on local models. The docs cover CPU-only, Nvidia GPU, and AMD GPU setups. You can launch models inside Docker and curl requests directly to the API, which includes several other callable endpoints.

### Comparison with vLLM and LM Studio [04:42](https://www.youtube.com/watch?v=LPDWUWP9SCk&t=282s)
vLLM is better suited for running models as services rather than as a local CLI tool, offering state-of-the-art serving throughput, efficient memory management, and quantization — making it significantly faster for server deployments. LM Studio is closer to Ollama in local workflow focus and includes a beautiful GUI, though Ollama has its own official GUI as well. Other tools in the space include Everything LLM. The host closes as Warren from Better Stack.

## Notable Quotes
- "You can carry on using all the tools you like in exactly the same way, but now you've unlocked access to every model you can think of."
- "It says API usage billing, but because this is actually a local model, it won't cost us anything at all."
- "It's still thinks that it's Claude Code, except it's still running the Gemma 4 model."
- "If you're running a hosted service, then vLLM may be the better choice."

## People, Tools & References Mentioned
- **Ollama** — headless LLM server (176,000+ GitHub stars)
- **Claude Code** — Anthropic's coding agent, repointed to Ollama
- **CodeX** — mentioned as compatible tool
- **Open Claw** — mentioned as compatible tool
- **OpenCode** — CLI tool launched via Ollama
- **Models mentioned:** GLM, DeepSeek, Gemma 4, Qwen 3.6, MiniMax
- **vLLM** — server-focused model serving alternative
- **LM Studio** — local model tool with GUI
- **Everything LLM** — another tool in the space
- **MLX** — Apple's machine learning framework, ported to in March
- **Docker** — containerized deployment option for Ollama
- **ollama.com/search** — model browser
- **Warren** — host, from Better Stack

## Who Should Watch
Developers and AI enthusiasts who want to run open-source models through familiar tools like Claude Code without paying API costs, or anyone comparing local LLM serving options like Ollama, vLLM, and LM Studio.


<details class="transcript">
<summary>Full transcript</summary>

<p>A Lama is a headless LM server with over 176,000 stars on GitHub that lets you run open models through any app or agent. That includes Claude Code, CodeX, and even open claw. You can point your tools at a Lama, which even manages local models, or route your traffic to hosted models. In Claude Code, for example, you can just change the base URL environment variable to point to your alarm a server. Now, everything works exactly the same as before, but you&#x27;ve unlocked access to hundreds of models instead of four. Models like GLM, Deep Seek, and</p>
<p>four. Models like GLM, Deep Seek, and even local models like Gemma and Gwen are all available. This is a huge unlock because you can carry on using all the tools you like in exactly the same way, but now you&#x27;ve unlocked access to every model you can think of. Today, we&#x27;ll test out a Lama. We&#x27;ll try running open models through Claude Code and see if it&#x27;s worth using over other competitors like V L L M and L M Studio. When we launch the alarm a CLI directly, it gives us options to launch other CLI tools like Claude Code or open code,</p>
<p>tools like Claude Code or open code, then being able to select our preferred model. Now, I&#x27;m inside open code, but I&#x27;m running Gemma 4 via a Lama. And now I can type something like are you subscribed to Better Stack? And if the answer&#x27;s no, then why not subscribe below this video? We don&#x27;t even need to go via the alarm a CLI at all. With Claude Code, for example, you can just change the environment variables to points to a Lama, changing the base URL and off tokens. And that now you can just run Claude Code directly pointing at whichever model you like. The result is now I&#x27;m inside Claude Code. I can use it exactly as I did before, but now I&#x27;m</p>
<p>it exactly as I did before, but now I&#x27;m running it with an open-source model. You can even run models directly with a Lama like running Gemma 4, which is a multi-model. I can ask it questions like to identify what is inside an image. And you can even enter a Lama&#x27;s harness directly to chat to models like Gemma, so you don&#x27;t need any third-party tool whatsoever. Okay, so we&#x27;re in the terminal here, and I&#x27;ll just type in a Lama to enter the CLI. And you can see here we&#x27;ve got a bunch of options of different agents or harnesses that we could enter. We could just chat to it directly, but in this case I&#x27;m just going to enter Claude Code. And you can</p>
<p>going to enter Claude Code. And you can see also that the default model, which I&#x27;ve already downloaded, is Gemma 4. So now we&#x27;re inside Claude Code, and you can see we&#x27;re on Gemma 4 with high effort. It says API usage billing, but because this is actually a local model, it won&#x27;t cost us anything at all. So we can type in a message like, &quot;Hello.&quot; So once the model replies, you can still see that it&#x27;s still thinks that it&#x27;s Claude Code, except it&#x27;s still running the Gemma 4 model. So we get response, &quot;Hello, I&#x27;m Claude Code, your assistant for all things software engineering.&quot; So this means you can now just carry on using</p>
<p>means you can now just carry on using Claude Code exactly as you did before, but you&#x27;ve tricked it in a way because instead of using Anthropic&#x27;s models, you&#x27;re actually using a local and open-source model. Now there are tons of other models available. You can see here at ollama.com/search, we&#x27;ve got the options of many, many models, including things like Qwen 3.6. We&#x27;ve got Mini Max. I&#x27;m sure we&#x27;ve got Yeah, the Deep Seek family is here as well. So basically any popular model that you can think of is going to be available. And to run this we can just type in a command like Ollama run Qwen</p>
<p>type in a command like Ollama run Qwen 3.6, and then that will, if the model&#x27;s not downloaded, start to download that model. So you&#x27;d have to wait a while for that to download, but once it&#x27;s available, you can then run it on your machine. Now let&#x27;s just check out that image detection script. So I can say Ollama run Gemma 4, and then inside quotes we say, &quot;What&#x27;s inside this image?&quot; and then just point it to an image that just happens to be in my downloads folder. And then straight away, very quickly actually, we get a response, and it&#x27;s analyzed this, and it says that there&#x27;s a cat in the image, it&#x27;s a tabby cat, the pose and action, the cat is lying down. All of this is true. And this is the</p>
<p>All of this is true. And this is the image that it did the detection against. Now your available memory and system performance really matters when running local models. If you&#x27;ve got less than 24 GB of VRAM, you&#x27;ll just get 4K of context. 28 to 48 GB of VRAM gets you 32 GB of context. and more than 48GB VRAM gets you 256 kind of context. Recently, Ollama also made huge updates when running on Mac OS. Back in March, Ollama ported over to MLX for Apple Silicon, which is Apple&#x27;s machine learning framework. This allows models to take full advantage of your unified memory</p>
<p>full advantage of your unified memory and allows Ollama to leverage GPU neural accelerators to accelerate both time to first token and generation speed. Basically, it&#x27;s faster. Aside from your local machine, Ollama can also run inside Docker so you can run your own services which rely on local models. The docs include a full guide on using Ollama inside a container either using CPU only or with Nvidia and AMD GPUs. Then you can launch the model inside Docker and even curl requests directly to it. The API reference also includes several other endpoints you can call.</p>
<p>several other endpoints you can call. Now, comparing Ollama to other tools, vLLM seems far more suited to running models as services rather than a local CLI tool and is significantly faster for server deployments due to a whole host of performance improvements like state-of-the-art serving throughput, efficient memory management, and quantization. So, if you&#x27;re running a hosted service, then vLLM may be the better choice. LM Studio is much closer to Ollama in terms of local workflows and also comes with a beautiful GUI. However, I would mention that Ollama does have its own official GUI if that&#x27;s</p>
<p>does have its own official GUI if that&#x27;s something you&#x27;re interested in. There are, of course, tons of other tools in this space like Everything LLM which we&#x27;ve covered an entire video on here. Otherwise, I hope you found this useful. I&#x27;ve been Warren from Best Stack. Thank you for watching and I&#x27;ll see you next time.</p>

</details>
