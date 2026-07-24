# 📺 ADHD対策で作った2台のロボットが連携して暴走した話

## 📋 動画情報

- **タイトル**: I Built Two Robots to Fix My ADHD. They Started Working Together.
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=ycG8pn9wUwI](https://www.youtube.com/watch?v=ycG8pn9wUwI)
- **動画ID**: ycG8pn9wUwI
- **公開日**: 2026年07月18日 00:30
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

ADHDで集中維持に悩む投稿者が、「通知では止まらない自分」に合わせて強制力の高い仕組みを2つ自作した動画です。  
1つはサボり検知時にSNSへ自動投稿するソフト、もう1つは25分ごとにノートPCを物理的に閉じるロボットで、どちらも言い訳を許さない設計になっています。  
誤検知の実例では、Sentryを使って許可リスト照合の不具合を特定・修正し、過激な自動化ほど監視と再発防止が重要だと示しています。  
AI活用や生産性改善に関心のある開発者にとって、「強制」の効果と副作用を具体例で学べる内容です。

## ⭐ 重要なポイント

- 生産性アプリが効かない前提で、「評判」と「物理」の2方向から行動を強制する仕組みを構築した。  
- サボり判定は「許可外ドメインに約4分滞在」や「約90秒放置」などの閾値で発火し、確認なしでSNS投稿する高リスク設計。  
- 実際の誤投稿はSentryで原因追跡し、許可リスト照合の大文字小文字ミスを修正。監視基盤の重要性が明確になった。  
- 物理ロボットはポモドーロ25分で動作し、サーボ試作から12Vソレノイド＋バネ構成へ改良して「止めにくさ」を実現。  
- 開発者向けの教訓は、罰ベースの自動化は短期的効果があっても心理的コストが高く、運用設計を誤ると逆効果になり得る点。

## 📖 詳細内容

### 🎬 導入

The thing about productivity apps is that they fundamentally respect your time. They don't do that. >> [music] >> So, as you know from me telling you a thousand times already, I have ADHD. I have tried every productivity system on Earth like a streak, a [music] gentle reminder, an app that grows a little tree while you focus, or maybe the timer that closes your apps after a while. [music] And they all fail for the same exact reason.

### 📋 背景・概要

An app can only ask so nicely. You can swipe a notification away. You can't swipe a solenoid away from slamming your laptop shut. So, I built two things that don't ask for your permission. One [music] punishes my laptop.

### ⭐ 主要ポイント

It ends my work session physically whether I'm ready or not. And the other punishes my reputation. If it catches me procrastinating, for example, well, it will post to my actual account in front of all of you exactly what I was doing instead of working and potentially even worse. So, one has a body and the other has a software with my password in it. And then I made the mistake of letting them talk to each other.

### 📝 詳細説明

So, we're going to build the software one first, of course. But that's the one that can actually ruin my life if I really wanted to. And I wanted to get out of the way while I was still brave. This one will live on my machine, on my laptop itself through software. The deal I made with myself is if I procrastinate during a work block, a script posts a pre-written confession to a real account.

### 💡 実例・デモ

These are extremely offensive things to say. Something that you wouldn't want, you know, posted and come back later. It's basically just one [music] script that's watching what I'm doing, which which window has the focus, how long I've been idle for, whether, you know, the research that I'm doing is quietly becoming YouTube or TikTok or something. Cross a threshold during a focus block and then 90 seconds idle or maybe like four minutes straight on a domain that isn't on the allow list, and [music] it just simply posts straight to the API, which again, that costs money, too. So, >> [music] >> no confirmation dialogue.

### 🔧 技術的詳細

That's the point, because it should always be in the back of my head. So, I wrote a couple things like, you know, [music] simple ones like, "Oh, I was supposed to be working. I've been watching drone videos for 45 minutes." But, [music] these are like, I mean, who gives it Who cares? Nobody looks at it. I went and grabbed the most offensive things I could find, pasted it in, and then used that essentially as my collateral.

### 🎯 応用例

So, the detector is simply just [music] guessing here. A false positive doesn't really throw a quiet error page that nobody sees. It just simply posts to everyone, and I find out from the replies. And so, I stopped guessing, thanks to today's sponsor, Sentry. A bug in normal software is an error page that nobody [music] sees.

### 💭 考察

A bug in this one, for example, is a post to everyone I know that [music] I did not mean to send, and can't take it back. This blast radius isn't a 500 error, it's basically, [music] you know, my reputation here. So, before the whole thing went anywhere near my real account, >> [music] >> I wired the whole stack into Sentry. Sentry caught the misfire with a full story attached, the stack trace, [music] and the breadcrumbs of everything that happened right before. The window matching check compared the active app against my allow list in the wrong case.

### 📌 まとめ

So, a documentation tab read as [music] an off-list domain. The idle timer rolled over, and the script queued to post. And since I'm already, you know, using coding [music] agents in my stack, I really enjoyed using Sentry. So, most AI tools help you write code, but Sentry [music] is kind of the opposite. It figures out why the code that you already wrote is broken.

### ✅ 結論

It read the error, it traced it back through the code base to the real root cause, and opened a [music] fix. Not the have you tried turning it off and on again, the actual line. And I haven't even built the dangerous hot yet, [music] because the plan was always to give the script a body to borrow a physical machine it could reach out and trigger. So, from here on, every decision that [music] this software makes gets logged, and if anything throws, for example, Sentry pages my actual phone before a single post or [music] anything else can fire. If you want to try Sentry and see it below, make sure you check out the link in the description.

### 📚 追加情報

I've been using Sentry for a very long time. Thank you to Sentry for sponsoring today's video. Now, if you don't know the Pomodoro technique, 25 minutes of focus, then a forced break. The problem is the word forced here because a timer goes off, you say one more minute, and suddenly it's like 1:00 a.m. and you're researching whether crows can hold grudges on one another.

### 🔖 補足

So, this robot makes the break non-negotiable. At 25 minutes exactly, an arm will come down and closes the laptop like a guillotine, but for productivity. First version was the simplest thing that I could possibly get work with this kind of mechanism. So, I have one servo body right here, has high torque in it, so that's really good, a 3D printed arm, and an ESP32 telling me [music] to swing down. So, nothing that's going to really do a [music] lot, but again, it sits up at a 120° angle, and I just send it one command and it'll just sweep down and push the lid shut.

### 🎨 セクション 13

[music] At least that's the hope. And so, after printing all of these parts and placing them in, it was surprisingly a lot of work in Fusion 360, but it works. It closes the laptop. It's also the least threatening machine I've ever built because [music] it comes down and, you know, it does it pretty good, but I can just like hold it and then it just stops. And so, that's not really a punishment here.

### 🚀 セクション 14

It's like a robot politely suggesting me that I've done [music] enough for today, you know, like the "All right, we're done." And you know, I respect it, but I would just ignore it instantly. As soon as I see it come down, I'm just holding it. And because a servo can't slam, not in like a traditional way, I guess, it can only push at whatever speed I program it to, and that slow push is easy to fight. I can hold the lid open with one finger, but the entire point is that the break is non-negotiable, and non-negotiable has to be felt in the room essentially. So, the servo version stays on the shelf as the safe prototype.

### ⚡ セクション 15

The real one is going to use physics, [music] aka springs. So, this mechanism is simple. The arm [music] sits lashed upright under a spring tension. A 12-V solenoid holds the latch. So, when the timer hits zero, the solenoid releases, the spring does the rest, [music] and the arm just comes down on the lid fast.

### 🌟 セクション 16

And now, before anyone, you know, asks the simple question, yes, I did the math on whether this would literally crush or destroy a MacBook if, you know, it [music] swung and hit. And so, that's why the spring choice matters, as well as adding a little padding [music] on the back. If it's too weak, it's just kind of like not funny, you know, I can still hold it. But too strong, it literally might split the whole thing in half. So, I bought a bunch of springs [music] and put a foam pad on the contact face, so it lands in a sweet spot.

### 🎬 セクション 17

And so, we have the servo version, and then we have our spring version. That one felt personal. So, I went full industrial guillotine on this design, basically. It looks like it's part of some sort of like industrial safety thing that's engineered to do a simple single dangerous job. There's an arm or a disarm button.

### 📋 セクション 18

I could maybe add an LED halo, because every dangerous machine deserves a big glowing button of some sort. The robot also runs on an ESP32. Connects to Wi-Fi [music] and then runs a 25-minute timer there, and it listens to a webhook, so other software can trigger it remotely, as well. [music] And now, you can see where this is going. The Shane script knows that webhook.

### ⭐ セクション 19

But before I wire them together on [music] purpose, they already introduced themselves. The first night the arm was on my desk, I woke up to the laptop closed and the arm down. >> [music] >> I mean, I I should have unplugged it. This is the only software that I've ever written with an incident [music] response plan, because it's the only software I've written that can humiliate me in public and physically shut me down, basically, in the same request. So, I start working with it for 1 day, with it both built, both wired together.

### 📝 セクション 20

Now, the first block, 25 minutes, heads down and a 25-minute slam break whether I wanted to or not. I basically resented this immediately, and that's how I kind of knew it worked because I was also kind of scared to use it. And then, I learned that the thing that nobody warns you about is the enforcer does not know what a video call is as well. So, that was a shock to both people. I had to email a real person trying to [music] explain what exactly happened was like a horror movie almost.

### 💡 セクション 21

I was literally kicked off by force. So, it did end up posting something, and then it closed the laptop on me while, you know, strangers watched. And the worst part [music] is that the system did nothing wrong. The detector was right. I was technically procrastinating.

### 🔧 セクション 22

The software worked exactly as designed, and that is somehow so much worse. Now, let's get a little serious for a second. Do punishments work exactly? [music] Well, I mean, yes, sort of, but, you know, there's tradeoffs. For one day, my breaks actually happened, and I was >> [music] >> too scared of my own desk to open a single thing I wasn't supposed to, which I'm pretty sure is not what the therapist means by, you know, intrinsic motivation.

### 🎯 セクション 23

One cold little script that knows its webhook and one dumb robot with a spring, zero intelligence in any of it. Everything that can actually hurt me lives in the software, and the worst thing that it does, it does by reaching out and pulling the robot's trigger. And it's also worth noting, too, is that do you get productive knowing that you are scared of the thing that might hurt you? Like, seriously, a lot of the ADHD productivity methods is attached to some sort of dangerous ideology that you should be punishing yourself, like, actually, in order [music] to do it. This is for entertainment here, but is the way that your brain works worthy of some sort of punishment?

### 💭 セクション 24

So, do I have a problem here with, you know, is this a me problem? Well, you let me know in the comments. And [music] if you want me to build some more of these type of robots, let me know, and I'd love to do it.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月21日

</div>
