# Task fMRI: SPM First-Level (Auditory) + FEAT replication

**Goal:** Reproduce the classic SPM Auditory first-level GLM and optionally replicate the same contrast in FSL FEAT.

---

## Snapshot
- **Dataset:** SPM Auditory tutorial (MoAEpilot), single subject
- **Local subset:** 1 subject, 84 analysis volumes
- **Tools:** MATLAB R2025b + SPM25
- **Status:** SPM analysis complete; FSL FEAT replication pending
- **Last updated:** 2026-07-15

---

## Data
- **Source:** official SPM Auditory tutorial dataset (BIDS/NIfTI)
- **Input:** `sub-01_task-auditory_bold.nii` and `sub-01_T1w.nii`
- **Layout:** BIDS
- Raw neuroimaging data are not stored in this repository.

---

## SPM pipeline
1. Realignment and motion-parameter estimation
2. Slice-timing correction
3. T1-to-mean-EPI coregistration
4. T1 segmentation and deformation estimation
5. Functional normalisation to MNI space at 3 mm isotropic resolution
6. Spatial smoothing with 6 mm FWHM
7. First-level GLM with one listening condition and 6 motion nuisance regressors
8. Contrast: **Listening > Rest**
9. Whole-brain voxel-level FWE inference at **p < 0.05**

---

## Results

### Motion QC
![SPM motion QC](../results/figures/fig0_spm_motion_qc.png)

### Thresholded activation map
![SPM activation map](../results/figures/fig1_spm_activation_map.png)

### Maximum-intensity projections
![SPM MIP](../results/figures/fig2_spm_mip.png)

### Statistical summary
- Contrast: **Listening > Rest**
- Threshold: **voxel-level FWE p < 0.05**
- T threshold: **5.296299**
- Extent threshold: **0 voxels**
- Largest clusters: **403 voxels** and **213 voxels**
- Peak T values: **11.868** and **11.874**
- Peak MNI coordinates include **[-63, -28, 14]** and **[57, -22, 11]**

See:
- `results/tables/table1_spm_peaks.csv`
- `results/tables/spm_threshold_info.txt`

---

## Reproducibility
- MATLAB: **R2025b**
- SPM: **SPM25**
- Retained scans: **84**
- TR: **7 s**
- Slice timing: **64 slices**, descending `64:-1:1`, reference slice 32
- Normalised voxel size: **3 × 3 × 3 mm**
- Smoothing: **6 mm FWHM**
- Motion nuisance regressors: **6**

---

## Next milestone
Replicate the same **Listening > Rest** first-level analysis in **FSL FEAT** and compare the resulting activation maps and thresholding approaches.

---

**Author:** Rene Andrade Rey · 🧪 ORCID: https://orcid.org/0000-0001-5627-579X · 🌐 Scholar: https://scholar.google.es/citations?hl=es&user=Nl3ApFEAAAAJ