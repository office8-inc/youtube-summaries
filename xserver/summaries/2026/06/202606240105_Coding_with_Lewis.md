# 📺 11行のleft-padがネット全体を止めた日

## 📋 動画情報

- **タイトル**: 11 Lines of Code Broke the Internet
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=LWKic13VqAU](https://www.youtube.com/watch?v=LWKic13VqAU)
- **動画ID**: LWKic13VqAU
- **公開日**: 2026年06月24日 01:05
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、2016年に起きたleft-pad削除事件を題材に、現代ソフトウェアが抱える依存関係リスクを解説しています。わずか11行の小さなパッケージでも、連鎖依存によってBabelやReactを含む広範な開発環境に障害が波及したことが示されます。結論として、問題は単発の騒動ではなく、無数の小規模パッケージに支えられた供給網構造そのものにあると指摘しています。JavaScript開発者やSRE、技術選定に関わる人にとって、依存管理の重要性を再確認できる内容です。

## ⭐ 重要なポイント

- 2016年、開発者Azer Koçuluがnpm上の複数パッケージを非公開化し、left-pad削除が大規模障害の引き金になった。
- left-pad自体は11行のユーティリティでも、依存の連鎖で巨大エコシステム全体に影響が広がった。
- npmは被害拡大を止めるため、異例の対応としてパッケージを復元する措置を取った。
- 本質的な課題は、重要システムが“見えにくい多数の外部依存”で成り立つサプライチェーン構造にある。
- 実践面では、依存の棚卸し・ロックファイル管理・代替策準備など平時のリスク対策が不可欠。

## 📖 詳細内容

### 🎬 導入

11 lines of code once broke the entire internet. In 2016, a developer named Azer Koçulu got into a fight with a company called Kik over the name of a package it was using. NPM sided with Kik. So, Azer, being fed up, did the nuclear option. He unpublished every single one of his packages from [music] NPM.

### 📋 背景・概要

And one of those packages was called left-pad. Left-pad is 11 lines of code. All it does is add spaces and zeros to the front of a string. That's literally it. But, the thing is that thousands of projects depended on it.

### ⭐ 主要ポイント

And those projects were depended on other big projects like Babel, React, basically half the JavaScript ecosystem, if not more. So, entire build systems suddenly just couldn't install it and just start crashing. So, the internet's most important tools were taken down by a simple 11-line of code utility. And so, NPM obviously panicked and did something that they'd never done before. They un-unpublished it.

### 📝 詳細説明

[music] Forcefully restored one guy's code without his permission just to stop the bleeding from happening across the internet. And of course, this is a disaster, but beneath all of this is a big underlying issue. We never really fixed the root problem [music] of it. Your app today is still a tower of just tiny packages maintained by random people that you've never met before. So, anyone of whom could just literally ragequit tomorrow and say, "Peace out." Follow for more.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年06月24日

</div>
