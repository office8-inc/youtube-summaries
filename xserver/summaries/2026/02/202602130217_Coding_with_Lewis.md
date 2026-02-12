# 📺 This $50 AI Command Center Runs My Life

## 📋 動画情報

- **タイトル**: This $50 AI Command Center Runs My Life
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=Pq3205RoOsI](https://www.youtube.com/watch?v=Pq3205RoOsI)
- **動画ID**: Pq3205RoOsI
- **公開日**: 2026年02月13日 02:17
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

I built a dedicated AI command terminal for my desk messing. It's like a stream deck, but for AI agents, and it runs open claw. In this video, I'll show you how I came up with this concept, the insane hurdles along the way, and how I open source this for you to build one for yourself. So if you're out of the loop here or live under a rock open claw, it's completely free, completely open sourced. You host it yourself, connect it to your tools, and it becomes this always on AI assistant that can take actions on your behalf.

### 📋 背景・概要

It's also filled with a ton of delusional 10 00:00:45,90 --> 00:00:45,290 height. You know what I'm talking about? Think of those like annoying people you see on Twitter who have the AI slot posts. Talk about how we haven't even seen the true potential yet, or people will be out of a job real soon, like brother. The true potential you have as senior is a job opportunity, and that's because you have no skills to automate in the first place.

### ⭐ 主要ポイント

But underneath all the hype, open Claw actually does some useful things, which got me thinking, what if instead of chatting back and forth with it, like every single other app that you use, I had a queue of actions. Open Claw has this heartbeat functionality that periodically checks on things like scanning for urgent emails or flagging overdue tasks. It built up a list of things that need my attention, and I just work through them, kinda like a notification system. So what have I built? A command terminal, which of course requires hardware.

### 📝 詳細説明

Two screens, a large one that shows live feed of everything that is being worked on, emails being checked, tasked, created automations, et cetera. And then on the left, we'll put multi the open claw mascot, the Space Lobster, whatever it is, with a cyberpunk aesthetic. That one I just chose for myself. And then on the smaller screen, we have touchscreen buttons that are customizable that can show notifications as well as trigger quick actions, I don't know, like such as approve or deny and other quickies. And this will all set in some sort of aesthetically pleasing enclosure that will sit on your desk always available, ready for its next mission.

### 💡 実例・デモ

So here's what I ordered here. A Raspberry PI four. And yes, you could technically run open claw directly on the pie, but I don't trust myself to leave it on all day. And then it's also just not that powerful. A four inch LCD display, a 2.8 inch LCD touchscreen micro SD card, some push buttons and knobs, a double-sided PCB boards for the final build.

### 🔧 技術的詳細

Now, total damage, about 35 to 40 USD plus a 3D printer if you have one. But first, let's set up open claw. Now here's the thing about open claw. It's free, completely open source, but it needs to run somewhere, and that somewhere needs to be on 24 7. It's like a server.

### 🎯 応用例

If your power goes out, internet resets or mom picks up the phone, your email monitor is no longer monitoring, which, come on, it's kind of useless at that point. But there's also something else people don't talk about enough. Open Claw has access to your email, your calendar, your files. So if you're running that on your personal machine, all of that is exposed locally. One bad skill, one misconfiguration, you've got a problem here.

### 💭 考察

The smart move is to isolate it, run it on a VPS, where it's sandboxed away from your personal stuff, and that's where hosting comes in. Who is the sponsor of today's video? They actually have a dedicated open claw setup page. You can go to the link of the description and you pick a plan. I'm gonna be using the KVM two, which is more than enough, and it walks you through getting open claw running step by step, set it up with an SSH key, and in about two and a half minutes you have a full VPS with open claw ready to go.

### 📌 まとめ

It's isolated. It's always on, and your personal machine stays clean. So whether you're a gamer developer or just tinker like me hosting or gets you from zero to one in under two minutes, use code coding with Lewis for 10%. Off link is in the description. Thanks again to hoster for sponsoring today's video.

### ✅ 結論

So now that we have open claw, potentially inflicting danger in my digital life, let's put my physical life in danger too by working with electricity. Ugh, no. Let me tell you, I was humbled immediately. This was nuts. These displays were designed for Arduino and ESP 32 boards.

### 📚 追加情報

I had them working on a separate project I was working on, but getting these to work on a raspberry pie was an absolute nightmare. Maybe it's just skill issues, but that's why you're watching because you know I can't do this stuff. Look at these wires though. Okay. Like, oh my God, what the hell?

### 🔖 補足

Part of it as well has to be plugged into the breadboards and some share pins with the raspberry pie. The whole soldering process is going to be interesting, that's for sure, because I'm also not like a huge soldering type of dude. After we got them to work though, we finally were able to progress on having some sort of user interface. I was able to get the display on the large one to consistently work, and the second one too, which again, they actually surprisingly had two separate interfaces. Then I was able to touch things to make the first display change state.

### 🎨 セクション 13

This is the point where I started to see this actually becomes something, and not just a silly little well demo project with a bunch of wires everywhere. Then we have to pair the raspberry pie to our open claw on hosting her. Now, that's why I love to see data from open claw on the displays. I can even send data back using the buttons, but it looked awful. Text on a screen.

### 🚀 セクション 14

It looks like Windows 98. Uh, this thing needs some personality. Let's add a cool little mascot. I'll add the Space Lobster that they have, but we can have him on screen in cyberpunk style, left side of the screen dedicated to the character, and on the right we have the activity feed on things to look at. This would be like do the email checks, the Slack messages and more that I have to keep updated on.

### ⚡ セクション 15

Then this small touch screen will have the same look, be more minimal. In comparison, we will have six programmable buttons, things that we can customize with things like NAN or Python scripts. I also wanna add a price at the top right there to remind me that this technically isn't free. API costs are extremely high. This is my prompt to tell you that I need you to subscribe.

### 🌟 セクション 16

Since I spend too much time and money doing these things and my wife left me, this whole UX UI reminds me of a pit boy from Fallout or Ben Ten's watch. It's supposed to feel a bit underground almost as if you are allowed to be using this, or if I built it in my basement, which I did. Now, listen, there for sure is a vibe about having alligator clams holding up two displays with wires everywhere. I didn't say a good vibe, I just said it simply is a vibe. We need to get our Steve Jobs out here and start designing a product.

### 🎬 セクション 17

I fired up Fusion 360 and started designing an enclosure. I'm not too familiar with this software actually, and had to learn quickly, but I have some 3D experience, so it wasn't too hard to pick up a simple idea, a wedge that has cutouts to put the screens in. This required me to get out some calipers to get exact dimensions, which is harder than you think. Believe it or not. You could have a simple enclosure that is just a wedge, but we need to make this a little bit more cyberpunk feeling.

### 📋 セクション 18

If you look at popular media, it has these low poly looking edges with metal engravings. This is how I wanted to model mine, so I added these blocky bezels to go over the screens. This will hopefully also cover up any imperfections in the final print to add some texture. I found some circuit board vectors and made a cutout of it directly on the face plate. I think it really elevates it up a notch.

### ⭐ セクション 19

The case splits into two distinct pieces, the front part that we talked about already, and a back plate so that when I assemble, I can insert everything in. Since it's running the raspberry pie, I decided to add cutout holes for the main ports so I can debug later, and this is what it will look like. I honestly think it looks great. It's not perfect, but I'm not really aiming for that. Now it's time to print.

### 📝 セクション 20

I use PLA mat for basically everything. However, I decided to try out this translucent Pet G as the little bevels to add some color. I think the light shining through, it could add some extra flare to it. I don't know about you, but I'm not really crazy about the 3D printed look. You know the ones where it's the visible lines throughout.

### 💡 セクション 21

It just kind of cheapens the look, especially if the cyberpunk look is what we're going for. So I went with some optional materials to make this look like brush metal. First, I gave the parts a quick sand to roughen up the edges a little bit. Sadly, a 3D printed artifact affected the roof of the case, but lucky for us, some scruffed bits adds a little bit of character. Then I hit it with a couple of coats of primer.

### 🔧 セクション 22

This will hide some of the layer lines and give it a coat of this metalish color. Now, on the face plate, especially, this really brings out the circuit board lines. Some of the primer didn't get into the lines, but honestly, that's what makes it look even better. Then we grab a much finer piece of sandpaper and smooth it all out, and with this aesthetic, things don't need to be perfect. After that, I have a metallic finish to give it a shine at the end of it, and honestly, the results are really awesome.

### 🎯 セクション 23

I will say that it's not completely perfect. Again, I'm not an experienced person here, but compared to an initial 3D print, it just looks 10 times better, and to make it much heavier, I glued together some metal washers and place them in there to add a little bit more weight. Just giving it that premium feel. Quickly though, before we assemble, I need to solder together the shared GPIO pin on the breadboard. The circuit goes through a row, which means that I can share pins, but I have to now solder this onto a board so I don't bring the breadboard into the device itself, and so here's me doing that, but a very crappy job.

### 💭 セクション 24

Feel free to leave a roast in the comments. It doesn't hurt me anymore. Well, I don't know. Maybe the moment of truth screens go in the back. Then I secure it with some M two screws.

### 📌 セクション 25

Put the raspberry pie at the bottom, then pop the rotary encoder at the top. Cable management is an absolute nightmare, as you can see. It fits. It lines up great. I mean, it's not perfect, but the bevels, give us a little bit more wiggle room.

### ✅ セクション 26

Now let's fire it up. I have open claw running on hosting here for the last three or four days. Now, if I click on the inbox button, it automatically gets my inbox and shows me on the large display. Awesome. I also have a brief button here that gives me a summary of what I need to do for the day.

### 📚 セクション 27

Now, you can really customize it to your hardest content, add buttons, maybe icons, send it to a Python server that you have running. It's not just a little device though that you have to interact with. It silently built up a catalog for you to review after a certain amount of time, especially when you're coming back to something, your phone is a huge distraction enough. So this is something that genuinely tries to help you with things. One of the big appeals of Open Claw was like, okay, you can put it on what side.

### 🔖 セクション 28

You can put it on Discord, you can put it on, you know, WeChat or whatever, but those are also places that you would be distracted by. So this no one's using. Well, sadly, I genuinely think that dedicated hardware for AI agents is an unexplored space. Of course, they're trying to throw it in everywhere, right? But I think when you just build something of your own, you just truly know how it works, and it's just a lot of fun along the way.

### 🎨 セクション 29

We are seeing incredible things like Claw Code dominate the whole entire space of AI agents, but we haven't really been able to see it in real life outside of our computer. So I made this for like 40, $50 worth of part. If you wanna build it yourself, I have made everything open source, including the 3D print that I use, the software that I built, and instructions on assembly, if that's something that you're interested in as well, check it out in the link below, and if you end up building one, send a picture in our Discord where we have 10,000 plus developers just talking. Liking, subscribe. If you want to see more of these hardware projects.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年02月13日

</div>
