# 完全自動化フローのシーケンス図

```mermaid
sequenceDiagram
    actor User as ユーザー
    participant Local as ローカル環境
    participant GitHub as GitHub Repository
    participant GHA1 as copilot-improve-summaries.yml
    participant Copilot as GitHub Copilot
    participant GHA2 as auto-merge-copilot-pr.yml
    participant GHA3 as deploy-to-ftp.yml
    participant XSERVER as XSERVERサーバー
    
    %% フェーズ1: 要約記事の生成とプッシュ
    Note over User,Local: フェーズ1: ローカルで要約生成（手動）
    User->>Local: python improved_summarize_youtube.py<br/>--from-list --limit 1<br/>xserver/summaries --push
    
    activate Local
    Note over Local: 1. channel-list.mdを読み込み
    Note over Local: 2. 全チャンネルから未処理動画を収集<br/>（各チャンネル最大50件）
    Note over Local: 3. 公開日時でソート（新→旧）
    Note over Local: 4. 最新1件を抽出
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
    GHA1->>GitHub: Issueを作成<br/>「🤖 要約記事の改善: YYYY-MM-DD HH:MM」
    GHA1->>Copilot: Copilotにアサイン<br/>@copilotメンション
    deactivate GHA1
    
    activate Copilot
    Note over Copilot: タスク内容を解析<br/>- 日本語の自然さ向上<br/>- 概要セクション追加<br/>- 重要ポイント抽出<br/>- 構造の最適化
    
    Copilot->>GitHub: ブランチ作成<br/>copilot/improve-summary-XXXXX
    Copilot->>Copilot: 要約記事を改善
    Copilot->>GitHub: ファイルをコミット
    Copilot->>GitHub: Pull Request作成<br/>「要約記事の品質向上」
    deactivate Copilot
    
    %% フェーズ3: 自動承認とマージ
    Note over GitHub,GHA2: フェーズ3: 自動承認＆マージ
    GitHub->>GHA2: トリガー: PR opened/synchronize<br/>paths: xserver/summaries/**/*.md
    activate GHA2
    
    GHA2->>GHA2: PR作成者をチェック<br/>（github-actions[bot] or Copilot）
    GHA2->>GHA2: 10秒待機<br/>（Copilotの処理完了待ち）
    GHA2->>GitHub: PRステータスを確認
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

## 📊 処理フロー概要

### コマンド実行
```bash
python python/improved_summarize_youtube.py --from-list --limit 1 xserver/summaries --push
```

### 自動実行される処理

| フェーズ | 担当 | 処理内容 | 所要時間 |
|---------|------|---------|---------|
| 1️⃣ 要約生成 | ローカル | 全チャンネルから最新1件を取得し要約記事を生成・プッシュ | 1-2分 |
| 2️⃣ Copilot改善 | GitHub Actions + Copilot | Issueを作成しCopilotが記事を改善してPR作成 | 3-10分 |
| 3️⃣ 自動マージ | GitHub Actions | PRを自動承認＆マージ | 10-20秒 |
| 4️⃣ FTPデプロイ | GitHub Actions | XSERVERへ自動アップロード | 30-60秒 |

### トータル所要時間
- **ユーザー作業**: コマンド1回実行のみ（5秒）
- **自動処理**: 5-15分程度で完全自動公開

## 🔑 必要な設定

### GitHub Secrets
| Secret名 | 用途 | 必須 |
|---------|------|------|
| `GH_TOKEN` | Personal Access Token（PR承認用） | ✅ |
| `FTP_HOST` | FTPサーバーホスト名 | ✅ |
| `FTP_USER` | FTPユーザー名 | ✅ |
| `FTP_PASSWORD` | FTPパスワード | ✅ |

### GH_TOKEN の権限
- `repo` (Full control of private repositories)
- `workflow` (Update GitHub Action workflows)

## 🎯 各ワークフローの役割

### 1. copilot-improve-summaries.yml
**トリガー**: `xserver/summaries/**/*.md`へのpush
- 新規要約ファイルを検出
- Copilotにタスクをアサイン（Issue経由）
- Copilotが記事を改善してPR作成

### 2. auto-merge-copilot-pr.yml
**トリガー**: PRが開かれた時（summariesディレクトリ対象）
- Copilotが作成したPRを自動承認
- squashマージで履歴を綺麗に保つ
- マージ後にブランチ削除

### 3. deploy-to-ftp.yml
**トリガー**: PRがマージされた時
- 変更ファイルをXSERVERへFTPアップロード
- ディレクトリ構造を維持（YYYY/MM/）
- Webシステムファイルも同時アップロード

## ⚠️ 注意点

### PR承認について
- `secrets.GITHUB_TOKEN`（自動生成トークン）では自分のPRを承認できない
- `secrets.GH_TOKEN`（Personal Access Token）を使用する必要がある
- PATは`repo`と`workflow`権限が必要

### エラーハンドリング
- 字幕が取得できない動画は自動スキップ
- FTP接続エラーはワークフローが失敗（ログで確認可能）
- Copilotのタスク失敗時は手動でIssueから再実行可能

## 🔄 繰り返し実行

2回目以降の実行では：
- 既に処理済みの動画は自動スキップ
- 未処理の最新動画のみを処理
- ページネーション機能で次々と古い動画へ進む

```bash
# 1回目: 全チャンネル中で最新1件
python python/improved_summarize_youtube.py --from-list --limit 1 xserver/summaries --push

# 2回目: 1回目の動画をスキップして次の1件
python python/improved_summarize_youtube.py --from-list --limit 1 xserver/summaries --push

# 3回目: 1-2回目をスキップして次の1件
python python/improved_summarize_youtube.py --from-list --limit 1 xserver/summaries --push
```
