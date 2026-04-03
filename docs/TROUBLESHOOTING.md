# Troubleshooting

## Plugin not visible

Check the installed plugin copy and marketplace entry:

```bash
ls ~/plugins/codex-seo/.codex-plugin/plugin.json
cat ~/.agents/plugins/marketplace.json
```

If the plugin is missing, rerun:

```bash
cd codex-seo
./install.sh
```

## Python utilities fail

Confirm the local virtualenv exists:

```bash
ls ~/plugins/codex-seo/.venv
```

If needed, reinstall:

```bash
cd codex-seo
./install.sh --skip-venv
python3 scripts/install_plugin.py install --force
```

## MCP extension not available

Inspect the plugin-local MCP file:

```bash
cat codex-seo/.mcp.json
```

Or if installed locally:

```bash
cat ~/plugins/codex-seo/.mcp.json
```

Then rerun the relevant extension installer.
