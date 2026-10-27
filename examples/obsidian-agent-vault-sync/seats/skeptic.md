# Seat: skeptic

## Core position
同步传输层不是最难的部分。我找到的所有有据可查的丢数据案例（Obsidian Sync、LiveSync、Headless）机制都一样：某个对端处于空/旧/离线/挂载丢失/刚执行过 rm 的状态，其他对端把它当成真相接受，删除和空文件被"忠实地"传播。VM 上的 agent 恰好是这类对端的高风险来源。"VM 必须持有持续同步的副本"这一假设我没有找到任何来源支持；真正的硬需求只有两条：VM 上有明文文件，以及有独立于同步的版本历史/备份。git 在 VM 与笔记本之间能解决约 80%，但手机端是 git 的弱点（obsidian-git 官方称手机端 very unstable）。置信度：对"丢数据机制"为中高；对"git+cron 足够"为中低（缺手机端证据）。注意：所有引文经 WebFetch 的小模型摘要转出，需核查员逐条回原页验证。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | 官方 Obsidian Sync 在 iPhone 上有多起"用旧/空内容覆盖较新桌面内容"的用户报告；官方解释是自动合并算法可能产生不良结果；冲突只记录在重启即清空的活动日志里，同步日志每天删除，即无人值守的写入方（如 agent）看不到冲突 | hmijail: "Obsidian Sync overwriting a file with text with an EMPTY file"（2026-01-13）；staff WhiteNoise: "the automatic merge algorithm can produce undesirable outputs."；CawlinTeffid: "Sync only notifies about conflicts in its activity log which is cleared when the app restarts"；hmijail: "the sync logs are deleted daily!" | https://forum.obsidian.md/t/obsidian-sync-on-iphone-overwrites-newer-data-causing-data-loss/85214?page=2 | 2025-11-26 至 2026-01-13 | primary（用户第一手报告；根因未确认） | H（报告存在）/ L（机制） |
| 2 | Obsidian Sync 把删除当作同步内容，官方称这是有意设计；Linux 上一条 rm/find 误删 home 目录后，删除同步到云端和所有设备，靠 Sync 的批量恢复找回。agent 在 VM 上的 rm 是同一类事件 | staff: "This is an intentional decision."；"This has the potential of creating a mess if the users doesn't understand what they are doing."（谈批量恢复）；帖子称 Sync 不是备份 | https://forum.obsidian.md/t/how-obsidian-nearly-lost-all-my-files-and-scared-the-crap-out-of-me/81104 | 2024-04-30（早于 2025，可能过时，但"删除即同步"是设计属性） | primary | H |
| 3 | LiveSync 有未解决的大规模删除报告：S3/MinIO 后端，0.25.27，几乎所有文件被移入 .trash；维护者"无法复现"，issue 仍开放；维护者说自己也在"磁盘被卸载"时遇到过。注意这是 S3 后端而非 CouchDB。VM 上若 vault 所在盘挂载失败，同步守护进程会看到"全部被删" | 维护者 (2025-11-18): "I have also encountered this occurring when a disk was unmounted."；(2026-04-03) "I am sorry, but I have not been able to reproduce it yet." "Renaming a file is indeed recorded as both a deletion and a creation"；报告人 (2025-11-16): "Every file except for one I just edited" 被删；标签 "awaiting confirmation" / "need more info"；v0.25.41 (2026-01-30) 新增"恢复到指定时间点"功能 | https://github.com/vrtmrz/obsidian-livesync/issues/754 | 2025-11-16 至 2026-04-28 | primary | H |
| 4 | CouchDB 后端的 LiveSync 也有一例整库消失（NAS 上），根因未确认；该用户靠 CouchDB 里的副本和另一份 Forgejo 上的 git 副本恢复。这同时说明：独立于同步的第二份副本是救命的。 | 报告人 (2026-01-11) 发现 vault 从 NAS 消失，"recovered from backups: LiveSync/CouchDB, and a Git repository on their local Forgejo server"（摘要转述）；版主: "I'd suspect something with your NAS or Livesync or encryption methods before Obsidian."；"Grok 的理论"是断网导致本地删除，未证实 | https://forum.obsidian.md/t/catastrophic-data-loss-entire-vault-contents-gone-wtaf/109823 | 2026-01-11 至 2026-01-13 | primary（单例，根因未明） | L-M |
| 5 | LiveSync 0.25.83 修复了"仅改文件名大小写会在其他设备上删除该文件"的 bug，说明重命名类操作（agent 常做）是已知的删除触发点 | "Changing only the letter case of a file name within the same directory could delete it on other devices when 'Handle files as Case-Sensitive' was disabled."（来自 newreleases.io 对发布说明的转录，我未看到日期） | https://newreleases.io/project/github/vrtmrz/obsidian-livesync/release/0.25.83 | 日期未知（2026 年内的 0.25.x） | secondary（发布说明镜像） | M |
| 6 | LiveSync README 自带的警告：必须备份；不要与其他同步方案并用；关闭 Obsidian 过早会致文件和数据库损坏。也就是同步客户端默认是 Obsidian 应用本身，README 里我没有看到 headless/CLI 方案的描述 | "Before installing or upgrading this plug-in, please back up your vault."；"Do not enable this plug-in alongside another synchronisation solution (including iCloud and Obsidian Sync)."；"To prevent file and database corruption, please avoid closing Obsidian until all progress indicators have disappeared." | https://github.com/vrtmrz/obsidian-livesync | 2026-10 抓取（README 无日期） | primary | H |
| 7 | 要让 LiveSync 的 CouchDB 内容落到无 Obsidian 的 VM 磁盘上，官方路线是 livesync-bridge；其 README 自述：不自动合并或删除冲突文档；双向路由改动"仍未发布"；目录刚创建后立刻写入的文件可能被漏掉（agent 常见的 mkdir + write 模式；README 指默认监视器下）| "The bridge does not merge, migrate, or delete conflicting documents automatically."；"This bidirectional routing change remains unreleased."；"A file written right after its directory is created can therefore be missed while the bridge is running." | https://github.com/vrtmrz/livesync-bridge | 2026-10 抓取（无日期） | primary | M-H |
| 8 | Obsidian 官方 Headless Sync（`ob sync --continuous`）是 VM 上最贴合"agent 写明文文件"的官方通道，但仍是公开 beta，需要 Sync 订阅，官方要求先备份，且不要和桌面端 Sync 在同一台设备上并用；冲突策略只有 merge/conflict 两个选项，页面未解释行为；Linux 无 birthtime | "Open beta"（页面标注）；"Always back up your data before you start in case anything unexpected happens."；不要同时使用桌面端 Sync 和 Headless Sync，"can cause data conflicts"；模式 bidirectional / pull-only / mirror-remote；仓库 obsidianmd/obsidian-headless 当时 23 commits，页面未见 LICENSE | https://obsidian.md/help/sync/headless ；https://github.com/obsidianmd/obsidian-headless | beta 发布 2026-02-28（hada.news 报道）；页面 2026-10 抓取 | primary | H |
| 9 | Headless 客户端早期出过"无限删除循环"：开启 appearance-data 时，桌面/手机上传的主题和 CSS snippet 被下载后立即从远端删除；修复发布于 v0.0.4。版本号 0.0.x 说明它很年轻 | 报告 (2026-03-01): 日志 "Deleting remote file .obsidian/snippets/my-style.css"；Licat (2026-03-02): "I was able to reproduce and fix. Published a fix in v0.0.4." | https://forum.obsidian.md/t/headless-sync-infinitely-deletes-themes-and-css-snippets/111757 | 2026-03-01/02 | primary | H |
| 10 | 官方 Obsidian CLI 必须有桌面应用在运行，所以不是 headless VM 上 agent 的写入通道；官方把"服务器上跑 Sync"留给 Headless Sync，把"agent 访问"描述为 CLI + 明文 | "Note that the Obsidian app must be running."；"Run Obsidian Sync without a GUI"；"Give agentic tools the ability to interact with your vault." | https://obsidian.md/cli | 2026-10 抓取（CLI 自 1.12.x） | primary | H |
| 11 | obsidian-git 作者自己说手机端 git 实现不稳定、不推荐；限制包括：无 SSH、仓库大小受内存限制、可能在 clone/pull 时崩溃或无限运行。这是 git 路线的真正弱点，不在 VM↔笔记本，而在手机 | "The Git implementation on mobile is very unstable!"；"I would not recommend using this plugin on mobile, but try other syncing services."；"Limited repo size, because of memory restrictions" | https://github.com/Vinzent03/obsidian-git | 2026-10 抓取（README 无日期） | primary | H |
| 12 | Syncthing 与 Obsidian 的已记录问题是冲突文件和卡住，而不是我能找到的静默丢笔记：.obsidian（尤其 workspace.json）被 Obsidian 和 Syncthing 同时写导致 sync-conflict；2025-10 仍有人因此卡在 93%；常见做法是忽略 .obsidian。我没有找到 Syncthing 丢笔记正文的报告（搜索覆盖有限，且无 Reddit 结果） | gadget (2025-10-02): "It's why Obsidian recommends that `.obsidian` not be synced between devices."（用户说法，我未核对官方文档）；martinleben (2025-10-01): "The above are the reasons why the “.Obsidian" directory should be excluded from syncing."；centifanto (2023-09-06): "I got tired of fighting Syncthing"（改用 Obsidian Sync）；dmchrn (2024-07-05) 的忽略规则 `(?d).obsidian` 等 | https://forum.syncthing.net/t/problems-with-obsidian-folder/25397 ；https://forum.obsidian.md/t/slow-app-load-times-and-workspace-sync-conflicts-when-using-syncthing/44853 | 2022-10 至 2025-10（2022-2024 的部分可能过时） | primary（论坛第一手） | M |
| 13 | Syncthing 手机端的现状取决于社区维护者：官方 Android 应用已停更，fork 经历过"状态不明"再到"新维护者接手"；iOS 无官方客户端（此点我没有来源，见下） | 开发者 (2025-11-29): "the official Syncthing app was discontinued and the status of the syncthing-fork project is unclear"；其更新 (2026-02-13): "syncthing-fork appears to be actively maintained by new maintainers now."；Privacy Guides (2026-01-27): "The two developers have eventually joined hands." | https://github.com/chenxiaolong/BasicSync/issues/1 ；https://discuss.privacyguides.net/t/which-syncthing-fork-should-one-use-after-the-projects-handover/34966/2.md | 2025-11-29 至 2026-02-13 | secondary（第三方开发者/论坛评论，非 Syncthing 官方声明） | M |
| 14 | "agent 写入 vault 前先 git、给 agent 专属输出目录、权限靠机制而非提示词"是 2026 年的主流防护建议；其核心是"写入所有权"而不是传输方式。来源是商业博客，视为意见 | "Obsidian warns that sync is not a backup."；"A local Git commit helps with text changes, but it is not a substitute for an independent backup"；"This file tells the agent how to work, but it is not a security control."；目录分工示例：`10 Sources` 只读、`20 Notes` 需批准、`90 Agent Output` 为 agent 审阅队列 | https://aident.ai/blog/claude-code-obsidian-without-losing-notes | 2026-07-24 | opinion（厂商博客，无数据） | L-M |
| 15 | Obsidian 官方排障文档不建议 Obsidian Sync 与其他同步服务并用，且"仅在线/按需下载"的云盘会让 Sync 把本地不可用文件视为已删除。对 VM 意味着：vault 目录不要同时被 rclone mount / 备份同步工具双向触碰 | 搜索摘要称该页写明 "does not recommend using Obsidian Sync alongside another sync service"，并称按需文件会被当作已删除（我只看到搜索摘要，镜像站 mintlify，没有打开原页） | https://www.mintlify.com/obsidianmd/obsidian-help/sync/troubleshoot | 日期未知 | secondary（官方文档镜像，仅见摘要） | L-M |

