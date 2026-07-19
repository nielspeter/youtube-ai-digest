---
title: "DuckDB is becoming unstoppable..."
channel: "Better Stack"
video_id: dKbV8MEzVPA
url: https://www.youtube.com/watch?v=dKbV8MEzVPA
published: 2026-07-13T18:00:07+00:00
generated: 2026-07-13T19:45:32+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/dKbV8MEzVPA/hqdefault.jpg
---
# DuckDB is becoming unstoppable...

[![DuckDB is becoming unstoppable...](https://i.ytimg.com/vi/dKbV8MEzVPA/hqdefault.jpg)](https://www.youtube.com/watch?v=dKbV8MEzVPA)

[Watch on YouTube](https://www.youtube.com/watch?v=dKbV8MEzVPA) · **Better Stack** · 2026-07-13

## TL;DR
DuckDB is a free, embedded, single-file analytical database—think SQLite but built for crunching numbers instead of transactions—that has matured into a production-capable tool with encryption, git-style upserts, and modern lakehouse format support. Its 1.4 release delivered the heavy-hitting features (and became the first long-term support release), while 1.5 refined the experience with a better CLI, a new variant type, and geometry support—though it remains unsuited for high-concurrency transactional workloads or memory-tuned billion-row queries.

## Key Takeaways
- DuckDB is an embedded, serverless, single-file analytical database: "SQLite but for analytics," designed to scan and aggregate millions of rows fast.
- It reads Parquet, CSV, and JSON directly—even from remote URLs—with no import or server setup step.
- A common confusion: the headline features (AES-256 encryption, `MERGE INTO` upserts, Apache Iceberg writes) shipped in **v1.4** (September), not v1.5.
- v1.4 was also DuckDB's first long-term support (LTS) release, marking its transition from query engine to a database you can trust with real data on a single machine.
- v1.5 (March) added quality-of-life improvements: a colored CLI with pager, a new `variant` type for messy semi-structured data, and core geometry support.
- The `variant` type lets you store mixed types (integers, strings, arrays, objects) in one column without a schema, as typed binary that compresses and queries better than plain JSON.
- `MERGE INTO` enables clean, single-statement upserts—work that previously required Spark or custom Python.
- Encryption is AES-256 at the page level, but strictly "bring your own key": DuckDB doesn't store, manage, or rotate keys; lose the key and your data is gone.
- Compared to SQLite (row store/transactions), Pandas (no SQL optimizer), and Snowflake/BigQuery (cloud, team-scale, petabytes), DuckDB is a free, single-machine, in-process column store.
- Main limitations: can run out of memory on very large datasets, single-writer (not a transactional backend), and Iceberg writing is still a new extension.

## Detailed Breakdown

### The pitch: a free local database that grew up [00:00](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=0s)
The video opens by challenging the default advice to spin up Snowflake or BigQuery the moment data outgrows a spreadsheet. DuckDB is presented as a tiny, free, laptop-based database that matured quietly while everyone focused on the cloud. It now has real encryption, git-style upserts, and its first long-term support release.

### DuckDB explained: SQLite for analytics [00:35](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=35s)
DuckDB is framed as "SQLite but for analytics"—same one-file, no-server, embedded model, but built for scanning and aggregating large row counts rather than transaction processing. A standout feature is direct reading of Parquet, CSV, and JSON files with no import step.

### Live demo: SQL on a remote Parquet file [01:06](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=66s)
The presenter drops into a terminal, types `duckdb`, and immediately runs SQL against a Parquet file hosted at a remote URL. No download, no server, no setup—DuckDB streams the remote file and executes SQL in a single line, illustrating why developers love the tool.

### The version confusion: 1.4 vs 1.5 [01:37](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=97s)
A key correction: the internet keeps blurring two releases together. The marquee features—AES-256 encryption, `MERGE INTO` for git-style upserts, and Apache Iceberg table writes—all shipped in **v1.4** in September, which was also DuckDB's first long-term support release. v1.5 arrived in March as an incremental update on top of 1.4.

### v1.5 highlights: CLI, variant type, geometry [02:09](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=129s)
v1.5 brought a nicer command-line client with colors and a pager, a new `variant` type for messy semi-structured data, and geometry baked into the core. The presenter keeps the earlier Parquet query and begins demonstrating the 1.4-plus-1.5 feature set in practice.

### The variant type in action [02:42](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=162s)
The new `variant` type is demonstrated by creating a table and inserting mixed types—integers, strings, arrays, and objects—into the same column with no schema and no JSON parsing. It stores typed binary data, which compresses and queries better than plain JSON.

### `MERGE INTO` and encryption [03:13](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=193s)
`MERGE INTO` (from v1.4) is shown as a single clean SQL statement for upserts, replacing logic that used to require Spark or custom Python. Encryption is demonstrated next: the file queries normally with the key, but opening it in a new session without the key fails as expected. It's AES-256 at the page level, and DuckDB never stores or manages the key.

### Why 1.4 was the milestone [03:45](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=225s)
1.4 is called the big update because it turned DuckDB from a query engine into something trustworthy for real data on a single machine: secure files, reliable upserts, and modern lakehouse formats. 1.5 improved the experience with a better CLI and the variant type. The presenter notes some users may prefer the `spatial` extension over core geometry support.

### How DuckDB compares to existing tools [04:15](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=255s)
SQLite is a row store for transactions; DuckDB is a column store for analysis. Versus Pandas, DuckDB offers a real SQL optimizer and multi-threaded joins, often faster on big group-bys. Versus Snowflake or BigQuery—cloud warehouses for teams and petabytes—DuckDB is one machine running in your own process, for free.

### Limitations and when not to use it [04:46](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=286s)
The number-one complaint is memory: point DuckDB at a billion rows and it can exhaust memory and fail, making it potentially too flaky for some production scenarios. It's also single-writer, not a transactional backend—that's still PostgreSQL's job, or SQLite for small MVPs. Encryption is bring-your-own-key with no rotation or recovery. Iceberg writing lives in a still-new extension.

### Final verdict: right tool for the right job [05:19](https://www.youtube.com/watch?v=dKbV8MEzVPA&t=319s)
For analytics—crunching Parquet/CSV, running ELT transforms, exploring data in notebooks, up to single-machine scale—DuckDB is one of the best free (MIT-licensed, no paywall) tools available. But if you need a transactional app backend or routinely query billions of rows without hand-tuning memory, pick a different tool. Right database for the right job.

## Notable Quotes
- "Duck DB, just think SQLite but for analytics."
- "You just point SQL at the file."
- "There are two releases in play here and the internet keeps blurring them together."
- "1.4 was the big update. It went from a query engine to something you can actually trust with real data on a single machine."
- "You lose the key, your data is gone."
- "Right database for the right job."

## People, Tools & References Mentioned
- **DuckDB** — the featured embedded analytical database (MIT licensed)
- **SQLite** — embedded transactional database used as a comparison
- **Snowflake** — cloud data warehouse, used as contrast
- **BigQuery** — cloud data warehouse, used as contrast
- **Pandas** — Python data library, used as contrast
- **PostgreSQL** — recommended for transactional app backends
- **Apache Spark** — referenced as tooling `MERGE INTO` replaces
- **Apache Iceberg** — lakehouse table format; writing supported via DuckDB extension
- **Parquet, CSV, JSON** — file formats DuckDB reads directly
- **AES-256** — page-level encryption standard used by DuckDB
- **DuckDB v1.4** — September release; first LTS; encryption, `MERGE INTO`, Iceberg writes
- **DuckDB v1.5** — March release; improved CLI, variant type, geometry support
- **`spatial` extension** — alternative to core geometry support
- **Better Stack** — the channel producing the video

## Who Should Watch
Data engineers, analysts, and developers who work with Parquet/CSV data, run ELT transforms, or explore data in notebooks on a single machine and want a fast, free, embedded SQL engine. It's also useful for anyone confused about what DuckDB's recent releases actually delivered and where the tool's limits are.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=0s">00:00</a></span> For years, the moment our data outgrew a spreadsheet, the advice never changed. Go spin up a cloud data warehouse, Snowflake or Big Query. But there&#x27;s this tiny free database that runs entirely on your laptop. And while everyone was staring at the cloud, it quietly grew up. It now has real encryption, git style upserts, and its first ever long-term support release. This is Duck DB and I want to show you exactly how it stacks up in 2026, including the one big thing that people keep getting wrong about it.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=35s">00:35</a></span> So, Duck DB, just think SQLite but for analytics. You know, SQLite, one file, no server, embedded right inside your app. Duct DB is that exact same idea except instead of being built for transactions, it&#x27;s built for crunching numbers. It&#x27;s built to scan and add up millions of rows really fast. And one of the best parts is it reads parquet, CSV, and JSON files directly. There&#x27;s no import step, no load the data first. You</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=66s">01:06</a></span> import step, no load the data first. You just point SQL at the file. Let me show you what that feels like. If you enjoy coding tools that speed up your workflow, be sure to subscribe. We have videos coming out all the time. Now, here in my terminal, I type duck DB and I&#x27;m sitting in a SQL prompt instantly. Now, watch this. I select from a parket file that lives on a URL out on the internet. I didn&#x27;t download it. I didn&#x27;t define anything or start a server. Duct DB reached out, streamed a remote file, and ran real SQL on it in a single line.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=97s">01:37</a></span> and ran real SQL on it in a single line. That right there in 5 seconds is a reason people love this. But here is the thing people are getting wrong. There are two releases in play here and the internet keeps blurring them together. The big exciting features everyone&#x27;s talking about full AES 256 encryption of your database, a merge into command for git style upserts and the ability to write Apache iceberg tables. None of those are in 1.5. They all shipped in ductb 1.4 in September, which was also ductb&#x27;s very first long-term support</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=129s">02:09</a></span> ductb&#x27;s very first long-term support release. Then 1.5 this past March, we got the updated version of that. A nice new command line client with colors and a pager, a new variant type for messy semistructured data and geometry baked right into the core. Instead of just one quick query, let me show you what the updated duct DB actually feels like in practice. The 1.4 features plus 1.5 on top of that. Now I still have the parquet query we saw earlier right here. Now, here is the new feature in 1.5, the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=162s">02:42</a></span> Now, here is the new feature in 1.5, the variant type. I create a quick table and insert mixed types, integers, strings, arrays, and objects all in the same column. There&#x27;s no schema, no JSON parsing. It just works. And it stores typed binary data which compresses and queries better than plain JSON. That is the new variant feature. Next up is the feature that actually changed what you can build with DOC DB. merge into this is from 1.4 4. Don&#x27;t confuse that. One clean SQL statement. There&#x27;s no app</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=193s">03:13</a></span> clean SQL statement. There&#x27;s no app logic. This is the kind of thing that used to require Spark or custom Python. Then the encryption piece as well since here we are. I can query it normally. But if I try to open the same file in a new session without the key, it fails exactly as it should. AES 256 at the page level. You bring the key. Duct DB doesn&#x27;t store it or manage it. And that&#x27;s before we even get into iceberg writing or geometry support, which a lot of you guys might just use spatial instead of geometry. This is why 1.4 was</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=225s">03:45</a></span> instead of geometry. This is why 1.4 was the big update. It went from a query engine to something you can actually trust with real data on a single machine. Secure files, reliable upserts, and the modern lakehouse formats. 1.5 just made the experience a lot better with improved CLI, and the new variant type. Okay, so how is this different from the tools already on your machine? Let&#x27;s take SQL light. Same one file, no server feeling. But SQL light is a row store built for transactions. And duct DB is a column store built for analysis.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=255s">04:15</a></span> DB is a column store built for analysis. Then we could take pandas. Duct DB hands you a real SQL optimizer and multi-threaded joins. So on a big group buy, it&#x27;s often a little bit faster. Then if we took snowflake or big query, those are cloud warehouses built for entire teams and pabytes of data. Duct DB is one machine running inside your own process for free. Now, the number one complaint over and over and over again is memory. Point Duck DB at a billion rows and it can run clean out of memory and fall over. It might be a bit</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=286s">04:46</a></span> memory and fall over. It might be a bit too flaky for production, too, if that&#x27;s what you&#x27;re dealing with. The second thing is this is not a transactional database. It&#x27;s a single writer. One process writes at a time. So, you don&#x27;t wire it up on your app&#x27;s back end or your session store. That&#x27;s still Postgress&#x27;s job or SQLite for small MVPs. And that whole encryption part, it&#x27;s real, it&#x27;s thorough, but it&#x27;s bring your own key. Duct DB does not store the key. It does not rotate the key. It doesn&#x27;t watch anything. You lose the key, your data is gone. And the iceberg</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=319s">05:19</a></span> key, your data is gone. And the iceberg writing lives in an extension that&#x27;s still pretty new. If you&#x27;re doing analytics, crunching parquet and CSV, running ELT transforms, exploring data in a notebook, anything with a few megabytes up to a single machine scale, DUTDB is one of the best tools you can possibly install, and it&#x27;s completely free, MIT licensed with no payw wall. But if you need a transactional backend for an app or you&#x27;re routinely firing billions of rows and you don&#x27;t want to handtune memory, this is the wrong tool and that&#x27;s fine. Right database for the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=dKbV8MEzVPA&amp;t=351s">05:51</a></span> and that&#x27;s fine. Right database for the right job. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack Chick. We&#x27;ll see you in another video.</p>

</details>
