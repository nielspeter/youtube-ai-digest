---
title: "TypeScript 7 Officially Released And Boy Is It Fast"
channel: "Better Stack"
video_id: kl42N7pI7lM
url: https://www.youtube.com/watch?v=kl42N7pI7lM
published: 2026-07-29T20:00:05+00:00
generated: 2026-07-29T21:12:56+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/kl42N7pI7lM/hqdefault.jpg
---
# TypeScript 7 Officially Released And Boy Is It Fast

[![TypeScript 7 Officially Released And Boy Is It Fast](https://i.ytimg.com/vi/kl42N7pI7lM/hqdefault.jpg)](https://www.youtube.com/watch?v=kl42N7pI7lM)

[Watch on YouTube](https://www.youtube.com/watch?v=kl42N7pI7lM) · **Better Stack** · 2026-07-29

## TL;DR
TypeScript 7 has been released, replacing the old JavaScript-based compiler with one written in Go, delivering massive performance improvements through native execution and shared-memory concurrency. The new compiler achieves up to 15x faster build times on multi-core machines, dramatically improves language server responsiveness and stability, and maintains near-full compatibility with TypeScript 6.

## Key Takeaways
- TypeScript 7 ships with a compiler ported from JavaScript to Go, now available via `npm install typescript`.
- The VS Code codebase (1.3 million lines, ~8,000 files) compiles in 10.6 seconds versus 125.7 seconds on the old compiler — an 11.9x improvement.
- Roughly half the speedup comes from running compiled native code; the other half comes from Go's shared-memory concurrency model utilizing multiple CPU cores.
- JavaScript's single-threaded nature and the overhead of serializing/deserializing data across workers made it unsuitable for further compiler optimization.
- Go's runtime automatically distributes work across cores without manual thread management, making it ideal for CPU-bound compiler work.
- Users can further boost performance with the `--checkers` flag (e.g., `--checkers 12`) to spin up more parallel type checkers.
- The language server is now dramatically faster, showing errors in milliseconds, with failing commands reduced by over 80% and crashes reduced by over 60%.
- This is a port, not a rewrite — the team prioritized compatibility, so behavior remains essentially identical to TypeScript 6 aside from speed.
- The programmatic API is not yet available, so tools like TypeScript ESLint, TS-Jest, and TS-Node must wait for the 7.1 release.
- VS Code users must install the explicit "TypeScript 7" extension to use the new compiler in their editor.

## Detailed Breakdown

### Why the Rewrite? [01:05](https://www.youtube.com/watch?v=kl42N7pI7lM&t=65s)
Anders Hejlsberg, creator of C# and technical fellow at Microsoft, explained that JavaScript is optimized for UI and browsers, not for compute-intensive workflows like compilers. JavaScript is single-threaded, meaning type checking and abstract syntax tree processing can only scale so far. While web workers are technically possible, they require serializing and deserializing data across threads, which is slow and memory-intensive.

### Why Go? [01:35](https://www.youtube.com/watch?v=kl42N7pI7lM&t=95s)
The TypeScript team chose Go because it is a compiled language that runs directly on the CPU rather than being interpreted. Go also has a strong concurrency model with shared memory, allowing multiple threads to execute simultaneously without the serialization overhead required in JavaScript. The performance improvement is roughly an even split: about half comes from native code execution, and the other half from shared-memory concurrency.

### Benchmark Numbers [02:06](https://www.youtube.com/watch?v=kl42N7pI7lM&t=126s)
The video presents concrete benchmarks: VS Code's 1.3 million lines of code compile in 10.6 seconds (down from 125.7, an 11.9x improvement); BlueSky goes from 24.3 to 2.8 seconds (8.7x); and Playwright from 12.8 to 1.5 seconds (also 8.7x). The presenter notes that as CPU cores multiply (his M3 Max has 14 cores), the performance gap will only widen since JavaScript could only use a single core.

### Live Demo and the Checkers Flag [03:08](https://www.youtube.com/watch?v=kl42N7pI7lM&t=188s)
The presenter downloads the VS Code repo and runs diagnostics on his M3 Max. TypeScript 7 completes in 5.4 seconds by default, with 4.7 seconds spent on type checking. Adding the `--checkers 12` flag drops the total to 3.5 seconds, with check time falling to 2.9 seconds. Running the same command with TypeScript 6 takes 45.3 seconds — a roughly 15x improvement when utilizing all cores.

### Inside the Go Compiler Code [04:40](https://www.youtube.com/watch?v=kl42N7pI7lM&t=280s)
The presenter examines a `bindSourceFiles` function from the new compiler. It loops over potentially thousands of files, queues each for binding, and waits for completion. Go's runtime handles work distribution across cores automatically — no manual thread spawning or inter-core communication is needed. In JavaScript, similar code using `Promise.all` would still execute sequentially on a single thread. Workers can't share objects, only raw bytes via `SharedArrayBuffer`, meaning syntax trees would need full serialization and copying, often costing more than the work itself.

### Language Server Improvements [06:13](https://www.youtube.com/watch?v=kl42N7pI7lM&t=373s)
Beyond compile time, the new language server delivers near-instant feedback — errors appear in milliseconds even on massive codebases. The presenter recalls waiting up to two minutes on Intel Macs just to see error squiggly lines. TypeScript 7 also improves stability: failing language server commands are down over 80%, and server crashes are down over 60%.

### Port, Not Rewrite — and Ecosystem Compatibility [07:15](https://www.youtube.com/watch?v=kl42N7pI7lM&t=435s)
The TypeScript team emphasizes this is a port, not a rewrite, ensuring the new compiler is essentially fully compatible with the old one. However, the programmatic API is still missing, so packages depending on it (TypeScript ESLint, TS-Jest, TS-Node) will need to wait for the 7.1 release. VS Code users must explicitly install the "TypeScript 7" extension from the marketplace to use the new compiler in their editor.

## Notable Quotes
- "JavaScript is optimized for UI and browsers. It's not really optimized for compute-intensive workflows and compilers." — Anders Hejlsberg
- "Go is basically the perfect language for this. It's not just that Go is faster, it literally has more resources to throw at the problem."
- "We're not spawning threads or managing complex communication between cores. We just say, 'Here's some work.' And it figures out how to do the rest."
- "Handing a parse syntax tree to a worker means serializing the whole thing and copying it across and rebuilding it on the other side. For a big file, that can cost more than the work itself."
- "That's less laptops thrown at walls, which is actually pretty good for the environment. So, who knew Microsoft actually cared about the planet?"

## People, Tools & References Mentioned
- **Anders Hejlsberg** — Creator of C# and technical fellow at Microsoft
- **Go** — The language used for the new TypeScript compiler
- **VS Code** — Used as a benchmark codebase (1.3M lines, ~8,000 files)
- **BlueSky** — Referenced as a benchmark project
- **Playwright** — Referenced as a benchmark project
- **M3 Max (Apple)** — Presenter's machine with 14 cores
- **TypeScript ESLint, TS-Jest, TS-Node** — Packages awaiting the 7.1 release for programmatic API support
- **`--checkers` flag** — Allows users to increase parallel type checker count for faster builds
- **TypeScript 7 VS Code Extension** — Required for using the new compiler in VS Code

## Who Should Watch
This video is ideal for TypeScript developers — especially those working on large codebases — who want to understand why TypeScript 7 is so much faster and how to take advantage of the new compiler. It's also valuable for anyone curious about the technical reasons Go was chosen over JavaScript for a compiler rewrite.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=0s">00:00</a></span> TypeScript 7 has officially been released and after more than a year of painstaking development porting the compilers go. But improve that you can actually just do the entire thing with AI. So, I&#x27;m sure the developers are happy about that. If you now run NPM install TypeScript, you&#x27;ll get version 7, which is the version with the go compiler. And following the announcement video from Microsoft a couple of days ago, I wanted to dive into exactly how they would achieve these massive performance gains. The results have been genuinely impressive. The new compiler builds the VS code code base, which is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=31s">00:31</a></span> builds the VS code code base, which is 1.3 million lines of code across almost 8,000 files in just 10 seconds compared to the 125 seconds from the old compiler. And with TypeScript now proudly sitting as the number one language on GitHub, believe it or not, the new compiler is going to change so many lives. I&#x27;m just getting emotional thinking about it. But rather than look at the almost identical features between six and seven, I wanted to dive into exactly how that performance is achieved. So, let&#x27;s take a look at the new compiler and see what makes it so fast.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=65s">01:05</a></span> So, why the rewrite? Well, the creator of C# and technical fellow at Microsoft Anders Hejlsberg said it quite plainly, &quot;JavaScript is optimized for UI and browsers. It&#x27;s not really optimized for compute-intensive workflows and compilers, which is pretty obvious. Why? Because it&#x27;s single-threaded and processing something like an abstract syntax tree or type checking can only really scale so far with access to a single core. You could technically work across workers, but then you&#x27;d need to serialize and deserialize the data,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=95s">01:35</a></span> serialize and deserialize the data, which is slow and memory-intensive. And then you&#x27;d have to deal with the complexity of managing all of that. So, they settled with go, which provides dramatic performance improvements using a language that is basically fit for purpose. Go is a compiled language, which means we can run compiled code directly on the CPU rather than having to interpret it. And go has a very good concurrency model, which means we can easily run multiple threads of execution at the same time all with shared memory. This means we can take advantage of all the cores on your machine rather than</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=126s">02:06</a></span> the cores on your machine rather than just one. And there&#x27;s roughly an even split up to half the speed up is attributed to being in native code and the rest from having shared memory concurrency. Go is basically the perfect language for this. It&#x27;s not just that Go is faster, it literally has more resources to throw at the problem and the results speak for themselves. If we look at the numbers, VS Code at 1.3 million lines of code came in at 125.7 seconds on the old compiler, 10.6 seconds, which is 11.9x improvement. For</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=157s">02:37</a></span> seconds, which is 11.9x improvement. For Blue Sky, we&#x27;ve got 24.3 to 2.8, that&#x27;s 8.7 improvement. And then for Playwright, we have 12.8 seconds down to 1.5, an 8.7 improvement. And funnily enough, it only takes 1 second to subscribe to Better Stack. Now, the gap here is only going to widen because cores are not really getting faster at the same rate they used to, but what we do get is more cores. I&#x27;m on an M3 Max, for example, which has 14 cores, which is insane. I remember building a gaming PC back in college, which had an Intel i7 with four cores, and I thought that</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=188s">03:08</a></span> i7 with four cores, and I thought that was an absolute beast. The JavaScript compiler would just use one of those cores, but with Go, I unlock all of them. And of course, the more cores you have, the more performance you get. If I compile a large project on this machine in version 6, you&#x27;ll see it takes 45 seconds. And with version 7, we can get that down to as little as 3 seconds. And there are multiple phases to the compilation process, and the type checking phase is just one of them. For this, Go will spin up four type checkers and have them check a quarter of the code base each, but you can actually</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=219s">03:39</a></span> code base each, but you can actually improve that even further. So, during compilation, you could set checkers to 12 for even faster performance. So, I&#x27;ve downloaded the VS Code repo to my machine, so we can see the difference between TypeScript 7 and 6. By default, TSC on my machine will now point to TypeScript 7. So, we&#x27;ll just run the diagnostics on this. And you can see that took 5.4 seconds, and the majority of the time was actually spent doing the check time. So, 4.7 of those seconds. We can actually speed that up as well. So, if we add another flag, checkers 12.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=249s">04:09</a></span> So, if we add another flag, checkers 12. So, you can see the total time now has gone down from 5.4 to 3.5. And all of that shaves off the check time. So, here we got 4.7, and then that&#x27;s gone down to 2.9. Now, let&#x27;s run the same command again, but this time we&#x27;re going to be using TypeScript 6. And this is going to take a little while, so we&#x27;ll speed through it. So, after waiting for that, you can see that TypeScript 6 finished with 45.3 seconds. Compared to 3.5 that we get when we run across all the cores. So, that is effectively a 15x improvement on my M3 Max chip. So, for</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=280s">04:40</a></span> improvement on my M3 Max chip. So, for me, this is where the 3.5 seconds actually comes from. Doing this will, of course, steal performance from other processes. But if you&#x27;re not doing anything, then you might as well use all the resources that your machine has. So, let&#x27;s take a look at some real code from the new compiler to understand how Go is able to achieve this performance. Here we have a bind source files function whose job is to build up every declaration in a file and work out what scope it belongs to. We&#x27;re processing possibly thousands of files. We loop over each file. We queue up a function to bind it. Then, we wait for all of them to finish. The beautiful</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=312s">05:12</a></span> for all of them to finish. The beautiful part is that we don&#x27;t have to think about how that work gets distributed across cores. Go&#x27;s runtime just handles all of that. We&#x27;re not spawning threads or managing complex communication between cores. We just say, &quot;Here&#x27;s some work.&quot; And it figures out how to do the rest. In JavaScript, we could write almost identical code. But this is pointless for CPU bound work. It would all still just happen on one thread in sequence, even if promise all gives the illusion of parallelism. Workers are technically a way around this, but you can&#x27;t share objects between them, only</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=342s">05:42</a></span> can&#x27;t share objects between them, only raw bytes with shared array buffer. So, handing a parse syntax tree to a worker means serializing the whole thing and copying it across and rebuilding it on the other side. For a big file, that can cost more than the work itself. Basically, it&#x27;s stuff like this that makes going inherently better for CPU-bound work. It has a runtime that can handle all of this concurrency for you, and it has shared memory, so you can pass objects around without having to copy them. Now, aside from the compile time, the thing you&#x27;re going to notice the most is the speed of your language server. Anyone who&#x27;s worked on a large TypeScript code base knows the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=373s">06:13</a></span> a large TypeScript code base knows the pain of waiting for types to be type checked. And my god, these Intel Macs really felt this. I remember working on projects a couple of years ago, and you would open the repository and literally have to wait up to 2 minutes just to see the squiggly lines come in. And then every time that you made a change, it would just be incredibly painful. The developer experience is terrible, and then no one wants to work on the code base. The new language server, however, means instant feedback in your IDE, so you can open a file, make a change, and see the errors in literally</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=404s">06:44</a></span> see the errors in literally milliseconds, even if you&#x27;re working on potentially massive code bases. Aside from performance, the new language server is now more stable, so the need to restart your IDE when the type checking just stops working is drastically reduced. TypeScript 7 reduced the failing language server commands by over 80% and reduced server crashes by over 60%. So, that&#x27;s less laptops thrown at walls, which is actually pretty good for the environment. So, who knew Microsoft actually cared about the planet? Now, it&#x27;s also worth mentioning this is a port, not a rewrite. So, the TypeScript</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=435s">07:15</a></span> port, not a rewrite. So, the TypeScript team have been very careful to ensure that the new compiler is basically fully compatible with the old one. You likely won&#x27;t even notice a difference except for the speed. But whilst you can now run TypeScript 7 on your own projects, you&#x27;ll still need to wait for your favorite packages to catch up. Their programmatic API is still missing, which means that any package that depends on that will need to wait for the 7.1 release. So, packages like TypeScript ESLint, TS-Jest, or TS-Node will lag behind. Now, the full release of TypeScript 7 is available for you to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=466s">07:46</a></span> TypeScript 7 is available for you to download, but you do need to explicitly install the TypeScript 7 extension for VS Code. The default package will eventually be updated, but for now, just install that extension. It&#x27;s called TypeScript 7 on the extension store, and then everything will run as expected. If you want to see more about the feature set of TypeScript 7, we filmed a video on exactly that that you can see here. And if you enjoy breakdowns like this, then subscribe to Better Stack for more. So, hopefully you learned something there, and now you can take advantage of the rapid development that you&#x27;re going to get with TypeScript 7. I definitely know I&#x27;m going to enjoy using this one,</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=kl42N7pI7lM&amp;t=497s">08:17</a></span> know I&#x27;m going to enjoy using this one, but thank you for watching, and of course, I&#x27;ll see you in the next one.</p>

</details>
