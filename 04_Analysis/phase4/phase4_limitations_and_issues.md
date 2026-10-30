# Phase 4 Limitations, Data Discontinuities, and Methodological Issues

**Project:** India's Petroleum Supply Chain and Import Exposure  
**Deliverable:** Register of Analytical Limitations, Data Breaks, and Scope Boundaries  

---

## 1. Upstream Domestic Crude Production Truncation

- **Observation:** The primary upstream domestic production workbook (`1717395338_PT_Crude_oil_production_H.xls`) terminates at **FY 2023–24 (Provisional)** (29.36 MMT). Downstream refinery throughput, trade, and consumption series extend through **FY 2024–25**.
- **Analytical Impact:** Descriptive statistics, CAGRs, and trend tests that include domestic crude production or its derived ratios (`crude_import_dependence_proxy_pct`, `crude_production_to_refinery_processing_ratio_pct`, `refining_multiplier`) are strictly bounded to the 26-year horizon **FY 1998–99 to FY 2023–24**.
- **Limitation for Subsequent Phases:** Econometric supply-chain balance models cannot extend into FY 2024–25 without an updated upstream production release.

---

## 2. Statistical Non-Causality & Descriptive Boundaries

- **Boundary:** Phase 4 analysis establishes historical co-movements, growth rates, and non-parametric monotonic trends. It does **not** establish causal mechanisms.
- **Example:** The parallel expansion of crude oil imports and product exports reflects corporate refinery investment decisions (e.g. Reliance Jamnagar merchant export configuration), not an automatic physical feedback loop.
- **Analytical Rule:** Temporal coincidence (e.g. oil price collapse in 2014 and PMUY launch in 2016) must not be asserted as econometric causation without structural modeling.

---

## 3. Structural Reclassifications and Accounting Breaks

1. **SEZ to DTA Sales Inclusion in Consumption (FY 2017–18):**
   - Domestic consumption series incorporates private SEZ sales to Domestic Tariff Area from FY 2017–18 onwards per PPAC accounting footnote. While this improved coverage, it represents an accounting structural break.
2. **BORL Bina Corporate Amalgamation (2022):**
   - Bharat Oman Refineries Limited (Bina) was reported as a standalone Joint Venture from 2011 to 2021 before being legally amalgamated into `BPCL-BINA` under `BPCL-TOTAL`. Sectoral subtotal series reflect this shift.
3. **Absence of Crude Oil Export Data:**
   - Indian regulations restrict domestic crude from commercial export. PPAC trade returns publish no crude export line. Consequently, gross crude imports are identical to net crude imports.

---

## 4. Seasonal Discontinuities in Forward Periods

- **FY 2025–26 & FY 2026–27:** While available in raw extracts, FY 2025–26 product production (Apr–Sep partial) and FY 2026–27 refinery throughput (Till June partial) were strictly excluded from annual CAGR and YoY growth calculations to prevent seasonal distortion.
