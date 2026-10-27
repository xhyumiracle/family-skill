# Obsidian 库的同步方案：VM 上 agent 直写文件 + 笔记本/手机人工编辑时，到底会怎么坏、谁会后悔、几年下来各花多少

standard 档 · 5 席（sonnet）+ 1 名核查员 · 2026-10-27 · 本次运行目录：`projects/xhyu/family/obsidian-agent-vault-sync/`（brief、cards、seats/、claims、verification 均在其中）

## Bottom line

四个方案（Obsidian Sync + 官方 Headless、自托管 LiveSync、git、Syncthing）没有一个在「agent 在 VM 上直接写文件，同时人在手机或笔记本改同一个文件」的场景下是正确的；差别只在冲突发生后谁看得到、以什么形式坏。但核查过的事故记录显示，真正丢数据的主因不是并发编辑的合并算法，而是「某个节点处于空、旧、离线或磁盘未挂载的状态，同步层把它当成真相」，再加上删除本身会被忠实传播（官方员工原话：这是有意设计）。VM 上的 agent 正是这类高风险节点。每条路线在 VM 端的客户端都是整套里最年轻的部件：官方 Headless 是 0.0.14 的闭源 open beta，有两条 open 的删文件 issue；LiveSync 的 CLI 刚在 1.0.29 修完同类「启动扫描漏文件→当成删除」的 bug，桥接工具的双向路由尚未发布。决定故障率的杠杆与选哪个产品无关：agent 与人不写同一个文件、独立于同步层的 git 或快照、VM 端用一次性同步而不是常驻守护进程。订阅费在这笔账里可以忽略（Sync 五年 $240 到 $480）。最大的单一 caveat：所有证据都是个案，没有任何一个方案有发生率数据。

## 五席都同意的

- **没有方案在「同一同步窗口内双写同一文件」下正确**。Obsidian Sync 对 Markdown 静默 diff-match-patch 合并、其他文件「最后修改者胜」（PRIMARY-CONFIRMED，#14）；Syncthing 整文件按 mtime 选赢家、输家变成 `.sync-conflict-*` 兄弟文件并照常传播；LiveSync 走 CouchDB 修订树；git 行级三方合并但手机端作者自称 very unstable。
- **官方 Headless 是唯一的官方 VM 端客户端，但它是 open beta，需要 Sync 订阅，`--conflict-strategy merge|conflict` 两个取值没有任何行为说明，官方要求先备份且不要与桌面端 Sync 同机并用**（PRIMARY-CONFIRMED，#1）。npm license 为 UNLICENSED，最新 0.0.14 发布于 2026-07-30，维护者明说暂无开源计划（PRIMARY-CONFIRMED，#10）。#19「新库开始删远端笔记」和 #28「随机删文件」仍 open（PARTIAL，#2，见下方修正）。`--continuous` 常驻模式集中了 5 条 open issue（PRIMARY-CONFIRMED，#11）。
- **手机是 git 和 Syncthing 的断点**。obsidian-git 的 README 原话不建议在手机使用（五席引文一致，未占核查预算）；Syncthing 官方 Android 应用 2024-12-03 归档，iOS 官方 FAQ 明确「可预见的未来不会官方支持」（PRIMARY-CONFIRMED，#15；iOS 一手来源由核查员补出）。
- **LiveSync 不是无人维护，而是单人高频迭代**：10 月 27 天内 10 个版本，其中多个要求「从权威库重建」或先升级所有设备；数据库 append-only，维护者原话「迟早需要重建一次」（PRIMARY-CONFIRMED，#12）。
- **现金成本不是变量**：Standard $4/月年付（1 库、1 GB、单文件 5 MB、历史 1 个月），Plus $8/月（10 库、10 GB 可扩至 100 GB、单文件 200 MB、历史 12 个月）；五年 $240 / $480（PRIMARY-CONFIRMED，#9）。LiveSync、git、Syncthing 现金约为零，账记在运维小时和手机端。
- **同步不是备份**。历史席与怀疑席各自找到的「整库消失」案例里，救回数据的都是独立于同步层的 git 或 CouchDB 副本。

一致意见不算多，分歧（下节）才是这次运行的产出；没有出现「全体一致」的选角失败。

## 分歧（cruxes）

