# 📺 Steamはどうやって膨大なダウンロード量を捌いているのか 🕹️

## 📋 動画情報

- **タイトル**: How Steam handles an INSANE amount of downloads 🕹️
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=suIfWt89z0E](https://www.youtube.com/watch?v=suIfWt89z0E)
- **動画ID**: suIfWt89z0E
- **公開日**: 2026年03月26日 02:20
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画では、ゲーム配信プラットフォームSteamが通常日に毎秒20テラバイト以上のゲームデータを配信する仕組みを、エンジニアリングの視点から解説しています。Steamのコンテンツ配信は、1MBチャンク分割・複数サーバーへの並列接続・差分ダウンロードという3つの技術で成り立っています。2002年にValveが自社ゲームのパッチ配布ツールとして始まったSteamが、今やインターネット最大級のコンテンツ配信ネットワークに成長した背景も紹介されます。システム設計やネットワーク技術に興味のあるエンジニア・学生にとって、実際のサービスを事例にした学びが得られます。

## ⭐ 重要なポイント

- **毎秒20TB超のゲームデータを配信**：Steamは世界最大級のコンテンツ配信ネットワーク（CDN）のひとつとして機能している
- **1MBチャンク分割と6接続の並列ダウンロード**：自社サーバーとCloudflareなどを組み合わせ、帯域を最大限に活用
- **gitのdiffに似た差分アップデート方式**：パッチ適用時は変更があったチャンクのみダウンロードするため、更新が高速・効率的
- **ダウンロードのボトルネックはI/O**：HDDでは遅いが、SSDなら非常に高速にチャンクを処理できる
- **2002年の自社パッチツールから始まったSteam**：当初はValve自身のゲーム更新用だったが、現在はインターネット全体でも屈指の巨大CDNに成長

## 📖 詳細内容

### 🎬 導入

Steam pushes over 20 terabytes of game downloads per second on a normal day. Here's how they do it. So, every game on Steam gets split into one megabyte chunks. When you download, your client opens six connections to multiple servers at the same time. Now, this is a mix of their own servers or Cloudflare and others to get the most out of your bandwidth.

### 📋 背景・概要

But one of the coolest parts of the engineering is the updates. When a patch drops, Steam checks the difference between the chunks that are on your machine to the new ones and only downloads what changed. similar to a git diff. So, in the scenario that your downloads are slow, chances are it's probably your I/O. On a hard disk, this could be really slow, but on an SSD, this will be blazingly fast.

### ⭐ 主要ポイント

No longer the bottleneck. Steam started in 2002 as a way to patch their own games, but now it's one of the largest content delivery networks on the entire internet. Follow for more.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年03月26日

</div>
