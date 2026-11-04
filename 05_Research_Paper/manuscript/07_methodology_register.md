# Comprehensive Methodology Register and Analytical Framework

**Document Reference:** `05_Research_Paper/manuscript/07_methodology_register.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption (FY98–FY24)*  
**Date:** November 2026  
**Status:** Phase 9 Preparation Output  
**Structure Alignment:** Prepared directly for **Section 3 (Method)** of the Professor's Journal Template.

---

## Overview and Methodological Philosophy

This document formalizes the complete methodology, analytical equations, data harmonization protocols, and econometric specifications governing the empirical research paper. The research adheres strictly to transparent, reproducible, and verifiable quantitative methods. All empirical calculations are grounded in official administrative data from the Ministry of Petroleum and Natural Gas (MoPNG), Petroleum Planning & Analysis Cell (PPAC), Directorate General of Commercial Intelligence and Statistics (DGCI&S), and Reserve Bank of India (RBI).

The method is structured into nine formal numbered subsections designed to map directly into **Section 3 (Method)** of the manuscript.

---

## 3.1 Data Acquisition and Multi-Source Auditing Architecture

### 3.1.1 Primary Administrative Sources
The study integrates primary administrative time series across four authoritative government and multilateral reporting tiers:
1. **Ministry of Petroleum and Natural Gas (MoPNG), Government of India:** Annual editions of *Indian Petroleum & Natural Gas Statistics* (IPNGS), covering long-run historical series from FY1997–98 through FY2023–24.
2. **Petroleum Planning & Analysis Cell (PPAC), MoPNG:** Official monthly and annual snapshot reports, historical data sheets (*Petroleum Snapshot*, *Historical Petroleum Data 2023–24*), and consumption registers.
3. **Directorate General of Commercial Intelligence and Statistics (DGCI&S), Ministry of Commerce & Industry:** Foreign trade data registers containing customs-cleared petroleum crude and petroleum product import/export values and physical volumes.
4. **Reserve Bank of India (RBI):** *Handbook of Statistics on the Indian Economy*, supplying official reference foreign exchange rates (INR/USD) and macroeconomic deflators.

### 3.1.2 Audit Hierarchy and Triangulation
Data ingestion followed a strict source verification protocol:
- Every data point was audited against primary physical workbooks and official PDF statistical reports.
- Discrepancies between MoPNG annual summaries and PPAC monthly aggregates were reconciled using the official revised historical series published in the latest available MoPNG IPNGS report.
- Provisional values (e.g., FY24 preliminary flash estimates) were cross-validated against finalized end-of-year audit figures.

---

## 3.2 Harmonization, Time-Basis Calibration, and Unit Standardization

### 3.2.1 Accounting Period Harmonization
All primary data series were harmonized to the **Indian Fiscal Year (FY)** basis, which runs from **April 1 through March 31**:
$$\text{FY}_t \equiv \text{April 1, Year } (t-1) \text{ to March 31, Year } t$$
For example, FY24 represents the twelve-month period from April 1, 2023 to March 31, 2024. Monthly data were aggregated strictly within financial year boundaries to eliminate calendar-year mismatch errors.

### 3.2.2 Physical and Monetary Unit Standardization
Primary sources record petroleum flows and values in disparate units. The dataset standardizes all observations into standardized physical and financial metrics:
- **Physical Quantities:** Standardized to **Million Metric Tonnes (MMT)** and **Thousand Metric Tonnes (TMT)**:
  $$1 \text{ MMT} = 1,000 \text{ TMT} = 10^6 \text{ Metric Tonnes} = 10^9 \text{ kg}$$
- **Domestic Monetary Values:** Standardized to **Indian Rupees Crore (INR Cr)**:
  $$1 \text{ Crore} = 10^7 \text{ INR} = 10 \text{ Million INR}$$
- **International Monetary Values:** Standardized to **United States Dollars Million (USD M)** and **Billion (USD B)**:
  $$1 \text{ USD Billion} = 1,000 \text{ USD Million} = 10^9 \text{ USD}$$

### 3.2.3 Exchange Rate and Implied Currency Conversion
When bilateral transaction values were reported in both currencies, the implied annual transaction exchange rate ($IER_t$) was derived to ensure absolute internal accounting consistency:
$$\text{IER}_t = \frac{\text{Value}_{\text{INR}, t} \times 10^7}{\text{Value}_{\text{USD}, t} \times 10^6} = \frac{\text{Value}_{\text{INR}, t} \times 10}{\text{Value}_{\text{USD}, t}} \quad (\text{INR/USD})$$
This implied rate was verified against the official RBI annual average reference rate to detect customs timing differentials or exchange rate lag distortions.

---

## 3.3 Physical Mass-Balance and Energy Flow Accounting

The physical supply chain is modeled as a mass-conserving flow system with distinct transformation stages:

```
+----------------------------------------------------------------------------------------------------+
|                                PHYSICAL HYDROCARBON MASS-BALANCE                                    |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  [Domestic Crude Extraction] (P_t) + [Crude Imports] (M_c,t) - [Stock Change / Stock Loss]          |
|                                         |                                                          |
|                                         v                                                          |
|                            [Refinery Throughput] (R_t)                                             |
|                                         |                                                          |
|                                         v (Refining Transformation: Yield Y_i + Loss L_t)          |
|                                                                                                    |
|                       [Total Domestic Product Output] (Q_p,t)                                      |
|                                         |                                                          |
|            +----------------------------+----------------------------+                             |
|            |                                                         |                             |
|            v                                                         v                             |
|  [Domestic Consumption] (C_t)                           [Net Product Trade Balance] (NPT_t)        |
|  = Sum(C_i,t)                                           = [Exports] (X_p,t) - [Imports] (M_p,t)    |
|                                                                                                    |
+----------------------------------------------------------------------------------------------------+
```

### 3.3.1 Crude Feedstock Mass Balance
Total crude oil availability at refinery gates ($A_{c,t}$) in year $t$ is governed by:
$$A_{c,t} = P_{c,t} + M_{c,t} - X_{c,t} \pm \Delta S_{c,t}$$
Where:
- $P_{c,t}$: Domestic crude oil extraction (MMT). Note: India does not export crude oil ($X_{c,t} = 0$).
- $M_{c,t}$: Gross crude oil imports (MMT).
- $\Delta S_{c,t}$: Net stock build/draw and pipeline inventory adjustments (MMT).
- Under steady-state operations, refinery crude processing throughput ($R_t$) equals total availability less refining stock variance: $R_t \approx P_{c,t} + M_{c,t} - \Delta S_{c,t}$.

### 3.3.2 Refinery Yield Transformation
Refineries process crude throughput into refined products subject to processing mass balance:
$$Q_{p,t} = \sum_{i=1}^{k} Q_{i,t} = R_t \times (1 - \lambda_t)$$
Where:
- $Q_{i,t}$: Domestic production of individual petroleum product $i$ (e.g., LPG, Petrol, Diesel, Kerosene, ATF, Naphtha, Fuel Oil, Bitumen).
- $\lambda_t$: Refinery processing fuel and loss (RFL) fraction, historically averaging $6.5\%\text{ to }7.8\%$ by weight.
- Product-specific refinery yield fraction is: $y_{i,t} = \frac{Q_{i,t}}{R_t}$.

### 3.3.3 Net Petroleum Product Trade Balance
For the refined product sector as a whole, and for each individual product $i$:
$$\text{NPT}_t = X_{p,t} - M_{p,t}$$
$$\text{NPT}_{i,t} = X_{i,t} - M_{i,t}$$
Where:
- $X_{p,t}$: Total petroleum product exports (MMT).
- $M_{p,t}$: Total petroleum product imports (MMT).
- $\text{NPT}_t > 0$ indicates a net export surplus; $\text{NPT}_t < 0$ indicates a net import deficit.

---

## 3.4 Growth and Instability Metrics (CAGR and Trend Fitting)

### 3.4.1 Compound Annual Growth Rate (CAGR)
Long-run multi-decadal growth trajectories are evaluated using the compound annual growth rate across the span $n = t_k - t_0$ years:
$$\text{CAGR}_{t_0, t_k}(X) = \left( \frac{X_{t_k}}{X_{t_0}} \right)^{\frac{1}{t_k - t_0}} - 1$$
Where:
- $X_{t_0}$: Baseline value in financial year $t_0$ (FY98).
- $X_{t_k}$: Terminal value in financial year $t_k$ (FY24).
- $n = 26$ years.

### 3.4.2 Log-Linear Trend Estimation
To prevent sensitivity to anomalous baseline or terminal endpoint years (e.g., pandemic disruptions), continuous growth rates are estimated via log-linear ordinary least squares (OLS) regression:
$$\ln(X_t) = \alpha + \beta \cdot t + \varepsilon_t$$
Where:
- $t$: Time index ($t = 1, 2, \dots, T$).
- The continuous exponential growth rate is given by $g = e^{\beta} - 1 \approx \beta$.
- $R^2$ of the regression indicates trajectory stability.

---

## 3.5 Supply-Chain Structural Indicators

To quantify structural exposure, the study formulates four distinct supply-chain metrics:

### 3.5.1 Crude Oil Import Dependency Ratio (Throughput-Based)
In accordance with official MoPNG/PPAC definitions, India's crude import dependency ($\text{CID}_t$) measures the share of refinery throughput fed by imported crude feedstock:
$$\text{CID}_t = \left( \frac{M_{c,t}}{R_t} \right) \times 100 \quad (\%)$$
*Alternative Self-Sufficiency Definition:*
$$\text{SS}_t = \left( \frac{P_{c,t}}{R_t} \right) \times 100 = 100 - \text{CID}_t \quad (\%)$$

### 3.5.2 Physical Upstream Feedstock Deficit Gap
The absolute physical gap ($\Delta_{\text{upstream}, t}$) between domestic crude processing requirements and domestic wellhead extraction:
$$\Delta_{\text{upstream}, t} = R_t - P_{c,t} \quad (\text{MMT})$$
This metric isolates the physical volume of hydrocarbon deficit that must be bridged via international crude logistics.

### 3.5.3 Product-Level Apparent Consumption and Self-Sufficiency
Apparent domestic consumption ($C_{i,t}$) for petroleum product $i$ is calculated from physical mass balance:
$$C_{i,t} = Q_{i,t} + M_{i,t} - X_{i,t} - \Delta S_{i,t}$$
Where $\Delta S_{i,t}$ is the net stock change at marketing installations.

The product-specific import dependency ratio ($\text{PID}_{i,t}$) is defined as net imports relative to domestic consumption:
$$\text{PID}_{i,t} = \left( \frac{M_{i,t} - X_{i,t}}{C_{i,t}} \right) \times 100 \quad (\%)$$
If $\text{PID}_{i,t} < 0$, the country is a net exporter of product $i$, with an export surplus ratio equal to $|\text{PID}_{i,t}|$.

### 3.5.4 Refining Coverage Ratio
The ratio of domestic refinery product output to total domestic product consumption:
$$\text{RCR}_t = \left( \frac{Q_{p,t}}{C_t} \right) \times 100 \quad (\%)$$
A ratio exceeding $100\%$ indicates domestic refining self-sufficiency, meaning domestic refineries produce more finished products than the domestic economy consumes.

---

## 3.6 Econometric Specifications and Robustness Protocols

### 3.6.1 Stationarity and Cointegration Testing
Prior to regression estimation, time series were evaluated for stationarity:
1. **Augmented Dickey-Fuller (ADF) Test:** Tests for the presence of a unit root in levels and first differences:
   $$\Delta Y_t = \mu + \gamma Y_{t-1} + \sum_{j=1}^{p} \psi_j \Delta Y_{t-j} + e_t$$
   Null hypothesis $H_0: \gamma = 0$ (non-stationary / unit root).
2. **First-Difference Correlation:** To prevent spurious correlation between trending series, correlations are computed on both raw levels ($r_{X, Y}$) and first differences ($r_{\Delta X, \Delta Y}$):
   $$\Delta X_t = X_t - X_{t-1}, \quad \Delta Y_t = Y_t - Y_{t-1}$$

### 3.6.2 Newey-West HAC Time-Series Regressions
To account for potential heteroskedasticity and arbitrary autocorrelation in annual time-series residuals, all linear regressions employ the **Newey-West Heteroskedasticity and Autocorrelation Consistent (HAC)** covariance estimator:
$$Y_t = \beta_0 + \beta_1 X_{1,t} + \dots + \beta_k X_{k,t} + \varepsilon_t$$
$$\widehat{\text{Var}}(\hat{\beta}) = (X'X)^{-1} \hat{\Omega}_{\text{HAC}} (X'X)^{-1}$$
$$\hat{\Omega}_{\text{HAC}} = \hat{\Gamma}_0 + \sum_{v=1}^{m} \left( 1 - \frac{v}{m+1} \right) (\hat{\Gamma}_v + \hat{\Gamma}_v')$$
Where:
- $\hat{\Gamma}_v = \sum_{t=v+1}^{T} e_t e_{t-v} x_t x_{t-v}'$.
- Lag truncation parameter $m = \lfloor 4 \cdot (T / 100)^{2/9} \rfloor \approx 2\text{ to }3$ lags for $T = 26$.
- Standard errors, $t$-statistics, and $p$-values are reported with full HAC adjustments.

### 3.6.3 Elasticity Formulation
Log-log econometric models are estimated to determine structural supply-chain elasticities:
$$\ln(\text{Crude Imports}_t) = \alpha_0 + \alpha_1 \ln(\text{Refinery Throughput}_t) + \alpha_2 \ln(\text{Domestic Production}_t) + \varepsilon_t$$
$$\ln(\text{Consumption}_t) = \gamma_0 + \gamma_1 \ln(\text{Real GDP}_t) + \gamma_2 \ln(\text{Crude Price}_t) + \nu_t$$
Where coefficients directly represent constant elasticities: $\alpha_1 = \frac{\partial \ln(M_c)}{\partial \ln(R)}$.

---

## 3.7 Index Decomposition Analysis (LMDI)

To decompose changes in India's aggregate petroleum import expenditure into physical, price, and currency drivers, the study deploys the **Logarithmic Mean Divisia Index (LMDI-I)** formulation established by **Ang (2004, 2015)**.

### 3.7.1 Import Expenditure Factorization
Aggregate import expenditure in Indian Rupees ($V_{\text{INR}, t}$) is factorized as the product of three distinct structural drivers:
$$V_{\text{INR}, t} = Q_t \times P_{\text{USD}, t} \times E_t$$
Where:
- $Q_t$: Physical import quantity (MMT).
- $P_{\text{USD}, t}$: Average import unit value in foreign currency (USD/MT).
- $E_t$: Effective exchange rate (INR/USD).

### 3.7.2 Logarithmic Weight Function
The logarithmic mean weight between base year 0 and target year $T$ is defined as:
$$L(V_T, V_0) = \begin{cases} 
\frac{V_T - V_0}{\ln(V_T) - \ln(V_0)} & \text{if } V_T \neq V_0 \\ 
V_0 & \text{if } V_T = V_0 
\end{cases}$$

### 3.7.3 Additive LMDI-I Decomposition
The absolute change in import expenditure ($\Delta V_{\text{tot}} = V_T - V_0$) is decomposed into three additive components leaving zero unexplained residual:
$$\Delta V_{\text{tot}} = \Delta V_Q + \Delta V_P + \Delta V_E$$
Where:
$$\Delta V_Q = L(V_T, V_0) \cdot \ln\left( \frac{Q_T}{Q_0} \right) \quad \text{[Physical Quantity Effect]}$$
$$\Delta V_P = L(V_T, V_0) \cdot \ln\left( \frac{P_{\text{USD}, T}}{P_{\text{USD}, 0}} \right) \quad \text{[International Dollar Price Effect]}$$
$$\Delta V_E = L(V_T, V_0) \cdot \ln\left( \frac{E_T}{E_0} \right) \quad \text{[Currency Depreciation / Exchange Rate Effect]}$$

### 3.7.4 Multiplicative LMDI-I Decomposition
Similarly, the proportional index change ($D_{\text{tot}} = \frac{V_T}{V_0}$) is multiplicatively decomposed into factor ratios:
$$D_{\text{tot}} = D_Q \times D_P \times D_E$$
Where:
$$D_Q = \exp\left( \frac{L(V_T, V_0)}{V_{\text{tot}}^*} \ln\left( \frac{Q_T}{Q_0} \right) \right)$$
$$D_P = \exp\left( \frac{L(V_T, V_0)}{V_{\text{tot}}^*} \ln\left( \frac{P_{\text{USD}, T}}{P_{\text{USD}, 0}} \right) \right)$$
$$D_E = \exp\left( \frac{L(V_T, V_0)}{V_{\text{tot}}^*} \ln\left( \frac{E_T}{E_0} \right) \right)$$
Where $V_{\text{tot}}^* = L(V_T, V_0) \sum \ln(\cdot)$, satisfying perfect factor reversal ($D_{\text{tot}} = D_Q \cdot D_P \cdot D_E$).

---

## 3.8 Validation Hierarchy and Cross-Verification Framework

To ensure that every numerical claim in the manuscript meets publication standards, an empirical validation hierarchy was established:

```
+----------------------------------------------------------------------------------------------------+
|                                    DATA VALIDATION HIERARCHY                                       |
+----------------------------------------------------------------------------------------------------+
|  LEVEL 1: Primary Administrative Record (MoPNG IPNGS Annual / PPAC Official Gazette)               |
|           Highest evidentiary weight; audited historical series.                                  |
|                                                                                                    |
|  LEVEL 2: Cross-Agency Triangulation (DGCI&S Customs Trade Data vs PPAC Marketing Reports)         |
|           Reconciles trade volume vs marketing dispatch; confirms import bills within < 1.5% delta.|
|                                                                                                    |
|  LEVEL 3: Multilateral External Benchmarking (IEA World Energy Balances, OPEC ASB, EI Review)       |
|           External validation of gross trends, refinery capacity rankings, and global trade shares.|
+----------------------------------------------------------------------------------------------------+
```

All 23 core empirical findings reported in the paper have undergone Level 1 and Level 2 audit verification, with exact source workbooks, worksheet names, and cell coordinates registered in `02_results_evidence_register.csv`.

---

## 3.9 Methodological Disclosures and Boundaries

To maintain rigorous academic integrity, three explicit boundary conditions and data treatments are disclosed:

1. **Lease Condensate Accounting Disclosure:**  
   In Indian official reporting (MoPNG/PPAC), domestic crude oil production figures include lease condensate extracted alongside natural gas at field gathering stations. Plant condensate and refinery natural gas liquids (NGL) are accounted for separately. The 26-year domestic crude production series reflects this standard MoPNG accounting definition throughout.

2. **Biofuel and Ethanol Blending Boundary:**  
   Under India's Ethanol Blended Petrol (EBP) program, ethanol blending in motor gasoline escalated from negligible levels pre-2014 to over 10% in FY23 and approximately 12–14% in FY24. In the core petroleum dataset, refinery throughput and motor spirit production represent pure hydrocarbon flows from refineries. Downstream ethanol blending conducted by Oil Marketing Companies (OMCs) at storage terminals is acknowledged as an offset to retail gasoline demand, but does not alter refinery gate crude processing statistics.

3. **Non-Causality and Structural Correlation Disclosure:**  
   Regression relationships between domestic crude production, refinery throughput, and crude imports are reported as structural empirical correlations and supply-chain elasticities, not as structural vector autoregressive (SVAR) causal identifications. The near-zero correlation between domestic production and imports ($r = 0.096$) is interpreted as proof of statistical decoupling and lack of crowding-out, rather than an structural exogeneity proof.
