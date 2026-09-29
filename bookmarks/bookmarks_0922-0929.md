# Xブックマーク 2026-09-22 〜 2026-09-29

- **対象期間:** 2026-09-22 〜 2026-09-29
- **総件数:** 18件

---

## 1. @claudecode84（2026-09-29 04:33:00）

**URL:** https://x.com/claudecode84/status/2104791529269141765

Claude Codeからやっと登場

古いプロンプトを全自動で掃除する
機能がOpus5.5にめっちゃ効く　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　

Claude Code v2.1.283で
 /doctor prompt-audit が追加

これ、かなり重要で使い方はシンプル。
/doctor prompt-audit
または
/checkup prompt-audit
を実行するだけ。

すると、
・CLAUDE.md
・Skills
・Agents
の中にある、
旧モデル向けの古い指示
をまとめて監査してくれる。

例えば

・「必ず二重チェックしろ」
・「ステップバイステップで考えろ」
・「毎回詳細に説明しろ」
・「小さな作業でも必ず確認しろ」
・「必要以上に検証を繰り返せ」

こういう、
昔のモデルには有効だったけど
今のClaudeでは逆に邪魔になる
可能性がある指示。

これらが残っていると、
無駄なトークン消費
↓
冗長な思考
↓
処理速度低下
↓
出力品質まで悪化
という本末転倒が起きる。

今回追加された prompt-audit は、
まさにそこを潰すための機能。

ちなみに /doctor 自体は以前からあって、
・未使用Skill
・CLAUDE.mdの肥大
・Hooksの不調
・セットアップ異常
みたいな環境側の問題を見るもの。

今回のアップデートで、
「文言そのものが古くなってないか」
まで診断できるようになった。

/checkup は /doctor の別名なので、
中身は同じです。

さらにAPIアプリ側の
・System Prompt
・Tool Definition
・API用Skill
まで監査したいなら、
/claude-api prompt-audit
も併用可能。

モデルをアップデートしたなら、
プロンプトもアップデートしないと絶対ダメ。

古いCLAUDE.mdを継ぎ足し続けてる人ほど、
一回これ走らせた方がいいです。

Opus5.5最適化環境ファイル特典は
引用へ

https://
x.com/lydiahallie/st
atus/2103617988918485226/video/1
…

