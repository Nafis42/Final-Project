# Phase 9B — Quality Assurance and Acceptance Criteria Checklist

**Document Reference:** `05_Research_Paper/Phase_9B_Correction_Audit/Phase_9B_QA_Checklist.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Authoritative Phase 9B Quality Assurance Assessment  

---

## 1. Quality Assurance Framework and Evaluation Standards

In accordance with the Phase 9B brief, each quality criterion is formally evaluated using one of four strict operational statuses:
- **PASS:** The requirement is fully satisfied, mathematically verified against original standardized datasets, traceable, and internally consistent across all Phase 9B deliverables.
- **FAIL:** The requirement contains uncorrected errors, contradictions, mathematical discrepancies, or unauthorized data alterations.
- **UNRESOLVED:** The available data or evidence cannot definitively resolve the issue, and the limitation has been formally documented without forcing an unjustified conclusion.
- **NOT APPLICABLE (N/A):** The criterion does not apply to the current audit phase.

---

## 2. Itemized Quality-Control Acceptance Checklist

| Item ID | Quality-Control Acceptance Criterion | Status | Evidence Location & Audit Verification Notes |
| :--- | :--- | :--- | :--- |
| **QC-01** | **LPG Gross and Net Import-Dependence Reproducibility:** LPG gross and net import-dependence calculations are independently reproducible from standardized source data. | **PASS** | Verified in `Phase_9B_Recalculated_Indicators.csv` (Row 26) and `audit_lpg.py`. Formulas explicitly evaluated: Gross Import-to-Consumption Ratio $	ext{GID} = (18,514.20 / 29,663.62) 	imes 100 = \mathbf{62.41\%}$; Net Import-to-Consumption Ratio $	ext{NID} = (17,988.82 / 29,663.62) 	imes 100 = \mathbf{60.64\%}$. All inputs trace to PPAC product series. |
| **QC-02** | **LPG 62.74% Discrepancy Resolution:** The 62.74% figure is either substantiated by a valid definition and source or removed/corrected. | **PASS** | Fully investigated and corrected in `Phase_9B_Correction_Register.csv` (CORR-01) and `Phase_9B_Final_Correction_Report.md`. Proved that $(18.10 - 0.11) / 30.40 	imes 100 = 59.18\%$, demonstrating that 62.74% was an uncalculated transcription error. The unverified 62.74% figure has been purged and replaced with verified 62.41% (GID) and 60.64% (NID). |
| **QC-03** | **Refining Coverage Ratio Consistency:** The refining coverage ratio is recalculated from compatible, traceable series, or marked unresolved. | **PASS** | Verified in `Phase_9B_Recalculated_Indicators.csv` (Row 26) and `derived_indicators.csv`. For FY 2023–24, ratio is exactly $\mathbf{117.84\%}$ ($276.058 / 234.259 	imes 100$). The 118.37% value in Phase 9A was reconciled as an artifact of preliminary unrevised consumption (233.28 MMT). All occurrences standardized on 117.84%. |
| **QC-04** | **Refining Coverage Ratio Conceptual Boundaries:** Coverage ratio is not described as refinery capacity utilization. | **PASS** | Documented in `Phase_9B_Correction_Register.csv` (CORR-05) and `Phase_9B_Revised_Manuscript_Outline.md` (Section 3.3). Clearly defined as *Downstream Physical Product Output Coverage Ratio* of domestic consumption (influenced by ~5.55% volumetric refining gain); distinguished from rated nameplate capacity utilization (MMTPA). |
| **QC-05** | **Crude-Oil Balance Identity & Sign Conventions:** The crude-oil balance uses a clearly defined identity and sign convention. | **PASS** | Formally specified in `Phase_9B_Regression_Audit.md` and `Phase_9B_Revised_Manuscript_Outline.md`: $P_{c,t} + M_{c,t} - X_{c,t} = R_t + \Delta S_{c,t} + 	heta_t$, where $X_{c,t} = 0$ (statutory export ban). Domestic production-to-throughput gap defined as $R_t - P_{c,t}$. |
| **QC-06** | **Crude Residual Decomposition Safeguards:** The 4.41 MMT / 4.51 MMT residual is not attributed to unmeasured causes without data. | **PASS** | Verified in `Phase_9B_Correction_Register.csv` (CORR-06) and `Phase_9B_Recalculated_Indicators.csv`. The 26-year mean residual $	ext{Res}_t = M_{c,t} - (R_t - P_{c,t})$ is $+4.5122	ext{ MMT}$ (std = 1.357 MMT; range: +0.37 to +6.93 MMT). All unmeasured causal claims (stocks, ISPRL, transit loss) removed; formally designated as the *Unreconciled Crude-Oil Accounting Residual*. |
| **QC-07** | **Regression Coefficient Labeling and Reproducibility:** Regression coefficients are correctly labelled and reproducible. | **PASS** | Reproduced in `Phase_9B_Regression_Audit.md` via `audit_regressions.py`. All 8 models report exact sample size, coefficients, conventional SE, Newey-West HAC SE (maxlags=2), $t$-statistics, $p$-values, $R^2$, and Durbin-Watson statistics. |
| **QC-08** | **Level Slopes vs. Elasticities Distinction:** Level-level slopes are not called elasticities. | **PASS** | Enforced in `Phase_9B_Regression_Audit.md` (Section 3.1) and `Phase_9B_Revised_Manuscript_Outline.md` (Section 4.2). The OLS level slope $\hat{lpha}_1 = 0.9927$ is strictly labeled as a *marginal physical import slope* (MMT/MMT). The true elasticity is estimated from a separate log-log model ($\hat{\gamma}_1 = 1.2519, p < 0.0001$). |
| **QC-09** | **Time-Series Non-Stationarity Disclosure:** Non-stationarity limitations are disclosed accurately. | **PASS** | Documented in `Phase_9B_Regression_Audit.md` (Section 3.3). Explicitly acknowledges that HAC SEs do not solve non-stationarity; Durbin-Watson autocorrelation is reported; stationary first-differences model (MOD-07: $\hat{eta} = 0.9406, R^2 = 0.9382$) is provided as short-run verification. |
| **QC-10** | **Crowding-Out Interpretation Restraint:** Crowding-out findings are described without overclaiming. | **PASS** | Enforced in `Phase_9B_Correction_Register.csv` (CORR-11) and `Phase_9B_Regression_Audit.md` (Section 4.3). Causal claims of "proving no crowding-out" removed; phrased strictly as: *Observational regressions fail to reject the null hypothesis of no linear relationship at conventional significance levels ($p > 0.10, R^2 < 0.01$)*. |
| **QC-11** | **Literature Reference Status Internal Consistency:** Reference verification statuses are internally consistent and authenticated. | **PASS** | Audited in `Phase_9B_Reference_Audit.csv`. All 30 references classified into 4 mutually exclusive categories: Verified as originally entered (8), Corrected and subsequently verified (17), Corrected and verified Replacement (4), Unverified / Excluded (1). Zero synthetic citations; all DOIs resolve to genuine articles. |
| **QC-12** | **Unsupported Causal Claims Qualified or Removed:** Unsupported causal or mechanistic claims are qualified or removed. | **PASS** | Reviewed in `Phase_9B_Correction_Register.csv` (CORR-16, 17, 18). LPG yield determinism qualified; upstream NELP/HELP sweeping failure claims toned down to descriptive facts; "Triple Paradox" preserved strictly as an empirical organizing motif. |
| **QC-13** | **Cross-Deliverable Numerical & Terminological Consistency:** The revised outline, indicators, regressions, and correction register use consistent figures. | **PASS** | Cross-verified across all 7 Phase 9B deliverables: LPG GID = 62.41%, NID = 60.64%; Coverage Ratio = 117.84%; Mean Crude Residual = 4.51 MMT; Throughput slope = 0.993; Throughput elasticity = 1.252; Bibliography count = 29. |
| **QC-14** | **Traceability of Corrections:** Every material correction is traceable to a source file, table, and formula. | **PASS** | Every entry in `Phase_9B_Correction_Register.csv` includes exact source file, table/sheet, financial year, mathematical formula, evidence status, and resolution status. |
| **QC-15** | **Study-Period and Panel Integrity Safeguard:** Balanced panel strictly maintained as FY 1998–99 to FY 2023–24 ($N=26$). | **PASS** | Enforced in `Phase_9B_Recalculated_Indicators.csv`. FY 1997–98 excluded from balanced supply-chain calculations due to missing upstream data; retained solely as downstream demand baseline. |
| **QC-16** | **Strict Phase 9B STOP Enforcement:** No manuscript prose, no abstract, no automatic launch of Phase 10. | **PASS** | Full manuscript drafting and abstract are strictly withheld. Awaiting explicit user review and authorization. |

---

## 3. Summary Quality Audit Verdict

- **Total Criteria Evaluated:** 16
- **Passed:** 16 (100.0%)
- **Failed:** 0 (0.0%)
- **Unresolved:** 0 (0.0%)
- **Overall Audit Status:** **FULLY PASSED**

The Phase 9B targeted correction and re-audit has successfully resolved all mathematical discrepancies, eliminated overconfident causal claims, authenticated the literature base, and produced a completely harmonized empirical foundation.