## My edge
- 把"同步选型"拆成两个独立问题：谁持有规范副本和历史（git / 快照），以及传输层把数据送到哪些设备。所有已记录的丢失事件都发生在"对端状态被当真"这一层，与选哪个传输产品关系不大（claim 1, 2, 3）。
- 指出 LiveSync 在 headless VM 上需要额外的一块可动部件（livesync-bridge，双向路由"未发布"，且有已声明的事件漏检）或让 Obsidian 在 VM 上跑；而 Obsidian Sync 的 headless 客户端是 0.0.x 的公开 beta，已有一例删除循环 bug（claims 6-9）。其他座位若只比较"同步协议"，会漏掉"VM 那一端的客户端本身"才是最年轻的组件。
- 关键的未验证前提被写出来：agent 是常驻的实时对端，还是按任务触发的短会话？如果是后者，"拉取 → 干活 → 提交推送"完全覆盖，且每次运行自带 diff 和回滚点（claim 14 是意见，机制是推理，见"没有证据的立场"）。
- 注意到 #754 是 S3 后端，不应与 CouchDB 的可靠性混为一谈（claim 3 vs 4）。

## What the other seats will get wrong
- operator 座位会用自己"跑了一年没出事"作为 LiveSync 的基线；这是幸存者样本，而且 2025-2026 最醒目的 LiveSync 删除报告是 S3 后端（#754），CouchDB 的那例（claim 4）根因未明，两类不该混合评分。
- sync-researcher 座位会把重点放在并发编辑的冲突模型（谁赢、谁输）；但我找到的损失案例大多不是并发编辑，而是旧/空/离线/挂载丢失的对端把状态推给别人，以及删除本身被同步。合并算法再精确也解决不了这个（claims 1-3）。
- pricing 座位会把 Obsidian Sync 的月费当成总成本；实际上要在 VM 上用它得依赖 beta 客户端，并且所有选项都还需要第二份独立备份，这项成本在各方案中相同，但常被漏记（claims 4, 8, 14）。
- historian 座位可能说"Syncthing 的冲突文件问题已解决"；2025-10 的论坛帖显示 .obsidian 冲突仍在，手机端又依赖社区 fork（claims 12, 13）。

