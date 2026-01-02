from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import subprocess

import pandas as pd
from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    fileserver_root: Path
    assets_dir: str = "ASSETS"
    templates_dir: str = "TEMPLATES"
    default_export_dir: Path = Path(r".\\reports")

    @property
    def fileserver_path(self) -> Path:
        return self.fileserver_root

    @property
    def assets_path(self) -> Path:
        return self.fileserver_root / self.assets_dir

    @property
    def templates_path(self) -> Path:
        return self.fileserver_root / self.templates_dir


def load_settings(env_path: Path = Path(".env")) -> Settings:
    load_dotenv(env_path)
    env_root = os.environ.get("FILESERVER_ROOT")
    if env_root:
        root = Path(env_root)
    else:
        root = Path.home() / "AssetManagement"
    assets_dir = os.environ.get("ASSETS_DIR", "ASSETS")
    templates_dir = os.environ.get("TEMPLATES_DIR", "TEMPLATES")
    export_dir = Path(os.environ.get("DEFAULT_EXPORT_DIR", r".\\reports"))
    export_dir.mkdir(parents=True, exist_ok=True)
    return Settings(
        fileserver_root=root,
        assets_dir=assets_dir,
        templates_dir=templates_dir,
        default_export_dir=export_dir,
    )

def create_fileserver_structure(settings: Settings) -> subprocess.CompletedProcess:
    """
    Run the create_fileserver_structure.ps1 PowerShell script with -RootPath set to assets_path.
    
    Args:
        settings: Settings object containing the assets_path configuration
        
    Returns:
        CompletedProcess object with the result of the PowerShell execution
    """
    script_path = Path(__file__).parent.parent / "scripts" / "create_fileserver_structure.ps1"
    fileserver_root = settings.fileserver_root
    
    command = [
        "powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-File", str(script_path),
        "-RootPath", str(fileserver_root)
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error executing script: {result.stderr}")
    else:
        print(f"Script executed successfully: {result.stdout}")
    
    return result


def get_current_phase(asset_folder: Path) -> str:
    """
    Infer phase from _STATUS_XX_*.txt files in the asset root.
    Returns '00' if none found.
    """
    if not asset_folder.exists():
        return "00"
    phases: list[str] = []
    for p in asset_folder.iterdir():
        if p.is_file() and p.name.startswith("_STATUS_"):
            try:
                # Expected: _STATUS_01_*.txt
                phase_num = p.name.split("_")[2][:2]
                phases.append(phase_num)
            except Exception:
                pass
    return max(phases) if phases else "00"


def get_folder_stats(folder: Path) -> dict:
    total_size = 0
    file_count = 0
    for p in folder.rglob("*"):
        if p.is_file():
            file_count += 1
            try:
                total_size += p.stat().st_size
            except OSError:
                pass
    return {"file_count": file_count, "total_size_bytes": total_size}


def list_assets(settings: Settings) -> pd.DataFrame:
    rows = []
    ap = settings.assets_path
    if not ap.exists():
        return pd.DataFrame(columns=["asset", "phase", "file_count", "total_size_mb"])

    for d in sorted([x for x in ap.iterdir() if x.is_dir()]):
        phase = get_current_phase(d)
        stats = get_folder_stats(d)
        rows.append(
            {
                "asset": d.name,
                "phase": phase,
                "file_count": stats["file_count"],
                "total_size_mb": round(stats["total_size_bytes"] / (1024 * 1024), 2),
            }
        )
    return pd.DataFrame(rows)


def export_excel(df: pd.DataFrame, out_path: Path) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(out_path, index=False)
    return out_path
