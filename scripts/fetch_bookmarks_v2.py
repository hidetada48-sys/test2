#!/usr/bin/python3
# XのブックマークをPlaywrightで収集し、週次統合mdファイルとして保存するスクリプト（v2）
# v1との違い: 個別ファイルなし・GDriveアップロードなし・~/test2/bookmarks/に出力

import json
import os
import sys
import time
import re
from pathlib import Path
from datetime import datetime, timezone

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout


# ===== 設定 =====

def get_config_dir():
    """設定ディレクトリを返す（v1と共有）"""
    if os.name == 'nt':
        return Path(os.environ['USERPROFILE']) / '.x-bookmark-sync'
    else:
        return Path.home() / '.x-bookmark-sync'


def load_config():
    """設定ファイルを読み込む（v1と同じconfig.jsonを使用）"""
    config_dir = get_config_dir()
    config_path = config_dir / 'config.json'

    if not config_path.exists():
        print(f"設定ファイルが見つかりません: {config_path}")
        sys.exit(1)

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    config['session_file'] = str(config_dir / 'session.json')
    # v2専用のprocessed_idsファイル（v1と独立して管理）
    config['processed_ids_file'] = str(config_dir / 'processed_ids_v2.json')

    if not Path(config['session_file']).exists():
        print("エラー: セッションファイルが見つかりません。")
        print("save_session.py を実行してXにログインしてください。")
        sys.exit(1)

    return config


def load_processed_ids(config):
    """v2の処理済みツイートIDを読み込む"""
    path = Path(config['processed_ids_file'])
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data.get('processed_ids', []))
    return set()


