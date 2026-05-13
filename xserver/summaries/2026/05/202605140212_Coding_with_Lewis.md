# 📺 GitLab本番データベース削除事故から学ぶバックアップの現実

## 📋 動画情報

- **タイトル**: How a GitLab engineer DESTROYED their main database…
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=R_mtO9uUCa8](https://www.youtube.com/watch?v=R_mtO9uUCa8)
- **動画ID**: R_mtO9uUCa8
- **公開日**: 2026年05月14日 02:12
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、2017年にGitLabで発生した本番データベース誤削除インシデントの経緯と復旧対応を解説しています。  
スパム攻撃対応中の操作ミスで約300GBの本番データが失われ、複数系統のバックアップが機能しなかった事実が共有されます。  
最終的には6時間前のステージングDBスナップショットで復旧したものの、6時間分のユーザーデータが消失しました。  
SREや開発チームに向けて、「復元テストされていないバックアップはバックアップではない」という教訓を強く示す内容です。

## ⭐ 重要なポイント

- 事故の直接原因は、本番/セカンダリの取り違えによる `rm -rf` 実行で、約300GBの本番DBが消失。  
- GitLab側は複数のバックアップ手段を持っていたが、未検証・設定不備で次々に失敗し、実運用で機能しなかった。  
- 復旧は「6時間前のステージングDB」から実施され、Issues・MR・コメントなど約6時間分のデータロスが発生。  
- 復旧作業を公開配信し、事後に詳細なポストモーテムを公開した透明性は、信頼回復の実務として重要。  
- 実践的教訓は明確で、定期的なリストア訓練と手順検証を行わない限り、バックアップ戦略は成立しない。  

## 📖 詳細内容

### 🎬 導入

What happens when one engineer deletes something 100,000 people depend on? Well, in 2017, a GitLab engineer did exactly that by accidentally deleting the production database. GitLab was dealing with a spam attack that was hammering their database. And so, the engineer tried to fix a replication issue and ran r-f on what he thought was the secondary database directory. Yeah, famous last words.

### 📋 背景・概要

It was the primary, of course. 300 GB of production data gone. GitLab's entire platform went down. Basically, the center of it all was down. They tried their backups, but they were silently failing.

### ⭐ 主要ポイント

Volume snapshots also broke. The Azure backups, they were never tested. And the S3 backups, it only covered a different type of database. Nothing was working. So, they were 0 and five.

### 📝 詳細説明

Not a good score at the moment. But they did have one snapshot that they can use, a database from their staging server from 6 hours earlier. And this worked, but lost about 6 hours of user data, issues, merge requests, comments, just completely gone. Yikes. And the craziest part is that they streamed this recovery process live for everyone to see it.

### 💡 実例・デモ

Over 5,000 people were watching someone try and recover their website. Insane. And after the incident, GitLab published a full postmortem. Every detail, every failure, every lesson. They turned the disaster into one of the most transparent incident reports in tech history.

### 🔧 技術的詳細

Like come on. Who live streams a freaking fix? Test your backups. If you haven't restored from one, you don't have backups. You just have hopes and dreams and memes.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年05月14日

</div>
