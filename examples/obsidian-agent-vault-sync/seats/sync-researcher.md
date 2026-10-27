# Seat: sync-researcher (分布式系统 / CRDT / 同步冲突语义工程师)

## Core position
四个方案里没有一个能让"agent 在磁盘上直接写 + 人在笔记本/手机上编辑同一文件"在一个同步窗口内保持正确;区别在于冲突发生后谁看见、怎么坏。Obsidian Sync 对 .md 做 diff-match-patch 自动合并(静默,可能出重复文本,靠版本历史兜底);LiveSync 走 CouchDB 修订树,2026 年 7-10 月仍在修"自动冲突导致数据丢失/误报冲突"的 bug,且服务器上没有明文文件,VM 需要 CLI daemon;Syncthing 整文件按 mtime 选赢家,输家变成库内的 .sync-conflict 兄弟文件;git 做行级三方合并但手机端官方称"very unstable"。最稳的缓解与同步技术无关:让 agent 和人不写同一个文件(按路径分区/收件箱模式)。置信度:中;发生频率数据基本没有。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | Obsidian Sync 对 Markdown 用 diff-match-patch 合并;非 md(含 canvas)是 last-modified-wins;插件/设置 JSON 是"本地 key 覆盖远端" | "Obsidian Sync merges the changes using Google's diff-match-patch algorithm." / "For all other files, including canvases, Obsidian uses a "last modified wins" approach." / "It applies keys from the local JSON on top of the remote JSON." (经 WebFetch 摘要器返回,引文未逐字人工核对) | https://obsidian.md/help/sync/troubleshoot | 页面无日期;设置项自 1.9.7 起 | primary | H |
| 2 | 1.9.7 起可选冲突策略:默认自动合并,或生成冲突文件;设置是按设备的(agent 所在设备与人的设备可以不同策略) | "Starting in Obsidian 1.9.7, you can choose how to handle conflicts." / "When Obsidian finds conflicting changes, it creates a separate conflict file instead of merging automatically." / "Conflict resolution settings are device-specific." 官方页没有说明合并用的基线版本,也没有说明库外(磁盘)写入的特殊处理。"自动合并可能产生重复文本"一句只在搜索摘要里见到,未在页面抓取结果中验证 | https://obsidian.md/help/sync/troubleshoot | 2025(1.9.7) | primary | H(策略)/ L("重复文本"表述) |
| 3 | Obsidian Headless(无桌面端的官方 Sync 客户端)是 open beta,需要 Node 22+ 和有效 Sync 订阅;`ob sync --continuous` 持续监听;模式 bidirectional/pull-only/mirror-remote;`--conflict-strategy merge|conflict` 但官方未解释二者行为;禁止与桌面端 Sync 同机并用 | "Obsidian Headless (open beta) is a headless client for Obsidian services." / "Do not use both the desktop app Sync and Headless Sync on the same device, as it can cause data conflicts." / `--conflict-strategy` accepts `merge` or `conflict`(页面无解释)。无 systemd 指引;Linux 无 birthtime | https://obsidian.md/help/sync/headless ; https://github.com/obsidianmd/obsidian-headless | 2026-02 起(第三方博客称 2026.02.27,未在官方页核实) | primary | H |
| 4 | Headless 早期有实质 bug:`appearance-data` 同步配置下无限删除循环,v0.0.4 修复;说明还很年轻 | "Any CSS snippet or theme file uploaded by a real Obsidian client is downloaded by the container and then immediately deleted from the remote in the same sync pass."(报告 2026-03-01;回复称"Published a fix in v0.0.4",2026-03-02;回复者是否官方员工页面未显示) | https://forum.obsidian.md/t/headless-sync-infinitely-deletes-themes-and-css-snippets/111757 | 2026-03 | primary(一手报告) | M |
| 5 | 官方 Obsidian Sync 并非无冲突:iPhone/iPad 用旧库覆盖桌面新内容的报告从 2024-07 持续到 2025-11,根因未确认,页面可见部分无官方修复声明 | 2024-07-12 原帖:iPhone 闲置五天后把旧版本推上服务器覆盖五天工作;2025-11-28 jhedlund:"iPhone overwrote a bases file that I had changed earlier in the day on my desktop."(第 2 页以后未读;有人猜测是 Windows 系统时钟错误,仅为假设) | https://forum.obsidian.md/t/obsidian-sync-on-iphone-overwrites-newer-data-causing-data-loss/85214 | 2024-07 至 2025-11 | primary(用户一手报告) | M(存在性)/ L(发生率) |
| 6 | Obsidian Sync 价格:$4/月(年付)或 $5/月(月付);Headless 需要有效订阅,定价页未提 Headless | "$4 USD" per user per month billed annually / "$5 USD" billed monthly;抓取摘要称页面只有一个 Sync 方案、无存储/文件大小/保险库数量信息。我印象中曾有 Standard/Plus 分档,与抓取结果冲突,需人工复核定价页 | https://obsidian.md/pricing | 页面脚注 © 2026,无具体日期 | primary | M |
| 7 | LiveSync 的服务器端不是明文文件:文件被存成 PouchDB/CouchDB 文档 + 分块 + 修订历史 + 墓碑;VM 想要明文 .md 就必须跑 LiveSync CLI(`mirror`/`daemon`) | CLI README:"Vault files are stored as documents in a local PouchDB database, and the CLI syncs those documents with CouchDB."(摘要);troubleshooting:"LiveSync stores file metadata, chunks, revision history, conflicts, deletions, and tombstones." / "Tombstones and retained metadata are not free, so Garbage Collection does not guarantee a minimal database." | https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/src/apps/cli/README.md ; https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/troubleshooting.md | main 分支(无日期),2026 | primary | H |
| 8 | LiveSync CLI 对"磁盘与 DB 同时都有改动"的规则只有 mtime;mirror 跳过已冲突文档;mirror 不处理删除(磁盘上删掉会被下次运行恢复);README 没写 daemon 遇到同时编辑怎么办。对 agent 的含义:改名/删除、时钟偏差、冲突文档停在旧内容 | "Both: the newer mtime wins, and equal times do nothing." / "In mirror, conflicted documents are skipped in the sync step." / "mirror does not respect file deletions. A file deleted from storage is restored on the next run, so rm must be used instead."(均为摘要器转述,非逐字)。另:搜索摘要称 1.0.29 发布说明写到 daemon 现在会同步启动时已存在文件并"picks up edits and deletions made while it was stopped",与 README 的删除说明可能冲突,我未打开该发布说明,两条并存 | https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/src/apps/cli/README.md ; https://github.com/vrtmrz/obsidian-livesync/releases | 2026 | primary | M |
| 9 | LiveSync 1.0.0(2026-07-27)重写冲突逻辑:自动合并改用两个分支"实际共享的最近修订"为基线;无法证明关系时保留分支人工审阅;3 个以上修订两两审阅;GC V3 仅限 CouchDB 并保护活冲突分支 | "Automatic text and structured-data merge now uses the nearest revision actually shared by both branches." / "When the relationship cannot be proven, LiveSync preserves the branches for review." / "Garbage Collection V3 is limited to CouchDB"(来自 newreleases.io 对 GitHub release 的镜像) | https://newreleases.io/project/github/vrtmrz/obsidian-livesync/release/1.0.0 | 2026-07-27 | secondary(GitHub release 镜像) | M |
| 10 | LiveSync 2026 年自动冲突仍有数据丢失/误报类 bug,多个仍 open:#994 移动端误判本地有修改→自动解决丢失对方新增内容,0.25.80 部分修复;9 月有人在 v1.0.6 遇到自动合并用旧版替换约 72 KB(可从 CouchDB 修订恢复);#1207 v1.0.30 在接收端无本地修改时频繁报冲突,1.0.32/1.0.38 分别修了不同路径,仍 open | #994 原报告:"In some cases it tries to auto-resolve the conflict without asking me, resulting in the additions being lost."(2026-07-04);维护者:"the conflict-preservation logic was too conservative";#1207(2026-09-24)维护者 10-18 评论称 1.0.38 "retaining a device-local content hash"。三者都是"文件没被本机改过却被当成改过"的同类问题,与 agent 外部写入无关但会放大误报 | https://github.com/vrtmrz/obsidian-livesync/issues/994 ; https://github.com/vrtmrz/obsidian-livesync/issues/1207 | 2026-07 至 2026-10 | primary | H |
| 11 | LiveSync 移动端要求 CouchDB 走受信任证书的 HTTPS;明确不支持纯 HTTP 与自签名;官方提示不要与别的同步方案(含 Obsidian Sync、iCloud)并用 | "Plain HTTP and self-signed certificates are not supported." / "Do not enable this plug-in alongside another synchronisation solution (including iCloud and Obsidian Sync)." | https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/troubleshooting.md ; https://github.com/vrtmrz/obsidian-livesync | 2026 | primary | H |
| 12 | Syncthing 冲突模型:整文件,无合并;mtime 较旧者被改名为 `<filename>.sync-conflict-<date>-<time>-<modifiedBy>.<ext>`;mtime 相同按设备 ID;冲突文件作为普通文件继续传播;修改 vs 删除若删除赢,同样产生冲突副本;默认 maxConflicts=10;监听器聚合 10 秒,全量扫描约每小时,官方提醒监听器可能漏变更 | "When a file has been modified on two devices simultaneously and the content actually differs, one of the files will be renamed." / "treated as normal files after they are created, so they are propagated between devices" / "The maximum number of conflict copies to keep around for any given file. The default is 10." / "the watcher may miss some changes"(摘要转述) | https://docs.syncthing.net/users/syncing.html ; https://docs.syncthing.net/users/config.html | 文档页无日期(当前版本) | primary | H |
| 13 | Syncthing 在 Obsidian 里的真实摩擦主要在 `.obsidian/*.json`(workspace 等),不是笔记正文;常见处理是忽略这些路径,但忽略模式是按设备的,手机也要配;有人关 watcher,有人换成 Obsidian Sync | 2022-10 起的帖子:".obsidian/workspace-conflict" 文件,加载 8-12 秒;`(?d).obsidian` 等忽略后降到 3 秒内但后来又复发(2024-08);Möbius 用户 2026-01-25:"The only place I have a few sync conflicts is my .obsidian folder." 同帖无人报数据丢失,"Syncthing keeps both copies" | https://forum.obsidian.md/t/slow-app-load-times-and-workspace-sync-conflicts-when-using-syncthing/44853 ; https://forum.obsidian.md/t/sync-mac-pc-and-ios-using-syncthing-mobius-sync/72022?page=2 | 2022-10 至 2026-04 | primary(用户一手报告) | M |
| 14 | Syncthing 的手机端是最大短板:官方 Android 应用 2024-12 停更(替代品 Syncthing-Fork 等社区维护);iOS 只有第三方客户端,2026-01 仍有用户报告 Möbius Sync "needs to be in the foreground whilst syncing"、iOS 冻结后台导致同步随机停止 | apastuszak 2026-01-10:"But eventually the OS will freeze the app, and it wills stop syncing." ;PaulDickson 2026-01-25:"it needs to be in the foreground whilst syncing";2026-04-06 有人推荐 Synctrain "Does background sync (according to iOS limitations)"。Android 停更来自二手报道,未在官方仓库核实 2026 年当前状态 | https://forum.obsidian.md/t/sync-mac-pc-and-ios-using-syncthing-mobius-sync/72022?page=2 ; https://alternativeto.net/news/2024/10/the-syncthing-android-app-is-being-discontinued-but-alternatives-remain-available | 2024-10 / 2026-01 至 04 | primary(iOS 用户报告)/ secondary(Android 停更) | M |
| 15 | obsidian-git:桌面端有完整 git 语义(冲突标记 + 内置 ours/theirs/both 面板,auto commit-and-sync 按计划执行),手机端作者自己都不推荐:基于 isomorphic-git,无 SSH、仓库大小受内存限制、无 rebase、可能崩溃 | "The Git implementation on mobile is very unstable!" / "I would not recommend using this plugin on mobile, but try other syncing services." / "No SSH authentication," "Limited repo size, because of memory restrictions," "No rebase merge strategy"(摘要);README 推荐 GitSync(iOS/Android,与插件无关联) | https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/README.md | master 分支(无日期) | primary | H |
| 16 | 针对"VM 上的 agent + 手机 + 笔记本同时写同一库"的一手实践材料基本找不到;检索到的比较文章全是博客综述,且互相只在"Git 可审计但手机差、Syncthing 保留双版本、Sync 最省事"上一致 | 检索摘要:"The sources don't address concurrent writes from a server agent and a phone"(检索工具自己的结论,我未逐篇打开这些博客) | https://vaultpicks.net/obsidian-sync-options-compared/ ; https://www.moltyflywheel.com/blog/obsidian-sync-vs-icloud-vs-git-2026/ | 2026 | opinion | L |

