# Asset Lifecycle File Server — Lite Ops Repo (Windows + Conda + Jupyter)

This is a **minimal** repo that:
- keeps your **official file-server structure** docs
- keeps your **PowerShell folder-creator** script (parameterized)
- provides a small **Python ops module** used from a **Jupyter notebook**

No packaging, no CI, no pre-commit — just enough to be productive on Windows.

## Setup (PowerShell)
```powershell
cd asset_lifecycle_lite
.\scripts\01_init_conda_env.ps1
copy .env.example .env
notepad .env
```

## Create the structure
```powershell
.\scripts\create_fileserver_structure.ps1 -RootPath "C:\AssetManagement"
# or UNC:
# .\scripts\create_fileserver_structure.ps1 -RootPath "\\FileServer\AssetManagement"
```

## Run notebook
Open `notebooks/00_operations_dashboard.ipynb` and select kernel **Asset Lifecycle Lite (py312)**.
