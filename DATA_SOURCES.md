# Data Sources & Disk Notes

## Dataset
- **Name:** SPM Auditory / MoAEpilot tutorial dataset
- **Official source:** https://www.fil.ion.ucl.ac.uk/spm/data/auditory/
- **Downloaded archive:** `MoAEpilot.bids.zip` (approximately 28.7 MB at download)
- **Layout used:** BIDS/NIfTI
- **Subject used:** `sub-01`

## Files used
- Anatomical image: `sub-01/anat/sub-01_T1w.nii`
- Functional image: `sub-01/func/sub-01_task-auditory_bold.nii`
- Events table: `sub-01/func/sub-01_task-auditory_events.tsv`
- BOLD metadata: `task-auditory_bold.json`

## Functional subset
- The downloaded BIDS functional NIfTI contained **84 analysis volumes**.
- TR: **7 s**.
- The analysis modeled the auditory `listening` blocks versus rest.

## Local organization
The raw BIDS dataset is stored locally under the user's neuroimaging data directory. SPM derivatives are generated outside the Git repository.

Raw NIfTI files, SPM working images, deformation fields, first-level NIfTI maps, and other large derivatives are **not committed** to this repository.

## Files retained in GitHub
Only lightweight portfolio outputs are tracked, including:
- QC and results figures (`results/figures/`)
- peak and threshold tables (`results/tables/`)
- documentation and reproducibility metadata

## Data policy
This repository documents how the public tutorial dataset was analyzed without redistributing the raw neuroimaging dataset through GitHub.
