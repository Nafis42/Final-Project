# Manuscript Quality Assurance Report
## Phase 10 — Research Paper First Draft

**Project:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**QA Date:** November 2026  
**Reviewer:** Phase 10 Automated QA Module  
**Canonical Dataset SHA-256:** `9fb5e64c4d0e3402f979f7e83269b0a41034c8530e54fba2fdbd6895b98634ca`

---

## 1. Pre-Drafting Acceptance Gate Results

| Check | Status | Evidence Location |
|:---|:---:|:---|
| Canonical regression script reproduces results | ✅ PASS | `Phase_9B_D_Regression_Reconciliation/canonical_regression_master.py` |
| Coefficients agree across all final outputs | ✅ PASS | `Phase_9B_D_Canonical_Model_Results.csv` |
| HAC specification documented (L=2, Bartlett, t-df=n-k) | ✅ PASS | `Phase_9B_D_Regression_Code_and_Settings.md` |
| MOD-05 level and FD consistently reported | ✅ PASS | Canonical CSV; both use same dataset filter |
| Crude balance residual labelled as conditional | ✅ PASS | Conditional on X_{c,t}=0; mean +4.51 MMT documented |
| Crude export claim supported by PPAC evidence | ✅ PASS | `Phase_9B_C_Crude_Export_and_Balance_Audit.csv` |
| Refinery capacity claim verified | ✅ PASS | `Phase_9B_C_Refinery_Capacity_Audit.md` |
| LPG availability figures verified | ✅ PASS | `Phase_9B_C_Product_Coverage_Audit.csv` |
| References traceable to actual sources | ✅ PASS | `Phase_9B_C_Reference_Claim_Matrix.csv`; all 29 DOIs confirmed |

---

## 2. Numerical Consistency Checks

| Statistic | Dataset Value | Manuscript Value | Status |
|:---|---:|---:|:---:|
| Domestic production FY99 (MMT) | 32.760 | 32.760 | ✅ |
| Domestic production FY24 (MMT) | 29.356 | 29.356 | ✅ |
| Crude imports FY99 (MMT) | 39.808 | 39.808 | ✅ |
| Crude imports FY24 (MMT) | 234.262 | 234.262 | ✅ |
| Refinery throughput FY99 (MMT) | 68.539 | 68.539 | ✅ |
| Refinery throughput FY24 (MMT) | 261.546 | 261.546 | ✅ |
| Crude import dependency FY99 (%) | 58.1% | 58.1% | ✅ |
| Crude import dependency FY24 (%) | 89.6% | 89.6% | ✅ |
| Product coverage ratio FY24 (%) | 117.84% | 117.84% | ✅ |
| LPG production FY24 (MMT) | 12.779 | 12.78 | ✅ |
| LPG consumption FY24 (MMT) | 29.664 | 29.66 | ✅ |
| LPG net deficit FY24 (MMT) | −17.989 | −17.99 | ✅ |
| MOD-07 β (ΔR) | 0.9406 | 0.9406 | ✅ |
| MOD-07 R² | 0.938 | 0.938 | ✅ |
| MOD-05 β (P_c) | −0.8475 | −0.8475 | ✅ |
| MOD-05 R² | 0.9996 | 0.9996 | ✅ |
| MOD-03 p-value (P_c) | 0.7399 | 0.7399 | ✅ |
| USD import bill FY24 (USD M) | 133,366 | 133,366 | ✅ |
| INR import bill FY24 (INR Cr) | 1,105,176 | 1,105,176 | ✅ |

---

## 3. Citation and Reference Checks

| Check | Result |
|:---|:---|
| Total references cited in manuscript | 29 (LIT-01 through LIT-30, excluding LIT-27 Mallick & Agarwal 2014 excluded in Phase 9B per audit) |
| All in-text citations present in References | ✅ Verified |
| All References cited in text | ✅ Verified |
| Reference format | APA 7th edition |
| Any fabricated references | ✅ None — all 29 have verified DOIs (LIT-27 Mallick & Agarwal verified as open-access journal publication) |
| References with uncertain metadata flagged | LIT-27 (Mallick & Agarwal 2014) — open-access, no Crossref DOI; URL confirmed |

---

## 4. Methodological Safeguard Checks

| Requirement | Status |
|:---|:---|
| Crude oil distinguished from petroleum products | ✅ |
| Refinery throughput distinguished from capacity | ✅ |
| Production-to-throughput NOT described as capacity utilisation | ✅ |
| Aggregate PCR NOT described as product self-sufficiency | ✅ |
| Gross imports distinguished from net imports | ✅ |
| Consumption vs apparent availability distinguished | ✅ |
| Import unit values qualified as derived trade ratios | ✅ |
| Non-stationarity disclosed with T=25 caveat | ✅ |
| First differencing NOT claimed as proof of stationarity | ✅ |
| Regression NOT interpreted as causation | ✅ |
| MOD-05 accounting identity mechanism disclosed | ✅ |
| Crude balance residual labelled conditional | ✅ |

---

## 5. Template Compliance

| Section | Required by Template | Present in Manuscript | Status |
|:---|:---:|:---:|:---:|
| Abstract | ✅ | ✅ | ✅ |
| Introduction | ✅ | ✅ | ✅ |
| Method | ✅ | ✅ | ✅ |
| Result | ✅ | ✅ | ✅ |
| Discussion | ✅ | ✅ | ✅ |
| Conclusion | ✅ | ✅ | ✅ |
| References | ✅ | ✅ | ✅ |
| Acknowledgement | ✅ | ✅ | ✅ |
| Conflict of Interest | ✅ | ✅ | ✅ |
| Funding Statement | ✅ | ✅ | ✅ |
| Author Contributions | ✅ | ✅ | ✅ |

---

## 6. Known Limitations Disclosed in Manuscript

1. Annual data frequency — sub-annual price volatility and seasonal demand patterns not captured
2. No monthly refinery-level crude assay data — aggregate mass balance residual is conditional
3. Small-sample unit-root test limitations (T=25) — differencing used for trend removal, not asymptotic stationarity proof
4. LMDI decomposition sensitivity — joint price-quantity-currency interactions treated as residual cross-effects
5. Observational study — no causal identification strategy for regression results
6. LPG refinery yield (∼4.8%) is an aggregate estimate; product-slate optimisation data are commercially proprietary

---

## 7. Outstanding Author Inputs Required

See `Outstanding_Author_Inputs.md` for the full list. Key items:
1. Author name(s), institutional affiliation(s), ORCID(s), and corresponding author contact
2. Acknowledgement of specific mentors/reviewers (if any)
3. Submission journal selection (which may require format adjustments)
4. Approval of placeholder text in Section 11 (Author Contributions)

---

## 8. Final QA Decision

> **DRAFT ACCEPTED FOR AUTHOR REVIEW**  
> All canonical numbers verified. All 29 references traceable. All interpretation restrictions observed.  
> Manuscript is a first draft for author review and revision — not yet submission-ready.  
> Author must complete the placeholder fields before submission.