## My edge
- 区分"外部写入者"与"两个 Obsidian 客户端":四个方案里只有 Obsidian Headless 与 LiveSync CLI 是为"无 Obsidian 的磁盘写入者"设计的客户端,而且两者对"磁盘上 agent 写入 vs 远端同一文件"的语义文档都很薄(Headless 的 `--conflict-strategy` 未解释;LiveSync CLI 只写了 mtime 规则)。Syncthing 和 git 天然就是文件级,对外部写入者没有特殊假设,但也没有任何合并智能(Syncthing 无合并;git 只有行级三方合并)。
- 看"输家看到什么"而不是"有没有冲突":Obsidian Sync 的输家基本看不到(静默合并,可能重复文本,事后靠版本历史);LiveSync 的输家在 mirror 里是"磁盘文件停在旧内容"(冲突文档被跳过),要靠 `ls` 的 `*` 标记发现;Syncthing 的输家是库里多出来的 `.sync-conflict-*.md`,会被 Obsidian 索引、被 agent 当作普通笔记读到(污染检索);git 的输家是工作区里带冲突标记的文件或停在 MERGING 状态的仓库,agent 如果不识别会把标记提交进去。
- 同步粒度决定可恢复性:LiveSync 的修订树(#994 里"可从 CouchDB 修订恢复")、Obsidian Sync 的版本历史、git 历史、Syncthing 的冲突副本,四者都是"丢了能找回"的设计,区别只在找回的成本和 agent 能否自助。
- 关键设计杠杆不在选哪种同步,而在命名空间分区:agent 只写自己的目录/新建文件(收件箱 + 人工归档),则"同一文件在一个同步窗口内被两个写入者碰"这一类基本被消除。这直接质疑"VM 必须持有人侧文件的实时副本"的假设。

## What the other seats will get wrong
- 实践派/市场派会把"Obsidian Sync 最省心"当结论,但官方 Sync 在 iOS 上有 2024-07 到 2025-11 持续的覆盖旧数据报告(行 5),Headless 又是 beta 且早期出过删除循环(行 4);"省心"是默认路径的体验,不是对 agent 外部写入的正确性保证。
- 容易把"LiveSync 有版本修订所以安全"当真:行 10 显示 2026 年 7-10 月维护者仍在修"自动冲突误判/丢内容",1.0.0 到 1.0.38 约三个月(版本号与日期取自 release 镜像和 issue 评论,是推算),变更频率本身就是长期运维成本。
- 容易把 Syncthing 的"保留双版本"当作"冲突解决":它只是不丢数据,不合并,并且把善后工作交给人或 agent(清理 `.sync-conflict-*`);手机端(行 14)才是真正的断点。
- 容易引用 2022-2024 年的博客/帖子描述当前行为:Obsidian 1.9.7 才有冲突策略开关,LiveSync 1.0.0 刚在 2026-07 重写冲突逻辑,Headless 2026-02 才出现。

## What would change my mind
- 对 Obsidian Headless(`bidirectional` + `--conflict-strategy merge`)做一次受控实验:agent 在 VM 上改文件,人同时在手机和笔记本改同一文件,各 N 次,结果无重复文本、无丢失,并且 Headless 离开 beta 且有稳定的 systemd 运行实例。我会因此把它上调为最低运维成本方案。
- LiveSync 的 #994 和 #1207 被关闭并连续 2-3 个月无新的"自动冲突误判/丢内容"报告,且 CLI README 补充了 daemon 的同时编辑与删除语义。我会把 LiveSync 的风险评级下调。
- 找到持续运行 6 个月以上的"agent 在服务器写、手机+笔记本人工编辑"的一手案例(任一方案),并附冲突发生次数。有了发生率,我对"没有方案正确"的措辞会调整为"实际很少坏"。

## Positions I hold without evidence
- 冲突只有在"两个写入者在彼此改动传播到对方之前都改了同一个文件"时才出现;顺序编辑(A 写完同步到 B 再由 B 改)不产生冲突,Syncthing 靠版本向量、LiveSync 靠 CouchDB 修订、Obsidian Sync 靠服务端版本。因此实际发生率取决于同步延迟与 agent 写入频率,而非人编辑频率。我没有为此找到来源,这是基于对这些系统设计的理解。
- agent 的写入方式(原地截断重写 vs 写临时文件再 rename)会影响监听型客户端(Syncthing 10 秒聚合、LiveSync CLI 的 chokidar、Headless 的 watch)是否读到半写文件;原子写入(tmp + rename)应当是默认纪律。没有查证各客户端对此的实际处理。
- 时钟偏差:Syncthing 与 LiveSync CLI 的初始规则都依赖 mtime,VM 与手机时钟漂移或 agent 工具保留旧 mtime(如 `cp -p`/rsync -t)会让赢家选择出错。行 5 里"系统时钟错误"只是论坛用户的猜测,不是证据。
- Obsidian Sync 的 diff-match-patch 合并若没有共同基线,就退化为"把双方改动拼接",这是重复文本的机制猜测;官方页面没有说明基线来源。
- 一次性 Notion 导入(成千上万个文件)对 LiveSync 的 chunk/墓碑/GC 开销和对 Syncthing 的初次扫描影响应当较大,对 Obsidian Sync 的限额(官方定价页没有写)可能有影响;未查证。
- 多年成本:Obsidian Sync 约 $48/年(年付,按行 6 的价格,需复核);LiveSync 与 Syncthing 与 git 的现金成本为零,成本主要是升级与排障时间;LiveSync 的该项最高(行 9-10 的变更频率),git 与 Syncthing 的变化最慢但手机端体验最差。这是定性判断。

## Deliberately not examined
- CRDT 类方案(Yjs/Automerge 型 Obsidian 插件如协作/实时同步服务)作为第五类:预算不够,未检索;它们是唯一在理论上能对"同一文件并发编辑"给出确定性合并的路线,但需要 Obsidian 在场,对"磁盘上的 agent 写入"可能不适用,这一点值得别的席位或后续轮次补查。
- iCloud/Dropbox 的历史冲突行为(按 brief 只作对照),以及 Remotely Save、WebDAV/S3 类插件、Obsidian Sync 之外的付费托管 LiveSync(如 Fly.io、第三方托管)。
- Syncthing Android 2026 年当前状态(官方应用停更之后 Syncthing-Fork 的现状)与 iOS 客户端的付费情况,仅有 2024-10 的二手报道。
- 各方案对大库(Notion 导入量级)的性能数据、Obsidian Sync 的存储与文件大小上限、版本历史保留期限。
- 隐私/加密差异(Headless 的 E2EE 口令存放方式页面未说明;LiveSync E2EE;git 仓库托管位置)。
- Obsidian 桌面端在文件被外部进程修改时的具体行为(重载/覆盖/合并),这对"笔记本上 Obsidian 开着、VM 上 Headless 把 agent 的改动同步进来"的路径很重要。

## Sources
1. https://obsidian.md/help/sync/troubleshoot - Obsidian Sync 冲突处理官方页(diff-match-patch、last-modified-wins、1.9.7 策略),无日期
2. https://obsidian.md/help/sync/headless - Obsidian Headless Sync 官方页(beta、订阅、--continuous、禁止与桌面端并用),2026
3. https://github.com/obsidianmd/obsidian-headless - Headless 命令与模式 README,2026
4. https://forum.obsidian.md/t/headless-sync-infinitely-deletes-themes-and-css-snippets/111757 - Headless 删除循环 bug,2026-03-01/02
5. https://forum.obsidian.md/t/obsidian-sync-on-iphone-overwrites-newer-data-causing-data-loss/85214 - iPhone 覆盖新数据长线帖,2024-07 至 2025-11
6. https://obsidian.md/pricing - Obsidian 定价页,2026(无具体日期)
7. https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/src/apps/cli/README.md - LiveSync CLI(mirror/daemon、mtime 规则、局限),2026
8. https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/troubleshooting.md - LiveSync 排障文档,2026
9. https://github.com/vrtmrz/obsidian-livesync - LiveSync README(不要与其他同步并用、备份提示),2026
10. https://newreleases.io/project/github/vrtmrz/obsidian-livesync/release/1.0.0 - LiveSync 1.0.0 发布说明镜像,2026-07-27
11. https://github.com/vrtmrz/obsidian-livesync/issues/994 - Auto-Conflict causes lost data,2026-07 至 2026-10,open
12. https://github.com/vrtmrz/obsidian-livesync/issues/1207 - v1.0.30 频繁误报冲突,2026-09-24 至 2026-10,open
13. https://docs.syncthing.net/users/syncing.html - Syncthing 冲突与扫描文档
14. https://docs.syncthing.net/users/config.html - Syncthing maxConflicts / watcher / rescan 配置
15. https://forum.obsidian.md/t/sync-mac-pc-and-ios-using-syncthing-mobius-sync/72022?page=2 - Möbius Sync + Obsidian 用户报告,2025-03 至 2026-04
16. https://forum.obsidian.md/t/slow-app-load-times-and-workspace-sync-conflicts-when-using-syncthing/44853 - Syncthing 与 .obsidian workspace 冲突,2022-10 至 2024-08
17. https://alternativeto.net/news/2024/10/the-syncthing-android-app-is-being-discontinued-but-alternatives-remain-available - Syncthing 官方 Android 应用停更报道,2024-10(二手,可能过时)
18. https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/README.md - obsidian-git README(手机端 "very unstable"、冲突 UI、auto sync)
19. https://vaultpicks.net/obsidian-sync-options-compared/ 和 https://www.moltyflywheel.com/blog/obsidian-sync-vs-icloud-vs-git-2026/ - 博客综述,仅经检索摘要看到,未打开,2026

注:所有 WebFetch 返回的"引文"经小模型摘要器处理,个别可能是转述而非逐字;凡标"摘要"处未逐字核对,事实核查席位应重点复核行 2、6、8、9。

## Budget used
searches: 10 / 10 · fetches: 20 (上限 20)
