# Phase 6 Results Report: Petroleum Import Expenditure, Import Unit Values, and Price Effects

**Project Title:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** 06 — Financial Import Outlays, Unit Values, and Price Effect Decomposition  
**Status:** Completed and Validated  
**Date:** October 2026  
**Master Analysis Script:** [`src/phase6_import_analysis.py`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/src/phase6_import_analysis.py)  

---

## 1. Executive Summary

Phase 6 investigates the financial magnitude, unit costs, and structural drivers of India's petroleum import outlays over the 26-year historical horizon from FY 1998–99 to FY 2024–25. By integrating physical import volumes ($Q$), customs financial outlays in US Dollars ($V_{\text{USD}}$) and Indian Rupees ($V_{\text{INR}}$), and international benchmark prices, this phase provides quantitative answers to the core research questions regarding India's external energy vulnerability:

1. **Massive Secular Expansion of Import Expenditure:**  
   India's total petroleum import bill expanded from **\$6.41 Billion** (₹27,191 Crore) in FY 1998–99 to **\$156.30 Billion** (₹12,95,244 Crore) in FY 2023–24, and **\$160.85 Billion** (₹13,42,234 Crore) in provisional FY 2024–25. Over the 26-year period, annual petroleum import outlays grew at a **Compound Annual Growth Rate (CAGR) of 13.19% in USD** and **16.24% in INR**.
2. **Extreme Decoupling of Financial Outlays from Physical Quantities:**  
   Physical crude oil imports grew **6.1-fold** (from $39.81\text{ MMT}$ to $243.22\text{ MMT}$), whereas crude import expenditure expanded **39.0-fold in USD** (from \$3.52B to \$137.17B) and **77.8-fold in INR** (from ₹14,917 Cr to ₹11,60,618 Cr). This extreme divergence proves that macroeconomic import exposure was driven primarily by global price cycles and currency depreciation rather than domestic volume adjustments.
3. **Price Contributions Overwhelmingly Dominate Short-Term Volatility:**  
   Symmetric two-factor decomposition ($\Delta V = \Delta Q \cdot \bar{P} + \Delta P \cdot \bar{Q}$) reveals that in periods of macroeconomic stress, **international price (unit value) fluctuations accounted for 75% to 90% of the annual change in India's import bill**:
   * During the FY 2021–22 recovery, crude expenditure increased by **+\$58.43 Billion**, of which **87.9% (+\$51.38B)** was arithmetically attributable to surging unit values.
   * During the FY 2014–16 global oil price collapse, India saved **\$78.99 Billion** in crude outlays, with price declines contributing **\$85.23 Billion** in savings (offsetting physical volume growth).
4. **Calculated Import Unit Values Faithfully Track the Indian Basket:**  
   Calculated crude oil import unit values (in USD per barrel at $7.33\text{ bbl/MT}$) track the official Indian Basket FOB benchmark with near-perfect correlation ($R^2 = 0.994$). The average implied conversion ratio of **7.12 barrels per metric tonne** reflects the physical density of India's import slate (dominated by heavy/sour Middle Eastern grades) and CIF transportation/insurance margins.
5. **The Currency Depreciation Multiplier:**  
   The secular depreciation of the Indian Rupee against the US Dollar—weakening from ₹42.07/\$ in FY 1998–99 to ₹83.45/\$ in FY 2024–25 (+98.4% weakening)—acted as a severe financial amplifier. India's nominal Rupee import bill expanded twice as fast as its Dollar bill, escalating domestic inflationary pressure and fiscal subsidy exposure.
6. **Structural Inversion of Product Import Outlays:**  
   In FY 1998–99, diesel (HSD) and kerosene (SKO) accounted for **71.0%** of all refined product import expenditure (\$2,057M of \$2,895M). By FY 2024–25, HSD and SKO imports were virtually eliminated (0.1% share), while **Liquefied Petroleum Gas (LPG)** expanded to consume **\$12.48 Billion**, representing **52.7% of total product import expenditure**.

---

## 2. Longitudinal Overview: Quantities, Values, and Unit Costs

The longitudinal dynamics of India's petroleum imports are summarized below using standardized series from [`import_quantity_value_aligned_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/import_quantity_value_aligned_dataset.csv):

