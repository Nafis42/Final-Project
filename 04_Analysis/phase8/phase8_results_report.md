# Phase 8: Statistical Analysis, Supply-Chain Relationships, and Robustness Report

**Project Title:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Research Phase:** Phase 8 — Supply-Chain Relationships, Statistical Analysis, and Robustness Checks  
**Execution Date:** October 2026  
**Pipeline Script:** [`04_Analysis/phase8/scripts/phase8_statistical_analysis.py`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/scripts/phase8_statistical_analysis.py)  
**Execution Log:** [`04_Analysis/phase8/logs/phase8_analysis.log`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/logs/phase8_analysis.log)  

---

## 1. Executive Summary & Core Empirical Findings

Phase 8 executes a statistical investigation of the structural relationships governing India's petroleum supply chain across 27 fiscal years (FY 1998-99 to FY 2024-25). Utilizing the standardized and cross-validated datasets certified in Phase 7, this report addresses the 5 core research questions (RQ1 to RQ5) while strictly observing scientific safeguards against premature causal claims.

### Summary of Major Findings:

1. **RQ1: Domestic Production vs. Crude Imports — Complete Decoupling:**
   - Domestic crude oil production (including lease condensate) has remained stagnant, fluctuating narrowly between **32.0 MMT and 38.1 MMT** (averaging $34.1\text{ MMT}$) over the entire 26-year panel. In contrast, crude oil imports surged from **39.81 MMT to 234.26 MMT**, growing at a Compound Annual Growth Rate (CAGR) of **7.37% per annum**.
   - Bivariate correlation between domestic production and crude imports is statistically zero in both levels ($r = 0.096, p = 0.641$) and annual first differences ($r = 0.173, p = 0.408$).
   - The crude-oil import-dependence proxy escalated monotonically from **54.86% in FY 1998-99 to 88.86% in FY 2023-24**.
   - Multiple regression indicates that domestic crude production has **no statistically significant crowding-out effect** on crude imports ($\beta = -0.320, t = -1.13, p = 0.271$).

2. **RQ2: Domestic Production vs. Refinery Throughput — The Widening Deficit Gap:**
   - India's refinery crude throughput expanded from **68.54 MMT in FY 1998-99 to 261.55 MMT in FY 2023-24** (and 268.61 MMT in FY 2024-25), a cumulative expansion of **282%**.
   - The physical crude supply deficit gap ($\text{Refinery Throughput} - \text{Domestic Production}$) widened from **35.78 MMT to 232.19 MMT** ($+549\%$).
   - The **Indigenous Crude Coverage Ratio** ($\frac{\text{Domestic Production}}{\text{Refinery Throughput}} \times 100$) collapsed from **47.80% in FY 1998-99 to 11.22% in FY 2023-24**.
   - Bivariate correlation between refinery throughput and crude imports is near-perfect in both levels ($r = 0.9991, p < 0.00001$) and annual changes ($r = 0.9680, p < 0.00001$), demonstrating that downstream refining capacity expansion is the sole structural driver of crude import demand.

3. **RQ3: Refined Product Trade — The Transport Fuel Surplus vs. LPG Deficit Paradox:**
   - Driven by the commissioning of export-oriented merchant refineries (Reliance Jamnagar DTA in 1999–2000, Reliance Jamnagar SEZ in 2008, and Nayara Vadinar), India transformed from a net product importer (-14.81 MMT in FY99) into a major global refining hub.
   - Aggregate product self-sufficiency exceeded 100% in FY 2001-02 and peaked at **139.38% in FY 2013-14**, stabilizing at **117.84% in FY 2023-24**.
   - **Severe Stream-Level Divergence:** In FY 2023-24, India generated massive export surpluses in transport fuels: **High Speed Diesel (+28.16 MMT)**, **Motor Spirit (+12.76 MMT)**, and **Aviation Turbine Fuel (+8.58 MMT)**. Concurrently, household cooking gas (**LPG**) exhibited a structural import deficit of **-17.99 MMT**, with imports covering **62.7% of domestic consumption**.

