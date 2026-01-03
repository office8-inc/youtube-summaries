# 📺 これなしでPythonを使うな！必須ツール8選

## 📋 動画情報

- **タイトル**: Don’t Use Python Without These 8 Tools
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=RU_ZcKzFdG0](https://www.youtube.com/watch?v=RU_ZcKzFdG0)
- **動画ID**: RU_ZcKzFdG0
- **公開日**: 2025年10月31日 01:39
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画では、Python開発を劇的に改善する8つの必須ツールを紹介しています。UV、Ruff、型チェッカー、Pytestなど、モダンなPython開発環境を構築するための厳選されたツールを解説。これらのツールを使うことで、開発速度の向上、コード品質の改善、そして生産性の大幅なアップが期待できます。Python開発者、特に効率的な開発環境を求めている方やAI/機械学習プロジェクトに取り組んでいる方に最適な内容です。

## ⭐ 重要なポイント

- **UV（パッケージマネージャー）**: Rust製でPIPの100倍高速、グローバルキャッシュ機能でAI/MLライブラリの再インストールが効率化
- **Ruff（リンター＆フォーマッター）**: 従来のリンターより圧倒的に高速（Autoflakeの6秒に対し0.16秒）、コード品質の即時改善が可能
- **型チェッカーの活用**: Pylance、Pyright、Basedpyright、Pylyzerなどで実行前にバグを発見し、開発サイクルを短縮
- **Pytest（テストフレームワーク）**: シンプルな構文で効果的なユニットテストを実現、豊富なプラグインエコシステム
- **Pydantic（データ検証）**: 型システムを活用した強力なデータバリデーション、厳格モードと非厳格モードの選択が可能

## 📖 詳細内容

### 🎬 導入

Python 3.14 is here, but don't write a single line of code without looking at these first. This is the Python modern toolkit. First off, one of my favorites is UV. I started using this as a replacement for the PIP package manager, but found out that it can do a ton of other really cool stuff that I never knew. Before I talk about that though, the UV package manager sold me with it being written in Rust.

### 📋 背景・概要

Just kind of like how you know everything gets karma nowadays. Now, their benchmarks do say that they are 100 times faster than PIP, which it's their own benchmark, so you got to kind of be a bit skeptical of that. But either way, you can just tell [music] that this is going to be a really, really fast. But something that I really like is the global caching. And that's something that is just an absolute lifesaver for me, especially if you've seen my other videos.

### ⭐ 主要ポイント

I'm always creating local AI or machine learning projects. So, I'm always having to reinstall those Python libraries that are just hefty and big like the Nvidia CUDA libraries or something. And this global cache can help me [music] with that. So, thank you very much. Now, UV was supposed to be the poetry and pip replacement, [music] but it's actually also the pi replacement as well.

### 📝 詳細説明

Yeah, you can manage your own Python versions in here as well. So, first you want to install a virtual environment. And what I like about it is that it has backwards compatibility with pip. [music] So, if you have like a requirements.txt file, it would be able to identify that. Why do people think it's hard in Python?

### 💡 実例・デモ

Like, it's just literally a text file. Like, it's not even that hard. And with UV Python, it gives me all my Python that I have installed like 3.10. If you're in the JavaScript ecosystem, first of all, how is your mental health doing today? Second of all, then you understand something called a lock file.

### 🔧 技術的詳細

And okay, I know it's in other programming languages as well, not just JavaScript. Okay, I just have to speak to my demographic here. Lock files offer more precision than traditional requirements.txt [music] files by capturing the exact versions of both direct and indirect dependencies. And this creates a complete snapshot of your project's dependency tree, preventing the dreaded it works on my machine problem. and ensuring identical setups across all your different environments.

### 🎯 応用例

So, next up is rough. Now, this project is actually made by the same people, [music] which let me have a look here. I'm on to you, which means that it's a really, really fast Python tool and it's a formatter and llinter for your Python code. Again, looking at their metric made by themselves, other llinters are extremely slow in comparison. Autoflake over here is at 6 seconds while rough is at.16 seconds.

### 💭 考察

And poor pilot. Look at this. It's still going on my screen. [laughter] Like wow. With flake 8, you would usually use a language server so you can implement it directly into your Visual Studio Code, PyCharm, Notepad++, Dreamweaver if that's what you're still using.

### 📌 まとめ

And with Rough, [music] it's actually the same. You install it through pip or UV like mentioned above. Usually this is done for you. if you install it as an extension in your code editor like Visual Studio Code and PyCharm. Now, I will save you the more technical in-depth details as you'll find a lot of things that you can do in their config files, but just know that Rough has the ability to lint your code, format your code, and more.

### ✅ 結論

But it's just really fast. [music] Rough is definitely a much easier switch than UV, and if you aren't using this, it just kind of feels like a waste of time. If you've seen my ADHD printer video with Python and want to build something similar with like a Gent AI, make sure you check out the sponsor of today's video, Arcade Dev. Arcade lets your AI agent securely take real world applications through user specific permissions, pre-built MCP servers for Gmail, Slack, GitHub, and more. But what I really like is easily creating my own MCP server.

### 📚 追加情報

Similar to if you're developing like an HTTP server, you can create an MCP server using a decorator and use Python typings to help generate the code that an agent that either you developed or claude cla cursor whatever can use. You simply install the arcade CLI. Then you run the arcade new command and then you just kind of start coding. Everything is ready to get going. Then we can just run our MCP server locally or deploy it.

### 🔖 補足

So you can use it in your VS Code, cursor CL. I mean, everyone's different, you know, where wherever they consume MCP servers if that's something you're into. When it comes to building with current LLM technology, the concept of tools or agents is what turns an AI app from an annoying little bubble in the corner of a software that you have downloaded to a massive productivity booster. Make sure you check out Arcade Dev in the description below. Thank you, Arcade, for sponsoring today's video.

### 🎨 セクション 13

This one is going to depend on what code editor that you use. Type-checking is something that isn't built into Python. When you say something has to return an integer, but you return a string instead, it will just kind of sit in the corner and watch you burn. It'll just let it happen. Type checkers, for the most part, will let you know about this before you even run your code, usually by telling you in your code editor or through the terminal.

### 🚀 セクション 14

I've had mixed results with this. So I have a couple of recommendations depending on what you use. If you use Visual Studio Code, then Microsoft has a really good one called Pilance. Now Pilance is not open- source, but it does use something called Pyite, which is open source, which is also from Microsoft. And so for the most part, Pyite is the kind of the standard when it comes to it.

### ⚡ セクション 15

Pyite has a language server and it's pretty fast and flexible. One of the OGs though is My Pi. My Pi is a static type checker for Python. It's really easy to set up. A lot of places already support it through plugins, [music] and it also does have its own language server of sorts, but from what I read online, it does seem somewhat unstable, but your move may vary.

### 🌟 セクション 16

It's also worth noting that this is actually written in Python. So, for large code [music] bases, it does recommend you use the server, but you still might have a really slow experience with it. Let's be honest here. To the kind of the more newcomers on the block here. First, we have something called Pyizer.

### 🎬 セクション 17

[music] Pyizer is written in Rust, so it goes really, really fast. We've gone over this before. Hi there, future me. This video was made like 3 or 4 months ago, but it turns out that Astral, the people that made Rough Nuv, yeah, those freaking people, they made something called Tai, which I talked about, but it was just new. Well, it turns out that Pylizer is working on that.

### 📋 セクション 18

And so, yeah. And as of this video, there's been a sneak peek from the people from Rough about a type checker that they're making called Thai. And that's been released for a minute now, and it has its own language server. You can actually just download it as a VS Code [music] extension. Um, it works pretty well so far, but it's my code.

### ⭐ セクション 19

And with Python being dynamic, we sometimes run into an iterative cycle of just running our code, fixing the bug, and seeing if it works versus getting the solution [music] right off the bat. In my opinion, a type checker is a huge productivity boost for developers, and I mean, it's been in Python for a bit now, but you should be using it. Unit test can help you change your code and know that you're not breaking something without having to test it manually. One of the best options for this is Piest. [music] Piest is just simple.

### 📝 セクション 20

You write small tests and it simply just works. There's a lot that goes into tests. one being fixtures which means that you have to run before or after a test like setting up a current state or connecting to a database of some sort. If you need to, you know, test a certain condition, you have to set that [music] up first. And in Piest, they have a pretty easy way of dealing with this using a decorator.

### 💡 セクション 21

You can do things with it like change the scope. So, you just run once per module rather than every single test or add in parameters or [music] auto use them. And the output is pretty nice as well, giving you a pretty detailed view of why your code succeeded or failed. It's also just really customizable where you can set up a test directory or just have it in testing in [music] different ways. And it's very heavily documented with huge plug-in and extension ecosystems like connecting it with playright or other Python tools like flake or even connecting to specific databases.

### 🔧 セクション 22

[music] Now, even though Piest is really simple, you could also just use the standard unit test library that is also built into Python. Although, I don't really mind the class-based unit test system, I know a lot of people on Reddit, YouTube, whatever didn't like it and prefer the whole functionbased system. [music] So, what can you really do? No matter what though, even if you choose to use the standard unit test library that comes built into Python or if you use Piest, make sure you implement some sort of test system in some sort of way. Idantic is a data validation library.

### 🎯 セクション 23

Often we're dealing with objects, [music] dictionaries of some sort. This could be the parameters that you send into an HTTP request or just data that your model is using. It could be a database. It could just literally be anything. With Pyantic, you can define all of this and get pretty complex with it like annotations, dictionaries, literals, and even more.

### 💭 セクション 24

This can also be converted into a JSON schema. [music] And since you're using types anyway, Pyantic just makes it really easy to validate your code in different ways. And depending on how you like to code, you can actually use a strict mode or a non-strict mode. Non-strict mode takes common differences and tries to infer them. However, there's also the strict mode which just doesn't even do this.

### 📌 セクション 25

It just tells you, [music] nope, that's not right. And Pyantic actually integrates with lots of different existing Python dev tools like PyCharm, Visual Studio Code, or even My Pi Rich, which is [music] the console formatting library. Pyantic uses the Python type system, which makes it really easy [music] to just plug into any codebase that you're using and just quickly iterate over that. [music] I'd highly recommend it. It's such an awesome library.

### ✅ セクション 26

So, here are some other things that I like using that I didn't really feel like had a certain category. One of my favorite ways to use Python is through Docker containers. Docker containers deserves their whole other video, and I've done a ton of shorts on them already, but being able to reliably run your code anywhere just makes Python even more powerful. Dealing with the whole virtual environments thing is just it can be a pain. There's a lot of benefits of using Docker, even just outside of the whole Python ecosystem, [music] but sometimes transferring projects between computers or between other collaborators can be a huge hassle.

### 📚 セクション 27

And Docker makes this really easy. You can basically just deploy it anywhere too as is. It's honestly great. Again, not Python specific, [music] but pre-commit is a really handy tool if you're working with a team. It essentially just gives you the ability to control actions in between different states of your [music] version control.

### 🔖 セクション 28

So, for example, I can choose to run something before a git commit like my pie rough. Make sure to check types. A lot of the times you want to do this to clean up your version control [music] in the repository using like a continuous integration software, but by using pre-commit, you can actually filter out a lot of the errors that you originally make as well as not [music] have to spend that cloud compute cost. This is just a handy tool to have in general. It's honestly pretty good.

### 🎨 セクション 29

[music] And this one is a little bit silly, but kind of motivated me to make this video. Just make sure you're upgrading to the newer version of Python. Don't use Python 2. Okay? And if you don't know what an fstring is, then you should have upgraded Python like 10 years ago.

### 🚀 セクション 30

Okay, I remember the days when people would argue against Python 2 versus Python 3. It was just it wow. The error messages are much better. A new type of interpreter, which looks pretty interesting. It's not always worth trying to get the latest and greatest, but just make sure that you've upgraded to a somewhat newer version.

### ⚡ セクション 31

I mean, it might just be a security risk otherwise. [music] Using Python in 2025 is the best it's [music] ever been. The amount of dev tools that are readily available to all Python developers just makes it such a fantastic [music] experience. As somebody who looks at the JavaScript and TypeScript ecosystem, I was jealous of their huge growth and fast growth. But I'm glad that Python is getting at least somewhat of a similar vibe to it.

### 🌟 セクション 32

Let me know what you use in your Python development library in the comments below and make sure you subscribe for more. Peace out coders.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年01月03日

</div>
