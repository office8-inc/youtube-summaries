# 📺 IBM watsonx orchestrateを使った開発

## 📋 動画情報

- **タイトル**: Building with IBM watsonx orchestrate #ad
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=LZT82V2d07Y](https://www.youtube.com/watch?v=LZT82V2d07Y)
- **動画ID**: LZT82V2d07Y
- **公開日**: 2025年11月07日 04:15
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画では、IBM watsonx orchestrateを使用して、複数のサービス（Slack、Gmail、Notionなど）を統合した生産性向上アプリケーションを構築する方法を紹介しています。開発者向けに、Watson X orchestrateのAIエージェント機能を活用して、メッセージやメールから情報を自動抽出し、タスクリストを作成・優先順位付けする実装方法を解説しています。MCPサーバーや統合管理が簡単にできる点が強調されており、開発効率を大幅に向上させるツールとして提示されています。

## ⭐ 重要なポイント

- **マルチサービス統合**: Slack、Gmail、Notionなどの複数サービスを一つのアプリケーションで管理できるTUIアプリケーションを構築
- **AIエージェントの活用**: Watson X orchestrateを使って、メッセージやメールから情報を自動抽出し、タスクリストを作成・優先順位付けする機能を実装
- **簡単なAPI統合**: Watson X orchestrateは他のLLMプロバイダーと同様にAPIリクエストで利用でき、MCPサーバーや統合管理が簡単
- **Webhookによる自動化**: 新しいメールやメッセージが届いたときに自動的にチャットリクエストを実行し、エージェントが自動処理
- **開発効率の向上**: 変化の激しい開発環境でも、Watson X orchestrateを使えば更新作業が非常に簡単になる

## 📖 詳細内容

### 🎬 導入

As a developer, there's always a better way to stay productive, which is why I'm partnering with IBM to build this agent [music] with Watson X orchestrate. So, I created this 2e application right here that connects to all of my services like [music] Slack, Gmail, Notion, and more. And so, I'm using Watson X orchestrate to build agents that could easily extract the information from messages, emails, and other unstructured data to create a task list for me and prioritize it. So when I'm building out this TUI, I can actually just connect to Watson X orchestrate using an API [music] request similar to if you were using any other LLM provider. However, I can easily manage all of [music] the MCP servers and integrations within Orchestrate.

### 📋 背景・概要

So I built a web hook that will do a chat request whenever a new email or message comes in. I then have the agent automatically process it and have it access to other agents in case it needs context or perform [music] other actions on my behalf like sending a message through Slack for example. And with this TUI that I built is really fast and I can see everything from a topown level. Things change constantly as a developer and Watson X orchestrate makes updating everything [music] just dead simple.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2025年12月28日

</div>
