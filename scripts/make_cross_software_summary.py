#!/usr/bin/env python3

from pathlib import Path
import csv
import math

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

SPM_TABLE = ROOT / "results/tables/table1_spm_peaks.csv"
FSL_TABLE = ROOT / "results/tables/table2_fsl_clusters.txt"

OUT = (
    ROOT
    / "results"
    / "figures"
    / "fig4_cross_software_summary.png"
)


def read_spm():
    with SPM_TABLE.open(
        encoding="utf-8",
        newline="",
    ) as f:
        rows = list(csv.DictReader(f))

    rows.sort(
        key=lambda r: int(
            r["cluster_size_voxels"]
        ),
        reverse=True,
    )

    result = {}

    for row in rows:
        x = float(row["x_mm"])

        hemi = (
            "left"
            if x < 0
            else "right"
        )

        if hemi not in result:
            result[hemi] = {
                "x": x,
                "y": float(row["y_mm"]),
                "z": float(row["z_mm"]),
                "stat": float(row["T"]),
                "voxels": int(
                    row["cluster_size_voxels"]
                ),
            }

    return result


def read_fsl():
    lines = [
        line
        for line in FSL_TABLE
        .read_text(
            encoding="utf-8"
        )
        .splitlines()
        if line.strip()
    ]

    rows = [
        line.split("\t")
        for line in lines[1:]
    ]

    rows.sort(
        key=lambda r: int(r[1]),
        reverse=True,
    )

    result = {}

    for row in rows:
        x = float(row[5])

        hemi = (
            "left"
            if x < 0
            else "right"
        )

        if hemi not in result:
            result[hemi] = {
                "x": x,
                "y": float(row[6]),
                "z": float(row[7]),
                "stat": float(row[4]),
                "voxels": int(row[1]),
                "p": row[2],
            }

    return result


def distance(a, b):
    return math.sqrt(
        (a["x"] - b["x"]) ** 2
        + (a["y"] - b["y"]) ** 2
        + (a["z"] - b["z"]) ** 2
    )


def delta(a, b):
    return (
        abs(a["x"] - b["x"]),
        abs(a["y"] - b["y"]),
        abs(a["z"] - b["z"]),
    )


