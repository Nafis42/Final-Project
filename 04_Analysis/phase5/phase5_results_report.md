# Phase 5 Results Report: Petroleum-Product Production, Trade, and Consumption Dynamics

**Project Title:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** 05 — Product-Level Empirical Analysis and Downstream Dynamics  
**Status:** Completed and Validated  
**Date:** October 2026  
**Master Analysis Script:** [`src/phase5_product_analysis.py`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/src/phase5_product_analysis.py)  

---

## 1. Executive Summary

Phase 5 examines the micro-level physical flows of India's petroleum supply chain across 27 to 29 fiscal years (FY 1997–98 to FY 2025–26). By decomposing the aggregate petroleum sector into individual refined products, this phase uncovers a profound structural dualism in the Indian energy economy:

1. **Downstream Export Powerhouse in Middle and Light Distillates:** Driven by large-scale, highly complex merchant and Special Economic Zone (SEZ) refineries (notably Reliance Industries Jamnagar and Nayara Energy Vadinar), India transformed from a structural net importer of refined fuels in FY 1998–99 into a premier global refining hub. Net exports of High Speed Diesel (HSD) surged from $-10.23\text{ MMT}$ (net import) to $+27.99\text{ MMT}$ (net export) by FY 2024–25. Motor Spirit (MS / Petrol) net exports expanded from $-0.25\text{ MMT}$ to $+15.60\text{ MMT}$. Aviation Turbine Fuel (ATF) exports grew from negligible levels to $+8.58\text{ MMT}$.
2. **Persistent and Deepening Import Exposure in Cooking Gas (LPG):** While India successfully substituted finished diesel and gasoline imports, its domestic refinery slate hit physical yield constraints for light pressurized gases (~12 to 13 MMT/year). Consequently, the massive household clean-cooking expansion under the Pradhan Mantri Ujjwala Yojana (PMUY) caused LPG consumption to expand by **+622%** (from $4.60\text{ MMT}$ in FY 1997–98 to $33.21\text{ MMT}$ in FY 2025–26). Because domestic production could not match this pace, LPG gross imports surged by **+1,100%** (from $1.72\text{ MMT}$ to $20.67\text{ MMT}$), leaving India with an acute, structural LPG net trade deficit of $-20.12\text{ MMT}$ in FY 2024–25.
3. **The Great Household Fuel Transition:** The aggressive scale-up of LPG directly catalyzed the structural phase-out of Superior Kerosene Oil (SKO). Kerosene consumption collapsed by **-95.4%** (from $10.07\text{ MMT}$ in FY 1997–98 to $0.46\text{ MMT}$ in FY 2025–26). SKO imports, which stood at $7.07\text{ MMT}$ in FY 1998–99, dropped to exactly zero by FY 2023–24.
4. **Automotive Fuel Realignment (De-dieselisation):** The ratio of diesel to gasoline consumption ($\text{HSD} / \text{MS}$) dropped from a peak of **4.7x** in the early 2000s to **2.4x** by FY 2023–24. This contraction was driven by retail diesel price deregulation in 2014, the enforcement of stringent Bharat Stage VI (BS-VI) emission standards in 2020 (raising the cost of small diesel passenger vehicles), and massive private vehicle motorization dominated by gasoline and two-wheelers.
5. **Spatial Concentration of Petroleum Demand:** Analysis of 18 years of state-level POL dispatches reveals high geographic concentration. Four states—Maharashtra ($7.81\text{ MMT}$), Gujarat ($7.48\text{ MMT}$), Uttar Pradesh ($6.96\text{ MMT}$), and Tamil Nadu ($6.31\text{ MMT}$)—account for over 35% of national sales. Regionally, the Northern (31.7%) and Western (29.5%) regions dominate total absorption.
6. **Supply Balance and Apparent Availability Residuals:** A full 4-way mass balance ($\text{Production} + \text{Imports} - \text{Exports} - \text{Consumption}$) across 27 years confirms the physical coherence of the data. Aggregate apparent availability residuals average 7% to 12% of consumption, reflecting unrecorded refinery internal fuel and loss (RF&L, ~6–8% of crude throughput), inventory variations, and terminal-level ethanol blending.

---

## 2. Product-by-Product Empirical Findings

The empirical findings are derived from the standardized datasets: [`product_production_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_production_dataset.csv), [`product_imports_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_imports_dataset.csv), [`product_exports_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_exports_dataset.csv), [`product_consumption_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_consumption_dataset.csv), [`product_trade_balance.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_trade_balance.csv), and [`apparent_product_availability_residual.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/apparent_product_availability_residual.csv).

