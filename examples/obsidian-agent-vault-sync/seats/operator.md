# Seat: operator (跑过 LiveSync 一年、也试过 Obsidian Sync 和 Syncthing 的 Obsidian 重度用户)

## Core position
没有哪个方案能干净处理"VM 上的 agent 直接写磁盘文件 + 笔记本 + 手机"。几乎所有失败都落在三类:外部写入者(半写文件、watcher 漏掉新建目录里的文件)、长期离线后重连的设备(iOS 用旧副本覆盖新文件)、隐藏/配置文件。运维成本从低到高:Obsidian Sync + 官方 Headless 最省事,但 Headless 仍是 open beta,iOS 覆盖 bug 在 2026-08 仍被复现;git 和 Syncthing 在 VM/笔记本侧稳,弱点在手机;LiveSync 要靠插件之外的 livesync-bridge(同作者的独立小项目,不是插件本体) 才能让 VM 拿到明文文件,运维面最大。信心中等:我没找到带日期、跑满一年的第一手 LiveSync 报告,下面关于"第三个月会坏什么"的部分多数来自官方文档的自述限制。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | Obsidian 官方 Headless 存在,可在无 GUI 的 Linux 上持续同步,但必须有 Sync 订阅,且仍是 open beta | "You must have an active Obsidian Sync subscription."; `ob sync --continuous` "Run continuously, watching for changes"; 页面称其为 "open beta" | https://obsidian.md/help/sync/headless | 页面未标日期(2026-10 抓取) | primary | H |
| 2 | 官方警告:同一台设备不要同时跑桌面 Sync 和 Headless;上手前先备份。冲突策略只列出选项 `merge`/`conflict`,没有解释语义 | "Do not use both the desktop app Sync and Headless Sync on the same device, as it can cause data conflicts." / "Back up your data before you start in case anything unexpected happens." | https://obsidian.md/help/sync/headless | 同上 | primary | H |
| 3 | Headless 在 Linux 上缺原生插件:预编译二进制只覆盖 win32/darwin,Linux 不支持 birthtime(对 agent 写文件的影响未知) | "On Linux, birthtime is not supported," 且预编译原生二进制只有 win32 与 darwin | https://obsidian.md/help/sync/headless | 同上 | primary | M |
| 4 | Headless 早期有会误删远端文件的 bug:`.obsidian` 下的主题/CSS snippet 在同一轮同步里被下载后又从远端删除,桌面端再上传,形成死循环;2026-03-02 在 v0.0.4 修复 | "downloaded by the container and then immediately deleted from the remote in the same sync pass"; Licat: "Thanks, I was able to reproduce and fix. Published a fix in v0.0.4." | https://forum.obsidian.md/t/headless-sync-infinitely-deletes-themes-and-css-snippets/111757 | 2026-03-01/02 | primary (第一手报告 + 开发者回复) | H |
| 5 | agent 直接写文件系统会把半写文件同步出去;用"写临时文件再 rename"的原子写入后消失。该作者最终选了 Obsidian Sync + Headless(Hetzner 无头 Ubuntu,开机自启) | "Sync errors started cropping up: partial writes propagating to other devices, files getting into odd states."; "Writes are atomic: the server writes to a temp file, then renames it into place, so Sync never sees a half-written file." | https://blog.dmcc.io/journal/obsidian-claude-personal-assistant/ | 2026-03-18 | primary (单人第一手) | M |
| 6 | 同一作者试过三种同步,各有各的日常摩擦:git 败在手机上忘了 commit,Syncthing 要"保姆式"照看,Sync 贵但省心 | git "works beautifully until you make a quick edit on your phone and forget to commit"; Syncthing "fine but needs babysitting"; Sync "It's not free and it's not self-hosted, but it just works." | https://blog.dmcc.io/journal/obsidian-claude-personal-assistant/ | 2026-03-18 | primary (单人第一手) | M |
| 7 | Obsidian Sync 的 iOS 端有反复出现的"旧副本覆盖新文件"数据丢失报告,2026-08 仍在 1.13.7 复现;用户转述官方尚未找到根因;"create conflict file" 设置有人说有效、有人说无效 | hmijail (2026-08-15): "Same exemplified data loss bug still present in Obsidian 1.13.7's Sync."; Sumac (2026-04-13): "the ios version simply rejects the server version and uploads its own outdated version, overwriting it."; Mark.Sebastian (2026-03-10): "a file which is almost two weeks older replaces a file from a day ago."; Kryton6 说该设置后冲突减少,Sumac 说 "doesn't seem to do anything" | https://forum.obsidian.md/t/obsidian-sync-on-iphone-overwrites-newer-data-causing-data-loss/85214?page=3 | 2026-01 至 2026-09 | primary (多人第一手,无官方回复) | M(报告真实,发生率未知) |
| 8 | Obsidian Sync 套餐的硬限制对 Notion 大导入有影响:Standard 单文件 5 MB、1 GB、1 个 vault、历史 1 个月;Plus 单文件 200 MB、10-100 GB、10 个 vault、历史 12 个月;附件版本历史只留两周且计入存储 | 比较表: Standard 5 MB / 1 GB / 1 vault / 1 month; Plus 200 MB / 10 GB to 100 GB / 10 vaults / 12 months; "Attachments are kept in version history for up to two weeks" | https://obsidian.md/help/sync/plans | 页面未标日期(2026-10 抓取) | primary | H |
| 9 | Sync 价格官方 plans 页不给数字("See the Sync landing page for pricing")。第三方摘要称 Standard 约 $4/月(年付)、Plus 约 $8-10/月,我只看到搜索结果摘要,没打开原页 | 搜索摘要: "Sync Standard is $4 per month billed annually or $5 per month billed monthly"; "Sync (Plus) $8-10/month" | https://obsidian.md/help/sync/plans (官方页无价格); 摘要来自 lindy.ai/costbench 等,未核实 | 2025-中 至 2026-07(摘要自述) | secondary | L |
| 10 | LiveSync 插件只在 Obsidian 运行时工作;VM 上的无头进程改 .md 文件,没有现成路径推进 LiveSync 网络(这是第三方项目对问题的描述,我没打开原文) | "The Self-hosted LiveSync plugin only works when Obsidian is running. If you edit markdown files in a headless environment ... there is no way to push those changes into the LiveSync network."(搜索结果摘要,出自 ecstatic-pirate/obsidian-git-livesync) | https://github.com/ecstatic-pirate/obsidian-git-livesync | 未知 | secondary | M |
| 11 | LiveSync 让 VM 拿到明文文件的主要路径是作者自己的 livesync-bridge(CouchDB peer <-> storage peer)。它不自动合并冲突;默认的 Deno.watchFs 可能漏报"新建目录里的文件",对"agent 先建目录再写文件"直接相关;隐藏文件默认关闭;双向内部文件路由"remains unreleased";仓库 143 star、38 个 open issue | "The default `Deno.watchFs` backend can report a directory being created or renamed without reporting changes to files inside it."; "The bridge does not merge, migrate, or delete conflicting documents automatically."; 隐藏文件 "opt-in and disabled by default" | https://github.com/vrtmrz/livesync-bridge | 未标日期(2026-10 抓取) | primary | H |
| 12 | 另一个社区 LiveSync 无头客户端用 30 秒定时器 + mtime/size 比对,先上传本地再下载远端;成熟度很低,CouchDB 密码明文存 config.json | "Change detection - Efficient mtime + size tracking"; "Every 30 seconds (configurable)"; "Upload local changes first (preserves edits)"; "config.json contains your CouchDB password in plain text."; 11 stars, 14 commits | https://github.com/tgmstudios/obsidian-livesync-headless | 未标日期(2026 版权) | primary | M(只看 README,没验证行为) |
| 13 | LiveSync 的长期成本是数据库不收缩:删除文件不会立刻清掉旧 chunk,墓碑不是免费的,GC 不保证最小;重建服务器数据是破坏性操作,可能丢掉只存在于别的设备上的修改 | "Deleting or shortening a file therefore does not immediately remove every object which once represented it."; "Tombstones and retained metadata are not free, so Garbage Collection does not guarantee a minimal database."; 覆盖服务器是 "destructive and may discard changes which exist only on another device." | https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/troubleshooting.md | 未标日期(2026-10 抓取) | primary | H |
| 14 | LiveSync 手机端对服务器有硬性要求:必须受信任的 HTTPS 证书(自签不行),CORS 必须先在 CouchDB 配好;经 Cloudflare 时会遇到 524 超时;主 README 还要求"不要与其他同步方案(含 iCloud、Obsidian Sync)同时启用"并且"Hidden File Sync 只在普通笔记同步已正常后再开" | "Plain HTTP and self-signed certificates are not supported."; "Configure CouchDB CORS first."; "A Cloudflare `524` response means that Cloudflare timed out while waiting for the origin."; "Do not enable this plug-in alongside another synchronisation solution (including iCloud and Obsidian Sync)."; "Configure Hidden File Sync only after ordinary note synchronisation works." | https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/troubleshooting.md ; https://github.com/vrtmrz/obsidian-livesync | 未标日期(2026-10 抓取) | primary | H |
| 15 | git 同步在手机上不可靠:官方 README 自己说"高度不稳定"、不推荐在手机用,限制包括无 SSH、仓库大小受内存限制、无 rebase;克隆/拉取可能崩溃 | "The plugin is highly unstable." / "I would not recommend using this plugin on mobile"; 限制: "No SSH authentication", "Limited repo size, because of memory restrictions", "No rebase merge strategy"; 一位 iPad Pro M1 用户 3000 文件仓库检查改动要 3 分 40 秒 | https://github.com/Vinzent03/obsidian-git | 未标日期,iPad 测试可能是 2022-2023 | primary | H(限制)/ L(基准数字可能过时) |
| 16 | Syncthing 与 Obsidian 的典型噪音:多设备共享同一文件夹时,即使只在一台设备编辑也会反复出现 .sync-conflict;workspace.json 反复冲突,常见建议是用 .stignore 排除;建议改为中心辐射拓扑。以下只来自搜索结果摘要,没打开原帖 | "got sync-conflicts all the time, even when they were sure they had edited the file on a single device only"(搜索摘要转述 Syncthing 论坛帖) | https://forum.syncthing.net/t/sync-conflicts-when-file-only-edited-on-one-device/25954 ; https://forum.obsidian.md/t/slow-app-load-times-and-workspace-sync-conflicts-when-using-syncthing/44853 | 未知(Obsidian 论坛帖 id 偏小,疑为 2022 年前后,可能过时) | secondary(摘要) | L |
| 17 | 社区里"agent 的写入放在单独文件夹"是主流做法,并有人干脆不同步文件,而是在 vault 所在机器上跑 MCP server、经 Tailscale 访问。这是搜索结果摘要的转述,出处未打开 | "keep agent-written content in a separate folder, since that makes conflicts easier to manage"(搜索摘要); MCP over Tailscale 见 dmcc 博文 | https://blog.dmcc.io/journal/obsidian-claude-personal-assistant/ | 2026-03-18(MCP 部分);"单独文件夹"部分来源不明 | secondary | L(单独文件夹)/ M(MCP 路径) |