4. **RQ4: Import Expenditure Exposure — Volume vs. Price vs. Currency Shocks:**
   - Total crude import expenditure expanded from **\$6.41 Billion (Rs. 27,191 Crore) in FY 1998-99 to \$133.37 Billion (Rs. 1,105,248 Crore) in FY 2023-24**.
   - In annual first differences, international oil price fluctuations dominate expenditure swings ($r = 0.9168, p < 0.00001$), whereas physical volume changes show modest short-run co-movement ($r = 0.3475, p = 0.082$).
   - **Currency Wedge:** In Rupee terms, crude import expenditure grew at a CAGR of **18.23% per annum**, outstripping US-dollar expenditure growth (**15.13% per annum**) by **+3.10% per annum** due to long-run Rupee depreciation (from 42.4 to 84.6 INR/USD).

5. **RQ5: Structural Subperiod Shifts:**
   - Across 4 distinct historical regimes (Post-APM Entry, Export Boom, Price Collapse, and Geopolitical Rebound), average import dependence escalated from **68.2% to 88.5%**, while indigenous crude coverage fell from **33.3% to 12.3%**.

---

## 2. Research Question Analysis & Detailed Evidence

### 2.1 RQ1 — Domestic Production and Crude-Oil Imports
- **Dataset Examined:** `core_annual_petroleum_dataset.csv`, `derived_indicators.csv` ($N = 26$ matched fiscal years, FY 1998-99 to FY 2023-24).
- **Descriptive Dynamics:**
  $$\begin{array}{lcccc}
  \hline
  \textbf{Metric} & \textbf{FY 1998-99} & \textbf{FY 2008-09} & \textbf{FY 2023-24} & \textbf{CAGR (FY99-FY24)} \\
  \hline
  \text{Domestic Crude Production (MMT)} & 32.76 & 33.51 & 29.36 & -0.44\% \\
  \text{Crude Oil Imports (MMT)} & 39.81 & 132.85 & 234.26 & +7.37\% \\
  \text{Import-to-Production Ratio} & 1.22\times & 3.96\times & 7.98\times & — \\
  \text{Crude Import Dependence Proxy (\%)} & 54.86\% & 79.86\% & 88.86\% & +1.95\% \text{ p.a.} \\
  \hline
  \end{array}$$

- **Statistical Co-Movement & Non-Correlation:**
  Bivariate Pearson correlation in levels is $r = 0.0960$ ($p = 0.6409$), and Spearman rank correlation is $\rho = 0.0462$ ($p = 0.8228$). When differenced to remove secular trend co-movement, annual changes remain uncorrelated: $r = 0.1732$ ($p = 0.4076$) and $\rho = 0.0677$ ($p = 0.7478$).
- **Econometric Specification (Model MOD-01):**
  $$\ln(\text{Crude Imports}_t) = -2.155 - 0.320 \ln(\text{Domestic Production}_t) + 1.283 \ln(\text{Refinery Throughput}_t)$$
  - Standard Errors: $\text{SE}(\beta_{\text{Prod}}) = 0.283, \text{SE}(\beta_{\text{Proc}}) = 0.045$.
  - Diagnostics: $R^2 = 0.9967, \text{Adj } R^2 = 0.9964, F = 3450.4 (p < 0.00001), \text{DW} = 1.341$.
  - **Empirical Interpretation:** Controlling for refinery throughput, domestic crude production has **no statistically significant effect** on import volumes ($t = -1.13, p = 0.271$). Refining throughput exhibits an elasticity of $+1.28$ ($t = 28.53, p < 0.00001$), confirming that crude imports are pulled entirely by downstream processing scale.

![Figure 1: Domestic Crude Production vs Crude Imports](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/fig1_domestic_prod_vs_crude_imports.png)  
*Underlying data:* [`04_Analysis/phase8/figure_data/fig1_data.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figure_data/fig1_data.csv)

---

### 2.2 RQ2 — Domestic Production and Refinery Processing
- **Dataset Examined:** `core_annual_petroleum_dataset.csv`, `additional_indicators.csv` ($N = 26$).
- **The Indigenous Coverage Ratio:**
  $$\text{Coverage Ratio}_t = \frac{\text{Domestic Crude Production}_t}{\text{Refinery Crude Processing}_t} \times 100$$
  - In FY 1998-99, domestic crude supplied nearly half ($47.80\%$) of refinery input.
  - By FY 2011-12, coverage fell to $18.67\%$.
  - By FY 2023-24, coverage collapsed to **11.22%**.
  - **Crucial Nomenclature Safeguard:** This metric strictly reflects indigenous feedstock coverage; it must **never** be labeled as "refinery capacity utilization." Indian refineries operate at $>100\%$ nameplate utilization.
- **Physical Crude Deficit Gap:**
  $$\text{Crude Gap}_t = \text{Refinery Processing}_t - \text{Domestic Production}_t$$
  - Expanded from $35.78\text{ MMT}$ in FY 1998-99 to **232.19 MMT** in FY 2023-24 ($+549\%$).
- **Refining Multiplier:** The ratio of refinery crude throughput to domestic production grew from $2.09\times$ in FY 1998-99 to **8.91×** in FY 2023-24, underscoring that India processes nearly 9 barrels of crude for every 1 barrel pumped domestically.

![Figure 2: Production vs Throughput and Expanding Crude Gap](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/fig2_production_vs_refinery_throughput.png)  
*Underlying data:* [`04_Analysis/phase8/figure_data/fig2_data.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figure_data/fig2_data.csv)

