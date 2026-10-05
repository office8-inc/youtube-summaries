# 📺 I Revisited My Project That Broke YouTube Shorts

## 📋 動画情報

- **タイトル**: I Revisited My Project That Broke YouTube Shorts
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=kORQK5NyXqo](https://www.youtube.com/watch?v=kORQK5NyXqo)
- **動画ID**: kORQK5NyXqo
- **公開日**: 2025年05月31日 01:51
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

Three years ago, I made one of the worst things that braced the Internet What's something people would need to stop romanticize '21 when my sister came from our dinner last night. And went viral. Open source automated brain rot. Today, I'm gonna look at the repository and see how it's doing as well as work on some new features. Let's go.

### 📋 背景・概要

Short form content is actually where I started everything, believe it or not. On TikTok, I would nonstop see these videos, for the most part, they were edited by an actual person. It followed the standard TikTok brain raw formula of reading the Reddit title, that's usually, you know, a question in an AI voice, and then read the questions all while having a jumping Minecraft background. And as I was scrolling, I was just thinking, that could probably be automated. So I built it, then I open sourced it, and then I made a video about it on TikTok, Instagram, and YouTube shorts.

### ⭐ 主要ポイント

And almost overnight, it went viral with 2,000,000 views on TikTok, 1,700,000 views on YouTube, and, I don't know about Instagram. I can't be bothered scrolling all the way. They need to fix that. When I made a Discord, it was swarmed with people just wondering how to use the Reddit bot. Make sure you join, by the way.

### 📝 詳細説明

Now the goal of this project was similar to all the projects I do on this channel. I wanted to inspire developers to build cool things even if it was, you know, unconventional. But the reception was definitely mixed. Okay. And understandably so.

### 💡 実例・デモ

Some people said that I created an even worse problem while others said it helped motivate them. So I decided to automate this process. I shat everywhere in my house last night. Was absolutely fucking Like, point taken. And almost three years later, it's still doing really well.

### 🔧 技術的詳細

Yeah. 7,000 stars, 2,000 forks, and a ton of contributors. In fact, the latest update was actually a couple weeks ago from or Jason Cameron, who's, you know, a long contributor of this Reddit bot, so shout out to that guy. What turned into a simple two to three file project has now turned into a huge project with a GUI, text to speech service, Docker, shell scripts, batch files, and a whole ton of things. Now let's clone it and see where we're at.

### 🎯 応用例

I wanna go through the whole project and act as if I'm new to this to maybe fix something if it's not working. A huge thing that this project went through was the transition from when Reddit decided to completely go haywire on their API. I have a video on that, by the way. So the project goes from the Reddit API to scraping using Playwright. I'm going to use Junie, who is the sponsor of today's video, to give me an understanding of what is in this repository at the moment.

### 💭 考察

Now the first thing I realized with this repository is that it takes a long time to just kind of, like, get it up and running. I ran into an issue where I was pretty far along the initialization process, and then something, like, aired out. And then I had to do the whole thing over again, which no. And for the most part, it's just the default settings anyway. So instead of this whole, like, onboarding flow, I think we should just skip this and have, like, a default profile that you can then edit at a later time if you're not happy with what it is.

### 📌 まとめ

That way, can get up and running almost instantly. All this state is handled in config dot toml. So if we just have a default there, then everything can just go as planned. And I think this fix is already just a huge improvement to the existing app already. But I realized one thing.

### ✅ 結論

It doesn't even work. Okay? Dammit. Remember when I talked about this switch to Playwright? Well, that's because the Reddit API went through a massive overhaul and there's a huge amount of drama with it.

### 📚 追加情報

Again, video talking all about it. Essentially, there's a constant war between the web scrapers and Reddit. Reddit is going to change how the HTML or JavaScript is rendered just so that it can throw off the web crawlers. I have a feeling that's what's happened here and why it's maybe not working as well as intended. I wanted to check to see if this was happening to anybody else.

### 🔖 補足

And when I looked at the GitHub issues, somebody did run into this issue, and it's actually open. But funny enough, somebody literally just said that this code is what worked for them, and it worked for me. They literally just pasted it. Not even, like, a pull request or nothing. So I asked them to put in a pull request so we can accept it.

### 🎨 セクション 13

I want to make sure that this person who did all the work is credited and can, like, you know, put it on their profile or something. So we'll wait. For getting into fairly large code bases like this, I highly recommend you check out Juni by JetBrains, who is the sponsor of today's video. Juni is a smart coding agent that creates an execution plan that executes on complex tasks in your code base. So for me, I want to be able to go into my repository and get the hang of things.

### 🚀 セクション 14

So I could ask Juni, or I could ask Juni to start up file for me to get started on a new feature. Whatever side of the spectrum you're on, whether you're a minimal AI user or a AI prompt engineer, there's something that Junie can do for you. I like that I'm able to see the execution plan happening in real time as well as the task being completed. I can also see the depth of what Junie thinks that should be changed without actually changing it first. This makes it easy for me to not to commit code if I don't want to.

### ⚡ セクション 15

I've been a huge fan of JetBrains IDEs for a very long time now, and being able to use AI in a productive way that doesn't feel too intrusive is honestly great. Thanks, JetBrains, for sponsoring today's video. You can check out Joonie in IntelliJ, PyCharm, WebStorm, Goland, PHPStorm, RubyMine, and RushRover. Link in the description. Something that hasn't been updated in a very long time is the dependencies of this project.

### 🌟 セクション 16

Since a lot of these requirements often rely on AI, the dependencies have changed somewhat dramatically. So I'm gonna ask Juni to see what critically needs updating. And one of these is Eleven Labs, which does the AI, text to voice and is probably one of the most popular packages in this repository. So definitely wanna update that. And not much needs to be refactored, but I do have to go into the code and just change up things a little bit so it follows the same procedures.

### 🎬 セクション 17

Now a really important package that this whole entire thing depends on, if not, like, you know, the rock in the middle of it, is MoviePie. The literal library meant to compile everything. It's currently on version one point zero point three, and currently, the latest version is two point one point three. It seems like they wanted to kind of unify everything, and they also just dropped support for Python 2.7, which, mean, like, honestly, props to you guys. That's that's a headache.

### 📋 セクション 18

Thankfully, the refactor isn't too bad at all. They had a migration guide, but it didn't seem like I had a lot of things in there that would affect me. Something I think would be really, really awesome with this that would take it to another level actually is if you updated the GUI. I think right now the GUI is great, but I think there's definitely ways we can improve on it. Something a lot of users complained about is that they had to use Python in order to run this, which, you know, I get it.

### ⭐ セクション 19

You know what I mean? Like, where's just the EXE file? I'm gonna create a simple UI that matches the vibe of the one that was already there. It needs to be noted that people who are working on this app are doing it for free and just out of the love of programming as well for the content. In no way should any code be deleted if unnecessary.

### 📝 セクション 20

That's the beauty of open source. Everyone gets to contribute their own version in some sort of way, so let's respect it. Something I want to do is similar to what we're doing already, but I kinda want to have a section where we can actually run the scripts. With PyWebView, we can actually embed this into WebView and have it run Python scripts for us. And one last thing, the read me is a little bit dated.

### 💡 セクション 21

This one is definitely gonna be one of the easier fixes, but definitely requires some technical understanding. I feel like we definitely need to update it so that it's easy for people to get started without having to read a bunch of gibberish. At the time, this repository was to accompany a video that came out, but now it's kind of taking a life of its own. So everything, you know, is just kind of fluff. And I'm also just kind of, like, staring at you, like, in a sus way when you first opened the repository.

### 🔧 セクション 22

Not not very proud of that thumbnail. I'm not gonna lie. I also think maybe streamlining the installation process, removing the experimental aspects, and then moving the demo up. I just kinda wanna clean it up a little bit. So if you're just getting started, you can go right off to the races.

### 🎯 セクション 23

And this is what I came up with. I'm pretty happy with how it turned out. Now while I was doing this over the last couple weeks, I had a lot of fun contributing and reading other people's code. Here are some other things that I enjoyed. First, I really enjoyed looking at people's pull requests.

### 💭 セクション 24

Being able to talk to other programmers really gave me a nice social moment, which I really miss from working as a programmer. When I was a programmer as a career, you know, like what most people are and not just silly little influencers like myself, I really enjoyed talking to other people about code changes directly in the repository. I also really enjoyed the feature request and scaffolding out ideas on how it can be implemented in the code base. At first, when I made this, I was really excited. The videos did really well.

### 📌 セクション 25

They went viral, but I think I quickly became a little bit embarrassed. I felt like maybe I was doing something bad by providing an easy tool for spammers to spam AI brain brain dead slob. And, yeah, it kind of is doing that. But this project made me realize something. That larger idea comes from smaller niches.

### ✅ セクション 26

As I was developing this, I felt like I was able to round off a lot of features and make it a much bigger thing. For example, I'm seeing a lot of these things right now. Okay? AWS Peter, where Peter Griffin talking to Stewie Griffin about how AWS resources work make that make sense. And when I look at that, it's really not that far off from what I've built three years ago.

### 📚 セクション 27

This project basically kicked off my whole programming influencer career, which is kind of insane to think about it. It was never there to get paid through AdSense or anything, which a lot of the gurus are telling you that you can do now with this. It was all about, can I do something cool? Can I automate something that I felt like was an automatable? That's even a word?

### 🔖 セクション 28

And I was able to, and it was an awesome feeling. And coming back to this repository three years later, it gave me that same feeling, and I'm so glad that I did it. Thanks again to JetBrains for sponsoring today's video. Make sure you check out Junie in the link below. Peace out, coders.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年10月06日

</div>
