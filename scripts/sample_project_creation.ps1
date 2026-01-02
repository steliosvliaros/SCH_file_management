# ====================================
# New Asset Creation Script
# ====================================
param(
    [string]$Subco = "AEN",
    [string]$Type = "PV",
    [string]$ID = "025",
    [string]$Name = "Sunfield-Solar",
    [string]$Location = "Athens",
    [string]$DevPM = "John Smith",
    [string]$DevPMEmail = "john.smith@alphaenergy.com"
)

$assetFolder = "${Subco}_${Type}${ID}_${Name}_${Location}"
$sourcePath = "TEMPLATES\ASSET_LIFECYCLE_TEMPLATE"
$destPath = "ASSETS\$assetFolder"

# Copy template
Write-Host "Creating new asset: $assetFolder" -ForegroundColor Green
Copy-Item -Path $sourcePath -Destination $destPath -Recurse

# Create initial status file
$statusContent = @"
STATUS: PIPELINE
Phase Started: $(Get-Date -Format "yyyy-MM-dd")
Responsible PM: $DevPM
PM Email: $DevPMEmail
Target Completion: $(Get-Date (Get-Date).AddMonths(3) -Format "yyyy-MM-dd")

Key Activities in Progress:
1. Initial site identification
2. Preliminary market research
3. High-level feasibility assessment

Next Milestones:
- Site visit: $(Get-Date (Get-Date).AddDays(14) -Format "yyyy-MM-dd")
- Go/No-Go Decision: $(Get-Date (Get-Date).AddMonths(2) -Format "yyyy-MM-dd")
- Board Presentation: $(Get-Date (Get-Date).AddMonths(3) -Format "yyyy-MM-dd")

Phase Closed: [Will be filled when moving to next phase]
Last Updated: $(Get-Date -Format "yyyy-MM-dd HH:mm")
Updated By: System Administrator
"@
Set-Content -Path "$destPath\_STATUS_01_PIPELINE.txt" -Value $statusContent

# Create Asset Summary from template
$csvTemplate = "TEMPLATES\EXCEL_TEMPLATES\Asset_Summary_Sheet_Template.csv"
$assetSummary = "$destPath\00_ASSET_MASTER\Asset_Summary_Sheet\${assetFolder}_Asset_Summary.csv"
Copy-Item -Path $csvTemplate -Destination $assetSummary

# Update Asset Summary with project details
$summary = Import-Csv $assetSummary
$summary | Where-Object { $_.Field -eq "Asset ID" } | ForEach-Object { $_.Value = "${Subco}_${Type}${ID}" }
$summary | Where-Object { $_.Field -eq "Asset Name" } | ForEach-Object { $_.Value = "$Name" }
$summary | Where-Object { $_.Field -eq "Location" } | ForEach-Object { $_.Value = "$Location" }
$summary | Export-Csv $assetSummary -NoTypeInformation

# Create initial contact list
$contactsContent = @"
Role,Name,Email,Phone,Company,Notes
Development PM,$DevPM,$DevPMEmail,+30 210 1234567,Alpha Energy,Primary contact
CEO,Michael Anderson,michael.anderson@alphaenergy.com,+30 210 1234560,Alpha Energy,Final approvals
Finance Director,Sarah Johnson,sarah.johnson@alphaenergy.com,+30 210 1234565,Alpha Energy,Budget and financial close
"@
Set-Content -Path "$destPath\00_ASSET_MASTER\Key_Contacts_Directory\Contacts_List.csv" -Value $contactsContent

# Create project folder shortcuts for team
$readme = @"
# $assetFolder

Created: $(Get-Date -Format "yyyy-MM-dd")
Current Phase: PIPELINE
Development PM: $DevPM

## Quick Links
- Asset Summary: 00_ASSET_MASTER\Asset_Summary_Sheet\
- Current Phase: 01_PREFEASIBILITY\
- Contacts: 00_ASSET_MASTER\Key_Contacts_Directory\

## Next Steps
1. Complete site identification
2. Conduct preliminary assessment
3. Prepare go/no-go decision materials
"@
Set-Content -Path "$destPath\README.md" -Value $readme

Write-Host "Asset created successfully at: $destPath" -ForegroundColor Green
Write-Host "Initial status file created" -ForegroundColor Green
Write-Host "Asset summary initialized" -ForegroundColor Green
Write-Host "Contact list created" -ForegroundColor Green

# Open asset folder
Start-Process explorer.exe -ArgumentList $destPath