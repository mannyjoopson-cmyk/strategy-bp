# 战略BP

战略BP是一个面向 Codex 的开源战略研究 Plugin。它在产品定义之前，把模糊方向转化为待支持的决策、可证伪假设、可追溯证据和明确的行动门槛。

## 它解决什么问题

- 市场机会是否值得进一步研究
- 用户需求是否真实、持续并具有支付可能
- 竞争格局是否仍有进入空间
- 商业模型和单位经济是否可能成立
- 团队是否具备进入权，关键能力缺口是什么
- 哪些证据支持继续、补证或停止

## 三种研究模式

- 机会扫描：快速判断是否值得正式研究。
- 标准研究：默认模式，按需覆盖市场、用户、竞品、商业可行性和进入能力。
- 深度尽调：用于高风险或高投入决策；额外成本、外联和数据权限必须先批准。

## 核心标准

- 决策先行，研究不以资料堆积为目标。
- 区分事实、推断、假设和建议。
- 关键结论原则上需要两个独立来源。
- 使用 A-D 证据等级，同时披露时效、样本、口径、冲突和局限。
- 输出做与不做、验证指标、放大条件和停止条件。

## 安装

GitHub 仓库发布后，把它添加为 Codex Marketplace，再安装其中唯一的 Plugin：

```bash
codex plugin marketplace add mannyjoopson-cmyk/strategy-bp
codex plugin add strategy-bp@strategy-bp
```

本地测试时，第一个命令也可以直接填写仓库目录。

只需要 Skill 时，也可以把 `plugins/strategy-bp/skills/strategy-bp/` 复制到 `$CODEX_HOME/skills/strategy-bp/`，然后新建 Codex 任务。

## 使用

```text
使用 strategy-bp。
请采用标准研究评估【产品方向】。
先明确待支持的决策、范围和关键假设。
关键结论执行 A-D 证据分级和独立来源验证。
只提供分析和推荐，不替我决定方向。
```

## 数据与权限

本 Plugin 不包含 Hook、MCP 服务、账号凭据或自动化外联能力，也不会自行购买数据、联系人员、进入私域或处理个人数据。真实外部研究是否可联网、可访问哪些来源，取决于用户为 Codex 提供的工具和权限。

## 仓库内容

- `.agents/plugins/marketplace.json`：只包含一个 Plugin 的 Marketplace 配置。
- `plugins/strategy-bp/skills/strategy-bp/`：可安装 Skill 和按需研究模块。
- `plugins/strategy-bp/templates/Strategy-Brief.md`：战略研究交付模板。
- `plugins/strategy-bp/examples/`：三种研究模式的路由示例。
- `plugins/strategy-bp/docs/ROLE-CONTRACT.md`：角色职责和边界。

## 许可证

MIT。详见 `LICENSE`。