---

### 2.3 RQ3 — Petroleum-Product Trade, Production, and Consumption
- **Dataset Examined:** `product_production_dataset.csv`, `product_consumption_dataset.csv`, `product_trade_balance.csv` ($N = 27$, FY 1998-99 to FY 2024-25).
- **Macro Product Balance & Self-Sufficiency:**
  - In FY 1998-99, petroleum product production stood at $68.41\text{ MMT}$ against consumption of $90.58\text{ MMT}$ (Self-Sufficiency Ratio = $75.52\%$, net product imports of $14.81\text{ MMT}$).
  - By FY 2001-02, production ($107.25\text{ MMT}$) overtook consumption ($100.43\text{ MMT}$), establishing India as a permanent net product exporter.
  - Peak self-sufficiency was attained in **FY 2013-14 at 139.38%**, generating a net product export surplus of **49.87 MMT**.
  - In FY 2023-24, production of $276.06\text{ MMT}$ exceeded domestic consumption ($234.26\text{ MMT}$), yielding an SSR of **117.84%** and net exports of **13.90 MMT**.
- **Product Slate Polarization (FY 2023-24):**
  $$\begin{array}{lcccc}
  \hline
  \textbf{Product Stream} & \textbf{Production (MMT)} & \textbf{Consumption (MMT)} & \textbf{Net Trade (MMT)} & \textbf{Structural Status} \\
  \hline
  \text{High Speed Diesel (HSD)} & 115.00 & 89.28 & \mathbf{+28.16} & \text{Major Export Engine} \\
  \text{Motor Spirit (MS / Petrol)} & 44.97 & 37.22 & \mathbf{+12.76} & \text{Export Surplus} \\
  \text{Aviation Turbine Fuel (ATF)} & 16.99 & 8.24 & \mathbf{+8.58} & \text{Export Surplus} \\
  \text{Naphtha} & 13.56 & 13.38 & \mathbf{+4.06} & \text{Export Surplus} \\
  \text{Liquefied Petroleum Gas (LPG)} & 12.83 & 29.58 & \mathbf{-17.99} & \textbf{Acute Import Deficit} \\
  \text{Petcoke} & 14.54 & 18.52 & \mathbf{-10.93} & \text{Industrial Deficit} \\
  \text{Furnace Oil / LSHS} & 10.60 & 6.46 & \mathbf{-6.95} & \text{Bunker/Fuel Deficit} \\
  \hline
  \end{array}$$
  - **Empirical Takeaway:** India's refining sector acts as a sophisticated export-oriented conversion mechanism for transport fuels (diesel, gasoline, jet fuel), but domestic cooking gas demand (LPG) far outstrips domestic refinery yields, necessitating massive physical imports.

