# Codex SEO

[中文说明](./README.zh-CN.md)

Codex SEO is a Codex-native SEO analysis plugin with slash-friendly entrypoints,
specialist agents, Python execution utilities, and optional MCP-backed
extensions.

This public repository is a standalone Codex adaptation of the original
[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo). The goal
is to preserve the original SEO capability set while shipping it in a cleaner
Codex-first layout for local installation, testing, and public distribution.

## Features

- Full-site audits with parallel specialist agents
- Deep analysis for pages, technical SEO, content, schema, sitemaps, images,
  GEO, local SEO, maps, hreflang, and backlinks
- Google API workflows for PageSpeed, CrUX, Search Console, Indexing, and GA4
- Optional MCP-backed extensions for DataForSEO, Firecrawl, and image generation
- PDF and HTML report generation through `scripts/google_report.py`

## Invocation

The main skill name is `seo`. Use whichever Codex entrypoint is available:

- Slash command: `/seo audit https://example.com`
- Explicit skill call: `$seo audit https://example.com`
- Natural language: `Run a full SEO audit for https://example.com`

Core subcommands:

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

## Repository Layout

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

## Install

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

The installer copies the plugin into `~/plugins/codex-seo`, updates
`~/.agents/plugins/marketplace.json`, and creates a local virtual environment for
the Python utilities.

More detail: [docs/INSTALLATION.md](./docs/INSTALLATION.md)

## Extensions

Optional extension installers configure the plugin-local `.mcp.json` instead of
writing to a global assistant configuration:

- `./extensions/dataforseo/install.sh`
- `./extensions/firecrawl/install.sh`
- `./extensions/banana/install.sh`

If no extension is configured, Codex SEO falls back to local scripts and static
analysis where possible.

## Verification

Useful smoke checks:

```bash
python3 scripts/install_plugin.py --help
python3 scripts/configure_mcp.py --help
python3 scripts/google_auth.py --help
python3 scripts/backlinks_auth.py --help
python3 scripts/google_report.py --help
```

## Credits

- Adapted from [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
- Original concepts and much of the SEO methodology come from the upstream
  project
- Repo-specific attribution details live in [NOTICE.md](./NOTICE.md)
