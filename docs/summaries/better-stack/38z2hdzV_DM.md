---
title: "Is This WordPress's Worst Hack In History?"
channel: "Better Stack"
video_id: 38z2hdzV_DM
url: https://www.youtube.com/watch?v=38z2hdzV_DM
published: 2026-07-30T08:00:07+00:00
generated: 2026-07-30T14:42:34+00:00
model: "z-ai/glm-5.2"
thumbnail: https://i.ytimg.com/vi/38z2hdzV_DM/hqdefault.jpg
---
# Is This WordPress's Worst Hack In History?

[![Is This WordPress's Worst Hack In History?](https://i.ytimg.com/vi/38z2hdzV_DM/hqdefault.jpg)](https://www.youtube.com/watch?v=38z2hdzV_DM)

[Watch on YouTube](https://www.youtube.com/watch?v=38z2hdzV_DM) · **Better Stack** · 2026-07-30

## TL;DR
A critical WordPress vulnerability affecting versions 6.9.0–6.9.4 and 7.0–7.0.1 allowed unauthenticated attackers to execute SQL injection, create rogue admin accounts, and upload malicious plugins for full shell access. The exploit chain was so complex that AI was reportedly essential to discovering it within 10 hours — something no human researcher could have done — highlighting a frightening new era of AI-accelerated attack discovery.

## Key Takeaways
- WordPress versions 6.9.0–6.9.4 and 7.0–7.0.1 contained a severe vulnerability allowing complete admin panel takeover.
- The attack required no malicious plugins — it worked against a standard, stock WordPress installation.
- The exploit chain began via an unauthenticated endpoint (`batch/v1`) and leveraged a desynchronization bug between two parallel arrays (validation and matches).
- Attackers could bypass HTTP method allow-listing, trigger SQL injection through internal request handling, and ultimately create a new admin account.
- Once an admin account was created, attackers uploaded a malicious plugin (e.g., a web shell) to gain full file and shell access to the website.
- The exploit chain was so complex that AI was credited with discovering it in roughly 10 hours — a task that would have taken human researchers weeks or months.
- A Reddit user reported their site was compromised just two days after the vulnerability was disclosed, because they only upgraded on weekends.
- The vulnerability was patched in WordPress version 7.0.2.
- WordPress powers over 44% of the world's websites, making this vulnerability's reach potentially enormous.
- Attackers could clean up after themselves by deleting the rogue admin account, making the breach more discreet.

## Detailed Breakdown

### The Scope of the Vulnerability [00:00](https://www.youtube.com/watch?v=38z2hdzV_DM&t=0s)
The video opens by contextualizing the severity of the hack. WordPress runs over 44% of the world's websites, meaning a critical vulnerability could affect a huge portion of the internet and the data users entrust to those sites. The presenter demonstrates a locally installed, stock version of WordPress and runs a script that returns HTTP 207, confirming the site is vulnerable.

### Demonstrating the Exploit [00:31](https://www.youtube.com/watch?v=38z2hdzV_DM&t=31s)
After confirming vulnerability, the presenter runs a second script that enters an interactive shell. The SQL injector creates a brand-new admin user and uploads a malicious plugin, granting access to interact with any file on the website. This sets the stage for a deeper technical explanation of how the exploit works.

### The Technical Exploit Chain [01:02](https://www.youtube.com/watch?v=38z2hdzV_DM&t=62s)
The presenter references a GitHub repository that details the SQL injection process. The attack begins by calling an unauthenticated endpoint, `batch/v1`, designed to batch multiple requests that are each validated and permission-checked. A bug in the `wp_passse_url_files` function (triggered by an invalid path) caused only the validation array to update while the matches array stayed unchanged, desynchronizing the two parallel arrays. Attackers exploit this by sending a batch containing a single POST request to the `v2/posts` endpoint with a GET request embedded in the body. Because the parent request was validated as a POST, the embedded GET bypasses the method allow-list. A GET request to a nonexistent post triggers the desync, causing WordPress to dispatch the request under `get_items`, where the `author_exclude` field maps to `author_notin`, which the vulnerable build interpolates directly into SQL as a string — unescaped because it runs internally.

### From SQL Injection to Admin Creation [02:35](https://www.youtube.com/watch?v=38z2hdzV_DM&t=155s)
The exploit chain culminates in a POST request to `v2/users` that creates a new admin account. The repository breaks this into six steps: the first five exploit the bug, while step six is simply normal WordPress behavior for authenticated users — uploading a plugin. The presenter emphasizes this works on a standard WordPress install with no third-party plugins required. Demonstration commands show the attacker can read the database user and name, run SQL queries to check the database version, and ultimately create an admin account with a web shell plugin for full filesystem access. After uploading the plugin, the attacker deletes the rogue admin account to cover their tracks.

### Full Admin Panel Access [03:38](https://www.youtube.com/watch?v=38z2hdzV_DM&t=218s)
To further demonstrate severity, the presenter runs a separate script that creates an admin account and leaves it on the system. Using the generated username and password at the `wp-login` route, they log in and gain full access to the WordPress admin panel — showing how trivially an attacker could control a compromised site.

### The AI Factor and Real-World Impact [04:08](https://www.youtube.com/watch?v=38z2hdzV_DM&t=248s)
The presenter notes the exploit chain was so absurdly complex that no human security researcher could have found and completed it in 10 hours without AI. This raises concerns that bad actors could deploy bots to scan repositories, check URLs, and exploit newly discovered vulnerabilities at unprecedented speed. A Reddit user reported their site was compromised just two days after discovery because they only upgraded on weekends. The fix is available in version 7.0.2, and the presenter directs viewers to the repo and article linked in the comments.

## Notable Quotes
- "No security researcher could have found and completed this exploit chain in 10 hours without AI."
- "This is just the standard stock version of WordPress. The vulnerability is not accessed through some sort of malicious plug-in."
- "Bad actors could effectively have bots scanning repos, checking URLs, just waiting for vulnerabilities to appear and exploiting it in record time using AI."
- "One user on Reddit said that their site was compromised just 2 days after it was discovered."

## People, Tools & References Mentioned
- WordPress versions 6.9.0–6.9.4 and 7.0–7.0.1 (vulnerable); 7.0.2 (patched)
- `batch/v1` unauthenticated endpoint
- `v2/posts` and `v2/users` REST API endpoints
- `wp_passse_url_files` function (bug source)
- `get_items` function and `author_exclude` / `author_notin` field mapping
- Web shell (malicious plugin used in the demo)
- GitHub repository detailing the exploit (linked in video comments)
- Reddit user report of real-world compromise
- Better Stack (channel)

## Who Should Watch
WordPress site administrators, security engineers, and anyone responsible for maintaining or patching WordPress installations should watch this to understand the severity of the vulnerability and the urgency of upgrading. It's also essential viewing for security professionals interested in how AI is dramatically accelerating the discovery and exploitation of complex vulnerability chains.


## Transcript

<details class="transcript">
<summary>Full transcript</summary>

<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=0s">00:00</a></span> WordPress has seen a string of vulnerabilities recently with the latest so severe that it lets hackers gain complete control of the admin panel. We&#x27;re talking SQL injection running shell commands. Pretty bad. And maybe you don&#x27;t care about WordPress, but it still runs over 44% of the world&#x27;s websites. So many of the websites that you interact with and give your data to could likely be running WordPress and this vulnerable version. So it basically works like this. So I&#x27;ve got installed locally a standard stock version of WordPress. And I can run this first script to see if the vulnerability is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=31s">00:31</a></span> script to see if the vulnerability is available. And you can see we get the response HTTP 207 which means yes it is in fact vulnerable. And that means we can now run the second check which is that enter the interactive shell. So this SQL injectors site creates a brand new admin user and then uploads a malicious plugin that allows me to now interact with any file on this website. So let&#x27;s dive into the issue and see exactly how it works. So, this repo that I&#x27;m looking at shows</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=62s">01:02</a></span> So, this repo that I&#x27;m looking at shows you exactly how to SQL inject vulnerable WordPress sites. That&#x27;s any site between 6.90 and 6.94 or 7.0 and 7.01. The whole attack starts by calling an unauthenticated endpoint, batch v1, which allows you to batch up other requests that themselves are validated and permission checked. The batch handler has two parallel arrays which are supposed to stay in sync validation and matches. But a bug meant that when the function WP passse URL files due to an invalid path, only validation was</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=93s">01:33</a></span> an invalid path, only validation was updated. So now the same index used to look at both arrays provided mismatched results. The PC takes advantage of this. It sends a batch containing just one request, a post to the v2 post endpoint which itself carries a requests body. Since the parents request was correctly validated as a post request, any request in the request body end up bypassing the method allow list letting you send get requests. Then inside that in a batch is a get request to a post that does not exist which triggers the earlier desync</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=124s">02:04</a></span> exist which triggers the earlier desync causing WordPress to dispatch the same request under a function called get items where a field author exclude maps to author notin which the vulnerable build interpolates into SQL as a string. Basically because all of this is running internally the SQL is not escaped. The PC uses a series of requests that ultimately allows a post request to V2 users to create a new admin account. The repo actually goes through all of these steps in detail. The first five are pre-orth. So take advantage of the bug. But step six is just normal WordPress</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=155s">02:35</a></span> But step six is just normal WordPress behavior for authenticated users, which is to upload a malicious package. Okay. So as mentioned earlier, this is just the standard stock version of WordPress. The vulnerability is not accessed through some sort of malicious plug-in. You can just install standard WordPress. We run this check script first which basically validates if the vulnerability can be run. Then we can run this read command for example which tells us things like the database user and the database name. We can now also run SQL against the website. So we can find out things like which version the database is actually running. And none of that is</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=186s">03:06</a></span> is actually running. And none of that is actually the bad stuff. This is the really bad one where we actually create an admin account that has access to be able to upload a malicious plugin. In this case it&#x27;s called web shell. This allows us to access the shell of the website. Meaning we can now have access to any file on this website. And this attack happens in the way that we explained earlier on in the video. So after the admin is created, the plug-in is then uploaded and then finally that user is deleted. So the existence of the plug-in and what&#x27;s happened is now more discreet. To also demonstrate how bad</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=218s">03:38</a></span> discreet. To also demonstrate how bad this is, I&#x27;ve created a separate script which will create an admin and then keep it on the system. So here I&#x27;ve got a username and a password. And back on the website, if I head over to the WP login route, I can enter that username and password, click login, and now I have full access to the admin panel. Now, if any of this is confusing, then don&#x27;t worry. It took me a long time to work out as well. The claim is that the resulting exploit chain was so absurdly complex that it would have taken a human security researcher weeks, if not months, to discover and piece together on its own. No security researcher could</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=248s">04:08</a></span> on its own. No security researcher could have found and completed this exploit chain in 10 hours without AI. And this is pretty scary because bad actors could effectively have bots scanning reapers, checking URLs, just waiting for vulnerabilities to appear and exploiting it in record time using AI. One user on Reddit said that their site was compromised just 2 days after it was discovered. And since they only upgrade on weekends, an attacker was able to create a new admin and log in. For those vulnerable, the exploit was fixed in version 7.0.2, so you can upgrade to</p>
<p><span class="ts"><a href="https://www.youtube.com/watch?v=38z2hdzV_DM&amp;t=278s">04:38</a></span> version 7.0.2, so you can upgrade to that. But that is a pretty mad one. You can find the repo and the article in the comments that I&#x27;ve used to run the PC. And why not subscribe to Better Stack to stay up to date with all of the tech news. I hope you enjoyed that one, guys. And of course, as always, I&#x27;ll see you in the next one.</p>

</details>