## My edge
- 失败模式按"谁在写、写在哪、谁离线"分类,而不是按产品分类:同一个 bug 形态(半写文件、新目录漏监听、离线设备重连覆盖)会在 Sync、LiveSync、Syncthing 里以不同名字出现。行 5、7、11 是同一件事的三个侧面。
- "VM 上要有明文副本"和"VM 在同步环里"是两个不同的需求。官方 Headless 和 livesync-bridge 都是把 VM 做成一个对等节点,代价分别是 beta、插件之外的独立项目、且都要处理 agent 写入的原子性。
- 原子写入(tmp + rename)和"别让 agent 与人改同一个文件"这两条与同步方案无关,但决定了任何方案的故障率(行 5、11)。
- LiveSync 的隐性成本不在服务器租金,而在"重建/覆盖服务器"这类破坏性恢复操作(行 13),以及手机必须有受信任 HTTPS(行 14)。

## What the other seats will get wrong
- 市场/定价席会把 Obsidian Sync 当"省心的默认答案"。证据显示 iOS 覆盖数据丢失 2026-08 仍在 1.13.7 复现(行 7),Headless 仍是 beta 且有过误删 bug(行 4)。省心是相对的,不是零风险。
- 研究/理论席会按产品文档把 LiveSync 的"自动合并冲突"当作可用特性。对 agent 场景它与 livesync-bridge 之间还隔着一层:bridge 明确"不合并"(行 11),VM 上的文件进 CouchDB 要走这个独立项目。
- 谁都可能默认"同步 = 双向"。Headless 提供 `pull-only` 和 `mirror-remote` 模式(官方页),意味着可以把 VM 做成只读镜像,或把 agent 目录做成单向,这比双向省很多事(见"没有证据的立场")。