```
+-------------------------------------------------------------------------------------------------------------------------+
|                                    HISTORICAL PETROLEUM IMPORT EXPENDITURE & UNIT VALUES                                |
|                                           (Values in Million USD, TMT, and USD/MT)                                      |
+-------------+-----------------------+-----------------------+-----------------------+---------------------+-------------+
| Financial   | Crude Imports         | Product Imports       | Total Petroleum       | Implied Unit Values | Implied FX  |
| Year        | Quantity    Value     | Quantity    Value     | Quantity    Value     | Crude       Product | Rate        |
|             | (TMT)       ($ Mil)   | (TMT)       ($ Mil)   | (TMT)       ($ Mil)   | ($/MT)      ($/MT)  | (INR / USD) |
+-------------+-----------------------+-----------------------+-----------------------+---------------------+-------------+
| FY 1998-99  |  39,808.0    3,518.0  |  23,771.0    2,895.0  |  63,579.0    6,413.0  |   88.37      121.79 |   42.07     |
| FY 2002-03  |  81,989.0   15,759.0  |   7,228.0    1,822.0  |  89,217.0   17,581.0  |  192.21      252.08 |   48.37     |
| FY 2008-09  | 132,775.0   76,876.0  |  22,462.0   14,482.0  | 155,237.0   91,358.0  |  578.99      644.73 |   45.89     |
| FY 2011-12  | 171,729.2  139,689.9  |  15,849.2   15,487.6  | 187,578.3  155,177.5  |  813.43      977.19 |   47.95     |
| FY 2012-13  | 184,795.2  144,293.1  |  16,339.7   19,951.7  | 201,135.0  164,244.8  |  780.83     1221.05 |   54.45     |
| FY 2013-14  | 189,238.2  142,961.6  |  16,717.3   12,284.1  | 205,955.5  155,245.7  |  755.46      734.82 |   60.50     |
| FY 2015-16  | 202,850.5   63,972.4  |  29,498.7   10,296.3  | 232,349.2   74,268.7  |  315.37      349.04 |   65.46     |
| FY 2019-20  | 226,954.7  101,376.2  |  43,767.1   17,801.3  | 270,721.8  119,177.5  |  446.68      406.73 |   70.88     |
| FY 2020-21  | 196,460.9   62,248.0  |  43,247.7   13,858.9  | 239,708.5   76,106.9  |  316.85      320.45 |   74.20     |
| FY 2021-22  | 212,381.6  120,675.2  |  39,016.7   22,143.2  | 251,398.3  142,818.4  |  568.20      567.53 |   74.51     |
| FY 2022-23  | 232,700.4  157,531.0  |  44,597.9   25,487.6  | 277,298.3  183,018.6  |  676.97      571.50 |   80.39     |
| FY 2023-24  | 234,261.6  133,366.4  |  48,692.8   22,932.6  | 282,954.4  156,299.0  |  569.31      470.97 |   82.87     |
| FY 2024-25  | 243,225.0  137,174.0  |  50,903.0   23,673.3  | 294,128.0  160,847.3  |  563.98      465.07 |   83.45     |
+-------------+-----------------------+-----------------------+-----------------------+---------------------+-------------+
```

---

## 3. Detailed Answers to Core Research Questions

### Question 1: How did petroleum import expenditure change over the observed period?
India's petroleum import expenditure followed three distinct macroeconomic phases:
1. **The Low-Cost Baseline (FY 1998–99 to 2002–03):** Import bills were modest, averaging \$6B to \$17B annually, with crude oil costing between \$88 and \$192/MT (\$12 to \$26/bbl).
2. **The Commodity Supercycle & \$100 Oil Era (FY 2003–04 to 2013–14):** Driven by rapid industrialization in emerging markets and global supply tightness, India's crude import bill surged from \$18.27B in FY 2003–04 to a peak of **\$144.29 Billion** in FY 2012–13. The total petroleum bill reached \$164.24 Billion.
3. **The Twin Volatility Shocks (FY 2014–15 to 2024–25):** The market experienced two historic price collapses and two violent rebounds:
   * **The 2014–16 Crash:** US shale supply expansion crashed crude import bills from \$142.96B to \$63.97B in FY 2015–16.
   * **The 2020 Pandemic Shock:** COVID-19 lockdowns collapsed outlays to \$62.25B in FY 2020–21.
   * **The 2022 Post-COVID / War Surge:** Global demand recovery and the Russia-Ukraine conflict drove the crude bill to an all-time record of **\$157.53 Billion** (₹12,60,372 Crore) in FY 2022–23.
   * **The 2023–25 Normalization:** Outlays moderated to \$133.37B (FY 2023–24) and \$137.17B (FY 2024–25).

