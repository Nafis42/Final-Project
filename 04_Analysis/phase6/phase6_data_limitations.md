# Phase 6 Data Limitations: Technical Caveats, Valuation Bases, and Analytical Boundaries

**Project Title:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** 06 — Financial Data Audit, Valuation Bases, and Accounting Limitations  
**Status:** Completed and Audited  
**Date:** October 2026  
**Pipeline Reference:** [`src/phase6_import_analysis.py`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/src/phase6_import_analysis.py)  

---

## 1. Introduction

Academic analysis of petroleum import expenditure requires rigorous awareness of data boundaries, valuation conventions, accounting classifications, and institutional reporting practices. The financial outlays recorded in Ministry of Petroleum and Natural Gas (MoPNG) and Petroleum Planning & Analysis Cell (PPAC) matrices reflect customs declarations compiled under Directorate General of Commercial Intelligence and Statistics (DGCIS) guidelines.

This document details the eight primary structural limitations and methodological caveats governing the Phase 6 financial and price datasets.

---

## 2. Institutional and Accounting Boundary Caveats

### 2.1 Valuation Basis Asymmetry: CIF Customs Clearance vs FOB Benchmark Pricing
* **The Asymmetry:**
  * **Import Values (Tables 21 & 22):** Reported on a **Cost, Insurance, and Freight (CIF)** basis at Indian discharge ports. This valuation includes the invoice price of crude oil, maritime tanker charter freight, demurrage, canal transit fees, and marine cargo insurance.
  * **Indian Basket Benchmark Price:** Quoted strictly on a **Free on Board (FOB)** basis at primary loading ports (e.g. Ras Tanura, Mina Al Ahmadi, Sullom Voe).
* **Analytical Impact:** Calculated import unit values (USD/bbl) will naturally exceed FOB benchmark prices during periods of elevated global tanker freight rates (e.g. Very Large Crude Carrier [VLCC] rate spikes in 2007–08 and 2022–23). The differential between calculated unit values and benchmark prices cannot be interpreted purely as refinery procurement inefficiency; it reflects the real physical logistics cost of maritime transport.

---

### 2.2 Product Composition Aggregation Bias (Mix Effect)
* **The Aggregation Bias:**
  When computing unit values for composite categories such as `Total Petroleum Products` or `Others`, the calculated unit value ($P = V / Q$) is a weighted harmonic average of its constituent products:
  $$P_{\text{agg}} = \sum_i w_i P_i, \quad w_i = \frac{Q_i}{\sum_k Q_k}$$
* **Impact over Time:** Between FY 1998–99 and FY 2024–25, the composition of India's product import basket underwent a radical inversion:
  * Low-to-medium unit-value products (HSD and SKO) declined from 71.0% of the volume to 0.1%.
  * High-unit-value pressurized gases (LPG) expanded from 7.2% to 40.6% of physical product import volume.
* **Analytical Rule:** A rise in the aggregate product import unit value does **not** indicate that individual product prices increased by that proportion. Econometricians must analyze homogeneous product lines (e.g. pure LPG, pure HSD) rather than aggregate product unit values when estimating price elasticity.

---

### 2.3 The Currency Valuation Divergence: Dollar vs Rupee Accounting
* **The Mechanism:** India operates under a managed floating exchange rate regime. The Indian Rupee depreciated from an average of ₹42.07 per US Dollar in FY 1998–99 to ₹83.45 per US Dollar in FY 2024–25, representing a cumulative currency weakening of **+98.4%**.
* **Analytical Consequence:**
  * In US Dollar terms, India's crude import bill expanded by **+3,799%** (39.0-fold).
  * In Indian Rupee terms, the same physical oil flow caused the import bill to expand by **+7,681%** (77.8-fold).
* **Research Guideline:** Macroeconomic balance-of-payments studies must evaluate outlays in US Dollars (the currency of international settlement), whereas domestic fiscal studies (budget subsidies, under-recoveries, fuel excise taxes, inflation pass-through) must evaluate outlays in Indian Rupees. Converting between the two using an annual average exchange rate captures average trends but masks intra-year currency volatility.

---

