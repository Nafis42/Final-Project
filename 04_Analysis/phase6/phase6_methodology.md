# Phase 6 Methodology: Petroleum Import Expenditure, Import Unit Values, and Price Effects

**Project Title:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** 06 — Financial Import Expenditure, Unit Values, and Symmetric Decomposition Analysis  
**Status:** Completed and Audited  
**Date:** October 2026  
**Pipeline Reference:** [`src/phase6_import_analysis.py`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/src/phase6_import_analysis.py)  

---

## 1. Research Objectives and Scope

Phase 6 examines the macroeconomic and financial dimensions of India's petroleum supply chain. While Phases 4 and 5 investigated physical throughput (metric tonnes of domestic crude extraction, refinery processing, product yields, and physical consumption), Phase 6 analyzes:
1. The **financial magnitude** of India's petroleum import outlays in both US Dollars (USD) and Indian Rupees (INR) across 27 fiscal years (FY 1998–99 to FY 2024–25).
2. The empirical calculation of **import unit values** ($P = V / Q$) across crude oil and ten refined product streams.
3. The relationship between calculated crude oil import unit values and the official **Indian Basket Crude Oil benchmark price**.
4. The structural **two-factor symmetric decomposition** of import expenditure changes into physical quantity effects versus international price effects.
5. The **currency depreciation multiplier**, quantifying how the secular weakening of the Indian Rupee against the US Dollar compounded nominal domestic import costs.

---

## 2. Source Provenance and Alignment Architecture

The empirical analysis integrates three primary institutional source matrices published by the Petroleum Planning & Analysis Cell (PPAC) and Ministry of Petroleum and Natural Gas (MoPNG):

| Measurement Dimension | Primary Source Workbook | Worksheet Name | Standardized File | Reporting Range | Native Units |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Physical Import Volume ($Q$)** | `1751964547_PT_IMPORT_TMT_H.xlsx` | `PT_IMPORT_H` | [`import_quantity_value_aligned_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/import_quantity_value_aligned_dataset.csv) | FY 1998–99 to 2024–25 | Thousand Metric Tonnes (TMT) |
| **Import Value in USD ($V_{\text{USD}}$)** | `1751964622_PT_IMPORT_VAL_US$_H.xlsx` | `PT_IMPORT_VAL$_H` | [`import_value_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/import_value_dataset.csv) | FY 1998–99 to 2024–25 | Million US$ |
| **Import Value in INR ($V_{\text{INR}}$)** | `1751964598_PT_IMPORT_VAL_RS.CRS._H.xlsx` | `PT_IMPORT_VALRS_H` | [`import_value_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/import_value_dataset.csv) | FY 1998–99 to 2024–25 | Crore Rupees (₹ Crore) |
| **Benchmark Crude FOB Price** | `1775133106_PP_Crude-Oil-FOB-Price-(Indian Basket)-Historical.xlsx` | `Sheet1` | [`indian_basket_price_series.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/indian_basket_price_series.csv) | FY 2000–01 to 2025–26 | USD per Barrel ($/bbl) |

### 1-to-1 Matrix Alignment:
Inspection of the underlying source workbooks reveals identical structural templates across all three matrices (Table 21/22 series). Each matrix shares exact row coordinates:
* **Row 10:** Crude Oil
* **Row 12:** Liquefied Petroleum Gas (LPG)
* **Row 13:** Motor Spirit (Petrol / MS)
* **Row 14:** Naphtha
* **Row 15:** Aviation Turbine Fuel (ATF)
* **Row 16:** Superior Kerosene Oil (SKO)
* **Row 17:** High Speed Diesel (HSD)
* **Row 18:** Lubricants & Greases (LOBS / Lube Oil)
* **Row 19:** Furnace Oil & LSHS (Fuel Oil)
* **Row 20:** Bitumen
* **Row 21:** Others
* **Row 22:** Total Petroleum Products (`PRODUCT IMPORT*`)
* **Row 24:** Total Petroleum Imports (`TOTAL IMPORTS`)

