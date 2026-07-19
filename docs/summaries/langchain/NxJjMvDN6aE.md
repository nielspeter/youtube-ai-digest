---
title: "OpenWiki 0.2 is adopting the OKF spec"
channel: "LangChain"
video_id: NxJjMvDN6aE
url: https://www.youtube.com/watch?v=NxJjMvDN6aE
published: 2026-07-16T16:57:07+00:00
generated: 2026-07-16T20:24:12+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/NxJjMvDN6aE/hqdefault.jpg
---
# OpenWiki 0.2 is adopting the OKF spec

[![OpenWiki 0.2 is adopting the OKF spec](https://i.ytimg.com/vi/NxJjMvDN6aE/hqdefault.jpg)](https://www.youtube.com/watch?v=NxJjMvDN6aE)

[Watch on YouTube](https://www.youtube.com/watch?v=NxJjMvDN6aE) · **LangChain** · 2026-07-16

## TL;DR
OpenWiki 0.2 is officially adopting Google's Open Knowledge Format (OKF) specification, meaning all generated or updated wikis will now include structured YAML front matter, an index file, and a changelog. This shift enables more deterministic, efficient search and retrieval for agents and connects OpenWiki to a growing open-source ecosystem of tooling around OKF.

## Key Takeaways
- OpenWiki 0.2 adopts the Open Knowledge Format (OKF) spec from Google; all new or updated wikis will conform to it.
- OKF is lightweight: it adds YAML front matter to each doc, an `index.md` for the directory, and a `log.md` changelog.
- YAML front matter includes structured fields: `type`, `title`, `description`, `resource`, and `tags`.
- Previously, agents discovered docs through pure agentic file-system search—iterating and reading files to find matches.
- With OKF metadata, agents can use deterministic filters (e.g., by `type` or `tags`) instead of reading every file's contents.
- `resource` fields can link to external URLs or internal files within the codebase wiki.
- Full-text search can now be performed on structured fields like `description` and `title`.
- A growing open-source ecosystem is forming around OKF, including a Google-built visualizer for exploring wiki docs and their connections.
- OpenWiki 0.2 has official OKF support now, with more features (better search tools, UI visualization) coming soon.
- OpenWiki is free and open source; users can log in with ChatGPT or an API key, and contributions via issues and PRs are encouraged.

## Detailed Breakdown
### Announcement and OKF Overview [00:00](https://www.youtube.com/watch?v=NxJjMvDN6aE&t=0s)
Brace from LangChain announces that OpenWiki is officially adopting the Open Knowledge Format (OKF) spec from Google. Going forward, every OpenWiki generated or updated will conform to OKF. At a high level, the spec is simple: it involves adding YAML front matter to wiki documents, an `index.md` file listing all markdown files in the directory, and a `log.md` serving as a changelog.

### YAML Front Matter in Practice [00:32](https://www.youtube.com/watch?v=NxJjMvDN6aE&t=32s)
Brace demonstrates the OpenSwee project's OpenWiki docs, showing the new YAML front matter at the top of each document. This metadata block is the key difference between old and new OpenWiki. OKF requires fields including `type`, `title`, `description`, `resource`, and `tags`, which enable more accurate search and retrieval capabilities.

### From Agentic Search to Deterministic Filtering [01:03](https://www.youtube.com/watch?v=NxJjMvDN6aE&t=63s)
Previously, agents discovered documentation through pure agentic search—navigating the file system, iterating through files, and reading contents to find the best match. With YAML front matter, agents can now use deterministic search tools, such as filtering by `type` or `tags`. For example, an agent can request all docs with a type of "BigQuery tables" and instantly retrieve matching documents without reading every file.

### Simplicity and the Open Source Ecosystem [02:05](https://www.youtube.com/watch?v=NxJjMvDN6aE&t=125s)
The OKF spec is easy to add—it's just YAML front matter—yet it unlocks faster, more efficient search tools. Beyond search improvements, a second major motivation is the emerging open-source ecosystem around OKF. Brace shows a Google-built open-source visualizer that lets users explore wiki docs, see how they connect, and click into individual docs to view metadata and content.

### OpenWiki 0.2 and Call to Action [03:06](https://www.youtube.com/watch?v=NxJjMvDN6aE&t=186s)
OpenWiki 0.2 ships with official OKF support, with more features coming soon including better search retrieval tools and UI for visualizing docs. Brace encourages viewers to try OpenWiki, which is free and open source, accessible via ChatGPT login or API key. He invites users to file issues for feedback or bugs and to submit PRs for new features.

## Notable Quotes
- "The OKF spec is fairly simple. It's basically just adding YAML front matter to your Wiki docs, an index.md file that contains an index of all the MD files in that directory, and a log.md which you can think of as a change log."
- "Before, the way your agent would discover docs in Open Wiki was through pure agentic search... With this YAML front matter, we can implement better, more deterministic search tools."
- "Instead of having to search through every single doc, read the actual contents of them, and try to decide which docs document BigQuery tables and which don't, it can just perform a deterministic filter based on the type."
- "We decided that it would make sense to adopt it in OpenWiki because it will give us better search, and we can utilize the open source community being built around OKF."

## People, Tools & References Mentioned
- **Brace** — Presenter from LangChain
- **OpenWiki** — Open-source wiki generation tool by LangChain
- **Open Knowledge Format (OKF)** — Specification from Google for structured wiki documentation
- **OpenSwee** — Project shown as a demo example with OpenWiki docs
- **Google's OKF visualizer** — Open-source tool for visualizing wiki docs and their connections
- **BigQuery** — Referenced as an example doc type for filtering
- **ChatGPT** — Mentioned as a login option for OpenWiki
- **GitHub** — Platform for issues, PRs, and contributions

## Who Should Watch
Developers and AI engineers using or considering OpenWiki for agent-driven documentation workflows, especially those interested in how structured metadata improves retrieval and search for LLM agents. It's also relevant for anyone curious about the emerging OKF ecosystem and its tooling.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=NxJjMvDN6aE&amp;t=0s">00:00</a></span> What&#x27;s everyone? It&#x27;s Brace from LangChain, and today I&#x27;m excited to announce that Open Wiki is officially adopting the Open Knowledge Format Spec from Google. What this means is every Open Wiki generated or updated going forward will conform to the OKF spec. So, what does this actually mean in practice? Well, at a high level, the OKF spec is fairly simple. It&#x27;s basically just adding YAML front matter to your Wiki docs, an index.md file that contains an index of all the MD files in that directory, and a log.md which you can think of as a change log. Let&#x27;s take</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=NxJjMvDN6aE&amp;t=32s">00:32</a></span> can think of as a change log. Let&#x27;s take a look at what this YAML front matter actually looks like in some real docs. So, as you can see, I have the Open Swee project up here with the Open Wiki docs, and there&#x27;s this new YAML front matter at the top of the docs. This is the main difference between the old Open Wiki without OKF and the new Open Wiki with OKF. OKF requires us to have this YAML front matter, uh which contains a type, title, description, resource, and tags. What this will mean for us is we can implement better and more accurate search and retrieval tools for Open</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=NxJjMvDN6aE&amp;t=63s">01:03</a></span> search and retrieval tools for Open Wiki. So, before, the way your agent would discover docs in Open Wiki was through pure agentic search, right? Using the file system, iterating through the files in the Open Wiki directory, and trying to find the one which best matched the question it had. With these YAML front matter, we can implement better, more deterministic search tools like, say, you know, filtering on different tags, or finding all the docs with a specific type. For example, let&#x27;s say the type is BigQuery tables, and your agent says, &quot;I want to get all the docs on BigQuery tables.&quot;</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=NxJjMvDN6aE&amp;t=95s">01:35</a></span> get all the docs on BigQuery tables.&quot; Well, it could say, &quot;Find all the Open Wiki docs with a type of BigQuery tables.&quot; Then, instead of having to search through every single doc, read the actual contents of them, and try to decide which docs document BigQuery tables and which don&#x27;t, it can just perform a deterministic filter based on the type, and get back every doc for, in this case, BigQuery tables. Same applies to tags, resources, which can link out to either external URLs or in often case in OpenWiki code base wikis, internal files. It can do full</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=NxJjMvDN6aE&amp;t=125s">02:05</a></span> wikis, internal files. It can do full text search on descriptions or titles and more. So, with this spec, because it&#x27;s so simple, it&#x27;s so easy to add to OpenWiki, right? It&#x27;s just adding this initial YAML front matter to your docs, and it will allow us to add many more deterministic, faster, and more efficient search tools to OpenWiki to allow your agents to more efficiently query data. The second main reason is the open source ecosystem that&#x27;s being built around OKF. Although OKF is a very new spec, there&#x27;s already a robust ecosystem being developed around it. As we can see here, this is an open source</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=NxJjMvDN6aE&amp;t=156s">02:36</a></span> we can see here, this is an open source visualizer from Google that you can plug into your wikis to visualize all the docs within their wiki, how they connect with each other, and click into these actual docs and see the description, resource, tags, and the actual doc contents. The OKF spec is still very new, so there&#x27;s still lots going on, but we decided that it would make sense to adopt it in OpenWiki because it will give us better search, and we can utilize the open source community being built around OKF. So, in OpenWiki 0.2, it has official support for OKF with</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=NxJjMvDN6aE&amp;t=186s">03:06</a></span> it has official support for OKF with lots of new features coming soon like better search retrieval tools, UI for visualizing your OpenWiki docs, and more. So, if you like this, please go try out OpenWiki. It&#x27;s open source, it&#x27;s free to use. You can log in with ChatGPT or set an API key. Try it out. If you have feature requests, feedback, or bug reports, open an issue. And of course, if you want to add new features, we love it getting contributed PRs, so please put up a PR, and I&#x27;ll see you all in GitHub.</p>

</details>
