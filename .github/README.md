# 📺 YouTube動画自動要約システム

英語圏のYouTube動画を自動的に日本語要約記事に変換し、Claude で品質向上、XSERVERに公開するシステムです。

## 🌟 機能

- ✅ 登録したYouTubeチャンネルから新着動画を自動収集
- ✅ 字幕を取得して日本語の要約記事を自動生成（ローカル実行）
- ✅ **Claude による自動品質向上**
  - 日本語の自然さ向上
  - 概要セクションの追加
  - 重要なポイントのハイライト
- ✅ 未改善（英語＋プレースホルダー）の記事は push を保留して誤公開を防止（crow-bot 経由の実行時）
- ✅ main への push 後、XSERVERへ自動FTPアップロード
- ✅ Webビューアで閲覧可能

## 📋 必要なもの

### 1. YouTube Data API キー

1. [Google Cloud Console](https://console.cloud.google.com/)にアクセス
2. 新しいプロジェクトを作成
3. 「APIとサービス」→「ライブラリ」から「YouTube Data API v3」を検索して有効化
4. 「認証情報」→「認証情報を作成」→「APIキー」を選択
5. 生成されたAPIキーをコピー

### 2. Claude Code CLI

**自動品質向上機能を使用するには必須**

- [Claude Code](https://claude.com/claude-code)（サブスクリプション枠で実行）
- 生成→改善→push は常駐ボット（crow-bot）のスケジューラが毎朝 JST 8:00 に実行する
- GitHub Actions 側では改善を行わない（API キーを Secrets に置かない設計）

> 2026-08-05 までは GitHub Copilot Coding Agent がこのフェーズを担当していた。
> 2026-08-03 の Copilot 側ランタイム更新で「編集ツールを呼ばず 0 ファイルの PR を作る」
> 挙動になったため Claude へ移行し、2026-09-26 の Copilot 解約で経路を削除した。

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

**通常は何もしなくてよい。** 常駐ボット（crow-bot）のスケジューラが平日 JST 8:00 に
以下を一括で実行する：

1. **要約生成** → `improved_summarize_youtube.py --from-list --limit 5 xserver/summaries`
   （`--push` なし）で生成し、crow-bot が `xserver/summaries` を commit（push はしない）
2. **Claudeが記事を改善**
   - 日本語の自然さ向上
   - 概要セクションの追加
   - 重要なポイントのハイライト
3. **改善完了を機械判定** → プレースホルダーが残っていれば push を保留
4. **mainへpush**
5. **XSERVERへ自動FTPアップロード**（`deploy-to-ftp.yml`）
6. **公開完了** → https://office8-inc.com/youtube-summaries/

### 手動で生成したい場合

`--push` を付けずに実行する。生成された記事は次回（平日 8:00）の crow-bot ジョブが
commit・改善・push まで引き取る。

```bash
python python/improved_summarize_youtube.py --from-list --limit 10 xserver/summaries
```

> ⚠️ **`--push` は付けない。** `--push` は生成直後の記事（英語タイトル＋プレースホルダー）を
> そのまま commit & push するため、`deploy-to-ftp.yml` が走って**改善前の記事が公開される**。
> 未改善記事の push を止める安全弁は crow-bot 側にあり、このスクリプト単体には無い。

### オプション

**単一動画を処理する場合：**
```bash
python python/improved_summarize_youtube.py <YouTube URL> xserver/summaries
```

**特定チャンネルのみ処理する場合：**
```bash
python python/improved_summarize_youtube.py --channel <Channel URL> --limit 10 xserver/summaries
```

## 📁 ディレクトリ構造

```
.
├── .github/
│   ├── workflows/
│   │   └── deploy-to-ftp.yml              # main push時のFTPアップロード
│   └── README.md                          # このファイル
├── CLAUDE.md                              # 開発エージェント向け指示書
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

### 改善指示（プロンプト）を変更

crow-bot 側の `YOUTUBE_IMPROVE_PROMPT`（`crow_bot/prompts.py`）を編集。
リポジトリ側の規約は [CLAUDE.md](../CLAUDE.md) に置く。

### 処理対象のチャンネルを変更

`channel-list.md`を編集して監視したいYouTubeチャンネルを追加/削除

## 🐛 トラブルシューティング

### 記事が英語タイトル・プレースホルダーのまま

**原因**: 改善フェーズ（Claude）が失敗している。多いのは Claude CLI の認証切れ。

**解決策**:
1. `claude auth status` で認証状態を確認
2. crow-bot のスケジューラ通知（Slack）で改善フェーズのエラーを確認
3. 直したら次回のジョブで再改善される（未改善のコミットは push されずローカルに残る）

### mainにpushされない

**原因**: 未改善ファイルが残っているため、安全弁が push を保留している（仕様）。

**解決策**: 上記の改善フェーズのエラーを解消する。緊急で公開したい場合のみ手動で
`git push` するが、未完成記事がそのまま公開されることに注意。

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