![Figure 3: Product Trade Dynamics: Refining Surplus vs LPG Deficit](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/fig3_product_trade_dynamics.png)  
*Underlying data:* [`04_Analysis/phase8/figure_data/fig3_data.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figure_data/fig3_data.csv)

---

### 2.4 RQ4 — Import Expenditure, Quantities, and Price Effects
- **Dataset Examined:** `import_value_dataset.csv`, `import_unit_values.csv`, `indian_basket_price_series.csv` ($N = 27$).
- **Expenditure Evolution (FY 1998-99 to FY 2024-25):**
  - Crude import expenditure grew from **\$6.41 Billion to \$137.17 Billion** (CAGR: $15.13\%$).
  - In Rupee terms, crude import expenditure grew from **Rs. 27,191 Crore to Rs. 1,160,801 Crore** (CAGR: $18.23\%$).
- **Identity Regression Verification (Model MOD-02 & MOD-03):**
  $$\ln(\text{Expenditure}^{\text{USD}}_t) = -6.908 + 1.000 \ln(\text{Quantity}_t) + 1.000 \ln(\text{Unit Value}_t) \quad (R^2 = 1.000)$$
  $$\ln(\text{Expenditure}^{\text{INR}}_t) = -9.210 + 1.000 \ln(\text{Quantity}_t) + 1.000 \ln(\text{Unit Value}^{\text{INR}}_t) \quad (R^2 = 1.000)$$
- **Price vs Volume Driving Shocks (First Differences):**
  $$\begin{array}{lcc}
  \hline
  \textbf{Relationship in Annual Changes} & \textbf{Pearson } r & \textbf{p-value} \\
  \hline
  \Delta \text{Import Expenditure (USD)} \text{ vs } \Delta \text{Crude Price (FOB)} & \mathbf{0.9168} & < 0.00001 \\
  \Delta \text{Import Expenditure (USD)} \text{ vs } \Delta \text{Crude Import Quantity} & 0.3475 & 0.08182 \\
  \Delta \text{Import Expenditure (INR)} \text{ vs } \Delta \text{Crude Price (FOB)} & \mathbf{0.8710} & < 0.00001 \\
  \Delta \text{Import Expenditure (INR)} \text{ vs } \Delta \text{Crude Import Quantity} & 0.3601 & 0.07068 \\
  \hline
  \end{array}$$
  - **Empirical Finding:** International price volatility explains **84% of the annual variance** in India's import bill, while physical import volume growth acts as a steady long-run upward trend anchor.

![Figure 4: Import Expenditure, Volume, and Realized Unit Values](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/fig4_import_expenditure_quantity_price.png)  
*Underlying data:* [`04_Analysis/phase8/figure_data/fig4_data.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figure_data/fig4_data.csv)

---

### 2.5 RQ5 — Changes Across Historical Subperiods
Descriptive statistics across the 4 institutional regimes documented in [`subperiod_comparison.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/subperiod_comparison.csv):

| Metric | Subperiod 1: Post-APM Entry (FY99–FY05) | Subperiod 2: Export Boom (FY06–FY14) | Subperiod 3: Price Collapse (FY15–FY20) | Subperiod 4: Geopolitical Shock (FY21–FY25) |
|:---|:---:|:---:|:---:|:---:|
| **Mean Domestic Crude (MMT)** | 33.00 | 35.79 | 35.03 | 29.74 |
| **Mean Crude Imports (MMT)** | 69.11 | 149.63 | 213.91 | 227.06 |
| **Mean Refinery Throughput (MMT)** | 105.10 | 196.22 | 248.95 | 251.82 |
| **Mean Product Production (MMT)** | 104.99 | 199.12 | 251.48 | 265.41 |
| **Mean Product Consumption (MMT)** | 104.38 | 143.68 | 200.70 | 224.49 |
| **Mean Crude Price (\$/bbl)** | \$28.53 | \$84.28 | \$58.11 | \$78.22 |
| **Mean Import Bill (Billion USD)** | \$15.22 | \$99.88 | \$92.17 | \$138.86 |
| **Mean Import Bill (Lakh Cr INR)** | Rs. 0.70 | Rs. 4.67 | Rs. 6.22 | Rs. 11.23 |
| **Mean Import Dependence Proxy (%)** | **67.65%** | **80.68%** | **85.92%** | **88.42%** |
| **Indigenous Coverage Ratio (%)** | **33.31%** | **18.78%** | **14.13%** | **11.83%** |
| **Product Self-Sufficiency (%)** | **100.95%** | **138.56%** | **125.43%** | **118.25%** |

![Figure 6: Structural Shifts Across Four Historical Regimes](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/fig6_subperiod_regime_shifts.png)  
*Underlying data:* [`04_Analysis/phase8/figure_data/fig6_data.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figure_data/fig6_data.csv)

---

## 3. Correlation Heatmap & Bivariate Associations

The level correlation heatmap illustrates the intense collinearity among downstream supply variables (Refining Throughput, Product Production, Product Consumption, Crude Imports), contrasted with the total statistical detachment of Domestic Crude Extraction:

