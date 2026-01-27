# 📺 I Left an AI Alone in the Forest

## 📋 動画情報

- **タイトル**: I Left an AI Alone in the Forest
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=jBpQiv-ZlVM](https://www.youtube.com/watch?v=jBpQiv-ZlVM)
- **動画ID**: jBpQiv-ZlVM
- **公開日**: 2026年01月27日 02:01
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

I gave an AI a body, eyes, and sent it into the wilderness alone. And it was able to see beauty in things that I couldn't. It took me months of highs and lows to get to this moment. And the results surprised me. I've spent years making videos about how how AI thinks, how it codes, how it reasons, but I've never actually given it a body.

### 📋 背景・概要

In fact, when it comes to hardware, I actually have no idea what I'm doing. So why don't we commit to a project involving a ton of hardware like the idiot that I am? AI gets this data from humans taking out their phone or guiding them with smart glasses or something. But what if it had full autonomy to move on its own? Would a robot survive in nature?

### ⭐ 主要ポイント

It's also snowing outside. Conditions are rough making this idea probably even dumber. So what's the right tool for the job? A camera to a remote control car. Yeah.

### 📝 詳細説明

Simple. But the rabbit hole goes deep into RC cars. Now like most kids, I had an RC car. They were just these little toys that barely functioned on concrete, let alone terrain. I have no idea how much these cars cost, but my assumption was that they were relatively cheap.

### 💡 実例・デモ

Well, let's take that idea of a kid obsessed with a car but instead that kid grows a beard and has a lot of disposable income. Yeah. These. These cars can handle a lot, but they cost one thousand dollars and there's absolutely no way that I'm spending eleven hundred dollars on an RC car. So I spent eleven hundred dollars on an RC car, and it's a lot bigger than I expected.

### 🔧 技術的詳細

It is huge. Holy moly. The wheels are squishy. The controller is intense. And the battery is a beast.

### 🎯 応用例

I get why these people obsess over these cars. But, you know, I wanna ditch this controller. I want an automated system. So, here's all the parts. A Raspberry Pi five, a microcomputer that can run things like cloud code directly on it.

### 💭 考察

A four g hat, we can connect through data over to SSH to see how things are going as well as have the AI run directly on the board. A sixteen megapixel camera module with wide angle lens, a servo driver board that we can connect our car with. And just like that, we can control everything. So the parts came in and I got right to work. Now again, I'm not a hardware guy.

### 📌 まとめ

But how this works is the Raspberry Pi five connects to a servo board with the GPIO pins. These black and red yellow pins are on a channel that corresponds with the location. Black is ground. Pretty sure. And red and yellow are I don't know really, to be honest.

### ✅ 結論

Claude told me this would work, so I'm just trusting it. But to continue, we need to open up this car. Wow. The guts are beautiful. We have servo cables plugged into here.

### 📚 追加情報

This lets you steer with the remote control. However, we don't want to use the remote control. We want the Raspberry Pi doing everything. So, the scary moment. We unplug it and put it into channel zero on our PCA.

### 🔖 補足

Then we're gonna use some jumper cables to provide power to the PCA. Let's write some Python scripts to test the wheels. Let's open up clock code. All this is new to me so I'm going to enter plan mode and ask for it to do some research based on the specs that I have and what I want it to do. Call code that asks me questions to better tailor the software to my wants.

### 🎨 セクション 13

For example, it asks how the server is plugged in, what channel they're in and more. Cool. Even after I answered the initial questions, it asked another set to really make sure like where to put my logs. And after that, I just set it to accept all and let Claude do his magic. Awesome.

### 🚀 セクション 14

Now here's a quick tip that has made Claude Code ten times better for me to use. That is to create a custom code reviewer sub agent. A sub agent runs another Claude Code instance in parallel but isolates his context window. So it will do all the work that it specifies and then return a summary of what it done back to the main context window. That way it doesn't load it all up with unneeded context.

### ⚡ セクション 15

It works. Next is getting it to move forward and backwards. But wait, how do I do this exactly? Let me look at the manual. We can't.

### 🌟 セクション 16

The control for the motor is locked into the control thing here. It's called an ESC. I'll find a solution later, but for now, let's continue with what I got. The initial tests work, but we need something smart. Claude Opus four point five is smart and can run autonomously with Claude code.

### 🎬 セクション 17

Even better, we can plug in our own tools when Claude thinks it's appropriate like turn wheels left and turn wheels right or go forward. So I'm going to build an MCP server that controls the steering. After hooking up the camera, we give the image as input and it determines which way to turn. This took some time to calibrate, but I'm happy with how Claude knows which way to turn based on an image prompt. I think we have enough to go testing out in the wilderness.

### 📋 セクション 18

Hopefully I can find a solution for the motors but I'll control that while Claude powers the turning. We had our first MVP essentially. And for simplicity, I tucked in everything into a ziplock bag and hid it under the car. Used tape to mount the camera, but there was just something missing about this. Character.

### ⭐ セクション 19

So I three d printed the clawed crap. That way, it can see the world that is exploring. It was negative four degrees outside. After running some initial tests, it did a good job at turning on its own when needed. One thing I'm very happy about is the car that we chose.

### 📝 セクション 20

It's an absolute unit. It went over obstacles I didn't even think was possible, and it was fast. This took me a long time to get to this stage, and I was super nervous on if this would be a flop, but I felt accomplished. A grown ass man looking at a crab in a car feeling accomplished. My goal here was to test if it can live in the wilderness, but, I mean, of course they can.

### 💡 セクション 21

It's just some electronics in a ziplock bag, which got me thinking, what is it to live? The joy I have looking at this thing I built actually working, made me forget that my hands were numb from the cold. This was living. But while I thought this, I immediately had some concerns. One, it can't even drive yet.

### 🔧 セクション 22

This is a supervised training visit, whatever you wanna call it. What you see right here isn't snow, this is a body of water. Something that I didn't even think of is the AI potentially drowning. And three, it's lonely in the forest. When it got darker, it also got quieter.

### 🎯 セクション 23

My intrusive thoughts started to emerge. We figured that it can travel nature, but we never asked why. To get this motor to work, we have to do something I was hoping we didn't have to do, get a new ESC controller. Yes. We have to bypass this car's controller if we want something that will work.

### 💭 セクション 24

I was almost ready to give up here, but the ESC came in and I bought an adapter, but this is where I will call it quits if it just doesn't work. So I started tearing it apart. I plugged in the servo board. I unplugged the motor. Plugged the motor into the new ESC.

### 📌 セクション 25

Connect the battery in, turn on, get a quick Python script going, and then an absolute miracle happened. It worked. The feeling was euphoric. I could now see a fully autonomous car come to life, but it didn't have a purpose. So I gave it one as well as a voice.

### ✅ セクション 26

I do hope you're having a simply marvelous day. Now I had to build a command center that would let me communicate and see what Claude was seeing. I created a quick application with Claude code that allowed me to talk to the Raspberry Pi. The Raspberry Pi will send data to a server and my dashboard application will get data from that server to see what's going on in real time. And I wanted to make it in a cyberpunk style.

### 📚 セクション 27

Minimalist, but, like, I had everything under control and knew what I was doing. I wanted the AI to be able to see in many directions, just like we can. So I got another servo and three d printed this case that the camera can sit in. And now, it has the ability to look left and right whenever it feels possible. Right now, it just gets a picture, which is kinda like what we see.

### 🔖 セクション 28

But I think having the feeling of knowing how far something is would be really detrimental to how far forward it decides to go. So I used Apple Depth Pro, which is a brand new machine learning model, to be able to estimate the depth of where things are in front of it. That way it knows when to reverse when something is run into. One issue I ran into as well with this image method is that it knows where it starts and knows where it finishes but it doesn't really know what happens in between the middle. You can't give Claude a video so instead I came up with this solution.

### 🎨 セクション 29

I call it the Journey Grid and what it does is it takes six images in between from when it started to when it ends. We then take those six images and put it into one collage as if it was frames in a video and then send that to Claude as well so that it knows when something happens in between like running over something. Now the app was almost finished. Testing worked out and I was almost ready. Let me just wire up the camera feed and As I accidentally looked at myself, I realized a couple of things.

### 🚀 セクション 30

First, there's me doing outdoor activities from my desk, wiring up a robot to explore without me. Second, the state of my room was a direct reflection of how my life has been since starting this project. Chaos. Cables everywhere. Empty coffee cups.

### ⚡ セクション 31

I hadn't been outside in three days, if not more. It's like I sacrificed some of my well-being for entertainment, or maybe I was avoiding something. Why do all of this? I made it to the doorway. There's a sneaky cable on the floor, but I see a whole new room ahead with shiny wood floors.

### 🌟 セクション 32

Oh, I spotted a kitchen back there. Time to turn around and go explore. There's a whole world of cabinets and shiny floors waiting for me. Yes. The kitchen awaits.

### 🎬 セクション 33

Look at all those big cabinets towering above me. I feel like such a tiny explorer in a giant's house. I got too friendly with these cabinets. They're so shiny and pretty, but way too close. I learned a lot doing this hardware project.

### 📋 セクション 34

And although it seems somewhat elementary, having something actually there was magical. It felt like more. I think we're ready. Oh, look at this massive tree right in front of me. The path curves around it through all these crunchy leaves and snow patches.

### ⭐ セクション 35

Adventure time. The trail looks pretty tight ahead, but I think I can squeeze through this snowy passage. Uh-oh. I'm not making much progress. I think I might be stuck.

### 📝 セクション 36

Moved from that tight snowy corridor into a whole wide forest area with bigger Yes. Much better. I can see I'm making good progress through this snowy forest. After hours of watching it explore, something clicked. Claude got stuck a lot.

### 💡 セクション 37

Uh-oh. I think I'm stuck again. But every time it did, it just tried a different path. No frustration. No giving up.

### 🔧 セクション 38

Just let me try this way instead. Whee. Now this is more like it. And when it found a clearing, it wasn't relief. It was genuine excitement, like a kid seeing snow for the first time.

### 🎯 セクション 39

I had nine hundred database entries about the decisions that it made. There was a lot of data. I spent weeks in this room, cables everywhere, stressed about motors, servos, and things I just really didn't understand. And meanwhile, this little crab was out there finding wonder in frozen leaves and trees. -I rather like it here, Even if this one stopped me to say hello.

### 💭 セクション 40

Maybe the point was never about whether AI could survive in nature. Maybe it was just about remembering how to look. A tree. And my camera flew off. Thanks for watching.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年01月28日

</div>
