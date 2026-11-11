# Phase 9B-D: Regression Code and Settings Documentation

**Project:** India's Petroleum Supply Chain and Import Exposure  
**Script:** `canonical_regression_master.py`  
**Run Timestamp:** 2026-11-11T17:24:47

---

## 1. Software Environment

| Component | Version |
|:---|:---|
| Python | 3.13.5 |
| NumPy | 2.4.6 |
| Pandas | 3.0.6 |
| SciPy | (see scipy package metadata) |
| statsmodels | Not used — all estimators implemented from scratch |

---

## 2. Canonical Dataset

| Property | Value |
|:---|:---|
| File path | `c:\Users\nafis\OneDrive\Desktop\Final-Project\03_Processed_Data\standardized\core_annual_petroleum_dataset.csv` |
| SHA-256 hash | `9fb5e64c4d0e3402f979f7e83269b0a41034c8530e54fba2fdbd6895b98634ca` |
| Total rows in file | 30 |
| Rows used for regression | 26 annual, complete observations |
| Regression sample | FY 1998-99 – FY 2023-24 |
| First-difference sample | FY 1999-00 – FY 2023-24 (N=25) |

**Row filter applied:** `reporting_period_type` contains `"Annual"` AND all three variables
(`domestic_crude_production_mmt`, `crude_import_quantity_mmt`, `refinery_crude_processing_mmt`) are non-missing.

---

## 3. OLS Estimator

Standard matrix OLS:
```
β̂ = (X'X)⁻¹ X'Y
ê = Y - Xβ̂
s² = (ê'ê) / (n - k)   [unbiased; k includes intercept]
Conv_SE(β̂_j) = sqrt(s² × [(X'X)⁻¹]_jj)
t_conv = β̂_j / Conv_SE
p_conv = 2 × CDF_t(|t_conv|, df=n-k)   [two-tailed, t-distribution]
```

---

## 4. HAC (Newey-West) Covariance Estimator

**Kernel:** Bartlett (triangular)  
**Bandwidth / Maximum Lag:**
```
L = floor(4 × (n/100)^(2/9))    [Newey-West 1987 rule-of-thumb]
```

For the levels sample (n=26):  L = 2  
For the first-difference sample (n=25): L = 2

**Covariance computation:**
```
Scores: s_t = x_t × ê_t    (n × k matrix)
S̃ = Σ_t s_t s_t'            (lag-0 term)
  + Σ_(l=1)^L  w_l × [Σ_(t=l+1)^n s_t s_(t-l)' + transpose]
  where w_l = 1 - l/(L+1)   (Bartlett weight)

V_HAC = (X'X)⁻¹ S̃ (X'X)⁻¹
HAC_SE(β̂_j) = sqrt([V_HAC]_jj)
t_HAC = β̂_j / HAC_SE
p_HAC = 2 × CDF_t(|t_HAC|, df=n-k)   [t-distribution, same df as OLS]
```

**Key design decision:** The t-distribution with df = n-k is used for HAC p-values.
Some software implementations use the normal distribution (df → ∞); this produces
smaller p-values in small samples. This script uses the t-distribution consistently
throughout, which is the more conservative finite-sample approach.

**No pre-whitening** is applied. This is consistent with standard Newey-West (1987).

---

## 5. Durbin-Watson Statistic

```
DW = Σ_(t=2)^n (ê_t - ê_(t-1))² / Σ_t ê_t²
```

Computed on the OLS residual vector after each model is estimated.

---

## 6. R² and Adjusted R²

```
R² = 1 - SS_res / SS_tot      [SS_tot measured around the sample mean]
Adj-R² = 1 - (1-R²)(n-1)/(n-k)
```

---

## 7. VIF (Variance Inflation Factor)

For each non-intercept regressor X_j:
```
VIF_j = 1 / (1 - R²_j)
```
where R²_j is obtained by regressing X_j on all other regressors plus intercept.

VIF is **not applicable** (reported as N/A) for bivariate models with a single regressor,
because multicollinearity is a multi-regressor concept.

---

## 8. Source of Discrepancy between Phase 9B-C CSV and Report

Both Phase 9B-C files (`Phase_9B_C_Model_Comparison.csv` and `Phase_9B_C_Final_Reconciliation_Report.md`)
report the same point estimate β₂ = -0.8475 for MOD-05, but differ substantially in:

| Statistic | CSV value | Report value |
|:---|---:|---:|
| Conv SE (domestic production) | 0.1002 | 0.3444 |
| HAC SE (domestic production) | 0.0709 | 0.2882 |
| HAC t-stat | -11.96 | -2.941 |
| DW | 2.8549 | 1.637 |

The most likely sources of this discrepancy are:
1. **Different samples:** One estimate may have used N=25 (dropping one year) or included
   FY 2024-25 (which has no domestic production observation).
2. **Different variable ordering:** R and P swapped in the design matrix could not change
   β values but could affect SE calculations if intermediate numerics differed.
3. **Different HAC lag:** L=1 vs L=2 produces substantially different HAC SEs in small samples.
4. **Independent script runs with different implementations:** The report and CSV were generated
   by different Python scripts (`build_time_series_audit_md.py` vs `build_model_comparison_csv.py`).

The **Phase 9B-D canonical results** in `Phase_9B_D_Canonical_Model_Results.csv` supersede
both conflicting Phase 9B-C sources. All future manuscript references must use the canonical values.
