# 📺 CSSだけでCPUを動かす「x86 CSS」がすごい

## 📋 動画情報

- **タイトル**: Someone Built a CPU Using CSS
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=LIXAMir9-AU](https://www.youtube.com/watch?v=LIXAMir9-AU)
- **動画ID**: LIXAMir9-AU
- **公開日**: 2026年07月24日 01:00
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、スタイル言語のCSSだけで8086相当のCPU挙動を再現する「x86 CSS」プロジェクトを紹介します。  
小さなCプログラムを8086マシンコードへ変換し、CSSの条件分岐・関数機能を使って命令実行やレジスタ管理を表現するのが核心です。  
完全な現代CPUではないものの、Chromium上で小規模プログラムを動かせる水準まで到達しており、技術デモとしての完成度が高いです。  
フロントエンド開発者や低レイヤー学習者にとって、「CSSの限界」と「実行モデルの理解」を同時に深められる内容です。

## ⭐ 重要なポイント

- 「x86 CSS」は、Cコード→8086機械語→CSS上で実行という異色のパイプラインを実装している。  
- 命令処理には、条件分岐やカスタム関数など最新CSS機能を活用し、メモリ・レジスタ状態を追跡。  
- 対応範囲は「小さな8086エミュレーション」で、フル機能CPUではない点を明確にしている。  
- 動作環境は現状Chromium中心で、JavaScriptを切ってもCSSアニメーション駆動で継続実行できる。  
- 実務直結よりも、Web技術の表現力を拡張して考える発想訓練として価値が高い。

## 📖 詳細内容

### 🎬 導入

Someone built a computer processor [music] using CSS. Yeah, CSS, the language used to make buttons blue and move [music] a div three pixels to the left on the web. x86 CSS takes a small C program, [music] turns it into real 8086 machine code, and then execute those instructions inside of [music] a stylesheet. It basically tracks the processor's memory and registers using new CSS features that can now handle conditions and custom functions which uh why are we doing this with CSS? Now it's not a full modern processor so you know careful in the a comments there.

### 📋 背景・概要

It emulates enough of the original 8086 [music] to run small programs and it currently works in Chromium. JavaScript can provide a faster clock obviously, but disable JavaScript and [music] CSS animations just keeps the processor ticking on its own. So CSS can now run compiled C code. This is just the world right now, folks. Front-end development has escaped containment [music] and you can now do basically anything with it.

### ⭐ 主要ポイント

Fall for more.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月24日

</div>
