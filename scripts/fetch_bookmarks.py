#!/usr/bin/env python3
# XのブックマークをPlaywrightで取得してテキストファイルとして保存するスクリプト

import json
import os
import sys
import time
import re
from pathlib import Path
from datetime import datetime

# Playwrightのインポート
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# ===== 設定読み込み =====

def get_config_dir():
    """OS判定で設定ディレクトリを返す"""
    if os.name == 'nt':  # Windows
        return Path(os.environ['USERPROFILE']) / '.x-bookmark-sync'
    else:  # Linux/Mac
        return Path.home() / '.x-bookmark-sync'


def load_config():
    """設定ファイルを読み込む"""
    config_dir = get_config_dir()
    config_path = config_dir / 'config.json'

    if not config_path.exists():
        print(f"設定ファイルが見つかりません: {config_path}")
        print("~/.x-bookmark-sync/config.json を作成してください")
        sys.exit(1)

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # セッションファイルのパスをOSに合わせて設定
    config['session_file'] = str(config_dir / 'session.json')
    config['processed_ids_file'] = str(config_dir / 'processed_ids.json')
    config['output_dir'] = str(config_dir / 'output')

    # セッションファイルの存在確認
    if not Path(config['session_file']).exists():
        print("エラー: セッションファイルが見つかりません。")
        print("先に save_session.py を実行してXにログインしてください。")
        sys.exit(1)

    return config


def load_processed_ids(config):
    """処理済みのツイートIDを読み込む"""
    path = Path(config['processed_ids_file'])
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data.get('processed_ids', []))
    return set()


def save_processed_ids(config, processed_ids):
    """処理済みのツイートIDを保存する"""
    path = Path(config['processed_ids_file'])
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        'last_run': datetime.now().isoformat(),
        'processed_ids': list(processed_ids)
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ===== ツイートをファイルに保存 =====

def save_tweet_as_file(tweet, output_dir):
    """1ツイートを1テキストファイルとして保存する"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # ファイル名: 日付_ツイートID.txt
    date_str = tweet['date'].replace(':', '-').replace(' ', '_')
    filename = f"{date_str}_{tweet['id']}.txt"
    filepath = output_path / filename

    content = f"""投稿者: @{tweet['username']}
日時: {tweet['date']}
URL: {tweet['url']}

---

{tweet['text']}
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


# ===== Playwrightでブックマーク取得 =====

