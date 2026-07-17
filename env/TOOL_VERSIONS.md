# Tool Versions and Analysis Environment

## System
- **OS:** macOS 26.5.2
- **Architecture:** arm64 (Apple Silicon)

## SPM analysis
- **MATLAB:** R2025b (`25.2.0.2998904`)
- **SPM:** SPM25, release `25.01.02`
- **Dataset:** SPM Auditory / MoAEpilot BIDS dataset
- **Subject:** sub-01
- **Volumes:** 84
- **TR:** 7 s
- **Slice timing:** 64 slices, descending `64:-1:1`, reference slice 32
- **Coregistration:** T1 to mean EPI
- **Normalization:** MNI space, 3 × 3 × 3 mm functional resolution
- **Smoothing:** 6 mm FWHM
- **Motion nuisance regressors:** 6 realignment parameters
- **Contrast:** Listening > Rest
- **Inference:** voxel-level whole-brain FWE p < 0.05
- **Observed T threshold:** 5.296299

## FSL FEAT replication
- **FSL:** 6.0.7.12 (modified local installation)
- **FEAT:** first-level analysis
- **Motion correction:** MCFLIRT
- **Slice timing:** regular descending
- **Brain extraction:** BET
- **Smoothing:** SUSAN, 6 mm FWHM
- **High-pass filter:** 128 s
- **Temporal model:** FILM prewhitening
- **HRF:** double gamma
- **Motion nuisance EVs:** 6 MCFLIRT parameters
- **Functional-to-T1 registration:** FLIRT, 6 DOF
- **T1-to-MNI152 registration:** FLIRT, 12 DOF
- **Nonlinear standard-space registration:** off
- **Contrast:** Listening > Rest
- **Inference:** cluster-forming Z > 3.1, cluster significance p < 0.05

Documentation updated: 2026-07-15
