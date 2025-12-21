"""
新着動画を一括処理してクオリティチェックを行うスクリプト
"""
import os
import json
from datetime import datetime
from improved_summarize_youtube import main as summarize_video
from github import Github
from dotenv import load_dotenv
import pytz

load_dotenv()

GH_TOKEN = os.getenv('GH_TOKEN')
GITHUB_REPO = os.getenv('GITHUB_REPO')
QUALITY_THRESHOLD = 50  # クオリティスコアの閾値


def create_output_directory(video_info):
    """動画情報から出力ディレクトリを作成"""
    jst = pytz.timezone('Asia/Tokyo')
    published_at = datetime.fromisoformat(video_info['published_at'].replace('Z', '+00:00'))
    published_jst = published_at.astimezone(jst)
    
    year = published_jst.strftime('%Y')
    month = published_jst.strftime('%m')
    
    output_dir = os.path.join('summaries', year, month)
    os.makedirs(output_dir, exist_ok=True)
    
    return output_dir


def create_github_issue(video_info, quality_score, file_path):
    """クオリティが低い場合にGitHub Issueを作成"""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        print("⚠️  GitHub設定がありません。Issueを作成できません。")
        return None
    
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(GITHUB_REPO)
        
        title = f"📝 要約レビュー必要: {video_info['title']}"
        body = f"""## 要約記事のクオリティが低いため、レビューが必要です

### 動画情報
- **タイトル**: {video_info['title']}
- **チャンネル**: {video_info['channel']}
- **URL**: {video_info['url']}
- **投稿日**: {video_info['published_at']}

### クオリティ評価
- **スコア**: {quality_score}/100
- **閾値**: {QUALITY_THRESHOLD}/100

### ファイル
- `{file_path}`

### 対応方法

1. 生成されたMarkdownファイルを確認
2. 内容を手動で修正・改善
3. 問題なければこのIssueをクローズ
4. 削除する場合はファイルを削除してクローズ

---

⚠️ **自動生成された要約が不十分な可能性があります**
"""
        
        issue = repo.create_issue(
            title=title,
            body=body,
            labels=['review-needed', 'auto-generated']
        )
        
        print(f"✓ GitHub Issueを作成しました: #{issue.number}")
        return issue.number
        
    except Exception as e:
        print(f"GitHub Issueの作成に失敗: {e}")
        return None


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
                
                # クオリティチェック
                if result['quality_score'] < QUALITY_THRESHOLD:
                    print(f"  ⚠️  クオリティスコア低: {result['quality_score']}/100")
                    issue_number = create_github_issue(
                        video, 
                        result['quality_score'],
                        result['file_path']
                    )
                    result['needs_review'] = True
                    result['issue_number'] = issue_number
                else:
                    print(f"  ✓ クオリティスコア: {result['quality_score']}/100")
                    result['needs_review'] = False
                
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
    print(f"レビュー必要: {sum(1 for r in results if r['result'].get('needs_review', False))}")
    print(f"問題なし: {sum(1 for r in results if not r['result'].get('needs_review', False))}")
    
    # 結果を保存
    with open('process_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