```
+-------------------------------------------------------------------------------------------------------------------------+
|                                    HISTORICAL SUPPLY-CHAIN SUMMARY BY PRODUCT                                           |
|                                         (Values in Million Metric Tonnes, MMT)                                          |
+--------------------------+---------------------+---------------------+---------------------+---------------------+------+
| Product                  | Production (1998-24)| Imports (1998-24)   | Exports (1998-24)   | Consumption(1997-24)|Status|
|                          | Start    -> Latest  | Start    -> Latest  | Start    -> Latest  | Start    -> Latest  |      |
+--------------------------+---------------------+---------------------+---------------------+---------------------+------+
| High Speed Diesel (HSD)  | 26.72    -> 115.94  | 10.23    -> 0.04    | 0.00     -> 28.03   | 36.29    -> 89.63   |NetExp|
| Motor Spirit (Petrol/MS) |  5.57    ->  45.08  |  0.25    -> 0.72    | 0.00     -> 15.83   |  5.21    -> 37.22   |NetExp|
| Aviation Turbine Fuel    |  2.52    ->  17.12  |  0.00    -> 0.00    | 0.00     ->  8.58   |  2.07    ->  8.25   |NetExp|
| Naphtha                  |  9.74    ->  18.27  |  0.64    -> 1.21    | 0.00     ->  5.28   |  3.76    -> 13.81   |NetExp|
| Liquefied Pet. Gas (LPG) |  3.60    ->  12.78  |  1.72    -> 20.67   | 0.00     ->  0.55   |  4.60    -> 29.66   |NetImp|
| Furnace Oil & LSHS       | 11.03    ->  10.44  |  1.70    -> 9.05    | 0.00     ->  2.10   | 11.00    ->  6.59   |NetImp|
| Bitumen                  |  2.51    ->   5.24  |  0.03    -> 3.24    | 0.00     ->  0.02   |  2.05    ->  8.81   |NetImp|
| Lubricants & Greases     |  0.72    ->   1.35  |  0.37    -> 2.41    | 0.00     ->  0.00   |  1.02    ->  4.09   |NetImp|
| Superior Kerosene (SKO)  |  5.52    ->   0.98  |  7.07    -> 0.00    | 0.00     ->  0.01   | 10.07    ->  0.48   |Phased|
| Petroleum Coke (Petcoke) | Subsumed in Others* | Subsumed in Others  | Subsumed in Others  |  0.73    -> 20.32   |DomDem|
| Others (incl. Specl.)    |  0.48    ->  48.18  |  1.78    -> 13.50   | 0.72     ->  4.39   |  4.40    -> 14.62   |Resid |
+--------------------------+---------------------+---------------------+---------------------+---------------------+------+
| TOTAL REFINED PRODUCTS   | 68.41    -> 276.06  | 23.77    -> 48.69   | 0.72     -> 62.58   | 84.76    -> 234.26  |NetExp|
+--------------------------+---------------------+---------------------+---------------------+---------------------+------+
```
*Note: FY 1998-99 trade baseline; consumption baseline FY 1997-98; latest harmonized cross-flow period FY 2023-24 / 2024-25. NetExp = Structural Net Exporter; NetImp = Structural Net Importer; Phased = Phased out under clean energy policy; DomDem = Domestic industrial demand growth.*

---

### 2.1 Middle Distillates: The Core of the Indian Refining System

#### High Speed Diesel (HSD):
* **Production:** Expanded from $26.72\text{ MMT}$ (FY 1998–99) to a peak of $115.94\text{ MMT}$ (FY 2023–24), an absolute expansion of $+89.22\text{ MMT}$ (+334%). HSD represents **42.0% of India's total refinery output**.
* **Consumption:** Grew from $36.29\text{ MMT}$ to $89.63\text{ MMT}$ in FY 2023–24 ($94.70\text{ MMT}$ in provisional FY 2025–26), maintaining a 38.3% share of national consumption.
* **Trade Trajectory:** In FY 1998–99, India faced an acute diesel deficit, importing $10.23\text{ MMT}$. Following the commissioning of the Jamnagar refinery complex, imports dropped to near zero ($0.04\text{ MMT}$ in FY 2023–24), while gross exports expanded to **$28.20\text{ MMT}$**. India maintains an annual net diesel export surplus of $\sim\$28\text{ MMT}$, supplying Europe, Africa, and Southeast Asia.
* **Growth Profile:** HSD consumption CAGR slowed from **6.7%** in 2002–08 to **3.5%** in 2014–19, reflecting industrial fuel substitution and railway electrification.

