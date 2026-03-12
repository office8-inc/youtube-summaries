# 📺 The Incredible Engineering That Saved Slack During COVID

## 📋 動画情報

- **タイトル**: The Incredible Engineering That Saved Slack During COVID
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=WFpEvs2sjgs](https://www.youtube.com/watch?v=WFpEvs2sjgs)
- **動画ID**: WFpEvs2sjgs
- **公開日**: 2025年09月25日 00:41
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

What happens when the entire world shuts down and is forced to use your software overnight? COVID nineteen. COVID nineteen. COVID nineteen. We've [speaker 1] been setting up a lot of remote tools, Slack, Zoom.

### 📋 背景・概要

We've built a remote workforce that is very talented. This [speaker 0] is how Slack went from thousands of database queries per second to 2,300,000, and it didn't crash once. Slack was released in 2013 as an internal communication tool for organizations. Slack was groundbreaking at the time. Communicating with different members of your team were often scattered around different places like email, project management software, or sticky notes.

### ⭐ 主要ポイント

Where Slack made a difference was that it would take your entire team and put them into a chat like system with integrations with the tools that you're most likely using. This let members in an organization move much faster. Right at launch, over 8,000 new users signed up. Two years later, 1,000,000 active users. Then in 2019, over 10,000,000 daily active users.

### 📝 詳細説明

It was Humble Origins. Believe it or not, Slack started as a simple LAMP application. Linux, Apache, MySQL, PHP, Python, or Perl. This stack still is one of the most popular ways to make web applications to this day. A Linux distribution is used as the server to host these applications while also providing other functionalities like cron job file management, logging, and more.

### 💡 実例・デモ

Apache is the web server that handles the requests that come in from the users as well as serves the web pages to the users. MySQL is the database that stores and manages the application data. PHP, Python, or Perl is the server side programming language that connects everything together and works out the logic of how things will work. So in Slack's case, tell the database to store a message, generate the way the page is supposed to look, and send it back using Apache, etcetera. If you've developed any sort of web software, you've most likely worked with one of these technologies before.

### 🔧 技術的詳細

And the great thing with these technologies is that they are flexible to fit whatever your needs are. Here's how Slack had it serving their first customers. All of the data from Slack was stored in three MySQL database clusters. Shards was where the customers, messages, channels, DMs, and more were stored. The data was partitioned and scaled horizontally based on your workspace ID, similar to how Notion did it if you want to check out that video right here.

### 🎯 応用例

Metadata was used as lookup tables to map the workspace ID to the required shard. So when Slack needed to find the information needed to get your Slack messages, it would have to stop here first to find it, almost like an index or table of contents. KitchenSync was what stored all other data that wasn't linked to a workspace ID but was required for Slack to work like their app directory or analytics. And all of this data was managed by a monolith application called WebApp. WebApp contained the logic to look up metadata for a workspace and create a connection to the shard associated with it.

### 💭 考察

Each shard would hold thousands of different workspaces and their data. These shards would have two identical copies in separate data centers. And there were many advantages to this infrastructure method. High availability since there are two shards in different data centers. You could just switch databases if one didn't connect, for example.

### 📌 まとめ

Developing with this method meant it was easy to add new functionality since all of the data was on one database. It's easy to migrate new columns or tables, and easy to scale since you could just add more database shards when more people joined. But just like anything in tech, there's tradeoffs. Every company wanted to join Slack. For companies with 150 employees or under, no problem.

### ✅ 結論

But what about mega corporations with tens of thousands of employees? Even the largest hardware you can put on a database wouldn't be enough to store this data. Developing new features became harder and harder over time, specifically Slack Connect, where a channel on your workspace was directly connected to a channel on someone else's workspace. With the sharded infrastructure, this was a challenge. And also, databases are expensive.

### 📚 追加情報

So a lot of the times, Slack would add more databases than needed while also running into issues of having slow points with larger companies, so top down, they would just have areas in their infrastructure that were hitting extreme traffic limits, while others were almost unutilized at all. This was becoming a problem fast. [speaker 1] I'm excited to to talk to you today. Just by show of hands, how many of you use Slack or or know about Slack? Because I think it's everyone.

### 🔖 補足

Cal, maybe give folks a sense of what's the latest with Slack just in terms of numbers. Kind of [speaker 2] where are you? So we're at about 9,000,000 weekly active users, across about 50,000 companies all around the world. [speaker 0] In 2016, Slack was going through hundreds of thousands of My SQL queries per second and thousands of sharded databases. It was getting to a point where the team at Slack kept seeing spikes in the graft and patching in solutions.

### 🎨 セクション 13

But this was obviously a shaky way of doing things. At times, messages were getting slower to deliver and at times, completely unresponsive. Since everything was split by Workspace ID, large customers were often the bottleneck overloading a server despite them not looking for the same data as you. And with the growth of Slack, there's lots of things you want to get around to, but this was the breaking point where a serious question needed answers. Should we evolve the current approach or completely replace it?

### 🚀 セクション 14

Since everything was split by Workspace ID, they weighed their different options, which they had to do fast. They could switch over to a NoSQL database like DynamoDB or Cassandra. However, since Slack was using MySQL since 2013, a lot of their existing tooling that is used to backup, deploy, ensure compliance, and more were written with MySQL queries that were exclusive to that database. So moving over would've been disruptive. They could rebuild their own sharding solution.

### ⚡ セクション 15

Since there were already sharding, they could start sharding databases by channel ID as well. After evaluating this option, they realized that it was much more time consuming than they initially believed with their existing codebase. And this was a big issue in of itself. The old codebase assumed a ton of their existing infrastructure. Their codebase had a ton of code that was like this: hardcoded areas that required you to look in specific shards.

### 🌟 セクション 16

For example, teams and channels. Rebuilding their sharding system wouldn't work too well in the long run either because they would just run into the same issues they did now if one of the shards got overwhelmed. However, there was another option that got the Slack engineers' attention. Vtest. In 2010, YouTube ran into a similar issue with scaling their databases.

### 🎬 セクション 17

Reaching over 200,000,000 users, YouTube's MySQL reached a point when their peak traffic would exceed their serving capacity. YouTube created a master database for write traffic, like creating comments, uploading videos, giving thumbs up, and then adding read replicas for viewing. But this would only partially alleviate their problems. As we all know, YouTube never stopped getting popular. You're watching this video on YouTube.

### 📋 セクション 18

It just continued to rise and rise. And so the read replica databases were just starting to give out. To distribute traffic, more read replicas were added, but this was just kicking a rock down the road. And with the rise of smartphones and YouTube going on Android devices, their rights to their master database was also exceeding their limits. So they would shard the database again.

### ⭐ セクション 19

Now that we have every database sharded and in all kinds of places, they needed to create an application that's sole purpose was to look at the query from the user and find the right shard in the database, similar to how Slack does it. And this is when YouTube decided to create vTest. VTest serves as a proxy between your application and the database to route and manage database interactions. This way, you don't have to worry about including that logic in your application code. It's also completely MySQL compatible.

### 📝 セクション 20

VTest then joined the nonprofit Cloud Native Computing Foundation in 2018. The Slack engineers looked at Vtest and decided to cross off all of their requirements, built on top of MySQL, can easily scale to the operation that they already had, was able to handle failovers and backups. Most importantly, it's open source and was built with the Go programming language. That way, if something needed to be extended with it, they can go in and do it themselves. The team built a prototype to see that they can migrate data from their traditional architecture to vTest, and this would take a significant effort.

### 💡 セクション 21

But they had to do it fast. The goal for this prototype was to build a working end to end use case of Vtest for a small feature in Slack, integrating an RSS feed into a Slack channel. RSS has been around for a long time. On most websites, it's just an XML file that constantly updates with new information regarding that website. So if you posted a new blog article, podcast, or video, your RSS feed will update with that entry and applications can easily parse the results of it so that they can create their own feed for a to read app or in Slack's case, to post updates on a channel.

### 🔧 セクション 22

The engineers went through each level of their development stack to refactor and rejig code. Deployments, service discovery, backup procedures, topology management, credentials, and more. Specific endpoints were required to route the queries through v test. A backfill system was made to clone the existing tables while performing double writes from the application as well as double reads in parallel. I actually explained how this works in my video about how Uber switches over databases.

### 🎯 セクション 23

But essentially, a double write system is when you write to both your current in production database as well as the one you want to migrate to, refactor the metadata service to work across isolation regions, adding support for updating columns with a secondary lookup v index, adding better integration support with visualization tools, adding tools to simulate query plans, and more, which the engineering team have developed and posted in the open for anyone to use. After seeing everything working fine and flawlessly, the Slack engineers decided that this was the future they were hoping for and made a transition slowly. The web servers go to Vtest. When Vtest gets the request, it goes into something called a VT gate. This is the proxy that routes traffic to the correct data location and returned the results back to the client.

### 💭 セクション 24

Slack has set up multiple gates for different request types. Web traffic for real time needs, so this would be when you send a message, you search something, or get real time updates. Queue traffic for when timing isn't important, so sending a notification to a user, indexing messages for search, or processing file uploads, the VT gate gets the information from a VT tablet, which is a server that runs MySQL. VT tablets are organized as keyspaces. In these keyspaces are the primary databases as well as the read replicas as mentioned earlier on.

### 📌 セクション 25

Think of it like a group of databases, and this setup would eventually be pivotal in one of the craziest moments in the history of Slack. Six months after migrating the RSS feeds, they decided that all the new tables will be created in vTest. One year later, 25% of all the tables were migrated using vTest. In July 2019, there were more rights to the database in vTest than their legacy database system. And in December 2019, about 45% of the tables have migrated over.

### ✅ セクション 26

[speaker 1] Concern about a new and rare pneumonia like virus. A new disease. We don't know a lot about this virus. How worried do I need to Information will continue to develop. A new name for the coronavirus.

### 📚 セクション 27

COVID nineteen. COVID nineteen. COVID nineteen. COVID nineteen. A virus more powerful than any terrorist attack.

### 🔖 セクション 28

[speaker 0] A pneumonia like virus was discovered spreading in Hubei with over two hundred and sixty six cases by the end of the year. Chaos was erupting in China, but the whole world didn't even notice yet. Every seven and a half days, cases of this virus would double, going to different provinces in China. By the January, close to eight thousand people had been infected, leading to the World Health Organization calling for a public health international concern. But alarm bells were still muted by the rest of the world.

### 🎨 セクション 29

The virus was found in Italy shortly after. Then, some in The United Kingdom. Now, The United States. Panic happens almost immediately. One month later, The United States has overtaken China with the highest number of confirmed infections.

### 🚀 セクション 30

Then, almost overnight, the world changed. In just three months, we went from a couple hundred people in China to almost one million cases worldwide. One of the first times in history we experienced something that never happened before. Governments and corporations around the world enforced or required a stay at home policy. Phones, computers, and laptops were the primary way most people needed to work across all fields.

### ⚡ セクション 31

This wasn't just a random traffic spike. This was a fundamental shift in how the world operated. What seems like overnight, a trendy tech company that lets you talk to your coworkers in chat interface with silly emojis became the primary communication method most people relied on to pay their bills. And over the past seven years, Slack's growth was steady and predictable. This wasn't just a random traffic spike.

### 🌟 セクション 32

In just one week in March 2020, database queries didn't just increase, they exploded by over 50%. To put that into perspective, if you're at 1,500,000 queries per second, you're suddenly handling 2,250,000 every single second. That means more channels, teams, messages, images, emojis being added every second. Unlike something like Black Friday where you know it's coming, this surge hit with zero warning or time to prepare. Remember, the Slack engineers weren't able to just upgrade physical hardware or optimize code on the fly.

### 🎬 セクション 33

The Slack engineers had to think quickly. How can we handle this sudden surge in traffic? This was the moment three years of preparation paid off. The messages Keyspace which would handle the messages coming in was under critical load and any moment about to collapse. But with VTest, they could do something they couldn't before.

### 📋 セクション 34

Split the overwhelmed database while millions of users were actively using it. Horizontally scaling is a common trick to scale fast. Slack had already been doing this, but essentially, rather than upgrading your existing database to a larger unit, you create a clone of it and start moving traffic there. This takes traffic off the main database. Vtest was able to do this live.

### ⭐ セクション 35

As the amount of users grew and grew, vTest became one of the best investments made by the Slack engineering team. Without making the switchover, databases would get overwhelmed and shut down for everyone, adding more pressure to an already terrible time in modern history. This type of load was truly a test to see if VTest was the right move. Slack's engineers were clear about what would happen without VTest, complete inability to scale for their largest customer. The ripple effects would have been catastrophic.

### 📝 セクション 36

One of the hardest things you can do is scale your database. It's literally the source of truth for most applications. So when you have to find ways to scale it to accept more connections or divvied it up to properly handle many real time users, you always risk going down. This video is based on the article that was written by Arca, Guido, Maggie, and Rafael, engineers at Slack in 2020. Something I really liked that they mentioned is the importance of how collaboration in the world of software engineering is extremely important.

### 💡 セクション 37

We talked about how VTest originally was by YouTube, but then open sourced so even you and I can use it, and this is what makes open source so essential to every project that we use on a day to day basis. Thanks so much to the engineers for being very transparent with the hits and misses that they made on this journey. If you like this type of video, check out how Notion scaled to billions of nodes or how Discord handled its largest server ever.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年03月13日

</div>
