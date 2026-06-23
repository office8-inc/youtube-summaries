# 📺 The Database That Should Be Dead but Runs the Internet

## 📋 動画情報

- **タイトル**: The Database That Should Be Dead but Runs the Internet
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=_CB_Aa2ODeM](https://www.youtube.com/watch?v=_CB_Aa2ODeM)
- **動画ID**: _CB_Aa2ODeM
- **公開日**: 2026年06月23日 23:51
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

Right now, a radiology system at a hospital is deciding which scan to show a doctor first. A trading algorithm is processing tens of thousands of transactions per second. And both of these depend on software that they couldn't replace. Maintained by the same nobody. In 1970, a computer scientist at IBM named Edgar F.

### 📋 背景・概要

Codd published a short paper. It described something called the relational model, a way of organizing data into tables, rows, and relationships. And this could be queried with mathematical precision. For 3 years, nobody actually implemented this. That is, until two professors, one named Michael Stonebraker and Eugene Wong, decided to prove that the theory could work in practice.

### ⭐ 主要ポイント

And they called their project Ingres. Surprisingly, it worked. Better than anyone actually expected. Ingres became the proof that relational databases were only just a theory. They were the future of computing.

### 📝 詳細説明

University shared the code. A generation of database engineers trained on it. The relational model went from just a simple academic paper to industry standard. And Ingres was a big reason for that. But then in 1980, Stonebraker did what researchers do when the research works.

### 💡 実例・デモ

He started a company. And this wasn't the first time. In fact, Stonebraker would do this probably nine times across his career. Build the proof, commercialize it, and then move on to the next idea. Research that could be turned into product of some sort just simply wasn't done.

### 🔧 技術的詳細

But by 1985, he was back at Berkeley. Relational Technology ran without him. He'd spend a decade watching users hit the same walls with it. The database was simply built around a specific kind of work: payroll, inventory, accounting. Outside of numbers, text, and dates, it couldn't really store much else.

### 🎯 応用例

And if you were a chemist with a molecular structure, or a mapmaker drawing a coastline, or an engineer designing a circuit, you couldn't just put your data into this database and call it a day. You had to break it into rows and numbers and rebuild it yourself every time you needed to use it for your project. It was the limit of his own creation. Most engineers who built something successful spend the next decade defending it. Stonebraker looked at his own success and saw what it couldn't do before he saw what it could.

### 💭 考察

So, he thought, "What would I do differently?" And that question became a brand new project, a complete rewrite, and he called it Postgres. Post-Ingres, named after the project it was leaving behind. But this time, it wasn't going to store just the world of business. It was going to be able to store everything. And so, funding came from DARPA, the agency that funded the internet, basically, from the Army Research Office, the National Science Foundation, a defense contractor called ESL.

### 📌 まとめ

We have military public money going in to build what would become one of the most open pieces of software in history. But this ambitious idea came at one of the most hostile markets in tech history. In the database wars of the 1980s, performance was the only argument that really mattered. It was the only thing that translated into profit, essentially, especially when you're dealing with businesses. Fast reads, fast writes, fast everything.

### ✅ 結論

So, when Stonebraker said he wanted to build a database that was correct over fast, it was definitely an uphill battle. His bet was extensibility, custom data types, custom index methods, custom query operators. A database that wouldn't be a fixed product, but a platform that could grow as computing also grew, which was fast. Nobody in 1986 knew what that would mean, not even Stonebraker himself did. By 1992, the research was done with version 4.2, the final Berkeley release of Postgres.

### 📚 追加情報

And after that, Stonebraker did what Stonebraker does. He started a company to commercialize Postgres, and venture capital funded it. Stonebraker left Berkeley for the second time. Two different theories about how software survives now began running in parallel, both with completely different ideologies on what makes software successful. One path, commercialization, resources, customers, direction, and the other, an FTP server at a university and whoever happened to find the address by coincidence.

### 🔖 補足

This video is sponsored by Supabase, which for a documentary about Postgres makes a lot of sense. Supabase is built on that second path, the one that nobody bet on. When you spin up a Supabase project, what's running underneath is real Postgres, the same database this whole video's about, the one behind the hospitals and the banks. Supabase runs it as a managed dedicated database, and build the rest of its back end around it like authentication, file storage, and auto-generated APIs. You get all of that hosted without running the server yourself.

### 🎨 セクション 13

And because it's standard Postgres, the whole ecosystem comes with it. Extensions like vector search for AI, PostGIS for mapping, and more. The standard tooling too. You can connect with PostgreSQL, PG dump or any PostgreSQL client that you already use. It's the same PostgreSQL that you run everywhere.

### 🚀 セクション 14

And Superbase also puts work back into PostgreSQL itself. They acquired Oriole DB, a new storage engine from PostgreSQL, built by Alexander Korotkov, a PostgreSQL committer who now works at Superbase. And they've said that they wanted to upstream that work into core PostgreSQL. They use what these strangers built and give back to it. You can start your project for free now.

### ⚡ セクション 15

Thanks again to Superbase for sponsoring today's video. All right, back to it. Andrew Yu and Jolly Chen were PhD students at Berkeley in the mid-90s, finishing their education and prepping to move to industry. They were not database legends or men on a mission. They just simply needed to use PostgreSQL to behave like a real database, one that other systems could talk to.

### 🌟 セクション 16

But one issue is that PostgreSQL used its own query language called Quel. Well, nobody outside of Berkeley had learned it. The rest of the database world had converged on something called structural query language or SQL for short. And PostgreSQL just didn't speak it. Any developer trying to connect it to an existing system hit a wall.

### 🎬 セクション 17

The database might as well just not exist at that point. So, they did what programmers did. They added SQL themselves. Without a grant or a mandate, without asking Stonebraker himself, who was obviously busy building Illustra. They needed it for themselves.

### 📋 セクション 18

Putting it on the internet cost them nothing. Nobody else was going to do it. So, they did it. And they called it PostgreSQL 95. Just a version name, not really a project name.

### ⭐ セクション 19

Someone else can take it from here. So, on September 5th, 1995, they sent the announcement from a personal email domain, that kind of distribution channel that didn't exist for software that anyone took seriously, even today to be honest. And they heard nothing back. You finished his education and joined HP while Chen also finished his and moved to the industry. The code went into the world without the authors.

### 📝 セクション 20

This time for the second time, the researcher built it and left. And then the students fixed it and left. Each handoff happened almost by accident. Mark Fournier ran hub.org, a small Canadian hosting company operating out of a leased rack space in an era when the internet was run by people with large phone bills and hardware that they'd already bought. He'd been following the project from outside.

### 💡 セクション 21

And he thought it was worth preserving. He had what it needed, a server essentially. And so he offered it. The first non-university server in PostgreSQL's history given by someone the project had never asked. Bruce Momjian was a consultant in Philadelphia who needed an SQL database for his home Unix machine.

### 🔧 セクション 22

And so he found Postgres 95, free with code legible enough to read. He started filing patches. No employer in the picture or no grant, just a mailing list where strangers in different time zones would review each other's work and either merge it or push back. And for years through the long stretch where the project had no obvious future, he kept coming back to it and surprisingly so did the others. And so by 1998, three years of volunteer patches, each one solving problems and sometimes creating another, had piled into a debt the project had not had the people to pay.

### 🎯 セクション 23

So, for several months, it was unclear whether the project would stabilize or just completely collapse under its own weight, as open source software often does. In Pittsburgh, Tom Lane was running a small trading models business. He needed a database, like most developers too, and he chose Postgres for one reason and one reason only. The code was clean and readable. He filed a few patches, then a few more.

### 💭 セクション 24

He started looking at the query optimizer, the layer that decides how every single query runs, and the component most likely to produce the silently wrong answers before anyone caught them. And after two or three years, in his own words, he realized he was basically shrinking SSS work completely and spending all my time on Postgres stuff. The trading models faded into the background. The optimizer became his life's work almost by accident. Then Vada Makeev was contributing from 3,000 km east of Moscow.

### 📌 セクション 25

He was working on MVCC, multi-version concurrency control, the feature that would define what Postgres felt like to use by letting readers and writers stop blocking each other. And he did this from a country whose economy had collapsed just years earlier, where a stable software job was not a given, let alone unpaid work on a foreign project with no clear future. His patches arrived in North American inboxes before anyone had even woken up. And when Lane opened his email in the morning, Makeev had already been working. The project had built a development cycle that did not sleep.

### ✅ セクション 26

That's when PostgreSQL 6.5 shipped in June of 1999 with Mickey's MVCC at its core. A stabilization release, proof that the community could hold together under pressure, deliver a major feature, and not break the existing system in the process. And that was the most important thing they ever proved. But meanwhile, Ingres sold to Ask, then to Computer Associates, then wandered through corporate owners for decades. And today it's called Actian.

### 📚 セクション 27

It is used by almost nobody. Illustra was acquired by Informix in 1997 and absorbed by IBM in 2001. And whatever it had been, it was something else now. The open version was on a donated server in Canada, maintained by people who fixed their own bugs. And the next decade would test whether that was really enough.

### 🔖 セクション 28

For the next 30 years, the volunteer track would face the kind of pressure that kills open source projects almost immediately. CouchDB faded. RethinkDB ran out of money and shut down. MongoDB pulled its license to fend off cloud providers. Elastic did the same.

### 🎨 セクション 29

And Redis did the same. Half the relational systems of the 1990s and early 2000s, Firebird, MSQL, the original Sybase, Informix, survived today as footnotes, if at all. And so Postgres faced the same waves. And it had less than any of them. No CEO, no marketing budget, no defensive moats, just the mailing list, the maintainers, and whoever happened to show up that week.

### 🚀 セクション 30

The first sign that the volunteer model was working came from places nobody expected. When Oracle acquired Sun Microsystems, the European Commission ran an antitrust review. And in its January 2010 clearance, the Commission named PostgreSQL by name as the credible alternative that could constrain Oracle's market power in the database industry. A regulatory body in Brussels had decided that a project with no owner was substantial enough to hold a multi-billion dollar company in check. Let that sink in for a second.

### ⚡ セクション 31

A year and a half later, Apple shipped OS X Lion Server. MySQL had been removed. PostgreSQL was running in its place. No press release, no announcements. Just engineers inside Cupertino who had reached the same conclusions as the regulators.

### 🌟 セクション 32

And so for the first time, the volunteer track was being treated as load-bearing infrastructure by the institutions that ran the modern internet, not just as an interesting experiment. And that recognition came at exactly the wrong moment. In 2009, a generation of developers decided that the relational model was over. NoSQL arrived. MongoDB raised hundreds of millions of dollars on the argument that the rigid table and row structure of databases like Postgres was a legacy idea.

### 🎬 セクション 33

Fine for accounting in 1985, but useless for the unstructured data that powered the modern web application era. Every conference, blog post, job posting reinforces message. Relational was the past and open source databases that didn't that got abandoned by their developer communities. The mailing list thinned, the patches stopped, the projects didn't shut down, they just stopped being relevant, which is the same thing. But slower.

### 📋 セクション 34

But on the Postgres mailing list, the volunteers had an argument on their hands. Some maintainers felt JSON support, the document format that NoSQL had popularized, would blur what Postgres was meant to be in the first place. A relational database that pretends to be a document database, they said, is just a worse document database. And others said that refusing to build it was handing the future to MongoDB. The debate ran for months between people who had never met with no CEO to break the tie.

### ⭐ セクション 35

There was only the mailing list, the arguments, the patches, and the rule that nothing shipped until enough of the maintainers were convinced. And from the outside, it looked like a process that should not be able to make hard decisions. From the inside, it had been making hard decisions for almost 15 years. PostgreSQL at 9.2 shipped in 2012 with native JSON support. Two years later, JSONB, a format that gave the flexibility of a document database with the guarantees of a relational one, and the extensibility design from 1986, Stonebraker's most academic-sounding decision, had just shown what it was for.

### 📝 セクション 36

Postgres didn't have to choose between relational and document. It simply could be both, and that was by design. NoSQL didn't kill it. The volunteers built the missing capability themselves, and then kept moving. And the next wave came from a direction nobody saw coming.

### 💡 セクション 37

In the mid-2020s, every major cloud provider started selling managed PostgreSQL. Amazon's RDS for Postgres, Google Cloud SQL, Azure Database for PostgreSQL. Trillion-dollar companies taking the work of unpaid volunteers, charging customers for it, and keeping the revenue. And other open-source projects watched this happen, and just completely broke. MongoDB changed its license in 2018, and Elastic changed its license in 2021, and Redis changed its license in 2024.

### 🔧 セクション 38

The argument was the same in each case. Cloud providers were extracting value from open code without contributing back. The community was being mined. Postgres didn't change its license, though, and that somehow made the world of difference. The maintainers had a choice.

### 🎯 セクション 39

They could lock the project down, pull the permissive license that had been there since the absolute beginning, and then switch to something that restricted commercial use, force the cloud providers to pay. Or they could keep going as they had since 1996. And so, they made the choice to keep going. And then, something unexpected happened. Because the license stayed permissive, the cloud providers and the new ecosystem of companies built around Postgres developed a stake in the project's health.

### 💭 セクション 40

They started hiring maintainers, paying them salaries to do what they had been doing for free for so many years, funding feature work that volunteers wouldn't have had time for otherwise. And the thing that looked like extraction turned into the strangest possible alliance. The biggest companies in software ended up sponsoring the people who maintained the database that their products depended on. And this is where the project could have died for real. The history of open source software is full of projects that have started as community efforts and ended as corporate ones.

### 📌 セクション 41

The pattern is gradual. A sponsor hires a few maintainers. The sponsor's priority becomes the road map, and eventually the sponsor is the project, and the community is a logo. Postgres has resisted that pattern for going on 20 years. The reason is structural.

### ✅ セクション 42

No single company funds most of the maintainers. The funding is fragmented competing sponsors that each have a stake in the project staying neutral. None of them can capture it without the others objecting. The mailing list still works the same way it did in 1998. The patches still get reviewed from different employers who don't always agree.

### 📚 セクション 43

And it looks fragile from the outside, but it has been fragile in the exact same way for 30 years. It somehow keeps working. In April of 2021, a year and a half before ChatGPT existed, a developer named Andrew Kane shipped an extension called PG vector. It added vector data types and similarity search to post grass. He didn't ask permission.

### 🔖 セクション 44

He didn't need to. The extensibility design from 1986 had made it possible. He saw it coming and he built it. And after the launch of chat GPT, the market for vector databases exploded. Venture capital funded a half a dozen new entrants, each one with a dedicated database for storing coordinates that machine learning models produce.

### 🎨 セクション 45

Post grass already had one sitting in a public repository available to anyone for free, written by one person who built it 18 months earlier. And so in 2023, post grass took over my sequel as the most used database among professional developers for the first time in the survey's history. The next year it stayed on top. And this was only possible because they showed up for nearly 30 years. But before any of that, there was a moment in 2015.

### 🚀 セクション 46

The Association for Computing Machinery had announced the winner, Michael Stonebraker, for ingress for post grass. And he said the biggest impact of post grass by far had come from the two Berkeley students he affectionately called grumpy and sleepy. He set a pick up team of volunteers, none of whom had anything to do with him or Berkeley, had been shepherding the open source system since 1995. And then he said this, "It is open source at its best. But I want to just mention that I have nothing to do with that.

### ⚡ セクション 47

And that collection of folks, we all owe a huge debt of gratitude because they have robusted that code line and made it so it really works. And he didn't know all of their names, but he knew that they existed, knew that they had taken and built and made it into something that he couldn't have made." Standing at the podium receiving the highest prize in this field of work that included post grass, he said it. The thing that won was not what he built. So, who owns the database running your hospital, your bank, your airlines? Well, nobody.

### 🌟 セクション 48

A professor who knew what an abandoned project looked like and moved on anyway. Two grad students who fixed a problem they needed fixed and then got on with their lives. A Canadian with a spare rack space. A consultant in Philadelphia who kept giving up evenings and weekends to a project that he had no commercial future. And dozens and dozens of volunteers over 20 years.

### 🎬 セクション 49

Some of them now draw salaries from companies that depend on what they built, but none of them own it. And the crazy part is the volunteers who carried Postgres aren't young anymore. The same pick up teams don't break or thank to 2015 has been the same team more or less for two decades. Some are still in their day jobs. Some are paid by companies that depend on the project.

### 📋 セクション 50

Some have stepped back. Stonebraker had a successor. He didn't choose them. He didn't even know their names or didn't ask them to show up. They just simply did.

### ⭐ セクション 51

And the maintainers don't have one. The generation of database engineers being trained today learn on cloud platforms where the work of running a database has been abstracted away from them. The most critical database infrastructure on the internet has no single owner. It belongs to whoever decides to show up. But the question is whether anyone actually will.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年06月24日

</div>