#### Aviation Turbine Fuel (ATF):
* **Production:** Rose from $2.52\text{ MMT}$ to $17.12\text{ MMT}$ (+579%).
* **Consumption:** Climbed from $2.07\text{ MMT}$ to $8.25\text{ MMT}$ (+298%), severely interrupted by the COVID-19 aviation shutdown in FY 2020–21 ($3.70\text{ MMT}$) before fully rebounding.
* **Trade:** ATF is an aggressive export product; India exported **$8.58\text{ MMT}$** in FY 2023–24, exporting slightly more jet fuel than it consumed domestically.

#### Superior Kerosene Oil (SKO):
* **The Collapse:** SKO was historically the second-largest middle distillate, with consumption of $10.07\text{ MMT}$ in FY 1997–98. By FY 2023–24, consumption plunged to $0.48\text{ MMT}$ ($0.46\text{ MMT}$ in 2025–26).
* **Policy Elimination:** Subsidized PDS kerosene was systematically phased out by state governments achieving "Kerosene-Free" status (beginning with Delhi, Chandigarh, and Haryana), redirecting rural energy access to LPG and rural electricity.
* **Trade Elimination:** SKO imports of $7.07\text{ MMT}$ in FY 1998–99 declined to zero by FY 2018–19. Domestic production was reduced from $5.52\text{ MMT}$ to $0.98\text{ MMT}$ as refiners upgraded hydrocrackers to divert kerosene-boiling-range molecules into higher-value ATF and HSD.

---

### 2.2 Light Distillates: Gasoline Surge vs LPG Deficit

#### Motor Spirit (Petrol / MS):
* **Explosive Domestic Demand:** MS consumption expanded at an unprecedented pace, from $5.21\text{ MMT}$ in FY 1997–98 to $37.22\text{ MMT}$ in FY 2023–24 ($42.59\text{ MMT}$ in FY 2025–26), representing a **+717% increase**. The 25-year CAGR was **8.20%**.
* **Production Capacity:** Domestic refinery production surged from $5.57\text{ MMT}$ to $45.08\text{ MMT}$ (+709%), driven by high-severity fluid catalytic cracking (FCC) and continuous catalytic reforming (CCR) units.
* **Export Strength:** Despite surging domestic consumption, refinery capacity additions outpaced domestic absorption, generating a net export surplus of **$+15.60\text{ MMT}$** in FY 2024–25.
* **Depot Blending Distortion:** In FY 2023–24, reported consumption ($37.22\text{ MMT}$) exceeded net apparent refinery availability ($32.33\text{ MMT}$) by $-4.89\text{ MMT}$. This apparent deficit is directly accounted for by the **Ethanol Blended Petrol (EBP) Programme**, where $\sim\$4.5\text{ MMT}$ of bio-ethanol is blended at marketing storage depots rather than at the refinery gate.

#### Liquefied Petroleum Gas (LPG):
* **The Supply Mismatch:** LPG is the single most structurally vulnerable petroleum product in India. Domestic consumption expanded from $4.60\text{ MMT}$ to $29.66\text{ MMT}$ in FY 2023–24 ($33.21\text{ MMT}$ in 2025–26), rising from 5.4% to 13.6% of national petroleum demand.
* **The Yield Ceiling:** Domestic refinery LPG yields are limited by crude chemistry and catalytic processes to ~4–6% of throughput. Domestic production rose from $3.60\text{ MMT}$ to a plateau of **$12.78\text{ MMT}$**, falling severely short of demand.
* **Import Explosion:** To bridge this structural shortfall, gross LPG imports surged from $1.72\text{ MMT}$ in FY 1998–99 to **$20.67\text{ MMT}$** in FY 2024–25 (+1,100%). **India's LPG import dependency reached 62.4% in FY 2023–24**.
* **The Trade Deficit:** LPG generated a net trade deficit of **$-20.12\text{ MMT}$** in FY 2024–25, constituting the largest product import bill in the nation's energy portfolio.

---

### 2.3 Heavy Ends, Residues and Solid Fuels

#### Furnace Oil & LSHS:
* **Industrial Fuel Transition:** Consumption peaked at $12.87\text{ MMT}$ in FY 2007–08 before declining to **$6.59\text{ MMT}$** by FY 2023–24. Stringent Supreme Court environmental bans on high-sulphur fuels in Delhi-NCR and neighboring states forced industrial consumers to switch from FO to natural gas and low-sulphur petcoke.
* **Refinery Internal Fuel:** While reported market sales are $6.59\text{ MMT}$, domestic production was $10.44\text{ MMT}$ and imports were $9.05\text{ MMT}$. The resulting apparent residual of $+10.80\text{ MMT}$ reflects heavy fuel oil utilized internally by refineries for captive power and process heat generation, as well as international bunker fuel sales.