## What would change my mind
- 找到 2026 年带日期、跑满半年以上的第一手报告,显示官方 Headless + agent 直接写磁盘(不加原子写入)长期无事故;那我会把 Sync + Headless 的排名再提高一档。
- 找到 livesync-bridge 在 agent 式写入(批量新建目录和文件)下的实测,证明 watchFs 漏报问题不会发生或已修复;那 LiveSync 的运维评价要上调。
- Obsidian 官方承认并修复 iOS 覆盖 bug(1.13.7 之后的版本说明),或发现该 bug 只发生在特定设置下;那么行 7 的风险要下调。

## Positions I hold without evidence
- 离线很久的手机重连时产生冲突或覆盖,是所有方案共有的结构性风险;最稳的缓解办法是让手机大多数时候在线或只读,而不是选更好的同步产品。
- Syncthing 的官方 Android 客户端已退役,继续维护的是 Syncthing-Fork;iOS 上只有闭源的第三方客户端(Möbius Sync),后台同步受 iOS 限制。这条来自我的记忆,本次没搜到可引用的页面。
- 我对 LiveSync "跑一年"的体感(CouchDB 体积增长、移动端偶发卡住后要做"fetch from remote"重建)没有带日期的外部证据支撑,只有行 13、14 的官方自述可以间接佐证。
- 如果 agent 与人几乎不会同时编辑同一个文件,三方都很少触发冲突;大部分痛感来自长时间离线设备和隐藏目录(.obsidian),而不是正文冲突。
- 把 Notion 大导入当作一次性批量写入,应当在同步关闭或只读状态下完成,导入完再开同步,这样可避免 chunk 膨胀(LiveSync)和 5 MB 限制触发(Sync Standard)带来的混乱。

