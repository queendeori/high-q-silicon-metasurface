"""
Find resonances in a transmittance (or reflectance) spectrum and compute
Q = λ0 / FWHM for each one, then plot the spectrum with annotations.

Usage:
    python q_factor.py spectrum.csv                       # dips in T (default)
    python q_factor.py spectrum.csv --peaks               # peaks instead of dips
    python q_factor.py spectrum.csv --col R --peaks --out R_Q.png

CSV: first column = wavelength (nm), then one or more columns (e.g. R, T, A).
COMSOL comment lines starting with '%' are ignored.
"""

import argparse

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks, peak_widths


def resonances(wl, y, peaks: bool, prominence: float):
    sig = y if peaks else -y
    idx, _ = find_peaks(sig, prominence=prominence)
    if len(idx) == 0:
        return []
    widths, _, left, right = peak_widths(sig, idx, rel_height=0.5)
    # convert fractional sample indices to wavelength (handles non-uniform grids)
    grid = np.arange(len(wl))
    lw = np.interp(left, grid, wl)
    rw = np.interp(right, grid, wl)
    out = []
    for i, l, r in zip(idx, lw, rw):
        fwhm = abs(r - l)
        out.append({"lambda_nm": wl[i], "fwhm_nm": fwhm, "Q": wl[i] / fwhm if fwhm else np.inf})
    return sorted(out, key=lambda d: -d["Q"])


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv")
    p.add_argument("--col", default="T", help="column to analyse (default T)")
    p.add_argument("--peaks", action="store_true", help="analyse peaks instead of dips")
    p.add_argument("--prominence", type=float, default=0.05)
    p.add_argument("--out", default="q_factor.png")
    a = p.parse_args()

    df = pd.read_csv(a.csv, comment="%")
    df.columns = [c.strip() for c in df.columns]
    wl = df.iloc[:, 0].to_numpy(float)
    y = df[a.col].to_numpy(float)
    order = np.argsort(wl)
    wl, y = wl[order], y[order]

    res = resonances(wl, y, a.peaks, a.prominence)
    print(f"{'lambda (nm)':>12} {'FWHM (nm)':>10} {'Q':>8}")
    for r in res:
        print(f"{r['lambda_nm']:12.1f} {r['fwhm_nm']:10.2f} {r['Q']:8.1f}")

    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.plot(wl, y, lw=1.6)
    for r in res:
        yi = np.interp(r["lambda_nm"], wl, y)
        ax.annotate(f"λ={r['lambda_nm']:.0f} nm\nQ={r['Q']:.1f}",
                    (r["lambda_nm"], yi), textcoords="offset points", xytext=(0, 18),
                    ha="center", fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel(a.col)
    ax.grid(alpha=0.4)
    fig.tight_layout()
    fig.savefig(a.out, dpi=200)
    print(f"saved {a.out}")


if __name__ == "__main__":
    main()
