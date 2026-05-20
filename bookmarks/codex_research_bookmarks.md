# Codex関連ブックマーク記事まとめ（2026-04-28〜2026-05-09）

**作成日：** 2026-05-15
**元データ：** bookmarks_0428-0504.md / bookmarks_0505-0509.md（計5件）

---

## 記事一覧

### F-1：Codexで5分15秒でLP制作（@hanjuku_yanen）
**投稿日：** 2026-05-04
**URL：** https://x.com/hanjuku_yanen/status/2051251198934814747

完全ゼロスタートから5分15秒でLPを制作。やったことはアプリインストール（5分）＋口頭指示（15秒）のみ。引用元の@makosan_writerも「1年前にこれがあればFIREできた」と絶賛。

---

### C-1：Codex移行を推奨（@gagarot200）
**投稿日：** 2026-05-08
**URL：** https://x.com/gagarot200/status/2052636616687329432

Claude最新モデル（Opus-4.7含む）の品質が2024年レベルに低下、Codexの使用者が世界一に。Claude CodeからCodexへの移行を推奨。

**Codexの基本概念（記事より）：**
- 「チャットAI」ではなく「作業環境」として設計
- ローカルフォルダを作業対象に取り込み、ファイル読み書き・アプリ構築・GitHub連携・定期実行まで可能
- `agents.md`（CLAUDE.mdに相当するプロジェクト説明書）を持てる
- 基本3原則：「フォルダの中で作業する」「計画を立ててから動かす」「うまくいった手順を再利用できる形で残す」

---

### C-2：Codex一択（デザイナー目線）（@halukik_0520）
**投稿日：** 2026-05-06
**URL：** https://x.com/halukik_0520/status/2051822420760395850

3〜4月はClaude Code一択だったが、今はCodex一択に転換。理由：
- 「仕事が終わる」＝会話で終わらず成果物が残る
- Image 2.0との組み合わせが強力：Codexで構成→Image 2.0でビジュアル→HTML化→修正→公開

**LP制作フロー（30分）：**
1. Codexで構成を整理
2. Image 2.0でビジュアル案を出す
3. 良かった案をHTML化
4. 注釈で細部を修正
5. 必要なら公開

---

### C-3：AIでLP外注不要（@MakeAI_CEO）
**投稿日：** 2026-05-06
**URL：** https://x.com/MakeAI_CEO/status/2051904542896443439

プロンプトを作り込めばCodexでプロ品質のLPが作れる。デザイナー・マーケターにも推奨。

---

### C-4：Claude Code vs Codex 徹底比較（@MakeAI_CEO）
**投稿日：** 2026-05-06（引用元）
**URL：** https://x.com/MakeAI_CEO/status/2050133272022094057

大型比較記事（推定5万字）。副業・SNSマネタイズ文脈での徹底比較。

#### 性能比較
| ベンチマーク | Claude Code | Codex |
|---|---|---|
| SWE-bench Verified（バグ修正） | **87.6%**（Opus 4.7） | 85.0%（GPT-5.4） |
| SWE-bench Pro（難問） | **64.3%** | 57.7% |
| Terminal-Bench 2.0（CLI精度） | 65.4% | **77.3%**（12pt差） |
| コード品質スコア | 76.8点 | **81.0点** |

#### 速度
- 対話・小さい修正：Claude Codeが速い
- 大きいタスク・ゼロからの実装：Codexが速い
- **要約：「対話して進めるならClaude Code、投げて待つならCodex」**

#### コスト
| プラン | 費用 | 特徴 |
|---|---|---|
| Codex（ChatGPT Plus） | 月20ドル | 一日中使える・コスパ最強 |
| Claude Code Max 5x | 月100ドル | 本格利用の実質最低ライン |
| 両刀 | 月120ドル | 海外Indie Hackersの標準構成 |

#### 使い分けパターン
1. **役割分担型**：Claude Codeで設計・Plan → Codexで実装・品質チェック
2. **Rate Limit Arbitrage**：`smux`（tmuxツール）で両者を並列運用。片方がレート制限に達したらもう片方で継続

#### エコシステム比較
| 項目 | Claude Code | Codex |
|---|---|---|
| カスタマイズ | Skills・Subagent・MCP・Plugins・Hooks | カスタムコマンド程度 |
| 連携 | Obsidian・Git worktree・VS Code拡張 | ChatGPT統合・GitHub PR @codexタグ・macOSアプリ |
| 対象ユーザー | エンジニア・高度カスタマイズ志向 | ChatGPT慣れ・非エンジニア・入門向け |
| computer use | なし | macOSアプリ操作対応 |

#### 向いている人
- 対話しながら進めたい・Obsidian利用・高カスタマイズ → **Claude Code**
- ChatGPT慣れ・まず試したい・GitHub PRレビュー・コスパ重視 → **Codex**
- コマンド多用・定型CLI・ゼロからの実装 → **Codex優位**
- 月予算20ドルで始めたい → **Codex一択**

#### 副業ROI試算（Claude Code＋Codex併用時）
| 作業 | AI前 | AI後 |
|---|---|---|
| LP制作1本 | 20〜30万円・2週間 | 3〜5時間 |
| note有料記事1本 | 8〜15時間 | 1〜2時間 |
| 講座スライド15枚 | 10万円・1週間 | 3〜5時間 |
| 会員サイト構築 | 50〜100万円 | 1〜3日 |

---

## 総評

「Codex最強・Claude Code終了」という煽り投稿が多いが、精読すると**「どちらか選ぶ」より「使い分ける」が現実解**に収束。特にMakeAI_CEO記事が最も詳細な一次情報。Codexの強みはコスパと入門しやすさ、Claude Codeの強みはカスタマイズ性と対話精度。
