# 📺 YouTube動画自動要約システム

英語圏のYouTube動画を自動的に日本語要約記事に変換し、FTPサーバーに公開するシステムです。

## 🌟 機能

- ✅ 登録したYouTubeチャンネルから新着動画を自動収集
- ✅ 字幕を取得して日本語の要約記事を自動生成
- ✅ クオリティチェック機能（低品質な記事はGitHub Issueで通知）
- ✅ 年/月/日のディレクトリ構造で整理
- ✅ FTPサーバーへの自動アップロード
- ✅ GitHub Actionsで毎日自動実行（日本時間03:00）

## 📋 必要なもの

### 1. YouTube Data API キー

1. [Google Cloud Console](https://console.cloud.google.com/)にアクセス
2. 新しいプロジェクトを作成
3. 「APIとサービス」→「ライブラリ」から「YouTube Data API v3」を検索して有効化
4. 「認証情報」→「認証情報を作成」→「APIキー」を選択
5. 生成されたAPIキーをコピー

### 2. GitHub Personal Access Token（オプション）

GitHub Issueを自動作成する場合に必要：

1. GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token" をクリック
3. スコープで `repo` を選択
4. トークンを生成してコピー

### 3. FTPサーバー

- ホスト名
- ユーザー名
- パスワード
- アップロード先パス

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

`.env.example`をコピーして`.env`ファイルを作成し、必要な情報を入力：

```bash
cp .env.example .env
```

`.env`ファイルを編集：

```env
YOUTUBE_API_KEY=あなたのYouTube_APIキー
FTP_HOST=ftp.example.com
FTP_USER=ftpユーザー名
FTP_PASSWORD=ftpパスワード
FTP_PORT=21
FTP_REMOTE_PATH=/public_html/blog
FTP_PUBLIC_URL=https://your-domain.com/youtube-summaries
GH_TOKEN=あなたのGitHubトークン（オプション）
GITHUB_REPO=username/repository
```

### 4. GitHub Secretsの設定

⚠️ **重要**: GitHub Actionsで自動実行する場合、リポジトリのSecretsに機密情報を設定してください。

リポジトリの Settings → Secrets and variables → Actions で以下を追加：

- `YOUTUBE_API_KEY` - YouTube Data API v3のキー
- `FTP_HOST` - FTPサーバーのホスト名
- `FTP_USER` - FTPユーザー名
- `FTP_PASSWORD` - FTPパスワード
- `FTP_PORT` - FTPポート（通常は21）
- `FTP_REMOTE_PATH` - アップロード先パス
- `GH_TOKEN` - Issue作成用のPersonal Access Token（オプション、repo権限が必要）

### 5. チャンネルリストの編集

`channel-list.md`を開いて監視したいYouTubeチャンネルを追加：

```markdown
- https://www.youtube.com/@channelname
- https://www.youtube.com/channel/UCxxxxxxxxxxxxxxxxxxxxxx
```

## 💻 使い方

### 手動実行（ローカル）

#### 1. 新着動画を取得

```bash
python python/fetch_videos.py
```

#### 2. 動画を要約

```bash
python python/process_videos.py
```

#### 3. FTPにアップロード

```bash
python python/upload_to_ftp.py
```

### 自動実行（GitHub Actions）

- 毎日日本時間03:00に自動実行されます
- 手動実行も可能：Actions → "Auto Summarize YouTube Videos" → "Run workflow"

## 📁 ディレクトリ構造

```
.
├── .github/
│   ├── workflows/
│   │   └── auto-summarize.yml  # GitHub Actions設定
│   └── README.md               # このファイル
├── python/                     # Pythonスクリプト
│   ├── fetch_videos.py         # 新着動画取得
│   ├── process_videos.py       # 要約生成とバッチ処理
│   ├── upload_to_ftp.py        # FTPアップロード
│   └── improved_summarize_youtube.py  # 要約エンジン本体
├── viewer/                     # FTP側のWebビューア
│   ├── index.html              # フロントエンド
│   └── get_articles.php        # 記事一覧API
├── summaries/                  # 生成された要約記事（.gitignore）
│   └── YYYY/
│       └── MM/
│           └── YYYYMMDDHHmm_ChannelName.md
├── channel-list.md             # 監視対象チャンネルリスト
├── requirements.txt            # Python依存関係
├── .env.example                # 環境変数のサンプル
└── processed_videos.json       # 処理済み動画リスト（.gitignore）
```

## 🌐 FTP側のWebシステム設置

### 方法1: PHPビューア（推奨）

`viewer/`ディレクトリの内容をFTPサーバーにアップロード：

```
/public_html/blog/
├── index.html
├── get_articles.php
└── summaries/
```

ブラウザで `https://your-domain.com/blog/` にアクセス

### 方法2: 静的サイトジェネレーター

Docsifyやその他の静的サイトジェネレーターを使用することも可能

## 🔧 カスタマイズ

### 1日の処理件数を変更

`.env`ファイル：

```env
MAX_VIDEOS_PER_DAY=20
```

### クオリティ閾値を変更

`process_videos.py`の`QUALITY_THRESHOLD`を編集

### 実行時刻を変更

`.github/workflows/auto-summarize.yml`のcron式を編集：

```yaml
# 毎日12:00 JST (03:00 UTC)の場合
- cron: '0 3 * * *'
```

## 🐛 トラブルシューティング

### YouTube APIのクォータ超過

- 1日のクォータは10,000ユニット
- 動画検索1回 = 100ユニット
- 必要に応じて`MAX_VIDEOS_PER_DAY`を調整

### 字幕が取得できない

- 動画に字幕（英語）が存在することを確認
- 自動生成字幕も利用可能

### FTP接続エラー

- FTP情報が正しいか確認
- ファイアウォール設定を確認
- パッシブモードが必要な場合は`upload_to_ftp.py`を修正

## 📝 ライセンス

MIT License

## 🙏 クレジット

- YouTube Transcript API
- Google YouTube Data API
- Marked.js
- GitHub Actions
