$ErrorActionPreference = "Stop"

if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
  Write-Host "Conda not found on PATH. Install Miniconda/Anaconda and reopen PowerShell." -ForegroundColor Red
  exit 1
}

Write-Host "== Creating/updating conda env ==" -ForegroundColor Cyan
conda env update -f environment.yml --prune

Write-Host "== Activating env ==" -ForegroundColor Cyan
conda activate asset-lifecycle-lite-py312

Write-Host "== Registering Jupyter kernel ==" -ForegroundColor Cyan
python -m ipykernel install --user --name asset-lifecycle-lite-py312 --display-name "Asset Lifecycle Lite (py312)"

if (-not (Test-Path ".\.env")) {
  Copy-Item ".\.env.example" ".\.env"
  Write-Host "Created .env from .env.example (edit FILESERVER_ROOT)." -ForegroundColor Yellow
}

Write-Host "Done." -ForegroundColor Green
