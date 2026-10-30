# Phase 5 Methodology: Petroleum-Product Production, Trade, and Consumption Analysis

**Project Title:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** 05 — Product-Level Production, Trade, Consumption, and Spatial Sales Analysis  
**Status:** Completed and Audited  
**Date:** October 2026  
**Pipeline Script:** [`src/phase5_product_analysis.py`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/src/phase5_product_analysis.py)  

---

## 1. Executive Overview and Analytical Scope

Phase 5 transitions the research investigation from macroeconomic aggregate time-series (domestic crude production, total refinery throughput, aggregate crude imports) to a **micro-foundational, product-level examination** of the Indian downstream and midstream petroleum sectors. Refined petroleum is not a homogeneous commodity; the Indian downstream complex produces, imports, exports, and consumes a diverse spectrum of hydrocarbon fractions ranging from ultralight pressurized gases (LPG) to heavy vacuum residues (Bitumen) and solid petcoke.

The primary methodological objective of Phase 5 is to establish a rigorous, reproducible, and standardized empirical foundation for:
1. Identifying and mapping all refined petroleum products across official Ministry of Petroleum and Natural Gas (MoPNG) and Petroleum Planning & Analysis Cell (PPAC) data sources.
2. Constructing standardized, long-format datasets for product-level **Refinery Production**, **Imports**, **Exports**, **Domestic Consumption**, and **State-Level Sales**.
3. Establishing technical product trade balances to identify structural export-oriented refining outputs versus structural import-dependent deficits.
4. Evaluating physical mass balances via **Apparent Product Availability Residuals** while explicitly modeling accounting boundaries, unobserved stock changes, and refinery internal fuel consumption.
5. Analyzing the spatial and subnational distribution of petroleum consumption across 38 States and Union Territories.

---

## 2. Source Provenance and Input Datasets

Phase 5 utilizes five primary validated datasets established and audited during Phases 1, 2, and 3:

| Flow Domain | Source Workbook / File | Worksheet Name | Standardized File Name | Temporal Coverage | Native Unit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Refinery Production** | `1761642701_PT_production_product_H.xls` | `PT_production_product_H` | [`annual_petroleum_product_production_by_product.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/annual_petroleum_product_production_by_product.csv) | FY 1998–99 to 2025–26 (28 yrs) | TMT |
| **Product Imports** | `1751964547_PT_IMPORT_TMT_H.xlsx` | `IMPORT_TMT_H` | [`annual_petroleum_product_trade_by_product.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/annual_petroleum_product_trade_by_product.csv) | FY 1998–99 to 2024–25 (27 yrs) | TMT |
| **Product Exports** | `1751964547_PT_IMPORT_TMT_H.xlsx` | `IMPORT_TMT_H` | [`annual_petroleum_product_trade_by_product.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/annual_petroleum_product_trade_by_product.csv) | FY 1998–99 to 2024–25 (27 yrs) | TMT |
| **Product Consumption** | `1788343376_PT_Consumption_English.xls` | `PT_Consumption_English` | [`annual_petroleum_product_consumption_by_product.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/annual_petroleum_product_consumption_by_product.csv) | FY 1997–98 to 2025–26 (29 yrs) | TMT |
| **State-Level Sales** | `1787137273_Statewise_Sales-POL_Consumption_Final.xlsx` | `PT_Cons_Statewise`, `MS`, `HSD` | [`statewise_sales_pol_consumption.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/statewise_sales_pol_consumption.csv) | 2008–09 to 2025–26 (18 yrs) | TMT |

All data points adhere strictly to the Indian Financial Year convention (1 April to 31 March). Units are preserved in Thousand Metric Tonnes (TMT) and cross-converted to Million Metric Tonnes (MMT) via exact arithmetic ($1\text{ MMT} = 1,000\text{ TMT}$).

---

## 3. Product Harmonization & Canonical Taxonomy

A primary technical challenge in product-level petroleum analysis is the divergence of nomenclatures and aggregation boundaries across institutional tables. PPAC Table 15 (Production), Table 21/22 (Trade), Table 1 (Consumption), and the Statewise Sales matrix classify hydrocarbon streams differently.

To enable cross-flow arithmetic while preserving raw provenance, a canonical 12-product taxonomy was established in [`product_category_mapping.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_category_mapping.csv):

