---
title: "Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs"
channel: "AI Engineer"
video_id: Bck7ABCZRZI
url: https://www.youtube.com/watch?v=Bck7ABCZRZI
published: 2026-07-18T18:15:06+00:00
generated: 2026-07-18T19:20:44+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/Bck7ABCZRZI/hqdefault.jpg
---
# Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs

[![Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs](https://i.ytimg.com/vi/Bck7ABCZRZI/hqdefault.jpg)](https://www.youtube.com/watch?v=Bck7ABCZRZI)

[Watch on YouTube](https://www.youtube.com/watch?v=Bck7ABCZRZI) · **AI Engineer** · 2026-07-18

## TL;DR
Thiyagarajan Maruthavanan shares his journey from ballooning inference costs on rented AI platforms to building his own cognitive infrastructure. He argues that while renting intelligence is fine for early experimentation, post-product-market-fit startups and enterprises must own their inference infrastructure to control costs, ensure compliance, and maintain reliability—summarized in his mantra: "Rent to learn, own to earn."

## Key Takeaways
- Inference costs on rented platforms (e.g., Anthropic, OpenAI) can spiral out of control rapidly, as experienced by major retailers and Uber.
- Rented intelligence platforms behave like prepaid casino credits—easy to lose track of spending until you've blown past your mental threshold.
- Token factories (open-source models on neo-clouds or local GPU rigs) are an alternative but come with their own bottlenecks, such as memory constraints.
- Enterprises face additional barriers with rented or leased infrastructure: rate-limit control (investment fund), third-party vendor dependency audits (hospital), and reproducibility of model outputs (tax practice).
- The decision to rent vs. own depends on product-market fit: pre-PMF startups can rent; post-PMF startups and budgeted enterprise projects cannot afford to.
- Maruthavanan built an open-source project called **JustTokenMax** for inference optimization, benchmarked favorably against Netflix's Headroom.
- He also authored a book titled *Peak Inference: Infraeconomics of AI Inference*.
- The AI market is noisy with conflicting visions from leaders like Jensen Huang (token factories) and Satya Nadella (unmetered local intelligence).
- Core philosophy: **"Rent to learn, own to earn."**

## Detailed Breakdown

**[00:00] The Cost of Rented Intelligence**
Maruthavanan opens with cautionary tales: a major retailer spent $200 million on Anthropic inference, and Uber's CTO saw a year's token budget consumed in four months. He notes that while inference feels inexpensive per call, the prepaid credit model makes it dangerously easy to overspend—likening it to loading credits in a casino.

**[01:01] Personal Experience: UltraSuno**
He built **UltraSuno**, an app that reverses Suno.com's text-to-music pipeline by deducing prompts from songs. After going viral with hundreds of thousands of users, his inference costs ballooned to hundreds of thousands of dollars. He attributes this to poor context management, lack of input token compression, and wasteful agent loops.

**[02:02] Security Incident**
Three weeks prior, his API key was stolen by someone in China, draining his endpoint. Costs rose rapidly from $7,000 toward a potential $100,000, but his co-founder arrested the breach at $10,000.

**[02:34] The Token Factory Alternative**
He explores "token factories"—using open-source models on neo-clouds or building local GPU rigs, as promoted by AI Twitter influencers. He bought a DGX box and migrated UltraSuno off Anthropic. It worked, but memory became a bottleneck. He then ran research lab agents on it successfully, but found the setup insufficient for enterprise needs.

**[04:08] Enterprise Barriers to Renting and Leasing**
Three enterprises approached him: an investment fund, a hospital, and a tax practice. Each hit distinct walls:
- **Investment fund:** Needed control over rate limits; token factories dictated consumption caps.
- **Hospital:** Passed the use case but failed a third-party audit due to vendor dependency.
- **Tax practice:** Required reproducibility of AI-generated recommendations, impossible without access to the model's internals.

**[05:08] When to Stop Renting**
Maruthavanan draws an analogy: you Airbnb and rent when exploring a new city, but eventually you buy a house—you can't raise a family in an Airbnb. Similarly, pre-PMF founders can rent, but post-PMF startups and enterprises with budgeted projects must build their own infrastructure.

**[06:09] JustTokenMax and Peak Inference**
He introduces **JustTokenMax**, an open-source optimization project addressing input cost, token management, and context management across renting and owning layers. It is benchmarked against Netflix's Headroom and performs superiorly on many parameters. He also mentions his book, *Peak Inference: Infraeconomics of AI Inference*.

**[06:42] A Noisy Market and Final Philosophy**
The AI market shifts every three to six months, with conflicting narratives from industry leaders. Jensen Huang champions token factories; Satya Nadella predicts unmetered local intelligence; neo-clouds claim endpoint providers will capture value. Maruthavanan distills his experience into one sentence: **"Rent to learn, own to earn."** He invites further conversation at the AI Engineer conference.

## Notable Quotes
- "Using inference feels like it's one of the most inexpensive thing. But then this is very different from using a phone where you get a bill once every month... it's almost as if you're loading credits inside a casino."
- "You cannot raise a family in an Airbnb."
- "If you want to learn, you can rent, but if you want to earn, then you have to own."
- "Rent to learn, own to earn."

## People, Tools & References Mentioned
- **Thiyagarajan Maruthavanan** (presenter; Twitter: @mtraj; site: mtraj.com)
- **Kalmantic Labs** (presenter's affiliation, implied)
- **Anthropic** and **OpenAI** (rented intelligence platforms)
- **Uber CTO** (budget overrun anecdote)
- **Suno.com** (text-to-music application)
- **UltraSono / Ulta Sono** (presenter's reverse-engineering app)
- **DGX box** (NVIDIA hardware for local inference)
- **JustTokenMax** (presenter's open-source optimization project)
- **Headroom** (Netflix's project, used as benchmark)
- **Peak Inference: Infraeconomics of AI Inference** (presenter's book)
- **Jensen Huang** (NVIDIA CEO; token factory advocate)
- **Satya Nadella** (Microsoft CEO; unmetered intelligence advocate)

## Who Should Watch
AI startup founders, enterprise architects, and engineering leaders who are feeling the pain of inference costs or facing compliance, control, and reproducibility constraints with rented AI platforms. It offers a practical framework for deciding when to transition from renting to owning your cognitive infrastructure.


<details class="transcript">
<summary>Full transcript</summary>

<p>One of the largest retailers in the country spent close to $200 million on inference with Anthropic and decided that things got way out of hand and built their own infrastructure. I&#x27;m pretty sure most of you have read the news from Uber CTO on how they had planned a budget of their tokens for an entire year and it got over in month four. I&#x27;m also confident that half of you in this room have come to a very similar conclusion that as time goes by the cost of intelligence really built. Using inference feels like, you know, it&#x27;s one of the most inexpensive thing.</p>
<p>it&#x27;s one of the most inexpensive thing. But then this is very different from using a phone where you get a bill once every month and then you have like a specific set of amount that you can actually anchor your mind to. But in case of using these rented intelligence platform, they are like prepaid. You load credits. It&#x27;s almost as if you&#x27;re loading credits inside a casino. You put some and then you pull it and then you are so addicted to it then you end up doing more and more of it and by some time you realize that you&#x27;ve blown past the threshold that you had mentally kept in mind. And I had this</p>
<p>in mind. And I had this experience myself. I built an app called Ultrazone or I experienced the inference cost ballooning here. Suno.com has anybody heard about Suno.com? Yeah, Suno.com is is this application that allows a user to turn a text prompt into music. What I was interested in is is doing the reverse which is given a particular song, what prompt could have actually generated it. This is something that I wanted. So I built this. I was having a lot of fun using this application, shared it with a few friends and spread wide around. I had</p>
<p>friends and spread wide around. I had hundreds of thousands of users, but then the cost ballooned way more than what I had anticipated. Hundreds of thousands of dollars I had to spend on inference. Now, this happens for many reason. There are many talks that are there at AIE itself where people talk about how you need to manage your context better. And many people forget about doing compression of their input token. And when there are agent loops, then there are many of these calls that are happening which are very, very wasteful. The inference endpoint that is consuming</p>
<p>The inference endpoint that is consuming this is is completely unaware of the shape of the workload and which is why this happens. And I have this other issue that had happened. 3 weeks ago, my key got stolen. Someone in China got hold of it and then was sucking my endpoint dry. I could see the cost rise up from 7,000 to 7,500 dollars to 8,000 and going and so forth. Thanks to my co-founder who heads the research and technology, we were able to arrest it at 10,000 dollars. Otherwise, it could have been 100,000 dollars. Now, many people suggest that the alternative to rented intelligence platform is is to</p>
<p>to rented intelligence platform is is to use token factory. Token factory is is basically saying that why are you paying money to Anthropic and OpenAI? Instead, go open source, have these open source models that are already deployed somewhere in the cloud, and then they are provisioned as tokens per second. There are neo clouds and then there are inference endpoint providers who actually do this. In fact, there is also an argument saying that, you know, you can build this token factory locally. There are AI Twitter influencers who actually talk about building inference in your garage, in your basement. Buy GPU cards, rig them up together, and</p>
<p>GPU cards, rig them up together, and then you could actually run a local token factory. In fact, I was in inspired by that a little bit. I bought my own DGX box and then I first moved Ulta Sono from Anthropic to DGX box. It worked well. I ran into this one issue of memory being the bottleneck. And then, it was good enough that I started building my next applications. I started having agents. I have some agents that I need for running my research lab. So, these agents started shaping up inside the DGX box, you know, two, six, eight, 12. And it worked all right. The issue</p>
<p>12. And it worked all right. The issue though is is that, you know, it may not be reliable for enterprise, which is what I exactly faced. Three enterprises reached out to me to replicate the same setup for them. But for enterprises, renting and leasing don&#x27;t cut it. Bill is a problem, but then there are secondary set of problems that makes it extremely ineffective approach. The enterprises that I reached out to me, one was a fund, another a hospital, and the third a tax practice. And each of them had different wall that they had hit. The fund, it was an investment fund,</p>
<p>The fund, it was an investment fund, they were running an investment analyst on an email client architecture, and they didn&#x27;t want somebody else to dictate as to what the rate limit that they could consume. So, control become a big issue for them to actually go with token factories. Hospital had a different issue. They used the use case, it worked well, but later when they went through an audit, a third-party vendor dependency was redlined, and then they couldn&#x27;t go forward. The tax practice was a completely different issue. In a tax practice, what is happening is this, when an intelligent generates a</p>
<p>when an intelligent generates a recommendation, you want to be able to recreate it. And when you don&#x27;t have access to the in-depth of the model, you will not be able to do this, and that became the issue. So, that brings me to the most important point of this presentation. Where do you sit? When do you stop renting infrastructure? If you&#x27;re a startup, if you&#x27;re a founder who is doing pre-product market fit work, so you&#x27;re still figuring out that the use case that you have, if there is demand for it, you can get by by renting. But if you&#x27;re post-product market fit, you cannot afford to And if</p>
<p>market fit, you cannot afford to And if you&#x27;re an enterprise who&#x27;s already budgeted a project, which means you&#x27;re telling that you are assuming that this particular use case has product market fit, then again, you cannot ignore to build your own infrastructure. Which is what I realized, and I said that this this situation is this like, if you&#x27;re going to a new city, you may initially start with saying that I don&#x27;t want to buy a house. Let me actually rent and see. Sometimes you might even Airbnb. You experience the environment, you experience the city, the neighborhood, but then eventually you have to buy the</p>
<p>but then eventually you have to buy the house. You cannot raise a family in an Airbnb. As I went through this experience, I decided I came to the conclusion that I need to build my own inference infrastructure for the apps, the agents, and the scaling of the apps that I&#x27;m building. And I call this as just infra. And while I went through this exercise, I realized that there is optimization to be done at multiple layers. Even at the renting and the lease layer, you can do optimization around input cost to token management, and then, you know, context management, and so on and so forth. Some of those</p>
<p>and so on and so forth. Some of those experiences that I&#x27;ve had in the last couple of months combined it into an open-source project and published it as just token max. If you have used headroom from Netflix, then this is an alternative to it. We benchmarked against headroom and on many parameters, just token maxes is far superior. If this is a thing that is of interest to you, give it a try, maybe a GitHub star if you like it. I also wrote the book called peak inference infraeconomics of AI inference when you have to think about building your own inference infrastructure. The AI market is is very</p>
<p>infrastructure. The AI market is is very different compared to the rest of the technology market that used to exist because here the rules of the game change every three to six months, which means it becomes a very noisy marketplace. You talk to someone like Jensen, he would say token factory is the future. You hear someone like a Satya Nadella, he will say unmetered intelligence is the future, it is going to be local. And then when you hear new clouds and inference endpoint providers, they&#x27;ll say, &quot;Hey, inference endpoint providers are the ones that are going to capture the value in the marketplace.&quot; Now, my experience walking from application to agents to scaling them</p>
<p>application to agents to scaling them and then building my own inference infrastructure taught me that if you want to learn, you can rent, but if you want to earn, then you have to own. And if there was the one sentence that you had to take away from this entire presentation, it is that. Rent to learn, own to earn. But then, you have to come to your own answers. Thank you. And if any of these topics are of interest to you, then I&#x27;m happy to talk to you about renting, about just token max, about how to build your own inference infrastructure. I&#x27;m here at the AI</p>
<p>infrastructure. I&#x27;m here at the AI Engineer&#x27;s conference for the next 3 days. Hit me up on Twitter at mtraj or through my site mtraj.com.</p>

</details>
