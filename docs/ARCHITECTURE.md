# Architecture

Codex SEO follows a three-layer structure inside `codex-seo/`:

1. Directive layer: skills in `skills/`
2. Orchestration layer: specialist agent prompts in `agents/`
3. Execution layer: Python utilities and templates in `scripts/`, `schema/`, and `pdf/`

## Plugin Root

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

## Main Entry

The main skill is `skills/seo/SKILL.md`. It preserves the original command vocabulary while documenting three Codex-friendly entry modes:

- `/seo ...`
- `$seo ...`
- natural language

## Extensions

Optional extension skills stay bundled in the tree:

- `extensions/dataforseo`
- `extensions/firecrawl`
- `extensions/banana`

Each extension installer configures `.mcp.json` instead of writing to a global
legacy assistant settings file.

## Validation

Public verification is command-based:

- `python3 scripts/install_plugin.py --help`
- `python3 scripts/configure_mcp.py --help`
- `python3 scripts/google_auth.py --help`
- `python3 scripts/backlinks_auth.py --help`
- `python3 scripts/google_report.py --help`
