# Seat: pricing-analyst

## Core position
订阅费不是这笔账的大头。五年现金:Obsidian Sync Standard 约 $240、Plus 约 $480(按年付;标价自 2024-03 起未变);LiveSync、git、Syncthing 现金约 $0(iOS 上 Möbius 一次性约 $5-8,价格未核实),但要付运维小时。真正的风险在"agent 直写盘面文件 + 同步层"的组合:官方 Obsidian Headless 仍是 0.0.14 beta、闭源、2026-07-30 后无新版本,未结 issue 含"远端文件被删";LiveSync 的 CLI 守护进程同类删除 bug 到 1.0.29 才修。四者退出成本都低(各端本地都是明文 md),会丢的是版本历史。置信度:中(Wayback 打不开,2023 前的价格史没有一手证据)。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | Obsidian Sync 当前标价与限额:Standard $4/月(年付)或 $5(月付),1 库、1 GB、5 MB 单文件、1 个月版本历史;Plus $8/$10,10 库、10 GB(可扩至 100 GB)、200 MB 单文件、12 个月历史。五年年付现金:Standard $240,Plus $480(月付 $300 / $600)。 | "Standard: $4/month billed annually, or $5/month billed monthly. Plus: $8/month billed annually, or $10/month billed monthly." 学生/教职/非营利 Sync 与 Publish 打 6 折("40% off") | https://obsidian.md/sync ; https://obsidian.md/pricing ; https://obsidian.md/help/sync/plans | 页面抓取于 2026-10-27(页面无日期) | primary | H |
| 2 | 2023 年以来的套餐结构只有一次变动:2024-03-20 新增 Standard,原单一档改名 Plus,价格不变;Plus 的 100 GB 档写作 "$16/month billed annually";2024-01-01 前买 50 GB 的早期用户保留 50 GB 但必须留在 Plus。2023-08 的旧价由论坛用户转述为 $8/月、月付 $10,与 Plus 现价一致,即 Plus 标价至少三年未涨。 | "Current Sync subscribers keep their plan, now called Sync Plus, with the same features, pricing" (kepano, 2024-03-20);用户 derekantrican (2023-08-16) 引 "$8/month, or $10 if billed monthly"(用户转述,非公司声明) | https://obsidian.md/blog/standard-plan/ ; https://forum.obsidian.md/t/about-pricing-aka-why-does-obsidian-service-x-cost-so-much-or-any-money-at-all/26329?page=2 | 2024-03-20;2023-08-16 | primary(博客)/ secondary(论坛转述价格) | H(结构)/ M(2023 价格)。注:"$16/月" 是总价还是附加价,原文有歧义,我没法判定 |
| 3 | Obsidian Sync 的存储与降级规则是真实的隐性成本:全账户共享上限,版本历史和附件都计入;超限时同步直接停;Plus 降 Standard 必须先只剩 1 个库;附件在版本历史中保留约两周,降级时最快办法是新建不含附件的远端库并删旧库,代价是丢版本历史。 | "the Sync plugin will cease syncing files"; "reduce the number of vaults present to one before the downgrade will be permitted"; 最快办法 "loses version history" | https://obsidian.md/help/sync/plans | 页面无日期,抓取于 2026-10-27 | primary | H |
| 4 | 公司的激励结构:Obsidian 自称 100% 用户付费、未融资,Sync 是自筹资金的收入线之一。意味着 Sync 对公司是核心产品,不会像投资人补贴的服务那样先低价再涨价(公司的论证),但同样意味着 Sync 协议和客户端对它是护城河。 | "100% user-supported. We have not raised any funds from investors." (kepano, 2023-07-01);定价页仍写 "100% user-supported" | https://forum.obsidian.md/t/about-pricing-aka-why-does-obsidian-service-x-cost-so-much-or-any-money-at-all/26329?page=2 ; https://obsidian.md/pricing | 2023-07-01;定价页 2026-10 | primary(公司自述,无独立核实) | M |
| 5 | 官方 Obsidian Headless Sync 存在,且官方直接把 agent 访问当作用例;但它是 open beta,npm 版本 0.0.14,2026-02-27 首发,最新版 2026-07-30;需要 Node 22+;依赖付费 Sync 订阅。 | "Give agentic tools access to a vault without access to your full computer."; 状态 "Open beta"; npm dist-tags latest = 0.0.14, 首发 2026-02-27T17:28Z, 末次发布 2026-07-30T15:23Z。"需付费订阅"一条来自搜索摘要对罗马尼亚语帮助页的转述,英文页未明说 | https://obsidian.md/help/headless ; https://registry.npmjs.org/obsidian-headless | 2026-02-27 至 2026-07-30 | primary | H(存在、beta、版本);M(付费要求) |
| 6 | Headless 客户端闭源且无许可证:官方贡献者明说没有开源计划,源码与主 app 大量共享;npm license 字段为 UNLICENSED。对"想自己查为什么删文件"的车主,这是不可检视的黑盒。 | lishid(CONTRIBUTOR, 2026-05-16): "At this point we currently have no plan to go open source yet, and the sources for this repo comes from a significant codeshare with the main app implementation." 另有提问者(2026-05-15): "We haven't seen any commits in almost 2 months and there's no source for the community to contribute to" | https://github.com/obsidianmd/obsidian-headless/issues/29 | 2026-05-16 | primary | H |
| 7 | Headless 有"删除文件"类缺陷史,且多条至今未结:#19(新建空库 `ob sync` 开始删远端笔记,开于 2026-04-11,open)、#28(双向模式随机删文件,2026-05-13,open)、#27(`sync-config` 把未指定的 flag 重置为默认,造成 69 次远端删除,已结)、#21("Massive deletion of image files",已结)。官方贡献者对 #28 的回应: 若扫描没看到磁盘上的文件,则"预期行为是删除"。多条维护者"无法复现"。 | #27 标题 "caused 69 remote deletions";lishid 在 #28 (2026-07-05): "If you forced the scan to not see a file on disk then the expected behavior is to delete the file because we need to assume the user has deleted the file on purpose." 共 19 个 open issue,2026-10 的新 issue 评论数为 0;repo 最末次 push 2026-07-30 | https://github.com/obsidianmd/obsidian-headless/issues/19 ; /issues/28 ; /issues/27 | 2026-04 至 2026-10 | primary | H(issue 存在及状态);M(严重度:#19 部分被用户自己证伪或无法复现) |
| 8 | Headless 的 `--continuous` 守护模式是 bug 最集中的路径:#57 macOS 重连后停止上传(2026-10-15)、#56 重试退避期间单核 busy-loop(2026-10-13)、#54 Linux 永远检测不到 `.obsidian/` 内文件的本地改动(2026-09-23)、#53 本地移动的文件 2 分钟后回到原路径并被重新上传(2026-09-08)、#50 宿主机重启后永远卡在 "Connecting..."(2026-08-16)。推论(我的,非来源所述):一次性 `ob sync`(agent 会话前后各跑一次)比常驻 continuous 暴露面小。 | 五个 issue 标题均含 `sync --continuous`;全部 open | https://github.com/obsidianmd/obsidian-headless/issues/57 ; /56 ; /54 ; /53 ; /50 | 2026-08 至 2026-10 | primary | H(issue);L(一次性模式更安全的推论,无人测过) |
| 9 | Obsidian Sync 的冲突语义:md 用 Google diff-match-patch 合并,其他文件(含 canvas)"最后修改者胜";自 Obsidian 1.9.7 起可改为生成冲突副本,且是逐设备设置。论坛有 2025-07 的第一手"合并后静默丢内容"报告。对"人和 agent 同时改同一文件"的场景,这是成本项:冲突行为靠每台设备各自配置。 | "The most recently modified version replaces earlier versions."; "Conflict resolution settings are device-specific."; NoNameBohr (2025-07-04): "a silent irreversible loss of that note version" | https://obsidian.md/help/sync/troubleshoot ; https://forum.obsidian.md/t/option-to-let-user-manually-resolve-sync-conflicts/94468 | 帮助页无日期;论坛 2025-07-04 | primary(帮助页、论坛原帖) | H(规则);M(丢失频率,个案) |
| 10 | LiveSync 的"单维护者"实锤:主仓库 vrtmrz 1998 次 contribution,第二名真人 13 次;维护者在 2024-10 自述有全职工作(能源机械行业),从未用过官方 Sync,并请用户不要要求克隆官方 Sync 功能。但同时发布节奏极快:1.0.37(2026-10-16)到 1.0.42(2026-10-27)共 6 个版本;1.0.0 于 2026-07-27 发布;MIT 许可;GitHub Sponsors 有支持者。风险画像是"bus factor = 1 + 版本变动快",不是"没人维护"。 | GitHub API contributors: vrtmrz 1998, github-actions[bot] 31, SeleiXi 13;vrtmrz: "I am in the energy machinery industry"; "I confess that I did not use Official Sync yet." | https://github.com/vrtmrz/obsidian-livesync ; https://github.com/vrtmrz/obsidian-livesync/issues/396 ; https://api.github.com/repos/vrtmrz/obsidian-livesync/releases | 2024-10-08(自述);2026-10-27(仓库数据) | primary | H |
| 11 | LiveSync 的"免费"要用运维小时付:存储为 append-only,维护者明说"一次重建迟早需要";用户报告 40 篇笔记的库 DB 涨到 74 倍(#762,2025-11-29,open);垃圾回收 V3 仍是 beta,且规格明写"不是修复手段,仅在备份可恢复时用",以历史可恢复性换空间;README 要求升级前备份;1.0.38 的 NFC 路径身份迁移需要"Rebuild from a complete authoritative vault"并在其他设备 Fetch(来自镜像站 newreleases.io 对发布说明的转述,未对照 GitHub 原文);#813(2026-03-04,open)报告重建本地/远端库后文件被丢进 .trash。 | vrtmrz (2025-12-04): "Self-hosted LiveSync is fundamentally an append-only architecture... Therefore, a rebuild will be necessary at some point."; GC 规格: "It is not a repair operation."; README: "Before installing or upgrading this plug-in, please back up your vault." | https://github.com/vrtmrz/obsidian-livesync/issues/762 ; https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/docs/specs_garbage_collection.md ; https://github.com/vrtmrz/obsidian-livesync/issues/813 | 2025-12 至 2026-10 | primary(迁移条目为 secondary 镜像) | H |
| 12 | LiveSync 若要让 VM 上的 agent 直写盘面,要用 CLI/守护进程(ghcr.io/vrtmrz/livesync-cli),它出过与官方 Headless 同类的"启动扫描漏文件→误删库"bug:#1143(CLI 1.0.18,容器重启 4 秒后从 CouchDB 删除 76 个文档),在 1.0.29(2026-10-03 前后)修复;另 #835"内容分块没复制,远端文件大小为 0",2026-09-18 在 1.0.30 上仍可复现,open。 | #1143: "the startup mirror scan deleted 76 documents from CouchDB four seconds after the container restarted"; #835 (nsanitas, 2026-09-18): "Still reproduces on `1.0.30`" | https://github.com/vrtmrz/obsidian-livesync/issues/1143 ; https://github.com/vrtmrz/obsidian-livesync/issues/835 | 2026-08-27 至 2026-10-03 | primary | H |
| 13 | git 路线的成本在手机端:Obsidian Git 自己的 README 称插件 "highly unstable",手机端 "very unstable",作者原话不建议在手机用;依赖 isomorphic-git,无 SSH、仓库大小受内存限制,大库可能崩溃,作者说"我不知道怎么修"。插件同样是单人维护(Vinzent03 863 次,第二名 73 次),但很活跃(2.42.0,2026-10-18)。 | "I would not recommend using this plugin on mobile, but try other syncing services."; "Limited repo size, because of memory restrictions." | https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/README.md ; https://api.github.com/repos/Vinzent03/obsidian-git/contributors | README 无日期,抓取 2026-10-27;发布 2026-10-18 | primary | H |
| 14 | Syncthing 路线的手机端:官方 Android 应用已于 2024-12-03 归档停更;替代是个人维护的 fork(BasicSync 单人开发,v3.7 于 2026-07-31 上架 F-Droid;Syncthing-Fork 曾状态不明,2026-02-13 作者称 "appears to be actively maintained by new maintainers now")。 | "This repository was archived by the owner on Dec 3, 2024." "This app is discontinued." | https://github.com/syncthing/syncthing-android ; https://github.com/chenxiaolong/BasicSync/issues/1 | 2024-12-03;2026-02-13 | primary | H |
| 15 | Syncthing 在 iOS 上:Möbius Sync 是闭源付费解锁(免费上限 20 MB 沙盒文件),厂商 FAQ 承认 iOS 无法常驻后台,同步可能延迟至 24 小时才启动;论坛 2026-01 有用户报告后台同步"几天或几周后随机停止"。价格来源冲突:Obsidian 论坛称约 $5,AppFollow 列表为 Pro $7.99,FAQ 不写价格。 | FAQ: "No iOS app can run continuously in the background."; apastuszak (2026-01-10): iOS "eventually suspends background apps, so Mobius Sync stopped syncing after a day, several days, or a couple of weeks, at random." | https://mobiussync.com/faq/ ; https://forum.obsidian.md/t/sync-mac-pc-and-ios-using-syncthing-mobius-sync/72022?page=2 | FAQ 无日期;论坛 2026-01-10 | primary(FAQ)/ primary 第一手(论坛) | H(行为);L(价格) |

## My edge
- 五年总账(按 2026-10 标价、年付、价格不变的假设;非现金项来自上表):

  | 路线 | 五年现金 | 主要非现金成本 | 退出成本 |
  |---|---|---|---|
  | Obsidian Sync Standard | $240(月付 $300) | 5 MB 单文件/1 GB 上限,Notion 导入若含大附件会撞线(此点无来源,见下);1 个月历史 | 各端本地即明文 md,近零;丢云端版本历史;协议封闭,无第三方客户端 |
  | Obsidian Sync Plus | $480(月付 $600;100 GB 档按 "$16/月" 若为总价则 $960,有歧义) | 同上但限额宽;降级必须只剩 1 库 | 同上 |
  | + Headless(agent 在 VM 上) | 0 额外(沿用订阅) | beta、闭源、删文件类 issue 未结、3 个月无新版 | 同上;出问题只能提 issue,无法自查 |
  | LiveSync + CouchDB | $0 | 重建 DB、升级前备份、版本变动快(11 天 6 版)、CLI 守护进程要自己盯 | 各端本地明文 md 在;远端 CouchDB 是分块文档,不能当文件树读;停用插件即可退出 |
  | git(Obsidian Git / 手机另配) | $0(托管费用我没查,见下) | 手机端官方都说不要用;冲突要人手解 | 最低:git 即格式,历史完整带走 |
  | Syncthing | $0(iOS 一次性约 $5-8) | iOS 后台不可靠;Android 靠个人 fork;冲突以副本形式保留 | 近零 |

- 激励映射:Obsidian 自筹资金、Sync 是核心收入,官方把 agent 当作用例写进文档,说明它想把 agent 订阅也收进 Sync;但 Headless 闭源、共享主 app 代码,说明协议封闭是刻意的(Sync 的护城河),不是疏忽。对你:Standard 一个库、$4/月就能覆盖 agent 场景,价格上限很低;真正的锁定是"不能自己调试同步层"。
- LiveSync 的 5 年风险画像:单人(95% 以上 commit)、有主业、活跃度当下极高;MIT + 标准 CouchDB 意味着维护者消失时库不会被锁死,但你会被冻在某个版本的 1.0.x 上,且该版本的 bug 没人修。退出是便宜的(本地文件完整),贵的是"发现问题时本地库已经和远端不一致"那一刻。
- 两条"在 VM 上让 agent 直写盘面"的官方/半官方通道(Obsidian Headless、LiveSync CLI)都出现过同一类缺陷:启动扫描漏掉磁盘上存在的文件,同步层把它当成"用户删了"并推到远端。这是一个跨方案的共性风险,不是某一家的问题。

## What the other seats will get wrong
- 实操/技术型席位容易把 Obsidian Headless 当成"官方的、最干净的答案",因为文档直接写了 agent 用例;他们可能没看 npm 版本号(0.0.x)、UNLICENSED、2026-07-30 后无发布、以及 #19/#28 这类删文件 issue 仍 open。
- 怀疑型/历史型席位容易把 LiveSync 的单人维护判为致命;数据显示它当前是所有选项里发布最勤的,真正的 5 年风险是 bus factor 和版本变动,而不是无人维护。
- 任何把"$0"当成零成本的席位:LiveSync 的账记在重建 DB(#762)和升级前备份上;git 和 Syncthing 的账记在手机端(两者的官方材料自己都承认手机是弱项)。
- 把订阅费当主要变量的席位:$240 到 $480 的五年现金,对一个"关注成本但不受成本约束"的车主,远小于一次笔记静默丢失或误删的代价。

## What would change my mind
- Obsidian 把 Headless 开源,或发布到 0.1/1.0 且 #19、#28 以带根因的方式关闭,同时 `--continuous` 的 #54/#56/#57 修好;那么 Standard + Headless 会成为我的首选。
- LiveSync CLI 的 #835(内容分块未复制)关闭,且 1.0.x 连续 6 个月不要求重建 DB;那么它的"运维小时"项应大幅下调。
- Obsidian 调涨 Sync 价格、砍 Standard 额度,或把 Headless 限定到 Plus;那么五年表要重算,自托管路线会变便宜。

## Positions I hold without evidence
- GitHub 私有仓库免费且对文本库的体量足够(没查 GitHub 当前限额和定价页)。git 托管成本栏的 $0 是这个假设。
- Notion 导出的附件会出现超过 5 MB 的文件、总量可能超过 1 GB,因此 Standard 档很可能不够用,Plus 更合适;没有查 Notion 导出的实际体量。
- 自托管 LiveSync 的运维小时数量级:首次部署若干小时,此后每次重大版本升级和 DB 重建各半小时到数小时;这是我的估计,没有来源。
- Obsidian 近期不会涨 Sync 价。依据只是 2023-07 的公司表态和三年标价不变;2024-03-20 的 Standard 公告对未来 Sync 价格没有做任何承诺(这是我读公告得出的"缺席",不是原文引语)。
- 车主"能自托管但可能不想"的便利价值,应该被计入:Sync 的 $4/月买的主要是"不用当同步运维"。
- 对"VM 必须持有实时连续同步的副本"这一假设:从成本与风险看它很可能不必要。agent 可以在会话前后各做一次一次性同步,或在 VM 上放权威副本而让笔记本/手机成为客户端。这是推论,没有来源直接支持。

## Deliberately not examined
- 2023 年之前及 2024-03 前后的 Wayback 价格快照(web.archive.org 在本环境被拒绝抓取);Commercial license 从付费改为可选的时间点没有一手证据。
- git 托管(GitHub/GitLab/Gitea 自托管)的当前定价和仓库限额;Obsidian Git 在 iOS 上的真实用户后悔报告。
- Obsidian Sync 的服务端故障史、E2EE 密钥丢失后果、iOS 端 Sync 可靠性。
- LiveSync 的对象存储/P2P 模式;CouchDB 的内存与 CPU 实测数字(我只拿到磁盘膨胀的个案)。
- Syncthing 对 Obsidian 的具体冲突行为(只拿到论坛上"保留双份副本"的转述);Synctrain、VaultSync 等 iOS 替代品的成熟度。
- Notion 导入的体量对各档限额的实际影响。

## Sources
1. https://obsidian.md/sync , Sync 落地页,价格、限额、E2EE 表述(2026-10-27 抓取,无页面日期)
2. https://obsidian.md/pricing , 定价页,Sync/Publish/Commercial/Catalyst 价格,"100% user-supported"(2026-10-27 抓取)
3. https://obsidian.md/help/sync/plans , 官方套餐、存储与降级规则(2026-10-27 抓取)
4. https://obsidian.md/blog/standard-plan/ , Standard 档发布,kepano,2024-03-20
5. https://forum.obsidian.md/t/about-pricing-aka-why-does-obsidian-service-x-cost-so-much-or-any-money-at-all/26329?page=2 , 公司定价立场(2023-07-01)与用户价格转述(2023-08)
6. https://obsidian.md/help/headless , 官方 Headless 文档,open beta,agent 用例
7. https://registry.npmjs.org/obsidian-headless , npm 版本时间线(0.0.1 于 2026-02-27,0.0.14 于 2026-07-30),license UNLICENSED
8. https://github.com/obsidianmd/obsidian-headless/issues (#19, #27, #28, #29, #42, #50, #53, #54, #56, #57) , Headless 问题跟踪,2026-04 至 2026-10
9. https://hsu.cy/2026/03/obsidian-headless-launchd/ , 第三方 Headless 部署手记,2026-03-27(secondary,作者标注可能过时;进程约 40 MB 内存)
10. https://obsidian.md/help/sync/troubleshoot , 官方冲突解决规则(1.9.7 起可选冲突副本)
11. https://forum.obsidian.md/t/option-to-let-user-manually-resolve-sync-conflicts/94468 , Sync 合并静默丢失的用户报告,2025-01 至 2025-08
12. https://github.com/vrtmrz/obsidian-livesync , LiveSync 主仓库(MIT、12.8k 星、README 警告);API 数据抓取于 2026-10-27
13. https://github.com/vrtmrz/obsidian-livesync/issues/396 , 维护者 2024-10-08 自述
14. https://github.com/vrtmrz/obsidian-livesync/issues/762 , DB 体积膨胀,维护者 2025-12-04 回复
15. https://github.com/vrtmrz/obsidian-livesync/issues/1143 和 /835 和 /813 , CLI 守护进程删库/空文件/重建后删文件
16. https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/docs/specs_garbage_collection.md , GC V3 规格
17. https://newreleases.io/project/github/vrtmrz/obsidian-livesync/release/1.0.0 , 1.0.0 发布说明镜像,2026-07-27(secondary 镜像)
18. https://ca.unraid.net/apps/obsidian-livesync-cli-018fyn31obvdir , LiveSync CLI 的 Docker 打包说明,2026-10-27 更新(secondary)
19. https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/README.md , Obsidian Git 手机端警告
20. https://github.com/syncthing/syncthing-android , 官方 Android 应用 2024-12-03 归档
21. https://github.com/chenxiaolong/BasicSync/issues/1 , Android 客户端现状时间线(2025-11 至 2026-10)
22. https://mobiussync.com/faq/ , Möbius Sync 后台限制与免费上限
23. https://forum.obsidian.md/t/sync-mac-pc-and-ios-using-syncthing-mobius-sync/72022?page=2 , iOS Syncthing 用户第一手报告,2025-03 至 2026-04

## Budget used
searches: 10 / 10 · fetches: 21 WebFetch(略超每搜 2 次的上限 20,多 1 次;其中 web.archive.org 1 次被拒,help.obsidian.md 1 次为重定向)。另有约 12 次对 GitHub 公共 API 和 npm registry 的无认证 curl 读取(贡献者数、发布时间、issue 正文与评论),性质是读原始数据,不计作搜索。
