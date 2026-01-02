# Asset Management Company - Per-Asset Lifecycle File System

## Table of Contents
1. [Overview](#overview)
2. [Folder Structure](#folder-structure)
3. [Naming Conventions](#naming-conventions)
4. [Workflow Procedures](#workflow-procedures)
5. [Quick Reference](#quick-reference)
6. [Maintenance](#maintenance)

---

## Overview

This file management system uses a **continuous lifecycle approach** where each asset has ONE folder containing all phases from concept through operations to decommissioning.

### Core Philosophy
**"One Asset, One Folder, One Location, Complete History"**

### Key Benefits
✓ **No Folder Movement**: Assets stay in one location forever  
✓ **No File Copying**: Documents never move from phase folders  
✓ **Status Tracking**: Simple text files show current phase  
✓ **Complete Visibility**: Entire asset history in one place  
✓ **Ultra-Simple**: No complex category management  
✓ **Audit-Friendly**: Complete trail for compliance  

---

## Folder Structure

### Level 1: Root Organization

```
\\FileServer\AssetManagement\
├── ASSETS\
├── CORPORATE\
├── TEMPLATES\
└── ARCHIVE\
```

### Level 2: All Assets in One Place

**CRITICALLY SIMPLE: No sub-categorization needed!**

```
ASSETS\
├── AEN_PV025_Sunfield-Solar_Athens\
├── AEN_PV026_Mountain-Solar_Crete\
├── BGP_WF003_Coastal-Wind_Thessaloniki\
├── BGP_WF004_Highland-Wind_Patras\
├── GRH_DC001_Metro-Datacenter_Piraeus\
├── DHO_HTL003_Seaside-Resort_Santorini\
├── DHO_HTL005_Urban-Hotel_Athens\
├── EAG_HF002_Urban-Greens_Patras\
└── [All other assets...]
```

**Why this works:**
- Folder names clearly identify asset type (PV, WF, HTL, DC, HF)
- Status files inside each folder show current phase
- No need to move folders between categories
- Simple alphabetical sorting keeps related assets together
- Windows search works perfectly across all assets

### Sorting & Filtering

**By Asset Type:**
- Sort alphabetically: all PV projects together, all Wind together, etc.
- Or use Windows search: `*_PV*` finds all solar projects

**By Status:**
- Search for `_STATUS_04_OPERATIONAL.txt` to find all operational assets
- Search for `_STATUS_02_UNDER_DEVELOPMENT.txt` for development projects

**By Subcompany:**
- Sort alphabetically: all AEN projects together
- Or search: `AEN_*` finds all Alpha Energy projects

### Archive Structure (Simplified)

```
ARCHIVE\
├── 2024\
│   ├── AEN_PV018_Cancelled-Project_Athens\
│   └── BGP_WF002_Sold-Project_Larissa\
├── 2025\
│   └── [Archived assets from 2025]
└── 2026\
    └── [Future archives]
```

**Archival Reasons:**
- Sold: Asset sold to another company
- Decommissioned: Asset end-of-life
- Cancelled: Project cancelled during development

### Level 3: Complete Asset Lifecycle Structure

**Each asset folder follows this comprehensive structure:**

```
[SUBCO]_[TYPE][ID]_[NAME]_[LOCATION]\
│
├── _STATUS_01_PIPELINE.txt             ← Status files (audit trail)
├── _STATUS_02_UNDER_DEVELOPMENT.txt
├── _STATUS_03_UNDER_CONSTRUCTION.txt
├── _STATUS_04_OPERATIONAL.txt
│
├── 00_ASSET_MASTER\                    ← Executive Summary & Quick Reference
│   ├── Asset_Summary_Sheet\
│   ├── Key_Contacts_Directory\
│   ├── Timeline_Milestones\
│   ├── Quick_Financial_Summary\
│   └── Document_Index\
│
├── 01_PREFEASIBILITY\                  ← Initial Concept Phase
│   ├── Site_Identification\
│   ├── Preliminary_Assessment\
│   ├── Market_Overview\
│   └── Go_No-Go_Decision\
│
├── 02_FEASIBILITY\                     ← Detailed Feasibility
│   ├── Site_Assessment\
│   ├── Technical_Feasibility\
│   ├── Market_Analysis\
│   ├── Financial_Model_Development\
│   ├── Risk_Assessment\
│   └── Feasibility_Report\
│
├── 03_LAND_ACQUISITION\                ← Securing Land Rights
│   ├── Title_Search_Due_Diligence\
│   ├── Negotiations\
│   ├── Contracts_Agreements\
│   ├── Surveys_Maps\
│   └── Legal_Documentation\
│
├── 04_PERMITTING\                      ← All Regulatory Approvals
│   ├── Environmental_Permits\
│   ├── Building_Construction_Permits\
│   ├── Grid_Connection_Permits\
│   ├── Operating_Licenses\
│   ├── Authority_Correspondence\
│   └── Permit_Register\
│
├── 05_DESIGN_ENGINEERING\              ← Technical Design
│   ├── Electrical_Design\
│   ├── Civil_Structural\
│   ├── Mechanical_HVAC\
│   ├── Technical_Specifications\
│   ├── Design_Reviews\
│   └── As_Designed_Drawings\
│
├── 06_FINANCING\                       ← Financial Close
│   ├── Financing_Strategy\
│   ├── Lender_Documentation\
│   ├── Term_Sheets\
│   ├── Financial_Close_Documents\
│   ├── Sponsor_Equity\
│   └── Financial_Model_Final\
│
├── 07_PROCUREMENT\                     ← Equipment & Contractor Selection
│   ├── Procurement_Strategy\
│   ├── RFQ_RFP_Documents\
│   ├── Bids_Proposals\
│   ├── Technical_Evaluations\
│   ├── Commercial_Evaluations\
│   ├── Contracts_Awarded\
│   └── Purchase_Orders\
│
├── 08_CONSTRUCTION\                    ← Build Phase
│   ├── Construction_Schedule\
│   ├── Progress_Reports\
│   ├── Site_Documentation\
│   ├── QA_QC\
│   ├── Safety_HSE\
│   ├── Change_Orders\
│   └── As_Built_Drawings\
│
├── 09_COMMISSIONING_COD\               ← Testing & Commercial Operation
│   ├── Commissioning_Plan\
│   ├── Test_Procedures\
│   ├── Test_Reports\
│   ├── Punch_List\
│   ├── Completion_Certificates\
│   ├── COD_Documentation\
│   ├── Warranty_Certificates\
│   ├── O&M_Manuals\
│   └── Training_Materials\
│
├── 10_OPERATIONS\                      ← Ongoing Operations (Organized by Year)
│   ├── YEAR_2025\
│   ├── YEAR_2026\
│   ├── Asset_Information\
│   ├── Maintenance_Strategy\
│   ├── Performance_Monitoring\
│   └── Compliance_Regulatory\
│
├── 11_CONTRACTS_LEGAL\                 ← All Contracts (Entire Lifecycle)
│   ├── Development_Phase\
│   ├── Construction_Phase\
│   ├── Operations_Phase\
│   ├── Financing_Agreements\
│   └── Contract_Register\
│
├── 12_FINANCIAL\                       ← All Financial (Entire Lifecycle)
│   ├── Development_Phase\
│   ├── Construction_Phase\
│   ├── Operations_Phase\
│   ├── Financial_Models\
│   ├── Tax_Accounting\
│   └── Audit_Documents\
│
├── 13_CORRESPONDENCE\                  ← All Communications (Entire Lifecycle)
│   ├── Development_Phase\
│   ├── Construction_Phase\
│   ├── Operations_Phase\
│   └── Meeting_Minutes\
│
└── 14_DECOMMISSIONING\                 ← End of Life (Future)
    ├── Decommissioning_Plan\
    ├── Environmental_Restoration\
    ├── Equipment_Disposal\
    └── Site_Closure\
```

---

## Naming Conventions

### Asset Folder Names

```
[SUBCO]_[TYPE][ID]_[PROJECT-NAME]_[LOCATION]

Components:
- SUBCO: 2-4 letter subcompany code
- TYPE: Asset type (PV, WF, HTL, DC, HF)
- ID: Unique 3-digit sequential number
- PROJECT-NAME: Short descriptive name (use hyphens, not spaces)
- LOCATION: City or region name

Examples:
AEN_PV025_Sunfield-Solar_Athens
BGP_WF008_Coastal-Wind_Thessaloniki
GRH_DC001_Metro-Datacenter_Piraeus
DHO_HTL003_Seaside-Resort_Santorini
EAG_HF002_Urban-Greens_Patras
```

### Document Naming Convention

```
[SUBCO]_[TYPE][ID]_[PHASE]_[DOCTYPE]_[DESCRIPTION]_[DATE]_[VERSION]_[STATUS]

Components:
- SUBCO: Subcompany code (matches folder)
- TYPE+ID: Asset identifier (matches folder)
- PHASE: 2-letter phase code
- DOCTYPE: Document type code
- DESCRIPTION: Brief description (use hyphens)
- DATE: YYYYMMDD format
- VERSION: v01, v02, v03, etc.
- STATUS: DRAFT, REVIEW, REVISED, FINAL, APPROVED

Examples:
AEN_PV025_FS_FST_Technical-Feasibility-Study_20230215_v02_FINAL.pdf
AEN_PV025_CN_REP_Monthly-Progress-Report_20240831_v01_FINAL.pdf
AEN_PV025_OP_REP_Production-Report_20250131_v01_FINAL.xlsx
BGP_WF008_DE_TEC_Single-Line-Diagram_20231120_v04_APPROVED.dwg
```

### Phase Codes

| Code | Phase | Typical Duration |
|------|-------|------------------|
| PF | Prefeasibility | 1-3 months |
| FS | Feasibility | 3-6 months |
| LA | Land Acquisition | 3-12 months |
| PM | Permitting | 6-18 months |
| DE | Design & Engineering | 4-8 months |
| FN | Financing | 3-6 months |
| PR | Procurement | 2-4 months |
| CN | Construction | 8-18 months |
| CM | Commissioning & COD | 1-3 months |
| OP | Operations | 20-30 years |
| DC | Decommissioning | 6-12 months |

### Document Type Codes

| Code | Category | Examples |
|------|----------|----------|
| FST | Feasibility Study | Market analysis, technical studies |
| CNT | Contract | All legal agreements |
| PER | Permit/License | Environmental permits, building permits |
| FIN | Financial | Budgets, invoices, financial statements |
| TEC | Technical | Drawings, specifications, calculations |
| REP | Report | Progress reports, performance reports |
| COR | Correspondence | Letters, emails, meeting minutes |
| LEG | Legal | Legal opinions, due diligence |
| PRO | Procurement | RFPs, bids, purchase orders |
| HSE | Health/Safety/Environment | Safety plans, incident reports |
| COM | Commissioning | Test reports, completion certificates |
| MNT | Maintenance | Work orders, maintenance logs |
| MAN | Manual | O&M manuals, equipment manuals |

### Subcompany Codes

**Update these with your actual subcompanies:**

| Code | Subcompany Name | Focus |
|------|-----------------|-------|
| AEN | Alpha Energy | Solar PV |
| BGP | Beta Green Power | Wind |
| GRH | Gamma Renewables Holdings | Mixed portfolio |
| DHO | Delta Hospitality Operations | Hotels |
| EAG | Epsilon Agritech | Hydroponic farms |
| ZDC | Zeta Datacenters | Data centers |

---

## Workflow Procedures

### 1. New Asset Initialization

**When**: New opportunity identified

**Steps**:
1. Determine appropriate asset type and assign next ID number
2. Create folder name following convention
3. Create folder in `ASSETS\`
4. Copy template structure from `TEMPLATES\ASSET_LIFECYCLE_TEMPLATE\`
5. Create initial status file: `_STATUS_01_PIPELINE.txt`
6. Fill out `00_ASSET_MASTER\Asset_Summary_Sheet.xlsx`
7. Assign Development PM
8. Set up permissions

**PowerShell**:
```powershell
$assetFolder = "AEN_PV025_Sunfield-Solar_Athens"
$source = "TEMPLATES\ASSET_LIFECYCLE_TEMPLATE"
$destination = "ASSETS\$assetFolder"
Copy-Item -Path $source -Destination $destination -Recurse
```

**CRITICAL: Asset folder NEVER moves from ASSETS\ - it stays there forever!**

### 2. Phase Progression (Status File Updates Only)

**Key Principle**: Asset folder NEVER moves - only status files change!

**Example: Pipeline → Feasibility**

**Steps**:
1. Complete prefeasibility deliverables
2. Hold go/no-go decision meeting
3. If GO:
   - Close `_STATUS_01_PIPELINE.txt` with end date
   - Create `_STATUS_02_UNDER_DEVELOPMENT.txt`
   - Set `01_PREFEASIBILITY\` folder to read-only
   - Start working in `02_FEASIBILITY\`
4. Update `00_ASSET_MASTER\Timeline_Milestones.xlsx`

**PowerShell**:
```powershell
# Navigate to asset folder
cd "ASSETS\AEN_PV025_Sunfield-Solar_Athens"

# Close pipeline status
$pipelineStatus = Get-Content "_STATUS_01_PIPELINE.txt"
$pipelineStatus += "`nPhase Closed: 2023-03-01"
$pipelineStatus += "`nClosed By: John Smith"
Set-Content "_STATUS_01_PIPELINE.txt" -Value $pipelineStatus

# Create development status
$devStatus = @"
STATUS: UNDER DEVELOPMENT - FEASIBILITY
Phase Started: 2023-03-01
Responsible PM: John Smith
Target Completion: 2023-08-31

Key Activities in Progress:
1. Detailed technical feasibility study
2. Financial model development
3. Preliminary permit research
4. Land acquisition negotiations

Next Milestones:
- Feasibility Report Complete: 2023-07-31
- Board Approval for Development: 2023-08-15

Phase Closed: [Will be filled when moving to next phase]
Last Updated: 2023-03-01
Updated By: John Smith
"@
Set-Content "_STATUS_02_UNDER_DEVELOPMENT.txt" -Value $devStatus

# Set completed phase to read-only
Get-ChildItem "01_PREFEASIBILITY" -Recurse | ForEach-Object { $_.IsReadOnly = $true }
```

**ZERO folder movement - just update status files!**

### 3. Major Phase Transitions

**All transitions work the same way: close old status, create new status, set phases read-only**

#### Financial Close (Development → Construction)
**Trigger**: Financial Close achieved

```powershell
cd "ASSETS\AEN_PV025_Sunfield-Solar_Athens"

# Close development status
$devStatus = Get-Content "_STATUS_02_UNDER_DEVELOPMENT.txt"
$devStatus += "`nPhase Closed: 2024-12-15"
$devStatus += "`nClosed By: John Smith"
Set-Content "_STATUS_02_UNDER_DEVELOPMENT.txt" -Value $devStatus

# Create construction status
$cnStatus = @"
STATUS: UNDER CONSTRUCTION
Phase Started: 2024-12-15
Responsible PM: John Smith (Development) + Maria Lopez (O&M oversight)
Target COD: 2025-12-31

Key Activities in Progress:
1. Procurement activities
2. EPC contractor mobilization
3. Construction execution
4. Commissioning preparation

Next Milestones:
- Construction Start: 2025-01-15
- Mechanical Complete: 2025-10-31
- COD: 2025-12-31

Phase Closed: [Will be filled at COD]
Last Updated: 2024-12-15
Updated By: John Smith
"@
Set-Content "_STATUS_03_UNDER_CONSTRUCTION.txt" -Value $cnStatus

# Set development phases to read-only
$completedPhases = @("01_PREFEASIBILITY", "02_FEASIBILITY", "03_LAND_ACQUISITION", 
                     "04_PERMITTING", "05_DESIGN_ENGINEERING", "06_FINANCING")
foreach ($phase in $completedPhases) {
    Get-ChildItem $phase -Recurse | ForEach-Object { $_.IsReadOnly = $true }
}
```

#### COD (Construction → Operations)
**Trigger**: Commercial Operation Date

```powershell
cd "ASSETS\AEN_PV025_Sunfield-Solar_Athens"

# Close construction status
$cnStatus = Get-Content "_STATUS_03_UNDER_CONSTRUCTION.txt"
$cnStatus += "`nPhase Closed: 2025-12-31"
$cnStatus += "`nClosed By: John Smith & Maria Lopez"
Set-Content "_STATUS_03_UNDER_CONSTRUCTION.txt" -Value $cnStatus

# Create operational status
$opsStatus = @"
STATUS: OPERATIONAL
COD: 2025-12-31
Phase Started: 2026-01-01
Responsible PM: Maria Lopez (O&M)

Asset Information:
- Capacity: 50 MWp
- PPA: 25 years from COD
- O&M Contractor: [Name]
- Performance Guarantee: 85% PR

Key Activities:
1. Daily performance monitoring
2. Preventive maintenance execution
3. Revenue optimization
4. Asset management

Annual Targets:
- Production: 85,000 MWh/year
- Availability: >99%
- Performance Ratio: >85%

Phase Closed: [To be filled at decommissioning]
Last Updated: 2026-01-01
Updated By: Maria Lopez
"@
Set-Content "_STATUS_04_OPERATIONAL.txt" -Value $opsStatus

# Create first operations year folder
New-Item -ItemType Directory -Path "10_OPERATIONS\YEAR_2026"

# Set construction phases to read-only
$completedPhases = @("07_PROCUREMENT", "08_CONSTRUCTION", "09_COMMISSIONING_COD")
foreach ($phase in $completedPhases) {
    Get-ChildItem $phase -Recurse | ForEach-Object { $_.IsReadOnly = $true }
}
```

### 4. Finding Assets by Status

**Windows Explorer Method**:
```
1. Open ASSETS folder
2. In search box, type: "_STATUS_04_OPERATIONAL.txt"
3. Results show all operational assets
```

**PowerShell Method**:
```powershell
# Find all operational assets
Get-ChildItem "ASSETS\" -Recurse -Filter "_STATUS_04_OPERATIONAL.txt" | 
    Select-Object @{Name="Asset";Expression={$_.Directory.Name}}

# Find all assets under construction
Get-ChildItem "ASSETS\" -Recurse -Filter "_STATUS_03_UNDER_CONSTRUCTION.txt" | 
    Select-Object @{Name="Asset";Expression={$_.Directory.Name}}
```

### 5. Operations Phase Management

**Annual Rollover Process**:

```powershell
cd "ASSETS\AEN_PV025_Sunfield-Solar_Athens\10_OPERATIONS"

# Create new year folder
$newYear = "YEAR_2027"
New-Item -ItemType Directory -Path $newYear

# Create monthly folders
$months = @("01_January", "02_February", "03_March", "04_April", "05_May", "06_June",
            "07_July", "08_August", "09_September", "10_October", "11_November", "12_December")

foreach ($month in $months) {
    $monthPath = Join-Path $newYear $month
    New-Item -ItemType Directory -Path $monthPath
    
    # Create standard subfolders
    New-Item -ItemType Directory -Path "$monthPath\Production_Data"
    New-Item -ItemType Directory -Path "$monthPath\Maintenance_Logs"
    New-Item -ItemType Directory -Path "$monthPath\Inspections"
    New-Item -ItemType Directory -Path "$monthPath\Work_Orders"
    New-Item -ItemType Directory -Path "$monthPath\Reports"
}

# Set previous year to read-only
Get-ChildItem "YEAR_2026" -Recurse | ForEach-Object { $_.IsReadOnly = $true }
```

### 6. Archiving

**When to Archive**:
- Asset sold: Move to `ARCHIVE\[YEAR]\`
- Asset decommissioned: Move to `ARCHIVE\[YEAR]\`
- Project cancelled: Move to `ARCHIVE\[YEAR]\`

**Archive Process**:
```powershell
# Example: Asset sold in 2030
$assetFolder = "ASSETS\AEN_PV025_Sunfield-Solar_Athens"
$archiveYear = "ARCHIVE\2030"

# Create archive year folder if needed
New-Item -ItemType Directory -Path $archiveYear -Force

# Move entire asset folder to archive
Move-Item -Path $assetFolder -Destination $archiveYear

# Rename to indicate reason
Rename-Item "$archiveYear\AEN_PV025_Sunfield-Solar_Athens" `
            "AEN_PV025_Sunfield-Solar_Athens_[SOLD]"
```

**Archive Naming Convention**:
- `[SOLD]` - Asset sold to another company
- `[DECOMMISSIONED]` - Asset end-of-life
- `[CANCELLED]` - Project cancelled during development

---

## Quick Reference

### "Where do I save...?"

| Document Type | Location | Example Path |
|---------------|----------|--------------|
| Feasibility study | `ASSETS\[ASSET]\02_FEASIBILITY\Feasibility_Report\` | 02_FEASIBILITY\Feasibility_Report\Technical_Study.pdf |
| Land contract | `ASSETS\[ASSET]\11_CONTRACTS_LEGAL\Development_Phase\Land_Agreements\` | 11_CONTRACTS_LEGAL\Development_Phase\Land_Agreements\Lease.pdf |
| Building permit | `ASSETS\[ASSET]\04_PERMITTING\Building_Construction_Permits\` | 04_PERMITTING\Building_Construction_Permits\Permit_Approved.pdf |
| Construction photo | `ASSETS\[ASSET]\08_CONSTRUCTION\Site_Documentation\Photos\` | 08_CONSTRUCTION\Site_Documentation\Photos\2024-08\photo.jpg |
| As-built drawing | `ASSETS\[ASSET]\08_CONSTRUCTION\As_Built_Drawings\` | 08_CONSTRUCTION\As_Built_Drawings\Final_Layout.dwg |
| Monthly production | `ASSETS\[ASSET]\10_OPERATIONS\YEAR_2025\01_January\Production_Data\` | 10_OPERATIONS\YEAR_2025\01_January\Production_Data\Daily_Gen.xlsx |

### "What phase is this asset in?"

Look for the highest numbered status file:
- `_STATUS_01_PIPELINE.txt` only = Pipeline
- `_STATUS_02_UNDER_DEVELOPMENT.txt` = Under Development
- `_STATUS_03_UNDER_CONSTRUCTION.txt` = Under Construction
- `_STATUS_04_OPERATIONAL.txt` = Operational

Or open `00_ASSET_MASTER\Asset_Summary_Sheet.xlsx`

### "How do I find all [type] assets?"

**Windows Explorer**: Sort ASSETS folder alphabetically
- All `AEN_PV*` projects together
- All `BGP_WF*` projects together
- All `DHO_HTL*` projects together

**Windows Search**: 
- Type `*_PV*` to find all PV projects
- Type `*_WF*` to find all Wind projects
- Type `AEN_*` to find all Alpha Energy projects

### "How do I find all operational assets?"

**Windows Search in ASSETS folder**:
```
_STATUS_04_OPERATIONAL.txt
```

**Or PowerShell**:
```powershell
Get-ChildItem "ASSETS\" -Recurse -Filter "_STATUS_04_OPERATIONAL.txt"
```

---

## Automation Scripts

### PowerShell Scripts

#### 1. Bulk Asset Status Report

```powershell
# Get status of all assets
$assetsPath = "\\FileServer\AssetManagement\ASSETS"
$report = @()

Get-ChildItem $assetsPath -Directory | ForEach-Object {
    $assetFolder = $_
    
    # Find highest status file
    $statusFiles = Get-ChildItem $assetFolder.FullName -Filter "_STATUS_*.txt"
    $currentStatus = $statusFiles | Sort-Object Name -Descending | Select-Object -First 1
    
    if ($currentStatus) {
        $content = Get-Content $currentStatus.FullName -Raw
        $phaseStarted = ($content | Select-String "Phase Started: (.+)").Matches.Groups[1].Value
        $pm = ($content | Select-String "Responsible PM: (.+)").Matches.Groups[1].Value
        
        $report += [PSCustomObject]@{
            Asset = $assetFolder.Name
            Status = $currentStatus.Name
            Phase_Started = $phaseStarted
            PM = $pm
        }
    }
}

$report | Export-Csv "Asset_Status_Report_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Report generated with $($report.Count) assets"
```

#### 2. Automated Monthly Operations Folder Creation

```powershell
# Create operations folders for new month
param(
    [string]$Year = (Get-Date).Year,
    [string]$Month = (Get-Date).ToString("MM_MMMM")
)

$operationalAssets = Get-ChildItem "ASSETS\" -Directory | 
    Where-Object { Test-Path "$($_.FullName)\_STATUS_04_OPERATIONAL.txt" }

foreach ($asset in $operationalAssets) {
    $opsPath = Join-Path $asset.FullName "10_OPERATIONS\YEAR_$Year\$Month"
    
    if (-not (Test-Path $opsPath)) {
        New-Item -ItemType Directory -Path $opsPath | Out-Null
        
        # Create standard subfolders
        $subfolders = @("Production_Data", "Maintenance_Logs", "Inspections", "Work_Orders", "Reports")
        foreach ($sub in $subfolders) {
            New-Item -ItemType Directory -Path "$opsPath\$sub" | Out-Null
        }
        
        Write-Host "Created operations folders for $($asset.Name)"
    }
}
```

#### 3. Automated Version Cleanup

```powershell
# Clean up old versions across all assets
$assetsPath = "ASSETS\"

Get-ChildItem $assetsPath -Directory | ForEach-Object {
    $asset = $_
    Write-Host "Processing $($asset.Name)..."
    
    # Process each phase folder
    Get-ChildItem $asset.FullName -Directory | Where-Object { $_.Name -match '^\d{2}_' } | ForEach-Object {
        $phase = $_
        
        # Process each subfolder
        Get-ChildItem $phase.FullName -Directory -Recurse | ForEach-Object {
            $folder = $_
            
            # Skip _SUPERSEDED folders
            if ($folder.Name -eq '_SUPERSEDED') { return }
            
            # Group files by base name
            $files = Get-ChildItem $folder.FullName -File | 
                Where-Object { $_.Name -notmatch 'FINAL|APPROVED' } |
                Group-Object { ($_.Name -split '_')[0..4] -join '_' }
            
            foreach ($group in $files) {
                if ($group.Count -gt 1) {
                    # Create _SUPERSEDED if needed
                    $supersededPath = Join-Path $folder.FullName '_SUPERSEDED'
                    if (-not (Test-Path $supersededPath)) {
                        New-Item -ItemType Directory -Path $supersededPath | Out-Null
                    }
                    
                    # Keep only latest version
                    $sorted = $group.Group | Sort-Object LastWriteTime -Descending
                    $sorted[1..($sorted.Count-1)] | ForEach-Object {
                        Move-Item $_.FullName -Destination $supersededPath -Force
                        Write-Host "  Moved to _SUPERSEDED: $($_.Name)"
                    }
                }
            }
        }
    }
}
```

#### 4. Asset Portfolio Statistics

```powershell
# Generate portfolio statistics
$assets = Get-ChildItem "ASSETS\" -Directory

$stats = @{
    Total = $assets.Count
    ByType = @{}
    ByPhase = @{}
    BySubco = @{}
}

foreach ($asset in $assets) {
    # Parse folder name
    $parts = $asset.Name.Split('_')
    $subco = $parts[0]
    $type = ($parts[1] -replace '\d', '')
    
    # Count by type
    if (-not $stats.ByType.ContainsKey($type)) {
        $stats.ByType[$type] = 0
    }
    $stats.ByType[$type]++
    
    # Count by subco
    if (-not $stats.BySubco.ContainsKey($subco)) {
        $stats.BySubco[$subco] = 0
    }
    $stats.BySubco[$subco]++
    
    # Count by phase
    $statusFiles = Get-ChildItem $asset.FullName -Filter "_STATUS_*.txt"
    $currentPhase = ($statusFiles | Sort-Object Name -Descending | Select-Object -First 1).Name -replace '_STATUS_(\d{2}).*', '$1'
    
    if (-not $stats.ByPhase.ContainsKey($currentPhase)) {
        $stats.ByPhase[$currentPhase] = 0
    }
    $stats.ByPhase[$currentPhase]++
}

# Display results
Write-Host "`nPORTFOLIO STATISTICS" -ForegroundColor Cyan
Write-Host "===================="
Write-Host "Total Assets: $($stats.Total)"
Write-Host "`nBy Asset Type:"
$stats.ByType.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host "  $($_.Key): $($_.Value)"
}
Write-Host "`nBy Phase:"
$stats.ByPhase.GetEnumerator() | Sort-Object Name | ForEach-Object {
    $phaseName = switch ($_.Key) {
        '01' { 'Pipeline' }
        '02' { 'Under Development' }
        '03' { 'Under Construction' }
        '04' { 'Operational' }
    }
    Write-Host "  $phaseName: $($_.Value)"
}
Write-Host "`nBy Subcompany:"
$stats.BySubco.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host "  $($_.Key): $($_.Value)"
}
```

#### 5. Document Count by Phase

```powershell
# Count documents in each phase across all assets
param([string]$AssetFolder = $null)

$path = if ($AssetFolder) { "ASSETS\$AssetFolder" } else { "ASSETS\" }

$results = @()

Get-ChildItem $path -Directory | ForEach-Object {
    $asset = $_
    $assetName = $asset.Name
    
    # Process each phase folder
    Get-ChildItem $asset.FullName -Directory | Where-Object { $_.Name -match '^\d{2}_' } | ForEach-Object {
        $phase = $_
        $fileCount = (Get-ChildItem $phase.FullName -File -Recurse | Measure-Object).Count
        
        if ($fileCount -gt 0) {
            $results += [PSCustomObject]@{
                Asset = $assetName
                Phase = $phase.Name
                File_Count = $fileCount
            }
        }
    }
}

$results | Export-Csv "Document_Count_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
$results | Format-Table -AutoSize
```

### Python Scripts (see Jupyter Notebook for full implementation)

The comprehensive Python notebook includes:
- Asset discovery and inventory
- Portfolio metrics and dashboards
- Automated file operations
- Document tracking and reporting
- Phase transition automation
- Version management
- Visualization generation

**Location**: `TEMPLATES\SYSTEM_DOCUMENTATION\Asset_Management_Automation.ipynb`

## Maintenance

### Daily Tasks
- [ ] Save documents in correct phase folders
- [ ] Use proper naming conventions
- [ ] Update Asset Master when major events occur

### Weekly Tasks
- [ ] Run version cleanup script
- [ ] Update Asset Summary Sheets for active projects
- [ ] Review work orders and maintenance logs

### Monthly Tasks
- [ ] Run automated monthly folder creation script
- [ ] Generate portfolio statistics
- [ ] Archive previous month (set to read-only)
- [ ] Review status files for accuracy
- [ ] Generate document count report

### Quarterly Tasks
- [ ] Run Python automation notebook for full metrics
- [ ] Audit random sample of assets for compliance
- [ ] Review folder sizes and archive old operations data
- [ ] Update templates if needed
- [ ] Train new staff on system
- [ ] Generate visualization dashboard

### Annual Tasks
- [ ] Run annual rollover script for operations folders
- [ ] Compress operations data >3 years old
- [ ] Full system audit with Python scripts
- [ ] Review and update this documentation
- [ ] Archive closed/sold/cancelled assets
- [ ] Generate annual portfolio report

---

## Access Permissions Guide

### Asset-Level Permissions

| Role | All Assets | Specific Notes |
|------|-----------|----------------|
| CEO | Full access | All assets, all folders |
| Finance Director | Full access | All assets, all folders |
| Dev PM (assigned) | Full access | Assigned assets only |
| Dev PM (not assigned) | Read-only | Can view all for reference |
| O&M PM (assigned) | Full access | Assigned operational assets |
| O&M PM (not assigned) | Read-only | Can view all for reference |
| HR | Limited | Corporate folders only |

### Phase-Level Permissions

**During Development**: Dev PM has full access to phases 01-09  
**During Operations**: O&M PM has full access to phases 10+  
**Completed Phases**: Set to read-only after phase complete

**Financial Folders**: Finance always has full access  
**Contracts**: Legal/Finance have full access, PMs read-only after signing

---

## Tips for Success

### For Development PMs
✓ Asset folder NEVER moves - stays in ASSETS\ forever  
✓ Update status files, don't move folders  
✓ Keep phase folders organized from day one  
✓ Set completed phases to read-only  
✓ Update Asset Master regularly  

### For O&M PMs
✓ Find your assets by searching for `_STATUS_04_OPERATIONAL.txt`  
✓ Reference Asset Information frequently  
✓ Create monthly folders at month start  
✓ Document everything in phase 10_OPERATIONS  

### For Finance
✓ All assets in one ASSETS\ folder - easy to track  
✓ Use 12_FINANCIAL\ folder exclusively  
✓ Update financial models with actuals  
✓ Link to source documents in phase folders  

### For Everyone
✓ **ASSETS NEVER MOVE** - they stay in ASSETS\ folder permanently  
✓ Status files show current phase  
✓ Use Windows search to find assets by type or status  
✓ Follow naming conventions strictly  
✓ When in doubt, check Asset Master folder  

---

## Support & Feedback

**Questions about the system?**
- Email: [filemanagement@yourcompany.com]
- Teams Channel: #file-management
- Documentation: `TEMPLATES\SYSTEM_DOCUMENTATION\`

**Found an issue or have a suggestion?**
- Use feedback form in Templates folder
- Contact IT/Admin team

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | 2025-01-01 | System Admin | Initial per-asset lifecycle system |
| v2.0 | 2025-01-02 | System Admin | Simplified: removed category folders, no folder movement |

---

*This document is the definitive guide to our file management system. All staff must follow these procedures.*

**Last Updated: January 2025**