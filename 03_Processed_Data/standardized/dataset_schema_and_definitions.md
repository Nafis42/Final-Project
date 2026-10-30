# Dataset Schema, Variable Definitions, and Accounting Identities

**Project:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** Phase 3 — Core Petroleum Supply-Chain Dataset  
**Standard Authority:** Petroleum Planning & Analysis Cell (PPAC), Ministry of Petroleum and Natural Gas (MoPNG), Government of India  
**Temporal Foundation:** Indian Financial Year (1 April to 31 March)  

---

## 1. Overview of Phase 3 Dataset Portfolio

Phase 3 delivers four integrated datasets in both Comma-Separated Values (`.csv`) and columnar Apache Parquet (`.parquet`):

1. **`core_annual_petroleum_dataset`** (30 periods, 36 columns):  
   The primary macroeconomic supply-chain table integrating upstream domestic crude production, crude imports/exports, refinery throughput, product production, product imports/exports, consumption, crude prices, and import values.
2. **`petroleum_product_level_dataset`** (372 records, 17 columns):  
   Harmonized long-panel table capturing product-specific production, imports, exports, net exports, and consumption across 12 standardized product lines.
3. **`petroleum_supporting_variables`** (27 periods, 19 columns):  
   Trade value accounts in USD and INR, implied transaction exchange rates, crude basket sour:sweet composition weights, and central/state exchequer contributions.
4. **`derived_indicators`** (30 periods, 18 columns):  
   Rigorously constructed economic ratios and proxies (Net crude imports, import-dependence proxy, production-to-processing ratio, import unit values, refining multiplier, product self-sufficiency ratio).

---

## 2. Mathematical Accounting Identities & Formulas

All physical quantities in the core dataset are tracked in parallel units:
- **Thousand Metric Tonnes (TMT)** — native reporting precision of PPAC downstream tables.
- **Million Metric Tonnes (MMT)** — standardized macroeconomic presentation unit ($1\text{ MMT} = 1,000\text{ TMT}$).

### A. Upstream Domestic Crude Production
$$\text{Total Crude Production} = \text{ONGC} + \text{OIL} + \text{PSC/Pvt/JV}$$
$$\text{Total Crude Production} = \text{Onshore Production} + \text{Offshore Production}$$

### B. Refinery Crude Processing
$$\text{Grand Total Throughput} = \sum \text{Corporate Groups} + \sum \text{Standalone Refineries}$$
*Corporate groups:* IOCL, BPCL (including Bina post-2022), HPCL, CPCL, ONGC (Tatipaka), RIL (Jamnagar DTA & SEZ).  
*Standalone units:* NRL (Numaligarh), HMEL (Bathinda), Nayara Energy (Vadinar), BORL (Bina, standalone 2011–2022).

### C. Downstream Petroleum Product Production
$$\text{Total Product Production} = \sum_{i=1}^{12} \text{Product}_i$$
*Categories:* LPG, Motor Spirit (Petrol), High Speed Diesel, Aviation Turbine Fuel, Superior Kerosene Oil, Naphtha, Furnace Oil, Low Sulphur Heavy Stock, Bitumen, Lubricants & Greases, Light Diesel Oil, Others.

### D. Petroleum Trade Physical Balance
$$\text{Net Petroleum Imports} = (\text{Crude Imports} + \text{Product Imports}) - \text{Product Exports}$$
*Crude Export Convention:* Officially unrecorded / restricted by statutory policy; domestic crude is allocated directly to Indian refineries. Recorded as NaN in raw source observations; evaluated as 0.0 in net physical balances.

### E. Derived Supply-Chain Indicators (Section 7 Formulas)
1. **Net Crude Imports:**
   $$\text{Net Crude Imports} = \text{Crude Imports} - \text{Crude Exports}$$
2. **Import-Dependence Proxy (%):**
   $$\text{Crude Import-Dependence Proxy (\%)} = \frac{\text{Net Crude Imports}}{\text{Domestic Crude Production} + \text{Net Crude Imports}} \times 100$$
   *Caveat:* Constructed proxy based on physical crude supply balance; not an official MoPNG import-dependence statistic.
3. **Production-to-Processing Ratio (%):**
   $$\text{Production-to-Processing Ratio (\%)} = \frac{\text{Domestic Crude Production}}{\text{Refinery Crude Processing}} \times 100$$
   *Caveat:* Measures indigenous crude self-sufficiency relative to refinery throughput. Does NOT represent refinery capacity utilization.
4. **Crude Import Unit Value (USD/MT and USD/bbl):**
   $$\text{Import Unit Value (USD/MT)} = \frac{\text{Crude Import Value (Million USD)} \times 10^6}{\text{Crude Import Quantity (TMT)} \times 1000}$$
   $$\text{Import Unit Value (USD/bbl)} = \frac{\text{Import Unit Value (USD/MT)}}{7.33}$$
5. **Implied Transaction Exchange Rate (INR/USD):**
   $$\text{Implied Exchange Rate} = \frac{\text{Petroleum Import Value (INR Crore)} \times 10^7}{\text{Petroleum Import Value (Million USD)} \times 10^6} = \frac{\text{INR Crore} \times 10}{\text{USD Million}}$$

---

## 3. Missing Value Conventions & Handling

- **Explicit Missingness:** No missing value has been silently replaced with zero, interpolated, or backfilled. All unobserved cells contain explicit `NaN` (or `null` in Parquet).
- **Upstream Truncation:** Domestic crude production ends at FY 2023–24 (P) in `PT_Crude_oil_production_H.xls`. For FY 2024–25 onwards, it is explicitly `NaN`, and its derived ratios are `NaN`.
- **Crude Basket Price Series:** FOB price series begins in FY 2000–01. Periods prior to FY 2000–01 are explicitly `NaN`.
- **Crude Exports:** PPAC publishes no crude oil export line. In the core observation table, `crude_export_quantity` is recorded as `NaN` with explicit explanatory notes.
- **SEZ to DTA Sales Shift:** A boolean flag `sez_dta_sales_included` is included in all consumption tables (`False` prior to FY 2017–18; `True` from FY 2017–18 onwards) to document the official PPAC reporting shift.
