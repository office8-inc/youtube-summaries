# 📺 自分専用ソフトをAIで素早く作る方法

## 📋 動画情報

- **タイトル**: How I Build Software Only I Will Ever Use
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=qgyckzrhWAc](https://www.youtube.com/watch?v=qgyckzrhWAc)
- **動画ID**: qgyckzrhWAc
- **公開日**: 2026年07月10日 01:04
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画では、発信者が自分の3Dプリント運用を効率化するために、AIコーディングエージェントで専用ソフトを作る流れを紹介しています。  
具体的には、印刷完了の通知を受けてログ化し、次に印刷するモデルを自動でキューに入れる仕組みを構築しています。  
さらに、SupabaseやMCPサーバー、Skill化を使うことで、実装からデプロイまでを短い手順で完結できる点が示されます。  
「万人向けアプリ」ではなく「自分の課題を解決する小さなソフト」を作りたい個人開発者に有益な内容です。

## ⭐ 重要なポイント

- 3Dプリンターの完了イベントをトリガーにして、状態記録と次ジョブ投入を自動化する実用的ワークフローを構築。  
- Supabase Edge Functionを使い、現実の作業（部品の取り外し・次の印刷準備）とソフト処理を連携している。  
- 依存関係を重く抱え込むより、APIエンドポイントやSkill化にオフロードすることで、実装と運用の負担を下げられる。  
- MCPサーバー経由で「作ってすぐデプロイ」を実行でき、個人用途ソフトの開発サイクルを大幅に短縮可能。  
- 動画の核心は、AI時代では“必要な人だけが使うソフト”を素早く作ること自体が強い競争力になるという点。

## 📖 詳細内容

### 🎬 導入

Coding agents are letting us build software that only we need. So, here's how I do that. I 3D print constantly and I'm always printing parts where one [music] finishes and I need to queue another one up to usually put them together of some sort. So, I built a Superbase Edge function. The printer [music] pings the second a part is done.

### 📋 背景・概要

And then that way it logs it, tells me what's ready, and then queues up the next model to go into the printer. Especially now that we have skills offloading to the [music] API endpoint instead of running it in the agent itself means that there's a potential token savings that you can get as well as it's just easier to do [music] than install dependencies. And with the Superbase MCP server, you just ask your coding agent to simply deploy [music] that software piece that you have built and save it as a skill right after and you're basically done. Easy as that. Whether we like it or not, [music] everyone's a little software company now.

### ⭐ 主要ポイント

You just got to build the software that you need.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月10日

</div>
