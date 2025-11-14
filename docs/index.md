# Task fMRI: SPM First-Level (Auditory) (+ FEAT replication)

**Goal:** Reproduce the classic SPM Auditory first-level GLM and (optionally) replicate one contrast in FSL FEAT.

---

## Snapshot
- **Dataset:** SPM Auditory tutorial (single subject)
- **Local subset:** 1 subject · **Disk:** ≤ ~0.5–1 GB
- **Tools:** SPM12 (GLM), optional FEAT replication
- **Status:** <planned / in progress / complete>
- **Last updated:** <YYYY-MM-DD>

---

## Data
- **Source:** SPM Auditory example (public).  
- **What I downloaded:** single subject, runs used.  
- **Layout:** BIDS or SPM-style folders.

---

## Pipeline (high-level)
1) Preprocess (realign, coreg, normalize, smooth) in SPM  
2) First-level GLM (conditions + 6 motion regressors)  
3) Threshold: FWE/FDR; export contrasts  
4) Optional: FEAT first-level to compare maps/thresholds

---

## Results (to be filled)
- Figure: thresholded activation map over anatomical  
- Table: peak coordinates, cluster sizes  
- Note: differences SPM vs FEAT if replicated

---

## Reproducibility
- Versions in `env/TOOL_VERSIONS.md`.  
- Steps: “Run SPM preprocessing → specify GLM → estimate → contrasts → export figures.”  
- Limitations: single-subject demo.

---

**Author:** Rene Andrade Rey · 🧪 ORCID: https://orcid.org/0000-0001-5627-579X · 🌐 Scholar: https://scholar.google.es/citations?hl=es&user=Nl3ApFEAAAAJ