```
+----------------------------------------------------------------------------------------------------+
|                                 CANONICAL PRODUCT TAXONOMY                                         |
+------------------------------+---------------------------+-----------------------------------------+
| Distillate Cut / Group       | Standardized Product Name | Constituent Source Streams              |
+------------------------------+---------------------------+-----------------------------------------+
| 1. Light Distillates         | LPG                       | Liquefied Petroleum Gas                 |
|                              | Motor Spirit (Petrol / MS)| Finished Motor Gasoline (E0-E12)        |
|                              | Naphtha                   | Light / Heavy Virgin Naphtha            |
+------------------------------+---------------------------+-----------------------------------------+
| 2. Middle Distillates        | High Speed Diesel (HSD)   | Automotive Gasoil, Bulk Industrial HSD  |
|                              | Aviation Turbine Fuel(ATF)| Jet A-1 Aviation Kerosene               |
|                              | Superior Kerosene (SKO)   | PDS Subsidized & Non-PDS Kerosene       |
|                              | Light Diesel Oil (LDO)    | Stationary Low-Speed Diesel             |
+------------------------------+---------------------------+-----------------------------------------+
| 3. Heavy Ends & Residuals    | Furnace Oil (FO)          | Industrial & Marine Residual Fuel       |
|                              | Low Sulphur Heavy (LSHS)  | Fertilizer/Boiler Indigenous Residual   |
|                              | FO & LSHS Combined        | Combined Residual Fuel Stream           |
|                              | Bitumen                   | Paving Asphalt (VG-10, 30, 40)          |
|                              | Lubricants & Greases      | Lube Oil Base Stocks (LOBS) & Lubes     |
|                              | Petroleum Coke (Petcoke)  | Green & Calcined Solid Residue          |
+------------------------------+---------------------------+-----------------------------------------+
| 4. Specialties & Others      | Others                    | Solvents, Wax, MTO, CBFS, Propylene     |
+------------------------------+---------------------------+-----------------------------------------+
```

