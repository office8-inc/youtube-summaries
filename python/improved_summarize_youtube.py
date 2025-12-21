"""
YouTube動画を要約記事に変換するスクリプト（改良版）
日本語化と装飾を自動で行います
"""
import sys
import os
import re
import json
import subprocess
import pytz
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')


def get_channel_id(channel_url):
    """チャンネルURLからチャンネルIDを抽出"""
    # @handle形式
    handle_match = re.search(r'@([\w-]+)', channel_url)
    if handle_match:
        # YouTube Data APIでハンドルからチャンネルIDを取得
        if YOUTUBE_API_KEY:
            try:
                youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
                request = youtube.search().list(
                    part='snippet',
                    q=f'@{handle_match.group(1)}',
                    type='channel',
                    maxResults=1
                )
                response = request.execute()
                if response['items']:
                    return response['items'][0]['snippet']['channelId']
            except Exception as e:
                print(f"ハンドルからチャンネルID取得エラー: {e}")
    
    # UC...形式のチャンネルID
    channel_id_match = re.search(r'(UC[\w-]{22})', channel_url)
    if channel_id_match:
        return channel_id_match.group(1)
    
    # /channel/形式
    channel_match = re.search(r'/channel/(UC[\w-]{22})', channel_url)
    if channel_match:
        return channel_match.group(1)
    
    return None


def get_channel_latest_videos(channel_id, max_results=10, output_dir=None):
    """チャンネルの未処理動画を取得（既に処理済みの動画をスキップして次のページへ進む）"""
    if not YOUTUBE_API_KEY:
        print("エラー: YOUTUBE_API_KEYが設定されていません")
        return []
    
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        
        # チャンネルのアップロードプレイリストIDを取得
        channel_request = youtube.channels().list(
            part='contentDetails',
            id=channel_id
        )
        channel_response = channel_request.execute()
        
        if not channel_response['items']:
            print(f"チャンネルが見つかりません: {channel_id}")
            return []
        
        uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        
        # 未処理の動画をmax_results件集めるまでページネーション
        unprocessed_videos = []
        next_page_token = None
        total_checked = 0
        
        while len(unprocessed_videos) < max_results:
            # プレイリストから動画を取得
            playlist_request = youtube.playlistItems().list(
                part='snippet',
                playlistId=uploads_playlist_id,
                maxResults=50,  # 1回あたり最大50件取得
                pageToken=next_page_token
            )
            playlist_response = playlist_request.execute()
            
            if not playlist_response['items']:
                break  # これ以上動画がない
            
            # 各動画をチェック
            for item in playlist_response['items']:
                video_id = item['snippet']['resourceId']['videoId']
                total_checked += 1
                
                # 既に処理済みかチェック
                if output_dir and is_video_processed(video_id, output_dir):
                    continue  # スキップ
                
                # 未処理の動画を追加
                unprocessed_videos.append({
                    'video_id': video_id,
                    'title': item['snippet']['title'],
                    'url': f'https://www.youtube.com/watch?v={video_id}',
                    'published_at': item['snippet']['publishedAt']
                })
                
                # 必要な件数に達したら終了
                if len(unprocessed_videos) >= max_results:
                    break
            
            # 次のページがあるかチェック
            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break  # これ以上ページがない
        
        if total_checked > 0:
            print(f"  チェックした動画数: {total_checked}件")
            print(f"  未処理の動画: {len(unprocessed_videos)}件")
        
        return unprocessed_videos
    
    except Exception as e:
        print(f"チャンネル動画取得エラー: {e}")
        return []


def parse_channel_list(file_path='channel-list.md'):
    """channel-list.mdを解析してチャンネルURLリストを取得"""
    if not os.path.exists(file_path):
        print(f"エラー: {file_path} が見つかりません")
        return []
    
    # サンプル・プレースホルダーを除外するパターン
    exclude_patterns = [
        '@channelname',
        'UCxxxxxxxxxxxxxxxxxxxxxx',
        '/channel/UCxxxxxx',
    ]
    
    channels = []
    in_code_block = False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # コードブロック内はスキップ
            if line.startswith('```'):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            
            # URLを含む行を抽出
            if 'youtube.com' in line or line.startswith('UC'):
                # サンプルURLを除外
                if any(pattern in line for pattern in exclude_patterns):
                    continue
                
                # マークダウンリンクから抽出
                url_match = re.search(r'https?://[^\s\)]+', line)
                if url_match:
                    channels.append(url_match.group(0))
                elif line.startswith('UC') and 'xxxx' not in line:
                    channels.append(line)
    
    return channels


