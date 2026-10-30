# Phase 5 Data Limitations: Technical Caveats and Boundary Definitions

**Project Title:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** 05 — Data Audit, Structural Limitations, and Harmonization Caveats  
**Status:** Completed and Audited  
**Date:** October 2026  
**Pipeline Reference:** [`src/phase5_product_analysis.py`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/src/phase5_product_analysis.py)  

---

## 1. Introduction

Academic rigor requires full transparency regarding data limitations, accounting boundary shifts, classification divergences, and institutional reporting conventions. The downstream petroleum sector in India is subject to complex fiscal, trade, and statistical reporting frameworks administered by multiple entities, including the Petroleum Planning & Analysis Cell (PPAC), the Ministry of Petroleum and Natural Gas (MoPNG), the Directorate General of Commercial Intelligence and Statistics (DGCIS), and individual public and private oil companies.

This document details the eight primary structural limitations and accounting caveats governing the Phase 5 product-level datasets.

---

## 2. Institutional and Accounting Boundary Caveats

### 2.1 The SEZ DTA Sales Structural Break (FY 2017–18)
* **The Policy Context:** Reliance Industries Limited operates two massive export-oriented refineries at Jamnagar, Gujarat: the DTA refinery ($33.0\text{ MMT/yr}$) and the SEZ refinery ($35.2\text{ MMT/yr}$). Historically, Special Economic Zones were legally treated as foreign territories under Indian customs law. Refined products produced in the SEZ refinery and sold into the domestic Indian market (Domestic Tariff Area, or DTA) were classified as imports under customs regulations, while sales dispatched directly from domestic refineries were classified as domestic consumption.
* **The Structural Break:** Effective **FY 2017–18**, PPAC revised its reporting methodology in Table 1 (`PT_Consumption_English`) to include SEZ sales into the DTA directly under domestic market consumption.
* **Analytical Impact:** National consumption figures from FY 2017–18 onwards include private SEZ DTA sales, whereas figures from FY 1997–98 to FY 2016–17 exclude them. This creates a one-time structural level shift (approximately $+12\text{ MMT}$ to $+15\text{ MMT}$) in the national consumption series. Researchers conducting econometric time-series analysis (e.g. ARIMA, structural break tests) must incorporate an intervention dummy variable ($D_t = 1$ for $t \ge 2017$) to avoid attributing institutional reclassification to real economic growth.

---

