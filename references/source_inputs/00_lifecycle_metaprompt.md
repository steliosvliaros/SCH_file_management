# Per-Asset Lifecycle File Management System - Metaprompt

## Context
You are designing a continuous lifecycle file management system for an asset management and development company where each asset has ONE folder that follows it from initial concept through development, construction, operations, and eventual decommissioning.

### Organization Structure
- **Total Staff**: 15 people
  - 3 Development Project Managers
  - 5 Operations & Maintenance (O&M) Project Managers
  - 7 Support staff (Finance, CEO, HR)
- **Multiple Subcompanies**: Organizational structure includes various subsidiaries

### Asset Portfolio

**Operational Assets:**
- 30 PV (Photovoltaic) Parks
- 10 Wind Farms
- 3 Hotels

**Under Development:**
- 2 Data Centers
- 3 Hydroponic Farms
- 30 PV Parks
- 2 Hotels

### Business Model
- Full lifecycle management: Concept → Development → Construction → Operations → Decommissioning
- All execution outsourced to partners/contractors
- Internal team manages entire asset lifecycle
- Small team requires complete visibility across all phases

### Technical Environment
- Windows File Server infrastructure
- Need for version control and document tracking
- Cross-functional access requirements

## Design Philosophy: Continuous Asset Lifecycle

### Core Principle
**One Asset = One Folder for Entire Life**

Each asset folder contains all phases chronologically, allowing anyone to understand the complete asset history by browsing one location.

### Key Advantages
1. **Single Source of Truth**: All information about an asset in one place
2. **No Handover Process**: Seamlessly transition between phases by adding folders
3. **Complete Audit Trail**: From feasibility study to decommissioning
4. **Simplified Access**: One permission set per asset
5. **Better for Finance**: Complete capex to opex visibility
6. **Investor-Friendly**: Due diligence in one folder
7. **Reduced Admin Overhead**: No file copying/moving between phases

## Folder Structure Principles

### Level 1: Asset Organization (SIMPLIFIED)
```
\\FileServer\AssetManagement\
├── ASSETS\                    ← All assets in ONE flat folder
│   ├── AEN_PV025_Sunfield-Solar_Athens\
│   ├── BGP_WF003_Coastal-Wind_Thessaloniki\
│   ├── GRH_DC001_Metro-Datacenter_Piraeus\
│   └── [All other assets...]
├── CORPORATE\
├── TEMPLATES\
└── ARCHIVE\
    └── [YEAR]\                ← Year-based only
```

**CRITICAL SIMPLIFICATION**:
- NO sub-categorization by asset type (folder names show type)
- NO sub-categorization by status (status files show phase)
- ALL assets in single ASSETS\ folder for entire lifecycle

### Level 2: Individual Asset Folder Structure
**Each asset has comprehensive lifecycle structure:**

```
[SUBCO]_[TYPE][ID]_[NAME]_[LOCATION]\
├── 00_ASSET_MASTER\
│   ├── Asset_Summary\
│   ├── Key_Contacts\
│   ├── Timeline_Milestones\
│   └── Quick_Reference\
├── 01_PREFEASIBILITY\
├── 02_FEASIBILITY\
├── 03_LAND_ACQUISITION\
├── 04_PERMITTING\
├── 05_DESIGN_ENGINEERING\
├── 06_FINANCING\
├── 07_PROCUREMENT\
├── 08_CONSTRUCTION\
├── 09_COMMISSIONING_COD\
├── 10_OPERATIONS\
│   ├── YEAR_[YYYY]\
│   └── YEAR_[YYYY+1]\
├── 11_CONTRACTS_LEGAL\
│   ├── Development_Phase\
│   └── Operations_Phase\
├── 12_FINANCIAL\
│   ├── Development_Phase\
│   └── Operations_Phase\
├── 13_CORRESPONDENCE\
│   ├── Development_Phase\
│   └── Operations_Phase\
└── 14_DECOMMISSIONING\
```

### Phase Status Management
Instead of moving folders, use **STATUS indicators**:
- Folder: `_STATUS_[CURRENT_PHASE].txt` in root of each asset
- Examples: `_STATUS_CONSTRUCTION.txt`, `_STATUS_OPERATIONAL.txt`

