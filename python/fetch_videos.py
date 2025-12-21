"""
チャンネルリストから新着動画を取得するスクリプト
"""
import os
import re
import json
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from dotenv import load_dotenv
import pytz

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
MAX_VIDEOS = int(os.getenv('MAX_VIDEOS_PER_DAY', 10))
PROCESSED_VIDEOS_FILE = 'processed_videos.json'


def load_processed_videos():
    """処理済み動画IDのリストを読み込み"""
    if os.path.exists(PROCESSED_VIDEOS_FILE):
        with open(PROCESSED_VIDEOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_processed_videos(video_ids):
    """処理済み動画IDのリストを保存"""
    with open(PROCESSED_VIDEOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(video_ids, f, indent=2)


def extract_channel_id(channel_input):
    """チャンネルURLまたはIDからチャンネルIDを抽出"""
    # すでにチャンネルIDの場合
    if channel_input.startswith('UC') and len(channel_input) == 24:
        return channel_input
    
    # URLからチャンネルIDを抽出
    patterns = [
        r'youtube\.com/channel/([^/\s]+)',
        r'youtube\.com/@([^/\s]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, channel_input)
        if match:
            username_or_id = match.group(1)
            # @username形式の場合はAPIで解決
            if not username_or_id.startswith('UC'):
                return resolve_username_to_channel_id(username_or_id)
            return username_or_id
    
    return None


def resolve_username_to_channel_id(username):
    """ユーザー名からチャンネルIDを解決"""
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        request = youtube.search().list(
            part='snippet',
            q=username,
            type='channel',
            maxResults=1
        )
        response = request.execute()
        
        if response['items']:
            return response['items'][0]['snippet']['channelId']
    except Exception as e:
        print(f"ユーザー名の解決に失敗: {e}")
    
    return None


def read_channel_list():
    """channel-list.mdからチャンネルリストを読み込み"""
    channels = []
    
    if not os.path.exists('channel-list.md'):
        print("channel-list.mdが見つかりません")
        return channels
    
    with open('channel-list.md', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # コメントや空行をスキップ
            if not line or line.startswith('#') or line.startswith('<!--'):
                continue
            
            # リスト形式の行を処理
            if line.startswith('-'):
                channel_input = line[1:].strip()
                channel_id = extract_channel_id(channel_input)
                if channel_id:
                    channels.append(channel_id)
    
    return channels


def get_recent_videos(channel_id, days_back=7):
    """チャンネルから最近の動画を取得"""
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        
        # 日本時間で計算
        jst = pytz.timezone('Asia/Tokyo')
        now = datetime.now(jst)
        published_after = (now - timedelta(days=days_back)).isoformat()
        
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            type='video',
            order='date',
            publishedAfter=published_after,
            maxResults=10
        )
        response = request.execute()
        
        videos = []
        for item in response['items']:
            video_id = item['id']['videoId']
            videos.append({
                'video_id': video_id,
                'title': item['snippet']['title'],
                'published_at': item['snippet']['publishedAt'],
                'channel': item['snippet']['channelTitle'],
                'url': f'https://www.youtube.com/watch?v={video_id}'
            })
        
        return videos
    
    except Exception as e:
        print(f"動画の取得に失敗 (チャンネルID: {channel_id}): {e}")
        return []


def main():
    """メイン処理"""
    print("チャンネルリストを読み込み中...")
    channels = read_channel_list()
    print(f"監視対象チャンネル数: {len(channels)}")
    
    if not channels:
        print("監視対象チャンネルがありません")
        return []
    
    # 処理済み動画を読み込み
    processed_videos = load_processed_videos()
    print(f"処理済み動画数: {len(processed_videos)}")
    
    # 新着動画を収集
    all_videos = []
    for channel_id in channels:
        print(f"\nチャンネル {channel_id} から動画を取得中...")
        videos = get_recent_videos(channel_id)
        
        # 未処理の動画のみ追加
        for video in videos:
            if video['video_id'] not in processed_videos:
                all_videos.append(video)
                print(f"  - {video['title']}")
    
    # 日付順にソート（古い順）
    all_videos.sort(key=lambda x: x['published_at'])
    
    # 最大件数まで制限
    new_videos = all_videos[:MAX_VIDEOS]
    
    print(f"\n処理対象の新着動画: {len(new_videos)}/{len(all_videos)} 件")
    
    # 結果を保存
    with open('new_videos.json', 'w', encoding='utf-8') as f:
        json.dump(new_videos, f, indent=2, ensure_ascii=False)
    
    return new_videos


if __name__ == "__main__":
    videos = main()
    if videos:
        print(f"\n✓ {len(videos)}件の新着動画を new_videos.json に保存しました")
    else:
        print("\n新着動画はありませんでした")
