# 邀请推荐模块 · 产品需求文档（PRD）

**Body Park Atom · Referral** · v2.0 · 2026-09-03 · 状态：待评审

> 中文在前，[English version](#referral-module--product-requirements-document) 在后，结构一一对应。
> 配套文件：`Demo-邀请全链路交互.html`（全部界面，可点走通，界面编号与本文一致）。
> 本目录只有这两个文件；改需求改本文，改界面改 Demo。

---

## 0. 一页纸：已决策

| 项 | 决定 |
|---|---|
| 北极星 | **可归因的主机订单数**。不记录点击。 |
| 落点 | 电商购买页（中国版 微信小程序商城 / 国际版 bodypark.com），**不是应用商店**。落地页无任何应用商店跳转。 |
| 归因 | 两条确定性来源相加：**订单带 token**、**激活时填码**；7 天内可补填一次。不做安装归因 SDK、联盟链接、概率匹配。 |
| 分享形式 | 只有两种：**邀请图（带二维码）**、**直接 URL（H5）**。邀请码印在图上、显示在落地页上，不是第三种形式。 |
| 邀请页 | **只有一个 CTA**。顺序：利益点 + 码 → 怎么做 → 邀请好友 → 邀请结果（注册 App / 购买 Atom 两个数 + 我的权益 + 最近动态）。 |
| 好友权益 | **−¥50 / $10** 买主机（无条件，官网可叠加；注册 App 即存入账户，90 天）+ **1 个月 PRO**（激活填码）。可叠加。 |
| 邀请人权益 | 每位成功邀请：**¥50 / $10 抵扣金**（主机或配件，90 天）+ **1 个月 PRO**，按次累计不封顶。好友仅注册**只计数不发奖**。 |
| 两段漏斗 | 注册 App（计数）→ 购买 Atom 并激活（发奖）。 |
| 版本 × 语言 | 版本决定做什么（金额、成交场、去处、规则），语言决定说什么。正交。版本按 App Store 区 / 账号归属地，不按 IP。 |
| 设备端 | 466×466 圆屏只做"入口 → 二维码 → 反馈"。内容落在内接正方形 330×330 内，二维码 ≥ 220px。 |
| 用词 | 叫「抵扣金」不叫「现金」。PRO 月必须标注价值。 |

**待拍板（四件）**：① 小程序商城 / bodypark.com 能否在订单上带 token 字段（电商 / 运营）② 各市场金额与 PRO 标注价值，本文 ¥50 / $10、¥30 / $4.99 为占位（运营 / 财务）③ 466 圆屏能否显示动态二维码（硬件）④ 抵扣金的会计与税务口径（法务）。

---

## 1. 背景与目标

Atom 是放在家里的力量训练设备，主机 **$239–299（≈ ¥1,700–2,150）**，购买决策强依赖熟人推荐。现有分享模块已能把训练成果做成图片和链接。邀请推荐是这套分享能力上的一层**薄挂载**：把"推荐"从口头变成可归因、可奖励的动作。它不是新模块——不新增载体族、不新增自由度层级，只在既有五层模型里各加一点（见 §14）。

| | 内容 |
|---|---|
| 业务目标 | **可归因的主机订单数**（北极星）。不看点击。 |
| 邀请人目标 | 一个按钮发出去；随时看到朋友注册 / 购买了几个、自己拿到了什么。 |
| 好友目标 | 优惠自动生效，不用研究规则。 |
| 首季指标 | 邀请页 CTA 点击率 ≥ 30%（进入页面的人）· 带码注册 / 带码订单比例 · 邀请带来的订单占主机订单 ≥ 8% · 每单推荐成本 ≤ 客单价 12% |

---

## 2. 范围

**本期做**
- App 邀请页（单 CTA）、分享面板、邀请图模板 T28
- H5 落地页（认人 / 认版本 / 透传 token）
- 好友：结算自动抵扣、注册存抵扣金、激活填码得 PRO
- 邀请人：抵扣金 + PRO 账本、明细、权益、推送
- Atom 设备端：邀请二维码、课后"分享到手机"二维码
- 中国版 / 国际版两套配置，中英双语

**本期不做**
- 现金返利、提现
- 点击统计、安装归因 SDK、平台联盟链接（淘宝客 / 京东联盟 / Amazon Attribution）
- 多级分销、KOC 后台
- 第三方电商（天猫 / 京东 / Amazon）的自动抵扣——只提供输码

---

## 3. 三条基础判断

这三条决定了后面所有结构；不认同其中任何一条，方案要重来。

**A · 落到电商，归因就不再靠猜。** 跳应用商店的链路里，iOS 没有官方的按人延迟深链、微信屏蔽 `itms-apps`、国内安卓没有统一商店与 Install Referrer——只能做概率匹配。改成落到**购买页**后，归因点从"安装时刻"移到"**下单时刻**"：订单一定有号、一定能带码、一定进账本。整条链路每一层都是确定性的。电商优先还顺手绕过了微信屏蔽应用商店的问题。

**B · H5 落地页是唯一的变化点。** 分享物（图片、短链）全球是同一份；地区、环境、目标的差异全部由落地页在运行时吸收。App 端和 Atom 设备端**不需要写任何地区逻辑**，只渲染一个 token。国际化 = 多配几份 Profile，不是多做几套分享 UI。

**C · 一个码，两个时刻。** 邀请码在**结算时是折扣**（促成交），在**首次激活时是凭证**（做归因）。同一个码复用两次——所以即使在天猫 / 京东 / Amazon 这类归因黑洞里成交，激活那一刻也能把关系补回来。这是电商链路能兜底的根本原因。

---

## 4. 用户与故事

| 角色 | 故事 | 验收 |
|---|---|---|
| **邀请人**（已激活 Atom） | 练完一节课想发给朋友看，顺手把主机推荐出去；一周后想知道朋友买了没、自己拿到了什么。 | 从入口到发出 ≤ 3 次点击；邀请页两个数字与权益在事件后 ≤ 5 秒更新 |
| **好友** | 收到图或链接，看到优惠已经生效；要么直接买，要么先注册把钱存起来；到货激活时填码拿 PRO。 | 落地页无需登录即显示优惠；结算页显示已抵扣；激活填码后 PRO ≤ 3 秒到账 |
| **运营** | 改金额、改渠道、上线新市场，不发版。 | 所有版本参数与文案在服务端配置下发 |

---

## 5. 权益与漏斗

### 5.1 结构：两侧各两样，全部可叠加

每一侧都是「一笔小钱 + 一个月 PRO」：钱让人填码，PRO 是全球都能无条件发的底座。永远不给现金。

| 谁 | 内容 | 规则 | 触发 |
|---|---|---|---|
| **好友** | **−¥50 / $10** 买主机 | 无条件；官网可与促销叠加；第三方渠道结算输码。注册 App 即存入账户，限主机，90 天有效，到期前 7 天提醒一次。同一账号一次。 | 结算自动抵扣，或注册入账 |
| | **1 个月 PRO**（标注价值 ¥30 / $4.99） | 与立减叠加。 | 激活时填码，即时到账 |
| **邀请人** | **¥50 / $10 抵扣金** | 主机或配件可用，90 天有效，按次累计不封顶；权益页显示"累计 ¥150 / $30 可换一件配件"。 | 好友**购买 + 激活**之后 |
| | **1 个月 PRO** / 位 | 按次叠加不封顶；服务端权益延期，不走商店 offer code。 | 同上。好友**仅注册只计数不发奖** |

### 5.2 两段漏斗，各在哪一屏发生

| 时点 | 界面 | 好友得到 | 邀请人看到 | 归因 |
|---|---|---|---|---|
| 打开落地页 | B1 → B2 | 看到 −¥50 / $10 已生效 + 填码得 1 个月 PRO | —（**不记录点击**） | 落地页只透传，不计数 |
| 注册 App（先不买） | B5 | 抵扣金入账，90 天内买主机可用 | **注册 App +1**，不发奖 | token 绑定账号（防假号：只计数） |
| 下单 | B3 → B4 | −¥50 / $10 在订单里抵扣 | "待激活" | 订单带 token；第三方靠码 |
| 激活并填码 | B6 → B7 | **1 个月 PRO 即时到账** | **购买 Atom +1**；抵扣金 + 1 个月 PRO 到账；推送 A9 | 激活填码 = 全渠道兜底 |
| 退货 | — | PRO 收回 | 抵扣金与 PRO 收回，动态留痕 | — |

### 5.3 力度判断

- 好友侧 ¥50 / $10 占客单价 3–4%：**够让人填码，不是购买理由**。落地页 hero 讲的是"优惠已自动生效"，不是折扣力度。
- 每成功推荐一台总成本约 $20 真实 / $25 名义（两笔抵扣金 + PRO 月对付费用户的递延），**占客单价 8% 左右**；整包控制在 10–12% 内。
- 同一个 $10，在好友侧是象征，在邀请人侧是一件配件的 1/6 到 2/3——这是持续邀请的真实动力。
- 若要给好友侧更强的转化拉力，硬件行业惯例是**送配件而不是送钱**（感知价值是成本的数倍）；在 $249 的价位上配件与 $10 二选一，不叠。

### 5.4 结算与账本

- 好友的 PRO 在**激活填码那一刻**发（它本身就是填码的激励）。
- 邀请人的奖励在好友**确认收货 + 完成激活**之后发——硬件退货率不为零，提前发奖是套利入口。
- 账本状态：`attributed`（已归因）→ `qualified`（收货 + 激活）→ `settled`（已发奖）→ `reversed`（退货）。

### 5.5 反薅与用词

- 邀请人奖励**只在好友购买 + 激活后触发**，注册不触发——假号无利可图。好友侧抵扣金只能抵主机，天然自限。
- 同设备指纹 / 同支付账号 / 同收货地址高频 → 转人工审核；异常速率**挂起而非拒绝**，避免误伤真实 KOC；邀请人需已激活设备且有真实训练记录。
- 叫「抵扣金」不叫「现金」：只能店内用、有有效期，避开个税与资质，不在账上堆成无期限负债。

---

## 6. 版本与语言

**版本决定做什么，语言决定说什么**，两者正交，不能合成"中文 = 中国版"。版本由 App Store 区 / 账号归属地判定，不用 IP（出差和 VPN 会把判定打歪）；语言跟随系统，可手动改。版本配置里的字符串自带语言键（`tier: {zh, en}`），所以**加一门语言 = 加一列，加一个市场 = 加一份配置**，不新增页面。设计稿按英文最长版定容器高度（英文比中文长 30–50%）。

| 参数 | 中国版 CN | 国际版 GLOBAL | 归谁管 |
|---|---|---|---|
| 好友立减 / 抵扣金 | ¥50 | $10（EUR / GBP 同额本币） | 版本 |
| 邀请人抵扣金 | ¥50 | $10 | 版本 |
| PRO 月标注价值 | ¥30 | $4.99 | 版本 |
| 主成交场 | 微信小程序商城 | bodypark.com（Shopify） | 版本 |
| 第三方渠道（输码） | 天猫 / 京东 | Amazon | 版本 |
| 分享去处 · 图片 | 相册 / 微信好友 / 朋友圈 / 小红书 | Save / Instagram / WhatsApp / Messages | 版本 |
| 分享去处 · 链接 | 复制 / 微信好友 / 更多 | Copy / Messages / WhatsApp / More | 版本 |
| 默认形式（面板顺序） | 图片在上（朋友圈 / 群图片传播强） | 链接在上（iMessage / WhatsApp 对链接友好） | 版本 |
| 规则附加条款 | 权益非现金，不开发票 | 见 bodypark.com/terms | 版本 |
| 页面所有文案 | 字符串表；金额 / 天数 / 昵称作为参数注入 | 同左 | 语言 |
| 昵称脱敏 | `Lin**` | `Lin W.` | 语言 |
| 数字与日期 | 09-01 · 30 天 · ¥1,799 | Sep 1 · 30 days · $249 | 语言 |

**Profile 注入五样东西**：成交场、落地页形态、归因优先级、奖励形态、合规文案。内核（token 身份、归因账本、奖励引擎、降级链抽象）全球唯一。

**中国版三条特殊规则**：① 微信内不出现任何应用商店跳转（电商优先已天然满足）；② 小程序商城如能上，它同时解决成交与归因（openid 归因近 100%，微信内传播衰减远小于 H5），**应作为国内主路而非降级路**；③ 安卓渠道包只能做渠道级、做不到人级归因，不要指望它替代激活填码。

---

## 7. 分享形式

只有两种。邀请码**不是第三种形式**——它印在图片上、显示在落地页上，是两种形式内部的一个字段。用户心智里只有"发张图"和"发个链接"。

### 7.1 图片（带二维码），三个变体

| 变体 | 来源 | 说明 |
|---|---|---|
| **A · 内容图挂载** ★主路径 | 任意 27 个分享模板 | G1 水印二维码里本来就该带 token。用户在分享训练成果，邀请是免费搭车的副产品——量最大、零额外动作、零新增设计 |
| **B · 专用邀请卡** | "邀请好友"入口 | 模板 **T28**，3:4 竖版：G3 身份条 + 产品图 + 利益点 + G4 明文码 + G1 大二维码 |
| **C · 设备屏版** | Atom 圆屏 | 1:1 超大二维码。**设备端图片是唯一可能的形式**——没有浏览器、分享面板、键盘，只能把码打到屏上让朋友当场扫。短链以明文并列供手输，是图片的降级不是独立形式 |

### 7.2 直接 URL（H5 落地页）

短链 `bp.fit/i/7K2A`。复制、发微信、发 iMessage 都是同一串。落地页是整个方案的**路由器**，必须做六件事：

1. **认人**：token → 邀请人昵称 / 头像 / 训练凭证（聚合数），做社交证明。
2. **认环境**：微信内 / 系统浏览器 / 桌面，决定 CTA 形态与是否可唤起小程序。
3. **认版本**：加载对应 Profile；用 App Store 区 / 店铺归属判定，不用 IP。
4. **透传 token**：下一跳是小程序、独立站还是别的，token 必须活着传下去。
5. **始终显示明文码**：链路里任何一跳断了，用户手上还有这个码。
6. **富媒体卡片**：配 OG / 微信 JS-SDK 的标题、描述、缩略图，链接在聊天里渲染成卡片。这是同一个 URL 的渠道渲染，不算第三种形式。

| 端 | 图片（带二维码） | 直接 URL |
|---|---|---|
| 手机 App | ✅ 存图 / 朋友圈 / 群 | ✅ 复制 / 微信 / iMessage |
| Atom 设备 | ✅ 屏幕直出二维码 | ✗ 无分享能力（短链明文供手输） |

### 7.3 Token 与链接结构

```
短链    https://bp.fit/i/7K2A?s=post&c=wx
明文码  ALEX-7K2A
二维码  编码同一条短链
```

- `7K2A` = 邀请人 token，永久绑定，**唯一被解析的部分**。Base32 去歧义字母表（无 0 / O / 1 / I / L），4–6 位起步，随机不自增。
- `ALEX-` 前缀纯装饰，便于人念人记；服务端只取后缀，改昵称不影响归因。
- `s`（场景）`c`（渠道）**仅用于分析，永不参与归因**。

**为什么参数必须可丢**：图片会被截图转发、二维码会被翻拍、短链会被手抄。把归因押在 token 上、分析押在参数上，意味着一张图转发十手之后归因依然正确，只是渠道标签失真——可接受。推论：**不做一次性链接、不做有效期链接**（活动券除外），邀请关系是长期资产。

---

## 8. 功能需求

### FR-1 · 邀请 token 与码 · P0
每个账号一个永久 token（§7.3）。对外三种呈现共用一个 token。
**验收**：截图转发、翻拍二维码、手抄短链三种情况下归因仍正确。

### FR-2 · 邀请页 · P0
入口：「我的」页 banner、课后报告底部、推送。自上而下：利益点 + 邀请码 → 怎么做（三步）→ **唯一 CTA** → 邀请结果（注册 App / 购买 Atom 两个数 + 我的权益 + 最近动态，同一区块）。
- 邀请码可见但不是按钮；两格与「规则」是导航。
- 不显示点击数。
- 未激活设备的账号：页面可见，CTA 置灰并说明"激活 Atom 后可邀请"。
**验收**：页面只有一个可点的主按钮；数字与动态在事件后 ≤ 5 秒更新。

### FR-3 · 分享面板与两种形式 · P0
CTA 拉起面板，两组：**邀请图**（T28）与**链接**（H5，带卡片元数据）。每组一排去处，按版本配置；每个去处都是终点。邀请图去处点击后进预览页，可发送 / 保存。现有 27 个分享模板的 G1 水印二维码一律带 token。
**验收**：中国版图片组在上，国际版链接组在上；面板内完成分享后回到邀请页并 toast。

### FR-4 · H5 落地页 · P0
按 §7.2 六件事。主 CTA 购买（中国版唤起小程序商城；国际版 bodypark.com，URL 带 ref），次 CTA「先注册 App 把 ¥50 / $10 存起来」，底部第三方渠道输码说明。**整页没有应用商店跳转。**
- token 无效或邀请人不满足资格：仍显示产品页，不显示优惠，不报错。
- 明文码始终可见。
**验收**：首屏 ≤ 1.5 s（4G）；微信内可直接唤起小程序。

### FR-5 · 好友：结算抵扣与注册存抵扣金 · P0
自有商城结算页显示「邀请优惠 −¥50 / $10」行与已应用的码，订单落库写 `referral_token`。带码注册 App 的账号，抵扣金入账，限主机、90 天有效，到期前 7 天推一次。
- 同一账号只能享受一次好友优惠。
- 抵扣金与结算自动抵扣是同一权益，不重复。
**验收**：结算行、订单字段、账户余额三处一致。

### FR-6 · 激活填码 · P0
设备配网成功后、首次训练前，一个可跳过的步骤：「有朋友的邀请码吗？」链接 / 注册来的码预填。填码即时发 1 个月 PRO 给好友；同时给邀请人发抵扣金 + PRO 并推送（如订单未确认收货则挂起到收货）。
- 激活后 7 天内可在 App 内补填（一次）。
- 自己的码、已用过的账号、邀请人未激活设备：提示原因，不发奖。
**验收**：填码到 PRO 到账 ≤ 3 s；邀请人推送 ≤ 1 min。

### FR-7 · 邀请明细与我的权益 · P1
明细：两个总数；按人列出注册之后的每一位（已注册 / 待激活 / 已到账）；按来源（邀请图 / 链接 / 训练图二维码 / 设备扫码）。权益：抵扣金余额与到期、PRO 月数与到期、已获得列表、「累计 ¥150 / $30 可换一件配件」进度。
**验收**：昵称按语言脱敏；纯注册标"仅计数"。

### FR-8 · 推送 · P1
邀请人：好友注册、好友下单、好友激活（权益到账）、抵扣金 7 天后过期。好友：抵扣金 7 天后过期。全部直达邀请页或权益页。

### FR-9 · Atom 设备端（466×466 圆屏）· P1
菜单「邀请好友」→ 二维码屏（≥ 220px，明文码 + 短链）；课后总结「分享到手机」→ 二维码，手机扫码打开这次训练的分享页（其水印二维码本来就带邀请码）。内容落在内接正方形 330×330 内（466 / √2），四角不放东西；一屏只放一件事；字号 ≥ 15px（466 尺度）。设备按当前登录用户生成码；若只能显示静态图，降级为设备渠道码。

### FR-10 · 配置下发与多语言 · P0
§6 的全部参数与规则文案由服务端按版本下发；所有界面文案走字符串表，金额 / 天数 / 昵称作为参数注入。

---

## 9. 界面清单

编号与 Demo 一致。要素、去向、优先级在 Demo 右侧面板与底部清单表里。

| 泳道 | 界面 |
|---|---|
| **邀请人手机** | A1 入口 · A2 邀请页（单 CTA）· A3 分享面板 · A4 邀请图预览（T28）· A6 邀请明细 · A7 我的权益 · A8 规则 · A9 推送 |
| **好友手机** | B1 收到消息 · B2 H5 落地页 · B3 结算 · B4 下单成功 · B5 注册（先不买）· B5s 抵扣金已入账 · B6 激活填码 · B7 激活完成权益到账 |
| **Atom 设备** | C1 菜单 · C2 邀请二维码 · C3 课后总结 · C4 分享到手机 · C5 扫码反馈 |

跨泳道跳转：A4 → 好友收到 B1；B7 → 邀请人推送 A9；C2 → 好友扫码 B2；C4 → 手机分享模块。

---

## 10. 归因规则

业务只需要一个数：通过邀请带来的主机订单。两条来源相加，全部确定性。

| 优先级 | 归因点 | 说明 |
|---|---|---|
| 1 | **订单带 token**（`order.referral_token`） | 自有商城（小程序 openid + 订单字段 / Shopify cart attribute）。100% 确定，无需用户动作。 |
| 2 | **激活时填码**（`activation.referral_code`） | 与在哪买的无关，覆盖天猫 / 京东 / Amazon / 线下 / 转送。100% 确定。**唯一覆盖全渠道的一层。** |
| 3 | **7 天内补填** | 同一账号一次。 |
| — | ~~点击 / 安装归因 / IDFA 概率匹配 / 联盟链接~~ | 不做。App 下载作为次要目标时 Android 可用 Play Install Referrer，iOS 直接走激活填码。 |

- **一个订单只归一个邀请人**：先到先得；订单 token 与激活码冲突时以订单 token 为准并记录冲突。
- 因为激活填码覆盖全渠道且 100% 确定，**不必强求订单 token 那条漏斗完美**。订单 token 优化成交转化，激活填码保证关系记账——两件事分开算 KPI。
- 参考：完整五级阶梯（L0 订单 token / L1 优惠码结算 / L2 平台联盟 / L3 激活填码 / L4 补填）曾评估过，P0 只做 L0 + L3 + L4；L1 依赖平台对自定义券码的限制，L2 只到渠道级不到人级，均不作为发奖依据。

---

## 11. 数据与事件

**实体**
- `referral_token`：user_id, token, created_at
- `referral_ledger`：inviter_id, invitee_id, source (image / link / workout_qr / device), stage (signed_up / ordered / activated), order_id, device_id, state, timestamps
- `reward`：user_id, kind (credit / pro_month), amount, currency, expires_at, ledger_id, state
- `edition_config`：edition, amounts, storefronts, destinations, strings{zh, en}

**事件**
- `invite_page_view`, `invite_cta_tap`, `share_complete`{form, dest}
- `landing_view`{token, env, edition} — 只记事件，不做点击统计展示
- `signup_with_token`, `order_with_token`, `activation_code_entered`{prefilled}, `activation_code_skipped`
- `reward_granted`, `reward_reversed`, `credit_redeemed`, `credit_expired`

**看板**：邀请带来的订单数 / 占比（北极星）· 分享率、带码注册率、注册 → 购买转化 · 每单成本、抵扣金核销率、PRO 递延 · 按来源 / 版本 / 语言拆分。

---

## 12. 边界与异常

| 情况 | 处理 |
|---|---|
| 自己填自己的码 | 提示"这是你自己的邀请码"，不发奖 |
| 好友退货 | 双方权益 `reversed`；已用掉的抵扣金不追回，未用的作废；PRO 剩余天数扣除 |
| 邀请人设备未激活 / 账号封禁 | 落地页照常显示产品，不显示优惠；码无效 |
| 好友已是老用户 | 已有激活设备的账号不能作为被邀请人；未激活的可以 |
| 两个码 / 换码 | 先绑定的生效；激活前可在 App 里改一次 |
| 版本不匹配（中国版账号打开国际版链接） | 按**好友账号**的版本发权益，金额取该版本；邀请人按自己版本得奖 |
| 抵扣金到期 | 到期前 7 天推一次；到期作废，明细留痕 |
| 刷单 | 同设备指纹 / 同支付账号 / 同收货地址高频 → 人工审核；异常速率挂起而非拒绝；邀请人需有真实训练记录 |
| token 无效链接被打开 | 当普通产品页处理，不报错 |
| 设备只能显示静态图 | 设备端邀请降级为设备渠道码，不归到人 |

---

## 13. 非功能需求

- **隐私**：好友昵称按语言脱敏，头像不展示给邀请人；落地页展示的邀请人训练凭证只用聚合数；中国版数据境内存储。
- **性能**：落地页首屏 ≤ 1.5 s（4G）；二维码本地生成；邀请图渲染 ≤ 1 s（走 ShareKit 现有管线）。
- **安全**：发奖只在服务端触发，客户端不可请求发奖；token 随机不可枚举；PRO 天数走服务端权益延期，不走商店 offer code。

---

## 14. 接入现有分享架构

| 层 | 改动 | 说明 |
|---|---|---|
| ① 分享体 | 新增 `E12 · 推荐邀请`（仅 R1） | 只为让邀请卡在矩阵里有位置 |
| ② 原子 | G 族 2 → 4 个 | `G1` 二维码水印注入 token（改造，27 个模板受益）· `G2` App 下载入口 → **购买入口** · `G3` 邀请人身份条 🆕 · `G4` 明文码条 🆕 |
| ③ 组装 | 新增 `T28 邀请卡`（3:4 手机版 / 1:1 设备版） | 模板注册表加两条 JSON；其余 27 个模板不改结构 |
| ④ 载体 | **不新增** | 只用既有的 ①图片 PNG 与 ③H5 |
| ⑤ 链路 | 新增入口：邀请好友、设备屏邀请 | 入口即分享体绑定规则不变 |
| ShareKit | `ReferralProvider`（DataProvider 层）+ `RegionProfile`（Composition 层注入） | 归因账本、奖励引擎是**后端服务**，不进 ShareKit；ShareKit 只负责"把 token 渲染进图 / 链接" |

---

## 15. 里程碑

| 阶段 | 范围 | 依赖 |
|---|---|---|
| **P0** | FR-1 / 2 / 3 / 4 / 5 / 6 / 10：token、邀请页、分享面板 + T28、落地页、结算抵扣、注册存抵扣金、激活填码、配置下发。两版两语言一起上。 | 小程序商城 / bodypark.com 接 token 字段；激活向导加一步 |
| **P1** | FR-7 / 8 / 9：明细、权益页、推送、设备端二维码 | 设备端能否显示动态二维码 |
| **P2** | 配件兑换、阶梯活动、按市场调整金额的 A/B | — |

**P0 建议只做"内容图挂载 + 落地页"起步**：G1 改造几乎零成本、量最大；专用邀请卡与设备端放 P1 也可接受。

---

## 16. 待定

| # | 谁定 | 问题 | 影响 |
|---|---|---|---|
| 1 | 电商 / 运营 | 小程序商城 / bodypark.com 能否在订单上带 token 字段？ | 决定归因第 1 层是否成立；不成立则全靠激活填码，落地页主 CTA 形态随之变 |
| 2 | 运营 / 财务 | 各市场金额与 PRO 标注价值 | 本文 ¥50 / $10、¥30 / $4.99 为占位；欧洲、日本等市场同额本币还是按购买力调整 |
| 3 | 硬件 | 466 圆屏能否显示动态二维码？ | 不能则设备端邀请只能归到设备渠道，不能归到人 |
| 4 | 法务 | 抵扣金的会计与税务口径 | 中国版：非现金、不开票、90 天有效；国际版：terms 条款 |
| 5 | 运营 / 法务 | 天猫 / 京东 / Amazon 能否挂自定义优惠码、能否回传核销明细 | 只影响第三方渠道的成交体验，不影响归因（激活填码兜底） |

---

## 附 · 决策记录

| 日期 | 决定 |
|---|---|
| 09-03 | 落点改为电商购买页（优先硬件），不是应用商店；分享形式只有图片（带二维码）与 H5 两种 |
| 09-03 | 归因简化：业务只看"邀请带来的订单数"，用户看注册 App / 购买 Atom 两个数；不记录点击 |
| 09-03 | 邀请页单 CTA；顺序 利益点 → 怎么做 → CTA → 邀请结果 |
| 09-03 | 分中国版 / 国际版，中英双语；版本与语言正交 |
| 09-03 | 权益：好友 −¥50 / $10 + 1 个月 PRO；邀请人 ¥50 / $10 抵扣金 + 1 个月 PRO / 位；全部可叠加；仅注册不发奖 |
| 09-03 | 主机定价修正为 $239–299（此前文档误记为 ¥5,499 / $799） |
| 09-03 | 邀请推荐独立成 `referral/` 目录；PRD 与设计文档合并为本文（Markdown），界面统一在 Demo |

---
---

# Referral Module · Product Requirements Document

**Body Park Atom · Referral** · v2.0 · 2026-09-03 · Status: for review

> English version. Structure mirrors the Chinese version above section by section.
> Companion file: `Demo-邀请全链路交互.html` (every screen, clickable end to end; screen IDs match this document).
> This folder holds only these two files: requirements live here, screens live in the Demo.

---

## 0. One page: decisions made

| Item | Decision |
|---|---|
| North star | **Attributable device orders.** Clicks are not tracked. |
| Destination | The purchase page (CN: WeChat mini-store / GLOBAL: bodypark.com), **not an app store**. The landing page never jumps to an app store. |
| Attribution | Two deterministic sources added together: **order carries token**, **code entered at activation**; one backfill within 7 days. No install-attribution SDK, no affiliate links, no probabilistic matching. |
| Share forms | Exactly two: **invite image (with QR)** and **direct URL (H5)**. The code is printed on the image and shown on the landing page; it is not a third form. |
| Invite page | **One CTA only.** Order: benefit + code → how it works → Invite friends → results (sign-ups / purchases counters + my rewards + recent activity). |
| Friend rewards | **−¥50 / $10** on the device (unconditional, stacks with promos on our store; banked on sign-up for 90 days) + **1 month Pro** (code at activation). Both stack. |
| Inviter rewards | Per successful invite: **¥50 / $10 credit** (device or accessories, 90 days) + **1 month Pro**, accumulating without cap. A friend who only signs up **counts but earns nothing**. |
| Two-stage funnel | Sign up (counted) → buy Atom and activate (rewarded). |
| Edition × language | Edition decides what the page does (amounts, storefront, destinations, rules); language decides what it says. Orthogonal. Edition from App Store region / account home, never IP. |
| Device | The 466×466 round screen does only "entry → QR → feedback". Content stays inside the inscribed 330×330 square; QR ≥ 220 px. |
| Wording | "Credit", never "cash". The Pro month always shows its value. |

**Open decisions (four)**: ① Can the mini-store / bodypark.com carry a token field on the order (e-commerce / ops)? ② Per-market amounts and the Pro value shown — ¥50 / $10 and ¥30 / $4.99 here are placeholders (ops / finance). ③ Can the 466 round screen render a dynamic QR (hardware)? ④ Accounting and tax treatment of credit (legal).

---

## 1. Background & Goals

Atom is a home strength device priced at **$239–299 (≈ ¥1,700–2,150)**; purchase decisions lean heavily on word of mouth. The existing sharing module already turns workouts into images and links. Referral is a **thin layer** on that capability: it turns a recommendation into an attributable, rewardable action. It is not a new module — no new carrier family, no new freedom tier, only small additions to the existing five-layer model (§14).

| | |
|---|---|
| Business goal | **Attributable device orders** (north star). Clicks are irrelevant. |
| Inviter goal | One tap to send; always see how many friends signed up / bought and what they earned. |
| Friend goal | The discount just applies; no rules to study. |
| First-quarter metrics | Invite page CTA rate ≥ 30% of visitors · share of sign-ups / orders carrying a code · referred orders ≥ 8% of device orders · cost per referred order ≤ 12% of ticket |

---

## 2. Scope

**In scope**
- In-app invite page (single CTA), share sheet, invite image template T28
- H5 landing page (identifies the inviter and edition, passes the token)
- Friend: automatic discount at checkout, credit banked on sign-up, Pro on code entry at activation
- Inviter: credit + Pro ledger, details, rewards, push
- Atom device: invite QR, post-workout "share to phone" QR
- CN / GLOBAL edition configs, zh / en strings

**Out of scope**
- Cash rebates, withdrawals
- Click tracking, install-attribution SDKs, affiliate networks (Taobao Union / JD Union / Amazon Attribution)
- Multi-level referral, creator back-office
- Automatic discounts on third-party stores (Tmall / JD / Amazon) — code entry only

---

## 3. Three founding judgments

These decide everything that follows; reject any one and the design must be redone.

**A · Landing on e-commerce makes attribution deterministic.** Through an app store, iOS has no official per-user deferred deep link, WeChat blocks `itms-apps`, and China Android has no unified store or Install Referrer — only probabilistic matching remains. Landing on the **purchase page** moves the attribution point from install time to **order time**: an order always has an id, always accepts a code, always lands in a ledger. Every layer becomes deterministic. It also sidesteps WeChat's app-store block entirely.

**B · The H5 landing page is the single point of variation.** The share artifacts (image, short link) are identical worldwide; region, environment and goal differences are absorbed by the landing page at runtime. The app and the Atom device carry **no region logic** — they render one token. Internationalization means more profiles, not more share UIs.

**C · One code, two moments.** The invite code is a **discount at checkout** (drives conversion) and a **credential at first activation** (drives attribution). The same code is used twice, so even a purchase inside an attribution black hole like Tmall / JD / Amazon is recovered at activation. This is why the e-commerce path has a floor.

---

## 4. Users & Stories

| Role | Story | Accepted when |
|---|---|---|
| **Inviter** (activated Atom) | Finishes a workout, wants to show a friend, recommends the device in passing; a week later wants to know whether the friend bought and what they earned. | Entry to send in ≤ 3 taps; the two counters and rewards update ≤ 5 s after an event |
| **Friend** | Receives an image or link, sees the discount already applied; buys now or signs up to bank the credit; enters the code at activation for Pro. | Landing page shows the discount without login; checkout shows it applied; Pro lands ≤ 3 s after code entry |
| **Ops** | Change amounts, channels, launch a market without an app release. | All edition parameters and strings are server-delivered config |

---

## 5. Rewards & Funnel

### 5.1 Structure: two items per side, all stackable

Each side gets "a small amount of money + a month of Pro": the money gets the code entered, Pro is the base that can be granted unconditionally worldwide. Never cash.

| Who | Item | Rule | Trigger |
|---|---|---|---|
| **Friend** | **−¥50 / $10** on the device | Unconditional; stacks with promos on our store; code entry on third-party stores. Banked on sign-up, device only, 90 days, one reminder 7 days before expiry. Once per account. | Auto-applied at checkout, or banked on sign-up |
| | **1 month Pro** (value shown: ¥30 / $4.99) | Stacks with the discount. | Code at activation, instant |
| **Inviter** | **¥50 / $10 credit** | Device or accessories, 90 days, accumulates per invite without cap; rewards page shows "¥150 / $30 gets you an accessory". | After the friend **buys + activates** |
| | **1 month Pro** per friend | Stacks without cap; server-side entitlement extension, not store offer codes. | Same. A friend who **only signs up counts, no reward** |

### 5.2 Two-stage funnel, screen by screen

| Moment | Screen | Friend gets | Inviter sees | Attribution |
|---|---|---|---|---|
| Opens landing page | B1 → B2 | −¥50 / $10 applied + 1 month Pro with code | — (**clicks not tracked**) | Landing page passes the token, no counting |
| Signs up (not buying yet) | B5 | Credit banked, good for 90 days on a device | **Sign-ups +1**, no reward | Token bound to account (fake accounts only count) |
| Orders | B3 → B4 | −¥50 / $10 off the order | "Pending activation" | Order carries token; third party via code |
| Activates with code | B6 → B7 | **1 month Pro instantly** | **Purchases +1**; credit + 1 month Pro land; push A9 | Code at activation covers every channel |
| Return | — | Pro reversed | Credit and Pro reversed, shown in activity | — |

### 5.3 Sizing

- The friend-side ¥50 / $10 is 3–4% of ticket: **enough to get the code entered, not a reason to buy.** The landing hero says "discount already applied", not "big discount".
- Real cost per referred device ≈ $20 ($25 nominal: two credits + the deferred month for paying Pro users), **about 8% of ticket**; keep the whole package within 10–12%.
- The same $10 is a token for the friend and one-sixth to two-thirds of an accessory for the inviter — that asymmetry is the real engine of repeat invites.
- For stronger friend-side pull, hardware convention is **gift an accessory rather than money** (perceived value several times cost); at $249, choose accessory or $10, not both.

### 5.4 Settlement & ledger

- The friend's Pro lands **the moment the code is entered** (it is the incentive to enter it).
- The inviter's rewards land after the friend's **delivery is confirmed + device activated** — return rates are non-zero; early payout is an arbitrage hole.
- Ledger states: `attributed` → `qualified` (delivered + activated) → `settled` → `reversed` (returned).

### 5.5 Anti-fraud & wording

- Inviter rewards trigger **only after purchase + activation**, never on sign-up — fake accounts gain nothing. Friend-side credit is device-only, so it is self-limiting.
- Same device fingerprint / payment account / shipping address at volume → manual review; abnormal velocity **suspends rather than rejects**, sparing real advocates; inviters must have an activated device and real workout history.
- "Credit", never "cash": redeemable only in our store and expiring, so no tax withholding, no license issues, no open-ended liability.

---

## 6. Editions & Language

**Edition decides what the page does; language decides what it says.** They are orthogonal — never collapse "Chinese" into "China edition". Edition comes from App Store region / account home, never IP (travel and VPNs break IP). Language follows the system and can be changed. Edition config strings carry language keys (`tier: {zh, en}`), so **a new language is a column and a new market is a config file** — never a new page. Size layouts to the longest English strings (30–50% longer than Chinese).

| Parameter | China (CN) | Global | Owned by |
|---|---|---|---|
| Friend discount / credit | ¥50 | $10 (EUR / GBP same figure in local currency) | Edition |
| Inviter credit | ¥50 | $10 | Edition |
| Pro month value shown | ¥30 | $4.99 | Edition |
| Primary storefront | WeChat mini-store | bodypark.com (Shopify) | Edition |
| Third-party (code entry) | Tmall / JD | Amazon | Edition |
| Share targets · image | Photos / WeChat / Moments / RED | Save / Instagram / WhatsApp / Messages | Edition |
| Share targets · link | Copy / WeChat / More | Copy / Messages / WhatsApp / More | Edition |
| Default form (sheet order) | Image first (images travel better in groups / Moments) | Link first (iMessage / WhatsApp render links well) | Edition |
| Extra rule clause | Rewards are not cash; no invoice | Subject to bodypark.com/terms | Edition |
| All UI copy | String table; amounts / days / names injected as parameters | same | Language |
| Name masking | `Lin**` | `Lin W.` | Language |
| Numbers & dates | 09-01 · 30 天 · ¥1,799 | Sep 1 · 30 days · $249 | Language |

**A profile injects five things**: storefront, landing-page form, attribution order, reward form, compliance copy. The core (token identity, ledger, reward engine, fallback chain) is global.

**Three CN-specific rules**: ① no app-store jump inside WeChat (already satisfied by e-commerce-first); ② if the mini-store is available it solves conversion and attribution at once (openid attribution ≈ 100%, far less decay than H5 inside WeChat) and **should be the primary CN path, not a fallback**; ③ Android channel builds attribute to a channel, not a person — never a substitute for the activation code.

---

## 7. Share Forms

Exactly two. The code is **not a third form** — it is printed on the image and shown on the landing page, a field inside both. Users think "send a picture" or "send a link".

### 7.1 Image (with QR), three variants

| Variant | Source | Notes |
|---|---|---|
| **A · Content-image mount** ★ main path | Any of the 27 share templates | The G1 watermark QR should carry the token anyway. The user shares a workout; the invite rides along free — highest volume, zero extra action, zero new design |
| **B · Dedicated invite card** | "Invite friends" entry | Template **T28**, 3:4: G3 inviter strip + product + benefit + G4 plain code + large G1 QR |
| **C · Device screen** | Atom round screen | 1:1 oversized QR. **On the device, image is the only possible form** — no browser, share sheet or keyboard; it can only put the code on screen for a friend to scan. The short link sits alongside as text for manual entry: a degradation of the image, not a separate form |

### 7.2 Direct URL (H5 landing page)

Short link `bp.fit/i/7K2A`. Copy, WeChat, iMessage all carry the same string. The landing page is the **router** of the whole scheme and must do six things:

1. **Identify the inviter**: token → name / avatar / workout proof (aggregates), as social proof.
2. **Detect the environment**: in-WeChat / system browser / desktop, deciding CTA form and whether the mini-program can be opened.
3. **Detect the edition**: load the profile; decide by App Store region / store affiliation, never IP.
4. **Pass the token through**: whatever the next hop is, the token must survive.
5. **Always show the plain code**: if any hop breaks, the user still has the code.
6. **Rich card**: OG / WeChat JS-SDK title, description, thumbnail so the link renders as a card in chat. Channel rendering of the same URL, not a third form.

| Endpoint | Image (with QR) | Direct URL |
|---|---|---|
| Phone app | ✅ save / Moments / groups | ✅ copy / WeChat / iMessage |
| Atom device | ✅ QR straight on screen | ✗ no share capability (link shown as text for manual entry) |

### 7.3 Token & link structure

```
Short link  https://bp.fit/i/7K2A?s=post&c=wx
Plain code  ALEX-7K2A
QR          encodes the same short link
```

- `7K2A` = inviter token, permanent, **the only part that is parsed**. Base32 without ambiguous glyphs (0 / O / 1 / I / L), 4–6 chars, random, not sequential.
- `ALEX-` prefix is cosmetic; the server reads only the suffix, so renames never affect attribution.
- `s` (scene) and `c` (channel) are **analytics only and never part of attribution**.

**Why parameters must be droppable**: images get screenshotted and forwarded, QRs re-photographed, links hand-typed. Pinning attribution on the token and analytics on the parameters means an image forwarded ten times still attributes correctly; only the channel label drifts — acceptable. Corollary: **no one-time links, no expiring links** (campaign coupons excepted); the referral relationship is a long-term asset.

---

## 8. Functional Requirements

### FR-1 · Referral token & code · P0
One permanent token per account (§7.3). Three renderings share it.
**Accept**: attribution survives screenshot forwarding, re-photographed QR, hand-typed link.

### FR-2 · Invite page · P0
Entries: "Me" tab banner, bottom of the post-workout report, push. Top to bottom: benefit + code → how it works (3 steps) → **the single CTA** → results (sign-ups / purchases counters + my rewards + recent activity in one block).
- The code is visible but not a button; the counters and Rules are navigation.
- No click count.
- Accounts without an activated device: page visible, CTA disabled with "Activate your Atom to invite".
**Accept**: exactly one primary button; counters and activity update ≤ 5 s after an event.

### FR-3 · Share sheet & the two forms · P0
The CTA opens a sheet with two groups: **invite image** (T28) and **link** (H5 with card metadata). Each group lists destinations from edition config; every destination completes the action. Image destinations open a preview with send / save. All 27 existing share templates carry the token in their G1 watermark QR.
**Accept**: CN shows the image group first, GLOBAL the link group first; completing a share returns to the invite page with a toast.

### FR-4 · H5 landing page · P0
The six duties in §7.2. Primary CTA buys (CN opens the mini-store; GLOBAL bodypark.com with ref in the URL), secondary "sign up and bank ¥50 / $10", third-party code note at the bottom. **No app-store jump anywhere.**
- Invalid token or ineligible inviter: product page still renders, no discount, no error.
- Plain code always visible.
**Accept**: first paint ≤ 1.5 s on 4G; inside WeChat the mini-store opens directly.

### FR-5 · Friend: checkout discount & banked credit · P0
Own-store checkout shows a "Referral −¥50 / $10" line and the applied code; the order persists `referral_token`. Accounts that sign up with a code get the credit banked, device-only, 90 days, one reminder 7 days before expiry.
- One friend discount per account.
- Banked credit and checkout discount are the same benefit, never both.
**Accept**: checkout line, order field and account balance agree.

### FR-6 · Code at activation · P0
After pairing succeeds and before the first workout, one skippable step: "Got a friend's code?" Codes from the link / sign-up are prefilled. Entering it grants the friend 1 month Pro instantly and grants the inviter credit + Pro with a push (held until delivery is confirmed if not yet).
- Backfill allowed once within 7 days in the app.
- Own code, already-redeemed account, inviter without an activated device: explain, no reward.
**Accept**: code to Pro ≤ 3 s; inviter push ≤ 1 min.

### FR-7 · Invite details & My rewards · P1
Details: the two totals; every friend from sign-up on (signed up / pending activation / settled); by source (image / link / workout-share QR / device scan). Rewards: credit balance and expiry, Pro months and expiry, earned list, "¥150 / $30 gets you an accessory" progress.
**Accept**: names masked per language; sign-up-only rows say "counted only".

### FR-8 · Push · P1
Inviter: friend signed up, friend ordered, friend activated (rewards landed), credit expiring in 7 days. Friend: credit expiring in 7 days. All deep-link to the invite or rewards page.

### FR-9 · Atom device (466×466 round) · P1
Menu "Invite" → QR screen (≥ 220 px, plain code + link); post-workout "Share to phone" → QR that opens this workout's share page on the phone (its watermark QR already carries the invite code). Content stays inside the inscribed 330×330 square (466 / √2), nothing in the corners; one thing per screen; type ≥ 15 px at 466 scale. Codes are generated for the signed-in user; if only static images are possible, fall back to a device channel code.

### FR-10 · Server config & i18n · P0
Every parameter and rule clause in §6 is server-delivered per edition; all UI strings come from the string table with amounts / days / names injected as parameters.

---

## 9. Screens

IDs match the Demo. Elements, next screens and priority are in the Demo's side panel and inventory table.

| Lane | Screens |
|---|---|
| **Inviter phone** | A1 Entry · A2 Invite page (single CTA) · A3 Share sheet · A4 Invite image preview (T28) · A6 Invite details · A7 My rewards · A8 Rules · A9 Push |
| **Friend phone** | B1 Message received · B2 H5 landing · B3 Checkout · B4 Order placed · B5 Sign up (not buying yet) · B5s Credit banked · B6 Activation code · B7 Activated, rewards landed |
| **Atom device** | C1 Menu · C2 Invite QR · C3 Post-workout · C4 Share to phone · C5 Scan feedback |

Cross-lane jumps: A4 → friend receives B1; B7 → inviter push A9; C2 → friend scans B2; C4 → phone sharing module.

---

## 10. Attribution Rules

The business needs one number: device orders brought by referral. Two deterministic sources, added together.

| Order | Attribution point | Notes |
|---|---|---|
| 1 | **Order carries token** (`order.referral_token`) | Own store (mini-program openid + order field / Shopify cart attribute). Deterministic, no user action. |
| 2 | **Code at activation** (`activation.referral_code`) | Independent of where the box was bought; covers Tmall / JD / Amazon / retail / gifted. Deterministic. **The only layer that covers every channel.** |
| 3 | **Backfill within 7 days** | Once per account. |
| — | ~~Clicks / install attribution / IDFA matching / affiliate links~~ | Not built. If app download is ever a secondary goal, Android can use Play Install Referrer; iOS goes straight to the activation code. |

- **One order, one inviter**: first wins; if order token and activation code disagree, the order token wins and the conflict is logged.
- Because the activation code covers every channel deterministically, **the order-token funnel need not be perfect**. Order token optimizes conversion; activation code guarantees the ledger — separate KPIs.
- Reference: a full five-tier ladder (L0 order token / L1 coupon at checkout / L2 platform affiliate / L3 activation code / L4 backfill) was evaluated; P0 builds L0 + L3 + L4 only. L1 depends on marketplace rules for custom codes; L2 attributes to a channel, not a person; neither is a basis for paying rewards.

---

## 11. Data & Events

**Entities**
- `referral_token`: user_id, token, created_at
- `referral_ledger`: inviter_id, invitee_id, source (image / link / workout_qr / device), stage (signed_up / ordered / activated), order_id, device_id, state, timestamps
- `reward`: user_id, kind (credit / pro_month), amount, currency, expires_at, ledger_id, state
- `edition_config`: edition, amounts, storefronts, destinations, strings{zh, en}

**Events**
- `invite_page_view`, `invite_cta_tap`, `share_complete`{form, dest}
- `landing_view`{token, env, edition} — logged, never surfaced as a click count
- `signup_with_token`, `order_with_token`, `activation_code_entered`{prefilled}, `activation_code_skipped`
- `reward_granted`, `reward_reversed`, `credit_redeemed`, `credit_expired`

**Dashboard**: referred orders / share (north star) · share rate, coded sign-up rate, sign-up → purchase · cost per order, credit redemption, Pro deferral · split by source / edition / language.

---

## 12. Edge Cases

| Case | Handling |
|---|---|
| Entering your own code | "That's your own code", no reward |
| Friend returns the device | Both sides `reversed`; spent credit not clawed back, unspent voided; remaining Pro days removed |
| Inviter has no activated device / is banned | Landing page shows the product without discount; code invalid |
| Friend is an existing user | Accounts with an activated device cannot be invitees; unactivated ones can |
| Two codes / switching | First binding wins; changeable once before activation |
| Edition mismatch (CN account opens a GLOBAL link) | The friend's reward follows the **friend's** edition; the inviter's follows the inviter's |
| Credit expires | One push 7 days before; voided on expiry, shown in details |
| Fraud | Same device fingerprint / payment account / address at volume → manual review; abnormal velocity suspends rather than rejects; inviter must have real workout history |
| Link with invalid token | Treated as a plain product page, no error |
| Device can only show static images | Device invites fall back to a device channel code, not attributed to a person |

---

## 13. Non-functional

- **Privacy**: friend names masked per language, avatars not shown to the inviter; inviter proof on the landing page uses aggregates only; CN data stored in-country.
- **Performance**: landing first paint ≤ 1.5 s on 4G; QR generated on device; invite image renders ≤ 1 s through the existing ShareKit pipeline.
- **Security**: rewards granted server-side only; tokens random, not enumerable; Pro days extend server-side entitlement, not store offer codes.

---

## 14. Fit with the existing sharing architecture

| Layer | Change | Notes |
|---|---|---|
| ① Subject | Add `E12 · Referral` (R1 only) | Just so the invite card has a cell in the matrix |
| ② Atoms | G family 2 → 4 | `G1` watermark QR injects the token (27 templates benefit) · `G2` app-download entry → **purchase entry** · `G3` inviter strip 🆕 · `G4` plain-code strip 🆕 |
| ③ Assembly | Add `T28 invite card` (3:4 phone / 1:1 device) | Two JSON entries in the template registry; the other 27 templates keep their structure |
| ④ Carriers | **None added** | Only the existing ① image PNG and ③ H5 |
| ⑤ Paths | New entries: Invite friends, device-screen invite | Entry-determines-subject rule unchanged |
| ShareKit | `ReferralProvider` (DataProvider layer) + `RegionProfile` (injected at the Composition layer) | The ledger and reward engine are **backend services**, outside ShareKit; ShareKit only renders the token into images / links |

---

## 15. Milestones

| Phase | Scope | Depends on |
|---|---|---|
| **P0** | FR-1 / 2 / 3 / 4 / 5 / 6 / 10: token, invite page, share sheet + T28, landing page, checkout discount, banked credit, activation code, server config. Both editions and both languages together. | Mini-store / bodypark.com accept the token field; the activation wizard gains one step |
| **P1** | FR-7 / 8 / 9: details, rewards page, push, device QR | Whether the device can render a dynamic QR |
| **P2** | Accessory redemption, tiered campaigns, per-market amount A/B | — |

**Suggested P0 start: content-image mount + landing page.** The G1 change is nearly free and carries the most volume; the dedicated invite card and device side can slip to P1.

---

## 16. Open Questions

| # | Owner | Question | Impact |
|---|---|---|---|
| 1 | E-commerce / Ops | Can the mini-store / bodypark.com carry a token field on the order? | Decides whether attribution layer 1 exists; otherwise everything rides on the activation code and the landing CTA changes shape |
| 2 | Ops / Finance | Per-market amounts and the Pro value shown | ¥50 / $10 and ¥30 / $4.99 are placeholders; same figure in local currency vs PPP-adjusted for EU / JP |
| 3 | Hardware | Can the 466 round screen render a dynamic QR? | If not, device invites attribute to a device channel, not a person |
| 4 | Legal | Accounting and tax treatment of credit | CN: non-cash, no invoice, 90-day expiry; GLOBAL: terms clause |
| 5 | Ops / Legal | Can Tmall / JD / Amazon host a custom code and report redemptions? | Affects third-party checkout experience only, not attribution (activation code is the floor) |

---

## Appendix · Decision log

| Date | Decision |
|---|---|
| 09-03 | Destination is the e-commerce purchase page (hardware first), not an app store; share forms are image (with QR) and H5 only |
| 09-03 | Attribution simplified: the business tracks "orders brought by referral"; users see sign-ups / purchases; clicks not tracked |
| 09-03 | Single CTA on the invite page; order benefit → how it works → CTA → results |
| 09-03 | CN / GLOBAL editions with zh / en; edition and language orthogonal |
| 09-03 | Rewards: friend −¥50 / $10 + 1 month Pro; inviter ¥50 / $10 credit + 1 month Pro per friend; all stackable; sign-up alone earns nothing |
| 09-03 | Device price corrected to $239–299 (earlier documents wrongly said ¥5,499 / $799) |
| 09-03 | Referral moved to its own `referral/` folder; PRD and design note merged into this Markdown; all screens in the Demo |
