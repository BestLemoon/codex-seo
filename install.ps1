#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Installing Codex SEO..."
python "$ScriptDir/scripts/install_plugin.py" install --force @args
Write-Host "Codex SEO installed."
Write-Host "Use /seo, `$seo, or natural language in Codex."
