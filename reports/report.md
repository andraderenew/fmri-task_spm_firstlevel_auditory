# Mini-Report — Task fMRI Auditory First-Level Analysis

## Aim
Reproduce a complete single-subject block-design task-fMRI workflow using the classic SPM Auditory / MoAEpilot dataset and demonstrate preprocessing, first-level GLM specification, nuisance-motion modeling, contrast estimation, statistical thresholding, QC, and reproducible reporting.

A second-stage FSL FEAT replication is planned so that the same task contrast can be compared across two widely used fMRI analysis environments.

## Data
- Dataset: **SPM Auditory / MoAEpilot** tutorial dataset
- Subject: **sub-01**
- Functional series used: **84 volumes**
- TR: **7 s**
- Task: block-design auditory stimulation versus rest
- Raw BIDS/NIfTI data are stored locally and are not committed to GitHub

## Methods
### Software
- MATLAB **R2025b**
- SPM **25.01.02 / SPM25**
- macOS on Apple Silicon (`arm64`)

### Preprocessing
1. Realignment (estimate and reslice)
2. Slice-timing correction with **64 slices**, descending order `64:-1:1`, reference slice **32**
3. Coregistration of the T1 image to the mean EPI
4. T1 segmentation and deformation estimation
5. Functional normalization to MNI space at **3 × 3 × 3 mm**
6. Spatial smoothing with a **6 mm FWHM** Gaussian kernel

### First-level model
- Units: scans
- TR: **7 s**
- Condition: `listening`
- Listening onsets: `6:12:84`
- Block duration: **6 scans**
- Nuisance regressors: **6 realignment parameters**
- Contrast: **Listening > Rest**

### Statistical inference
- Whole-brain voxel-level **FWE p < 0.05**
- T threshold: **5.296299**
- Extent threshold: **0 voxels**

## Results
### QC
- `results/figures/fig0_spm_motion_qc.png` contains translation and rotation traces from SPM realignment.

### Activation figures
- **Fig 1:** thresholded activation map over the normalized mean EPI: `results/figures/fig1_spm_activation_map.png`
- **Fig 2:** maximum-intensity projections of the thresholded SPM T-map: `results/figures/fig2_spm_mip.png`

### Peak table
The two largest suprathreshold clusters were:

| Cluster size (voxels) | Peak T | MNI x | MNI y | MNI z |
|---:|---:|---:|---:|---:|
| 213 | 11.8743 | 57 | -22 | 11 |
| 403 | 11.8681 | -63 | -28 | 14 |

The complete table is stored in `results/tables/table1_spm_peaks.csv`.

Threshold and model metadata are stored in `results/tables/spm_threshold_info.txt`.

## QC and interpretation notes
- The automated workflow generated a dedicated realignment-parameter QC figure rather than relying only on the final statistical map.
- Statistical results are reported using the actual threshold that survived whole-brain voxel-level FWE correction.
- Peak coordinates are reported in MNI space.
- No atlas-based anatomical labels were assigned automatically; this avoids introducing unsupported anatomical labels into the portfolio.

## Limitations
- Single-subject tutorial dataset; no population-level inference can be made.
- This is a didactic reproducibility analysis rather than a clinical or hypothesis-confirmatory study.
- The FSL FEAT replication and cross-software comparison are not yet complete.
- Motion traces are provided as a QC visualization, but no additional framewise-displacement censoring model was added to this tutorial analysis.

## Reproducibility
- Data provenance: `DATA_SOURCES.md`
- Software and system information: `env/TOOL_VERSIONS.md`
- Published statistical settings: `results/tables/spm_threshold_info.txt`
- Full peak table: `results/tables/table1_spm_peaks.csv`
- High-level workflow and figures: `README.md`
