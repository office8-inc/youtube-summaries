# 📺 How the New York Times Beat Paywall Hackers For Good

## 📋 動画情報

- **タイトル**: How the New York Times Beat Paywall Hackers For Good
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=9Ej9JUnFCO0](https://www.youtube.com/watch?v=9Ej9JUnFCO0)
- **動画ID**: 9Ej9JUnFCO0
- **公開日**: 2025年08月22日 00:07
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

[Music] The biggest war on the internet is between users and payw walls. Developers build payw walls, but also bring them down. Here's how the New York Times brought in a new player. AI payw walls. They don't really need an explanation, do they?

### 📋 背景・概要

You click on an intriguing link, you get an idea of what the content is going to be, and bam, please pay up. And one of the first pay walls to ever exist was in 1996 by Microsoft, believe it or not, with their online magazine called Slate. That was $19.95 annual subscription fee. Later, the Wall Street Journal became one of the first mainstream form of media to install a payw wall, and it was highly controversial, charging $50 a year, or about $100 in today's currency. But the Wall Street Journal spiked to over 200,000 online subscribers.

### ⭐ 主要ポイント

And remember, this is 1998. 200,000 paying customers online. That's pretty wild. With the success, other companies followed suit. But with search engines dominating how users navigated the web, the web was starting to feel like it was blocked by constant pay walls left and right.

### 📝 詳細説明

And to the basic user in 1998, pay walls were a dead end. But not to developers. This was a challenge. In the early days, the web was limited with the technology needed to provide a concrete solution to block non-paying users from content. There were many ways to bypass this.

### 💡 実例・デモ

Even today, one of the first ways websites did this was cookie tracking. Cookies are still used to this day and work the same. When you join a website, a unique cookie is given to your browser. In the website's database, they could keep the ID of the cookie so that the next time you come by, they know you're trying to come back. This method was short-lived because you could just delete your cookies from your browser and get the same experience as if you were a new user.

### 🔧 技術的詳細

Another way was a much simpler approach. Multiple emails. Often you'd get a free trial if you sign up with an email. Once you reach your limit, you just switch over to a new one. Developers were easily able to create email servers that just automatically rotated new emails as needed across many different domains.

### 🎯 応用例

But sometimes the payw walls were just insecure to begin with. Adding the question mark print equal true to the URL would sometimes give you a printerfriendly version of the website. These things are called URL parameters and they're a way you can store the state or data of a website. So let's take an e-commerce website for example. I can change my sorting from A to Z.

### 💭 考察

And then when I want to share this to a friend and send a link, the programmer can change the behavior based on the URL parameters. That way the link that I sent is the exact same as what I saw. So sometimes this means the bypass equal true would work. It just yeah it was not good whatsoever. Now in the early 2000s when JavaScript was kind of becoming the new kid on the block, it was used a lot to dynamically block people from entering their websites.

### 📌 まとめ

But guess what? You can just disable JavaScript on your browser and there you go. And this one is still very popular to this day. But ranking on Google search, you know, before the whole AI results thing came through would require you to have needed info from the user search. So a lot of the times the publishers cached the full version in the search results to then change it for when users come.

### ✅ 結論

However, Google allows users to look at the cache results of the website. So you just go to that instead and you get the full article for free. [Applause] >> It's described as nothing short of breathtaking, a points drop never before seen on the US markets. Despite success from the Wall Street Journal, other companies failed adding payw walls. Then when the dot bubble crash happened, things just got worse.

### 📚 追加情報

Investors wanted more sustainable ways of making revenue. In 2003, the Los Angeles Times paywalled their calendar live section, going from 730,000 users to 18,000 users, a 97% drop. And we have to be honest here, the concept of payw walls is a tough discussion to have. Pay walls are often extremely intrusive and just like a really bad UI quirk nowadays. Even that like, you know, cookie banner that shows up everywhere.

### 🔖 補足

Like sometimes I just click off of a website out of spite. However, how do you monetize a publication without resorting to other factors that can have a negative effect on the journalism provided? Could we 100% trust a publication telling the truth if it also had big ad dollars from a corporation? So, it makes sense why these pay walls are implemented. And historically, they worked, but something needed to change.

### 🎨 セクション 13

[Music] A soft payw wall was introduced by the Financial Times in 2007. Rather than a complete outright block, you would have like 30 free articles a month until you require a payment. And this method of paywalling changed everything. Users would still be able to get free content. Search engines could still index all of their full content, which will bring up their rankings, and payw walls won't prevent users from clicking away.

### 🚀 セクション 14

This was genius from a business standpoint as well. As a reader, I could understand and see what I was getting if I decided to subscribe. This was so successful that in 2011, the New York Times implemented their own version of this payw wall. In the first 3 months, they raised their subscriber count by 224,000 users. And in 2022, it would surpass over 10 million.

### ⚡ セクション 15

This is something that the New York Times is actually well known for. The technology behind their paywalling system. It's not just like a simple if statement that sits in between a server and the client. It's actually more complex. Now, the way that these meters work typically is in a funnel.

### 🌟 セクション 16

You have the unregistered users at the top who read a few articles per day. Then they trickle down into the registered users who don't pay who have an increase of free articles per day. And then the paying customers who can read unlimited amount of times. And this technique in the world of sales is called a foot in the door technique. It's easier to ask the customer for a smaller request before asking them for something bigger.

### 🎬 セクション 17

And this is when the New York Times introduced something called the dynamic meter which finds the best correlation between engagement and conversions. And this meter uses machine learning to analyze how often do you visit, what sections do you read, how long do you spend on the article, and do you share on social media. And the outcomes about the readers were pretty clear. Show the payw wall too early, people bounce and don't come back. Show it too late, the user just never subscribes.

### 📋 セクション 18

So the model will predict what is the most optimal amount of free articles to give you. But there's a massive issue with this approach. We can't serve the user both five free articles and 10 free articles. We have to make a prediction on other related data. This is observed in the fundamental problem of causal inference.

### ⭐ セクション 19

The cause of something needs a comparison. But we can only witness one version of history. One user can only interact one way and not all users act the same way. The machine learning model uses something called an s-arner. An s-learner estimates the treatment using a single machine learning model.

### 📝 セクション 20

But what does treatment mean here? The treatment in this case is the meter limit. How many free articles a user gets. The benefit of slearner is the single which means you can train a single model to test different limits. Without it, the New York Times would have to train a separate model with each number of articles.

### 💡 セクション 21

So that could be like 20 different models, maybe even 50. With the slearner, they can just plug it all into one model and learn from all the data. So the model from the New York Times takes two inputs. The user features, which could be the reading history, the visit frequency, etc., and the meter limit they want to test. So it could look something like this.

### 🔧 セクション 22

Lewis reads four articles per week, loves coding, visits daily, testing the five article limit, and then the output could be a 70% chance of subscribing. The New York Times has developed two of these slearning models, one for the subscription chances and the other for user engagement. The model results are then combined to create an equation of the best chances of subscribing. And when optimized for subscriptions, these metrics return some interesting results showing different results for different types of readers now. Creating a model is one thing, right?

### 🎯 セクション 23

But how do we go out and test it on data that actually matters? Back testing is a common strategy where you take your new algorithm, model, software, program, whatever, and test to see how it would perform on previous data. I've done this when I gave $10,000 to my AI trading bot that was really crappy. You can check out the video here. So they took their data of random control tests and back tested it with the data.

### 💭 セクション 24

They found that a few groups aligned with the model predictions. Again, the issue with the missing data problem, causal inference, it's hard to really determine if that's true. So they just took the data that matched. And after testing, they were able to come to a pretty clever solution. Comparing the back testing with the model results, they can see the optimizations needed.

### 📌 セクション 25

The delta variable can be adjusted to optimize for more page views or more subscriptions based on what the times needs to do for that month which can be expressed in this curve. At the end of the day, pay walls are just annoying to deal with. They are a bad user experience and they're just annoying. But so are ads. To finance this channel, I rely on ad revenue and channel sponsors.

### ✅ セクション 26

So, it's not a perfect industry, but there's ad blockers and payw wall removers. Even to this day, as we continue to use the internet, companies have to keep finding clever ways using machine learning models like the New York Times to bypass users who are trying to avoid ads and pay walls. It's an interesting way of working. If you want a more in-depth analysis, make sure you check out the article which is written by Rohit Supcar. It goes into a lot more detail like with like that math and kind of stuff.

### 📚 セクション 27

It's just great to see them talk about a subject that you know is a bit tough to talk about. Let me know what you want to see next on this channel. Peace out, coders.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年06月09日

</div>
