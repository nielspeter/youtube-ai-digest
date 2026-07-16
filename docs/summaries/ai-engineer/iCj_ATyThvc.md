---
title: "An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge — Zhengyao Jiang, Weco"
channel: "AI Engineer"
video_id: iCj_ATyThvc
url: https://www.youtube.com/watch?v=iCj_ATyThvc
published: 2026-07-16T18:08:16+00:00
generated: 2026-07-16T19:32:35+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/iCj_ATyThvc/hqdefault.jpg
---
# An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge — Zhengyao Jiang, Weco

[![An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge — Zhengyao Jiang, Weco](https://i.ytimg.com/vi/iCj_ATyThvc/hqdefault.jpg)](https://www.youtube.com/watch?v=iCj_ATyThvc)

[Watch on YouTube](https://www.youtube.com/watch?v=iCj_ATyThvc) · **AI Engineer** · 2026-07-16

## TL;DR
Zhengyao Jiang, co-founder and CEO of Weco, presents Aiden, an autonomous AI research agent that became the #1 contributor in OpenAI's "Parameter Golf" hiring challenge—setting seven leaderboard records and achieving the highest community impact (H-index of 10 vs. 7 for the next human). Rather than replacing human engineers, Aiden demonstrates that auto-research agents excel at execution—finding, combining, and implementing ideas from human researchers—while the value of human creativity shifts toward designing evaluations and codebase abstractions that guide agent exploration.

## Key Takeaways
- Aiden, Weco's auto-research agent, submitted 7 leaderboard-record PRs in OpenAI's Parameter Golf competition, more than twice what any single human achieved.
- The agent ran for 22 days on a single H100 node, conducting ~1,300 experiments while using at most 4% of the competition's total compute.
- Aiden's work had the highest community impact, measured by an H-index of 10 over PRs, compared to 7 for the next human contributor—the community actively built on its findings.
- Most of Aiden's ideas originated from human sources: research papers, community discussions, and abandoned ideas from other participants; a small fraction were genuinely original.
- The agent's core strength is execution—rapidly finding and implementing promising ideas across a huge search space, not fundamental creative breakthroughs.
- Human-AI collaboration follows a pattern: humans collectively provide creative ideas; the agent executes them to solve concrete challenges.
- Designing good competitions and problem frameworks becomes tremendously important in the auto-research era—bad design can waste entire community efforts.
- Auto-research is analogous to model training: the codebase abstraction is the architecture, and the evaluation is the loss function/data—both critically shape what the agent explores and optimizes.
- Vertical moats can be built through proprietary evaluation data or domain-specific understanding of what matters and how to measure it.
- As auto-research automates execution, human skills shift up the stack: creativity, judgment in designing evals and abstractions, and the ability to drive these systems become exponentially more valuable.

## Detailed Breakdown

**[00:12] — Aiden's Dominance in Parameter Golf**
OpenAI ran a hiring challenge called Parameter Golf in April, where ~1,000 ML engineers and researchers competed to train the best language model under size and compute constraints. The top contributor was not a human but Aiden, an AI agent built by Weco. Of the 2,000 submissions fired, only 47 passed open review to reach the leaderboard—and 7 of those were Aiden's, more than twice what any human contributed.

**[01:14] — Beyond Benchmark Scores: Community Recognition**
Jiang frames the key question not as whether agents can climb benchmarks, but whether an auto-research agent can produce work that a human community genuinely recognizes—work that others can merge, fork, and build upon. Aiden was designed to publish its own work, not just optimize locally.

**[01:47] — Weco and Aiden's Background**
Weco is an auto-research company founded ~2.5 years ago. Jiang, co-founder and CEO, got his PhD at UCR on reinforcement learning. About two years ago, Weco built an agent independently evaluated by OpenAI in their MLE bench paper. Aiden is the next step: a multi-agent, self-improving system that reads public information (papers, PRs), runs experiments, and submits PRs once findings pass a quality gate.

**[02:52] — Aiden's Competition Results**
Aiden ran for ~22 days in the competition and set 7 leaderboard records—each a new best, stamped by OpenAI—while the best human made only 3. Beyond passing host review, Aiden's work had the highest community impact, measured by an H-index computed over PRs: Aiden scored 10, the next human 7. The entire community was building on the AI system's work, including other leaderboard entries.

**[03:55] — Why the Autonomous System Is Powerful**
The obvious advantage is tirelessness: ~1,300 experiments over 22 days on a single H100 node. But throughput isn't the whole story—a well-tuned AI system also maintains high output quality. Aiden used at most 4% of the competition's total compute and made ~15% of the records. 28% of its submissions made the leaderboard, roughly 6x the community average hit rate, effectively lifting the signal-to-noise ratio in the community's public PR channel.

**[05:29] — Humans and AI Contribute Differently**
Despite the numbers, auto-research doesn't simply dominate human experts. When tracing ideas, nearly all of Aiden's record PRs came from human research papers, other participants, or similar communities like nanoGPT. Sometimes ideas were abandoned notes—human researchers who gave up on implementation difficulties—and the agent was good at finding and actually implementing them. A very small fraction of original ideas emerged from Aiden's own efforts to navigate file-size constraints.

**[06:36] — Concrete Example: Gated Attention**
Aiden picked up "gated attention" from a Qwen paper; it worked but broke the 16MB file-size limit. Aiden figured out a quantization mechanism to bring file size down, but the combined score barely moved. Then another contributor posted a tokenizer improvement. Aiden recognized the idea, combined it with the architectural work, and after ~5 days of iteration, the three ideas produced a huge synergy—a big performance jump that became one of Aiden's leaderboard records.

**[08:07] — Interpreting Auto-Research Effectiveness**
Aiden is very strong at finding and implementing ideas: bringing an idea from a recent paper into actual competition implementation, digging promising ingredients out of a noisy public channel, and coming up with logically straightforward ideas (e.g., quantization to fix file size). It is fast and efficient at finding the right combinations across a huge search space. Jiang acknowledges this is mostly good execution, not glamorous innovation—but execution is usually the real bottleneck. What moves the frontier is typically belief in existing ideas plus tons of good execution.

**[09:13] — Human-AI Collaboration and the Value of Design**
The current state of collaboration: humans collectively provide creative ideas; the agent executes to solve concrete challenges. Does a single human's marginal contribution shrink? Not necessarily—the competition's design itself is tremendously important. Bad design can make the whole community effort useless, and thoughtful design work will have huge leverage in the auto-research era.

**[10:15] — The Gradient Descent Metaphor**
Jiang recalls Andrej Karpathy's tweet from ~10 years ago: "gradient descent can write code better than you." Back then, deep learning was eating conventional coding work, and Karpathy argued against people who thought they could hand-write better code than a trained model. Today, no one hand-writes code to beat a model, yet software engineering jobs still exist—and training models is one of the best-paid work. Jiang sees this as a metaphor: auto-research will commoditize certain execution skills while making higher-level skills far more valuable.

**[11:19] — Auto-Research Is Like Training a Model**
Doing auto-research is a lot like training a model. The codebase abstraction is the architecture—it sets constraints and priorities for what the agent can explore. The eval is the loss function and data—it sets what the agent optimizes for, like an environment in reinforcement learning. No one argues data or environments don't matter, and this is where vertical moats can be built: proprietary evaluation data or unique domain understanding of what matters and how to measure it.

**[12:53] — Codebase Abstraction as Architecture**
Codebase abstraction is underrated. It provides the framework the agent iterates on and biases the whole search direction—like neural network architecture design. Different architectures can theoretically represent the same function, but architecture systematically makes some functions easier to learn and biases optimization toward solutions that generalize better. Jiang gives an example: in a fraud detection pipeline, a loose API that processed training and testing data in the same function led to test-set leakage. Tightening the abstraction to a stricter API where test data couldn't reach training data dropped the leakage rate to zero—even though the agent could theoretically reward-hack.

**[14:58] — A New Craft and What Skills Matter**
Using auto-research is a new craft: designing the hill for the agent to climb. Creativity and judgment in designing good evals and abstractions will soon become exponentially more important. Driving these systems is a new skill that barely existed 1–2 years ago. The search is automated; humans move up the stack, not out of it. Jiang encourages following Weco's blog and his posts on X for ongoing learnings.

## Notable Quotes
- "The top contributor was one candidate that they couldn't hire. It wasn't a person, it's an agent we build called Aiden."
- "Can the auto research agent produce work that a human community actually recognize beyond a good score—work that other engineers can merge, fork, and build on?"
- "Most of them are just good execution. But in reality, execution is mostly the bottleneck. What moves the frontier is usually exactly some belief on existing ideas and tons of good executions."
- "Gradient descent can write code better than you. I'm sorry." — referencing Andrej Karpathy's tweet
- "How gradient descent changed coding is a great metaphor for how auto research will change research and ML engineering. It commoditizes certain execution skills. At the same time, it makes some higher-level skills far more valuable."
- "The search is automated. The human would just move up the stack, not out of it."

## People, Tools & References Mentioned
- **Zhengyao Jiang** — Co-founder and CEO of Weco; PhD from UCR on reinforcement learning; presenter
- **Weco** — Auto-research product research lab/company, founded ~2.5 years ago
- **Aiden** — Weco's multi-agent, self-improving auto-research system; top contributor in Parameter Golf
- **OpenAI** — Host of the Parameter Golf hiring challenge; independently evaluated Weco's earlier agent in MLE bench
- **Parameter Golf** — OpenAI's competition to train the best LM under size and compute constraints
- **MLE bench** — OpenAI paper that independently evaluated Weco's earlier ML engineering agent
- **Qwen** — Source of the "gated attention" idea Aiden implemented
- **nanoGPT** — Referenced as a similar community whose ideas Aiden drew from
- **Andrej Karpathy** — Referenced for his ~10-year-old tweet about gradient descent writing code better than humans
- **H-index** — Academic citation measure adapted to measure PR impact within the competition community

## Who Should Watch
AI engineers, ML researchers, and engineering leaders interested in how autonomous agents are transforming research workflows—and what human skills will matter most as execution becomes automated. The talk offers both a concrete case study and a strategic framework for thinking about evals, abstractions, and human-AI collaboration.


<details class="transcript">
<summary>Full transcript</summary>

<p>This April, OBI ran a hiring challenge, a competition called Parameter Golf. The top contributor was one candidate that they couldn&#x27;t hire. It wasn&#x27;t a person, it&#x27;s an agent we build called Aiden. In parameter golf, the goal is to train the best language model you can under size and computation constraints. About 1,000</p>
<p>About 1,000 machine learning engineers, researchers participate. They fired 2,000 submissions. Only 47 passed open review and made into the leaderboard. Seven of those are actually agents. More than twice what any human contributed. You&#x27;ve seen a lot of auto research today. Agents are here climbing benchmarks. Those are really impressive</p>
<p>benchmarks. Those are really impressive results. The question I want to ask is a bit different here. Can the auto research agent produce work that a human community actually recognize beyond a good score agent is optimizing for something that other engineers can merge fork and build on. So instead of having an agent just here climbing locally, we build one that publishes its own work and that&#x27;s Aiden.</p>
<p>publishes its own work and that&#x27;s Aiden. Quick context on us. Wiko is a auto research company that founded about two and a half years ago. Uh I&#x27;m co-founder and a CEO Jungao. Um got my PhD at UCR on reinforcement learning. About two years ago, we buil aid the top auto research agent independently evaluated by OpenAI in their MLE bench paper. Even though back then there&#x27;s a no such name called auto research, people call</p>
<p>name called auto research, people call it machine learning engineering agent. Aiden is the next step and a experimental prototype. It&#x27;s a multi-agent self-improving system that can read public information like research papers and other PRs, run its own experiments and submit a PR once the findings pass a quality gate. We send Aiden to parameter golf competition and it ran for about 22</p>
<p>competition and it ran for about 22 days. By the end, Aid has set seven leaderboard records. Each one is a new best for the competition stampled by OpenAI and the best human only made three. Passing the host review is a one signal for the quality. A second maybe more important one is whether other participants would build on your work. And it turns out Aiden&#x27;s work had the</p>
<p>And it turns out Aiden&#x27;s work had the highest impact within the whole community. Here we are using a inference measure that used widely in academia. It&#x27;s called a H index. Roughly if you have X papers get cited X times then your Ach index is X. Computed over PRs. Aiden was 10 and the next human was seven. The whole community was building on a AI systems</p>
<p>community was building on a AI systems work including many of other leaderboard entries. To break it down a little bit, why can a autonomous AI system be so powerful? One obvious reason is that it&#x27;s an AI. It can run tirelessly. Over 22 days, it ran about 1,300 experiments on a single H100 node. But the throughput isn&#x27;t the whole</p>
<p>But the throughput isn&#x27;t the whole picture. A well tuned AI system can also keep its output quality high. On the compute side, it uses at most 4% of competition&#x27;s total compute. and it made about 15% of the records. Also, 28% of its submissions made the leaderboard. Roughly six times higher heat rate than</p>
<p>Roughly six times higher heat rate than the community average. So, Aiden actually lifted the signal noise ratio within the whole community&#x27;s public communication channel, which is a PR. It didn&#x27;t win through massive paralization even though auto research have a tons of a potential of paralyzation. By those numbers it might feel like auto research already dominates human experts</p>
<p>research already dominates human experts on ML engineering and research but that&#x27;s not the full story I want to tell. Humans and AI are actually contribute in very different ways. When we trace the ideas, Aiden Aiden&#x27;s record PR almost all of them come from human research papers other participants in parameter golf or in similar communities like nano GBT. Those ideas are not necessarily a merged</p>
<p>Those ideas are not necessarily a merged PR. Sometimes it&#x27;s a note um a human researcher said oh I give up this idea because of some implementation implementation difficulty and the agent is good at finding them and actually implement them. There are also a very small fraction of original ideas Aiden came up by itself which emerged from its efforts to navigate the file size constraints. Here&#x27;s a concrete example that traces</p>
<p>Here&#x27;s a concrete example that traces the patterns I just talked about. So Aiden picked up an idea from Quen paper called gated attention and it worked but it introduced more parameters and it broke the 16 megapy file size limit. So it figure out a qualization mechanism to bring the file size down. But with those two primitives combined, the score</p>
<p>those two primitives combined, the score barely moved. Then another contributor posted a tokenizer improvement. Aiden recognized the idea, combine it with architectural work. It just work for five days or so. And after this combination, the three takea the three ideas turns out to have a huge synergy that lead to a big jump in performance and they become one of</p>
<p>in performance and they become one of the Aiden&#x27;s leaderboard records. So to sum up how I interpret Aiden and in general auto research systems effectiveness, it&#x27;s very strong at finding and implementing ideas. In the case we just saw, it brought an idea from a recent paper into a actual implementation in the competition and it&#x27;s good at dug promising ingredients out of the primary golf community even</p>
<p>out of the primary golf community even though the public channel is actually very noisy information wise. It can also came up logically straightforward ideas. For example, in this case, once you add the parameters and it breaks the file size limit, one obvious next move is just a quantization. And it&#x27;s really fast and really efficient at finding right combinations across a huge search space.</p>
<p>Okay, maybe none of those sounds very sexy. Most of them are just a good execution. But in reality, execution is a mostly the bottleneck. What moves the frontier is usually exactly some belief on existing ideas and tons of good executions. Okay. To step back, the state of a human AI collaboration is a human collectively</p>
<p>AI collaboration is a human collectively provide a lot of creative ideas and agent do the execution to solve a concrete challenge. What we are looking at is a a large group of a human and one AI system. Does this mean a single human engineer&#x27;s contribution marginally get smaller? I didn&#x27;t say even for that not really. In primate golf competition, it&#x27;s easy to only focus on engineers that&#x27;s</p>
<p>to only focus on engineers that&#x27;s actually doing hill climbing. But the design behind the competition itself is tremendously important. A bad design can make the whole community effort useless and their evil design work will have a few huge leverage in the auto research era. I really like one tweet from Andre Kapasi about 10 years ago where he said greeting descent can write code better</p>
<p>greeting descent can write code better than you. I&#x27;m sorry for the context about 10 years ago deep learning was starting to eat up a lot of software engineering like conventional coding work and his tweet was arguing against those people who thought they can handw write better code than a trained model. Okay, now obviously no one is seriously trying to handr write code to beat a model. However, software engineering I</p>
<p>model. However, software engineering I mean as a job still exist and so many people&#x27;s job are just training those models and those are one of the most well paid job today. I think how gradient descent change coding is a great metaphor for how auto research will change research and ML engineering. It commonize certain execution skills. At the same time, it makes some higher level skills far more valuable.</p>
<p>level skills far more valuable. So actually doing auto research is a lot like training a model. Your codebased abstraction is essentially the architecture. It sets the constraint and the priorities um for what the agent can explore. Your eval is the loss function and the data. It sets what the agent optimizes for. Take the eval first. The eval is the signal you use to train a model. In this</p>
<p>signal you use to train a model. In this case, it&#x27;s training your code. It plays the same role that like data and the loss function uh in model training or in a reinforcement learning setting. It&#x27;s like a environment that the agent is training. Nowadays, no one would argue data or environments um don&#x27;t matter. And uh this is where a vertical mode can also be built. You might have a</p>
<p>also be built. You might have a proprietary data for evaluation or a unique understanding of a in a particular field what matters and how to measure it. and a good evaluation would be amplified more and more as auto research are getting stronger. The other one I think is really underrated is codebased abstraction. The abstraction provides the framework that auto research can iterate on</p>
<p>that auto research can iterate on and uh that&#x27;s also that starting point hugely bias the whole search direction. This is a lot like a architecture design in neural networks. Different architecture in theory can represent the same function, but the architecture systematically makes some of the functions easier to be learned. And a good architecture biases the optimization towards</p>
<p>biases the optimization towards solutions that generalize better, perform better, even when the training loss might looks the same. That&#x27;s exactly the same for auto research. Here&#x27;s an example. We run auto research for a um fraud detection pipeline um and we trying to optimize the data prep-processing and first we give it a loose API where the same function process both the</p>
<p>the same function process both the training and testing data and the score looks great but the solution was polluted because there&#x27;s a certain certain test set information got leaked to the training information. We then tighten the obstruction to a more strict API where the test data couldn&#x27;t reach the training and the data leakage rate just dropped to zero. In</p>
<p>leakage rate just dropped to zero. In this case, a good abstraction leads to better solutions. Even though if the agent really want they can steer reward hack. So my point is using auto research is a new craft. It&#x27;s about the designing a here for an agent to climb and we are still very early on it. I think that makes this extremely exciting time to be an AI engineer. Other research will</p>
<p>an AI engineer. Other research will change what skills matter most. Creativity, the judgment to design a good eval or an abstraction. Those will soon get exponentially more important. Driving those system itself is where will be a new skill and that one is like barely existed one or two years ago. So the search is automated. the human would just move up the stack not out of</p>
<p>would just move up the stack not out of it. Again, um we call is a auto research um product research lab. We we keep sharing what we are learning as we build uh on our blog and I will also post some of my thinking to on ax. If you think some of this uh useful to you, feel free to follow me on X. Thank you.</p>

</details>
