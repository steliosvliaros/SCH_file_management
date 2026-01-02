# Asset Management System - Automation & Metrics
# Python 3.12 Notebook
# Purpose: Automate file management operations and generate portfolio metrics

import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
import json
import shutil
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================================================
# CONFIGURATION
# =============================================================================

ROOT_PATH = r"\\FileServer\AssetManagement"  # Update with your path
ASSETS_PATH = os.path.join(ROOT_PATH, "ASSETS")
TEMPLATES_PATH = os.path.join(ROOT_PATH, "TEMPLATES")
ARCHIVE_PATH = os.path.join(ROOT_PATH, "ARCHIVE")

# Asset type mapping
ASSET_TYPES = {
    'PV': 'Solar Photovoltaic',
    'WF': 'Wind Farm',
    'HTL': 'Hotel',
    'DC': 'Data Center',
    'HF': 'Hydroponic Farm'
}

# Phase codes
PHASE_CODES = {
    '01': 'Pipeline',
    '02': 'Under Development',
    '03': 'Under Construction',
    '04': 'Operational'
}

# =============================================================================
# PART 1: ASSET DISCOVERY AND INVENTORY
# =============================================================================

def discover_all_assets(assets_path: str = ASSETS_PATH) -> pd.DataFrame:
    """
    Scan ASSETS folder and create complete inventory
    Returns DataFrame with asset information
    """
    print("Discovering assets...")
    
    assets = []
    
    for folder in os.listdir(assets_path):
        folder_path = os.path.join(assets_path, folder)
        
        if not os.path.isdir(folder_path):
            continue
        
        # Parse folder name: SUBCO_TYPEID_NAME_LOCATION
        try:
            parts = folder.split('_', 3)
            if len(parts) >= 3:
                subco = parts[0]
                type_id = parts[1]
                asset_type = ''.join([c for c in type_id if c.isalpha()])
                asset_id = ''.join([c for c in type_id if c.isdigit()])
                name = parts[2] if len(parts) > 2 else "Unknown"
                location = parts[3] if len(parts) > 3 else "Unknown"
                
                # Determine current phase from status files
                current_phase = get_current_phase(folder_path)
                
                # Get basic stats
                stats = get_folder_stats(folder_path)
                
                asset_info = {
                    'Asset_Folder': folder,
                    'Subcompany': subco,
                    'Asset_Type': asset_type,
                    'Asset_ID': asset_id,
                    'Asset_Name': name,
                    'Location': location,
                    'Current_Phase': current_phase,
                    'Phase_Name': PHASE_CODES.get(current_phase, 'Unknown'),
                    'Folder_Path': folder_path,
                    'Total_Files': stats['total_files'],
                    'Total_Size_MB': stats['total_size_mb'],
                    'Last_Modified': stats['last_modified']
                }
                
                assets.append(asset_info)
        
        except Exception as e:
            print(f"Error parsing {folder}: {e}")
            continue
    
    df = pd.DataFrame(assets)
    print(f"Discovered {len(df)} assets")
    
    return df

def get_current_phase(folder_path: str) -> str:
    """Get current phase from status files"""
    status_files = [f for f in os.listdir(folder_path) if f.startswith('_STATUS_')]
    
    if not status_files:
        return '00'
    
    # Get highest numbered status file
    phases = []
    for sf in status_files:
        try:
            phase_num = sf.split('_')[2][:2]
            phases.append(phase_num)
        except:
            continue
    
    return max(phases) if phases else '00'

def get_folder_stats(folder_path: str) -> Dict:
    """Get statistics about a folder"""
    total_files = 0
    total_size = 0
    last_modified = None
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                total_files += 1
                total_size += os.path.getsize(file_path)
                
                mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if last_modified is None or mod_time > last_modified:
                    last_modified = mod_time
            except:
                continue
    
    return {
        'total_files': total_files,
        'total_size_mb': round(total_size / (1024 * 1024), 2),
        'last_modified': last_modified.strftime('%Y-%m-%d') if last_modified else None
    }

# =============================================================================
# PART 2: PORTFOLIO METRICS AND DASHBOARDS
# =============================================================================