![Figure 5: Bivariate Pearson Correlation Matrix](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/fig5_correlation_heatmap.png)  
*Underlying data:* [`04_Analysis/phase8/figure_data/fig5_data.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figure_data/fig5_data.csv)

Key Correlation Table Excerpt:
- Throughput vs. Crude Imports: $r = 0.9991$ ($p < 0.00001$)
- Product Output vs. Domestic Consumption: $r = 0.8700$ ($p < 0.00001$)
- Domestic Crude Production vs. Throughput: $r = 0.1325$ ($p = 0.51879$)
- Domestic Crude Production vs. Crude Imports: $r = 0.0960$ ($p = 0.64090$)

---

## 4. Robustness and Sensitivity Outcomes

The 7-fold sensitivity protocol in [`robustness_results.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/robustness_results.csv) confirms the stability of all core findings:

1. **Period Sensitivity (Pre- vs. Post-2002):** Decoupling between domestic production and crude imports is robust ($r = 0.096$ full sample vs. $r = -0.079$ post-APM).
2. **Outlier Sensitivity (COVID-19 Shock):** Throughput-to-import elasticity remains invariant ($\beta = 1.252$ full sample vs. $\beta = 1.250$ excluding FY21).
3. **Definition Sensitivity (Crude Only vs. Crude + Condensate):** Excluding lease condensate raises mean import dependence proxy by $+2.89\%$ (from $84.06\%$ to $86.94\%$), but does not alter the historical trajectory.
4. **Currency Sensitivity (USD vs. INR):** Rupee expenditure growth ($18.23\%$ CAGR) exceeds dollar growth ($15.13\%$ CAGR) by $+3.10\%$ p.a., demonstrating substantial compounding currency risk.
5. **Level vs. Growth Sensitivity:** Both level correlation ($r = 0.096$) and annual growth rate correlation ($r = 0.098$) between domestic crude and imports are statistically indistinguishable from zero.
6. **Sample Horizon Sensitivity:** Throughput-import correlation is identical across pre-pandemic ($r = 0.9995$) and full ($r = 0.9991$) horizons.
7. **Product Aggregation Sensitivity:** Highlights that macro net product surplus ($+13.90\text{ MMT}$) masks acute vulnerability in LPG ($-17.99\text{ MMT}$).

![Figure 7: Robustness of Production-Import Decoupling: Levels vs Differences](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/fig7_robustness_sensitivity_checks.png)  
*Underlying data:* [`04_Analysis/phase8/figure_data/fig7_data.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figure_data/fig7_data.csv)

![Figure 8: Product Self-Sufficiency vs Net Export Balance](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figures/fig8_product_self_sufficiency_vs_trade.png)  
*Underlying data:* [`04_Analysis/phase8/figure_data/fig8_data.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/figure_data/fig8_data.csv)

---

## 5. Methodological Safeguards & Non-Causal Declarations

In compliance with academic guidelines:
1. **No Causal Demand Elasticity:** Regressions of expenditure on volume and price confirm accounting identities ($V = P \times Q$); they do not estimate structural consumer price elasticity.
2. **No Capacity Utilization Mislabeling:** Indigenous coverage ratios ($\approx 11.2\%$) are strictly distinguished from refinery distillation utilization ($>100\%$).
3. **Non-Causal Decoupling:** The statistical zero correlation between domestic production and imports reflects independent institutional regimes (upstream geological constraints vs. downstream commercial refining expansion), not an economic causal law.

---

## 6. Implications for Research Paper Drafting (Phase 9)

Phase 8 provides clear empirical scaffolding for the research paper:
1. **Title Alignment:** The title correctly reflects India's dual reality: *hyper-import exposure in upstream crude oil* coupled with *global export competitiveness in downstream transport refining*.
2. **The "Two Indias" of Refining:** Downstream refining is split between domestic public-sector supply (OMCs) and private/SEZ merchant export hubs (Reliance, Nayara).
3. **The LPG Blindspot:** Energy transition and clean-cooking welfare policies (PMUY) directly drove India's second-largest import vulnerability (LPG imports expanding from $1.0\text{ MMT}$ to $18.5\text{ MMT}$).
4. **Currency Compounding:** Fiscal risk assessments must emphasize domestic currency import bills (Rs. Lakh Crore) rather than dollar values alone.