### 2.2 State-Level Dispatches vs National Consumption
* **The Structural Divergence:** The statewise sales dataset ([`statewise_sales_pol_consumption.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/statewise_sales_pol_consumption.csv)) reports dispatches for 38 States and Union Territories. When summing these state-level observations, the total is consistently **11% to 15% lower** than the reported `ALL INDIA TOTAL` and the national consumption figures in Table 1.
* **The Explanatory Footnote:** Row 57 of the original workbook `1787137273_Statewise_Sales-POL_Consumption_Final.xlsx` explicitly records:
  > `"*Total Fig. includes IMPORTS & SEZ STATE"`
* **Institutional Reality:**
  1. State rows reflect dispatches by public and private Oil Marketing Companies (OMCs: IOCL, BPCL, HPCL, Shell, Nayara) through retail fuel stations and state-registered consumer depots.
  2. The gap represents: (a) direct imports of refined products (especially Fuel Oil, Bitumen, and LPG) by private commercial entities outside the OMC marketing network; and (b) direct deliveries from SEZ refineries into industrial DTA hubs not attributed to state retail networks.
* **Methodological Mandate:** State-level data must be utilized strictly for analyzing **relative spatial distribution, regional concentration, and subnational growth differentials**. They must **never** be interpreted as exhaustive measures of total state-level hydrocarbon consumption.

---

### 2.3 Furnace Oil and LSHS Classification Asymmetry
* **The Classification Divergence:**
  * **Production (Table 15):** Reports `Furnace Oil (FO)` and `Low Sulphur Heavy Stock (LSHS)` in two separate historical time series.
  * **Trade (Table 21/22):** Combines both streams under a single customs category: `Fuel Oil`.
  * **Consumption (Table 1):** Combines both streams into an aggregate category: `FO & LSHS`.
* **Harmonization Solution:** To construct a viable 4-way mass balance without discarding historical fidelity, Phase 5 created an integrated canonical category: [`Furnace Oil & LSHS Combined`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_category_mapping.csv), defined as:
  $$\text{Production}_{\text{FO\&LSHS}} = \text{Production}_{\text{FO}} + \text{Production}_{\text{LSHS}}$$
  The individual production trajectories for FO and LSHS are preserved separately in [`product_production_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_production_dataset.csv) for granular industrial analysis.

---

### 2.4 Treatment of Petroleum Coke (Petcoke)
* **The Source Asymmetry:**
  * **Consumption:** Table 1 reports `Petroleum coke` as an independent product row across all 29 fiscal years (growing from $0.73\text{ MMT}$ in FY 1997–98 to $20.32\text{ MMT}$ in FY 2023–24).
  * **Production:** Table 15 does not contain an independent row for Petcoke. Instead, the official footnote explicitly clarifies:
    > `"* Others include products like Propylene, solvents (Hexane, Benzene, Toluene, Xylene and Specialty solvents), Reformate, Mineral Turpentine Oil, Carbon Black Feed Stock, Waxes, Sulphur and petcoke etc."`
  * **Trade:** Table 21/22 does not break out Petcoke imports, subsuming them under `Others`.
* **Analytical Impact:** Petcoke cannot be evaluated in an isolated 4-way mass balance. In the Apparent Availability Residual dataset ([`apparent_product_availability_residual.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/apparent_product_availability_residual.csv)), Petcoke consumption is combined with `Others` consumption to match the production basket definition.

---

### 2.5 Ethanol Blending Volume Distortion in Motor Spirit
* **The Mechanism:** Under the National Biofuel Policy and the Ethanol Blended Petrol (EBP) Programme, the Government of India mandated blending anhydrous fuel ethanol into motor gasoline (petrol). The national blending percentage increased from less than 1.5% in FY 2013–14 to **over 12.0% in FY 2023–24** (aiming for 20% by 2025–26).
* **Statistical Impact on Refinery Data:**
  * Refineries produce and report pure hydrocarbon petrol (E0 grade).
  * Ethanol is sourced from domestic sugar mills and grain distilleries and blended into petrol at **OMC marketing terminals and supply depots** before retail distribution.
  * Reported MS consumption in Table 1 represents total dispensed automotive petrol, which includes ethanol volumes (~$4.5\text{ MMT}$ in FY 2023–24).
* **The Apparent Residual Deficit:** Because domestic refinery production plus net trade represents pure hydrocarbon gasoline while reported consumption includes blended ethanol, the apparent availability residual for Motor Spirit becomes negative ($-4.89\text{ MMT}$ in FY 2023–24). This negative residual is not a data error; it reflects non-petroleum biofuel volume entering the retail supply chain post-refining.

---

### 2.6 Refinery Internal Fuel and Losses (RF&L)
* **The Physical Mechanism:** Crude oil refining is an energy-intensive chemical conversion process. To operate atmospheric distillation columns, vacuum distillation towers, fluid catalytic crackers (FCC), and hydrocrackers, refineries consume a significant portion of incoming crude internally as fuel gas, heavy fuel oil, and catalyst coke.
* **Magnitude:** In the Indian refining sector, Refinery Fuel & Loss (RF&L) typically accounts for **6.0% to 8.5% of total crude throughput**.
* **Impact on Apparent Availability:** In PPAC reporting:
  * Table 15 (Refinery Production) reports finished net marketable products.
  * Table 1 (Consumption) reports commercial sales in the domestic market.
  * Captive heavy residual fuel consumed inside refinery furnace boilers is partially recorded in refinery output but does not enter retail sales ledgers. This generates a structural positive residual in [`apparent_product_availability_residual.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/apparent_product_availability_residual.csv) for `Furnace Oil & LSHS Combined` ($+10.80\text{ MMT}$ in FY 2023–24) and `Total Petroleum Products` ($+27.91\text{ MMT}$).

---

### 2.7 Light Diesel Oil (LDO) Trade Flow Omission
* **The Omission:** In the trade volume workbook `1751964547_PT_IMPORT_TMT_H.xlsx`, LDO exports are tracked and recorded, whereas LDO imports are not reported as a distinct row.
* **Analytical Treatment:** In [`product_imports_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_imports_dataset.csv), LDO imports are omitted. In the trade balance calculation, LDO imports are treated as zero. This reflects the reality that India does not import significant commercial volumes of light diesel oil; any incidental imports are subsumed under general industrial gas oils or `Others`.

---

### 2.8 Provisional Status of Terminal Years
* **Reporting Periods:**
  * Datasets covering up to **FY 2023–24** represent fully audited, finalized official historical data.
  * Data for **FY 2024–25** are classified by PPAC as **Provisional (P)** and remain subject to minor historical reconciliation.
  * Data for **FY 2025–26** represent **provisional / partial period estimates** based on early fiscal projections.
* **Research Guideline:** All formal regression modeling, structural change detection, and econometric specifications must utilize **FY 2023–24** as the terminal audited year, treating FY 2024–25 and FY 2025–26 as out-of-sample provisional benchmarks.

---

## 3. Summary Risk and Compliance Matrix

| Limitation Dimension | Affected Products | Magnitude / Extent | Academic Treatment / Safeguard |
| :--- | :--- | :--- | :--- |
| **SEZ DTA Inclusion** | All Products Consumption | $+12$ to $+15\text{ MMT}$ post-2017 | Introduce intervention dummy in econometric models |
| **State vs National Gap** | State POL Sales | $11-15\%$ national gap | Limit state data to spatial distribution and regional shares |
| **FO / LSHS Aggregation** | Heavy Residual Fuels | Production FO/LSHS split | Created harmonized aggregate for 4-way cross-flow |
| **Petcoke in Others** | Petcoke / Others | $\sim 20\text{ MMT}$ consumption | Mapped into residual basket for physical mass balance |
| **Ethanol Blending** | Motor Spirit (MS) | $\sim 4.5\text{ MMT}$ volume | Documented as depot-level non-refinery volume addition |
| **Refinery Fuel & Loss** | FO & Total Products | $6-8\%$ of crude throughput | Documented as physical internal conversion consumption |
| **LDO Import Omission** | Light Diesel Oil | Negligible / Unrecorded | Documented as zero in trade balance tables |
| **Provisional Data** | FY 2024–25 / 2025–26 | Terminal observations | Benchmark econometric horizon at FY 2023–24 |