def generate_portfolio_dashboard(assets_df: pd.DataFrame) -> Dict:
    """Generate comprehensive portfolio metrics"""
    print("\nGenerating portfolio dashboard...")
    
    metrics = {}
    
    # Overall statistics
    metrics['total_assets'] = len(assets_df)
    metrics['total_size_gb'] = round(assets_df['Total_Size_MB'].sum() / 1024, 2)
    metrics['total_files'] = int(assets_df['Total_Files'].sum())
    
    # By asset type
    metrics['by_type'] = assets_df.groupby('Asset_Type').agg({
        'Asset_Folder': 'count',
        'Total_Files': 'sum',
        'Total_Size_MB': 'sum'
    }).to_dict('index')
    
    # By phase
    metrics['by_phase'] = assets_df.groupby('Phase_Name').agg({
        'Asset_Folder': 'count',
        'Total_Files': 'sum',
        'Total_Size_MB': 'sum'
    }).to_dict('index')
    
    # By subcompany
    metrics['by_subcompany'] = assets_df.groupby('Subcompany').agg({
        'Asset_Folder': 'count',
        'Total_Files': 'sum',
        'Total_Size_MB': 'sum'
    }).to_dict('index')
    
    # Asset type + phase matrix
    metrics['type_phase_matrix'] = pd.crosstab(
        assets_df['Asset_Type'], 
        assets_df['Phase_Name']
    ).to_dict()
    
    # Recent activity (last 30 days)
    assets_df['Last_Modified'] = pd.to_datetime(assets_df['Last_Modified'])
    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent = assets_df[assets_df['Last_Modified'] > thirty_days_ago]
    metrics['recent_activity'] = {
        'assets_modified_30d': len(recent),
        'files_modified_30d': int(recent['Total_Files'].sum())
    }
    
    return metrics

def print_dashboard(metrics: Dict):
    """Print formatted dashboard"""
    print("\n" + "="*80)
    print(" PORTFOLIO DASHBOARD")
    print("="*80)
    
    print(f"\nOVERALL STATISTICS:")
    print(f"  Total Assets: {metrics['total_assets']}")
    print(f"  Total Files: {metrics['total_files']:,}")
    print(f"  Total Storage: {metrics['total_size_gb']:.2f} GB")
    
    print(f"\nBY ASSET TYPE:")
    for asset_type, data in metrics['by_type'].items():
        type_name = ASSET_TYPES.get(asset_type, asset_type)
        print(f"  {type_name:30} {int(data['Asset_Folder']):3} assets | "
              f"{int(data['Total_Files']):6,} files | "
              f"{data['Total_Size_MB']/1024:6.2f} GB")
    
    print(f"\nBY PHASE:")
    for phase, data in metrics['by_phase'].items():
        print(f"  {phase:30} {int(data['Asset_Folder']):3} assets | "
              f"{int(data['Total_Files']):6,} files | "
              f"{data['Total_Size_MB']/1024:6.2f} GB")
    
    print(f"\nBY SUBCOMPANY:")
    for subco, data in metrics['by_subcompany'].items():
        print(f"  {subco:30} {int(data['Asset_Folder']):3} assets | "
              f"{int(data['Total_Files']):6,} files | "
              f"{data['Total_Size_MB']/1024:6.2f} GB")
    
    print(f"\nRECENT ACTIVITY (Last 30 days):")
    print(f"  Assets Modified: {metrics['recent_activity']['assets_modified_30d']}")
    print(f"  Files Modified: {metrics['recent_activity']['files_modified_30d']:,}")
    
    print("\n" + "="*80 + "\n")