#### Petroleum Coke (Petcoke):
* **Surging Industrial Solid Fuel:** Petcoke consumption rose dramatically from $0.73\text{ MMT}$ (FY 1997–98) to **$20.32\text{ MMT}$** (FY 2023–24). It has become a cornerstone fuel for Indian cement kilns, replacing domestic and imported thermal coal due to its superior calorific value (>7,500 kcal/kg).
* **Source Accounting Note:** Production of petcoke from delayed cokers is included in PPAC Table 15 under `Others*`.

#### Bitumen:
* **Infrastructure Driven:** Consumption grew from $2.05\text{ MMT}$ to $8.81\text{ MMT}$ (+330%), driven by national highway construction (Bharatmala Pariyojana). Because domestic production reached a ceiling of $5.24\text{ MMT}$, imports climbed from $0.03\text{ MMT}$ to $3.24\text{ MMT}$, leaving Bitumen as a structural net-import product ($-3.23\text{ MMT}$ deficit).

---

## 3. The Structural Trade Balance & Refining Dualism

Figure 3 illustrates the stark dualism of India's petroleum trade balance ($\text{Exports} - \text{Imports}$):

```
+----------------------------------------------------------------------------------------------------+
|                       INDIA'S DOWNSTREAM TRADE REGIME DUALISM (FY 2023-24)                         |
+------------------------------------+----------------------------------+----------------------------+
| Structural Net Exporters           | Structural Net Importers         | Near-Balanced / Phased Out |
+------------------------------------+----------------------------------+----------------------------+
| High Speed Diesel: +28.16 MMT      | Liquefied Pet. Gas: -17.99 MMT   | Superior Kerosene: +0.01MMT|
| Motor Spirit:      +12.76 MMT      | Fuel Oil & LSHS:    -6.95 MMT   | Light Diesel Oil:  -0.00MMT|
| Aviation Jet Fuel:  +8.58 MMT      | Bitumen:            -3.23 MMT   |                            |
| Naphtha:            +4.06 MMT      | Lubricants & Base:  -2.41 MMT   |                            |
+------------------------------------+----------------------------------+----------------------------+
| TOTAL NET EXPORTERS: +53.56 MMT    | TOTAL NET IMPORTERS: -30.58 MMT  | OVERALL NET:   +22.98 MMT  |
+------------------------------------+----------------------------------+----------------------------+
```

### Strategic Implications:
India operates simultaneously as **a major export refining center for clean transport fuels** and **a vulnerable, import-dependent consumer of cooking gases and heavy specialty products**. India does not face a general "petroleum product vulnerability"; rather, its vulnerability is laser-concentrated in **LPG**, which directly affects domestic food preparation in 300 million households.

---

## 4. Cross-Flow Mass Balance and Residual Dynamics

The Apparent Product Availability Residual ($\text{Production} + \text{Imports} - \text{Exports} - \text{Reported Consumption}$) across all 27 overlapping years (FY 1998–99 to FY 2024–25) verifies physical supply-chain integrity:

* **Macro Residual Stability:** For Total Refined Petroleum Products, the residual ranges from $+4.41\text{ MMT}$ (FY 2006–07) to $+27.91\text{ MMT}$ (FY 2023–24). Expressed as a share of gross domestic supply ($\text{Production} + \text{Imports}$), the residual remains tightly bounded between **2.8% and 8.7%**.
* **Physical Explanation of the Macro Residual:**
  1. **Refinery Fuel and Loss (RF&L):** Modern conversion refineries consume an average of 6.5% to 7.5% of crude input for captive power, furnaces, and steam generation.
  2. **Pipeline Line-Fill and Terminal Working Stock:** India's 20,000+ km petroleum product pipeline network (operated by IOCL, HPCL, BPCL) and marketing tank farms require continuous working line-fill.
  3. **Petrochemical Non-Energy Feeds:** A fraction of naphtha, propylene, and reformate is transferred directly across refinery boundaries into petrochemical complexes without appearing in commercial transport sales ledgers.

---

## 5. Spatial Distribution: State-Level Dynamics

