# Existing Graphs, Figures, Reports, and Findings Summary

**Project:** *India's Petroleum Supply Chain and Import Exposure*  
**Deliverable:** `02_Source_Audit/existing_findings_summary.md`  
**Phase:** Phase 2 Supplementary Audit & Review  
**Date:** October 2026  
**Status:** Complete  

---

## 1. Overview of Existing Visualizations and Reports

In accordance with the project instructions, a comprehensive audit was conducted across all 29 Excel workbooks and 4 PDF reports in [`01_Original_Data`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data) to inventory all pre-existing visualizations, charts, dashboards, statistical tables, and published narrative interpretations.

A total of **50 graphical figures and visualization sheets** and **4 major official reports containing 19 core tables** were inventoried and cataloged in:
- [`02_Source_Audit/existing_graphs_and_figures.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/existing_graphs_and_figures.csv)
- [`02_Source_Audit/chart_data_availability.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/chart_data_availability.csv)
- [`02_Source_Audit/relevant_reports_and_tables.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/relevant_reports_and_tables.csv)

---

## 2. Visualizations in Excel Workbooks

Across the 29 Excel workbooks, the majority of PPAC files are formatted strictly as tabular reporting matrices without embedded charts. However, two specific visualization assets were identified:

1. **Dedicated Visualization Worksheet (`1781164814_NG-H_LNG_Consumption.xlsx`):**
   - **Sheet Name:** `Graph` (Worksheet index 2).
   - **Type:** Dedicated interactive dashboard worksheet depicting the historical trend of natural gas consumption, domestic gas production, and LNG import consumption.
   - **Data Linkage:** Fully available. Fed directly from the adjacent worksheet `Historical Consumption ` (cells `A8:P17`).
   - **Relevance:** Pertains to natural gas and LNG (classified as an adjacent/secondary domain in Phase 1).

2. **Embedded Drawings in Secondary Workbooks:**
   - Minor embedded shape objects and formatting drawings were identified in `1761715894_petroleum-prices-and-under-recoveries.xlsx` and legacy files. None of the primary core historical workbooks (`PT_Crude_oil_production_H.xls`, `PT_crude_processing_H.xls`, `PT_production_product_H.xls`, `PT_IMPORT_TMT_H.xlsx`) rely on embedded chart objects for data presentation; all underlying data are stored as native worksheet cells.

---

## 3. Published Figures and Dashboards in Official PDF Reports

The four supplied PDF reports contain extensive visualization frameworks representing the official statistical and analytical perspective of the Petroleum Planning & Analysis Cell (PPAC):

### 3.1 PPAC Industry Consumption Report (ICR) — July 2026 (`1787315734_ICR_July 26.pdf`)
This 31-page report contains **44 distinct figures** and **10 structured tables**:
- **National Monthly Consumption Profile:**
  - `Figure-A` (p. 9): Monthly POL consumption (MMT) since April 2023.
  - `Figure-B` (p. 9): POL domestic consumption profile & YoY growth rates.
- **Product-Specific Monthly Trends & Drivers:**
  - `Figure-C` & `Figure-D` (p. 10): State-wise growth in MS (Petrol) and monthly MS volumes (MMT) from April 2023 to July 2026.
  - `Figure-E` to `Figure-N` (pp. 12–23): HSD consumption patterns, rainfall deviations, commercial vehicle sales correlations, and toll collections.
  - `Figure-O` to `Figure-Q` (pp. 24–25): Monthly LPG consumption (MMT) and sectoral domestic vs non-domestic demand breakdowns.
  - `Figure-R` to `Figure-T` (pp. 26–27): State-wise ATF demand, aircraft movements, passenger traffic, and sectoral ATF offtake.
  - `Figure-U` to `Figure-Y` (pp. 28–31): Furnace Oil, Petcoke, LDO, and Natural Gas sectoral consumption pie charts.
- **Conversion Factor Benchmark:**
  - **`Table-9` (p. 31): Official conversion factors for MT to barrel conversion for 12 POL products.**

### 3.2 Revised Estimates FY 2025–26 Combined (`1773137026_Revised Estimates FY 2025-26_Combined.pdf`)
- Contains two authoritative national tables:
  - `Table-1` (p. 1): Product-wise Estimated Petroleum Product Consumption for FY 2025–26 across Sensitive Products (34.15 MMT), Major Decontrolled Products (178.61 MMT), and Minor Decontrolled Products (31.24 MMT), totaling **244.00 MMT (244,002 TMT)**.
  - `Table-2` (p. 2): State-wise and regional allocations of RE 2025–26 for LPG, MS, HSD, and ATF.

### 3.3 PPAC Flash Report on Oil & Gas — August 2026 (`1788266780_Flash_Report_WEB_UPLOAD_Aug26.pdf`)
- Single-page dashboard containing provisional monthly flash numbers for August 2026 (Petrol: 3,824 TMT; Diesel: 7,001 TMT; ATF: 720 TMT; LPG: 2,424 TMT) and cumulative FY 2026–27 (April–August) comparisons.

### 3.4 24th PPAC Foundation Day Report (`1748348757_Foundation_Day_Report_vfinal_26052025.pdf`)
- Contains presentation graphics and thematic infographics summarizing executive dialogues on energy security, refining modernization, green hydrogen, and bio-fuel blending.

---

## 4. Underlying Numerical Data Availability & Linkage

In [`chart_data_availability.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/02_Source_Audit/chart_data_availability.csv), every identified figure was evaluated against the underlying raw data:

* **Available (High Feasibility):** 46 figures (92%) have complete underlying numerical data available in either the monthly sheets of [`1788343376_PT_Consumption_English.xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1788343376_PT_Consumption_English.xls), [`1751964547_PT_IMPORT_TMT_H.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1751964547_PT_IMPORT_TMT_H.xlsx), or the report's own structured tables. These charts can be independently reconstructed and validated.
* **Partially Available / External:** 4 figures (8%) rely on external macro-economic indicators mentioned in the report narrative (such as FADA vehicle sales, GST e-way bills from `gstn.org.in`, and port cargo from `shipmin.gov.in`). These external series are noted as contextual benchmarks rather than core supply chain data.

> [!CAUTION]
> **Methodological Rule:** Under no circumstances will values estimated visually from PDF chart pixels be treated as exact observations. All empirical modeling in this project must derive strictly from machine-extracted numerical tables.

---

## 5. Summary of Published Findings vs. Independent Research Role

The narrative interpretations presented in the PPAC reports reflect official government and OMC perspectives:
- **LPG Demand Volatility:** The ICR July 2026 report attributes the 16.4% YoY decline in July 2026 LPG consumption to geopolitical disruptions and booking interval restrictions.
- **Transportation Fuel Expansion:** Motor Spirit (MS) growth (+9.2%) is attributed to passenger vehicle sales (+19.1% YoY) and post-GST personal mobility expansion.
- **Refining Resilience:** The Foundation Day report emphasizes India's status as a refining hub, processing crude not only for domestic consumption but also for export to global markets.

**Research Boundary:** In subsequent phases (Phase 3 through Phase 8), these published findings will serve as official contextual benchmarks against which our independent econometric and supply-chain calculations will be compared and evaluated.
