#!/usr/bin/env python3
# Xのログインフローをデバッグするスクリプト（スクリーンショットで確認）

import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

username = 'senmoo39'
password = os.environ.get('X_PASSWORD', '')

debug_dir = Path('/home/hidetada48/.x-bookmark-sync/debug')
debug_dir.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        viewport={'width': 1280, 'height': 900},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    )
    page = context.new_page()

    print("ログインページに移動中...")
    page.goto('https://x.com/i/flow/login', wait_until='networkidle', timeout=30000)
    time.sleep(3)
    page.screenshot(path=str(debug_dir / '01_login_page.png'))
    print("スクショ1: ログインページ")
    print(f"  URL: {page.url}")

    # ユーザー名入力
    try:
        # ユーザー名フィールドに入力（クリックしてからタイプ）
        input_field = page.locator('input[autocomplete="username"]')
        input_field.click()
        time.sleep(0.5)
        input_field.type(username, delay=50)  # 人間っぽく1文字ずつ入力
        time.sleep(1)
        page.screenshot(path=str(debug_dir / '02_username_filled.png'))
        print("スクショ2: ユーザー名入力後")

        # ボタン一覧を確認
        buttons = page.locator('button').all()
        print(f"  ボタン数: {len(buttons)}個")
        for i, btn in enumerate(buttons):
            try:
                print(f"    button[{i}]: text='{btn.inner_text()[:30]}'")
            except:
                pass

        # 「次へ」ボタンをクリック（テキストで探す）
        next_clicked = False
        for btn in buttons:
            try:
                text = btn.inner_text().strip()
                if text in ['次へ', 'Next']:
                    btn.click()
                    next_clicked = True
                    print(f"  「{text}」ボタンをクリック")
                    break
            except:
                pass

        if not next_clicked:
            # Enterキーを試す
            page.keyboard.press('Enter')
            print("  Enterキーを押しました")

        time.sleep(3)
        page.screenshot(path=str(debug_dir / '03_after_username.png'))
        print("スクショ3: 次へ後")
        print(f"  URL: {page.url}")

        # 次のページの入力欄を確認
        print(f"  入力欄: {page.locator('input').count()}個")
        inputs = page.locator('input').all()
        for i, inp in enumerate(inputs):
            try:
                print(f"    input[{i}]: type={inp.get_attribute('type')}, placeholder={inp.get_attribute('placeholder')}, autocomplete={inp.get_attribute('autocomplete')}")
            except:
                pass

        # ボタンも確認
        buttons = page.locator('button').all()
        print(f"  ボタン数: {len(buttons)}個")
        for i, btn in enumerate(buttons):
            try:
                print(f"    button[{i}]: text='{btn.inner_text()[:30]}'")
            except:
                pass

    except Exception as e:
        print(f"エラー: {e}")
        import traceback
        traceback.print_exc()

    browser.close()

print(f"\nスクリーンショットを保存しました: {debug_dir}")
