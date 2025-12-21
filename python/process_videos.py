"""
新着動画を一括処理して要約記事を生成するスクリプト
"""
import os
import json
from datetime import datetime
from improved_summarize_youtube import main as summarize_video
from dotenv import load_dotenv
import pytz

load_dotenv()


def create_output_directory(video_info):
    """動画情報から出力ディレクトリを作成"""
    jst = pytz.timezone('Asia/Tokyo')
    published_at = datetime.fromisoformat(video_info['published_at'].replace('Z', '+00:00'))
    published_jst = published_at.astimezone(jst)
    
    year = published_jst.strftime('%Y')
    month = published_jst.strftime('%m')
    
    output_dir = os.path.join('xserver', 'summaries', year, month)
    os.makedirs(output_dir, exist_ok=True)
    
    return output_dir


def main():
    """メイン処理"""
    # 新着動画リストを読み込み
    if not os.path.exists('new_videos.json'):
        print("new_videos.json が見つかりません")
        return
    
    with open('new_videos.json', 'r', encoding='utf-8') as f:
        videos = json.load(f)
    
    if not videos:
        print("処理する動画がありません")
        return
    
    print(f"処理開始: {len(videos)}件の動画")
    
    results = []
    processed_video_ids = []
    
    for i, video in enumerate(videos, 1):
        print(f"\n[{i}/{len(videos)}] {video['title']}")
        print(f"  チャンネル: {video['channel']}")
        
        # 出力ディレクトリを作成
        output_dir = create_output_directory(video)
        
        # 要約記事を生成
        try:
            result = summarize_video(video['url'], output_dir)
            
            if result:
                processed_video_ids.append(video['video_id'])
                print(f"  ✓ クオリティスコア: {result['quality_score']}/100")
                
                results.append({
                    'video': video,
                    'result': result
                })
            else:
                print(f"  ✗ 処理に失敗しました")
                
        except Exception as e:
            print(f"  ✗ エラー: {e}")
    
    # 処理済み動画IDを保存
    if processed_video_ids:
        # 既存の処理済みリストを読み込み
        if os.path.exists('processed_videos.json'):
            with open('processed_videos.json', 'r', encoding='utf-8') as f:
                existing_ids = json.load(f)
        else:
            existing_ids = []
        
        # 新しいIDを追加
        all_ids = list(set(existing_ids + processed_video_ids))
        
        with open('processed_videos.json', 'w', encoding='utf-8') as f:
            json.dump(all_ids, f, indent=2)
        
        print(f"\n✓ {len(processed_video_ids)}件の動画を処理済みリストに追加")
    
    # 結果サマリー
    print("\n" + "="*50)
    print("処理結果サマリー")
    print("="*50)
    print(f"総処理数: {len(results)}")
    print(f"成功: {len(results)}")
    
    # 結果を保存
    with open('process_results.json', 'w', encoding='utf-8') as f:
        json.dumprint(f"  ✓ クオリティスコア: {result['quality_score']}/100")