This row parity ensures zero risk of misaligned commodity mapping across quantities, dollar expenditures, and rupee expenditures.

---

## 3. Mathematical Formulations and Derivations

### 3.1 Calculated Import Unit Values
Import unit values are calculated as the ratio of financial expenditure to physical volume cleared through customs:

$$\text{Unit Value (USD/MT)} = \frac{V_{\text{USD}} \times 10^6}{Q_{\text{TMT}} \times 10^3} = \frac{V_{\text{USD}}}{Q_{\text{TMT}}} \times 1000$$

$$\text{Unit Value (INR/MT)} = \frac{V_{\text{INR}} \times 10^7}{Q_{\text{TMT}} \times 10^3} = \frac{V_{\text{INR}}}{Q_{\text{TMT}}} \times 10,000$$

Where:
* $V_{\text{USD}}$ is import expenditure in Million US\$.
* $V_{\text{INR}}$ is import expenditure in Rs. Crore ($1\text{ Crore} = 10^7$).
* $Q_{\text{TMT}}$ is import volume in Thousand Metric Tonnes ($1\text{ TMT} = 10^3\text{ MT}$).

#### Crude Oil Conversion to Barrels ($/bbl):
To compare calculated crude import costs with international benchmark prices quoted in USD per barrel, crude oil metric tonnes are converted using the official PPAC standard conversion factor ($1\text{ MT} = 7.33\text{ barrels}$):

$$\text{Crude Unit Value (USD/bbl)} = \frac{\text{Unit Value (USD/MT)}}{7.33}$$

#### Implied Conversion Factor and Price Differential:
To evaluate how actual import baskets deviate from the benchmark, the implied physical density ratio is derived:

$$\text{Implied Barrels per MT} = \frac{\text{Calculated Unit Value (USD/MT)}}{\text{Indian Basket FOB Price (USD/bbl)}}$$

$$\text{Differential (USD/bbl)} = \text{Crude Unit Value (USD/bbl)} - \text{Indian Basket FOB Price (USD/bbl)}$$

$$\text{Percentage Differential (\%)} = \left( \frac{\text{Differential}}{\text{Indian Basket FOB Price}} \right) \times 100$$

A positive differential reflects the wedge between **CIF customs valuation** (which includes ocean freight, tanker demurrage, and marine insurance) and **FOB port-of-loading benchmarks**, as well as the quality premia of specific sweet/sour crude blends relative to the standardized Indian Basket.

---

### 3.2 Symmetric Two-Factor Expenditure Decomposition
To investigate whether annual fluctuations in import expenditure were driven primarily by physical volume expansion or international price shocks, a **symmetric two-factor decomposition** (Montgomery-Vartia / Bennet framework) is applied.

Let import expenditure be defined as the product of physical quantity and unit value:

$$V_t = Q_t \times P_t$$

The annual change in expenditure between period $t-1$ (base) and period $t$ (current) is:

$$\Delta V = V_t - V_{t-1} = Q_t P_t - Q_{t-1} P_{t-1}$$

This change can be decomposed identically into:

$$\Delta V = \underbrace{\Delta Q \cdot \bar{P}}_{\text{Quantity Contribution}} + \underbrace{\Delta P \cdot \bar{Q}}_{\text{Unit-Value (Price) Contribution}}$$

Where:
* $\Delta Q = Q_t - Q_{t-1}$ (change in physical volume, in TMT).
* $\Delta P = P_t - P_{t-1}$ (change in unit value, in Million USD / TMT).
* $\bar{P} = \frac{P_{t-1} + P_t}{2}$ (arithmetic mean unit value).
* $\bar{Q} = \frac{Q_{t-1} + Q_t}{2}$ (arithmetic mean physical volume).

#### Exact Arithmetic Closure Proof:
$$\Delta Q \cdot \bar{P} + \Delta P \cdot \bar{Q} = (Q_t - Q_{t-1}) \left(\frac{P_{t-1} + P_t}{2}\right) + (P_t - P_{t-1}) \left(\frac{Q_{t-1} + Q_t}{2}\right)$$

