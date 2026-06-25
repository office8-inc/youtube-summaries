# 📺 OpenAIの新オープンソースモデルを徹底チェック 🤖

## 📋 動画情報

- **タイトル**: OpenAIs NEW Open Source models 🤖
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=YosOtEcYw48](https://www.youtube.com/watch?v=YosOtEcYw48)
- **動画ID**: YosOtEcYw48
- **公開日**: 2025年08月07日 01:50
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、OpenAIが6年ぶりに公開したオープンソースモデル（20B/120B）の性能と使いどころを短く解説した内容です。20Bモデルのローカル実行速度や、120Bモデルを動かすための高性能GPU要件が具体的に示され、実運用時の現実的な選択肢にも触れています。加えて、クラウド実行時の高速推論結果（数百〜1000超tokens/秒）を比較し、体感的な差を伝えています。ローカルAI環境を整えたい開発者や、オープンモデルの活用を検討している人にとって、判断材料を得やすい動画です。

## ⭐ 重要なポイント

- OpenAIの新オープンモデルは20Bと120Bの2種類で、ライセンスはApache 2.0として紹介されている。
- 20BモデルはRTX 5090環境で約151 tokens/秒という高速推論が示され、ローカル実行の現実性が高い。
- 120BモデルはH100級GPU（動画内では約2.5万ドル相当）を前提にしており、導入ハードルが高い点が強調されている。
- クラウド経由では約538〜1,200 tokens/秒の結果も示され、用途次第でローカルとクラウドを使い分ける重要性が示唆されている。
- 結論として、モデルの高性能化が進むほど「自分の環境で動かせるオープンモデル」の価値はさらに高まる。

## 📖 詳細内容

### 🎬 導入

Open AAI just went open source for the first time in 6 years. Open AAI finally dropped their long- aaited open- source models and it comes in two variations. The 120 billion parameters and the 20 billion parameter models. And the best part, Apache 2. So, go ham.

### 📋 背景・概要

But like, are they any good? First, the 20 billion parameter version on Nvidia RTX 5090. Let's give it a try. Wow, it's insanely fast. Like, we're getting about 151 tokens per second.

### ⭐ 主要ポイント

And it might be more because I am recording this on my computer. The 120 billion parameter one, you need like an H100 for which is like 25K. So, either get your bread up or if you're like me, you use something like Grock. So, I have it right here. 120 billion parameters.

### 📝 詳細説明

Like, it's just so fast. You don't you you blink and it's gone. 538 tokens per second. Like that's insane. Let's do the same prompt but do the 20 billion parameter of Model 1.

### 💡 実例・デモ

It's just it's not even funny at this point. It's almost just like a bit disturbing. 1,200 tokens per second. The people behind Grock need to be stopped. And the benchmarks allegedly compare it close to the 03 model, which if true, that's a huge aura boost for little Sammy over here.

### 🔧 技術的詳細

In my opinion, running AI locally is going to be so important as we get more powerful models. It just becomes more important to open source these models and be able to run them on your own machines is the future of AI. Fall for more.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年06月26日

</div>