def visualize_portfolio(assets_df: pd.DataFrame, output_path: str = None):
    """Create visualization charts for portfolio"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Asset Portfolio Dashboard', fontsize=16, fontweight='bold')
    
    # Chart 1: Assets by Type
    type_counts = assets_df['Asset_Type'].value_counts()
    type_labels = [ASSET_TYPES.get(t, t) for t in type_counts.index]
    axes[0, 0].pie(type_counts.values, labels=type_labels, autopct='%1.1f%%')
    axes[0, 0].set_title('Assets by Type')
    
    # Chart 2: Assets by Phase
    phase_counts = assets_df['Phase_Name'].value_counts()
    axes[0, 1].bar(range(len(phase_counts)), phase_counts.values)
    axes[0, 1].set_xticks(range(len(phase_counts)))
    axes[0, 1].set_xticklabels(phase_counts.index, rotation=45, ha='right')
    axes[0, 1].set_title('Assets by Phase')
    axes[0, 1].set_ylabel('Number of Assets')
    
    # Chart 3: Storage by Asset Type
    type_storage = assets_df.groupby('Asset_Type')['Total_Size_MB'].sum() / 1024
    type_storage_labels = [ASSET_TYPES.get(t, t) for t in type_storage.index]
    axes[1, 0].bar(range(len(type_storage)), type_storage.values)
    axes[1, 0].set_xticks(range(len(type_storage)))
    axes[1, 0].set_xticklabels(type_storage_labels, rotation=45, ha='right')
    axes[1, 0].set_title('Storage by Asset Type')
    axes[1, 0].set_ylabel('Storage (GB)')
    
    # Chart 4: Phase Distribution by Asset Type
    phase_type_matrix = pd.crosstab(assets_df['Asset_Type'], assets_df['Phase_Name'])
    phase_type_matrix.plot(kind='bar', stacked=True, ax=axes[1, 1])
    axes[1, 1].set_title('Phase Distribution by Asset Type')
    axes[1, 1].set_xlabel('Asset Type')
    axes[1, 1].set_ylabel('Number of Assets')
    axes[1, 1].legend(title='Phase', bbox_to_anchor=(1.05, 1), loc='upper left')
    axes[1, 1].set_xticklabels([ASSET_TYPES.get(t, t) for t in phase_type_matrix.index], 
                                rotation=45, ha='right')
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Dashboard saved to: {output_path}")
    
    plt.show()

# =============================================================================
# PART 3: AUTOMATED FILE OPERATIONS
# =============================================================================

def create_new_asset(subco: str, asset_type: str, asset_id: str, 
                    name: str, location: str, dev_pm: str) -> str:
    """Create new asset from template"""
    
    asset_folder = f"{subco}_{asset_type}{asset_id}_{name}_{location}"
    template_path = os.path.join(TEMPLATES_PATH, "ASSET_LIFECYCLE_TEMPLATE")
    asset_path = os.path.join(ASSETS_PATH, asset_folder)
    
    if os.path.exists(asset_path):
        print(f"Asset already exists: {asset_folder}")
        return asset_path
    
    print(f"Creating new asset: {asset_folder}")
    
    # Copy template
    shutil.copytree(template_path, asset_path)
    
    # Create initial status file
    status_content = f"""STATUS: PIPELINE
