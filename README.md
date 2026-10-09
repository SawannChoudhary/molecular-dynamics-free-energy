# Molecular Dynamics and Free-Energy Analysis

Computational study of molecular dynamics, enhanced sampling, metadynamics, free-energy reconstruction, trajectory reweighting, collective-variable analysis, and conformational-state sampling using GROMACS and PLUMED.

## Systems

- **Dialanine:** standard MD, metadynamics, reweighting, block analysis, and collective-variable comparison.
- **RfaH C-terminal domain:** RMSD-based metadynamics and two-dimensional free-energy analysis.

## Software

- GROMACS 2019.6
- PLUMED 2.7.0
- Python
- NumPy
- Matplotlib
- GNU/Linux

## Methods

1. Standard molecular dynamics
2. Well-tempered metadynamics
3. Free-energy reconstruction
4. Trajectory reweighting
5. Block analysis
6. Collective-variable comparison
7. RfaH conformational free-energy analysis

## Repository Contents

- `plumed/` contains PLUMED input files.
- `analysis/scripts/` contains analysis scripts.
- `analysis/results/` contains selected numerical results.
- `figures/` contains final analysis figures.
- `structures/` contains molecular structures used for analysis.

## Reproducibility

Large trajectory and simulation-state files are intentionally excluded. The repository contains the essential PLUMED inputs, analysis scripts, selected results, structures, and figures needed to document the workflow.

## Scientific Focus

Enhanced sampling, molecular dynamics, metadynamics, free-energy calculations, collective-variable selection, statistical error estimation, reweighting, and molecular conformational landscapes.