---

### Question 2: Did import expenditure rise or fall in periods when import quantity moved differently?
**Yes.** Decoupling between physical volume and financial outlays occurred repeatedly:
* **FY 2008–09 vs FY 2009–10:** In FY 2009–10, crude import quantity surged by **+19.9%** (from $132.78\text{ MMT}$ to $159.26\text{ MMT}$, an increase of $+26.48\text{ MMT}$) as Indian refiners expanded throughput post-GFC. However, import expenditure grew by only **+3.5%** (+\$2.68B), because unit values fell from \$578.99/MT to \$499.52/MT.
* **FY 2014–15:** Crude import volume increased by **+0.1%**, but import expenditure plunged by **-21.1%** (saving \$30.22 Billion) entirely due to global price declines.
* **FY 2015–16:** Crude volume expanded by **+7.1%** ($+13.42\text{ MMT}$), yet expenditure plummeted by **-43.3%** (saving \$48.77 Billion).
* **FY 2021–22:** Crude volume grew by **+8.1%**, but financial expenditure skyrocketed by **+93.9%** (increasing by +\$58.43 Billion) due to unit values leaping by +79.3%.

---

### Question 3: How did calculated import unit values evolve?
Calculated import unit values ([`import_unit_values.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/import_unit_values.csv)) exhibited massive cyclical dispersion:
* **Crude Oil Unit Value:**
  * Baseline (1998–99): **\$88.37/MT** (\$12.06/bbl)
  * Historical Peak (2011–12): **\$813.43/MT** (\$110.97/bbl)
  * Pandemic Trough (2020–21): **\$316.85/MT** (\$43.23/bbl)
  * Post-War Peak (2022–23): **\$676.97/MT** (\$92.36/bbl)
  * Latest Period (2024–25): **\$563.98/MT** (\$76.94/bbl)
* **Refined Product Unit Values:**
  * High-value distillates (LPG, MS, ATF, Lubes) consistently commanded premiums over crude oil. In FY 2023–24, Motor Spirit import unit value was **\$923.6/MT**, Lubricants were **\$957.7/MT**, and LPG was **\$562.4/MT**, compared to heavy Bitumen at **\$405.2/MT** and Fuel Oil at **\$448.6/MT**.

---

### Question 4: How closely did calculated crude unit values track the Indian Basket price?
Tracking is exceptionally close across the entire 24-year overlapping series (FY 2000–01 to FY 2024–25):
* **Correlation:** $r = 0.997$ ($R^2 = 0.994$).
* **Mean Absolute Tracking Error:** \$2.14 per barrel.
* **Why Differences Occur:**
  1. **CIF vs FOB Valuation Wedge:** The calculated import unit value is on a CIF basis (including maritime shipping freight, tanker insurance, and port handling charges), whereas the Indian Basket is an FOB loading-port benchmark. In years of elevated tanker freight rates (e.g. 2007–08 and 2022–23), CIF unit values exceed FOB benchmarks.
  2. **Crude Gravity Variation:** Indian refiners import diverse grades ranging from heavy Latin American and Middle Eastern crudes (API 24–28, density ~6.8 to 7.1 bbl/MT) to light African and US crudes (API 38–44, density ~7.4 to 7.6 bbl/MT). The implied conversion ratio averaged **7.12 bbl/MT**, slightly denser than the PPAC convention of 7.33 bbl/MT.
  3. **Discounts on Russian Urals (FY 2022–24):** Post-2022, Indian refiners imported discounted Russian crude. Because customs values reflect actual invoiced purchase prices while the theoretical Indian Basket weighting maintained traditional Middle Eastern benchmarks, calculated unit values tracked slightly below benchmark spot prices.

---

### Question 5: Were major changes in expenditure associated with quantity, unit value, or mixed changes?
The symmetric two-factor decomposition ([`import_expenditure_decomposition.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/import_expenditure_decomposition.csv)) confirms that **price (unit value) contributions overwhelmingly dominated major annual swings**:

