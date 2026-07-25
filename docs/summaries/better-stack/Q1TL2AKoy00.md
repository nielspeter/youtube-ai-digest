---
title: "Wails: Golang's Bet On Desktop Grade Apps To Beat Electron"
channel: "Better Stack"
video_id: Q1TL2AKoy00
url: https://www.youtube.com/watch?v=Q1TL2AKoy00
published: 2026-07-25T08:00:37+00:00
generated: 2026-07-25T11:25:23+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/Q1TL2AKoy00/hqdefault.jpg
---
# Wails: Golang's Bet On Desktop Grade Apps To Beat Electron

[![Wails: Golang's Bet On Desktop Grade Apps To Beat Electron](https://i.ytimg.com/vi/Q1TL2AKoy00/hqdefault.jpg)](https://www.youtube.com/watch?v=Q1TL2AKoy00)

[Watch on YouTube](https://www.youtube.com/watch?v=Q1TL2AKoy00) · **Better Stack** · 2026-07-25

## TL;DR
Wails is a cross-platform desktop app framework that pairs a Go backend with a web-technology frontend rendered via each platform's native web view, much like Tauri but with Go instead of Rust. The video builds a screen-recording app in Wails and compares it against Electron and Tauri on bundle size, startup time, runtime performance, and developer experience—finding Wails competitive on most metrics but noting that Go's smaller native ecosystem can force you to write Objective-C by hand.

## Key Takeaways
- Wails uses a Go backend and a web frontend rendered through the OS's native web view, avoiding the bundled Chromium that makes Electron apps large.
- Architecture is very similar to Tauri; the main difference is Go vs. Rust on the backend.
- Wails auto-generates TypeScript bindings from Go functions, giving you type-safe frontend calls and live reload on backend changes.
- Bundle sizes: Wails ~52 MB, Tauri ~57 MB, Electron ~324 MB—Wails and Tauri are dramatically smaller.
- Startup times are close across all three; Electron is slightly faster on cold starts, while Wails and Tauri win on warm starts.
- Runtime performance during screen recording is better for Wails and Tauri than Electron because they use native capture APIs instead of recording from the web view.
- Developer experience in Wails is generally pleasant, but Go lacks mature wrappers for macOS frameworks like ScreenCaptureKit.
- To access macOS ScreenCaptureKit in Wails, the presenter had to write ~450 lines of Objective-C via cgo, whereas Tauri could use an existing Rust crate.
- Choice between Wails and Tauri largely comes down to language preference (Go vs. Rust) and ecosystem maturity for your specific use case.
- Using native web views (as Wails and Tauri do) can introduce minor platform rendering differences compared with Electron's bundled Chromium.

## Detailed Breakdown

### What Is Wails and How It Compares [00:00](https://www.youtube.com/watch?v=Q1TL2AKoy00&t=0s)
Wails is introduced as a cross-platform technology for building desktop-grade apps in Go, a frequently requested topic on the channel. It works similarly to Tauri but uses Go instead of Rust for the backend while still using web technologies for the frontend. Unlike Electron, Wails does not embed a browser; it reuses each platform's native rendering engine, which should result in a smaller bundle size. The video plans to build a desktop screen recorder and compare file size, performance, and developer experience across Wails, Tauri, and Electron.

### Demo: The Screen Recording App [01:05](https://www.youtube.com/watch?v=Q1TL2AKoy00&t=65s)
The presenter demonstrates a screen recording tool built with Wails (and previously built in Electron and Tauri). The app lets you select a screen, record it (the app window itself doesn't appear in the recording), stop, preview, optionally trim, and export to MP4. The project structure mirrors a typical Electron app: frontend files live in a `frontend` folder, and the entry point is a Go file called `main.go`, where you declare the window title, dimensions, background color, and platform-specific settings.

### Frontend and Auto-Generated API Bindings [02:07](https://www.youtube.com/watch?v=Q1TL2AKoy00&t=127s)
The frontend is standard React code (e.g., `app.tsx`) that calls APIs defined on the Go side. Wails automatically generates a TypeScript file (`wailsjs/go/main/app.js`) containing functions like `exportVideo`, `listSources`, and `requestScreenAccess`. The generated file even includes a Welsh comment at the top because the creator of Wails is Welsh. When you modify a Go function (e.g., comment out `listSources`), `wails dev` automatically regenerates the TypeScript definitions and reloads the app, giving you live, type-safe bindings between frontend and backend.

### Bundle Size Comparison [03:09](https://www.youtube.com/watch?v=Q1TL2AKoy00&t=189s)
Wails comes in at 52 MB, Tauri at 57 MB, and Electron at 324 MB. Wails and Tauri are noticeably smaller because neither bundles Chromium. However, relying on native web views means you may see minor platform rendering differences, though this is less of an issue today. Wails and Tauri produce similar artifacts because they are architected similarly despite using different backend languages.

### Startup Time Comparison [04:12](https://www.youtube.com/watch?v=Q1TL2AKoy00&t=252s)
Each app was launched 10 times and averaged. Warm starts: Wails 385 ms, Tauri 410 ms, Electron 350 ms. Cold starts (cache purged each time): Wails 2337 ms, Tauri 249 ms (likely a transcription quirk), Electron 1890 ms. Electron is slightly faster on cold starts, but all three are in a comparable range.

### Runtime Performance [04:44](https://www.youtube.com/watch?v=Q1TL2AKoy00&t=284s)
Runtime performance during screen recording is better in Wails and Tauri than in Electron. This is because Wails and Tauri use macOS's native ScreenCaptureKit, so no data travels over the JavaScript-to-native bridge. Electron, by default, records from the web view and passes data to the backend, adding overhead. The presenter notes you could theoretically write custom C code in Electron to use native capture, but that isn't the default approach and isn't what's being compared.

### Developer Experience and the Objective-C Problem [05:16](https://www.youtube.com/watch?v=Q1TL2AKoy00&t=316s)
The presenter enjoyed building with Wails overall, but screen capture was harder than in Tauri. Tauri has a mature Rust crate (`ScreenCaptureKit`) that wraps Apple's framework in pure Rust. Go has no equivalent, so the presenter used cgo—Go's built-in mechanism for compiling C code—to write ~450 lines of Objective-C in a `.m` file, link against Apple's frameworks, and expose plain C functions to Go. This means you end up writing real Objective-C and owning all that code, whereas the Tauri version needed none. The presenter leans slightly toward Tauri due to Rust's stronger ecosystem for native framework wrappers, but emphasizes the choice is largely about language preference. If you pick Wails, be prepared to write native code where the Go ecosystem is thin.

## Notable Quotes
- "Unlike Electron, Wails does not embed a browser. Instead, it reuses the native rendering engine for each platform much like Tauri does."
- "Anytime a change happens inside the Go file, it automatically rerenders the TypeScript definitions."
- "Wails comes in at 52 megabytes, Tauri at 57 megabytes, and Electron at no surprise 324 megabytes."
- "I had to write Objective C code to access capture kit. Whereas with Tauri, you could stay completely in Rust."
- "It does come down to preference. If you like developing in Go then Wails is a really decent option and if you like Rust then just choose Tauri."

## People, Tools & References Mentioned
- **Wails** — Go-based cross-platform desktop app framework
- **Tauri** — Rust-based counterpart to Wails
- **Electron** — JavaScript/Chromium-based desktop framework
- **Go (Golang)** — backend language used by Wails
- **Rust** — backend language used by Tauri
- **cgo** — Go's built-in mechanism for compiling and linking C code
- **ScreenCaptureKit** — Apple's native screen capture framework; also the name of a Rust crate
- **Objective-C** — used to write native macOS capture code in the Wails app
- **React / TypeScript** — frontend stack used in the demo app
- **Warren (presenter)** — from Better Stack
- **Milo** — referenced at the end as having vetoed more videos for the week
- **Deno Desktop / Electro Bun** — mentioned as subjects of a prior comparison video

## Who Should Watch
Developers evaluating lightweight alternatives to Electron for cross-platform desktop apps, especially those who already know or are curious about Go. It's also useful for anyone weighing Wails against Tauri and wanting concrete benchmarks plus a real-world look at where Go's native ecosystem falls short.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=0s">00:00</a></span> Wales is a cross-platform technology that lets you build desktop grade apps in Go. This has been requested a ton of times on the channel after doing a bunch of desktop comparison videos. So, today I&#x27;m going to take you through using Wales to build desktop grade apps and compare it to using frameworks like Electron and Tori. We&#x27;re going to go through the build of a desktop video recorder, which we&#x27;ve done in other videos, and compare things like file size, performance, and developer experience. And Wales is actually completely new to me, so we&#x27;re going to be learning together on this one.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=33s">00:33</a></span> So Wales works very much in the same way as Tori, but the back end is in Go rather than Rust. You still build a front end in a web view using web technologies then called native APIs which are managed by Golang. This means you can compile an application that&#x27;s compatible with both Mac and Windows. But unlike Electron, Wales does not embed a browser. Instead, it reuses the native rendering engine for each platform much like Tori does. So, the bundle size technically should be a lot smaller, but we&#x27;re going to see that later on when we do the comparison. And if you enjoy content like this, guys,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=65s">01:05</a></span> if you enjoy content like this, guys, then subscribe for more. So, this is the screen recording tool that I&#x27;ve developed with Wales, and I&#x27;ve also done the same thing in Electron and Tori. We&#x27;ll select the screen that we want to record. Press record. You can move the mouse around. The actual desktop app won&#x27;t appear in the record itself. I&#x27;ll press stop. Then, you can see the screen I&#x27;ve just recorded. I could cut this up if I wanted to. and then just click export to MP4 to just save the video directly to my machine. So, if we look inside the build for this, you&#x27;ll see that it&#x27;s a very similar setup to what you would expect on Electron. We have all the front-end files in a front-end</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=96s">01:36</a></span> all the front-end files in a front-end folder. And then we have the entry file, and in this case, it&#x27;s a Go file called main.go. And inside here, we&#x27;ve got a main function. Again, you would expect to see a similar thing inside Electron. And we can do things like declare the title, the width and height, set things like the background color, and then set things for max specifically. So if you do want differences between Mac and Windows, that&#x27;s completely possible. Now if we look inside the front end here inside source, you would actually see all of the React code. So if we look inside app.tsx, this is just standard</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=127s">02:07</a></span> inside app.tsx, this is just standard react code except from we&#x27;re calling APIs that are defined on the go side. So if we look at this import here, API, and see its usages across the file, you can see we&#x27;re doing API.onrecording on recording finished on recording failed start recording and that API is automatically generated by Wales. So if we look inside the API itself you can see that all of the core functions are coming from this file here wales.js/go/main/ app. Now if we look inside here you can see that this file is automatically generated and we&#x27;ve got Welsh at the top</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=158s">02:38</a></span> generated and we&#x27;ve got Welsh at the top and English and that&#x27;s because believe it or not the creator of Wales is Welsh. So, we&#x27;ve got all these functions here like export video, list sources, request screen access, all the things that you would need for a screen recording tool. So, then if we jump over to the Go side here in app.go and then we comment out list sources and then save that file, you&#x27;ll see that suddenly we get an error inside api.ts because now list sources does not exist. And this is because we&#x27;re running wales.dev. So, anytime a change happens inside the Go file, it automatically rerenders the TypeScript</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=189s">03:09</a></span> automatically rerenders the TypeScript definitions. So if we go back now and then comment this back in, you&#x27;ll see that now the error disappears and then the desktop app actually reloads because all of the changes from the go side, so from the back end, automatically recompile and rerender the application. Now let&#x27;s do some comparisons to see the difference between these three frameworks. First, we&#x27;ll look at bundle size. Wales comes in at 52 megabytes, Tori at 57 megabytes, and Electron at no surprise 324 megabytes. Wales and Tory are noticeably smaller here. And that&#x27;s</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=220s">03:40</a></span> are noticeably smaller here. And that&#x27;s because they do not bundle Chromium. So that&#x27;s pretty much expected. However, I would say by using each platform&#x27;s native web view, which is what Wales and Tori do, you are more likely to see some platform differences, that is much less of an issue these days, but just something to keep in mind. So basically, Tori and Wales are going to produce similar artifacts in terms of bundle size because both frameworks are architected in pretty much the same way despite using vastly different technologies under the hood. Now, let&#x27;s take a look at startup time. And as with previous videos I&#x27;ve done on desktop</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=252s">04:12</a></span> previous videos I&#x27;ve done on desktop apps, we&#x27;re going to launch each of these apps 10 times and then just take the average. Wales comes in at 385 milliseconds, Tory at 410 milliseconds, and Electron at 350 miseconds. Now, with cold starts, where we purge the cache each time, Wales gets 2337, Tori 249, and Electron comes in a little bit faster actually at 1,890. Now looking at performance and as with Tori the runtime performance when recording the screen is much better than Electron and that&#x27;s actually because of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=284s">04:44</a></span> Electron and that&#x27;s actually because of our setup where we use the native capture kit from Mac. So no data is traveling over the bridge. Whereas with Electron we record from the web view itself and then pass data to the back end which does come with a little bit of overhead. Technically you could use the native capture kit if you was to write some custom C code with Electron but this is like the default way of doing things with Electron. So that&#x27;s what we&#x27;re comparing it to today. Now let&#x27;s take a look at developer experience. And this is really where we&#x27;re going to see the biggest difference. I actually really enjoyed building with Wales. However, I would say the part around uh</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=316s">05:16</a></span> However, I would say the part around uh screen capture was not as easy as with Tori. I had to write Objective C code to access capture kit. Whereas with Tori, you could stay completely in Rust. And this is because Rust has a big ecosystem of community crates wrapping Apple&#x27;s native frameworks. So in Tori, I just pulled in a crate called Screen Capture Kit. And the whole recording API is normal Rust. Go has nothing decent for screen capture kit that I could find. But it does have something called C Go, which is Go&#x27;s built-in way for compiling C code. This means with Go, you can just</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=346s">05:46</a></span> C code. This means with Go, you can just write native C in a M file, expose it as plain C functions, and then tell Go which of Apple&#x27;s frameworks to link against. So this means you end up writing real Objective C and calling the same Apple APIs as the Rust crate, but this time you own all of the code. that actually ended up being about 450 lines of Objective C code which the Rust app just didn&#x27;t have. So overall I am leaning slightly more towards Tori. The ecosystem around Rust Crates is better from what I found. But really it does come down to preference. If you like</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=376s">06:16</a></span> come down to preference. If you like developing in Go then Wales is a really decent option and if you like Rust then just choose Tori. However, if you do pick Wales you may have to write some native code just because the ecosystem isn&#x27;t as established. Well, hopefully you enjoyed this one, guys. And you can subscribe for more content like this. And if you want to see more comparison videos of desktop frameworks, like where we compared Dino Desktop to Electro Bun, I&#x27;ve linked a video right here that you can watch. Otherwise, thanks so much for watching. I&#x27;ve been Warren from Better Stack, and I&#x27;ll see you in the next one. And unfortunately, guys, Milo said no</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=Q1TL2AKoy00&amp;t=408s">06:48</a></span> And unfortunately, guys, Milo said no more videos for the week. So, I&#x27;ll see you on Monday.</p>

</details>
