# 📺 7日間ターミナルだけで生活してみた

## 📋 動画情報

- **タイトル**: I Only Used the Terminal for 7 Days Straight
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=udr6CLFERE4](https://www.youtube.com/watch?v=udr6CLFERE4)
- **動画ID**: udr6CLFERE4
- **公開日**: 2025年12月11日 01:35
- **再生回数**: 31,704 回
- **高評価数**: 1,508

## 💡 概要

現代のテクノロジーによる燃え尽き症候群から逃れるため、7日間コンピューターをターミナルのみに制限した実験的チャレンジです。HP Prodesk 600にUbuntu Serverをインストールし、i3ウィンドウマネージャー、Neovim、Neomuttなど、すべてCLI/TUIツールで作業環境を構築しました。最初は不便に感じましたが、自分好みにカスタマイズできる自由度の高さと、テキストベースの効率性に魅力を発見します。開発者がミニマリストな作業環境に興味を持つきっかけとなる、技術的にも哲学的にも深い内容です。

## ⭐ 重要なポイント

- **ミニマルなハードウェア**: 中古HP Prodesk（i3-8100T、16GB RAM、128GB SSD）にUbuntu Serverをインストールし、GUI完全排除の環境を構築
- **完全なTUI環境**: Firefox+Vimium（ブラウジング）、Neomutt（メール）、Neovim+LazyVim（エディタ/メモ）、TaskWarrior（タスク管理）、Discordo（Discord）など、すべてテキストベースのツールで完結
- **カスタマイズの自由度**: 設定ファイルを直接編集することで、自分だけの作業環境を作り上げる過程が、アイデンティティの表現となる
- **効率性とミニマリズム**: テキストUIは見た目の魅力を排除することで、純粋な実用性に集中でき、作業効率が向上する
- **哲学的な気づき**: 「与えられたOS」ではなく「自分で作り上げるOS」という体験を通じて、テクノロジーとの関係性を再考し、本当に必要なものを見極められるようになった

## 📖 詳細内容

### 🎬 導入

I've been staring at screens for 25 years. Why? So, I got rid of my computer and replaced it with only a terminal for 7 days. Chrome froze on my computer and crashed. When I reopened it and restored all my previous tabs, it was chaotic.

### 📋 背景・概要

things that were bookmarks. Amazon links for more peripherals. AI doomsday articles. Modern technology is starting to burn me out. I need to reset my brain.

### ⭐ 主要ポイント

So, why not strip a computer down to its absolute basics? Now, the terminal isn't super scary to me. I've deployed a ton of things using YUbuntu servers. However, that terminal is black and white. Here, I'll be using it for work and productivity as a daily driver.

### 📝 詳細説明

So, I kind of need a little bit more from it. And since it's just a terminal, I want to grab the lowest spec computer I could find. Of course, you could use something like a Raspberry Pi, but I went to my local scrap electronic store and grabbed one of these HP Prodesk 600 G4DMs. This has an i38100T at 3.10 GHz, 16 GB of DDR4 RAM, and a 128 GB hard drive. Now, they wouldn't tell me where specifically they got them from, but my guess is that they get them before they're tossed out from other companies in the area.

### 💡 実例・デモ

Now, we have the hardware. What about the software? Well, as you know, Linux is a rabbit hole. There are many distributions. The one you choose comes down to your use case or personal philosophy.

### 🔧 技術的詳細

But for me though, I'm just going to go with something that I'm used to. Yubuntu server. I'm not too bothered by the proprietary software that is installed, but understand why some people would. Now, let me know your thoughts in the comments. Anyway, let's boot up a USB.

### 🎯 応用例

Now when you install Windows, Mac or even a Linux distribution like Ubuntu, you are used to seeing a guey leading you through the process. But since we have the server version, we only get the TUI version of it. Now, if this is already intimidating to you, then bring a couple of pair of pants because this is not even the worst of it. This is where things start to settle in. Am I doing something silly by trying out something insane like text user interfaces?

### 💭 考察

How can I stimulate my brain enough by seeing only text? I felt like I was entering a brand new world filled with nothing I was familiar with. I couldn't just mess around for a week either. I actually have real things I had to work on. I'm feeling burnt out, but adding anything on to that would be devastating.

### 📌 まとめ

What world was I entering? And then we're in white text on a black background. It's funny how when we see no options in front of us, we feel stuck. But what if it's a million options? I feel even more stuck.

### ✅ 結論

Let's get something looking nice. I am first going to install Xorg, a display protocol that will let us expand how it will use this computer. Right now, Wayland is also a popular choice, but I want something I know will work. Xorg has been around for a long time. And yeah, that's just basically it.

### 📚 追加情報

After that, I'm going to use i3 as a tiling window manager. Think about how Windows you can drag a window to the left or right and it will position it in a way so that you can have two windows side by side. Well, i3 is that but using the Xorg display protocol. And this is when you start looking like a hacker. I'm going to use elacrity as the terminal emulator.

### 🔖 補足

And this is where things get funny. Emulator. Now, to put it simply, a terminal is quite literally a terminal machine like a VT100. It's a small computer that connected to a big computer where you would input something and received output back from the main frame computer back when people did actual work. But nowadays, every terminal we use is an emulator.

### 🎨 セクション 13

We realized that the interface of input and output was the most reliable and the easiest way to use a computer. Installation is easy. We just use these commands. But something we need to do is edit configuration files, which is where people either give up or fall in love. Yeah, it's not a UI with fun little buttons.

### 🚀 セクション 14

It's text. And sometimes it doesn't even come with a preset one. So, you have to do some reading here, folks. And before we even go into the configuration file, we start learning about ways we can automate things already. This long command right here is annoying to run every single time.

### ⚡ セクション 15

But don't worry, I will show you something later that will make this awesome. But here's what we installed. I3 elacrity roy, which is an app launcher similar to spotlight polyar. So we have a nice status bar. Cat pooin theme, which is just kind of like a vibe.

### 🌟 セクション 16

Pycom for fun little effects like shadows and blurs. Now, this is the cheat I was talking about with these config files. If you type out the command into your zshrc file, which yeah, I use that. I forgot to say, and do something like i3 config, you can automatically open it up, then do something similar with the remaining items. And it's at this point you feel like a hacker.

### 🎬 セクション 17

I looked like a hacker, but nothing was actually being done, though. That's when reality hit. What do I even do now? I work at my computer for like 12 hours a day. And while doing some work in the terminal looks cool for a bit, it strains your eyes fast.

### 📋 セクション 18

You've probably seen in my videos already that I use the BenQ screen bar and I've been doing it for years now. They light your desk and the back of your monitor without any glare on the screen itself. The Halo 2 is the newest version, and there's a few upgrades that actually matter to me. First is the auto detection. It knows when I've stepped away and turns off, which is perfect when you're the kind of person who forgets to turn things off and finds themselves still coding at like 11 p.m.

### ⭐ セクション 19

The controller is USBC now instead of battery powered. And the illumination radius is way wider than before. I've used this thing on my ultrawide, my OLED, and even the cheap monitor I'm using for this video. It works great on all of them. for a video about stripping everything down to just a terminal.

### 📝 セクション 20

It felt right to keep the one thing that actually makes those long sessions sustainable. Thank you, BenQ, for sponsoring today's video. We are bombarded by software no matter what industry you're in. But despite all of the options that we think we have to deal with, we basically use the same ones. Here are my categories I'm going to show today.

### 💡 セクション 21

web browsing, email, note takingaking, project management and to-do list, and messaging. We will get into the coding ones, but those are more obvious, while these would be more challenging. First, for web browsing, I just chose Firefox. I'm not crazy about Firefox, but to be honest, I'm also not crazy about web browsers either. For what I'm using this computer for, Firefox is more than enough.

### 🔧 セクション 22

But we do have one issue is that browsers and websites are almost always gooies. And if I don't have a mouse, how can I scroll? That's where the Vimeium plugin comes in handy. It lets you use the Vim keybindings to browse the web. Then when you want to click something, it will map keys on the screen where you'd be able to click.

### 🎯 セクション 23

Awesome. But apart from that, web browsing really isn't different. It just is web browsing. We all do this every single day. But next up is emails.

### 💭 セクション 24

I primarily use Gmail, but I hate using the Gmail website. I usually use some dedicated desktop application like superhuman. So, I'm going to get a dedicated email viewer. And the one I'm choosing is Neomut. Now, this is a good time to bring up Tuy's or text user interfaces, which is something we brought up before, and it's exactly what it sounds like, a user interface, but made up of text.

### 📌 セクション 25

What separates a TUI from a command line interface is that the TUEI acts as a replacement for a traditional guey, while a CLI mostly consists of input and output with command line arguments with maybe some input in between. And this actually makes it great to open up on separate windows so you can see from the side. But this almost made me give up. Neioma is a fantastic piece of software, but the amount of customization available is intimidating and made me think that maybe, just maybe, this was all a mistake. Am I doing all of this just for vanity?

### ✅ セクション 26

I I questioned everything. Neomat took a lot of time to set up, and I had to go online and basically copy some other guy's configuration file, which I'm finding is a very common procedure for a lot of these softwares. Email is something you really don't think twice about. It just kind of is a thing. We accept it.

### 📚 セクション 27

But when it's managed locally, there's a lot to optimize for. Like, how do you want to cache it? Different protocols, you name it. And I think overall after I got everything set up, I think I enjoyed using it. I'm not entirely sure to be honest because I find that the email experience has never been the best.

### 🔖 セクション 28

But I think if you were to stack everything up together, this is probably the best one because you can choose to open up an email in an external editor, which more on that later. It was easy to just get used to the feeling of going into a separate software and then watching them all connect. I think what I really love too about this whole entire text user interface is that it makes things not fun to look at, which is good in a weird way. These email clients all look the same basically. But there's a reason for that because this is just the most efficient way.

### 🎨 セクション 29

But when you put it in a text user interface on the command line, it becomes a lot faster to navigate things. Especially when you think, hey, where is this email or where is an attachment in a certain email? It becomes fast. Taking notes is a core aspect to using any computer. Sticky Notes, Notion, Obsidian.

### 🚀 セクション 30

These are all softwares with huge and massive dedicated fan base that will fight to the death about what is right and what is wrong. And at first, I tried to find a CLI tool that would connect to these existing tools. I found one for Obsidian called Bassalt, which is a TUI that has experimental editing and viewing of Obsidian Vaults. Now, Obsidian is an open- source, but it has the philosophy of just markdown so that you can bring your notes anywhere. So this made me think, what am I doing?

### ⚡ セクション 31

Why am I trying to close myself off in an ecosystem that doesn't even require it? So what could both write and read markdown the best? Well, the answer was obvious. Neoim. So I went down a deep and complex rabbit hole history lesson.

### 🌟 セクション 32

Vim is one of the most popular text editors ever, especially to developers. So when Neoim came out, it took that foundation and made it extensible via Lua, opening the floodgates for plug-in developers to expand its functionality however it seemed fit. And just like how the Obsidian folks think that they're being productive by showing their setup on Reddit, Neovim can take away from the productivity by indulging in this vast ecosystem. So to make it easy, I installed Lazy Vim, a preconfigured setup for Neovim. Almost like if you're trying to get VS Code, but as Neoim, this is important when I start doing some coding things.

### 🎬 セクション 33

In i3, I can set up a new workspace and plop this here so that when I need to go jot something down, I can quickly move over and start typing in Z mode. Now, I'm not a Vim expert. I know the basics to get me around, which is more than good enough for this use case of writing notes. I'll have another video about this soon, but text is all you need. This is what makes Obsidian so popular.

### 📋 セクション 34

But my favorite two features is linking and the daily notes. I like being able to hop into my day knowing what I can do as well as jot down things periodically and then have it translate over to the next day. And I think this is where I understood the popularity behind Neoim because not only is it so lightweight and easy to just do anything with the amount of customization allowed you to truly make it yours, which you could also say is popular with Obsidian or Notion. But with Neoam, it's completely open- source. Anything is accessible to you if you have some time, which a lot of these Linux people do.

### ⭐ セクション 35

Task management is something I feel religious about. I have a few ways I like to keep track of things. One is the inbox system where I quickly jot something down and then come back to it later. Two, it needs to be minimal. The good news is that the terminal is a perfect opportunity to hit both of these points.

### 📝 セクション 36

And that's when I found Task Warrior. It's a CLI tool that lets you quickly add tasks, tag them, set due dates, priorities, etc. Now, this is actually a very popular software and it's really easy to use, but there's something even better, a TUI. Task Warrior 2 takes a task warrior file that you have and creates a user interface. So, if I have to add this to the same workspace as my daily note, I can have a workspace dedicated to just managing my daily productivity goals.

### 💡 セクション 37

And what I liked about Task Warrior specifically is that no matter where I was, I was just able to quickly jot something down and then use the appropriate keywords to set priority, date, etc. I usually use to-doist, which kind of has this same way of using natural language processing to understand and parse it for you. And I really like that natural language processing aspect. So, I found this one package called Task Vanguard, which is written in Go, and it allows AI power suggestions and all that. It doesn't seem like it's maintained.

### 🔧 セクション 38

So, instead, I just decided to make it myself like anyone else would do. And speaking of AI, because we use it so often, AI chat. And that allows me to connect to any LLM service and just chat with it either through a command mode or through a ripple mode. And I think this is where things become so easy with the command line because you can just activate any function from any application anywhere. And this is where things like shell scripts and that just come so handy because you can start automating things with all the packages that are already installed.

### 🎯 セクション 39

Everything has a input and output, so it's easy to just be able to write everything. There are some other softwares I use randomly, but I didn't have a spot to put them. Someone built a TUI for Discord called Discordo. It basically turns your Discord account into what looks like an IRC channel. And from a development standpoint, it looks pretty active.

### 💭 セクション 40

And if I were a hardcore Discord user, I might have more to say about it, but it does the job for me, which is basic DMs and basic messaging and channels. For Slack, I wasn't able to find any two available. Of course, we have Firefox and most of these applications use web platforms anyway. I could just download the clients in their respective Electron installers, but that's kind of defeating the purpose of what this video was about in the first place. Now, I'm going to be honest, and I think most people agreed with me at some point.

### 📌 セクション 41

Lex people are a bit crazy. Why paralyze yourself with the choices? Why remove most easy UI trades? Why go through so much effort just to spend more time on simple things? But I think after doing this for 7 days, I got it.

### ✅ セクション 42

Every key combination, every customization, every software I chose to install and tweak was me telling my story. How often do you go on a subreddit for a software you like and see feature requests just to never be implemented? What if instead you just started working on that software yourself? This philosophy has completely immersed itself across all of the Linux and Unix ecosystems. Identity.

### 📚 セクション 43

And I'm not going to lie, at first this intimidated me. I didn't even think about how I could represent myself in an operating system. I've already embraced one through Windows or Mac OS. But the funny thing is that was given to me. In a way, exclusively using the terminal has made me hate using a computer.

### 🔖 セクション 44

But that's kind of like why I love it. The brutalist way the terminal is laid out. It forces you into utility only. Text is the only thing you need. And I think it's made me appreciate the things around me more that aren't tech.

### 🎨 セクション 45

I started this video wanting to detox from modern technology, but I ended up finding out what my relationship with technology actually is like. Now I'm primarily back on my Windows machine. I need video editing softwares to make this video, but it's changed the way I like to operate. And I try to keep guey applications to an absolute minimum. It does look intimidating, but stuff like Claw Code is great for doing this.

### 🚀 セクション 46

You just ask Claw to do it for you, and it will do it. If you like this video, subscribe for more and consider becoming a member to help support the channel further. Let me know what you'd like to see

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2025年12月24日

</div>
