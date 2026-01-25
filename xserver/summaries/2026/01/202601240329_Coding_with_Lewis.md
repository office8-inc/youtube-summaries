# 📺 1億5000万ドルの損失を招いたタイプミス

## 📋 動画情報

- **タイトル**: The $150,000,000 Typo 🧑‍💻
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=bMMKdmr-jfk](https://www.youtube.com/watch?v=bMMKdmr-jfk)
- **動画ID**: bMMKdmr-jfk
- **公開日**: 2026年01月24日 03:29
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

2017年2月28日、Amazon Web Servicesのエンジニアが実行したコマンドのタイプミスが、1億5000万ドル以上の損失を引き起こした事件を紹介する動画です。S3ビリングサブシステムのサーバーを削除するつもりが、意図した以上のサーバーを停止させてしまいました。世界中の数百万の企業が利用するS3が完全にダウンし、Slack、Docker、Expediaなど多数のサービスが影響を受けました。復旧まで3時間以上かかり、小さなミスが大きな影響を及ぼす教訓的な事例です。

## ⭐ 重要なポイント

- **1億5000万ドルの損失**: 単一のタイプミスが企業に1億5000万ドル以上の損失をもたらした
- **2017年2月28日の事件**: AWS S3のビリングサブシステムのサーバー削除コマンドに誤りがあり、想定以上のサーバーが停止
- **世界的なサービス停止**: Slack、Docker、Expedia、信用組合など、数百万の企業が影響を受けた
- **復旧に3時間以上**: サービスヘルスダッシュボードもS3に依存していたため、状況報告すらできない状態が続いた
- **小さなミスの大きな影響**: タイプミス1つが世界規模の障害を引き起こす可能性があるという教訓

## 📖 詳細内容

### 🎬 導入

This typo cost companies over $150 million. On February 28, 2017, at 9:37 a.m., an Amazon Web Services engineer executed a command that removed servers for an S3 billing subsystem. S3 lets applications store things like files, photos, or videos. The billing subsystem would process the analytics for customers using S3. Now, a reminder that S3 is used by millions of companies worldwide.

### 📋 背景・概要

However, somewhere in that command, a typo was inserted and it took down way more servers than intended. Almost immediately, S3 was unable to handle any requests. It required a full restart. Slack, Docker, Expedia, credit unions, and more were all down because of this outage. Hours and hours go by without any update whatsoever because even their service health dashboard depended on Amazon S3.

### ⭐ 主要ポイント

3 hours later at 12:26 p.m. their index subsystem recovers enough capacity to handle the critical requests while service came back about an hour and a half later. And it's estimated that roughly this outage cost companies over $150 million. So next time you panic over a typo that you sent in your last email, well at least it's not $150 million. Fall for more.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年01月25日

</div>