### Specific Reconciliation Decisions:
1. **Furnace Oil & LSHS Harmonization:** Production tables report `FO` and `LSHS` separately. Trade tables report a single composite `Fuel Oil` stream. Consumption tables report a composite `FO & LSHS` category. To permit trade balance and mass balance evaluations, production is aggregated ($\text{FO} + \text{LSHS}$) to form the canonical `Furnace Oil & LSHS Combined` stream, while preserving the individual production series in [`product_production_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_production_dataset.csv).
2. **Petroleum Coke (Petcoke) Allocation:** In consumption sources, Petcoke is explicitly disaggregated for 29 years. In production sources, Petcoke is not listed as an independent row; the official table footnote explicitly states: `"* Others include products like Propylene, solvents..., petcoke etc."` In trade, petcoke is subsumed under `Others`. Therefore, for apparent availability residual calculations, Petcoke consumption is combined with `Others` consumption to match the production basket definition.
3. **Light Diesel Oil (LDO) Trade Flows:** LDO exports are tracked officially in customs data, whereas LDO imports are not broken out (either zero or negligible). LDO imports are treated as zero in trade balance tables, with explicit caveats documented.

---

## 4. Mathematical and Analytical Formulations

### 4.1 Product Trade Balance
For any product $p$ in fiscal year $t$, the net trade balance is defined strictly as:

$$\text{Trade Balance}_{p,t} = \text{Exports}_{p,t} - \text{Imports}_{p,t}$$

* **Sign Convention:**
  * $\text{Trade Balance}_{p,t} > 0$: Net Exporter (domestic production exceeds domestic demand plus stock build, generating an exportable surplus).
  * $\text{Trade Balance}_{p,t} < 0$: Net Importer (domestic refining yields fall short of domestic consumption, necessitating physical foreign imports).

### 4.2 Apparent Product Availability Residual
To evaluate physical supply-chain equilibrium and verify data integrity across the four flows, an apparent product availability residual is computed:

$$\text{Apparent Gross Availability}_{p,t} = \text{Production}_{p,t} + \text{Imports}_{p,t} - \text{Exports}_{p,t}$$

$$\text{Apparent Availability Residual}_{p,t} = \text{Apparent Gross Availability}_{p,t} - \text{Reported Consumption}_{p,t}$$

$$\text{Residual \% of Consumption}_{p,t} = \left( \frac{\text{Residual}_{p,t}}{\text{Reported Consumption}_{p,t}} \right) \times 100$$

$$\text{Residual \% of Gross Supply}_{p,t} = \left( \frac{\text{Residual}_{p,t}}{\text{Production}_{p,t} + \text{Imports}_{p,t}} \right) \times 100$$

#### Methodological Interpretation of Residuals:
In physical petroleum economics, a non-zero residual does **not** signify an accounting error. Rather, it represents structural physical and institutional phenomena:
* **Refinery Internal Fuel and Losses (RF&L):** Modern conversion refineries consume between 6.0% and 8.5% of crude throughput internally as fuel gas, heavy fuel oil, and catalyst coke to generate process heat and steam. This fuel is recorded under refinery crude processing but does not enter commercial consumption sales.
* **Secondary and Tertiary Stock Variations:** The delta between refinery gate dispatch and retail dispensing is buffered by storage tanks at refineries, cross-country pipeline line-fill, railway transit batches, and OMC marketing terminals.
* **Ethanol Blending Discrepancy:** In motor gasoline (MS), anhydrous ethanol is blended into petrol at marketing depots (not at refinery gates). Consequently, consumer dispensing volumes exceed pure hydrocarbon refinery production.
* **Non-Energy Feedstock Use:** Naphtha and FO diverted into petrochemical complexes (e.g. steam crackers) and fertilizer plants under captive pipeline transfer may experience reporting lags relative to trade data.

### 4.3 Growth Formulations
1. **Year-over-Year (YoY) Change:**
   $$\Delta V_t = V_t - V_{t-1}, \quad \text{YoY \%} = \left( \frac{V_t - V_{t-1}}{V_{t-1}} \right) \times 100$$
2. **Compound Annual Growth Rate (CAGR):**
   $$\text{CAGR}_{t_0, t_n} = \left[ \left( \frac{V_{t_n}}{V_{t_0}} \right)^{\frac{1}{n}} - 1 \right] \times 100$$
   CAGRs are computed only across economically coherent, policy-driven structural subperiods:
   * **Subperiod 1 (FY 1998–99 to 2002–03):** Pre-NELP / Early Reform Era.
   * **Subperiod 2 (FY 2002–03 to 2008–09):** Private Refinery Commissioning (Jamnagar Phase 1).
   * **Subperiod 3 (FY 2008–09 to 2014–15):** Post-GFC & SEZ Export Expansion (Jamnagar Phase 2, Vadinar).
   * **Subperiod 4 (FY 2014–15 to 2019–20):** Pradhan Mantri Ujjwala Yojana (PMUY) & Pre-COVID Automotive Surge.
   * **Subperiod 5 (FY 2019–20 to 2023–24):** COVID-19 Demand Contraction & Post-Pandemic Rebound.
   * **Full Harmonized Horizon (FY 1998–99 to 2023–24):** 25-year structural long-term growth.

---

## 5. State-Level Sales vs National Consumption Accounting

A critical audit requirement in Phase 5 is reconciling the state-wise petroleum sales workbook (`1787137273_Statewise_Sales-POL_Consumption_Final.xlsx`) against national consumption totals (`1788343376_PT_Consumption_English.xls`).

### The Institutional Finding:
Inspection of the statewise workbook reveals three separate worksheets:
1. `PT_Cons_Statewise` (All Products)
2. `PT_Cons_Statewise MS` (Motor Spirit)
3. `PT_Cons_Statewise HSD` (High Speed Diesel)

Each worksheet lists 38 States and Union Territories, aggregated into five geographic regions (`REGION - NORTH`, `REGION - NORTH EAST`, `REGION - EAST`, `REGION - WEST`, `REGION - SOUTH`), followed by a row labeled `ALL INDIA TOTAL`.

When summing the sales of individual states, a structural gap of 11% to 15% emerges relative to `ALL INDIA TOTAL`. For instance, in FY 2023–24:
* **Sum of 38 Individual States:** 207,494.0 TMT
* **Reported `ALL INDIA TOTAL`:** 234,258.7 TMT
* **Discrepancy:** +26,764.7 TMT (+12.9%)

Crucially, **the reported `ALL INDIA TOTAL` in the statewise workbook matches national total consumption in `annual_petroleum_product_consumption.csv` with 0.00% error** ($234,258.7\text{ TMT} = 234,258.7\text{ TMT}$).

The explanation for this divergence is found in **Row 57 of the original Excel workbook**:
> `"*Total Fig. includes IMPORTS & SEZ STATE"`

#### Structural Decomposition:
* **State Rows:** Represent dispatches by public and private oil marketing companies (OMCs) to retail fuel outlets and state-registered consumer depots.
* **`ALL INDIA TOTAL`:** Incorporates direct petroleum product imports by private commercial consumers (e.g. independent power producers, industrial plants) and sales by Special Economic Zone (SEZ) export refineries into the Domestic Tariff Area (DTA), which are not allocated to specific state jurisdictions in OMC dispatch ledgers.
* **Methodological Rule:** State sales data must be used strictly for spatial, geographic, and regional share comparisons; they must not be conflated with total national demand.

---

## 6. Visualization & Reporting Architecture

All Phase 5 figures were engineered to meet rigorous publication standards:
* **Dual Format Rendering:** Every figure is generated as a 300 DPI high-resolution PNG (`04_Analysis/phase5/figures/*.png`) and an editable vector SVG (`04_Analysis/phase5/figures/*.svg`).
* **Underlying Data Isolation:** The numerical arrays used to plot each chart are extracted and dual-saved as standalone CSV files in `04_Analysis/phase5/figure_data/`.
* **Standard Visual Formatting:** Fixed color palettes, explicit axis units (MMT or %), transparent grid lines, and comprehensive multi-line source and analytical footnotes.

```
Figure 1: Major Product Production Trajectories (FY 1998-99 to 2024-25)
Figure 2: Major Product Consumption Trajectories (FY 1997-98 to 2024-25)
Figure 3: Product Trade Balance Dynamics: Refining Dualism (FY 1998-99 to 2024-25)
Figure 4: The Great PMUY Structural Shift: LPG Expansion vs Kerosene Phasing-out
Figure 5: Automotive Fuel Dynamics: Diesel (HSD) vs Gasoline (MS) Shifts
Figure 6: Cross-Flow Supply Balance & Apparent Availability Residuals
Figure 7: Product Composition of Consumption (% Shares over 27 Years)
Figure 8: Spatial Distribution of POL Consumption (Top States & Regional Breakdown)
```

---

## 7. Deliverables & File Registry

```
Final-Project/
├── 03_Processed_Data/
│   └── standardized/
│       ├── product_production_dataset.csv & .parquet
│       ├── product_imports_dataset.csv & .parquet
│       ├── product_exports_dataset.csv & .parquet
│       ├── product_consumption_dataset.csv & .parquet
│       ├── statewise_sales_consumption_dataset.csv & .parquet
│       ├── product_category_mapping.csv
│       ├── product_data_coverage.csv
│       ├── product_level_provenance.csv
│       ├── product_trade_balance.csv & .parquet
│       └── apparent_product_availability_residual.csv & .parquet
└── 04_Analysis/
    └── phase5/
        ├── phase5_methodology.md
        ├── phase5_results_report.md
        ├── phase5_data_limitations.md
        ├── phase5_completion_checklist.md
        ├── product_descriptive_statistics.csv
        ├── product_growth_summary.csv
        ├── phase5_product_analysis.py
        ├── figures/ (Figures 1 to 8 in .png and .svg)
        └── figure_data/ (Figures 1 to 8 data tables in .csv)
```