## Deliberately not examined
- 官方 Obsidian Sync 的价格(plans 页不给数字,搜索摘要未核实)。
- LiveSync 主仓库自己是否已内置 CLI / 无头模式(搜索里出现了 Unraid 上的 "obsidian livesync cli" 应用页,我没打开确认)。
- Syncthing 在 iOS/Android 上的现状(Möbius Sync、Syncthing-Fork),以及 .stignore 的最佳实践。
- git 方案中 agent 自动 commit/pull 的具体工具(agentic-git-sync 等),和 GitSync 手机客户端的真实表现。
- Obsidian Sync 的 E2EE 与 Headless 一起用时的恢复流程,Node 版本要求(webpronews 称 Node 22+,官方页未写;有论坛帖报告 Node 版本依赖错误,我没打开)。
- r/ObsidianMD 的带日期长帖:这次预算内的搜索没有返回任何 Reddit 结果。

## Sources
1. https://obsidian.md/help/sync/headless : 官方 Headless 文档(open beta、命令、警告),页面未标日期,2026-10 抓取
2. https://obsidian.md/help/sync/plans : 官方 Sync 套餐对比(文件大小、存储、历史),未标日期,2026-10 抓取
3. https://forum.obsidian.md/t/headless-sync-infinitely-deletes-themes-and-css-snippets/111757 : Headless 误删 bug 与 v0.0.4 修复,2026-03-01/02
4. https://forum.obsidian.md/t/obsidian-sync-on-iphone-overwrites-newer-data-causing-data-loss/85214?page=3 : iOS 旧副本覆盖新文件的多人报告,2026-01 至 2026-09
5. https://blog.dmcc.io/journal/obsidian-claude-personal-assistant/ : 作者试过 git/Syncthing/Sync,agent 直写文件产生半写传播,原子写入修复,2026-03-18
6. https://github.com/vrtmrz/livesync-bridge : LiveSync 与文件系统之间的官方作者桥接工具,watcher 与冲突限制,未标日期
7. https://github.com/vrtmrz/obsidian-livesync : LiveSync 主 README(版本要求、不与其他同步方案共用、备份警告),未标日期
8. https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/troubleshooting.md : LiveSync 故障排查(数据库增长、HTTPS/CORS、破坏性重建),未标日期
9. https://github.com/tgmstudios/obsidian-livesync-headless : 社区 LiveSync 无头客户端 README,2026 版权,未标提交日期
10. https://github.com/ecstatic-pirate/obsidian-git-livesync : 第三方项目对"LiveSync 只在 Obsidian 运行时工作"的描述,仅见搜索摘要
11. https://github.com/Vinzent03/obsidian-git : obsidian-git README(移动端限制与不稳定警告),未标日期
12. https://forum.syncthing.net/t/sync-conflicts-when-file-only-edited-on-one-device/25954 : Syncthing 单设备编辑仍出现冲突,仅见搜索摘要,日期未知
13. https://forum.obsidian.md/t/slow-app-load-times-and-workspace-sync-conflicts-when-using-syncthing/44853 : workspace 冲突与 Syncthing,仅见搜索摘要,疑较旧
14. https://obsidian.md/help/sync/plans 与 lindy.ai/costbench 价格摘要 : Sync 价格(未核实),2025-中 至 2026-07

## Budget used
searches: 10 / 10 · fetches: 10
