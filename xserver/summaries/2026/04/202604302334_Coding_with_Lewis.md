# 📺 The Code Inside Everything (That Gets Zero Credit)

## 📋 動画情報

- **タイトル**: The Code Inside Everything (That Gets Zero Credit)
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=lSVgeMoXJTs](https://www.youtube.com/watch?v=lSVgeMoXJTs)
- **動画ID**: lSVgeMoXJTs
- **公開日**: 2026年04月30日 23:34
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

What's the most used piece of software in human history? Windows? Chrome? IOS? No.

### 📋 背景・概要

There are over 1,000,000,000,000 active SQLite databases on earth right now. It's on every iPhone, every Android, every copy of Chrome, Safari, Firefox, every Mac, every Windows. If you have a phone in your pocket, you're running hundreds of SQLite databases at this very moment and almost nobody knows what it is. How did the most important software on earth become the most invisible? It was the year 2000.

### ⭐ 主要ポイント

The y two k panic settled. The Nasdaq hits a record high during the .com boom. Tech could only go up from here. But not on the DDG seven nine Oscar Austin, a guided missile destroyer in Maine. One piece of software kept failing at the worst possible times and Richard Hip was a contractor on that ship.

### 📝 詳細説明

It was contracted with Bath Iron Works, and Bath Iron Works was building DGG 79. They had a damage there was a damage control system. Mhmm. It's just an information system for the sailors so that, you know, if they take damage to the ship, you know, you need to be able to turn valves and circuit breakers off to isolate the damage and then turn others on in order to get Mhmm. Necessary support to critical systems.

### 💡 実例・デモ

But Richard wasn't a database guy. He had a PhD in computational linguistics and masters in electrical engineering. He ran a small consulted company with his wife out of Charlotte, North Carolina. She was the president and he was the head of research. During the nineteen nineties, there were two extreme players in the world of enterprise databases, Oracle and Informix.

### 🔧 技術的詳細

And to say they were obsessed with beating one another is an understatement. Informix put a billboard outside of Oracle's headquarters saying dinosaur crossing, claiming they're old and frail. But all that corporate warfare didn't matter much when the servers just stopped working. Cannot connect a database server. All the data to to compute this was stored on an informix database.

### 🎯 応用例

Software that I wrote to solve this, you know, they double click on it to bring it up. And if the Informix database engine was down, I'd paint a dialogue box and say, database unavailable. And that would happen, and they'd call me up and complain that my software broke. I'm thinking, this this is not a good situation. I don't want I don't want to take the blame because some system administrator took down the database engine.

### 💭 考察

That's when Richard asked himself Why why do I need a separate process to store this data? Why can't I just read it directly from the disk myself? And that way, if the machine is healthy enough that they can double click on my application, it should be able to read the data. Right? But sadly, there were not many solutions.

### 📌 まとめ

Remember, you couldn't just Google something around this time. Then someone Richard worked with said, why don't you just write one? Richard did the thing that all programmers are guilty of, added to his list of side projects to do. Eventually, of course. Well, eventually came sooner than expected.

### ✅ 結論

A government funding dispute shut down contracts across the country and Richard was one of those casualties. To occupy his free time, he decided to work on that very project that he tried to find before, a SQL database that didn't need a server. What if it was just a file? SQLite skips the server entirely. Your app opens a file on your disk and just reads the data directly.

### 📚 追加情報

There's no middleman or dependency on an outside service. It's just one file. And just like that, SQLite was created. Then even better news. His contract renewed for the ship project and things will be easier this time.

### 🔖 補足

We have a SQL database that will make things 10 times easier. Well, unfortunately, the hype didn't last long. And Formix was here to stay. But hey, maybe someone will find this useful for their small project online. So Richard uploads SQLite to his own company's website under open source software.

### 🎨 セクション 13

That way, anyone can use it. Now, back to work. It didn't take long before people caught on what Richard actually posted online. The flexibility that a one file database provided had a ton of use cases. One of those posts would show the true potential of what SQLite can do.

### 🚀 セクション 14

Someone was able to put SQLite on a PalmPilot, a computer that can fit in your pocket. If you're in business, you had a PalmPilot. One of the biggest limitations, no internet and only two to eight megabytes of ram. So the fact that someone was able to put an entire SQL database onto it was revolutionary to say the least. The news group went crazy.

### ⚡ セクション 15

Tinkerers start to download SQLite to try it out on their own projects. People would give their feedback and this made Richard continue working on it in his spare time. Emails, downloads, news groups, it was growing rapidly and then a phone call. It was Motorola. They'd seen what sequel like could do on devices like the Palm Pilot.

### 🌟 セクション 16

They wanted it baked into their brand new mobile phone OS. Can you do that? Sure. I'll get back to you tomorrow with a budget. Immediate panic.

### 🎬 セクション 17

How do you price out a software that is open source and free? How does that even work? At the end of the day, there really isn't a way you can put a price on it. It's about the hard work and labor that goes into the $80,000. So Richard brought on three other people he worked with to integrate SQLite into the new mobile phone operating system.

### 📋 セクション 18

Richard received the most money he'd ever received in his life by making free software. How does that work? It wasn't long before another call came in, this time AOL. If you're too young to remember, AOL wasn't just an internet company, it was the internet back then. Version five point o.

### ⭐ セクション 19

The easiest just got easier. Plug it in and you're good to go. Even my grandpa can do it. AOL's got it all. You've got mail, you've got pictures.

### 📝 セクション 20

Every house in America would open up their mailboxes and see yet another free minute CD. And AOL wanted Sequel Light on all of those. Sequel Light would provide the benefits of having a database while taking only a tiny fraction of the space. If Motorola was a game changer, then this was a life changer. They flew Richard out to discuss contract specifics.

### 💡 セクション 21

During the negotiations, he decided to show off a feature that he was developing specifically for AOL. Temporary indexes. It's like a shortcut for finding data faster. Instead of the database scanning through every single row, the index tells it exactly where to look. Except this was temporary.

### 🔧 セクション 22

It exists while you need it and disappears when you don't. As this was being presented, Richard realized something crucial in the sentence. It's completely broken. If one user creates a temp index and another user updates the table, well, the index goes stale. He just bragged about a feature that was completely broken.

### 🎯 セクション 23

But nobody noticed. Hopefully. Motorola, AOL, Richard's side project was becoming a real business. But the call that would change everything came from London, Symbian, the operating system that powered Nokia, the biggest phone company on the planet at the time. They wanted Richard to fly out and meet with them Thanksgiving Day.

### 💭 セクション 24

Richard landed in London and was surprised by what they told him. They told me that they had a a bake off. All nine other than they all had the opportunity to tune their database for the operating system. They had a bake off and I won. Mhmm.

### 📌 セクション 25

And I didn't even know this was happening. They had 10 different database engines, and this is them telling me. I I have no person on it. The other nine, seven of them were closed proprietary. But Symbian had one concern.

### ✅ セクション 26

They called it the bus factor. As in how many people have to get hit by a bus before this project dies. It probably sounded nicer on paper. For SQLite, that number was way too low. So Richard tried to set up a consortium, a formal structure where companies could fund SQLite's development and guarantee its longevity, something we see to this very day.

### 📚 セクション 27

He put together this whole plan, voting rights for members, corporate governments, the works, the boring stuff. But then his phone rang again. It was Mitchell Baker, the head of the Mozilla Foundation, a lawyer by training. She said that he was doing everything wrong. The developers make all the decisions.

### 🔖 セクション 28

The companies get the honor of contributing money. No voting rights on what goes into the code. No corporate governments over the technical direction. The developers are in control, period. But how did they get people to join under those conditions?

### 🎨 セクション 29

And that's when Mitchell pledged Mozilla being a founding member of the consortium. Sure enough, Symbian, Mozilla, and Adobe became the founding members of the SQLite consortium. The project finally had financial backing. But here's the thing, the consortium funded the project, it didn't open it up. Richard didn't start accepting code from the public.

### 🚀 セクション 30

He didn't even put it on GitHub. He didn't invite contributions. The money came in but the code stayed closed. The whole world could depend on SQLite, but SQLite would not depend on the whole world. Every line of SQLite would continue to be written by the people who understand the entire system.

### ⚡ セクション 31

That was the deal. That was always going to be the deal. And by the mid two thousands, all major smartphones were running Sequel Lite. Richard had seen early phone development from every angle. Motorola, Nokia, Symbian.

### 🌟 セクション 32

Then in 2005, Google called. They were working on a prototype phone. It had a full keyboard at the bottom and a small screen at the top, like a Blackberry. They were debugging SQLite on the phone and had it connected to a workstation, running a full debugger on a mobile device. Nobody else could do that.

### 🎬 セクション 33

But then the phone actually rang, an actual phone call on the prototype. The engineer looked at it and answered. Richard played it cool, but inside his mind was exploding. They were debugging software on a phone that was connected to the public cell network. Motorola couldn't do that.

### 📋 セクション 34

Nokia couldn't do that. They were still using breadboard prototypes that couldn't even make calls. This early prototype was where Android first started. In that moment, Richard knew. Android was going to be huge and he couldn't tell anyone.

### ⭐ セクション 35

Not Motorola, not Symbian, not Nokia. He just had to watch it happen. Android launched. SQLite shipped on every single device. Millions of phones.

### 📝 セクション 36

Then tens of millions. Then hundreds of millions. But that's when the bugs started showing up. They were getting crash reports constantly. The scale had exposed every edge case, every assumption, every corner they never tested.

### 💡 セクション 37

The thing that worked perfectly for years was suddenly breaking everywhere. A small team drowning in bug reports from millions of users on the world's fastest growing platform. What now? Being such a small team, they could have folded but instead, Richard did something kind of insane. Around the same time he'd been doing work for Rockwell Collins, an avionics manufacturer, they introduced him to d o one seven eight b, a quality standard used for safety critical aviation software.

### 🔧 セクション 38

The stuff that makes sure planes don't crash. So pretty secure. Richard decided to hold SQLite, a free open source database to the same standard as commercial flight software. He spent an entire year, sixty hour weeks, twelve hour days, every single day writing tests to achieve 100% MCDC coverage. That's modified condition decision coverage at the machine code level.

### 🎯 セクション 39

Every single branch in the compiled binary had to be tested both ways. A 155,000 lines of source code, 92,000,000 lines of tests, a 590 to one ratio. Before every release, they ran billions of individual test cases across multiple operating systems, multiple architectures for at least three days straight. What I did find is when I tested the d o one seventy eight b level, the bugs just largely went away. And, like, how many would you get?

### 💭 セクション 40

Like, how much was it, like, from the start versus how much was it after? I I don't have hard numbers for you but it got to the point we just didn't hear from. Right. So it's kind of like, you know, you got so many a day to like like almost like you'd wake up to it to like you wouldn't hear from for a couple weeks or some. One year of brutal grinding work and then near silence for almost a decade.

### 📌 セクション 41

Growth didn't stop. If anything, it was rising at a much more rapid pace. Android kept growing. The iPhone launched and shipped with SQLite. Every browser adopted it.

### ✅ セクション 42

Every major operating system bundled it. The Airbus a three five zero runs it. WhatsApp stores every message you've ever sent in it. Your iMessages, your Spotify library, your Dropbox sync, Adobe Photoshop, Skype. There are now more active SQL like databases on earth than there are human beings.

### 📚 セクション 43

And throughout all of this, Motorola, AOL, Symbian, Google, the Android crisis, the team never got big. Dan Kennedy, an Australian developer living in Southeast Asia joined in 2002. Joe Moustacheken came on too and that was it. Three people. A trillion databases.

### 🔖 セクション 44

And they weren't hiring. Let's just sit with that for a sec. MongoDB, a database with a fraction of SQLite's deployment, went public at $4,000,000,000 valuation. Snowflake IPO'd at 33,000,000,000. Redis Labs raised 350,000,000.

### 🎨 セクション 45

Hundreds of engineers, thousands, massive campuses, billions in funding. Richard never took a dollar VC money, never IPO'd, never been acquired. He still runs the same small company with his wife in Charlotte, North Carolina. She's still the president and he's still the head of research. So how does a three person team maintain something this massive?

### 🚀 セクション 46

How does that even work? It works because nobody else is allowed to touch it. SQL ite does not accept much outside contributions. It hasn't for its entire existence. You can copy it, sell it, modify it, but you cannot contribute code to it.

### ⚡ セクション 47

But why? Because SQLite is a public domain. Not MIT licensed, not Apache, not GPL. No license at all. And to keep that status bulletproof, every single line has to be clean.

### 🌟 セクション 48

If even one of the copyrighted code gets in, the entire public domain status could be challenged. The first version of SQLite used GDBM, a GPL licensed library. If he'd kept it, SQLite would have been locked into the GPL forever. It could never have shipped on the iPhone or Photoshop or the Airbus A350. So he rewrote the storage engine from scratch.

### 🎬 セクション 49

When he needed the algorithm, he pulled the art of computer programming off his shelf and built it. Except the book only described searching and inserting into a b tree. Deleting? An exercise for the reader. So Richard had to solve the homework before he could build the database.

### 📋 セクション 50

He wrote his own parser generator, his own version control, his own bug tracker, even his text editor. Every dependency avoided was a future crisis prevented. Why why do I need to write all these test for somebody else's code when I can write my own. Right? So I did.

### ⭐ セクション 51

And that was SQLite version two. When I did that, I I I dropped this dependency on GDBM, and I could I could choose any license I want. Years later, SQLite's architecture independently converged on the same optimizations as Postgres SQL, a database built by the entire teams at Berkeley. Everything, the architecture, the history, the reasoning behind every decision lives in three people's heads. SQLite might be the most extreme version of that in computing history.

### 📝 セクション 52

Three people, a trillion databases and they don't accept help. So what kind of person looks at all of this and puts a frayer where the license should be? In 2018, the open source world was going through a major wave. Every major project was adopting a code of conduct, community guidelines for how contributors and maintainers should behave. It was becoming expected in every open source project.

### 💡 セクション 53

So the pressure of course came to sequel light. Richard submitted the rule of Saint Benedict, a 1,500 year old set of rules written for monks that included guidance like prefer nothing more than the love of Christ and be not addicted to wine. And the internet did what the internet does, outrage. Confusion, hot takes, think pieces. Why a prayer instead of a license?

### 🔧 セクション 54

Oh, a prayer rather than a license. Yeah. Alright. So this was in 20 of SQLite. It was just the SQL parser, and it used GDBM.

### 🎯 セクション 55

Version one of SQLite was GPL. It had to be, but no option. GDBM is a it it it's a hashing store, and I I I wanted to be able to do range queries. And for that, you need a b tree or something like that. And so I said, well, I'm gonna change the back end to something different.

### 💭 セクション 56

I looked at Berkeley DB. The documentation of Berkeley DB was such that I recognized I'm gonna have to write test programs to understand how it actually worked. So I don't hey. I'll just write my own. What?

### 📌 セクション 57

Why not? Richard's response, the idemozilla's community participation guidelines as the official code of conduct for external interactions. Fine. Done. And he renamed the rule of Saint Benedict to a code of ethics, the internal standard the developers hold themselves to.

### ✅ セクション 58

But the whole incident pulled back a curtain on something that had always been there. Where every other piece of software has a license file like the MIT, the Apache, the GPL, SQLite has this at the top of every single source file where the copyright notice should be. May you do good and not evil. May you find forgiveness for yourself and forgive others. May you share freely, never taking more than you give.

### 📚 セクション 59

At that time, there were really, there was a GPL, there was the Berkeley license, and there was the MIT license. That was it. We didn't have 5,000,000,000 different licenses like you do today. Right. And I looked at the MIT and Berkeley, and, you know, they're I mean, they're they're really open and everything.

### 🔖 セクション 60

They're great, but there's a bunch of legalese and all of the stuff. Do we need any of this? What what is the point of this? Why can't I just say public domain and be done with it? I wrote every line and code this my myself.

### 🎨 セクション 61

Let's just call it public domain. And I needed something to put in the header comment, so I came up with that cheesy blessing. So I did it that way, you know. Would I do it differently knowing than what I do now? Perhaps.

### 🚀 セクション 62

But it's worked out. Eight blessing. A prayer where a legal document should be. It's been there since the beginning and this is who Richard Hip is. A devout Christian from Charlotte who put a prayer in his source code and a monistic rule in his code of ethics.

### ⚡ セクション 63

And the entire tech industry just depends on it. But here's the thing about building a fortress, the same walls that keeps threats out also keeps progress in. In December 2018, the same year Richard submitted the rule of Saint Benedict as his code of conduct, a security team at Tencent discovered a vulnerability in SQLite. They called it Magalin, a remote code execution flaw in F t s three extension that theoretically affected every Chromium based browser on Earth. Billions of devices.

### 🌟 セクション 64

Richard's team patched it before Tencent even went public. The system worked. But then Richard got on Twitter and called the reports, greatly exaggerated. He accused the researchers of being motivated to spin it as a bigger deal than it was. And he was probably right.

### 🎬 セクション 65

There's no evidence that Megalin was ever exploited in the wild. But the image it painted, a three person team publicly waving off security researchers from one of the biggest tech companies in the world made a lot of people uncomfortable. Because there was a pattern forming. Companies asked for a code of conduct. Richard gave them a 1,500 year old rule and only added standard guidelines after the backlash forced his hand.

### 📋 セクション 66

Symbian raised the bus factor 20 ago. Still, three people. He built the t h three test suite partly hoping to sell it to avionics companies. They've sold exactly zero. The engineering was flawless but the world around SQLite kept changing and Richard's answer to every outside concern was the same answer it had always been.

### ⭐ セクション 67

I've got this. He'd even say it himself in interviews. Meanwhile, developers were building applications that SQLite was never designed for. Edge computing, serverless functions, AI workloads that need vector search and replication, features that the closed contribution model meant they couldn't add and couldn't even propose. Now it's worth saying something here, SQLite isn't completely closed to contributors.

### 📝 セクション 68

That's a common misconception. Apple has contributed code. Google has contributed. But every contribution requires meetings with lawyers, signed affidavits, documents stored in a fire safe at the office. It's not that outside code can't get in, it's that the friction is so high that most people just don't even bother trying.

### 💡 セクション 69

And for a lot of developers, they did try. One project called DQ Lite tried to contribute replication code directly to SQLite. The answer was just no. Not gonna happen. Glauber Costa has seen what he called a pile of bodies.

### 🔧 セクション 70

People who tried to contribute SQLite and failed. Costa was the CEO of a startup called Terso. He and his co founder Pekka Enberg had spent years in Linux kernel development where the entire culture was built on open contribution. Linus Torvald said Linux would never run on anything but his PC. And then thirty years of community contributions made it run on everything.

### 🎯 セクション 71

Cosa and Enberg were building a product that depended heavily on SQLite. They needed to modify it, add replication, server mode, things SQLite wasn't designed to do, and they just couldn't. So in October 2022, they made a decision. They forked SQLite. But they didn't write a single line of new code, not one.

### 💭 セクション 72

They sat down and asked themselves what is the minimum amount of code that we need to write to prove this is worth doing? And after a few days of deliberation, they had their answer, zero. They wrote a manifesto instead. A letter that said, SQLite is open source but does not accept contributions. Community improvements cannot be widely enjoyed.

### 📌 セクション 73

We want to change that. In two weeks, they had 1,500 GitHub stars. Their previous product, a year of actual engineering work, had a thousand. This thing with no code changes had 50% more interest in fourteen days. And the community had been waiting for someone to do this.

### ✅ セクション 74

They just needed someone to go first. Then a year, over 80 contributors, a proper code of conduct, an MIT license, native replication, vector search baked directly into the SQL engine, everything Richard deliberately chosen not to do. And Cosa was clear. He wasn't angry at Richard. He wasn't trying to take something from him.

### 📚 セクション 75

Two different traditions, two different answers to the same question. But Terso didn't stop at a fork. In 2024, they announced they were rewriting SQLite entirely from scratch. In Rust, a memory safe language. Not building on Richard's code anymore.

### 🔖 セクション 76

Replacing it, A clean room implementation with no ties to the original architecture. A fork still depends on the original. A rewrite depends on nothing. They wanted to control their own destiny. So now there are two versions of this story.

### 🎨 セクション 77

A man in Charlotte who spent twenty five years building something by hand, who refused outside help because every time he depended on someone else's work, it nearly cost him everything. Who was right about architecture, testing, about keeping the team small, who put a prayer in his source code and pledged to support it until 2050 which would make him 89 years old. And a team of engineers who looked at the same man and saw it with real justification that depending on him was the risk. That the fortress that he built to protect Sequelite had also frozen it in place. That the stubbornness that made it great was the stubbornness that wouldn't let it evolve.

### 🚀 セクション 78

Richard never responded publicly. Not to the manifesto, not to the fork, not to the rewrite. The most he'd ever said about the possibility was years earlier in a podcast interview. No lawsuit, no angry blog posts, no defensive Twitter thread, just silence and permission he'd given in advance because that's the whole point of public domain. That's what the blessing says.

### ⚡ セクション 79

May you share freely, never taking more than you give. And someone finally took him up on it. Everybody's doing this all the time because we're we're apparently the king of the hill. We're the ones to knock off. Every morning I wake up and and I'm thinking, this will be the last day.

### 🌟 セクション 80

Somebody's gonna come up with something better than SQLite, and the ride will be over. But it just keeps going. Mhmm. I'm gonna keep doing this as long as I'm able to. The manifesto talked about how we need to you need you need to develop software according to the the GitHub model.

### 🎬 セクション 81

If you're not doing it this way, you're doing it wrong. Turns out I get to choose how I do it myself, you know, how I how I write my own software. And that's not the way I want to do it. And if you wanna do it that way, that's fine. I enjoy doing this, and Mhmm.

### 📋 セクション 82

I don't think it would've been enjoyable if I'd spent all my days trying to deal with pull requests. Suppose you had a pull request for SQL. Hey. I've got this new feature for SQLite. Here's the pull request.

### ⭐ セクション 83

When you're wanting me to pull that into the tree, you want me to maintain it for you, to to document it for you, to test it for you, to maintain it for you for the next twenty five years. Linus Torvalds is famous famous for saying, you know, there's free as in beer and free as in speech. But there's another kind of freedom. Free as in as in puppies. Oh, look.

### 📝 セクション 84

I've got a free puppy for you. Okay? Yeah. Yep. You see where this is going?

### 💡 セクション 85

A pull request is a free puppy. Yep. And then you just got a kennel at the end of the day full of puppies. Yeah. You're just like Yeah.

### 🔧 セクション 86

And and you can't just throw them out. Okay. They're you you're you're you're morally obligated to take care of them for their natural life. Yep. I know I don't want any free puppies.

### 🎯 セクション 87

The USS Oscar Austin was commissioned in the year 2000. The same year Richard Hipp wrote the first version of Sequel Light during a government shutdown. The Navy insisted on keeping Informix. The software that was supposed to use Sequel Light never officially did. The side project that a contractor built out of frustration with a crashing database on a warship ended up on every phone, every browser, every plane, and every device that you touched.

### 💭 セクション 88

And the guy who built it, he never left Charlotte. No logo, no conference, three developers. A blessing where everyone else puts a license and a trillion databases that nobody thinks about. And then he went back to work. Subscribe if you want more stories like this.

### 📌 セクション 89

I'll leave links to all the podcast interviews with Richard and all the other sources in the description. They're worth your time. And thank you again to Richard for talking with me for about an hour. The full podcast interview is down below if you want to go see it. Thank you so much.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年05月01日

</div>
