# 📺 The Steam Bug That Deleted Your Entire Home Directory

## 📋 動画情報

- **タイトル**: The Steam Bug That Deleted Your Entire Home Directory
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=C9pUJya5aZc](https://www.youtube.com/watch?v=C9pUJya5aZc)
- **動画ID**: C9pUJya5aZc
- **公開日**: 2026年07月09日 01:05
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

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
