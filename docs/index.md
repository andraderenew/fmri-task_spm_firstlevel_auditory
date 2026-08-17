# Task fMRI: SPM25 + FSL FEAT Auditory Replication

**Goal:** Reproduce the classic SPM Auditory first-level GLM in two software ecosystems and compare the same `Listening > Rest` contrast.

## Snapshot
- **Dataset:** SPM Auditory / MoAEpilot
- **Subject:** sub-01
- **Volumes:** 84
- **TR:** 7 s
- **Tools:** MATLAB R2025b, SPM25, FSL FEAT 6.0.7.12
- **Status:** complete
- **Last updated:** 2026-07-15

## SPM25 analysis
- Realignment and reslicing
- Descending slice timing, 64 slices, reference slice 32
- T1-to-EPI coregistration
- Segmentation and MNI normalization
- 3 mm isotropic functional output
- 6 mm FWHM smoothing
- First-level GLM with six motion nuisance regressors
- Contrast: **Listening > Rest**
- Inference: voxel-level whole-brain FWE p < 0.05
- Observed threshold: **T > 5.296299**

## FSL FEAT replication
- MCFLIRT motion correction
- Regular-descending slice timing
- BET brain extraction
- SUSAN smoothing, 6 mm FWHM
- High-pass filter, 128 s
- FILM prewhitening
- Double-gamma HRF
- Six motion nuisance EVs
- FLIRT registration to T1 and MNI152
- Contrast: **Listening > Rest**
- Inference: cluster-forming **Z > 3.1**, cluster significance **p < 0.05**

## Results

### SPM motion QC
![SPM motion QC](https://raw.githubusercontent.com/andraderenew/fmri-task_spm_firstlevel_auditory/main/results/figures/fig0_spm_motion_qc.png)

### SPM thresholded activation
![SPM activation](https://raw.githubusercontent.com/andraderenew/fmri-task_spm_firstlevel_auditory/main/results/figures/fig1_spm_activation_map.png)

### SPM maximum-intensity projections
![SPM MIP](https://raw.githubusercontent.com/andraderenew/fmri-task_spm_firstlevel_auditory/main/results/figures/fig2_spm_mip.png)

### FSL FEAT thresholded activation
![FSL FEAT activation](https://raw.githubusercontent.com/andraderenew/fmri-task_spm_firstlevel_auditory/main/results/figures/fig3_fsl_feat_activation_map.png)

### Cross-software summary
![Cross-software peak-coordinate comparison](https://raw.githubusercontent.com/andraderenew/fmri-task_spm_firstlevel_auditory/main/results/figures/fig4_cross_software_summary.png)

The SPM and FEAT results are compared qualitatively at the pattern level.
Their T/Z statistics, cluster sizes, and significance values are not directly
interchangeable because the inferential procedures differ.

Peak-coordinate correspondence is approximate because SPM MNI and FSL MNI152 normalized coordinates are not guaranteed to represent identical template geometry; no voxelwise overlap analysis is claimed.

## Statistical summary

### SPM25
- Largest clusters: 403 and 213 voxels
- Peaks: `[-63, -28, 14]` and `[57, -22, 11]`
- Peak T values: approximately 11.87

### FSL FEAT
- Left dominant cluster: 863 voxels, Z max 10.5, peak `[-61.1, -27.0, 8.85]`
- Right dominant cluster: 718 voxels, Z max 10.3, peak `[58.7, -22.8, 5.68]`

Both pipelines recovered strong bilateral auditory activation. This is a conceptual replication rather than an expectation of exact voxelwise equivalence because the packages use different temporal models, registration strategies, statistical images, and inference procedures.

## Reproducibility and archive status

The repository preserves completed-result figures, quantitative tables,
threshold information, software metadata, and data provenance. The original
executable analysis scripts and complete SPM/FEAT derivative workspaces are
not present in the audited archive; this is therefore not presented as a fully
executable end-to-end pipeline.

Archived resources:

- `results/tables/table1_spm_peaks.csv`
- `results/tables/table2_fsl_clusters.txt`
- `results/tables/spm_threshold_info.txt`
- `results/tables/fsl_threshold_info.txt`
- `env/TOOL_VERSIONS.md`
- `DATA_SOURCES.md`

The repository is not presented as a fully executable end-to-end pipeline.

## Limitations
Single-subject tutorial analysis, no group-level inference, affine FSL standard-space registration, and non-equivalent cross-package thresholding procedures.

---

**Author:** Rene Andrade Rey · 🧪 ORCID: https://orcid.org/0000-0001-5627-579X · 🌐 Scholar: https://scholar.google.es/citations?hl=es&user=Nl3ApFEAAAAJ
