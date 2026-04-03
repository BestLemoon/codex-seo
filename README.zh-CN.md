# Codex SEO

[English README](./README.md)

Codex SEO 是一个面向 Codex 的 SEO 分析插件，支持 slash 命令入口、技能路由、
专用分析 agent、Python 执行脚本，以及可选的 MCP 扩展能力。

这个公开仓库是从原始项目
[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
改版迁移出来的独立 Codex 版本。目标是尽量保留原仓库的 SEO 能力，同时把结构、
安装方式和发布形式改成更适合 Codex 的公共仓库。

## 功能概览

- 全站 SEO 审计，支持并行 specialist agents
- 单页、技术 SEO、内容质量、Schema、Sitemap、图片、GEO、本地 SEO、地图、
  hreflang、外链分析
- Google API 工作流：PageSpeed、CrUX、Search Console、Indexing、GA4
- 可选 MCP 扩展：DataForSEO、Firecrawl、AI 图片生成
- 通过 `scripts/google_report.py` 生成 PDF / HTML 报告

## 调用方式

主 skill 名称是 `seo`。根据你的 Codex 环境，任选以下入口：

- Slash 命令：`/seo audit https://example.com`
- 显式 skill 调用：`$seo audit https://example.com`
- 自然语言：`Run a full SEO audit for https://example.com`

主要子命令：

- `audit`
- `page`
- `technical`
- `content`
- `schema`
- `sitemap`
- `images`
- `geo`
- `local`
- `maps`
- `hreflang`
- `google`
- `backlinks`
- `dataforseo`
- `firecrawl`
- `image-gen`

## 目录结构

```text
codex-seo/
  .codex-plugin/plugin.json
  .agents/plugins/marketplace.json
  .mcp.json
  skills/
  agents/
  scripts/
  extensions/
  docs/
  schema/
  hooks/
```

## 安装

```bash
git clone https://github.com/BestLemoon/codex-seo.git
cd codex-seo
./install.sh
```

Windows:

```powershell
git clone https://github.com/BestLemoon/codex-seo.git
cd codex-seo
.\install.ps1
```

安装器会把插件复制到 `~/plugins/codex-seo`，更新
`~/.agents/plugins/marketplace.json`，并为 Python 工具创建本地虚拟环境。

详细说明见 [docs/INSTALLATION.md](./docs/INSTALLATION.md)。

## 扩展

可选扩展安装器会修改插件本地 `.mcp.json`，不会去写全局助手配置：

- `./extensions/dataforseo/install.sh`
- `./extensions/firecrawl/install.sh`
- `./extensions/banana/install.sh`

如果没有配置这些扩展，Codex SEO 仍会尽量使用本地脚本和静态分析继续工作。

## 验证

建议先跑这些基础检查：

```bash
python3 scripts/install_plugin.py --help
python3 scripts/configure_mcp.py --help
python3 scripts/google_auth.py --help
python3 scripts/backlinks_auth.py --help
python3 scripts/google_report.py --help
```

## 致谢

- 改版自 [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
- 原项目的方法论、技能设计和大量 SEO 能力来自上游仓库
- 更详细的来源与归属说明见 [NOTICE.md](./NOTICE.md)
