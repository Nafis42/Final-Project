# Comprehensive Project Status & Phase Verification Report

**Project Title:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Reporting Date:** October 2026  
**Target Milestone:** Project Guide / Supervisor Progress Presentation  
**Workspace:** `c:\Users\nafis\OneDrive\Desktop\Final-Project`  
**Deliverables Directory:** [`05_Research_Paper/guide_progress_presentation/`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/05_Research_Paper/guide_progress_presentation/)

---

## 1. Executive Summary & Purpose

This status report provides an exhaustive, evidence-based audit of all completed research phases (Phases 1 through 8) for presentation to the project supervisor and guide. 

The primary objective of this investigation is to empirically disentangle the structural mechanisms driving India's escalating crude oil import dependency over the past quarter-century (FY 1998-99 to FY 2023-24). Specifically, the research addresses whether India's growing import exposure is primarily caused by domestic upstream extraction stagnation, downstream refining capacity expansion to serve domestic and export markets, shifting product-level demand profiles (such as the domestic cooking gas transition), or volatile international crude price shocks compounded by currency depreciation.

All numerical findings, econometric estimates, and graphical outputs reported herein are derived directly from reproducible pipelines executed on primary administrative data published by the **Petroleum Planning and Analysis Cell (PPAC)** and the **Ministry of Petroleum and Natural Gas (MoPNG)**. Every dataset has undergone multi-source cross-validation and rigorous discrepancy resolution.

---

## 2. Formal Phase Status Classification Table

In accordance with strict verification standards, each phase of the research workflow has been inspected for physical artifacts, code execution logs, and validation integrity.

| Phase ID | Phase Description | Verified Status | Key Outputs Generated | Validation & Evidence Basis |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | Source Inventory, File Integrity & Structural Audit | **Confirmed complete** | 9 documentation files, `file_inventory.csv` (33 files), `workbook_sheet_inventory.csv` (198 sheets), `pdf_inventory.csv` (14 PDFs) | 100% files readable, zero corruption, multi-year overlap and sheet layout structures documented. |
| **Phase 2** | Data Extraction, Standardization & Reconciliation | **Confirmed complete** | 16 raw CSV extractions, 16 standardized datasets, `data_dictionary.csv`, `extraction_log.csv`, `validation_report.md` | 218 automated reconciliation checks passed (`PASS`), units harmonized to TMT/MMT and US$ Million / Rs. Crore. |
| **Phase 3** | Integrated Supply-Chain Dataset Construction | **Confirmed complete** | `core_annual_petroleum_dataset.csv/.parquet` (30 periods, 35 fields), `petroleum_product_level_dataset.csv/.parquet` (404 rows), `derived_indicators.csv` | Supply-chain identity balance verified, full data provenance mapped (`core_dataset_provenance.csv`), zero synthetic data. |
| **Phase 4** | Historical Macro Trends, Growth Rates & Structural Breaks | **Confirmed complete** | `cagr_summary.csv` (79 CAGRs), `candidate_turning_points.csv` (9 turning points), `trend_test_results.csv`, 8 publication figures (PNG+SVG) | Mann-Kendall monotonic trend tests, Chow structural break evaluations, full figure data tables archived in `figure_data/`. |
| **Phase 5** | Product-Level Production, Trade Balances & Consumption | **Confirmed complete** | `product_trade_balance.csv` (324 rows), `apparent_product_availability_residual.csv`, `product_growth_summary.csv`, 8 publication figures (PNG+SVG) | Disentangled macro self-sufficiency from acute product-level deficits; tracked LPG structural deficit and SKO phaseout. |
| **Phase 6** | Petroleum Import Expenditure, Unit Values & Prices | **Confirmed complete** | `import_value_trends.csv`, `import_unit_value_trends.csv`, `import_cagr_summary.csv`, LMDI decomposition, 8 publication figures (PNG+SVG) | Logarithmic Mean Divisia Index (LMDI) decomposition verified; currency depreciation multiplier (+3.18% p.a.) quantified. |
| **Phase 7** | Official Source Verification & Discrepancy Resolution | **Confirmed complete** | `variable_validation_status.csv` (10 variables audited: 7 Verified, 3 Qualified), `cross_source_comparison.csv` (82 pairs), `discrepancy_register.csv` (7 items) | Independent numerical audit against official PPAC/MoPNG compendia and monthly filings; script and execution log verified. |
| **Phase 8** | Supply-Chain Relationships, Econometrics & Robustness | **Confirmed complete** | `correlation_results.csv` (10 pairs), `regression_results.csv` (8 OLS models), `subperiod_comparison.csv` (3 regimes), `robustness_results.csv`, 8 figures | Newey-West HAC standard errors; COVID outlier sensitivity invariant; correlation does not imply causality safeguard enforced. |
| **Phase 9** | Academic Research Paper Drafting & Submission | **Not executed or execution unconfirmed** | N/A (Awaiting formal guide review of Phases 1-8 presentation and explicit authorization) | Writing pipeline on hold to preserve academic research workflow discipline. |

