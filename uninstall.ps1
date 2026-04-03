#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Removing Codex SEO..."
python "$ScriptDir/scripts/install_plugin.py" uninstall @args
Write-Host "Codex SEO removed."