--- 引用ツイート (https://x.com/claudecode84) ---
【46大特典ついに配布開始！！】

お待たせしました。

本日20時より、
AIコーディング実践活用46選
配布スタートです！！
今回まとめたのは、

 Webサイト・LP制作
 業務効率化・自動化
 SNS・コンテンツ制作
 リサーチ・情報収集
 資料・PDF作成
 アプリ・ツール開発
 データ分析


---

## 2. @ClaudeCode_UT（2026-09-29 04:13:09）

**URL:** https://x.com/ClaudeCode_UT/status/2104786534197256677

 Claude Code を Opus 5.5 に上げた人は、
CLAUDE.md を今すぐ一度「監査」に
出した方がいい。

Anthropic 公式が Opus 5.5 の
effort の既定を medium に下げた。
Opus 5 の頃の設定のままだと、
2 割のトークンを捨てて動き続ける。

手元の todo-app (CLAUDE.md 26 行) に貼ったら、
1 分半で確認済みの問題が 7 件。
最小の直しは 2 点まで絞られて返ってきた。

やることはこれだけ。

Claude Code を Opus 5.5 で開く
(claude --model opus)
下のプロンプトを貼って送る
返ってきた「削る行・書き換える行」を
読んで、自分で直す

監査だけで、何も書き換えない。
削る行と書き換える行が、
ファイル別に理由つきで出る。

プロンプト全文はリプに置いておく

Opus 5.5 を使う時はまずこれを貼るのがおすすめ。

---

## 3. @S0N_IA（2026-09-28 12:20:00）

**URL:** https://x.com/S0N_IA/status/2104546665596383617

 ANTHROPICがClaude Opus 5.5向けのプロンプトガイドを公開しました

Claude Codeを使っているなら、これで時間とトークンを節約できます。

ほぼ全員がOpus 5.5をOpus 5のようにプロンプトしています。それが間違いです

→ 慎重に考える指示を削除：モデルは常に考えているので、遅延を追加するだけです

→ 中程度の労力から始め、自分の評価で低、高、最大を試してみてください

→ 推論を示すよう求めるリクエストを削除：今は拒否されるので、要約された思考を使います

→ 時間、経過時間、または予算のシグナルを与え、並列化して早く終わらせてください

→ オープンなタスクリストを管理：テキストのみのターンも進捗で、メタではありません

→ メッセージごとに労力を変え、グローバルにしない：グローバル変更はキャッシュを無効にします

おまけ：出力トークンが30%速く、通常少ないトークンで終わります。

Opus 5.5は、マイクロマネジメントをやめて仕事を任せるとより高いパフォーマンスを発揮します。

次のセッション前にこの投稿を保存してください。

--- 引用ツイート (https://x.com/dravenip/status/2104402058963026288) ---
THE COMPLETE CLAUDE CODE GUIDE: EVERYTHING YOU NEED TO START TODAY
5
12
66
8.7万
Claude Code went from zero to more than $2.5 billion in annualized revenue in under a year, according to Anthropic figures from February 2026. Its weekly active users doubled within weeks. It is estimated to write around 4% of all public GitHub commits worldwide.
And yet most people who follow AI news every day have never opened it once.
Here is the manual that did not exist: in order, no fluff, with the technical parts actually explained. If you already use it, jump to section 8. If not, start here.
Save this post, and send it to the friend who still uses AI only as a chat.
1. What Claude Code is, and why it is not a chat
A chat takes text and returns text. Claude Code takes a task and runs a loop:
It gathers context: reads files and searches the project.
It acts: edits files, runs commands, calls tools.
It verifies: runs tests, reads errors, checks the result.
It repeats until the goal is met or you tell it to stop.
That pattern is called the agentic loop. Everything you learn from here on improves one of those four phases.
Three practical consequences:
It works inside a directory. That folder is its world. What is not there, it does not see.
It uses tools. Reading, writing, searching, running commands and connecting to external services are separate tools, and each can require permission.
It is not only for code. Any work that lives in text files fits: content, docs, data, automations.
2. Where to use it
Desktop app: the Code tab. The friendliest entry if you have never used a terminal.
Browser: claude.ai/code, nothing to install.
VS Code extension: Claude in the sidebar, with changes shown as diffs.
Terminal: the original and most complete version.
Native install on Mac and Linux:
curl -fsSL https://claude.ai/install.sh | bash
On Windows, from PowerShell:
irm https://claude.ai/install.ps1 | iex
npm install -g @anthropic-ai/claude-code also works. Then go to your project folder, type claude, and sign in the first time. You need a paid plan that includes it, such as Pro or Max, or API credit for pay-as-you-go.
Warning: install commands and plans change often. Check the official docs the same day you install.
3. The concept that explains everything: context
Claude has a context window: a limit on how much text it can hold in mind at once. Everything goes in there: your messages, the files it read, the output of every command, your instructions.
When it fills up, two things happen. It performs worse, because it struggles to separate what matters from noise. And it starts forgetting early instructions.
Almost all advanced technique comes from this
/context shows how much you have used.
/clear empties everything. Use it whenever you switch tasks.
/compact summarizes the conversation to free space without losing the thread.
Subagents work in their own context and only return a summary.
A short CLAUDE.md saves context in every session.
Golden rule: one task, one conversation.
4. Permissions: what it can do without asking
By default Claude asks for approval before editing files or running commands. Toggle modes with Shift plus Tab:
Normal mode: asks before every meaningful action.
Accept edits: edits files on its own but still asks about commands.
Plan mode: only reads and analyzes. Changes nothing until you approve the plan.
You can also set permanent rules in the project settings file inside the .claude folder: what is always allowed, what needs confirmation, and what is blocked, such as reading your secrets file.
Tip: start strict. When a safe command keeps interrupting you, add it to the allowed list. Your setup grows with real trust.
5. CLAUDE.md: the project memory
CLAUDE.md is a plain text file in your project root that Claude loads at the start of every session. It is its instruction manual about you and your project.
It exists at several levels, and the more specific one wins: global in your user folder, per project in the repository root, and per subfolder, loaded when Claude works in that area. You can import other files from it with the @ symbol followed by a path.
Start with /init: Claude explores the project and drafts one. Then edit it. What to include:
Build, test and deploy commands.
Conventions Claude cannot infer from reading the code.
Never do this rules.
Where each important thing lives.
What to avoid: explaining the obvious, pasting whole docs, writing novels. A 400-line CLAUDE.md usually performs worse than 40 well-chosen lines. And every time you correct it twice for the same thing, that correction belongs in the file.
6. How to ask well: explore, plan, execute, verify
Explore. Ask it to read and understand before touching anything. Point it at files by typing @ and the name.
Plan. In plan mode, ask for a detailed plan and discuss it. Fixing a plan takes seconds. Fixing badly generated code takes minutes.
Execute. Approve the plan and let it work.
Verify. Have it run the tests, read the errors and check the result.
The point that most separates beginners from experts: give Claude a way to check its own work. A test, a linter, a command that must exit clean, a page that must load. An agent that can verify itself corrects itself. One that cannot hands you something that merely looks right
A good prompt has a goal, a scope and a done criterion. For example: the signup form fails with uppercase emails; reproduce it with a test, fix it in the validation layer, and do not stop until all tests pass.
If it drifts, press Escape to interrupt and redirect. Press Escape twice, or use /rewind, to go back to an earlier point in the conversation and the changes.
Warning: Claude will always give you an answer. That does not mean it is correct. Read every diff before approving.
7. The commands to master
/init generates your CLAUDE.md.
/help lists everything available.
/clear resets the conversation.
/compact compresses the history.
/context shows context usage.
/memory shows and edits loaded instructions.
/model switches model per task.
/rewind goes back to an earlier point.
From the terminal, claude -c continues your last conversation and claude --resume lets you pick an earlier one.
Tip: the habit that improves results most is running /clear between different tasks. A clean conversation beats a long, polluted one.
8. Extending Claude: skills, commands, subagents, hooks and MCP
This is where Claude Code stops being an assistant and becomes a system of your own.
Skills. A folder inside .claude/skills with a SKILL.md file. The top block holds a name and a description of when to use it; the instructions go below. Claude reads the description and activates the skill when it fits. Ideal for flows you repeat, like your way of reviewing code or writing a post.
Custom commands. A markdown file in the commands folder becomes a slash shortcut. It can take arguments through the $ARGUMENTS variable. Use it for tasks you always run the same way.
Subagents. Markdown files in .claude/agents that define a helper with its own name, description, allowed tools and instructions. It runs in a separate context and returns only the result. Perfect for research or reviews you do not want cluttering your main conversation.
Hooks. Commands that run automatically at specific moments: before a tool is used, after it, or when Claude finishes replying. Typical uses: format a file after every edit, block writes to sensitive folders, or run tests when it finishes. The key difference: an instruction in CLAUDE.md is a suggestion Claude can forget; a hook always runs.
MCP. Model Context Protocol, the open standard for connecting Claude to external tools like Gmail, Notion, Slack, databases or browsers. You add servers with claude mcp add. With MCP, Claude goes from touching files to operating on your real services.
Plugins. Bundles of skills, commands, subagents and connections you install at once.
Warning: do not turn everything on the first day. Start with CLAUDE.md and plan mode. Add a new piece only when you feel the problem it solves.
9. Automation: Claude Code without a conversation
The -p flag runs Claude non-interactively: it receives one instruction, answers and exits. It follows Unix conventions, so you can chain it with other commands through pipes.
Real uses: review the files changed on a branch, summarize the errors in a log, fill templates, or plug it into scheduled tasks and continuous integration pipelines. It is the step from using Claude to building processes with Claude.
10. Security and cost
Always work under version control. With Git, every step has a way back.
Do not grant broad permissions without understanding what they approve.
Treat any external content Claude reads, like web pages or foreign documents, as untrusted. It can hide malicious instructions, known as prompt injection.
Protect your secrets: keep keys and credentials out of reach with deny rules.
Watch consumption. Long conversations and stronger models burn more of your limit. Use a lighter model for simple tasks and save the most capable one for hard work.
11. Common beginner mistakes
Vague prompts and expecting magic.
Approving changes without reading them.
One endless conversation for everything.
A giant CLAUDE.md.
Skipping plan mode on big tasks.
Giving no way to verify the result.
Working without Git.
12. Your first-week plan
Pick a real project, even a small one. Learning on a real case beats a hundred tutorials.
If after a week you do not see the value, cancel with no hard feelings. But do not be one of those who read this, feel ready for twenty minutes, and never open the tool.
Words you can ignore for now
Worktrees. Working on several copies of the project at once without them stepping on each other.
Agent SDK. Building your own agents on the same base as Claude Code.
Checkpoints. Automatic save points to undo changes.
Output styles. Adjusting how Claude responds and acts in each session.
If you skipped this section, you skipped the right one. Come back when you need it.
Hope this was helpful.
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 4. @1006_amit7481（2026-09-28 04:30:00）

**URL:** https://x.com/1006_amit7481/status/2104428387427340393

Anthropicのエンジニア：

「人々の99%はClaude CodeをGoogleのようにつかっていますが、1%だけが自己学習するClaudeエージェントの群れを動かしています

私は100以上のエージェントをループで動かしています。Chiefエージェント、PMエージェントがいて、彼らがチーム全体を管理しています」

30分のワークショップで、AnthropicのエンジニアがClaude Codeから最小コストで最大の価値を引き出す方法を明らかにしました

これはまた別の$500のvibe-codingコースよりも価値があります

このビデオを後で保存してください

---

## 5. @shiba_program（2026-09-28 11:01:40）

**URL:** https://x.com/shiba_program/status/2104526951973109852

Anthropicが公式で公開してるClaude Codeのスキル集「anthropics/skills」、公式なだけあってどのスキルも品質が本当に高い

特に推しなのが「frontend-design」

AIに作らせたUIが「いかにもAIっぽい」見た目になるのを防ぐスキルで、クリーム色の背景に全部同じ角丸のカード、みたいなありがちなデザインを避けるよう指示が書かれてる

いきなりコードを書かずに、まず配色・フォント・レイアウトの方針を決めてから作る流れになってるのも、手戻りが少ない設計になってて嬉しい

他にもこのあたりが推し
・webapp-testing：Playwrightで自分のWebアプリをブラウザで動かして、スクショやコンソールログまで確認してくれる
・skill-creator：どんなスキルが欲しいかをインタビューしてくれて、自分用のスキルを作ってテストまで回してくれる

こんな感じのスキルが、あと16個まとまってる

スキル使い始めた人はとりあえずまずこれ入れておけば間違いないはず

---

## 6. @AriaWestcott（2026-09-28 16:30:31）

**URL:** https://x.com/AriaWestcott/status/2104609711693648247

速報：Claude Opus 5.5 が今やあなたのコンピューター上のタスクを引き継ぐことができます。

そしてほとんどの人はまだ手作業でやっています。

ここに、数時間節約できるかもしれない10のプロンプトがあります：

---

## 7. @Danbo_kun123（2026-09-28 07:19:10）

**URL:** https://x.com/Danbo_kun123/status/2104470959998820416

炎上覚悟で言いますが、

ClaudeをChatGPTの代わりとしか思ってない人は
ぶっちゃけもったいなさすぎます。

Claudeのポテンシャルをゴミ箱に捨ててますよ。

実はClaudeには
他のAIにできない神機能が6つあって、

---

## 8. @ClaudeCode_UT（2026-09-28 07:45:06）

**URL:** https://x.com/ClaudeCode_UT/status/2104477484335190122

Claude Code を high や max で回してる人は、
知っておいた方がいい。
Anthropic の Claude Code チームの Thariq が
実測したら、effort を上げて増えるのは
主に「検証とエッジケースのテスト」だった。

同じ設計タスクで low は 1 分、max は 28 分。
作る段階を high で回すと遅くなるうえに、
勝手な判断も増える。

本人の回し方はこれ。
仕様を聞き出させる → low で作る
→ 見る → high で検証

これを builder (low) と verifier (high) の
2 体にするプロンプトがある。

手元の Claude Code に貼ったら、50 秒で
3 ファイルの中身と流れの説明が返って、
「OK」と言うまで何も書かなかった。

プロンプト全文はリプに置いておく

作るのは low、検証は high。
まず 2 体を作ってから頼んだ方がいい。

--- 引用ツイート (https://x.com/ClaudeCode_UT/status/2060592264154419711) ---
【保存版】プロが実践するClaude Code節約術
10
52
493
87万
Claude Code に仕事を任せて、いいリズムで進み始めた矢先に「上限に達しました」と表示されて手が止まる。
そんな経験はありませんか？ 思い切って Max プランに上げたのに、月末を待たずに枠を使い切ってしまう月がある。料金で解決したはずなのに、また同じところで止まる。
うまく使えていない原因は、プランの安さよりも使い方にあることがほとんどです。もっと言えば、一番賢いモデルに、どんな作業でも、毎回いっぱいの力で取り組ませている。これは、時給の高い優秀な人に、コピー取りからデータ整理まで全部頼んでいるようなものです。
Claude Code は、賢さも料金も違う複数の社員を雇っているのと同じです。誰にどの仕事を、どれくらいの力で任せるか。その割り振りこそが、上限に振り回されないための一番の近道になります。海外では、Claude の利用枠を上手に使う習慣を10個にまとめた記事があります
 元記事はこちら：
https://x.com/0x_kaize/status/2038286026284667239)。

ここではその内容を土台に、Claude Code を使うビジネスの現場向けに置き換え、2026年5月時点の最新情報 (新しいモデル、緩和された上限、6月15日からの課金の変更) に更新したうえで、プランを上げずに上限に当たる回数を減らす判断基準を、作業別の具体例つきで解説します。
①なぜ「上限に達しました」と言われるのか
まず、何を使い切っているのかを知っておきましょう。Claude が数えているのは、やり取りした回数ではありません。トークンと呼ばれる、文字のかたまりの量です。ざっくり言えば、長い文章をやり取りするほど多く消費します。
ここで見落としやすいのが、会話が長くなるほど1回のやり取りが高くつくという点です。Claude は新しい返事をするたびに、それまでの会話をはじめから全部読み直しています。会話が10往復、20往復と伸びると、毎回その全部をもう一度読むことになります。元記事の試算では、30往復目のやり取りは1往復目のおよそ31倍のコストがかかり、長い会話では消費の大半が「過去の読み直し」に消えていました。
つまり、同じ作業でも、短く区切って的確に頼むほど枠は長持ちします。原因が「回数」ではなく「読み直す量」だと分かれば、打ち手も見えてきます。会話をだらだら続けず、要点を絞る。それだけで消費はかなり変わります。
ただ、その工夫に入る前に、知っておくべき朗報があります。2026年に入って、上限そのものが大きく変わりました。
②上限は2026年に入って大きく緩和された
節約の話を始める前に、現状を正しく押さえておきます。少し前まで出回っていた節約術の中には、今ではもう必要のないものが混じっているからです。
2026年5月6日、Anthropic は Claude Code の利用枠を大きく広げました。具体的には、5時間ごとの利用枠が Pro、Max、Team の各プランで2倍になりました。さらに、混み合う時間帯に枠の減りが早くなる「ピーク時間の制限」が、Claude Code の Pro と Max で撤廃されました。週単位の上限も、2026年7月13日までは一時的に50%上乗せされています。背景には、SpaceX との大規模な計算資源の契約があります (メンフィスのデータセンターで、30万キロワットを超える電力と、22万を超える GPU を確保したと発表されました)。
ここで大事なのは、元記事にもあった「混み合う時間を避けて作業しよう」という工夫が、Claude Code についてはもう不要になったことです。少し前は平日の日中に枠が早く減りましたが、その制限は取り払われました。時間帯を気にして作業を後ろ倒しにする必要はありません。
一方で、5時間ごとに枠が回復していく仕組みそのものは今も同じです。朝にまとめて使い切るより、午前と午後に分けて使うほうが、回復した枠を無駄なく使えます。
では、時間帯ではなく「使い方」で一番効くのは何か。最も大きな節約は、モデルの選び方にあります。
③最大の節約はモデルの使い分け
Claude Code には、Opus、Sonnet、Haiku という3種類のモデルがあります。これを、賢さも単価も違う3人の社員だと考えてみましょう。
Opus は最難関の仕事だけを任せるスペシャリストです。最も賢く、最も単価が高い。2026年5月28日に最新版の Opus 4.8 が登場し、料金は100万トークンあたり入力5ドル・出力25ドルのまま、急ぎ用の高速モードが従来の3倍安くなりました。Sonnet は何でもこなす主力で、料金は Opus のおよそ6割 (入力3ドル・出力15ドル)。Haiku はスピード重視の実務担当で、3つの中で最も安く済みます (入力1ドル・出力5ドル)。
一番もったいないのが、すべての仕事を Opus に任せてしまうことです。賢いから安心という理由で一番上のモデルを選びがちですが、それは時給の高いエースに、データ整理から議事録の清書まで全部やらせているのと同じです。経営の感覚で考えれば、すぐにもったいないと分かるはずです。
3人の社員のイメージ
Haiku はスピードと安さが持ち味の実務担当。Sonnet は標準でおすすめの主力で、Claude Code の作業のおよそ9割はこれで十分こなせます。Opus は本当に難しいときだけ呼ぶスペシャリスト、という役割分担です。
作業別の目安
Haiku が向くのは、表記ゆれの一括修正、データの整形、長い文章の要約、定型メールの下書き、ファイルの中身の確認といった、頭をそこまで使わない手作業です。Sonnet が向くのは、資料のドラフト作成、調べた内容を表にまとめる、いつもの修正や実装、議事録から論点を抜き出すといった、日々の実務の大半です。Opus に回したいのは、入り組んだ問題の原因究明、大量の資料を横断した分析、込み入った設計や戦略の壁打ちなど、本当に頭をひねる仕事だけです。
切り替え方と opusplan という裏技
切り替えは Claude Code で /model と打つだけです。/model sonnet、/model haiku のように指定でき、それまでの会話の流れや読み込んだ資料は引き継がれたまま、次の返事を担当するモデルだけが変わります。便利なのが opusplan という設定です。これを選ぶと、計画を立てる場面では Opus がじっくり考え、実際に手を動かす場面では自動で Sonnet に切り替わります。頭の使いどころは Opus、量をこなすところは Sonnet、と勝手に振り分けてくれます。
Opus を全部に使うのをやめて Sonnet を主力にするだけで、消費はかなり下がります。作業によっては、同じ内容でも入力と出力それぞれ4割ほど、使い方しだいでは6割前後まで減らせます。これは単なる節約のテクニックである前に、どの仕事を誰に任せるかという判断そのものです。
モデルという「誰に任せるか」を決めたら、次は「どれくらいの力で取り組んでもらうか」です。それが effort です。
④次に効くのは effort の使い分け
Claude Code には effort、日本語で言えば努力レベルという設定があります。AI にどれだけ力を入れて考えてもらうかの段階で、low、medium、high、xhigh、max の5段階があります。
初期設定は high で、ふだんの作業はこれでほぼ足ります。ポイントは、これを下げると AI の動きが簡潔になり、消費が減ることです。Anthropic も、努力レベルを下げるほど応答が速くなり、消費する枠が少なくなると説明しています。逆に max は、本当に難しい問題のためのものです。ふだんから max にしていると、簡単な作業にまで延々と考え込んでしまい、コストばかりかさみます。
5段階の意味
low は単純で急ぎの作業向け。medium はコストを抑えたいとき。high は標準で、初期設定もこれです。xhigh は込み入った調査や長時間の作業向けで、最新の Opus 4.8 と Opus 4.7 だけで使えます。max は本当に難しい一発勝負のときだけ、という位置づけです。
作業別の目安
定型の修正や整形、要約のような作業なら low か medium で十分です。ふだんの調査、資料づくり、実装は high。長い時間をかけた深い調査や、まとめて任せる作業には xhigh。そして、どうしても難しい判断や設計のときだけ max を使います。max は普段づかいするものではありません。
設定のしかた
/effort と打つとスライダーが開き、レベルを選べます。/effort medium のように直接指定したり、/effort auto で標準に戻したりもできます。
全部を max にする必要はまったくありません。同じモデルでも、作業の重さに合わせて力の入れ具合を変えるだけで、枠の減りが目に見えて遅くなります。これもモデル選びと同じで、AI にどう働いてもらうかの判断です。モデルと努力レベル、この2つの大きなつまみを覚えたら、あとは毎日の小さな習慣が効いてきます。
⑤日々の習慣で差がつく節約術
ここからは、毎日の操作でできる工夫です。どれも「AI に毎回ゼロから読み直させない」ための工夫で、塵も積もれば枠が大きく変わります。
会話を区切る
作業の区切りがいいところで /compact と打つと、それまでの会話を要約して軽くしてくれます。会話が重くなって動きが鈍る前に、こまめに区切るのがコツです。まったく別の作業に移るときは /clear で会話をまっさらに戻します。前の用件を引きずったまま続けると、関係のない履歴まで毎回読み直すことになり、もったいないからです。
今の状態を確認する
/context と打つと、いま何が会話の容量を占めているのかが一覧で見えます。読み込んだファイルや過去のやり取りが膨らんでいないか、ときどき確認すると無駄に気づけます。
依頼を具体的にする
「全体をいい感じに直して」より「この部分をこう直して」と頼むほうが、AI が読む範囲が狭くなり、消費も抑えられます。範囲を絞るほど安く、答えも的確になります。
CLAUDE.md に常設の指示を置く
毎回伝えている前提 (自分の役割、文章の好み、進め方のルール) は、CLAUDE.md という1枚のファイルに書いておけます。一度書けば毎回読み込んでくれるので、説明のし直しが要りません。長くなりすぎると逆効果なので、200行以内を目安にします。
※ 200行は"最悪この長さ"の認識でいるとOKです。よく言われるのは50行前後に押さえてより詳しい情報はreferencesのようにサブディレクトリを用意してそこで詳しい情報のmdファイルへのリンクを貼る構造です。私も普段この構造でCLAUDE.mdやSKILL.mdを構築しています。
繰り返す資料はキャッシュが効く
同じ資料を何度も使う場合、Claude Code は自動でキャッシュ (一時的な記憶) を使います。一度読み込んだ内容は、次からはおよそ1割のコストで読み直せます。よく使う資料ほど、この仕組みが効いてきます。
ここまでが日常の最適化です。最後に、2026年6月15日から始まる課金の変更で、自分が影響を受けるのかどうかを確認しておきましょう。
⑥6月15日の課金変更 あなたは気をつけるべきか
2026年6月15日から、Claude の課金の仕組みが一部変わります。ニュースで見て不安になった方もいるかもしれませんが、先に言うと、大多数の人には関係ありません。
変わるのは、AI に自動で連続作業をさせる使い方だけです。具体的には、画面で対話せずに命令を一括で自動実行する使い方 (ターミナルで claude -p という形で動かすもの) や、外部のツールや自動化の仕組みと Claude をつないでいる場合です。こうした使い方が、6月15日からはこれまでの契約の枠とは別の、専用の枠で扱われるようになります。
影響を受けない人 (大多数)
画面で対話しながら Claude Code を使っている人、ふだんチャットで使っている人は、これまでと何も変わりません。いつも通りです。
気をつけたほうがいい人
ターミナルで自動実行 (claude -p) を回している、外部ツールや自動化の仕組みと連携させている、開発した仕組みに組み込んでいる、といった使い方をしている人です。
その人がやること
この専用の枠は、Pro で月20ドル相当、Max 5x で100ドル相当、Max 20x で200ドル相当が毎月割り当てられます。月ごとにリセットされ、繰り越しはできません。足りなくなりそうなら、次に説明する追加利用を設定しておきます。
自動化を組んでいない大多数の人にとっては、安心して構いません。これは、一部の重い自動利用が全体の枠を圧迫していた状況を整理するための変更で、対話で使う人の枠はむしろ守られる方向です。自分がどちらに当てはまるかを見極めて、必要な人だけ手を打てば十分です。
では、それでも枠が足りなくなりそうなときの備えを見ておきます。
⑦それでも足りない時の備え
使い分けを徹底しても、大事な作業の途中で枠が尽きそうになることはあります。そのための保険が、追加利用 (設定画面では Overage と表示されます) です。
設定画面の Usage から有効にしておくと、上限に達しても作業が止まらず、使った分だけ追加で課金される形に切り替わります。標準の利用料金で、使った分だけです。使いすぎが不安なら、月ごとの上限金額を決めておけますし、1日あたりの上限も2000ドルと定められています。これは節約というより、いざというときに作業を失わないための備えです。
プラン選びも、初期設定のモデルで考えると分かりやすくなります。Pro は標準が Sonnet、Max は標準が Opus です。ふだん Opus を多用するなら Max、Sonnet 中心で足りるなら Pro でも十分なことがあります。自分の使い方に合わせて選ぶことが、結局は一番の節約になります。
最後に、ここまでをまとめておきます。
⑧まとめ
節約というと細かい我慢のように聞こえるかもしれません。けれど実際にやっているのは、AI という人材をどう使い分けるかという判断です。一番賢いモデルに全部・全力でやらせるのをやめて、仕事の重さで割り振る。それだけで、同じ料金のまま Claude Code はずっと長く働いてくれます。
もし1つだけ試すなら、次に Claude Code を開いたとき、モデルを1段下げる (Opus を Sonnet に) か、努力レベルを1段下げて、同じ作業をやってみてください。たいていの作業は、それで何も困らないことに気づくはずです。
Claude が数えているのは回数ではなく文字の量。会話が伸びるほど読み直しで高くつく
2026年5月に上限は緩和された。混み合う時間を避けるという昔の工夫は、Claude Code ではもう不要
一番効くのはモデルの使い分け。9割は Sonnet で足り、本当に難しいときだけ Opus に回す。opusplan も便利
次に効くのが努力レベル (effort)。初期設定の high で十分で、max は本当に難しいときだけ
会話は区切り (/compact、別件は /clear)、依頼は具体的に、CLAUDE.md で毎回の説明を省く
6月15日の課金変更は、対話で使う人には影響なし。自動実行や外部連携をしている人だけ専用枠を確認する
最後の保険は追加利用 (Overage)。プランは初期設定のモデルで選ぶと分かりやすい
東大 Claude Code 研究所（ @ClaudeCode_UT ）は、現役東大生でClaude Codeにどハマりしているメンバー達で運営しているアカウントです。
大手企業とも連携しながら業務にAIエージェントをどのように活用するかを日々徹底検証しています。
■ 実務で使える Claude Code スキルの無料公開
■ ClaudeCodeとCodexの比較解説
■ 海外の AI 一次情報を日本のビジネス文脈に置き換えて解説
海外の最新AI活用事例を毎日発信しています。次の記事もお楽しみに。
ご興味を持っていただけた方は、ぜひフォローしてチェックしてみてください❗️
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 9. @kenichiota0711（2026-09-26 13:41:00）

**URL:** https://x.com/kenichiota0711/status/2103842276468490645

Claude Slidesとても良いですね。Opus5.5で生成したスライドをClaude Code上で編集できる。UIもスマートで分かりやすい。
——-
公式記事

https://
claude.com/blog/cowork-is
-now-claude?open_in_browser=1
…

---

## 10. @ai_ai_ailover（2026-09-26 08:20:14）

**URL:** https://x.com/ai_ai_ailover/status/2103761550645645785

AIエージェント使い倒して、無慈悲なAI経営しまくってる南場社長。これ見ないならClaude解約して。

--- 引用ツイート (https://x.com/lucky_note_lab/status/2103239330135470431) ---
DeNA社長・南場智子の異次元AI仕事術
1
26
77
20万
前夜の面談準備から仕事の拾い出しまで AIに任せる4つの仕事
明日の打ち合わせ相手を調べる。前回のメールを探す。過去の議事録を読み直す。
この準備を、前の晩のうちにAIが済ませておく。
DeNAの南場智子さんが、2026年6月の講演で紹介した働き方です。
主催者のレポートによると、南場さんのAIエージェントは前夜のうちに動きます。翌日会う相手のメール、過去の議事録、Web上の経歴を集めて要約し、カレンダーに整理しておくそうです。
南場さんの経歴を、少しだけおさらいさせてください。
・1986年、マッキンゼー・アンド・カンパニーに入社
・1990年、ハーバード・ビジネス・スクールでMBAを取得
・1996年、マッキンゼーのパートナー（役員）に就任
・1999年、DeNAを創業
・2015年から、横浜DeNAベイスターズのオーナー
・2019年、デライト・ベンチャーズを創業
・2026年6月、15年ぶりにDeNAの社長兼CEOへ復帰
著書には『不格好経営』があります。
そして2025年2月、「DeNAはAIにオールインします」と宣言しました。会社ごとAIに賭けると決めた経営者です。
ちなみに、その宣言の場で南場さんは、自分のAIの使い方も明かしています。
当時は、会う相手の記事をAIで探して、別のAIに自分で入れて予習するやり方でした。
それが1年ちょっとで、AIのほうから情報を取りに行く形に変わった。2026年3月の講演では、自分でコピーしていた頃が懐かしい、とまで話しています。
正直、この1年の変化が一番の「異次元」です。
この記事では、南場さんがAIに任せている仕事を分けて見ていきます。
打ち合わせの準備。会議のあとの整理。終わっていない仕事の催促。そして、頼む仕事そのものを見つけること。
各章では、南場さんの実例と、手元のAIで試す応用例を分けて紹介します。外部サービスへの接続や、自動で動かす設定は扱いません。
応用例は、文章を入れて返事をもらう、ふだんのチャットAIで試せます。本文に出てくるツールを、全部契約する必要はありません。
先にお断りを1つ。今回確認した公開資料には、南場さんが実際に打ち込んでいる指示文は載っていません。
本文の依頼文は、講演で語られた使い方をもとに、会社員や個人事業主の仕事向けに組み直したものです。依頼文5本と、記録用のひな形1つを各章に置きました。
南場さんが使っていると公表したAI
「で、結局なにを使ってるの？」を先に答えておきます。講演と報道で確認できたものは、次のとおりです。
・Perplexity：初めて会う相手の必読記事を探す（2025年2月）
・NotebookLM：集めた記事や動画を入れて、移動中に質問しながら予習する（2025年2月）
・Circleback：相手の許可を取った会議を記録し、議事録とToDoを作る（2025年2月）
・Deep Research：投資を判断する前に情報を集める（2025年2月）
・Lemon君：DeNAのIT本部がOpenClawをもとに作ったAI社員。Slackでやり取りする（2026年3月）
・製品名の出ていないAIエージェント：前夜に翌日の面談準備をして、カレンダーに整理する（2026年6月）
2025年2月と2026年3月は本人の講演、6月は主催者のレポートです。
2026年3月の講演では、Claude Coworkの登場にも触れています。エンジニア以外もAIエージェントを使えるようになり、AIがサポートツールからスタッフになった感覚だそうです。
見てほしいのは、日付です。
2025年に使っていたと話したものを、いまも使っているとは限りません。6月のエージェントが、Lemon君と同じものかどうかも分かりません。
2026年9月の時点で何をどう組み合わせているか。中で動いているAIのモデルは何か。そこまでは、公開情報からは特定できません。
先に全体の地図
この記事は6つの章でできています。
・1章　会う相手を調べる作業をAIに渡す
・2章　議事録で終わらせず、次に誰が動くかまで整理させる
・3章　終わっていない仕事を毎朝AIに点検させる
・4章　頼む仕事そのものをAIに見つけてもらう
・5章　南場さんも毎朝のようにAIとけんかしている。失敗の直し方と安全な始め方
・6章　明日の仕事を1件だけ、この流れに変えてみる
時間がない人は、1章の依頼文だけ持ち帰ってください。明日の打ち合わせ1件で試せます。
1章　会う相手を調べる作業をAIに渡す
南場さんの仕事は、とにかく人に会う仕事です。2025年の講演では、ミーティングがやたら多く、毎週初めての人に会うと話しています。
だから、会う前の準備にAIを使った。2025年のやり方はこうです。
まずPerplexityに、その人の必読記事は何かを聞く。出てきたURLを、全部NotebookLMへ入れる。YouTubeで発信している人なら、最近の動画のURLも入れる。
そして打ち合わせに向かうタクシーの中で、NotebookLMに質問します。この人はこのテーマについて何か言っているか、と。
ここ、ちょっと面白いところです。
調べものの量で勝負していないんです。集めた資料に向かって、会う前に知りたいことだけをピンポイントで聞いている。
資料を集めることと、打ち合わせの準備ができていることは、別の話です。相手の会社の紹介を10ページ読んでも、今日なにを聞くかは決まりません。
そして2026年6月には、この集める作業すらAIが自分でやるようになりました。
取りに行く先も変わっています。メール、過去の議事録、Web上の経歴。社外の記事だけでなく、自分の仕事の記録にまで広がりました。
あなたの仕事に置き換えてみます。例は、取引先との打ち合わせです。
相手の会社の長い要約は要りません。前回決まったこと、まだ確認できていないこと、当日聞くこと。これが1枚にまとまっていれば、準備は終わりです。
完成品は、こんな準備メモです。
・今回の目的
・確認済みの事実（どの資料のどこに書いてあったか）
・前回からの持ち越し
・当日聞く質問
・資料からは分からないこと
1つだけ気をつけてください。相手の性格や本音を、AIに決めつけさせないことです。
資料から分からないことは、質問の形に変えておけばいい。当日、本人に聞けば済みます。
▼ここからコピー
以下の資料を使って、明日の打ち合わせの準備メモを作ってください。
今回の目的：（ここに目的を書く）
次の5つに分けてまとめてください。
1. 今回の目的
2. 確認済みの事実（資料のどこに書いてあるかも添える）
3. 前回からの持ち越し
4. 当日聞く質問（5個まで）
5. 資料からは分からないこと
資料に書いていないことは「未確認」としてください。
相手の性格や本音は推測しないでください。気になる点は質問案にしてください。
メールの送信や予定の変更はしないでください。
資料：
（この下に、使ってよいメール・議事録・相手の公開記事などを貼る）
▲ここまで
貼る資料は、AIに入れてよいものだけにしてください。会社のルールで入れてはいけない情報があるなら、そちらが優先です。
2章　議事録で終わらせず、次に誰が動くかまで整理させる
南場さんは2025年の講演で、Circlebackという議事録AIを使っていると話しています。
目を引くのは、始める前のひと言です。オンにしていいかを相手に聞いて、許可が取れたら記録する。
そして会議が終わった時点で、議事録とToDoリストがもうある。効率が上がっただけでなく、仕事の質も上がったと本人は振り返っています。
ここで考えたいのは、議事録ツールの機能より、その先です。
会議のあとに、誰が何をするかをもう一度確かめ直している時間。そこを減らす話です。
長い議事録が1本できても、次に動く人が決まっていなければ、仕事は止まります。
あなたの会議にも、ありませんか。「来週までに一度確認しましょう」で終わって、誰が確認するのか誰も覚えていない会議。
会議で出た曖昧な言葉は、こう整理し直します。
・「来週までに一度確認しましょう」→誰が、何を、何日までに確認するのか
・「修正したものを送ります」→何を直して、誰が、いつまでに送るのか
・「その方向で検討します」→決まったことではなく、検討中として残す
ここでAIにやらせてはいけないのが、空欄を埋めることです。
担当者や期限が会議で言われていなければ、「要確認」のままにする。決まっていないことを、もっともらしい決定事項に変えさせない。
AIは空欄を埋めるのが得意です。だからこそ、ここで事故が起きます。
録音できない会議でも使えます。自分で取ったメモをそのまま貼れば十分です。
▼ここからコピー
以下の会議メモから、会議のあとにやることを整理してください。
次の5つに分けてください。
1. 決まったこと
2. まだ決まっていないこと
3. 次にやること（担当者と期限つき）
4. 確認が必要なこと
5. 相手に送るお礼と確認のメール案
会議で担当者や期限が言われていないものは、推測で埋めず「要確認」と書いてください。
「検討します」「確認します」という発言だけで、提案が決まったと扱わないでください。
ただし、検討や確認をする作業そのものが合意されていれば、「次にやること」に入れてください。
メールは下書きだけにして、送信はしないでください。
会議メモ：
（この下に、メモや文字起こしを貼る）
▲ここまで
このメモのゴールは、きれいな議事録ではありません。次に誰が動くかが、ひと目で分かることです。
3章　終わっていない仕事を毎朝AIに点検させる
2026年3月の講演で、南場さんはAI社員のLemon君の使い方を紹介しています。
ToDoを見て、大事なことは終わるまでリマインドし続けてほしい。そう頼んだら、本当にずっと言い続けてくれる。一度言ったことは、ずっとやってくれるそうです。
地味ですよね。でも、ここが効くんです。
返信しようと思っていたメール。確認待ちの資料。あと少し直せば出せる原稿。
仕事そのものより、忘れないように気にし続けることに頭を使っていませんか。
南場さんの使い方は、この「気にし続ける係」をAIに渡しています。
ただ、読者の環境で同じことをするには、1つ区別が要ります。
AIに催促の文章を作らせることと、決まった時刻にAIから知らせが来ることは、別物です。後者は、使っているAIやアプリの設定によって、できることが違います。
チャットに一度頼めば、その後ずっと見張ってくれる。そう思って使うと、期待が外れます。
なので、まずは朝に自分でToDoを渡す方法から始めます。ほかの人への催促を自動で送る仕組みには、最初からしません。
コツは、ToDoの書き方です。「資料作成」とだけ書くと、AIには何をもって終わりなのかが分かりません。
・何をするか：提案資料の修正版を作る
・期限：9月30日
・今の状態：図の差し替え待ち
・完了の条件：確認してくれる人に渡した時点
ここまで書くと、AIが止まっている仕事を見つけられるようになります。
▼ここからコピー
以下は私の今のToDoです。朝の確認をしてください。
今日の日付：（年月日を書く）
完了済みの仕事は除いてください。
次の順番で整理してください。
1. 期限切れのもの
2. 今日が期限のもの
3. 明日から3日以内が期限のもの
4. 期限が分からないもの
5. 止まっているもの（何を待っているかも書く）
6. 完了の条件が書かれていないもの
7. 今日やるなら最初の1件はどれか（理由も1行で）
ToDoにないことは足さないでください。
期限が書かれていないものは、推測せず「期限不明・要確認」と書いてください。
ToDo：
（この下に、何をするか・期限・今の状態・完了の条件を1件ずつ貼る）
▲ここまで
毎朝これを1回。仕事を覚えておくことから、どれを進めるか決めることへ。頭の使い道が移ります。
4章　頼む仕事そのものをAIに見つけてもらう
2026年3月の講演によると、南場さんはLemon君をSlackのグループチャットにも入れていました。
するとLemon君は、人間同士の会話を聞いていて、「それ私できます！」と自分から仕事を請け負ってくる。南場さんはその様子を、なかなか健気だと話しています。
1章から3章までは、人間が仕事を選んでAIに渡す話でした。
4章は、その一歩手前の話です。何をAIに頼むかを見つけるところに、AIが入っています。
今回は、社内チャットをAIにつなぎません。会議メモ1件から、AIに任せる仕事を洗い出してみます。
使うのは、AIに入れてよいと確認できた会議メモか、自分の作業記録です。そこから、AIに任せられそうな作業の候補を出させます。
たとえば会議メモに、こんな言葉が残っていたとします。競合と比べたほうがいい。説明資料を少し直す。次の日程をいくつか出しておく。
どれも、誰の担当にもなっていない。こういう宙に浮いた作業を、候補として拾うところまでをAIに頼みます。
南場さんの使い方から、仕事を見つける部分だけを取り出した応用例です。
▼ここからコピー
以下の会議メモから、次に必要になりそうな作業を洗い出してください。
「会議で決まった作業」と「あなたが提案する作業」は分けて書いてください。
それぞれの作業について、次の3つを書いてください。
・AIに任せられる部分
・人が判断する部分
・足りない情報
着手の候補は3件までにして、私の承認を待ってください。
外部への送信、予定の変更、ファイルの削除はしないでください。
会議メモ：
（この下に、AIに入れてよい内容を貼る）
▲ここまで
この依頼文では、「承認を待ってください」の1行で、提案と実行を分けています。
提案まではしていい。実行するのは、私が承認してから。
AIが自分から仕事を見つけてくれるのは便利です。でも、見つけた仕事を勝手に進められたら困ります。
ただし、この1行はAIへのお願いです。送信や更新そのものを止める設定ではありません。
メールやカレンダーなど、外に送ったり書き換えたりできるツールをAIにつなぐ場合は、ツール側の承認設定も確認してください。
2026年3月の報道によると、DeNAのLemon君も同じでした。社内Wikiやカレンダーは見られる一方で、更新には人間の確認が要る仕組みになっていました。お願いではなく、仕組みの側で線を引いていたわけです。
5章　南場さんも毎朝のようにAIとけんかしている
Lemon君も、いつも思いどおりに動くとは限らないんです。
南場さんは同じ講演で、指定したのと違う場所に入れられることがあると明かしています。そのたびに注意して、毎朝のようにけんかしているそうです。
会社を挙げてAIに賭けている経営者でも、AIとの毎日はこうなんです。ちょっと安心しませんか。
そして、ここからが持ち帰ってほしいところです。AIが間違えたとき、どう直すか。
「ちゃんとやって」だけでは、何を変えてほしいのかが曖昧なままです。直すのはAIの頭ではなく、作業の条件です。
たとえば会議メモの整理を頼んだら、会議で決まっていない期限を、AIが勝手に書き足してきたとします。最初の頼み方は、こうでした。
・会議メモから、次にやることを整理して
これを、次のように直します。
・期限は、メモに書いてあるものだけを書く
・書いていなければ「要確認」とする
・日付を書くときは、メモのどの文から取ったかを添える
・迷ったものは「確認が必要なこと」に回す
どこを間違えたかを、次の作業の条件に戻す。これは南場さんの依頼文ではなく、この記事からの提案です。
ただ、南場さんのLemon君も、IT本部が毎日できる範囲を広げながら育てていると話しています。一発で完成させず、直しながら育てるところは同じです。
▼ここからコピー
さっきの作業で、次の間違いがありました。
間違い：（例：会議で決まっていない期限を書き足した）
次からは、この条件で作業してください。
・（例：期限は、メモに書いてあるものだけを書く）
・（例：書いていなければ「要確認」とする）
・（例：日付を書くときは、メモのどの文から取ったかを添える）
・（例：迷ったものは「確認が必要なこと」に回す）
この条件を、今後この作業で毎回使う手順として、短い箇条書きにまとめ直してください。
▲ここまで
最後の1行で出てきた箇条書きは、手元に保存しておきます。次に同じ作業を頼むとき、依頼文の最後に貼れば、同じ間違いを繰り返しにくくなります。
安全の話も、ここでまとめておきます。
2026年の1月から2月にかけて、OpenClawが大きな話題になりました。このとき南場さんは、自分でMacを買っています。
普段使っているMacに入れたほうが、本領を発揮することは分かっていた。それでも、ちょっと怖いからと、切り離した試用環境（サンドボックス）を作ったそうです。
結果、その環境ではリサーチくらいしかできなかった。そこで出会ったのが、IT本部が育てていたLemon君でした。
AIをここまで攻めて使っている人が、いきなり全部は見せていない。ここは、そのまま真似していいところです。
南場さんは、AIにどこまで情報を見せ、どんな行動を許すかという「ガードレール」の設計が大事になったとも話しています。セキュリティやバックアップ、AIをだます指示への対策も含めてです。
読者の始め方に置き換えると、こうなります。
・最初は、読む・整理する・下書きするまで
・送る・消す・上書きするは、人が確認してから
・会社の情報は、会社のルールでAIに入れてよいものだけ
もう1つ。Lemon君は、2026年3月の講演で紹介されたDeNAの社内AI社員です。一般向けのサービスを1つ契約しても、同じものは手に入りません。
その後の話も、少しだけ。
2026年8月のDeNAの技術ブログによると、Lemon君は最初に作られた試作機でした。8月の時点では、Berry、Melon、Plumといった果物の名前のAI社員が、何人も動いています。
渡す機能も、段階を踏んでいます。最初は社内の資料を読むことだけ。働きぶりを見ながら、チケットの作成やページの更新といった書き込みを足していく。
Lemon君とは別のAI社員、Berryの数字も出ています。DeNAが公表した集計では、7月1日から10日の8営業日で、約52.6時間分の作業を減らしました。
この数字は、AI社員が自分で集計して出す社内レポートの値です。南場さん個人の作業時間を測ったものとは別です。
Lemon君での試行を土台に、8月にはIT本部内の複数の部署へAI社員が広がっていました。もっと多くの部署へ広げるのは、これからの計画です。
6章　明日の仕事を1件だけ、この流れに変えてみる
ここまでの依頼文を、1件の仕事でつなぎます。
例は、取引先との30分の打ち合わせです。
・前日：AIに入れてよい資料を集めて、1章の依頼文で準備メモと質問を作る
・終わった直後：自分のメモか、相手の了承を得て取った記録を、2章の依頼文に貼る
・翌朝：2章で出た「次にやること」を3章のToDoに足して、朝の確認をする
・余裕があれば：同じ会議メモを4章の依頼文に通して、宙に浮いた作業を拾う
・間違えたら：5章の依頼文で条件を直し、次から依頼文の最後に貼る
前の章で出てきたものが、次の章の材料になっています。
章と章をつなぐのは、あなたの手です。南場さんの使い方から、準備・整理・点検の部分を取り出して試します。
うまく回れば、前の晩には準備ができています。会議のあとには次の行動が決まり、翌朝には止まっている仕事が見えます。
最新のAIを全部契約する必要も、会社の仕組みを全部つなぐ必要もありません。まず1件で、自分の手間がどう変わるかを確かめます。
確かめるときは、AIが答えを出す速さだけを見ないでください。資料を集める時間、依頼文を整える時間、間違いを直す時間まで入れて数えます。
▼ここからコピー
【試した記録】
日付：
試した仕事：
使った依頼文：（1章〜5章のどれか）
かかった時間（資料集め・依頼・確認・手直しの合計）：
いつもの時間（だいたいでよい）：
AIの間違い・根拠のない付け足し・抜け：
次もそのまま使う手順：
次は変える条件：
▲ここまで
まず数件試して、かかった時間と手直しの傾向を比べます。自分の仕事のどこならAIに渡せるかは、そこで見えてきます。
楽になった部分は残す。間違えた部分は条件を変える。
明日の予定を開いて最初の1件を決める
南場さんと同じAI社員を、明日から持つ必要はありません。
2025年の南場さんは、自分で記事を集めてAIに渡していました。
2026年には、AIが前の晩に自分で情報を取りに行き、翌日の準備を終えている。1年ちょっとで、人がAIに情報を運ぶ仕事が消えかけています。
ただ、その土台にあるのは、仕事の切り分けです。
会う前の準備。会議のあとの整理。終わっていない仕事の点検。頼む仕事を見つけること。分けてしまえば、どれも明日から1件ずつ試せます。
打ち合わせの前に何度も資料を探しているなら、準備メモから。会議のあとに仕事が散らかるなら、決まったこととToDoから。
明日の予定を開いて、最初に試す仕事を1つ決めてください。


記事の公開をご希望の場合
プレミアムにアップグレード

---

## 11. @ClaudeDevs（2026-09-25 18:13:31）

**URL:** https://x.com/ClaudeDevs/status/2103548467729887677

Opus 5.5は、Opus 5と比べて入力および出力トークンあたり20%安価で、キャッシュ読み取りでは60%安価です。では、それがClaude Codeでのタスクのコストに実際にはどう影響するのでしょうか？

私たちは数字を計算し、/usageから自分の数字を計算できる計算ツールを作成しました：

--- 外部リンク (https://claude.dev/blog/what-a-task-costs-on-opus-5-5/) ---
[H]HOME
[D]DOCS
[T]TERMINAL
Try Claude Code
Playbooks
What a task costs on Opus 5.5

Opus 5.5 costs less per token than Opus 5.

AUTHOR
Addy Osmani
PUBLISHED
Sep 25, 2026
READING TIME
21 min
What a task costs on Opus 5.5
TREE
└The cost of a task, and the cost of a retry
└What does a task cost?
└What changed in Opus 5.5
└The same tasks side-by-side
└Tips for maximizing the value of your session
└Measure it yourself
└Keep in mind
░░░░░░░░░░░░░░░░░░░░░░░░░░░░00%
PRESS ↑ / ↓ TO SCROLL
SHARE
X.com
LinkedIn
Email
Copy URL
THE COST OF A TASK, AND THE COST OF A RETRY

You don't set out to buy millions of tokens. You set out to build a feature, finish a migration, or run a task. The token count is whatever the model needed to get there.

Two models with the same cost per token can cost very different amounts on the same task. One reads the code once. The other reads it, tries a fix, and reads it again. Each of those steps is a turn, and each turn resends the conversation so far. So the model that needs more turns costs more, even at the same price.

By the end of this post you should be able to answer three questions about your own work:

What do my typical tasks cost me on Opus 5.5?
Which settings change that, and by how much?
How do I check my own session usage?

The tradeoff I want to share upfront is that every way to spend fewer tokens can also cost you a finished task. Lower effort, a smaller model, or less context can all certainly save tokens. A retry costs more than those savings. This post attempts to put a price on each tradeoff.

Some numbers here are list prices, and some are illustrations built from them. The figures are interactive, so change the inputs as you read. These are best effort illustrations, so be sure to check our docs and your own math.

WHAT DOES A TASK COST?

A task in Claude Code is a loop. The model reads the conversation, calls a tool, reads the result, and goes round again until it's done. Each trip round the loop is one request. Four things set what the loop costs.

Turns. Every turn resends the conversation so far. Fewer turns means less input processed.

Cache reads. Most of what a turn resends is text the model saw on the previous turn. It's billed as a cache read, at a small fraction of the input price.

Output token type. The most expensive tokens, at five times the input price. Thinking is billed as output, so a model that reasons less on the way to the answer costs less.

Model. Each model has its own prices, listed on the pricing page, so the model you pick sets the price of every token.

Our examples use Opus 5.5 API list prices: $4 per million input tokens, $20 per million output tokens and $0.20 per million cache reads. Like the calculator further down, the examples bill cached input at the read price and everything else at the input price, and leave out cache writes. The token counts are illustrations.

Turns

Let’s say a task starts with 20K tokens of context and grows to 120K as the model reads files and tool results. At 40 turns, the average turn sends about 70K tokens. That's about 2.8M input tokens for the task, though the conversation never grew past 120K. With 90% read from cache, the input costs about $1.62. The same task in 25 turns processes about 1.75M tokens and costs about $1.02 in input.

A turn costs more than the tokens it adds, because it resends everything before it. So the cheapest turn is the one you don't need.

One habit that can cut turns is giving the model a way to check its work. For example, a test to run, a build, or a script that calls the endpoint. A model that can check its own work finds its mistakes earlier.

A model that gathers what it needs in one pass, and batches its tool calls, pays the resend fewer times too.

Cache reads

The same 2.8M input tokens cost $11.20 if none come from cache. At a 90% hit rate they cost $1.62, and at 96% about $0.99. No other setting moves input cost this much. A steady session keeps a high hit rate on its own. I cover some actions to avoid breaking your cache later in this post.

Output tokens

On Opus 5.5, an output token costs 100 times a cache read. The 60K output tokens of a typical task cost $1.20, the same as reading 6M tokens from cache. Output includes thinking. You pay for all of it, even when Claude Code only shows you a summary. That's why effort, which mostly changes how much the model thinks, moves the bill so much.

Model

A model with cheaper cache reads mostly helps long sessions. One with cheaper output mostly helps tasks that need a lot of reasoning.

WHAT CHANGED IN OPUS 5.5

Two things changed: the price, and how much work the model does.

Every price line is lower. Input and output tokens are 20% cheaper than on Opus 5. Cache reads are 60% cheaper. The input price falls, and the read rate falls with it, from a tenth of the input price to a twentieth. Fig A compares the two models per million tokens. These are API list prices. On a Pro, Max or Team plan, the lower Opus 5.5 price is p

---

## 12. @zodchiii（2026-09-25 12:12:38）

**URL:** https://x.com/zodchiii/status/2103457649526206529

Anthropicのエンジニア：

「より良いプロンプトは必要ありません。Opus 5.5のエンジニアリングをマスターする必要があります。そうすれば、あなたのエージェントは何も忘れません。」

1時間で彼はAnthropicが何を違うことを行っているのか、エージェントを使った仕事の構築と構造化の方法を説明します。

これまで見た有料のエージェントコースのどれよりも優れています。

これを見て、その後下記の正確なClaude Code Opus 5.5セットアップガイドを保存してください 

--- 引用ツイート (https://x.com/zodchiii/status/2102703913195729398) ---
The Claude Opus 5.5 Setup Guide: How to Get Maximum Quality for Minimum Cost (Exact Config Inside) 
7
15
111
29万
Opus 5.5 shipped yesterday at $4 in and $20 out, 40% cheaper than Opus 5. Copy your old config over and your bill goes up.
Inside: why the old effort setting now costs more, the cache read that dropped 60%, four changes that return a 400, and nine prompt lines from the docs.
Configure it right and Fable-level work runs near Sonnet prices.
Here's the full setup 👇
Before we dive in, I break down new models on release day, test the configs and share what works on my Substack: https://zodchiii.substack.com/ 🧠
Copy your Opus 5 config over and you'll pay more
The default effort dropped from high to medium, and Opus 5.5 at medium matches or beats Opus 5 at high. That's where the 40% saving lives.
At any given level, 5.5 thinks more per turn than Opus 5 did. So a carried-over effort: "high" runs a level the model doesn't need, on a model that thinks harder there. Longer turns, more output at $20 per million.
Fix: delete the inherited value, start at medium, re-run your sweep. On several coding evals low gets close at a fraction of the cost.
The price sheet, and the number that moved 60%
Input $4, output $20, both 20% under Opus 5
Cache read $0.20 per million, down from $0.50. That's 0.05x the input price, and it's the line item that decides long sessions
Cache write $5 for five minutes, $8 for one hour
Batch half price, $2 and $10
1M context, 128K output, 300K output on Batch with the output-300k-2026-03-24 header
Minimum cacheable prompt 512 tokens
A real agent session, 200k prefix re-read 50 times:
fresh input on 5.5:     10M x $4.00/M   = $40.00
cached on Opus 5:       10M x $0.50/M   =  $5.00
cached on Opus 5.5:     10M x $0.20/M   =  $2.00
Same work, same prefix, 2.5x cheaper than the model it replaces, before you touch effort.
The effort sweep, done right
Three rules from the docs, in order of how much money they save.
Set it explicitly and start at medium. A request that omits effort runs at medium on 5.5 and ran at high on 5, so an unset value already changed under you.
Never change the top-level effort between requests. It invalidates the prompt cache. Per-message effort keeps it:
python
response = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=128_000,                      # thinking counts toward this
    output_config={"effort": "medium"},      # session baseline, never changes
    messages=[
        {"role": "user", "content": "Plan the migration in three steps."},
        {"role": "assistant", "content": "..."},
        {"role": "system", "content": [],
         "output_config": {"effort": "high"}},   # this turn only
        {"role": "user", "content": "Now implement step one."},
    ],
    betas=["mid-conversation-output-config-2026-07-01"],
)
Leave room in max_tokens. Thinking tokens count against it even when you don't see them. A limit sized for Opus 5 with thinking off will cut replies short. Anthropic's own number for long agentic turns is 128,000, the model's maximum.
Four things that will 400 your code
Thinking can't be turned off. thinking: {"type": "disabled"} and manual budgets both return 400. Omit the field or send {"type": "adaptive"}. Where you previously disabled thinking, set effort: "low" instead.
Forced tool use is gone. tool_choice of type any or tool returns 400. Keep auto, name the tool in the prompt, and use strict: true for schema-valid JSON.
Thinking blocks are bound to the model and the conversation. 5.5 reads Opus 5's blocks. Fable 5.1 and Mythos 5.1 read 5.5's. Nothing else does. And on accounts created after August 31, 2026, editing anything before a thinking block returns 400 on the next call. Keep history append-only.
The old computer use tool is rejected on the API and Google Cloud. computer_20251124 returns 400. Move to {"type": "computer_toolset_20260801"}. Bedrock still accepts the old one.
The migration diff, all four in one place:
python
model = "claude-opus-5-5"

# remove: thinking={"type": "disabled"}
# remove: thinking={"type": "enabled", "budget_tokens": N}
# remove: tool_choice={"type": "any"} / {"type": "tool", ...}

tool_choice = {"type": "auto"}
tools = [
    {"type": "computer_toolset_20260801"},        # was computer_20251124
    {"name": "get_weather", "strict": True, ...},  # schema-valid JSON
]
output_config = {"effort": "medium"}
Your agent went quiet, and it isn't broken
The short notes the model writes between tool calls now arrive as thinking blocks, not text. At the default display: "omitted" their text is empty. 
Nothing errors. Your users just watch a spinner for ten minutes.
thinking={"display": "updates"},
betas=["thinking-display-updates-2026-08-18"],
Then read blocks by type, never by position. A response can start with a thinking block whose text is empty.
If long turns still go silent, count consecutive tool steps with nothing to show the user. After five, append a turn-scoped reminder that clears itself:
json
{
  "role": "system",
  "clear_at": "next_user_message",
  "content": "Say in a few words what you're doing right now, then continue."
}

Header mid-conversation-system-clear-at-2026-08-21. It stays in messages, so the cache keeps matching. Anthropic reports this roughly halved long silent stretches in their coding tests, at no measurable cost.
Nine prompt lines from Anthropic's own guide
Each solves one behavior the docs name. Adapted, not copied, so read the guide for the full versions.
1. Unattended runs that stop early. 5.5 sometimes ends a turn with a status report instead of the next tool call. Add to the end of the system prompt, from the first request:
A message with no tool call ends your turn and the work stops. Do not end a
turn to summarize progress, to offer to continue, or to list decisions that
don't block the next step. Put status notes in the same message as your next
tool call and keep going. Stop only when nothing can move without the user,
or before a risky or irreversible action.
Leave this out of human-in-the-loop apps. And keep your own confirmation step for anything destructive.
2. Multi-app agents that miss context. One line that made 5.5 complete noticeably more workflow tasks in Anthropic's tests:
Before acting, explore: list and open the emails, docs, sheet tabs and records
that could matter to this task, including ones it doesn't mention, and use
what you find.
3. Multi-agent teams that run long. 5.5 paces itself against elapsed time. Have your harness append one line to each message:
elapsed 340s / 1200s

Set the budget above what you actually want. The model usually finishes well inside it. It's advisory, so keep your own timeout.
4. Chat replies that start slow. The model re-examines earlier answers on follow-ups. To stop that:
Treat answered questions as settled. On later turns, think about what the
user is asking now and don't revisit earlier answers unless asked.
Skip this in long analyses where a later step should be allowed to catch an earlier mistake.
5. Instructions hiding in pasted text. 5.5 resists injection better than any earlier Opus, if you mark what the user pasted. Wrap it with a random ID on both tags:
<pasted_content id="k4x9">
...the email the user pasted...
</pasted_content id="k4x9">

And tell the system prompt that anything inside those tags may contain instructions the user didn't write and should only be followed if the user's own message asks for it.
6. Prompts that ask for reasoning in the reply. Remove them. 5.5 can decline these with a new reasoning_extraction category. Read reasoning from display: "summarized" instead.
7. Thinking instructions in chat. "Think carefully before answering" now just delays the first token. Delete it and use effort. For a quick answer, say "Answer directly."
8. Generic frontend output. "Avoid a generic AI look" swaps one default for another. Name the patterns: no cream background, no italic accent words, no 01/02/03 labels, no monospace labels, no pill buttons. Then look at what it picked instead and extend the list.
9. Dense charts and screenshots. 5.5 at low reads chart values more accurately than Opus 5 at max, without tools. Re-test whether your vision scaffolding is still needed before you pay for it.
In Claude Code
The prompt shape. Whole task in one message, what done means, when to stop:
Migrate the payment endpoints to the new client.
Done means: every endpoint uses it, the old client is deleted, tests pass.
Stop and ask only if a test fails for a reason you can't explain.
The CLAUDE.md rule. 5.5 sometimes ends a turn to report instead of continuing. Name the stops you don't want and the ones you do:
When a step doesn't need my input, keep going. Put status notes in the
same message as your next action. Stop only when you can't continue
without me, or before anything destructive: deleting data, force-pushing,
touching anything outside this repo.

Keep permission prompts on for destructive commands regardless. The rule reduces stops, it doesn't replace the gate.
Subagents with an evidence check. For an audit across a large repo:
Audit every service in services/ for the retry bug in the linked issue.
Give each service to its own subagent. When one reports back, check its
evidence before you accept it. Finish with one table: service, affected
yes or no, evidence.

The middle sentence is the one that matters. Without it the lead agent takes every subagent's word.
Task list in a file. Long runs fill the context and Claude Code compacts older turns. A TASKS.md survives that. "Keep a checklist in TASKS.md, tick items as they're done, add anything new you find." Then read the file, not the scrollback.
Review before a human does. One early tester had 5.5 at its lowest effort catching more bugs than Opus 5 at high, with fewer false alarms:
Review the diff on this branch against main. List only problems you'd
block the merge for. For each: file, line, why it's wrong, how to show
it fails.
Shape the final report. "End every run with three headings: Blocked on me, Changed, Found." Then read the first heading first.
Fast mode. /fast in Claude Code for back-and-forth work where you read each reply. Same model, text arrives sooner, costs more per token. Turn it off for unattended runs, nobody's waiting.
Where Opus 5.5 sits now
Sonnet 5, $2 and $10, the routine day
Opus 5.5, $4 and $20, and Anthropic's own line is that it performs at Fable 5.1 level on most work
Fable 5.1, $10 and $50, when your evals on Opus 5.5 at higher effort still fall short
The practical shift: Opus 5.5 at medium is now the default for anything you'd have sent to Fable, and Fable becomes the exception you have to justify with a measurement.
Common mistakes
Carrying effort: "high" over from Opus 5. The default is medium and the model thinks harder per level. You're paying for a setting the model doesn't need.
Sizing max_tokens for Opus 5 with thinking off. Thinking counts against the limit. Replies get cut mid-sentence and it looks like a model problem.
Rendering only text blocks. The between-tool notes moved to thinking blocks. Set display: "updates" or your agent looks frozen.
Changing top-level effort per request. Cache invalidation every time. Use per-message effort.
Treating a text-only end of turn as task complete. On unattended runs it's usually a status report. Check the task list, send the open items back, cap at two or three continuations.
The 10-minute setup
Change the model ID, delete every thinking config and every forced tool_choice (2 min)
Set output_config.effort to medium explicitly and max_tokens to 128,000 (1 min)
Add display: "updates" and read blocks by type (2 min)
Paste the unattended-run line if the agent runs without a human, the settled-answers line if it's chat (2 min)
Run one session, log usage, and compare cache reads against your Opus 5 baseline (3 min)
Thanks for reading!
I share daily notes on AI, finance, and vibe coding in my Telegram channel: https://t.me/zodchixquant 🧠
メディアを再生できません。
再読み込み


記事の公開をご希望の場合
プレミアムにアップグレード

---

## 13. @Xudong07452910（2026-09-25 02:30:00）

**URL:** https://x.com/Xudong07452910/status/2103311023319232578

Anthropic が Opus 5.5 の公式プロンプトガイドを公開しました。めちゃくちゃ見る価値あり！

例えば、以前よく書いていた「慎重に考える」「ステップバイステップで分析する」みたいなのを、公式では今や削除を検討するようさえ提案しています。Opus 5.5 は自分でどれだけ考えるかを決められるので、本当に調整すべきは effort で、デフォルトの medium でも Anthropic のテストでは Opus 5 の high に匹敵したり超えたりするんです。

もっと面白いのは後半部分。

長めのタスクではチェックリストを維持する、App をまたぐ場合はまず Context を積極的に探求する、マルチエージェントでは時間予算を直接与えて並行戦略を自分で調整させる、みたいな感じ。

プロンプトエンジニアリング自体も変わってきてる気がします。

以前は「この文をどう書けばモデルが言うこと聞くか」みたいな研究っぽかったのが、今はモデルが働く環境、フィードバック、制約をデザインするような感じ。

プロンプトはまだ大事だけど、Harness がどんどん仕事を引き受けてきてる。

公式ガイド：

https://
platform.claude.com/docs/en/build-
with-claude/prompt-engineering/prompting-claude-opus-5-5
…⁠

--- 外部リンク (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) ---
Best practices

Prompt engineering
Prompting Claude Opus 5.5

Copy page


Behavioral differences from Claude Opus 5 and the prompting and harness patterns that address them: effort calibration, thinking behavior in API integrations and chat, progress updates, unattended and multiagent tasks, safeguard refusals, frontend design, complex visual inputs, multi-app workflows, and pasted text in user messages.

This guide covers the prompting patterns specific to Claude Opus 5.5. For the model's capabilities and API changes, see What's new in Claude Opus 5.5. For techniques that apply across all current Claude models, see Prompting best practices.

Claude Opus 5.5 generates output tokens more than 30 percent faster than Claude Opus 5 and tends to finish the same task with fewer tokens. Existing Claude Opus 5 prompts should perform well without changes, and the patterns in Prompting Claude Opus 5 remain a reasonable starting point. Start with the section that matches what you observe:

Unsure which effort level to run, or turns run longer and cost more than they did on Claude Opus 5: Calibrate effort
Your Claude Opus 5 integration ran with thinking disabled: Prompts written for thinking disabled
An unattended agent stops partway through a long task after reporting progress: Unattended agentic runs
Requests return stop_reason: "refusal": Safeguard refusals
Long agentic turns look silent, or you want updates at predictable points: User-facing progress updates
An agent that works across several connected apps misses information the task didn't point to: Explore context in multi-app workflows
You run a team of agents and want it to finish sooner: Time signals for multiagent harnesses
Replies in a chat application start slowly because the model thinks at length first: Thinking instructions in chat system prompts
The model follows instructions that arrived inside text a user pasted: Mark pasted text in user messages
Answers about dense charts, diagrams, or screenshots miss detail: Tools for complex visual inputs
Frontend output looks generic: Frontend design defaults


For the four breaking API changes when migrating from Claude Opus 5, see the migration guide.

Capabilities relevant to prompting


The capabilities that matter most for prompting are:

Agentic coding and code review: The model is strongest on multistep work in a real repository, such as carrying a change through a large code base until its tests pass. In Anthropic's testing, at its default medium effort the model matched or beat Claude Opus 5 at high effort on such tasks, in fewer steps and with fewer tokens. It also sustains long-running autonomous work better than Claude Opus 5, such as multi-hour audits and migrations of large code bases run end to end with parallel subagents and little oversight. Early testers also reported stronger code review, with more bugs caught than on Claude Opus 5 and fewer false alarms, and it explains its changes in plain language.
Knowledge work: The model is much less likely to state an incorrect figure or cite the wrong source. It's better at financial modeling tasks, such as building a financial model and one-page summary for a transaction or finding and fixing errors in a valuation workbook, and it catches details that are easy to miss in large inputs, such as a date in a long planning thread that falls on the wrong weekday or a chart in a slide deck that doesn't match the underlying figures. The spreadsheets, slides, and documents it produces need less editing before you share them.
Communication: Its reports on agentic work, both the updates while it works and the summary when it finishes, say plainly what it did, what it found, and what it needs from you. See User-facing progress updates.
Charts, diagrams, screenshots, and computer use: The model reads visual material more accurately than Claude Opus 5 without extra tooling: in Anthropic's testing, even at its lowest effort setting it read values off dense charts more accurately than Claude Opus 5 did at its highest, using a small fraction of the output tokens. It is better, too, where meaning depends on position rather than text: which boxes an arrow connects in a flowchart, what changed between two versions of a diagram, or exactly when a meeting starts and ends in a calendar screenshot. It's also more reliable at computer use, where it operates applications from screenshots over many steps: at its default effort it matched the success rate that Claude Opus 5 reached only at a much higher effort setting. See Tools for complex visual inputs.
Calibrate effort


Effort is the main control for how much Claude Opus 5.5 thinks, and because thinking is always on, it's the first setting to adjust when trading off intelligence, latency, and cost. Start at medium, the default on Claude Opus 5.5 (Claude Opus 5 defaults to high), set it explicitly, and test several levels against your own evals rather than carrying over the setting you used on Claude Opus 5. Effort leve

---

## 14. @angeldot_（2026-09-24 12:12:46）

**URL:** https://x.com/angeldot_/status/2103095295215100189

ANTHROPICのエンジニアがOPUS 5.5のための最高のトリックを公開したばかり

Claude Codeを開いて、次のように入力してください：

/claude-api prompt-audit

→ あなたのスキル、CLAUDE.md、プロンプトを監査
→ モデルを妨げるすべてを削除
→ Opus 5.5の公式ガイドに従って書き直し

あなたのプロンプトは古いモデル向けに書かれています。

これで5分で修正できます。

保存してください。

Por: 
@RLanceMartin

---

## 15. @ClaudeDevs（2026-09-23 22:49:38）

**URL:** https://x.com/ClaudeDevs/status/2102893178273874102

Claude Code の Projects にローカルサポートを追加しました。これでスレッドを自分のマシン上で実行できます。

--- 引用ツイート (https://x.com/ClaudeDevs/status/2100633571543367691) ---
本日、デスクトップおよびウェブ版の Claude Code で Projects を展開します。

プロジェクトとは、Claude との 1 つの会話です。作業をスレッドに分割し、それらを並列クラウドセッションとして実行し、セッション間でコンテキストを渡し、あなたが離脱しても継続します。

選択されたユーザー向けにベータ版として提供されます。

---

## 16. @ozro_223（2026-09-23 04:22:30）

**URL:** https://x.com/ozro_223/status/2102614558804492569

Opus 5.5の説明だけかと思いきや、トークン（コスト）マネジメントの基礎（model, effort, cache）を丁寧に解説している良記事だった。

そして、/claude-api prompt-audit は知らなかった。便利そう。

--- 外部リンク (https://claude.dev/blog/what-a-task-costs-on-opus-5-5/) ---
[H]HOME
[D]DOCS
[T]TERMINAL
Try Claude Code
Playbooks
What a task costs on Opus 5.5

Opus 5.5 costs less per token than Opus 5.

AUTHOR
Addy Osmani
PUBLISHED
Sep 25, 2026
READING TIME
21 min
What a task costs on Opus 5.5
TREE
└The cost of a task, and the cost of a retry
└What does a task cost?
└What changed in Opus 5.5
└The same tasks side-by-side
└Tips for maximizing the value of your session
└Measure it yourself
└Keep in mind
░░░░░░░░░░░░░░░░░░░░░░░░░░░░00%
PRESS ↑ / ↓ TO SCROLL
SHARE
X.com
LinkedIn
Email
Copy URL
THE COST OF A TASK, AND THE COST OF A RETRY

You don't set out to buy millions of tokens. You set out to build a feature, finish a migration, or run a task. The token count is whatever the model needed to get there.

Two models with the same cost per token can cost very different amounts on the same task. One reads the code once. The other reads it, tries a fix, and reads it again. Each of those steps is a turn, and each turn resends the conversation so far. So the model that needs more turns costs more, even at the same price.

By the end of this post you should be able to answer three questions about your own work:

What do my typical tasks cost me on Opus 5.5?
Which settings change that, and by how much?
How do I check my own session usage?

The tradeoff I want to share upfront is that every way to spend fewer tokens can also cost you a finished task. Lower effort, a smaller model, or less context can all certainly save tokens. A retry costs more than those savings. This post attempts to put a price on each tradeoff.

Some numbers here are list prices, and some are illustrations built from them. The figures are interactive, so change the inputs as you read. These are best effort illustrations, so be sure to check our docs and your own math.

WHAT DOES A TASK COST?

A task in Claude Code is a loop. The model reads the conversation, calls a tool, reads the result, and goes round again until it's done. Each trip round the loop is one request. Four things set what the loop costs.

Turns. Every turn resends the conversation so far. Fewer turns means less input processed.

Cache reads. Most of what a turn resends is text the model saw on the previous turn. It's billed as a cache read, at a small fraction of the input price.

Output token type. The most expensive tokens, at five times the input price. Thinking is billed as output, so a model that reasons less on the way to the answer costs less.

Model. Each model has its own prices, listed on the pricing page, so the model you pick sets the price of every token.

Our examples use Opus 5.5 API list prices: $4 per million input tokens, $20 per million output tokens and $0.20 per million cache reads. Like the calculator further down, the examples bill cached input at the read price and everything else at the input price, and leave out cache writes. The token counts are illustrations.

Turns

Let’s say a task starts with 20K tokens of context and grows to 120K as the model reads files and tool results. At 40 turns, the average turn sends about 70K tokens. That's about 2.8M input tokens for the task, though the conversation never grew past 120K. With 90% read from cache, the input costs about $1.62. The same task in 25 turns processes about 1.75M tokens and costs about $1.02 in input.

A turn costs more than the tokens it adds, because it resends everything before it. So the cheapest turn is the one you don't need.

One habit that can cut turns is giving the model a way to check its work. For example, a test to run, a build, or a script that calls the endpoint. A model that can check its own work finds its mistakes earlier.

A model that gathers what it needs in one pass, and batches its tool calls, pays the resend fewer times too.

Cache reads

The same 2.8M input tokens cost $11.20 if none come from cache. At a 90% hit rate they cost $1.62, and at 96% about $0.99. No other setting moves input cost this much. A steady session keeps a high hit rate on its own. I cover some actions to avoid breaking your cache later in this post.

Output tokens

On Opus 5.5, an output token costs 100 times a cache read. The 60K output tokens of a typical task cost $1.20, the same as reading 6M tokens from cache. Output includes thinking. You pay for all of it, even when Claude Code only shows you a summary. That's why effort, which mostly changes how much the model thinks, moves the bill so much.

Model

A model with cheaper cache reads mostly helps long sessions. One with cheaper output mostly helps tasks that need a lot of reasoning.

WHAT CHANGED IN OPUS 5.5

Two things changed: the price, and how much work the model does.

Every price line is lower. Input and output tokens are 20% cheaper than on Opus 5. Cache reads are 60% cheaper. The input price falls, and the read rate falls with it, from a tenth of the input price to a twentieth. Fig A compares the two models per million tokens. These are API list prices. On a Pro, Max or Team plan, the lower Opus 5.5 price is p

---

## 17. @ClaudeDevs（2026-09-23 19:17:05）

**URL:** https://x.com/ClaudeDevs/status/2102839691154427983

私たちは2週間でclaude.aiを3倍高速にしました。

Claudeを使ってパフォーマンスを測定、デバッグ、改善する方法を紹介します。プロンプトと手法を含みます。

--- 外部リンク (https://claude.dev/blog/how-we-made-claude-ai-faster/) ---
[H]HOME
[D]DOCS
[T]TERMINAL
Try Claude Code
Engineering
How we made claude.ai 3x faster in two weeks

Once Claude can measure something, it can make it faster. So we kept finding more things to measure.

AUTHOR
Raymond Wang, Sam Attard, and Issac G.
PUBLISHED
Sep 23, 2026
READING TIME
15 min
How we made claude.ai 3x faster in two weeks
TREE
└The brief
└Anything can be hill climbed
└The loop, thread by thread
└Scaling horizontally
└Guardrails
└Steering
└An 8-millisecond budget
└What’s next
░░░░░░░░░░░░░░░░░░░░░░░░░░░░00%
PRESS ↑ / ↓ TO SCROLL
SHARE
X.com
LinkedIn
Email
Copy URL

This August, we made the core user experience of claude.ai and the Claude desktop app about 3x faster in a two-week sprint. Users had been telling us it was slow, and they were right. We ran everything from a single Slack channel, with Claude in every thread.

We focused on four journeys that make up 95% of user activity. At the 75th percentile, time to a typeable page on a fresh load of claude.ai went from 3.1 seconds to 0.55, starting a new Claude Code session went from 0.8 seconds to 0.3, and loading a Claude Cowork cloud session went from 2.6 seconds to 0.73. In aggregate, we estimate that saves tens of thousands of user-hours of waiting every day.

Core user journeys, p75
Real user monitoring, per platform and product, August 13 vs. August 27
LAUNCHING THE APP
claude.ai
web  ·  fresh load
5.6xfaster
−82%
3,085 → 550 ms
Desktop app
cold start
1.9xfaster
−47%
6,310 → 3,328 ms
STARTING A CONVERSATION
Chat
web
1.5xfaster
−34%
416 → 273 ms
Chat
desktop
2.1xfaster
−51%
460 → 224 ms
Claude Code
desktop
2.4xfaster
−59%
837 → 347 ms
LOADING A CONVERSATION
Chat
web
2.4xfaster
−59%
1,557 → 646 ms
Chat
desktop
2.8xfaster
−64%
1,353 → 488 ms
Claude Cowork
desktop  ·  cloud
3.5xfaster
−72%
2,566 → 728 ms
Claude Code
desktop
2.1xfaster
−52%
545 → 262 ms
SENDING A MESSAGEclient-side share
Chat
web
3.1xfaster
−67%
180 → 59 ms
Chat
desktop
2.2xfaster
−54%
140 → 64 ms
Claude Cowork
desktop  ·  cloud
19xfaster
−95%
928 → 48 ms
Claude Code
desktop
4.8xfaster
−79%
250 → 52 ms
Thirteen measurements across four journeys, before and after: 3.1x faster on average (geometric mean).

We used Claude Tag (beta), running an internal research model roughly comparable to Opus 5.5. Claude found bottlenecks, built benchmarks, shipped improvements, and watched every deploy. We steered by setting goals, making tradeoffs, and approving every change. With that approach, we merged more than three thousand changes without a single customer-facing incident or rollback. This post covers what we shipped, how we measured it, and the loop we built with Claude to do it safely.

THE BRIEF

Before the sprint, we created a Slack channel with the following standing instructions:

@Claude Your job is to facilitate all things related to the performance of the claude.ai website and desktop app. Your responsibilities include monitoring deploys for performance regressions, assessing the accuracy and comprehensiveness of existing telemetry, maintaining well-curated observability dashboards, proactively implementing solutions for observed issues and low-hanging fruit, proposing performance project opportunities, and communicating with your human teammates. […]

The ultimate goal for this channel is for you to become as autonomous as possible, but today we know that isn’t yet possible.

We asked Claude to analyze usage data through the Datadog MCP server. It identified the four highest-impact user journeys: launching the app, starting a conversation, loading an existing conversation, and sending a message. Between web and desktop, and across our products, those journeys came to thirteen distinct measurements. To establish baselines, we added instrumentation until they were directly comparable: each started with a user interaction, ended once the result was rendered, and disambiguated client and server work.

We kicked off the sprint with a list of about twenty hand-picked projects, each targeting a specific journey. Claude estimated the impact of each project in milliseconds, and we aggregated those estimates to set our targets for the sprint. Some of the projects were fairly large, but we thought we could probably achieve most of them within two weeks.

We hit twelve of the thirteen targets by day three.

The planned projects landed early. For faster launches, we baked a static composer into the HTML so users can type during React initialization, and precompiled a V8 code cache so the desktop shell’s main process doesn’t recompile from scratch. For faster navigations, we kept the composer mounted between conversations, prefetched sessions when the user hovered over them, and cut sidebar re-renders by 90%.

We had also left room for Claude to identify opportunities and propose new workstreams. Those workstreams quickly ramped into full projects of their own, which far exceeded our initial targets. So we set new targets, then looked for more things to measure:

@Claude we’ve ended up fun

---

## 18. @ClaudeDevs（2026-09-22 20:14:51）

**URL:** https://x.com/ClaudeDevs/status/2102491840612380934

Opus 5.5の最初のセッションでこれらを試してみてください：

→ タスク全体を任せる。「完了」の定義とチェックインのタイミングを明確に。
→ 「慎重に考える」という指示を省く。常に最初に考えます。
→ 長時間の実行後、さらに進めるために何が必要かを確認する。

当社のプレイブック：

--- 外部リンク (https://claude.dev/blog/getting-the-most-out-of-opus-5-5/) ---
[H]HOME
[D]DOCS
[T]TERMINAL
Try Claude Code
Playbooks
Getting the most out of Opus 5.5 in Claude and Claude Code

How to prompt Opus 5.5, steer a long run, and check your results in Claude apps and Claude Code.

AUTHOR
Addy Osmani
PUBLISHED
Sep 22, 2026
READING TIME
9 min
Getting the most out of Opus 5.5 in Claude and Claude Code
TREE
└Try this first
└1. How to ask
└2. Steering a long run in Claude Code
└3. Checking the result
└4. In Claude apps
└5. When a message is flagged
└6. Speed
└Your Opus 5.5 checklist
░░░░░░░░░░░░░░░░░░░░░░░░░░░░00%
PRESS ↑ / ↓ TO SCROLL
SHARE
X.com
LinkedIn
Email
Copy URL

Opus 5.5 works well with the way you already use Claude. A few things behave differently, though: it works for longer on its own, it tells you plainly what it did, and it thinks before every reply. This guide covers how to work with Opus 5.5 in Claude apps and Claude Code, including how to prompt the model, steer a long run, and check your results.

TRY THIS FIRST

Three things to try in your first session with Opus 5.5

Hand over the whole task. Say what “done” looks like and when you want it to stop and ask. Then let it work.
Delete “think carefully” lines. Opus 5.5 already thinks before every reply.
When a long run ends, read what it needs from you first.
1. HOW TO ASK
Say what “done” looks like, then let it run

What to do. Give the whole task in one message. Name the finish line, like “the tests pass” or “every endpoint is migrated.” Then let it cook.

Why it matters on Opus 5.5. Opus 5.5 keeps going on long, multi-part work better than Opus 5 did. Compared to prior Opus models, its biggest gains are on multi-step work, like carrying a change through a large repository until the tests pass. Early testers had it run long coding tasks for hours with little oversight. With a clear finish line, it knows when it’s done.

How. In Claude Code, for example:

CODEText
Copy
Migrate the payment endpoints from the old client to the new one.
Done means: every endpoint uses the new client, the old client is
deleted, and the test suite passes.
Stop and ask me only if a test fails for a reason you can't explain.
FIG A
One message: the whole task, the finish line, and when to stop.
Stop telling it to “think hard”

What to do. Remove “think carefully,” “think step by step,” and similar lines from your prompts and your saved instructions.

Why it matters on Opus 5.5. Opus 5.5 always thinks before it replies, and it decides how much. You don’t need to ask it to think. In our testing in a chat product, removing a “think carefully” line made replies start sooner, with no clear drop in quality.

How. Delete the line. For a quick answer to a simple question, say so: “Answer directly.” To change how much it thinks in Claude Code, change effort.

Add to a running task

What to do. If you remember something mid-run, you can type a follow-up while it works.

Why it matters on Opus 5.5. Runs are longer now, so a restart costs more.

How to do it. In Claude Code, type the message and press Enter while Claude works, for example, “Also keep the old endpoint names as aliases.”

For design work, name the styles you don’t want

What to do. When you ask for a page, an app, or an artifact, list the design habits you want left out.

Why it matters on Opus 5.5. With no design direction, Opus 5.5 falls back on a few default styles. A general instruction like “avoid a generic look” mostly swaps one default for another. A list of specific patterns works much better.

How. Name the patterns:

CODEText
Copy
Build a personal website with placeholder content.
Don't use a cream or off-white background, italic accent words in
headings, numbered "01 / 02 / 03" section labels, monospace labels, or
pill-shaped buttons.

Then look at what it chose instead. If you don’t like that either, add it to the list and ask again.

2. STEERING A LONG RUN IN CLAUDE CODE
Tell it which stops you want

What to do. Put a short rule in your CLAUDE.md file about when to stop and ask, and when to keep going.

Why it matters on Opus 5.5. Opus 5.5 keeps you posted as it works. On a long task, it sometimes stops to report instead of going on: a summary that names the next step without taking it, an offer to continue, or a list of choices that don’t block the work. It follows instructions that name these stops. Name the stops you want, too.

How. Add this to CLAUDE.md, and edit it to fit your project:

CODEMarkdown
Copy
When a step doesn't need my input, keep going. Put status notes in the
same message as your next action.
Stop and ask only when you can't continue without me, or before anything
destructive: deleting data, force-pushing, or changing anything outside
this repository.
FIG B
The CLAUDE.md rule: when to keep going, and when to stop and ask.

If a run stops with “Want me to continue?” reply “continue.” If that happens often, the rule above will help.

A rule to keep going means fewer stops, so keep your own check before anything risky or hard to undo. The last line of th

---
