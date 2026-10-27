# Seat: historian

## Core position
四个选项都没有消灭上一代同步工具的失败模式,只是搬了家。反复出现三类:旧设备覆盖新内容(Dropbox 到 Obsidian Sync 2024-25);冲突副本被当普通文件传播(Dropbox、Syncthing);工具误判远端状态后自动删除(LiveSync 2026-01 报告、官方 obsidian-headless 2026 年 issue)。差别在出事后的恢复手段由谁掌握。历史上最稳的是独立于同步层的 git 或快照;"连续双向实时同步"失败最集中。置信度中等:证据多为个案,无发生率数据。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | Dropbox 式"conflicted copy"的触发条件里已包含"文件在另一台电脑上保持打开后被当成新编辑保存",即自动保存类程序天然制造冲突。注意:我没有打开该页面,依据搜索结果摘要 | 搜索摘要转述 Dropbox 帮助中心:冲突副本在多人同时编辑、一人离线编辑、"a file left open on another computer that gets saved as a new edit, which is common with auto-save apps" 时产生;"The last version saved will always appear as the conflicted copy"(此处为摘要转述,非原页面逐字引文) | https://help.dropbox.com/organize/conflicted-copy | 页面无日期(Dropbox 该机制约 2008 起,日期未核实) | primary(未开页) | M |
| 2 | Syncthing 不做合并:修改时间较旧的一份被改名为 .sync-conflict-*,且冲突文件会像普通文件一样传播到所有设备 | "The file with the older modification time will be marked as the conflicting file and thus be renamed."; 冲突文件"are treated as normal files after they are created, so they are propagated between devices." | https://docs.syncthing.net/users/syncing.html | 页面无日期,2026-10 抓取 | primary | H |
| 3 | Obsidian Sync 对 markdown 做 diff-match-patch 合并,其他文件(含 canvas)"last modified wins";1.9.7 起可选"创建冲突文件"。官方排障页没有提到外部(文件系统)写入 | "Obsidian Sync merges the changes using Google's diff-match-patch algorithm."; "For all other files, including canvases, Obsidian uses a \"last modified wins\" approach."; "Starting in Obsidian 1.9.7, you can choose how to handle conflicts."; 启动时自动创建/修改笔记的用户会被保留远端版本而不合并 | https://obsidian.md/help/sync/troubleshoot | 页面无日期,版本节点 1.9.7;2026-10 抓取 | primary | H |
| 4 | Obsidian Sync 存在"陈旧设备覆盖新数据"的长期未结案 bug 报告串,与 Dropbox 时代同型 | 2024-07 起:iPhone 闲置五天后"ERASES hours and days worth of work!";2024-07-16 iOS 合并把 daily note 清空;2025-05 Android;2025-10 iPad 冲突文件只含旧版本;2025-11 iPhone 覆盖当天在桌面编辑的 Bases 文件;串中回复者称 "most (all?) people don't have this problem",无记录的结论或修复 | https://forum.obsidian.md/t/obsidian-sync-on-iphone-overwrites-newer-data-causing-data-loss/85214 | 2024-07 至 2025-11 | primary(用户第一手报告) | M(个案,发生率未知) |
| 5 | "无头 Obsidian Sync"是用户 2021 年就提出的需求,官方 CLI 到 2026 年初才出现,约四年半;期间社区的变通办法是在 Linux VM 或树莓派上长期运行完整 Obsidian | 论坛帖 2021-10-25 开帖;bdillahu 2021-10-27:"I have a VM (linux) that's running Obsidian and syncing so that it can run the backup."; equuapotesta 2022-04-12:"I keep obsidian running on a pi that runs various text manipulation scripts against the note directory"。obsidian-headless 仓库最早的 issue 日期为 2026-02-28(#2) | https://forum.obsidian.md/t/possibility-for-headless-syncing-with-a-cli-daemon/26162 ; https://github.com/obsidianmd/obsidian-headless/issues | 2021-10 至 2026-02 | primary | H(时间线)/M(发布日期取自 issue 日期与二手博客的 2026-02 说法) |
| 6 | 官方 obsidian-headless 是第一代产品,19 个未关闭 issue 中有删除文件和连续模式失效类问题,Linux 上连续模式漏检 .obsidian 目录改动 | #19 "Headless on new vault starts deleting remote notes"(2026-04-11,7 条评论);#28 "`ob sync` regularly deleting files it thinks are \"local only\", or in bidirectional mode deleting files seemingly at random"(2026-05-13,5 条评论);#53 "locally moved file reappears at its old path ~2 minutes later and is re-uploaded"(2026-09-08);#54 "sync --continuous on Linux never detects local changes to config-folder files (.obsidian/…) until restart"(2026-09-23);#50 "hangs indefinitely at \"Connecting...\" after a host reboot"(2026-08-16)。README:模式有 bidirectional(默认)、pull-only、mirror-remote;"--conflict-strategy accepts merge or conflict" 但未解释 | https://github.com/obsidianmd/obsidian-headless/issues ; https://github.com/obsidianmd/obsidian-headless | 2026-02 至 2026-10 | primary | H(issue 存在)/L(这些 issue 是否已在本地修复未核实) |
| 7 | LiveSync 的丢库报告:用户 2026-01 报告整库从 NAS 消失、新建文档消失,根因未确认;恢复靠的是 CouchDB 和独立的 Forgejo git 备份;用户的缓解办法是关掉实时同步改定期同步 | 用户称 "I've just had a newly created document totally vanish";版主怀疑环境:"I'd suspect something with your NAS or Livesync or encryption methods before Obsidian.";变通:`liveSync: true → false`,改定期复制,开启 `disableWorkerForGeneratingChunks`;"No official root cause or fix was identified in the thread."(此句为我抓取工具的概括,非原帖引文) | https://forum.obsidian.md/t/catastrophic-data-loss-entire-vault-contents-gone-wtaf/109823 | 2026-01-11 至 01-13 | primary(用户第一手,根因未证实) | L(是否因 LiveSync 未证实;但"git 备份救了他"这一点 M) |
| 8 | LiveSync 没有被放弃,相反迭代极快,但迁移/重建要求频繁。2026-10 的 27 天里发了 10 个版本;README 要求不得与任何其他同步方案并存,并要求升级前备份 | 1.0.33(10-01)至 1.0.42(10-27);1.0.38:"Migration requires updated clients, a Rebuild from a complete authoritative Vault";1.0.33:"Update every synchronising device before enabling it."; README:"Do not enable this plug-in alongside another synchronisation solution (including iCloud and Obsidian Sync)." 与 "Before installing or upgrading this plug-in, please back up your vault."; "Self-hosted LiveSync 1.0 requires Obsidian 1.7.2 or later."; 12.8k stars,2,186 commits | https://github.com/vrtmrz/obsidian-livesync/releases ; https://github.com/vrtmrz/obsidian-livesync | 2026-10 | primary | H |
| 9 | LiveSync 的托管历史本身是先例:README 提示"自己搭服务器"并注明 Fly.io 不再免费,即曾被推荐的免费托管路径消失过 | README Tip:"please set up your own server",并说明 "Fly.io is no longer free." | https://github.com/vrtmrz/obsidian-livesync | 2026-10 抓取 | primary | M |
| 10 | obsidian-git 的维护者自己写明手机端"very unstable"并说不会修;该插件已经历过一次作者交接(原作者 denolehov,Vinzent03 自 2021-03 起维护,仓库 2024-07 迁到他名下) | "The Git implementation on mobile is **very unstable**!"; "I would not recommend using this plugin on mobile, but try other syncing services."; "I don't know how to fix this. So commenting on any issue or creating a new one won't help. I am sorry."; "the GitHub repository got moved to my account in July 2024" | https://github.com/Vinzent03/obsidian-git | 2024-07(迁移);README 其余无日期 | primary | H |
| 11 | Syncthing 在 Android 端的官方应用已停更,移动端依赖社区 fork;fork 近半年仍保持约月更 | 官方应用 2024-10 宣布停更,最终随 2024-12 版本发布(二手报道);fork 的 README:"Switching from the deprecated official version";fork 的 8 个最近 release:v2.1.7.0(21 Oct)... v2.0.16.0(08 Apr),页面不显示年份,我推断为 2026 | https://alternativeto.net/news/2024/10/the-syncthing-android-app-is-being-discontinued-but-alternatives-remain-available ; https://github.com/Catfriend1/syncthing-android ; https://github.com/Catfriend1/syncthing-android/releases | 2024-10(停更);fork 年份推断 | secondary(停更)/primary(fork) | M |
| 12 | Syncthing + Obsidian + Android 的一例"潜在破坏性"报告,无结论,且是 2023 年旧版本(过期,仅作类型参考) | "tested it out, and yes, it does happen - potentially destructive."(用户);帖子 2023-12-28 发布,2024-01-27 因 30 天无回复自动关闭,无确认修复;环境 Syncthing v1.25.0 / Android app v1.23.6(均已不是当前版本) | https://forum.syncthing.net/t/obsidian-notes-modified-on-android-sometimes-not-updated-to-desktop-and-can-get-destructively-overwritten/21350 | 2023-12 | primary | L(版本过期) |
| 13 | 自动写入者与同步并存的竞态,agent 工具自己的文档已承认;建议"暂停同步"或"把写入限制在同步忽略的文件夹" | AIWG 文档:"if Obsidian Sync (or another sync plugin) is also writing to the same vault, external writes can race with sync."; "The recommended workflow is to either pause Sync during heavy AIWG ingest, or scope AIWG to a `folder` that Sync ignores." | https://cdn.jsdelivr.net/npm/aiwg@2026.7.12/docs/storage/backends/obsidian.md | 2026-07(npm 版本号 2026.7.12) | primary(第三方工具文档,非 Obsidian 官方) | M |
| 14 | Obsidian Sync 的多年成本与限制(截至抓取日 2026-10-27,页面无日期) | Standard $4/月(年付)/ $5/月(月付),1 个库、1 GB、单文件 5 MB、版本历史 1 个月;Plus $8/月(年付)/ $10/月(月付),10 个库、10 GB(可升到 100 GB)、单文件 200 MB、版本历史 12 个月。按年付算,Standard 五年 $240,Plus 五年 $480(我的算术) | https://obsidian.md/sync | 2026-10-27 抓取 | primary | H |

## My edge
- 把 2021 年的论坛帖当时间线用:"VM 上必须有一份实时同步的副本"这个假设,社区当年的解法正是在 VM 或树莓派上常驻完整 Obsidian(行 5)。这不是新问题,而且那套解法后来被官方 CLI 取代,但官方 CLI 还处在第一代缺陷期(行 6)。
- 失败分类而不是产品排名:覆盖(行 4)、冲突副本传播(行 2)、基于错误远端认知的自动删除(行 6、7)。三类在 Dropbox 时代都有,当前四个选项至少各占一类。
- 自动写入者加人类编辑者的共享文件,在 AI 之前就是 Dropbox 的已知触发场景(行 1:自动保存类程序)和 2021-22 年用户在树莓派上跑文本处理脚本(行 5)。agent 只是把写入频率和量级拉高了。
- 维护者风险有具体先例而不是抽象担忧:obsidian-git 换过手并公开承认手机端修不了(行 10);Syncthing 官方 Android 应用停更靠 fork 接盘(行 11);LiveSync 托管推荐路径(Fly.io)失效过(行 9)。

## What the other seats will get wrong
- practitioner 席很可能把 LiveSync 在 2026 年的高迭代当作"健康"的证据。同一份 release 记录同时显示每隔几天就有迁移/重建/升级所有设备的要求(行 8),活跃与稳定是两回事。
- 谁若拿"Obsidian Sync 官方、付费、所以可靠"当结论,会漏掉行 4 的多年未结案覆盖报告,以及行 3 官方页面对外部文件系统写入只字未提(agent 写入恰恰属于这一类)。
- 谁若把 obsidian-headless 当成"VM 问题已被官方解决",会漏掉行 6:它发布仅八个月,有删除类 issue,且 README 对 conflict-strategy 几乎没有说明。
- 谁若依据 2023 年前后的 Syncthing 帖子下结论,会用到过期版本(行 12);Syncthing 本身已到 v2,Android 端是 fork。

## What would change my mind
- 找到任一方案的发生率数据(比如 LiveSync 或 obsidian-headless 的丢数据 issue 占活跃用户的比例,或 Obsidian 官方公布的覆盖类 bug 修复记录),足以说明上述个案是低概率事件。
- 能证实行 6 的删除类 issue 已在当前版本修复,并有回归测试或官方说明;那么"官方 CLI + 拉取/镜像模式"应上调。
- 能证实行 7 的丢库有明确根因且与 LiveSync 无关(比如 NAS 或加密环境问题),则 LiveSync 一项下调风险。

## Positions I hold without evidence
- 单人维护的同步插件五年存活率不高(我的先验大致是一半以下);这次没有找到公开的基数,Obsidian 论坛只有"很多插件几个月没更新但仍能用"的讨论,没有放弃率数字。
- agent 的写入模式(一次改很多文件、短时间反复改同一文件、整文件重写)比人类编辑对实时双向同步更具破坏性,这是推断,没有直接的 2026 年一手报告(我的搜索没有找到"Obsidian Sync 回滚 agent 编辑"的具体事故)。
- 实务上收敛到的缓解办法是"降低实时性"(定期而非连续、写入前暂停、写入限定在不同步的目录),依据只有行 7 和行 13 两个来源,不足以称为共识。
- 无论选哪个方案,在 VM 上保留一份独立于同步层的 git 或快照,是历史上唯一被多次证明有效的保险;证据只有行 7 的一个个案加上整个行业的常识。

## Deliberately not examined
- Syncthing 的 Android/iOS 现状细节(iOS 没有官方客户端;Möbius 等第三方)和 Syncthing v2 的变更日志。
- Evernote 锁定、Notion 导出痛点、iCloud 与 Obsidian 的具体事故年表(预算优先给了当前四个选项)。
- Remotely Save、Git 类移动端替代品(GitSync 等)的存活情况。
- 各方案的冲突行为在 agent 高频写入下的实测;这需要实验而非史料。
- 插件放弃率的基数:预算内没有找到公开数字(Moritz Jung 的统计页文本中没有数值,图表内容未能读取)。
- LiveSync 的 CLI(1.0.37 release 标题提到 "CLI changes")是否可作为 VM 端无头客户端,未核实。

## Sources
1. https://help.dropbox.com/organize/conflicted-copy , Dropbox 帮助:什么是 conflicted copy(未打开,仅见搜索摘要)
2. https://docs.syncthing.net/users/syncing.html , Syncthing 官方文档,冲突处理(2026-10 抓取)
3. https://obsidian.md/help/sync/troubleshoot , Obsidian Sync 官方排障页(2026-10 抓取)
4. https://forum.obsidian.md/t/obsidian-sync-on-iphone-overwrites-newer-data-causing-data-loss/85214 , Obsidian 论坛 bug 帖(2024-07 至 2025-11)
5. https://forum.obsidian.md/t/possibility-for-headless-syncing-with-a-cli-daemon/26162 , 无头同步需求帖(2021-10 起)
6. https://github.com/obsidianmd/obsidian-headless , 官方无头客户端仓库(2026,README)
7. https://github.com/obsidianmd/obsidian-headless/issues , 同仓库 19 个未关闭 issue(2026-02 至 2026-10)
8. https://forum.obsidian.md/t/catastrophic-data-loss-entire-vault-contents-gone-wtaf/109823 , LiveSync 用户丢库报告(2026-01)
9. https://github.com/vrtmrz/obsidian-livesync/releases , LiveSync 发布记录(1.0.33 至 1.0.42,2026-10)
10. https://github.com/vrtmrz/obsidian-livesync , LiveSync README(2026-10 抓取)
11. https://github.com/Vinzent03/obsidian-git , obsidian-git README(含移动端警告与维护历史)
12. https://alternativeto.net/news/2024/10/the-syncthing-android-app-is-being-discontinued-but-alternatives-remain-available , 官方 Syncthing Android 停更的二手报道(2024-10,仅见搜索摘要)
13. https://github.com/Catfriend1/syncthing-android 及 /releases , Syncthing-Fork 仓库与发布(年份未显示)
14. https://forum.syncthing.net/t/obsidian-notes-modified-on-android-sometimes-not-updated-to-desktop-and-can-get-destructively-overwritten/21350 , Syncthing 论坛 Android 覆盖帖(2023-12)
15. https://cdn.jsdelivr.net/npm/aiwg@2026.7.12/docs/storage/backends/obsidian.md , AIWG 文档中的同步竞态警告(2026-07)
16. https://obsidian.md/sync , Obsidian Sync 定价页(2026-10-27 抓取)
17. https://www.moritzjung.dev/obsidian-stats/pluginstats/updates , 插件更新统计页(抓取后无数值,未被引用为证据)

## Budget used
searches: 10 / 10 · fetches: 16
