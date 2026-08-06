---
title: "Postgres Is Releasing An Incredible New Feature"
channel: "Better Stack"
video_id: _0A2BnRYVCo
url: https://www.youtube.com/watch?v=_0A2BnRYVCo
published: 2026-08-06T08:00:37+00:00
generated: 2026-08-06T10:48:12+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/_0A2BnRYVCo/hqdefault.jpg
---
# Postgres Is Releasing An Incredible New Feature

[![Postgres Is Releasing An Incredible New Feature](https://i.ytimg.com/vi/_0A2BnRYVCo/hqdefault.jpg)](https://www.youtube.com/watch?v=_0A2BnRYVCo)

[Watch on YouTube](https://www.youtube.com/watch?v=_0A2BnRYVCo) · **Better Stack** · 2026-08-06

## TL;DR
Postgres 19 is bringing a slate of powerful new features, headlined by native graph query support that lets developers traverse complex relationships without writing massive SQL joins. The release also introduces atomic "upsert-and-return" syntax, built-in table repacking for disk space reclamation, and a quick-fire list of quality-of-life improvements like query plan pinning and direct JSON exports.

## Key Takeaways
- **Graph queries are the headline feature:** Postgres 19 introduces a `CREATE PROPERTY GRAPH` syntax that lets you model existing tables as vertices and edges, allowing you to query complex relationships without long join chains.
- **No schema changes required:** The new graph functionality works like a view on top of your existing tables; it doesn't create new tables or alter your current schema.
- **Atomic "upserts" simplified:** The new `ON CONFLICT DO SELECT` (and `DO SELECT FOR UPDATE`) syntax allows you to insert a row or return the existing row in a single, atomic statement.
- **Built-in table repacking:** Postgres 19 introduces `REPACK`, which rewrites tables to reclaim disk space, functioning like `VACUUM FULL` but without locking the table when used with the `CONCURRENTLY` keyword.
- **Query plan control:** A new module called `PG_PLAN_ADVICE` lets you capture and pin a fast query plan so it doesn't suddenly slow down if the Postgres planner changes its mind.
- **JIT is now off by default:** Just-In-Time compilation was turned off by default because the planner's cost estimates for when to use it were unreliable.
- **Parallel vacuuming and JSON exports:** Vacuum can now clean indexes with multiple parallel workers, and the `COPY` command can now export directly to JSON.
- **Release timeline:** Beta 2 landed in July, with the final release expected around September or October.

## Detailed Breakdown

### On Conflict Do Select [00:30](https://www.youtube.com/watch?v=_0A2BnRYVCo&t=30s)
The video begins with a common developer workflow: inserting a row only if it doesn't already exist and returning the row either way. Previously, this required an `INSERT ... ON CONFLICT DO NOTHING` followed by a `SELECT`, which was not atomic. Postgres 19 solves this with the `ON CONFLICT DO SELECT` clause. You can also use `ON CONFLICT DO SELECT FOR UPDATE` if you want to modify the row in the same atomic statement.

### Native Graph Queries [01:33](https://www.youtube.com/watch?v=_0A2BnRYVCo&t=93s)
The presenter highlights graph queries as the standout feature of Postgres 19. Using a standard e-commerce schema (customers, orders, products, and pivot tables), they demonstrate how finding what a customer bought normally requires a query with four separate `JOIN` statements. While functional, this syntax is ugly and hard to scale. With the new graph syntax, the query is massively simplified into a readable flow that traces the path from customers through the pivot tables to products.

### Creating a Property Graph [03:36](https://www.youtube.com/watch?v=_0A2BnRYVCo&t=216s)
To use graph queries, you must first define the graph using the `CREATE PROPERTY GRAPH` command. The presenter shows how to name the graph (e.g., "my shop") and define the "vertex tables" (the tables holding the data, like customers, orders, and products) and the "edge tables" (the pivot/join tables making the connections). The syntax is simple: you define the source and destination for each edge. Crucially, this acts like a view—it points at your existing tables without creating new ones or changing your underlying schema.

### Is This a Neo4j Replacement? [04:38](https://www.youtube.com/watch?v=_0A2BnRYVCo&t=278s)
The video addresses whether this new feature replaces dedicated graph databases like Neo4j. The answer is nuanced: if you need raw graph storage and high-performance graph traversal, a dedicated graph database is still the better choice. However, if you simply want to avoid writing painful, 10-table SQL joins, Postgres 19's graph syntax is a massive quality-of-life improvement.

### Built-in Repack [05:09](https://www.youtube.com/watch?v=_0A2BnRYVCo&t=309s)
Postgres never updates a row in place; it writes a new version and leaves the old one behind. While `VACUUM` marks this dead space as reusable, it doesn't lower disk usage. `REPACK` rewrites the table into a fresh file without wasted space, returning disk to the OS. Unlike `VACUUM FULL`, which locks the table, `REPACK` can be used with the `CONCURRENTLY` keyword to keep the table readable and writable. You do need enough free disk space for a second copy of the table and its indexes.

### Quick-Fire Feature Round [06:11](https://www.youtube.com/watch?v=_0A2BnRYVCo&t=371s)
The video closes with a rapid rundown of remaining features:
- **Query Hints (`PG_PLAN_ADVICE`):** Capture a fast query plan and pin it so the planner doesn't suddenly change to a slow plan.
- **JIT Off by Default:** Just-In-Time compilation is now off because the planner's cost estimates for triggering it were unreliable.
- **Parallel Vacuum:** Vacuum can now clean indexes with multiple parallel workers (must be manually enabled).
- **Smarter Group By:** Postgres will now automatically infer `GROUP BY` columns when they are already in the `SELECT` clause.
- **JSON Export:** The `COPY` keyword can now export directly to JSON, eliminating the need to dump CSV and convert it.

## Notable Quotes
- "So, it turns out all of those developers saying, 'Oh, bro, just use Postgres for everything.' are even more correct with the upcoming release of Postgres 19, which includes native support for graph queries."
- "You just point it at the five tables you've already got. The three that actually hold the data become vertices, and the two join tables become the edges. It works much more like a view, so your previous schema remains completely unchanged."
- "If you want a graph database because you needed graph storage and traversal performance, then no... But if you want this because writing 10 table joins in SQL is painful and ugly, then it's definitely going to benefit you."

## People, Tools & References Mentioned
- **Postgres 19** (upcoming release)
- **Neo4j** (dedicated graph database)
- **pg_repack** (Postgres extension for table repacking)
- **VACUUM FULL** (existing Postgres command)
- **PG_PLAN_ADVICE** (new module for query plan pinning)
- **PG Durable** (mentioned as a related Better Stack video topic)
- **Better Stack** (channel/creator)

## Who Should Watch
This video is ideal for backend developers, database administrators, and software architects who currently use PostgreSQL and want to understand how the upcoming version 19 will simplify complex queries, improve database maintenance, and offer new tools for performance tuning.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=0s">00:00</a></span> So, it turns out all of those developers saying, &quot;Oh, bro, just use Postgres for everything.&quot; are even more correct with the upcoming release of Postgres 19, which includes native support for graph queries. And this is a really cool feature. So, in today&#x27;s video, I want to cover all of the headline features for Postgres 19, and also take a deeper look at graph queries specifically, because I think it can fundamentally change the way that we design our queries and use Postgres.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=30s">00:30</a></span> So, the first one up is something called on conflict do select. If you want to insert a row only if it does not already exist, and either way you want to return that row back as a result, usually you&#x27;d need two queries for this, an insert and a select. And this is a really common workflow. So, here in the example, we say we&#x27;re going to insert into users email and name, and then we give those values, and then at the end we say on conflict for email do nothing returning star. Do nothing gives you nothing back when the row already exists, so you follow it up with a select, but together this is not atomic. With 19, you can do</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=62s">01:02</a></span> this is not atomic. With 19, you can do this with just one query. Insert into users given the email and name, and then we say on conflict email do select returning star. And if you want to modify in the same query, we can say insert into users and then we give the values again, on conflict for the email do select for update returning ID and name. And because it&#x27;s a single statement, it&#x27;s atomic. You either insert it or you select it every single time. And this is such a common use case, it&#x27;s going to be really useful. So, next up is graphs, but if you&#x27;re</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=93s">01:33</a></span> So, next up is graphs, but if you&#x27;re enjoying this, then why not subscribe to Better Stack to stay up to date with the latest in tech. Now, as I said before, this is the headline feature in my opinion. So, say you&#x27;ve got the usual schema for a shop, you&#x27;ve got customers, orders, and products, plus the two join tables that wire them all together, and you want to know which product a given customer actually bought. In SQL, it&#x27;s a chain of joins across all five tables, and that&#x27;s pretty manageable here, but it does get pretty ugly quickly for more complex relationships. Well, now we can query all of this as a graph, so that</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=124s">02:04</a></span> query all of this as a graph, so that complex join syntax now becomes a new graph syntax instead. And with complex joins in particular, you&#x27;re going to see a really big benefit here. So, we&#x27;re inside our database viewer here, and you can see we&#x27;ve got all of our tables. We&#x27;ve got products, orders, events. We&#x27;ve got customers as well, and then we have the pivot tables to connect all of this data. So, we&#x27;ve got order items and customer orders. And now let&#x27;s try and run a query against all of these tables. So, say for example, I&#x27;ve got this user here called Alice, and I want to work out all of the things that Alice has</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=154s">02:34</a></span> out all of the things that Alice has ordered. To do this, I&#x27;d have to go through a bunch of different join queries to connect up all of those tables. So, I&#x27;d run this query which has got four separate join statements within it, and whilst this is not necessarily hard to write, it is very ugly. But if we run this, you can see that we can see all of the things Alice has ordered, a mechanical keyboard, and ergonomic mouse. But now we can use graph syntax to massively simplify this. So, we&#x27;ll replace all of this with the new graph syntax, and we&#x27;ll execute this again, and you can see we get the same results. And if we line all of this up, it starts</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=186s">03:06</a></span> And if we line all of this up, it starts to become easier to read. So, you can see we&#x27;re just going from customers to customer orders to orders to order items to products. So, you can basically just follow this simple flow to get through the entire graph, which in my opinion is much much easier to read. If you want to select multiple columns as well, we can do that. We have the same graph query at the top here, but then we can define columns at the bottom, and then we select all the columns that we want to display. And executing that, we get the results at the bottom. Now, none of this will work unless we&#x27;ve actually created the graph in the first place. So, the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=216s">03:36</a></span> the graph in the first place. So, the query that I&#x27;ve used to generate that graph is here. We say create property graph, and then we give it a name, my shop, and then we outline the vertex tables, which is going to be customers, orders, and products. So, these are the things that actually hold the data. And then we have the edge tables, and these are the things that actually make the connections, so the pivot tables in our case. Those would be customer orders and order items. And the syntax for this is super simple. We say for customer orders, the source is customers and the destination is orders. And for order items, the source is orders and the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=246s">04:06</a></span> items, the source is orders and the destination is products. And with that in place, Postgres will now be aware every time we run a graph query of how those relationships are defined. For this to work, you need to create a graph, but this doesn&#x27;t create new tables or anything. You just point it at the five tables you&#x27;ve already got. The three that actually hold the data become vertices, and the two join tables become the edges. It works much more like a view, so your previous schema remains completely unchanged. You just get this added functionality on top. So here we&#x27;re going to say create property graph, we&#x27;ll call it my shop, and then</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=278s">04:38</a></span> graph, we&#x27;ll call it my shop, and then we start to describe how that relationship actually works. And this is where we&#x27;re doing all the work for the graph, and it means that the queries can be much much thinner than the respective join syntax. So is this a Neo4j replacement? Well, if you want a graph database because you needed graph storage and traversal performance, then no, and a dedicated graph database is still probably the better choice. But if you want this because writing 10 table joins in SQL is painful and ugly, then it&#x27;s definitely going to benefit you, and it&#x27;s going to be much nicer in</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=309s">05:09</a></span> and it&#x27;s going to be much nicer in comparison. The third new feature is repack, and this one&#x27;s about getting disk space back. Postgres never updates a row in place. It writes a new version and leaves the old one behind, and vacuum only marks that dead space reusable. So your disk usage never actually comes down. Repack rewrites the whole table into a fresh file with none of the wasted space in it, and that&#x27;s what hands the space back to the operating system. You could actually already do this with vacuum full, but that locks the table for the entire rewrite. So for anything massive, you</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=340s">05:40</a></span> rewrite. So for anything massive, you just never run it, and that&#x27;s why people would install extensions like pg_repack, but now we get it built into Postgres directly. Use the concurrently keyword with this, and it keeps the table readable and writable while repack works. One thing to watch here, though, you need enough free disk space for a second copy of the table and all of its indexes, so you need the spare space to actually reclaim more space. So, this is not an exact replacement for a PG repack, but for a normal table, it does the job without the extension. Okay, now we&#x27;re going to do a quick fire round for</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=371s">06:11</a></span> we&#x27;re going to do a quick fire round for the remaining features in the 19 release. First up is query hints. Postgres decides how to actually run your query, and it can change its mind over time, so a query that&#x27;s been fine for a year suddenly gets slow, and nothing in your code changed. A new module called PG plan advice lets you capture the plan while it&#x27;s still fast and pin it, so it always stays that way. JIT is now off by default. Postgres compiles heavy queries down to machine code, but it decided when to bother from the planner&#x27;s cost estimate, and the release notes say that that costing was</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=403s">06:43</a></span> release notes say that that costing was actually unreliable. So, it was firing on queries that didn&#x27;t actually need it. Also, vacuum can now clean up your indexes with several workers in parallel, so that&#x27;s less time spent vacuuming a big table. You do have to turn this on yourself, though. You know when you add a column to do a select, and then you have to add the same column to the group by as well? It does all of that for you. And the copy keyword can now export straight to JSON, so if you&#x27;ve been dumping CSV and converting it afterwards, you can stop doing that. So, that&#x27;s Postgres 19. Beta 2 landed in</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=_0A2BnRYVCo&amp;t=434s">07:14</a></span> So, that&#x27;s Postgres 19. Beta 2 landed in July, and the final release is expected around September or October. So, if you&#x27;re running anything older, it&#x27;s worth pulling the beta down and testing against it now. And if you want to see more about Postgres, you can actually check out our breakdown of PG durable. It puts durable workflows directly inside Postgres. I&#x27;ve been Warren from BetterStack. Thank you for watching, and I&#x27;ll see you in the next one.</p>

</details>
