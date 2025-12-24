# 📺 この新ファイル形式がJSONを置き換える!?

## 📋 動画情報

- **タイトル**: Will this file format REPLACE JSON!?
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=0pNlWY8hOeE](https://www.youtube.com/watch?v=0pNlWY8hOeE)
- **動画ID**: 0pNlWY8hOeE
- **公開日**: 2025年12月13日 03:37
- **再生回数**: 175,430 回
- **高評価数**: 0

## 💡 概要

この動画では、JSONに代わる新しいファイルフォーマット「TOUNE（Token-oriented object notation）」について解説しています。TOUNEは人間が読みやすく、より短い形式でデータを表現できることが特徴で、コンテキスト長の削減を目的としています。動画では、JSONと比較してトークン数が大幅に削減できる点や、ミニファイ化との比較、実際の採用可能性について議論されています。開発者やAI技術に関心がある方にとって、データフォーマットの最新動向を知る良い機会となる内容です。

## ⭐ 重要なポイント

- **TOUNEはJSONより大幅にコンパクト**: 412文字のJSONが154文字のTOUNEに削減され、約63%の圧縮率を実現
- **CSV形式との比較**: さらに短いCSV形式（36トークン）も提案されたが、ヘッダー情報が欠落しているため実用性に疑問
- **既存技術との互換性が課題**: 大規模言語モデルはJSON、XML、CSVで訓練されており、TOUNEの採用には障壁がある
- **ミニファイ化も有効**: 既存のJSONをミニファイ化するだけでトークン数を約半分に削減可能
- **実用性より革新性**: TOUNEはアイデアとしては興味深いが、既存のエコシステムとの互換性を考えると、実際の採用は難しい可能性

## 📖 詳細内容

### 🎬 導入

Is this new file format revolutionary or stupid? Tokenoriented object notation or tune is like JSON but human readable and much shorter. The point is is to reduce the context length. So as you can see right here, JSON is 412 characters while tune is 154 characters. And of course, the internet went absolutely crazy over this, and someone came up with an even better spec called values separated by comma, which reduces to 36 tokens.

### 📋 背景・概要

Now, buddy over here thought he ate with this, but bro, literally [music] forgot the headers and the whole ID column, so no wonder is so much smaller. Now, something I do like about Toune, which I don't know why the name tune is pissing me off, but I like how it explicitly gives the number of objects it contains. So, if you just run a simple header query, then you get the amount of objects. And also, I did a test. I took this JSON object that they specified here, which is 92 tokens, minified it, and it took like half the amount of tokens off of it, which you can make the argument, hey, this isn't readable.

### ⭐ 主要ポイント

But like why do you need to read it? If it's asking you to do a function call for example, why don't you just do a manual format once it prompts you? It would even be faster that way both from the generation as well as like the speed side. Also, large language models are trained on JSON, XML, CSV, etc. Tune does have a converter, but the amount of data that is already available that exists, it just makes this a hard decision.

### 📝 詳細説明

I like the idea though. What do you think?

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2025年12月24日

</div>