### Crux 1：丢数据的主因是并发编辑的合并模型，还是「节点状态被当真」+ 删除传播？
- **A 面**（sync-researcher）：关键在每个系统的冲突语义，谁赢谁输、输家看到什么。
- **B 面**（skeptic、historian）：有据可查的损失几乎都不是并发编辑，而是空/旧/离线/未挂载的节点把状态推给别人，以及删除被同步。合并算法再好也挡不住。
- **证据**：官方员工对「rm 误删经 Sync 传播到所有设备」的回应是 "This is an intentional decision."（PRIMARY-CONFIRMED，#4，2024-04 发言，身份经论坛 JSON 核实为 Obsidian Team）；LiveSync CLI #1143「容器重启 4 秒后从 CouchDB 删了 76 个文档」，根因是启动扫描被截断、被当成用户删除（PARTIAL，#6，已在 1.0.29 修复）；LiveSync #754 近乎整库删除，维护者自述「磁盘被卸载时我也遇到过」（PARTIAL，#13，MinIO 后端而非 CouchDB）；Headless #19/#28 open（#2）。
- **什么能解决它**：任一方案的发生率数据；或在你自己的 VM 上做两周受控实验（见「下一步」）。
- **当前倾向**：B 面。所有经核查的事故都属于「节点状态被当真」一类；并发编辑冲突有理论但没有事故记录。

### Crux 2：Obsidian Sync + Headless 是「最省心的默认答案」，还是「最年轻、闭源、带 open 删文件 bug 的黑盒」？
- **A 面**（operator，以及那篇 2026-03 博客）：Hetzner 上跑 Headless 的作者试过 git 和 Syncthing 后留在 Sync，「它就是能用」。
- **B 面**（pricing-analyst、historian）：0.0.x、UNLICENSED、2026-07-30 后无新版本、#19/#28 open、出问题只能提 issue 不能自查。
- **证据**：两面陈述的事实都经核查属实（#1、#10、#11 PRIMARY）。但核查员修正了一处关键引文：维护者 lishid 的原话是「如果你**人为**让扫描看不到磁盘上的文件，预期行为才是删除」，同一条评论里还写了「启动扫描绝不应静默漏文件，如果漏了那是要修的 bug」。pricing-analyst 席的转述把它截断成「扫描看不到就删是预期行为」，含义相反。#27 的「69 次远端删除」成因是 `sync-config` 把模式重置为双向，与扫描漏文件不是同一类（#2 PARTIAL）。
- **什么能解决它**：Headless 发布 0.1 并以带根因的方式关闭 #19/#28；或官方文档解释 `merge` 与 `conflict` 的实际语义。
- **当前倾向**：对「运维最省」成立，对「零风险」不成立；维护者的态度比 B 面的转述健康，但产品成熟度就是 0.0.x。`pull-only` / `mirror-remote` 模式和一次性 `ob sync` 比 `--continuous` 常驻暴露面小，这一点是推论（#11 的 5 条 issue 全在 continuous 模式，其中 #57 是 macOS 而非 Linux）。

### Crux 3：LiveSync 的高频迭代是健康还是成本？
- **A 面**（operator、pricing-analyst）：发布最勤、bug 修得快，MIT + 标准 CouchDB 意味着维护者消失也不会锁死数据。
- **B 面**（historian）：活跃和稳定是两回事；每隔几天就要求迁移、重建、全设备升级，本身就是五年期的运维账。
- **证据**：#994「自动冲突丢数据」维护者 3 天内复现、10 天后在 0.25.80 修复，仍因残留案例保持 open；#1207 误报冲突在 1.0.32 与 1.0.38 分两次修，最新评论报告三天无冲突（#5 PARTIAL：原稿漏掉了「已部分修复」）。#835「远端文件大小为 0」维护者称在 E2EE V2 下是预期表现，是否真丢数据待验证（#6 PARTIAL）。对 agent 场景，LiveSync 的 VM 端需要 CLI daemon 或 livesync-bridge，后者 README 自述「不自动合并冲突文档」「默认 watcher 可能漏掉新建目录内的文件」「双向路由尚未发布」（PRIMARY-CONFIRMED，#7）。
- **什么能解决它**：#1143 修复后 CLI 连续 6 个月无同类删除报告；bridge 的双向路由发布。
- **当前倾向**：open。这是「你愿意每月花多少小时跟版本」的问题，不是可靠性高低的问题。

