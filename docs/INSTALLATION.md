# Installation

## Prerequisites

- Python 3.11+
- Git
- A Codex environment that can load local plugins and skills

Optional:

- Chromium via Playwright for visual analysis
- Node.js 20+ for MCP-backed extensions

## Local Install

From the repository checkout:

```bash
cd codex-seo
./install.sh
```

Windows:

```powershell
cd codex-seo
.\install.ps1
```

The installer:

- Copies this subproject to `~/plugins/codex-seo`
- Updates `~/.agents/plugins/marketplace.json`
- Creates `~/plugins/codex-seo/.venv`
- Installs `requirements.txt` into that virtualenv

## Verify

Check the local plugin copy:

```bash
ls ~/plugins/codex-seo/.codex-plugin/plugin.json
ls ~/plugins/codex-seo/skills/seo/SKILL.md
```

Then open Codex and use one of:

```text
/seo audit https://example.com
$seo audit https://example.com
Run a full SEO audit for https://example.com
```

## MCP Extensions

The plugin ships with a plugin-local `.mcp.json`. Configure optional providers with the bundled extension installers:

```bash
./extensions/dataforseo/install.sh
./extensions/firecrawl/install.sh
./extensions/banana/install.sh
```

Those scripts update the plugin-local MCP config instead of modifying any global
legacy assistant settings file.

## Uninstall

```bash
cd codex-seo
./uninstall.sh
```

Windows:

```powershell
cd codex-seo
.\uninstall.ps1
```
