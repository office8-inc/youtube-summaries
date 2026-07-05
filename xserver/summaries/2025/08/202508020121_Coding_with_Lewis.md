# 📺 3種類のAIエージェントを理解する実践ガイド

## 📋 動画情報

- **タイトル**: 3 Different Types of AI Agents #ad
- **チャンネル**: Coding with Lewis
- **動画URL**: [https://www.youtube.com/watch?v=mtXaK9peqCA](https://www.youtube.com/watch?v=mtXaK9peqCA)
- **動画ID**: mtXaK9peqCA
- **公開日**: 2025年08月02日 01:21
- **再生回数**: 0 回
- **高評価数**: 0

## 💡 概要

この動画は、業務で使いやすいAIエージェントの代表的な3パターンを短く整理した解説です。  
プロンプト連鎖型、人間承認を挟むHuman-in-the-loop型、複数エージェントを束ねるオーケストレーター型の違いを示しています。  
あわせて、ServiceNow上で自然言語からエージェントを作り、既存データと連携して実運用に乗せる流れも紹介されます。  
AI導入を検討する業務担当者や、社内自動化を進めたいチーム向けの内容です。  
視聴することで、用途別にどのアーキテクチャを選ぶべきかの判断軸が得られます。

## ⭐ 重要なポイント

- 代表的な構成は「プロンプト連鎖型」「Human-in-the-loop型」「オーケストレーター型」の3種類。  
- プロンプト連鎖型は、文脈取得→検証→実行のような多段処理に向いている。  
- Human-in-the-loop型は自動実行しつつ重要判断だけ人が承認するため、実務導入時のリスクを抑えやすい。  
- オーケストレーター型は専門エージェントを連携させ、複雑業務を分担処理できる。  
- ServiceNowのWorkflow Data Fabric連携により、既存システムのデータを横断活用しやすくなる。

## 📖 詳細内容

### 🎬 導入

Here are three ways that AI agents work. First is the prompt chaining agent. This type of agent accepts a prompt, then determines if the output of a prompt feeds into the next action. It's helpful for multi-step reasoning like gathering context, validating input, and then executing a task. Second is a human in the loop agent.

### 📋 背景・概要

This is when an AI agent performs tasks autonomously across systems using tool calls and internal prompts while making sure to include checkpoints to validate with human reviewers and approvers. For example, on the Service Now AI platform, you can have an AI agent handle some of the most tedious support tasks with just a human at the end reviewing and approving actions at key decision points. And third is a AI agent orchestrator. The AI agent orchestrator acts as a manager coordinating a team of specialized AI agents to work together in harmony to achieve a specific goal. With Service Now, you can create pre-built AI agents and use AI agent studio to create fully customizable AI agents.

### ⭐ 主要ポイント

Teams of autonomous AI agents work together guided by the AI agent orchestrator. Building AI agents isn't complicated. Users can create specialized AI agents using conversational natural language to describe the purpose of the agent. You can then use Service Now workflow data fabric to connect your data from any system of record, including databases and other large storage systems. Service Now is automating the tedious parts of our job and freeing up time for people to focus on what matters most.

### 📝 詳細説明

Learn how Service Now AI agents can help you work smarter, not harder.

---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: 2026年07月06日

</div>