### Crux 4：VM 到底需不需要一份实时同步的副本？
- **A 面**（brief 里的工作假设）：agent 要在 VM 上读写明文文件，所以 VM 必须在同步环里。
- **B 面**（skeptic、pricing-analyst，historian 的「降低实时性」观察）：没有任何来源支持这个前提。硬需求只有两条：VM 上有明文文件；有独立于同步的版本历史。如果 agent 是离散任务（触发、跑完、退出），「跑前拉取、跑后提交推送」即可覆盖，且每次运行自带 diff 和回滚点。
- **证据**：双方都没有一手来源；B 面是推理。唯一相关的一手材料是那篇博客（#3 PARTIAL）：作者的修复不是「让 agent 改用原子写」，而是**让 agent 不再直接写盘，改走自建 MCP server，由 server 做临时文件 + rename 的原子写**。这暗示第三条路：agent 根本不直接碰同步目录。
- **什么能解决它**：回答「手机上编辑后几十秒内 agent 就要读到最新内容」是否是真实需求。如果不是，持续同步就不是必需的。
- **当前倾向**：B 面，但取决于 agent 的运行形态，这是 owner 才能回答的事实。

## 盲区（没有任何席位查的）

- **Obsidian 桌面端对「文件被外部进程修改」的行为**（重载、覆盖、合并）。这对「笔记本上 Obsidian 开着，Headless 把 agent 的改动同步进来」的路径至关重要，没人查。
- **各客户端对非原子写入的处理**（原地截断重写 vs 临时文件 + rename）。这是 agent + 同步最直接的技术风险，全部席位只有一篇 n=1 博客（#3）。
- **发生率**。所有证据是论坛和 issue 的分子，没有分母。Obsidian Sync 报告最多可能只是因为用户基数最大。
- **Notion 一次性导入的体量**对 Sync Standard 5 MB / 1 GB 限额、LiveSync chunk 膨胀、Syncthing 首次扫描的影响。pricing-analyst 认为 Standard 大概率不够用，但没有来源。
- **CRDT / 实时协作类插件**作为第五类方案，理论上唯一能对同一文件并发编辑给出确定性合并的路线，但可能要求 Obsidian 在场。
- **git 路线自身的丢数据报告**，以及 Working Copy / GitSync 在手机上的长期可靠性。怀疑席的「git 的失败是响的而不是静默的」是推断。
- **CouchDB 运维面**：压缩、TLS、备份、升级。
- 核查员额外找到但没人引用的：Sync 官方排障页说「double-syncing（Sync 与另一个同步服务并行）是冲突的常见原因」，这直接约束「git 管 VM↔笔记本、Sync 管笔记本↔手机」这类混搭；论坛帖 113242「离线设备重连后 Sync 复活已删除/已移动的文件」只看到标题没打开。

以上盲区中，「桌面端对外部修改的行为」和「非原子写入」两条若有不利证据，会改变 bottom line 里对 Headless 路线的评价。

## 证据账本

| # | Claim（短） | 判定 | 权重 | 原始来源 |
|---|---|---|---|---|
| 1 | Headless：官方、open beta、需订阅、三模式、冲突策略无说明、勿与桌面 Sync 同机 | PRIMARY-CONFIRMED | = | obsidian.md/help/sync/headless |
| 2 | Headless #19/#28 open；#27「69 次删除」；lishid「扫描看不到就删」 | PARTIAL | ↓ 引文已改写；#27 成因不同 | github.com/obsidianmd/obsidian-headless/issues/28 |
| 3 | 博客：agent 直写盘导致半写传播，原子写修复 | PARTIAL | ↓ n=1；修复是改走 MCP server | blog.dmcc.io（2026-03-18） |
| 4 | 官方员工：删除经 Sync 传播「是有意设计」 | PRIMARY-CONFIRMED | = | forum.obsidian.md/t/…/81104（2024-04-30，WhiteNoise = Obsidian Team） |
| 5 | LiveSync #994 / #1207 自动冲突丢数据与误报，仍 open | PARTIAL | ↓ 已部分修复（0.25.80、1.0.32、1.0.38），残留案例跟踪中 | github.com/vrtmrz/obsidian-livesync/issues/994 |
| 6 | LiveSync CLI #1143 删 76 文档（1.0.29 修复）；#835 空文件 | PARTIAL | ↓ #1143 可用；#835 维护者称 E2EE V2 下属预期 | …/issues/1143 |
| 7 | livesync-bridge：不合并、watcher 漏新目录内文件、双向未发布 | PRIMARY-CONFIRMED | = | github.com/vrtmrz/livesync-bridge |
| 8 | Sync iOS 旧副本覆盖新数据长帖，2024-07 至今，无官方修复 | PRIMARY-CONFIRMED | = 帖子延续到 2026-09-22 | forum.obsidian.md/t/…/85214 |
| 9 | Sync 价格与限额（Standard / Plus） | PRIMARY-CONFIRMED | = 席间矛盾源于 /pricing 页只显示一条 | obsidian.md/sync |
| 10 | Headless 闭源：UNLICENSED、0.0.14（2026-07-30）、暂无开源计划 | PRIMARY-CONFIRMED | = | registry.npmjs.org/obsidian-headless |
| 11 | Headless `--continuous` 五条 open issue | PRIMARY-CONFIRMED | = #57 为 macOS | …/obsidian-headless/issues/50,53,54,56,57 |
| 12 | LiveSync append-only、「迟早需要重建」、DB 膨胀约 74 倍 | PRIMARY-CONFIRMED | = 此后已加 GC V3（beta） | …/obsidian-livesync/issues/762 |
| 13 | LiveSync #754 近乎整库删除；「磁盘被卸载时我也遇到过」 | PARTIAL | ↓「无法复现」一句出自另一回复；后端为 MinIO | …/obsidian-livesync/issues/754 |
| 14 | Sync 冲突语义：diff-match-patch / 最后修改者胜 / 1.9.7 起可生成冲突文件 | PRIMARY-CONFIRMED | = 同页另有 double-syncing 警告 | obsidian.md/help/sync/troubleshoot |
| 15 | Syncthing 官方 Android 归档（2024-12-03）；iOS 无官方客户端 | PRIMARY-CONFIRMED | = Android 社区 fork 仍在发布 | github.com/syncthing/syncthing-android；docs.syncthing.net/users/faq.html |

