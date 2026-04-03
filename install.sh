#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing Codex SEO..."
python3 "${SCRIPT_DIR}/scripts/install_plugin.py" install --force "$@"
echo "Codex SEO installed."
echo "Use /seo, \$seo, or natural language in Codex."
