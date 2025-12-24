# 📺 The Database Query That Cost $1,000,000

## 📋 動画情報

- **タイトル**: The Database Query That Cost $1,000,000
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=e4nGjTsvADc](https://www.youtube.com/watch?v=e4nGjTsvADc)
- **動画ID**: e4nGjTsvADc
- **公開日**: 2025年12月11日 02:18
- **再生回数**: 534,767 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

Imagine losing $1 million when you run a single database query. Well, Shopify almost did that. And when they were building a data pipeline for this marketing tool they were building, they use something called Big Query, a data warehouse tool by Google that can query fast and store a crazy amount of data, especially if you're a big company. So, they entered their massive amount of data and found a shocking discovery. 75 GB of data was being queried every single time.

### 📋 背景・概要

Now, Big Query charges you per data queried. So the more data that you query, the more it will cost you. But after doing the math, 60 requests per minute times 60 minutes time 24 hours times 30 days turns into 2 and 12 million queries per month, which when Google comes to collect their bill, it's just short of $1 million. The solution, well, to get their bread up. Okay, they clustered their database, meaning that they can sort columns based off of date, geography, timestamp, and more.

### ⭐ 主要ポイント

then BigQuery just goes for that instead of everything all at once that you're never going to use anyway. So after that optimization, 75 gigabytes went down to 508 megabytes. Wow. Or just under $1,400 a month. Now the real winner here, the cloud.

### 📝 詳細説明

Let me know what you want to see

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2025年12月24日

</div>
