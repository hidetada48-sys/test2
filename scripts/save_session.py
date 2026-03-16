#!/usr/bin/env python3
# 【一回だけ実行】XにログインしてセッションをJSON形式で保存するスクリプト
# Windows: 起動済みChromeにCDP経由で接続
# Linux/Mac: PlaywrightのChromiumを直接起動してログイン

import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright


def get_config_dir():
    """OS判定で設定ディレクトリを返す"""
    if os.name == 'nt':  # Windows
        return Path(os.environ['USERPROFILE']) / '.x-bookmark-sync'
    else:  # Linux/Mac
        return Path.home() / '.x-bookmark-sync'


def save_on_windows(p, session_file):
    """Windows用: 起動済みChromeにCDP接続してクッキーを取得"""
    print("起動済みのChromeに接続してクッキーを取得します...")
    print()

    try:
        # 起動済みChromeにCDP経由で接続（IPv4を明示）
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    except Exception as e:
        print(f"❌ Chrome接続エラー: {e}")
        print()
        print("解決策：以下のコマンドでChromeを起動してから再実行してください")
        print()
        print('& "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
              ' --remote-debugging-port=9222'
              ' --user-data-dir="C:\\Users\\miryo\\AppData\\Local\\Google\\Chrome\\User Data"')
        print()
        print("※ Chromeを完全に閉じてから上記コマンドを実行してください")
        return False

    # 既存のコンテキスト（ウィンドウ）を取得
    contexts = browser.contexts
    if not contexts:
        print("❌ Chromeのウィンドウが見つかりません")
        browser.close()
        return False

    context = contexts[0]

    # x.com と twitter.com のクッキーを取得
    all_cookies = context.cookies(["https://x.com", "https://twitter.com"])

    if not all_cookies:
        print("❌ Xのクッキーが見つかりません")
        print("ChromeでXにログインしてから再実行してください")
        browser.close()
        return False

    # Playwright互換のstorage_state形式で保存
    storage_state = {
        "cookies": all_cookies,
        "origins": []
    }

    with open(session_file, 'w', encoding='utf-8') as f:
        json.dump(storage_state, f, ensure_ascii=False, indent=2)

    print(f"✓ クッキーを {len(all_cookies)} 件取得しました")
    browser.close()
    return True


def save_on_linux(p, session_file):
    """Linux/Mac用: PlaywrightのChromiumを直接起動してログインしてもらう"""
    print("ブラウザを起動します。Xにログインしてください...")
    print()

    # GUIあり（headless=False）でChromiumを起動
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 1280, 'height': 900})
    page = context.new_page()

    # Xのログインページを開く
    page.goto("https://x.com/login", wait_until='domcontentloaded')

    print("ブラウザが開きました。Xにログインしてください。")
    print("ログイン完了を自動検知します（最大3分）...")

    # ログイン完了を自動検知（ホーム画面に遷移するまで待つ）
    try:
        page.wait_for_url(
            lambda url: 'x.com/home' in url or ('x.com/' in url and 'login' not in url and 'flow' not in url),
            timeout=180000  # 最大3分待つ
        )
    except Exception:
        print("❌ タイムアウトしました。もう一度試してください。")
        browser.close()
        return False

    print("✓ ログインを確認しました。セッションを保存中...")

    # セッション（クッキー）を保存
    context.storage_state(path=str(session_file))

    print(f"✓ セッションを保存しました: {session_file}")
    browser.close()
    return True


def main():
    config_dir = get_config_dir()
    config_dir.mkdir(parents=True, exist_ok=True)
    session_file = config_dir / 'session.json'

    print("=" * 50)
    print("X セッション保存ツール")
    print("=" * 50)
    print()

    with sync_playwright() as p:
        # まずCDP接続を試みる（Windows・Linux共通）
        # CDP接続に失敗した場合のみLinux独自方式にフォールバック
        try:
            import urllib.request
            urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=2)
            success = save_on_windows(p, session_file)  # CDP接続方式
        except Exception:
            if os.name == 'nt':
                print("❌ Chromeが起動していません。リモートデバッグモードで起動してください。")
                success = False
            else:
                success = save_on_linux(p, session_file)  # Playwright起動方式

        if success:
            print()
            print("完了！次回からは fetch_bookmarks.py を実行するだけで")
            print("自動的にブックマークを取得できます。")


if __name__ == '__main__':
    main()
