# Xブックマーク 2026-07-06 〜 2026-07-06

- **対象期間:** 2026-07-06 〜 2026-07-06
- **総件数:** 2件

---

## 1. @ClaudeCode_love（2026-07-06 02:32:00）

**URL:** https://x.com/ClaudeCode_love/status/2073958110411284619

【速報】
Anthropicが「自分で育つAIエージェント」の作り方を
3時間分のワークショップで出してたエージェント構築のロードマップはこれ

https://
x.com/0xMovez/status
/2073765125958348964/video/1
…
・最初のClaudeエージェントを作る
・Claudeに記憶を持たせる
・自律的に動く形へ進める
・先回りして動くエージェントにする
・ツールとSkillsで自己改善させる
・5本まとめて無料で見られる
ここがヤバい。

もう「プロンプトを1個書く」話じゃない。

同じClaudeでも
仕事の記憶
実行手順
改善ループ
まで持たせると別物になる。

これは「便利なAI」じゃない。
“小さな開発チーム”を作る教材。

次にエージェント作る前に
次にSkillsを入れる前に
この3時間、先に見た方がいい。

自己改善エージェントの全体像は、Skills 67選の記事と合わせると一気に見える

--- 引用ツイート (https://x.com/ClaudeCode_love/status/2045082723027751079) ---
【保存推奨】Claude Skills 67選──ポテンシャルを100%引き出し“開発チーム化”する方法
16
336
3,115
318万
皆さんSkillsって多すぎてどれを入れればいいか迷いますよね😱
大丈夫です。マジでこの記事で全部解決します！最後まで見ていただけたら本当にあなたのClaudeが10倍頭良くなることをお約束します！🔥
ところで、Claude,ClaudeCode普段使っててこんな悩みありませんか？
・Claude Codeを使ってるけど、毎回同じ説明を繰り返してる
・Skillsという機能があるのは知ってるけど、何を入れればいいのかわからない
・設計→開発→テスト→ドキュメントの流れを自動化したい
・Claude Codeを「ただのコード補完」以上に使いこなしたい
今、海外のAI・クリプト領域で影響力のあるMr. Buzzoni氏（@polydao）が投稿した「Claude Skills 67選」が124万ビューの大バズ中😳
今回はその内容をわかりやすく噛み砕いて解説します👇
元ポストはこちら：https://x.com/polydao/status/2044317956893471081?s=20
■ そもそも𝗖𝗹𝗮𝘂𝗱𝗲 𝗦𝗸𝗶𝗹𝗹𝘀とは何か
ほとんどの人はClaude Codeを「普通に指示するだけで」使っています。質問して、回答を得て、それで終わり。
でもClaude Codeには「Skills」という仕組みがあり、これを使うとClaude Codeは設計者・レビュアー・デバッガー・ドキュメントライターを兼ねた開発チームとして機能します。
Skillとは、SKILL.mdファイルが入ったフォルダのことです。このファイルには「特定の作業をどうやるか」がステップバイステップで書かれています。制約、例、ヘルパースクリプト、テンプレートも含められます。
つまり、毎回セッションのたびに「こうやって、ああやって」と説明する必要がなくなります。一度Skillとしてインストールすれば、以降はずっと再利用できます。
インストールは基本的にこのコマンド：
npx skills@latest add [リポジトリ/パス]
主要なSkillsのソース：
・Anthropic公式：github.com/anthropics/skills
・Matt Pocock（15,000スター超）：github.com/mattpocock/skills
・コミュニティマーケットプレイス（66,000以上のSkills）：skillsmp.com
■ 𝗠𝗲𝘁𝗮 𝗦𝗸𝗶𝗹𝗹𝘀 ── まず最初に入れるべき「スキルを作るスキル」
他のすべてのSkillの土台になるのがMeta Skillsです。
𝗦𝗸𝗶𝗹𝗹 𝗖𝗿𝗲𝗮𝘁𝗼𝗿（これクッッッソ有益）
あなたのタスクでClaudeをベンチマークし、実際の実行結果に基づいて新しいSkillの作成と改善を支援します。
使い方：ワークフローを箇条書きで説明 → SKILL.md案を提案させる → 3〜5回テストして失敗を分析 → 改善させる
リンク：github.com/anthropics/skills/tree/main/skills/skill-creator
𝗪𝗿𝗶𝘁𝗲 𝗮 𝗦𝗸𝗶𝗹𝗹
適切な構造・段階的開示・バンドルリソースを備えたSkillの書き方をガイドします。Skill Creatorで生の下書きができたら、これで構造を整えます。
インストール：npx skills@latest add mattpocock/skills/write-a-skill
リンク：github.com/mattpocock/skills/tree/main/write-a-skill
𝗙𝗶𝗻𝗱 𝗦𝗸𝗶𝗹𝗹𝘀
SkillsMPなどの公開マーケットプレイスから、あなたのユースケースに合ったSkillを検索します。新しいSkillを書く前に、まず既存のものを探してフォークするのが鉄則です。
マーケットプレイス：skillsmp.com
■ 𝗣𝗹𝗮𝗻𝗻𝗶𝗻𝗴 & 𝗗𝗲𝘀𝗶𝗴𝗻 ── 「間違ったものを作る」を防ぐスキル群
ここが最も重要かもしれません。設計段階のSkillsは、開発後の手戻りの80%を防ぎます。
その上でここではそんな「間違ったものを作る」を防ぐスキル群を紹介します👇
𝗚𝗿𝗶𝗹𝗹 𝗠𝗲
Claudeが容赦なく質問を投げかけ、意思決定ツリーの全分岐が解決するまで追い詰めます。新機能、リファクタ、リスクの高いマイグレーションに使います。
インストール：npx skills@latest add mattpocock/skills/grill-me
データモデル、エッジケース、障害モード、既存システムとの関連について質問されます。一度辛抱強く答えれば、後で火消しに追われることがなくなります。
𝗪𝗿𝗶𝘁𝗲 𝗮 𝗣𝗥𝗗
インタラクティブなインタビュー、コードベース探索、モジュール設計を通じてPRD（プロダクト要件定義書）を作成し、GitHubイシューとして登録します。
インストール：npx skills@latest add mattpocock/skills/write-a-prd
𝗣𝗥𝗗 𝘁𝗼 𝗣𝗹𝗮𝗻
PRDをトレーサーバレット方式の垂直スライスで多段階の実装計画に変換します。単なるタスク分解ではなく、統合リスクを実際に下げる順序を出してくれます。
インストール：npx skills@latest add mattpocock/skills/prd-to-plan
𝗣𝗥𝗗 𝘁𝗼 𝗜𝘀𝘀𝘂𝗲𝘀
PRDを独立して着手可能なGitHubイシューに分解します。垂直スライスとブロッキング関係付き。
インストール：npx skills@latest add mattpocock/skills/prd-to-issues
𝗗𝗲𝘀𝗶𝗴𝗻 𝗮𝗻 𝗜𝗻𝘁𝗲𝗿𝗳𝗮𝗰𝗲
並列サブエージェントを使い、1つのモジュールに対して3〜5個の根本的に異なるインターフェース設計を生成します。1つだけではなく、異なるトレードオフを持つ複数の選択肢が得られます。
インストール：npx skills@latest add mattpocock/skills/design-an-interface
𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗥𝗲𝗳𝗮𝗰𝘁𝗼𝗿 𝗣𝗹𝗮𝗻
ユーザーインタビューを通じて小さなコミット単位の詳細なリファクタ計画を作成し、GitHubイシューとして登録します。
インストール：npx skills@latest add mattpocock/skills/request-refactor-plan
■ 𝗖𝗼𝗱𝗲 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗺𝗲𝗻𝘁 ── Claude Codeを「規律ある開発パートナー」に変える
𝗧𝗗𝗗
厳格なテストファースト・red-green-refactorループを強制します。まず失敗するテスト → それを通す最小のコード → テストを維持したままリファクタ。
インストール：npx skills@latest add mattpocock/skills/tdd
𝗧𝗿𝗶𝗮𝗴𝗲 𝗜𝘀𝘀𝘂𝗲
「なぜ壊れてるのか全くわからない」時のスキル。コードベースを探索して根本原因を特定し、TDDベースの修正計画をGitHubイシューとして登録します。
インストール：npx skills@latest add mattpocock/skills/triage-issue
𝗤𝗔
機能に対するフルQAパスを実行。ブロッキング関係付きのイシュー分解を行います。PR前に毎回使うことで、エッジケースを洗い出してリグレッションなしで出荷できます。
インストール：npx skills@latest add mattpocock/skills/qa
𝗜𝗺𝗽𝗿𝗼𝘃𝗲 𝗖𝗼𝗱𝗲𝗯𝗮𝘀𝗲 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲
コードベースのアーキテクチャ改善ポイントを探索。ホットスポットの特定、2〜3のリファクタ戦略の提案、各戦略のリスク・工数・インパクトの詳細を出してくれます。
インストール：npx skills@latest add mattpocock/skills/improve-codebase-architecture
𝗦𝘆𝘀𝘁𝗲𝗺𝗮𝘁𝗶𝗰 𝗗𝗲𝗯𝘂𝗴𝗴𝗶𝗻𝗴
「とりあえず変えてみる」を禁止する4段階デバッグ方法論。再現 → 最小の失敗テスト作成 → 根本原因の絞り込み → 単一修正 → テスト検証。
リンク：github.com/obra/superpowers/tree/main/skills/systematic-debugging
𝗔𝘂𝘁𝗼-𝗖𝗼𝗺𝗺𝗶𝘁 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀
ステージされたdiffを読み、type・scope・bodyを含むConventional Commitメッセージを自動生成。深夜2時に「fix stuff」と書く必要がなくなります。
リンク：github.com/anthropics/skills/tree/main/skills/auto-commit
𝗖𝗼𝗱𝗲 𝗥𝗲𝘃𝗶𝗲𝘄
セキュリティ・パフォーマンス・エラーハンドリング・アーキテクチャの体系的レビュー。「セキュリティ重視レビュー」「パフォーマンス重視レビュー」など焦点を指定できます。
リンク：github.com/anthropics/skills
𝗦𝘂𝗽𝗲𝗿𝗽𝗼𝘄𝗲𝗿𝘀
TDD・デバッグ・リファクタリング・実行の実戦テスト済みSkill一式。デフォルトの「エンジニアリング脳」レイヤーとして使えます。
リンク：github.com/obra/superpowers
■ 𝗧𝗼𝗼𝗹𝗶𝗻𝗴 & 𝗦𝗲𝘁𝘂𝗽 ── 「一度やったら二度と触らない」系スキル
𝗦𝗲𝘁𝘂𝗽 𝗣𝗿𝗲-𝗖𝗼𝗺𝗺𝗶𝘁
Husky pre-commitフック + lint-staged + Prettier + 型チェック + テストをセットアップ。新しいリポジトリごとに実行すべき。
インストール：npx skills@latest add mattpocock/skills/setup-pre-commit
𝗚𝗶𝘁 𝗚𝘂𝗮𝗿𝗱𝗿𝗮𝗶𝗹𝘀 𝗳𝗼𝗿 𝗖𝗹𝗮𝘂𝗱𝗲 𝗖𝗼𝗱𝗲
push、reset --hard、cleanなどの危険なgitコマンドを実行前にブロックするフックを設定。本番リポジトリでClaude Codeを使うなら必須のセーフティネットです🚨
インストール：npx skills@latest add mattpocock/skills/git-guardrails-claude-code
𝗗𝗲𝗽𝗲𝗻𝗱𝗲𝗻𝗰𝘆 𝗔𝘂𝗱𝗶𝘁𝗼𝗿
package.jsonの古い・脆弱・放棄されたパッケージをスキャンし、優先度付きの修正リストを出力。
リンク：github.com/ComposioHQ/awesome-claude-skills
■ 𝗪𝗿𝗶𝘁𝗶𝗻𝗴 & 𝗞𝗻𝗼𝘄𝗹𝗲𝗱𝗴𝗲 ── ドキュメント・記事・用語定義
𝗘𝗱𝗶𝘁 𝗔𝗿𝘁𝗶𝗰𝗹𝗲
「文法修正」ではなく、議論の再構成・不要部分のカット・各セクションの論点を研ぎ澄ませるレベルの編集を行います。
インストール：npx skills@latest add mattpocock/skills/edit-article
𝗨𝗯𝗶𝗾𝘂𝗶𝘁𝗼𝘂𝘀 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲
DDD（ドメイン駆動設計）スタイルのユビキタス言語用語集を会話から抽出。「event」「order」「user」がチーム内で異なる意味で使われている問題を解決します。コードを書く前にドメイン言語を定義・統一することで、コードベース・ドキュメント・会話が同じ言葉を共有できます。
インストール：npx skills@latest add mattpocock/skills/ubiquitous-language
𝗔𝗣𝗜 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿
ルートを読み取り、例・エラーコード・認証要件付きのOpenAPI/Swaggerドキュメントを生成。APIを出荷したのにドキュメントを書いてない時に。30秒で完了。
リンク：github.com/ComposioHQ/awesome-claude-skills
𝗢𝗯𝘀𝗶𝗱𝗶𝗮𝗻 𝗩𝗮𝘂𝗹𝘁
Obsidian Vaultの検索・作成・管理をwikilinksとインデックスノート付きで行います。Vault内を自動でナビゲートし、新しいノートを作成し、リンクの一貫性を維持します。
インストール：npx skills@latest add mattpocock/skills/obsidian-vault
■ 𝗨𝗜 / 𝗗𝗲𝘀𝗶𝗴𝗻 / 𝗙𝗿𝗼𝗻𝘁𝗲𝗻𝗱 ── デザイン系スキル
𝗙𝗿𝗼𝗻𝘁𝗲𝗻𝗱 𝗗𝗲𝘀𝗶𝗴𝗻
モダンでクリーンなUI生成をガイド。
リンク：github.com/anthropics/skills/tree/main/skills/frontend-design
𝗧𝗵𝗲𝗺𝗲 𝗙𝗮𝗰𝘁𝗼𝗿𝘆
テキストプロンプト1つから完全なカラーパレットとテーマを生成。「落ち着いたフィンテック、信頼感、ダークアクセント」→ トークン付きパレット → Tailwind/CSS変数に適用。
リンク：github.com/anthropics/skills/tree/main/skills/theme-factory
𝗪𝗲𝗯 𝗔𝗿𝘁𝗶𝗳𝗮𝗰𝘁𝘀 𝗕𝘂𝗶𝗹𝗱𝗲𝗿
自然言語からインタラクティブなダッシュボード・計算機・ツールを構築。
リンク：github.com/anthropics/skills/tree/main/skills/web-artifacts-builder
𝗕𝗿𝗮𝗻𝗱 𝗚𝘂𝗶𝗱𝗲𝗹𝗶𝗻𝗲𝘀
全ての新しいコンポーネントにブランドシステムを強制適用。
リンク：github.com/anthropics/skills/tree/main/skills/brand-guidelines
■ 𝗕𝘂𝘀𝗶𝗻𝗲𝘀𝘀 / 𝗦𝗮𝗹𝗲𝘀 / 𝗠𝗮𝗿𝗸𝗲𝘁𝗶𝗻𝗴 ── ビジネス系スキル
𝗦𝘁𝗿𝗶𝗽𝗲 𝗜𝗻𝘁𝗲𝗴𝗿𝗮𝘁𝗶𝗼𝗻
安全な決済フロー・Webhook・サブスクリプションのセットアップ。初歩的なAPIミスを防ぎます。
リンク：github.com/wshobson/agents/tree/main/plugins/payment-processing/skills/stripe-integration
𝗠𝗮𝗿𝗸𝗲𝘁𝗶𝗻𝗴 𝗦𝗸𝗶𝗹𝗹𝘀
CRO・コピーライティング・メールフローなど20以上のスキル集。
リンク：github.com/coreyhaines31/marketingskills
𝗖𝗹𝗮𝘂𝗱𝗲 𝗦𝗘𝗢
テクニカルSEO監査、スキーマ、オンページ最適化の完全版。
リンク：github.com/AgriciDaniel/claude-seo
𝗗𝗼𝗺𝗮𝗶𝗻 𝗡𝗮𝗺𝗲 𝗕𝗿𝗮𝗶𝗻𝘀𝘁𝗼𝗿𝗺𝗲𝗿
プロダクト名の生成とドメインの空き状況チェック。新しいアプリやマイクロブランドの立ち上げ時に。
リンク：github.com/Microck/ordinary-claude-skills/tree/main/skills_all/domain-name-brainstormer
■ 𝗢𝗳𝗳𝗶𝗰𝗲 & 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁𝘀 ── オフィス系スキル
𝗣𝗗𝗙 / 𝗗𝗢𝗖𝗫 / 𝗣𝗣𝗧𝗫 / 𝗫𝗟𝗦𝗫
テーブル抽出・フォーム入力・PDF結合、Wordの変更履歴付き編集、スライドデッキの作成・編集、平文からの数式・ピボットテーブル・チャート作成。全てAnthropic公式から提供。
リンク：github.com/anthropics/skills/tree/main/skills/
𝗗𝗼𝗰 𝗖𝗼-𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝗻𝗴
あなたとClaudeのリアルタイム共同執筆。
リンク：github.com/anthropics/skills/tree/main/skills/doc-coauthoring
■ 𝗠𝘂𝗹𝘁𝗶-𝗔𝗴𝗲𝗻𝘁 ── マルチエージェント系スキル
𝗦𝘁𝗼𝗰𝗵𝗮𝘀𝘁𝗶𝗰 𝗠𝘂𝗹𝘁𝗶-𝗔𝗴𝗲𝗻𝘁 𝗖𝗼𝗻𝘀𝗲𝗻𝘀𝘂𝘀
多数のサブエージェントを生成して同じ問題を解かせ、回答を集約。戦略判断・アーキテクチャ選択・リスク分析に。
リンク：github.com/hungv47/meta-skills
𝗠𝗼𝗱𝗲𝗹-𝗰𝗵𝗮𝘁（𝗗𝗲𝗯𝗮𝘁𝗲）
複数のClaudeインスタンスをディベートさせてアイデアをストレステスト。2〜3の大きな賭けの間で迷っている時に。
リンク：github.com/tommasinigiovanni/conclave
𝗙𝗶𝗿𝗲𝗰𝗿𝗮𝘄𝗹 𝗦𝗸𝗶𝗹𝗹
一般的なスクレイパーをブロックする複雑なサイトから構造化データを抽出。
リンク：github.com/mendableai/firecrawl
■ おすすめの導入順序
元記事で提案されている導入順序がかなり実践的なので、そのまま紹介します：
1. まずMeta Skillsから ── Write a SkillとSkill Creatorを入れて、Skillsの作成と修正ができる状態にする
2. Planning系を追加 ── Grill Me、Write a PRD、PRD to Plan、PRD to Issues、Design an Interface。これで手戻りの80%を防止
3. コードの安全装置 ── Git Guardrails、Setup Pre-Commit、TDD、Systematic Debugging、Triage Issue。全リポジトリに入れる
4. Superpowersをベースレイヤーとして追加 ── github.com/obra/superpowers
5. ビジネス系スキルを上に重ねる ── Marketing Skills、Claude SEO、Lead Research、Content Researcher
6. SkillsMPで穴を埋める ── skillsmp.com で新しい課題に当たったら、作る前にまず検索
重要なのは、Skillsは「全部入れる」ものではなく「必要なものを選んで入れる」ものだということです。各セクションから1つずつ選んで今日インストールする。1週間後には「これなしでは仕事できない」と感じるはずです🔥
この記事が少しでも参考になった方へ。
𝗖𝗹𝗮𝘂𝗱𝗲 𝗖𝗼𝗱𝗲 𝗦𝘁𝘂𝗱𝗶𝗼 @ 𝗝𝗮𝗽𝗮𝗻（@ClaudeCode_love）は、
Claude Codeガチ勢3人で運営しているアカウントです。
実務レベルのCLI活用・自動化を毎日発信しています。
現在は上場企業とAIエージェントを共同開発中。
普段の発信内容👇
・Claude CodeやClaudeを活用したリアルなプロダクト開発事例
・Claude Code活用／Vibe Coding／開発トレンドの整理
・海外のClaude Codeに関する最新情報
開発思想から設計、実装、改善まで、
「作って終わり」ではなく動くプロダクトを世に出すところまでを
海外の情報や１次情報をまとめています。
ご関心のある方は、ぜひフォローしてチェックしてみてください👀有益だと思います！
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 2. @daniel_mac8（2026-07-06 15:25:18）

**URL:** https://x.com/daniel_mac8/status/2074152718407520628

Claude Fable 5 は Claude サブスクライバー向けに *明日* リリースされます。

以下のことを必ず実行してください。

使わなければ失う。

---
