#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_SCRIPT="${SCRIPT_DIR}/../../scripts/configure_mcp.py"

echo "Configuring Banana image generation for Codex SEO..."
read -rsp "Google AI API key: " GOOGLE_AI_API_KEY
echo

python3 "${CONFIG_SCRIPT}" upsert banana "${GOOGLE_AI_API_KEY}"
echo "Banana MCP entry updated."
