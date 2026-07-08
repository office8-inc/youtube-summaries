# 📺 ホームディレクトリを丸ごと消したSteamの致命的バグ

## 📋 動画情報

- **タイトル**: The Steam Bug That Deleted Your Entire Home Directory
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=C9pUJya5aZc](https://www.youtube.com/watch?v=C9pUJya5aZc)
- **動画ID**: C9pUJya5aZc
- **公開日**: 2026年07月09日 01:05
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、2015年にLinux版Steamで発生した「ユーザーデータを大規模削除し得る不具合」の事例を短く解説した内容です。フォルダ移動とシンボリックリンクの組み合わせでSteamの想定が崩れ、削除コマンドが危険な形で実行される可能性があった点が問題の核心です。修正自体は小さなコード変更で済んだ一方、レビュー不足が重大事故につながることを示しています。Linuxユーザーや開発者に向けて、破壊的コマンドの安全対策の重要性を再確認できる動画です。

## ⭐ 重要なポイント

- 問題は`rm -rf "$STEAMROOT/"*`系の処理で、変数解決が想定外になると**ルート配下の広範囲削除**につながり得た点にある。
- 実際の発端は、Steamフォルダ移動後のシンボリックリンク運用で不整合が起き、再インストール処理時に事故が発生したケース。
- 修正は比較的シンプルでも、**危険コマンド実行前の存在確認・パス検証・ガード条件**が必須だと分かる。
- 教訓として、利用者が多い有名ソフトでも安全性は自動で担保されないため、コードレビューと防御的実装が不可欠。

## 📖 詳細内容

### 🎬 導入

There was a time when Steam would accidentally delete your entire file system by simply moving a folder. And that's exactly what happened to this user here named Caden [music] back in 2015. He moved his Steam folder to another drive, sim linked it back, and launched [music] Steam. And since Steam couldn't find the folder, well, it just had to reinstall itself. Normal behavior here.

### 📋 背景・概要

Until he noticed that Steam had recursively deleted every single file that his user owned starting [music] from the root directory, including the 3 TB external drive that he backed everything up onto. Yeah, that's that's not good. How does this end up happening? Well, people found this line of code right [music] here. rm-rf steamroot.

### ⭐ 主要ポイント

Basically, it removes the directory and all the contents of it at what is defined as the steamroot. But the issue is that if that's empty, it will then default to rm-rf/, which is basically the nuclear option to remove everything from the root directory, the delete [music] system32 of Linux. And of course, the GitHub issues went crazy. It was eventually fixed with just a simple line update. But the lesson in all of this [music] is that it doesn't really matter how popular a software is.

### 📝 詳細説明

It might have some scary code lingering in there that you will be the dummy [music] testing. Follow for more.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月09日

</div>
