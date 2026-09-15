# 📺 I Overengineered a Cure for My ADHD

## 📋 動画情報

- **タイトル**: I Overengineered a Cure for My ADHD
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=abzbtEcxXSA](https://www.youtube.com/watch?v=abzbtEcxXSA)
- **動画ID**: abzbtEcxXSA
- **公開日**: 2026年09月16日 01:28
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

This is what living with ADHD looks like. But rather than trying to fix the issue, I thought I would do what all programmers do best, overengineer a solution. So instead, I wrote the software with Devon for a robot arm that scans my desk, figures [music] out what every object is, and files it into a bin on the wall. 40 hours of work to avoid 20 minutes of cleaning. This is how I overengineered a cure for my ADHD.

### 📋 背景・概要

>> [music] >> On this channel before, you've seen me cure my ADHD in many different ways. Whether that's customuilt laptop [music] cases or a receipt printer, but you know, even though they worked great, somehow it just it didn't cure the ADHD in me. [music] Who would have guessed? And those projects specifically were for working on the computer. But the trajectory of this channel has changed [music] a lot for the type of work I'm doing right now.

### ⭐ 主要ポイント

I'm constantly bouncing between different electronics projects such as a Pokedex or the laptop case that I already mentioned. And if you [music] haven't noticed before, all of these little electronic things are just these small little pieces that you constantly lose. Amazon is like my number one. I'm probably buying Jeff Bezos another yacht at this point with how much stuff I'm buying there. And naturally speaking, for anyone who has ADHD can [music] relate, what ends up happening is that you slowly build up a mess.

### 📝 詳細説明

And rather than incrementally just kind of clean up after yourself and do it one by one, what ends up happening is that you just have a gigantic mess that [music] you have to clean up that you have to set time aside for in order to do. And I don't have time or really patience or effort or even intelligence to be fair. And so [music] that's when this comes in. This right here is the XRM7. A couple of videos back, I built an entire coffee shop that was operated completely by this and [music] it was interesting to say the least.

### 💡 実例・デモ

Now, these arms are typically built for some sort of like enterprise use case. like you would make a test software on this using this arm, using maybe a miniature version of it to eventually deploy on the [music] way bigger versions that could carry probably like 50 to 100 lb or something like that. This thing [music] can carry about 8 to 10 lb. And of course, I got to show you how it works, right? Look at that.

### 🔧 技術的詳細

It's slow. Now, it's got to go real fast. [music] Watch this. Wa! That was fast.

### 🎯 応用例

That was crazy. So, like I said, it could hold about 8 lbs. It has seven different axis [music] that controls itself so that it can be as fluid as possible. Has this little gripper attachment at the end, [music] which is actually surprisingly one of the biggest features of this type of arm is that it has different grippers that you can use for [music] it. So, I have a little gripper right here that is just like a claw.

### 💭 考察

I have another one as well that's like a bio hand where it's like built to grab trays or something like that. Don't necessarily know the difference there. And then you could also get like a robot hand for it. It all uses the same connector that is on underneath here. But like I mean come on here, you know what you're watching.

### 📌 まとめ

The reason I enjoy this type of stuff is because it has its own SDKs that you can use, Python, whatever. [music] And I mean like you don't even necessarily have to care what kind of SDKs there are, just as long as it exists. And so obviously this made me curious, what can I use this for to solve the problem that I just mentioned, aka this? The one thing that AI agents have proven to me is that it doesn't necessarily matter how slow something goes [music] as long as it just does it right eventually. And we could probably apply that same sort of philosophy to a robot arm.

### ✅ 結論

The reason I don't clean is because it's a commitment. And [music] so if this robot arm is doing it for me, well, it takes it away from me. And so when I can just use this and it goes pretty slow, well, I can do something else and come back in like a couple of hours. [music] At least that's the thought. So, if I just constantly start putting things down on the desk, it can maybe just automatically sort it until there's basically nothing there.

### 📚 追加情報

Constantly applying that philosophy on each turn. And then that way it comes back basically completely sorted like in one of many bins based on some sort of certain category. But of course, the first thing that we need for this entire project is vision. And actually, that's where this little mount comes in. is for something called the Intel Real Sense camera.

### 🔖 補足

[music] And in plain English, it essentially is running off of two cameras that just gets everything, but then it also has an infrared light as well that captures the depth values in it. And this [music] would be able to judge something by a distance. So, you can see that it's able to like work like a normal webcam could. Not the best quality, but it's like it's a webcam here. But then also, it has another pass in it, too, that looks like this.

### 🎨 セクション 13

and it's like a bunch of crap, but basically it's highlighting things that are closer [music] or further. And of course, with a machine like the XRM 7 right here, being able to grab stuff is fairly [music] easy, I guess you could say, from like a vision model stance, but it's more so the depth, and you don't want to have to go 1 millm at a time. So, let's just hook this up. It comes with this UFACtory Studio software that you can use and Windows warned me that it was very very dangerous. And I guess in terms of complexity here, it's actually not bad of a software, but I don't really care to use it.

### 🚀 セクション 14

I want this to work automatically for me. So, it's time to lock in, get on the floor, and let's do this fast. Okay. So, I'm going to open this up with Devon, who is the sponsor of today's video. So, let's just run a coding agent here that will take this from beginning to end.

### ⚡ セクション 15

And just let me iterate over it uh as I go. Since I'm already focusing on a million things at once here, like [music] I got this arm, I got a bunch of other stuff, it's nice to be able to just hand this off [music] and just let it kind of go on its own. So, I'm going to be using their SWE 1.7 [music] model with lightning mode, which uh runs on Cerebras at 1,000 tokens per second. If you haven't used that before, well, [music] you're about to see what's up. All right, let's try it.

### 🌟 セクション 16

It's actually kind of like hilarious how fast it's going. [music] I don't even get like why they're even showing me the tool calls and everything because it's just I can't even read it. Like physically can't even read it. And one of the foot guns with working with coding agents specifically is not having that feedback loop. [music] And we're in a weird place here because we require vision.

### 🎬 セクション 17

And something [music] that the LLMs are not necessarily too good at is vision. I highly [music] recommend this based off of like any of the tools that you're writing here, like maybe as tests or um [music] I don't know, formatting or something like that. But I'll actually create a stop hook here so that every time the [music] agent kind of stops and figures out what uh it's doing next. Uh it has to take a picture with the depth [music] sense camera to kind of like understand where it is and see if it's working as expected. And again, it's a coding agent, so it's not a perfect solution here, but again, it's way better than just [music] kind of coming back hoping it works and then firing it off again.

### 📋 セクション 18

I don't want to do that whole like [music] management of a coding agent thing. Um you don't want to be wasting tokens here either. So, it's just a proof of concept. Let's see if it could even be done in the first place. And for the most part, almost everything is run locally on this Nvidia GPU that's on this laptop here.

### ⭐ セクション 19

But let me first explain to you how this works in detail. So, the basic way it works is this. It goes to the very top and looks down to see the whole desk. We use the Florence 2 model to detect what the object is. And then we use SAM 2.1 to actually segment them.

### 📝 セクション 20

And then we use the depth image [music] to lift each mask to a 3D position in the robot's frame. And this is where the calibration process really comes in handy here. I had to print out this here. One second. I'll show you.

### 💡 セクション 21

So I had to print off this little grid of things right here. [music] And the reason for that is that the robot is able to see where it is. And then it's able to use a lot of its xcoordinate uh positions to get the best idea of where that depth is. And you only have to do that like once. Uh or maybe again if you kind of like move it around a bit.

### 🔧 セクション 22

And so when we do that, it surprisingly works [music] pretty well. Now, let's go ahead and scan the robot to see. And so it's [music] able to segment. It looks like five different objects there. We'll see how it does.

### 🎯 セクション 23

You can see like there's like [music] small little purple kind of bits on there that kind of show you that it's a bit closer. [music] So, this is going to grab the yellow cup. Not bad. [music] Definitely you don't want to put your glass in there. And then it's going to grab a blue and black screwdriver.

### 💭 セクション 24

[music] Now, this is an interesting one because we have two things that are kind of close to each other. So, oh yeah. [music] So, it it stopped uh because it almost just completely [music] broke this arcade button that I have right here. Let's try that again. So, let's be real.

### 📌 セクション 25

That's one bug that needs to be fixed. [music] And so, now it's going to go to the screwdriver. Look at that. Okay. How?

### ✅ セクション 26

All right. Hold up. Hold up. Hold up. Okay.

### 📚 セクション 27

Thank god. As you can see here, it's able to grab things and just place them down into random spots. [music] We actually come into a couple of issues. This is not necessarily as clean as we wanted to. And then it just also rolls off.

### 🔖 セクション 28

When we let that happen, we have that infinite [music] glitch happen, the token burner with the vision model. So [music] maybe I found the true use case of ADHD here and that is a box. I printed about two or three of them. So let's add a new feature here. Okay, I'm going to make it so that I can click on a box and this will tell the arm that this is where they put things.

### 🎨 セクション 29

Then with the first scan, what I'm going to do is have AI detect what these categories should be based on all the objects that are roughly on the table so that when it picks something up, it knows which bin to put it down. Right now, my little example only has five different items on the table. Right. So, let's just set up a couple boxes here and see [music] how it sorts all these out. So, it's a different day.

### 🚀 セクション 30

I got a haircut, as you can see right here. So, some interesting things happened along the way here that I never really expected. One interesting thing that it messed up was [music] the gaffer tape right here, which makes sense maybe to the computer's brain because when you look at the tape from here to here, well, the gripper just can't grab [music] it. But the thing is is that we don't grab tape like this. We grab it like this.

### ⚡ セクション 31

We find the entry point. So, we need to find an intelligent way to be able to pick something up depending on the width of its opening. So, another good example would be a mug or maybe just another sort of coffee cup or something like that. I love the grill me skill by Matt PCO for this reason. Now, I know that this is possible just based off of the mathematics here, but it's also fairly complex.

### 🌟 セクション 32

So, I'm going to run this through to ask some questions and align [music] on what I need. And then I run the improve codebase architecture, which is also by Matt, so that it can question me on some of the architectural decisions. And that's the thing with coding with AI nowadays. It's a lot easier to write code, but it's a lot harder to validate it at the same time. So, after a bit of back and forth, here we go.

### 🎬 セクション 33

Thanks to the segmenting model, we now understand when we have a good grabbing spot to pick something up. So, it measures the two closest distances [music] between a edge where it segments. And here we are, a continuous stream of constantly picking up and organizing. But one issue is this constant setting up the boxes and then tearing down again. We need a better system here altogether.

### 📋 セクション 34

Right now, I think the arm does a really good job of putting the items that are on the table [music] and putting them in the bins by category, but we need to put them away. Now, we could attach another desk in between the arm if we wanted to. And then that way we have two large desks right next to each other, but of course that kind of just defeats the whole purpose. We're just moving the mess into a larger surface area, something I'm already doing basically right now. So, if you put this whole system up against the wall and then have the arm right next to the shelving unit, then it could pick up or put away bins on a shelf.

### ⭐ セクション 35

And this also takes advantage of one of the best things [music] about the XARM 7 specifically and mass the precision, not necessarily the speed, but the fact that it can do 0.1 mm of wiggle room is pretty impressive. And something that the 3D print enthusiasts just love is the IKEA Status board. Now, [music] you probably have one to be honest. If you go to IKEA, it's one of the only things that you pick up there. It's just a pegboard that is popular.

### 📝 セクション 36

And because of its popularity, people have 3D printed everything [music] for it. And because of all the designs that exist out there, it was easy for me to reference when I was building out my own. I didn't even have to get the calipers out or nothing. [music] And this is what I came up with here. So, it comes in two different parts.

### 💡 セクション 37

So, first I have the cassette, I like to call it, right here where it has like a little knob on it where it could just clamp onto. And then I also have this part which goes onto the IKEA Skyus board. And then it just goes in like this. Just hangs. And look at that.

### 🔧 セクション 38

Fits literally perfectly. And then it grabs it like this. And thanks again to Devon for sponsoring this video. Make sure to check them out in the link in the description to get these lightning fast inference speeds. [music]

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年09月16日

</div>