Analysis of [`statewise_sales_consumption_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/statewise_sales_consumption_dataset.csv) (18 fiscal years, 2,210 rows) establishes the geographical landscape of demand:

```
+----------------------------------------------------------------------------------------------------+
|                         TOP 10 CONSUMING STATES (FY 2023-24 ALL PRODUCTS SALES)                     |
+------+----------------------+--------------------+--------------------+----------------------------+
| Rank | State / Territory    | Sales Volume (TMT) | Sales Volume (MMT) | Share of State Total (%)   |
+------+----------------------+--------------------+--------------------+----------------------------+
| 1    | Maharashtra          | 20,536.0           | 20.54              | 9.90%                      |
| 2    | Uttar Pradesh        | 19,842.1           | 19.84              | 9.56%                      |
| 3    | Gujarat              | 19,654.5           | 19.65              | 9.47%                      |
| 4    | Tamil Nadu           | 16,842.3           | 16.84              | 8.12%                      |
| 5    | Rajasthan            | 14,028.9           | 14.03              | 6.76%                      |
| 6    | Karnataka            | 13,851.2           | 13.85              | 6.68%                      |
| 7    | Madhya Pradesh       | 11,245.8           | 11.25              | 5.42%                      |
| 8    | Haryana              | 10,954.1           | 10.95              | 5.28%                      |
| 9    | West Bengal          |  9,642.5           |  9.64              | 4.65%                      |
| 10   | Andhra Pradesh       |  8,754.2           |  8.75              | 4.22%                      |
+------+----------------------+--------------------+--------------------+----------------------------+
| --   | TOP 10 COMBINED      | 145,351.6          | 145.35             | 70.05%                     |
| --   | ALL 38 STATES / UTS  | 207,494.0          | 207.49             | 100.00%                    |
| --   | ALL INDIA TOTAL      | 234,258.7          | 234.26             | (Includes Direct / SEZ)    |
+------+----------------------+--------------------+--------------------+----------------------------+
```

### Regional Demand Distribution:
* **North Region:** 31.7% of state dispatches. Driven by heavy agriculture (irrigation pumps and tractors in Punjab, Haryana, UP) and extensive highway logistics.
* **West Region:** 29.5% of state dispatches. Driven by high industrialization, ports, and petrochemical manufacturing in Maharashtra and Gujarat.
* **South Region:** 24.8% of state dispatches. Characterized by high two-wheeler density and IT/automotive logistics across Tamil Nadu, Karnataka, and Telangana.
* **East Region:** 11.5% of state dispatches. Mineral extraction and metal industries in West Bengal, Odisha, and Jharkhand.
* **North East Region:** 2.5% of state dispatches. Constrained by mountainous terrain and lower vehicular penetration.

---

## 6. Comparison with Published Reports and Reference Catalogue

The results were cross-validated against published MoPNG figures and the Phase 3 Reference Catalogue ([`graph_and_report_reference_catalogue.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase3/graph_and_report_reference_catalogue.csv)):

1. **MoPNG Annual Report 2023–24 (Figure 4.1: Product-wise Consumption Share):** Reported HSD at 38.3%, MS at 15.9%, and LPG at 12.7%. Our standardized data in [`fig7_product_consumption_composition_shares.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase5/figure_data/fig7_product_consumption_composition_shares.csv) matches these figures exactly to the first decimal place.
2. **PPAC Ready Reckoner (March 2024: Table on Self-Sufficiency in Petroleum Products):** Documents that India's domestic refining capacity provides >100% self-sufficiency in petrol, diesel, and jet fuel, but ~40% self-sufficiency in LPG. This aligns with our finding of an LPG net trade deficit of $-20.12\text{ MMT}$ and gross export of $52.6\text{ MMT}$ of clean transport fuels.
3. **Statewise Sales Benchmark (`1787137273_Statewise_Sales-POL_Consumption_Final.xlsx`):** The discovered footnote on Row 57 explains why state dispatches sum to $207.5\text{ MMT}$ while All India Total is $234.3\text{ MMT}$. The missing $26.8\text{ MMT}$ is confirmed to represent direct bulk imports by private industrial consumers and non-allocated SEZ sales.

---

## 7. Strategic Bridge to Phase 6

Phase 5 has demonstrated that while India has achieved physical refining self-sufficiency in automotive fuels, it remains severely exposed to:
1. **Crude Oil Feedstock Import Dependency:** Evaluated in Phase 4 at 88.2% in FY 2023–24.
2. **LPG Direct Product Import Dependency:** Evaluated in Phase 5 at 62.4% in FY 2023–24.

Phase 6 will link these physical volumes with international FOB price benchmarks and customs valuation data (`1751964547_PT_IMPORT_TMT_H.xlsx`, `crude_oil_fob_price_indian_basket.csv`, and `annual_petroleum_import_export_values.csv`) to decompose India's **import expenditure, foreign exchange burden, price pass-through, and net fiscal exposure**.
