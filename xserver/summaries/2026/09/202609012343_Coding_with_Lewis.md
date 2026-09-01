# 📺 WordPressは自らを食い潰している

## 📋 動画情報

- **タイトル**: WordPress Is Eating Itself Alive
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=AC8zIESRyVs](https://www.youtube.com/watch?v=AC8zIESRyVs)
- **動画ID**: AC8zIESRyVs
- **公開日**: 2026年09月01日 23:43
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

インターネットの40%を動かすソフトウェアが、なぜ数か月で信頼を失ったのか。2003年5月27日にb2/cafelogのフォークとして公開されたWordPressが、20年かけてWebの標準CMSになるまでと、2024年の90日でそれを損なうまでを追った動画です。  
普及の転機は2004年、Movable Type 3.0が無料ユーザーに約70〜200ドルのライセンス料を課したこと。その月に8,000だったWordPressのダウンロードは翌月2万近くへ跳ね上がりました。  
2024年9月20日のWordCamp USでMatt MullenwegがWP Engineを寄生的な存在だと名指しし、翌日には「WordPressのがん」と書きます。wordpress.orgがWP Engineを遮断し、人気プラグインACFをSecure Custom Fieldsとしてフォークし、ログイン時に宣誓のチェックボックスを求めるところまで進みました。  
結果としてWP Engineは提訴して仮差止命令を勝ち取り、Automatticでは159人が退職。オープンソースへの貢献時間は週4,000時間近くから45時間へ削られ、市場シェアも6四半期連続で低下しています。

## ⭐ 重要なポイント

- WordPressは2003年5月27日、Matt Mullenwegと「Mike」と名乗るユーザーによるb2/cafelogのフォークとして公開された。翌2004年にMovable Type 3.0が無料ユーザーへ約70〜200ドル（今の価値で120〜350ドル）のライセンス料を課したことで、その月8,000だったダウンロードが翌月には約2万へ急増し、一気に広まった。  
- 「WordPress」は4つの別物を指す。GPLのソフトウェア本体、更新やプラグイン配布を担うwordpress.org、商標を持つ非営利のWordPress Foundation、そして2005年設立の営利企業Automattic。2010年にAutomatticは商標を財団へ移管したが、同時に財団は商用権を事実上永久にAutomatticへ独占ライセンスし直しており、3つの権力の中心の頂点には結局一人の人物がいた。  
- 2024年9月20日、ポートランドのWordCamp USのキーノートでMattはWP Engineを寄生的だと名指しし、Five for the Futureの貢献時間をAutomatticの週3,786時間に対しWP Engineは47時間だと比較した。翌日のwordpress.orgの投稿ではWP Engineを「WordPressのがん」と表現。その1年半前のDECODEでは逆に「WP Engineのような会社を支持しよう」と語っていた。  
- 対抗措置は利用者を直撃した。wordpress.orgがWP Engineを遮断して更新経路が止まり、200万以上のサイトで動いていたAdvanced Custom Fieldsが公式ディレクトリ側でSecure Custom Fieldsとしてフォークされ、インストールした覚えのないプラグインが客先サイトに現れた。ログインには「WP Engineとは一切関係がない」という宣誓チェックボックスが要求された。キーノートから3か月弱で連邦地裁が仮差止命令を出し、72時間以内にアクセス復旧・チェックボックス撤去・ACFの返還を命じた。  
- 代償は大きい。方針に同意しないAutomattic社員159人（8.4%）が3万ドルまたは給与6か月分のいずれか高い方を受け取って退職し、16年間日本語ロケールマネージャーを務めたNaoko Takanoもその一人だった。Automatticのオープンソースへの貢献は週4,000時間近くから45時間へ削減され、REST APIを率いたRyan McCueらはLinux Foundationの下でFair Package Managerを立ち上げた。2026年7月時点でシェアは6四半期連続で低下して41.5%（2025年12月は43%）、BlackRockによるAutomattic株の評価も85ドルから27.74ドルへ下がっている。

## 📖 詳細内容

### 🎬 導入

How does software that powers 40% of the internet lose so much of its trust >> [music] >> in just a few months? >> What you've done is so immensely unpopular. >> We're trying to make this like a WordPress is trouble or something. >> WordPress [music] spent about 20 years becoming the default open CMS of the web, but it took about 90 days in 2024 for a large loud slice of that community to stop trusting the man who steered it. The people who built for a living, agencies, plugin developers, hosts, the ones who have to bet a business on the update buttons still working next Friday.

### 📋 背景・概要

[music] Here's how WordPress took over the world and then lost all of its trust in 90 days. >> [music] >> It's 2003. The internet has taken off worldwide and everyone wanted a piece of real estate. One issue though, there wasn't a simple deploy button. Personal sites meant static files on a server, which was very [music] slow, fragile, and had to be rebuilt every time that you made an edit.

### ⭐ 主要ポイント

And this is the problem that B2 was trying to solve. Posts, comments, metadata in a database, pages generated on the fly. No [music] huge publish queue. People had their complaints and one of them was Matt Mullenweg. Matt started publishing on his blog around the end of 1999, camera galleries, and then shorter tweet-like posts.

### 📝 詳細説明

Don't you hate it when you're working on a really nice post through the web interface and you lose it? Bah humbug. And after posting a while, his blog got popular. Hundreds and hundreds of posts and the scaffolding started to crack and it showed. And so that's when he published the blogging software dilemma.

### 💡 実例・デモ

Fork compatibility has lately been in my mind more. My blogging software hasn't been updated for months and the main developer has disappeared [music] and I hope that he's okay. Fortunately, b2 Cafe Log is GPL, which means I could use the existing [music] codebase to create a fork. It would be nice to have the flexibility of Movable Type, the parsing of text [music] pattern, the hackability of b2 and the ease of setup of Blogger [music] someday, right? But then a comment from user named Mike, "If you're serious about forking b2, I'd be interested in contributing." And [music] just like that, the way that we published on the internet changed forever.

### 🔧 技術的詳細

4 months of public hack logs later, on May 27, 2003, WordPress was available to download. Early comments were looking really promising as well. But slow growth and, you know, not a breakout yet, but it would take something big to move a wave of users in just one go like that. That something big was when one of the leaders in this area rug pulls their own users. 1 year after WordPress launched, Six Apart or Movable Type released version 3.0 with features people wanted and [music] forced free users into licensing fees.

### 🎯 応用例

So, personal sites, which was what a lot of people were using at the time, were hitting a licensing wizard. [music] Tiers running from about $70 up to $200 depending [music] on how many blogs and authors that you had. So, maybe like $120 to $350 in today's money [music] just to keep a website up, um a personal website. And so of course, people flocked. The easiest [music] door that month was a trendy project called WordPress.

### 💭 考察

>> [music] >> The month before that happened, only about 8,000 total downloads happened with WordPress, [music] but after this almost 20,000, and the user base exploded. WordPress wasn't the [music] superior product yet, not by a long shot, but it had the best foot in the door. [music] It was free, and for months Matt and Mike just shipped what these migrants were looking for. On a blog post addressing this [music] migration, Jeff comments, "Well, you could always start screwing this up. Don't go buying a bigger hut anytime soon." In October of 2004, Matt moved to San Francisco and started [music] at CNET part-time to work on WordPress, but then came version 1.5, Strayhorn, which is [music] kind of how we see it today almost.

### 📌 まとめ

Themes, pages, dashboard. 2 weeks after release, they had over 50,000 downloads. 3 weeks after that, [music] 100,000. They threw a party in San Francisco for it. It was a big deal.

### ✅ 結論

In 2004, that already felt like a one-click home on the internet. It was the closest [music] thing to it, and you owned the whole thing. Publishing was being democratized. Nobody could pull the plug on you like [music] a paid license just had. But, there was also a huge issue here.

### 📚 追加情報

WordPress was absorbing a huge audience of users who left specifically because of a paid option. So, Matt wasn't just [music] maintaining software anymore. He was holding a movement that said the right to publish should stay open for everyone. How do you free the world of publishing, but make money off of it at the same time? Now, selling licenses for the code is off the table.

### 🔖 補足

That's what made people move from Movable Type and show up here. A donate button wasn't going to fund the servers, [music] full-time work, or basically anything close to what a real company would need. [music] So, Matt tried a different route. In 2005, he started a company called Automattic and built wordpress.com. WordPress, the free [music] software, stayed free.

### 🎨 セクション 13

Anyone could still download it from the internet with no strings attached. Wordpress.com, however, was something [music] else. It was the same engine under the hood. Automattic ran the servers, [music] and you could pay a monthly fee for the easy button hosting convenience, not a pay license for the code itself. And so, over the years, Automattic fills roles [music] with people who thought the job was the movement.

### 🚀 セクション 14

We have translators, program managers, contributor folks, the unglamorous backend behind >> [music] >> WordCamps and democratizing publishing. These roles were being filled. And one of them is Naoko Takano. She found WordPress in the mid-2000s [music] and started translating it for free because there was almost nothing written about WordPress in Japanese. [music] And so, in 2008, she became the Japanese locale manager [music] for over 16 years.

### ⚡ セクション 15

That same year, she organized her first WordCamp in Japan [music] and kept organizing them for basically another decade. If you've ever loaded WordPress in [music] Japanese, you have used something that she gave the project before anyone paid her to do it. And so, Automattic hired her in [music] 2010. Polyglots community team, the volunteers who make WordPress speak every language it speaks. The quiet half of the machine.

### 🌟 セクション 16

>> [music] >> Back in 2005, though, before the company era had even really settled, Matt already learned how ugly money gets when it touches the comments. [music] A company called Hot Nacho paid to park around 160,000 articles on wordpress.org, the project's own site. Users noticed pretty fast that some was off. Fluffed up pages, SEO sludge, keywords hidden against the background, [music] links pushed off screen, so regular visitors wouldn't see them. And so, when it blew, well, it blew loudly.

### 🎬 セクション 17

Tech press, mainstream [music] coverage, Google stripped wordpress.org of its page rank and pulled it out of the index. The site was back within about a day, but the point had been made. People asked the question that never really left. Is this an open source project, [music] or is it a company? Matt eventually wrote a long apology on his blog.

### 📋 セクション 18

He took the pages down [music] and called it a badly run experiment. He was still riding the scene on stretcher on then. Company brand and project brand already getting tangled in public opinion. And to be fair to Matt, you know, this was an early way of trying to monetize [music] this. So, it is what it is.

### ⭐ セクション 19

WordPress kept growing anyway, though. Hundreds of thousands of installs, [music] then millions. Automattic grew with it. In 2006, the company filed for the [music] WordPress trademark. In 2008, it raised a real venture round, tens of millions.

### 📝 セクション 20

[music] The kind of check that investors write when software is already living on a scary amount of websites. And then, in 2010, Matt did something that looked completely insane. >> WordPress has grown a huge, huge amount. And so, I think it's time we're going to try something different. >> up a nonprofit called the WordPress Foundation, and Automattic transferred the WordPress trademark to it.

### 💡 セクション 21

The public pitch was clean. The name should live past any one company. WordPress should remain a beacon even if Automattic changed. The community praised him. Getting rid of one of the biggest assets for the sake of the cause is something insane.

### 🔧 セクション 22

No one would ever think about doing it. The contract was smarter than a gift. So, when people say WordPress, they mean like four or five different things here. One, the software. Free, GPL, download it, fork it, sell services around it.

### 🎯 セクション 23

Nobody owns the code the way that you own a product in a box. It just simply is there. Two is wordpress.org. Now, this is kind of like the the pipes underneath, the downloads, the plugin directory, the theme directory, the default update path half the internet leans on without even thinking. Three is the WordPress Foundation that we just mentioned.

### 💭 セクション 24

This is the nonprofit that [music] holds the name, the trademark, the legal doodad that says we can brand something as WordPress. And four is automatic, which is the for-profit company from 2005. This is like wordpress.com, which later was WordPress VIP for enterprise, WooCommerce, a big pile of apps. The company that makes money around the free WordPress. And so, in September of 2010, [music] automatic transferred the trademark to the foundation.

### 📌 セクション 25

And the foundation licensed the commercial rights back to automatic, exclusive, effectively forever, with automatic deciding who else gets a commercial seat at that table. So, here we have non-commercial which lives in one pocket, and the money lives in the other. So, in practice here, we have free software, project infrastructure, a nonprofit brand deed, and a commercial gate. And for a long, long time, if you asked who was really in charge of any of that, it was still [music] Matt. Three power centers, but one man.

### ✅ セクション 26

What could go wrong? >> Even if >> [music] >> you know, I I grew devil horns and became evil and automatic decided to know, you know, whatever, WordPress would still belong just as much to you as it would to me. You can still own it. You can still build on top of it. So, >> [music] >> those things I think are uh yeah, really important.

### 📚 セクション 27

Now, just like all great open source software, people use it to build businesses on top of it. In 2010, Jason Cohen had already founded and sold a company called SmartBear. His blog, a SmartBear, kept failing over under traffic. WordPress was extremely popular even at this time, but it quickly built a reputation for constant updates, hacks, and sluggishness. Maybe due to the popularity, it maybe due to the actual software around it.

### 🔖 セクション 28

So, in 2010, he built his own solution called WP Engine. And he had about 30 customers right at launch. Then, a bunch of agencies who had hundreds of websites needing reliability, who were happy to pay big bucks doing it. Set it and forget it. This target demographic was perfect for the kind of website [music] that WordPress businesses wanted.

### 🎨 セクション 29

Something you can push and not worry about while collecting a monthly [music] fee for their clients. Again, the markup here for the agencies was it didn't even make any sense. So, in 2011, Automattic themselves invested [music] in WP Engine. Matt has talked about Jason in positive terms. This looks like something that the WordPress ecosystem was supportive of.

### 🚀 セクション 30

Free software builds million-dollar [music] businesses. In 2013, Jason hands the CEO job to Heather [music] Brunner and moves himself to the Chief Technology Officer so he can go back to building things [music] as developers just love doing. She came out of Bazaarvoice, where she'd been the COO. 40 people with 7,000 [music] customers. WP Engine continued to grow, but something that threw people a bit in the wrong direction was in January of 2018, when they announced that Silver [music] Lake, the private equity firm, invested about $250 million into to Engine.

### ⚡ セクション 31

This would give them a majority stake with three board seats. One of those board seats [music] goes to a guy named Lee Wintlinger. And a lot of people were concerned, [music] but the product didn't flip overnight. Jason was still around as the CTO. Heather was still the CEO.

### 🌟 セクション 32

They've been there for this whole time. But above both of them, the people in charge [music] were no longer the people with the original mission in mind. But people were still happy, and business just went on as usual. But the world of WordPress competition was ramping up hard. GoDaddy, WP Engine, [music] Wix, Squarespace, these were huge companies taking actual big chunks out of WordPress's pie.

### 🎬 セクション 33

Whether that be the open-source versions or the [music] paid product. So, that's when Matt raises about $288 million in 2021, putting Automattic's valuation around $7.5 [music] billion, led by BlackRock. And the competition was clear. Matt had one of the biggest names in internet history, as well as hundreds of millions of dollars that could be deployed. With a reputation as well for being the one to save the internet, how was he going to do any of this?

### 📋 セクション 34

>> [music] [music] >> In June of 2022, Matt tweeted that GoDaddy was a parasitic company and an existential threat to WordPress's future. His claim here was that GoDaddy [music] makes hundreds of millions of dollars off of WordPress-related products and doesn't put enough hours back into making the project better. GoDaddy responded with canned text, essentially. "We all want WordPress [music] better every day. We contribute roles, projects, passion, people.

### ⭐ セクション 35

We spend hundreds of thousands sponsoring WordCamps and events." Matt eventually deleted the tweets. The GoDaddy drama faded and was basically forgotten about. But, the template did it. Name a host, count their hours, call them whatever you want. And so, in March of 2023, WP Engine's developer conference, DECODE, Matt says explicitly, >> When you support companies like a WP Engine, who are don't just provide a commercial service, but are also part of a wider open-source community, cuz so much of whatever you spend in the WordPress ecosystem gets reinvested back into the thing that again you own.

### 📝 セクション 36

So, it's like everyone's a shareholder in WordPress, because we all have the fruits of of the labor. >> I love that, Matt. It's it's so true. >> a voice that seemed to be emerging out of Matt Cutts at this time. Rather than it being a liberated type of feeling, it was now more about defeating the takers of WordPress.

### 💡 セクション 37

Behind the scenes here, by Automattic's own account of it, they were asking that if you're going to be making serious money off of WordPress's name and gravity, you pay for a commercial relationship. WP Engine side basically lived on years of WP branding, plus lawyers who thought the foundation's own old WP is fine five still protected them essentially. But, Matt's side says he spent 18 months feeling gaslit. WP Engine says he was rewriting the rules with a competitor's fingerprint on the pen. And after what Matt describes as 18 months of back and forth with private equity, his side decided it wasn't going anywhere.

### 🔧 セクション 38

So, Matt decided to use everything in his own favor. September 20th, 2024. WordCamp US, Oregon Convention Center in Portland. This is the big annual family reunion for the WordPress industrial complex. [music] Agencies, hosts, freelancers, plug-in people, the folks who built careers [music] on democratizing publishing.

### 🎯 セクション 39

This was the community half of it, not the private equity side. And so, everyone gathered around the main stage to hear Matt's keynote [music] speech. And then, Matt walks on stage. >> Hey everybody. Good to see you all.

### 💭 セクション 40

This might be one of my spiciest WordCamp presentations ever. So, we'll see. >> In the presentation, he talks about nourish. It's where you water the garden. >> Like learn, evolve, nourish, teach.

### 📌 セクション 41

Spells out lint. >> But, then he talks about >> specific parasitic entities that just want to feed off the host without giving [music] anything back. And there are those that treat open source simply as a resource to extract from its natural surroundings, like oil from the ground. Compare the five for the future pages from Automatic and WP [music] Engine. Automatic has 3,786 hours per week.

### ✅ セクション 42

WP Engine has 47 hours listed. Uh, that's actually gone down since I wrote this. >> But, then he starts targeting actual people. >> Who's the person behind all this? His name's Lee Widdlinger.

### 📚 セクション 43

And he's on the board of WP Engine. He owns WP Engine. Actually, they control it. Um, he's also on the board of another company that's here. When there's like one person, one thing behind all of this.

### 🔖 セクション 44

And >> [music] >> um, it's just like a schoolyard bully. >> The presentation was styled like an us against them, us against the man, the ones that want to take everything from you. But, the immediate audience reception was mixed to say the least. >> When we name and shame, I want to know from a leadership perspective, >> [music] >> have we gone to the top leaders that you've shared, and have you tried to work channels without it becoming an incident? >> I want to thank you in person for your, honestly, for your braveness.

### 🎨 セクション 45

You've been my [music] inspiration for more than 10 years. >> Well, I think it's a valid criticism for someone to be making a ton of money off of >> [music] >> a freely available resource without contributing back. What you said in your presentation sounded like you were blaming all the downfall on one person. >> And then the next day, Matt posted on the wordpress.org, the foundation blog, WP Engine is not WordPress. In his post, he summarizes [music] what he mentioned the day prior at his keynote.

### 🚀 セクション 46

But, he also calls WP [music] Engine a cancer to WordPress. And it's important to remember that unchecked cancer will spread. And that's why people were confused because just a year and a half earlier, Matt was telling you to >> support companies like a WP Engine. So, when you give your dollars there versus like, you know, Wix or Shopify, when these proprietary things, you're uh saying like, "Hey, I want more of this in the world." >> And the internet goes out of control. The things people are saying about the guy behind WordPress right now are absolutely brutal.

### ⚡ セクション 47

He has main character syndrome, a cancer to his own community. He's getting into more and more trouble day by day. >> Matt Mullenweg called WP Engine a cancer to WordPress last week. >> I wasn't ready for this one. >> If I called myself like Nike Engine or something like that and had like a shoe thing, I probably owe a little bit of money at least to Nike corporate shoe >> is optically, publicly, this was very sudden.

### 🌟 セクション 48

And even internally, privately, the switch was very sudden. >> Three days later, WP Engine pushes a cease and desist to Automattic and posts it publicly. In there, some interesting claims were being made. Mullenweg threatened that if WP Engine did not agree to pay Automattic his for-profit entity a very large sum of money before his September 20th keynote address at the WordCamp US convention, he was going to embark on a self-described scorched-earth nuclear approach towards WP Engine within the WordPress community and beyond, as well as text messages that were allegedly sent from Matt to Heather Brunner and a WP Engine board member through the night of the 19th and the morning of the 20th. I'm literally waiting for them to finish the raffle so my talk can start.

### 🎬 セクション 49

I can make it just a Q&A about WP [music] very easily. Heather offers to get on a call the following week, a business conversation. But Matt says no, and then minutes before he goes on, he sends her a photo of the crowd sitting in that room waiting for him. >> WP Engine has good people, some of whom are listed on that page. The company is controlled by Silver Lake, a private equity firm with 102 billion in assets under [music] management.

### 📋 セクション 50

Silver Lake doesn't give a dang about your open source ideals. It just wants return on capital. So, it's at this point that I ask everyone in the WordPress community to go vote with your wallet. Who are you giving your money to? Someone who's going to nourish the ecosystem, or someone who's going [music] to frack every bit of value out of it until it withers?

### ⭐ セクション 51

>> So, in response to the blog post, WP Engine disabled the wordpress.org news feed that shows you by default in your admin [music] panel, considering their users would see it and panic. The same day, Automattic fired back with their own cease and desist [music] about how WP Engine violated the WordPress trademark. Then, wordpress.org bans WP Engine from their services completely. Matt posts a post on the wordpress.org blog. Any WP Engine customers having trouble with their sites should contact WP Engine support and ask them to fix it.

### 📝 セクション 52

And Matt claims that WP Engine broke thousands of customers' websites when trying to block the news widget, and that aren't paying for a license. And then, this. WP Engine is free to offer their hacked-up bastardized simulacra of WordPress's GPL code to their customers, >> [music] >> and they can experience WordPress as WP Engine envisions it, with them getting all of the profits and providing all of the services. Now, whether or not Matt is correct, this is Matt's voice, [music] and it's being used in the channel that is only supposed to speak objectively for the WordPress community. But instead, we're all hearing the licensing wizard just reversed.

### 💡 セクション 53

So, plugin installs and updates through the normal wordpress.org path, you know, aka the invisible oxygen pipe, it completely broke for WP Engine's world. Sites didn't disappear. Security debt and update red lights did. That's when people realized that >> [music] >> there was a valve to begin with. And businesses and agencies with client sites didn't really care who won the private equity sermon.

### 🔧 セクション 54

They cared that Friday's employees turned into the risk memos. And then WP Engine sued Automattic and Matt personally. Trademark abuse, attempted extortion, anti-competitive [music] practices. They'd add antitrust claims later, but Automattic says it's completely meritless. On October 3rd, he posted [music] on his personal blog, Automattic Alignment.

### 🎯 セクション 55

There he talks about the lawsuit and that a good chunk of people at Automattic have disagreed with Matt on the actions taken. So, we offered those who resigned $30,000 or 6 months of salary, >> [music] >> whichever was higher. And 8.4% of the company took that offer. 159 people walked. And one of them is Naoko Takano.

### 💭 セクション 56

On the way home from WordCamp US, right after the spicy talk circus, she decided that she was [music] done. She puts it on her own blog. Clean, short, not a rage threat. I'm resigning because I'm not aligned with the recent strategic decision taken by Matt and the conflict with WP Engine. We have obviously the evil corporations, you know, David versus Goliath, but we have the builders of the actual movement looking at their own reflection and deciding not to march along with the rest of the group.

### 📌 セクション 57

But about a week later, they would do something that would make the community not trust them one bit. Advanced Custom Fields or ACF is one of the most popular plugins ever on WordPress. If you don't know about it, well, you just simply didn't use WordPress. It's as easy as that. But ACF lets developers or site [music] owners create custom fields on the post that they were making.

### ✅ セクション 58

So, if you had a pizza restaurant theme, I can have a pizza toppings field that is queryable rather than a standard blog title and body. WP Engine bought the company behind ACF years prior, but it was running on over 2 million active sites. So, [music] wordpress.org forked free ACF and renamed it to Secure Custom Fields >> [music] >> and took the official directory seal. So, anyone still taking the updates from the default >> [music] >> wordpress.org would wake up on another maintainer's package installed on their machine. And if you're a developer of any sort and you wake up and see something that you did not install, well, you panic.

### 📚 セクション 59

And this is one of the only times that they've ever done this in their history of operation. And for a lot of people, this was the first time the fight showed up inside their own job. The repository reported agency owners spending that weekend on unscheduled maintenance across hundreds of client sites fixing things that broke on an update nobody asked for. One of them put it in a comment on WP Tavern. They logged into client sites and found a SCF plugin that we never installed.

### 🔖 セクション 60

And nobody at that agency had an opinion about the trademark law. They were just there because it was Monday. But many people were thinking of completely porting their websites to a brand new provider or even rebuilding around it. >> [music] >> But around the same stretch when people logged into wordpress.org, they had to check a box. I am not affiliated with WP Engine in any way, financially or otherwise.

### 🎨 セクション 61

A required oath on your front door essentially. And it was at this point where it was unclear what the true motivations were. The fight wasn't only private equity versus the founder anymore. Alignment paid automatic employees to walk, including people like Naoko who still believe in the licenses and still refused the strategy. The dot org login asked the world for an oath.

### 🚀 セクション 62

Advanced custom fields taught agencies that their update button had a landlord. And Matt wasn't only fighting WP Engine here. He was stress testing everyone who still needed the pipe. Just under 3 months after the keynote, a federal judge told Matt to put everything back. WP Engine got a preliminary injunction.

### ⚡ セクション 63

Restore the wordpress.org access. Drop the login checkbox. And back ACF. And do it all within 72 hours. And so automatic says it's just temporary and that it will be resolved in court.

### 🌟 セクション 64

Matt posts, "I'm disgusted and sickened by being legally forced to provide free labor and services to WP Engine." 10 days later, a holiday break was announced. wordpress.org would shut down. New plugin, [music] theme, and photo submissions, plus new account restrictions would just completely be off for that time. WP Engine kept their access. The court order that they just made made sure of that.

### 🎬 セクション 65

And after this, automatic published a post called aligning [music] automatic sponsor contributions to WordPress. Automaticians, which I guess that's what it's called, who worked on WordPress core would be pushed onto four-profit products >> [music] >> instead. wordpress.com, Pressable, WP VIP, Jetpack, WooCommerce, and the company would [music] contribute only 45 hours a week to the open source project. And before that, it had been just under 4,000 hours. >> [music] >> Matt being Matt, he just straight up said, "Why?

### 📋 セクション 66

Our number one goal is for WP Engine to drop [music] their expensive lawsuits." And around the same time, Matt would go on Reddit and ask people what drama he should stir up. But, where things started crumbling was about 5 months later. A group of WordPress veterans, including Ryan McCue, who led the WordPress REST API, launched the Fair package manager under the Linux Foundation. This would replace the dependence of wordpress.org for updates. The Linux Foundation maintained other open-source projects that came out of the lack of trust of the original maintainer, like Open Tofu, Valkyrie, and Open Search.

### ⭐ セクション 67

WordPress was now added to that list. Now, let's look at some numbers real quick. I'm recording this video in July of 2026. So, if you're watching this later, you know, you can check these for yourself. But, WordPress has gone through six consecutive quarters of declining market share.

### 📝 セクション 68

Whenever you hear about WordPress, it's always the same stat: 43% of the web is powered by WordPress. And that was true in December of 2025, but today it's 41.5. Now, can we attribute this to the WordPress [music] fiasco? Well, probably not, to be honest. I wouldn't be surprised if 95% of [music] WordPress users never even heard about it to begin with.

### 💡 セクション 69

People are flocking to existing services like Shopify or Wix. Or what's [music] really kind of shocking in the data, none. No CMS is growing. BlackRock, the company that led the $288 million funding round for Automatic, valued it at $85 per share >> [music] >> at the time. But, as of June 30th, 2025, it valued it at only $27.74 per share.

### 🔧 セクション 70

AI has made people skeptical of written content, something that WordPress literally [music] built his entire business on. On May 27th of this year, WordPress turned 23 years old, older than some of you probably. [music] Matt posted on wordpress.org a post called WP23. At first, he acknowledges everyone who [music] had worked over the years and how proud he is. But, then he spends the next three quarters of the article talking about developments [music] in this dispute.

### 🎯 セクション 71

But, this time though, it's coming off as a little bit desperate. I have colleagues literally dying. I can't be [music] with because Silver Lake, Quinn Emanuel, and WP Engine is trying to make it seem like I am hiding or destroying evidence because we rotate logs on wordpress.org or I have disappearing [music] chats on Signal with romantic partners. Closing the whole thing off with, "You have so much money and power, you don't need to control and take over WordPress, too. If you win, you destroy it.

### 💭 セクション 72

And then what? Please have mercy and stop trying to ruin people's lives. >> [music] >> Let's move on." And whether you buy this submission or not, this isn't garden variety Matt anymore. It's a defendant [music] fighting a multi-year trench from the blog of the project he still helps define. It's easy to look at Matt and see someone with a lot of money acting out on the internet.

### 📌 セクション 73

But, sadly, this is a story that keeps getting retold over and over and over again [music] in the world of software. And it's like we're stuck in an infinite loop. How do you get paid to make software for [music] people while also giving out the source code unconditionally? We've seen this happen with Redis. March 2024, they dropped the open source license.

### ✅ セクション 74

Eight days later, Amazon, Google, and Oracle forked [music] the last free version into Valkey. A year after that, Redis quietly goes [music] back to open source. They lost the fight and the fork outlived the reason for it. Terraform, same script. Elasticsearch, same script.

### 📚 セクション 75

It's tempting [music] to turn this into a capitalism lecture, you know, just as us YouTube millennials like to do it. But, forget about it. We're inside the system either way. The same loop, but a different logo. I genuinely believe that two things can be true at the same time.

### 🔖 セクション 76

Matt wanted to create a large profitable [music] business, and he wanted to democratize publishing for everyone. But, he almost runs [music] into two different moral dilemmas. He needs to get paid to make free software for everyone, and he needs to get paid to make publishing free for everyone. And not only [music] do people not pay you, people make money off of you and your free thing. And they try to find a way to replace you at the same time.

### 🎨 セクション 77

So, when a cloud provider creates a Redis compatible [music] closed-source database, you're digging your own grave for their own gain. And when companies [music] try to do something about it, they're the ones that lose trust, while the companies taking everything absorb the same sentiment that they've always had. So, why even try to hide it at that point? And [music] maybe that's what Matt was doing. Matt had just too much to lose.

### 🚀 セクション 78

WordPress [music] wasn't just open-source software, it was a movement. So, if every angle [music] he took would lead to the failure of the mission or hate from his supporters, well, why not just be the bad guy for once and [music] see where that takes you. A week before that WP 23 post, WordPress 7.0 shipped. Inside of 7 days, 46% of installs had already auto-updated. Tens of millions of sites.

### ⚡ セクション 79

Every hosting environment that you can think of from like a Raspberry Pi >> [music] >> to the White House government website, nothing broke. No supply chain attack, basically nothing. The software works perfectly. The fall, if you want [music] to call it that, wasn't just one site going dark, it was quieter than that. People who build for a living stopped assuming that the steward and the commons were the same thing.

### 🌟 セクション 80

Some of them said it with a lawsuit, some with a plugin fork, some like Neoko with a short blog post and a badge left on the table, still believing in the licenses, but not aligned [music] with the fight. Thanks for watching. >> [music] [music] >> Mhm.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年09月02日

</div>
