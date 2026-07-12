---
title: "Postgres Just Got It's Biggest Upgrade In Years"
channel: "Better Stack"
video_id: 4Lmqvn_yz-c
url: https://www.youtube.com/watch?v=4Lmqvn_yz-c
published: 2026-07-10T18:00:09+00:00
generated: 2026-07-12T21:42:35+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/4Lmqvn_yz-c/hqdefault.jpg
---
# Postgres Just Got It's Biggest Upgrade In Years

[![Postgres Just Got It's Biggest Upgrade In Years](https://i.ytimg.com/vi/4Lmqvn_yz-c/hqdefault.jpg)](https://www.youtube.com/watch?v=4Lmqvn_yz-c)

[Watch on YouTube](https://www.youtube.com/watch?v=4Lmqvn_yz-c) · **Better Stack** · 2026-07-10

## TL;DR
PG Durable is an open-source PostgreSQL extension by Microsoft that brings durable, crash-proof functions directly into the database, enabling scheduled jobs, automatic retries, long-running workflows, and human-in-the-loop approvals without any external services. The video demonstrates how to replace hundreds of lines of boilerplate code with concise SQL using built-in operations for sequencing, parallelism, waiting, and signaling.

## Key Takeaways
- PG Durable is a Microsoft-developed, open-source PostgreSQL extension that persists functions to disk at every step, making them crash-proof and durable.
- It enables managing scheduled jobs, automatic retries, long-running processes, and human-in-the-loop workflows entirely inside PostgreSQL—no external services required.
- Durable functions are submitted via the `df_start` function, which returns an 8-character ID for tracking status (`df_status`) and retrieving results (`df_result`).
- Built-in operations include running steps in sequence, in parallel, or racing operations to return the fastest result.
- The `df.wait` function supports cron expressions, allowing scheduled jobs to run natively in Postgres without third-party cron systems.
- A looping schedule demo shows a one-minute recurring job that waits, then calls a procedure to insert a log entry—running permanently as long as the script is active.
- A human-in-the-loop approval workflow demonstrates waiting for a signal (up to 24 hours) from a human before updating an order's status to approved or rejected.
- The `df_signal` function wakes a parked workflow when external approval is given.
- PG Durable can reduce 300 lines of boilerplate SQL (queue setup, worker management, polling, error handling, retries) down to just 7 lines.
- Error handling and retries are handled automatically, which is a major reason for the dramatic code reduction.

## Detailed Breakdown

**[00:00] Introduction to PG Durable**
The video opens by announcing a major upgrade to PostgreSQL: durable, crash-proof functions inside the database. PG Durable, an open-source extension developed by Microsoft, allows users to manage scheduled jobs, automatic retries, long-running processes, and workflows like human-in-the-loop approvals—all without external services. The host promises a hands-on demo, including setting up scheduling directly in Postgres.

**[00:30] What Durable Functions Provide**
Durable functions in PG Durable are persisted to disk at every step, offering guarantees beyond a plain `BEGIN`/`COMMIT` block or a cron job. This means database crashes, restarts, long waits, and failures can all be managed natively inside Postgres.

**[01:01] Core Concepts and API**
A durable function is a graph of steps submitted via SQL using the `df_start` function. A simple example wraps `SELECT 'hello world'` inside `df_start`, returning an 8-character ID. That ID can be passed to `df_status` to check operation status or `df_result` to retrieve the final output. PG Durable also includes built-in operations for sequencing, parallelism, racing operations, and `df.wait` for cron-based scheduling.

**[02:02] Demo: Scheduled Job Loop**
The first demo sets up a permanent one-minute schedule using `df_start` with a `loop` operation. Inside the loop, a `sequence` operation first waits one minute (`df.wait`), then calls a procedure (`refresh_materialized_views`) that inserts a row into a `refresh_log` table. After running the script, the host queries the table and observes multiple log entries accumulating, confirming the loop runs indefinitely on a one-minute cadence.

**[03:05] Demo: Human-in-the-Loop Order Approval**
The second demo demonstrates a workflow for approving orders with human intervention. The workflow selects the top order, stores it in a variable, then waits for a human approval signal (up to 24 hours). An `if` conditional checks whether approval was granted and not timed out; if so, the order status is set to approved, otherwise rejected. The host runs the workflow script, observes the order in `pending` status, then runs a separate approval script that uses `df_signal` to wake the parked workflow, which updates the status to `approved`.

**[04:40] Running Locally with Docker Compose**
The host briefly walks through the Docker Compose configuration for running the examples locally. It uses Microsoft's PG Durable image running Postgres 17, with `shared_preload_libraries` set to `pg_durable`. The rest of the config is customizable, and the setup runs a Postgres database with the extension enabled.

**[05:10] Code Reduction Example**
The video highlights a comparison from the PG Durable site: 300 lines of boilerplate SQL (handling queue setup, worker management, polling, message handling, state tracking, error handling, and retries) reduced to just 7 lines using PG Durable. The concise version runs three operations in parallel (using the `&` character) and then sequences a dashboard refresh. The reduction is possible not only because of new operations but also because error handling and retries are automatic. The host closes by pointing viewers to links in the description for deeper exploration.

## Notable Quotes
- "A durable function in PG Durable is persisted to disk every step of the way. That gives you a specific set of guarantees you don't get from a plain begin commit block or a cron job."
- "This is 300 lines of boilerplate which can then be reduced down to just seven lines with PG Durable."
- "Things like error handling and retries are handled automatically inside PG Durable."

## People, Tools & References Mentioned
- **PG Durable** — open-source PostgreSQL extension by Microsoft
- **PostgreSQL 17** — the database version used in the demo
- **Docker Compose** — used to run the local demo environment
- **Microsoft** — developer of the PG Durable extension
- **Warren (Better Stack)** — video host
- **Better Stack** — YouTube channel publishing the video
- Functions referenced: `df_start`, `df_status`, `df_result`, `df.wait`, `df_signal`
- Operations referenced: `loop`, `sequence`, parallel (using `&`), `if`

## Who Should Watch
Backend developers and database administrators who want to eliminate external job schedulers, workflow engines, or retry systems and instead manage long-running, crash-proof workflows directly inside PostgreSQL. It's especially valuable for teams already invested in Postgres who want to simplify their infrastructure and reduce boilerplate code.


<details class="transcript">
<summary>Full transcript</summary>

<p>Everyone&#x27;s favorite database just got a huge upgrade. Durable crash proof functions inside Postgress. You can now manage scheduled jobs, automatic retries or long running processes and workflows like human in the loop approval all with no external services. This is PG Durable, an open- source Postgress extension developed by Microsoft. Today we&#x27;ll cover exactly what PG durable is and even run through some examples like setting up scheduling directly into Postgress so you can ditch whatever</p>
<p>Postgress so you can ditch whatever external service you are using. And we cover a huge amount of developer content on this channel. So if you want to stay up to date then subscribe. A durable function in PG durable is persisted to disk every step of the way. That gives you a specific set of guarantees you don&#x27;t get from a plain begin commit block or a cron job. And this means operations like database crashes and restarts, long weights and failures can now be managed directly inside Postgress. So let&#x27;s dive into</p>
<p>inside Postgress. So let&#x27;s dive into exactly how all of this works. PG durable provides durable functions which are just a graph of steps you submit with SQLDS and then submit with the DF start function. So here&#x27;s a super simple example just to explain the concepts. If we take SQL like select hello world, this would just return to us the string hello world. But now we can run it as select df start select hello world. Obviously this would benefit from long running processes. But what we get back from this is an 8 character ID we can pass to the df status function. This</p>
<p>pass to the df status function. This would just give us the operation status or we can use df result to give us the final output from the operation once it&#x27;s complete. So you can see straight away how this would be valuable for long running tasks or for tasks that require an approval step. PG durable also comes with a bunch of built-in operations like running multiple operations in sequence, running multiple operations in parallel or racing operations to return the fastest. We also have a bunch of built-in functions including df.weight for schedule to wait on cron expressions. Using this we could run</p>
<p>expressions. Using this we could run schedule jobs without any third party systems. So let&#x27;s jump straight into a demo to show you how it&#x27;s done. So in this example here, we&#x27;re setting up a schedule. We&#x27;re calling select with the DF start function. And then inside this, we&#x27;re using the loop operation. So that means this will just loop around forever on a minute schedule. So every single minute. And then here we&#x27;re using the sequence operation. So we&#x27;re saying first we&#x27;ll wait for 1 minute. Then after that task is completed, we&#x27;re going to call our procedure which is called refresh materialized views. You could just call any SQL here, but in our</p>
<p>could just call any SQL here, but in our case, we&#x27;ll call call in a procedure. This in our case will insert into a table called refresh log and it&#x27;s just going to insert the value weekday refresh. So if we run this, you can see first the original DF start operation runs and then we get an ID coming back from that. So then we can just watch the logs fill up inside that table by running this SQL here. Select id from refresh log and then we&#x27;ll ordering by the ID. So you can see now that&#x27;s fired a couple of times. And if we head into our database client and refresh this, you can see now we&#x27;ve got three logs</p>
<p>you can see now we&#x27;ve got three logs inside the database because this is now running on a permanent loop. So as long as this script is running, this will just loop around forever and insert data into our table on a one minute schedule. In the next example, we&#x27;ll run through a workflow that can approve orders with human in the loop approval. So again, we&#x27;re using select DF start. So the first thing that we&#x27;re going to do is just to run this SQL here, which is just going to select the top order in our database. And then this is the variable assignment command. So the result of this will be stored inside the variable order. Then this is the sequence</p>
<p>order. Then this is the sequence command. We&#x27;ll say once we&#x27;ve got the order, we&#x27;re going to then wait for the signal of approval from a human. This will then be stored in the sig variable and it will wait up to 24 hours. Again, we use the sequence operation and then we&#x27;re using the if function. And we&#x27;re basically saying if the approval didn&#x27;t time out and the user approved it, then we can update the order status as approved. Otherwise, we update it as rejected. So, if we run this script in the first terminal, npm run workflow. You can see that we execute the SQL, we get an ID back. And now we&#x27;re waiting on</p>
<p>get an ID back. And now we&#x27;re waiting on approval from our second script. So, if we look inside the database at this point, you can see we have an order and the status is set to pending. And then if we run our approval script, the status now has switched to approved. The first script then exits because the approval has now happened. And you can see inside this SQL when we actually made the approval, we&#x27;re using the DF signal function which wakes the parked workflow to then approve the record in the database. Now, if you want to run all of this yourself, I&#x27;ll just quickly go over the Docker Compose file. So, you can run it all locally. So, here inside my Docker Compose file, I&#x27;m using the PG</p>
<p>my Docker Compose file, I&#x27;m using the PG durable image from Microsoft, which is running Postgress 17 because this of course includes the PG durable extension. You can see further down as well inside commands, we&#x27;re using the shared preload libraries set to PG durable, but other than that, the rest of the config can just be customized as you like it. This will then run a Postgress database with the PG durable extension running. So you can then run any of these examples locally yourself. There are also a bunch of cool examples on the PG durable site like this example showing you how to replace 300 lines of</p>
<p>showing you how to replace 300 lines of SQL with a single sevenline SQL statement. So you can see here on the left without PG durable we have 300 lines of boiler plate which do things like Q setup and configuration, worker management and polling, message handling and state tracking, error handling and retries and it carries on. This is 300 lines of boilerplate which can then be reduced down to just seven lines with PG durable. This will first run three operations in parallel using the amperand character and then we&#x27;re going to use the sequence character to then</p>
<p>to use the sequence character to then refresh the dashboard. Now, this is so concise, not just because of the new operations we got access to, but also because things like error handling and retries are handled automatically inside PG Durable. And if you want to dive deeper into PG Durable, check out the relevant links in the video description. I hope you enjoyed that one, guys. I&#x27;ve been Warren from Better Stack. Thanks for watching and I&#x27;ll see you next time.</p>

</details>
