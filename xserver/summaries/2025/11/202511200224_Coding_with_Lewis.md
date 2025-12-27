# 📺 Cloudflare大規模障害の全貌解説

## 📋 動画情報

- **タイトル**: The Cloudflare Outage EXPLAINED
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=M-qMklGGFLU](https://www.youtube.com/watch?v=M-qMklGGFLU)
- **動画ID**: M-qMklGGFLU
- **公開日**: 2025年11月20日 02:24
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画では、インターネット全体の約3分の1に影響を与えたCloudflareの大規模障害について詳しく解説されています。2025年11月20日午前11時30分頃から発生した障害は、データベースのパーミッション変更が原因で、フィーチャーファイルが肥大化しサーバーがクラッシュした技術的なトラブルでした。Cloudflareの透明性のあるポストモーテムの重要性や、CDN・リバースプロキシの仕組みについても触れられており、インフラエンジニアやWeb開発者にとって貴重な学びが得られる内容です。

## ⭐ 重要なポイント

- **影響範囲**: インターネット全体の約3分の1に影響を与える大規模障害で、ほぼ全てのアプリとウェブサイトが停止
- **障害の原因**: データベースのパーミッション変更により、フィーチャーファイル（ボット防御用）に重複エントリが大量発生し、サイズ制限を超過
- **復旧までの時間**: 11:48に障害報告、約1時間半後に原因特定、さらに1時間後にサービス復旧開始
- **Cloudflareの役割**: CDN（コンテンツデリバリーネットワーク）とリバースプロキシで、多くの企業のWebサイト高速化と攻撃防御を担当
- **透明性の重要性**: Cloudflareが詳細なポストモーテムを公開し、何が起きたのか、なぜ起きたのかを明確に説明した点が評価される

## 📖 詳細内容

### 🎬 導入

Almost a third of the internet went down yesterday. Here's what happened. Around 11:30 a.m., people started noticing that their apps and websites just stopped working. And it wasn't just one website. It was like almost all of them.

### 📋 背景・概要

11:48 Cloudflare reports that it's experiencing service outages. Cloudflare is used by a lot of tech companies. One of their most popular services is the content delivery network or reverse proxy, which helps deliver websites faster and protects from attacks. But about an hour and a half later, they identified the issue. But what happened?

### ⭐ 主要ポイント

One of their databases had a permission change, which caused the database to duplicate entries into something called a feature file, which is used to protect your websites from bots. This was then deployed to all machines in their global network. And the software used on their servers used this file to keep up to date with attacks, but had a size limit. But the database that changed permissions pushed that way over the limit, causing everything to crash. And so about an hour later, they stopped the bad file and then eventually service started recovering again.

### 📝 詳細説明

This was one of the worst outages since 2019. And it's awesome that Cloudflare was able to do a postmortem about it, saying what happened and why it

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2025年12月28日

</div>
