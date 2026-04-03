#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ConfigScript = Join-Path $ScriptDir ".." ".." "scripts" "configure_mcp.py"
$Username = Read-Host "DataForSEO username (email)"
$Password = Read-Host "DataForSEO password"

python $ConfigScript upsert dataforseo $Username $Password
Write-Host "DataForSEO MCP entry updated."
