# Molecular Dynamics and Free-Energy Analysis

> Enhanced sampling, metadynamics, collective-variable analysis, and free-energy reconstruction using GROMACS and PLUMED.

![GROMACS](https://img.shields.io/badge/GROMACS-2019.6-blue)
![PLUMED](https://img.shields.io/badge/PLUMED-2.7.0-orange)
![Python](https://img.shields.io/badge/Python-Analysis-yellow)
![Linux](https://img.shields.io/badge/Platform-Linux-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Project Overview

This repository contains computational studies of molecular conformational dynamics and enhanced sampling using **GROMACS** and **PLUMED**.

The project focuses on:

- Molecular dynamics simulation
- Well-tempered metadynamics
- Collective-variable (CV) selection
- Free-energy surface reconstruction
- Trajectory reweighting
- Statistical error estimation
- Conformational-state sampling
- Two-dimensional free-energy analysis

The workflow was developed around exercises from the **PLUMED Masterclass 21.4**, with additional analysis and interpretation performed as part of the study.

---

## Scientific Objectives

1. Investigate conformational sampling using molecular dynamics.
2. Accelerate transitions between metastable states using metadynamics.
3. Reconstruct free-energy landscapes.
4. Evaluate different collective variables.
5. Estimate statistical uncertainty using block analysis.
6. Reweight trajectories to recover unbiased distributions.
7. Analyze conformational transitions using multidimensional free-energy surfaces.

---

# Systems Studied

## 1. Dialanine

Dialanine was used to investigate backbone conformational sampling through the **φ/ψ torsional degrees of freedom**.

The system was studied using:

- Standard molecular dynamics
- Well-tempered metadynamics
- Free-energy reconstruction
- Trajectory reweighting
- Block analysis
- Collective-variable comparison

Standard MD showed substantially different sampling behaviour for the two initial conformational states.

| System | φ SD (rad) | ψ SD (rad) |
|---|---:|---:|
| Dialanine A | 0.556 | 1.036 |
| Dialanine B | 0.133 | 0.343 |

---

## 2. RfaH C-Terminal Domain

The RfaH C-terminal domain from *Escherichia coli* was used as a model for conformational-state sampling.

The system contains two major structural states:

- α-helical state
- β-barrel state

Two RMSD-based collective variables were used:

- RMSD to the α-helical reference
- RMSD to the β-barrel reference

A two-dimensional free-energy surface was reconstructed to investigate the conformational landscape.

---

# Computational Workflow

```text
Molecular Dynamics
        ↓
Collective Variable Selection
        ↓
Well-Tempered Metadynamics
        ↓
HILLS / COLVAR Generation
        ↓
Free-Energy Reconstruction
        ↓
Reweighting + Block Analysis
        ↓
Convergence and CV Assessment
        ↓
Conformational Free-Energy Analysis
```

---

# Methods

### Molecular Dynamics

Standard molecular dynamics simulations were performed to investigate conformational sampling.

### Well-Tempered Metadynamics

Well-tempered metadynamics was used to enhance sampling of slow conformational degrees of freedom by depositing Gaussian bias potentials along selected collective variables.

### Free-Energy Reconstruction

Free-energy surfaces were reconstructed from accumulated metadynamics bias using PLUMED `sum_hills`.

### Trajectory Reweighting

Biased trajectories were reweighted to estimate unbiased distributions and free-energy profiles.

### Block Analysis

Block averaging was used to assess statistical uncertainty and investigate convergence.

### Collective-Variable Assessment

Multiple candidate CVs were compared based on sampling efficiency, exploration of conformational space, free-energy error, and convergence behaviour.

---

# Key Results

## Metadynamics Free-Energy Reconstruction

Well-tempered metadynamics was used to enhance sampling along the φ torsion.

The reconstructed free-energy profile showed a dominant low-energy region around:

**φ ≈ −1.37 rad**

---

## Reweighting Validation

The reweighted free-energy profile was compared with the metadynamics-derived free-energy profile.

| Metric | Value |
|---|---:|
| RMSE | 2.60 kJ/mol |
| MAE | 1.90 kJ/mol |
| Maximum difference | 7.24 kJ/mol |
| Correlation | 0.9992 |

The high correlation indicates strong agreement in the overall shape of the two free-energy profiles.

---

## Collective Variable Comparison

Several collective variables were evaluated.

| Collective Variable | Approx. block error |
|---|---:|
| φ torsion | ~0.14 kJ/mol |
| Radius of gyration | ~0.16 kJ/mol |
| O6-H8 distance | ~0.21 kJ/mol |
| ψ torsion | ~0.69 kJ/mol |

The φ torsion produced the lowest estimated statistical error among the tested CVs, while ψ showed substantially larger uncertainty.

These results demonstrate that **collective-variable selection is critical for efficient enhanced sampling**.

---

# RfaH Free-Energy Landscape

A two-dimensional free-energy surface was reconstructed using the two RMSD-based collective variables.

The landscape contained low-energy regions corresponding to the reference conformational states as well as intermediate regions.

### Basin Analysis

Using selected RMSD-based basin boundaries, an illustrative basin analysis gave approximately:

- α-like population: **71.1%**
- β-like population: **28.9%**
- Estimated ΔG(β − α): **~2.25 kJ/mol**

These values depend on the selected basin definitions and should therefore be interpreted as an analysis of the chosen state boundaries rather than universal thermodynamic values.

---

# Software

| Software | Version / Use |
|---|---|
| GROMACS | 2019.6 |
| PLUMED | 2.7.0 |
| Python | Data analysis |
| NumPy | Numerical analysis |
| Matplotlib | Visualization |
| GNU/Linux | Computational environment |

The tutorial exercises were tested using **PLUMED 2.7.0 and GROMACS 2019.6**.

---

# Repository Structure

```text
molecular-dynamics-free-energy/
│
├── analysis/
│   ├── results/
│   │   ├── ex6_fes.dat
│   │   ├── fes_normalized.dat
│   │   └── ffphi.dat
│   │
│   └── scripts/
│       ├── calculate_deltaF.py
│       └── do_block_fes.py
│
├── figures/
│   ├── DeltaG_convergence.png
│   ├── FES_2D.png
│   ├── free_energy_phi.png
│   └── phi_psi_comparison.png
│
├── plumed/
│   ├── ex2_metadynamics.dat
│   ├── ex3_reweighting.dat
│   ├── ex5_distance.dat
│   ├── ex5_psi.dat
│   ├── ex5_radius_of_gyration.dat
│   └── ex6_rfah_metadynamics.dat
│
├── structures/
│   ├── diala/
│   │   ├── dialaA.pdb
│   │   └── dialaB.pdb
│   │
│   └── rfah/
│       ├── stateA.pdb
│       ├── stateB.pdb
│       ├── state_A-Ca.pdb
│       └── state_B-Ca.pdb
│
├── .gitignore
└── README.md
```

---

# Reproducibility

The repository contains the essential input files, structures, analysis scripts, numerical results, and visualization outputs required to document the workflow.

Large simulation-generated files are intentionally excluded from version control, including:

- GROMACS trajectories
- Binary run input files
- Checkpoint files
- Energy files
- Simulation logs
- PLUMED HILLS files
- COLVAR files

This keeps the repository lightweight while preserving the computational methodology and analysis workflow.

---

# Scientific Takeaways

This project provided practical experience with:

- Molecular dynamics simulation
- Enhanced sampling
- Well-tempered metadynamics
- Free-energy calculations
- Collective-variable design
- Trajectory reweighting
- Statistical error estimation
- Convergence assessment
- Multidimensional free-energy landscapes
- Computational analysis using Python

A major focus of the project was understanding that **a successful metadynamics simulation is not determined only by generating a free-energy surface**. CV choice, sampling, convergence, reweighting, and statistical uncertainty must also be evaluated.

---

# Acknowledgements

This project was developed using the **PLUMED Masterclass 21.4** as the primary methodological framework.

The computational analysis was performed using the GROMACS molecular dynamics engine and the PLUMED enhanced-sampling framework.

---

# References

- PLUMED documentation and Masterclass 21.4
- GROMACS documentation
- Barducci et al., Well-Tempered Metadynamics
- Tiwary & Parrinello, Reweighted and driven metadynamics
- Relevant PLUMED and GROMACS methodological literature

---

## Project Status

**Completed**

The repository represents a completed computational study and analysis workflow focused on molecular dynamics, enhanced sampling, and free-energy calculations.
