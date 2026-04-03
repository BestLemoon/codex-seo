#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_SCRIPT="${SCRIPT_DIR}/../../scripts/configure_mcp.py"

echo "Configuring DataForSEO for Codex SEO..."
read -rp "DataForSEO username (email): " DFSE_USERNAME
read -rsp "DataForSEO password: " DFSE_PASSWORD
echo

python3 "${CONFIG_SCRIPT}" upsert dataforseo "${DFSE_USERNAME}" "${DFSE_PASSWORD}"
echo "DataForSEO MCP entry updated."
