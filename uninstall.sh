#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Removing Codex SEO..."
python3 "${SCRIPT_DIR}/scripts/install_plugin.py" uninstall "$@"
echo "Codex SEO removed."