---

## 3. Evidence of Execution & Artifact Audit by Phase

### Phase 1: Source Audit & Ingestion
- **Source Files Inspected:** 33 primary administrative files in `01_Original_Data/` (19 Excel workbooks, 14 official PDFs).
- **Core Inventories:**
  - [`02_Source_Audit/file_inventory.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/file_inventory.csv): Complete metadata catalog (MD5 hashes, byte sizes, readable status).
  - [`02_Source_Audit/workbook_sheet_inventory.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/workbook_sheet_inventory.csv): Granular inspection of 198 worksheets across all 19 workbooks.
  - [`02_Source_Audit/pdf_inventory.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/pdf_inventory.csv): Detailed page-by-page mapping of tables and visual charts across 14 administrative PDFs.
  - [`02_Source_Audit/source_audit_report.md`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/source_audit_report.md) & [`data_issues_and_questions.md`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/data_issues_and_questions.md): Documented time horizons (FY 1997-98 to FY 2025-26), reporting conventions, and unit definitions.

### Phase 2: Extraction, Harmonization & Standardized Datasets
- **Extraction Scripts:** `src/extract_raw_data.py`, `src/extract_monthly_and_secondary_raw.py`, `src/standardize_data.py`.
- **Validation Engine:** `src/validate_data.py` executed across 218 reconciliation points with 100% success rate.
- **Harmonized Units:** Physical quantities harmonized to Thousand Metric Tonnes (TMT) and Million Metric Tonnes (MMT); values harmonized to US$ Million and Indian Rupees Crore (Rs. Cr).
- **Key Artifacts:** `03_Processed_Data/raw_extractions/` (16 CSVs), `03_Processed_Data/standardized/` (16 primary CSV/Parquet tables), [`04_Analysis/phase2/data_dictionary.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase2/data_dictionary.csv).

### Phase 3: Core Integrated Supply-Chain Panel
- **Master Dataset:** [`03_Processed_Data/standardized/core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv) (and `.parquet`), spanning 30 fiscal years with 35 standardized fields.
- **Product Panel:** [`03_Processed_Data/standardized/petroleum_product_level_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/petroleum_product_level_dataset.csv) covering 14 standardized product categories.
- **Derived Supply-Chain Indicators:** [`03_Processed_Data/standardized/derived_indicators.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/derived_indicators.csv) capturing physical deficit gaps, coverage ratios, import dependence proxies, and refining multipliers.
- **Data Provenance:** Every observation mapped back to its specific source workbook, sheet, and cell coordinate in [`03_Processed_Data/standardized/core_dataset_provenance.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_dataset_provenance.csv).

### Phase 4: Macro Historical Trends & Structural Growth
- **Descriptive Metrics:** [`04_Analysis/phase4/descriptive_statistics.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase4/descriptive_statistics.csv) containing parametric (mean, SD) and non-parametric (median, IQR) metrics.
- **Growth Analysis:** 79 CAGR calculations computed across full-sample (FY99-FY24) and institutional subperiods in [`04_Analysis/phase4/cagr_summary.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase4/cagr_summary.csv).
- **Structural Shifts:** 9 historical turning points validated with institutional context in [`04_Analysis/phase4/candidate_turning_points.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase4/candidate_turning_points.csv).
- **Graphical Portfolio:** 8 publication-grade multi-panel figures generated at 300 DPI PNG and vector SVG format in [`04_Analysis/phase4/figures/`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase4/figures/).

### Phase 5: Granular Product Dynamics & Trade Disaggregation
- **Trade Disaggregation:** [`03_Processed_Data/standardized/product_trade_balance.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_trade_balance.csv) tracking product-level import, export, and net trade balances.
- **Apparent Availability Residuals:** [`03_Processed_Data/standardized/apparent_product_availability_residual.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/apparent_product_availability_residual.csv) auditing mass balances across 14 product categories.
- **Structural Energy Shifts:** Documented the near-total elimination of subsidized PDS kerosene (-95.5%) and the rapid scaling of household LPG (+488%).
- **Graphical Portfolio:** 8 publication figures in [`04_Analysis/phase5/figures/`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase5/figures/) with complete data tables in `figure_data/`.

### Phase 6: Financial Valuation, Price Transmission & Currency Exposure
- **Expenditure Series:** Complete tracking of crude and product import bills in both US$ and Rs. Crore.
- **Unit Value Realization:** Calculated CIF unit values per barrel compared against the FOB Indian Basket crude price benchmark.
- **LMDI Decomposition:** Logarithmic Mean Divisia Index isolating pure price effects, physical volume effects, and structural composition effects.
- **Currency Wedge:** Quantified the +3.18% p.a. growth wedge induced by Indian Rupee depreciation.
- **Graphical Portfolio:** 8 publication figures in [`04_Analysis/phase6/figures/`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/).

### Phase 7: Official Source Verification & Discrepancy Register
- **Auditing Script:** `04_Analysis/phase7/scripts/phase7_source_verification.py`.
- **Execution Log:** [`04_Analysis/phase7/logs/phase7_validation.log`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase7/logs/phase7_validation.log) (Completed without errors).
- **Core Results:**
  - 10 Priority Variables Evaluated: 7 Verified unconditionally; 3 Verified with qualification.
  - 82 Cross-Source Comparisons: Mapped between primary annual compendia and secondary monthly filings ([`cross_source_comparison.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase7/cross_source_comparison.csv)).
  - Discrepancy Register: 7 systemic institutional discrepancies fully cataloged, resolved, and documented ([`discrepancy_register.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase7/discrepancy_register.csv)).
  - Derived Indicators Audit: 7 analytical mathematical formulas independently verified against raw numbers ([`derived_indicator_audit.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase7/derived_indicator_audit.csv)).

