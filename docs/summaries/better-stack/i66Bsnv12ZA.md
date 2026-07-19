---
title: "Git Can’t Handle Games… So Epic Built Lore"
channel: "Better Stack"
video_id: i66Bsnv12ZA
url: https://www.youtube.com/watch?v=i66Bsnv12ZA
published: 2026-07-14T14:00:37+00:00
generated: 2026-07-14T15:42:29+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/i66Bsnv12ZA/hqdefault.jpg
---
# Git Can’t Handle Games… So Epic Built Lore

[![Git Can’t Handle Games… So Epic Built Lore](https://i.ytimg.com/vi/i66Bsnv12ZA/hqdefault.jpg)](https://www.youtube.com/watch?v=i66Bsnv12ZA)

[Watch on YouTube](https://www.youtube.com/watch?v=i66Bsnv12ZA) · **Better Stack** · 2026-07-14

## TL;DR
Epic Games built Lore, a free, open-source version control system written in Rust, designed to handle the massive binary assets (textures, 3D models, audio) that game development requires and that Git struggles with. It combines a central server of record with fast local operations, using content-addressed chunking and deduplication to manage large files efficiently. While still pre-1.0 and not yet a production replacement for Perforce, it offers a promising look at the future of version control for asset-heavy projects.

## Key Takeaways
- Git was designed for text and small code files, making it a poor fit for game development, which involves massive, frequently changing binary assets.
- Git LFS helps manage large files but feels like a workaround, bringing quotas, bandwidth limits, and bloated history. Perforce works for game studios but is expensive and complex to maintain.
- Lore is built in Rust, MIT licensed, and offers the core library, server, CLI, and SDKs for free.
- Instead of storing full copies of large files, Lore breaks them into smaller chunks, hashes and compresses them with Zstandard, and stores them in a content-addressed Merkle tree, enabling deduplication.
- Lore supports on-demand file hydration, allowing developers to pull down only the assets they need rather than cloning the entire repository history.
- It is a centralized system with a server of record, but day-to-day operations (staging, committing, branching, switching) happen locally and work offline, sitting somewhere between Git and Perforce.
- Lore is still pre-1.0; the APIs may change, there is no Git interoperability, and it is self-hosted only (no hosted cloud service).
- The desktop GUI application seen floating around is not included in the open-source release.
- Independent performance benchmarks are currently lacking, with most performance claims coming from Epic Games itself.
- It is not recommended to replace a production Perforce setup tomorrow, but it is worth testing on new or non-critical projects to see where version control for large binaries is heading.

## Detailed Breakdown

### The Problem with Git for Game Development [00:00](https://www.youtube.com/watch?v=i66Bsnv12ZA&t=0s)
Git was built for code—mostly text files and small changes. Games are the opposite, relying on massive textures, audio files, videos, and 3D models that can be hundreds of megabytes or gigabytes in size. When these large binary files change, Git repositories grow bloated, clones slow down, and history becomes massive. Git LFS helps but feels like a workaround layered on a system never designed for this data, introducing quotas and bandwidth limits. Perforce is the industry standard for games, but it is expensive, complicated, and often requires a dedicated person to maintain it.

### Demo: Running Lore Locally [01:37](https://www.youtube.com/watch?v=i66Bsnv12ZA&t=97s)
The presenter runs Lore using a single install command with a demo flag. Within seconds, a Lore server is running locally without needing a cloud account, authentication tokens, or a setup wizard. Hitting a health endpoint confirms the server is alive. The presenter creates a repository folder and generates a 100 MB dummy binary file using the `dd` command.

### Chunking and Deduplication [02:38](https://www.youtube.com/watch?v=i66Bsnv12ZA&t=158s)
When the large file is committed, Lore does not treat it as one huge object. Instead, it breaks the file into smaller chunks, hashes them, compresses them with Zstandard, and stores them in a content-addressed Merkle tree. If a file is modified but most of it stays the same, Lore reuses existing chunks and only stores the parts that changed. After committing, a local Lore directory with config and metadata is created on disk.

### Local Workflow and Branching [03:09](https://www.youtube.com/watch?v=i66Bsnv12ZA&t=189s)
Lore's workflow feels similar to Git. The presenter creates a branch with `lore branch create`, switches to it, makes a text file, stages it, and commits it. Switching back to the main branch is instant. Crucially, staging, committing, branching, switching, and diffing all happen locally without needing to communicate with a server, allowing for fast, offline work.

### Architecture: Centralized with Local Speed [04:13](https://www.youtube.com/watch?v=i66Bsnv12ZA&t=253s)
In the demo, data is temporary and disappears when the server stops. In a real setup, you run the server with a config file pointing to persistent storage or object storage. Lore is a centralized system with one server of record, but because operations happen locally, it sits between Perforce and Git, offering central access management with quick, server-independent daily work. It also supports on-demand file hydration, so developers only download the assets they need rather than the entire repository.

### Licensing and Realistic Expectations [05:16](https://www.youtube.com/watch?v=i66Bsnv12ZA&t=316s)
Lore is MIT licensed, open source, and has SDKs for multiple languages, making it easy to script around. However, it is not a production replacement for Perforce yet. It is pre-1.0, and APIs may change. There is no Git interoperability, meaning you cannot import existing Git history. It is self-hosted only, with no managed cloud service, and the desktop GUI application is not part of the open-source release. Performance claims come solely from Epic, with no independent benchmarks yet.

### Should You Use It? [06:49](https://www.youtube.com/watch?v=i66Bsnv12ZA&t=409s)
Lore is fun to play with and worth trying for new, asset-heavy projects or non-critical tests to evaluate its performance and workflow. The bigger takeaway is that version control is no longer a solved problem once projects ship with huge amounts of binary data. Lore represents a direction for solving this, and whether it wins or not, it is a cool development for the industry.

## Notable Quotes
- "Git was built for code. Mostly text files, lots of small files, changes that are usually a few lines at a time. Games are basically the opposite of that."
- "Instead of treating that 100 megabyte file as one huge object, lore breaks into smaller chunks. Those chunks are hashed, compressed with Zstandard, and stored in a content addressed Merkel tree."
- "Even though lore has a central server, your normal day-to-day work still feels fast and you can keep working offline."
- "The bigger point here isn't whether lore replaces Git or Perforce anytime soon. The bigger point is that version control stop being a solved problem once project started shipping with huge amounts of binary data."

## People, Tools & References Mentioned
- **Epic Games** (company behind Fortnite and Lore)
- **Git** (distributed version control system)
- **Git LFS** (Git Large File Storage)
- **Perforce** (version control system used by many game studios)
- **Lore** (Epic's Rust-based version control system)
- **Rust** (programming language used to build Lore)
- **Zstandard** (compression algorithm used by Lore)
- **Merkle Tree** (data structure used for content-addressed storage)
- **DD** (command-line utility used to create a dummy file in the demo)

## Who Should Watch
Game developers, technical artists, and DevOps engineers working with massive binary assets who are curious about alternatives to Git and Perforce. It is also valuable for anyone interested in the architecture of modern version control systems and content-addressed storage.


<details class="transcript">
<summary>Full transcript</summary>

<p>Epic Games built its own version control system all because it got fed up with Git. They built it in Rust and then released it for free. It&#x27;s called Lore. So yeah, the company behind Fortnite built a Git alternative, but Git is still great obviously, but Git was built for code. Mostly text files, lots of small files, changes that are usually a few lines at a time. Games are basically the opposite of that. So, how does lore compare to Git, and how do we even work with it? Let&#x27;s find out.</p>
<p>Now, at this point, we&#x27;ve got massive textures, audio files, videos, 3D models, and all kinds of binary assets that can be hundreds of megabytes or even several gigabytes each. And once those files start changing, things get really messy. your repository grows, clones get slower, history becomes huge, and eventually someone says, &quot;Okay, maybe we should use git LFS.&quot; Git LFS helps, but it also feels like a workaround added to a system that was never designed for this kind of data.</p>
<p>never designed for this kind of data. Then you&#x27;ve got quotas, bandwidth limits, and old assets hanging around in history. So, a lot of studios use Perforce. And to be fair, Perforce works. There&#x27;s a reason so many game studios use it, but it&#x27;s expensive. It can get complicated, and once your setup gets big enough, somebody usually ends up becoming the person who keeps it all alive. This is the thing that lore was sort of designed to fix. If you enjoy coding tools to speed up your workflow, be sure to subscribe. We have videos coming out all the time. All right. Now,</p>
<p>coming out all the time. All right. Now, instead of just talking about lore, it&#x27;s cool. Let me get it running. Let me show you how it works. The demo starts with one install command and a demo flag which we&#x27;re going to run right here. And that&#x27;s it. A couple of seconds later, I&#x27;ve got a lore server running locally. No cloud account, no key, noert setup. It&#x27;s running here on these ports. And just to prove it&#x27;s actually alive, I can just hit the health endpoint right here. And I&#x27;m going to do that over on this terminal. And there we go. It is alive.</p>
<p>terminal. And there we go. It is alive. It is running. There are no background services I need to manually hook together. No off token to generate. There&#x27;s no setup wizard. It just starts. Now let me create a repository. So I&#x27;m going to create a folder, right? And we are going to create this repository. And now I&#x27;m going to create a large binary file and commit it. Right? This is just a dummy file, right? But let&#x27;s create a larger file. I&#x27;m running DD here for data duplication. Now instead of treating that 100 megabyte file as one</p>
<p>treating that 100 megabyte file as one huge object, lore breaks into smaller chunks. Those chunks are hashed, compressed with Zstandard, and stored in a content addressed Merkel tree. If most of the file stays the same, Lore doesn&#x27;t need to save another full copy of the whole thing. It can reuse the trunks it already has and only store the parts that changed. That&#x27;s a much better fit for a large binary asset. Right after the commit finishes, you can see the local state that was created on disk. There&#x27;s now a lore directory here with</p>
<p>There&#x27;s now a lore directory here with the config and the metadata. All right, now that we have that, let&#x27;s make a branch. Okay, I can run lore branch create name the branch. It works pretty much like git. So, let&#x27;s switch to it. Let&#x27;s actually make a small change here. I&#x27;ll create a quick text file and commit it to this branch. So I modify then we can stage it and then we can commit it. Right? The same flow is roughly the same as get. Now I&#x27;m going to switch back and that was basically instant. The</p>
<p>and that was basically instant. The other important thing is that none of that required a trip to any server. Staging, committing, branching, switching, diffing, all of that happens locally. So even though lore has a central server, your normal day-to-day work still feels fast and you can keep working offline. It just makes it feel all lightweight. Now the question becomes, okay, where is all the data going? In this demo here, everything is temporary. So when I stop the server, the data disappears. That&#x27;s because I&#x27;m just using demo mode. In a real setup,</p>
<p>just using demo mode. In a real setup, you would run lore server with a config file and persistent storage. The same CLI commands and local workflow stay the exact same. you&#x27;re just pointing the server at real directories or object storage instead of throwing away that temporary folder. Now with Git, Git gives you a history of project snapshots. Although internally it does a lot of clever optimization, lore is designed around chunking and dduplication from the get-go. So for a large asset heavy project, it doesn&#x27;t</p>
<p>large asset heavy project, it doesn&#x27;t have to treat every new version of the file as a completely separate giant object. Lore can also hydrate files on demand so you can work with a repository containing a huge amount of data without downloading every single asset from day one. You pull down what you actually need for the part of the project you&#x27;re working on. Now, one thing that&#x27;s a tad bit confusing here when Laura launched was whether it&#x27;s centralized or distributed. It&#x27;s centralized. There is one server of record, but most of the work that we&#x27;re doing is happening</p>
<p>work that we&#x27;re doing is happening locally. So in practice it sits somewhere between perforce and git. You get central control and access management but local operations still feel quick and don&#x27;t depend on the server being available every single second. There are some nice differences too. Lore is MIT licensed. The protocol is open source and there are SDKs for multiple languages which makes it much easier to script and build tooling around. Now it&#x27;s probably a good point to be realistic here. lore is not something I would replace a production</p>
<p>something I would replace a production perfor setup tomorrow with. It&#x27;s still pre 1.0. Epic Games says the APIs may change before the first stable release. And the project is clearly still evolving. There&#x27;s also no Git interoperability right now, and you can&#x27;t just point lore at an existing Git repository and bring the full history across. It&#x27;s self-hosted, too. There isn&#x27;t a hosted service where you create an account, push your repo, and you&#x27;re done. and the desktop app you may see floating around isn&#x27;t included in the open- source release. What you get is</p>
<p>open- source release. What you get is the core library, the server, the CLI, and the SDKs. That GUI is not a part of it. Then, of course, performance. How does this perform? Epic says Lore can handle huge repositories without slowing down the way other systems do. And Epic obviously has experience with some very large projects, but right now, most of those claims are coming from Epic themselves. There isn&#x27;t really solid independent benchmarks yet. So, performance looks promising, but until we really start testing this out, it&#x27;s hard to see how this performs. Should</p>
<p>hard to see how this performs. Should you use it? Well, it&#x27;s fun to play around with. Are you making games? Are you building massive projects? Okay, for a new project, maybe. If you just want to see where version control for large binary assets could be going, it&#x27;s worth a try. Test it on something non-critical. Play around with it. See how it performs. See how the flow is. The bigger point here isn&#x27;t whether lore replaces Git or Perforce anytime soon. The bigger point is that version control stop being a solved problem once project started shipping with huge amounts of</p>
<p>started shipping with huge amounts of binary data. Get one for text smaller files. Lore is trying to solve something that comes after that. And honestly, whether it wins, whether it doesn&#x27;t is still a really cool direction. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
