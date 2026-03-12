#!/usr/bin/env python3
# 【一回だけ実行】Xに手動でログインしてセッションを保存するスクリプト
# このスクリプトはブラウザ画面が表示される環境（Windows等）で実行すること

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
    print("X セッション保存ツール")
    print("=" * 50)
    print()
    print("ブラウザが開きます。Xに手動でログインしてください。")
    print("ログイン完了後、ホーム画面が表示されるまで待ってから")
    print("このターミナルに戻って Enter を押してください。")
    print()

    with sync_playwright() as p:
        # GUI表示モード（headless=False）でブラウザ起動
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1280, 'height': 900}
        )
        page = context.new_page()

        # Xのログインページを開く
        page.goto('https://x.com/login')

        print("ブラウザでXにログインしてください...")
        print("（ログインが完了したら Enter を押してください）")
        input()

        # セッション（クッキー＋ローカルストレージ）を保存
        context.storage_state(path=str(session_file))
        print(f"✓ セッションを保存しました: {session_file}")

        browser.close()

    print()
    print("完了！次回からは fetch_bookmarks.py を実行するだけで")
    print("自動的にブックマークを取得できます。")

if __name__ == '__main__':
    main()
