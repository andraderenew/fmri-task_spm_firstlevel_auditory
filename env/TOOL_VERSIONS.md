# Tool Versions and Analysis Environment

## System
- **OS:** macOS 26.5.2
- **Architecture:** arm64 (Apple Silicon)

## Software used for the SPM analysis
- **MATLAB:** R2025b (`25.2.0.2998904`)
- **SPM:** SPM25, release `25.01.02`

## SPM analysis settings
- **Dataset:** SPM Auditory / MoAEpilot BIDS dataset
- **Subject:** sub-01
- **Functional volumes analysed:** 84
- **TR:** 7 s
- **Slice timing:** 64 slices, descending `64:-1:1`, reference slice 32
- **Coregistration:** T1 to mean EPI
- **Normalisation:** MNI space, 3 × 3 × 3 mm functional resolution
- **Smoothing:** 6 mm FWHM
- **First-level condition:** listening
- **Motion nuisance regressors:** 6 realignment parameters
- **Contrast:** Listening > Rest
- **Inference:** whole-brain voxel-level FWE p < 0.05
- **Observed T threshold:** 5.296299
- **Extent threshold:** 0 voxels

## FSL environment available for planned replication
- **FSL:** 6.0.7.12 (modified local installation)
- **FEAT:** available on PATH during environment check

Documentation updated: 2026-07-15