$$= \frac{1}{2} \left[ Q_t P_{t-1} + Q_t P_t - Q_{t-1} P_{t-1} - Q_{t-1} P_t + P_t Q_{t-1} + P_t Q_t - P_{t-1} Q_{t-1} - P_{t-1} Q_t \right]$$

$$= \frac{1}{2} \left[ 2 Q_t P_t - 2 Q_{t-1} P_{t-1} \right] = Q_t P_t - Q_{t-1} P_{t-1} = \Delta V \quad \blacksquare$$

Arithmetic closure holds **identically with zero residual**, eliminating arbitrary interaction terms ($\Delta Q \Delta P$) by distributing the cross-product equally between quantity and price effects.

---

### 3.3 Implied Exchange Rate and the Currency Multiplier
Because India settles international oil purchases primarily in US Dollars while downstream consumers pay in Indian Rupees, exchange rate movements exert a powerful transmission effect.

#### Implied Petroleum Trade Exchange Rate:
$$e_t = \frac{V_{\text{INR}, t} \times 10^7}{V_{\text{USD}, t} \times 10^6} = \frac{V_{\text{INR}, t} \times 10}{V_{\text{USD}, t}} \quad (\text{INR per USD})$$

#### The Currency Multiplier Formulation:
Letting $V_{\text{INR}, t} = e_t \times V_{\text{USD}, t}$, the cumulative growth ratio of Rupee expenditure relative to Dollar expenditure is:

$$\frac{V_{\text{INR}, t} / V_{\text{INR}, 0}}{V_{\text{USD}, t} / V_{\text{USD}, 0}} = \frac{e_t}{e_0}$$

Where $\frac{e_t}{e_0}$ is the cumulative exchange rate depreciation multiplier. When the Rupee weakens ($e_t > e_0$), domestic fiscal and macroeconomic import exposure expands at a rate strictly greater than international dollar price increases.

---

### 3.4 Compound Annual Growth Rate (CAGR) Specification
CAGR is calculated across seven policy and economic regimes:

$$\text{CAGR}_{t_0, t_n} = \left[ \left( \frac{V_{t_n}}{V_{t_0}} \right)^{\frac{1}{n}} - 1 \right] \times 100$$

* **Subperiod 1 (FY 1998–99 to 2002–03):** Pre-Commodity Supercycle / Early Deregulation (4 yrs).
* **Subperiod 2 (FY 2002–03 to 2008–09):** The Great Global Commodity Supercycle (6 yrs).
* **Subperiod 3 (FY 2008–09 to 2013–14):** Post-GFC \& \$100+ Oil Regime (5 yrs).
* **Subperiod 4 (FY 2013–14 to 2019–20):** Structural Oil Price Collapse \& PMUY Scale-Up (6 yrs).
* **Subperiod 5 (FY 2019–20 to 2022–23):** COVID-19 Demand Shock \& Ukraine War Energy Crisis (3 yrs).
* **Subperiod 6 (FY 2022–23 to 2024–25):** Post-Crisis Price Moderation \& Normalization (2 yrs).
* **Full Horizon (FY 1998–99 to 2024–25):** 26-year structural long-term historical CAGR.

---

## 4. Analytical Quality Assurance and Caveats

1. **Valuation Basis Disclosure:** All import values in Tables 21 and 22 are reported on a **Cost, Insurance, and Freight (CIF)** basis at Indian discharge ports. Benchmark crude prices (Indian Basket) are quoted on a **Free on Board (FOB)** basis at loading ports in the Middle East and North Sea.
2. **Product Basket Unit Values:** Aggregate unit values for `Total Petroleum Products` and `Others` represent composite weighted averages. Changes in composite unit values reflect both underlying price movements and structural shifts in product mix (e.g., rising LPG share).
3. **Provisional Data Labeling:** Data for **FY 2024–25** are classified as Provisional (P) in PPAC ledgers.
4. **Zero-Value Treatment:** Undefined unit values resulting from zero import volumes (e.g. SKO post-2020) are preserved as `NaN` and excluded from ratio and CAGR evaluations.
