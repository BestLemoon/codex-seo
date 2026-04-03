#!/usr/bin/env python3
"""Upsert or remove extension MCP server entries in .mcp.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def plugin_root() -> Path:
    return Path(__file__).resolve().parents[1]


def mcp_path(explicit: Path | None) -> Path:
    return explicit or plugin_root() / ".mcp.json"


def load_payload(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {"mcpServers": {}}


def write_payload(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n")


def server_config(extension: str, value_one: str, value_two: str | None = None) -> tuple[str, dict]:
    if extension == "dataforseo":
        return (
            "dataforseo",
            {
                "command": "npx",
                "args": ["-y", "dataforseo-mcp-server"],
                "env": {
                    "DATAFORSEO_USERNAME": value_one,
                    "DATAFORSEO_PASSWORD": value_two or "",
                    "ENABLED_MODULES": "SERP,KEYWORDS_DATA,ONPAGE,DATAFORSEO_LABS,BACKLINKS,DOMAIN_ANALYTICS,BUSINESS_DATA,CONTENT_ANALYSIS,AI_OPTIMIZATION",
                    "FIELD_CONFIG_PATH": "./extensions/dataforseo/field-config.json",
                },
            },
        )
    if extension == "firecrawl":
        return (
            "firecrawl-mcp",
            {
                "command": "npx",
                "args": ["-y", "firecrawl-mcp"],
                "env": {"FIRECRAWL_API_KEY": value_one},
            },
        )
    if extension == "banana":
        return (
            "nanobanana-mcp",
            {
                "command": "npx",
                "args": ["-y", "@ycse/nanobanana-mcp@latest"],
                "env": {"GOOGLE_AI_API_KEY": value_one},
            },
        )
    raise ValueError(f"Unsupported extension: {extension}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Configure Codex SEO MCP entries.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    upsert = subparsers.add_parser("upsert", help="Create or update an MCP entry.")
    upsert.add_argument("extension", choices=["dataforseo", "firecrawl", "banana"])
    upsert.add_argument("value_one", help="Primary credential value.")
    upsert.add_argument("value_two", nargs="?", help="Secondary credential value when required.")
    upsert.add_argument("--mcp-file", type=Path)

    remove = subparsers.add_parser("remove", help="Remove an MCP entry.")
    remove.add_argument("extension", choices=["dataforseo", "firecrawl", "banana"])
    remove.add_argument("--mcp-file", type=Path)

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = mcp_path(getattr(args, "mcp_file", None))
    payload = load_payload(path)
    payload.setdefault("mcpServers", {})

    if args.command == "upsert":
        name, config = server_config(args.extension, args.value_one, getattr(args, "value_two", None))
        payload["mcpServers"][name] = config
        write_payload(path, payload)
        print(f"Configured {name} in {path}")
        return 0

    name, _ = server_config(args.extension, "placeholder")
    payload["mcpServers"].pop(name, None)
    write_payload(path, payload)
    print(f"Removed {name} from {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