Phase Started: {datetime.now().strftime('%Y-%m-%d')}
Responsible PM: {dev_pm}
Target Completion: {(datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')}

Key Activities in Progress:
1. Initial site identification
2. Preliminary market research
3. High-level feasibility assessment

Next Milestones:
- Site visit: {(datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')}
- Go/No-Go Decision: {(datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d')}

Phase Closed: [Will be filled when moving to next phase]
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Updated By: Python Automation Script
"""
    
    with open(os.path.join(asset_path, '_STATUS_01_PIPELINE.txt'), 'w') as f:
        f.write(status_content)
    
    print(f"Asset created successfully: {asset_path}")
    return asset_path

def transition_phase(asset_folder: str, new_phase: str, responsible_pm: str) -> bool:
    """Transition asset to new phase"""
    
    asset_path = os.path.join(ASSETS_PATH, asset_folder)
    
    if not os.path.exists(asset_path):
        print(f"Asset not found: {asset_folder}")
        return False
    
    # Get current phase
    current_phase = get_current_phase(asset_path)
    
    print(f"Transitioning {asset_folder} from phase {current_phase} to {new_phase}")
    
    # Close current status file
    current_status_file = f"_STATUS_{current_phase}_*.txt"
    current_status_path = None
    for f in os.listdir(asset_path):
        if f.startswith(f'_STATUS_{current_phase}'):
            current_status_path = os.path.join(asset_path, f)
            break
    
    if current_status_path:
        with open(current_status_path, 'a') as f:
            f.write(f"\nPhase Closed: {datetime.now().strftime('%Y-%m-%d')}")
            f.write(f"\nClosed By: Python Automation Script")
    
    # Create new status file
    phase_names = {
        '01': 'PIPELINE',
        '02': 'UNDER DEVELOPMENT',
        '03': 'UNDER CONSTRUCTION',
        '04': 'OPERATIONAL'
    }
    
    new_status_content = f"""STATUS: {phase_names.get(new_phase, 'UNKNOWN')}
Phase Started: {datetime.now().strftime('%Y-%m-%d')}
Responsible PM: {responsible_pm}
Target Completion: TBD

Key Activities in Progress:
1. [To be updated]

Next Milestones:
- [To be updated]

Phase Closed: [Will be filled when moving to next phase]
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Updated By: Python Automation Script
"""
    
    new_status_path = os.path.join(asset_path, f'_STATUS_{new_phase}_{phase_names.get(new_phase, "UNKNOWN")}.txt')
    with open(new_status_path, 'w') as f:
        f.write(new_status_content)
    
    # Set previous phase folders to read-only
    phase_mapping = {
        '02': ['01_PREFEASIBILITY'],
        '03': ['01_PREFEASIBILITY', '02_FEASIBILITY', '03_LAND_ACQUISITION', 
               '04_PERMITTING', '05_DESIGN_ENGINEERING', '06_FINANCING'],
        '04': ['07_PROCUREMENT', '08_CONSTRUCTION', '09_COMMISSIONING_COD']
    }
    
    folders_to_lock = phase_mapping.get(new_phase, [])
    for folder in folders_to_lock:
        folder_path = os.path.join(asset_path, folder)
        if os.path.exists(folder_path):
            # Set read-only (platform-specific)
            try:
                os.chmod(folder_path, 0o444)
            except:
                pass  # Windows has different read-only handling
    
    print(f"Phase transition completed successfully")
    return True

def manage_superseded_versions(asset_folder: str, phase_folder: str, 
                              subfolder: str = None, keep_latest: int = 1) -> int:
    """Move old versions to _SUPERSEDED folder"""
    
    if subfolder:
        target_path = os.path.join(ASSETS_PATH, asset_folder, phase_folder, subfolder)
    else:
        target_path = os.path.join(ASSETS_PATH, asset_folder, phase_folder)
    
    if not os.path.exists(target_path):
        print(f"Path not found: {target_path}")
        return 0
    
    superseded_path = os.path.join(target_path, '_SUPERSEDED')
    os.makedirs(superseded_path, exist_ok=True)
    
    # Group files by base name (without version and status)
    file_groups = {}
    
    for file in os.listdir(target_path):
        if os.path.isfile(os.path.join(target_path, file)):
            # Extract base name
            parts = file.split('_')
            if len(parts) >= 5:
                base_name = '_'.join(parts[:-2])  # Remove date and version
                
                if base_name not in file_groups:
                    file_groups[base_name] = []
                
                file_path = os.path.join(target_path, file)
                file_groups[base_name].append({
                    'name': file,
                    'path': file_path,
                    'mtime': os.path.getmtime(file_path)
                })
    
    moved_count = 0
    
    # For each group, keep only latest versions
    for base_name, files in file_groups.items():
        # Skip if FINAL or APPROVED in any filename
        if any('FINAL' in f['name'] or 'APPROVED' in f['name'] for f in files):
            continue
        
        # Sort by modification time
        files.sort(key=lambda x: x['mtime'], reverse=True)
        
        # Move older versions
        if len(files) > keep_latest:
            for file in files[keep_latest:]:
                dest_path = os.path.join(superseded_path, file['name'])
                shutil.move(file['path'], dest_path)
                moved_count += 1
                print(f"Moved to _SUPERSEDED: {file['name']}")
    
    print(f"Total files moved to _SUPERSEDED: {moved_count}")
    return moved_count

# =============================================================================
# PART 4: DOCUMENT TRACKING AND REPORTING
# =============================================================================

def scan_asset_documents(asset_folder: str) -> pd.DataFrame:
    """Scan all documents in an asset folder and create register"""
    
    asset_path = os.path.join(ASSETS_PATH, asset_folder)
    
    if not os.path.exists(asset_path):
        print(f"Asset not found: {asset_folder}")
        return pd.DataFrame()
    
    documents = []
    
    # Walk through all folders
    for root, dirs, files in os.walk(asset_path):
        # Skip _SUPERSEDED folders
        if '_SUPERSEDED' in root:
            continue
        
        for file in files:
            if file.startswith('_STATUS') or file.startswith('.'):
                continue
            
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(root, asset_path)
            
            # Parse filename if follows convention
            parts = file.split('_')
            
            doc_info = {
                'Filename': file,
                'Folder': rel_path,
                'Full_Path': file_path,
                'File_Size_MB': round(os.path.getsize(file_path) / (1024 * 1024), 3),
                'Modified_Date': datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d'),
                'Extension': os.path.splitext(file)[1],
            }
            
            # Try to parse document code
            if len(parts) >= 4:
                doc_info['Phase_Code'] = parts[2] if len(parts) > 2 else ''
                doc_info['Doc_Type'] = parts[3] if len(parts) > 3 else ''
                
                # Extract version
                for part in parts:
                    if part.startswith('v') and part[1:3].isdigit():
                        doc_info['Version'] = part
                        break
                
                # Extract status
                status_keywords = ['DRAFT', 'REVIEW', 'REVISED', 'FINAL', 'APPROVED', 'SIGNED']
                for keyword in status_keywords:
                    if keyword in file.upper():
                        doc_info['Status'] = keyword
                        break
            
            documents.append(doc_info)
    
    df = pd.DataFrame(documents)
    
    print(f"Scanned {len(df)} documents in {asset_folder}")
    
    return df

def generate_document_register(asset_folder: str, output_file: str = None) -> pd.DataFrame:
    """Generate complete document register for an asset"""
    
    df = scan_asset_documents(asset_folder)
    
    if df.empty:
        return df
    
    # Add statistics
    print(f"\nDocument Register Summary for {asset_folder}:")
    print(f"Total Documents: {len(df)}")
    print(f"Total Size: {df['File_Size_MB'].sum():.2f} MB")
    print(f"\nBy Phase:")
    print(df.groupby('Phase_Code').size())
    print(f"\nBy Document Type:")
    print(df.groupby('Doc_Type').size())
    print(f"\nBy Status:")
    print(df.groupby('Status').size() if 'Status' in df.columns else "No status info")
    
    # Export to CSV
    if output_file is None:
        asset_path = os.path.join(ASSETS_PATH, asset_folder)
        output_file = os.path.join(asset_path, '00_ASSET_MASTER', 'Document_Index',
                                  f'Document_Register_{datetime.now().strftime("%Y%m%d")}.csv')
    
    df.to_csv(output_file, index=False)
    print(f"\nDocument register exported to: {output_file}")
    
    return df

# =============================================================================
# PART 5: MAIN EXECUTION
# =============================================================================

def main():
    """Main execution function"""
    
    print("="*80)
    print(" ASSET MANAGEMENT SYSTEM - AUTOMATION & METRICS")
    print("="*80)
    
    # 1. Discover all assets
    print("\n### STEP 1: Asset Discovery ###")
    assets_df = discover_all_assets()
    
    # Export asset inventory
    inventory_file = os.path.join(ROOT_PATH, f"Asset_Inventory_{datetime.now().strftime('%Y%m%d')}.csv")
    assets_df.to_csv(inventory_file, index=False)
    print(f"Asset inventory exported to: {inventory_file}")
    
    # 2. Generate dashboard
    print("\n### STEP 2: Portfolio Metrics ###")
    metrics = generate_portfolio_dashboard(assets_df)
    print_dashboard(metrics)
    
    # Export metrics to JSON
    metrics_file = os.path.join(ROOT_PATH, f"Portfolio_Metrics_{datetime.now().strftime('%Y%m%d')}.json")
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2, default=str)
    print(f"Metrics exported to: {metrics_file}")
    
    # 3. Create visualizations
    print("\n### STEP 3: Visualizations ###")
    viz_file = os.path.join(ROOT_PATH, f"Portfolio_Dashboard_{datetime.now().strftime('%Y%m%d')}.png")
    visualize_portfolio(assets_df, viz_file)
    
    # 4. Example operations
    print("\n### STEP 4: Example Operations ###")
    
    # Example: Create new asset
    print("\nExample: Create new asset")
    print("(Commented out - uncomment to execute)")
    # new_asset = create_new_asset(
    #     subco="AEN",
    #     asset_type="PV",
    #     asset_id="030",
    #     name="New-Solar-Project",
    #     location="Crete",
    #     dev_pm="John Smith"
    # )
    
    # Example: Transition phase
    print("\nExample: Transition asset to new phase")
    print("(Commented out - uncomment to execute)")
    # transition_phase(
    #     asset_folder="AEN_PV025_Sunfield-Solar_Athens",
    #     new_phase="03",
    #     responsible_pm="John Smith"
    # )
    
    # Example: Manage superseded versions
    print("\nExample: Clean up superseded versions")
    print("(Commented out - uncomment to execute)")
    # manage_superseded_versions(
    #     asset_folder="AEN_PV025_Sunfield-Solar_Athens",
    #     phase_folder="02_FEASIBILITY",
    #     subfolder="Financial_Model_Development",
    #     keep_latest=1
    # )
    
    # 5. Generate document register for first asset
    if len(assets_df) > 0:
        print("\n### STEP 5: Document Register ###")
        first_asset = assets_df.iloc[0]['Asset_Folder']
        print(f"Generating document register for: {first_asset}")
        doc_df = generate_document_register(first_asset)
    
    print("\n" + "="*80)
    print(" AUTOMATION COMPLETE")
    print("="*80)

# Execute main function
if __name__ == "__main__":
    main()


# =============================================================================
# ADDITIONAL UTILITY FUNCTIONS
# =============================================================================

def find_assets_by_criteria(assets_df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Find assets matching specific criteria
    
    Example:
        find_assets_by_criteria(assets_df, Asset_Type='PV', Phase_Name='Operational')
    """
    result = assets_df.copy()
    
    for key, value in kwargs.items():
        if key in result.columns:
            result = result[result[key] == value]
    
    return result

def get_asset_timeline(asset_folder: str) -> pd.DataFrame:
    """Extract timeline from status files"""
    
    asset_path = os.path.join(ASSETS_PATH, asset_folder)
    timeline = []
    
    for file in os.listdir(asset_path):
        if file.startswith('_STATUS_'):
            file_path = os.path.join(asset_path, file)
            with open(file_path, 'r') as f:
                content = f.read()
                
                # Extract phase started
                if 'Phase Started:' in content:
                    start_line = [l for l in content.split('\n') if 'Phase Started:' in l][0]
                    start_date = start_line.split('Phase Started:')[1].strip()
                    
                    # Extract phase closed
                    closed_date = None
                    if 'Phase Closed:' in content:
                        closed_line = [l for l in content.split('\n') if 'Phase Closed:' in l][0]
                        closed_str = closed_line.split('Phase Closed:')[1].strip()
                        if closed_str != '[Will be filled when moving to next phase]':
                            closed_date = closed_str
                    
                    phase_num = file.split('_')[2][:2]
                    phase_name = PHASE_CODES.get(phase_num, 'Unknown')
                    
                    timeline.append({
                        'Phase': phase_name,
                        'Phase_Number': phase_num,
                        'Start_Date': start_date,
                        'End_Date': closed_date,
                        'Status': 'Closed' if closed_date else 'Active'
                    })
    
    df = pd.DataFrame(timeline).sort_values('Phase_Number')
    return df

def export_portfolio_report(assets_df: pd.DataFrame, output_excel: str):
    """Export comprehensive portfolio report to Excel with multiple sheets"""
    
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        # Sheet 1: Asset Inventory
        assets_df.to_excel(writer, sheet_name='Asset_Inventory', index=False)
        
        # Sheet 2: Summary by Type
        by_type = assets_df.groupby('Asset_Type').agg({
            'Asset_Folder': 'count',
            'Total_Files': 'sum',
            'Total_Size_MB': 'sum'
        }).rename(columns={'Asset_Folder': 'Count'})
        by_type.to_excel(writer, sheet_name='Summary_by_Type')
        
        # Sheet 3: Summary by Phase
        by_phase = assets_df.groupby('Phase_Name').agg({
            'Asset_Folder': 'count',
            'Total_Files': 'sum',
            'Total_Size_MB': 'sum'
        }).rename(columns={'Asset_Folder': 'Count'})
        by_phase.to_excel(writer, sheet_name='Summary_by_Phase')
        
        # Sheet 4: Summary by Subcompany
        by_subco = assets_df.groupby('Subcompany').agg({
            'Asset_Folder': 'count',
            'Total_Files': 'sum',
            'Total_Size_MB': 'sum'
        }).rename(columns={'Asset_Folder': 'Count'})
        by_subco.to_excel(writer, sheet_name='Summary_by_Subcompany')
        
        # Sheet 5: Cross-tab (Type x Phase)
        crosstab = pd.crosstab(assets_df['Asset_Type'], assets_df['Phase_Name'])
        crosstab.to_excel(writer, sheet_name='Type_Phase_Matrix')
    
    print(f"Portfolio report exported to: {output_excel}")
