# 📺 5GBのJSONファイルをパースしてみた💀

## 📋 動画情報

- **タイトル**: Parsing a 5GB JSON file 💀
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=9tWvDFhBlNU](https://www.youtube.com/watch?v=9tWvDFhBlNU)
- **動画ID**: 9tWvDFhBlNU
- **公開日**: 2025年05月01日 02:26
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この短い動画は、300万件超の論文データを収めた5GB超のJSONファイルを、どれだけ速くパースできるかを試すものです。  
カテゴリ名にHを含む論文を検索するテストで、Python標準ライブラリとSIMD JSONライブラリを比較しています。  
標準ライブラリの23秒に対し、SIMD JSONは約4秒で完了しました。  
この規模のJSONは似た構造のオブジェクトの配列であることが多く、全体をメモリに載せず特定の属性だけを狙えることも高速化の理由だと説明しています。

## ⭐ 重要なポイント

- テストデータは300万件超の科学論文を含む、5GB超のJSONファイル。  
- Python標準ライブラリでは23秒かかり、話者は「実用に耐えない」と評している。  
- SIMD JSONライブラリでは5秒未満、正確には4秒で完了した。  
- SIMDは「Single Instruction Multiple Data」の略で、1つの命令を複数のデータに並列で適用できるため高速になる。  
- 大きなJSONは同じ構造のオブジェクトが並ぶことが多いため、全体をメモリに読み込まず特定の属性だけを対象にできる。

## 📖 詳細内容

### 🎬 導入

How fast can you parse a JSON file with over three million items? I have this data set right here that just has a bunch of scientific papers in it. It's over 5 gigabytes big. And in my test, I'm going to query for every paper that has H in the category name. First, I'm going to use the standard Python library.

### 📋 背景・概要

Okay. Uh 23 seconds. Wow. So, of course, that's pretty slow. Not really acceptable whatsoever.

### ⭐ 主要ポイント

However, we can use the SIMD JSON library, which I hope I'm saying that right. And here we do it in less than 5 seconds. 4 seconds to be exact. Insane. SIMD or SIMD stands for single instruction multiple data and can parallel process a single instruction on multiple data points making it much faster.

### 📝 詳細説明

And the thing with JSON data of this size is that it's usually an array of objects that are very similar in structure. So we can target a specific attribute easily versus loading the whole entire thing into memory, making it that much faster. Always bet on speed. Make sure you follow for more dev content.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年11月05日

</div>