## What would change my mind
- 看到明确要求"手机上编辑后几十秒内 agent 就要读到最新内容"的使用场景，且无法用"agent 运行前先拉取"满足：则持续同步是必需的，我对前提的攻击就站不住。
- Headless Sync 脱离 beta、有文档化的 conflict-strategy 语义，并且 obsidian-headless 的 issue 里没有新的删除/覆盖类 bug：则它作为 VM 端的风险会明显下降。
- 找到手机端 git（Working Copy / GitSync）连续 6 个月以上的一手可靠性报告；或者找到 git 方案的静默丢数据案例（我没来得及专门搜）。前者支持 git+cron，后者反驳我的"git 失败是响的"。

## Positions I hold without evidence
- agent 的运行是离散任务（被触发、跑完退出），因此"运行前 pull、运行后 commit + push"够用；这取决于 owner 的实际用法，我没有这方面的证据。
- agent 只写新文件或只追加到自己拥有的目录，可以消除绝大多数合并冲突，与同步产品无关；claim 14 是意见来源，不是实证。
- git 的失败多半是"响的"（冲突标记、崩溃、拒绝推送），而不是静默覆盖；我没有专门搜 git 方案的丢数据报告，所以这只是推断。
- 在 VM 上用 systemd 的 RequiresMountsFor / ConditionPathExists 让同步守护进程在 vault 盘缺失时拒绝启动，可以挡住"挂载失败 → 全部被删"（claim 3 的维护者自述是触发条件之一，但这个缓解办法是我的推断，没有来源）。
- Syncthing 的版本控制（staggered versioning）可以当作一道廉价的安全网；我没有为此搜任何来源。
- Obsidian Sync 的论坛报告最多，主要因为用户基数最大和论坛最活跃，论坛报告是分子没有分母，不能当作发生率比较。
- 手机端 iOS 上 Syncthing 没有官方客户端（只有第三方付费应用）；这是我的背景知识，本次没有来源。
- 大规模 Notion 导入（含大量附件）会让 git 仓库膨胀，需要 LFS 或排除附件；没有来源。

