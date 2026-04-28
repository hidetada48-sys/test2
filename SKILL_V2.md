---
name: x-bookmark-weekly
description: Xのブックマークを週次で自動収集し、統合mdファイルとインデックスファイルを~/test2/bookmarks/に作成してGoogle Driveにアップロードする。「週次ブックマーク」「bookmark weekly」「ブックマークv2」などと言ったとき、またはスケジュール実行時に使うこと。
---

# X Bookmark 週次収集スキル（v2）

毎週火曜0:00に自動実行。新着ブックマークを収集し、以下の2ファイルを作成する。

- `bookmarks_MMDD-MMDD.md` — 全文統合ファイル（収集順に羅載）
- `bookmarks_index_MMDD-MMDD.md` — カテゴリ別インデックス

## ステップ1: ブックマーク収集

```bash
cd ~/test2 && python3 scripts/fetch_bookmarks_v2.py
```

実行後、出力の最終行 `OUTPUT_FILE:/path/to/file.md` からファイルパスを取得する。
「新着ブックマークはありません」と出た場合はここで終了。

## ステップ2: インデックスファイルを作成

ステップ1で作成された統合mdファイルを読み込み、以下の形式でインデックスファイルを作成する。

**インデックスのファイル名:** 統合ファイルと同じ日付範囲で `bookmarks_index_MMDD-MMDD.md`

**インデックスの構成:**

```markdown
# Xブックマーク インデックス YYYY/MM/DD 〜 MM/DD

**合計：N件**

---

## カテゴリー別 目次

### A. [カテゴリ名]（N件）

| # | タイトル概要 | 投稿者 |
|---|---|---|
| A-1 | **概要** — 詳細説明 | @username |
...

---

## 全体サマリー

| カテゴリ | 件数 |
|---|---|
| A. カテゴリ名 | N件 |
| **合計** | **N件** |

---

## よく出るキーワード

- **キーワード** — 関連する投稿の傾向説明
...
```

**カテゴリ分類の方針:**
- 内容からテーマを読み取り、自然なカテゴリに分類する
- カテゴリ化が難しい場合は「その他」にまとめる
- カテゴリは5〜8個程度が目安（件数が少なければそれ以下でもよい）

インデックスファイルは統合ファイルと同じディレクトリ（`~/test2/bookmarks/`）に保存する。

## ステップ3: Google Driveにアップロード

統合ファイルのみアップロードする（インデックスファイルはアップロード不要）。

```bash
rclone copy [統合ファイルのパス] gdrive:X-Bookmarks-Weekly/ --progress
```

アップロード成功を確認したら完了を報告する。

## ステップ4: Discord通知

`~/test2/.discord_webhook` が存在する場合のみ実行する。

```bash
WEBHOOK_URL=$(cat ~/test2/.discord_webhook 2>/dev/null)
```

ファイルが存在しない場合はスキップして完了を報告する。

存在する場合は、ステップ1で取得した件数とファイル名を使って通知を送る：

```bash
curl -s -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d "{\"content\": \"週次ブックマーク収集完了\\n件数: ${COUNT}件\\nファイル: ${FILENAME}\"}"
```

`COUNT` はステップ1の出力から取得した件数、`FILENAME` は統合ファイル名（例: `bookmarks_0407-0413.md`）を使う。

送信成功（HTTPステータス2xx）を確認したら完了を報告する。

## ステップ5: INBOX に日付フォルダーを作成

統合ファイル名（例: `bookmarks_0414-0420.md`）から週の開始日を取得し、フォルダーを作成する。

```bash
# ファイル名から開始日を取得（例: 0414 → 2026-04-14）
BASENAME=$(basename [統合ファイルパス] .md)   # bookmarks_0414-0420
START_MMDD=$(echo $BASENAME | sed 's/bookmarks_\([0-9]*\)-.*/\1/')  # 0414
YEAR=$(date +%Y)
FOLDER_DATE="${YEAR}-${START_MMDD:0:2}-${START_MMDD:2:2}"  # 2026-04-14
INBOX_DIR=~/dotfiles/INBOX/bookmarks_analysis/${FOLDER_DATE}
mkdir -p "$INBOX_DIR"
```

フォルダー作成を確認したら全ステップ完了を報告する。

---

## エラー対応

- **セッション切れ**: `cd ~/test2 && python3 scripts/save_session.py` を実行してログインし直す
- **rclone失敗**: `rclone listremotes` でリモート名を確認する
- **新着0件**: 何もせず終了（正常動作）
