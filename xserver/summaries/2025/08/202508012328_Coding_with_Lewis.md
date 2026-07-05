# 📺 レシートプリンターでADHD流の生産性を改善した方法

## 📋 動画情報

- **タイトル**: I Fixed My ADHD with a Receipt Printer
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=xg45b8UXoZI](https://www.youtube.com/watch?v=xg45b8UXoZI)
- **動画ID**: xg45b8UXoZI
- **公開日**: 2025年08月01日 23:28
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画では、レシートプリンターとPythonを使って、タスク管理を“見える化”する独自の生産性システムを作る方法が紹介されます。  
ゲーム的な達成感を活用し、タスクを紙で処理していくことで先延ばしを減らす発想が中心です。  
プリンター接続、印字の整形、画像化による見た目改善、さらに自動化連携まで段階的に実装しています。  
集中が続きにくい人や、デジタルだけでは管理しづらい開発者に特に参考になります。  
最終的に、自分に合った運用へカスタマイズすることが生産性向上の鍵だと結論づけています。

## ⭐ 重要なポイント

- レシートを使ったタスク処理で「次にやる1件」を明確化し、心理的負荷を下げる設計が効果的。  
- Pythonの `escpos` ライブラリでプリンター制御が可能で、まずは簡単な文字印字から検証している。  
- レシート紙は10本で約35ドルと述べられており、初期コストと運用量の見積もりが必要。  
- 文字だけでなく画像印字に切り替えることで、チケットの可読性と達成感を高められる。  
- GmailやSlack連携、重複防止（埋め込み比較）まで拡張し、半自動のタスク発行基盤へ発展させている。

## 📖 詳細内容

### 🎬 導入

I cured my ADHD by building a productivity system using Python and this receipt printer. In this video, I'll show you how I built this and give you the source code at the end of the video. But first, what stops us from being productive? I read this great article called A Receipt Printer Cured My Procrastination by Laurie Harrell. In this article, they use game psychology to have a visual progression system while quickly creating tasks by printing to the receipt.

### 📋 背景・概要

What makes a video game addictive? Well, again, Laurie wrote a very detailed explanation so I'll let you check that out there. The easy answer is the small dopamine hits you get from the visuals, sound effects, or small sense of progression that helps you move along further even if the goal seems out of sight. For example, in World of Warcraft, telling someone to get to level 80 would be a tough ask. But defeat these small insects?

### ⭐ 主要ポイント

Easy. Now in real life, killing small insects for personal gain is dark morally. So what are these small ass in real life that we can imitate in gaming? And then it clicked. When I used to work at Starbucks, rather than stacking 12 cups that need to be made, we would put them in a line so that I was only working on one to two drinks at a time.

### 📝 詳細説明

That way, it was easy to visualize the queue. Or when I worked at a pizza place, we would print a ticket and once the order was complete, we would put it through the spike to let us know that we're finished it. This was also used as a gauge at the end of the night to see how crazy the day was or how slow it was. Now here is the annoying thing about receipt printers. When ordering the paper, you have to get a lot.

### 💡 実例・デモ

This 10 pack of receipt paper cost me $35. On Amazon at least, they don't sell anything with a smaller quantity, which I get. When I worked at Starbucks, we'd go through a ton of these a day. But this might last me forever. There's a lot of ways you can get these printers to work.

### 🔧 技術的詳細

First, there's USB B. Wow. But we also have Serial, which sends one bit at a time. It's very slow, but a lot of older systems still rely on this. Parallel sends the data in parallel because it has multiple data lines in the cable itself and port connector.

### 🎯 応用例

Still, this is widely obsolete. Network interface, let's say you're connecting a bunch of these things together. And then a cache box control, which sends a power signal to your POS device to open the cache box when the printer starts printing. You know, to give change. Now let's plug it in and put some paper in it to give it a test.

### 💭 考察

There's a Python package called esc POS, or esqpos, which lets us access these printers using Python. Let's go ahead and print out a simple message. So things worked out well. One issue though. Noise everywhere.

### 📌 まとめ

On the product page, it has a graphic saying low noise operation with picture of a woman sleeping with a baby. Yeah, maybe if your baby was deaf. The worst part though is that in the Windows settings, it already thinks it's silent. I almost returned it thinking it was broken. But guess what?

### ✅ 結論

Underneath the printer, there's a little screw area where you have little switches you can manipulate. Enterprise devices. Interesting. And so let's just flick this switch. Alright, another test.

### 📚 追加情報

Silent. Well, no more beeping at least. Now that we've set the printer up, let's get to coding. But first, thanks to the sponsor of today's video, Arcade. When building outwards facing AI apps that use tools with your existing services, things can be a headache really quickly.

### 🔖 補足

But with Arcade, you can securely authenticate your agents, connect to pre built connectors for apps you use daily, and evaluate your tool calls. You can deploy using Arcadeploy or a Docker container with easy integrations with some of the most popular SDKs that you build your AI apps with like LangChain, CrewAI, OpenAI Agents, and more. If you're using a weird software that no one uses like my receipt printer app, well, you can easily build your own tools by building your own toolkit. Keeping current with AI is already a huge headache, and with integrating AI with your own softwares, it becomes even harder. So I use arcade to manage this all for me and make it a breeze.

### 🎨 セクション 13

Thanks arcade for sponsoring this video. Now that we have our printer printing receipts, let's make this a little bit more pretty. Yeah, so this is where character encoding comes in. When you type out text in a word processor, or really anywhere, chances are it's in UTF-eight format. In comparison, which is an old school way of text, uses seven bits per character.

### 🚀 セクション 14

Since each bit can be a zero or a one, this gives us 127 unique characters we can use. But with UTF-eight, each character can be one to four bytes, meaning that the amount of possibilities is massive and can include emojis, accents, or other language characters. At first, I tried making some ASCII art, but wasn't really a fan of the readability. What we can do though, is print images. So I create a little webpage designed specifically for tickets using Tailwind.

### ⚡ セクション 15

I can then save this as an image using this Python package, and then print the image directly. And this gives us a nicer look. I went through a ton of iterations, but this is the one that I think looks best. Now, we have the most basic version of our productivity system working. We can easily insert something, post process using AI if needed, and print the receipt.

### 🌟 セクション 16

When finished, crush it up and view it in a container of some sort. Automatically, this feels pretty good, viewing a visual hierarchy. But that being said, this is a little bit too easy. What we can do though is take this to a whole other level. To help automate this process of printing tickets that I need to work on, I'm going to use Arcade to access my services programmatically.

### 🎬 セクション 17

The first obvious one is Gmail. Gmail is basically what everyone tries to automate, but sadly it just is the king. New emails mean that I have to insert tasks that come from a client or some other thing. Right now I'm just going run this through the command line, which is fine, but having something like this will mean we have to transform the way our application works a bit. When I get a new email or a Slack message, I can determine if it's worth creating a task for.

### 📋 セクション 18

Let's also create a whiteboard, in real life, to organize my tickets. I want to set it up also like a Kanban board, which I find helps me visualize the progress on tasks I need to complete. We have a extra to do, doing, done. Managing duplicates is something I want to prevent as well. If Gmail automatically prints my ticket, but I already manually printed it, well, confusion will happen.

### ⭐ セクション 19

So to keep track of everything, I'm going to create a vector database that will store the task in task descriptions and in embedding, which lets us easily match to see if a task is roughly the same. Let's build a toolset with Arcade. Essentially, of this as little functions that an AI can grab onto and execute if it deems as relevant to the user query. Our database is simple. Just single table with all the tasks that it has created.

### 📝 セクション 20

So I'm going to create a few tools that the AI agent can use. Read from the database, write a row to the database, and compare embeddings. Let's deploy and give it a test. So perfect. A fully autonomous system to help me get things done.

### 💡 セクション 21

Way overengineered, of course. And there we go. Going analog, well, sort of, is a huge boost in productivity for someone like me that needs to see everything in a visual hierarchy. Something I learned is that productivity systems are really dependent on your personal needs, which is why you can check out the code and implement something yourself by clicking the link below. Peace out, coders.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月06日

</div>