def fetch_bookmarks(config):
    """保存済みセッションを使ってXのブックマークを取得する"""
    session_file = config['session_file']
    bookmarks = []

    with sync_playwright() as p:
        # ヘッドレスモード（画面なし）で起動
        browser = p.chromium.launch(headless=True)
        # 保存済みセッション（クッキー）を読み込む
        context = browser.new_context(
            storage_state=session_file,
            viewport={'width': 1280, 'height': 900},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = context.new_page()

        try:
            # ブックマークページへ直接移動（ログイン不要）
            print("ブックマークページに移動中...")
            page.goto('https://x.com/i/bookmarks', wait_until='domcontentloaded', timeout=60000)
            time.sleep(3)

            # ログインできているか確認
            if 'login' in page.url or 'flow' in page.url:
                print("エラー: セッションが切れています。")
                print("save_session.py を再実行してログインしてください。")
                browser.close()
                sys.exit(1)

            print("ログイン状態を確認しました。ブックマークを取得中...")
            page.goto('https://x.com/i/bookmarks', wait_until='domcontentloaded', timeout=60000)
            time.sleep(3)

            # スクロールしながらツイートを収集
            prev_count = 0
            scroll_attempts = 0
            max_scrolls = 20  # 最大スクロール回数（多すぎると時間がかかる）

            while scroll_attempts < max_scrolls:
                # 現在表示されているツイートを取得
                tweets = page.locator('[data-testid="tweet"]').all()
                current_count = len(tweets)

                for tweet_elem in tweets:
                    try:
                        # ツイートIDをURLから抽出
                        link = tweet_elem.locator('a[href*="/status/"]').first
                        href = link.get_attribute('href', timeout=2000)
                        if not href:
                            continue

                        match = re.search(r'/status/(\d+)', href)
                        if not match:
                            continue
                        tweet_id = match.group(1)

                        # 既に収集済みならスキップ
                        if any(b['id'] == tweet_id for b in bookmarks):
                            continue

                        # ユーザー名取得
                        try:
                            user_link = tweet_elem.locator('a[href^="/"][href*="status"]').first
                            user_href = user_link.get_attribute('href', timeout=2000)
                            username_match = re.match(r'/([^/]+)/status/', user_href or '')
                            tweet_username = username_match.group(1) if username_match else 'unknown'
                        except Exception:
                            tweet_username = 'unknown'

                        # ツイート本文取得
                        try:
                            text_elem = tweet_elem.locator('[data-testid="tweetText"]').first
                            tweet_text = text_elem.inner_text(timeout=2000)
                        except Exception:
                            tweet_text = ''

                        # 投稿日時取得
                        try:
                            time_elem = tweet_elem.locator('time').first
                            tweet_date = time_elem.get_attribute('datetime', timeout=2000) or ''
                            # ISO形式を読みやすい形式に変換
                            if tweet_date:
                                dt = datetime.fromisoformat(tweet_date.replace('Z', '+00:00'))
                                tweet_date = dt.strftime('%Y-%m-%d %H:%M:%S')
                        except Exception:
                            tweet_date = ''

                        tweet_url = f"https://x.com/{tweet_username}/status/{tweet_id}"

                        bookmarks.append({
                            'id': tweet_id,
                            'username': tweet_username,
                            'text': tweet_text,
                            'date': tweet_date,
                            'url': tweet_url
                        })

                    except Exception as e:
                        continue

                print(f"  収集済み: {len(bookmarks)}件", end='\r')

                # スクロール
                page.keyboard.press('End')
                time.sleep(2)

                # 新しいツイートが増えなくなったら終了
                new_count = len(bookmarks)
                if new_count == prev_count:
                    scroll_attempts += 1
                else:
                    scroll_attempts = 0
                    prev_count = new_count

            print(f"\n合計 {len(bookmarks)} 件のブックマークを取得しました")

        except Exception as e:
            print(f"エラーが発生しました: {e}")
            browser.close()
            raise

        browser.close()

    return bookmarks


# ===== Google Driveへアップロード =====

def upload_to_gdrive(config, output_dir):
    """rcloneを使ってGoogle Driveにアップロードする"""
    remote = config['gdrive_remote']
    folder = config['gdrive_folder']
    destination = f"{remote}{folder}/"

    print(f"Google Driveにアップロード中... ({destination})")

    import subprocess
    result = subprocess.run(
        ['rclone', 'copy', str(output_dir), destination, '--progress'],
        capture_output=False
    )

    if result.returncode == 0:
        print("アップロード完了！")
    else:
        print("アップロードに失敗しました。rcloneの設定を確認してください。")
        sys.exit(1)


# ===== メイン処理 =====

def main():
    print("=== X Bookmark → NotebookLM 同期ツール ===\n")

    # 設定読み込み
    config = load_config()

    # 処理済みIDを読み込む
    processed_ids = load_processed_ids(config)
    print(f"処理済みブックマーク数: {len(processed_ids)}件\n")

    # ブックマーク取得
    all_bookmarks = fetch_bookmarks(config)

    # 新着だけ抽出
    new_bookmarks = [b for b in all_bookmarks if b['id'] not in processed_ids]
    print(f"新着ブックマーク: {len(new_bookmarks)}件\n")

    if not new_bookmarks:
        print("新着ブックマークはありません。終了します。")
        return

    # テキストファイルとして保存
    output_dir = Path(config['output_dir'])
    print("テキストファイルを作成中...")
    saved_files = []
    for tweet in new_bookmarks:
        filepath = save_tweet_as_file(tweet, output_dir)
        saved_files.append(filepath)
        print(f"  保存: {filepath.name}")

    print(f"\n{len(saved_files)}件のファイルを作成しました\n")

    # Google Driveにアップロード
    upload_to_gdrive(config, output_dir)

    # 処理済みIDを更新
    new_ids = {b['id'] for b in new_bookmarks}
    processed_ids.update(new_ids)
    save_processed_ids(config, processed_ids)

    print(f"\n✓ 完了！{len(new_bookmarks)}件のブックマークをGoogle Driveに保存しました。")
    print(f"NotebookLMで「Google ドライブ」→「X-Bookmarks-NotebookLM」フォルダを追加してください。")


if __name__ == '__main__':
    main()
