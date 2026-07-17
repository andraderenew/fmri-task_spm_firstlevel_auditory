# Mini-Report — Task fMRI Auditory First-Level Analysis

## Aim
Reproduce a complete single-subject block-design task-fMRI workflow using the classic SPM Auditory / MoAEpilot dataset and compare the same `Listening > Rest` contrast across SPM25 and FSL FEAT.

## Data
- Dataset: **SPM Auditory / MoAEpilot** tutorial dataset
- Subject: **sub-01**
- Functional series: **84 volumes**
- TR: **7 s**
- Task: block-design auditory stimulation versus rest
- Raw BIDS/NIfTI data remain local and are not committed to GitHub

## SPM25 methods
- MATLAB R2025b and SPM25 release 25.01.02
- Realignment and reslicing
- Slice timing: 64 slices, descending `64:-1:1`, reference slice 32
- T1-to-mean-EPI coregistration
- T1 segmentation and deformation estimation
- MNI normalization at 3 mm isotropic functional resolution
- Spatial smoothing: 6 mm FWHM
- First-level GLM with listening blocks and 6 realignment nuisance regressors
- Contrast: **Listening > Rest**
- Inference: whole-brain voxel-level FWE p < 0.05

## FSL FEAT methods
- FSL 6.0.7.12 local installation
- MCFLIRT motion correction
- Regular-descending slice timing
- BET brain extraction
- SUSAN smoothing: 6 mm FWHM
- High-pass filter: 128 s
- FILM model with prewhitening
- Double-gamma HRF
- Six MCFLIRT motion nuisance EVs
- Functional-to-T1 FLIRT registration: 6 DOF
- T1-to-MNI152 FLIRT registration: 12 DOF
- Contrast: **Listening > Rest**
- Inference: cluster-forming Z > 3.1 and cluster significance p < 0.05

## Results

### SPM25
- T threshold: **5.296299**
- Largest clusters: **403** and **213 voxels**
- Principal peaks: `[-63, -28, 14]` and `[57, -22, 11]`
- Peak T values: approximately **11.87** bilaterally

### FSL FEAT
- Largest cluster: **863 voxels**, Z max **10.5**, peak `[-61.1, -27.0, 8.85]`, p = `1.77e-35`
- Second-largest cluster: **718 voxels**, Z max **10.3**, peak `[58.7, -22.8, 5.68]`, p = `2.85e-31`

Both analyses recovered a strong bilateral auditory activation pattern with closely corresponding left and right temporal peak locations.

## Figures
- Motion QC: `results/figures/fig0_spm_motion_qc.png`
- SPM activation: `results/figures/fig1_spm_activation_map.png`
- SPM MIP: `results/figures/fig2_spm_mip.png`
- FSL FEAT activation: `results/figures/fig3_fsl_feat_activation_map.png`
- SPM/FSL comparison: `results/figures/fig4_spm_vs_fsl.png`

## Interpretation
The cross-software agreement supports successful conceptual replication of the auditory task effect. Exact map correspondence is not expected because the packages differ in HRF modeling, temporal estimation, registration, statistical image scaling, and thresholding.

SPM used voxel-level whole-brain FWE correction, while FEAT used cluster-based inference. Consequently, cluster sizes and p-values should not be treated as directly equivalent across packages.

## QC
- SPM motion traces were exported and inspected
- Both workflows included six motion nuisance regressors
- Both used the same 84-volume series and equivalent block timings
- The dominant bilateral auditory pattern was reproduced in both packages

## Limitations
- Single-subject tutorial dataset; no population-level inference
- Didactic reproducibility analysis rather than a confirmatory study
- FSL standard-space registration was affine rather than nonlinear
- No additional framewise-displacement censoring model
- No automatic atlas-based anatomical labeling

## Reproducibility
- Data provenance: `DATA_SOURCES.md`
- Environment: `env/TOOL_VERSIONS.md`
- SPM settings: `results/tables/spm_threshold_info.txt`
- FSL settings: `results/tables/fsl_threshold_info.txt`
- SPM peaks: `results/tables/table1_spm_peaks.csv`
- FSL clusters: `results/tables/table2_fsl_clusters.txt`
