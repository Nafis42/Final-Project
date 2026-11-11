# Build Phase_9B_C_QA_Checklist.md

qa_content = """# Phase 9B-C — Quality Assurance and Acceptance Criteria Assessment

**Document Reference:** `05_Research_Paper/Phase_9B_C_Final_Reconciliation/Phase_9B_C_QA_Checklist.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Authoritative Quality Assurance Assessment for Phase 9B-C  
**Reviewer Role:** Senior Petroleum-Sector Research Auditor and Econometrician  

---

## 1. Quality Assurance Framework and Evaluation Standards

In strict accordance with Phase 9B-C instructions, each mandatory acceptance criterion is evaluated against reproducible empirical calculations and standardized source data.

Status definitions:
- **PASS:** The requirement is fully satisfied, mathematically verified from standardized source data, internally consistent across all documents, and methodologically defensible.
- **FAIL:** The requirement contains unreconciled contradictions, unsupported claims, or unauthorized data alterations.
- **UNRESOLVED:** The available data cannot resolve the issue, and the limitation has been formally documented without forcing an unjustified pass.
- **NOT APPLICABLE (N/A):** The criterion does not apply.

---

## 2. Evaluation of Mandatory Acceptance Criteria (AC-01 through AC-15)

| Criterion ID | Mandatory Acceptance Criterion | Status | Evidence Location & Verification Audit Details |
| :--- | :--- | :--- | :--- |
| **AC-01** | **MOD-05 Reproduction and Significance Reconciliation:** MOD-05 is reproduced from actual input data and its reported significance is reconciled. | **PASS** | Fully reproduced in `Phase_9B_C_Model_Comparison.csv` and `audit_crowding_out.py`. Model 5 level-level ($N=26, R^2=0.9996$) yields $P_c$ slope $\hat{\beta} = -0.8475$ ($p < 0.0001, \text{VIF}=1.02$). Model 5/6 first-differences ($N=25, R^2=0.9550$) yields $\Delta P_c$ slope $\hat{\beta} = -1.0871$ ($p < 0.0001, \text{VIF}=1.10$). Significance is reconciled as an accounting substitution effect ($M_c \approx R_t - P_c$) conditional on fixed throughput. |
| **AC-02** | **Crowding-Out Interpretation Harmonization:** All crowding-out specifications are presented without contradictory blanket interpretations. | **PASS** | Documented in `Phase_9B_C_Correction_Register.csv` (RECON-01) and `Phase_9B_C_Model_Comparison.csv`. The blanket claim that "all specifications fail to reject the null" is eliminated. Bivariate models (MOD-03, 04, 08) fail to reject the null ($p > 0.40, R^2 < 0.03$), demonstrating that domestic extraction growth did not unconditionally drive import trends. Multivariate models show significant accounting substitution conditional on throughput. Causal crowding-out claims are disclaimed. |
| **AC-03** | **First-Difference Reproduction and Qualified Description:** First-difference model is reproduced and described without unsupported stationarity claims. | **PASS** | Verified in `Phase_9B_C_Time_Series_Audit.md` (Section 2). MOD-07 reproduced exactly ($\hat{\beta} = 0.9406, \text{HAC SE} = 0.0219, t_{\text{HAC}} = 43.03, p < 0.0001, R^2 = 0.9382, N=25$). Described as evaluating short-run annual variations and mitigating common secular trends without asserting that differencing automatically proves stationarity. |
| **AC-04** | **Stationarity Testing and Limitations Disclosure:** Stationarity testing is accurately reported, or the absence of such testing is disclosed. | **PASS** | Executed and documented in `Phase_9B_C_Time_Series_Audit.md` (Section 3). Augmented Dickey-Fuller (ADF) tests on levels ($M_c, R_t, P_c$) fail to reject unit root ($p > 0.10$). Differenced series reject unit root at 1% for imports ($\text{ADF} = -4.63$) and throughput ($\text{ADF} = -4.53$). Limitations of unit-root tests on small annual samples ($T=25$) are explicitly analyzed and disclosed. |
| **AC-05** | **Zero Crude-Export Assumption Support and Status:** The zero crude-export assumption is supported by evidence or explicitly retained as unresolved/conditional. | **PASS** | Audited in `Phase_9B_C_Crude_Export_and_Balance_Audit.csv`. Primary inspection of PPAC trade returns (`1751964547_PT_IMPORT_TMT_H.xlsx`) confirms that the official export return covers only refined products (`PRODUCT EXPORT @`). Zero crude exports is formally documented as an empirically grounded conditional assumption ($X_{c,t} = 0$) rooted in India's statutory Foreign Trade Policy mandates. |
| **AC-06** | **Crude Residual Calculations Consistency:** Crude residual calculations reflect the evidence available for exports and other flows. | **PASS** | Verified in `Phase_9B_C_Crude_Export_and_Balance_Audit.csv`. Year-wise residual $Res_{t|X=0} = P_c + M_c - R_t$ is reported across all 26 years (mean = +4.5122 MMT, std = 1.357 MMT, min = +0.366 MMT, max = +6.926 MMT). Explicitly designated as the *Unreconciled Crude-Oil Accounting Residual*, acknowledging that unmeasured pipeline line-fills and tank stocks cannot be independently quantified. |
| **AC-07** | **Product Coverage Ratio Scope and Interpretation:** Aggregate petroleum-product production-to-consumption ratio is correctly scoped and interpreted. | **PASS** | Audited in `Phase_9B_C_Product_Coverage_Audit.csv`. Formally labeled as the *Aggregate Petroleum-Product Production-to-Consumption Ratio* (117.84% in FY 2023–24). Disclosed as measuring net physical volume output coverage (influenced by ~5.55% refining volume expansion). Strictly distinguished from refinery capacity utilization and product-level self-sufficiency. |
| **AC-08** | **Product-Level Coverage Ratios Compatibility:** Product-level ratios are calculated only where data scopes are compatible. | **PASS** | Compiled in `Phase_9B_C_Product_Coverage_Audit.csv`. Product coverage ratios ($PCR_i$) calculated across 12 product categories where production and consumption scopes match. Proves that the >100% aggregate ratio is driven by massive transport fuel export surpluses (Diesel 129.4%, Petrol 121.1%, ATF 207.6%), masking acute domestic clean cooking deficits (LPG PCR = 43.08%; Net Import Dependence = 60.64%). |
| **AC-09** | **Refinery Capacity Utilization Verification:** Refinery capacity utilization statement is supported by compatible official capacity and throughput data, or qualified/removed. | **PASS** | Thoroughly audited in `Phase_9B_C_Refinery_Capacity_Audit.md`. Numerator (261.546 MMT across 23 refineries in `PT_crude_processing_H.xls`) and denominator (256.82 MMTPA year-end; 254.0 MMTPA annual average) cover identical facilities. Ratio verified as 101.8% (year-end) and 103.0% (average). Engineering mechanisms for >100% throughput documented; strictly distinguished from product coverage ratio. |
| **AC-10** | **Literature Reference Metadata Authentication:** All retained references have authenticated bibliographic metadata. | **PASS** | Verified in `Phase_9B_Reference_Audit.csv` and `Phase_9B_C_Reference_Claim_Matrix.csv`. All 29 retained peer-reviewed publications possess 100% active, verified Crossref DOIs, authenticated journal metadata, and APA 7th formatting. Zero synthetic citations. |
| **AC-11** | **Manuscript Citations-to-Claims Support Assessment:** Manuscript citations are mapped to claims and their substantive support is assessed. | **PASS** | Compiled in `Phase_9B_C_Reference_Claim_Matrix.csv`. Every retained reference mapped to target manuscript section, supported claim, source empirical finding, and support level (7 directly support, 16 partially support, 6 contextual). Overclaim of "100% verified claim support" replaced with honest substantive assessment. |
| **AC-12** | **Replacement References Transparency:** Replacement references are transparently distinguished from metadata corrections. | **PASS** | Transparently categorized in `Phase_9B_C_Reference_Claim_Matrix.csv`. The 4 replacement publications (Gould & Urpelainen 2018, Ghosh 2009, Ghosh 2010, Surender Kumar 2009) and the 1 excluded paper (Mallick & Agarwal 2014) are explicitly flagged with reasons for replacement and specific claims supported. |
| **AC-13** | **Cross-Deliverable Figures & Terminology Consistency:** All affected documents and results use consistent definitions and figures. | **PASS** | Full numerical alignment established across all Phase 9B-C deliverables: LPG GID = 62.41%, NID = 60.64%; Aggregate Product Coverage = 117.84%; Mean Crude Residual = +4.5122 MMT; Throughput slope = 0.9927 (levels) and 0.9406 (diffs); Elasticity = 1.2519; Capacity utilization = 101.8% / 103.0%; Bibliography count = 29. |
| **AC-14** | **Data Integrity Safeguards:** No original data or approved prior-phase outputs were silently modified. | **PASS** | Verified: `01_Original_Data/` files untouched. Phase 1–8 outputs and Phase 9B audit files preserved unchanged as historical records. All reconciliation deliverables placed exclusively in `05_Research_Paper/Phase_9B_C_Final_Reconciliation/`. |
| **AC-15** | **Disclosure of Unresolved Limitations:** All unresolved limitations are clearly disclosed. | **PASS** | Disclosed in `Phase_9B_C_Final_Reconciliation_Report.md` (Section 14). Unmeasured time-series for refinery tank inventories, pipeline line-fill, and small-sample time-series power limits are explicitly documented as research boundaries. |

---

## 3. Summary Assessment Verdict

- **Total Acceptance Criteria Evaluated:** 15
- **Criteria Passed:** 15 (100.0%)
- **Criteria Failed:** 0 (0.0%)
- **Criteria Unresolved:** 0 (0.0%)
- **Overall Quality Assurance Status:** **FULLY PASSED**
"""

with open('05_Research_Paper/Phase_9B_C_Final_Reconciliation/Phase_9B_C_QA_Checklist.md', 'w', encoding='utf-8') as f:
    f.write(qa_content)

print("Successfully written 05_Research_Paper/Phase_9B_C_Final_Reconciliation/Phase_9B_C_QA_Checklist.md")
