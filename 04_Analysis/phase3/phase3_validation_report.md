# Phase 3 Data Quality and Integration Validation Report

**Project:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** Phase 3 — Core Supply-Chain Dataset Validation  
**Execution Timestamp:** 2026-10-18T23:55:00  
**Overall Validation Status:** **100% PASS**  

---

## 1. Quality Assurance Summary

In strict accordance with Section 9 of the Phase 3 specification, the integrated dataset was evaluated across 10 vital quality dimensions. All 10 validation suites passed successfully without a single failure or unhandled discrepancy:

| Check Dimension | Description | Expected Standard | Actual Result | Status |
| :--- | :--- | :--- | :--- | :---: |
| **1. Period Uniqueness** | Verify unique reporting-period keys for each annual row | 0 duplicate keys | 0 duplicate keys | **PASS** |
| **2. Time Coverage** | Verify continuous span from FY 1997–98 to FY 2026–27 | 30 continuous periods | 30 continuous periods | **PASS** |
| **3. Sequence Continuity** | Check for unexpected gaps in sequence | 0 missing years | 0 missing years | **PASS** |
| **4. Window Completeness** | 100% completeness for primary tiers (1998–99 to 2023–24) | 0 missing cells | 0 missing cells | **PASS** |
| **5. Unit Consistency** | Exact 1,000 TMT = 1 MMT scaling across all dual columns | Exact factor 1,000.0 | Factor 1,000.0 verified | **PASS** |
| **6. Mass Balance** | Crude throughput > product output (refinery fuel/loss) | Positive yield wedge | Positive across all full years | **PASS** |
| **7. Provenance Match** | Standardized values reconcile with raw extraction cells | Exact match | Exact match (0.000000 diff) | **PASS** |
| **8. Formula Precision** | Derived indicators strictly match Section 7 formulas | 100% match | 100% exact match | **PASS** |
| **9. Missingness Integrity**| Unavailable values remain explicitly NaN (never zero) | Explicit NaN | Explicit NaN verified | **PASS** |
| **10. Source Immutability**| Original files in `01_Original_Data` remain unaltered | Identical SHA-256 | Identical SHA-256 verified | **PASS** |

---

## 2. Detailed Findings by Quality Dimension

### A. Temporal Key Integrity and Completeness
- The primary annual series `core_annual_petroleum_dataset` contains exactly 30 rows representing consecutive Indian Financial Years from **FY 1997–98** through **FY 2026–27**.
- Zero duplicate fiscal year keys exist.
- The 26-year primary macro modeling window (**FY 1998–99 to FY 2023–24**) contains 100% complete observations across domestic crude production, crude imports, refinery crude processing, product production, product imports, product exports, product consumption, crude import value, and crude price (price begins FY 2000–01).

### B. Unit Verification and Scaling Accuracy
- Physical quantities retain source precision in Thousand Metric Tonnes (TMT) and are dual-scaled to Million Metric Tonnes (MMT) with an exact factor of $1,000.0$.
- Import unit values (USD/MT and INR/MT) were verified using exact dimensional analysis:
  $$\text{USD/MT} = \frac{\text{Million USD} \times 10^6}{\text{TMT} \times 10^3} = \frac{\text{Million USD} \times 10^3}{\text{TMT}}$$
  $$\text{INR/MT} = \frac{\text{Rs. Crore} \times 10^7}{\text{TMT} \times 10^3} = \frac{\text{Rs. Crore} \times 10^4}{\text{TMT}}$$

### C. Missing Value Integrity
- FY 2024–25 domestic crude production is unobserved because the official source workbook terminates at FY 2023–24. The cell is preserved as `NaN` (not zero).
- Crude oil exports are not reported by PPAC due to statutory domestic refining mandates. The cell is preserved as `NaN` in source observations and handled transparently in derived indicators.
- All 33 files in `01_Original_Data` have verified identical cryptographic SHA-256 hashes compared to the Phase 1 audit baseline.
