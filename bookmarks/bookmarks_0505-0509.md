# Xブックマーク 2026-05-05 〜 2026-05-09

- **対象期間:** 2026-05-05 〜 2026-05-09
- **総件数:** 15件

---

## 1. @tetumemo（2026-05-09 03:23:31）

**URL:** https://x.com/tetumemo/status/2052952578426884422

Claudeの中の人（Claude Codeチームメンバー）が「MarkdownよりHTMLの方が圧倒的に読みやすい」と公言している記事が、AI活用の常識を根底から覆していた

「100行を超えたMarkdownファイルは、正直ほとんど読めない。HTMLなら情報密度も視覚的な整理も段違いだ」

この人物、ただの開発者ではない。Claude Codeチームの内側にいる人間が、自分たちの使い方を赤裸々に語っている

なぜAIへの指示でHTML出力が最強なのか？

非エンジニアでも明日から使える10の教訓をプロンプト付きでスレッドにまとめた

①Markdownの限界という現実
②HTMLが持つ情報密度の圧倒的な差
③「読まれる資料」を作る視覚的整理力
④URLひとつで共有できる手軽さ
⑤双方向インタラクションという革命
⑥Claude Codeが持つ文脈理解力
⑦今すぐ始める方法（プロンプト例付き）
⑧ユースケース：企画・探索
⑨ユースケース：レポート・学習
⑩ユースケース：カスタム編集インターフェース

以下、一つずつ解説していく

