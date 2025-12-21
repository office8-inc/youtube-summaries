<?php
/**
 * summariesディレクトリからMarkdownファイルの一覧を取得するPHPスクリプト
 */

header('Content-Type: application/json; charset=utf-8');

// summariesディレクトリのパス
$summariesDir = '../summaries';

// Markdownファイルを再帰的に検索
function findMarkdownFiles($dir, $summariesDir) {
    $articles = [];
    
    if (!is_dir($dir)) {
        return $articles;
    }
    
    $iterator = new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator($dir, RecursiveDirectoryIterator::SKIP_DOTS),
        RecursiveIteratorIterator::SELF_FIRST
    );
    
    foreach ($iterator as $file) {
        if ($file->isFile() && $file->getExtension() === 'md') {
            $filePath = $file->getPathname();
            $relativePath = str_replace($dir . DIRECTORY_SEPARATOR, '', $filePath);
            $relativePath = str_replace('\\', '/', $relativePath);
            
            // Markdownファイルの内容を読み込んで情報を抽出
            $content = file_get_contents($filePath);
            
            // タイトルを抽出（最初の# 見出し）
            $title = 'タイトルなし';
            if (preg_match('/^#\s+(.+)$/m', $content, $matches)) {
                $title = trim($matches[1]);
                // 絵文字を除去
                $title = preg_replace('/[\x{1F300}-\x{1F9FF}]/u', '', $title);
                $title = trim($title);
            }
            
            // チャンネル名を抽出
            $channel = 'Unknown Channel';
            if (preg_match('/\*\*チャンネル\*\*:\s*(.+)$/m', $content, $matches)) {
                $channel = trim($matches[1]);
            }
            
            // 日付を抽出（ファイルのパスから）
            $pathParts = explode('/', $relativePath);
            if (count($pathParts) >= 3) {
                $year = $pathParts[0];
                $month = $pathParts[1];
                $date = "$year-$month-01"; // デフォルトで月初
                
                // ファイル名から日付を抽出できる場合
                $filename = basename($relativePath, '.md');
                if (preg_match('/^(\d{4})(\d{2})(\d{2})/', $filename, $matches)) {
                    $date = "{$matches[1]}-{$matches[2]}-{$matches[3]}";
                }
            } else {
                $date = date('Y-m-d', $file->getMTime());
            }
            
            $articles[] = [
                'title' => $title,
                'channel' => $channel,
                'date' => $date,
                'path' => $summariesDir . '/' . $relativePath
            ];
        }
    }
    
    return $articles;
}

try {
    $articles = findMarkdownFiles($summariesDir, $summariesDir);
    echo json_encode($articles, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'error' => $e->getMessage()
    ], JSON_UNESCAPED_UNICODE);
}
?>
