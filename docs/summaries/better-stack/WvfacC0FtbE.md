---
title: "Postgres was rewritten in Rust… and somehow passed every test"
channel: "Better Stack"
video_id: WvfacC0FtbE
url: https://www.youtube.com/watch?v=WvfacC0FtbE
published: 2026-07-17T12:00:16+00:00
generated: 2026-07-17T14:02:37+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/WvfacC0FtbE/hqdefault.jpg
---
# Postgres was rewritten in Rust… and somehow passed every test

[![Postgres was rewritten in Rust… and somehow passed every test](https://i.ytimg.com/vi/WvfacC0FtbE/hqdefault.jpg)](https://www.youtube.com/watch?v=WvfacC0FtbE)

[Watch on YouTube](https://www.youtube.com/watch?v=WvfacC0FtbE) · **Better Stack** · 2026-07-17

## TL;DR
PGRust is a Rust rewrite of PostgreSQL that passes all 46,000 official Postgres regression queries and works with standard PSQL clients, but is not production-ready. The project's most exciting features—including a thread-per-connection model and dramatic performance claims—live in an unreleased version, and the rewrite was heavily aided by AI coding agents, raising questions about whether large infrastructure rewrites are becoming economically feasible.

## Key Takeaways
- PGRust passes the full official Postgres regression test suite (46,000+ queries) and can boot from an existing Postgres 18.3 data directory.
- It is a completely separate implementation, not an extension or fork—it preserves Postgres behavior, client experience, and disk formats while replacing the underlying engine with Rust.
- The released version shows no dramatic speed improvements; the major performance claims come from an unpublished thread-per-connection version.
- Developers Michael Malis and Jason Seebol claim roughly 50% better transactional performance and 300x better analytical performance, but the code is not yet available for independent benchmarking.
- The thread-per-connection model could reduce per-connection overhead and improve state sharing, but removes the fault isolation that separate processes provide.
- AI coding agents were heavily used, making the real experiment about whether AI can make large-scale rewrites affordable enough to rethink foundational architecture.
- Passing regression tests is a serious, measurable achievement, but does not equate to production trust—crash recovery, replication, and long-running stability remain unproven.
- Extension compatibility is a major gap that is still unfinished.
- The developer community is roughly split: some see a genuine breakthrough in compatibility and AI-assisted development; others caution that tests don't replace real-world production hardening.
- The project is explicitly not production-ready, but is worth experimenting with via its Docker image.

## Detailed Breakdown

**[00:00] Introduction: A Postgres Rewrite That Passes Every Test**
The video opens by introducing PGRust, a Rust rewrite of PostgreSQL that passes all 46,000 Postgres regression queries, works with standard PSQL, and can even boot an existing Postgres 18.3 data directory. While this sounds production-ready, it is not—but the most exciting version remains unreleased.

**[00:32] The Problem With Postgres**
Postgres is one of the best databases ever built, but it carries nearly four decades of architecture and roughly a million lines of C. Its process-per-connection model provides useful isolation but introduces memory overhead, connection pooling pressure, and difficulty sharing state across parallel work. PGRust takes a different approach: keep the behavior, client experience, and disk formats, but replace the engine with Rust.

**[01:35] Testing PGRust in Practice**
The presenter runs the official Docker image and connects with a standard PSQL client. PGRust reports itself as a distinct version, but from the outside it is indistinguishable from Postgres—same SQL, same output, real query plans with index scans and execution stats. A 100,000-row insert demonstrates it is a functional database server, not a partial implementation.

**[02:38] What This Actually Proves**
The released version does not show dramatic speed improvements. The bigger performance claims come from an unreleased development version. However, the current release proves this is a real, complete implementation: it passes the full regression suite, speaks the real wire protocol, and has working query planning and storage engines.

**[03:10] Why Not an Extension or Fork?**
Extensions sit on top of the existing Postgres core and cannot change it. Forks can modify the core but inherit the same architecture and the burden of tracking upstream. Distributed databases like CockroachDB and Yugabyte are independent systems where exact drop-in compatibility is not the primary goal. PGRust uses actual Postgres behavior as its specification, targeting Postgres 18.3 compatibility.

**[03:41] The Thread-per-Connection Experiment**
The unpublished version replaces Postgres's process-per-connection model with thread-per-connection. Threads reduce per-connection overhead and make state sharing easier, but they also remove the fault isolation that separate processes provide—a memory bug or unsafe extension could affect more of the server. This trade-off opens new doors but may remove safety rails.

**[04:43] The Role of AI in the Rewrite**
Michael Malis and Jason Seebol used AI coding agents heavily. The published version intentionally mirrors original Postgres structure, while the unpublished version explores larger architectural changes. The real experiment is whether AI can make a rewrite of this scale affordable enough that developers can rethink foundational architecture rather than just asking whether Rust makes Postgres faster.

**[05:14] Performance Claims and Skepticism**
Developers claim roughly 50% better transactional performance and 300x better analytical performance, but the code behind these numbers is not publicly available for inspection or benchmarking. The community is split, with reasonable questions raised on GitHub. The presenter advises treating the numbers as promising claims, not settled facts, while noting that the exact multiplier may matter less than the freedom to experiment.

**[06:17] Community Reaction: Two Sides**
The Hacker News discussion drew hundreds of comments, with both sides making valid points. Supporters note that passing every regression query is a serious, measurable achievement in a space where "Postgres compatible" can mean almost anything, and that AI-assisted rewrites may make previously prohibitively expensive infrastructure experiments viable. Critics argue that regression tests do not replace years of crash recovery, replication, and long-running stability testing, and that extension compatibility remains a major gap.

**[07:52] Should You Use PGRust?**
The project itself states it is not production-ready, not fully optimized, and has unfinished extension compatibility. However, developers working with databases, Rust, query execution, compatibility testing, or AI development are encouraged to try it—run the Docker image, test client libraries, and read the source code.

## Notable Quotes
- "Postgres is one of the best databases ever built. Let's face it. But, it also carries nearly four decades of architecture and roughly a million lines of C."
- "This is not a Postgres extension. It's not a feature added on top. This is completely separate, an implementation trying to behave just like Postgres."
- "The real experiment is not simply can Rust make Postgres faster? It's more like can AI make a rewrite this large affordable enough that developers can actually rethink architecture underneath things."
- "Passing regression tests is not the same as earning production trust. Those tests don't replace years of crash recovery and replication testing, or databases that run for months without stopping."
- "We don't need to change the entire Postgres project before learning whether an idea actually works or not. That freedom may be more valuable than any single benchmark we can get."

## People, Tools & References Mentioned
- **PGRust** — the Rust rewrite of PostgreSQL discussed throughout the video
- **PostgreSQL 18.3** — the compatibility target for the current PGRust release
- **Michael Malis and Jason Seebol** — developers behind PGRust
- **CockroachDB and Yugabyte** — mentioned as independent distributed databases where exact drop-in compatibility is not the main goal
- **Bun** — referenced for its own Rust rewrite covered in a separate video
- **Docker** — the official PGRust Docker image used for testing
- **PSQL** — the standard Postgres client used to connect to PGRust
- **Hacker News** — cited for the main community discussion thread
- **GitHub** — referenced for issues and community questions about the project

## Who Should Watch
Database engineers, Rust developers, and anyone interested in AI-assisted code generation or infrastructure rewrites will find this video valuable. It offers a hands-on look at a serious Postgres compatibility experiment while honestly assessing what the project does and does not prove, making it useful for viewers who want to understand the current state and limits of AI-driven database rewrites.


<details class="transcript">
<summary>Full transcript</summary>

<p>Someone rebuilt Postgres in Rust, and somehow the release version now passes all 46,000 Postgres regression queries. It works with normal PSQL. It can even boot an existing Postgres 18.3 data directory. That sounds like a production-ready replacement. It isn&#x27;t. But, the most exciting version of this project has yet to even be released. So, what exactly are we even looking at here? Is this the future of Postgres or just an AI experiment?</p>
<p>Now, to understand why this matters, you need to understand the problem. Postgres is one of the best databases ever built. Let&#x27;s face it. But, it also carries nearly four decades of architecture and roughly a million lines of C. Every client connection gets its own back-end process. That isolation is useful, but it also means more memory overhead, more pressure to use connection pooling, and more difficulty sharing state across parallel work. PGRust takes a different path. Keep the Postgres behavior, keep</p>
<p>path. Keep the Postgres behavior, keep the client experience, keep the disk formats, but replace the engine underneath with Rust. This is not a Postgres extension. It&#x27;s not a feature added on top. This is completely separate, an implementation trying to behave just like Postgres. We&#x27;re seeing a lot of Rust rewrites now, just like the one we covered the other day on Bun rewriting its entire codebase with Rust. I&#x27;ll put it somewhere right here. And now, all this sounds good, but does it actually feel like real Postgres? Let&#x27;s test it properly. If you enjoy coding tools that speed up your workflow, be</p>
<p>tools that speed up your workflow, be sure to subscribe. We have videos coming out all the time. Now, I&#x27;m starting with the official Docker image, then connecting with a completely normal PSQL client. Nothing custom. Now, I&#x27;m in. First, let&#x27;s check the version. As you can see, it reports itself as PGRust with the latest version. Now, I can create a table, insert some data, and look at a query plan. I&#x27;m just going to run this right here in my terminal. From the outside, this is completely indistinguishable from Postgres. Same client, same SQL, same</p>
<p>Postgres. Same client, same SQL, same output. You can even see the query planner chose an index scan and gave us real execution stats. And to make this a little more interesting, let&#x27;s insert 100,000 rows and run another query. This is just a generated 100k rows of data. We&#x27;re going to drop it in here. Now, what is the point of all this? Okay, well, good question. Well, in this current early version release, we&#x27;re not going to see dramatic speed improvements over regular Postgres. The bigger performance claims come from an</p>
<p>performance claims come from an unreleased development version that switches to a thread per connection model. This all does prove though that this isn&#x27;t just a partial implementation. It has passed the full official Postgres regression test suite, over 46,000 queries. It speaks the real wire protocol, and it has a working query plan and storage engine. This is a real database server. It&#x27;s just written in Rust. So, with this progressing, we could see some serious performance enhancements on the speed side of things. So, now the question is, why not</p>
<p>things. So, now the question is, why not just create another Postgres extension? Because extensions sit on top of the original Postgres core. A fork can change that core, but then it inherits the same architecture and the permanent job of keeping up with upstream Postgres. You have databases like CockroachDB and Yugabyte, but they are independent distributed databases. Exact drop-in compatibility is not their main goal. PG Rust is trying something else. It uses actual Postgres behavior as the specification. The current release</p>
<p>specification. The current release targets Postgres 18.3. It passes the default regression suite and isolation tests. And it is just compatible enough to boot from an existing Postgres 18.3 data directory. The bigger experiment here is happening in a separate unpublished version. And that version reportedly replaces Postgres process per connection model with a thread per connection model. With the normal Postgres model, each connection gets its own process. With the new model, each connection gets a thread inside the same</p>
<p>connection gets a thread inside the same process. That can lower per connection overhead and make it easier for different parts of the database to actually share information. But with all this, there is going to be a trade-off, right? Separate processes also create useful walls between connections. If one process fails, that separation can help contain the damage. With threads, one unsafe extension or memory bug could affect more of the server. So, thread per connection is not automatically better. It just opens new doors, but it</p>
<p>better. It just opens new doors, but it may also remove some safety rails. Then there is the second major part of the story, AI. Michael Malis and Jason Seebol used coding agents heavily to speed up the rewrite. The published version intentionally follows the original Postgres structure in many places. The unpublished version is where they are trying larger architectural changes. So, the real experiment is not simply can Rust make Postgres faster? It&#x27;s more like can AI make a rewrite this large affordable enough that developers can actually rethink</p>
<p>developers can actually rethink architecture underneath things because AI was heavily used here. Now, does this change things? Well, it might. It&#x27;s also where we need to slow down a little bit. The released version is not heavily optimized. The major performance claims come from the unpublished thread per connection version, which right now we can&#x27;t quite test. The devs claim roughly 50% better performance on transactional workloads. They also claim around 300 times Postgres&#x27; performance on analytical workloads. Those numbers are</p>
<p>analytical workloads. Those numbers are huge, but the code behind those results is not currently available for any type of inspection or benchmarking. So, hence this, there is still a lot of speculation. It seems there is a good 50/50 split here, at least reading online with questions that look kind of like these. These are just the issues here on GitHub. Then you even get one issue like this one, right? Which is a completely reasonable question. As you read through this issue, the devs seem adamant about actually making this work. So, we don&#x27;t have real stats just yet.</p>
<p>So, we don&#x27;t have real stats just yet. That does not automatically mean the numbers are false, though. It just means we should treat them as promising claims, not settled facts. And honestly, the exact multiplier may not be the most important part. We don&#x27;t need to change the entire Postgres project before learning whether an idea actually works or not. That freedom may be more valuable than any single benchmark we can get. Now, the reaction from devs with all these Rust rewrites, even on this pg Rust, has been massive. The main Hacker News discussion passed hundreds of points and comments, but again, the</p>
<p>of points and comments, but again, the response is split. Both sides are making good points. First, passing every regression query is a serious achievement. A lot of projects claim to be Postgres compatible. That phrase can mean almost anything. pg Rust has a measurable target. The real Postgres tests are the judge of this. And the speed of this rewrite suggests that coding agents may completely change cost of large infrastructure experiments. Ideas that once looked too expensive to attempt are now seemingly becoming more possible. Now, for the other side of</p>
<p>possible. Now, for the other side of things, passing regression tests is not the same as earning production trust. Those tests don&#x27;t replace years of crash recovery and replication testing, or databases that run for months without stopping. A project can pass every known test and still fail in a situation nobody even thought to test. Generating hundreds of thousands of lines of code is one challenge. Extension compatibility is another major gap. Now, should you replace your production Postgres cluster with PG Rust? No, absolutely not. The project itself is</p>
<p>absolutely not. The project itself is not production ready. It&#x27;s stated. It&#x27;s not fully optimized. And major compatibility areas, including the extension ecosystem, they&#x27;re still unfinished. But should you try it? Sure. If you work with databases, Rust query execution, compatibility testing, or AI development, why not give it a try? Run the Docker image, test your client library against it, read the source, and see what happens. So, drop your verdict in the comments. Where is this project going? Are we going to start rewriting more in Rust? We&#x27;re going to find out.</p>
<p>more in Rust? We&#x27;re going to find out. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
