---
title: "Microsoft Built a New Charting Language for AI Agents"
channel: "Better Stack"
video_id: xFWhiWe91BE
url: https://www.youtube.com/watch?v=xFWhiWe91BE
published: 2026-07-27T12:00:20+00:00
generated: 2026-07-27T15:12:47+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/xFWhiWe91BE/hqdefault.jpg
---
# Microsoft Built a New Charting Language for AI Agents

[![Microsoft Built a New Charting Language for AI Agents](https://i.ytimg.com/vi/xFWhiWe91BE/hqdefault.jpg)](https://www.youtube.com/watch?v=xFWhiWe91BE)

[Watch on YouTube](https://www.youtube.com/watch?v=xFWhiWe91BE) · **Better Stack** · 2026-07-27

## TL;DR
Microsoft Research published Flint, a research-stage charting language that splits chart generation into two jobs: LLMs write ~10 lines of JSON describing the *meaning* of the data, and a deterministic compiler handles all the *geometry* (axes, scales, color schemes), outputting real Vega-Lite, ECharts, or Chart.js specs. The broader insight is that agentic AI systems are converging on this pattern—models emit tiny, validatable intermediate representations while deterministic layers handle the rest.

## Key Takeaways
- **Chart generation is secretly two jobs**: meaning (which LLMs excel at) and geometry (which LLMs struggle with).
- Flint's model: the LLM writes ~10 lines of JSON using semantic types (e.g., "quantity," "percentage change," "rank"); a deterministic compiler makes every geometric decision.
- Setup is one line (`Claude MCP add flint`); it's pure TypeScript on Node 18, runs locally, and data never leaves your machine.
- Changing a single semantic type word (e.g., "quantity" → "percentage change") triggers the compiler to automatically fix color schemes, number formatting, and axis scaling.
- Flint compiles *to* existing standards (Vega-Lite, ECharts, Chart.js)—it's an intermediate language, not a replacement.
- A waterfall chart that balloons past 100 lines in Vega-Lite is roughly 10 lines in Flint because the compiler owns the complex parts.
- Flint is five tools, one schema, all local—unlike chart MCP servers with 26 tools that render data on remote servers.
- This is a research project (~2 months old, version .28, ~7 contributors), not a product; bugs are still being caught.
- The "100,000 tokens down to 200 per chart" claim has zero benchmarks and the paper is still forthcoming.
- Flint's real value is for small/cheap models, composite charts (waterfalls, sunbursts), and products where end users see charts and 80% success isn't good enough.
- Missing features: no maps, no 3D, no network graphs, no layering, no Python package, and accessibility is an empty GitHub issue.
- Over 5,000 npm downloads/week; it's already replacing Microsoft's own Data Formulator, meaning there's an internal customer keeping it alive.
- The most agreed-upon takeaway isn't about charts—it's that all agentic systems are converging on this architecture: LLMs emit tiny validatable intermediate representations, deterministic layers do everything else.

## Detailed Breakdown

### The Core Problem with AI Chart Generation [00:00](https://www.youtube.com/watch?v=xFWhiWe91BE&t=0s)
The video opens with a relatable frustration: AI agents can build entire backends in minutes, but ask for a single waterfall chart and you get 100 lines of Vega-Lite that renders a blank page. The presenter argues this isn't a model problem—it's a language problem. Microsoft Research's Flint project is positioned as a fix for a pattern that will become ubiquitous in AI tooling.

### Chart Generation as Two Jobs [00:35](https://www.youtube.com/watch?v=xFWhiWe91BE&t=35s)
The key insight is that chart generation is secretly two separate jobs. Job one is *meaning*—understanding that a column represents months, another represents revenue, another a percentage change. LLMs handle this well. Job two is *geometry*—axes, step sizes, scale domains, label spacing, color ramps. LLMs are bad at geometry, and that's where generated charts fail. The Flint team hit this wall building their own analytics agent, which achieved roughly 80% success on good-looking charts—a number that sounds decent until real users are involved and one in five charts is broken.

### The Flint Architecture [01:06](https://www.youtube.com/watch?v=xFWhiWe91BE&t=66s)
Flint splits the two jobs. The model writes about 10 lines of JSON describing only meaning, using over 70 semantic types like "quarter," "price," "rank," and "percentage change." A deterministic compiler then takes over, making every geometric decision and emitting a real Vega-Lite, ECharts, or Chart.js spec. The mantra: "The model does meaning, the compiler does math."

### Setup and Demo [01:37](https://www.youtube.com/watch?v=xFWhiWe91BE&t=97s)
Setup is a single command: `Claude MCP add flint`. It's pure TypeScript on Node 18 with nothing weird on Apple Silicon. The presenter pastes a CSV of monthly signups and asks for a heat map of new users by month per game. Claude writes a 10-line Flint spec, calls `rendered chart`, and a finished PNG drops into chat in seconds—all rendered locally so data never leaves the computer. A tool called `create chart view` opens an interactive panel without requiring reprompting or spending additional tokens; the chart remains editable after the model's job is done.

### Semantic Types in Action [02:09](https://www.youtube.com/watch?v=xFWhiWe91BE&t=129s)
Everything hinges on semantic types. The presenter demonstrates changing a single word: a column tagged "quantity" becomes "percentage change," and the compiler automatically flips the entire color scheme to a diverging palette, rewrites number formatting, and rescales the axis. One word in, a dozen correct decisions out. The philosophy: you tell Flint what the data is, never where the pixels go. Because the output is genuine Vega-Lite, ECharts, or Chart.js spec, the same input can target any backend—there's no Microsoft rendering lock-in. The compiled spec is yours to hand-tune; Flint gets you 95% of the way and is not a replacement for anything.

### Comparison with Existing Tools [03:10](https://www.youtube.com/watch?v=xFWhiWe91BE&t=190s)
Flint isn't fighting Vega-Lite—it compiles to it. Vega-Lite feels high-level until you want a chart to look good, at which point a waterfall chart balloons past 100 lines of coupled parameters. The same waterfall in Flint is about 10 lines because the compiler owns the complex parts. Mermaid is for flowcharts, not customer-facing charts. The presenter references Hacker News commentary noting that chart MCP servers with 26 separate tools render your data on someone else's server, whereas Flint is five tools, one schema, all local.

### Caveats and Limitations [03:41](https://www.youtube.com/watch?v=xFWhiWe91BE&t=221s)
Flint is a research project, not a product—about 2 months old, version .28, with roughly 7 contributors. Bugs were still being caught this month where the same spec rendered differently in Vega-Lite and ECharts. The viral-sounding claim of "100,000 tokens down to 200 per chart" comes with a caveat: zero benchmarks, and the paper is still "coming soon." The sharpest objection is that frontier models already one-shot simple charts just fine, meaning power users with big models may not need Flint. Its real case is narrower: small or cheap models, composite charts like waterfalls and sunbursts, and any product where an end user sees the chart and 80% success isn't good enough. Missing features include no maps, no 3D, no network graphs, no layering, accessibility is an empty GitHub issue, and there's no Python package yet.

### Adoption and the Bigger Picture [04:43](https://www.youtube.com/watch?v=xFWhiWe91BE&t=283s)
Adoption is notable: over 5,000 npm downloads per week for a two-month-old research drop. It's already replacing Data Formulator, Microsoft's own analytics tool, meaning Flint has an internal customer keeping it alive. The most agreed-upon takeaway from the community wasn't about charts at all—it was that all agentic systems are converging on this shape: the LLM emits a tiny, validatable intermediate representation, and a deterministic layer does everything else. You can validate 10 lines of JSON before rendering; you can't validate 100 lines of generated D3.

## Notable Quotes
- "The model does meaning, the compiler does math. That's the whole trick."
- "You tell Flint what the data is, never where the pixels go."
- "It's an intermediate language that gets you 95% of the way. It's not a replacement for anything."
- "You can validate 10 lines of JSON before it even renders. You can't validate 100 lines of generated D3."
- "All agentic systems are converging on exactly this shape."

## People, Tools & References Mentioned
- **Flint** — Microsoft Research's charting language (the subject of the video)
- **Vega-Lite** — declarative charting grammar; Flint compiles to it
- **ECharts** — charting library; Flint compiles to it
- **Chart.js** — charting library; Flint compiles to it
- **Mermaid** — flowchart tool (noted as unsuitable for customer-facing charts)
- **D3** — referenced in context of generated code being hard to validate
- **Data Formulator** — Microsoft's own analytics tool, already being replaced by Flint internally
- **Claude MCP** — the integration path for Flint (`Claude MCP add flint`)
- **Hacker News** — cited for community reactions and critiques
- **Node 18 / TypeScript** — Flint's runtime and language
- **npm** — distribution platform; 5,000+ downloads/week

## Who Should Watch
AI tooling developers, data visualization engineers, and anyone building agentic systems where LLMs generate structured output. Even if you've never built a chart, the architectural pattern Flint demonstrates—LLMs emitting tiny validatable intermediate representations while deterministic compilers handle complexity—is one you'll likely encounter across AI tooling broadly.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=0s">00:00</a></span> Our AI agents can build our entire backend in minutes. Then we ask it for one waterfall chart and it hands you a 100 lines of Vega light that renders a blank page. We blame the model. Microsoft Research just published a bet that everyone&#x27;s wrong. It&#x27;s not a model problem, it&#x27;s a language problem. This is Flint and it fixes a pattern you&#x27;re about to see everywhere in AI tooling. So stick around even if you&#x27;ve never chart anything cuz this might just change how models and languages work together.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=35s">00:35</a></span> The project is called Flint and the idea clicks once you see the chart generation is secretly two jobs. Job one is meaning this column is month, that one&#x27;s revenue and that one&#x27;s a percentage change. LLMs nail that. Job two is geometry. Axis, step sizes, scale domains, label spacing, color ramps. LLMs are bad sometimes at geometry. And that&#x27;s exactly where your generated charts kind of die off. The Flint team hits this wall themselves, building their own</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=66s">01:06</a></span> wall themselves, building their own analytics agent that measured roughly 80% success on good-looking charts. Sounds decent until real users are on the other end, and one in five charts is broken. So, Flint splits the jobs into two. The model writes about 10 lines of JSON that only describe meaning using semantic types quarter price rank percentage change over 70 of them. Then a deterministic compiler takes over makes every geometric decision and emits a real Vega light echarts or charjs spec. The model does meaning the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=97s">01:37</a></span> spec. The model does meaning the compiler does math. That&#x27;s the whole trick. If you enjoy coding tools that speed up your workflow, be sure to subscribe. We have videos coming out all the time. Now watch how fast this gets. Setup is one line. Claude MCP add flint. It&#x27;s pure Typescript on Note 18. There&#x27;s nothing weird on Apple silicone. I paste in a CSV of monthly signups and ask for new users by month per game as a heat map. Claude writes a 10line Flint spec calls rendered chart. And the finished PNG drops into the chat in seconds.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=129s">02:09</a></span> PNG drops into the chat in seconds. Rendered locally so my data never left my computer. But here&#x27;s the part I didn&#x27;t expect. There&#x27;s a tool called create chart view that opens an interactive panel. I didn&#x27;t have to reprompt and I didn&#x27;t spend any tokens on that. The model finished its job and the chart is still editable. So here&#x27;s what&#x27;s actually happening now. Everything hangs on those semantic types. Watch this. I change one word. The column tagged quantity becomes percentage change and the compiler flips the entire color scheme to a diverging</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=160s">02:40</a></span> the entire color scheme to a diverging pallet, rewrites the number formatting and rescales the axis. One word in a dozen correct decisions out. Now think of it like this. You tell Flint what the data is, never where the pixels go. And because the output is genuinely Vega light or echarts or chartjs spec, that means same input, pick your backend. There&#x27;s no Microsoft rendering island here. The compiled spec is yours to handtune. It&#x27;s an intermediate language that gets you 95% of the way. It&#x27;s not a</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=190s">03:10</a></span> that gets you 95% of the way. It&#x27;s not a replacement for anything. Now, the question someone in data science or you are already asking, don&#x27;t we already have Vegaite for this? Here&#x27;s the thing. Flint isn&#x27;t fighting Vegaite. It compiles to it. Vega light feels high level right up until you want the chart looking good and then a waterfall chart balloons past a 100 lines of coupled parameters. The same waterfall in Flint about 10 lines because the compiler owns all the weird parts. Then we have mermaid but that&#x27;s for flowcharts.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=221s">03:41</a></span> mermaid but that&#x27;s for flowcharts. Hacker News said the quiet part out loud. You don&#x27;t ship mermaid charts to customers and those chart MCP servers with 26 separate tools that render your data on someone else&#x27;s server. Flint is five tools, one schema, all local. Now, the caveat with all this. First, this is a research project. It&#x27;s not a product. It&#x27;s about 2 months old, version.28 contributors. They were still catching bugs this month where the same spec rendered differently in Vega Light and</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=251s">04:11</a></span> rendered differently in Vega Light and in Echarts. Then that viral sounding claim of a 100,000 tokens down to 200 per chart. There is a cut. The author&#x27;s own number. Zero benchmarks. the paper is still coming soon. Then yes, the sharpest objection here was Frontier Models already oneshot simple charts. It&#x27;s just fine. If you&#x27;re a power user with a big model, Flint solves a problem you don&#x27;t have. The case for this is a bit more narrow. Small or cheap models. Composite charts like waterfalls and sunbursts and any product where an end</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=283s">04:43</a></span> sunbursts and any product where an end user sees the chart and 80% isn&#x27;t good enough. Also, there&#x27;s no maps in here. There&#x27;s no 3D, no network graphs, no layering. Accessibility is literally an empty GitHub issue. In Python devs, there is no package yet, so don&#x27;t go looking for it. The adoption says something over 5,000 npm downloads a week for a two-month-old research drop, and it&#x27;s already P&#x27;s data formulator, Microsoft&#x27;s own analytics tool, which means Flint has a customer inside the building keeping it alive. The most agreed on take here wasn&#x27;t about charts</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=xFWhiWe91BE&amp;t=315s">05:15</a></span> agreed on take here wasn&#x27;t about charts at all. It was that all agentic systems are converging on exactly this shape. The LLM emits a tiny validatable intermediate representation and a deterministic layer does everything else. You can validate 10 lines of JSON before it even renders. You can&#x27;t validate a 100 lines of generated D3. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We&#x27;ll see you in another video.</p>

</details>
