---
title: "Can Cursor's HARDCORE Review Skill Stop The Slop?"
channel: "Matt Pocock"
video_id: mh5XZ-L5SFQ
url: https://www.youtube.com/watch?v=mh5XZ-L5SFQ
published: 2026-05-28T14:00:25+00:00
generated: 2026-07-15T18:49:44+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/mh5XZ-L5SFQ/hqdefault.jpg
---
# Can Cursor's HARDCORE Review Skill Stop The Slop?

[![Can Cursor's HARDCORE Review Skill Stop The Slop?](https://i.ytimg.com/vi/mh5XZ-L5SFQ/hqdefault.jpg)](https://www.youtube.com/watch?v=mh5XZ-L5SFQ)

[Watch on YouTube](https://www.youtube.com/watch?v=mh5XZ-L5SFQ) · **Matt Pocock** · 2026-05-28

## TL;DR
Matt Pocock reviews Cursor's "thermonuclear code quality review" skill, testing it against recent commits in his open-source project Sandcastle. The skill's ambition and focus on structural improvements impress him—he finds it catches real issues most review prompts miss—but he criticizes its verbosity, repetition, and complete lack of attention to testing.

## Key Takeaways
- The skill's defining trait is **ambition**: it pushes the agent to look beyond the diff and propose structural simplifications across the codebase.
- A 1K-line file-size limit is enforced because large files are hard for agents to navigate efficiently; splitting files lets filenames act as context pointers.
- The skill discourages spaghetti code—random if-statements and nested conditionals should be abstracted into helpers, state machines, or dedicated modules.
- It emphasizes type and boundary cleanliness, specifically questioning unnecessary optionality, `unknown`, `any`, and cast-heavy code (TypeScript-focused).
- Sequential orchestration of independent work is treated as a design smell; parallel execution is preferred where obvious.
- The concept of "code judo moves"—reframings that dramatically simplify code—is central to the review philosophy.
- Matt found roughly 5 out of 7 substantive suggestions valid, with false positives being easy to dismiss.
- Major gaps: no mention of testing, seams, or feedback loops—all of which Matt considers essential to maintainable codebases.
- The prompt is highly duplicative and could be significantly shortened; some sections like "review tone" feel unnecessary.
- More ambition means more false positives, but false positives are cheap to reject—missed improvement opportunities are the real danger.

## Detailed Breakdown

**[00:00] Introduction and Motivation**
Matt introduces automated code review as one of the most impactful ways to improve agent-generated code quality. He has his own review skill in a popular repo (109K stars) but isn't satisfied with it, so he's looking for inspiration elsewhere.

**[00:30] Discovering Cursor's Thermonuclear Review Skill**
He found a skill from the Cursor team called "thermonuclear code quality review," designed for unusually strict reviews focused on implementation quality, maintainability, abstraction quality, and codebase health. What stands out immediately is how ambitious it asks the reviewer to be, specifically looking for "code judo moves."

**[01:02] Setting Up the Test**
The skill is a single `skill.md` file. Matt copies it locally and tests it against the last five PRs merged to main in Sandcastle, his open-source software factory. He runs it on auto mode and begins reading the skill while it works.

**[01:32] The Baseline Prompt**
The skill opens by instructing a deep code quality audit: rethink structure, improve abstractions, modularity, reduce spaghetti code, improve succinctness and legibility. Matt notes that most review prompts fail because the agent treats the diff as its boundary. This one explicitly tells the agent to look throughout the entire codebase.

**[02:34] The 1K-Line File Rule**
The skill prohibits pushing a file past 1,000 lines without strong justification. Matt agrees: large files are hard for agents because they must ingest the entire file into context. Splitting files lets filenames serve as context pointers. He personally splits files over 5K tokens.

**[03:04] Anti-Spaghetti and Anti-Nesting Rules**
Random if-statements scattered in existing code are treated as design problems, not style nits. The skill prefers pushing logic into dedicated abstractions, helpers, state machines, or separate modules. Matt is somewhat ambivalent but accepts it as generally good practice.

**[03:35] Boring Code Over Magical Code**
The skill prefers direct, boring, maintainable code over hacky and magical solutions. Matt recognizes this as a classic prompt pattern, similar to Claude Code's "simplify" philosophy.

**[04:07] Type and Boundary Cleanliness**
The skill pushes hard on types: question unnecessary optionality, `unknown`, `any`, and cast-heavy code. Matt strongly resonates with the optionality point—agents always add props as optional even when required, which he finds frustrating.

**[05:09] Canonical Helpers and Parallel Execution**
The skill prefers existing utilities over bespoke one-offs and treats unnecessary sequential orchestration as a design smell. Matt finds the parallelism point valid but thinks the wording is "word salad" and would rewrite it more directly.

**[05:40] Primary Review Questions**
Key questions include: Is there a code judo move that would make this dramatically simpler? Can this be reframed to need fewer concepts? Matt loves the first two but criticizes "Does this improve or worsen the local architecture?" because without defining what good and bad look like, the agent can't meaningfully answer.

**[06:10] Escalation and Repetition Concerns**
The skill lists escalation triggers and examples of perverse suggestions (delete a whole layer of indirection, split large files). Matt grows concerned that the prompt is a "huge ball of mud"—too many instructions with unclear priorities for the agent. He also notes significant duplication throughout.

**[07:12] Review Tone and Output Expectations**
The skill includes a tone section (be direct, serious, demanding; don't be rude), which Matt finds bizarre and unnecessary. However, he appreciates the output expectations section, which prioritizes findings—structural regressions at the top, legibility concerns at the bottom—and requires an explicit approve/reject decision.

**[08:14] The Missing Piece: Testing**
Matt's biggest criticism: there's no mention of testing, seams, or feedback loops. He believes the entire point of a maintainable, modular codebase is to make future changes easier, and testing is central to that. All of the skill's focus is on source code, none on tests.

**[08:46] Reviewing the Results: Blocker Issues**
The skill found that an init service file exceeded 1,000 lines and proposed a split. It also suggested a generic `make registry` function to eliminate 20 lines of duplicated boilerplate. Matt rates both suggestions as good—2 for 2.

**[09:17] Scattered Conditionals and Type Boundaries**
The skill identified feature-specific if-statements scattered across three layers and suggested pushing custom tracker variations into a type. Matt approves. A third suggestion about discriminated unions for template args was a false positive from incomplete system understanding, but Matt accepts this as normal. Score: 2 out of 3.

**[10:18] Strong Code Quality Issues**
The skill found a weird hardcoded Zod dependency path, swallowed errors in `execSync`, and a half-finished file decomposition. Matt rates these positively—roughly 5 out of 7 valid suggestions so far. A prompt duplication suggestion was rejected; Matt prefers prompts to be independently changeable.

**[11:53] Final Verdict and Reflections**
Under the skill's bar, a couple of PRs shouldn't have landed in their current shape—behavior was correct but the codebase got messier. Matt concludes that ambition produces more false positives, but those are easy to reject. The dangerous misses are the improvement opportunities you never see. He would make the skill more DRY and add testing focus, but overall finds it worth experimenting with.

## Notable Quotes
- "It's the ones that you miss, that you never know about, the opportunity for improvement that you never see, those are the dangerous ones."
- "What I've often found with review skills like this is that the agent is not ambitious enough. If you pass an agent a diff, then it will usually treat that diff as its bounds within which it can work."
- "Large files are just quite hard for agents to navigate because they need to ingest the entire file into their context window in order to find the thing that's actually useful within it."
- "Whenever an agent adds a prop onto a React component, it always adds it as optional. I don't know why. It's so stupid."
- "This is just word salad to me. I don't know what that means."
- "What sort of scares me about these big review-based prompts is that this is a huge ball of mud for the agent to read."

## People, Tools & References Mentioned
- **Cursor team** — creators of the thermonuclear code quality review skill
- **Sandcastle** — Matt's open-source software factory, used as the test codebase
- **Claude Code** — referenced for its "simplify" philosophy
- **Zod** — a TypeScript validation library mentioned in the code review results
- **Matt's skills repo** — his own collection of agent skills, at 109K stars
- **AI Coding for Real Engineers cohort** — Matt's course starting June 1st

## Who Should Watch
Engineers using AI coding agents who want to improve automated code review quality, especially those interested in prompt design for review skills and the tradeoffs between ambition and false positives in AI-generated feedback.


<details class="transcript">
<summary>Full transcript</summary>

<p>Automated code review is one of the most impactful ways that you can improve the code quality coming out of your agent. I&#x27;ve known this for a while, but it&#x27;s taken me a while to kind of implement it and figure out a reusable skill that I can give to people to review their code. I&#x27;ve got this review skill here in my skills repo, which is currently sitting at whoa, 1,000 Sorry, 109,000 stars, and it is currently marked as in progress. I&#x27;m sort of okay with it, but I&#x27;m not</p>
<p>sort of okay with it, but I&#x27;m not terribly happy with it. So, I&#x27;ve been looking around for inspiration in other skills that I can copy from, steal ideas from, and one crossed my path I want to show you. It is this one from the cursor team. It is the thermonuclear code quality review. Use this skill for an unusually strict review focused on implementation quality, maintainability, abstraction quality, and code base health. And one thing I think is notable about this skill is how ambitious it asks the reviewer to be. It&#x27;s asking it to be very ambitious and look for code judo moves throughout the review. The</p>
<p>judo moves throughout the review. The skill itself is simply one file. It&#x27;s just a skill.md up here. And what I thought I&#x27;d do is I would copy it to my local system, try it out on some actual code of mine, and see what it comes up with. Yesterday, I spent a lot of time working on Sandcastle, my open-source software factory, and so I figure I would review the last X number of commits and see what it thought about them. So, I&#x27;m going to be pretty loose here. I&#x27;m just going to say thermonuclear code quality review, review the last five PRs that made it to main. I&#x27;m going to stick it on auto mode, and while it&#x27;s doing this, let&#x27;s actually go and read the skill</p>
<p>let&#x27;s actually go and read the skill because that should explain the skill a bit more. So, it starts from this baseline. Perform a deep code quality audit of the current branches changes. Rethink how to structure implement the changes to meaningfully improve code quality without impacting behavior. Work to improve abstractions, modularity, reduce spaghetti code, improve succinctness and legibility. Be ambitious. If there is a clear path to improving the implementation that involves restructuring some of the code base, go for it. Be extremely thorough and rigorous. Measure twice, cut once. What I&#x27;ve often found with review skills like</p>
<p>I&#x27;ve often found with review skills like this is that the agent is not ambitious enough. If you pass an agent a diff, then it will usually treat that diff as its bounds within which it can work. Whereas this prompt appears to be going beyond that. It&#x27;s essentially saying, &quot;Look throughout the entire code base for opportunities, but starting from this current current branch&#x27;s changes.&quot; It also goes on to add a bunch of non-negotiable non-negotiable additional standards. Be ambitious about structural simplification. Again, the ambition. Do</p>
<p>simplification. Again, the ambition. Do not let a PR push a file from under 1K lines to over 1K lines without a very strong reason. This is really interesting. I&#x27;ve actually reached this conclusion myself as well. Large files are just quite hard for agents to navigate because they need to ingest the entire file into their context window in order to find the thing that&#x27;s actually useful within it. A much better way to structure that is to split them into multiple files and let the kind of the file name of the file be the context pointer that tells it what&#x27;s in that</p>
<p>pointer that tells it what&#x27;s in that file and whether it might need to open it. This ends up being a lot more context efficient. I have generally split my files if they go over 5K tokens, but this 1K lines is sort of I guess a similar rubric. Do not allow random spaghetti growth in existing code, okay? I see it&#x27;s sort of arguing against nesting here. If a change adds weird if statements in random places, treat that as a design problem, not a stylistic nit. Prefer pushing the logic into a dedicated abstraction, helper, state machine, policy object, or separate module instead of tangling an existing path. Interesting. This is</p>
<p>existing path. Interesting. This is another way of telling it to be aggressive about, you know, if there&#x27;s a bunch of nested if statements and weird conditionals, maybe abstract that into a cleaner abstraction or a helper or something. It&#x27;s arguable whether I prefer that. I suppose sometimes I do, sometimes I don&#x27;t, but let&#x27;s assume it&#x27;s a good thing for now. Bias towards cleaning the design, not just accepting working code, again pushing it to be ambitious. Prefer direct, boring, maintainable code over hacky and magical code. This is like a classic one in these prompts. This comes from I think simplify in Claude code. And not the same wording I think, but a similar idea</p>
<p>same wording I think, but a similar idea that you want simple, direct code that&#x27;s easy to read. I really like this one actually. Push hard on type and boundary cleanliness when they affect maintainability. So we&#x27;re specifically talking about types here. Question unnecessary optionality, unknown, any, or cast heavy code when a clearer type boundary could exist. This is kind of TypeScript focused here. Unknown and any are specifically TypeScript terms. And the unnecessary optionality is one that always gets me. Whenever an</p>
<p>is one that always gets me. Whenever an agent adds a prop onto a React component, let&#x27;s say, it always adds it as optional. I don&#x27;t know why. I don&#x27;t know why. It&#x27;s so stupid. Even when it&#x27;s always required, it will add it as optional just to make it backwards compatible or something or to lessen the blast radius of the change. So yeah, question unnecessary optionality is a great one. Keep logic in the canonical layer and reuse existing helpers. Prefer existing canonical utilities and helpers over bespoke one-offs. Yes, I suppose it&#x27;s basically just telling it to look for places where this has already been</p>
<p>for places where this has already been solved in the code base and use those instead. Makes sense. Treat unnecessary sequential orchestration and non-atomic updates as design smells when the cleaner structure is obvious. If independent work is serialized for no good reason, ask whether the flow should run in parallel instead. I see, this is about performance essentially. Obviously, when two things that are independent, if they run in parallel, then it&#x27;s going to be faster than if they run sequentially. So that&#x27;s kind of what it&#x27;s going for here. But it&#x27;s also saying do not over-index on micro-optimizations. Okay, so it&#x27;s basically telling it don&#x27;t go too far. I think if this was my</p>
<p>go too far. I think if this was my skill, I would definitely rewrite this to be a lot more direct. Treat unnecessary sequential orchestration and non-atomic updates as design smells. That&#x27;s just word salad to me. I don&#x27;t know what that means. So, this is really cool. Primary review questions for every meaningful change ask, is there a code judo move that would make this dramatically simpler? That&#x27;s great. I love that. Can this be reframed so that fewer concepts branch or helper layers are needed? Lovely. I don&#x27;t love this. Does this improve or worsen the local architecture? You&#x27;ve got to say exactly what good and bad looks like to an agent in order for improve or worsen to mean</p>
<p>in order for improve or worsen to mean anything. Overall, this set of questions along with the kind of rules above give the agent a nice kind of way into talking about the code, which is what you need. And now it talks about really bad stuff. Escalate findings when you see a complicated implementation where a cleaner reframing could delete whole categories of complexity. Refactors that move code around but fail to reduce the number of concepts a reader must hold in their head. Yeah, there&#x27;s a bit of repetition going on here. Unnecessary casts, any unknown or optional params. What sort of scares me about these big review-based prompts is that this is a huge ball of mud for the agent to read.</p>
<p>huge ball of mud for the agent to read. Like there&#x27;s a lot of instructions in here and it&#x27;s hard to know what to prioritize for the agent. So, I don&#x27;t know. This this makes me a little bit nervous. I do like this though. When you identify a code quality problem, perverse suggestions like delete a whole layer of indirection rather than polishing it. Again, ambitious. Split a large file into smaller focused modules. Again, you know, making things easier to navigate for the agent. Again, duplication. Make type boundaries more explicit so the control flow gets simpler. There&#x27;s a lot of duplication throughout a lot of this. This could be cut down I think quite a lot. Review tone. I don&#x27;t know why this is here.</p>
<p>tone. I don&#x27;t know why this is here. This is just sort of saying choose your tone. I suppose. Be direct, serious, and demanding about quality. Do not be rude. This seems like a crazy thing to add to a skill. I don&#x27;t know why that&#x27;s here. What this does do is it does really punch the language that the agent should be using. So, we&#x27;re really emphasizing code judo, saying decompose, pushes the file past, makes the surrounding code more spaghetti. I like that. But the down we can say output expectations. Right, this is nice. It&#x27;s saying to prioritize findings in this order. It&#x27;s saying to float the important stuff to the top. And legibility and maintainability concerns</p>
<p>legibility and maintainability concerns are at the bottom, structural code quality regressions right at the top. Right, and it is asking for an approval here. So, it&#x27;s approving or rejecting the PR. And again, tons and tons of repetition here. This skill could be a lot shorter. So, what we have is a large block of text that basically says, &quot;Be more ambitious. Here are some specific things that you can focus on in your review. Really go nuts here and like uh propose a ton of structural changes. Make sure that you uh prioritize your findings in a certain order so you don&#x27;t flood it with useless crap, and then</p>
<p>flood it with useless crap, and then approve or reject based on these conditions.&quot; What I don&#x27;t like here is there&#x27;s no mention of testing. There&#x27;s no mention of seams. There&#x27;s no mention of any kind of like improving the feedback loops to make future runs better, which in my view is the entire point now of having a good code base or having a code base that&#x27;s easy to change and modular and easy to navigate. All of this appears to be focused on actual source code, none of it on tests. Interesting. But, okay, let&#x27;s read what it said here. So, it&#x27;s taken the last five PRs to main, and it has found some</p>
<p>five PRs to main, and it has found some blocker class structural issues. Okay, it&#x27;s found that an init service is now a big file, so it&#x27;s over 1,000 lines, and it mixes a bunch of stuff here, and it should have been preceded by a split, and it&#x27;s proposed an I split there. Ooh, it&#x27;s also trying to create an abstraction here, a little make registry generic function. Returning this would delete 20 lines of duplicated boilerplate for the same time. Feels good. That&#x27;s nice. So, we now go to the next one. The feature specific if issue tracker name custom scattered across</p>
<p>tracker name custom scattered across three layers. Interesting. It&#x27;s basically saying that instead of this being a special case if statement here, we should instead do a bit of code judo and push the custom tracker variations into a type itself, and then it can be read later. I think in terms of suggestions here, I happen to know this code quite well. I think we are at two out of two here. That&#x27;s um seems like two really good suggestions. Down here we have an inconsistent contract template args carries both shell commands and prose markers. It&#x27;s basically saying that some of these are runnable, but some of these are not</p>
<p>runnable, but some of these are not runnable here. And it&#x27;s saying that maybe we should widen the type to either a command or a to-do marker discriminated union or use a different field entirely for unfilled markers. So it&#x27;s basically it&#x27;s basically trying to strengthen the type boundary here so that we don&#x27;t later pass in a prose marker into something else. That&#x27;s interesting. I think that this comes from an inaccurate understanding of the whole system, which is okay. You&#x27;re going to get some false positives. I suppose it&#x27;s a false positive in any review prompt. So this is the kind of</p>
<p>review prompt. So this is the kind of thing if it came up in a PR, I would say this is fine. Don&#x27;t worry about it. So two out of three, not bad. Let&#x27;s go look at the strong code quality issues. Aha, we do have a weird bug here that it&#x27;s found or not a bug, just a weird bit of code design. We essentially have different templates in Sandcastle that each declare the dependencies that they need and mostly they declare Zod as the dependency. So we have this weird code path in here that looks like it just hard codes Zod and then interesting. What Yeah, overall this is quite hard to</p>
<p>What Yeah, overall this is quite hard to explain, but it&#x27;s definitely pulled up something weird here. So I think we&#x27;re at three out of four, which is good. Oh, it&#x27;s found some swallowed errors here. Exec sync inside effect. sync with swallowed errors. Interesting. We can see it&#x27;s trying something inside here and if it fails, then it just like returns false inside here. So yeah, this is definitely another thing that I would like the reviewer to look at. Looks like we started decomposing a large file into small files, but only half finished. So this again is a good one. This is five out of six so far. And it&#x27;s now saying there&#x27;s a bit of prompt duplication</p>
<p>there&#x27;s a bit of prompt duplication within some prompts that were changed here. So the change is bite identical for two different prompts here. It&#x27;s saying that we should refactor those into a issue list preamble. I don&#x27;t think that&#x27;s right. I think the prompts should just be independently changeable. So, not bad though, five out of seven. Then, it&#x27;s got a list of smaller items worth fixing here. I&#x27;ve done a quick scan and I would say most of those look pretty good. And interesting, I&#x27;m kind of intrigued by the approval bar here. Under the skill stated bar, a couple of the PRs should</p>
<p>stated bar, a couple of the PRs should not have landed in their current shape. The behavior is correct in all three substantive PRs, but the code base is meaningfully messier than it was a week ago.</p>
<p>[laughter]</p>
<p>Well, cool. I mean, we got some really good feedback from this skill, I think. I think what this is teaching me is that actually getting the review to be super ambitious and getting it to push a lot of different options will give you more false positives, but those false positives are pretty easy just to say no to, right? It&#x27;s the ones</p>
<p>just to say no to, right? It&#x27;s the ones that you miss, that you never know about, the opportunity for improvement that you never see, those are the dangerous ones. Overall, I would clean up this skill so it&#x27;s not quite so duplicative, so there&#x27;s, you know, a bit more dry. And I would also just get it to focus a lot more on tests, as well. Think about the seams in your code base, kind of like what my improved code base architecture does. But overall, I think this is worth pulling down, experimenting with, and just seeing what comes out of it. Now, if you dig this stuff, then I&#x27;m running a cohort</p>
<p>stuff, then I&#x27;m running a cohort starting next week, starting June 1st, on AI coding for real engineers. This has been my most subscribed to course ever. People are going nuts for this. We&#x27;re going to have, I think, around 4,000, 4,500 people in there. So, yeah, it&#x27;s absolutely wild. But if you&#x27;re enjoying this stuff, if there&#x27;s a skill that you want me to review, I really like making that content because it lets me steal ideas from other people&#x27;s great skills, then let me know. Nice work, and I&#x27;ll see you very soon.</p>

</details>
