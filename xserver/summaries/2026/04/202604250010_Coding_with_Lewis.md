# 📺 10億行のデータベースを現実世界で可視化すると？

## 📋 動画情報

- **タイトル**: What a Billion Database Rows Look Like in Real Life
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=sEQ1ecQq0HI](https://www.youtube.com/watch?v=sEQ1ecQq0HI)
- **動画ID**: sEQ1ecQq0HI
- **公開日**: 2026年04月25日 00:10
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

データベースに保存された膨大なデータを「紙」という物理的な媒体に置き換えたらどうなるか？という斬新な視点で、データの規模感をわかりやすく可視化した動画です。1,000行は手のひらに収まるサイズですが、10億行になるとエッフェル塔を超える高さになることをVFXを駆使して実演しています。データベース初心者から中上級者まで楽しめる内容で、インデックスやジョインといった重要な概念も直感的に解説しています。Spotifyが1日に1兆イベント、Uberが1日6兆行ものデータを処理しているという衝撃的な数字も紹介されており、現代のソフトウェアが扱うデータ規模の壮大さを実感できます。

## ⭐ 重要なポイント

- **データ規模の可視化**：1,000行は手に収まる量、100万行は身長（2m）と同じ高さ、10億行はエッフェル塔を超える約2km分の紙に相当する
- **インデックスの仕組み**：インデックスとは「名前順の薄い目次スタック」であり、10億行の中から1行を数ミリ秒で検索できる仕組みの鍵となる
- **ジョインの概念**：2つのテーブルを結合（JOIN）する操作は、データベースならミリ秒で完了するが、紙では現実的に不可能なレベルの作業量
- **企業の膨大なデータ量**：Spotifyは1日1兆イベント、Uberは1日6兆行・約20,000データベースでデータを処理しており、紙換算では宇宙規模になる
- **Postgresの強さ**：Supabaseを活用することで、こうした大規模データを扱うPostgreSQLアプリケーションを容易に構築・運用できる

## 📖 詳細内容

### 🎬 導入

If you could take all the data inside of a database and make it real, how big would it actually be? And I went back to the very first data storage we ever had, paper. This right here is 50 rows of a database on a single page of paper. But, of course, that's an absolute nothing burger. So let's raise the stakes a little bit.

### 📋 背景・概要

Now this right here is a thousand rows of data on pages. Now it seems like nothing but just understand this for a second that a whole entire database I can hold in my hand like this. A thousand users, for example, is nothing to bat an eye at. If I wanted to find someone named John in a database, for example, doing this in Postgres do it in like ten milliseconds, maybe even less. Trying to find it here might take like twenty seconds if I am doing it all in alphabetical order.

### ⭐ 主要ポイント

And like, to be honest, I didn't even try because I just know it's going to be slow and I got things to do. At the end of the day, paper stores data but it's not really good for retrieving data. I don't know why I'm trying to convince you of this. And for 10,000 rows, we have over 200 pages of paper, which seems like a lot. But think about 10,000 rows for a second.

### 📝 詳細説明

That's a decent size application if it's users for example. Now, 200 pages is cool. But if I wanted to do like a 100,000 rows for example, that would cost me a small fortune in paper which a, I don't really want to do or spend the money or b, I mean, it's just not good for the environment, is it? So I flexed some of my VFX skills. If any of you say what prompt I used, I'm going to kill you.

### 💡 実例・デモ

100,000 rows. That's like 2,000 pages of paper, which again, doesn't seem like much at the moment. And 100,000, like, users say, that's obviously just one table. This is not how databases work for the most part. But what happens when we have over a million rows which you know we could add a pets table and get that pretty easily especially with 100,000 users.

### 🔧 技術的詳細

Well, that would equal to 20,000 pages as you can see right here. Basically, the same size as me, two meters tall. This is a lot like the picture of Margaret Hamilton, standing next to the moon code or whatever, except for me, it's not as impressive. I mean, or really impressive at all. Now in a database, this gets queried instantly.

### 🎯 応用例

You don't have to do any waiting whatsoever. This probably happens so many times per second. And these two stacks aren't just sitting next to each other for the fun of it. If I wanted to find out which pet belongs to which person, I'd have to grab a pet, check the user ID, come back here. Yeah.

### 💭 考察

Yeah. I give up. Well, this is what's called a join. Databases do it in milliseconds. I do it in well, never.

### 📌 まとめ

I'm never finishing. On paper, yeah, you just need a lot of time. Joins are one problem. But here's another. What if I just need to find one specific user in this giant stack?

### ✅ 結論

Well, this is where indexes come in. An index is basically a second skinny stack, just the names in order, with page numbers pointing back to the original, smaller than the main stack, way faster to flip through. Now imagine adding sticky notes for letter ranges A through E, F through J, all the way down. I've got the alphabet memorized, hopefully you do too, so when someone asked me to find John, well remember when I said this would take twenty seconds before? Well, it's done now.

### 📚 追加情報

And that's an index. And real databases don't stop at one. You can have indexes on emails, on dates, on anything you query a lot. That's just how Postgres pulls one row out of a billion in milliseconds. Okay.

### 🔖 補足

A 100,000,000 rows. How tall will that be? Well, the database chugs a little as it should. Queries take a little bit longer especially when you're doing this. With paper, that's 2,000,000 sheets.

### 🎨 セクション 13

So in here, well, that's like 20 stacks of paper, my height. Yeah. I can't even walk in here anymore. That's 10 tons of paper and almost $200,000 in printer ink alone, which I didn't even factor in this to be honest. And that's significantly more than my entire camera kit.

### 🚀 セクション 14

VFX saved my life here. But if I was to stack it up all in one, well, we're getting roughly to the height of the Eiffel Tower, all fitting inside of a single database. And this isn't some sort of magic box, it's Postgres, the goat of databases, which you can easily use with the sponsor of today's video, Supabase. You've already heard about them, but Supabase helps you build your project in days rather than weeks with everything you need for a backend like Postgres, authentication, edge functions, storage, and real time subscriptions. You can use Supabase with basically any framework you or your AI agent decides for you, and Supabase scales with you.

### ⚡ セクション 15

Some of my favorite features is branching of your entire project or read replicas for faster speeds to all of your users. To get started, you can go to the Supabase dashboard or if you really wanna go crazy, download the MCP server and just get your agent to do it all for you. Thanks to Supabase for sponsoring today's video. So what about a billion rows of data? You know, as if it was on one table or something.

### 🌟 セクション 16

Well, taller than any building in Canada. That's what a billion rows looks like when you pull it out of the machine and make it real. 20,000,000 sheets of paper. That's two kilometers tall. And of course, we could argue about trillions and whatever.

### 🎬 セクション 17

But I thought, why don't we take some real life use cases and stack it up? See how that goes. So at this scale, companies aren't just storing data, they're drinking from a fire hose essentially. So what does their numbers look like on paper? Spotify generates 1,000,000,000,000 events every single day.

### 📋 セクション 18

Every play, every skip, every search, most of that flows through streaming pipelines, not a single database. But even if you take that same idea of like logs or something being a single row, well, it still adds up pretty quickly. And I did the math. Printed, Vastax passes the International Space Station every single day. Uber ingests over, let's see here, 6,000,000,000,000 rows of data per day across almost 20,000 databases.

### ⭐ セクション 19

So I ran the numbers on just one day of storage. That stack of paper reaches from Toronto to Tokyo. And tomorrow, they do it all again. Now if we have something like Facebook, they have over 3,000,000,000 users. They have trillions of interactions.

### 📝 セクション 20

Their data warehouses passed 300 petabytes years ago. I mean, and if I try and calculate this one, you're past the moon at this point. I just I couldn't even figure it out because it's just so much data. But imagine all of that just one day at a time. I start off with a question, how big is your data if you make it something physical?

### 💡 セクション 21

And honestly, the answer is pretty surprising. A thousand rows fits in my hand, a billion towers over my house. And the software that we're using every single day is generating space level heights almost every single day, which makes you really think like, wow, that's just insane. And despite us knowing how much data and information we're going through on a daily basis, that kind of scale makes us think like what crazy technology is able to retrieve the information at millisecond speeds. So next time you spin up an empty database, understand you're opening up a gigantic file cabinet that could be endless.

### 🔧 セクション 22

And if you want to start your application with Postgres, make sure you use Supabase. It's a great platform. I use it for my clock car video that you might have seen as well as almost everything. So thank you Supa Base for sponsoring today's video.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年04月27日

</div>