--- 引用ツイート (https://x.com/trq212/status/2052809885763747935) ---
Using Claude Code: The Unreasonable Effectiveness of HTML
927
3,459
1.4万
1,082万
Markdown has become the dominant file format used by agents to communicate with us. It’s simple, portable, has some rich text capability and is easy for you to edit. Claude has even gotten surprisingly good at using ASCII to make diagrams inside of markdown files.
But as agents have become more and more powerful, I have felt that markdown has become a restricting format. I find it difficult to read a markdown file of more than a hundred lines. I want richer visualizations, color and diagrams and I want to be able to share them easily.
I'm also increasingly not editing these files myself, but using them as specs, reference files, brainstorming outputs, etc. When I do make edits, I’m usually prompting Claude to edit them, which removes one of markdown’s largest benefits.
I’ve started preferring HTML as an output format instead of Markdown and increasingly see this being used by others on the Claude Code team, this is why.
(if you want to start with some examples, you can see a bunch here: https://thariqs.github.io/html-effectiveness, just be sure to come back and read more about why)
Why HTML?
Information Density
HTML can convey much richer information compared to markdown. It can of course do simple document structure like headers and formatting, but it can also represent all sorts of other information such as:
Tabular data using tables
Design data with CSS
Illustrations with SVG
Code snippets with script tags
Interactions using HTML elements with javascript + CSS
Workflows using SVG and HTML
Spatial data using absolute positions and canvases
Images using image tags
I would go so far as to say that there is almost no set of information that Claude can read that you cannot fairly efficiently represent with HTML. This makes it a highly efficient way for the model to communicate in-depth information to you and for you to revie wit.
I’ve found that in the absence of being able to do this, the model may do more inefficient things in markdown like ASCII diagrams or, my favorite, estimating colors with unicode characters like in this screenshot from Claude Code.
Claude Code trying to show color in markdown
Visual Clarity & Ease of Reading
As Claude is able to do more complex work, it is also writing larger and larger specs and plans. In practice, I've found I tend to not actually read more than a 100-line markdown file, and I certainly am not able to get anyone else in my organization to read it.
But HTML documents are much easier to read, Claude can organize the structure visually to be ideal to navigate with tabs, illustrations, links, etc. It can even be mobile responsive so you can read it differently based on your form factor.
Ease of Sharing
Markdown files are fairly hard to share since most browsers do not render them natively well. You often have to add them as attachments to emails or messages.
With HTML, as long as you upload the file (for example to S3), you can share the link easily. Your colleagues can open it wherever they wish and easily reference it.
The chance of someone actually reading your spec, report or PR writeup is much much higher if it’s in HTML.
Two-way Interaction
HTML can allow you to interact with the document, for example you might want to ask it to add sliders or knobs to adjust a design or allow you to tweak different options in the algorithm to see what happens. You can also ask it to let you copy these changes into a prompt to paste back into Claude Code. 

Read more about my playgrounds post to see examples of this two way interaction: https://x.com/trq212/status/2017024445244924382
Data Ingestion
Why use Claude Code to make HTML files instead of ClaudeAI or Claude Design for example? One of the biggest reasons is all the context Claude Code can ingest. 

For example, when writing this article, I asked Claude Code to read through my code folder and find all the HTML files I’ve generated, group and categorize them and then make an HTML file with all diagrams representing each type. The diagrams you see in this article are a direct result of that.
Besides the file system, Claude Code can find additional context using your MCPs (like Slack, Linear, etc.), your web browser (with Claude in Chrome), your git history, etc.
It’s Joyful
Making HTML documents with Claude is just more fun and makes me feel more involved and invested in the creation, and that by itself is enough.
How to Get Started
I’m a little bit afraid that people will read this article and turn it into a /html skill or something. While there might be some value in that, I want to emphasize that you don’t need to do much to get Claude to do this. You can just ask it to “make a HTML file” or “make a HTML artifact”.
The trick is knowing what you want the artifact to do and how you might use it. You may over time make a skill, but for now I’d suggest just prompting from scratch to get a hang of how to use it in different cases.
Use Cases
To make this more concrete, I’ve made many different HTML files for different use cases. You can view all of them here: https://thariqs.github.io/html-effectiveness/ but here’s an overview.
Specs, Planning & Exploration
HTML is a rich canvas for Claude to dive into a problem. When I start working on a problem instead of a simple markdown plan I expect to make a web of HTML files. For example, I might start with asking Claude Code to brainstorm and create some explorations of different options. I would then ask it to expand more into one, maybe make mockups or code snippets. Finally, when I feel good I’ll ask it to write an implementation plan. When I’m happy with the plan I’ll create a new session and pass in all of these files for it to implement.
When verifying I’ll also ask the verification agent to read in the files and it will have much broader context on what is needed.
Example Prompts:
I'm not sure what direction to take the onboarding screen. Generate 6 distinctly different approaches — vary layout, tone, and density — and lay them out as a single HTML file in a grid so I can compare them side by side. Label each with the tradeoff it's making.
Create a thorough implementation plan in a HTML file, be sure to make some mockups, show data flow and add important code snippets I might want to review. Make it easy to read and digest.
Use Cases:
Exploring other ways to implement something in code
Exploring multiple visual designs
Code Review & Understanding
Code can be difficult to read in a Markdown file.  But with HTML we can render diffs, annotations, flowcharts, modules, etc.  Use this to understand code that the agent has written, to get code review or to explain a PR to someone reviewing your code. I find this often works better than the default Github diff view, and I attach a HTML code explainer to every PR I make now. 
Example prompt:
Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the streaming/backpressure logic so focus on that. Render the actual diff with inline margin annotations, color-code findings by severity and whatever else might be needed to convey the concept well.
Use Cases:
Creating a PR
Reviewing a PR
Understanding a topic in Code
Design & Prototypes
Claude Design is based on HTML because HTML is incredibly expressive at design, even if your end surface is not HTML. Claude can sketch out a design in HTML and then write it in your language of choice, be it React, Swift, etc.
You can also prototype interactions, such as animations, actions, etc. Consider asking Claude to make sliders, knobs, etc. to tune in exactly what you’re looking for.
Example prompt:
I want to prototype a new checkout button, when clicked it does a play animation and then turns purple quickly. Create a HTML file with several sliders and options for me to try different options on this animation, give me a copy button to copy the parameters that worked well.
Use this for:
Creating design system artifacts
Adjusting components
Visualizing component libraries
Prototyping Joyful Animations
Reports, Research & Learning
Claude Code is incredibly good at synthesizing information across multiple data sources and converting it into a report for readability. You can prompt Claude to search your Slack, your codebase, git history, the internet, etc. and use it to generate extremely readable reports for yourself, for leadership, for your team, etc. 
You could assemble this in the form of a long HTML document, an interactive explainer or even a slideshow/deck. Ask Claude to use SVG for diagrams to help visualize it.

For example, for my posts on prompt caching, I asked Claude to prepare an in-depth research file in HTML for me to read on all of our changes to prompt caching after reading the git history.
Example prompt:
I don't understand how our rate limiter actually works. Read the relevant code and produce a single HTML explainer page: a diagram of the token-bucket flow, the 3–4 key code snippets annotated, and a "gotchas" section at the bottom. Optimize it for someone reading it once.
Use this for:
Summarize how a feature works
Explain a concept to me
Weekly status reports to your boss
Incident reports to your leadership
SVG illustrations, flowcharts, technical diagrams, etc
Custom Editing Interfaces
Sometimes it’s hard to describe what you want purely in a text box. In this case, I'll ask Claude to build me a throwaway editor for the exact thing I'm working on. Not a product, or a reusable tool, but a single HTML file, purpose-built for this one piece of data.
The trick is always to end with an export: a "copy as JSON" or "copy as prompt" button that turns whatever I did in the UI back into something I can paste into Claude Code.
Example prompts:
I need to reprioritize these 30 Linear tickets. Make me an HTML file with each ticket as a draggable card across Now / Next / Later / Cut columns. Pre-sort them by your best guess. Add a "copy as markdown" button that exports the final ordering with a one-line rationale per bucket.
Here's our feature flag config. Build a form-based editor for it,  group flags by area, show dependencies between them, warn me if I enable a flag whose prerequisite is off. Add a "copy diff" button that gives me just the changed keys.
I'm tuning this system prompt. Make a side-by-side editor: editable prompt on the left with the variable slots highlighted, three sample inputs on the right that re-render the filled template live. Add a character/token counter and a copy button.
Use this for:
Reordering, triaging, or bucketing anything (tickets, test cases, feedback)
Editing structured config (feature flags, env vars, JSON/YAML with constraints)
Tuning prompts, templates, or copy with live preview
Curating datasets, approve/reject rows, tag examples, export the selection
Annotating a document, transcript, or diff and exporting the annotations
Picking values that are painful to express in text: colors, easing curves, crop regions, cron schedules, regexes.
Frequently Asked Questions
I’ve been telling many people about how I’ve switched to HTML and I’ve seen a few repeated questions.
Isn’t it less token efficient?
While markdown often uses fewer tokens, I’ve found that the added expressiveness of HTML and the much higher likelihood of me reading it means I get overall better output. With the 1MM context window in Opus 4.7, the increased token usage is not really noticeable in the context window.
When do you use markdown for now?
I have honestly stopped using markdown altogether for almost everything, but I’m probably far on the HTML maximalist side of things.
How do I view the HTML file? 
I tend just open it in a browser locally (you can ask Claude to open it), or upload to S3 if you want a shareable link.
Doesn't this take longer to generate than markdown? 
This does take longer! HTML can take 2-4x longer than Markdown, but I've found the results are worth it.
What about version control? 
This is honestly one of the biggest downsides of HTML, HTML diffs are noisy and hard to review compared to Markdown.
How do I get Claude to match my taste / not make it ugly? 
The frontend design plugin helps Claude make good HTML files. But to match your own companies style, you can create a single design system HTML file by pointing Claude at your codebase. You can then use that design system file as a reference for other html files.
Stay in the Loop
All of the above is to say that I think the real reason I use HTML is that I feel much more in the loop with Claude. I had begun to fear that because I had stopped reading plans in depth I would simply have to leave Claude to make its choices.
But I am happy to say instead that I feel more in the loop than ever before when using HTML. I hope you do too.
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 2. @ClaudeCode_love（2026-05-09 08:15:00）

**URL:** https://x.com/ClaudeCode_love/status/2053025932211028333

【速報】
Claude Codeから
17,000以上の株式データに
数秒でアクセスできるようになりました

https://
x.com/milesdeutscher
/status/2052425788377755680/video/1
…
接続方法も簡単
Claude Codeを開いてこれを貼るだけ。
claude mcp add --transport http financial-datasets 
https://
mcp.financialdatasets.ai
その後、Claude Code内で
/mcp
と入力してOAuth認証。
接続確認はこれ。
claude mcp list
これで例えば、
「Appleの現在のP/Eレシオと時価総額は？」
「Teslaの過去4四半期の損益計算書を見せて」
「Bitcoin価格は過去1年でどう推移した？」
みたいな金融リサーチを
Claude Codeにそのまま聞ける。
これ、地味に見えてかなり大きい。
今まで金融データを見るには、
サイトを開く
CSVを探す
Excelに入れる
分析する
という流れが必要だった。
でもこれからは、
Claude Codeに金融データを接続
↓
自然言語で質問
↓
財務・株価・企業データを即分析
という流れになる。
Claude Codeが
「開発ツール」から
「リサーチOS」に進化してきてる。

---

## 3. @gagarot200（2026-05-08 06:28:00）

**URL:** https://x.com/gagarot200/status/2052636616687329432

【完全終了Claude Code】
Claudeで最も賢いモデル
『Opus-4.7』の性能が大幅に落ちて
まともにバズるポストすら生成不可になり
Codexの使用者が爆増し世界一になった事で
完全にClaude Codeしか使ってなかった
ユーザーをぶち抜けるんよ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　

そもそもの使用モデルのレベルが
Opus4.7とGPT5.5では桁違い

同じ作業時間回してたとして
その差は歴然。

今Opus関係にAPI費用を払っても
溶ける一方だから注意しろ。

ClaudeユーザーはCodexに
簡単に移ってこれない今がかなりチャンスだな

オラも1時間である程度落とし込めて
ショート動画の自動化まではいける

--- 引用ツイート (https://x.com/Gencoin8/status/2052521292100956371) ---
【Claude Code完全終了】Codexを1時間で実務レベルに使いこなす方法
1
77
660
86万
ClaudeやClaude Codeが今最も使われているから
自分も使っているという方は今すぐやめてください。
実は今のClaude最新モデルOpus-4.7含め
全てのモデルの品質が2024年ゴロのレベルまで
低下しています。
ClaudeやClaudeCodeしか触っていなかった方は
この記事1時間で全てCodexについて
マスターしてください。

ちなみにClaude Codeの3倍は使えます。
YouTubeコメント分析からExcelレポート、ダッシュボード、自動化まで
AIツールを使っていると、「これは便利そうだけど、実際の仕事でどう使えばいいのか分からない」と感じることがあります。
ChatGPTで文章を書いたり、アイデアを出したり、ちょっとした調べものをしたりする人は増えました。
一方で、AIを使って実際にファイルを作り、アプリを動かし、データを分析し、毎週の作業まで自動化している人は、まだ多くありません。
そこで注目したいのが、Codexです。
Codexは、ただ質問に答えてくれるAIではありません。
パソコン上のフォルダを作業場所として扱い、その中でファイルを読み書きし、Excelを作り、Webアプリを構築し、ブラウザで動作確認し、GitHubやVercelと連携し、さらに定期実行まで設定できる「AI作業環境」です。
言い換えると、Codexはチャット相手というより、手を動かしてくれる作業パートナーに近い存在です。
この記事では、Codexを使ってYouTubeコメント分析システムを作る流れを、日本のユーザー向けに分かりやすく整理します。
具体的には、次のような流れです。
YouTubeのコメントを取得する。
コメントを分類し、Excelレポートにまとめる。
分析結果をWebダッシュボードで見える化する。
その作業手順をSkillとして保存する。
毎週自動で更新されるようにAutomationを設定する。
最後にブラウザで動作確認まで行う。
これだけ見ると少し難しそうに感じるかもしれません。
ただ、考え方をつかむと非常にシンプルです。
Codexの基本は、「フォルダの中で作業すること」「計画を立ててから動かすこと」「うまくいった手順を再利用できる形で残すこと」です。
この3つを押さえるだけで、Codexの使い方は一気に実務寄りになります。
Codexは「チャットAI」ではなく「作業環境」
まず、Codexの基本的な見方から整理します。
ChatGPTのようなAIに慣れている人にとって、Codexの画面は一見すると普通のチャットツールに見えるかもしれません。
中央に入力欄があり、こちらが指示を出すとAIが返答してくれる。
この点だけを見ると、普段のChatGPTと大きく変わらないように見えます。
しかし、Codexの本質はそこではありません。
Codexは、ローカルフォルダを作業対象として扱えます。
つまり、自分のパソコンの中にあるプロジェクトフォルダを指定すると、その中のファイルを読んだり、編集したり、新しく作ったりできます。
たとえば、次のような作業ができます。
Excelファイルを作成する。
CSVやJSONを読み込んで分析する。
Next.jsやReactのアプリを作る。
PythonやNode.jsのスクリプトを書く。
ダッシュボードをローカルで起動する。
ブラウザで画面を確認する。
GitHubにコードを送る。
VercelでWebサイトとして公開する。
定期的に処理を実行する。
これらは、通常のチャットAIではなかなか完結しにくい作業です。
ChatGPTに「Excelを作って」と頼んでも、ファイルを直接プロジェクトに組み込んだり、アプリとして動かしたり、ブラウザで検証したりするところまでは環境によって制限があります。
一方、Codexは最初から「作る」「直す」「確認する」「繰り返す」という作業に向いています。
そのため、Codexを使うときは「AIに質問する」という感覚よりも、「AIと一緒に作業場所に入る」という感覚を持つと分かりやすくなります。
プロジェクトはフォルダから始まる
Codexで作業を始めるとき、最初に意識したいのがプロジェクトフォルダです。
Codexにおけるプロジェクトは、基本的にパソコン上の1つのフォルダです。
そのフォルダの中に、設定ファイル、スクリプト、Excel、画像、アプリのソースコードなどが入っていきます。
Codexでは、まず作業対象となるフォルダを指定する。フォルダ内のファイルを読み書きしながら作業が進む。
この「フォルダ単位」という考え方はかなり重要です。
なぜなら、Codexはチャットの内容だけでなく、フォルダ内のファイル構成を見ながら作業するからです。
プロジェクトの中にどんなファイルがあるのか。
どこに設定があるのか。
どこに出力ファイルを保存すべきなのか。
どのスクリプトを実行すればレポートが更新されるのか。
こうした情報を、Codexはフォルダを通じて理解します。
今回の例では、YouTubeコメント分析用のプロジェクトフォルダがあり、その中に .env.local、agents.md、scripts、outputs、src などのファイルやフォルダが並んでいます。
 実際のプロジェクトフォルダには、環境変数、スクリプト、出力ファイル、アプリのソースコードなどがまとまっている。
この構成ができていると、Codexに対して「コメント分析を更新して」「ダッシュボードを修正して」「Excelを再生成して」といった指示を出しやすくなります。
フォルダが作業の土台になる。
これはCodexを使ううえで最初に覚えておきたいポイントです。
最初に用意すべき agents.md
プロジェクトフォルダを用意したら、次に作りたいのが agents.md です。
agents.md は、Codexに対するプロジェクト説明書のようなものです。
もしClaude Codeを使ったことがある人なら、claude.md に近い役割だと考えると分かりやすいでしょう。
このファイルには、たとえば次のような内容を書きます。
このプロジェクトは何を目的としているのか。
どんな成果物を作るのか。
どんなデータを扱うのか。
どのファイルを編集してよいのか。
どのファイルには秘密情報が含まれるのか。
作業時に守るべきルールは何か。
完成時にどのような確認を行うのか。
こうした前提が書かれていると、Codexは新しいチャットを始めても、プロジェクトの文脈を理解しやすくなります。
毎回、「これはYouTubeコメント分析プロジェクトで、コメントを取得して、Excelにして、ダッシュボードを更新して……」と長々説明する必要がなくなります。
もちろん、最初から完璧な agents.md を自分で書く必要はありません。
おすすめは、Codexに作ってもらうことです。
たとえば、次のように頼みます。
「このプロジェクトでは、YouTubeコメントを取得して、Excelレポートとダッシュボードを作ります。今後の作業ルールも含めて、agents.mdのたたき台を作ってください。」
するとCodexは、プロジェクトの目的、作業方針、ディレクトリ構成、注意点などを整理したファイルを作ってくれます。
その内容を人間が確認し、必要に応じて修正する。
これで十分です。
agents.md は一度作ったら終わりではありません。
作業を進める中で、「この方法は失敗した」「このAPIの呼び出し方が正しい」「Excelファイルを開いたままだと更新できない」といった学びが出てきます。
そうした内容をプロジェクトの記憶として追記していくと、Codexは次回以降、同じ失敗を避けやすくなります。
Plan Modeでいきなり作業させない
Codexを使い始めたばかりの人がやりがちな失敗があります。
それは、いきなり「作って」と頼むことです。
もちろん、Codexはかなり強力なので、いきなり作業を始めてもある程度は進めてくれます。
ただ、API連携、Excel生成、ダッシュボード構築、自動化のように複数の工程が絡む作業では、最初に計画を立てた方が圧倒的に安定します。
そこで使うのがPlan Modeです。
大きな作業を始める前は、Plan Modeをオンにして、まず作業手順を整理する。
Plan Modeをオンにすると、Codexは勝手にファイルを編集したり、コマンドを実行したりせず、まず計画を立てます。
どんな手順で進めるか。
どんなファイルを作るか。
どのAPIを使うか。
どんな確認が必要か。
こうした内容を先に出してくれます。
今回のようなYouTubeコメント分析プロジェクトであれば、Plan Modeでは次のような流れを確認できます。
YouTube Data APIを使ってコメントを取得する。
取得したコメントをJSONとして保存する。
コメントをカテゴリ別に分類する。
質問コメントや返信優先度を判定する。
Excelレポートを生成する。
ダッシュボード用のデータに整形する。
ローカルでダッシュボードを起動する。
ブラウザで画面を確認する。
問題があれば修正する。
必要ならGitHubに反映する。
定期実行の設定を作る。
このように、先に全体像を確認しておけば、途中で作業が散らかりにくくなります。
特に、ビジネス用途で使う場合はPlan Modeを使う価値が大きいです。
なぜなら、AIが勝手に進めた内容を後から修正するより、最初に目的と制約を共有した方が効率的だからです。
「作業前に計画を立てる」
これは人間の仕事でも当たり前ですが、Codexでも同じです。
APIキーや秘密情報は .env.local に入れる
YouTubeコメントを取得するには、YouTube Data APIを使います。
そのためにはGoogle Cloud側でAPIキーを発行し、プロジェクトに設定する必要があります。
ここで注意したいのが、APIキーの扱いです。
APIキーやアクセストークンのような秘密情報は、コードに直接書いてはいけません。
また、適当な secrets.txt のようなファイルに貼っておくのも避けた方がよいです。
一般的には .env.local のような環境変数ファイルに保存します。
キャプション: APIキーなどの秘密情報は .env.local に保存する。公開リポジトリに含めないよう注意が必要。
.env.local は、GitHubなどに公開しない前提のローカル設定ファイルとして使われます。
通常は .gitignore に含めて、誤って公開されないようにします。
Codexに頼む場合も、次のように伝えるとよいでしょう。
「YouTube APIキーは .env.local に保存してください。GitHubには含めないように .gitignore も確認してください。」
このように一言入れておくだけで、セキュリティ面の事故をかなり減らせます。
日本の企業や個人事業で使う場合、APIキーの管理は非常に重要です。
小さな検証プロジェクトであっても、最初から正しい場所に保存する習慣をつけておくべきです。
YouTubeコメントを取得してExcel化する
今回の中心になる成果物は、YouTubeコメント分析レポートです。
単にコメントを一覧にするだけではなく、視聴者の反応を分析し、次のアクションに使える形に整理します。
取得したYouTubeコメントをExcelレポートにまとめ、カテゴリ別の傾向や質問率を可視化する。
Excelレポートには、次のような情報を入れることができます。
分析対象のコメント数。
対象動画数。
質問コメントの割合。
返信が必要なコメントの数。
最も多く言及されたツールやテーマ。
コメントカテゴリ別の割合。
よくある質問のパターン。
返信優先度。
今後のコンテンツ案。
たとえば、画像の例では200件のコメントを分析し、3本の動画が対象になっています。
質問率は約50％で、最も多く言及されているツールはClaude Codeです。
これだけでも、かなり実務的な示唆があります。
もし質問コメントが多いなら、視聴者はまだ内容を理解しきれていない可能性があります。
同じテーマに関する質問が繰り返されているなら、そのテーマを解説する動画や記事を作る価値があります。
特定のツール名が多く出ているなら、そのツールに関する比較記事やチュートリアルが求められているかもしれません。
つまり、コメント分析は単なる振り返りではなく、次のコンテンツ制作の材料になります。
YouTube運営者にとって、コメント欄は宝の山です。
ただし、手作業で全部読むのは時間がかかります。
Codexを使えば、そのコメント欄を分析可能なデータに変換できます。
よくある質問を抽出する
コメント分析で特に価値が高いのが、質問パターンの抽出です。
視聴者が何に疑問を持っているのか。
初心者向けの質問が多いのか。
比較検討の質問が多いのか。
設定方法や接続方法でつまずいているのか。
料金や制限に不安を持っているのか。
こうした情報は、次の発信内容を考えるうえで非常に役立ちます。
よくある質問をテーマ別に分類し、回答方針や次回コンテンツの切り口に変換する。
画像の例では、質問テーマ、件数、初心者向けか上級者向けか、質問例、回答方針が一覧化されています。
たとえば、次のような分類ができます。
一般的な質問。
モデルやツールの選び方。
セットアップや接続方法。
ワークフローの作り方。
料金や制限。
学習リソースの要望。
これはYouTubeだけでなく、さまざまな業務に応用できます。
たとえば、オンライン講座を運営しているなら、受講者の質問を分析して教材改善に使えます。
SaaS企業なら、問い合わせ内容を分類してFAQやヘルプページの改善に使えます。
営業チームなら、見込み客からの質問を分類して提案資料に反映できます。
採用活動なら、候補者からの質問を分析して採用ページを改善できます。
日本の現場では、こうした声はSlack、メール、フォーム、YouTube、X、LINE、Notionなど、いろいろな場所に散らばっています。
Codexを使うと、それらを集めて分析し、次の施策に変える流れを作りやすくなります。
Excelだけで終わらせず、ダッシュボード化する
Excelレポートは便利ですが、毎回ファイルを開いて確認するのが面倒な場合もあります。
そこで、分析結果をWebダッシュボードにすると、より見やすくなります。
キャプション: Excelで分析した内容を、ブラウザ上で見られるダッシュボードとして可視化する。
画像のダッシュボードでは、次のような情報がカード形式で表示されています。
分析コメント数。
質問率。
返信候補数。
注目されているツール。
コメントカテゴリの分布。
分析結果から分かる示唆。
たとえば、「コメントの中心は一般的なフィードバックだが、質問も多い」「Claude Codeへの関心が高い」「高優先度の返信候補から対応すべき」といった内容がすぐに分かります。
これは、単なるデータ表示ではありません。
意思決定しやすい形に変換している点が重要です。
YouTube運営者であれば、次にどの動画を作るか。
SNS担当者であれば、どの質問に回答投稿を作るか。
マーケターであれば、どのトピックを広告やLPに反映するか。
カスタマーサポートであれば、どのFAQを整備するか。
ダッシュボードは、そうした判断を早くするための画面です。
Codex内のブラウザで確認できる
Webダッシュボードを作ったら、次に必要なのが動作確認です。
通常であれば、ローカルサーバーを起動し、ブラウザを開き、画面をクリックし、表示崩れや不具合を人間が確認します。
Codexでは、この確認作業もかなり任せられます。
 Codex内のブラウザで、作成したダッシュボードをそのまま確認できる。
Codexに対して、次のように依頼できます。
「ダッシュボードをブラウザで開いて、タブ切り替え、検索、リンク、空データ時の表示を確認してください。問題があれば修正してください。」
するとCodexは、実際に画面を開いて確認し、必要に応じて修正を提案または実行します。
これはかなり実用的です。
コードだけを見ていると、UIの違和感には気づきにくいことがあります。
ボタンの文字が小さい。
カードの余白が狭い。
検索結果が空のときに何も表示されない。
外部リンクが同じタブで開いてしまう。
タブの選択状態が分かりにくい。
スマホ幅で表示が崩れる。
こうした問題は、ブラウザで実際に触ってみないと分かりにくいものです。
CodexのBrowser Useを使えば、この確認作業をAIに組み込めます。
Browser UseはQAに強い
Codexのプラグイン画面を見ると、Browser Use、Spreadsheets、Presentationsなどの機能が表示されています。
Browser Useを使うと、Codexがブラウザを操作しながら画面確認やテストを行える。
Browser Useは、単にブラウザを開くだけの機能ではありません。
Codexがブラウザを操作し、クリックし、入力し、画面を確認しながら作業できます。
たとえば、次のようなことができます。
ローカルで起動したアプリを開く。
ダッシュボードのタブを切り替える。
検索ボックスに文字を入力する。
外部リンクが正しく開くか確認する。
ボタンを押して反応を見る。
表示崩れを見つける。
空データ時の画面を確認する。
アクセシビリティ上の問題を指摘する。
開発者にとっては、これはQAの補助になります。
非エンジニアにとっても、「画面を見ながら改善してくれるAI」として使えるのが大きなメリットです。
日本の業務現場では、ちょっとした社内ツールや管理画面が作られても、十分なテストがされないまま使われることがあります。
Codexにブラウザ確認を組み込めば、少なくとも初歩的な不具合や使いにくさは事前に見つけやすくなります。
UIの完成度を上げるには、画像生成や参考ビジュアルも使える
今回の元のワークフローでは、ダッシュボードを作る前に、GPT Image 2でUIコンセプトやロゴ案を作り、それをプロジェクトの素材として保存しています。
参考ビジュアルを用意してから実装すると、ダッシュボードの見た目が安定しやすい。
これはとても良い使い方です。
AIにいきなり「かっこいいダッシュボードを作って」と頼むと、無難だけれど印象の薄い画面になることがあります。
一方で、先に参考画像や方向性を作っておくと、デザインの軸が定まりやすくなります。
たとえば、次のような指定ができます。
暗めの管理画面にしたい。
YouTube分析らしい色を少し入れたい。
カード型で指標を見やすくしたい。
グラフは派手すぎず、実務向けにしたい。
コンテンツ制作者が毎週見たくなる画面にしたい。
こうした方向性を先に決めておくと、Codexが作るUIも一段実務向けになります。
特に日本向けの記事やサービスでは、過度に派手なデザインより、見やすく、落ち着いていて、情報が整理されている画面の方が受け入れられやすいことが多いです。
作業手順をSkill化する
Codexで一度うまくいった作業は、Skillとして保存できます。
Skillとは、簡単に言えば「再利用できる作業レシピ」です。
一度作った分析フローはSkillとして保存し、次回以降すぐに呼び出せる。
たとえば、今回のYouTubeコメント分析には、いくつもの工程があります。
YouTube APIからコメントを取得する。
コメントを保存する。
カテゴリ分類する。
質問を抽出する。
Excelを生成する。
ダッシュボード用JSONを更新する。
グラフ画像や補助ファイルを作る。
ローカルで画面確認する。
これを毎回、長いプロンプトで説明するのは面倒です。
そこでSkill化します。
Skillにしておけば、次回からは短い指示で同じ作業を再現できます。
スラッシュコマンドや自然文で、保存したSkillを呼び出せる。
たとえば、次のように頼めます。
「YouTubeコメント分析のSkillを実行して、最新データでExcelとダッシュボードを更新して。」
または、スラッシュコマンドとして呼び出すこともできます。
この考え方は、Codexを実務で使ううえで非常に重要です。
AI活用でありがちな失敗は、毎回その場限りの会話で終わってしまうことです。
昨日うまくいったプロンプトを、今日また探す。
前回の手順を思い出しながら、もう一度説明する。
少し違う言い方をしたせいで、出力が変わってしまう。
これでは作業が安定しません。
Skillとして手順を残しておけば、良かった作業を再現できます。
さらに改善点が見つかれば、そのSkillを更新すればよいのです。
つまり、Codexは使えば使うほど、自分専用の作業環境に育っていきます。
Skillはグローバルとプロジェクトで使い分ける
Skillには、大きく分けて2つの置き場所があります。
1つはグローバルSkill。
これは、どのプロジェクトでも使えるSkillです。
もう1つはプロジェクトSkill。
これは、そのプロジェクト内だけで使うSkillです。
どちらを選ぶべきかは、用途によります。
たとえば、「議事録を要約する」「CSVを分析する」「記事構成を作る」といった汎用的な作業は、グローバルSkillに向いています。
一方で、「特定のYouTubeチャンネルのコメント分析」「特定企業の営業レポート更新」「特定プロダクトのFAQ生成」のように、プロジェクト固有のルールが多いものは、プロジェクトSkillにした方が安全です。
今回のYouTubeコメント分析は、プロジェクト固有の情報が多く含まれます。
APIキー、対象チャンネル、出力先、ダッシュボード構成、分析カテゴリなどが決まっているからです。
そのため、まずはプロジェクトSkillとして保存するのが自然です。
もし後から「他のYouTubeチャンネルでも使いたい」となれば、汎用化してグローバルSkillに移すこともできます。
毎週の作業はAutomationで自動化する
Skill化した作業は、さらにAutomationで定期実行できます。
CodexにはAutomationsという機能があり、決まった曜日や時間に指定した作業を実行できます。
Automationsでは、現在設定されている定期実行タスクを確認できる。
今回の例では、「Weekly YouTube Comment Insights Refresh」という自動化が設定されています。
毎週日曜日の17時に、YouTubeコメント分析を更新する内容です。
自動実行のプロンプト、実行頻度、モデル、実行環境などを設定できる。
Automationの中には、かなり具体的な指示を書けます。
たとえば、次のような内容です。
YouTubeコメント分析ワークフローを実行する。
新しいコメントデータを取得する。
Excelレポートを再生成する。
ダッシュボード用JSONを更新する。
ブラウザで画面確認する。
問題がなければGitHubにコミットする。
Vercelの自動デプロイに任せる。
変更がなければ空コミットはしない。
ここまで設定しておけば、毎週の分析作業をかなり自動化できます。
YouTube運営者なら、毎週決まった時間に視聴者コメントの傾向が更新されます。
企業のマーケティング担当なら、週次レポートのたたき台が自動でできます。
カスタマーサポートなら、問い合わせ傾向の変化を定期的に把握できます。
ただし、注意点もあります。
ローカル実行の場合、パソコンが起動していて、Codexが動作できる状態である必要があります。
ノートPCを閉じていたり、Codexを終了していたりすると、定期実行は止まります。
24時間確実に動かしたい場合は、クラウド環境やVPSで動かす構成を検討した方がよいでしょう。
Automationのモデル設定に注意する
Automationを使うときに見落としがちなのが、使用モデルの設定です。
普段のチャットで使っているモデルが、自動化にもそのまま反映されるとは限りません。
Automationごとにモデルを確認する必要があります。
画像の例では、Automationの詳細画面でモデルがGPT-5.5、ReasoningがHighに設定されています。
 Automationでは、通常チャットとは別に実行モデルを確認する必要がある。
モデル設定が適切でないと、処理が遅くなったり、思ったほど安定しなかったりする場合があります。
特に、毎週のレポート更新のように実行時間が気になる作業では、モデル設定は確認しておきたいポイントです。
また、Excelファイルを開いたままにしていると、Codexが上書きできないことがあります。
これは地味ですが、実務ではよくある問題です。
自動化を組むときは、次のような注意書きをAutomationのプロンプトに入れておくとよいでしょう。
Excelファイルが開かれていて更新できない場合は、その旨を報告する。
失敗した場合は、どの工程で止まったかを明記する。
データが取得できない場合は、空のレポートで上書きしない。
変更がない場合は、無理にコミットしない。
こうしたルールを入れておくと、自動化の信頼性が上がります。
GitHubとVercelで公開する
ローカルで作ったダッシュボードは、自分のパソコン上でしか見られません。
もしチームメンバーやクライアントに共有したいなら、Webに公開する必要があります。
そのときに便利なのが、GitHubとVercelの組み合わせです。
基本的な流れは次の通りです。
Codexでダッシュボードを作る。
GitHubにリポジトリを作る。
CodexからコードをGitHubに送る。
VercelでGitHubリポジトリを読み込む。
デプロイする。
以後、GitHubに変更が送られるたびにVercelが自動更新する。
この構成にしておくと、Codexで作業してGitHubに反映するだけで、公開サイトも自動で更新されます。
小規模なダッシュボードや社内確認用のWebアプリであれば、かなり使いやすい構成です。
もちろん、公開範囲には注意が必要です。
YouTubeコメントのように公開データ中心なら比較的扱いやすいですが、顧客情報や社内データを扱う場合は、認証やアクセス制限を必ず考える必要があります。
日本企業で使う場合、個人情報や機密情報の扱いは特に慎重にすべきです。
Side Chatで作業を分ける
CodexにはSide Chatという便利な機能もあります。
これは、メインの作業スレッドとは別に、同じプロジェクト文脈を持ったサブチャットを開ける機能です。
Side Chatを使うと、メイン作業を止めずに別の質問や確認ができる。
たとえば、メインのチャットではダッシュボード実装を進めているとします。
その途中で、「このAPIの制限ってどうなっている？」「このExcelの列構成は変えた方がいい？」といった別の確認をしたくなることがあります。
そのたびにメインチャットへ質問を混ぜると、作業の流れが散らかります。
Side Chatを使えば、メイン作業の流れを保ったまま、別スレッドで質問できます。
確認が終わったら閉じればよいので、作業ログも整理しやすくなります。
これは小さな機能ですが、長いプロジェクトではかなり効きます。
Personality設定で返答スタイルを変える
CodexにはPersonality設定があります。
Codexの返答スタイルはFriendlyとPragmaticから選べる。
Friendlyは、温かく協力的な返答スタイルです。
説明が丁寧で、会話しながら進めたいときに向いています。
Pragmaticは、簡潔でタスク中心の返答スタイルです。
実務でサクサク進めたい場合はこちらが向いています。
日本の業務利用では、最初はFriendlyでもよいですが、慣れてきたらPragmaticの方が使いやすいと感じる人が多いかもしれません。
特に、毎日のようにCodexを使う場合、余計な説明が多いと少し重く感じることがあります。
Pragmaticにすると、要点を絞って返してくれるので、作業が進めやすくなります。
Full Accessは便利だが慎重に使う
CodexにはFull Accessの設定もあります。
Full Accessを有効にすると作業は速くなるが、権限が広がるため慎重に使う必要がある。
Full Accessを有効にすると、Codexがより広い権限でファイル編集やコマンド実行を行えるようになります。
承認の手間が減るため、作業は速くなります。
ただし、その分リスクもあります。
意図しないファイルを編集してしまう可能性。
ネットワーク経由で外部にアクセスする可能性。
秘密情報を含むファイルに触れる可能性。
誤ったコマンドを実行してしまう可能性。
もちろん、Codexは慎重に動くよう設計されていますが、権限を広げる以上、人間側も注意が必要です。
おすすめは、最初は通常の権限で使うことです。
プロジェクト構成に慣れ、Codexの挙動を信頼できるようになってから、必要に応じてFull Accessを使うのがよいでしょう。
特に、仕事用PCや会社のデータを扱う場合は、安易にFull Accessをオンにしない方が安全です。
Context Windowも意識する
Codexには、会話や作業の文脈を保持するためのContext Windowがあります。
Codexはコンテキスト使用量を表示し、必要に応じて自動的に圧縮する。
長い作業をしていると、会話履歴やファイル内容が増えていきます。
Codexは自動的にコンテキストを圧縮してくれますが、プロジェクトの重要情報はできるだけファイルに残しておく方が安定します。
その意味でも、agents.md やSkillは重要です。
チャットの中だけに情報を置いておくと、長い作業の途中で文脈が薄れることがあります。
一方、プロジェクトファイルとしてルールや手順を残しておけば、Codexはそれを参照できます。
長期的に使うプロジェクトほど、「チャットで説明する」より「ファイルに残す」意識が大切です。
小さな作業から始めるのが現実的
ここまで読むと、Codexでできることが多すぎて、逆に何から始めればよいか迷うかもしれません。
おすすめは、小さな定型作業から始めることです。
たとえば、次のような作業です。
YouTubeコメントを週1回分析する。
Xの投稿案を過去反応から作る。
問い合わせメールを分類する。
営業メモから提案書のたたき台を作る。
CSVを読み込んで簡単なレポートを作る。
社内FAQを更新する。
Notionのメモを整理する。
週次レポートをExcelで作る。
最初から大きな業務システムを作る必要はありません。
むしろ、最初は「毎週やっていて面倒だが、ルール化できる作業」を選ぶのがよいです。
Codexに向いているのは、完全に創造的な仕事だけではありません。
むしろ、繰り返しがあり、入力と出力がある程度決まっていて、毎回少し判断が必要な仕事に強みがあります。
YouTubeコメント分析は、その典型です。
コメントという入力がある。
分類、集計、要約という処理がある。
Excelやダッシュボードという出力がある。
次の動画案や返信候補という判断材料が得られる。
このような作業は、Codexとの相性が非常に良いです。
日本の個人事業主や小規模チームでの活用例
日本でCodexを使うなら、特に個人事業主、小規模チーム、マーケティング担当、コンテンツ制作者に向いています。
たとえば、YouTube運営者なら、コメント分析から次回動画の企画を作れます。
noteやブログを書いている人なら、読者の反応や検索キーワードから記事案を整理できます。
オンライン講師なら、受講者の質問を分類して教材を改善できます。
SaaS企業なら、問い合わせやチャットログを分析してヘルプページを改善できます。
営業担当なら、商談メモから提案内容やフォローアップ文面を作れます。
採用担当なら、応募者からの質問や面談メモを整理できます。
大企業のように大きなシステムを作らなくても、Codexは十分に役立ちます。
むしろ、小さなチームほど効果が出やすいかもしれません。
なぜなら、定型作業を自動化するだけで、人間が本来やるべき判断や企画に時間を戻せるからです。
Codexを使いこなすコツ
最後に、Codexを実務で使いこなすためのコツを整理します。
まず、作業はフォルダ単位で考えること。
プロジェクトごとにフォルダを分け、必要なファイルを整理します。
次に、agents.md を作ること。
プロジェクトの目的やルールをCodexに共有します。
そして、いきなり作業させず、Plan Modeで計画を立てること。
大きな作業ほど、先に流れを確認した方が失敗しにくくなります。
うまくいった手順はSkill化すること。
毎回同じ説明をするのではなく、再利用できるレシピとして保存します。
定期的にやる作業はAutomationにすること。
ただし、ローカル実行ではPCが起動している必要がある点に注意します。
Web画面を作ったらBrowser Useで確認すること。
コードだけでなく、実際の画面を見て使いやすさを確認します。
APIキーや秘密情報は .env.local に保存すること。
GitHubに誤って公開しないようにします。
Full Accessは慎重に使うこと。
便利ですが、権限が広がるため最初は通常設定がおすすめです。
このあたりを押さえるだけで、Codexはかなり実務で使いやすくなります。
まとめ
Codexは、魔法のようにすべてを一発で完璧にしてくれるツールではありません。
最初の実行では失敗することもあります。
API接続でつまずくこともあります。
Excelファイルが開きっぱなしで更新できないこともあります。
ダッシュボードのUIが思ったより普通になることもあります。
Automationの実行が遅いこともあります。
しかし、それらはすべて改善できます。
大切なのは、失敗をその場限りにしないことです。
うまくいった手順はSkillにする。
失敗した原因は agents.md やプロジェクトメモに残す。
毎週の作業はAutomationにする。
画面確認はBrowser Useに組み込む。
プロジェクトフォルダの中に、作業の知識を蓄積していく。
この流れを作ると、CodexはただのチャットAIではなく、自分専用の実務パートナーになっていきます。
今回のYouTubeコメント分析の例では、Codexを使って次のことができました。
YouTubeコメントを取得する。
200件以上のコメントを分析する。
Excelレポートを作る。
よくある質問を抽出する。
返信候補を整理する。
次のコンテンツ案を出す。
Webダッシュボードを作る。
ブラウザで確認する。
Skillとして再利用可能にする。
毎週の自動更新を設定する。
これらが、1つのプロジェクトフォルダの中でつながっています。
日本の現場でCodexを使うなら、「AIに全部任せる」というより、「自分が毎週やっている作業を、Codexと一緒に仕組み化する」と考えるのがちょうどよいです。
まずは小さな作業で構いません。
毎週作っているExcel。
毎回読んでいるコメント。
何度も似たように書いている返信文。
月次でまとめているレポート。
社内に散らばっているFAQ。
投稿後に見返しているSNSの反応。
そうした作業を1つ選び、Codexに手順を整理させ、実行し、Skill化し、必要なら自動化する。
このパターンを身につけるだけで、Codexの価値は一気に上がります。
AI時代に重要なのは、単に便利なツールを知っていることではありません。
自分の仕事の中に、AIが入り込める作業の流れを見つけることです。
Codexは、その流れを作るためのかなり強力な選択肢です。
Codex無料講習会など随時開催予定です！

「いいね」「引用」「フォロー」
お願いします！
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 4. @MakeAI_CEO（2026-05-06 23:17:23）

**URL:** https://x.com/MakeAI_CEO/status/2052165860710859130

Anthropicが本日、ガチで歴史的なニュース2発を同時投下。

1. Claude Code 5時間レート制限を全プランで2倍に
2. Pro/Maxのピーク時間制限を完全撤廃
3. Opus API レート制限を大幅引き上げ（Tier 1で入力1,500%、出力900%増）

しかも理由がヤバい。SpaceXのColossus 1データセンター丸ごと契約、22万のNVIDIA GPU獲得。
昨日まで犬猿の仲だったイーロンと提携した話を全部解説する↓

---

## 5. @Shuhei_Ohno（2026-05-07 04:29:04）

**URL:** https://x.com/Shuhei_Ohno/status/2052244300243915102

Claudeの新しいプラグイン「financial-services」使ってみました。

結論「エグいて」

詳細はツリーにて。
（最後に設定方法も解説しますね）

--- 引用ツイート (https://x.com/claudeai/status/2051679629488865498) ---
New for financial services: ready-to-run Claude agent templates for building pitches, conducting valuation reviews, closing the books at month-end, and more.

Install them as plugins in Cowork and Claude Code, or use our cookbooks to run them in production as Managed Agents.

---

## 6. @MakeAI_CEO（2026-05-07 02:20:51）

**URL:** https://x.com/MakeAI_CEO/status/2052212030887858529

今日、AIエージェント業界の歴史が変わった。

Anthropicが「Code with Claude 2026」で発表↓

1. Claudeが「夢を見る（Dreaming）」機能を研究プレビュー公開
2. Outcomes（成果評価ループ）、マルチエージェントオーケストレーション、Webhooks をパブリックベータ提供開始

「AIが寝てる間に過去の経験を整理して自己進化する」が現実化。ガチで未来の話を全部解説する↓

---

## 7. @masahirochaen（2026-05-07 03:01:36）

**URL:** https://x.com/masahirochaen/status/2052222286699368754

【速報】Anthropicが「Claude Managed Agents」に3機能を一気投入

これはすごいな。話題のHermes agentの機能を搭載したみたいな感じ。

OpenClawもDispatchなどで即座に対応したし、基本OSSで話題になったAIエージェントは全てClaudeに吸収される。

・dreaming：過去セッション横断で記憶を自己更新
・outcomes：ルーブリック採点で成功率＋最大10pt
・multiagent：並列委任＋トレース
・Harveyで完了率約6倍

エージェント運用の標準が一段階上がる

↓詳細

---

## 8. @shota7180（2026-05-06 02:02:11）

**URL:** https://x.com/shota7180/status/2051844947691893187

【Claude Code の活用方法40選】99%の人は、機能の大半を使っていません
3
14
165
4万
Claude Codeを触っている人は増えていますが、使い方はかなり偏っています。
多くの場合、やっていることはシンプルです。
コードを書かせる、文章を整える、ファイルを整理する。
それぞれは有効です。ただ、この使い方のままだと「作業を少し楽にするツール」で止まってしまいます。
Claude Codeは、単発の処理を任せるためのツールではありません。
・タスクを受け取る
・内容を整理する
・処理を分解する
・実行する
・結果をまとめる
この一連の流れを設計して、まとめて任せる。
ここまでできるようになると、作業の一部ではなく、業務の進み方そのものが変わります。
実際に使われている機能も、単体ではありません。
スラッシュコマンド、スケジュール実行、外部ツール連携、Hooks。
これらをつなげて初めて、継続的に処理が回る状態になります。
ここでは、その前提で使える活用方法を40個に整理しました。
単体のテクニックとしてではなく、「どう組み合わせるか」を前提に見てください。
＝＝＝＝＝
仕組みを作るための基本操作を整える（01〜10）
01. 定期タスクを自動で回す
毎週のレポート作成や確認作業など、繰り返し発生する業務で使う
スケジュール実行と外部ツール連携を組み合わせることで、手動対応が不要になり、抜け漏れを防げる
02. 長時間の作業で精度を落とさない
やり取りが長くなり、出力がブレてきたタイミングで使う
文脈を整理し直せるため、途中からでも精度を立て直せる
03. タスクが崩れたときにやり直す
指示が混ざり、意図しない動きをし始めたときに使う
不要な文脈を切り離し、最初から正しく進められる
04. 新規企画の方向性を整理する
プロダクトや施策の全体像を考えるときに使う
抜け漏れなく戦略を整理でき、短時間で骨子が固まる
05. 作業のチェック精度を上げる
コンテンツや資料を最終確認するときに使う
あらかじめ定義した観点で確認でき、品質のばらつきを防げる
06. 文脈のズレを特定する
出力が安定しない、挙動がおかしいと感じたときに使う
どの情報が読み込まれているか把握でき、原因の切り分けができる
07. 不具合の原因を把握する
動作が想定通りでないときに使う
環境や設定の状態を確認でき、問題の特定が早くなる
08. 複雑なタスクを着手前に分解する
複数工程の作業に入る前に使う
/plan とスラッシュコマンドを組み合わせることで、手順を整理した状態で進められる
09. 実行前にコストを把握する
処理が重そうなタスクを実行する前に使う
無駄な実行を避け、リソースの消費を抑えられる
10. 直前の操作をすぐに取り消す
ファイル操作などでミスをした直後に使う
すぐに元の状態に戻せるため、リカバリーが早い
ファイル管理を自動化する（11〜18）
11. ファイル名をルールに沿って一括整理する
ダウンロードフォルダが散らかっているときに使う
内容に応じて自動でリネームされ、管理しやすくなる
12. 重複ファイルをまとめて整理する
同じファイルが複数存在しているときに使う
不要なデータを削減でき、ストレージの無駄を防げる
13. フォルダ構造を自動で整理する
ファイルが雑多に溜まっているときに使う
プロジェクト単位で整理され、探す手間が減る
14. 古いファイルを自動でアーカイブする
長期間更新していないファイルが増えてきたときに使う
現行データと過去データが分離され、作業効率が上がる
15. 過去の資料からテンプレートを作る
提案書や資料を何度も作成しているときに使う
フォーマットを再利用でき、作成時間を短縮できる
16. 複数ファイルから必要な情報を抽出する
大量の資料から特定の情報を探すときに使う
横断的に検索・整理でき、リサーチ時間を削減できる
17. ファイル形式をまとめて変換する
複数のファイルを別形式に変換したいときに使う
手作業が不要になり、変換ミスを防げる
18. ストレージの使用状況を可視化する
容量不足や整理が必要なときに使う
不要なファイルを特定でき、効率的に容量を確保できる
情報処理と業務連携をまとめて回す（19〜26）
19. メール対応をまとめて処理する
未読メールが溜まっているときに使う
分類・返信案作成まで一括で行え、対応時間を短縮できる
20. 会議前の準備情報を自動でまとめる
翌日の予定や会議内容を把握したいときに使う
事前準備が整い、打ち合わせの質が上がる
21. チャットからタスクを抽出する
やり取りの中で指示や依頼が流れてしまうときに使う
外部ツール連携と処理の自動化を組み合わせることで、タスク管理まで一括で整理できる
22. データ分析から資料作成まで一括で行う
数値データをもとに資料を作りたいときに使う
分析からアウトプットまで自動化でき、作業時間を短縮できる
23. メールのやり取りを整理する
やり取りが何往復も続き、話が複雑になっているときに使う
決定事項と未対応事項が明確になり、次の行動が取りやすくなる
24. 複数ソースからレポートを作成する
異なるツールに情報が分散しているときに使う
情報を統合でき、一貫したレポートが作れる
25. 会議内容を関係者ごとに整理する
会議後のタスク共有が必要なときに使う
各人に必要な情報だけ伝えられ、認識ズレを防げる
26. 複数のツールを横断して情報を探す
必要な情報がどこにあるかわからないときに使う
一括で検索でき、情報収集の手間を減らせる
コンテンツ・資料作成を効率化する（27〜34）
27. メモから記事を作成する
音声メモや下書きを文章化したいときに使う
構造化された文章になり、そのまま公開できる状態になる
28. 会議内容を整理して残す
議事録をまとめたいときに使う
決定事項やタスクが明確になり、後から見返しやすくなる
29. 複数資料から要点をまとめる
リサーチ内容を整理したいときに使う
重要なポイントが抽出され、意思決定に使える形になる
30. テンプレートを元に提案書を作る
案件ごとに資料を作り分けたいときに使う
フォーマットを維持しながら、内容を最適化できる
31. 契約書を読みやすく整理する
契約内容を素早く把握したいときに使う
重要なポイントが整理され、確認の手間を減らせる
32. データを文章として説明する
数値データを共有したいときに使う
非専門者にも理解できる形で伝えられる
33. コンテンツを複数媒体向けに展開する
1つのコンテンツを使い回したいときに使う
SNSやメールなどに展開でき、発信効率が上がる
34. 複数記事からニュースレターを作る
週次の情報発信をまとめたいときに使う
内容を選定・整理でき、配信作業を効率化できる
定期業務を自動化する（35〜40）
35. メール処理を毎日自動化する
日々のメール対応を効率化したいときに使う
確認・分類・下書きまで自動で進み、対応負荷が減る
36. フォルダ整理を定期的に行う
ファイルが溜まり続けているときに使う
定期的に整理され、常に整った状態を保てる
37. 週次の計画を自動で作る
週のタスク整理を効率化したいときに使う
優先順位が整理され、スムーズに着手できる
38. 経費管理を自動化する
領収書の処理が溜まっているときに使う
データ化と集計が自動化され、管理が楽になる
39. 競合情報を定期的に収集する
市場動向を把握したいときに使う
変化を継続的に追えるため、判断の精度が上がる
40. 1日の終わりに作業ログを自動で記録する
日々の業務を振り返りたいときに使う
進捗が可視化され、次の行動が明確になる
まとめ
Claude Codeは、調査、文書作成、ファイル管理、外部ツール連携、定期実行。
これらをまとめて処理する「仕組み」です。
使い方が変わると、作業を任せる状態から、業務を任せる状態に変わります。
まずは1つ、試してみてください。
＝＝＝＝＝
Claude Codeは、使い方を知るだけで終わるともったいないです。
自分の業務にどう組み込むかまで考えると、見える景色が変わります。
差が出るのは、この先です。
AIエージェント活用を一歩進めたい方は、こちらから。
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 9. @tetumemo（2026-05-06 23:01:04）

**URL:** https://x.com/tetumemo/status/2052161755401576707

ClaudeのAIエージェントが「寝ている間に学習する」機能が追加されて話題になってます。

https://
x.com/i/status/20520
69321355182447/video/1
…
これ何かというと、Anthropicが発表した「Dreaming（ドリーミング）」という新機能。

① AIが過去の作業履歴を振り返る
② 失敗したパターンや成功したやり方を抽出
③ 次の作業にその学びを活かす
ㅤ
普通のAIって、毎回「初めまして」の状態で作業を始めるから、同じミスを繰り返すことが多かったんですよね 。
ㅤ
でもこの機能を使うと、AIが「あ、このやり方だと失敗するんだった」と過去の経験から勝手に学んでくれる。
ㅤ
つまり、人間が寝ている間にAIが勝手に反省会をして、翌朝にはもっと賢くなっているという仕組み。
ㅤ
これ、AIが「指示されたことをやる」から「自分で考えて成長する」に変わる大きなターニングポイントだと思います。
ㅤ
スレッドでさらに深掘りします↓

--- 引用ツイート (https://x.com/claudeai/status/2052067399088664981) ---
Live from Code with Claude: we're launching dreaming in Claude Managed Agents as a research preview.

Outcomes, multiagent orchestration, and webhooks are now in public beta.

---

## 10. @halukik_0520（2026-05-06 00:32:40）

**URL:** https://x.com/halukik_0520/status/2051822420760395850

【Codex一択】全ビジネスマン今すぐ使った方がいい理由
5
22
165
10万
ClaudeCode、やめました。
今はCodex一択です。


「は...？」
「こないだまでClaudeCode、ClaudeCodeって騒いでたじゃん」
って思った人もいるはず。
ごめんなさい。
でもこれがAI時代の現実です。
最先端のツールは、すぐ変わる。
3~4月はClaudeCodeで衝撃を受けた。

でも今、AIでLP・スライド・HP・記事画像を作るなら、
Codexの方が強いです。


しかもこれ、エンジニアだけの話じゃない。
デザイナーも、マーケターも、経営者も、資料を作る会社員も。
PCで仕事する人は全員、早めに触った方がいい。
今日はCodexを全力で推します。


① Codexは、仕事を終わらせてくれる
Codexを触って一番感動したのはここです。
ちゃんと仕事が終わる。
これがマジで大きい。
AIに相談して、
いい感じの返答が来て、
「なるほど」で終わる。
これだと、仕事は進んでるようで進んでないんですよね。
でもCodexは違う。
「LP作って」と言ったら、
構成を整理して、
ファイルを作って、
画像を入れて、
修正して、
確認して、
どこを触ったかまで返してくれる。
会話で終わらない。
成果物が残る。
この「仕事を代わりにやってくれる感」がかなり強い。
ビジネスマン全員に使ってほしい理由はここです。
資料作成でも、LPでも、社内ツールでも、議事録整理でも、
AIが返答するだけじゃなくて、実際に作業を前に進めてくれる。
この感覚、一回触らないと分からないです。マジで感動します笑


② Image2.0まで使えるのが強すぎる
ここが一番デカいです。
特にデザイナーの僕からすると、
CodexでImage2.0までそのまま使えるのが強すぎる。
これがAI制作ではかなり強い。
今のLP制作は、いきなりHTMLを書かせるより、
先に画像で完成イメージを出した方が早いです。
↓これとかCodexだけで30分とかで作ってます。しかもノンデザイナーが。
メディアを再生できません。
再読み込み
流れはこれ。
① Codexで構成を整理 
② Image2.0でビジュアル案を出す 
③ 良かった案をHTML化 
④ 注釈で細部を修正 
⑤ 必要なら公開
デザイナーにとっては、これはかなり大きい変化です。
手を動かす時間より、
方向性を決める力、良し悪しを判断する力の方が重要になる。
だからこそ、
デザイナーはCodexを触った方がいい。
もちろん、デザイナーだけじゃないです。
LPを作るマーケター、資料を作る営業、企画を形にしたい経営者にも必須。


③ コスパがいい
細かい料金は使い方やプランで変わります。
ただ、現場で使っている感覚として、
Codexはかなりコスパがいいです。
単純に賢いし、
画像生成もできるし、
成果物まで持っていける。
あと体感として、ClaudeCodeよりも長く回せる感じがあります。
トークンや制限まわりで止まりづらい感覚がある。
これ、実務ではかなり大事です。
AI制作って、途中で止まるのが一番しんどい。
ノってきたところで制限が来ると、作業の流れが切れる。
特に、すでにChatGPTに課金している人は、
まずCodexを触った方がいい。
Claude系に追加課金するか悩む前に、
今ある環境でどこまでできるか試した方がいいです。
制限や課金で止まるなら、Codexを触らない理由がない。
Codexは無料プランからも使えるのでとりあえず試すのがおすすめ。


じゃあ、ClaudeCodeはもう不要なのか？
完全に不要と言いたいわけではないです。
ただ、ツールの正解は変わります。
昨日までClaude。
今日はCodex。
明日はまた別の何か。
これが普通になる。
だから大事なのは、
ツールそのものに依存しないこと。
プロンプト、制作ルール、デザインガイドライン、過去の修正履歴、自分のナレッジ。
こういうものをローカルに貯めておく。
そうすれば、AIが変わっても引き継げる。
ツールを乗り換えるたびにゼロからやり直すんじゃなくて、
自分の制作OSを育てる。
これがAI時代の仕事術になると思ってます。


まずCodexでデザインを作ってみてほしい
本当におすすめなのは、
まず1回、Codex × Image2.0でLPかスライドを作ってみること。
これ、昨日のセミナーで実演したんですが、
かなり反響がありました。
実際に参加者からも、
「ClaudeCodeもすごいと思ったけど、Codexがさらにすごいと分かった」「Codexまだ触ってなかったので、早速触ってみます」
「LPが完成していく過程も、スライドが量産される流れも、全部ノーカットで腑に落ちた」
みたいな感想がかなり来てます。

テキストで読むより、実際の作業画面を見た方が早いです。


5/4に開催した
『Image2.0でデザイン制作 実演解説LIVE』のアーカイブを無料配布します。


LP、スライド、HPをAIで作る流れを実際に見せています。
Codex × Image2.0 の感覚を掴みたい人は、
まずこれを見てください。
ノンデザイナーもデザイナーも、普通に必見です。
↓受け取りはこちら
https://liff.line.me/1657292180-JgXbO5A7/landing?follow=%40109dsllv&lp=ThN6B0&liff_id=1657292180-JgXbO5A7


AI時代にデザインで稼ぎ続けるための
『デザインの教科書 5Daysマガジン』も無料で配布してます。
ツールの使い方だけじゃなく、
AI時代に必要な考え方・判断軸・稼ぎ方をまとめた内容です。
固定ポストから受け取れるので、
まだの人は必ず受け取っておいてください。
コンドウハルキ｜Harukaze
@halukik_0520
·
5月2日
\ 完全無料公開 /
【デザインの教科書　5Daysマガジン】　

AI時代に稼ぎ続けるデザイナーの
”思考”と”戦略”を5日間でインストールする短期集中プログラム

▶︎ AIを武器にして右肩上がりに稼ぎ続ける人
▶︎ AIに代替されて消えていく人

この二極化を分けるのは
才能でもスキルでもなく....

すべて『この5Daysマガジン』に書きました。

AIをクリエイティブの最前線で活用するデザイン制作会社代表が見てる”AI時代のデザインの価値”

 AI時代に才能の差を無視して”最速で理想を叶える”ための思考法

月100万を超えるデザイナーが当たり前にしている”本物の基準値”をインストール

AIを活用して案件単価を10倍に上げるデザイナー思考と戦略

スキル本では絶対に書かれない、
"稼げるデザイナーの内側"の話です。

AI時代にこそクリエイターに届けたい、本気の5日間にしました。

受け取り方
①このポストに♡いいね
②「デザインの教科書」とリプ
367
39
484
3.2万


https://liff.line.me/1657292180-JgXbO5A7/landing?follow=%40109dsllv&lp=ThN6B0&liff_id=1657292180-JgXbO5A7
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 11. @1osabori（2026-05-06 07:34:39）

**URL:** https://x.com/1osabori/status/2051928614820893132

欧米圏のClaude Codeガチ勢がAIエージェント量産しまくってクソほど儲けてる方法、Anthropic公式が30分でほぼ全部喋ってもうとるんやけどwww

冗談抜きで、これ日本人で知ってる人1%もおらんでwww
日本語でまとめたから時間あるとき読んで↓

海外で静かに広まってるチート手法知りたい人はブクマ推奨

---

## 12. @MakeAI_CEO（2026-05-06 05:59:00）

**URL:** https://x.com/MakeAI_CEO/status/2051904542896443439

ガチでLPは外注しなくていいな。このクオリティですよAI使ってるみなさん。いや、使ってないデザイナーさんもCodex使いましょう。

本気でプロンプト作り込めば、ガチで使えるLP作れるでしょ。

--- 引用ツイート (https://x.com/MakeAI_CEO/status/2050133272022094057) ---
Claude Code vs Codex 徹底比較｜マネタイズで使うならどっちが正解か現在地を全部晒す
7
56
474
71万
ふざけんなって叫んでる暇はない。2026年4月、Claude CodeとCodeの現在地
「またCodex覚えるのか」って思いませんでした？
正直に聞きます。
このタイトルを見て、「いやマジでさ、Claude Code覚えたばっかなのに、なんで今度はCodexなんだよ」って思ったでしょう。わかります。めちゃくちゃわかります。
私も同じ気持ちでした。
ChatGPT触って、Cursor触って、Claude Code触って、ようやく「これで自分のワークフロー固まったわ」って思った矢先に、OpenAIが2026年3月にCodexを大型アップデートして、4月にはGPT-5.5を載せてきた。NVIDIAが社員1万人で使ってるとか、SWE-bench Verified 87.6%でClaude Opus 4.7に肉薄してるとか、もう情報量が多すぎる。
しかも厄介なのが、X開けば「Codex最強」「いやClaude Codeのほうが」って論争が毎日のように起きてて、よく見ると同じ人が両方絶賛してたりする。「結局どっちなんだよ」って。
ぶっちゃけ、AIツール出るたびにキャッチアップしてたら、本業も副業も回らないんですよね。気づいたら情報収集だけで一日が終わってる、みたいなことが起きる。これが俗に言う「AIツール疲れ」ってやつです。
でも、ここで一回立ち止まってほしいんです。
「ふざけんな」って叫んでる暇は、もうないんですよ。なぜなら、2026年4月時点で、すでにこの2つを使い分けて副業や個人開発で結果を出してる人たちが普通にいるから。あなたが「またかよ」ってぼやいてる間に、彼らは月5万、月30万、なんなら年商数百万の自動化システムを組んでる。これが現実です。
だからこの記事では、ぼやくのをやめて、いったん腹くくって両方の現在地を整理します。徹底比較して、「副業・SNSマネタイズ用途で結局どっち使えばいいの？」に明確な答えを出します。
ぼやいてる人と、動いてる人の決定的な差
ここで一つ、衝撃的な事実をお伝えします。
2026年初頭、Anthropic（Claudeの開発元）のCEOダリオ・アモデイが「最初の従業員1人で10億ドル企業が、2026年中に生まれる可能性がある」と発言しました。これ、最初聞いたとき正直「またビッグマウスかよ」って思ったんですよ。でも、よく考えてみてください。
実際、Claude Codeを使って4ヶ月で507万円のSNS自動化売上を作った人がいる。Web制作未経験の非エンジニアが180日で月5万円の副業収益に到達してる。X上では「副業ゼロからClaude Codeだけで月収100万を達成した3ステップ」を公開してる人もいる。これ、別に特別な才能持ってる人の話じゃないんです。
つまり、何が起きてるかと言うと——「AIツール出るたびに疲れてる人」と「AIツール出るたびに自分の武器に変えてる人」で、収入の桁が変わり始めてる。これが2026年の現実です。
しかも厄介なのが、この差は「最初の3ヶ月」で決まるってこと。Claude Codeが出た2024年〜2025年に飛びついて触り始めた人と、「もう少し様子見してから」って言ってた人で、2026年4月時点ではもう後戻りできないくらい差がついてます。
「いや、俺もうClaude Codeはやってるよ」っていう人。それは合格ライン。でも、Codexがここまで強くなった以上、Claude Codeだけで戦うのは正直キツくなってきてます。なぜなら、Claude CodeとCodexは競合じゃなくて補完関係——片方の弱点をもう片方で埋める使い方が業界標準になりつつあるから。
ここがめちゃくちゃ大事なポイントなので、もう一回言います。
Claude CodeとCodexは「どっちか選ぶ」ものじゃなくて、「どう使い分けるか」で差がつくフェーズに入ってます。
そして、その使い分けを知ってるか知らないかで、副業の生産性は2倍も3倍も変わる。これが今、Xで「両方使ってる」って人が爆増してる理由です。
この記事で約束すること
ここまで読んで「やっぱ両方使うんかよ、めんどくせー」って思った方、もう少し付き合ってください。
この記事では、以下のことを約束します。
第一に、「ふざけんな」って思ってる感情は最後まで否定しません。だって本当にツールが多すぎるんだもん。でも、感情を整理しつつ、「で、結局どうすればいいのか」を必ず提示します。逃げません。
第二に、技術的な数字（ベンチマークとか）も出しますが、「副業・SNSマネタイズで使うならどっち」っていう実用観点で全部翻訳します。SWE-bench Verified 87.6%って言われても、副業勢には何のことかわからないですよね。それを「あなたのnote記事LP制作で何が変わるか」レベルまで落として書きます。
第三に、両方使ってる人のリアルな声を載せます。X上で実際に発信されてる本音、ブログ記事の体験談、副業勢の月収実績、海外Hacker NewsやRedditでの議論——リサーチで集めた一次情報をそのままお見せします。「両方いいと思います！」みたいな腰の引けたまとめは絶対にしません。
第四に、最後には「あなたはこっち使え」って明確に結論を出します。属性別、用途別、予算別で分岐して、迷わなくて済むようにします。読み終わったその日から、行動できる状態にします。
正直、この記事は5万文字あります。長いです。途中で疲れるかもしれません。でも、これを読み切った3時間後のあなたは、もう「ふざけんな」って言わなくていい状態になってます。なぜなら、AIツールに振り回される側じゃなくて、選ぶ側に立ててるから。
そろそろ本題に入りましょう。次の章では、なぜ「AIツール疲れ」を放置すると副業勢から脱落するのか、その構造を解説します。ここを理解しないまま個別ツールの話に入っても、また次のツールが出たときに同じ「ふざけんな」を繰り返すことになるので、絶対飛ばさず読んでください。
第1章：「AIツール疲れ」を放置すると、副業勢から脱落する
ツール疲れは「実は努力不足」じゃない
最初に断っておきます。AIツール疲れは、あなたの努力不足じゃないです。
これ、本当に大事な前提なので、最初にハッキリ言わせてください。「ついていけてない自分が悪い」って思い込んでる人、めちゃくちゃ多いんですけど、違います。本当に情報量が異常なんです。
具体的に2026年に入ってから何が起きたか、数えてみますね。
1月：Claude Sonnet 4.5登場、Claude Code Skillsの拡充
2月：Cursor、Windsurf、Devin、Cline……エージェント型ツールが乱立
3月：OpenAIがCodexを大型アップデート、CLIに本格参入
4月：Claude Opus 4.7リリース、GPT-5.5登場、Codex CLIにcomputer use機能、Claude Codeデスクトップアプリ刷新
これ、たった4ヶ月の出来事です。これで疲れない人がいるなら、その人はAI業界で生計立ててる人か、人間じゃないかのどちらかです。
実際、Zennに上がってる記事で「AIツール疲れしてない？2026年サバイバルのための『選ばない』技術」っていうのがあって、これがめちゃくちゃバズってるんですよ。何で読まれてるかって、みんな同じこと感じてるからです。「もう全部追えない」「でも遅れたくない」「結局どれ使えばいいの」って。
しかも、ここに追い打ちをかけるのが、Qiitaに投稿された「約9割の開発者がAIツールで遅くなっている」っていう記事。読むと、AIツール導入で生産性が下がってる人が、実は多数派だってデータが出てます。理由は単純で、ツールに振り回されて、本来の作業に集中できてないから。
つまり、AIツール疲れは構造的な問題なんですね。あなたが弱いんじゃない。ツールが多すぎて、しかも進化が速すぎて、人間の認知リソースの限界を超えてる。これが本質。
だから、まずやるべきは「全部追うのをやめる」って決断です。これができないと、Claude CodeとCodexの話を始めても、半年後にまた新しいツールが出てきて「ふざけんな」って繰り返すだけ。
2026年、AI開発ツールはとっくに「インフラ」になった
ここでもう一つ、視点を変える話をします。
2026年4月時点で、AI開発ツールはもう「便利なツール」じゃないんです。「インフラ」になってます。これがどういうことか、具体例で説明しますね。
電気とかインターネットって、別に使うのが偉いとか進んでるとかじゃないですよね。使えて当たり前。使わないと仕事にならない。AI開発ツールも、もうそのレベルに入ってます。
例えばUberみたいな大企業でも、社内ではClaude CodeとCodexを両方使い分けてるって報告が出てます。NVIDIAは社員1万人がGPT-5.5搭載のCodexを日常的に使ってる。Anthropic社内では、エンジニアがClaude Codeで自社のClaude Codeを開発してる。これが2026年の業界標準。
副業や個人開発の世界でも、状況は同じです。ココナラでWeb制作の案件取ってる人は、ほぼ全員Claude CodeかCursor使ってる。note書いて販売してる人は、ChatGPTかClaudeで構成練ってる。X運用してる人は、Threadsの自動投稿システムをClaude Codeで組んでる。
ここで質問です。あなたが今から「AIツールなしで副業始めます」って言ったら、どうなると思います？
答え：勝てません。マジで。
時給換算したら、ライバルが時給1万円相当の生産性で動いてる中、あなたは時給1,000円で戦うことになる。これは精神論じゃなくて、純粋に作業量の話です。Claude Codeで30分でできるLP制作を、AIなしで6時間かけてやってたら、永遠に追いつけない。
だから、「AIツール疲れ」を放置するのは、副業の世界では「インフラを使わない選択」と同じ意味になります。電気使わずに事業やるくらい、無理ゲーなんですよ。これが2026年の現実です。
じゃあどうすればいいか。答えは「インフラとしての必須2つだけ押さえる」です。それが、この記事のテーマであるClaude CodeとCodex。次の節で、なぜこの2つに絞るのか、根拠を説明します。
「全部追う」をやめると、選択肢が見えてくる
ここで思い切った提案をします。
Cursor、Windsurf、Devin、Cline、Aider、GitHub Copilot Workspace……これら全部、いったん忘れていいです。
え、って思いますよね。「いやでもCursor人気じゃん」「Windsurfも気になってた」って。気持ちはわかります。でも、副業・SNSマネタイズという観点で見たとき、2026年4月時点での最適解は明確にClaude CodeとCodexの2つに絞られます。理由を3つ挙げます。
理由1：Claude Code（Opus 4.7）とCodex（GPT-5.5）が、コーディング性能ベンチマークで他を引き離してます。Claude Opus 4.7はSWE-bench Verifiedで87.6%、SWE-bench Proで64.3%。Codex CLIはTerminal-Bench 2.0で77.3%。GPT-5.4比較で14%の性能向上、ツールエラーは3分の1。これらの数字を超えるツールは、4月時点では存在しません。
理由2：エコシステムが成熟してます。Claude CodeにはSkills機能、Subagent、MCP、Plugins、Git worktree対応、デスクトップアプリ……「インフラ」と呼べる土台が揃ってます。CodexはChatGPT、CLI、VS Code、macOSアプリ、Webと、あらゆる入り口から使える。他のツールはまだここまで完成してない。
理由3：副業勢のコミュニティが既に2つに収束してきてる。X見てもブログ見ても、結局Claude CodeとCodexの話ばかり。「Cursorからの乗り換え」「Windsurf試したけど結局Claude Code」みたいな投稿が、2026年に入ってから加速度的に増えてます。
これ、どういうことかと言うと、選択肢が絞られたほうが、結果的にラクなんですよ。「全部試して比較する」って、一見効率的に見えるけど、実は時間の無駄。なぜなら、業界が収束してきてる方向に乗ったほうが、情報も人脈も案件も集まるから。
例えば、2025年にCursorで頑張ってた人は、2026年に入ってClaude CodeとCodexにシフトしてる人が大半です。なぜなら、Skillsとか、Subagentとか、computer useとか、後発の機能が一気に来たから。Cursorも進化してるけど、Claude Code＋Codexの組み合わせには現時点で勝てない。
だからここで一回、決め打ちしましょう。「副業・SNSマネタイズで結果出すなら、Claude CodeとCodexの2つだけ押さえる」——これが2026年4月の最適解です。他のツールが気になったら、それは半年後に検討すればいい。
Claude CodeとCodex、この2つだけ押さえれば現状OK
じゃあ、Claude CodeとCodexを押さえることで、具体的に何ができるようになるのか。ここを明確にしておきます。
副業・SNSマネタイズで必要な作業を、ざっと並べてみます。
· LP制作（note販売LP、講座LP、商品LP）
· ブログ記事執筆（noteの有料記事、Substack、自社メディア）
· SNS投稿作成（X、Threads、Instagramキャプション）
· 動画台本作成（YouTube Shorts、TikTok、Reels）
· スライド資料作成（講座スライド、ウェビナー資料）
· 顧客管理・売上分析（Excel、CSV、Notion）
· 自動化スクリプト（投稿自動化、メール返信自動化）
· 会員サイト構築（決済込み、認証込み）
· 画像・動画生成（サムネ、商品画像、ショート動画）
· フォーム制作（リード獲得、アンケート、申込フォーム）
これ全部、Claude CodeとCodexの組み合わせで対応可能です。マジで全部。
具体例を1つ。「note記事を書いて、それを元にLPを作って、Threadsで告知投稿を10本作る」っていうワークフロー。これを従来の手作業でやると、たぶん1週間かかります。デザイナー外注したら数十万かかります。
これをClaude Code＋Codexでやると、半日で全部終わります。Claude Codeでnote記事を書いて、Skillsを使ってThreads投稿に展開して、CodexでLPのコードを書いて、ローカルで確認して、Vercelにデプロイ。「半日」って、誇張じゃなくて本当です。Xで実際にやってる人の投稿が山ほどあります。
しかも、この作業に必要な月額コストは、Claude Code Max 5xプラン（月100ドル）+ ChatGPT Plus（月20ドル）= 月約120ドル、日本円で18,000円くらい。デザイナー外注1案件分で、ほぼ無限に作業できる。これはコスパおかしいレベル。
ここで重要なのが、「Claude Codeだけ」とか「Codexだけ」じゃダメな理由。Claude Codeは長尺の文章作成、プロジェクト全体の文脈理解、Skillsによる自分専用ワークフロー化に強い。一方、Codexは速いコーディング、Plan→実装の精度、セカンドオピニオン的なレビューに強い。両方使うことで、お互いの弱点を消せるんですよ。
X上で「Claude Codeで作ったPlanをCodexでレビューするの良さそう！」っていう投稿がバズったんですが、まさにこの使い分けが副業勢にも効きます。Claude Codeで書いた記事をCodexにレビューさせる、Claude Codeで作ったLPをCodexで品質チェックさせる、みたいな使い方が、2026年の標準になりつつある。
まとめ：疲れる側でいるな、選ぶ側に立て
第1章の結論を一言でまとめます。
「ふざけんな」って叫んで疲れてる側にいるか、「2つだけ押さえる」って決めて選ぶ側にいるか。これがあなたの2026年を決めます。
もう一度整理しますね。
AIツール疲れは構造的な問題で、あなたの努力不足じゃない。でも、放置すると副業の世界では確実に脱落する。なぜなら、AI開発ツールはもう「便利なもの」じゃなくて「インフラ」になってるから。
そして、インフラとしての最適解は、2026年4月時点ではClaude CodeとCodexの2つだけ。CursorもWindsurfも、いったん忘れていい。なぜなら、業界が既にこの2つに収束してきてるから。
この2つを押さえることで、副業・SNSマネタイズで必要な作業——LP制作、記事執筆、SNS投稿、自動化、会員サイト構築、画像生成まで——ほぼ全部対応できる。月18,000円くらいのコストで。
ここまで読んで、「いや、それでもふざけんなって気持ちは消えない」って思う方もいると思います。それも正直で良いです。でも、感情と行動は分けましょう。「ふざけんな」って思いながら、手は動かす。これが副業で結果出してる人たちの共通点です。
次の章からは、いよいよClaude CodeとCodexのそれぞれの正体を、ガチで詳しく解説していきます。第2章でClaude Code、第3章でCodex。両方の特徴、強み、弱み、料金、最新機能を、副業勢の観点で全部晒します。ここから先が本番です。
第2章：Claude Codeの正体—2026年4月時点のガチ情報
Claude Codeって、結局なんなの？
まずシンプルに、Claude Codeが何者なのかをハッキリさせます。
Claude Codeは、Anthropic（Claudeを作ってる会社）が出してる「ターミナルで動くAIエージェント」です。「エージェント」って言葉、ちょっと曖昧なので具体的に言うと、あなたのPCの作業フォルダに入って、ファイルを読んだり書いたり、コマンド実行したり、ブラウザでサイトを確認したりまで、自律的にやってくれるAI。
「いや、ChatGPTやClaude.aiでもできるじゃん」って思うかもしれない。でも違うんです。決定的な違いは「あなたのファイルを直接触れる」かどうか。
例えば、ChatGPTで「LPを作って」って頼んだら、HTMLとCSSのコードが返ってきます。でも、それをコピーして自分のフォルダに保存して、ファイル名つけて、ブラウザで開いて確認して、修正があったらまた質問して……この往復が必要。
Claude Codeなら、「このフォルダにLP作って、ブラウザで確認して、スマホ崩れてたら直して」って一言で全部終わります。実際に`index.html`、`styles.css`、`script.js`を作って、ローカルサーバー立てて、ブラウザで開いて、見た目崩れてたら直すところまで自分でやる。
これが「エージェント型AI」の本質です。チャットで答えるだけじゃなくて、作業を完遂する。
2026年4月16日にClaude Opus 4.7がリリースされて、Claude Codeの中身もこれに更新されました。SWE-bench Verifiedで87.6%、SWE-bench Proで64.3%。これは2026年4月時点で世界最高クラスのコーディング性能です。GPT-5.4を超えて、Gemini 3.1 Proも超えてる。
しかも、Anthropicの内部テストで「Rakuten-SWE-Bench」っていうのをやったら、Opus 4.7がOpus 4.6の3倍の本番タスクを解決したらしい。3倍ですよ、3倍。これがどれだけヤバい数字かと言うと、ベンチマーク上の伸びだけじゃなくて、実務で本当に使い物になるレベルが一気に上がったってこと。
2026年4月時点で押さえるべき新機能
Claude Codeの進化スピードがエグいので、2026年4月時点で押さえるべき新機能を整理します。
まず、1Mトークンのコンテキストウィンドウ。これがGA（一般提供）になりました。1Mトークンって、日本語で言うと約75万字。これ、何ができるかと言うと、「数百ページの仕様書を丸ごと読み込んでコードを書く」「プロジェクト全体のファイル構造を一度に理解する」レベルの処理が現実的になりました。副業文脈で言うと、過去の自分のnote記事30本全部読み込ませて、それを元に新しい記事を書かせるみたいなことができる。
次に、Subagent @mention機能（2026年4月追加）。Claude Codeのセッションの中から、特定の専門エージェント（Subagent）を呼び出せます。例えば、「@design-reviewer このLPのデザインレビューして」「@security-auditor この決済ページのセキュリティチェックして」みたいに、用途特化のエージェントを使い分けられる。これは複雑なプロジェクトの並列処理にめちゃくちゃ効きます。
Git worktree対応（–worktreeフラグ）も大きい。これは、同じプロジェクトの違うブランチを並列で作業できる機能。例えば、「ブランチAでLP作りながら、ブランチBで記事執筆」みたいな並列開発がリスクなくできる。副業で複数案件を回してる人には地味に効く。
デスクトップアプリ刷新（2026年4月14日）も話題でした。複数のClaude Codeセッションを並列で扱いやすくなって、「並列エージェント時代」に合わせて再設計されました。実質、ChatGPTのデスクトップアプリよりUXが洗練されてる、っていう声がXで多数。
ネイティブ音声モード（/voiceコマンド）も入りました。スペースキー長押しのPush-to-Talk方式で、日本語含む20言語に対応。追加コストなし。これ、運転中とか散歩中にClaude Codeに指示出せるってこと。マジで未来感ある。
そして、副業勢に一番効くのがSkills機能の拡充。Skillsっていうのは、特定の作業に特化した「手順書つき能力」のことで、例えば「Threads投稿用Skill」「LP制作Skill」「医者権威投稿Skill」みたいに、自分の仕事の型をAIに渡せる。GitHubの`awesome-claude-code`リポジトリには、すでに何百ものSkillsが公開されてて、これがエコシステムとしての強さになってます。
Claude Codeが副業勢に強い理由
ここから、副業勢の観点で「なぜClaude Codeが強いのか」を整理します。
理由1：コンテキスト把握力が圧倒的。Claude Codeは「対話型のシニアエンジニア」として設計されてます。プロジェクトのファイル構造、既存のコード、過去の会話、ユーザーの好みを覚えていて、それに合わせた提案をしてくれる。副業で「過去の自分のnote記事のトーンに合わせて新記事を書いて」みたいな依頼が、めちゃくちゃ精度高くできる。
理由2：Skills機能で自分の型を持たせられる。例えば、「自分のLPの基本構成」「自分のThreads投稿の型」「自分の講座スライドの章立て」をSkill化しておけば、毎回ゼロから指示しなくていい。リピート作業の時間が劇的に減ります。Yomo WebbっていうWebマーケメディアのブログには、Skills機能で実際に作業を自動化したコードが全公開されてます。
理由3：Claude Coworkとの連携。CoworkはAnthropicが出してる別ツールで、Claude Codeと連携することで、SNS同時投稿、Canva連携、ブログ記事からInstagram投稿への変換とかができる。実際、しのジャッキーさんっていう発信者がCoworkでX・LinkedIn・Facebookに同時投稿するスキルを作って公開してます。
理由4：長文コンテンツに強い。1Mトークンのコンテキストウィンドウのおかげで、有料note（1万字〜5万字）の執筆、講座スライド15枚分のテキスト、商品LPの全コピーを、一回の文脈で扱える。これは記事販売や講座販売をやってる副業勢には決定的な強み。
理由5：MCPでObsidianと連携できる。Obsidianっていうメモアプリと連携できて、自分の過去メモから素材を拾って、それを元に投稿や記事を作れる。「ネタ帳から発信を量産する」って副業の王道パターンが、Claude CodeとObsidianの組み合わせで成立する。
Claude Codeの弱点—正直に晒す
ここまで褒めまくったので、次は弱点を正直に晒します。記事の信頼性のためにも、ここは絶対飛ばさない。
弱点1：料金プランが混乱してる。2026年4月21日に、Anthropicが「Pro 20ドルプランからClaude Codeを削除する」って発表して、X上で大炎上しました。その後撤回されたんですが、「結局20ドルで使えるのか？」が4月時点でまだ曖昧。海外のSimon Willisonさんもブログで「This is all very confusing（マジで混乱してる）」って書いてます。
弱点2：レート制限が厳しい。これは海外Reddit/Hacker Newsで一番不満が出てる点。Pro 20ドルプランだと「複雑なプロンプト1〜2回で5時間制限の50〜70%消費する」っていう報告が多数。本気で使うならMax 5x（100ドル）以上が事実上の必須。
弱点3：重い・遅い問題。2026年に入ってから、特にQiitaで「Claude Codeが急に遅くなる」「最初のトークンが返るまで15秒以上かかる」って報告が増えてます。原因は、1M context、subagents、MCPなど機能が増えすぎて、雑に使うと崩れやすくなってる。
弱点4：コンテキストが長くなると性能が落ちる。Anthropic公式のBest Practicesでも明記されてますが、長い会話だとClaude Codeは最初に設定した制約を忘れがちになる。「フォーマット指定したのに守られない」「設計方針を途中から無視する」みたいなことが起きる。対処法は`/clear`で適度にリセットすること。
弱点5：初学者には設定が複雑。CLAUDE.md、hooks、MCP、Skillsの組み合わせを使いこなすには、それなりの学習コストがいる。「とりあえず触る」レベルなら良いけど、本気で副業に使うなら最初の設定で1〜2週間溶けることを覚悟しといた方がいい。
これらの弱点、Codexと比較するとどう違うのか。それは次の第3章で詳しく見ていきます。
Claude Codeを副業で使うときの実践イメージ
最後に、Claude Codeを副業で使うときの具体的な動きを、実例ベースで描いておきます。
ケース1：有料note記事の執筆。過去の自分のnote記事をClaude Codeに読み込ませて、トーンを学ばせる。新記事のテーマを伝えて、章立て→見出し→本文ドラフト→推敲→最終稿まで、一気通貫で書かせる。Skills機能で「自分の文体テンプレ」を作っておけば、毎回0から指示しなくていい。所要時間：構成30分、本文1〜2時間、推敲1時間。合計3〜4時間で、従来1日かかってた記事が完成。
ケース2：販売LPの制作。記事を書き終わったら、その記事を元にClaude Codeに販売LPを作らせる。`vercel:nextjs`っていうSkillで、Next.jsベースのLPをShadcn/uiで実装。Stripeも組み込み。ローカルで確認して、Vercelにデプロイ。所要時間：3〜5時間。デザイナー外注なら20万コースの作業が、ほぼ無料で完成。
ケース3：SNS投稿の量産。Claude CodeのSkillsで「Threads投稿Skill」「3スライド投稿Skill」を仕込んでおいて、記事のテーマからSNS投稿を10本ずつ生成。Obsidian Vaultにある過去メモも参照させて、自分の言い回しを保つ。所要時間：1時間で30投稿。
ケース4：会員サイトの構築。Claude Codeに「note販売した有料記事のメンバー専用閲覧サイトを作って」と頼む。認証、決済、コンテンツ配信、管理画面まで実装。所要時間：1日。これも従来なら数十万円の外注案件。
ここまで読んでもらえれば、Claude Codeが副業勢にとってどれだけ強力なインフラかわかると思います。次の章では、もう片方の刺客、Codexの正体を見ていきます。
第3章：Codexの正体—GPT-5.5を背負った刺客
Codexって、結局なんなの？
次はCodexの番です。
Codexは、OpenAI（ChatGPTの会社）が出してるAIコーディングエージェント。Claude Codeと同じく、ターミナルで動くCLIツール、VS Code拡張、ChatGPT Webアプリ、macOSデスクトップアプリ、複数の入り口があります。
「あれ、Codexって昔からなかったっけ？」って思う方、鋭いです。実は2021年頃にもCodexっていうのがあって、GitHub Copilotの基盤になってたんですけど、いったん消えました。それが2025年に「新しいCodex」として復活して、2026年3月の大型アップデートと4月のGPT-5.5搭載で、一気に化けました。
Claude Codeとの最大の違いは、「クラウドで動く」って点。Claude Codeはあなたのローカルマシンで動いて、ファイルもローカルに保存されます。Codexはクラウドのサンドボックス環境でタスクを実行できる（もちろんローカルCLIでも使える）。これが何を意味するかと言うと、「重い作業を投げて放置できる」ってこと。例えば、「このリポジトリの全ファイルにテストを追加して」みたいな数時間かかる作業を、ChatGPT上から指示して放置できる。
そして、2026年3月15日にOpenAIが正式にCodexのGPT-5.5搭載を発表しました。GPT-5.5は、OpenAIの最新フラッグシップモデルで、複雑なコーディング、コンピュータ利用、ナレッジワーク、リサーチ用途に特化してます。
Codexの強みを一言でまとめると、「タスクを任せられるクラウドワーカー」です。Claude Codeが「対話型のシニアエンジニア」だとすると、Codexは「依頼を投げたら勝手に進めて、終わったら報告してくれる外注ワーカー」のイメージ。
2026年4月時点のCodex最新機能
Codexの最新機能を、2026年4月時点で押さえるべきものに絞って解説します。
まず、GPT-5.5搭載。これが最大のアップデート。GPT-5.5の特徴は3つあります。1つ目、トークン効率がエグい。同じタスクに必要なトークン数がGPT-5.4比で大幅減。2つ目、速度が速い。GPT-5.4のHighモードで5〜6分かかってた処理が、5.5のMediumモードで2分半で終わる、という体感報告がある。3つ目、複雑なIssue対応で「指示通り完了させる力」が一段上がった。Plan→ツール使用→自己検証のループが内部で回せるようになって、人間の介入なしで最後まで仕上げる。
次に、computer use機能。CodexがあなたのmacOSアプリを「見て、クリックして、入力する」ことができるようになりました。これ、副業勢にとって結構ヤバい機能です。ネイティブアプリのテスト、シミュレーターでの操作、GUI専用のバグ調査ができる。例えば「KeynoteでこのテンプレートからスライドAB作って、PDF書き出しまでやって」みたいな依頼が成立する。
Amazon Bedrock対応も入りました。AWS SigV4署名やAWS資格情報認証に対応して、エンタープライズ環境でもCodexが使いやすくなった。これは個人副業には直接関係ないですが、業界としての成熟度を示す指標。
TUIの改善も実用的。Alt+, でreasoningレベルを下げる、Alt+. で上げる。モデル切り替え時にreasoning設定が新モデルのデフォルトにリセットされる。地味だけど、CLIで一日中使う人には効く改善。
App-server sessions機能で、複数の環境を管理できるようになった。プロジェクトごとに違う作業ディレクトリ、違う設定で動かせる。マルチワークスペース運用がしやすくなった。
そして、副業勢に一番効くのはChatGPT統合。Codexは独立ツールではなくて、ChatGPTの一部として使える。ChatGPTで「このPRレビューして」「このリポジトリのバグ直して」って指示すると、Codexがクラウドで実行して、結果をチャットに返してくれる。これは「コードを書く専門の手」がChatGPT内に内蔵されてる感覚。
Codexが副業勢に強い理由
Codexが副業勢にとってどう強いのか、整理します。
理由1：ChatGPT 20ドルプランで使える。これがマジで大きい。海外Redditの最大の不満が「Claude Code Pro 20ドルは複雑プロンプト1〜2回でレート制限に引っかかる」だったのに対し、Codexは20ドルで「コードを一日中書ける」って評価されてる。コスパで言うと圧倒的。
理由2：初期設定が軽い。Claude CodeはCLAUDE.mdとかhooksとか設定が多いけど、Codexはインストールしてログインすれば即使える。「初期設定なしで即戦力になる」っていう評価が、特に副業初心者から強い。
理由3：コード品質が安定してる。Qiitaの「同じアプリを作って比較した」検証では、コード品質スコアが「Codex 81.0点 / Claude Code 76.8点」で、特に保守性とエラーハンドリングでCodexが上回ってる。「Codex CLIは複雑なロジックや大規模システム設計でClaude Codeより高品質なコードを生成する」っていう評価が複数の検証記事で出てる。
理由4：速度が速い。Terminal-Bench 2.0で77.3%を取ってる通り、ターミナル作業の速度はCodexが優位。Claude Codeが65.4%なので、約12ポイント差。日常的にCLIで作業する副業勢には地味に効く。
理由5：バグが少ない。「0からの実装ではCodexのほうがバグが少ない」っていう評価が複数のレビュー記事で出てます。一回で動くコードが返ってくる確率が高い。これは副業で時間が限られてる人には決定的に重要。
理由6：セカンドオピニオンとして使える。OpenAI公式の`codex-plugin-cc`っていうプラグインがあって、Claude CodeのセッションからCodexを呼び出して、コードレビューさせられる。「Claude Codeが書いたコードをCodexにレビューさせる」っていう使い方が、業界標準になりつつある。
Codexの弱点—こちらも正直に晒す
Codexにも弱点があります。Claude Code推しの人が見落としがちなポイントも含めて、晒します。
弱点1：コンテキスト把握力でClaude Codeに劣る。Codexは「限られたコンテキスト窓内での情報しか参照できず、プロジェクト全体の設計方針や既存コードとの整合性を完全に理解することは困難」っていう評価が出てます。長尺のプロジェクトをまるごと理解させたいときは、Claude Codeのほうが優位。
弱点2：カスタマイズ性が低い。Claude CodeはSkills、hooks、MCP、Subagentで細かくカスタマイズできるけど、Codexはカスタムコマンド程度。自分専用のワークフローを作り込みたい人には、物足りなく感じることがある。
弱点3：利用制限が突然来る。Codexは「5時間制限」と「週次制限」を同時に管理してて、週次を使い切ると5時間枠が残ってても続けて使えない。しかも警告なしに突然来るから、作業が中断される不満が多い。
弱点4：新しいフレームワークやライブラリへの対応が遅いことがある。学習データのカットオフの関係で、最新のAPIや非推奨パターンを提案してくることがある。これはClaude Codeも同じ問題があるけど、Codexのほうが顕著という報告がある。
弱点5：セキュリティリスク。これはどちらにも言えるけど、Codexが生成するコードには、SQL Injection、NoSQL Injection、Command Injectionなどの脆弱性が含まれる可能性が指摘されてる。本番に出す前のセキュリティチェックは必須。
弱点6：料金プランの変更が激しい。2026年4月にChatGPT Pro 100ドルプランが新設されて、Codexの利用枠が再編されました。「以前はこれで足りてたのに、今月から足りない」みたいなことが起きやすい。
Codexを副業で使うときの実践イメージ
Codexを副業で使うときの具体的な動きを、実例ベースで描きます。
ケース1：リポジトリ全体のバグ修正。「このリポジトリの全テストを通して、失敗してるテストは全部修正して」って指示を出して放置。クラウドサンドボックスで自動実行されて、PRが立つ。所要時間：人間の作業30分、AIの自動作業数時間。
ケース2：Plan→実装の高速化。Claude Codeで設計（Plan）を立てて、その実装をCodexに投げる。「Codexが書く速度はClaude Codeの2倍くらい」っていう評価がある通り、実装フェーズで時短になる。所要時間：Plan 30分、実装1時間。
ケース3：PRレビューの自動化。GitHubのPRに`@codex`タグでメンションすると、Codexが自動でレビューコメント書いてくれる。これ、副業でクライアント案件持ってる人には超強力。
ケース4：ローカルアプリの操作自動化。computer use機能で、Keynoteでスライド作成、Excelで集計表作成、Photoshopで画像書き出し、みたいなGUI作業を自動化できる。所要時間：30分の指示で、3時間分の作業が完了。
ケース5：ChatGPT内でのワンストップ作業。ChatGPTで記事の構成相談→そのままCodexに「この内容でLP作って」と指示→クラウドで実装→Vercelデプロイまで。ChatGPTから出ずに完結する。所要時間：2〜3時間。
Claude CodeとCodex、ここまでで見えてきた違い
第2章と第3章で、両方の正体を見てきました。ここまでで見えてきた違いを、ザックリまとめます。
📷
これだけ見ると、「あれ、Codexのほうが良くない？」って思った方もいるかも。でも、Claude CodeにはSkillsとObsidian連携、長文耐性っていう、副業勢にとって決定的な武器があります。だから単純比較じゃなくて、「どっちがどの用途で強いか」を理解することが大事。
次の第4章では、機能をもっとガチで比較します。ベンチマーク数字、コード品質、速度、UI/UX、エコシステムまで、全部見ていきます。
第4章：機能ガチンコ比較—ベンチマーク・速度・コード品質
ベンチマーク数字を、副業文脈に翻訳する
まずベンチマーク数字を整理して、それを副業文脈に翻訳します。
2026年4月時点の主要ベンチマークはこう：
SWE-bench Verified（既知の実プロジェクトのバグ修正タスク）
· Claude Opus 4.7：87.6%
· GPT-5.4：85.0%（GPT-5.5の数値は未公表だが向上見込み）
· Gemini 3.1 Pro：80.6%
SWE-bench Pro（より難しい、汚染の少ない問題）
· Claude Opus 4.7：64.3%
· GPT-5.4：57.7%
· Gemini 3.1 Pro：54.2%
Terminal-Bench 2.0（ターミナル作業の精度）
· Codex CLI：77.3%
· Claude Code：65.4%
Rakuten-SWE-Bench（Anthropic内部テスト）
· Opus 4.7：Opus 4.6の3倍のタスク解決
これ、数字だけ見ても「で？」って感じだと思うので、副業文脈に翻訳します。
SWE-benchは「既存コードのバグ修正能力」のテスト。副業文脈で言うと、「既存のLPテンプレートをカスタマイズして、不具合を直す」みたいな作業の精度。Claude Opus 4.7が87.6%、GPT-5.4が85.0%。差は2.6ポイント。これは正直、副業実用では誤差レベル。どっちでも問題ない。
SWE-bench Pro（より難しい問題）では差が広がって、Claude Opus 4.7の64.3% vs GPT-5.4の57.7%、6.6ポイント差。複雑な案件ではClaude Codeのほうが安定するイメージ。
Terminal-Bench 2.0は「ターミナル作業の正確性」。Codex CLIが77.3%、Claude Codeが65.4%。これは12ポイント差で、結構大きい。「コマンド実行を多用する作業」では Codex 優位。
ここで重要なのが、ベンチマーク数字の差は、実務では「3倍速い・遅い」みたいな極端な体感差にはならないってこと。両方とも実用レベルでは「使い物になる」のは確実。差が出るのは、複雑性が上がったときと、特定タスクの得意/不得意。
副業勢にとって意味のある翻訳をすると、こうなります：
· 「LP作って」「note記事書いて」みたいなシンプルタスク → どっちでもほぼ同じ
· 「複雑な会員サイト構築」「決済込みSaaS」 → Claude Codeがやや優位
· 「コマンド多用する自動化スクリプト」「定型のCLI作業」 → Codex優位
· 「PRレビュー・既存コードのリファクタ」 → Codex優位
コード品質、ガチで比較した結果
次にコード品質。これは複数の検証記事で実測されてます。
Qiitaに上がってる「Claude Code vs Codex：同じアプリを作ってコード品質を比較してみた」っていう検証記事では、同じ要件で同じアプリを作らせて、コード品質をスコア化してます。結果はこう：
· Codex：81.0点
· Claude Code：76.8点
特に差が出たのが「保守性」と「エラーハンドリング」。Codexのほうが、後から見たときに整理されてて、エラー処理が丁寧。これは「タスクを任せられるクラウドワーカー」っていう設計思想が反映されてる結果。
一方で、Claude Codeは「コンテキスト把握力」と「ユーザーの意図汲み取り力」で上。例えば、「過去の会話で言ってた方針」を覚えてて、それに合わせてくる精度はClaude Codeのほうが高い。
ここでX上の興味深い投稿を紹介します。「@masa_oka108」さんが「Claude Codeで作ったPlanをCodexでレビューするの良さそう！」って投稿して、これがバズりました。これは、両者の特性をうまく活かす使い分けです。
つまり、
1. Claude Codeで「文脈理解」「設計（Plan）」を担当させる
2. Codexで「実装」「品質チェック」を担当させる
この役割分担で、両者の強みを最大化できる。
海外でも同じパターンが流行ってて、Hacker Newsの「Codex vs. Claude Code (today)」スレッドで「I prefer Claude for the small tasks and fast iteration pair coding experience」っていうコメントに高評価が集まってる一方、別のスレッドでは「Some developers use a pattern where Codex drafts and Claude reviews, as the two models catch different classes of mistakes」（CodexがドラフトしてClaudeがレビューするパターン。両モデルは違う種類のミスを捕まえる）っていう知見が共有されてます。
つまり、「どっちがレビューでどっちがドラフトか」は、人によって逆になることもある。重要なのは「両方のモデルが違う観点で見る」ことで、品質が上がるってこと。
速度比較、これは体感差デカい
速度に関しては、両者の体感差はデカいです。
複数のレビュー記事を読むと、こういう傾向があります。
Claude Code
· 初動が遅い（最初のトークンまで5〜15秒）
· でも、いったん動き出すと文脈に沿った提案が早い
· 1Mコンテキストを使うとさらに重くなる
Codex（GPT-5.5）
· 初動が速い
· トークン効率が良くて、同じタスクでもトークン消費が少ない
· 「GPT-5.4 Highで5〜6分→GPT-5.5 Mediumで2分半」という体感報告
具体的な比較として、AQUA テックブログの「実際にチャットボットを作らせてみた」検証では、Claude Codeが約25分でプロジェクト完了、Codexが約40分。逆にCodexが速かった例もあって、Qiitaの検証では「Codex CLIは2倍速」っていうケースも報告されてる。
要するに、速度は「タスクの種類」で勝ち負けが入れ替わる。
· 小さい修正、対話的なやりとり：Claude Codeが速い
· 大きいタスク、まとめて実装：Codexが速い（特にGPT-5.5以降）
· コンテキスト読み込みが必要なタスク：Claude Codeのほうが速い場合がある（1Mコンテキストで一気に読める）
· ゼロからの実装：Codexが速いことが多い
副業勢の運用としては、「対話して進めるならClaude Code、投げて待つならCodex」って覚えとけばOK。
UI/UXとエコシステム比較
UI/UXとエコシステムも大事な比較ポイント。
Claude Code側
· ターミナルベース。最近デスクトップアプリも刷新（2026年4月14日）
· VS Code拡張あり
· Skills、hooks、MCP、Subagentで超カスタマイズ可能
· Claude Coworkとの連携が強力（SNS投稿同時化など）
· GitHubの`awesome-claude-code`に何百ものSkillsが公開
· Obsidian連携が強い（個人発信者・ライターに刺さる）
Codex側
· ChatGPT、CLI、VS Code、macOSアプリ、Web、複数の入り口
· GitHub PRレビューが`@codex`タグで起動
· ChatGPT内で完結できるので、非エンジニアでも使いやすい
· カスタマイズはカスタムコマンド程度
· Computer use機能（macOSアプリ操作）
· Amazon Bedrock対応で、エンタープライズ環境にも対応
エコシステムの観点では、Claude Codeが圧倒的に成熟してる。Skills、Subagent、Plugins、MCPの組み合わせで、自分専用の作業環境を構築できる。これはX上のIndie Hackersコミュニティで「Claude Code is the most enjoyable to work with. UI and interaction flow feels like a damn video game」って評されてる通り。
一方、Codexは「使い始める敷居の低さ」と「ChatGPT統合」が強み。非エンジニアでChatGPTに慣れてる人には、Codexのほうが入りやすい。
副業勢への翻訳：
· 既にClaudeに課金してて、本気でカスタマイズしたい → Claude Code
· ChatGPTに慣れてて、まずは試したい → Codex
· ライター・発信者で、Obsidian使ってる → Claude Code
· GitHubで案件管理してる → 両方（CodexのPRレビュー機能が便利）
「rate limit arbitrage」って知ってますか？
最後に、海外勢が編み出した裏技を紹介します。
Rate Limit Arbitrage（レート制限裁定）——これは、Claude CodeとCodexを並列で動かして、片方がレート制限に達したらもう片方に切り替える、っていう運用。
X上のAlphaSignal AIが投稿した「smux」っていうツールがあって、これはtmuxセットアップでClaude CodeとCodexを同じワークスペースで連携させる仕組み。両方が同じプロジェクトを見て、メッセージを行き来できる。
Indie Hackersコミュニティでは、Dennis Lysenkoが「Why I Run Claude Code and Codex Side By Side」っていうブログ記事を書いてて、「2〜4個のエージェントを並列で動かして、Claude Codeがレート制限に達したらCodexに移して作業を継続する」っていう運用を公開してます。
これ、副業勢にとってどう意味があるかと言うと、「月120ドルで、ほぼ無制限の作業時間を確保できる」ってこと。Claude Code Max 5xで100ドル、ChatGPT Plusで20ドル、合計120ドル。これで、レート制限に振り回されずに副業作業を回せる。
逆に、「片方だけ」だと、絶対どこかでレート制限に当たって作業が止まる。これが副業の生産性を下げる最大の要因。だから、本気で稼ぐなら両方契約が、海外Indie Hackersでは標準になりつつある。
次の第5章では、この料金の話をもっと詳しく、コスパ観点で深掘りします。
第5章：料金とコスパのリアル—月いくら、何ができるか
Claude Codeの料金プラン早見表
Claude Codeの料金プランを、2026年4月時点で整理します。
ここで注意点。2026年4月21日に「Pro 20ドルプランからClaude Codeを削除する」って一旦発表されて、X上で大炎上→撤回された経緯があります。Maximiliano Firtmanっていう海外開発者が「¿CHAU CLAUDE CODE?（さよならClaude Code？）Pro 20ドルプランからClaude Codeが削除された」ってスペイン語で投稿して、世界中で混乱が広がった。
Simon Willisonっていう著名な開発者も「Is Claude Code going to cost 100ドル/month? Probably not—it's all very confusing」（Claude Codeは100ドル/月になるのか？たぶんならない、でもマジで混乱してる）ってブログに書いてます。
結論：2026年4月末時点では、Pro 20ドルでClaude Code利用可。ただし、レート制限が厳しいので、本格利用にはMax 5x（100ドル）以上が事実上必須。これは今後も変わる可能性あるので、契約前に最新情報を確認する必要があります。
Codexの料金プラン早見表
2026年4月2日にOpenAIが料金体系を改定して、Plus、Pro、Business、Enterpriseがトークンベースのクレジット制になりました。4月9日には新しいPro 100ドルプランが追加。Pro 100ドルは「Codexのレート制限10倍プロモ期間（5月31日まで）」を含んでて、その後5倍に戻る予定。
ここで重要なのが、ChatGPT Plus 20ドルでCodexが普通に使えるってこと。海外Reddit/Hacker Newsの一致した評価が「Codex 20ドルは一日中コーディングできる、Claude Code 20ドルは複雑プロンプト数回で枠が尽きる」。
これがCodexの強烈なコスパ優位性。月20ドルで本気で使えるのはCodexだけ。
用途別最適プラン早見表
副業・SNSマネタイズ用途で、月の予算別に最適プランを整理します。
ここで一番おすすめなのが「予算 月120ドルの両刀型」。海外Indie HackersのDennis Lysenkoも、複数の検証記事も、X上の発信者も、ほぼ全員がこの組み合わせを推してます。理由は、コスパと機能のバランスが最高だから。
「月120ドル」の現実的な投資対効果
「月120ドルって、副業初心者には高くない？」って思う方もいるかも。ここでガチで現実的な投資対効果を計算します。
副業の作業内容と、AI併用前後の所要時間を比較してみます。
LP制作1本
· AI併用前（外注前提）：20〜30万円、納期2週間
· 自力（AIなし）：60〜80時間
· Claude Code＋Codex：3〜5時間
note有料記事1本（5,000字）
· AI併用前：8〜15時間
· Claude Code＋Codex：1〜2時間
Threads投稿30本（1ヶ月分）
· AI併用前：15〜20時間
· Claude Code＋Codex：1〜2時間
講座スライド15枚
· AI併用前（デザイナー外注）：10万円、納期1週間
· 自力：20〜30時間
· Claude Code＋Codex：3〜5時間
会員サイト構築
· AI併用前（外注）：50〜100万円
· 自力（エンジニア前提）：80〜120時間
· Claude Code＋Codex：1〜3日
これ、月120ドル（約18,000円）で、外注換算すると数十万〜数百万円分の作業が回せるってこと。ROIで言うと、最低でも10倍、案件によっては100倍以上。
しかも、副業で重要なのは「時間」。本業がある人は、副業に使える時間が週10〜20時間しかない。その時間で月10〜30万稼げるかどうかは、生産性で決まる。月120ドルの投資で生産性が3倍になるなら、それは絶対ペイする。
「月20ドルで始める」の現実
「いや、それでも月120ドルは厳しい」って人へ。月20ドルで始める現実を見ます。
月20ドルコース：ChatGPT Plus のみ（Codex使用）
メリット：
· Codexが一日中使える
· 初期設定が軽くて、即戦力
· 副業始めたばかりの人には十分
できること：
· LP制作（基本レベル）
· note記事執筆
· SNS投稿生成
· 簡単なWebアプリ
· PRレビュー（GitHub連携）
· 画像生成（DALL-E）
制限：
· Claude CodeのSkills、Obsidian連携、長文耐性は使えない
· カスタマイズ性が低い
· 複雑なプロジェクトでは厳しい
これでも、副業始めたばかりで「まず月5万円稼ぎたい」レベルなら、十分戦える。実際、X上で「ChatGPT Plus 20ドルで副業100万円達成」っていう発信もある（信ぴょう性は要確認だが、可能性としてはあり得る）。
つまり、最低ラインは月20ドル。本気でやるなら月120ドル。プロ型なら月300ドル。これがコスパの3段階。
予算別の判断ロジックは：
· 副業始めたばかりで売上ゼロ → 月20ドル（Codexのみ）でスタート
· 月5〜10万売上が出始めた → 月100〜120ドルにアップグレード
· 月30万以上、または本業並み → 月200〜300ドルのプロ型
次の第6章では、もっと具体的に「副業・SNSマネタイズで本当に使えるのはどっち」を、用途別にガチで比較します。
https://note.com/hataraku_writer/n/n25386bdad859?app_launch=false
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 13. @L_go_mrk（2026-05-05 09:05:25）

**URL:** https://x.com/L_go_mrk/status/2051589071307497678

「Anthropic社員のClaudeCodeの使い方」という記事を書きました！！！

まっっっっっっじで有用なものばかりなので是非！！

--- 引用ツイート (https://x.com/L_go_mrk/status/2051588898900586831) ---
【コードの70〜90%がAI生成】Anthropicの社員が実践するClaude Code活用法
20
127
5.6万
こんにちは、AI駆動塾です。
ネットを見ていると、日々さまざまな発信者が「Claude Codeのベストプラクティス」を発信しています。ただ、それらの多くは発信者個人の使い方にカスタマイズされた内容で、必ずしも汎用的とは言いきれません。
そんな中、汎用的に通用する「Claude Codeのベストプラクティス」を見つけました。Anthropic公式が出している内容です。
今回はAnthropicが公開している2つのドキュメント — 「How Anthropic teams use Claude Code」と「Best practices for Claude Code」 — を中心に、Anthropicのエンジニアが社内でClaude Codeをどう使っているのかをまとめました。
===
＜PR＞engram - 超精密エンジニア診断
「資質」「特性」「経験」の3軸 × 各10次元で、エンジニアとしての全体像を可視化する診断サービスです。100問の設問に答えるだけで、自分の個性が立体的に見えるようになります。
診断後は、自分のプロファイルにマッチする案件オファーが匿名で届く機能も使えます。今の会社や経歴を晒さずに、市場が自分にいくらの値段をつけるかを観測できる設計です。
👉 https://engram-axg.pages.dev/?utm_source=x&utm_medium=social&utm_campaign=engram_article&utm_content=article-03
===
まず、AnthropicがどれだけClaude Codeを使い倒しているのか、まずいくつか数字を見ておきます。
Anthropicの広報が2026年1月、Fortuneの取材に対してこう発言しています。
「社内全体で、コードの70〜90%がClaude Codeで書かれている」
（出典: https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/ ）
Claude Codeの開発責任者であるBoris Cherny本人は、もう一段先を行っています。2025年11月以降、自分のコードを1行も手で書いていない。毎日10〜30件のPull Requestを出し、その全てがClaude Codeによる生成だと公にしています（出典: https://www.developing.dev/p/boris-cherny-creator-of-claude-code ）。
会社の規模感も異常です。Anthropicは2025年初頭から従業員数が3倍に増えていますが、1人あたりのエンジニア生産性は同時期に約70%上昇しています。組織が3倍に拡張されたとき、普通は1人あたりの生産性が下がります。Anthropicの場合は逆に上がっている。差分の正体がClaude Codeの社内活用です（出典: https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens ）。
外側の数字も塗り替わっています。SemiAnalysisが2026年2月に出した分析によると、GitHubの公開コミットの4%が既にClaude Code製。同社は「2026年末には20%を超える」と予測しています（出典: https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point ）。
これだけの数字を出しているAnthropicのエンジニアたちが、社内で何をやっているのか。どれも超有益な内容なので、興味があれば覗いていってみてください。
Anthropic社内のチーム別Claude Code活用 — 公式公開の事例集
Anthropicが2025年7月に公開した「How Anthropic teams use Claude Code」というブログ記事に、社内のチーム別の使い方が具体的に書かれています。
（出典: https://www.anthropic.com/news/how-anthropic-teams-use-claude-code ）
引用してみると、こんな顔ぶれです。
セキュリティエンジニアリングは、本番インシデントが発生したときにスタックトレースと社内ドキュメントを丸ごとClaudeに投げます。Claudeが制御フローを追いかけて、コードベースのどこに問題があるかを特定する。従来10〜15分かかっていた手動スキャンが、約3倍速で解決するようになった、と報告されています。
データインフラチームの事例は具体的です。Kubernetesクラスタが突然podをスケジュールしなくなった本番障害のとき、彼らはダッシュボードのスクリーンショットをそのままClaudeに渡しました。ClaudeがGoogle CloudのUIを画像から読んで操作手順を案内し、Pod IPアドレスの枯渇という原因にたどり着いた。さらに新しいIPプールを作成する正確なコマンドまでClaudeが提示した、という流れです。障害対応中に20分の節約と書かれています。
インファレンスチームは、既存のテストを未経験の言語（Rustなど）に翻訳する用途で使っています。「言語が読めないから手を出せない」だった移植作業が、Claudeのドライバ駆動で進められるようになった。
グロースマーケティングは数百件の広告データのCSVをClaudeに処理させ、低パフォーマンス広告を検出して新しいバリエーションを生成する自動ワークフローを構築しています。手作業で数時間かかっていた広告生成が分単位になった、と報告されています。
法務チームですら使っています。弁護士が「社内メンバーを正しい担当弁護士に振り分ける電話ツリーシステム」のプロトタイプを、自分でClaude Codeに作らせた、というエピソードが載っています。
プロダクトデザインは、TypeScriptが書けないデザイナーがClaudeを使ってReactで可視化アプリを構築する、という使い方をしています。
「Anthropicのエンジニアが」というより、「Anthropicの全職種が」Claude Codeを使い倒している、というのが社内の現実です。
Anthropic公式ベストプラクティスの第一原則 — 「Claudeに自分で検証させる仕組みを先に作る」
ここから先はAnthropic公式の「Best practices for Claude Code」ドキュメントの中身です。
（出典: https://code.claude.com/docs/en/best-practices ）
このドキュメントの一番最初に出てくる原則が、これです。
"Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do."
（テスト、スクリーンショット、期待される出力を渡して、Claudeが自己検証できるようにする。これがあなたができる、唯一最大のレバレッジを持つアクション）
なぜ第一原則として置かれているのか。理由はシンプルで、検証手段がないとClaudeは「それっぽく見えるが動かないコード」を生成してしまうからです。検証手段がないと、人間が唯一のフィードバックループになるしかなく、ミスのたびに人間の注意を消費することになる。検証手段を渡しておけば、Claudeは自分で何度もリトライして仕上げてくれる。
公式ドキュメントの比較表で印象的なのが、「メールバリデーション関数を書いて」というプロンプトと、「メールバリデーション関数を書いて、user@example.com=true、invalid=false、user@.com=falseのテストケースで検証してから完了して」というプロンプトの差です。同じ依頼でも、後者のほうが圧倒的に正確に仕上がる、と公式が明言しています。
UIの変更ならスクリーンショット、ロジックならテスト、ビルドならコマンド出力。「Claudeに自分で検証させる仕組み」は、何をするタスクでも先に用意する。これが社内で最も重要視されている習慣です。
Explore → Plan → Implement → Commit の4フェーズワークフロー
公式ドキュメントが推奨している標準ワークフローが、4フェーズ構成になっています。
Explore（探索）: プランモードに入り、Claudeにファイルを読ませて理解させるフェーズ。書き換えはしない
Plan（計画）: 詳細な実装計画をClaudeに作らせるフェーズ。Ctrl+Gで計画をエディタで直接編集できる
Implement（実装）: プランモードを抜け、計画に沿って実装、テスト
Commit: 記述的なコミットメッセージとPR作成
ここで興味深いのは、公式自身が「プランモードは万能ではない」と明言している点です。
"For tasks where the scope is clear and the fix is small (like fixing a typo, adding a log line, or renaming a variable) ask Claude to do it directly."
（スコープが明確で修正が小さいタスク — タイポ修正、ログ追加、変数リネーム — はClaudeに直接やらせろ）
プランニングが効くのは、複数ファイルを触る変更のとき、アプローチが不確かなとき、未経験のコードを触るときの3条件です。「とりあえずプランモードで」という思考停止の使い方を、公式自身が否定しているのが面白いところ。
CLAUDE.mdは「短く、容赦なく刈り込め」が公式の指針
公式が二番目に強調している領域がCLAUDE.mdの設計です。多くのユーザーが誤解している部分でもあります。
CLAUDE.mdは「Claudeが毎セッションの最初に必ず読むファイル」です。長く書けば書くほどClaudeに伝わる、と思いがちですが、公式の見解は真逆です。
"Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"
（膨らんだCLAUDE.mdは、本当に必要な指示をClaudeに無視させる）
公式が示している刈り込みのルールがあります。各行ごとに「これを消したらClaudeがミスをするか？」を自問する。しないなら消す。標準的な言語規約や、Claudeがコードを読んで分かることは入れない。
入れるべきもの: 自社固有のBashコマンド、デフォルトと違うコードスタイル、テスト実行の好み、リポジトリのお作法、独自のアーキテクチャ判断、開発環境の癖、よくある落とし穴。これだけ入れる。
入れないもの: 標準的な言語規約、詳細なAPIドキュメント（公式へのリンクを置けばよい）、頻繁に変わる情報、長い解説文、ファイル単位のコードベース説明、「コードをきれいに書け」のような自明なルール。
ドメイン知識や時々しか必要にならない情報は、CLAUDE.mdに常駐させずに Skills（.claude/skills/SKILL.md） に切り出します。Claudeが必要なときだけ自動的にロードしてくれるので、毎回コンテキストを汚さずに済む。
「Claudeが指示を無視し始めたら、CLAUDE.mdが長すぎるサインだ」と公式が明言している。日々の運用感としても、これが一番効くチェックです。
＜PR＞engram - 超精密エンジニア診断
「資質」「特性」「経験」の3軸 × 各10次元で、エンジニアとしての全体像を可視化する診断サービスです。100問の設問に答えるだけで、自分の個性が立体的に見えるようになります。
診断後は、自分のプロファイルにマッチする案件オファーが匿名で届く機能も使えます。今の会社や経歴を晒さずに、市場が自分にいくらの値段をつけるかを観測できる設計です。
無料、所要時間100問だけ。
👉 https://engram-axg.pages.dev/?utm_source=x&utm_medium=social&utm_campaign=engram_article&utm_content=article-03
Boris Cherny流のサブエージェント・コードレビュー（多重レビューパターン）
ここからもう一段ミクロな実践に降ります。Claude Code開発責任者のBoris Chernyが、Every podcastのインタビューで明かした、自分のコードレビューフローです。
（出典: https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it ）
パターンが2段構えになっています。
第一波: 複数のサブエージェントを並列起動する。1人がスタイルガイドラインをチェック、1人がプロジェクトの履歴をスキャンして既存実装パターンを把握、1人が明らかなバグをフラグ付けする。
第二波: さらに5つのサブエージェントを起動して、第一波の指摘に「穴を空けに行く」専門タスクを与える。誤検知を削るためです。
なぜこのパターンが効くのか。単一エージェントの単発レビューは false alarm（誤検知）が多すぎる、というのがBorisの観察です。AIにお互いを攻撃させることで、本物の問題だけが残る。サブエージェントは独立したコンテキストウィンドウで動くので、メインのコンテキストを汚さない。
これが「Claude Codeの開発責任者本人が、自分のコードのレビューに使っているフロー」のレベル感です。
Hooks／Skills／Subagents — 3つの拡張機構の使い分け
Claude Codeには拡張のレイヤーが3つあります。多くのユーザーが「全部MCPだろ」のように混同しがちな箇所を、公式の整理で見ていきます。
Hooksは「例外なく毎回必ず実行されるべき動作」のためのものです。CLAUDE.mdの指示はあくまで助言ですが、hooksは決定論的に発火します。「ファイル編集後にeslintを必ず走らせる」「migrationsフォルダへの書き込みは必ずブロックする」のような、確実性が必要な場面で使う。
Skillsは、ドメイン知識や繰り返しワークフローを .claude/skills/SKILL.md ファイルとして置いておく仕組みです。CLAUDE.mdと違って常駐しないので、コンテキストを汚さない。Claudeが必要だと判断したときだけ自動でロードします。.claude/skills/fix-issue/SKILL.md のような形でGitHubイシュー対応のテンプレートを置いておけば、/fix-issue 1234 で呼び出せる、といった使い方。
Subagentsは、独立したコンテキストで動く専門アシスタントです。読み込みが多いタスク、専門的なフォーカスが必要なタスクを、メインの会話を汚さずに委譲できる。.claude/agents/security-reviewer.md のような形でセキュリティレビュー専門のエージェントを定義しておく、といった使い方が公式ドキュメントに例示されています。
役割が明確に違います。Hooksは確実性、Skillsは知識の遅延ロード、Subagentsはコンテキスト分離。「全部入れる」のではなく、目的で使い分けるのがAnthropic社内の運用です。
コーディング作業の並列化 — Anthropic公式が示す自動化パターン
Claude Codeを「対話的に1人で使う」だけでは、Anthropicの社内活用には届きません。公式ドキュメントが「Automate and scale」セクションで具体的に示している並列化パターンがあります。
非対話モード（claude -p）。CIパイプライン、pre-commitフック、自動化スクリプトに組み込んで、Claudeを裏側で呼び出します。--output-format jsonを付けるとプログラム的に結果をパースできるので、既存のデータパイプラインに組み込みやすい。
Writer/Reviewerパターン。セッションAで実装し、別セッションBで独立コンテキストでレビューする。レビュー側は実装の経緯を知らないので、コードに対して公平な判定ができる、という設計です。同じ理屈で「テスト先書き／実装後書き」の分担も可能。
Fan-outパターン。「Reactで書かれた2,000ファイルをVueに移行する」のような大量作業を、ループでclaude -pを回して並列処理する。公式ドキュメントの実例コードがそのまま掲載されています:
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
最初の2〜3ファイルでプロンプトを調整し、結果を見てからフルセットを流す、というのが公式の推奨手順です。
「対話で使う」フェーズを超えて、Claude Codeをパイプラインの構成要素として扱う。Boris Chernyが毎日10〜30 PRsを出せるのは、この並列化が手元に組み立てられているからです。
公式が名指しで警告する5つの失敗パターン
最後に、公式ドキュメントが「Avoid common failure patterns」として明記している5つの失敗パターンを並べます。読者が自分の使い方と照らし合わせるチェックリストとして使えます。
The kitchen sink session — タスクA→無関係なB→Aに戻る、を繰り返してコンテキストがゴミだらけになる。対処: /clear を挟む
Correcting over and over — 同じことを2回以上修正したら、コンテキストが失敗アプローチで汚れている。対処: /clear して、学んだことを反映した新プロンプトで再開
The over-specified CLAUDE.md — 長すぎて重要な指示が埋もれる。対処: 容赦なく刈り込む。Claudeが指示なしで正しく動いている項目は削除する
The trust-then-verify gap — 「もっともらしく見えるが端ケースを処理していない」コードをそのままshipしてしまう。対処: 検証手段（テスト、スクリプト、スクショ）を必ず先に用意する
The infinite exploration — スコープを切らずに「調査して」と頼むと、Claudeが何百ものファイルを読んでコンテキストを潰す。対処: スコープを絞る、またはサブエージェントに委譲する
公式が「これは間違いだ」と名指ししている、という点が読者にとって意外に効きます。多くのユーザーが「自分の使い方は最先端」と思っている領域に、Anthropic自身が「それは典型的な失敗パターン」と書いているからです。
===
＜PR＞engram - 超精密エンジニア診断
「資質」「特性」「経験」の3軸 × 各10次元で、エンジニアとしての全体像を可視化する診断サービスです。100問の設問に答えるだけで、自分の個性が立体的に見えるようになります。
診断後は、自分のプロファイルにマッチする案件オファーが匿名で届く機能も使えます。今の会社や経歴を晒さずに、市場が自分にいくらの値段をつけるかを観測できる設計です。
無料、所要時間100問だけ。
👉 https://engram-axg.pages.dev/?utm_source=x&utm_medium=social&utm_campaign=engram_article&utm_content=article-03
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 14. @MakeAI_CEO（2026-05-05 13:31:26）

**URL:** https://x.com/MakeAI_CEO/status/2051656014093750338

Codex、、、これはダメやろ！！！

既存サイトのURL渡して「完全再現して」って言ったら、画像生成フル活用しつつ、Codex自身がサイトをスクショ撮って、Higgsfieldを完コピしてきやがりました…

ただ、他社サイトをコピーして、、、ってよくないけど、参考にしたいUI/UXがあれば、Codexで一瞬で作れてしまいますわな！

※さすがにそのまま掲載するのはまずいので、名前とデザインを少しだけ変更して作成

--- 引用ツイート (https://x.com/MakeAI_CEO/status/2050133272022094057) ---
Claude Code vs Codex 徹底比較｜マネタイズで使うならどっちが正解か現在地を全部晒す
7
56
474
71万
ふざけんなって叫んでる暇はない。2026年4月、Claude CodeとCodeの現在地
「またCodex覚えるのか」って思いませんでした？
正直に聞きます。
このタイトルを見て、「いやマジでさ、Claude Code覚えたばっかなのに、なんで今度はCodexなんだよ」って思ったでしょう。わかります。めちゃくちゃわかります。
私も同じ気持ちでした。
ChatGPT触って、Cursor触って、Claude Code触って、ようやく「これで自分のワークフロー固まったわ」って思った矢先に、OpenAIが2026年3月にCodexを大型アップデートして、4月にはGPT-5.5を載せてきた。NVIDIAが社員1万人で使ってるとか、SWE-bench Verified 87.6%でClaude Opus 4.7に肉薄してるとか、もう情報量が多すぎる。
しかも厄介なのが、X開けば「Codex最強」「いやClaude Codeのほうが」って論争が毎日のように起きてて、よく見ると同じ人が両方絶賛してたりする。「結局どっちなんだよ」って。
ぶっちゃけ、AIツール出るたびにキャッチアップしてたら、本業も副業も回らないんですよね。気づいたら情報収集だけで一日が終わってる、みたいなことが起きる。これが俗に言う「AIツール疲れ」ってやつです。
でも、ここで一回立ち止まってほしいんです。
「ふざけんな」って叫んでる暇は、もうないんですよ。なぜなら、2026年4月時点で、すでにこの2つを使い分けて副業や個人開発で結果を出してる人たちが普通にいるから。あなたが「またかよ」ってぼやいてる間に、彼らは月5万、月30万、なんなら年商数百万の自動化システムを組んでる。これが現実です。
だからこの記事では、ぼやくのをやめて、いったん腹くくって両方の現在地を整理します。徹底比較して、「副業・SNSマネタイズ用途で結局どっち使えばいいの？」に明確な答えを出します。
ぼやいてる人と、動いてる人の決定的な差
ここで一つ、衝撃的な事実をお伝えします。
2026年初頭、Anthropic（Claudeの開発元）のCEOダリオ・アモデイが「最初の従業員1人で10億ドル企業が、2026年中に生まれる可能性がある」と発言しました。これ、最初聞いたとき正直「またビッグマウスかよ」って思ったんですよ。でも、よく考えてみてください。
実際、Claude Codeを使って4ヶ月で507万円のSNS自動化売上を作った人がいる。Web制作未経験の非エンジニアが180日で月5万円の副業収益に到達してる。X上では「副業ゼロからClaude Codeだけで月収100万を達成した3ステップ」を公開してる人もいる。これ、別に特別な才能持ってる人の話じゃないんです。
つまり、何が起きてるかと言うと——「AIツール出るたびに疲れてる人」と「AIツール出るたびに自分の武器に変えてる人」で、収入の桁が変わり始めてる。これが2026年の現実です。
しかも厄介なのが、この差は「最初の3ヶ月」で決まるってこと。Claude Codeが出た2024年〜2025年に飛びついて触り始めた人と、「もう少し様子見してから」って言ってた人で、2026年4月時点ではもう後戻りできないくらい差がついてます。
「いや、俺もうClaude Codeはやってるよ」っていう人。それは合格ライン。でも、Codexがここまで強くなった以上、Claude Codeだけで戦うのは正直キツくなってきてます。なぜなら、Claude CodeとCodexは競合じゃなくて補完関係——片方の弱点をもう片方で埋める使い方が業界標準になりつつあるから。
ここがめちゃくちゃ大事なポイントなので、もう一回言います。
Claude CodeとCodexは「どっちか選ぶ」ものじゃなくて、「どう使い分けるか」で差がつくフェーズに入ってます。
そして、その使い分けを知ってるか知らないかで、副業の生産性は2倍も3倍も変わる。これが今、Xで「両方使ってる」って人が爆増してる理由です。
この記事で約束すること
ここまで読んで「やっぱ両方使うんかよ、めんどくせー」って思った方、もう少し付き合ってください。
この記事では、以下のことを約束します。
第一に、「ふざけんな」って思ってる感情は最後まで否定しません。だって本当にツールが多すぎるんだもん。でも、感情を整理しつつ、「で、結局どうすればいいのか」を必ず提示します。逃げません。
第二に、技術的な数字（ベンチマークとか）も出しますが、「副業・SNSマネタイズで使うならどっち」っていう実用観点で全部翻訳します。SWE-bench Verified 87.6%って言われても、副業勢には何のことかわからないですよね。それを「あなたのnote記事LP制作で何が変わるか」レベルまで落として書きます。
第三に、両方使ってる人のリアルな声を載せます。X上で実際に発信されてる本音、ブログ記事の体験談、副業勢の月収実績、海外Hacker NewsやRedditでの議論——リサーチで集めた一次情報をそのままお見せします。「両方いいと思います！」みたいな腰の引けたまとめは絶対にしません。
第四に、最後には「あなたはこっち使え」って明確に結論を出します。属性別、用途別、予算別で分岐して、迷わなくて済むようにします。読み終わったその日から、行動できる状態にします。
正直、この記事は5万文字あります。長いです。途中で疲れるかもしれません。でも、これを読み切った3時間後のあなたは、もう「ふざけんな」って言わなくていい状態になってます。なぜなら、AIツールに振り回される側じゃなくて、選ぶ側に立ててるから。
そろそろ本題に入りましょう。次の章では、なぜ「AIツール疲れ」を放置すると副業勢から脱落するのか、その構造を解説します。ここを理解しないまま個別ツールの話に入っても、また次のツールが出たときに同じ「ふざけんな」を繰り返すことになるので、絶対飛ばさず読んでください。
第1章：「AIツール疲れ」を放置すると、副業勢から脱落する
ツール疲れは「実は努力不足」じゃない
最初に断っておきます。AIツール疲れは、あなたの努力不足じゃないです。
これ、本当に大事な前提なので、最初にハッキリ言わせてください。「ついていけてない自分が悪い」って思い込んでる人、めちゃくちゃ多いんですけど、違います。本当に情報量が異常なんです。
具体的に2026年に入ってから何が起きたか、数えてみますね。
1月：Claude Sonnet 4.5登場、Claude Code Skillsの拡充
2月：Cursor、Windsurf、Devin、Cline……エージェント型ツールが乱立
3月：OpenAIがCodexを大型アップデート、CLIに本格参入
4月：Claude Opus 4.7リリース、GPT-5.5登場、Codex CLIにcomputer use機能、Claude Codeデスクトップアプリ刷新
これ、たった4ヶ月の出来事です。これで疲れない人がいるなら、その人はAI業界で生計立ててる人か、人間じゃないかのどちらかです。
実際、Zennに上がってる記事で「AIツール疲れしてない？2026年サバイバルのための『選ばない』技術」っていうのがあって、これがめちゃくちゃバズってるんですよ。何で読まれてるかって、みんな同じこと感じてるからです。「もう全部追えない」「でも遅れたくない」「結局どれ使えばいいの」って。
しかも、ここに追い打ちをかけるのが、Qiitaに投稿された「約9割の開発者がAIツールで遅くなっている」っていう記事。読むと、AIツール導入で生産性が下がってる人が、実は多数派だってデータが出てます。理由は単純で、ツールに振り回されて、本来の作業に集中できてないから。
つまり、AIツール疲れは構造的な問題なんですね。あなたが弱いんじゃない。ツールが多すぎて、しかも進化が速すぎて、人間の認知リソースの限界を超えてる。これが本質。
だから、まずやるべきは「全部追うのをやめる」って決断です。これができないと、Claude CodeとCodexの話を始めても、半年後にまた新しいツールが出てきて「ふざけんな」って繰り返すだけ。
2026年、AI開発ツールはとっくに「インフラ」になった
ここでもう一つ、視点を変える話をします。
2026年4月時点で、AI開発ツールはもう「便利なツール」じゃないんです。「インフラ」になってます。これがどういうことか、具体例で説明しますね。
電気とかインターネットって、別に使うのが偉いとか進んでるとかじゃないですよね。使えて当たり前。使わないと仕事にならない。AI開発ツールも、もうそのレベルに入ってます。
例えばUberみたいな大企業でも、社内ではClaude CodeとCodexを両方使い分けてるって報告が出てます。NVIDIAは社員1万人がGPT-5.5搭載のCodexを日常的に使ってる。Anthropic社内では、エンジニアがClaude Codeで自社のClaude Codeを開発してる。これが2026年の業界標準。
副業や個人開発の世界でも、状況は同じです。ココナラでWeb制作の案件取ってる人は、ほぼ全員Claude CodeかCursor使ってる。note書いて販売してる人は、ChatGPTかClaudeで構成練ってる。X運用してる人は、Threadsの自動投稿システムをClaude Codeで組んでる。
ここで質問です。あなたが今から「AIツールなしで副業始めます」って言ったら、どうなると思います？
答え：勝てません。マジで。
時給換算したら、ライバルが時給1万円相当の生産性で動いてる中、あなたは時給1,000円で戦うことになる。これは精神論じゃなくて、純粋に作業量の話です。Claude Codeで30分でできるLP制作を、AIなしで6時間かけてやってたら、永遠に追いつけない。
だから、「AIツール疲れ」を放置するのは、副業の世界では「インフラを使わない選択」と同じ意味になります。電気使わずに事業やるくらい、無理ゲーなんですよ。これが2026年の現実です。
じゃあどうすればいいか。答えは「インフラとしての必須2つだけ押さえる」です。それが、この記事のテーマであるClaude CodeとCodex。次の節で、なぜこの2つに絞るのか、根拠を説明します。
「全部追う」をやめると、選択肢が見えてくる
ここで思い切った提案をします。
Cursor、Windsurf、Devin、Cline、Aider、GitHub Copilot Workspace……これら全部、いったん忘れていいです。
え、って思いますよね。「いやでもCursor人気じゃん」「Windsurfも気になってた」って。気持ちはわかります。でも、副業・SNSマネタイズという観点で見たとき、2026年4月時点での最適解は明確にClaude CodeとCodexの2つに絞られます。理由を3つ挙げます。
理由1：Claude Code（Opus 4.7）とCodex（GPT-5.5）が、コーディング性能ベンチマークで他を引き離してます。Claude Opus 4.7はSWE-bench Verifiedで87.6%、SWE-bench Proで64.3%。Codex CLIはTerminal-Bench 2.0で77.3%。GPT-5.4比較で14%の性能向上、ツールエラーは3分の1。これらの数字を超えるツールは、4月時点では存在しません。
理由2：エコシステムが成熟してます。Claude CodeにはSkills機能、Subagent、MCP、Plugins、Git worktree対応、デスクトップアプリ……「インフラ」と呼べる土台が揃ってます。CodexはChatGPT、CLI、VS Code、macOSアプリ、Webと、あらゆる入り口から使える。他のツールはまだここまで完成してない。
理由3：副業勢のコミュニティが既に2つに収束してきてる。X見てもブログ見ても、結局Claude CodeとCodexの話ばかり。「Cursorからの乗り換え」「Windsurf試したけど結局Claude Code」みたいな投稿が、2026年に入ってから加速度的に増えてます。
これ、どういうことかと言うと、選択肢が絞られたほうが、結果的にラクなんですよ。「全部試して比較する」って、一見効率的に見えるけど、実は時間の無駄。なぜなら、業界が収束してきてる方向に乗ったほうが、情報も人脈も案件も集まるから。
例えば、2025年にCursorで頑張ってた人は、2026年に入ってClaude CodeとCodexにシフトしてる人が大半です。なぜなら、Skillsとか、Subagentとか、computer useとか、後発の機能が一気に来たから。Cursorも進化してるけど、Claude Code＋Codexの組み合わせには現時点で勝てない。
だからここで一回、決め打ちしましょう。「副業・SNSマネタイズで結果出すなら、Claude CodeとCodexの2つだけ押さえる」——これが2026年4月の最適解です。他のツールが気になったら、それは半年後に検討すればいい。
Claude CodeとCodex、この2つだけ押さえれば現状OK
じゃあ、Claude CodeとCodexを押さえることで、具体的に何ができるようになるのか。ここを明確にしておきます。
副業・SNSマネタイズで必要な作業を、ざっと並べてみます。
· LP制作（note販売LP、講座LP、商品LP）
· ブログ記事執筆（noteの有料記事、Substack、自社メディア）
· SNS投稿作成（X、Threads、Instagramキャプション）
· 動画台本作成（YouTube Shorts、TikTok、Reels）
· スライド資料作成（講座スライド、ウェビナー資料）
· 顧客管理・売上分析（Excel、CSV、Notion）
· 自動化スクリプト（投稿自動化、メール返信自動化）
· 会員サイト構築（決済込み、認証込み）
· 画像・動画生成（サムネ、商品画像、ショート動画）
· フォーム制作（リード獲得、アンケート、申込フォーム）
これ全部、Claude CodeとCodexの組み合わせで対応可能です。マジで全部。
具体例を1つ。「note記事を書いて、それを元にLPを作って、Threadsで告知投稿を10本作る」っていうワークフロー。これを従来の手作業でやると、たぶん1週間かかります。デザイナー外注したら数十万かかります。
これをClaude Code＋Codexでやると、半日で全部終わります。Claude Codeでnote記事を書いて、Skillsを使ってThreads投稿に展開して、CodexでLPのコードを書いて、ローカルで確認して、Vercelにデプロイ。「半日」って、誇張じゃなくて本当です。Xで実際にやってる人の投稿が山ほどあります。
しかも、この作業に必要な月額コストは、Claude Code Max 5xプラン（月100ドル）+ ChatGPT Plus（月20ドル）= 月約120ドル、日本円で18,000円くらい。デザイナー外注1案件分で、ほぼ無限に作業できる。これはコスパおかしいレベル。
ここで重要なのが、「Claude Codeだけ」とか「Codexだけ」じゃダメな理由。Claude Codeは長尺の文章作成、プロジェクト全体の文脈理解、Skillsによる自分専用ワークフロー化に強い。一方、Codexは速いコーディング、Plan→実装の精度、セカンドオピニオン的なレビューに強い。両方使うことで、お互いの弱点を消せるんですよ。
X上で「Claude Codeで作ったPlanをCodexでレビューするの良さそう！」っていう投稿がバズったんですが、まさにこの使い分けが副業勢にも効きます。Claude Codeで書いた記事をCodexにレビューさせる、Claude Codeで作ったLPをCodexで品質チェックさせる、みたいな使い方が、2026年の標準になりつつある。
まとめ：疲れる側でいるな、選ぶ側に立て
第1章の結論を一言でまとめます。
「ふざけんな」って叫んで疲れてる側にいるか、「2つだけ押さえる」って決めて選ぶ側にいるか。これがあなたの2026年を決めます。
もう一度整理しますね。
AIツール疲れは構造的な問題で、あなたの努力不足じゃない。でも、放置すると副業の世界では確実に脱落する。なぜなら、AI開発ツールはもう「便利なもの」じゃなくて「インフラ」になってるから。
そして、インフラとしての最適解は、2026年4月時点ではClaude CodeとCodexの2つだけ。CursorもWindsurfも、いったん忘れていい。なぜなら、業界が既にこの2つに収束してきてるから。
この2つを押さえることで、副業・SNSマネタイズで必要な作業——LP制作、記事執筆、SNS投稿、自動化、会員サイト構築、画像生成まで——ほぼ全部対応できる。月18,000円くらいのコストで。
ここまで読んで、「いや、それでもふざけんなって気持ちは消えない」って思う方もいると思います。それも正直で良いです。でも、感情と行動は分けましょう。「ふざけんな」って思いながら、手は動かす。これが副業で結果出してる人たちの共通点です。
次の章からは、いよいよClaude CodeとCodexのそれぞれの正体を、ガチで詳しく解説していきます。第2章でClaude Code、第3章でCodex。両方の特徴、強み、弱み、料金、最新機能を、副業勢の観点で全部晒します。ここから先が本番です。
第2章：Claude Codeの正体—2026年4月時点のガチ情報
Claude Codeって、結局なんなの？
まずシンプルに、Claude Codeが何者なのかをハッキリさせます。
Claude Codeは、Anthropic（Claudeを作ってる会社）が出してる「ターミナルで動くAIエージェント」です。「エージェント」って言葉、ちょっと曖昧なので具体的に言うと、あなたのPCの作業フォルダに入って、ファイルを読んだり書いたり、コマンド実行したり、ブラウザでサイトを確認したりまで、自律的にやってくれるAI。
「いや、ChatGPTやClaude.aiでもできるじゃん」って思うかもしれない。でも違うんです。決定的な違いは「あなたのファイルを直接触れる」かどうか。
例えば、ChatGPTで「LPを作って」って頼んだら、HTMLとCSSのコードが返ってきます。でも、それをコピーして自分のフォルダに保存して、ファイル名つけて、ブラウザで開いて確認して、修正があったらまた質問して……この往復が必要。
Claude Codeなら、「このフォルダにLP作って、ブラウザで確認して、スマホ崩れてたら直して」って一言で全部終わります。実際に`index.html`、`styles.css`、`script.js`を作って、ローカルサーバー立てて、ブラウザで開いて、見た目崩れてたら直すところまで自分でやる。
これが「エージェント型AI」の本質です。チャットで答えるだけじゃなくて、作業を完遂する。
2026年4月16日にClaude Opus 4.7がリリースされて、Claude Codeの中身もこれに更新されました。SWE-bench Verifiedで87.6%、SWE-bench Proで64.3%。これは2026年4月時点で世界最高クラスのコーディング性能です。GPT-5.4を超えて、Gemini 3.1 Proも超えてる。
しかも、Anthropicの内部テストで「Rakuten-SWE-Bench」っていうのをやったら、Opus 4.7がOpus 4.6の3倍の本番タスクを解決したらしい。3倍ですよ、3倍。これがどれだけヤバい数字かと言うと、ベンチマーク上の伸びだけじゃなくて、実務で本当に使い物になるレベルが一気に上がったってこと。
2026年4月時点で押さえるべき新機能
Claude Codeの進化スピードがエグいので、2026年4月時点で押さえるべき新機能を整理します。
まず、1Mトークンのコンテキストウィンドウ。これがGA（一般提供）になりました。1Mトークンって、日本語で言うと約75万字。これ、何ができるかと言うと、「数百ページの仕様書を丸ごと読み込んでコードを書く」「プロジェクト全体のファイル構造を一度に理解する」レベルの処理が現実的になりました。副業文脈で言うと、過去の自分のnote記事30本全部読み込ませて、それを元に新しい記事を書かせるみたいなことができる。
次に、Subagent @mention機能（2026年4月追加）。Claude Codeのセッションの中から、特定の専門エージェント（Subagent）を呼び出せます。例えば、「@design-reviewer このLPのデザインレビューして」「@security-auditor この決済ページのセキュリティチェックして」みたいに、用途特化のエージェントを使い分けられる。これは複雑なプロジェクトの並列処理にめちゃくちゃ効きます。
Git worktree対応（–worktreeフラグ）も大きい。これは、同じプロジェクトの違うブランチを並列で作業できる機能。例えば、「ブランチAでLP作りながら、ブランチBで記事執筆」みたいな並列開発がリスクなくできる。副業で複数案件を回してる人には地味に効く。
デスクトップアプリ刷新（2026年4月14日）も話題でした。複数のClaude Codeセッションを並列で扱いやすくなって、「並列エージェント時代」に合わせて再設計されました。実質、ChatGPTのデスクトップアプリよりUXが洗練されてる、っていう声がXで多数。
ネイティブ音声モード（/voiceコマンド）も入りました。スペースキー長押しのPush-to-Talk方式で、日本語含む20言語に対応。追加コストなし。これ、運転中とか散歩中にClaude Codeに指示出せるってこと。マジで未来感ある。
そして、副業勢に一番効くのがSkills機能の拡充。Skillsっていうのは、特定の作業に特化した「手順書つき能力」のことで、例えば「Threads投稿用Skill」「LP制作Skill」「医者権威投稿Skill」みたいに、自分の仕事の型をAIに渡せる。GitHubの`awesome-claude-code`リポジトリには、すでに何百ものSkillsが公開されてて、これがエコシステムとしての強さになってます。
Claude Codeが副業勢に強い理由
ここから、副業勢の観点で「なぜClaude Codeが強いのか」を整理します。
理由1：コンテキスト把握力が圧倒的。Claude Codeは「対話型のシニアエンジニア」として設計されてます。プロジェクトのファイル構造、既存のコード、過去の会話、ユーザーの好みを覚えていて、それに合わせた提案をしてくれる。副業で「過去の自分のnote記事のトーンに合わせて新記事を書いて」みたいな依頼が、めちゃくちゃ精度高くできる。
理由2：Skills機能で自分の型を持たせられる。例えば、「自分のLPの基本構成」「自分のThreads投稿の型」「自分の講座スライドの章立て」をSkill化しておけば、毎回ゼロから指示しなくていい。リピート作業の時間が劇的に減ります。Yomo WebbっていうWebマーケメディアのブログには、Skills機能で実際に作業を自動化したコードが全公開されてます。
理由3：Claude Coworkとの連携。CoworkはAnthropicが出してる別ツールで、Claude Codeと連携することで、SNS同時投稿、Canva連携、ブログ記事からInstagram投稿への変換とかができる。実際、しのジャッキーさんっていう発信者がCoworkでX・LinkedIn・Facebookに同時投稿するスキルを作って公開してます。
理由4：長文コンテンツに強い。1Mトークンのコンテキストウィンドウのおかげで、有料note（1万字〜5万字）の執筆、講座スライド15枚分のテキスト、商品LPの全コピーを、一回の文脈で扱える。これは記事販売や講座販売をやってる副業勢には決定的な強み。
理由5：MCPでObsidianと連携できる。Obsidianっていうメモアプリと連携できて、自分の過去メモから素材を拾って、それを元に投稿や記事を作れる。「ネタ帳から発信を量産する」って副業の王道パターンが、Claude CodeとObsidianの組み合わせで成立する。
Claude Codeの弱点—正直に晒す
ここまで褒めまくったので、次は弱点を正直に晒します。記事の信頼性のためにも、ここは絶対飛ばさない。
弱点1：料金プランが混乱してる。2026年4月21日に、Anthropicが「Pro 20ドルプランからClaude Codeを削除する」って発表して、X上で大炎上しました。その後撤回されたんですが、「結局20ドルで使えるのか？」が4月時点でまだ曖昧。海外のSimon Willisonさんもブログで「This is all very confusing（マジで混乱してる）」って書いてます。
弱点2：レート制限が厳しい。これは海外Reddit/Hacker Newsで一番不満が出てる点。Pro 20ドルプランだと「複雑なプロンプト1〜2回で5時間制限の50〜70%消費する」っていう報告が多数。本気で使うならMax 5x（100ドル）以上が事実上の必須。
弱点3：重い・遅い問題。2026年に入ってから、特にQiitaで「Claude Codeが急に遅くなる」「最初のトークンが返るまで15秒以上かかる」って報告が増えてます。原因は、1M context、subagents、MCPなど機能が増えすぎて、雑に使うと崩れやすくなってる。
弱点4：コンテキストが長くなると性能が落ちる。Anthropic公式のBest Practicesでも明記されてますが、長い会話だとClaude Codeは最初に設定した制約を忘れがちになる。「フォーマット指定したのに守られない」「設計方針を途中から無視する」みたいなことが起きる。対処法は`/clear`で適度にリセットすること。
弱点5：初学者には設定が複雑。CLAUDE.md、hooks、MCP、Skillsの組み合わせを使いこなすには、それなりの学習コストがいる。「とりあえず触る」レベルなら良いけど、本気で副業に使うなら最初の設定で1〜2週間溶けることを覚悟しといた方がいい。
これらの弱点、Codexと比較するとどう違うのか。それは次の第3章で詳しく見ていきます。
Claude Codeを副業で使うときの実践イメージ
最後に、Claude Codeを副業で使うときの具体的な動きを、実例ベースで描いておきます。
ケース1：有料note記事の執筆。過去の自分のnote記事をClaude Codeに読み込ませて、トーンを学ばせる。新記事のテーマを伝えて、章立て→見出し→本文ドラフト→推敲→最終稿まで、一気通貫で書かせる。Skills機能で「自分の文体テンプレ」を作っておけば、毎回0から指示しなくていい。所要時間：構成30分、本文1〜2時間、推敲1時間。合計3〜4時間で、従来1日かかってた記事が完成。
ケース2：販売LPの制作。記事を書き終わったら、その記事を元にClaude Codeに販売LPを作らせる。`vercel:nextjs`っていうSkillで、Next.jsベースのLPをShadcn/uiで実装。Stripeも組み込み。ローカルで確認して、Vercelにデプロイ。所要時間：3〜5時間。デザイナー外注なら20万コースの作業が、ほぼ無料で完成。
ケース3：SNS投稿の量産。Claude CodeのSkillsで「Threads投稿Skill」「3スライド投稿Skill」を仕込んでおいて、記事のテーマからSNS投稿を10本ずつ生成。Obsidian Vaultにある過去メモも参照させて、自分の言い回しを保つ。所要時間：1時間で30投稿。
ケース4：会員サイトの構築。Claude Codeに「note販売した有料記事のメンバー専用閲覧サイトを作って」と頼む。認証、決済、コンテンツ配信、管理画面まで実装。所要時間：1日。これも従来なら数十万円の外注案件。
ここまで読んでもらえれば、Claude Codeが副業勢にとってどれだけ強力なインフラかわかると思います。次の章では、もう片方の刺客、Codexの正体を見ていきます。
第3章：Codexの正体—GPT-5.5を背負った刺客
Codexって、結局なんなの？
次はCodexの番です。
Codexは、OpenAI（ChatGPTの会社）が出してるAIコーディングエージェント。Claude Codeと同じく、ターミナルで動くCLIツール、VS Code拡張、ChatGPT Webアプリ、macOSデスクトップアプリ、複数の入り口があります。
「あれ、Codexって昔からなかったっけ？」って思う方、鋭いです。実は2021年頃にもCodexっていうのがあって、GitHub Copilotの基盤になってたんですけど、いったん消えました。それが2025年に「新しいCodex」として復活して、2026年3月の大型アップデートと4月のGPT-5.5搭載で、一気に化けました。
Claude Codeとの最大の違いは、「クラウドで動く」って点。Claude Codeはあなたのローカルマシンで動いて、ファイルもローカルに保存されます。Codexはクラウドのサンドボックス環境でタスクを実行できる（もちろんローカルCLIでも使える）。これが何を意味するかと言うと、「重い作業を投げて放置できる」ってこと。例えば、「このリポジトリの全ファイルにテストを追加して」みたいな数時間かかる作業を、ChatGPT上から指示して放置できる。
そして、2026年3月15日にOpenAIが正式にCodexのGPT-5.5搭載を発表しました。GPT-5.5は、OpenAIの最新フラッグシップモデルで、複雑なコーディング、コンピュータ利用、ナレッジワーク、リサーチ用途に特化してます。
Codexの強みを一言でまとめると、「タスクを任せられるクラウドワーカー」です。Claude Codeが「対話型のシニアエンジニア」だとすると、Codexは「依頼を投げたら勝手に進めて、終わったら報告してくれる外注ワーカー」のイメージ。
2026年4月時点のCodex最新機能
Codexの最新機能を、2026年4月時点で押さえるべきものに絞って解説します。
まず、GPT-5.5搭載。これが最大のアップデート。GPT-5.5の特徴は3つあります。1つ目、トークン効率がエグい。同じタスクに必要なトークン数がGPT-5.4比で大幅減。2つ目、速度が速い。GPT-5.4のHighモードで5〜6分かかってた処理が、5.5のMediumモードで2分半で終わる、という体感報告がある。3つ目、複雑なIssue対応で「指示通り完了させる力」が一段上がった。Plan→ツール使用→自己検証のループが内部で回せるようになって、人間の介入なしで最後まで仕上げる。
次に、computer use機能。CodexがあなたのmacOSアプリを「見て、クリックして、入力する」ことができるようになりました。これ、副業勢にとって結構ヤバい機能です。ネイティブアプリのテスト、シミュレーターでの操作、GUI専用のバグ調査ができる。例えば「KeynoteでこのテンプレートからスライドAB作って、PDF書き出しまでやって」みたいな依頼が成立する。
Amazon Bedrock対応も入りました。AWS SigV4署名やAWS資格情報認証に対応して、エンタープライズ環境でもCodexが使いやすくなった。これは個人副業には直接関係ないですが、業界としての成熟度を示す指標。
TUIの改善も実用的。Alt+, でreasoningレベルを下げる、Alt+. で上げる。モデル切り替え時にreasoning設定が新モデルのデフォルトにリセットされる。地味だけど、CLIで一日中使う人には効く改善。
App-server sessions機能で、複数の環境を管理できるようになった。プロジェクトごとに違う作業ディレクトリ、違う設定で動かせる。マルチワークスペース運用がしやすくなった。
そして、副業勢に一番効くのはChatGPT統合。Codexは独立ツールではなくて、ChatGPTの一部として使える。ChatGPTで「このPRレビューして」「このリポジトリのバグ直して」って指示すると、Codexがクラウドで実行して、結果をチャットに返してくれる。これは「コードを書く専門の手」がChatGPT内に内蔵されてる感覚。
Codexが副業勢に強い理由
Codexが副業勢にとってどう強いのか、整理します。
理由1：ChatGPT 20ドルプランで使える。これがマジで大きい。海外Redditの最大の不満が「Claude Code Pro 20ドルは複雑プロンプト1〜2回でレート制限に引っかかる」だったのに対し、Codexは20ドルで「コードを一日中書ける」って評価されてる。コスパで言うと圧倒的。
理由2：初期設定が軽い。Claude CodeはCLAUDE.mdとかhooksとか設定が多いけど、Codexはインストールしてログインすれば即使える。「初期設定なしで即戦力になる」っていう評価が、特に副業初心者から強い。
理由3：コード品質が安定してる。Qiitaの「同じアプリを作って比較した」検証では、コード品質スコアが「Codex 81.0点 / Claude Code 76.8点」で、特に保守性とエラーハンドリングでCodexが上回ってる。「Codex CLIは複雑なロジックや大規模システム設計でClaude Codeより高品質なコードを生成する」っていう評価が複数の検証記事で出てる。
理由4：速度が速い。Terminal-Bench 2.0で77.3%を取ってる通り、ターミナル作業の速度はCodexが優位。Claude Codeが65.4%なので、約12ポイント差。日常的にCLIで作業する副業勢には地味に効く。
理由5：バグが少ない。「0からの実装ではCodexのほうがバグが少ない」っていう評価が複数のレビュー記事で出てます。一回で動くコードが返ってくる確率が高い。これは副業で時間が限られてる人には決定的に重要。
理由6：セカンドオピニオンとして使える。OpenAI公式の`codex-plugin-cc`っていうプラグインがあって、Claude CodeのセッションからCodexを呼び出して、コードレビューさせられる。「Claude Codeが書いたコードをCodexにレビューさせる」っていう使い方が、業界標準になりつつある。
Codexの弱点—こちらも正直に晒す
Codexにも弱点があります。Claude Code推しの人が見落としがちなポイントも含めて、晒します。
弱点1：コンテキスト把握力でClaude Codeに劣る。Codexは「限られたコンテキスト窓内での情報しか参照できず、プロジェクト全体の設計方針や既存コードとの整合性を完全に理解することは困難」っていう評価が出てます。長尺のプロジェクトをまるごと理解させたいときは、Claude Codeのほうが優位。
弱点2：カスタマイズ性が低い。Claude CodeはSkills、hooks、MCP、Subagentで細かくカスタマイズできるけど、Codexはカスタムコマンド程度。自分専用のワークフローを作り込みたい人には、物足りなく感じることがある。
弱点3：利用制限が突然来る。Codexは「5時間制限」と「週次制限」を同時に管理してて、週次を使い切ると5時間枠が残ってても続けて使えない。しかも警告なしに突然来るから、作業が中断される不満が多い。
弱点4：新しいフレームワークやライブラリへの対応が遅いことがある。学習データのカットオフの関係で、最新のAPIや非推奨パターンを提案してくることがある。これはClaude Codeも同じ問題があるけど、Codexのほうが顕著という報告がある。
弱点5：セキュリティリスク。これはどちらにも言えるけど、Codexが生成するコードには、SQL Injection、NoSQL Injection、Command Injectionなどの脆弱性が含まれる可能性が指摘されてる。本番に出す前のセキュリティチェックは必須。
弱点6：料金プランの変更が激しい。2026年4月にChatGPT Pro 100ドルプランが新設されて、Codexの利用枠が再編されました。「以前はこれで足りてたのに、今月から足りない」みたいなことが起きやすい。
Codexを副業で使うときの実践イメージ
Codexを副業で使うときの具体的な動きを、実例ベースで描きます。
ケース1：リポジトリ全体のバグ修正。「このリポジトリの全テストを通して、失敗してるテストは全部修正して」って指示を出して放置。クラウドサンドボックスで自動実行されて、PRが立つ。所要時間：人間の作業30分、AIの自動作業数時間。
ケース2：Plan→実装の高速化。Claude Codeで設計（Plan）を立てて、その実装をCodexに投げる。「Codexが書く速度はClaude Codeの2倍くらい」っていう評価がある通り、実装フェーズで時短になる。所要時間：Plan 30分、実装1時間。
ケース3：PRレビューの自動化。GitHubのPRに`@codex`タグでメンションすると、Codexが自動でレビューコメント書いてくれる。これ、副業でクライアント案件持ってる人には超強力。
ケース4：ローカルアプリの操作自動化。computer use機能で、Keynoteでスライド作成、Excelで集計表作成、Photoshopで画像書き出し、みたいなGUI作業を自動化できる。所要時間：30分の指示で、3時間分の作業が完了。
ケース5：ChatGPT内でのワンストップ作業。ChatGPTで記事の構成相談→そのままCodexに「この内容でLP作って」と指示→クラウドで実装→Vercelデプロイまで。ChatGPTから出ずに完結する。所要時間：2〜3時間。
Claude CodeとCodex、ここまでで見えてきた違い
第2章と第3章で、両方の正体を見てきました。ここまでで見えてきた違いを、ザックリまとめます。
📷
これだけ見ると、「あれ、Codexのほうが良くない？」って思った方もいるかも。でも、Claude CodeにはSkillsとObsidian連携、長文耐性っていう、副業勢にとって決定的な武器があります。だから単純比較じゃなくて、「どっちがどの用途で強いか」を理解することが大事。
次の第4章では、機能をもっとガチで比較します。ベンチマーク数字、コード品質、速度、UI/UX、エコシステムまで、全部見ていきます。
第4章：機能ガチンコ比較—ベンチマーク・速度・コード品質
ベンチマーク数字を、副業文脈に翻訳する
まずベンチマーク数字を整理して、それを副業文脈に翻訳します。
2026年4月時点の主要ベンチマークはこう：
SWE-bench Verified（既知の実プロジェクトのバグ修正タスク）
· Claude Opus 4.7：87.6%
· GPT-5.4：85.0%（GPT-5.5の数値は未公表だが向上見込み）
· Gemini 3.1 Pro：80.6%
SWE-bench Pro（より難しい、汚染の少ない問題）
· Claude Opus 4.7：64.3%
· GPT-5.4：57.7%
· Gemini 3.1 Pro：54.2%
Terminal-Bench 2.0（ターミナル作業の精度）
· Codex CLI：77.3%
· Claude Code：65.4%
Rakuten-SWE-Bench（Anthropic内部テスト）
· Opus 4.7：Opus 4.6の3倍のタスク解決
これ、数字だけ見ても「で？」って感じだと思うので、副業文脈に翻訳します。
SWE-benchは「既存コードのバグ修正能力」のテスト。副業文脈で言うと、「既存のLPテンプレートをカスタマイズして、不具合を直す」みたいな作業の精度。Claude Opus 4.7が87.6%、GPT-5.4が85.0%。差は2.6ポイント。これは正直、副業実用では誤差レベル。どっちでも問題ない。
SWE-bench Pro（より難しい問題）では差が広がって、Claude Opus 4.7の64.3% vs GPT-5.4の57.7%、6.6ポイント差。複雑な案件ではClaude Codeのほうが安定するイメージ。
Terminal-Bench 2.0は「ターミナル作業の正確性」。Codex CLIが77.3%、Claude Codeが65.4%。これは12ポイント差で、結構大きい。「コマンド実行を多用する作業」では Codex 優位。
ここで重要なのが、ベンチマーク数字の差は、実務では「3倍速い・遅い」みたいな極端な体感差にはならないってこと。両方とも実用レベルでは「使い物になる」のは確実。差が出るのは、複雑性が上がったときと、特定タスクの得意/不得意。
副業勢にとって意味のある翻訳をすると、こうなります：
· 「LP作って」「note記事書いて」みたいなシンプルタスク → どっちでもほぼ同じ
· 「複雑な会員サイト構築」「決済込みSaaS」 → Claude Codeがやや優位
· 「コマンド多用する自動化スクリプト」「定型のCLI作業」 → Codex優位
· 「PRレビュー・既存コードのリファクタ」 → Codex優位
コード品質、ガチで比較した結果
次にコード品質。これは複数の検証記事で実測されてます。
Qiitaに上がってる「Claude Code vs Codex：同じアプリを作ってコード品質を比較してみた」っていう検証記事では、同じ要件で同じアプリを作らせて、コード品質をスコア化してます。結果はこう：
· Codex：81.0点
· Claude Code：76.8点
特に差が出たのが「保守性」と「エラーハンドリング」。Codexのほうが、後から見たときに整理されてて、エラー処理が丁寧。これは「タスクを任せられるクラウドワーカー」っていう設計思想が反映されてる結果。
一方で、Claude Codeは「コンテキスト把握力」と「ユーザーの意図汲み取り力」で上。例えば、「過去の会話で言ってた方針」を覚えてて、それに合わせてくる精度はClaude Codeのほうが高い。
ここでX上の興味深い投稿を紹介します。「@masa_oka108」さんが「Claude Codeで作ったPlanをCodexでレビューするの良さそう！」って投稿して、これがバズりました。これは、両者の特性をうまく活かす使い分けです。
つまり、
1. Claude Codeで「文脈理解」「設計（Plan）」を担当させる
2. Codexで「実装」「品質チェック」を担当させる
この役割分担で、両者の強みを最大化できる。
海外でも同じパターンが流行ってて、Hacker Newsの「Codex vs. Claude Code (today)」スレッドで「I prefer Claude for the small tasks and fast iteration pair coding experience」っていうコメントに高評価が集まってる一方、別のスレッドでは「Some developers use a pattern where Codex drafts and Claude reviews, as the two models catch different classes of mistakes」（CodexがドラフトしてClaudeがレビューするパターン。両モデルは違う種類のミスを捕まえる）っていう知見が共有されてます。
つまり、「どっちがレビューでどっちがドラフトか」は、人によって逆になることもある。重要なのは「両方のモデルが違う観点で見る」ことで、品質が上がるってこと。
速度比較、これは体感差デカい
速度に関しては、両者の体感差はデカいです。
複数のレビュー記事を読むと、こういう傾向があります。
Claude Code
· 初動が遅い（最初のトークンまで5〜15秒）
· でも、いったん動き出すと文脈に沿った提案が早い
· 1Mコンテキストを使うとさらに重くなる
Codex（GPT-5.5）
· 初動が速い
· トークン効率が良くて、同じタスクでもトークン消費が少ない
· 「GPT-5.4 Highで5〜6分→GPT-5.5 Mediumで2分半」という体感報告
具体的な比較として、AQUA テックブログの「実際にチャットボットを作らせてみた」検証では、Claude Codeが約25分でプロジェクト完了、Codexが約40分。逆にCodexが速かった例もあって、Qiitaの検証では「Codex CLIは2倍速」っていうケースも報告されてる。
要するに、速度は「タスクの種類」で勝ち負けが入れ替わる。
· 小さい修正、対話的なやりとり：Claude Codeが速い
· 大きいタスク、まとめて実装：Codexが速い（特にGPT-5.5以降）
· コンテキスト読み込みが必要なタスク：Claude Codeのほうが速い場合がある（1Mコンテキストで一気に読める）
· ゼロからの実装：Codexが速いことが多い
副業勢の運用としては、「対話して進めるならClaude Code、投げて待つならCodex」って覚えとけばOK。
UI/UXとエコシステム比較
UI/UXとエコシステムも大事な比較ポイント。
Claude Code側
· ターミナルベース。最近デスクトップアプリも刷新（2026年4月14日）
· VS Code拡張あり
· Skills、hooks、MCP、Subagentで超カスタマイズ可能
· Claude Coworkとの連携が強力（SNS投稿同時化など）
· GitHubの`awesome-claude-code`に何百ものSkillsが公開
· Obsidian連携が強い（個人発信者・ライターに刺さる）
Codex側
· ChatGPT、CLI、VS Code、macOSアプリ、Web、複数の入り口
· GitHub PRレビューが`@codex`タグで起動
· ChatGPT内で完結できるので、非エンジニアでも使いやすい
· カスタマイズはカスタムコマンド程度
· Computer use機能（macOSアプリ操作）
· Amazon Bedrock対応で、エンタープライズ環境にも対応
エコシステムの観点では、Claude Codeが圧倒的に成熟してる。Skills、Subagent、Plugins、MCPの組み合わせで、自分専用の作業環境を構築できる。これはX上のIndie Hackersコミュニティで「Claude Code is the most enjoyable to work with. UI and interaction flow feels like a damn video game」って評されてる通り。
一方、Codexは「使い始める敷居の低さ」と「ChatGPT統合」が強み。非エンジニアでChatGPTに慣れてる人には、Codexのほうが入りやすい。
副業勢への翻訳：
· 既にClaudeに課金してて、本気でカスタマイズしたい → Claude Code
· ChatGPTに慣れてて、まずは試したい → Codex
· ライター・発信者で、Obsidian使ってる → Claude Code
· GitHubで案件管理してる → 両方（CodexのPRレビュー機能が便利）
「rate limit arbitrage」って知ってますか？
最後に、海外勢が編み出した裏技を紹介します。
Rate Limit Arbitrage（レート制限裁定）——これは、Claude CodeとCodexを並列で動かして、片方がレート制限に達したらもう片方に切り替える、っていう運用。
X上のAlphaSignal AIが投稿した「smux」っていうツールがあって、これはtmuxセットアップでClaude CodeとCodexを同じワークスペースで連携させる仕組み。両方が同じプロジェクトを見て、メッセージを行き来できる。
Indie Hackersコミュニティでは、Dennis Lysenkoが「Why I Run Claude Code and Codex Side By Side」っていうブログ記事を書いてて、「2〜4個のエージェントを並列で動かして、Claude Codeがレート制限に達したらCodexに移して作業を継続する」っていう運用を公開してます。
これ、副業勢にとってどう意味があるかと言うと、「月120ドルで、ほぼ無制限の作業時間を確保できる」ってこと。Claude Code Max 5xで100ドル、ChatGPT Plusで20ドル、合計120ドル。これで、レート制限に振り回されずに副業作業を回せる。
逆に、「片方だけ」だと、絶対どこかでレート制限に当たって作業が止まる。これが副業の生産性を下げる最大の要因。だから、本気で稼ぐなら両方契約が、海外Indie Hackersでは標準になりつつある。
次の第5章では、この料金の話をもっと詳しく、コスパ観点で深掘りします。
第5章：料金とコスパのリアル—月いくら、何ができるか
Claude Codeの料金プラン早見表
Claude Codeの料金プランを、2026年4月時点で整理します。
ここで注意点。2026年4月21日に「Pro 20ドルプランからClaude Codeを削除する」って一旦発表されて、X上で大炎上→撤回された経緯があります。Maximiliano Firtmanっていう海外開発者が「¿CHAU CLAUDE CODE?（さよならClaude Code？）Pro 20ドルプランからClaude Codeが削除された」ってスペイン語で投稿して、世界中で混乱が広がった。
Simon Willisonっていう著名な開発者も「Is Claude Code going to cost 100ドル/month? Probably not—it's all very confusing」（Claude Codeは100ドル/月になるのか？たぶんならない、でもマジで混乱してる）ってブログに書いてます。
結論：2026年4月末時点では、Pro 20ドルでClaude Code利用可。ただし、レート制限が厳しいので、本格利用にはMax 5x（100ドル）以上が事実上必須。これは今後も変わる可能性あるので、契約前に最新情報を確認する必要があります。
Codexの料金プラン早見表
2026年4月2日にOpenAIが料金体系を改定して、Plus、Pro、Business、Enterpriseがトークンベースのクレジット制になりました。4月9日には新しいPro 100ドルプランが追加。Pro 100ドルは「Codexのレート制限10倍プロモ期間（5月31日まで）」を含んでて、その後5倍に戻る予定。
ここで重要なのが、ChatGPT Plus 20ドルでCodexが普通に使えるってこと。海外Reddit/Hacker Newsの一致した評価が「Codex 20ドルは一日中コーディングできる、Claude Code 20ドルは複雑プロンプト数回で枠が尽きる」。
これがCodexの強烈なコスパ優位性。月20ドルで本気で使えるのはCodexだけ。
用途別最適プラン早見表
副業・SNSマネタイズ用途で、月の予算別に最適プランを整理します。
ここで一番おすすめなのが「予算 月120ドルの両刀型」。海外Indie HackersのDennis Lysenkoも、複数の検証記事も、X上の発信者も、ほぼ全員がこの組み合わせを推してます。理由は、コスパと機能のバランスが最高だから。
「月120ドル」の現実的な投資対効果
「月120ドルって、副業初心者には高くない？」って思う方もいるかも。ここでガチで現実的な投資対効果を計算します。
副業の作業内容と、AI併用前後の所要時間を比較してみます。
LP制作1本
· AI併用前（外注前提）：20〜30万円、納期2週間
· 自力（AIなし）：60〜80時間
· Claude Code＋Codex：3〜5時間
note有料記事1本（5,000字）
· AI併用前：8〜15時間
· Claude Code＋Codex：1〜2時間
Threads投稿30本（1ヶ月分）
· AI併用前：15〜20時間
· Claude Code＋Codex：1〜2時間
講座スライド15枚
· AI併用前（デザイナー外注）：10万円、納期1週間
· 自力：20〜30時間
· Claude Code＋Codex：3〜5時間
会員サイト構築
· AI併用前（外注）：50〜100万円
· 自力（エンジニア前提）：80〜120時間
· Claude Code＋Codex：1〜3日
これ、月120ドル（約18,000円）で、外注換算すると数十万〜数百万円分の作業が回せるってこと。ROIで言うと、最低でも10倍、案件によっては100倍以上。
しかも、副業で重要なのは「時間」。本業がある人は、副業に使える時間が週10〜20時間しかない。その時間で月10〜30万稼げるかどうかは、生産性で決まる。月120ドルの投資で生産性が3倍になるなら、それは絶対ペイする。
「月20ドルで始める」の現実
「いや、それでも月120ドルは厳しい」って人へ。月20ドルで始める現実を見ます。
月20ドルコース：ChatGPT Plus のみ（Codex使用）
メリット：
· Codexが一日中使える
· 初期設定が軽くて、即戦力
· 副業始めたばかりの人には十分
できること：
· LP制作（基本レベル）
· note記事執筆
· SNS投稿生成
· 簡単なWebアプリ
· PRレビュー（GitHub連携）
· 画像生成（DALL-E）
制限：
· Claude CodeのSkills、Obsidian連携、長文耐性は使えない
· カスタマイズ性が低い
· 複雑なプロジェクトでは厳しい
これでも、副業始めたばかりで「まず月5万円稼ぎたい」レベルなら、十分戦える。実際、X上で「ChatGPT Plus 20ドルで副業100万円達成」っていう発信もある（信ぴょう性は要確認だが、可能性としてはあり得る）。
つまり、最低ラインは月20ドル。本気でやるなら月120ドル。プロ型なら月300ドル。これがコスパの3段階。
予算別の判断ロジックは：
· 副業始めたばかりで売上ゼロ → 月20ドル（Codexのみ）でスタート
· 月5〜10万売上が出始めた → 月100〜120ドルにアップグレード
· 月30万以上、または本業並み → 月200〜300ドルのプロ型
次の第6章では、もっと具体的に「副業・SNSマネタイズで本当に使えるのはどっち」を、用途別にガチで比較します。
https://note.com/hataraku_writer/n/n25386bdad859?app_launch=false
記事の公開をご希望の場合
プレミアムにアップグレード

---

## 15. @ComagerTon79278（2026-05-05 09:43:02）

**URL:** https://x.com/ComagerTon79278/status/2051598535427231802

これ、誰も知らないClaude Codeの使い方じゃない？

スキルを超絶パワーアップする方法があって、「このスキルに最適なサブエージェント作って」って投げるだけで、そのスキルを爆速でパワーアップしてくれるサブエージェントを4個を自動生成してくれる！

クラウドワークス半自動運用してるんやけど、納品物作成スキルがイマイチで困ってたけど、抜群に改善したね。

---
