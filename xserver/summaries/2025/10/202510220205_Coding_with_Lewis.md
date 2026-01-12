# 📺 AWS大規模障害の全容解説 ☁️

## 📋 動画情報

- **タイトル**: The AWS Outage EXPLAINED ☁️
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=d911naXJhKU](https://www.youtube.com/watch?v=d911naXJhKU)
- **動画ID**: d911naXJhKU
- **公開日**: 2025年10月22日 02:05
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画では、Amazon Web Services (AWS)で発生した大規模障害について解説しています。US-East-1リージョンでDNS解決の問題が発生し、Snapchat、Fortnite、Reddit、Roblox、Amazonなど、多数の主要サービスが約2時間にわたって影響を受けました。DNS（ドメインネームシステム）は「インターネットの電話帳」とも呼ばれ、その障害がいかに広範囲に影響を及ぼすかを実例とともに説明しています。クラウドサービスへの過度な依存のリスクについても言及しています。

## ⭐ 重要なポイント

- **DNS障害が原因**: 「It's always DNS（いつもDNSが原因）」という格言通り、ドメインネームシステムの解決エラーによって大規模障害が発生しました
- **DynamoDB への影響**: AWSの高速NoSQLデータベースであるDynamoDBがエラーを起こし、「橋を支える主要な柱」のように多くのサービスが連鎖的にダウンしました
- **影響を受けた主要サービス**: Snapchat、Fortnite、Reddit、Roblox、Amazon本体など、数十億のユーザーに影響が及びました
- **「大きすぎて潰れない」という幻想**: AWSのような巨大インフラでも障害は起こりうるため、自社サーバーの検討や冗長化の重要性が再認識されました

## 📖 詳細内容

### 🎬 導入

Half of the internet went offline yesterday. Here's what happened. Amazon Web Services, aka AWS, had an outage in the US East1 region due to DNS issues. More on that in a second. But because everyone relies on AWS to power everything in their applications, everything went down like Snapchat, Fortnite, Reddit, Roblox, Amazon.

### 📋 背景・概要

You know what? Maybe it was a good thing it went down to be honest. Around midnight Pacific time, they started investigating errors with Dynamo DB. And around two hours later, they identified DNS resolution issues causing the errors. It's always DNS.

### ⭐ 主要ポイント

It's always DNS. Domain name system is like the internet phone book explaining where everything is on the internet. I type in example.com. My browser then goes to that and knows how to connect to the server. But what happens when that just stops working?

### 📝 詳細説明

Well, it just says nope. Now, imagine billions of nopes. Dynamo DB is a fast NoSQL database that can have many use cases for different companies, but it's very important. Think of it as a main pillar holding up a gigantic bridge. If that falls, most likely it's bringing a lot of things with it.

### 💡 実例・デモ

And this is where sometimes we think that things are too big to fail until it happens. Then you have to realize I have to get my own server. What are your thoughts?

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年01月12日

</div>
