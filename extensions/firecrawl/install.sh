#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_SCRIPT="${SCRIPT_DIR}/../../scripts/configure_mcp.py"

echo "Configuring Firecrawl for Codex SEO..."
read -rsp "Firecrawl API key: " FIRECRAWL_API_KEY
echo

python3 "${CONFIG_SCRIPT}" upsert firecrawl "${FIRECRAWL_API_KEY}"
echo "Firecrawl MCP entry updated."
