---
title: "What's The Best Electron Alternative? Let's Find Out."
channel: "Better Stack"
video_id: ktkDGQyRx3Y
url: https://www.youtube.com/watch?v=ktkDGQyRx3Y
published: 2026-07-15T18:30:03+00:00
generated: 2026-07-15T18:43:25+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/ktkDGQyRx3Y/hqdefault.jpg
---
# What's The Best Electron Alternative? Let's Find Out.

[![What's The Best Electron Alternative? Let's Find Out.](https://i.ytimg.com/vi/ktkDGQyRx3Y/hqdefault.jpg)](https://www.youtube.com/watch?v=ktkDGQyRx3Y)

[Watch on YouTube](https://www.youtube.com/watch?v=ktkDGQyRx3Y) · **Better Stack** · 2026-07-15

## TL;DR
The video compares four cross-platform desktop app frameworks—Electron (baseline), Tauri, Electro Bun, and Dino Desktop—by building the same screen recording app and measuring bundle size, startup time, memory usage, and developer experience. Tauri and Dino come out ahead on size and memory, while Electro Bun struggles with bloat and crashes; overall, Tauri is the presenter's top pick, with Electron remaining the solid choice for TypeScript teams.

## Key Takeaways
- Tauri had the smallest bundle at 57 MB, followed by Dino at 111 MB, Electron at 323 MB, and Electro Bun at 418 MB.
- Dino had the fastest startup time (242 ms), beating Electron (273 ms) and Tauri (311 ms); Electro Bun was slowest at 773 ms.
- Dino also used the least memory after launch (98 MB), with Tauri close behind (109 MB); Electro Bun used the most (208 MB).
- Tauri's memory advantage isn't as dramatic as marketing suggests—system web view processes must be counted to get the real footprint.
- Tauri records screen via native macOS Screen Capture Kit (like QuickTime), avoiding the web view bridge and improving recording performance.
- Electro Bun lacked the screen capture API in its native web view, forcing Chromium to be bundled—adding ~200 MB.
- Dino had a bug where hiding the app during recording terminated the process, requiring a workaround.
- Electro Bun unexpectedly depended on 3JS and BabylonJS, contributing to bundle bloat.
- Electron and Tauri offered the best developer experience; Dino and Electro Bun had crashes and issues.
- The presenter would choose Tauri overall, but recommends Electron for TypeScript developers who don't want Rust.

## Detailed Breakdown

### Introduction and Frameworks Compared [00:00](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=0s)
The video sets out to compare the three best Electron alternatives for cross-platform desktop apps: Tauri (Rust), Electro Bun (from the Bun team), and Dino Desktop (from Dino), with Electron as the baseline. Four criteria are used: bundle size, startup performance, runtime performance, and developer experience.

### The Test App [00:30](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=30s)
The presenter built the same screen recording tool four times—an app that records the screen, lets you trim the recording on a timeline, and exports to MP4. Video processing was chosen specifically to push the frameworks to their limits.

### App Demo [01:02](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=62s)
A brief demo shows the app: launch, pick a screen, record, stop, trim dead space on a timeline, and export to MP4. Though simple, the app exercises multiple APIs, video processing, and UI rendering, making it a fair stress test.

### Bundle Size Results [01:34](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=94s)
Electron: 323 MB. Tauri: 57 MB. Electro Bun: 418 MB. Dino: 111 MB. All bundles include FFmpeg (~45 MB). Electro Bun is largest because Chromium had to be shipped—its native web view lacked the screen capture API (`getDisplayMedia`), so Chromium was reintroduced for ~200 MB of extra bloat. Dino implemented the same JavaScript APIs without Chromium. Tauri doesn't record from the web view at all.

### Tauri's Native Recording Approach [02:36](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=156s)
Tauri records via macOS Screen Capture Kit—the same framework QuickTime uses—entirely from the Rust back end. You pass a display, codec, and file path; it writes the file directly. The web view is only for UI and never touches a frame. This also gives you mixed mic/system audio and a proper MP4 for free. FFmpeg was left in for format conversion but is technically optional.

### Startup Performance [03:07](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=187s)
A script launched each app 10 times to get the median. Electron: 273 ms. Tauri: 311 ms. Electro Bun: 773 ms. Dino: 242 ms. Dino was fastest, beating even Tauri. The assumption that Rust + system web view would start instantly was wrong—the rendering engine still needs to boot. Electro Bun is slowest because it chains three runtimes: launcher → Bun → Chromium.

### Memory Usage After Launch [03:37](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=217s)
Electron: 128 MB. Tauri: 109 MB. Electro Bun: 208 MB. Dino: 98 MB. Tauri and Dino are close; Electro Bun is roughly double the others. Tauri's runtime memory is nowhere near the "10x improvement" marketing implies—on disk it's smaller, but running memory is comparable. A caveat: Tauri's system web view processes aren't children of the app, so Activity Monitor shows ~36 MB; adding the separate processes brings it to ~109 MB.

### Screen Recording Performance [04:39](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=279s)
Tauri showed noticeably better recording performance, likely because it avoids recording in the web view and transferring data over a bridge. For near-60fps recording, Rust + Tauri is the recommended path.

### Developer Experience [05:10](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=310s)
Electron and Tauri were easiest to build with. Dino had a bug: starting a recording and hiding the app terminated the entire process (Dino assumes the app is done when no screens are visible). The workaround was to move the view off-screen instead of hiding it. Electro Bun had issues bundling Chromium for screen capture and unexpectedly depended on 3JS and BabylonJS (3D libraries), adding to bloat.

### Final Verdict [06:10](https://www.youtube.com/watch?v=ktkDGQyRx3Y&t=370s)
The presenter would personally choose Tauri. For teams that don't want Rust, Electron remains the mature, reliable option for TypeScript developers. Dino shows promise but needs more time to mature. Electro Bun was the worst overall experience for this use case.

## Notable Quotes
- "Tauri comes in at just 57 megabytes."
- "Electro Bun doesn't include that API at all. So, the only way to get access to it is to reintroduce Chromium, and that brings in an extra 200 megabytes of bloat."
- "Tauri doesn't record from the web view at all. It does it all through the back end through the native screen capture kit."
- "For Tauri, that's nowhere near the 10x improvement that the marketing implies."
- "If you really don't want to program in Rust then Electron is still the mature platform for TypeScript developers."

## People, Tools & References Mentioned
- **Frameworks:** Electron, Tauri, Electro Bun, Dino Desktop
- **Languages/Runtimes:** Rust, Bun, TypeScript
- **Libraries/Tools:** FFmpeg, 3JS, BabylonJS, Chromium
- **macOS APIs:** Screen Capture Kit, QuickTime
- **Web APIs:** Screen Capture API, `getDisplayMedia`, MediaRecorder
- **Presenter:** Warren (Better Stack)

## Who Should Watch
Developers evaluating Electron alternatives for cross-platform desktop apps—especially those building performance-sensitive or media-heavy applications—who want a practical, benchmark-based comparison to guide their framework choice.


<details class="transcript">
<summary>Full transcript</summary>

<p>Building crossplatform desktop apps used to mean reaching for Electron, but these days we&#x27;re spoiled for choice. So to clear up any confusion, today we&#x27;re comparing the three best options for building cross-platform desktop apps. We&#x27;ll look at Tori written in Rust, Electro Bun from the Bun team, Dino Desktop, the new offering from Dino. We&#x27;ll also use Electron as a baseline. And if you would like to see a different tool covered on this channel, then just let me know in the comments. We&#x27;ll be comparing four things: bundle size, startup performance, runtime performance, and developer experience.</p>
<p>performance, and developer experience. I&#x27;ve built the same app four times, a screen recording tool that lets you edit the results on a timeline and output to MP4. I&#x27;ve specifically chosen this kind of app because video processing can push these kind of tools to their limits. Now, of course, not everything comes down to performance. your team&#x27;s skill set and the kind of product you&#x27;re building will all influence the type of framework you choose. But hopefully this can give you some guidance on what to expect. So let&#x27;s just quickly jump into a demo of the application we&#x27;ve built. We start</p>
<p>of the application we&#x27;ve built. We start off by launching our app. We can choose which screen to record, then hit the record button. Now we can do a short record of the screen. Once we&#x27;re done, we can press stop. Then a window will appear with our recording on the timeline. We can then clip this up to remove dead space. Then hit export to output as an MP4. The app is actually incredibly simple, but because we&#x27;re using multiple APIs, recording and processing video, and rendering UI, this should actually be a decent test. So, the first thing that we&#x27;re going to check is the bundle size. And remember, these apps all provide identical functionality. Electron as the baseline</p>
<p>functionality. Electron as the baseline is 323 megabytes, Tori comes in at just 57 megabytes. Electro Bun is 418 megabytes. and Dino was 111 megabytes. All of them also have FFmpeg embedded for exports to MP4 and that brings 45 megabytes alone. And Electro Bun is so large because I had to ship Chromium with it. I tried really hard but I literally could not get the screen record to work with the native system web view. Specifically to record from JavaScript, you need the screen capture API and the get display media function.</p>
<p>API and the get display media function. You ask the browser for the screen, it hands you a stream. The media recorder encodes it, and that&#x27;s how Electron and Dino does it. Electro Bun doesn&#x27;t include that API at all. So, the only way to get access to it is to reintroduce Chromium, and that brings in an extra 200 megabytes of bloat. Dino&#x27;s API did implement this. So, it&#x27;s all of the same code, but with no Chromium. And that&#x27;s why Dino&#x27;s bundle size ends up being around 100 megabytes, and Electro Buns ends up being closer to 400. And Rust didn&#x27;t need any of this because Tori doesn&#x27;t record from the web view at</p>
<p>Tori doesn&#x27;t record from the web view at all. It does it all through the back end through the native screen capture kit. This is the same Mac OS framework that QuickTime uses and it&#x27;s all recorded directly from the back end. You hand it a display, a codec and a file path and it writes the file itself. The web view is only the UI. It never touches a single frame and you also get things for free that the JavaScript build has to hand roll. Screen capture kit mixes your mic and your system audio itself and it finalizes a proper MP4. I did also leave FFmpeg inside the Tory app so we could export to different formats but</p>
<p>export to different formats but technically that is actually optional. Okay, now we can launch these apps to detect the startup time and I&#x27;ve written a script that does this 10 times. So then I can take the median. Electron as a baseline was 273 milliseconds. Tory actually came in at 311 milliseconds. Electro Bun was 773 milliseconds and Dino was 242 milliseconds. And the surprise here for me was that Tori wasn&#x27;t the fastest. It&#x27;s just a hair behind Electron and then Dino actually beat everyone. The assumption would be that Rust plus the</p>
<p>assumption would be that Rust plus the system web view would mean instant starts. But since the rendering engine still has to boot either way, that&#x27;s probably what contributes to the slightly slower startup speed. Electro Bun is the outlier nearly three times Electron. It&#x27;s booting a launcher which boots bun which boots chromium. Three run times in a chain and you can really feel it. Now let&#x27;s look at memory after launch once the app is actually up and running. Electron is the baseline again and it was 128 mgby. Tori came in at 109 megabytes. Electroun at 208 mgabytes and</p>
<p>megabytes. Electroun at 208 mgabytes and Dino at 98 mgabytes. So Dino and Tori were basically even and then electroun was basically double everything else. Fort Tori, that&#x27;s nowhere near the 10x improvement that the marketing implies. On disk, yes, it is much smaller, but the actual memory footprint when the application is running is much more similar to the other tools. And one thing to keep an eye on when you&#x27;re actually doing these checks yourself, Tori uses the system web view, and those processes aren&#x27;t children of your app. Mac OS starts them separately. So, Activity Monitor shows Tori at about 36</p>
<p>Activity Monitor shows Tori at about 36 megabytes, and it looks like it beats Electron three times over, but it doesn&#x27;t. So, when you add all of those processes up, the 36 megabytes becomes closer to 109 megabytes, which is what we recorded in the test. In terms of the screen record itself, I did notice much better performance from the Tory app. And this is probably because we&#x27;re not recording the data in the web view and then transferring it over a bridge. Instead, it&#x27;s all recorded with the native SDK that comes with the system. If you want to get closer to like 60fps records, then Rust and Tori is going to</p>
<p>records, then Rust and Tori is going to be the way to go. Now, let&#x27;s look at developer experience. And due to each platform&#x27;s differences, this simple app was actually not straightforward to build at all. Overall, Electron and Tori were the easiest to implement, but Dino and Electrobun actually had a load of issues and system crashes. In Dino, when we started a record and then hide the app, the entire application would just close. I think this is because when no screens remain visible, Dino just assumes that the application is done and so it just terminated the entire process. So the hacky workaround for this was just to hide the view off</p>
<p>this was just to hide the view off screen instead. Electrobun had all of these issues around needing to bundle chromium for the screen record and for some reason the package actually depends on 3JS and BabylonJS which are for 3D rendering which contributed to the bloated bundle size. So all in all personally I would choose Tori but if you really don&#x27;t want to program in Rust then Electron is still the mature platform for TypeScript developers. Dino looks okay but I think the platform still needs some time to mature and then Electro Bun for me was the worst of all of them. So hopefully you can make a</p>
<p>of them. So hopefully you can make a judgment for yourself. Let me know what you think in the comments. And we&#x27;ve also done a video entirely on Dino Desktop. So if you want to learn more about that, then you can click this video here. Otherwise, I&#x27;ve been Warren from Better Stack. Thank you for watching and I&#x27;ll see you next time.</p>

</details>