未进入核查预算（因多席引文一致或承重较低）：obsidian-git 手机端警告；Syncthing 冲突文档；LiveSync 1.0.0 发布说明；LiveSync 发布节奏与提交占比；AIWG 文档「外部写入会与同步竞争」；论坛帖 109823；2021 年无头同步需求帖；Headless v0.0.4 删除循环修复；Dropbox conflicted-copy 页。

## 五席一句话

- **operator**：没有方案干净处理三方写入；失败按「谁在写、写在哪、谁离线」分类而非按产品；Headless 的 `pull-only` 模式被其他席忽略。核查结果：其最重的一条（博客原子写）被降为 n=1 且因果改写。
- **sync-researcher**：区分「同步能用」和「同步正确」，指出输家在四个方案里分别看到什么；最有价值的洞察是「命名空间分区消除冲突类」。核查结果：引文全部成立，但 #994 漏掉了维护者已修复的部分。
- **pricing-analyst**：订阅费不是变量，真正的锁定是「不能自己调试同步层」；两条 VM 端通道出过同类删除 bug。核查结果：数据最扎实（npm、API 一手），但 lishid 引文截断翻转了原意。
- **historian**：四个方案没有消灭上一代的失败模式只是搬了家；2021 年社区解法就是在 VM 上常驻 Obsidian。核查结果：引文成立。
- **skeptic**：把问题拆成「谁持有规范副本和历史」与「传输层」两件事，所有已记录损失都在前一层；攻击了「VM 必须有实时副本」的前提。核查结果：#4 成立（含员工身份），#754 的「无法复现」一句张冠李戴但机制成立。

## 开放问题与下一步

- **先回答一个事实**：agent 是离散任务还是常驻进程？是否存在「手机改完几十秒内 agent 就要读到」的需求？这个答案决定 Crux 4，也决定要不要常驻同步。
- **两周受控实验比再搜十篇论坛帖有用**：在现有 VM 上跑 Headless `pull-only` 或一次性 `ob sync`，agent 只写自己的目录，同步目录外另做 git 快照（独立于 Sync），人在手机和笔记本正常用，记录冲突次数与任何删除事件。这同时回答 Crux 1 和 Crux 2。
- **先读这四个**：obsidian.md/help/sync/headless；Headless issue #28 全帖（含 lishid 原话）；livesync-bridge README；dmcc 博客（注意作者是走 MCP server 而不是直写）。
- **可以直接问的人**：在 #28 下问 lishid，`pull-only` / 一次性模式是否避开启动扫描这一类问题。
- **若走 Sync**：Notion 导入前核对附件体量与 Standard 的 5 MB / 1 GB 限额，很可能需要 Plus；导入在同步关闭状态下完成。

## Cost

seats: 5 (sonnet) · searches: 50 / 50 (seats) + 7 (verifier) · fetches: 85 (seats) + 40 (verifier) · claims checked: 15 / 15 listed（另约 10 条未纳入预算） · agents spawned: 6 · tokens: 482,031 subagent（seats 411,471：70K / 73K / 80K / 81K / 107K；verifier 70,560）+ orchestrator 读写约 60-80K · wall time: 约 20 分钟（seats 并行 5-9 分钟，verifier 5.5 分钟，其余为编排与写作）
Not verified: 「未进入核查预算」清单中的 9 项；盲区中列出的全部。
