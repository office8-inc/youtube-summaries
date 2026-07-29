# 📺 そのアプリ、もう存在する？を調べるツールを作ってみた

## 📋 動画情報

- **タイトル**: I Built an App That Finds if Your App Already Exists
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=6LHHOBXNmUw](https://www.youtube.com/watch?v=6LHHOBXNmUw)
- **動画ID**: 6LHHOBXNmUw
- **公開日**: 2026年07月30日 01:00
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、思いついたアプリ案が既存サービスと重複していないかを素早く調べるためのアプリ開発を紹介する内容です。  
約15,000件のGitHubリポジトリを収集し、SupabaseとPGVectorで意味ベース検索できるようにした実装が解説されています。  
入力したアイデアに近い既存プロジェクトを提示し、LLMが「なぜ競合しそうか」を短く説明する流れが実演されます。  
個人開発者や起業準備中の人が、開発前のアイデア検証を効率化するうえで参考になる動画です。

## ⭐ 重要なポイント

- 「作る前に調べる」を徹底し、アイデア段階で重複リスクを下げることが主目的。  
- データ基盤として約15,000リポジトリを取り込み、単純キーワードではなく意味類似で候補を探している。  
- Supabase + PGVectorを使うことで、実装コストを抑えつつベクトル検索機能を実現している。  
- 検索結果に対してLLMが補足コメントを返すため、類似サービスとの差分を素早く判断しやすい。  
- トークンや開発時間を消費する前の事前調査フローとして、実践投入しやすい構成になっている。  

## 📖 詳細内容

### 🎬 導入

AI slop is flooding the internet. So, I flooded it once more with an app that sees if your app already exists in this giant world of slop. Now, it's easier than ever to ship something. >> [music] >> So, here we are. We're just going to enter our idea and it'll scan GitHub to see if it exists.

### 📋 背景・概要

Let's give it a try. So, first I'm just going to be like uh you know, an app that waters your flowers. See, okay. So, [music] you know, this is not anything here. A modern, beautifully designed flow of flutter.

### ⭐ 主要ポイント

Okay. Cool. And C++? All right, let's see what else we got here. Anime speak into English conversion.

### 📝 詳細説明

Okay, comic translate. [music] Not too crazy of a match. Oh, manga translator at wall. I guess that would be Japanese. Anime speak into English is I guess not really a good way to do it.

### 💡 実例・デモ

How about this? Waifu speak into English conversion. So, normal speech to ooh speech translator. Okay, cool. An app that looks for local bathrooms in your area sorted by ranking.

### 🔧 技術的詳細

Nearby public toilet, world of toilets. Okay, well. Dating app or programmers. Okay, so it's just competitive programmers randomly. So, that doesn't exist, but then again, when do programmers go on dates?

### 🎯 応用例

So, under the hood, I scraped about 15,000 repos and put them into Supabase. I then used PG vector, which matches your idea by the meaning of it. And then an LLM writes like a little thing telling you why your idea might not be the best compared to the ones it found. So, before you burn your tokens building this, check whether some stranger already gave up on it like a couple of years ago. And all of it was built with Supabase.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月30日

</div>
