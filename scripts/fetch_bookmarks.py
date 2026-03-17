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
    """設定ディレクトリを返す（スクリプトの親ディレクトリ = リポジトリルート）"""
    if os.name == 'nt':  # Windows
        return Path(os.environ['USERPROFILE']) / '.x-bookmark-sync'
    else:  # Linux/Mac: Windowsと同じく ~/.x-bookmark-sync/ に統一
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

def fetch_bookmarks(config, max_bookmarks=None):
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

            # 取得対象の期間（1ヶ月前まで）
            from datetime import timezone, timedelta
            cutoff_date = datetime.now(timezone.utc) - timedelta(days=30)

            # スクロールしながらツイートを収集
            prev_count = 0
            scroll_attempts = 0
            max_scrolls = 20  # 最大スクロール回数
            reached_cutoff = False  # 期間外に達したフラグ

            # 取得上限: 引数指定がなければデフォルト25件
            fetch_limit = max_bookmarks if max_bookmarks is not None else 25

            while scroll_attempts < max_scrolls and not reached_cutoff and len(bookmarks) < fetch_limit:
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

                        # 投稿日時取得（本文はフェーズ2で詳細ページから取得）
                        try:
                            time_elem = tweet_elem.locator('time').first
                            tweet_date_raw = time_elem.get_attribute('datetime', timeout=2000) or ''
                            if tweet_date_raw:
                                dt = datetime.fromisoformat(tweet_date_raw.replace('Z', '+00:00'))
                                # 1ヶ月より古ければ打ち切り
                                if dt < cutoff_date:
                                    reached_cutoff = True
                                    break
                                tweet_date = dt.strftime('%Y-%m-%d %H:%M:%S')
                            else:
                                tweet_date = ''
                        except Exception:
                            tweet_date = ''

                        tweet_url = f"https://x.com/{tweet_username}/status/{tweet_id}"

                        # フェーズ1では本文を空にしておく（フェーズ2で取得）
                        bookmarks.append({
                            'id': tweet_id,
                            'username': tweet_username,
                            'text': '',
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

            # ===== フェーズ2: 各詳細ページを開いて全文を取得 =====
            print("詳細ページから全文を取得中...")
            for i, bookmark in enumerate(bookmarks):
                try:
                    tweet_id = bookmark['id']
                    print(f"  [{i+1}/{len(bookmarks)}] {bookmark['url']}", end='\r')
                    page.goto(bookmark['url'], wait_until='domcontentloaded', timeout=30000)

                    # article要素が出現するまで待つ（SPAの遅延読み込み対応）
                    try:
                        page.wait_for_selector('article', timeout=15000)
                    except Exception:
                        continue  # 読み込み失敗はスキップ
                    time.sleep(2)

                    # 「もっと見る」があれば展開（長文ツイート対応）
                    try:
                        show_more = page.locator('[data-testid="tweet-text-show-more-link"]')
                        if show_more.count() > 0:
                            show_more.first.click()
                            time.sleep(2)
                    except Exception:
                        pass

                    # 投稿種別を判定して本文を取得
                    post_type = page.evaluate("""() => {
                        if (document.querySelector('[data-testid="twitterArticleReadView"]')) return 'x_article';
                        if (document.querySelector('[data-testid="tweetText"]')) return 'tweet';
                        return 'unknown';
                    }""")

                    text = ''
                    article_full_text = ''
                    if post_type == 'x_article':
                        # X記事: twitterArticleReadViewから取得
                        text = page.evaluate("""() => {
                            const view = document.querySelector('[data-testid="twitterArticleReadView"]');
                            return view ? view.innerText : '';
                        }""")
                    elif post_type == 'tweet':
                        # 通常ツイート: article全体のinnerText（引用ツイートのプレビューも含む）
                        article_full_text = page.evaluate(f"""() => {{
                            const articles = document.querySelectorAll('article');
                            for (const article of articles) {{
                                if (!article.innerHTML.includes('{tweet_id}')) continue;
                                return article.innerText;
                            }}
                            return document.querySelector('article')?.innerText || '';
                        }}""")
                        # tweetText部分（ツイート本文）を優先、なければarticle全体
                        tweet_text_only = page.evaluate(f"""() => {{
                            const articles = document.querySelectorAll('article');
                            for (const article of articles) {{
                                if (!article.innerHTML.includes('{tweet_id}')) continue;
                                const tweetText = article.querySelector('[data-testid="tweetText"]');
                                if (tweetText) return tweetText.innerText;
                            }}
                            return '';
                        }}""")
                        text = tweet_text_only or article_full_text

                    if text and len(text) >= 30:
                        bookmark['text'] = text

                    # ===== 引用ツイートの全文を取得 =====
                    # article全体のテキストに「引用」が含まれていれば引用ツイートが埋め込まれている
                    if article_full_text and '引用' in article_full_text:
                        try:
                            current_url = page.url
                            # 引用部分をクリックして遷移先URLを取得
                            # innerTextの「引用」より後ろにある最初の長いテキスト行がタイトル候補
                            lines_after_quote = article_full_text.split('引用\n', 1)
                            quoted_title = ''
                            if len(lines_after_quote) > 1:
                                for line in lines_after_quote[1].split('\n'):
                                    line = line.strip()
                                    # @ユーザー名・日付・短い記号行を除外
                                    if len(line) > 10 and not line.startswith('@') and not line.startswith('·') and line not in ('記事',):
                                        quoted_title = line
                                        break

                            quoted_url = None
                            if quoted_title:
                                try:
                                    with page.expect_navigation(timeout=8000):
                                        page.get_by_text(quoted_title, exact=False).first.click()
                                    quoted_url = page.url
                                except Exception:
                                    pass

                            if quoted_url and quoted_url != current_url and '/status/' in quoted_url:
                                print(f"\n    → 引用ツイート取得中: {quoted_url[:60]}", end='')
                                page.wait_for_selector('article', timeout=10000)
                                time.sleep(2)

                                q_post_type = page.evaluate("""() => {
                                    if (document.querySelector('[data-testid="twitterArticleReadView"]')) return 'x_article';
                                    if (document.querySelector('[data-testid="tweetText"]')) return 'tweet';
                                    return 'unknown';
                                }""")

                                if q_post_type == 'x_article':
                                    q_text = page.evaluate("""() => {
                                        const view = document.querySelector('[data-testid="twitterArticleReadView"]');
                                        return view ? view.innerText : '';
                                    }""")
                                else:
                                    q_text = page.evaluate("""() => {
                                        const el = document.querySelector('[data-testid="tweetText"]');
                                        return el ? el.innerText : '';
                                    }""")

                                if q_text and len(q_text) >= 30:
                                    bookmark['text'] = (bookmark.get('text') or '') + \
                                        f"\n\n--- 引用ツイート ({quoted_url}) ---\n" + q_text

                                # 引用元ページに戻る
                                page.goto(bookmark['url'], wait_until='domcontentloaded', timeout=30000)
                                page.wait_for_selector('article', timeout=10000)
                                time.sleep(1)

                        except Exception:
                            pass

                except Exception:
                    pass  # 取得失敗してもスキップして続行

            print(f"\n全文取得完了")

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
    import argparse
    # コマンドライン引数のパース
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=None, help='取得する最大件数（例: --limit 5）')
    args = parser.parse_args()

    print("=== X Bookmark → NotebookLM 同期ツール ===\n")

    # 設定読み込み
    config = load_config()

    # 処理済みIDを読み込む
    processed_ids = load_processed_ids(config)
    print(f"処理済みブックマーク数: {len(processed_ids)}件\n")

    # ブックマーク取得（limitが指定された場合はその件数のみ取得）
    all_bookmarks = fetch_bookmarks(config, max_bookmarks=args.limit)

    # 新着だけ抽出（limitが指定された場合はさらにその件数に絞る）
    new_bookmarks = [b for b in all_bookmarks if b['id'] not in processed_ids]
    if args.limit:
        new_bookmarks = new_bookmarks[:args.limit]
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
