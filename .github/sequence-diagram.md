# 完全自動化フローのシーケンス図

```mermaid
sequenceDiagram
    actor User as ユーザー
    participant Local as ローカル環境
    participant GitHub as GitHub Repository
    participant GHA1 as copilot-improve-summaries.yml
    participant Issue as Issue + テンプレート
    participant Copilot as GitHub Copilot
    participant GHA2 as auto-merge-copilot-pr.yml
    participant GHA3 as deploy-to-ftp.yml
    participant XSERVER as XSERVERサーバー
    
    %% フェーズ1: 要約記事の生成とプッシュ
    Note over User,Local: フェーズ1: ローカルで要約生成（手動）
    User->>Local: python improved_summarize_youtube.py<br/>--from-list --limit 1<br/>xserver/summaries --push
    
    activate Local
    Note over Local: 1. channel-list.mdを読み込み
    Note over Local: 2. 全チャンネルから未処理動画を収集<br/>（API節約: limitに応じて動的調整）
    Note over Local: 3. 公開日時でソート（新→旧）
    Note over Local: 4. 最新N件を抽出
    Note over Local: 5. 字幕を取得
    Note over Local: 6. 要約記事を生成<br/>xserver/summaries/YYYY/MM/file.md
    Note over Local: 7. git add, commit
    Local->>GitHub: git push (main)
    deactivate Local
    
    %% フェーズ2: Copilotによる改善
    Note over GitHub,Copilot: フェーズ2: Copilotによる自動改善
    GitHub->>GHA1: トリガー: push to main<br/>paths: xserver/summaries/**/*.md
    activate GHA1
    
    GHA1->>GHA1: 変更ファイルを検出<br/>（git diff HEAD~1 HEAD）
    GHA1->>Issue: Issueを作成<br/>「🤖 要約記事の改善: YYYY-MM-DD HH:MM」<br/>📋 テンプレート: copilot-improve-summary.md
    GHA1->>Copilot: Copilotにアサイン<br/>@copilotメンション
    deactivate GHA1
    
    activate Copilot
    Note over Issue,Copilot: 📋 Issueテンプレートの指示を読み込み
    Note over Copilot: タスク内容を解析<br/>- 日本語の自然さ向上<br/>- 概要セクション追加<br/>- 重要ポイント抽出<br/>- 構造の最適化
    
    Copilot->>GitHub: ブランチ作成<br/>copilot/improve-summary-XXXXX
    Copilot->>Copilot: 要約記事を改善
    Copilot->>GitHub: ファイルをコミット
    Copilot->>GitHub: Draft Pull Request作成<br/>「要約記事の品質向上」
    
    Note over Issue,Copilot: 🔑 バトンタッチポイント
    rect rgb(255, 240, 200)
        Note over Copilot: 📋 テンプレート指示に従い<br/>「gh pr ready」を実行
        Copilot->>GitHub: gh pr ready<br/>（Draft → Ready for Review）
    end
    deactivate Copilot
    
    %% フェーズ3: 自動承認とマージ
    Note over GitHub,GHA2: フェーズ3: 自動承認＆マージ
    rect rgb(200, 255, 200)
        GitHub->>GHA2: 🎯 トリガー: ready_for_review イベント<br/>paths: xserver/summaries/**/*.md
    end
    activate GHA2
    
    GHA2->>GHA2: ブランチ名チェック<br/>（copilot/ で始まるか）
    GHA2->>GHA2: 5秒待機<br/>（GitHub API反映待ち）
    GHA2->>GitHub: PRを自動承認<br/>（secrets.GH_TOKEN使用）
    GHA2->>GitHub: PRを自動マージ（squash）<br/>ブランチ削除
    deactivate GHA2
    
    %% フェーズ4: FTPアップロード
    Note over GitHub,XSERVER: フェーズ4: XSERVERへデプロイ
    GitHub->>GHA3: トリガー: PR closed (merged=true)<br/>paths: xserver/summaries/**/*.md
    activate GHA3
    
    GHA3->>GHA3: Python環境セットアップ
    GHA3->>GHA3: FTP接続情報を環境変数に設定<br/>（secrets.FTP_HOST/USER/PASSWORD）
    GHA3->>XSERVER: FTP接続
    
    loop 各要約ファイル
        GHA3->>XSERVER: ディレクトリ作成<br/>（存在しない場合）
        GHA3->>XSERVER: ファイルアップロード<br/>YYYY/MM/file.md
    end
    
    GHA3->>XSERVER: Webシステムファイルアップロード<br/>（index.html, get_articles.php, marked.min.js）
    GHA3->>XSERVER: FTP接続終了
    deactivate GHA3
    
    %% 完了
    Note over User,XSERVER: ✅ 完了: 要約記事が公開されました
    XSERVER-->>User: https://office8-inc.com/youtube-summaries/<br/>で閲覧可能
```

## 🔑 バトンタッチの仕組み（重要！）

### Issueテンプレート → Auto Merge ワークフロー

```
┌─────────────────────────────────────────────────────────────┐
│  📋 Issueテンプレート (copilot-improve-summary.md)          │
│                                                             │
│  ### 🤖 作業完了後の必須アクション                          │
│                                                             │
│  **重要：全ての改善作業が完了したら、                       │
│  必ず以下のコマンドを実行してPRをReady状態にしてください：**│
│                                                             │
│  ```bash                                                    │
│  gh pr ready                                                │
│  ```                                                        │
│                                                             │
│  これにより自動マージワークフローがトリガーされ、            │
│  変更がmainブランチにマージされます。                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Copilotがこの指示に従い
                           │ gh pr ready を実行
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  ⚡ ready_for_review イベント発火                           │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ イベントをキャッチ
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  🔧 auto-merge-copilot-pr.yml                               │
│                                                             │
│  on:                                                        │
│    pull_request_target:                                     │
│      types: [ready_for_review]  ← このイベントでトリガー   │
│      paths:                                                 │
│        - 'xserver/summaries/**/*.md'                        │
│                                                             │
│  jobs:                                                      │
│    auto-merge:                                              │
│      if: contains(...head.ref, 'copilot/')                  │
│      steps:                                                 │
│        - 自動承認                                           │
│        - 自動マージ                                         │
└─────────────────────────────────────────────────────────────┘
```
