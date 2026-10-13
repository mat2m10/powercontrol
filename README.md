# powercontrol

> **Superseded:** this work moved to `abyss_notebooks` and then [mat2m10/abyss](https://github.com/mat2m10/abyss). Kept for history only; not developed further.

Notebooks (March to July 2023) on GWAS statistical power and how population stratification affects it, using synthetic phenotypes on 1000 Genomes genotypes.

## Notebooks

| Notebook | What it does |
|----------|--------------|
| `01_Power_theoretical` | Power analysis on synthetic data with an additive effect |
| `02_Power_empirical_by_looping` | Estimate power empirically from sample size, allele frequency, effect and effect SD |
| `03_Finding_Ratio_effect_VS_standard_deviation` | Find the effect-to-SD ratio that keeps 80% power at any allele frequency (produces the data in `df_ratio_vs_power.pkl`) |
| `04_population_stratification_analysis` | Analysis of population stratification |
| `05_introducing_pop_strat` | Introduce population stratification into the synthetic phenotypes |
| `06_power_pop_strat_no_corr` | Power under population stratification, without correction |
| `07_Population_Manifold_Association_Study` | Population Manifold Association Study (continued in `abyss_notebooks/07_PMAS.ipynb`) |
| `08_Silhouette` | Silhouette scores of super-population / population clustering (chromosome 21) |
| `09_Raw_LD_Clustering` | Clustering on raw LD blocks |

`ratio.py` (`find_power_vals`) looks up effect sizes for a target power from `df_ratio_vs_power.pkl`.

## Data

Not included. Notebooks expect local 1000 Genomes genotypes under `/mnt/d/data_1KG` and data produced by `swampy` under `/mnt/d/swampy_data`. On a fresh clone `ratio.py` looks for `./data/df_ratio_vs_power.pkl`, but the pickle is at the repo root.
