# 📺 I Built My First AI Robot

## 📋 動画情報

- **タイトル**: I Built My First AI Robot
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=Sf-nklw0ljQ](https://www.youtube.com/watch?v=Sf-nklw0ljQ)
- **動画ID**: Sf-nklw0ljQ
- **公開日**: 2026年07月03日 00:00
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

I built a robot from scratch. >> I can see Lewis and move my head. >> It's intelligent. >> What's that thing you're holding, Louis? >> And I'm going to show you from beginning to end how I built it.

### 📋 背景・概要

Starting with the brain, which is right here, the Jetson or Nano Super. 67 trillion operations per second, 1.7 GHz CPU. It's honestly perfect for its size. And plugged in. To start off, I have this simple USB speaker.

### ⭐ 主要ポイント

It's a little tiny speaker right here. I have a little USB lavalier microphone right here, so I could talk to it. And I also have a camera plugged into it, uh, which is not here right now. My robust behaviors I'm building with Mistral Vibe. For the voice, I'm using Mistral Voxil.

### 📝 詳細説明

So, the Mistral model that we're using generates the text and then this turns it into the audio in real time. And then that way I can also adjust how fast it talks, the specific emotion that maybe I wanted to lean on. And so I'm going to put a system prompt in right here just saying you're curious about the world. Your goal is to pick up trash, but you currently don't know how you can do that. If you're being built and are keeping Louis and the audience company, I'm including you guys.

### 💡 実例・デモ

Hey, how's it going? >> Trying to figure out my trash picking arms right now. And where do you think this is going to go from here? >> Hopefully. I'll be picking up trash soon somehow.

### 🔧 技術的詳細

>> Okay. And am I the person to do it? >> You're helping Louis build me, so probably. Yeah. >> Well, there you go.

### 🎯 応用例

How should you move? >> Pants or claws would be really helpful. Tank dress could work really well, too. >> Okay, well, let's get started. Let's build my trash picking body now.

### 💭 考察

>> It sounds like it's trying to learn English. So, I got this preassembled tank chassis right here. It literally works fine. It works great, actually. Uh, it came with a lithium battery and one of these little microcontrollers that is used to work with the motors inside of it, which we will be able to control ourselves.

### 📌 まとめ

And the reason I got this was because it's shock absorbent. If it runs over something, it's not going to fall over. If it just alternates between these two treads, then it's going to completely turn left or right. And that just makes it easy for this robot to be able to go wherever it wants. Okay, I got the tank chassis now for you.

### ✅ 結論

Wait, does that mean I'll have wheels or tracks, Louis? Yes. >> How will I actually move around? >> Treads. >> Treads.

### 📚 追加情報

That's like a real tank. Will they be big and rubbery, Louis? >> I'm not liking where this is going. I'm asking Vive to write the ESP32 firmware that controls the motors. So, this tells it which GPIO pins drive the chassis, the directions, and it generates the whole control loop.

### 🔖 補足

So, let's flash it to the chip. And now the tank actually listens. So, simply having a brain doesn't make something intelligent. You know, you're looking at right now. What makes it intelligent is the ability for it to reason across different multi-step tools.

### 🎨 セクション 13

And we've already obviously seen this with agentic workflows that is so popular today amongst basically every AI application. A cause and effect, a feedback loop. Move to the right, please. I think I just drifted right. Did I bust into anything?

### 🚀 セクション 14

>> Move left. >> I think I slid back left. >> Move forward. >> I think I rolled forward. Did something shift?

### ⚡ セクション 15

What do you sense ahead? >> I just realized you can't see anything, can you? >> Yeah, I'm kind of blind to it. Did I actually move forward? Right now, this doesn't really have any feedback loop.

### 🌟 セクション 16

If it runs into a wall, well, it's not going to know that, and it'll just continue doing that. There's no thought process behind the robot whatsoever. What can you see right now? >> Ooh, a face. Hi there.

### 🎬 セクション 17

Is that you, Louis? Everything looks so bright. >> Based off of what you're looking at right now, which way should you go? >> Whoa. Hi again.

### 📋 セクション 18

I think I backed up a little. >> I'm new to electronics, so I don't want to overwhelm myself here with the code as well. So, I just tell it what the robot should do. It's their coding agent. It lives in my terminal.

### ⭐ セクション 19

It knows the robot's codebase and takes instructions in plain English. When you see trash, drive over and open it. But the part I actually care a lot about is that it can run local models. So on the Jetson or in Nano Super, I can run quantized models on it locally. So it's completely private.

### 📝 セクション 20

So even if I don't have an internet connection, it'll still run. That way it can still steer all around my office. Nothing has to leave the room. You can try it out for free in the link below. Thanks again to Mr.

### 💡 セクション 21

AI for sponsoring today's video. Now, I could have stopped here. I had a brain, a camera, and a literal tank that drives itself around, and it worked. But the issue is that it just looked like a science fair project. And I think it deserved better if it wanted to look like an actual robot.

### 🔧 セクション 22

Now, I'm not a cat person. I've gotten better over the years because, you know, I've done the RC car project, the Cyber Deck, but this is the biggest thing I've designed, and it has actual moving parts. The body is simple. It's just a shell over the chassis, which thankfully I was able to find online. And on the chest, a lid on a hinge.

### 🎯 セクション 23

The lid will open with a servo, a motor that moves to an exact position that you tell it to. A normal motor will just spin continuously, like a wheel for example. But a servo goes where it's told, where it's told, never why. For the head, just two displays, one for each eye. The camera will sit right between them, so when he looks at you, he's actually looking at you.

### 💭 セクション 24

And that was the robot. This is bop. Then the printers took over. Days of printing. And not everything worked the first time or even the second time to be honest.

### 📌 セクション 25

After that, it was just putting them all together. Wiring through channels. I designed three weeks ago and forgot about servos for the neck. Servos for the lid. the speaker in the chest.

### ✅ セクション 26

Somewhere along the lines, it started to actually come together and look like a robot. But all these moving parts required one thing, power. I was testing this by having it plugged in to the wall. And spoiler alert, it can't really move if it's plugged into the wall. Well, not far, at least.

### 📚 セクション 27

So, I decided to use a Vmount battery. And although it did add to the build, I 3D printed this custom Vmount plate and just super glued it to the back of Bop. And I think it really adds to the charm. It's also a little easy to put it on. This buck converter is what converts these high voltages to lower ones.

### 🔖 セクション 28

I think after putting everything on the chassis, I came into another problem, the wires. This made debugging BOP feel almost impossible. On the software side, I could just use something like Vibe to be able to just quickly get the answer to if there's a software issue, but a lot of the time it was physical and I would have to get down on the floor and do it. Otherwise, I would have to disassemble the whole thing. This drove me crazy.

### 🎨 セクション 29

So, there's holes all over Bob just trying to get around so that it's not completely visible on the outside. But even with that, it still came out with a lot of wires. So, I created a little skirt at the bottom that could hide it as much as it could. But even then, it still looked a little jank. But to be honest, I kind of like it like that.

### 🚀 セクション 30

I often see so many projects with very flush design robots that look really good, but to me, this is what a robot feels like. At least a build, wires everywhere, very fragile, but still kind of alive at the end of the day. Wow. I can see Lewis and move my head and I can turn around. Wow.

### ⚡ セクション 31

I see you, Louis. Now, let me navigate around the area. If there's one thing I learned about this project is that there's trade-offs everywhere. I started off with a very ambitious idea. I originally wanted to have like a mechanical arm at one point, but struggle to even get what seems like the basics.

### 🌟 セクション 32

And then one of the biggest lessons I learned was looking at the wiring. Usually with a lot of these projects, I'm fine with these wires going all over the place, but I'm usually not used to it. Having to go around and look like a robot. Modeling a whole robot and engineering it are two separate tasks that make combining them a very beautiful thing. I've experimented with little projects like this before, but starting from close to scratch at least has been tough.

### 🎬 セクション 33

But made me really appreciate what people are still doing to this day.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月03日

</div>
