# Results

All designs: Si bars (height 700 nm, length 2.0 µm) on a 4 µm CaF₂ substrate, period P = 2.5 µm, gap g = 150 nm, sweep 3000–5000 nm.
`R = |S11|²`, `T = |S21|²`, `A = 1 − (R + T)`, `Q = λ0 / FWHM`.

Field figures: **(a, b)** E-field, **(c, d)** H-field (side and top views).

**Contents**
1. [Single Bar Resonator (SBR)](#1-single-bar-resonator-sbr)
2. [Symmetric Dual-Bar Resonator (SDR)](#2-symmetric-dual-bar-resonator-sdr)
3. [Asymmetric Dual-Bar Resonator (ADR) baseline](#3-asymmetric-dual-bar-resonator-adr-baseline)
4. [ADR, W₂ + 50 nm](#4-adr-w--50-nm-smaller-bar-wider)
5. [ADR, W₂ − 50 nm](#5-adr-w--50-nm-smaller-bar-narrower)
6. [ADR, W₁ + 50 nm ⭐ best](#6-adr-w--50-nm-larger-bar-wider--best)
7. [ADR, W₁ − 50 nm](#7-adr-w--50-nm-larger-bar-narrower)
8. [ADR, both + 50 nm](#8-adr-both-bars--50-nm)
9. [ADR, both − 50 nm](#9-adr-both-bars--50-nm)
10. [Summary](#10-summary)

---

## 1. Single Bar Resonator (SBR)

**W = 1.6 µm**, L₂ = 0.45 µm

| Geometry | R / T / A | Q-factor |
|:---:|:---:|:---:|
| <img src="figures/01_sbr/geometry.png" width="260"> | <img src="figures/01_sbr/rta.png" width="300"> | <img src="figures/01_sbr/q_factor.png" width="320"> |

- **Resonance:** a broad fundamental dipole resonance at **3520 nm**, with FWHM 529.1 nm and **Q = 6.7**.
- **Absorption:** about 0 across the band, so the incident energy is reflected rather than lost.
- **Fields:** the E-field is confined in the high-index bar, and the displacement current produces an H-field at the bar centre.

<img src="figures/01_sbr/fields.png" width="420">

---

## 2. Symmetric Dual-Bar Resonator (SDR)

**W₁ = W₂ = 0.8 µm**, g = 150 nm, L₂ = 0.375 µm

| Geometry | R / T / A | Q-factor (reflection) |
|:---:|:---:|:---:|
| <img src="figures/02_sdr/geometry.png" width="260"> | <img src="figures/02_sdr/rta.png" width="300"> | <img src="figures/02_sdr/q_factor.png" width="320"> |

| λ₀ (nm) | FWHM (nm) | Q |
|--------:|----------:|--:|
| **4104** | **34.1** | **120.4** |
| 3848 | 117.8 | 32.7 |
| 3036 | 186.2 | 16.3 |

Near-field coupling **splits** the single resonance. The E-field is squeezed into the **150 nm gap**, and the H-field is **symmetric in both bars**, because the bars resonate in phase.

<img src="figures/02_sdr/fields.png" width="420">

---

## 3. Asymmetric Dual-Bar Resonator (ADR) baseline

**W₁ = 1.05 µm, W₂ = 0.55 µm**, L₂ = 0.375 µm

| Geometry | R / T / A | Q-factor |
|:---:|:---:|:---:|
| <img src="figures/03_adr_baseline/geometry.png" width="260"> | <img src="figures/03_adr_baseline/rta.png" width="300"> | <img src="figures/03_adr_baseline/q_factor.png" width="320"> |

| λ₀ (nm) | Q | Note |
|--------:|--:|------|
| **4080** | **537.3** | FWHM ≈ 7.6 nm, strongly coupled asymmetric mode |
| 3760 | 490.3 | |
| 4340 | 145.6 | |
| 4012 | 27.0 | broad dip |

| λ = 3.760 µm | λ = 4.032 µm |
|:---:|:---:|
| <img src="figures/03_adr_baseline/fields_3760nm.png" width="330"> | <img src="figures/03_adr_baseline/fields_4032nm.png" width="330"> |
| Larger bar dominates, plus coupling through the gap | Both bars strongly coupled |
| **λ = 4.088 µm** | **λ = 4.340 µm** |
| <img src="figures/03_adr_baseline/fields_4088nm.png" width="330"> | <img src="figures/03_adr_baseline/fields_4340nm.png" width="330"> |
| High-Q coupled mode, H stronger in the larger bar | Controlled by the larger bar |

---

## 4. ADR, W₂ + 50 nm (smaller bar wider)

**W₁ = 1.05 µm, W₂ = 0.60 µm**, L₂ = 0.325 µm. **Highest Q = 545.1 at ~4080 nm.**

| Geometry | R / T / A | Q-factor |
|:---:|:---:|:---:|
| <img src="figures/04_w2_plus50/geometry.png" width="260"> | <img src="figures/04_w2_plus50/rta.png" width="300"> | <img src="figures/04_w2_plus50/q_factor.png" width="320"> |

| 3.584 µm | 3.812 µm | 4.112 µm | 4.388 µm |
|:---:|:---:|:---:|:---:|
| <img src="figures/04_w2_plus50/fields_3584nm.png" width="190"> | <img src="figures/04_w2_plus50/fields_3812nm.png" width="190"> | <img src="figures/04_w2_plus50/fields_4112nm.png" width="190"> | <img src="figures/04_w2_plus50/fields_4388nm.png" width="190"> |
| Gap E-field; H in the **smaller** bar | Both bars coupled | Larger bar stronger | **Larger** bar dominates |

---

## 5. ADR, W₂ − 50 nm (smaller bar narrower)

**W₁ = 1.05 µm, W₂ = 0.50 µm**, L₂ = 0.40 µm. **Highest Q = 684.2 at 3732 nm.**

| Geometry | R / T / A |
|:---:|:---:|
| <img src="figures/05_w2_minus50/geometry.png" width="260"> | <img src="figures/05_w2_minus50/rta.png" width="320"> |

Increasing the size difference between the bars sharpens the short-λ resonance. Other coupled resonances appear near 4052 and 4316 nm.

| 3.724 µm | 4.052 µm | 4.316 µm |
|:---:|:---:|:---:|
| <img src="figures/05_w2_minus50/fields_3724nm.png" width="250"> | <img src="figures/05_w2_minus50/fields_4052nm.png" width="250"> | <img src="figures/05_w2_minus50/fields_4316nm.png" width="250"> |
| Gap E-field; both bars interact | H mainly in the larger bar | Almost entirely the larger bar |

---

## 6. ADR, W₁ + 50 nm (larger bar wider) ⭐ best

**W₁ = 1.10 µm, W₂ = 0.55 µm**, L₂ = 0.35 µm. **Highest Q = 719.3 at 3732 nm (FWHM ≈ 5.2 nm).**

| Geometry | R / T / A | Q-factor |
|:---:|:---:|:---:|
| <img src="figures/06_w1_plus50/geometry.png" width="260"> | <img src="figures/06_w1_plus50/rta.png" width="300"> | <img src="figures/06_w1_plus50/q_factor.png" width="320"> |

| λ₀ (nm) | FWHM (nm) | Q |
|--------:|----------:|--:|
| **3732** | **5.2** | **719.3** |
| 4044 | 10.8 | 376.0 |
| 4252 | 26.4 | 161.3 |
| 4052 | 27.8 | 145.8 |
| 3984 | 129.7 | 30.7 |

| 3.732 µm | 4.044 µm | 4.252 µm |
|:---:|:---:|:---:|
| <img src="figures/06_w1_plus50/fields_3732nm.png" width="250"> | <img src="figures/06_w1_plus50/fields_4044nm.png" width="250"> | <img src="figures/06_w1_plus50/fields_4252nm.png" width="250"> |
| Strong gap confinement; both bars → **highest Q** | Larger bar becomes dominant | Controlled by the larger bar |

---

## 7. ADR, W₁ − 50 nm (larger bar narrower)

**W₁ = 1.00 µm, W₂ = 0.55 µm**, L₂ = 0.40 µm. **Highest Q = 545.1 at 4080 nm** (also Q ≈ 489 at 3760 nm).

| Geometry | R / T / A | Q-factor |
|:---:|:---:|:---:|
| <img src="figures/07_w1_minus50/geometry.png" width="260"> | <img src="figures/07_w1_minus50/rta.png" width="300"> | <img src="figures/07_w1_minus50/q_factor.png" width="320"> |

| 3.760 µm | 4.080 µm | 4.340 µm |
|:---:|:---:|:---:|
| <img src="figures/07_w1_minus50/fields_3760nm.png" width="250"> | <img src="figures/07_w1_minus50/fields_4080nm.png" width="250"> | <img src="figures/07_w1_minus50/fields_4340nm.png" width="250"> |
| **Smaller** bar dominates | Coupled response | **Larger** bar dominates |

---

## 8. ADR, both bars + 50 nm

**W₁ = 1.10 µm, W₂ = 0.60 µm**, L₂ = 0.40 µm. **Highest Q = 509.3 at 3552 nm.**

| Geometry | R / T / A | Q-factor |
|:---:|:---:|:---:|
| <img src="figures/08_both_plus50/geometry.png" width="260"> | <img src="figures/08_both_plus50/rta.png" width="300"> | <img src="figures/08_both_plus50/q_factor.png" width="320"> |

| 3.552 µm | 3.828 µm | 4.112 µm |
|:---:|:---:|:---:|
| <img src="figures/08_both_plus50/fields_3552nm.png" width="250"> | <img src="figures/08_both_plus50/fields_3828nm.png" width="250"> | <img src="figures/08_both_plus50/fields_4112nm.png" width="250"> |
| Gap-edge E-field; H in the smaller bar | Both bars strongly coupled | Weaker, less confined mode |

---

## 9. ADR, both bars − 50 nm

**W₁ = 1.00 µm, W₂ = 0.50 µm**, L₂ = 0.425 µm. **Highest Q = 673.1 at 3724 nm (FWHM ≈ 5.5 nm).**

| Geometry | R / T / A | Q-factor |
|:---:|:---:|:---:|
| <img src="figures/09_both_minus50/geometry.png" width="260"> | <img src="figures/09_both_minus50/rta.png" width="300"> | <img src="figures/09_both_minus50/q_factor.png" width="320"> |

| 3.724 µm | 4.052 µm | 4.316 µm |
|:---:|:---:|:---:|
| <img src="figures/09_both_minus50/fields_3724nm.png" width="250"> | <img src="figures/09_both_minus50/fields_4052nm.png" width="250"> | <img src="figures/09_both_minus50/fields_4316nm.png" width="250"> |
| Gap E-field; both bars excited | Larger bar dominant | Almost entirely the larger bar |

---

## 10. Summary

<img src="figures/q_factor_summary.png" width="720">

| Configuration | W₁ / W₂ (µm) | λ₀ (nm) | Highest Q |
|---------------|:-----------:|--------:|----------:|
| SBR | 1.6 / – | 3520 | 6.7 |
| SDR | 0.80 / 0.80 | 4104 | 120.4 |
| ADR baseline | 1.05 / 0.55 | 4080 | 537.3 |
| W₂ + 50 nm | 1.05 / 0.60 | 4080 | 545.1 |
| W₂ − 50 nm | 1.05 / 0.50 | 3732 | 684.2 |
| **W₁ + 50 nm** | **1.10 / 0.55** | **3732** | **719.3** |
| W₁ − 50 nm | 1.00 / 0.55 | 4080 | 545.1 |
| Both + 50 nm | 1.10 / 0.60 | 3552 | 509.3 |
| Both − 50 nm | 1.00 / 0.50 | 3724 | 673.1 |

**Design rules**
1. **Symmetry breaking is the key lever.** Going from SDR to ADR raises Q by about 4.5× (120 → 537).
2. **Widening the larger bar** (W₁ = 1.10 µm) gives the sharpest mode, Q = 719.3 at 3732 nm.
3. **Short-λ high-Q modes** (about 3.5–3.75 µm) come from **gap E-field confinement** and **magnetic activity in the smaller bar**.
4. At **long λ** (about 4.2–4.4 µm), energy moves into the **larger bar**, which becomes the dominant resonator.
