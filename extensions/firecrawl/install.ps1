#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ConfigScript = Join-Path $ScriptDir ".." ".." "scripts" "configure_mcp.py"
$ApiKey = Read-Host "Firecrawl API key"

python $ConfigScript upsert firecrawl $ApiKey
Write-Host "Firecrawl MCP entry updated."
