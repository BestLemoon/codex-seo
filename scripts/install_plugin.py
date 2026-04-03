#!/usr/bin/env python3
"""Install or uninstall the Codex SEO local plugin."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


PLUGIN_NAME = "codex-seo"
SKIP_NAMES = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "tests",
}


def plugin_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_target() -> Path:
    return Path.home() / "plugins" / PLUGIN_NAME


def default_marketplace() -> Path:
    return Path.home() / ".agents" / "plugins" / "marketplace.json"


def should_skip(path: Path) -> bool:
    return any(part in SKIP_NAMES for part in path.parts)


def copy_plugin(target: Path, force: bool) -> None:
    source = plugin_root()
    if target.exists():
        if not force:
            raise FileExistsError(f"{target} already exists. Use --force to replace it.")
        shutil.rmtree(target)

    def ignore_filter(_src: str, names: list[str]) -> set[str]:
        return {name for name in names if name in SKIP_NAMES}

    shutil.copytree(source, target, ignore=ignore_filter)


def update_marketplace(path: Path, plugin_path: str) -> None:
    payload: dict
    if path.exists():
        payload = json.loads(path.read_text())
    else:
        payload = {
            "name": "local-plugins",
            "interface": {"displayName": "Local Plugins"},
            "plugins": [],
        }

    plugins = payload.setdefault("plugins", [])
    entry = {
        "name": PLUGIN_NAME,
        "source": {"source": "local", "path": plugin_path},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }

    for index, existing in enumerate(plugins):
        if isinstance(existing, dict) and existing.get("name") == PLUGIN_NAME:
            plugins[index] = entry
            break
    else:
        plugins.append(entry)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n")


def remove_marketplace_entry(path: Path) -> None:
    if not path.exists():
        return

    payload = json.loads(path.read_text())
    plugins = payload.get("plugins", [])
    payload["plugins"] = [
        entry
        for entry in plugins
        if not (isinstance(entry, dict) and entry.get("name") == PLUGIN_NAME)
    ]
    path.write_text(json.dumps(payload, indent=2) + "\n")


def build_venv(target: Path) -> None:
    import subprocess
    import sys

    venv_dir = target / ".venv"
    requirements = target / "requirements.txt"
    subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
    subprocess.run([str(venv_dir / "bin" / "pip"), "install", "-r", str(requirements)], check=True)


def install(target: Path, marketplace: Path, force: bool, skip_venv: bool) -> None:
    copy_plugin(target, force=force)
    update_marketplace(marketplace, "./plugins/codex-seo")
    if not skip_venv:
        build_venv(target)


def uninstall(target: Path, marketplace: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    remove_marketplace_entry(marketplace)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install or uninstall the Codex SEO plugin.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser("install", help="Install the plugin locally.")
    install_parser.add_argument("--target", type=Path, default=default_target())
    install_parser.add_argument("--marketplace", type=Path, default=default_marketplace())
    install_parser.add_argument("--force", action="store_true")
    install_parser.add_argument("--skip-venv", action="store_true")

    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall the plugin locally.")
    uninstall_parser.add_argument("--target", type=Path, default=default_target())
    uninstall_parser.add_argument("--marketplace", type=Path, default=default_marketplace())

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "install":
        install(args.target, args.marketplace, force=args.force, skip_venv=args.skip_venv)
        print(f"Installed {PLUGIN_NAME} to {args.target}")
        print(f"Updated marketplace: {args.marketplace}")
        return 0

    uninstall(args.target, args.marketplace)
    print(f"Removed {PLUGIN_NAME} from {args.target}")
    print(f"Updated marketplace: {args.marketplace}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