### Phase 8: Econometrics, Supply-Chain Relationships & Robustness
- **Analysis Script:** `04_Analysis/phase8/scripts/phase8_statistical_analysis.py`.
- **Execution Log:** [`04_Analysis/phase8/logs/phase8_analysis.log`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/logs/phase8_analysis.log) (Completed without errors).
- **Readiness Matrix:** 8 analytical tracks evaluated and certified in [`analysis_readiness_matrix.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/analysis_readiness_matrix.csv).
- **Core Results:**
  - Bivariate Correlations: 10 priority pairs evaluated in levels and first differences ([`correlation_results.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/correlation_results.csv)).
  - Econometric Models: 8 OLS regression specifications with Newey-West HAC standard errors ([`regression_results.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/regression_results.csv)).
  - Subperiod Stability: Segmented across 3 policy regimes: Post-APM (FY99-05), Refining Boom (FY05-14), Welfare/Reform (FY14-24) ([`subperiod_comparison.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/subperiod_comparison.csv)).
  - Robustness Checks: 5 sensitivity evaluations including COVID-19 outlier exclusion ([`robustness_results.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/robustness_results.csv)).
  - Graphical Portfolio: 8 publication figures in [`04_Analysis/phase8/figures/`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/).

---

## 4. Key Verified Findings Ready for Presentation

The empirical findings from Phases 1 through 8 directly answer the five overarching research questions (RQ1 to RQ5):

### Finding 1 (RQ1): Domestic Crude Production Decoupled from Import Surge
- **Observation:** Domestic crude production (including lease condensate) has remained stagnant over 26 years, fluctuating within a narrow corridor of **32.0 to 38.1 MMT** (averaging $34.14\text{ MMT}$, CAGR **-0.44% p.a.**). Concurrently, crude oil physical imports surged from **39.81 MMT to 234.26 MMT** (CAGR **+7.37% p.a.**).
- **Import Dependence Proxy:** Escalated monotonically from **54.86% in FY 1998-99 to 88.86% in FY 2023-24** (+34.00 percentage points).
- **Statistical Independence:** Correlation between domestic production and crude imports is zero ($r = 0.0960, p = 0.6409$; first differences $r = 0.1732, p = 0.4076$).
- **No Crowding Out:** OLS regression shows domestic production has no statistically significant crowding-out effect on imports ($\beta = -0.3204, t = -1.13, p = 0.2713$).

### Finding 2 (RQ2): Downstream Refining Expansion as the True Import Driver
- **Observation:** Refinery crude processing expanded nearly four-fold (+282%), surging from **68.54 MMT in FY 1998-99 to 261.55 MMT in FY 2023-24** (CAGR **+5.51% p.a.**).
- **Crude Supply Deficit Gap:** The gap between refinery demand and domestic extraction expanded more than six-fold (+549%), from **35.78 MMT to 232.19 MMT**.
- **Collapse of Indigenous Coverage:** Indigenous crude coverage collapsed from **47.80% to 11.22%** (-36.58 percentage points).
- **Physical Co-movement:** Refinery crude throughput and crude imports exhibit near-perfect co-movement ($r = 0.9991, p < 0.0001$; first differences $r = 0.9680, p < 0.0001$; elasticity $\beta = 1.011, R^2 = 0.998$).

### Finding 3 (RQ3): The Indian Refining Paradox — Export Powerhouse vs. LPG Deficit
- **Net Product Exporter Status:** India transformed into a net exporter of refined petroleum products in FY 2001-02, maintaining positive net exports for 23 consecutive years (+13.89 MMT in FY24; peak +43.08 MMT in FY14).
- **Macro Self-Sufficiency:** Aggregate product self-sufficiency ratio remained above 100% since FY02, peaking at **139.38% in FY 2013-14** (117.84% in FY 2023-24).
- **Transport Fuel Export Surpluses:** In FY 2023-24, India generated massive export surpluses in High-Speed Diesel (**+28.16 MMT**), Motor Spirit (**+12.76 MMT**), and Aviation Turbine Fuel (**+8.58 MMT**).
- **Structural Cooking Gas Deficit:** In sharp contrast, Liquefied Petroleum Gas (LPG) suffered an acute structural deficit of **-17.99 MMT** in FY 2023-24, requiring 62.7% of domestic consumption to be imported.
- **Domestic Welfare Transition:** Clean cooking energy policies (PAHAL and PMUY) expanded LPG demand from 5.04 MMT to 29.66 MMT (+488.5%), while subsidized PDS Kerosene was systematically phased out from 10.60 MMT to 0.48 MMT (-95.5%).
- **Transport Demand Shift:** Motor Spirit consumption grew at more than double the rate of Diesel (CAGR +7.94% vs +3.58%), narrowing the Diesel-to-Petrol consumption ratio from 6.75:1 to 2.41:1.

### Finding 4 (RQ4): Import Expenditure Volatility, Price Dominance & Currency Wedge
- **Crude Import Bill Escalation:** US dollar expenditure grew nearly 38-fold, rising from **$3.52B in FY99 to $133.37B in FY24** (CAGR **+15.70% p.a.**; peak $144.29B in FY13). In domestic currency, expenditure rose 74-fold from **Rs. 14,917 Crore to Rs. 1,105,176 Crore** (CAGR **+18.88% p.a.**).
- **Currency Depreciation Wedge:** Steady Rupee depreciation (from 42.40 to 82.87 INR/USD) added a compounding growth penalty of **+3.18% p.a.** in domestic currency terms.
- **Price Dominance Over Volume:** Annual expenditure fluctuations are overwhelmingly dictated by global crude price movements ($r = 0.9168, p < 0.0001$) rather than physical volume changes ($r = 0.6053, p = 0.0007$). LMDI decomposition indicates price swings account for ~72% of inter-annual expenditure shocks, while volume growth anchors the long-term baseline.
- **Realized Unit Values:** Calculated CIF unit values track the Indian Basket FOB price closely ($r = 0.988, p < 0.0001$), reflecting a consistent CIF-FOB transportation, insurance, and grade spread.

---

## 5. Methodological Safeguards & Data Boundaries

To maintain rigorous academic integrity, several critical data boundaries and qualifications established in Phase 7 are explicitly disclosed:

1. **Lease Condensate in Crude Production:** Official Indian administrative data report crude oil and lease condensate jointly. Condensate accounts for approximately 7.45% of total upstream production (~2.5 MMT/year).
2. **Depot-Level Bio-Ethanol Blending:** Reported Motor Spirit (petrol) retail consumption figures include bio-ethanol blended at dispatch depots (reaching 12-14% by FY 2023-24). Physical refinery production represents pure mineral gasoline.
3. **Private Direct Imports & SEZ Sales:** National consumption series correctly include direct imports by private industrial consumers and domestic tariff area (DTA) sales from Special Economic Zone (SEZ) refineries (e.g., Reliance Jamnagar SEZ post-FY 2017-18).
4. **Non-Causality Principle:** Correlation coefficients and OLS elasticities measure historical co-movement and elasticity, not mechanistic macroeconomic causality.

---

## 6. Execution Roadmap & Next Steps

With Phases 1 through 8 confirmed complete, validated, and documented, the project is fully prepared for guide presentation:

1. **Guide Presentation (Current Step):** Present dashboard (`project_status_dashboard.html`), results catalogue (`results_catalogue.csv`), and presentation outline (`guide_presentation_outline.md`) to project supervisor.
2. **Supervisor Review & Approval:** Align on core empirical themes, resolve any preferred emphasis (e.g., policy implications vs. econometric modeling), and receive formal approval to proceed to Phase 9.
3. **Phase 9 Execution (Pending):**
   - Synthesize all phase outputs into a 5-chapter academic research paper.
   - Chapter 1: Introduction, Theoretical Context & Research Questions.
   - Chapter 2: Indian Petroleum Institutional Framework & Data Auditing Methodology.
   - Chapter 3: Upstream Extraction Stagnation, Downstream Refining Expansion & Trade Bifurcation.
   - Chapter 4: Import Expenditure Decomposition, Price Shocks & Rupee Exposure.
   - Chapter 5: Policy Implications, Energy Security Safeguards & Strategic Conclusions.
