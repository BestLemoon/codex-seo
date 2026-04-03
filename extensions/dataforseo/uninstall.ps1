#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ConfigScript = Join-Path $ScriptDir ".." ".." "scripts" "configure_mcp.py"

python $ConfigScript remove dataforseo
Write-Host "DataForSEO MCP entry removed."
