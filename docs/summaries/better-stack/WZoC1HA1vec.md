---
title: "This Free Go Alternative to Firebase is Just One File"
channel: "Better Stack"
video_id: WZoC1HA1vec
url: https://www.youtube.com/watch?v=WZoC1HA1vec
published: 2026-07-14T07:00:00+00:00
generated: 2026-07-14T11:42:49+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/WZoC1HA1vec/hqdefault.jpg
---
# This Free Go Alternative to Firebase is Just One File

[![This Free Go Alternative to Firebase is Just One File](https://i.ytimg.com/vi/WZoC1HA1vec/hqdefault.jpg)](https://www.youtube.com/watch?v=WZoC1HA1vec)

[Watch on YouTube](https://www.youtube.com/watch?v=WZoC1HA1vec) · **Better Stack** · 2026-07-14

## TL;DR
PocketBase is an open-source, single-file Go binary with SQLite embedded that serves as a free alternative to Firebase or Supabase, offering a realtime database, authentication, and file storage. The video demonstrates how it works through a React bug tracker app, covering the admin UI, API rules, TypeScript hooks, deployment considerations, and its production readiness.

## Key Takeaways
- PocketBase is a single Go binary with SQLite embedded, providing realtime database, authentication, and file storage out of the box.
- You don't need to write Go to extend it — hooks can be written in JavaScript or TypeScript (though TypeScript must be compiled to JavaScript).
- It includes an admin UI similar to Supabase for configuring collections and setting API rules.
- Front-end integration is done via the JavaScript SDK, allowing direct database access with realtime subscriptions.
- API rules secure collections using patterns like `@request.auth.id`, familiar to Supabase users.
- There are 82 unique hooks available for extending backend behavior (e.g., sending emails on record creation).
- Because it uses SQLite, it requires persistent storage — platforms with ephemeral filesystems (Heroku, Render, Railway) are poor fits without attached storage.
- A VPS is the recommended and cheapest hosting option, costing as little as $4/month.
- PocketBase includes production features like migrations, job scheduling, logging, static file serving, and template rendering.
- It is pre-v1, meaning breaking changes may occur and manual migrations may be required.

## Detailed Breakdown

### Introduction to PocketBase [00:00](https://www.youtube.com/watch?v=WZoC1HA1vec&t=0s)
PocketBase is introduced as an open-source alternative to Supabase and Firebase, and possibly the simplest backend you could ever run. It's a single Go binary with SQLite embedded, providing realtime database, authentication, and file storage. The video aims to test whether this simple architecture holds up beyond basic apps.

### Architecture and Admin UI [00:32](https://www.youtube.com/watch?v=WZoC1HA1vec&t=32s)
PocketBase is a single Go binary, but coding in Go is optional since the backend can be extended with JavaScript and TypeScript. It includes a basic admin UI for configuring collections, similar to how Supabase works. Front-end connection is done via the JavaScript SDK, allowing direct database access from the client — a design pattern shared with Firebase and Supabase. API rules and auth keep access secure.

### Demo App Overview [01:02](https://www.youtube.com/watch?v=WZoC1HA1vec&t=62s)
The demo application is a bug tracker built with a React front-end and PocketBase backend. The key file is `pb.ts`, which imports the PocketBase class, creates an instance, and connects to the backend. This instance (`PB`) is then used throughout the application.

### Authentication and State Management [01:33](https://www.youtube.com/watch?v=WZoC1HA1vec&t=93s)
The logged-in user hook initializes state with `PB.authStore.model`, grabbing the currently authenticated user. A listener is set up via the `onChange` event so that when the auth store changes, the new user is set into state. This allows accessing and subscribing to auth state simply.

### Realtime Data Subscriptions [02:05](https://www.youtube.com/watch?v=WZoC1HA1vec&t=125s)
The `useIssues` hook initializes empty state, then uses a `useEffect` to fetch all issues via `getFullList` and populate state. Realtime subscriptions are set up with `pb.collection('issues').subscribe`, so when records are created, updated, or deleted (e.g., dragging cards between columns), state is automatically updated.

### File Storage and Issue Creation [03:07](https://www.youtube.com/watch?v=WZoC1HA1vec&t=187s)
Creating a new issue supports attaching a screenshot. The submit function appends form data and calls `pb.collection('issues').create()` with the data. On the backend, collection API rules prevent misuse. The admin interface shows the `users` and `issues` collections, and API rules can be configured per collection — for example, requiring `@request.auth.id` to match the user ID for updates or deletes.

### Extending with Hooks [04:08](https://www.youtube.com/watch?v=WZoC1HA1vec&t=248s)
PocketBase can be extended via hooks in Go, JavaScript, or TypeScript. There are 82 unique hooks available at the time of filming, covering events like `onBootstrap` (app start) and `onRecordCreate` (database record creation). The presenter's hooks are written in TypeScript and compiled into JavaScript in the `pb_hooks` folder, since PocketBase only natively supports JavaScript.

### Hook Example: Sending Emails [05:10](https://www.youtube.com/watch?v=WZoC1HA1vec&t=310s)
The main hook file demonstrates an `onRecordCreate` hook targeting issue creation. Every time a record is created, an email is sent to the user via `e.app.newMailClient().send()` with a constructed message object. This illustrates how custom functionality is supported through the extensive hook system.

### Deployment and Storage Considerations [05:41](https://www.youtube.com/watch?v=WZoC1HA1vec&t=341s)
Because PocketBase uses SQLite, it requires persistent storage. Platforms with ephemeral filesystems (Heroku, Render, Railway) would lose data on redeploy. A VPS is the recommended and cheaper option. Data lives in the `pb_data` folder, which contains a `storage` folder for uploaded files and a `db` file for the SQLite database. Deleting the db file would lose all application data, so a backup strategy is essential.

### Cost Comparison and Production Features [06:12](https://www.youtube.com/watch?v=WZoC1HA1vec&t=372s)
Compared to Supabase (starting at $25/month for the basic tier), PocketBase is essentially free — you only pay VPS costs (as little as $4/month) and can run unlimited projects. It includes production features like migrations, job scheduling, and logging. Static files can be served directly from the `pb_public` folder (useful for React front-ends), and dynamic routes with template rendering are supported (useful for email templates).

### Production Readiness and Pre-v1 Caveat [07:14](https://www.youtube.com/watch?v=WZoC1HA1vec&t=434s)
PocketBase includes all features needed for a modern SaaS app and is fully extensible. However, it is pre-v1, meaning you must be comfortable reading changelogs and running manual migrations occasionally. If that's acceptable, it's a viable option for building a production app.

## Notable Quotes
- "PocketBase is an open-source alternative to Supabase or Firebase and possibly the simplest backend you could ever run. Just one single file, giving you realtime database authentication and file storage."
- "This is in complete contrast to how insanely complex modern webdev has become."
- "If you've used Supabase in the past, you'll find this kind of pattern super familiar."
- "Compared to tools like Supabase, which can start at $25 for the basic tier, PocketBase is basically free."
- "They do explicitly say to only use this if you're fine reading change logs and running manual migrations from time to time."

## People, Tools & References Mentioned
- **PocketBase** — the main subject; open-source single-file Go backend
- **Supabase** — referenced as a comparable alternative (pricing and API rules patterns)
- **Firebase** — referenced as a comparable alternative
- **Go** — the language PocketBase is built in
- **JavaScript / TypeScript** — languages for extending PocketBase via hooks
- **SQLite** — embedded database engine used by PocketBase
- **React** — used for the demo app front-end
- **Heroku, Render, Railway** — platforms with ephemeral filesystems (not recommended for PocketBase)
- **VPS** — recommended hosting option
- **Open Code** — mentioned as another open-source alternative (subject of another video)
- **Warren** — presenter from Better Stack

## Who Should Watch
Indie developers, solo founders, and small teams looking for a lightweight, self-hosted backend alternative to Firebase or Supabase will find this video valuable. It's especially relevant if you want to understand whether PocketBase's single-binary architecture can handle real-world applications without the complexity and cost of larger BaaS platforms.

## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=0s">00:00</a></span> PocketBase is an open- source alternative to Superbase or Firebase and possibly the simplest backend you could ever run. Just one single file, giving you realtime database authentication and file storage. This is in complete contrast to how insanely complex modern webdev has become. So, in today&#x27;s video, we&#x27;ll test out PocketBase and see if it&#x27;s simple architecture really stands up when building anything beyond a simple app. Pocket Base is a single Go binary with</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=32s">00:32</a></span> Pocket Base is a single Go binary with SQL light embedded, but coding in Go itself is actually optional because the back end can be expanded with both JavaScript and TypeScript. And you&#x27;ll also get access to a basic admin UI where you can configure all of your collections exactly how Superbase works. Now, jumping into the architecture and how you&#x27;d actually use it. Once PocketBase is live, you can connect to it from the front end via the JavaScript SDK. This again is very much the same as how Firebase and Superbase are designed as you can then access your database directly from the front end. And don&#x27;t</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=62s">01:02</a></span> directly from the front end. And don&#x27;t worry, PocketBase has API rules and orth to keep all of these rules secure. But let&#x27;s jump straight into a demo to show a real application with authentication, database, and file storage. And if you&#x27;re enjoying this video, then subscribe to Better Stack as we cover a huge amount of developer content on this channel. So we have our application here. We&#x27;ve got pocket base on the back end and then we&#x27;ve just got a web front end written in React. The most important file inside the web front end is this pb.ts file here because inside here we&#x27;re importing from pocket base. So</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=93s">01:33</a></span> we&#x27;re importing from pocket base. So we&#x27;ve got the pocket base class. We create a new instance of that. Then we can connect to our backend service and then now we can use PB throughout the rest of the application. So the application itself is just a simple bug tracker. We can drag items between columns. we can create brand new issues. So if we look inside the hook that controls the logged in user, you can see initially we set the state with PB or record. So this will just grab the currently authenticated user from pocket base and then we set up a listener as well. So we say if the off store changes</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=125s">02:05</a></span> well. So we say if the off store changes with the onchange event, then we&#x27;ll just set the brand new user into state. So it is really as simple as that. We can access state, we can subscribe to state and the same is true for our issues as well. So inside our use issues hook again we initialize some state but in this case we&#x27;ll leave it empty. Then we have a use effect and we say that we&#x27;ll grab all of the issues get the full list and then we&#x27;ll set the issues with that list. So that would initially prepopulate the data and then we can also again subscribe to issues. So if you drag issues between columns or</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=156s">02:36</a></span> you drag issues between columns or create or delete an issue we can then say pb.colction issues subscribe and then anytime a new record comes in we can then append it to our state. That means when we&#x27;re interacting with the pocketbased database directly, like when we drag a card here, the state would be automatically updated. In the case of creating a brand new issue, we can also attach a screenshot to that. So let&#x27;s grab a screenshot of the application itself. We then click file issue and then the new issue appears here in the frontend code. This is handled through a submit</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=187s">03:07</a></span> code. This is handled through a submit function and then we append all of the form data and then finally we call PB collection issues and then create passing the data in. What we have on the back end is collection API rules to prevent misuse of these APIs. So pocket base will give you this admin interface as default and then here you can see we&#x27;ve got the users collection and we&#x27;ve also got the issues collection where all of our issues live. If we look inside the users collection and then press settings up here, then we have this tab API rules and these are all the rules that restrict access to this particular</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=217s">03:37</a></span> that restrict access to this particular collection. So we say in the case of users, the request or ID cannot be an empty string. And then when updating or deleting users, the ID has to match the ID of the authenticated user. And we can access that with this special string here, the at@ character and then request.orth ID. If you&#x27;ve used Superbase in the past, you&#x27;ll find this kind of pattern super familiar. Now, what happens if the back end doesn&#x27;t do everything you need? Well, luckily, you can extend it via hooks with, of course, Go, but also</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=248s">04:08</a></span> hooks with, of course, Go, but also JavaScript and TypeScript. So, we can hook into events such as on Bootstrap when the app starts or on record create when a database record is created. There are 82 unique hooks at the time of filming, so pretty much everything you need would be covered. Now let&#x27;s extend our PocketBase service to see how it all works. If we look inside the PB folder, you can see we have our PocketBase binary. And this file is literally all you need to run the default version of PocketBase. In my case though, I&#x27;ve written all of the hooks in Typescript.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=279s">04:39</a></span> written all of the hooks in Typescript. So I have some setup to compile those hooks into the PB hooks folder as JavaScript because PocketBase only actually supports JavaScript natively. So if you are using TypeScript, you need to compile it down. If we look inside the main hook file, we can see that we&#x27;ve got a hook here saying on record create. And this is specifically targeting when we create issues. And what we&#x27;re doing here is we&#x27;re saying every time a record is created, we&#x27;re going to send an email to the user. And we can do that by calling e.app new mail client and then send and then passing the message object which we&#x27;ve</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=310s">05:10</a></span> the message object which we&#x27;ve constructed here. You can of course hook into a ton of different features inside PocketBase. So any custom functionality that you might need is always going to be supported with the 82 plus hooks already available in PocketBase. Because this runs SQL light, it means we need persisted storage. So past platforms like Heroku, Render or Railway would actually be a bad fit due to their ephemeral file systems. Basically, you&#x27;d lose your data every time you redeploy your app. To avoid this, you can attach a permanent file system, but the better and cheaper option would just be to host</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=341s">05:41</a></span> and cheaper option would just be to host on a VPS. And that data lives inside the PB data folder. So if we have a look inside here, you can see we have a storage folder and this would contain all of the images that we&#x27;ve uploaded against our issues. They just happen to be stored in the storage folder. So inside this random ID here, for example, you can see the image here that I uploaded against the issue earlier. The database files themselves would also be persisted within this folder. So data db here, this would contain all of our SQL light code. So if I were to delete this file, I would lose all the data in the</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=372s">06:12</a></span> file, I would lose all the data in the application. So obviously you need a good backup strategy rather than just leaving it as a single file on disk. Compared to tools like Superbase, which can start at $25 for the basic tier, Pocket Base is basically free. You just have to pay your VPS costs, which can be as little as $4 and allows you to run as many projects as you like. But of course, you would want to scale this up with usage. Pocket Base also comes with everything you need for production apps like migrations, job scheduling, and logging. You can also serve static files directly with PocketBase by dropping</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=402s">06:42</a></span> directly with PocketBase by dropping them into the PG public folder. And this would be useful for something like a React front end. Alternatively, you can also host dynamic routes with template rendering. And this would be perfect for things like email templates. So, if you do want a singlebox setup, then this is how you do it. Now, the big question is, is this production ready? Well, it does include all of the features that you need to build a modern SAS app, particularly the production grade features like migrations and logging. It&#x27;s also entirely extensible, so you&#x27;re not just stuck with the defaults. But the big gotcha is that this is prev1.</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=WZoC1HA1vec&amp;t=434s">07:14</a></span> the big gotcha is that this is prev1. So, they do explicitly say to only use this if you&#x27;re fine reading change logs and running manual migrations from time to time. But if that is you, then go ahead. You can just build the first single file unicorn. You can learn more about PocketBase by checking out the relevant links down in the description. And if you love open source alternatives, then check out our video on Open Code, the open-source alternative to clawed code. I&#x27;ve been Warren from Better Stack. Thanks for watching and of course, I&#x27;ll see you next time.</p>

</details>
