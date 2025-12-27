# 📺 YouTube動画自動要約システム

英語圏のYouTube動画を自動的に日本語要約記事に変換し、GitHub Copilotで品質向上、XSERVERに公開するシステムです。

## 🌟 機能

- ✅ 登録したYouTubeチャンネルから新着動画を自動収集
- ✅ 字幕を取得して日本語の要約記事を自動生成（ローカル実行）
- ✅ **GitHub Copilot Coding Agentによる自動品質向上** 🆕
  - 日本語の自然さ向上
  - 概要セクションの追加
  - 重要なポイントのハイライト
- ✅ Pull Request経由での品質管理
- ✅ マージ後、XSERVERへ自動FTPアップロード
- ✅ Webビューアで閲覧可能

## 📋 必要なもの

### 1. YouTube Data API キー

1. [Google Cloud Console](https://console.cloud.google.com/)にアクセス
2. 新しいプロジェクトを作成
3. 「APIとサービス」→「ライブラリ」から「YouTube Data API v3」を検索して有効化
4. 「認証情報」→「認証情報を作成」→「APIキー」を選択
5. 生成されたAPIキーをコピー

### 2. GitHub Copilot Pro サブスクリプション 🆕

**自動品質向上機能を使用するには必須**

- [GitHub Copilot Pro](https://github.com/features/copilot) ($10/月)
- または GitHub Copilot Business/Enterprise

Copilot Coding Agentが自動でPull Requestを作成し、記事の品質を向上させます。

### 3. XSERVERアカウント

- ホスト名
- ユーザー名
- パスワード
- アップロード先パス（通常は `/`）

## 🚀 セットアップ

### 1. リポジトリのクローン

```bash
git clone <your-repo-url>
cd 英語圏YouTube動画を要約記事へ変換
```

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数の設定

⚠️ **重要**: `.env`ファイルは機密情報を含むため、絶対にGitにコミットしないでください。

プロジェクトルートに`.env`ファイルを作成し、YouTube APIキーやFTP情報などの必要な環境変数を設定してください。

### 4. GitHub Secretsの設定

⚠️ **重要**: GitHub Actionsで自動実行する場合、リポジトリのSecretsに機密情報を設定してください。

リポジトリの Settings → Secrets and variables → Actions で以下を追加：

| Secret名 | 説明 | 必須 |
|---------|------|------|
| `FTP_HOST` | FTPサーバーのホスト名 | ✅ |
| `FTP_USER` | FTPユーザー名 | ✅ |
| `FTP_PASSWORD` | FTPパスワード | ✅ |

### 5. チャンネルリストの編集

`channel-list.md`を開いて監視したいYouTubeチャンネルを追加：

```markdown
- https://www.youtube.com/@channelname
- https://www.youtube.com/channel/UCxxxxxxxxxxxxxxxxxxxxxx
```

## 💻 使い方

### 完全自動化フロー ⚡

#### 1. ローカルで要約を生成＆自動プッシュ（手動実行・週1回程度）

```bash
python python/improved_summarize_youtube.py --from-list --limit 10 xserver/summaries --push
```

このコマンド1つで以下が実行されます：
- ✅ `channel-list.md`の全チャンネルから未処理動画を取得
- ✅ 字幕を取得して要約記事を生成（`xserver/summaries/YYYY/MM/` に保存）
- ✅ 自動的にgit commit & push

#### 2. 以降は完全自動 🤖

**何もしなくても以下が自動実行されます：**

1. **Push検知** → GitHub Actionsが起動
2. **Issueが作成** → Copilotに自動アサイン
3. **Copilotが記事を改善**
   - 日本語の自然さ向上
   - 概要セクションの追加
   - 重要なポイントのハイライト
4. **Pull Requestが作成**
5. **自動承認＆マージ** ⚡ 🆕
6. **XSERVERへ自動FTPアップロード**
7. **公開完了** → https://office8-inc.com/youtube-summaries/

**あなたがやること：最初のコマンド実行だけ！**

### オプション

**単一動画を処理する場合：**
```bash
python python/improved_summarize_youtube.py <YouTube URL> xserver/summaries --push
```

**特定チャンネルのみ処理する場合：**
```bash
python python/improved_summarize_youtube.py --channel <Channel URL> --limit 10 xserver/summaries --push
```

## 📁 ディレクトリ構造

```
.
├── .github/
│   ├── workflows/
│   │   ├── copilot-improve-summaries.yml  # Copilot自動改善
│   │   ├── auto-merge-copilot-pr.yml      # ⚡ PR自動マージ
│   │   └── deploy-to-ftp.yml              # マージ時FTPアップロード
│   └── README.md                          # このファイル
├── python/                                # Pythonスクリプト
│   └── improved_summarize_youtube.py      # 要約エンジン本体
├── xserver/                               # XSERVER公開ファイル
│   ├── index.html                         # Webビューア
│   ├── get_articles.php                   # 記事一覧API
│   ├── marked.min.js                      # Markdownレンダラー
│   └── summaries/                         # 生成された要約記事
│       └── YYYY/
│           └── MM/
│               └── YYYYMMDDHHmm_ChannelName.md
├── channel-list.md                        # 監視対象チャンネルリスト
└── requirements.txt                       # Python依存関係
```

## 🌐 FTP側のWebシステム設置

`xserver/`ディレクトリの内容をXSERVERの公開ディレクトリにアップロード：

```
/home/YOUR_FTP_USER/YOUR_DOMAIN/public_html/youtube-summaries/
├── index.html
├── get_articles.php
├── marked.min.js
└── summaries/
```

ブラウザで `https://YOUR_DOMAIN/youtube-summaries/` にアクセス

## 🔧 カスタマイズ

### Copilotの改善指示を変更

[.github/workflows/copilot-improve-summaries.yml](.github/workflows/copilot-improve-summaries.yml) の `custom_instructions` セクションを編集

### 処理対象のチャンネルを変更

`channel-list.md`を編集して監視したいYouTubeチャンネルを追加/削除

## 🐛 トラブルシューティング

### Copilotにタスクがアサインされない

**原因**: GitHub Copilot Pro/Business/Enterpriseが有効になっていない

**解決策**:
1. [GitHub Copilot](https://github.com/features/copilot)のサブスクリプションを確認
2. リポジトリでCopilot Coding Agentが有効か確認
3. Organization設定でCopilotが許可されているか確認

### Pull Requestが作成されない

**原因**: Copilotが処理中、またはエラーが発生している

**解決策**:
1. Issueページでステータスを確認
2. Copilotのセッションログを確認（Issue内のリンクから）
3. 必要に応じてIssueにコメントで追加指示

### FTPアップロードが失敗する

**原因**: FTP認証情報が正しくない、または接続エラー

**解決策**:
1. GitHub Secretsの設定を確認
2. XSERVERのFTP設定を確認
3. GitHub Actionsのログでエラーメッセージをチェック

### YouTube APIのクォータ超過

**原因**: 1日のAPI使用量が上限（10,000ユニット）に達した

**解決策**:
- 翌日まで待つ（クォータは毎日リセット）
- 処理する動画数を減らす

### 字幕取得時にIPブロックされる（IpBlocked エラー）

**原因**: YouTubeのボット検出システムが、短時間に多数の字幕リクエストを検出してIPをブロック

**背景**:
- YouTube Data API（公式、認証あり）は成功するが、youtube-transcript-api（非公式スクレイピング）だけブロックされる
- youtube-transcript-apiは内部でYouTubeのWebページをスクレイピングしており、ボット判定の対象

**解決策**:
1. **数時間～24時間待つ**（最も確実）
2. **処理件数を減らす**: `--limit 1` または `--limit 3` で少量ずつ処理
3. **プロキシを使用**（`.env`に設定）:
   ```bash
   # .envファイルに追加
   TRANSCRIPT_PROXY_URL=http://proxy-server:port
   ```
4. **VPNを使用**: ネットワーク環境を変更
5. **時間を空けて実行**: 1日1回、深夜に実行など

**現在の対策**:
- スクリプトは自動的に5-10秒のランダムな待機時間を挿入（ボット検出回避）
- APIリクエスト数は最小限に最適化済み

## 📝 ライセンス

MIT License

## 🙏 クレジット

- YouTube Transcript API
- Google YouTube Data API
- Marked.js
- GitHub Actions
