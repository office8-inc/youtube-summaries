# 📺 Eインク市場を支配する“独占”の実態

## 📋 動画情報

- **タイトル**: The E-Ink Monopoly
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=3QbJ7pnc1Lc](https://www.youtube.com/watch?v=3QbJ7pnc1Lc)
- **動画ID**: 3QbJ7pnc1Lc
- **公開日**: 2026年07月28日 23:30
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、安価な自作Eインクタブレットを作ろうとした体験から、Eインク部材の高価格と供給集中の背景を掘り下げています。  
発明特許の失効後も価格競争が進まない理由として、過去の企業買収、製造難易度、部材ライセンス構造が重なっている点を示します。  
特に、画面サイズが大きくなるほど歩留まりが悪化しやすく、結果として13インチ級や25インチ級が高価格に固定される実態が語られます。  
ハードウェア開発者やガジェット好きにとって、製品価格の裏側を「技術×産業構造」で理解できる学びの大きい内容です。

## ⭐ 重要なポイント

- 自作計画の初期見積もり（約200ドル）に対し、**Eインクパネル単体で約214ドル**とコストが大幅に上振れ。  
- 13インチ級は約400ドル、25インチ級は**1,800〜2,000ドル級**と、一般LCDより大幅に高価。  
- 1997年由来の主要特許は2017年に失効しているが、**買収による供給集中**で競争が限定的なまま。  
- ペン入力の中核技術（センサー層など）も個人調達が難しく、**「完成品を買うしかない」構造**が参入障壁になっている。

## 📖 詳細内容

### 🎬 導入

There's a tablet right here on my desk that costs $400, but it shows black text on a gray screen. It can't play video. It can't show a single color. It does one thing, and it does it at the speed of a single piece of paper. And so, I want to build my own.

### 📋 背景・概要

Now, I've made a self-driving RC car on this channel, as well as other [music] crazy things. So, I looked at this tablet and figured I had it number, a screen, a small computer like a Raspberry Pi or something, a battery, a shell that I could 3D print, and maybe two weekends, $200 maybe if I was careful. Well, that was like what, 3 weeks ago, and I had the price completely wrong. I even had the timeline wrong. But being wrong sent me somewhere I didn't expect.

### ⭐ 主要ポイント

One company in Taiwan, a patent that stopped meaning anything in 2017, and a list of every single competitor who walked up to this same wall that I did and simply gave up. So, the brain was pretty easy. I have a Raspberry Pi, a battery, a charge board, you know, some wiring. All this is cheap on Amazon and [music] it's all sitting in my drawer essentially. And the pen aspect was easy, too.

### 📝 詳細説明

But I'll come back to that because that turned [music] into its own problem. Then I went looking for the e- in screen, an e- in panel that's about 10 in wide. And I found one on Amazon by Wave Share. So, I put it in the cart. [music] $214 for the screen.

### 💡 実例・デモ

One part. And it basically ate up that whole budget on its own. I can't do the whole they wanted X, so I made it for Y. It didn't make sense. So, my first thought was [music] that I found the wrong one.

### 🔧 技術的詳細

Maybe it was just an overpriced niche, you know, maybe sold to a hobbyist at a markup. But this is where the whole rabbit hole just got started. Oh, >> so first I tried going bigger. If the screen was the expensive part, then maybe a larger one came at a much better price per inch. May you know the scaling laws here.

### 🎯 応用例

A 13-inch e- in monitor runs [music] for about $400 and up. A 25-in one, you know, the one that you'd put on your desk and use as like an actual desktop monitor, cost $1,800, and [music] some push past $2,000. And for reference, a 25-in LCD would probably cost [music] you like a couple hundred bucks on Amazon or something. So, the e- in version of the same size, [music] well, it just costs you a small car payment essentially. So, obviously [music] bigger was out.

### 💭 考察

I tried the other direction and looked for something maybe in between 13 and 19. So like, you know, 15 [music] or 16 in, but there isn't one. The whole market lives at 13 in and at 25 [music] with really nothing in between that gap. So then I gave up on buying a finished panel and just went for the real hacker move. Buy a bare screen, wire it to the Pi myself, and write the software myself or get Claude to do it.

### 📌 まとめ

But there's really no bare touch panel to buy. Well, not at this size at least. The little ones exist 3 in the size of the price tags that you maybe see at like a grocery store or something. But above that, the touch layer comes [music] welded inside somebody's finished product already and you buy the whole product [music] or basically nothing, which kind of defeats the purpose of the video itself. which then obviously brought me to the pen aspect.

### ✅ 結論

The thing that makes the remarkable too or like the scribe feel like a remarkable in the writing. The no lag, the ink that lands under the tip the instant you touch down. [music] I assume that that was some sort of like e ink doing something kind of clever or something, but it isn't the screen. There's actually a second layer underneath it, a grid of sensors made by Wake. And the pen has no battery because that grid powers it through the glass with a magnetic field.

### 📚 追加情報

[music] The screen is slow. The pen tracking is fast. The software paints the ink [music] the spot where the sensor already knows. And of course, you just can't buy that sensor anywhere. Wake licensed it to companies, not to people.

### 🔖 補足

So now, three different parts of my cheap little build that I was going to make an awesome YouTube video for had run into the same kind of wall. and I started to notice the shape of it. Every e ink screen that I look at on basically any product from every brand, so remarkable, Kindle, uh, Coobo books, it it came back to one place, one supplier, and that same name kept turning up under basically any direction I looked. I didn't want to know how to get the screen cheaper anymore. I wanted to know why one screen on basically every single device that already exists came from a single company and why that company would be able to decide it could charge whatever it wanted.

### 🎨 セクション 13

So the company is called E in based in Taiwan and if you've ever read on a Kindle then you've used their product before. You kind of exactly know what this looks like. the name got so attached to the thing it makes that people say e- in the way they say like Kleenex or something you know without knowing that that's the brand and not the product by revenue though e- in controls somewhere between 60 and 70% of the entire electronic paper market in the premium stuff the e-readers and the writing tablets their share climbs basically past 90 when analysis put it plainly the brand name is the product so my first guess here was patent You know, a company invents something, it locks it down under the idea for like 20 years or something and then charges what it likes until that lock expires. Ordinary boring stuff similar to like Ompic or something like that. And so I figured that E in held the patent on E in that that was the end of it.

### 🚀 セクション 14

You know, boohoo, you got to do what you got to do. And the patent is real. Three people filed it at MIT in 1997. Joseph Jacobson, Barrett Ksky, and JD Albert. basically these tiny capsules that are smaller than a hair is wide.

### ⚡ セクション 15

Each one holding white and black particles in a clear fluid. Run a charge across them and the particles move. The white comes up or the black comes up. That's the screen. That's just how a Kindle e-reader works, for example.

### 🌟 セクション 16

[music] But here's the thing, that patent expired [music] in March of 2017. So, yeah, like almost 10 years ago, the lock is gone. So anyone on earth can microenccapsulate elect whatever that thing is called they can make it now. No license, no permission. By the rules of how this is supposed to work, at least you know in this [music] capitalist society is that prices should have dropped because competitors should have flooded [music] in and my screen should only cost like $40 or something like that.

### 🎬 セクション 17

Well, [music] that's what I hoped at least. But of course, none of that happened. E in bigger now than it was when the patent died. You go everywhere and there's different e- [music] in display tablets. So, the patent was never really the thing that was holding things up.

### 📋 セクション 18

Something else [music] was. And I had to figure out what that was. So, let's go back to 2005. E In at that point is a small American company with a clever idea and not a lot of money. You know, we've all been there.

### ⭐ セクション 19

The clever idea has competition. Phillips, which you know, yeah, that Phillips has an electrofaretic display business. A company called Scypix has its own version using tiny cups [music] instead of capsules. A Korean firm, Hidis, makes these specialized glass back [music] planes that the screens need. And at this point, the field is crowded and the [music] patents won't last forever.

### 📝 セクション 20

So, a Taiwanese display [music] manufacturer called Prime View International watched basically all of this happen and made a decision. [music] Instead of waiting for the patent to expire and then fight on equal grounds these companies who were making own displays, they bought the companies instead. [music] They bought Philip's display business in 2005. They got a controlling stake in Hidis and his backplane factories in 2007 and 2008. But then in 2009, this is the big [music] one here, Prime View bought E in itself, the original American company, for a number that had climbed towards $450 million.

### 💡 セクション 21

They took the name Cypix and his cup technology followed a few years after that. And so eventually, by the time that the founding patent expired in 2017, there was literally no one left to compete really. Every company that could have built the screen freely was now just one company. Prime View, flying the E- in flag owned the original invention, the factories tuned to make it, the rival technologies, and the deals with Amazon and Sony and Coobo, all of the big players who use this technology in the field. The patent running out didn't open a door really at all because there was no longer anyone standing on the other side of it.

### 🔧 セクション 22

And so the monopoly isn't built on a patent, which makes this easy to solve, I guess, but it's built on a shopping spree. They spent the years the patent protected them buying up everyone who might use the idea after the protection basically ended. What makes this green interesting as well is that it's actually really hard to make. Hard in a way that has killed serious companies even before that patent started. The hardest step is filling those millions of microscopic capsules with fluid evenly across a sheet the size of a magazine without leaving, you know, gaps that wreck the picture and hole.

### 🎯 セクション 23

E- In's own patent actually describes that step as the one that ruins their yield more than any other. And so if you make that panel bigger, the defects will probably multiply, which is probably a reason why a 25-in screen doesn't scale up accordingly and cost $1,800. The failures [music] just pile up the faster that size grows. And trust me, other people have tried even recently. Samsung owned a different reflective screen technology called Liquid Vista and poured, [music] no pun intended, years into it.

### 💭 セクション 24

They then sold it to Amazon in 2013, but they shut it down in 2018 without ever shipping a known product with it. A company called Clearing spent a decade on a competing approach. The same booth, the same demo, a little better every year. a team that kept showing up to CES or one of these trade shows to genuinely believe that this was the year that they cracked it. But, you know, they never made it at scale clearly because we don't hear about them.

### 📌 セクション 25

And even Qualcomm had one. Xerox had one going back to the '7s. Pixel Q, Bridgestone, Plastic, Logic, every one of them either died or retreated to [music] some tiny corner of the market. So, you could argue here that E in isn't really, you know, the the villain twiddling his thumbs here. It's the last company standing in a business that genuinely might actually be hard that everyone else [music] just quit.

### ✅ セクション 26

They stuck with a screen that nobody else had, the stomach to keep on making essentially. And that maybe holds up until you look at how they treat the customers who have nowhere else to go. When Amazon launched the Kindle Scribe, which is kind of like the remarkable, [music] e- in confirmed that Amazon got exclusive use of that particular screen for a stretch period of time, Amazon, the company that bought Liquid Vista and try to build an alternative, ended up getting vendor locked to the one supplier on terms and supplier set. And so, Coobo, Remarkable Books, and all these other direct competitors in the e-reader business [music] buys from that same place. There really is no second source that they could compete with, no backup, no nothing.

### 📚 セクション 27

They're just the only thing in that assembly line. [music] And really, the money tells the truth about how comfortable that position is. In 2024, E Inc. posted a net profit margin near 28%. That is not a number of a company scraping by and doing razor thin margins here.

### 🔖 セクション 28

That's a number of a company that basically owns the only road that exists and charges everyone for the toll. So I came back to my build. I set out to make a $400 tablet for I don't know like a hundred or something. But I can't. The screen alone costs more than half of what the finished device costs in a store.

### 🎨 セクション 29

And the screen is the one part that [music] I can't talk down or, you know, bargain with. I can't scavenge cheaply or go really online to any store, even if it's from China. Amazon buys that screen by the hundreds of thousands and pays less than I can for a single one. I was never going to beat them on the part that matters because the part that matters comes from a company that sells to them and to me and decides what each of us pays for. And it wasn't just about the screen here.

### 🚀 セクション 30

Remember the pen that I was talking about? The thing that made it, you know, feel like writing? Well, that sensor grid is Waycoms and Waycoms licensed it to companies, not to people. Two different walls, two different companies and two different countries. And the same answer at both.

### ⚡ セクション 31

You buy the finished product or you basically get nothing, which is a whole separate discussion. Now, I [music] could have faked an entire ending to that previous video here. You know, I could have gotten a smaller display. Hey, I could have just tossed away the whole aspect [music] of getting a pen in there, but the honest answer is the more interesting one. I tried to beat something and couldn't.

### 🌟 セクション 32

[music] And now I know exactly why. And that why turned out to be a better story than maybe like a cheaper tablet that, you know, realistically a million people have already done at this point. [music] But there are a few cracks that are starting to show a bit here. A two-person open- source project called Modos got a standard e- in panel running at 75 times a second. Fast enough to feel almost like a normal display with hardware that anyone could copy.

### 🎬 セクション 33

And of course, there's a handful of Chinese factories that are making their own panels now. Slow and small for the moment, but you know, it's moving. It takes time for these things. And so, the screen on my desk here, it still costs $400. I know who decided that move.

### 📋 セクション 34

[music] And the next time that someone tells me a piece of technology is expensive because it's [music] just simply hard to make, well, I'm going to maybe ask a second question after that. Hard to make, yeah, sure. [music] But hard for who? And owned by who? Thanks for watching.

### ⭐ セクション 35

[music]

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月29日

</div>