```
+----------------------------------------------------------------------------------------------------+
|                         DECOMPOSITION OF MAJOR CRUDE IMPORT EXPENDITURE SWINGS                      |
|                                       (Values in Million US$)                                      |
+-------------+----------------+----------------+----------------+-------------+---------------------+
| Fiscal Year | Total Change   | Quantity       | Unit Value     | Arithmetic  | Dominant Driver     |
| Transition  | (Delta V)      | Contribution   | Contribution   | Closure     |                     |
+-------------+----------------+----------------+----------------+-------------+---------------------+
| 2003 -> 2004| +$7,722.0 M    | +$1,283.8 M    | +$6,438.2 M    | EXACT PASS  | Price (83.4%)       |
| 2007 -> 2008| +$8,888.0 M    | +$6,316.4 M    | +$2,571.6 M    | EXACT PASS  | Quantity (71.1%)    |
| 2008 -> 2009| +$2,677.0 M    | +$14,281.7 M   | -$11,604.7 M   | EXACT PASS  | Quantity Rebound    |
| 2010 -> 2011| +$39,609.9 M   | +$5,796.3 M    | +$33,813.6 M   | EXACT PASS  | Price (85.4%)       |
| 2013 -> 2014| -$30,218.0 M   |   +$132.8 M    | -$30,350.8 M   | EXACT PASS  | Price Drop (100.4%) |
| 2014 -> 2015| -$48,771.2 M   | +$6,107.6 M    | -$54,878.8 M   | EXACT PASS  | Price Drop (112.5%) |
| 2019 -> 2020| -$39,128.1 M   | -$11,641.4 M   | -$27,486.7 M   | EXACT PASS  | Price (70.2%)       |
| 2020 -> 2021| +$58,427.1 M   | +$7,045.3 M    | +$51,381.8 M   | EXACT PASS  | Price Surge (87.9%) |
| 2021 -> 2022| +$36,855.9 M   | +$12,650.2 M   | +$24,205.7 M   | EXACT PASS  | Price (65.7%)       |
| 2022 -> 2023| -$24,164.6 M   |   +$972.8 M    | -$25,137.4 M   | EXACT PASS  | Price Drop (104.0%) |
+-------------+----------------+----------------+----------------+-------------+---------------------+
```

---

### Question 6: How do crude oil imports differ from petroleum product imports in expenditure patterns?
1. **Magnitude:** Crude oil constitutes the dominant share, accounting for **85.3% of total petroleum import expenditure** in FY 2024–25 (\$137.17B of \$160.85B).
2. **Structural Compositional Shift in Product Imports:** While crude oil is a relatively homogeneous feedstock, product import expenditure underwent a radical structural inversion:
   * **HSD:** Fell from \$1,134M (39.2% of product bill) in 1998–99 to \$32.5M (0.1%) in 2024–25.
   * **SKO:** Fell from \$923M (31.9%) to \$0.0M (0.0%).
   * **LPG:** Expanded from \$300M (10.4%) to **\$12,479M (52.7%)**.
   Consequently, while crude imports reflect macroeconomic industrial expansion, product import expenditures reflect **household cooking policy (PMUY)** and domestic refining yield limits.

---

### Question 7: What do the data establish about exposure to international prices, and what remains uncertain?
* **Established Facts:** India is a structural price-taker. Because domestic production of crude oil covers less than 12% of national throughput, movements in international crude benchmarks translate directly into domestic import expenditure. Short-term volume adjustments are virtually powerless to mitigate international price shocks; refiners cannot rapidly curb crude runs without triggering domestic fuel shortages.
* **What Remains Uncertain:** The extent to which long-term term-contracts versus spot market purchases mitigated volatility; the precise ocean freight component for specific discharge ports (Vadinar, Paradip, Mundra); and the net corporate hedging gains/losses realized by refiners.

---

### Question 8: Which conclusions are limited by currency, valuation, and coverage?
* **Currency Compounding:** Nominal Rupee expenditure grew at **18.23% CAGR** for crude oil, compared to **15.13% CAGR** in USD. A significant portion of India's perceived domestic cost inflation was driven by foreign exchange depreciation rather than physical barrel consumption.
* **Valuation Basis:** PPAC import values are CIF, while export values are FOB. Direct subtraction to obtain "net import bills" includes a transportation margin on imports.

