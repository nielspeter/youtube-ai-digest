---
title: "A Practitioner's Guide to Graphs - Tim Ainge, Good Collective"
channel: "AI Engineer"
video_id: 3ySF0I5iE_0
url: https://www.youtube.com/watch?v=3ySF0I5iE_0
published: 2026-07-18T21:30:06+00:00
generated: 2026-07-19T03:48:35+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/3ySF0I5iE_0/hqdefault.jpg
---
# A Practitioner's Guide to Graphs - Tim Ainge, Good Collective

[![A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://i.ytimg.com/vi/3ySF0I5iE_0/hqdefault.jpg)](https://www.youtube.com/watch?v=3ySF0I5iE_0)

[Watch on YouTube](https://www.youtube.com/watch?v=3ySF0I5iE_0) · **AI Engineer** · 2026-07-18

## TL;DR
Tim Ainge presents a practitioner-oriented overview of graph data structures and algorithms for AI builders, focusing on how to build well-structured graphs from unstructured text and leverage graph-native algorithms like personalized PageRank, shortest path, and subgraph matching. The talk emphasizes practical patterns that make AI applications smarter, cheaper, and more reliable—without diving into GraphRAG or agent memory graphs.

## Key Takeaways
- Graphs are powerful but not always the right tool; understanding fundamentals reveals genuinely useful, graph-native opportunities.
- Building better graphs starts with giving the extractor a schema (e.g., structured recipe with ingredients and steps) rather than generic triples.
- Ontology-level instructions—like standardizing ingredient names and metric units—are as important as the schema itself.
- Entity matching (e.g., unifying "garlic cloves" and "minced garlic") strengthens relationships across nodes; embedding models enable flexible, pre-unknown matching in hybrid graph+AI approaches.
- Graph queries (e.g., Cypher) make multi-hop traversals far more natural than relational SQL, which becomes unwieldy beyond a few joins.
- Personalized PageRank (PPR) ranks nodes by relationship strength to a starting node; real-world uses include Pinterest recommendations and HippoRAG.
- Shortest path algorithms retrieve explanatory subgraphs as context—useful for codebases, legal citation graphs, and debugging—yielding measurable wins like a 40% reduction in tool calls.
- Subgraph matching enables searching for structural patterns (e.g., decorator pattern, anti-patterns, malicious transaction shapes) without knowing specific node identities up front.
- The talk deliberately skips GraphRAG, agent memory graphs, and schema-less/dynamic graphs, pointing to the presentation pack for further reading.
- Hybrid graph + AI techniques often produce the best results, combining graph structure with embedding-based flexibility.

## Detailed Breakdown

### Introduction & Motivation [00:00](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=0s)
Tim introduces himself from The Good Collective and frames the talk around making AI applications "smarter, cheaper, and more reliable" using graphs. He acknowledges the common experience of being mesmerized by graph visualizations but then falling into a "valley of despair and disillusionment" when GraphRAG or graph databases don't deliver instant payoff. The talk aims to help practitioners get to the other side of that valley by focusing on fundamentals. He explicitly scopes out GraphRAG and agent memory graphs, instead targeting underlying patterns AI builders can use.

### Speed-Running Graph Basics [02:04](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=124s)
A graph consists of nodes (vertices) and edges (relationships) connecting them. Nodes and edges can have types, labels, properties, and direction. This minimal definition is the foundation for everything that follows.

### Extracting Graphs from Unstructured Text [02:35](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=155s)
Tim demonstrates extracting a graph from a wrap pancake recipe using a basic subject-predicate-object triple structure. The agent does an "all right" job, but the resulting graph has problems—it's too unstructured to be genuinely useful.

### Building Better Graphs: Give the Extractor a Schema [03:38](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=218s)
The key improvement is replacing generic triples with a typed schema: a recipe has ingredients, and ingredients have quantities. Using structured outputs, the agent returns a far tidier, more meaningful graph. Extending the schema so recipes also have steps (each step applying a cooking technique) produces an even richer structure. Consistent node and edge types make relationships interrogable.

### Adding Ontology Detail [04:43](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=283s)
Beyond the schema, the ontology specifies extraction instructions—e.g., standardize ingredient names to lowercase and convert units to the metric system. These instructions are as critical to the model as the schema itself, ensuring consistency for downstream matching and conversion.

### Entity Matching: The "Potato, Potato" Problem [05:16](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=316s)
Tim shows duplicate-ish nodes like "garlic cloves," "minced garlic," "cumin," "cumin seeds," and "oil" vs. "vegetable oil." A naive retrospective mapping can unify these, strengthening cross-recipe relationships, but requires knowing all ingredients ahead of time. Embedding models solve this by enabling flexible matching on terms not known in advance—a good example of hybrid graph + AI techniques working together.

### Simple Graph Queries vs. SQL [06:49](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=409s)
A basic query finds all recipes containing garlic. The Cypher graph query is shown alongside a relational SQL equivalent. Tim highlights that SQL quickly becomes unwieldy for multi-hop traversals (5, 10, 20 edges), whereas graph queries handle relationship traversal inherently and more naturally.

### Personalized PageRank (PPR) [07:40](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=460s)
Tim explains PPR via an analogy: a "little dude" runs around the graph marking nodes, teleporting back to the starting node (the "personalized" part), and repeating until worn out. Nodes with more marks have stronger relationships to the start. References include the Pinterest Pixie paper and HippoRAG. PPR shines in dense clusters where importance isn't obvious. A real-world example: finding Miranda v. Arizona as an authoritative landmark case for a Supreme Court case that doesn't directly cite it—discovered purely through the citation graph.

### Shortest Path Algorithms [09:57](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=597s)
When you know two nodes but not the relationships between them, shortest path finds the most direct route. Example: "the checkout code broke after we changed the basket constructor"—the algorithm traverses code-graph edges to return relevant symbols, text, or summaries as context. Variants include K shortest paths, paths through a particular node, and cheapest weighted paths. Tim reports a 40% reduction in tool calls for code search on a .NET codebase using these techniques to identify needed context. Intermediate nodes found this way wouldn't surface via vector search or individual lookups.

### Subgraph Matching: Querying by Shape [10:50](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=650s)
Tim shifts to querying purely on relationships—searching for a structural pattern rather than specific nodes. The example finds a decorator pattern in an eShop codebase: a class that wraps a target class, both implementing the same interface. The query finds a catalog view model service and a cached version. This is powerful for finding patterns, anti-patterns, security issues, malicious transaction shapes, or legal arguments without knowing specific instances up front. Tim calls subgraph matching a "big enabling algorithm" that's hard to replicate with other tools.

### Wrap-Up & Further Reading [13:02](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=782s)
Tim recaps the three main areas covered: navigating paths, ranking importance, and finding patterns. He notes that traditional flow, cost, and search algorithms (common in dependency/network modeling) were skipped as more run-of-the-mill. The presentation pack includes references for prediction, similarity, and clustering—topics edging into GraphRAG and schema-less graph territory that were deliberately excluded but are "where things get super interesting." He closes by hoping the concepts inspire smarter, cheaper, more reliable AI applications.

## Notable Quotes
- "The more I learn about the fundamentals of graph data structures and algorithms, the more interesting opportunities seem to present themselves."
- "With consistent node and edge types, relationships become meaningful and something that we can interrogate or query."
- "These extra instructions are just as important to the title model as the schema is."
- "This is a good example of where graph techniques and AI techniques working in hybrid give us the best result."
- "It's not so much an optimization problem as like a big enabling algorithm. It's something that's just not easy to do with other tools." (on subgraph matching)

## People, Tools & References Mentioned
- **Tim Ainge** — speaker, The Good Collective
- **Brin and Page** — creators of vanilla PageRank (1998)
- **Pinterest Pixie paper** — demonstrates PPR for Pinterest recommendations
- **HippoRAG** — uses graph techniques to link memories to questions and answers
- **Miranda v. Arizona** — landmark case found via citation graph PPR
- **Canvas v. Sheba** — Supreme Court case example
- **Cypher** — graph database query language
- **SQL** — relational query language (used for comparison)
- **eShop** — reference codebase used for subgraph matching examples
- **.NET** — codebase where shortest-path techniques reduced tool calls by 40%
- **Obsidian** — mentioned for its graph vault view
- **GraphRAG, agent memory graphs, schema-less/dynamic graphs** — explicitly scoped out; pointers in presentation pack

## Who Should Watch
AI engineers and application builders who want practical, foundational understanding of how graph data structures and algorithms can complement AI workflows—especially those extracting knowledge from unstructured text and looking beyond vector search for smarter retrieval, ranking, and pattern discovery.


<details class="transcript">
<summary>Full transcript</summary>

<p>Hi, I&#x27;m Tim Angers from The Good Collective and welcome to AI Engineer&#x27;s presentation, a practitioner&#x27;s guide to graphs, how to make your AI applications smarter, cheaper, and more reliable. Graphs have always been a powerful foundation of computer science and they look beautiful. But sometimes they&#x27;re genuinely not the right tool for the job. We&#x27;ve all felt the wonder of a mesmerizing data science graph or ogled the graph view of our Obsidian vault.</p>
<p>vault. It can be tempting to rush into something like GraphRAG or rebuilding our e-commerce shop with a graph database. But often we don&#x27;t see the instant payoff we might have expected. In frustration, many journeys end here in the dust at the bottom of the valley of despair and disillusionment. What&#x27;s on the other side of the valley and how do we get there? That&#x27;s exactly the question that sparked the idea for this talk. Have I nailed all of the answers? Definitely not. But what I&#x27;m finding</p>
<p>But what I&#x27;m finding is that the more I learn about the fundamentals of graph data structures and algorithms, the more interesting opportunities seem to present themselves. Many of these graph native use cases or good fits for graphs are also a lovely complement to many of the search, pattern recognition, retrieval, or knowledge-based problems that are ripe for solving in the AI age. Now, just a quick disclaimer. This talk isn&#x27;t going to go into GraphRAG or agent memory graphs. Not because I&#x27;m throwing shade on those patterns and products, but</p>
<p>patterns and products, but partly because there&#x27;ll be many other talks covering each of those single topics. But more importantly, this talk is for AI builders and I&#x27;d like to focus on the underlying patterns, which may just help you come up with your next big graph-powered AI application. Today, we&#x27;re going to speed run the basics of graphs. Then we&#x27;ll walk through some tips and tricks for building better graphs to get better results. And then we&#x27;ll look at graph native algorithms that leverage a graph and the benefits that they deliver. At each step of the way, we&#x27;ll open with a principle,</p>
<p>a principle, look at an easy example and some code, and then finally, we&#x27;ll reference some real-world examples with real-world benefits. All right, let&#x27;s speed run the basics. What&#x27;s a graph? A graph is something that has nodes, also called vertices, and edges, which I sometimes call relationships, that connect the nodes together. That&#x27;s it. That is the most basic definition of a graph. We can have different types of nodes and edges, which convey more meaning. Uh we</p>
<p>edges, which convey more meaning. Uh we can also put labels on edges and nodes and have properties. And of course, edges can have direction. Now that we&#x27;ve speed run that, a really, really important part of getting good value out of graphs is how we build good graphs. Today, we&#x27;re going to focus on extracting graphs from unstructured text, cuz that&#x27;s a pretty common use case and a pretty popular one at the moment. So, in this example, we&#x27;ve defined a very basic data structure for our graph, a triple,</p>
<p>structure for our graph, a triple, that has a subject, a predicate, and an object, or a node that somehow relates to another node. And we say to our agent, &quot;Hey, go and pull the key information out of this thing as subject, predicate, and object triples. You figure it out.&quot; And then we give it a wrap pancake recipe. It&#x27;s done an all right job. We&#x27;ve got a graph. But, we wouldn&#x27;t get very far with this graph. It&#x27;s got some problems, so we&#x27;ll</p>
<p>graph. It&#x27;s got some problems, so we&#x27;ll talk through that next. One of the key principles about building better graphs is giving the extractor a schema to fill. In this case, if we say, &quot;Instead of using triples, use a recipe. And a recipe has ingredients, and ingredients have a quantity. If we give this to an agent with its structured outputs, what we get back is instantly way more meaningful than the graph we had before, and a lot tidier.</p>
<p>and a lot tidier. So, the benefit here is that with consistent node and edge types, relationships become meaningful and something that we can interrogate or query. Let&#x27;s take this a little bit further to say that a recipe has ingredients, but it also has steps, and each step is the application of a cooking technique. Now, we&#x27;ve got a graph with structure that&#x27;s starting to look a bit interesting. Now that we have a well-defined schema and a nicely structured graph, we need to add detail to our ontology.</p>
<p>we need to add detail to our ontology. The ontology describes how to extract information into our graph, or precisely what to put into that structure. In our case, we want to provide instructions to our agent to standardize the formatting of ingredient names and to standardize units on the metric system to make matching and conversion easier. These extra instructions are just as important to the title model as the schema is. And boom, there we go. We&#x27;ve got lowercase ingredients and metric units.</p>
<p>ingredients and metric units. We know that the best prompt in the world isn&#x27;t bulletproof, though. So, we&#x27;ll look next at how to make sure we really do standardize our units. Here&#x27;s an example where we have a couple of ingredients that probably shouldn&#x27;t be represented by multiple nodes. We&#x27;ve got garlic cloves and minced garlic, cumin and cumin seeds, vegetable oil and oil. We&#x27;ve also got plain old garlic down there as well. So, in our first attempt at solving the potato, potato problem,</p>
<p>potato, potato problem, we can see that by taking a naive approach to mapping these, we can eliminate the duplication, which unifies the nodes, but it also strengthens the relationships between the different recipes that have common ingredients. We&#x27;ll explain why this is helpful later. The problem with this naive approach is that we&#x27;ve applied it retrospectively. And for this to work well, we&#x27;d have to know all of the ingredients ahead of time. Of course, these days, we have embedding models, which take the pain out of this sort of problem.</p>
<p>sort of problem. And by using an embedding model here, we have not only more flexible matching, but we also have the ability to match on terms that we don&#x27;t need to know in advance. This is a good example of where graph techniques and AI techniques working in hybrid give us the best result. So, now that we have a well-structured graph, we have nicely curated information put into that graph, and we&#x27;ve done extra work to make sure that the nodes are matched or the entities are matched before we create new nodes.</p>
<p>are matched before we create new nodes. Let&#x27;s start talking about what we can do with our graph. The very first thing we&#x27;re going to do is just do a simple query to see which recipes contain the ingredient garlic. We&#x27;ve got the Cypher or graph database query on top, and the relational SQL query below just for comparison. Here we can see all the recipes that have garlic and their ingredients, which we print to the if they&#x27;re fit on the slide. I think if you look at this example, you can see how out of hand the</p>
<p>example, you can see how out of hand the SQL query might get if we wanted to traverse 5, 10, 20 edges to find the nodes that we&#x27;re looking for. In a graph query, not only is it a little bit easier and more natural to write, but traversing relationships like that is where the graph data structures start to inherently excel. Stepping things up a notch, the next graph algorithm we&#x27;ve got is the personalized PageRank algorithm. This is a variant on vanilla PageRank,</p>
<p>This is a variant on vanilla PageRank, which was made famous by a certain Brin and Page back in 1998. It works by having a little dude run around the graph, and he marks each node as he passes. After a certain amount of hops around the graph, he&#x27;ll teleport back to the starting node. And that&#x27;s the bit that makes it personalized. It&#x27;s personalized to our starting node. By repeating this process until he&#x27;s completely worn out, some nodes will emerge with more marks on them than others. These are the nodes that have a</p>
<p>others. These are the nodes that have a stronger relationship with the starting node than those around them. A really common and popular reference point for personalized PageRank is the Pinterest Pixie paper. How&#x27;s that for some alliteration? Um that showed how PPR could be used for Pinterest recommendations. But, an even more contemporary one is Hippo Rag, uh which uses some other cool graph techniques as well to link memories to questions and answers.</p>
<p>questions and answers. In the presentation pack, you&#x27;ll find links and references to different variants and how they can be used. So, it looked a bit obvious in that last example. But, algorithms like this really shine when we have dense clusters of nodes and relationships, and it isn&#x27;t that easy to infer which ones are the most important. Another real-world example is taking a real-world US Supreme Court case and being able to find the authoritative landmark cases upon which it relies.</p>
<p>landmark cases upon which it relies. In this example, Miranda v. Arizona is not cited in the Canvas v. Sheba case. It&#x27;s purely through the relationships in the citation graph that we are able to find it. Not only to find it, but to be able to return a string of citations that show how it is related to this existing case through another. Shortest path algorithm is another good way to look at the relationships between two nodes in a graph. In this case where we know both nodes in advance and we don&#x27;t understand the relationships, we can look at the most</p>
<p>relationships, we can look at the most direct route between them. In this case, if we say the checkout code broke after we changed the basket constructor, but I have no idea why, we can traverse the edges between those two nodes in the code graph and return either the symbols or the text or a summary as context. In this case, the shortest path is highly useful, but we might want the K shortest paths or the shortest path that passes through a particular node or the cheapest path if the edges are</p>
<p>or the cheapest path if the edges are weighted. So, there are multiple variants and they&#x27;re all very useful at telling us what nodes and edges might help explain the relationship between two other nodes on the graph. One of the benefits of this, being able to retrieve a subgraph as context, is that we wouldn&#x27;t have found these intermediate nodes by doing vector search or even by doing individual symbol and reference lookups and the process of figuring that out for ourselves would have been slow. In one particular evaluation where we used this technique on a .NET code base,</p>
<p>used this technique on a .NET code base, we saw a 40% reduction in tool calls for code search where we used techniques like this to identify the context we needed to give the agent. This is another eShop example. The one thing I like about this particular example is that instead of starting with a node or a set of nodes and navigating our way through the graph, we&#x27;re querying entirely on relationships. We could specify a node type or a node ID in this query and it would still be a subgraph match. However,</p>
<p>subgraph match. However, in In case, we&#x27;re searching for code in a certain shape, not knowing anything specific about the code we&#x27;re looking for or any symbols up front. We&#x27;ll search for a decorator pattern in the eShop example, which is commonly used to enhance an existing class. So, what we&#x27;re looking for is a class that wraps its target class or consumes methods from its target class, where both the wrapper and the target class implement the same interface.</p>
<p>interface. Boom. There we go. In our eShop code base, we found a catalog view model service and a cached version that calls the same class and implements the same API. If we knew we were looking for caching classes, we could have searched on that. But, if we&#x27;re looking for a specific pattern or if we were looking for an anti-pattern or a particular type of security issue, a malicious transaction pattern, or legal arguments in a big corpus,</p>
<p>or legal arguments in a big corpus, sometimes it&#x27;s really important to be able to look for the shape of something without knowing the specific instance or node details themselves. The benefits of subgraph matching, where you have the opportunity to use it, I think are are quite unique. It&#x27;s not so much an optimization problem as like a big enabling algorithm. It&#x27;s something that&#x27;s just not easy to do uh with other tools. All right. So, we&#x27;ve covered a lot of ground. Thanks for bearing with me.</p>
<p>Thanks for bearing with me. We&#x27;ve looked at navigating paths, at ranking how important things are, and finding patterns. We&#x27;ve skipped over some of the traditional flow and cost and search algorithms that you might find often used in modeling dependencies or networks, and there&#x27;s heaps of use cases of those, but I think probably a little bit more run-of-the-mill. In the presentation back, we&#x27;ll also include some notes about some of the things that we couldn&#x27;t get to today like prediction, similarity, and clustering. These are now edging into some of the</p>
<p>These are now edging into some of the graph rag, building dynamic graphs, or schema-less graph kind of territory that we deliberately didn&#x27;t want to go into today, but it is also where things get super interesting as well. We&#x27;ll have some references and some pointers in the presentation pack. Otherwise, you can go and explore some of those things on your own. So, I hope that some of these concepts will have given you some insight or inspired you and that you can take them and either use graph native algorithms or hybrid algorithms to help make smarter, cheaper, and more reliable AI applications.</p>
<p>applications. Thank you.</p>

</details>
