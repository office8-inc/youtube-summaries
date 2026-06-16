# 📺 Parsing a 300GB JSON File

## 📋 動画情報

- **タイトル**: Parsing a 300GB JSON File
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=OCXlJ9_F6bQ](https://www.youtube.com/watch?v=OCXlJ9_F6bQ)
- **動画ID**: OCXlJ9_F6bQ
- **公開日**: 2026年06月17日 01:32
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この記事は、YouTube動画の日本語字幕（自動翻訳含む）から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

### 🎬 導入

How fast can you parse a 300 GB JSON [music] file? Let's find out. I'm doing this on a DGX Spark just because it has all that memory for me. Now, first we're going to try the normal way, loading it all into memory, which I don't think is going to work. Okay, so it just literally crashed, which like understandable.

### 📋 背景・概要

Next, we're going to use Python's built-in JSON library, which will stream it, which will be hopefully a lot better. So, 10 million records took over 33 seconds, [music] which is 303,000 lines or records per second. We're going to be here for a long time. This time we're going to use the C-based U.JSON parser, which allegedly is a lot [music] faster. Okay, well, it's a little faster.

### ⭐ 主要ポイント

We're at 26.9 seconds. [music] The comparison here is that we get about 400,000 records per second, which is almost 100,000 more than what we did previously. Now, we're going to take that same loop and we're just going to use the Rust base or [music] JSON. That one's actually a lot faster. 18.9 seconds for 10 million records.

### 📝 詳細説明

[music] That's half a million records per second, which honestly really good, but again, I don't got time for that. So, this one uses [music] C and C JSON. So, we're no longer in the Python ecosystem here. Now, we get some really good results here. Almost 600,000 records per second that we're getting with this.

### 💡 実例・デモ

C is not just the magic solution here. There's actually more we can do with it. And one of those is with [music] SIMD JSON. SIMD JSON. Okay, look at that.

### 🔧 技術的詳細

[laughter] Look at that. Whatever that number is, that's insane. [music] But what happens when we do it in parallel? Because we're only using a single thread here. Okay, look at that.

### 🎯 応用例

Under 1 minute 48 seconds to do the entire 270 million. [music] That's crazy. Now, this one is new. I haven't even heard of it actually. It's called QDF and it's on the GPU.

### 💭 考察

So, it's kind of experimental. So, apparently how it works according to Claude here. CPU workers strip columns into RAM [music] and then the GPU parses the JSON in batches. So, it needs a free GPU to do it. So yeah, you can already see that this is like a huge improvement in [music] general.

### 📌 まとめ

This is just so much faster. This is something you could wait through versus like that whole single threaded thing that we were doing before. So the obvious answer seems like just pick the right programming language. But really the parser is a huge part in it. So why even do this in the [music] first place?

### ✅ 結論

I don't know. That's a good question, but I did it anyway. And there's your answer.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年06月17日

</div>
