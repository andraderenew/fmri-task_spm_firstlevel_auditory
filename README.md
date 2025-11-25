# Task fMRI — SPM First-Level (Auditory) + FEAT replication
[![License](https://img.shields.io/github/license/andraderenew/fmri-task_spm_firstlevel_auditory)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17715106-blue)](https://doi.org/10.5281/zenodo.17715106)
[![Pages](https://img.shields.io/website?url=https%3A%2F%2Fandraderenew.github.io%2Ffmri-task_spm_firstlevel_auditory%2F)](https://andraderenew.github.io/fmri-task_spm_firstlevel_auditory/)
![Release](https://img.shields.io/github/v/release/andraderenew/fmri-task_spm_firstlevel_auditory?include_prereleases)
![Last commit](https://img.shields.io/github/last-commit/andraderenew/fmri-task_spm_firstlevel_auditory)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5627--579X-A6CE39)](https://orcid.org/0000-0001-5627-579X)
[![Google Scholar](https://img.shields.io/badge/Google%20Scholar-Profile-4285F4)](https://scholar.google.es/citations?hl=es&user=Nl3ApFEAAAAJ)

**One-line:** Classic SPM Auditory first-level GLM, with optional FSL FEAT replication to compare contrast maps and thresholds.

## Overview
Reproduce the classic **SPM Auditory** first-level GLM (single subject). Optionally replicate one contrast in **FSL FEAT** and compare thresholds.

## Data & subset
See `DATA_SOURCES.md`. Suggested: 1 subject; disk ≤ ~0.5–1 GB.

## Pipeline
SPM (realign, coreg, normalize, smooth) → GLM (conditions + 6 motion) → contrasts → threshold (FWE/FDR) → (opt) FEAT replication and map comparison.

## Results (to be filled)
- Thresholded activation map over anatomy  
- Peak table (MNI, cluster size)  
- Notes on SPM vs FEAT differences (if replicated)

## Reproducibility
- Versions: see `env/TOOL_VERSIONS.md`  
- Steps: “Preprocess in SPM → specify GLM → estimate → contrasts → export figures.”  
- Known limits: single-subject demo

## Cite this work
A `CITATION.cff` is included; add DOI after your first Zenodo-backed Release.