def is_video_processed(video_id, output_dir):
    """動画が既に処理済みかチェック（JSONファイルを使用）"""
    if not output_dir:
        return False
    
    processed_file = os.path.join(output_dir, 'processed_videos.json')
    
    if not os.path.exists(processed_file):
        return False
    
    try:
        with open(processed_file, 'r', encoding='utf-8') as f:
            processed = json.load(f)
        return video_id in processed.get('video_ids', [])
    except (json.JSONDecodeError, IOError):
        return False


def mark_video_processed(video_id, output_dir, video_info=None):
    """動画を処理済みとして記録"""
    if not output_dir:
        return
    
    os.makedirs(output_dir, exist_ok=True)
    processed_file = os.path.join(output_dir, 'processed_videos.json')
    
    # 既存のデータを読み込み
    processed = {'video_ids': [], 'details': {}}
    if os.path.exists(processed_file):
        try:
            with open(processed_file, 'r', encoding='utf-8') as f:
                processed = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    
    # video_idsリストに追加
    if video_id not in processed.get('video_ids', []):
        if 'video_ids' not in processed:
            processed['video_ids'] = []
        processed['video_ids'].append(video_id)
    
    # 詳細情報も保存
    if 'details' not in processed:
        processed['details'] = {}
    
    processed['details'][video_id] = {
        'processed_at': datetime.now().isoformat(),
        'title': video_info.get('title', '') if video_info else '',
        'channel': video_info.get('channel', '') if video_info else ''
    }
    
    # ファイルに保存
    with open(processed_file, 'w', encoding='utf-8') as f:
        json.dump(processed, f, ensure_ascii=False, indent=2)


def get_video_id(url_or_id):
    """YouTubeのURLまたはIDから動画IDを抽出"""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/)([0-9A-Za-z_-]{11})',
        r'^([0-9A-Za-z_-]{11})$'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return None


def get_video_info(video_id):
    """YouTube Data APIで動画情報を取得"""
    if not YOUTUBE_API_KEY:
        return None
    
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        request = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        )
        response = request.execute()
        
        if response['items']:
            item = response['items'][0]
            return {
                'title': item['snippet']['title'],
                'channel': item['snippet']['channelTitle'],
                'published_at': item['snippet']['publishedAt'],
                'description': item['snippet']['description'],
                'view_count': item['statistics'].get('viewCount', 'N/A'),
                'like_count': item['statistics'].get('likeCount', 'N/A')
            }
    except Exception as e:
        print(f"動画情報の取得に失敗: {e}")
    
    return None


def get_transcript(video_id):
    """動画の字幕を取得"""
    try:
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=['en'])
        return transcript_data, 'en'
    except Exception as e:
        try:
            api = YouTubeTranscriptApi()
            transcript_data = api.fetch(video_id)
            return transcript_data, 'auto'
        except Exception as e2:
            print(f"字幕の取得に失敗しました: {e2}")
            return None, None


def format_transcript(transcript_data):
    """字幕データを読みやすいテキストに整形"""
    text = ""
    for entry in transcript_data:
        if hasattr(entry, 'text'):
            text += entry.text + " "
        elif isinstance(entry, dict):
            text += entry.get('text', '') + " "
        else:
            text += str(entry) + " "
    
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def create_summary_sections(text):
    """テキストを段落に分割"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sections = []
    current_section = []
    
    for i, sentence in enumerate(sentences):
        current_section.append(sentence)
        if (i + 1) % 5 == 0 or i == len(sentences) - 1:
            sections.append(' '.join(current_section))
            current_section = []
    
    return sections


def translate_section_title(index):
    """セクションタイトルを内容に応じた日本語タイトルに"""
    titles = [
        "導入", "背景・概要", "主要ポイント", "詳細説明",
        "実例・デモ", "技術的詳細", "応用例", "考察",
        "まとめ", "結論", "追加情報", "補足"
    ]
    if index < len(titles):
        return titles[index]
    return f"セクション {index + 1}"


def get_section_emoji(index):
    """セクションに適切な絵文字を割り当て"""
    emojis = [
        "🎬", "📋", "⭐", "📝", "💡", "🔧", "🎯", "💭",
        "📌", "✅", "📚", "🔖", "🎨", "🚀", "⚡", "🌟"
    ]
    return emojis[index % len(emojis)]


def create_markdown_article(video_id, transcript_text, url, video_info=None):
    """Markdown形式の記事を生成（装飾版）"""
    today = datetime.now().strftime('%Y年%m月%d日')
    
    # 動画情報
    title = video_info['title'] if video_info else f"Video ID: {video_id}"
    channel = video_info['channel'] if video_info else "Unknown Channel"
    
    # 公開日時を取得
    published_date = ""
    if video_info and 'published_at' in video_info:
        published_at = video_info['published_at']
        pub_date = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
        jst = pytz.timezone('Asia/Tokyo')
        pub_date_jst = pub_date.astimezone(jst)
        published_date = pub_date_jst.strftime('%Y年%m月%d日 %H:%M')
    
    markdown = f"""# 📺 {title}