## Deliberately not examined
- 价格、Sync 的版本历史保留期、文件大小/数量上限（pricing 座位负责）；Notion 导入落到各方案时的体量问题。
- CouchDB 运维面：压缩、认证、TLS、备份、CouchDB 升级对 LiveSync 的影响。
- LiveSync 的移动端限制、E2EE/混淆选项；Unraid 应用商店里出现了 "obsidian-livesync-cli"，我没有打开，不知道它的成熟度。
- 各方案对"agent 的非原子写入"（先写临时文件再 rename，或原地截断再写）的具体行为；这是 agent + 同步最直接的技术风险，但我没有找到可引用的一手来源。
- git 方案自身的丢数据报告、Working Copy / GitSync 的可靠性。
- 论坛帖 "Obsidian Sync silently resurrects deleted/moved files when offline device reconnects"（forum.obsidian.md/t/…/113242）：搜索摘要显示约 80 条笔记被复活，但页面抓取返回 404，我没能打开，因此没有入表。
- Reddit：搜索工具没有返回 Reddit 结果，所以没有覆盖。
- 所有引文都经过 WebFetch 的摘要模型转出，未逐字回原页比对；其中 claim 4 的 "recovered from backups" 是摘要转述，不是原文引用。

## Sources
1. https://forum.obsidian.md/t/obsidian-sync-on-iphone-overwrites-newer-data-causing-data-loss/85214?page=2 ：Obsidian Sync iPhone 覆盖/空内容报告及官方回复，2025-11 至 2026-01
2. https://forum.obsidian.md/t/how-obsidian-nearly-lost-all-my-files-and-scared-the-crap-out-of-me/81104 ：Linux rm 删除经 Sync 传播，官方称为有意设计，2024-04-30
3. https://github.com/vrtmrz/obsidian-livesync/issues/754 ：LiveSync S3 后端大规模删除 issue，2025-11-16 至 2026-04，仍开放
4. https://forum.obsidian.md/t/catastrophic-data-loss-entire-vault-contents-gone-wtaf/109823 ：LiveSync+CouchDB+NAS 整库消失，2026-01
5. https://newreleases.io/project/github/vrtmrz/obsidian-livesync/release/0.25.83 ：LiveSync 0.25.83 发布说明镜像（大小写重命名删除修复），日期未见
6. https://github.com/vrtmrz/obsidian-livesync ：LiveSync README 警告，2026-10 抓取
7. https://github.com/vrtmrz/livesync-bridge ：livesync-bridge README 限制，2026-10 抓取
8. https://obsidian.md/help/sync/headless ：官方 Headless Sync 文档（open beta），2026-10 抓取
9. https://github.com/obsidianmd/obsidian-headless ：Headless 客户端仓库，2026-10 抓取
10. https://forum.obsidian.md/t/headless-sync-infinitely-deletes-themes-and-css-snippets/111757 ：Headless 删除循环 bug 与 v0.0.4 修复，2026-03-01/02
11. https://news.hada.io/topic/27076.md ：Headless Sync 开放 beta 的报道（只见搜索摘要，日期 2026-02-28）
12. https://obsidian.md/cli ：官方 CLI 页面，要求 app 运行，2026-10 抓取
13. https://github.com/Vinzent03/obsidian-git ：obsidian-git README（手机端警告），2026-10 抓取
14. https://forum.syncthing.net/t/problems-with-obsidian-folder/25397 ：Syncthing 与 .obsidian，2025-10-01/02
15. https://forum.obsidian.md/t/slow-app-load-times-and-workspace-sync-conflicts-when-using-syncthing/44853 ：Syncthing workspace 冲突长帖，2022-10 至 2024-08
16. https://github.com/chenxiaolong/BasicSync/issues/1 ：官方 Syncthing Android 停更与 fork 状态，2025-11-29 / 2026-02-13
17. https://discuss.privacyguides.net/t/which-syncthing-fork-should-one-use-after-the-projects-handover/34966/2.md ：fork 合并，2026-01-27
18. https://aident.ai/blog/claude-code-obsidian-without-losing-notes ：agent 写入 vault 的防护建议（厂商博客），2026-07-24
19. https://www.mintlify.com/obsidianmd/obsidian-help/sync/troubleshoot ：官方排障文档镜像（仅见搜索摘要）

## Budget used
searches: 10 / 10 · fetches: 18（其中 1 次 301 重定向未取得内容、1 次 404；成功取得内容 16 次）
