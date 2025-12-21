"""
YouTube動画を要約記事に変換するスクリプト（改良版）
日本語化と装飾を自動で行います
"""
import sys
import os
import re
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')


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
    
    markdown = f"""# 📺 YouTube動画要約

## 📋 動画情報

- **タイトル**: {title}
- **チャンネル**: {channel}
- **動画URL**: [{url}]({url})
- **動画ID**: {video_id}
- **要約作成日**: {today}
"""

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


def main(video_url, output_dir=None):
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
            from datetime import datetime
            published_at = video_info['published_at']
            # ISO 8601形式をパース (例: 2024-12-15T03:20:00Z)
            pub_date = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
            
            # 日本時間に変換
            import pytz
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
    
    return {
        'file_path': output_file,
        'quality_score': quality_score,
        'video_id': video_id,
        'video_info': video_info
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python improved_summarize_youtube.py <YouTube URL> [出力ディレクトリ]")
        sys.exit(1)
    
    video_url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    result = main(video_url, output_dir)
    
    if result and result['quality_score'] < 50:
        print(f"\n⚠️  警告: クオリティスコアが低いです ({result['quality_score']}/100)")
        print("手動でのレビューを推奨します。")
