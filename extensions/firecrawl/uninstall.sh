#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_SCRIPT="${SCRIPT_DIR}/../../scripts/configure_mcp.py"

python3 "${CONFIG_SCRIPT}" remove firecrawl
echo "Firecrawl MCP entry removed."