def save_processed_ids(config, processed_ids):
    """v2の処理済みツイートIDを保存する"""
    path = Path(config['processed_ids_file'])
    data = {
        'last_run': datetime.now().isoformat(),
        'processed_ids': list(processed_ids)
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ===== 統合mdファイルとして保存 =====

def save_as_markdown(bookmarks, output_dir):
    """全ブックマークを1つのmdファイルに保存して、ファイルパスを返す"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not bookmarks:
        return None

    # ファイル名: bookmarks_MMDD-MMDD.md（最古〜最新の日付）
    dates = [b['date'][:10] for b in bookmarks if b['date']]
    if dates:
        date_min = min(dates).replace('-', '')[4:]  # MMDD
        date_max = max(dates).replace('-', '')[4:]  # MMDD
        filename = f"bookmarks_{date_min}-{date_max}.md"
    else:
        filename = f"bookmarks_{datetime.now().strftime('%m%d')}.md"

    filepath = output_path / filename

    # ヘッダー
    period_start = min(dates) if dates else ''
    period_end = max(dates) if dates else ''
    lines = [
        f"# Xブックマーク {period_start} 〜 {period_end}",
        "",
        f"- **対象期間:** {period_start} 〜 {period_end}",
        f"- **総件数:** {len(bookmarks)}件",
        "",
        "---",
        "",
    ]

    # ブックマーク本文（収集順に羅列）
    for i, b in enumerate(bookmarks, 1):
        lines.append(f"## {i}. @{b['username']}（{b['date']}）")
        lines.append("")
        lines.append(f"**URL:** {b['url']}")
        lines.append("")
        if b['text']:
            lines.append(b['text'])
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return filepath


# ===== Playwrightでブックマーク収集（v1から流用・簡略化） =====

def fetch_bookmarks(config, processed_ids, max_bookmarks=None, from_date=None, to_date=None):
    """未処理のブックマークを取得して返す

    Args:
        processed_ids: 処理済みツイートIDのset
        max_bookmarks: 取得上限件数（--limit用）
        from_date: 取得開始日時（--from用）
        to_date:   取得終了日時（--to用）
    """
    session_file = config['session_file']
    bookmarks = []

    # 期間指定モードかどうか
    date_range_mode = from_date is not None or to_date is not None

    # v2の収集開始日（これより古いブックマークは永久に無視）
    V2_START_DATE = datetime(2026, 4, 6, tzinfo=timezone.utc)

    # 安全網: 30日以上前は対象外
    cutoff_date = datetime.now(timezone.utc).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    from datetime import timedelta
    cutoff_date = cutoff_date - timedelta(days=30)

    # V2_START_DATEと30日前の新しい方を下限として使用
    cutoff_date = max(cutoff_date, V2_START_DATE)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            storage_state=session_file,
            viewport={'width': 1280, 'height': 900},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = context.new_page()

        try:
            print("ブックマークページに移動中...")
            page.goto('https://x.com/i/bookmarks', wait_until='domcontentloaded', timeout=60000)
            time.sleep(3)

            if 'login' in page.url or 'flow' in page.url:
                print("エラー: セッションが切れています。save_session.py を再実行してください。")
                browser.close()
                sys.exit(1)

            print("ログイン確認OK。ブックマーク収集中...")

            try:
                page.wait_for_selector('[data-testid="tweet"]', timeout=15000)
            except Exception:
                pass

            seen_ids = set()
            prev_seen = 0
            scroll_attempts = 0
            max_scrolls = 30
            reached_cutoff = False

            while scroll_attempts < max_scrolls and not reached_cutoff and \
                    (max_bookmarks is None or len(bookmarks) < max_bookmarks):
                tweets = page.locator('[data-testid="tweet"]').all()

                for tweet_elem in tweets:
                    try:
                        link = tweet_elem.locator('a[href*="/status/"]').first
                        href = link.get_attribute('href', timeout=2000)
                        if not href:
                            continue

                        match = re.search(r'/status/(\d+)', href)
                        if not match:
                            continue
                        tweet_id = match.group(1)

                        if tweet_id in seen_ids:
                            continue
                        seen_ids.add(tweet_id)

                        # ユーザー名取得
                        try:
                            user_link = tweet_elem.locator('a[href^="/"][href*="status"]').first
                            user_href = user_link.get_attribute('href', timeout=2000)
                            username_match = re.match(r'/([^/]+)/status/', user_href or '')
                            tweet_username = username_match.group(1) if username_match else 'unknown'
                        except Exception:
                            tweet_username = 'unknown'

                        # 日時取得
                        dt = None
                        tweet_date = ''
                        try:
                            time_elem = tweet_elem.locator('time').first
                            tweet_date_raw = time_elem.get_attribute('datetime', timeout=2000) or ''
                            if tweet_date_raw:
                                dt = datetime.fromisoformat(tweet_date_raw.replace('Z', '+00:00'))
                                tweet_date = dt.strftime('%Y-%m-%d %H:%M:%S')
                        except Exception:
                            pass

                        # 停止判定
                        if dt:
                            # 安全網: 30日より古ければ必ず停止
                            if dt < cutoff_date:
                                reached_cutoff = True
                                break

                            if date_range_mode:
                                # 期間指定モード: --to より新しければスキップ、--from より古ければ停止
                                if to_date and dt > to_date:
                                    continue
                                if from_date and dt < from_date:
                                    reached_cutoff = True
                                    break
                            elif max_bookmarks is None:
                                # 通常モード: 処理済みIDが出たら停止
                                if tweet_id in processed_ids:
                                    reached_cutoff = True
                                    break
                            # --limit指定時は処理済みIDがあっても停止しない（phase2でスキップ）

                        # 件数上限に達したら即停止
                        if max_bookmarks is not None and len(bookmarks) >= max_bookmarks:
                            reached_cutoff = True
                            break

                        tweet_url = f"https://x.com/{tweet_username}/status/{tweet_id}"
                        bookmarks.append({
                            'id': tweet_id,
                            'username': tweet_username,
                            'text': '',
                            'date': tweet_date,
                            'url': tweet_url
                        })

                    except Exception:
                        continue

                print(f"  収集済み: {len(bookmarks)}件 (確認: {len(seen_ids)}件)", end='\r')

                page.evaluate("window.scrollBy(0, window.innerHeight * 0.8)")
                time.sleep(2.5)

                new_seen = len(seen_ids)
                if new_seen == prev_seen:
                    scroll_attempts += 1
                else:
                    scroll_attempts = 0
                    prev_seen = new_seen

            print(f"\nフェーズ1完了: {len(bookmarks)}件収集")

            # ===== フェーズ2: 詳細ページから全文取得 =====
            new_bookmarks = [b for b in bookmarks if b['id'] not in processed_ids]
            print(f"詳細ページから本文取得中... ({len(new_bookmarks)}件)")

            for i, bookmark in enumerate(new_bookmarks):
                try:
                    tweet_id = bookmark['id']
                    print(f"  [{i+1}/{len(new_bookmarks)}] {bookmark['url']}", end='\r')
                    page.goto(bookmark['url'], wait_until='domcontentloaded', timeout=30000)

                    try:
                        page.wait_for_selector('article', timeout=15000)
                    except Exception:
                        continue
                    time.sleep(2)

                    # 「もっと見る」展開
                    try:
                        show_more = page.locator('[data-testid="tweet-text-show-more-link"]')
                        if show_more.count() > 0:
                            show_more.first.click()
                            time.sleep(2)
                    except Exception:
                        pass

                    # 投稿種別判定
                    post_type = page.evaluate("""() => {
                        if (document.querySelector('[data-testid="twitterArticleReadView"]')) return 'x_article';
                        if (document.querySelector('[data-testid="tweetText"]')) return 'tweet';
                        return 'unknown';
                    }""")

                    text = ''
                    article_full_text = ''

                    if post_type == 'x_article':
                        text = page.evaluate("""() => {
                            const view = document.querySelector('[data-testid="twitterArticleReadView"]');
                            return view ? view.innerText : '';
                        }""")
                    elif post_type == 'tweet':
                        article_full_text = page.evaluate(f"""() => {{
                            const articles = document.querySelectorAll('article');
                            for (const article of articles) {{
                                if (!article.innerHTML.includes('{tweet_id}')) continue;
                                return article.innerText;
                            }}
                            return document.querySelector('article')?.innerText || '';
                        }}""")
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

                    # 引用ツイート取得
                    if article_full_text and '引用' in article_full_text:
                        try:
                            current_url = page.url
                            lines_after_quote = article_full_text.split('引用\n', 1)
                            quoted_title = ''
                            if len(lines_after_quote) > 1:
                                after_article_marker = False
                                for line in lines_after_quote[1].split('\n'):
                                    line = line.strip()
                                    if line in ('記事', 'X 記事'):
                                        after_article_marker = True
                                        continue
                                    if len(line) > 10 and not line.startswith('@') and not line.startswith('·'):
                                        if after_article_marker or not quoted_title:
                                            quoted_title = line
                                        if after_article_marker:
                                            break

                            if quoted_title:
                                try:
                                    with page.expect_navigation(timeout=8000):
                                        page.get_by_text(quoted_title, exact=False).first.click()
                                    quoted_url = page.url
                                    if quoted_url != current_url and ('x.com' in quoted_url or 'twitter.com' in quoted_url):
                                        print(f"\n    → 引用ツイート: {quoted_url[:60]}", end='')
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

                                        page.goto(bookmark['url'], wait_until='domcontentloaded', timeout=30000)
                                        page.wait_for_selector('article', timeout=10000)
                                        time.sleep(1)
                                except Exception:
                                    pass
                        except Exception:
                            pass

                    # 外部リンク取得
                    if post_type == 'tweet':
                        try:
                            card = page.locator('[data-testid="card.wrapper"] a').first
                            if card.count() > 0:
                                card_url = card.get_attribute('href')
                                if card_url and ('t.co' in card_url or card_url.startswith('https')) \
                                        and 'x.com' not in card_url and 'twitter.com' not in card_url:
                                    print(f"\n    → 外部リンク: {card_url[:60]}", end='')
                                    ext_page = context.new_page()
                                    try:
                                        ext_page.goto(card_url, wait_until='domcontentloaded', timeout=15000)
                                        time.sleep(2)
                                        ext_text = ext_page.evaluate("""() => {
                                            const selectors = ['article', 'main', '#content', '.content', 'body'];
                                            for (const sel of selectors) {
                                                const el = document.querySelector(sel);
                                                if (el && el.innerText.length > 200) return el.innerText;
                                            }
                                            return '';
                                        }""")
                                        if ext_text and len(ext_text) >= 100:
                                            bookmark['text'] = (bookmark.get('text') or '') + \
                                                f"\n\n--- 外部リンク ({ext_page.url}) ---\n" + ext_text[:5000]
                                    except Exception:
                                        pass
                                    finally:
                                        ext_page.close()
                        except Exception:
                            pass

                except Exception:
                    pass

            print(f"\n本文取得完了")

        except Exception as e:
            print(f"エラー: {e}")
            browser.close()
            raise

        browser.close()

    return bookmarks


# ===== メイン =====

def main():
    import argparse
    from datetime import timezone

    parser = argparse.ArgumentParser(description='Xブックマークを週次mdファイルとして保存する（v2）')
    parser.add_argument('--limit', type=int, default=None,
                        help='取得上限件数（テスト・初回用）例: --limit 10')
    parser.add_argument('--from', dest='from_date', default=None,
                        help='取得開始日（期間指定）例: --from 2026-04-06')
    parser.add_argument('--to', dest='to_date', default=None,
                        help='取得終了日（期間指定）例: --to 2026-04-06')
    args = parser.parse_args()

    # 日付文字列をdatetimeに変換
    from_dt = None
    to_dt = None
    if args.from_date:
        from_dt = datetime.strptime(args.from_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    if args.to_date:
        to_dt = datetime.strptime(args.to_date, '%Y-%m-%d').replace(
            hour=23, minute=59, second=59, tzinfo=timezone.utc)

    print("=== X Bookmark 週次収集ツール v2 ===\n")

    config = load_config()

    # 出力先: ~/test2/bookmarks/
    script_dir = Path(__file__).parent.parent  # ~/test2/
    output_dir = script_dir / 'bookmarks'

    processed_ids = load_processed_ids(config)
    print(f"v2処理済み件数: {len(processed_ids)}件\n")

    # モード表示
    if from_dt or to_dt:
        print(f"【期間指定モード】 {args.from_date or '制限なし'} 〜 {args.to_date or '制限なし'}\n")
    elif args.limit:
        print(f"【件数制限モード】 最大{args.limit}件\n")
    else:
        print("【通常モード】 処理済みIDが出たら自動停止\n")

    # ブックマーク収集
    all_bookmarks = fetch_bookmarks(
        config,
        processed_ids=processed_ids,
        max_bookmarks=args.limit,
        from_date=from_dt,
        to_date=to_dt
    )

    # 新着のみ抽出
    new_bookmarks = [b for b in all_bookmarks if b['id'] not in processed_ids]
    print(f"\n新着: {len(new_bookmarks)}件")

    if not new_bookmarks:
        print("新着ブックマークはありません。終了します。")
        # 何もなければ終了（スケジュール実行で新着なし時は静かに終わる）
        return

    # 統合mdファイルとして保存
    print("統合mdファイルを作成中...")
    filepath = save_as_markdown(new_bookmarks, output_dir)
    print(f"保存完了: {filepath}")

    # 処理済みIDを更新
    new_ids = {b['id'] for b in new_bookmarks}
    processed_ids.update(new_ids)
    save_processed_ids(config, processed_ids)

    # スキルがこのパスを読み取ってインデックス作成・GDriveアップロードを行う
    print(f"\nOUTPUT_FILE:{filepath}")


if __name__ == '__main__':
    main()
