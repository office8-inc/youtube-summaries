# 📺 配列の添字が0から始まる本当の理由

## 📋 動画情報

- **タイトル**: Why arrays really start at zero
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=5i1fByfOotg](https://www.youtube.com/watch?v=5i1fByfOotg)
- **動画ID**: 5i1fByfOotg
- **公開日**: 2026年06月25日 01:09
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、配列のインデックスがなぜ0始まりなのかを、歴史的背景と実装上の事情から短く解説しています。  
単なる「メモリアドレスの都合」だけでなく、1967年の言語Bでコンパイル時間を削る必要があったことが起点として紹介されます。  
その設計がC言語に継承され、さらに多くの言語へ広がったことで、現在の標準的な慣習として定着しました。  
プログラミング初学者から実務開発者まで、日常的な仕様の背景を理解して納得感を得られる内容です。

## ⭐ 重要なポイント

- 配列の0始まりは「最初の要素までのオフセットが0」というメモリ表現と直感的に対応している。  
- 歴史的には、1967年の言語Bで共有メインフレーム利用時のコンパイル時間を短縮する工夫が大きな理由だった。  
- C言語がこの仕様を引き継ぎ、C系言語の普及によって0-based indexingが事実上の標準になった。  
- 仕様の背景を知ると、添字0始まりは不合理な慣習ではなく、当時の制約下で合理的だった設計判断だと理解できる。  

## 📖 詳細内容

### 🎬 導入

Arrays start at zero in most programming languages. Beginners sometimes hate it, and experienced devs, well, stop questioning it a long time ago. Now, the clean intuition is memory. An array is a block of values. The variable points to the start, and the first element sits right there at the start.

### 📋 背景・概要

Zero offset, index zero. But, that's [music] technically not why we count from zero. It actually comes from a language called Bopel, written in 1967. So, before C even existed, C didn't invent zero-based indexing. It just inherited it.

### ⭐ 主要ポイント

And it wasn't about saving CPU cycles at runtime. It was about saving compile time. Bopel ran on a shared mainframe that you rented by the clock. Kind of similar to how you do today, to be honest. So, if you compiled too slowly, well, your job just got bumped off the machine before it even finished.

### 📝 詳細説明

And so, when you start at zero, well, it shaved that time down. Just like a little hack there, I guess. And so, C copied it, and then everyone copied C. So, 50 years later, here [music] we are. So, next time when someone complains about why arrays start at zero, well, don't blame C.

### 💡 実例・デモ

Blame a 1967 language trying not to get kicked off of the mainframe computer >> [music] >> that it was sharing access to, on the clock.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年06月25日

</div>