---

## 4. Subperiod Growth Analysis (CAGR Summary)

Key CAGR metrics from [`import_cagr_summary.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/import_cagr_summary.csv):

```
+----------------------------------------------------------------------------------------------------+
|                                SUBPERIOD GROWTH PROFILE (CAGR %)                                    |
+-----------------------------------------+--------------------+------------------+------------------+
| Economic & Policy Regime                | Crude Value ($)    | Crude Volume (Q) | Crude Price (P)  |
+-----------------------------------------+--------------------+------------------+------------------+
| 1. Pre-Commodity Supercycle (1998-02)   | +45.45%            | +19.78%          | +21.43%          |
| 2. The Commodity Supercycle (2002-08)   | +30.23%            |  +8.37%          | +20.18%          |
| 3. Post-GFC & $100 Oil Era (2008-13)    | +13.21%            |  +6.84%          |  +5.97%          |
| 4. Oil Price Collapse & PMUY (2013-19)  |  -5.57%            |  +3.08%          |  -8.39%          |
| 5. Pandemic & Ukraine Shock (2019-22)   | +15.82%            |  +0.84%          | +14.86%          |
| 6. Post-Crisis Moderation (2022-24)     |  -6.68%            |  +2.24%          |  -8.72%          |
+-----------------------------------------+--------------------+------------------+------------------+
| FULL 26-YEAR HISTORICAL HORIZON (1998-24| +15.13%            |  +7.21%          |  +7.39%          |
+-----------------------------------------+--------------------+------------------+------------------+
```
*(Note: In Subperiod 1, high CAGR reflects normalization from the 1998 Asian Financial Crisis oil trough).*

---

## 5. Visualizations Catalogue

All 8 publication-grade figures have been generated and archived in [`04_Analysis/phase6/figures/`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/) (in both 300 DPI PNG and vector SVG), with underlying data preserved in [`04_Analysis/phase6/figure_data/`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figure_data/):

* **Figure 1 ([`fig1...png`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig1_historical_crude_import_expenditure.png) / [`.svg`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig1_historical_crude_import_expenditure.svg)):** Historical Crude Oil Import Expenditure (Dual panel: USD Billion vs Lakh Crore INR).
* **Figure 2 ([`fig2...png`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig2_product_import_expenditure_trajectories.png) / [`.svg`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig2_product_import_expenditure_trajectories.svg)):** Historical Petroleum Product Import Expenditure Trajectories (Total, LPG, HSD, SKO, Naphtha, FO).
* **Figure 3 ([`fig3...png`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig3_volume_vs_value_decoupling.png) / [`.svg`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig3_volume_vs_value_decoupling.svg)):** Physical Volume vs Financial Expenditure Decoupling (Indexed 1998–99 = 100).
* **Figure 4 ([`fig4...png`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig4_crude_unit_value_vs_indian_basket.png) / [`.svg`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig4_crude_unit_value_vs_indian_basket.svg)):** Calculated Crude Import Unit Value vs Indian Basket Crude FOB Price ($/bbl alignment and implied bbl/MT density).
* **Figure 5 ([`fig5...png`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig5_expenditure_vs_quantity_growth_elasticity.png) / [`.svg`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig5_expenditure_vs_quantity_growth_elasticity.svg)):** Expenditure Growth vs Physical Volume Growth Elasticity (YoY % scatter showing dispersion from 1:1 parity).
* **Figure 6 ([`fig6...png`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig6_expenditure_decomposition_contributions.png) / [`.svg`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig6_expenditure_decomposition_contributions.svg)):** Symmetric Two-Factor Expenditure Decomposition (Bar chart of Volume vs Price contributions).
* **Figure 7 ([`fig7...png`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig7_currency_depreciation_multiplier.png) / [`.svg`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig7_currency_depreciation_multiplier.svg)):** The Currency Depreciation Multiplier (USD vs INR total bill growth and implied INR/USD exchange rate).
* **Figure 8 ([`fig8...png`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig8_product_import_bill_composition_shares.png) / [`.svg`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figures/fig8_product_import_bill_composition_shares.svg)):** Product Composition of Import Expenditure (% shares over 27 years illustrating the rise of LPG).
