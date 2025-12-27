# 📺 魚に1万ドルを渡して株取引をさせてみた

## 📋 動画情報

- **タイトル**: I Gave This Fish $10,000 to Trade Stocks
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=cjoYPSbzHV0](https://www.youtube.com/watch?v=cjoYPSbzHV0)
- **動画ID**: cjoYPSbzHV0
- **公開日**: 2025年11月21日 01:25
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画では、魚にS&P 500銘柄の株取引をさせるという前代未聞の実験が行われています。当初は鳥でテストしたものの失敗し、魚の群れの集合知を活用する「民主主義システム」を開発。YOLO（You Only Look Once）を使った物体検出、バイトトラックによる追跡、そしてInteractive Brokersとの統合により、実際に3日半の取引で結果を出しました。コンピュータービジョン、アルゴリズムトレーディング、集合知の研究に興味がある人にとって、技術的にもエンターテイメント的にも非常に面白い内容です。

## ⭐ 重要なポイント

- **YOLO物体検出の活用**: YOLOv8とバイトトラックアルゴリズムを使用し、魚の個体を正確に追跡。オクルージョン（遮蔽）問題にも対応
- **集合知の民主主義システム**: 水槽を4分割し、最も魚が集まったエリアの株を購入。上半分/下半分で保持/売却を決定
- **バックテスト結果**: 過去30日間のバックテストで446ドルの利益（4%の利益率）を記録し、S&P 500に迫る成績
- **実取引の結果**: 3.5日間の実取引で約12%の損失。AMCの急落が最大の原因で、S&P 500も同期間に3%下落
- **技術スタック**: Modal（クラウドGPU）、Interactive Brokers API、Redis（ブロッキングPop）を使用した高速取引インフラ

## 📖 詳細内容

### 🎬 導入

I give fish ten thousand dollars Speaker: and let them trade stocks all on Speaker: their own. Speaker: But getting here took months and Speaker: started with a completely Speaker: different animal. Speaker: Three years ago, I watched Speaker: Michael Reeves video where he Speaker: did something similar with a Speaker: goldfish. Speaker: And I thought, why don't we do this with an actual live stream Speaker: that is happening right now? Speaker: The technology exists in order to do it, and I build this Speaker: channel on having the funds to do stupid things like this.

### 📋 背景・概要

Speaker: In fact, I've done something similar. Speaker: So here's what I was thinking. Speaker: I will take this twenty four over seven live stream of birds Speaker: coming and going in this area. Speaker: Every time a bird comes into the frame, we assign it a random Speaker: stock from the S&P five hundred. Speaker: And while it stays on screen, eats chills, whatever.

### ⭐ 主要ポイント

Speaker: We hold that position. Speaker: And when it flies off the screen we sell the the position. Speaker: So we're going to be selling a lot of stocks essentially. Speaker: Let's see if it works though because who knows maybe it will. Speaker: Computer vision is really easy to implement nowadays.

### 📝 詳細説明

Speaker: I mean really even five years ago, one of the most popular Speaker: ways to do this is you only look once or YOLO, which is funny Speaker: because my brain's current algorithm is also YOLO. Speaker: In this project, YOLO learns what something looks like based Speaker: on the dataset that you give it. Speaker: Then it splits your frame or Speaker: image into a grid and looks Speaker: through it to see if there's an Speaker: object. Speaker: It will then give a confidence Speaker: score on that object being a Speaker: bird or whatever you're looking Speaker: for. Speaker: And that's it.

### 💡 実例・デモ

Speaker: Very simplified. Speaker: But because of modern hardware Speaker: and algorithm optimizations, you Speaker: can get really, really fast with Speaker: this. Speaker: Now let's start easy. Speaker: Let's see if we can grab a live stream using Python. Speaker: Yep.

### 🔧 技術的詳細

Speaker: Pretty easy. Speaker: Wasn't really that hard. Speaker: Next, let's use YOLO to see if Speaker: we can track the birds that come Speaker: on screen. Speaker: Honestly, pretty easy. Speaker: Maybe I'm just such an incredible programmer.

### 🎯 応用例

Speaker: Uh, or I just have, like, a Claude Max account. Speaker: But honestly, though, you can do Speaker: this with, like, such little Speaker: Python code. Speaker: You can go in the documentation and you're done. Speaker: That's just why I love it so much. Speaker: Now we're able to track the birds and do some sort of like Speaker: futuristic surveillance on them, which feels a bit creepy, but Speaker: I'll also set it to assign a random stock so that when the Speaker: bird is on screen, it can see you can see it with it.

### 💭 考察

Speaker: And again, this library is just such a piece of cake because Speaker: honestly, kind of ridiculous. Speaker: One issue that we're running into though a lot is occlusions. Speaker: Sometimes a bird will either go behind this branch, another bird Speaker: will get in the way, or the detection will just not Speaker: recognize it for a second. Speaker: And when the bird is recognized again, it will think it's a Speaker: brand new bird. Speaker: Thinking let's buy a new stock.

### 📌 まとめ

Speaker: And these are fast, jittery animals. Speaker: They're unpredictable, but we Speaker: can make it so that if a similar Speaker: looking bird disappears and then Speaker: reappears in the general area of Speaker: pixels, we can reassign that Speaker: bird to the one that Speaker: disappeared. Speaker: Again, it's not like a perfect system, but it's just the one Speaker: that we have to deal with. Speaker: I'm also using something called Speaker: byte track instead of the Speaker: standard one that comes with Speaker: YOLO. Speaker: I found better results of the tracking algorithms with it, so Speaker: honestly pretty cool.

### ✅ 結論

Speaker: Now you know what would be really reckless? Speaker: To just kind of go live with it and just say YOLO. Speaker: So let's see how this performs on historical data. Speaker: And we can do this with Speaker: something called backtesting, Speaker: which I did in the last video I Speaker: did of this, and a lot of you Speaker: subscribed there. Speaker: There are a lot of libraries that do exactly this, but in Speaker: layman's terms, here's how we are going to do it.

### 📚 追加情報

Speaker: So I'm going to take an existing stream and grab about twelve Speaker: hours of it. Speaker: I will let the OCR process run and record every moment that a Speaker: bird is on, and then off with the corresponding stock it used. Speaker: We then get a list of all stocks that were grabbed in this Speaker: recording, and download the data for a specific day by seconds, Speaker: which is a lot of data. Speaker: We then map our data over top of it, and we run a simulation to Speaker: see how much money we would have made or most likely lost, and Speaker: see it on a graph. Speaker: First, we have to process a twelve hour video.

### 🔖 補足

Speaker: Yikes! Speaker: If only we had bigger hardware. Speaker: Which brings me to the sponsor of today's video modal. Speaker: Modal allows developers to Speaker: easily build apps on top of AI Speaker: infrastructure with programmable Speaker: infrastructure, elastic GPU Speaker: scaling, and unified Speaker: observability. Speaker: So for computer vision apps like Speaker: this, we need some powerful Speaker: hardware that can just run for Speaker: twelve hours straight, rather Speaker: than having to provision a Speaker: server and building a whole dev Speaker: environment, I can actually just Speaker: add a decorator here in Python, Speaker: and automatically we use a GPU Speaker: in the cloud to complete Speaker: whatever task we want, whether Speaker: that is, you know, something Speaker: stupid like this or using large Speaker: language models.

### 🎨 セクション 13

Speaker: But I can free up some space and instead use parallel processing Speaker: to get the job done faster. Speaker: There are a ton of examples you Speaker: can just play around with, like Speaker: using Lama cpp to do some Speaker: inference. Speaker: Flux context, fine tune, a large language model for a different Speaker: use case, and a lot more. Speaker: I mean, you know what? Speaker: You can use a GPU with your folks locally.

### 🚀 セクション 14

Speaker: This would have taken me like ninety minutes, but doing it on Speaker: modal did it in about eight. Speaker: So thanks again to modal for allowing this reckless behavior Speaker: on my channel. Speaker: I don't know if I should thank you, um, or hate you. Speaker: I ran this result about three Speaker: times, so he would have some Speaker: actual random assortment and we Speaker: lost money. Speaker: We lost fifty bucks, which Speaker: honestly, not as bad as I Speaker: thought.

### ⚡ セクション 15

Speaker: Not good though. Speaker: Ninety five percent of our trades are under one minute. Speaker: We basically are only holding Speaker: for like three and a half Speaker: seconds. Speaker: It's just complete noise. Speaker: I even decided, hey, let's try Speaker: identifying the bird species to Speaker: see if maybe there's like some Speaker: sort of correlation between a Speaker: certain bird type and our Speaker: losses.

### 🌟 セクション 16

Speaker: Some pattern I could find. Speaker: But really, it's just a nothing burger. Speaker: I just wanted them to stay on screen for longer. Speaker: And it got to a point that no matter what correlations I did, Speaker: nothing was working. Speaker: Was I making a stupid decision?

### 🎬 セクション 17

Speaker: Is correlating how people buy Speaker: stocks with birds on the Speaker: livestream dumb? Speaker: I went into a depression for a couple of days. Speaker: Maybe this coding video thing is a fluke. Speaker: Should I just get fireship to buy my channel? Speaker: But then it hit me what moves randomly but within boundaries.

### 📋 セクション 18

Speaker: Fish. Speaker: Which is like what Michael Reeve did, is why he did that. Speaker: Why didn't I listen? Speaker: The one issue with these models off the bat is they can't detect Speaker: fish of any kind. Speaker: So I had to grab a data set Speaker: online and tried training it and Speaker: it worked.

### ⭐ セクション 19

Speaker: But when we track, it would intersect. Speaker: So what if we could segment? Speaker: So I found this new model called Speaker: YOLO that lets you put in a text Speaker: prompt and it will automatically Speaker: segment. Speaker: The tracker works much better and doesn't give us issues when Speaker: the fish intersect. Speaker: Let's build some tests.

### 📝 セクション 20

Speaker: And I ran the test and patterns started emerging. Speaker: Wait, we're making profit. Speaker: The fish know the game better Speaker: than we do, but they don't know Speaker: transaction cost. Speaker: Neither do I. Clearly.

### 💡 セクション 21

Speaker: So again, ninety nine percent of Speaker: fish are on screen for only 20s Speaker: or less. Speaker: This means that the transaction costs are eating us alive. Speaker: Basically, the only winner here is Interactive Brokers. Speaker: As it always is. Speaker: Another wave of depression hit me.

### 🔧 セクション 22

Speaker: Why can't I get these trays to work properly? Speaker: I almost gave up until I remembered. Speaker: What if the fish were together? Speaker: Individually, fish are random, but together, schools of fish Speaker: exhibit collective intelligence. Speaker: Organized chaos.

### 🎯 セクション 23

Speaker: The market works the same way. Speaker: Millions of random traders creating emergent order. Speaker: We can create a democracy system. Speaker: We split the sections into quadrants with random stocks. Speaker: Whatever one has the most fish.

### 💭 セクション 24

Speaker: That stock is bought with all ten thousand dollars. Speaker: Then the tank gets split in half. Speaker: The top half says we hold the bottom says we sell. Speaker: Again, this is looking a lot like Michael's video. Speaker: Damn it.

### 📌 セクション 25

Speaker: It was perfect. Speaker: I'd create a democracy that Speaker: allowed fish to extract maximum Speaker: shareholder value. Speaker: That would go directly into my pocket. Speaker: So I built the democracy system and washed the fish curiously. Speaker: Vote on each station.

### ✅ セクション 26

Speaker: I took a full day's worth of data and back. Speaker: Traded it over the last thirty days. Speaker: And the results shocked me. Speaker: Four hundred and forty six dollars profit. Speaker: That's a four percent profit.

### 📚 セクション 27

Speaker: Not only were the fish intelligent, they were catching Speaker: up to the S&P five hundred. Speaker: And just when I thought that Speaker: this was done, ten thousand Speaker: dollars just hit the bank Speaker: account. Speaker: One last thing, though. Speaker: The bridge. Speaker: We have modal running our tracking on a cloud GPU.

### 🔖 セクション 28

Speaker: We then create a standard interface for Interactive Speaker: Brokers so that our fish can talk to it. Speaker: Then we create a bridge which connects to a Reddis instance Speaker: that uses blocking pop to get the events as fast as possible. Speaker: This would be things like by Nvidia or sell Microsoft. Speaker: So I ran it through the paper trading side of it to make sure Speaker: that the integration worked. Speaker: And sadly it worked as expected.

### 🎨 セクション 29

Speaker: Meaning I have to now go live with this bad boy. Speaker: So we ran it for about three days, three and a half days Speaker: roughly, and we lost money. Speaker: A lot of money. Speaker: My wife is divorcing me and leaving tomorrow. Speaker: The top performers here, we have hymns, which is like a online Speaker: pharmacy, I think.

### 🚀 セクション 30

Speaker: But they were my best performer. Speaker: They went up to about, well, not even one percent better than Speaker: nothing, I guess. Speaker: Right. Speaker: And then Ark don't know who these people are. Speaker: Oh, it's an ETF managed by Cathie Wood's.

### ⚡ セクション 31

Speaker: Of course, an ETF. Speaker: I should have known. Speaker: Make sure you follow me on Twitter by the way then. Speaker: Lunar. Speaker: Tesla was a big one.

### 🌟 セクション 32

Speaker: Ignore the USD here. Speaker: Robinhood, Apple, Nvidia, unity, and even Reddit. Speaker: Thank you for the gold kind stranger. Speaker: Now the bottom performers. Speaker: Wow.

### 🎬 セクション 33

Speaker: Okay. Speaker: These like really, really hurt me. Speaker: And it's funny because the AMC one was on the first day and Speaker: that one just killed me. Speaker: Because if you look over the last five days, it's only two Speaker: dollars fourteen cents. Speaker: And so when you buy ten thousand dollars worth of that, you're Speaker: getting a lot of stocks.

### 📋 セクション 34

Speaker: We lost a lot of money there. Speaker: The fish were not not nice to me whatsoever. Speaker: But it's funny though because a I must have just chose a really Speaker: bad time to trade. Speaker: Over the last five days, the S&P Speaker: five hundred went down by almost Speaker: three percent. Speaker: So yeah, we went down by roughly twelve percent on the first day.

### ⭐ セクション 35

Speaker: We lost like seven point eight percent. Speaker: And that was basically all from AMC. Speaker: Then the next time it was Speaker: negative two point three Speaker: percent, with the last one being Speaker: negative two. Speaker: But hey, we we got up by zero point two on the last day. Speaker: But really that's just what you expect.

### 📝 セクション 36

Speaker: This is a complete gamble. Speaker: It was just pick a stock at random and hold for an Speaker: unspecified amount of time. Speaker: You didn't really need fish to Speaker: do that, but it was kind of cool Speaker: learning about some computer Speaker: vision technology. Speaker: You can obviously look at the Speaker: S&P five hundred and be like, oh Speaker: my God. Speaker: Technically speaking, on this day the compounded values of Speaker: Delta six would have shut up.

### 💡 セクション 37

Speaker: You're just gambling. Speaker: That's what this is. Speaker: It's just gambling. Speaker: So I encourage you to not do this. Speaker: You know, I have the privilege of being able to do this because Speaker: I'm a YouTuber and I get paid well to do it.

### 🔧 セクション 38

Speaker: If you want to know more behind the scenes, more in depth of the Speaker: code, and just more, consider becoming a channel member. Speaker: I also want to say sorry for not Speaker: posting the source code of the Speaker: last project. Speaker: I still have it somewhere, but Speaker: around the time the video blew Speaker: up, I got countless DMs saying Speaker: people were pretending to be me Speaker: and asking for money, and it Speaker: just wasn't a good look at the Speaker: time. Speaker: I'm still debating about Speaker: releasing it, but let me know Speaker: should I release this one as Speaker: well?

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2025年12月28日

</div>
