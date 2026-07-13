# 📺 Claudeに運営させるコーヒーショップを開いてみた

## 📋 動画情報

- **タイトル**: I Opened a Coffee Shop Run by Claude
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=R7bC46BUEok](https://www.youtube.com/watch?v=R7bC46BUEok)
- **動画ID**: R7bC46BUEok
- **公開日**: 2026年07月14日 00:15
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、Claudeを中核に据えて「実店舗のコーヒー提供」をロボットで実現する挑戦を追ったプロジェクト記録です。  
ロボットアーム、ポンプ、搬送機構、センサーを組み合わせ、注文から受け渡しまでを自動化する工程が紹介されます。  
技術的な成功だけでなく、現場運用では故障や調整が頻発する現実も共有され、開発の学びが具体的です。  
ハードウェア×AIエージェント開発に関心があるエンジニアや、プロトタイプを公開検証したいクリエイターに有益な内容です。

## ⭐ 重要なポイント

- コーヒー提供の自動化は、ロボットアーム単体ではなく「搬送・抽出・注入・制御」の全体設計が鍵。  
- 高価な機材（大型アームや周辺装置）を含めても、実運用では細かな故障対策と手動バックアップが必要になる。  
- Claudeのエージェント実行で、ポンプ制御や姿勢制御などを並列で実装し、開発速度を大きく上げている。  
- 最終的な価値は“完璧な一杯”だけでなく、来店者の体験設計とストーリーづくりにあると示している。  

## 📖 詳細内容

### 🎬 導入

I made yours a little sweet on the house. >> I used to make coffee for a living. I always told myself that the job wasn't about the coffee, it was about the people. >> Lewis, I think it's time for another incredible adventure. So, I built a machine to find out if I was lying.

### 📋 背景・概要

I used to work at a Starbucks like 10 years ago. The hardest part for me is multitasking. Making a combination of hard drinks while also trying to talk to the customers at the same time. Well, my brain isn't wired for this. But I thought if we take the same brain over here and let it control a bunch of different coffee shop parts, well, could it do it on its own?

### ⭐ 主要ポイント

My idea was that the cup would go on a simple conveyor belt and stop at intervals where Claw can dispense different items like coffee, syrups, and different dairy options. While I was sketching out this idea, well, one issue came up. Where does the coffee cup even come from? Like, not philosophically, but how can the cup go on the conveyor belt to begin with? Well, the only way I could think is my actual arm putting it there.

### 📝 詳細説明

But what if we can give Claude an arm? After a quick look on Amazon, everything was targeted towards a beginner learner, which ironically was me, but couldn't really pick anything up with a decent amount of weight to it, like a coffee cup with liquid. And I'm already looking at like a,000 bucks here for a small arm. And when I asked Claw to look for one that matches my specs, well, he gave me this one called the XARM 7. It's about 3 or 4 feet tall and could hold up to 8 lb with precise movements.

### 💡 実例・デモ

One issue, though, $15,000 and then $3,000 for a gripper. So, that's out of the equation. Back to the drawing board. Well, I guess now I have to commit to the bit. So, here it is.

### 🔧 技術的詳細

The big arm we were talking about. In the box is the big arm itself, already assembled, which thank God for that. Then, we have a mount to attach it to any surface of our choosing. But what really freaks me out is this big ass box that powers the entire thing. There's an emergency stop button on it.

### 🎯 応用例

Big red button. The first thing to do is to test this puppy out. Now, downloading the software, you can see it comes with some Python scripts to demo it out. >> Wow. Do you think I could control that thing?

### 💭 考察

>> Let's hook this up into clock code, I guess. I opened it up in my terminal and set it to Opus 4.8 with high thinking mode. I told it that it has an XARM 7 attachment and to test out a bunch of positions. The first position it chose was unexpected. This is when I realized I have already built something similar with the RC car.

### 📌 まとめ

I'm adding a depth sensor camera on its arm so it can track where it is and how far things are. I had to 3D print a mount for this. This mixed with the existing journey grid method that I did before gives Claude an easy way to loop through what it needs to do. >> Do you think I could dance in this? >> We need to do a coffee test.

### ✅ 結論

Great. It can pick up a coffee cup. And picking up the coffee cup was never the hard part. But what about all of this other stuff I have? Let's take a cup of coffee for one second.

### 📚 追加情報

A robot arm is obviously very cool, but it's not the hardest part of this operation, which is honestly surprising. A coffee shop is like nine machines, and we have to make them agree with each other somehow. Well, first pumps. getting the liquid from point A to point B in a decent manner. Milk, oat milk, syrups, cold brew.

### 🔖 補足

I got nine of them, each with a tiny brain with its own job. Sensors clearly would work perfectly in this scenario because I have to kind of do timings on what the right amount is for each type of ingredient. Otherwise, you get a vanilla syrup latte with a splash of milk. I need a lab coat for this. Oh, and speaking of lattes, you kind of need a special ingredient for a latte, right?

### 🎨 セクション 13

Yeah. Uh, espresso. But most espresso machines aren't exposing themselves to you. Sorry. Sorry.

### 🚀 セクション 14

By that I mean exposing their python, too. Yeah, that just sounded even worse. But something that does exist is a servo. A servo basically rotates a small motor to a specific angle. So, we can do something simple and wire this up to activate when we want.

### ⚡ セクション 15

And just like that, a simple espresso machine with an exposed Python back end. This metaphor is just not resolving itself, is it? >> I'm afraid not. Louis, >> how are you hearing this? >> Since there are going to be lots of different pumps, having them all kind of lined up risks crosscontamination, so we would need separate stations that can be triggered.

### 🌟 セクション 16

Having a robot arm wait for all of these steps is kind of counterproductive. As an expirista, we were supposed to work on two drinks at once, never more, and never less, ideally. So having the robot arm just chill there waiting for things is not really a good use of his time. It could be going out for a smoke break. So the conveyor belt works here as a way to transport everything to the final drop off point.

### 🎬 セクション 17

Then the arm can say thank you and drop your coffee off. Awesome. This just sounds like a Daniel plan, but uh software, right? Uh how do I make that stuff again? >> Ultra code Lewis.

### 📋 セクション 18

Let's open up cloud code quickly and basically take what I said for the last 2 minutes and ask it to come up with a plan on how it's going to implement this. Perfect. We got a plan back. It's long and we could leave cloud code to do this for like 48 hours if we want, but we want to use ultra code mode here. Ultra code spins up a bunch of sub aents that each grab one piece.

### ⭐ セクション 19

One writes the pump driver, one wires up the conveyor logic, one builds the pose recorder all at the same time until the whole thing's done, saving me a lot of time, which I don't have much of right now. Okay, another coffee break. Now, let's test all this out. So, we have our Raspberry Pi set up and I have this little web app that can do things like activate our pumps, activate the servos, activate the conveyor belt, but best of all, we can program poses with this big arm. The arm can go into manual mode, which makes the arm go limp and let you physically move it to a position you wanted to, while it automatically records the coordinates of all seven of these moving parts.

### 📝 セクション 20

This is the key here because I attached an infrared camera to Claw to see if it could move on its own accord. But instead, I think we're going to have Claw decide which pose it has to be in. So, I can put a pose here and then put a pose at the top of the conveyor belt. And then when we ask it to go to that pose, we can Okay, so yeah, another issue. Clearly this happens because it works like key frame interpolation.

### 💡 セクション 21

We're setting key frames at two different spots and then the arm determines the path between them. In this case, that's a straight line, but most robotics do this instead. It determines what height is considered clear and goes to that position before then going down to that location. So, I programmed about 12 different positions it can go to with a line it has to hit before going to each. But what if we gave this instructions to Claude so he can agentically do it itself?

### 🔧 セクション 22

>> Do you think I'm smart enough to do that? >> We give Claude a query. It reasons and creates a step list it has to do to create that order. Then in parallel, it executes it one by one in a sequence. This adds a fun dynamic where you can get surprised by what it makes you >> on it.

### 🎯 セクション 23

Lewis, I think you'll love this. >> So, we had a pretty cool system, but I essentially made myself a really, really expensive coffee maker. A machine that works in my basement for me isn't really a test. The test is a stranger who wants a coffee and didn't sign up to be a science experiment. Something of this scale needs a coffee shop.

### 💭 セクション 24

So, my real estate agent, shout out to Mark, let me use a building in the heart of downtown to do this stupid video. It used to be a bar. Keyword used to here. I mean, look at it. It's not really giving a coffee robot vibe.

### 📌 セクション 25

really nothing some more impulsive spending can't fix though. But we also have another issue needing tackling that state-of-the-art AI agentic models can't ever do for me. Talk to health inspectors. Yeah, humans. I needed a license to do this because technically it's still me.

### ✅ セクション 26

I can't just point my finger at a robot arm and tell it to go to jail for poisoning someone. Wait, can I? >> So, it's like a coffee machine. >> Yeah, it's like uh it's like a regular cafe, I guess. Um, but it's a robot serving you.

### 📚 セクション 27

>> And after a long, long period, I finally got that license. So, it's a coffee shop for 2 days. Everything is going to be free or donate to charity. No cashier. There's no barista.

### 🔖 セクション 28

You walk in and you talk to it. It picks your drink and it makes your drink and the arm hands it to you. But before I got there, lots had to be done. First, the place didn't look like a coffee shop, so I had to do my best to at least make it look somewhat convincing. One of these things was just getting a big white curtain both ways so that I could just hide all the imperfections.

### 🎨 セクション 29

And although I didn't really like this old bar look, it was basically the best I was going to get. So, we just kind of had to roll with it. Nothing some plants can't really fix, can it? After spending days and days and days setting all this up, I'm finally ready. So, first we have the Raspberry Pi 5, which is the brain.

### 🚀 セクション 30

Everything that it powers reports to this one board. So, if it locks up, the whole shop stops mid order. Then, of course, we have the XARM. You know, don't need an explanation there. I had it memorize about 20 to 30 different positions so that when the customer orders, it knows which one to go to at each time.

### ⚡ セクション 31

I also built this, the ice augur, which is actually a repurposed fridge part. Ice is one of the ingredients that can't be really missed. It's the only solid that the machine handles, and it goes in first before a drop of liquid. But it turns out that this didn't end up working. So, I had to end up doing a ice station at the end.

### 🌟 セクション 32

I got a real espresso machine that thinks a finger press is pressing the screen, but it's not really a finger, of course. It's just a little servo that's connected with a copper pad and a live wire. I ended up sticking with about five or six pumps. Two of them are diaphragm pumps, which are kind of a more traditional pump that you might see where it shoots a solid amount of liquid out. This is great if you want like 200 ml in like 2 seconds.

### 🎬 セクション 33

But for the syrups, I have these ones right here, which are the high precision uh stepper motor liquid dozing pumps. And you can tell by how it dispenses here, but it kind of like just pumps slowly in small intervals. So, it's great for syrup, but when it's cold brew or milk, it takes a long time. And one of the best ways was building vertically. A lot of the times when you see these types of machines, they're kind of up in a vertical position to take up less space.

### 📋 セクション 34

And I felt like this is the best way of doing it. I already made the post online saying that I'll be open this day and I couldn't really bring it back. I was up almost all night and then by the time the day came by, I decided screw it. We open. >> Hey there.

### ⭐ セクション 35

What can I get started for you today? >> You guys back up. That's salt hot coffee, right? >> Oh, it's it's climbing on itself. >> Oh.

### 📝 セクション 36

Oh. >> Oh my god, dude. It is a SN. Overall, I probably served like 30 or 40 people. It only lasted for about 3 or 4 hours, so I was kind of happy with the results.

### 💡 セクション 37

Now, let's be honest, half the systems basically broke at least once, if not more. A robot arm is a gimmick. You can buy a machine right now that makes and pours a drink itself with no arm required. I didn't even need this. But something about a thing physically reaching out and handing you your coffee made it feel a little bit more personal than a machine just making it and dispensing, even if it was a little unnecessary.

### 🔧 セクション 38

The robot broke constantly. Sometimes Claude would misread people. The arm fumbled a cup on camera many times. But the thing is is that people laughed at the failures instead of getting annoyed by them. A few ordered a second drink just to see if it would work that time, but nobody came for a good cup of coffee.

### 🎯 セクション 39

I mean, nobody was even really coming for the robot. They were coming to watch a guy attempt something completely insane, and they stuck around to see if he'd pull it off. That's the whole thing there. 10 years ago, I told myself my old job was never about the coffee. It was about the people.

### 💭 セクション 40

And I thought that meant something about me. Reading the room, making someone's day, well, it turns out I had it backwards. It was never really about what I gave the people in front of me. It's about the people who show up for you when you're clearly out of your depth and decide to stay anyway. Now, Claw's the reason I could even attempt something this reckless, but it's not why the two days actually felt like something.

### 📌 セクション 41

It was never part of the machine. It was everyone who showed up and rude for me anyway, including you watching this video. And I think that's the part that I'll actually remember. Not that this worked, but that people didn't actually need it to.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月14日

</div>
