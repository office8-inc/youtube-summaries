"""
生成されたMarkdownファイルをFTPサーバーにアップロードするスクリプト
"""
import os
import ftplib
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

FTP_HOST = os.getenv('FTP_HOST')
FTP_USER = os.getenv('FTP_USER')
FTP_PASSWORD = os.getenv('FTP_PASSWORD')
FTP_PORT = int(os.getenv('FTP_PORT', 21))
FTP_REMOTE_PATH = os.getenv('FTP_REMOTE_PATH', '/')


def ensure_remote_directory(ftp, remote_path):
    """リモートディレクトリが存在することを確認（なければ作成）"""
    dirs = remote_path.strip('/').split('/')
    current_path = ''
    
    for dir_name in dirs:
        if not dir_name:
            continue
        
        current_path += f'/{dir_name}'
        
        try:
            ftp.cwd(current_path)
        except ftplib.error_perm:
            # ディレクトリが存在しない場合は作成
            try:
                ftp.mkd(current_path)
                ftp.cwd(current_path)
                print(f"  ディレクトリ作成: {current_path}")
            except ftplib.error_perm as e:
                print(f"  警告: ディレクトリ作成失敗 {current_path}: {e}")


def upload_file(ftp, local_file, remote_file):
    """ファイルをFTPサーバーにアップロード"""
    try:
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file}', f)
        return True
    except Exception as e:
        print(f"  アップロード失敗: {e}")
        return False


def upload_directory(local_dir, remote_base_path):
    """ディレクトリ内のすべてのMarkdownファイルをアップロード"""
    if not all([FTP_HOST, FTP_USER, FTP_PASSWORD]):
        print("FTP設定が不完全です。.envファイルを確認してください。")
        return
    
    try:
        # FTP接続
        print(f"FTPサーバーに接続中: {FTP_HOST}")
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, FTP_PORT)
        ftp.login(FTP_USER, FTP_PASSWORD)
        print("✓ FTP接続成功")
        
        # ベースディレクトリに移動
        ensure_remote_directory(ftp, remote_base_path)
        
        # ローカルディレクトリを再帰的に走査
        local_path = Path(local_dir)
        uploaded_count = 0
        failed_count = 0
        
        for file_path in local_path.rglob('*.md'):
            # 相対パスを取得
            relative_path = file_path.relative_to(local_path)
            remote_path = str(relative_path).replace('\\', '/')
            
            # リモートディレクトリ構造を作成
            remote_dir = os.path.dirname(remote_path)
            if remote_dir:
                full_remote_dir = f"{remote_base_path}/{remote_dir}"
                ensure_remote_directory(ftp, full_remote_dir)
                ftp.cwd(full_remote_dir)
            else:
                ftp.cwd(remote_base_path)
            
            # ファイルをアップロード
            remote_filename = os.path.basename(remote_path)
            print(f"アップロード中: {relative_path} -> {remote_path}")
            
            if upload_file(ftp, str(file_path), remote_filename):
                uploaded_count += 1
                print(f"  ✓ 成功")
            else:
                failed_count += 1
                print(f"  ✗ 失敗")
        
        ftp.quit()
        
        print("\n" + "="*50)
        print("アップロード完了")
        print("="*50)
        print(f"成功: {uploaded_count} ファイル")
        print(f"失敗: {failed_count} ファイル")
        
    except Exception as e:
        print(f"FTPエラー: {e}")


def main():
    """メイン処理"""
    summaries_dir = 'summaries'
    
    if not os.path.exists(summaries_dir):
        print(f"{summaries_dir} ディレクトリが見つかりません")
        return
    
    print(f"ローカルディレクトリ: {summaries_dir}")
    print(f"リモートパス: {FTP_REMOTE_PATH}")
    
    upload_directory(summaries_dir, FTP_REMOTE_PATH)


if __name__ == "__main__":
    main()
