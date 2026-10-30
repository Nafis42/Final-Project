# Phase 3 Build Report: Construction of the Core Petroleum Supply-Chain Dataset

**Project:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** Phase 3 — Core Dataset Construction  
**Execution Date:** October 2026  
**Pipeline Status:** Verified Complete, Validated, and Auditable  
**Compliance:** Phase 3 executed strictly; stopped prior to Phase 4 exploratory data analysis and econometric modeling.  

---

## 1. Executive Summary & Deliverables Completed

Phase 3 has successfully integrated, standardized, validated, and documented the core historical datasets for the Indian petroleum supply chain. All deliverables reside in `03_Processed_Data/standardized/` (in dual `.csv` and `.parquet` formats) and `04_Analysis/phase3/`:

1. [`core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv) & [`.parquet`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.parquet) (30 periods, 36 columns)
2. [`petroleum_product_level_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/petroleum_product_level_dataset.csv) & [`.parquet`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/petroleum_product_level_dataset.parquet) (372 records, 17 columns)
3. [`petroleum_supporting_variables.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/petroleum_supporting_variables.csv) & [`.parquet`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/petroleum_supporting_variables.parquet) (27 periods, 19 columns)
4. [`derived_indicators.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/derived_indicators.csv) & [`.parquet`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/derived_indicators.parquet) (30 periods, 18 columns)
5. [`source_coverage_matrix.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/source_coverage_matrix.csv) (10 core & supporting variable domains)
6. [`core_dataset_provenance.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_dataset_provenance.csv) (300 record-level lineage entries)
7. [`dataset_schema_and_definitions.md`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/dataset_schema_and_definitions.md) (Complete specification)
8. [`graph_and_report_reference_catalogue.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase3/graph_and_report_reference_catalogue.csv) (50 published visualizations linked)
9. [`phase3_validation_report.md`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase3/phase3_validation_report.md) (100% PASS validation suite)
10. [`build_core_supply_chain_dataset.py`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/src/build_core_supply_chain_dataset.py) (Reproducible pipeline build script)

---

## 2. Integrated Variables & Sources Used

The integrated supply-chain dataset synthesizes 7 primary official PPAC series:

| Core Variable | Standardized Field Name | Primary Source File | Source Sheet | Native Unit | Standardized Units | Verified Time Coverage |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| **Domestic Crude Production** | `domestic_crude_production` | `1717395338_PT_Crude_oil_production_H.xls` | `Sheet1` | MMT | TMT & MMT | FY 1998–99 to 2023–24 |
| **Refinery Throughput** | `refinery_crude_processing` | `1788266304_PT_crude_processing_H.xls` | `Crude Processing` | TMT | TMT & MMT | FY 1998–99 to 2026–27 (June) |
| **Product Production** | `petroleum_product_production` | `1761642701_PT_production_product_H.xls` | `Product Production` | TMT | TMT & MMT | FY 1998–99 to 2025–26 (H1) |
| **Crude Imports** | `crude_import_quantity` | `1751964547_PT_IMPORT_TMT_H.xlsx` | `History` | TMT | TMT & MMT | FY 1998–99 to 2024–25 |
| **Crude Exports** | `crude_export_quantity` | `1751964547_PT_IMPORT_TMT_H.xlsx` | `History` | N/A | TMT & MMT | Unrecorded / Restricted |
| **Product Imports** | `petroleum_product_imports` | `1751964547_PT_IMPORT_TMT_H.xlsx` | `History` | TMT | TMT & MMT | FY 1998–99 to 2024–25 |
| **Product Exports** | `petroleum_product_exports` | `1751964547_PT_IMPORT_TMT_H.xlsx` | `History` | TMT | TMT & MMT | FY 1998–99 to 2024–25 |
| **Product Consumption** | `petroleum_product_consumption` | `1788343376_PT_Consumption_English.xls` | `Consumption` | TMT | TMT & MMT | FY 1997–98 to 2025–26 (P) |
| **Crude FOB Price** | `crude_price` | `1775133106_PP_Crude-Oil-FOB-Price...xlsx` | `Historical` | $/bbl | $/bbl. | FY 2000–01 to 2025–26 |
| **Crude Import Value** | `crude_import_value` | `1751964622_PT_IMPORT_VAL_US$_H.xlsx` | `History` | Million US$ | Million US$ & Rs. Cr | FY 1998–99 to 2024–25 |

---

## 3. Reporting Basis and Temporal Harmonization

- **Time Basis:** Official Indian Financial Year (1 April to 31 March). Financial years are preserved strictly and never relabeled as calendar years.
- **Anchor Key:** Standardized integer `fiscal_year_start` (e.g. 1998 for FY 1998–99) serves as the universal merge and time-series anchor.
- **Authoritative Baseline Period:** **FY 1998–99 to FY 2023–24 (26 Financial Years)** represents the unbroken, synchronized baseline where all supply-chain tiers possess complete verified observations.
- **Downstream Extended Period:** FY 2024–25 provides verified data for refinery throughput (268.61 MMT), product production (283.77 MMT), crude imports (232.53 MMT), product exports (61.94 MMT), and consumption (239.22 MMT), with domestic crude production explicitly left as `NaN`.

---

## 4. Derived Indicators Portfolio & Formulas

In accordance with Section 7, all derived indicators were constructed and saved separately in `derived_indicators.csv` without contaminating raw source observations:

1. **Net Crude Imports:**
   $$\text{Net Crude Imports} = \text{Crude Imports} - \text{Crude Exports}$$
   *(Crude exports = 0.0 under Indian statutory domestic processing mandate).*
2. **Crude Import-Dependence Proxy (%):**
   $$\text{Import-Dependence Proxy (\%)} = \frac{\text{Net Crude Imports}}{\text{Domestic Crude Production} + \text{Net Crude Imports}} \times 100$$
   *Rose from 54.88% in FY 1998–99 to 88.78% in FY 2023–24.*
3. **Production-to-Processing Ratio (%):**
   $$\text{Production-to-Processing Ratio (\%)} = \frac{\text{Domestic Crude Production}}{\text{Refinery Crude Processing}} \times 100$$
   *Declined from 47.74% in FY 1998–99 to 11.24% in FY 2023–24 as refining expanded.*
4. **Crude Import Unit Values (USD/MT, INR/MT, USD/bbl):**
   Derived from nominal trade values divided by physical import volumes. Tracks delivered costs (CIF) and quality premia relative to the FOB Indian Basket spot price.
5. **Refining Multiplier:**
   $$\text{Refining Multiplier} = \frac{\text{Refinery Crude Processing}}{\text{Domestic Crude Production}}$$
   *Expanded from 2.09x in FY 1998–99 to 8.90x in FY 2023–24.*
6. **Product Self-Sufficiency Ratio (%):**
   $$\text{Product Self-Sufficiency (\%)} = \frac{\text{Petroleum Product Production}}{\text{Petroleum Product Consumption}} \times 100$$
   *Shifted from a deficit of 71.27% in FY 1998–99 to a structural surplus of 118.62% in FY 2024–25.*

---

## 5. Limitations Affecting Subsequent Analysis

1. **Upstream Domestic Crude Truncation:**
   - The upstream source workbook terminates at FY 2023–24 (P). Consequently, upstream econometric models cannot extend into FY 2024–25 without an updated upstream source file.
2. **Absence of Crude Oil Export Tracking:**
   - Because Indian regulations require domestic processing of indigenous crude, PPAC does not publish commercial crude exports. Net crude imports are numerically identical to gross crude imports.
3. **SEZ to DTA Sales Inclusion in Consumption (FY 2017–18):**
   - Econometricians evaluating consumption time-series must account for the inclusion of SEZ private sales from FY 2017–18 onwards using the provided `sez_dta_sales_included` indicator.
4. **BORL Corporate Amalgamation (2022):**
   - Bina refinery throughput transitioned from a standalone JV to `BPCL-BINA` in 2022. Corporate panel models must account for this merger.

---

## 6. Recommended Priorities for Phase 4

Upon receiving user approval, Phase 4 should focus on:
1. **Exploratory Data Analysis (EDA) & Long-Term Trend Profiles:**
   - Long-run growth trajectories (CAGR) across domestic production, refining throughput, trade, and consumption.
   - The transition of India from a refined product deficit nation to a major regional refining export hub.
2. **Import Exposure & Vulnerability Diagnostics:**
   - Structural widening of the crude import-dependence proxy (54.9% to 88.8%).
   - Price vs volume decomposition of the petroleum import bill.
   - Foreign exchange exposure and the impact of Rupee depreciation on domestic landed costs.
3. **Product-Level Supply-Demand Balances:**
   - Dieselization vs gasoline motorization trajectories.
   - Structural contraction of kerosene (SKO) vs expansion of LPG (PMUY impact).
   - Naphtha and petcoke industrial utilization trends.
4. **Econometric & Statistical Modeling:**
   - Price elasticity of crude and product demand.
   - Cointegration and vector autoregression (VAR) between crude prices, import expenditure, and domestic consumption.
