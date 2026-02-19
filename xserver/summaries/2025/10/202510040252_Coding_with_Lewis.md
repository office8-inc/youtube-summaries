# 📺 銀行に騙されそうになったのでPythonで対抗してみた 💀

## 📋 動画情報

- **タイトル**: My Bank Tried to Scam Me… So I used Python instead 💀
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=eXOvTmEDa7Y](https://www.youtube.com/watch?v=eXOvTmEDa7Y)
- **動画ID**: eXOvTmEDa7Y
- **公開日**: 2025年10月04日 02:52
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

本動画では、開発者のLewisが銀行の不当な手数料（明細書の印刷に$17.63を請求）に対抗するため、Pythonを使って問題を解決する様子を紹介しています。Charles Proxyでモバイルアプリの通信を解析したところ、銀行が全明細書のデータをすでに送信しているにもかかわらず、UIで意図的に非表示にして有料サービスへ誘導していたことが判明します。Pythonで全明細書を約1分半でダウンロードするスクリプトを作成し、手数料を完全に回避したというユニークな実体験です。プログラミングの実用的な活用方法に興味のある開発者や、Charles Proxyなどのネットワーク解析ツールを学びたい人に最適な内容です。

## ⭐ 重要なポイント

- 銀行はモバイルアプリで全明細書データを一度に送信していたが、UIを意図的に制限し、1件ずつしか表示しない設計にして有料窓口を利用させていた
- Charles Proxyを使えばモバイルアプリの通信内容を詳細に解析でき、バックエンドが実際にどのようなデータを返しているかを確認できる
- PythonでHTTPリクエストを自動化することで、手作業で17分かかる作業を約1分半で完了し、$17.63の手数料を節約できた
- 「17分の作業を3時間かけて自動化した」という開発者あるあるのジョークが含まれており、エンジニア的思考の楽しさが伝わる内容
- ネットワーク解析とPython自動化の組み合わせは、日常の不便や理不尽な制限を解決する強力な手段になりうる

## 📖 詳細内容

### 🎬 導入

My bank wanted to charge me $17.63 to print old credit card statements. So, I used Python instead to teach them a lesson. I needed 3 years of credit card statements that weren't available on desktop. The mobile app had them, but only one at a time. Painfully slow.

### 📋 背景・概要

So, I used Charles proxy to understand what data the bank was giving me, as normal people do, and was shocked at what I saw. The bank was already sending every single statement in the request, but was hiding them behind a crappy UI so I would ask the branch on the phone to get them for me for a fee. That's when I got my Python out and grabbed the URLs that the bank already provided me and downloaded them all in just like a minute and a half. As any good developer, I took a 17-minute task and stretched it out over 3 hours. Never let them know your next

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年02月20日

</div>
