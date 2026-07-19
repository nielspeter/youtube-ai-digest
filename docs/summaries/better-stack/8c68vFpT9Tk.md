---
title: "Google Just Made TensorFlow.js Obsolete (LiteRT.js)"
channel: "Better Stack"
video_id: 8c68vFpT9Tk
url: https://www.youtube.com/watch?v=8c68vFpT9Tk
published: 2026-07-17T21:38:54+00:00
generated: 2026-07-17T23:04:36+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/8c68vFpT9Tk/hqdefault.jpg
---
# Google Just Made TensorFlow.js Obsolete (LiteRT.js)

[![Google Just Made TensorFlow.js Obsolete (LiteRT.js)](https://i.ytimg.com/vi/8c68vFpT9Tk/hqdefault.jpg)](https://www.youtube.com/watch?v=8c68vFpT9Tk)

[Watch on YouTube](https://www.youtube.com/watch?v=8c68vFpT9Tk) · **Better Stack** · 2026-07-17

## TL;DR
Google has released LiteRT.js, a WebAssembly-based JavaScript binding for its on-device LiteRT inference runtime that brings near-native machine learning performance to the browser, effectively superseding TensorFlow.js. The video explains its architecture, benchmarks, and compatibility before demonstrating it with a real-time 3D motion capture app running entirely client-side.

## Key Takeaways
- LiteRT.js is Google's new JavaScript binding for its LiteRT on-device inference runtime, delivered via WebAssembly instead of JavaScript-based kernels.
- It effectively replaces TensorFlow.js, whose JS kernels bottlenecked CPU/GPU utilization; LiteRT.js ships the same native runtime used on Android/iOS, compiled to WASM.
- It offers three backend tiers: XNNPACK for CPU (multi-threaded, relaxed SIMD), ML Drift over WebGPU for GPUs, and experimental WebNN for NPUs.
- Google's benchmarks (2024 M4 MacBook Pro) claim roughly 3× faster inference than other web runtimes on CPU/GPU, and 5×–60× speedups for GPU/NPU workloads like object tracking and audio transcription.
- Existing TFLite models run directly; PyTorch models can be converted via LiteRT Torch, and an AI Edge Quantizer shrinks models without rewrites.
- Google demos include real-time YOLO object detection, depth estimation with Depth Anything, and image upscaling with Real-ESRGAN—all client-side.
- An upcoming LiteRT LM.js will bring local LLM inference to the browser.
- The presenter built a real-time 3D motion capture app using BlazePose (33 landmarks) and Three.js, running offline in the browser.
- CPU ran ~38 FPS at 23.3 ms inference; WebGPU jumped to ~120 FPS at 8.4 ms—roughly a 3× frame-rate gain and 2.8× latency drop, aligning with Google's modest-end claims.
- Pose animations can be exported as JSON or Biovision (.bvh) motion capture files for use in tools like Blender.

## Detailed Breakdown
### Introduction [00:00](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=0s)
The video opens by announcing Google's release of LiteRT.js, a runtime library for running ML/AI models in the browser at near-native speeds. The host promises a hands-on test building a real-time 3D motion capture application that runs entirely client-side.

### What is LiteRT.js? [00:31](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=31s)
LiteRT.js is a JavaScript binding for Google's LiteRT on-device inference runtime, which has powered Android, iOS, and embedded inference for years. It is brought into the browser via WebAssembly through the `lirtrt.js-core` NPM package, delivering the actual native runtime rather than a web abstraction.

### Why it beats TensorFlow.js [01:02](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=62s)
TensorFlow.js has existed for years but relies on JavaScript-based kernels that can't fully exploit CPU or GPU hardware. LiteRT.js instead compiles the same native runtime used on mobile devices to WASM and exposes it to JS, providing a truly optimized engine rather than a JavaScript-flavored layer.

### Backend architecture (CPU, GPU, NPU) [01:33](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=93s)
LiteRT.js supports three tiers. CPU uses XNNPACK with multi-threading and relaxed SIMD as a universal fallback. GPU uses ML Drift over WebGPU for native GPU kernels without JS shader orchestration. NPU targets WebNN (experimental in Chrome/Edge) for power-efficient inference on dedicated neural hardware.

### Benchmarks and compatibility [02:34](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=154s)
Google's benchmarks on a 2024 M4 MacBook Pro show ~3× faster inference than other web runtimes on CPU/GPU for vision/audio models, and 5×–60× speedups for GPU/NPU workloads. Results vary by hardware, thermals, and drivers. Existing TFLite files run directly; PyTorch models convert via LiteRT Torch; the AI Edge Quantizer shrinks models without full rewrites, easing migration from TensorFlow.js.

### Demos and what's next [04:06](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=246s)
Google showcases real-time YOLO object detection, monocular depth estimation with Depth Anything (webcam to 3D point cloud), and image upscaling with Real-ESRGAN—all client-side. They've also announced LiteRT LM.js for running full language models locally in the browser, expanding beyond computer vision.

### Live demo: 3D motion capture app [05:10](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=310s)
The host built a real-time pose-estimation motion capture app using Cloud Code and the Fable 5 model. It uses LiteRT.js with the BlazePose model (33 body landmarks) to drive a 3D character via Three.js, entirely offline with no backend. The repo is linked in the description.

### Performance comparison: CPU vs WebGPU [05:44](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=344s)
On CPU, the app averaged ~38 FPS with 23.3 ms inference, with noticeable pose-estimation lag. Switching to WebGPU yielded ~120 FPS at 8.4 ms inference—a ~3× frame-rate jump and ~2.8× latency drop, matching the modest end of Google's published numbers. BlazePose is a small model, limiting the GPU's headroom, but moving tensor math to WebGPU still cut latency significantly.

### Export and closing thoughts [06:16](https://www.youtube.com/watch?v=8c68vFpT9Tk&t=376s)
The app can record pose captures and export them as JSON or Biovision motion capture (.bvh) files for retargeting in Blender. The host notes the animation is rough but emphasizes the app was built in just 10 minutes. He closes praising WebAssembly's impact, noting LiteRT.js proves JavaScript can be a bottleneck for near-native performance, and expresses excitement for the upcoming LiteRT LM.js.

## Notable Quotes
- "You're not getting a web-flavored abstraction layer anymore, you're actually getting a truly optimized runtime engine."
- "This new LiteRT.js library truly proves that sometimes JavaScript can be a real bottleneck for getting to those near native performance speeds."
- "Moving the tensor math off the CPU and on the WebGPU cuts the latency enough that the lag is significantly lower."

## People, Tools & References Mentioned
- **LiteRT.js** / **LiteRT** — Google's on-device inference runtime and its JS binding
- **TensorFlow.js** — Google's prior browser ML library
- **WebAssembly (WASM)** — delivery mechanism for the native runtime
- **XNNPACK** — Google's optimized CPU kernel library
- **ML Drift** — GPU kernel layer used over WebGPU
- **WebGPU** — GPU backend API
- **WebNN** — experimental NPU-targeting web API (Chrome/Edge)
- **TFLite** — existing model format supported directly
- **PyTorch** / **LiteRT Torch** — conversion path to .tflite
- **AI Edge Quantizer** — tool for shrinking model sizes
- **YOLO** — object detection model
- **Depth Anything** — monocular depth estimation library
- **Real-ESRGAN** — image upscaling library
- **LiteRT LM.js** — upcoming local LLM inference runtime
- **BlazePose** — pose estimation model with 33 body landmarks
- **Three.js** — 3D rendering library
- **Blender** — 3D software for retargeting motion capture
- **Biovision motion capture (.bvh)** — motion capture file format
- **Cloud Code** — environment used for live coding the demo
- **Fable 5** — model used in the demo build
- **Andres (Better Stack)** — video host

## Who Should Watch
Web developers and ML practitioners interested in running inference client-side in the browser, especially those who have hit performance limits with TensorFlow.js or want to deploy existing TFLite/PyTorch models to the web without a backend.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=0s">00:00</a></span> Google just released a new runtime library that lets you run machine learning and AI models inside the browser at near native speeds. It&#x27;s called light rt.js and it&#x27;s super impressive. So, in this video, we&#x27;ll take a look at light rt.js, see how it works, and we&#x27;re going to test it out by building a real-time 3D motion capture application running entirely in the browser. It&#x27;s going to be a lot of fun, so let&#x27;s dive into it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=31s">00:31</a></span> So, what exactly is light rt.js? Well, it&#x27;s a JavaScript binding for light RT, their on-device inference runtime, that&#x27;s been running models on Android, iOS, and embedded hardware for years now. But, light rt.js brings the same runtime into the browser via WebAssembly using the light rt.js core NPM package. And, here&#x27;s what makes light rt.js different. So, Google already has a browser machine learning library. It&#x27;s called tensorflow.js,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=62s">01:02</a></span> called tensorflow.js, and it&#x27;s been around for years. But, tensorflow.js runs on JavaScript-based kernels, and that is a big bottleneck. You see, JavaScript kernels can&#x27;t fully exploit CPU or GPU the way a native runtime can. So, tensorflow.js has always lagged behind native app performance. But, light rt.js uses WebAssembly, and it ships with its own optimized kernel. So, the same native runtime that powers Android and iOS inference is compiled to WASM and then</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=93s">01:33</a></span> inference is compiled to WASM and then exposed to JS. So, you&#x27;re not getting a web-flavored abstraction layer anymore, you&#x27;re actually getting a truly optimized runtime engine. And, this also shows up in their back-end architecture. Light rt.js has three different tiers that allows it to perform well on CPUs, GPUs, and even NPUs. So, on the CPU side, it uses XNNPACK, Google&#x27;s optimized CPU kernel library, which is multi-threaded with relaxed SIMD</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=123s">02:03</a></span> multi-threaded with relaxed SIMD support. And this is your universal fallback that will run anywhere, no GPU required. But for GPUs, it uses ML Drift over WebGPU, and this is where the real performance lives. It utilizes native GPU kernels, so things like shaders are no longer rendered using some sort of JavaScript orchestration. And for MPUs, it has WebNN, which is still experimental in Chrome and Edge, and it targets dedicated neural processing hardware for power efficient inference.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=154s">02:34</a></span> hardware for power efficient inference. And according to Google&#x27;s own benchmarks, which they conducted on a 2024 MacBook Pro with M4 silicon, it appears to have a three times faster inference than other web runtimes on CPU and GPU across vision and audio models. And when running workloads like object tracking, audio transcription, or image manipulation on the GPU or MPU, rather than on the CPU, we get performance boosts that jump from five times all the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=184s">03:04</a></span> boosts that jump from five times all the way to 60 times faster results, depending on the task. And it&#x27;s worth mentioning that that is the best-case scenario, and Google also acknowledges this. So, your mileage may vary taking into consideration your specific GPU, thermal throttling, and driver quality. And there&#x27;s one more thing that really matters for this runtime. If you already have models that you use to run on PyTorch or TensorFlow, if you&#x27;ve got an existing TFLite file, light rt.js can actually run it directly. And if you&#x27;re</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=215s">03:35</a></span> actually run it directly. And if you&#x27;re on PyTorch, there&#x27;s also light rt torch, a conversion path that takes your model straight to .tflite. Plus, there&#x27;s also an AI Edge Quantizer for shrinking model sizes without a full rewrite. So, legacy workflows you&#x27;ve been using on tensorflow.js can easily be ported to the new light rt.js which is super cool. But, what can you actually do with it? Well, Google has some pretty cool demos out there which give you a sense of the range. So, you can do real-time YOLO object</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=246s">04:06</a></span> you can do real-time YOLO object detection, monocular depth estimation with the depth anything library that turns your webcam feed into a live 3D point cloud, and it can also do image upscaling with the real ESRGAN library. And all these demos are running completely client-side with no back-ends, no APIs, directly inside your browser. And they&#x27;ve already announced what&#x27;s coming next, light rt lm.js, and this is going to be for running full language models locally in the browser. So, this isn&#x27;t just for computer vision,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=278s">04:38</a></span> So, this isn&#x27;t just for computer vision, soon it will also offer local LLM inference, too. All right, that all sounds great, but I wanted to test it out on my own to see how powerful it actually is. So, for this demo, I decided to create a real motion capture application that uses your webcam for real-time pose estimation. And it also runs entirely on your browser, client-side, and offline with no strings attached. So, I live-coded this app on Cloud Code using the new Fable 5 model, and here&#x27;s the end result. And by the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=310s">05:10</a></span> and here&#x27;s the end result. And by the way, if you want to download this repo and play around with it yourself, I&#x27;ve also added the link to the project in the description below. So, here light rt.js is running through the browser using a blaze pose model with 33 body landmarks driving a 3D character in real-time using 3.js. There&#x27;s no back-end server, and everything you see is happening on this machine right now, completely offline. So, we can see here that on the CPU, we are averaging around 38 FPS with an inference of 23.3</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=344s">05:44</a></span> 38 FPS with an inference of 23.3 milliseconds. And we can also see that the pose estimation is lagging behind a bit. But now, if we switch to the WebGPU version, we can see that we are now getting a solid 120 frames per second with an 8.4 ms inference, and the pose estimation is also a bit faster. And that&#x27;s roughly a three times jump in frame rate and a 2.8 times drop in inference time, which lines up with Google&#x27;s own numbers, though it&#x27;s on the modest end of what they published. But</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=376s">06:16</a></span> modest end of what they published. But we have to take into consideration that Blaze Pose is generally a small model, so there&#x27;s less raw compute for the GPU to chew through. But even with that, moving the tensor math off the CPU and on the WebGPU cuts the latency enough that the lag is significantly lower. And I also added a feature where you can record your pose capture animation and export it as a JSON or as a Biovision motion capture file, and then open that in something like Blender and retarget</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=406s">06:46</a></span> in something like Blender and retarget that animation to your own custom character. And as you can see here, it&#x27;s not perfect. The movements are not very detailed or refined, so this is still very much a work in progress, but it&#x27;s super cool that I was able to get this initial version working in just 10 minutes using the new light rt.js. So there you have it, folks. That is light rt.js in a nutshell. It&#x27;s honestly amazing to see how far WebAssembly has pushed the capabilities of running complex applications on the browser. And</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=436s">07:16</a></span> complex applications on the browser. And this new light rt.js library truly proves that sometimes JavaScript can be a real bottleneck for getting to those near native performance speeds. So I&#x27;m super impressed with this library, and I can&#x27;t wait to try out light rtlm.js when it finally ships later this year. But what do you think about light rt.js? Have you tried it? Will you use it? Let us know in the comments down below. And folks, if you like these types of technical breakdowns, please let me know by smashing that like button underneath the video and also don&#x27;t forget to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=8c68vFpT9Tk&amp;t=467s">07:47</a></span> the video and also don&#x27;t forget to subscribe to our channel. This has been Andres from Better Stack and I will see you in the next videos.</p>

</details>
