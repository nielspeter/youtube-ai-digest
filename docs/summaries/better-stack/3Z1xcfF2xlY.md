---
title: "Github's Biggest Release In Years. Stacked PRs."
channel: "Better Stack"
video_id: 3Z1xcfF2xlY
url: https://www.youtube.com/watch?v=3Z1xcfF2xlY
published: 2026-08-05T15:00:29+00:00
generated: 2026-08-05T17:57:31+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/3Z1xcfF2xlY/hqdefault.jpg
---
# Github's Biggest Release In Years. Stacked PRs.

[![Github's Biggest Release In Years. Stacked PRs.](https://i.ytimg.com/vi/3Z1xcfF2xlY/hqdefault.jpg)](https://www.youtube.com/watch?v=3Z1xcfF2xlY)

[Watch on YouTube](https://www.youtube.com/watch?v=3Z1xcfF2xlY) · **Better Stack** · 2026-08-05

## TL;DR
GitHub has released stacked PRs, a major new feature that lets developers break large code changes into a chain of smaller, dependent pull requests that can be reviewed and merged together. The feature is managed via the GitHub CLI (`gh stack` commands) and integrates throughout GitHub's UI, with particularly strong potential for AI-driven agentic workflows.

## Key Takeaways
- Stacked PRs break large code changes into a chain of smaller, dependent pull requests that can be reviewed and merged independently or all at once.
- The bottom PR in a stack targets the default branch (e.g., `main`), and each subsequent PR targets the previous one, forming a dependency chain.
- Foundational changes (shared types, database schemas) go in lower branches; dependent code (API routes, UI components) goes in higher branches.
- Stacked PRs are a GitHub-level concept — Git itself has no notion of "stacks"; it's just daisy-chained branches.
- The GitHub CLI simplifies stack management with commands like `gh stack init`, `gh stack add`, and `gh stack submit`.
- You can still create stacks manually by linking PRs together; GitHub will detect them as a stack once pushed.
- GitHub's UI shows a stack icon on associated PRs and offers a "merge stack" button to merge all PRs at once.
- Stack references are integrated throughout GitHub — pull request pages, PR lists, and GitHub workflows.
- The feature eliminates the need to wait for individual PRs to merge into `main` and then manually rebase or merge yourself.
- Stacked PRs are especially powerful when combined with AI agents, which can produce organized stacks of PRs rather than one massive PR or many disconnected ones.

## Detailed Breakdown

### What Stacked PRs Are [00:00](https://www.youtube.com/watch?v=3Z1xcfF2xlY&t=0s)
GitHub has released its biggest update in years: stacked PRs. The concept is simple but powerful — you break large code changes into a chain of smaller, dependent pull requests that can be reviewed and merged independently. A stack requires two or more PRs in the same repository, where the bottom PR targets the trunk (usually `main`), and each subsequent PR targets the previous one. This creates a dependency chain where foundational changes live in lower branches and dependent code sits in higher branches.

### Git vs. GitHub: What's Actually New [01:04](https://www.youtube.com/watch?v=3Z1xcfF2xlY&t=64s)
The presenter acknowledges that developers have always been able to daisy-chain PRs in Git — there's no such thing as "stacked PRs" in Git itself. The feature only has meaning within GitHub's platform, where it brings real advantages in manageability, UI integration, and merge workflow. The CLI further streamlines the process.

### Creating a Stack with the GitHub CLI [01:36](https://www.youtube.com/watch?v=3Z1xcfF2xlY&t=96s)
The demo begins by running `gh stack init setup-database`, which creates the base branch pointing to `main`. After making changes (editing the README as a stand-in for implementing a database), standard `git add` and `git commit` commands are used. To move to the next layer of changes, `gh stack add` is run with a new branch name (e.g., for API endpoints). Multiple commits per branch are supported. A third branch (`setup-front-end`) is added the same way. Once all changes are ready, a single command — `gh stack submit` — pushes all branches to GitHub at once, presenting a mini CLI UI to add titles and descriptions for each PR.

### Manual Stack Creation Without the CLI [03:07](https://www.youtube.com/watch?v=3Z1xcfF2xlY&t=187s)
You can achieve the same result without the CLI by manually linking PRs from `main` to PR1 to PR2 and so on. GitHub will still detect these as a stack once everything is pushed. The CLI simply makes the process much easier to manage.

### Reviewing and Merging Stacks in GitHub's UI [03:37](https://www.youtube.com/watch?v=3Z1xcfF2xlY&t=217s)
On GitHub, each PR in the stack displays a small stack icon indicating its association. Opening the top (tail) PR reveals a "merge stack" option that shows every PR in the stack and allows you to approve them one by one or merge the entire stack into `main` simultaneously. Stack references are integrated throughout GitHub — visible on PR pages, PR list pages, and within GitHub workflows.

### Why This Matters and AI Potential [04:09](https://www.youtube.com/watch?v=3Z1xcfF2xlY&t=249s)
Stacked PRs eliminate the old workflow of waiting for individual PRs to merge into `main` and then manually rebasing and merging. You can now create one long stack and let GitHub manage it in the UI. The online response has been overwhelmingly positive, especially regarding AI use cases: when running agentic loops for hours, agents can now create stacked PRs that link all their work together, avoiding either one massive PR or many disconnected ones.

## Notable Quotes
- "In the context of just Git, there's no such thing as stacked PRs and you'd still just be daisy chaining PRs together. Only within GitHub itself does stacked PRs actually mean anything."
- "Foundational changes such as shared types or database schemas go in the lower branches and code that depends on them, such as API routes and UI components, goes in the higher branches."
- "If you're working on massive PRs and you need an easy way to split that up into separate segments, you no longer need to wait for separate PRs to be merged into main and do all the rebasing and the merging yourself."
- "When you do things like design agentic loops and let the agent run for hours, it can now create stacked PRs and link all of that work together rather than creating either a massive PR or loads of completely separated PRs."

## People, Tools & References Mentioned
- **GitHub** — platform releasing the stacked PRs feature
- **GitHub CLI** — used for stack management (`gh stack init`, `gh stack add`, `gh stack submit`)
- **Git** — underlying version control system (noted as unchanged by this feature)
- **Better Stack** — the channel publishing the video
- **AI / Agentic loops** — highlighted as a powerful use case for stacked PRs

## Who Should Watch
Developers and engineering leads who regularly deal with large pull requests or work with AI coding agents will benefit most from this video, as it explains a practical new way to structure, review, and merge complex code changes more efficiently.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=0s">00:00</a></span> GitHub have just released its biggest update in years, stacked PRs. A brand new way to break down massive PRs into more manageable chunks. In this video, we&#x27;re going to cover exactly what they are and why you&#x27;d use them. Stacked PRs are a powerful but fairly simple concept. Break large code changes into a chain of smaller dependent pull requests you can review and merge independently. To have a stack, you need two or more pull requests in the same repository where the first or bottom</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=32s">00:32</a></span> repository where the first or bottom pull request targets the trunk, usually your repository&#x27;s default branch, such as main. Then each subsequent pull request targets the previous. This forms a dependency chain where each branch builds on the one below it. Foundational changes such as shared types or database schemas go in the lower branches and code that depends on them, such as API roots and UI components, goes in the higher branches. And you may be thinking, well, I&#x27;ve always been able to do this, right? I could raise a PR to main and then raise a second PR to that PR and chain the PRs as much as I like.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=64s">01:04</a></span> PR and chain the PRs as much as I like. And that is absolutely true because in the context of just Git, there&#x27;s no such thing as stacked PRs and you&#x27;d still just be daisy chaining PRs together. Only within GitHub itself does stacked PRs actually mean anything. But they do bring some massive advantages. And if you want to stay up to date with tech and AI, then subscribe to Better Stack. So to make use of stacked PRs, it&#x27;s best to have the GitHub CLI installed and with that you can run ghst stack init and then declare your new stack. So let&#x27;s go to our text editor and now we</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=96s">01:36</a></span> let&#x27;s go to our text editor and now we can go through an example of stacking multiple PRs. So the first thing we&#x27;re going to do is run ghst stack init setup database. So in this case the PR or the branch is going to be called setup database and this will be the base PR that&#x27;s now going to point to main. Then we can make our changes. For the case of the demo, I&#x27;m just going to put changes into the readme file. So I said it implemented the database and then you can just do git add get commit. So everything here is just standard git. And then when you&#x27;re ready to switch to your next set of changes, you can then</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=126s">02:06</a></span> your next set of changes, you can then do gh stack add and then your next branch. Then I can make more changes. Create the API endpoints. Maybe I want to add some extra points here. So I&#x27;ll commit this change. Then we can add a second change as well. And then again we can commit this. So as you would expect, you can make multiple commits per branch. And then finally we&#x27;ll do gh stack add setup front end and then make one more change here. And then again we do get add and get commit. Now once we&#x27;re happy with all of our changes and we want to push all of those branches up to GitHub at the same time. We can just</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=157s">02:37</a></span> to GitHub at the same time. We can just run one command gh stack submit. This will then give us this mini CLI UI where we can go through each one of the PRs in the stack and add a title and a description if we want to. Or we can just press next on each one and then submit three PRs in one go. So you can see all three of those PRs, setup, database, API, and front end have all been pushed to GitHub as a stack within a single command. And you can actually do all of this without the GitHub CLI. Just follow the old school method of</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=187s">03:07</a></span> Just follow the old school method of linking PRs together manually from main to PR1 to PR2. Then GitHub will still detect these as a stack once you push them all up. The CLI just makes this much easier to manage. Now remember, nothing has changed within Git itself. If you want to check out a completely different branch that&#x27;s not within the stack you&#x27;re working on, you can do that and then just come back to the branch within the stack later. If we now head over to GitHub itself, you can see we&#x27;ve got each of our three PRs and they&#x27;re raised as pull requests here. And you can see we also have this little stack</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=217s">03:37</a></span> can see we also have this little stack icon here to tell us that these PRs are associated to a stack. If we open the tail PR, so the one that&#x27;s on top of the stack, you can see down here, we can click merge stack and you can see this UI as well. So we see every single PR as part of the stack. We could go through this and approve it one by one, but once we&#x27;re happy with all of this, you can then just click merge stack and every single one of those PRs would be merged into main at the same time. You&#x27;ll also notice that references to stacks are now integrated throughout the entirety of GitHub. So you can see them on the pull request page, on the pull request list</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=249s">04:09</a></span> request page, on the pull request list page. You&#x27;ll also see them on things like GitHub workflows and throughout really the entire application. So if [clears throat] you&#x27;re working on massive PRs and you need an easy way to split that up into separate segments, you no longer need to wait for separate PRs to be merged into main and do all the rebasing and the merging yourself. You can just create one long stack and GitHub is now perfectly equipped to manage all of that within the UI. And the CLI is a really nice way to manage it all automatically. There&#x27;s been an overwhelmingly positive response to this online and particularly when used with</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=3Z1xcfF2xlY&amp;t=280s">04:40</a></span> online and particularly when used with AI. I think this can be a really powerful feature. When you do things like design agentic loops and let the agent run for hours, it can now create stacked PRs and link all of that work together rather than creating either a massive PR or loads of completely separated PRs. But I hope you found this one useful, guys. Let me know what you think of stacked PRs in the comments and subscribe to Better Stack to stay up to date with the latest tech and AI news. Thanks for watching and of course I&#x27;ll see you next time.</p>

</details>