## 📋 動画情報

- **タイトル**: {title}
- **チャンネル**: {channel}
- **動画URL**: [{url}]({url})
- **動画ID**: {video_id}
"""
    
    if published_date:
        markdown += f"- **公開日**: {published_date}\n"

    if video_info:
        view_count = int(video_info['view_count']) if video_info['view_count'] != 'N/A' else 0
        like_count = int(video_info['like_count']) if video_info['like_count'] != 'N/A' else 0
        markdown += f"""- **再生回数**: {view_count:,} 回
- **高評価数**: {like_count:,}
"""

    markdown += """
## 💡 概要

この記事は、YouTube動画の字幕から自動生成された要約です。

## ⭐ 重要なポイント

> 📌 この動画の主要なトピックとポイントがここに表示されます

## 📖 詳細内容

"""
    
    # セクションに分割
    sections = create_summary_sections(transcript_text)
    
    for i, section in enumerate(sections):
        emoji = get_section_emoji(i)
        section_title = translate_section_title(i)
        markdown += f"### {emoji} {section_title}\n\n"
        markdown += f"{section}\n\n"
    
    markdown += f"""---

<div align="center">

**📝 この記事は自動生成されたものです**

生成日: {today}

</div>
"""
    
    return markdown


def calculate_quality_score(transcript_text, sections):
    """要約記事のクオリティスコアを計算"""
    score = 100
    
    # 文字数チェック
    if len(transcript_text) < 500:
        score -= 30
    elif len(transcript_text) < 1000:
        score -= 10
    
    # セクション数チェック
    if len(sections) < 3:
        score -= 20
    
    # 多様性チェック（同じ単語の繰り返しが多い場合）
    words = transcript_text.lower().split()
    unique_ratio = len(set(words)) / len(words) if words else 0
    if unique_ratio < 0.3:
        score -= 20
    
    return max(0, score)


def auto_commit_and_push(file_path, video_info):
    """生成したファイルを自動的にgit commit & push"""
    try:
        # git add
        subprocess.run(['git', 'add', file_path], check=True, capture_output=True)
        
        # コミットメッセージを生成
        title = video_info['title'][:50] if video_info else "YouTube要約"
        channel = video_info['channel'] if video_info else "Unknown"
        commit_msg = f"📝 要約追加: {title}\n\nチャンネル: {channel}"
        
        # git commit
        result = subprocess.run(
            ['git', 'commit', '-m', commit_msg],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            # コミット済みまたはエラー
            if 'nothing to commit' in result.stdout:
                print("  ℹ️  変更なし（既にコミット済み）")
                return False
            else:
                print(f"  ⚠️  コミット失敗: {result.stderr}")
                return False
        
        print("  ✓ コミット完了")
        
        # git push
        print("  📤 プッシュ中...")
        push_result = subprocess.run(
            ['git', 'push'],
            capture_output=True,
            text=True
        )
        
        if push_result.returncode == 0:
            print("  ✓ プッシュ完了 - Copilotワークフローがトリガーされます")
            return True
        else:
            print(f"  ⚠️  プッシュ失敗: {push_result.stderr}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Git操作エラー: {e}")
        return False
    except FileNotFoundError:
        print("  ✗ gitコマンドが見つかりません")
        return False


def main(video_url, output_dir=None, auto_push=False):
    """メイン処理"""
    print(f"動画を処理中: {video_url}")
    
    # 動画IDを取得
    video_id = get_video_id(video_url)
    if not video_id:
        print("エラー: 有効なYouTube URLではありません")
        return None
    
    print(f"動画ID: {video_id}")
    
    # 動画情報を取得
    print("動画情報を取得中...")
    video_info = get_video_info(video_id)
    if video_info:
        print(f"タイトル: {video_info['title']}")
        print(f"チャンネル: {video_info['channel']}")
    
    # 字幕を取得
    print("字幕を取得中...")
    transcript_data, lang = get_transcript(video_id)
    
    if not transcript_data:
        print("エラー: 字幕を取得できませんでした")
        return None
    
    print(f"字幕を取得しました（言語: {lang}）")
    
    # テキストに整形
    transcript_text = format_transcript(transcript_data)
    print(f"トランスクリプトの長さ: {len(transcript_text)} 文字")
    
    # セクション分割
    sections = create_summary_sections(transcript_text)
    
    # クオリティスコア計算
    quality_score = calculate_quality_score(transcript_text, sections)
    print(f"クオリティスコア: {quality_score}/100")
    
    # Markdown記事を生成
    markdown_content = create_markdown_article(
        video_id, transcript_text, video_url, video_info
    )
    
    # 出力ファイル名を決定
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        
        if video_info:
            # 投稿日時を取得してフォーマット
            published_at = video_info['published_at']
            # ISO 8601形式をパース (例: 2024-12-15T03:20:00Z)
            pub_date = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
            
            # 日本時間に変換
            jst = pytz.timezone('Asia/Tokyo')
            pub_date_jst = pub_date.astimezone(jst)
            
            # ファイル名用のタイムスタンプ (年月日時分)
            timestamp = pub_date_jst.strftime('%Y%m%d%H%M')
            
            # チャンネル名をファイル名に使用（安全な文字のみ）
            safe_channel = re.sub(r'[^\w\s-]', '', video_info['channel'])
            safe_channel = re.sub(r'[-\s]+', '_', safe_channel)
            
            # 年/月のディレクトリ構造
            year = pub_date_jst.strftime('%Y')
            month = pub_date_jst.strftime('%m')
            dir_path = os.path.join(output_dir, year, month)
            os.makedirs(dir_path, exist_ok=True)
            
            output_file = os.path.join(dir_path, f"{timestamp}_{safe_channel}.md")
        else:
            output_file = os.path.join(output_dir, f"summary_{video_id}.md")
    else:
        output_file = f"summary_{video_id}.md"
    
    # ファイルに保存
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✓ 要約記事を作成しました: {output_file}")
    
    # 処理済みとして記録
    mark_video_processed(video_id, output_dir, video_info)
    
    result = {
        'file_path': output_file,
        'quality_score': quality_score,
        'video_id': video_id,
        'video_info': video_info
    }
    
    # 自動プッシュが有効な場合
    if auto_push:
        print("\n🔄 Git操作を実行中...")
        auto_commit_and_push(output_file, video_info)
    
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方:")
        print("  単一動画: python improved_summarize_youtube.py <YouTube URL> [出力ディレクトリ] [--push]")
        print("  チャンネル: python improved_summarize_youtube.py --channel <Channel URL> [--limit N] [出力ディレクトリ] [--push]")
        print("  リストから: python improved_summarize_youtube.py --from-list [--limit N] [出力ディレクトリ] [--push]")
        print("\nオプション:")
        print("  --channel <URL>  指定チャンネルの最新動画を処理")
        print("  --from-list      channel-list.mdの全チャンネルを処理")
        print("  --limit N        取得する動画数（デフォルト: 10）")
        print("  --push           生成後に自動的にgit commit & push")
        print("\n例:")
        print("  python improved_summarize_youtube.py --channel https://www.youtube.com/@AllAboutAI --limit 1 xserver/summaries --push")
        print("  python improved_summarize_youtube.py --from-list --limit 5 xserver/summaries")
        sys.exit(1)
    
    # 引数解析
    mode = 'single'  # single, channel, list
    video_url = None
    channel_url = None
    output_dir = None
    auto_push = False
    limit = 10
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--channel':
            mode = 'channel'
            if i + 1 < len(sys.argv):
                channel_url = sys.argv[i + 1]
                i += 2
            else:
                print("エラー: --channel にはURLが必要です")
                sys.exit(1)
        elif arg == '--from-list':
            mode = 'list'
            i += 1
        elif arg == '--limit':
            if i + 1 < len(sys.argv):
                limit = int(sys.argv[i + 1])
                i += 2
            else:
                print("エラー: --limit には数値が必要です")
                sys.exit(1)
        elif arg == '--push':
            auto_push = True
            i += 1
        elif not arg.startswith('--'):
            if mode == 'single' and not video_url:
                video_url = arg
            else:
                output_dir = arg
            i += 1
        else:
            i += 1
    
    # モード別処理
    if mode == 'single':
        # 単一動画処理
        if not video_url:
            print("エラー: 動画URLを指定してください")
            sys.exit(1)
        
        result = main(video_url, output_dir, auto_push)
        
        if result and result['quality_score'] < 50:
            print(f"\n⚠️  警告: クオリティスコアが低いです ({result['quality_score']}/100)")
            print("手動でのレビューを推奨します。")
    
    elif mode == 'channel':
        # チャンネルから最新動画を処理
        if not channel_url:
            print("エラー: チャンネルURLを指定してください")
            sys.exit(1)
        
        print(f"\n📺 チャンネルから最新{limit}件の動画を取得中...")
        print(f"チャンネル: {channel_url}\n")
        
        channel_id = get_channel_id(channel_url)
        if not channel_id:
            print("エラー: チャンネルIDを取得できませんでした")
            sys.exit(1)
        
        print(f"チャンネルID: {channel_id}")
        
        videos = get_channel_latest_videos(channel_id, limit, output_dir)
        if not videos:
            print("動画が見つかりませんでした")
            sys.exit(1)
        
        print(f"\n取得した動画: {len(videos)}件\n")
        
        processed_count = 0
        skipped_count = 0
        failed_count = 0
        
        for i, video in enumerate(videos, 1):
            print(f"\n{'='*60}")
            print(f"[{i}/{len(videos)}] 処理中: {video['title']}")
            print(f"{'='*60}")
            
            # 既に処理済みかチェック
            if output_dir and is_video_processed(video['video_id'], output_dir):
                print(f"⏭️  スキップ: 既に処理済みです")
                skipped_count += 1
                continue
            
            result = main(video['url'], output_dir, auto_push)
            
            if result:
                processed_count += 1
                if result['quality_score'] < 50:
                    print(f"⚠️  クオリティスコア低: {result['quality_score']}/100")
            else:
                failed_count += 1
        
        print(f"\n{'='*60}")
        print(f"📊 処理完了")
        print(f"{'='*60}")
        print(f"✅ 処理成功: {processed_count}件")
        print(f"⏭️  スキップ: {skipped_count}件")
        print(f"❌ 失敗: {failed_count}件")
        print(f"合計: {len(videos)}件")
    
    elif mode == 'list':
        # channel-list.mdから全チャンネルの動画を収集し、新しい順に処理
        print(f"\n📋 channel-list.mdから全チャンネルを処理中...\n")
        
        channels = parse_channel_list()
        if not channels:
            print("エラー: チャンネルが見つかりませんでした")
            sys.exit(1)
        
        print(f"登録チャンネル数: {len(channels)}件")
        print(f"取得件数: 全チャンネル合計で最新{limit}件\n")
        
        # 全チャンネルから動画を収集
        all_videos = []
        
        for ch_idx, channel_url in enumerate(channels, 1):
            print(f"[{ch_idx}/{len(channels)}] チャンネルから動画を取得中: {channel_url}")
            
            channel_id = get_channel_id(channel_url)
            if not channel_id:
                print("  ⚠️  チャンネルIDを取得できませんでした")
                continue
            
            # 各チャンネルから多めに取得（最大50件）
            videos = get_channel_latest_videos(channel_id, 50, output_dir)
            if videos:
                for video in videos:
                    video['channel_url'] = channel_url  # チャンネル情報を追加
                all_videos.extend(videos)
                print(f"  ✓ {len(videos)}件の未処理動画を取得")
            else:
                print(f"  ℹ️  未処理動画なし")
        
        if not all_videos:
            print("\n全チャンネルで未処理の動画が見つかりませんでした")
            sys.exit(0)
        
        # 公開日時でソート（新しい順）
        all_videos.sort(key=lambda x: x['published_at'], reverse=True)
        
        print(f"\n{'='*60}")
        print(f"📊 収集結果")
        print(f"{'='*60}")
        print(f"全チャンネルから収集した未処理動画: {len(all_videos)}件")
        print(f"これから処理する動画: {min(limit, len(all_videos))}件")
        print(f"{'='*60}\n")
        
        # 上位limit件だけを処理
        total_processed = 0
        total_failed = 0
        
        for i, video in enumerate(all_videos[:limit], 1):
            print(f"\n{'='*60}")
            print(f"[{i}/{min(limit, len(all_videos))}] 処理中")
            print(f"{'='*60}")
            print(f"タイトル: {video['title']}")
            print(f"公開日: {video['published_at']}")
            print(f"動画URL: {video['url']}")
            
            result = main(video['url'], output_dir, auto_push)
            
            if result:
                total_processed += 1
            else:
                total_failed += 1
        
        print(f"\n{'='*60}")
        print(f"🎉 全チャンネル処理完了")
        print(f"{'='*60}")
        print(f"✅ 処理成功: {total_processed}件")
        print(f"❌ 失敗: {total_failed}件")
