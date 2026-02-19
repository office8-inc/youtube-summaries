# 📺 Human Developer vs AI Agent (Actual Test)

## 📋 動画情報

- **タイトル**: Human Developer vs AI Agent (Actual Test)
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=EkadHKoGriE](https://www.youtube.com/watch?v=EkadHKoGriE)
- **動画ID**: EkadHKoGriE
- **公開日**: 2025年10月04日 02:46
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

These two apps look identical, but one was made by me and the other completely by an AI agent. In this video, me and an AI agent both make the same apps, and I'm gonna show you the pros and cons of both. Replit is a sponsor of today's video, but they haven't seen the results of this test. So let's establish some rules. For me, I cannot use AI to generate code, but can use it as a rubber duck of sorts.

### 📋 背景・概要

All features in the specification must be included. And to help the AI, I will bump it generally in the right direction if it asks me anything. Let's start off with a fairly easy application. A dev portfolio generator. The idea is the user goes on the site, uses the GitHub API to grab all projects from a user and format it in a way that is nice so that you can share this to potential employers.

### ⭐ 主要ポイント

The bare bones would be authentication, connect to the GitHub API, use a database to store all of your portfolios, have a link that's publicly available, a design that is fresh. And I'm also going to use a technology I'm not 100% familiar with as a way to truly test how fast someone could go. So let's try. Now without much thinking, I just chose some of the technologies I thought of off the top of my head. Next.

### 📝 詳細説明

Js, Supabase for the managed database and auth, Drizzle for ORM, and Tailwind for styling. Luckily, there's a good Supabase starter pack that includes the authentication already. So I just used that and dug around a little bit. My first goal is to knock out the hardest thing, I think. And that is the GitHub OAuth integration.

### 💡 実例・デモ

So 10 have gone by and I'm about halfway through the integration of GitHub. So, so far it's much easier than I thought. Of course, though, with a managed service like Supabase, that will do it for you for a cost. The Repla agent basically created all the components needed and created a design for the overall look of the application. Now here's one of the issues right away with AI is that the look and feel of an application always feels blocky or the same.

### 🔧 技術的詳細

I think AI has a hard time seeing something complex and then turning it into code. Either way though, it got the vibe right. A GitHub search bar right in the middle of the screen. One thing that is strange about this though is the fact that when you enter a GitHub username, it forces Not you to log the best user experience at the moment. It still is fixing some other things it detects though, so we'll come back to that later.

### 🎯 応用例

At this point I started looking into Drizzle ORM so I can start creating this application data structure. Now how this will work is that the user can have a profile, the profile can have many portfolios, the portfolios can have many portfolio items, But a portfolio item can only be part of one portfolio. And a portfolio can only be part of one profile. Then, just so we can save on API requests, we'll also store the repositories that we get from the GitHub API in a repository table as well. For the thirty minute mark, I was actually able to start defining the schemas for our database.

### 💭 考察

I actually feel like I'm blazing through this application, and to be honest, pretty impressed with myself. Replit was focused on making the user flow a lot cleaner and to handle almost all use cases like failures, registration failures, proper redirects, and database errors, which wow, okay. Almost like it's mocking me by working on the more boring stuff. This is where agents are really handy compared to your regular chat interface, but it's also where it spends most of his time looking at screenshots and thinking about his next steps. Think about this for a second.

### 📌 まとめ

When you do a search on Google, it's almost our first instinct to almost immediately click the first or second link. But with an agent, it has to sit there and ponder the universe before it decides to do that. Now, even though it's doing these things slower than I would, it's still thinking and implementing much faster. Yeah, it really does still win at the end of the day. Now, one hour has passed and I've just finished migrating all of the database schemas and got started on working on the main portfolio generator.

### ✅ 結論

This would have been a little quicker, but I'm still trying to figure out some of these technologies I haven't used before. But so far so good. But here's the thing, I'm actually really enjoying writing the code myself. I have a grasp of what is working and what isn't. So when something does go wrong on the application, I actually know where to go and roughly what it will take to fix versus when you vibe code, you just kind of have to guess.

### 📚 追加情報

You're like a project manager. There's no way you're checking that code, so you keep prompting away. It kind of reminds me of when I worked on a large code base for a long time. Everything felt comfortable. I kind of knew how to navigate it.

### 🔖 補足

And then when I had a new request for a feature come in, I knew where to navigate and how to tackle it. At this rate, Replit was just flexing for fun. It just decided, what if we add functionality for you to print your portfolio page as a PDF? It's like it needs to entertain itself by making features up and just implementing them. It also decided to add a password reset functionality, which come on, chill.

### 🎨 セクション 13

You guys gotta chill. I did have to go back and forth with it a little to get the GitHub OAuth working, because just it can't log in or get an API key on its own. But once that was implemented, it actually worked pretty well. Really, Replit finished this a while ago. Let's be honest here.

### 🚀 セクション 14

But I would say at this spot here is where I would release this application. However, since I'm still working on mine for who knows how, I'm going to give Replit the ability to just go ham and keep going and build whatever it thinks is the best. One hour and forty five minutes. This is when I finished the biggest functionality of this application, the portfolio section. Realistically, this would have taken way less than forty five minutes if I were using a different stack.

### ⚡ セクション 15

However, I think my implementation was pretty good. I also added the ability to go public or private. This feature is actually pretty easy. You just disable the ability for people to view by putting it behind an auth log. Otherwise, just go to the URL and you're good to go.

### 🌟 セクション 16

Now, the app works as intended but looks super ugly, so I'll spend the remaining amount of time making it look a lot cleaner. Replit decided to add a new template system. Testimonials, follows, endorsements, advanced analytics, monetization. It went crazy. Amazing scheme life and change complete.

### 🎬 セクション 17

Something I realized is that I created the ability to have multiple portfolios while this application only lets you have one. Here's the thing though, with Replit, I can just tell it to change this and it will do it in like five minutes. For me, this would be a complete refactor. And this is where things started to become clear to me. But more on that in a second.

### 📋 セクション 18

So I would say at this point, I would happily show this to my friends and be like, hey, do you think this is a stupid idea or a smart idea? I added some styling, animations and some polish in areas that just really needed it. Of course, this is still a rush of a job. But I actually had a lot of fun making it. And isn't that the point of everything anyway?

### ⭐ セクション 19

Replit on the other hand just kept going, going and going. I told it to not stop until it had every feature that it deemed complete. Maybe it's having a little bit more fun than I had. Overall, if you look at the code quality between mine and the one in Replit, Replit says much better. I can't really beat a robot that has all of the training data on the internet, can I?

### 📝 セクション 20

But here's what became clear to me when I did this challenge: Writing your own code is valuable despite AI's disruption in this industry. AI develops software for humans, but obviously lacks the empathy or the true understanding of a human. So it can only get so far when it comes to creating software. While I was working on this, I had an AI agent work in the background on another small project, Notion, but in a text user interface, and it makes using Notion much better. This is where I believe AI comes really handy actually.

### 💡 セクション 21

For building ideas you want to validate or maybe just a small use case that you and a small amount of people might have, then kind of just jump on it, let the AI do its work, and then you just kind of get to try it out once it's done. Where I find writing code makes a lot of sense is when you are developing a product that people need and you need to iterate over quickly. And when I worked on this, I really just enjoyed having that knowledge of my project, knowing where to go, you know, kind of like the old days, I guess. So when people say like AI is replacing programmers, it definitely is not true. It's just becoming a great valuable tool for developers to use to make their software better.

### 🔧 セクション 22

Sometimes you are stuck at the mercy of the AI because of an infinite loop and you just have to go in yourself. Which kind of brings me to another point. You're probably going to have to read a lot more code, which, you know, is that really a bad thing? If you want to check out Repla Agent three, you can check out the link in my description. I really enjoyed using it and I have a couple of other projects on the go that I wanted to work on but didn't really have the time to do, and it'll notify me on my iPad or my phone when, you know, it needs a review.

### 🎯 セクション 23

Agent three is able to run for like two hundred minutes at a single prompt, meaning you can, you know, go do your laundry, maybe speak to somebody. Yeah, you're probably not going to do that, though, are you? Thanks for watching. Subscribe for more.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年02月20日

</div>