### Access Control Strategy
- **Asset-Level Permissions**: Assign permissions per asset folder
- **Phase Subfolders**: Use sub-permissions where needed
- **Read-Only After Phase Complete**: Lock completed phase folders
- **Cross-Functional Visibility**: Finance, CEO see all; PMs see assigned

## Naming Conventions

### Asset Folder Names
```
[SUBCO]_[TYPE][ID]_[NAME]_[LOCATION]
```

### Document Names
```
[SUBCO]_[TYPE][ID]_[PHASE]_[DOCTYPE]_[DESCRIPTION]_[DATE]_[VERSION]_[STATUS]
```

### Phase Codes
- PF = Prefeasibility
- FS = Feasibility  
- LA = Land Acquisition
- PM = Permitting
- DE = Design Engineering
- FN = Financing
- PR = Procurement
- CN = Construction
- CM = Commissioning
- OP = Operations
- DC = Decommissioning

## Document Type Classification

### Cross-Phase Documents
Documents that span multiple phases should be located based on primary use:
- **Contracts**: Always in `11_CONTRACTS_LEGAL\`
- **Financial Models**: Always in `12_FINANCIAL\`
- **Correspondence**: Always in `13_CORRESPONDENCE\`

### Phase-Specific Documents
Technical and execution documents in their respective phase folders.

## Workflow Procedures

### 1. New Asset Initialization
- Create asset folder in `PIPELINE\`
- Copy template structure
- Create `00_ASSET_MASTER\Asset_Summary.xlsx`
- Create `_STATUS_PIPELINE.txt`
- Assign project manager

### 2. Phase Transition (e.g., Development → Construction)
**NO FILE MOVEMENT REQUIRED**
- Update status file: Delete `_STATUS_DEVELOPMENT.txt`, Create `_STATUS_CONSTRUCTION.txt`
- Create new phase summary document in phase folder
- Set previous phase folders to read-only
- Update asset summary

### 3. COD (Construction → Operations)
**NO FILE MOVEMENT REQUIRED**
- Update status file: Delete `_STATUS_CONSTRUCTION.txt`, Create `_STATUS_OPERATIONAL.txt`
- Create first year operations folder: `10_OPERATIONS\YEAR_2025\`
- Populate with monthly subfolders
- Set construction phase to read-only
- Move asset from `UNDER_CONSTRUCTION\` to `OPERATIONAL\` (folder moves, not files)

### 4. Annual Operations Rollover
- Create new year folder: `10_OPERATIONS\YEAR_2026\`
- Previous year becomes read-only
- Archive old years (>3 years) can be compressed

### 5. Asset Disposal/Sale
- Move entire asset folder to `ARCHIVE\[YEAR]\[ASSET_TYPE]\`
- Create disposal documentation in `14_DECOMMISSIONING\`
- Maintain for retention period

## Success Criteria
The system should enable:
- **Complete Asset Understanding** in under 5 minutes by browsing one folder
- **No handover meetings** for file transfer (operational handover still needed for training)
- **Instant History**: See evolution of any document through versions
- **Simplified Due Diligence**: Send one folder link to investors/buyers
- **Easy Onboarding**: New team members can self-educate on any asset

## Key Design Decisions

### Why Operations Has Year Subfolders
Operations generates high volume documents. Annual subfolders prevent folder bloat while maintaining organization.

### Why Contracts/Financial/Correspondence Are Separate
These cross-cut all phases and need visibility across lifecycle. Separating them improves findability.

### Why Asset Master Folder
Provides executive summary and quick reference without diving into detailed phases. Essential for management reporting.

### Why Status Files Instead of Folder Movement
- Preserves complete history
- Eliminates risk of losing files during moves
- Makes current phase instantly visible
- Allows easy phase-based filtering in file explorer

## Additional Considerations
- **Backup Strategy**: Asset-level backups easier to manage
- **Search Optimization**: Windows indexing per asset folder
- **Mobile Access**: Single asset folders easier to sync to mobile
- **Collaboration**: Share one link for complete asset access
- **Scalability**: Structure works from 10 to 500+ assets
- **Compliance**: Complete audit trail in one location
- **Knowledge Retention**: Asset knowledge doesn't fragment across systems