def main():
    spm = read_spm()
    fsl = read_fsl()

    for hemi in ("left", "right"):
        if hemi not in spm:
            raise RuntimeError(
                f"Missing SPM {hemi} peak"
            )

        if hemi not in fsl:
            raise RuntimeError(
                f"Missing FEAT {hemi} peak"
            )

    left_d = distance(
        spm["left"],
        fsl["left"],
    )

    right_d = distance(
        spm["right"],
        fsl["right"],
    )

    left_delta = delta(
        spm["left"],
        fsl["left"],
    )

    right_delta = delta(
        spm["right"],
        fsl["right"],
    )

    fig = plt.figure(
        figsize=(13.5, 8.0)
    )

    fig.suptitle(
        (
            "SPM25 vs FSL FEAT — approximate spatial correspondence "
            "of dominant Listening > Rest peaks"
        ),
        fontsize=17,
        fontweight="bold",
        y=0.965,
    )

    ax_left = fig.add_axes(
        [0.055, 0.43, 0.41, 0.40]
    )

    ax_right = fig.add_axes(
        [0.535, 0.43, 0.41, 0.40]
    )

    ax_dist = fig.add_axes(
        [0.08, 0.13, 0.36, 0.19]
    )

    ax_note = fig.add_axes(
        [0.52, 0.105, 0.43, 0.24]
    )

    for ax, hemi, label in (
        (ax_left, "left", "Left hemisphere"),
        (ax_right, "right", "Right hemisphere"),
    ):
        s = spm[hemi]
        f = fsl[hemi]

        d = distance(s, f)
        dx, dy, dz = delta(s, f)

        ax.axis("off")

        ax.text(
            0.5,
            0.98,
            label,
            ha="center",
            va="top",
            fontsize=15,
            fontweight="bold",
            transform=ax.transAxes,
        )

        spm_text = (
            "SPM25\n"
            f"MNI = ({s['x']:.1f}, "
            f"{s['y']:.1f}, "
            f"{s['z']:.1f}) mm\n"
            f"Peak T = {s['stat']:.3f}\n"
            f"Dominant cluster = {s['voxels']} voxels"
        )

        fsl_text = (
            "FSL FEAT\n"
            f"MNI152 = ({f['x']:.1f}, "
            f"{f['y']:.1f}, "
            f"{f['z']:.2f}) mm\n"
            f"Z max = {f['stat']:.2f}\n"
            f"Dominant cluster = {f['voxels']} voxels"
        )

        ax.text(
            0.08,
            0.70,
            spm_text,
            ha="left",
            va="top",
            fontsize=11.5,
            linespacing=1.55,
            transform=ax.transAxes,
        )

        ax.text(
            0.58,
            0.70,
            fsl_text,
            ha="left",
            va="top",
            fontsize=11.5,
            linespacing=1.55,
            transform=ax.transAxes,
        )

        correspondence = (
            f"Coordinate differences\n"
            f"|Δx| = {dx:.2f} mm   "
            f"|Δy| = {dy:.2f} mm   "
            f"|Δz| = {dz:.2f} mm\n"
            f"3D Euclidean peak distance = {d:.2f} mm"
        )

        ax.text(
            0.5,
            0.16,
            correspondence,
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold",
            linespacing=1.55,
            transform=ax.transAxes,
        )

    hemis = [
        "Left",
        "Right",
    ]

    distances = [
        left_d,
        right_d,
    ]

    bars = ax_dist.bar(
        hemis,
        distances,
        width=0.55,
    )

    ax_dist.set_ylabel(
        "Approximate peak-to-peak distance (mm)"
    )

    ax_dist.set_title(
        "Approximate peak-coordinate correspondence",
        fontsize=12,
        fontweight="bold",
    )

    ax_dist.set_ylim(
        0,
        max(distances) + 2.5,
    )

    ax_dist.spines[
        "top"
    ].set_visible(False)

    ax_dist.spines[
        "right"
    ].set_visible(False)

    for bar, value in zip(
        bars,
        distances,
    ):
        ax_dist.text(
            bar.get_x()
            + bar.get_width() / 2,
            value + 0.15,
            f"{value:.2f} mm",
            ha="center",
            va="bottom",
            fontsize=11,
        )

    ax_note.axis("off")

    note = (
        "Inference was intentionally kept separate\n\n"
        "SPM25\n"
        "• voxel-level whole-brain FWE p < 0.05\n"
        "• observed threshold T > 5.296299\n\n"
        "FSL FEAT\n"
        "• cluster-forming Z > 3.1\n"
        "• cluster significance p < 0.05"
    )

    ax_note.text(
        0.0,
        1.0,
        note,
        ha="left",
        va="top",
        fontsize=11.5,
        linespacing=1.35,
        transform=ax_note.transAxes,
    )

    fig.text(
        0.5,
        0.035,
        (
            "Approximate coordinate-level comparison of reported peaks in "
            "MNI-normalized spaces. SPM MNI and FSL MNI152 coordinates "
            "are treated as approximately corresponding; this is not a "
            "voxelwise overlap analysis. T/Z values, cluster sizes, and "
            "p-values are not directly interchangeable."
        ),
        ha="center",
        va="center",
        fontsize=10.5,
    )

    OUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fig.savefig(
        OUT,
        dpi=220,
        bbox_inches="tight",
        facecolor="white",
    )

    plt.close(fig)

    print(
        f"LEFT_DISTANCE_MM={left_d:.6f}"
    )

    print(
        f"RIGHT_DISTANCE_MM={right_d:.6f}"
    )

    print(
        f"OUTPUT={OUT}"
    )

    print(
        "CONTROLLED_CROSS_SOFTWARE_FIGURE=PASS"
    )


if __name__ == "__main__":
    main()
