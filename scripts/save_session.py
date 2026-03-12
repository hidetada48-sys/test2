#!/usr/bin/env python3
# 【一回だけ実行】起動済みChromeに接続してXのセッションを保存するスクリプト
# 事前にChromeをリモートデバッグモードで起動しておくこと

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

def main():
    config_dir = get_config_dir()
    config_dir.mkdir(parents=True, exist_ok=True)
    session_file = config_dir / 'session.json'

    print("=" * 50)
    print("X セッション保存ツール（リモートデバッグ方式）")
    print("=" * 50)
    print()
    print("起動済みのChromeに接続してクッキーを取得します...")
    print()

    with sync_playwright() as p:
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
            return

        # 既存のコンテキスト（ウィンドウ）を取得
        contexts = browser.contexts
        if not contexts:
            print("❌ Chromeのウィンドウが見つかりません")
            return

        context = contexts[0]

        # x.com と twitter.com のクッキーを取得
        all_cookies = context.cookies(["https://x.com", "https://twitter.com"])

        if not all_cookies:
            print("❌ Xのクッキーが見つかりません")
            print("ChromeでXにログインしてから再実行してください")
            browser.close()
            return

        # Playwright互換のstorage_state形式で保存
        storage_state = {
            "cookies": all_cookies,
            "origins": []
        }

        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(storage_state, f, ensure_ascii=False, indent=2)

        print(f"✓ クッキーを {len(all_cookies)} 件取得しました")
        print(f"✓ セッションを保存しました: {session_file}")
        print()
        print("完了！次回からは fetch_bookmarks.py を実行するだけで")
        print("自動的にブックマークを取得できます。")

        browser.close()

if __name__ == '__main__':
    main()
