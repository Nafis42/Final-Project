# Phase 2 Unresolved Issues, Anomalies, and Decisions for Phase 3

**Project:** India's Petroleum Supply Chain and Import Exposure  
**Deliverable:** Register of Anomalies, Inconsistencies, and Methodological Decisions  
**Status:** Open for User Review Prior to Phase 3 Execution  

---

## 1. Upstream Domestic Crude Production Series Truncation

- **Observation:** In the official PPAC workbook `1717395338_PT_Crude_oil_production_H.xls`, domestic crude oil production terminates at **FY 2023–24 (Provisional)** (totaling 29.397 MMT). Downstream refinery crude throughput (`PT_crude_processing_H.xls`) and petroleum trade flows (`PT_IMPORT_TMT_H.xlsx`) extend through **FY 2024–25**.
- **Root Cause:** The upstream historical workbook in `01_Original_Data` was compiled prior to the release of the final FY 2024–25 upstream figures.
- **Recommended Action for Phase 3:** Establish the **Core Historical Modeling Baseline** as the 26-year period **FY 1998–99 to FY 2023–24**, where all supply-chain tiers (upstream production, refinery processing, product production, trade, consumption, import values, and crude basket prices) possess complete, synchronized, and unbroken coverage. FY 2024–25 can be evaluated as an extended downstream analysis window.

---

## 2. Accounting Convention for Crude Oil Exports

- **Observation:** In `1751964547_PT_IMPORT_TMT_H.xlsx`, the trade quantity tables record detailed monthly and annual rows for Crude Oil Imports, Product Imports, and Product Exports, but contain **no row for Crude Oil Exports**.
- **Regulatory Reality:** Indian statutory policy (under the Foreign Trade Policy and MoPNG allocation mechanisms) restricts the export of domestically produced crude oil; virtually 100% of indigenous crude is allocated directly to domestic refineries. Minor offshore condensate or test cargoes that may occur are not tracked in PPAC commercial trade returns.
- **Adopted Standardization:** Crude oil exports are formally recorded as `0.0 TMT` in `annual_petroleum_trade_volumes.csv`, resulting in $\text{Net Crude Imports} = \text{Gross Crude Imports}$. This convention is fully documented in the data dictionary.

---

## 3. Structural Transition: BORL (Bina Refinery) Amalgamation into BPCL

- **Observation:** In `1788266304_PT_crude_processing_H.xls`, Bharat Oman Refineries Limited (BORL, Bina) appears as an independent standalone Joint Venture refinery from FY 2011–12 through FY 2021–22. From FY 2022–23 onwards, the standalone row ceases and is reported as `BPCL-BINA` under the `BPCL-TOTAL` corporate subtotal.
- **Impact on Long Panels:** Analysts building firm-level panel regressions must account for this corporate restructuring to prevent artificial spikes in BPCL throughput and an artificial vanishing of BORL.
- **Adopted Standardization:** Both corporate totals and detailed unit rows are preserved in `annual_refinery_crude_processing.csv` and `annual_refinery_crude_processing_detailed.csv`, with explanatory notes in the data dictionary.

---

## 4. Provisional Rounding Discrepancy in FY 2025–26 H1 Product Production

- **Observation:** In `1761642701_PT_production_product_H.xls`, for the partial fiscal period FY 2025–26 (Apr–Sep), the printed total is `139,648.589 TMT`, whereas the sum of the 12 constituent product rows is `139,647.589 TMT`—an exact difference of `1.000 TMT` (0.000716%).
- **Verification:** Exhaustive line auditing confirmed that the printed component rows sum to 139,647.589 TMT. This discrepancy is an internal rounding artifact in the provisional publication's residual "Others" line.
- **Adopted Standardization:** The raw reported total and individual component rows are preserved verbatim. In validation checks, this is documented and flagged.

---

## 5. SEZ to Domestic Tariff Area (DTA) Sales in Consumption Series

- **Observation:** In `1788343376_PT_Consumption_English.xls`, footnote 1 explicitly notes that from FY 2017–18 onwards, domestic consumption figures include private SEZ refinery sales to the Domestic Tariff Area (DTA). Prior to FY 2017–18, SEZ DTA sales were accounted for under separate customs reporting.
- **Adopted Standardization:** A boolean indicator `sez_dta_sales_included` is incorporated into `annual_petroleum_product_consumption.csv` (set to `False` for FY 1997–98 to 2016–17, and `True` from FY 2017–18 onwards) to alert downstream econometricians to this structural accounting break.

---

## 6. Format Defect in OMC Under-Recoveries File

- **Observation:** `1785841030_Under_Recoveries_to_Oil_Marketing_Companies_(OMCs)_on_Sale_of_Sensitive_Petroleum_Products_Rs_Crore.xls` has an `.xls` extension but contains an OOXML (PK zip) file structure.
- **Resolution:** Successfully extracted into `raw_omc_under_recoveries_sensitive_products.csv` using an in-memory byte buffer without altering the original file on disk. This dataset provides secondary fiscal context and is not part of the physical supply-chain core.

---

## 7. Recommended Time Windows for Phase 3 Modeling

Based on the validated data availability, the following analysis horizons are recommended for Phase 3:
1. **Primary Core Macro Supply Chain Balance:** **FY 1998–99 to FY 2023–24 (26 Financial Years)** — Unbroken, fully synchronized across upstream crude production, refinery throughput, product yields, trade flows, product consumption, import expenditure, and exchange rates.
2. **Downstream Refining & Trade Extended Window:** **FY 1998–99 to FY 2024–25 (27 Financial Years)** — Downstream processing, trade, and consumption balance.
3. **High-Frequency Monthly Micro-Panel:** **April 2011 to March 2025 (168 Months / 14 Years)** — Monthly refinery throughput and trade volumes for seasonal and shock analysis.
4. **Sub-national Regional Panel:** **FY 2008–09 to FY 2024–25 (17 Financial Years)** — State-level consumption dynamics.