### 2.4 Russian Crude Invoicing and Sanctions Wedges (FY 2022–24)
* **The Structural Event:** Following the escalation of the Russia-Ukraine conflict in 2022 and the imposition of G7/EU maritime price caps, Indian refiners shifted a substantial portion of their crude feedstock from traditional Middle Eastern suppliers to discounted Russian grades (Urals, Sokol, ESPO). Russian crude imports rose from <2% of throughput in 2021 to over 35% in 2023–24.
* **Accounting Complexities:**
  1. **Discounts vs Benchmarks:** Official PPAC Indian Basket prices maintain a fixed theoretical weighting (historical sour/sweet ratio of Oman/Dubai and Brent). Because Indian Basket formulas did not incorporate Russian Urals spot prices, benchmark prices diverged from actual customs invoiced values.
  2. **Non-Dollar Invoicing:** A portion of bilateral petroleum trade was settled in non-dollar currencies (UAE Dirhams, Russian Rubles, Indian Rupees). Customs authorities convert non-dollar invoices into US Dollars and Rupees using statutory customs exchange rates on the date of bill of entry clearance, introducing minor currency translation wedges.

---

### 2.5 Strategic Petroleum Reserve (SPR) Inclusions and Exclusions
* **The Institutional Facility:** Indian Strategic Petroleum Reserves Limited (ISPRL) maintains underground rock caverns at Visakhapatnam ($1.33\text{ MMT}$), Mangalore ($1.50\text{ MMT}$), and Padur ($2.50\text{ MMT}$) totaling $5.33\text{ MMT}$ of strategic crude storage.
* **Reporting Boundary:** In historical PPAC matrices (Table 21/22), commercial refinery crude imports are compiled from oil company returns. Footnotes in Table 21 explicitly note: `"Crude import excludes procurement for Strategic Petroleum Reserve (Mangalore cavern) during FY 2016-17."`
* **Analytical Impact:** Strategic storage injections are financed under capital outlays and do not directly enter commercial refinery crude throughput in the year of injection. Researchers cross-referencing refinery crude throughput with crude imports must account for SPR inventory movements.

---

### 2.6 Partial-Year Data vs Annual Complete Series (FY 2025–26)
* **The Source Files:** Workbook `1784609810_PT_IMPORT_VAL_US$_25-26.xlsx` contains monthly import values for April through November/December of FY 2025–26.
* **Methodological Mandate:** Partial-year data must **never** be merged directly into annual time series without explicit labeling. In Phase 6, all long-term trend models, CAGRs, and symmetric decompositions terminate at **FY 2024–25 (P)** to preserve full twelve-month annual comparability.

---

### 2.7 Incidental and Unrecorded Import Streams
* **Light Diesel Oil (LDO):** LDO is an industrial fuel used in stationary low-speed engines. While PPAC Table 21 tracks LDO exports, LDO imports are not broken out as an independent row. Incidental commercial imports are subsumed under `Others`.
* **Private Direct Imports:** While national totals capture direct imports by private parties through customs bills of entry, granular product breakdowns for specialized petrochemical solvents are occasionally aggregated under `Others&`.

---

## 3. Summary Risk and Compliance Matrix

| Limitation Dimension | Affected Variables | Magnitude / Extent | Analytical Treatment / Safeguard |
| :--- | :--- | :--- | :--- |
| **CIF vs FOB Wedge** | Crude Unit Values | \$2.00 to \$4.50 / bbl | Explicitly document as maritime freight and insurance margin |
| **Product Mix Bias** | Total Product Unit Value | Distorts price index | Limit decomposition and price elasticity to homogeneous products |
| **Currency Compounding** | Rupee Import Outlays | +98.4% nominal inflation | Evaluate USD for balance of payments; INR for domestic fiscal impact |
| **Russian Urals Discounts**| Post-2022 Unit Values | \$5.00 to \$12.00 / bbl discount | Disclose benchmark divergence in 2022–24 observations |
| **SPR Storage Buffer** | Crude Import Quantities | $\sim 1.5$ to $2.5\text{ MMT}$ injections | Flag SPR footnote exclusions in FY 2016–17 |
| **Partial-Year Data** | FY 2025–26 Monthly | 8-month incomplete period | Exclude from annual CAGR and decomposition horizons |
| **Provisional Status** | FY 2024–25 Data | Terminal fiscal observations | Label as Provisional (P); benchmark audited models at 2023–24 |
