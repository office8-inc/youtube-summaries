# 📺 GitHubのコードが8時間ごとに壊れていた理由 - マージキューの物語

## 📋 動画情報

- **タイトル**: GitHub's Code Was Breaking Every 8 Hours. Here's Why.
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=JJZQr2AuEI0](https://www.youtube.com/watch?v=JJZQr2AuEI0)
- **動画ID**: JJZQr2AuEI0
- **公開日**: 2026年02月19日 00:49
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

GitHubが2016年に直面した深刻な開発問題と、その解決策としてのマージキューシステムの誕生を詳しく解説する動画です。当時、GitHubのエンジニアは新機能をデプロイするのに8時間も待たされ、テストが通ってもプロダクション環境で失敗するという問題を抱えていました。「trains」という独自システムから最新のマージキューへの進化の過程を通じて、大規模ソフトウェア開発における継続的インテグレーションの重要性を学べます。ソフトウェアエンジニアや開発チームのマネージャーに最適な内容です。

## ⭐ 重要なポイント

- **Not Rocket Science Rule（2001年）**: テストが通れば マージ、失敗すれば却下 - 壊れたコミットをメインブランチに絶対に入れない
- **Trainsシステムの限界**：15個のプルリクエストを一括テストしていたが、1つが失敗すると全員がブロックされ8時間待ち
- **マージキューの革新**：各プルリクエストを個別にテストすることで、1つの失敗が他のエンジニアをブロックしない
- **2023年の成果**：1日あたり2,500以上のプルリクエストを500人のエンジニアが処理、待ち時間が33%削減
- GitHubは2023年半ばに**マージキューを全ユーザーに公開**し、オープンソースコミュニティ全体で利用可能に

## 📖 詳細内容

### 🎬 導入

Eight hours. That's how long GitHub engineers waited to deploy code. In 2016, test passed. Everything was green, but then production broke. The site could break every eight hours, push the boulder up the hill, watch it roll back down every single time.

### 📋 背景・概要

Here's how GitHub built that system. On October 18th, 2007, 22-year-old Chris Troth walked into a San Francisco bar called I Icon has Ruby, a weekly programmer meetup off to the side. Tom Preston Werner was seated alone when he saw Chris walk in. Despite barely knowing him, Tom waved him over to share some code that he's been working on, a program called Grit that made GI repositories easier to work with, and Chris loved it as a self-taught programmer used to piecing code together from blogs and forearms. This just felt like magic.

### ⭐ 主要ポイント

He made his first commit to Tom's repository the very next night. So lemme tell you about GitHub. In the very early days, GitHub was started by myself and my co-founder, Chris Stro. Initially there was two of us. What I did was the design, the front end.

### 📝 詳細説明

I also did the very back end. Being in the Ruby community and and going to Ruby Meetups. This is how I found my co-founders and Chris Swans. Roth was very big into Rails. He had a blog post that that outlined everything about how to be the best rails developer you can be.

### 💡 実例・デモ

I said, this is a guy that I can start a company with because we have complimentary skills. I'll do the front and back end, he'll do the middle part, and together we have the whole thing. And over the next four months, Chris, Tom and newcomer, PJ Hyatt spent countless hours building grit into something bigger. An online platform where developers can collaborate on code and host their own repositories. And they called it GitHub.

### 🔧 技術的詳細

GitHub is a place for web developers or desktop developers, security developers, really any kind of developer to share code with their colleagues with the world via open source. Everyone can make changes in their own little sphere of influence and then merge those up into the what is called a master. By April of 2008, they launched with zero outside investment that July. Tom's employer was acquired by Microsoft and he faced a choice, a cushy Microsoft job, paying nearly half a million in today's dollars, or GitHub, a scrappy startup with an uncertain future. Well, Tom believed in GitHub, so he took the risk.

### 🎯 応用例

Uh, we worked on it as a side project for probably almost a year, eight months or so without taking any salaries. And then any money that we made from the site, we just put in the bank account, we figured someday there will be enough money here and enough income to support us full time, hopefully. Right? And so really it was just patience, loving it enough to work on it after work. Patience to just wait for money to come in slowly.

### 💭 考察

And it paid off. 2009, 135,000 repositories, 2010 a million repositories, 2011, 2 million repositories, 2013, 10 million repositories. GitHub's growth was rapid. It was insane. A massive team of developers was then brought on to meet that growth.

### 📌 まとめ

But it wasn't long before the problems started. By 2016, GitHub had a massive code base constantly expanding from new services and updates and a ton of developers building and maintaining all of those. GitHub was considered a mono repo, a single repository hosting many different projects as opposed to something like a poly repo where each project sits separately. Both have their trade offs. Mono repos let you reuse code across projects easily.

### ✅ 結論

But by 20 16, 8 years into service, GitHub central repository was bombarded with nearly 1000 pull requests every single month. And this pushed the system to its computational limits. Developers had to wait for other branches to merge before trying their own, creating this giant dependency issue. Things were looking bad, but the devs had a solution that they called trains. A train was a special type of pull request that grouped multiple pull requests called passengers onto a train.

### 📚 追加情報

A user called a conductor would then deploy the test and merge them all at once. And at first, trains were great. It was significantly faster than testing each request individually, which there would be many of them. But with the passenger count quickly growing, it wasn't long before things just went off the rails. Eventually trains would carry 15 pull requests, all with gigantic significant changes.

### 🔖 補足

But with 15 requests on one train, conflicts were just inevitable. And when one failed, the whole train would just completely derail. Developers would wait eight hours for their feature to ship, only for the conductor to remove them and start over. It wasn't even used everywhere causing confusion about where you should work. It was just a mess.

### 🎨 セクション 13

And not only was this slowing down developers, it was causing site-wide issues. And users started to notice that Boulder kept rolling backwards. But before we get to GitHub's problem, we need to go back even further. Yeah, to 2001, programmers grade in horror and Ben Ellison were working at Red Hat on complex multi-time zone integration testing. It was high stakes work where even the smallest bug had disastrous consequences.

### 🚀 セクション 14

So Ben came up with something called the not Rocket Science Rule. Test Pass, merge it. If they fail, reject it. In other words, never allow a broken commitment to the main branch. Sounds obvious, right?

### ⚡ セクション 15

But here's why it's harder than it might seem. When a developer wants to fix a bug or add a feature, they have to create a branch, a copy of the main code base to work off of Safely. Next, they test their code and request team review. Once approved, their changes merge back into the main code base. But here's the problem.

### 🌟 セクション 16

What happens if someone changes the main code base while you're working? This is called merge sku, where the code you're testing code is out of date. It might work on the old version, but completely break the new version of it. So why even allow this? Why not just wait for the most up-to-date code before merging?

### 🎬 セクション 17

Well, simple time for small teams with few changes, the risk might be low, and if something breaks, it's quick to fix. So you prioritize speed over safety. But because of the high stakes nature of Grayden and Ben's project, they prioritized safety. They never allowed a broken commit into the main branch. Years later, Grayden was working on the Russ programming language and realized that nobody was enforcing this rule anymore.

### 📋 セクション 18

So he built Boris a small script that monitors pull requests, test them, and either merges them or rejects them. And this is one of the earliest versions of the merge queue. The idea evolved, homo bulldozer, Mefi, Kodiak, different tools, but fixing the same problems. Who knew that one part of the software development lifecycle would just be so cumbersome? What would you say was the largest technical challenge from, uh, with starting GitHub?

### ⭐ セクション 19

There was a period where performance became a problem. This is constantly a thing, right? Like your, your software project, it's popular if it's a service and then you have to scale it. And you didn't build it originally to scale very well because you're just trying to get it done. And so early in the GitHub story, after about a year, performance was getting really bad.

### 📝 セクション 20

Page loads were taking forever. And it was just because of the, the architecture that we had was all designed to work on a single file system. NFS disks set up so that every front end server would contact the same, a set of backend servers, but they would mount them and pretend like they were local. And it eventually turned out that this was not gonna scale really well. And this is where the performance problems were coming from.

### 💡 セクション 21

2020 was a huge year for GitHub acquired by Microsoft. Less than two years prior, the platform hosted over 56 million developers and 150 million repositories. Naturally, the internal team grew as well. And as GitHub engineers passed trains to handle increasing passengers, a massive flaw was revealed. The batch testing of the trains was quicker than individual testing, but only if the test passed, if it failed, the entire process derailed for trains.

### 🔧 セクション 22

Carrying 15 passengers with massive code changes, a single mistake blocked everyone else. Developers had to figure out who broke it, remove them, and start again. A process that sometimes took an eye watering eight hours per attempt and developers were reasonably frustrated. Front end users noticed these issues and the the trains just came to a grinding halt. After years of patching, GitHub realized that the trains had become a huge bottleneck.

### 🎯 セクション 23

Something fundamental had to change. Before we get to GitHub solution, another bottleneck that developers go through nowadays is code review, which is where today's sponsor codo comes in. 85% of developers are using AI to write code now, which means more pull requests, more changes and more stuff to review. CODO streamlines that by checking your PRS against rules it auto discovers from your existing MD files, actual code-based patterns and even historical PR comments. That way you're not building a rule bug from scratch.

### 💭 セクション 24

By the time you actually sit down to review code, the tedious stuff has already been caught with full code-based context. So the feedback is actually relevant to what you need to review, and you can see which rules get violated the most, which helps me decide if a rule should stay or go in my code base. Human code review can never ever be replaced, but with how much code that's being contributed nowadays, we can at least cut through the noise. And you can try CODO for free today by clicking the link in the description. Thanks again to Koto for sponsoring this part of the video.

### 📌 セクション 25

Now to GitHub solution, GitHub formed a small team to develop a successor to their train system. And like all proud software engineers, they decided to build it from scratch. As a company servicing massive enterprise clients, they couldn't just abandon the not rocket science rule for possible speed increases. They need something safe and fast, especially at the scale that they were. And so the thing that they built was a merge queue.

### ✅ セクション 26

How does a merge queue actually work with trains? GitHub would batch 15 pull requests together and test them as a group. One fails. All 15 engineers are blocked with a merge queue. Each pull request enters a line and gets tested individually against the current production code pass.

### 📚 セクション 27

It merges immediately fail. Well, only that one engineer is blocked. Think of it like airport security. Instead of sending 15 people through as a group, you check each person individually. One person fails only they get pulled aside or even picture it like this.

### 🔖 セクション 28

Imagine we have a simple drawing, a grassy hill with the sun and a dirt trail. Three artists want to make changes. Well, artist one adds birds in the sky, flowers on the ground, and changes the dirt trail into our river. No conflicts changes. Merged artist number two adds a bicyclist to the dirt.

### 🎨 セクション 29

But artist number one, remove the trail. So this doesn't work. It's sent back to artist two without merging in artist number three, adds a city skyline and a smiley face to the sun. No conflicts changes. Merged.

### 🚀 セクション 30

Same concept, different speeds. Each change is tested against the current state, non outdated one. The idea behind Merge queue is actually brilliant, but it does have its trade offs. Trains method of grouping requests and running a single test was less resource intensive than merge queue running a test for every individual request. Remember, there were so many developers working on this team that each developer was putting in multiple merge requests all the time.

### ⚡ セクション 31

But despite that, merge Q accomplished exactly what the team set out to do. They just had to implement it into the production system. By 2021, GitHub had over 1000 engineers across the globe. For the Merge Q team, this was an absolute nightmare. How do you roll out a new system with 1000 engineers actively pushing bug fixes new features and third party services?

### 🌟 セクション 32

It's like asking a pit crew to jump on a moving car and replace a wheel at the same time. What's the worst that could happen? They decided to implement it in phases, starting with small pul requests. Coordinating with the international team. They identify the least invasive moments to block deployments.

### 🎬 セクション 33

Sometimes they deploy and immediately roll back just before developers go online for the day. And it wasn't just implementation. They had to simultaneously train GitHub engineers on the new tool. If it's just you and your body working on something, well that's easy. But a thousand engineers, that takes weeks, if not months.

### 📋 セクション 34

For the next two years, they marched steadily forward testing, troubleshooting, implementing, and training this new system slowly replacing trains with this brand new system until finally implementation hit 100% and the results were remarkable. Over 2,500 pull requests daily from 500 engineers over double the amount from a few years ago wait times dropped by 33% and the system could handle 30 plus changes. Instead of 15. Engineers call it one of the best quality of life improvements ever made to their system. The Boulder stopped rolling backwards.

### ⭐ セクション 35

What started as a simple fix for a project over 20 years ago has become one of the most essential tools for the open source community. And in mid 2023, GitHub made merch queue available for everyone to use. When I first started learning how to program, I often got caught up thinking there was a right way to do everything. Even senior engineers often start from zero, inventing new solutions, taking risks, and hoping that they'll work. And one of the best parts about software is the reliance on the open source software community.

### 📝 セクション 36

Being able to find a solution that existed in the past can only happen because of these selfless engineers doing things just for the love of the game. We always stand on the shoulders of giants. Ais the inspiration behind some of the earliest versions of our merge queue was developed by Australian software engineer Peter Miller, who tragically passed away in 2014 after a long battle with leukemia. Without this massive contribution, we might not have the same systems that we have today. Software is complicated.

### 💡 セクション 37

Two developers doesn't mean software is written two times faster. It comes with its own caveats the more that you add. But when you find yourself pushing the same boulder uphill every single day, ask if there's a better way. Thanks to Will Smy and Lawrence gripper for the article on how GitHub merges hundreds of changes every single day. Also, great horror for his recollection of the origins of the merge queue and his script bores.

### 🔧 セクション 38

And Julian Dandu for the detailed overview of how merch queues became a small niche software to an industry requirement. What other hidden systems you want me to uncover next? Let me know in the comments. Thanks for watching.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年02月19日

</div>
