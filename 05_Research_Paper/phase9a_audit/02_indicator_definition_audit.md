# Audit and Reconciliation of Crude Import-Dependence Indicators

**Document Reference:** `05_Research_Paper/phase9a_audit/02_indicator_definition_audit.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Phase 9A Critical Audit Output  

---

## 1. Executive Summary

A critical inconsistency in Phase 9 preparation documents was the conflation of two mathematically distinct indicators of national crude oil import vulnerability:
1. **Supply-Pool Import Share** (Imports relative to total physical crude supply pool: $\frac{\text{Imports}}{\text{Production} + \text{Imports}}$).
2. **Imports Relative to Refinery Processing Throughput** ($\frac{\text{Imports}}{\text{Refinery Throughput}}$).

This audit proves that the headline result cited throughout the project—that India's crude import dependency escalated from **54.86% in FY 1998–99 to 88.86% in FY 2023–24**—was derived exclusively from **Formula A (Supply-Pool Import Share)**. 

However, Phase 9 `07_methodology_register.md` (Section 3.5.1) erroneously defined the Crude Oil Import Dependency Ratio ($\text{CID}_t$) using **Formula B** ($\frac{M_{c,t}}{R_t} \times 100$), which actually yields **58.08% in FY 1998–99** and **89.57% in FY 2023–24**.

This document reconciles both indicators, establishes a definitive variable dictionary and formula register, and provides precise language for the final manuscript to prevent any further confusion.

---

## 2. Empirical Verification of the Competing Formulas

By testing the raw observations from `core_annual_petroleum_dataset.csv` and `derived_indicators.csv`, we observe the exact mathematical divergence between the indicators:

```
+----------------------------------------------------------------------------------------------------+
|                                      EMPIRICAL FORMULA COMPARISON                                   |
+-------------+-------------+------------+------------+----------------+---------------+-------------+
| Financial   | Domestic    | Crude      | Refinery   | Stored Proxy   | Formula A     | Formula B   |
| Year        | Production  | Imports    | Throughput | in Dataset     | (Supply-Pool) | (Imp / Ref) |
|             | (MMT)       | (MMT)      | (MMT)      | (%)            | (%)           | (%)         |
+-------------+-------------+------------+------------+----------------+---------------+-------------+
| FY 1998-99  |   32.760    |   39.808   |   68.539   |     54.86%     |    54.856%    |   58.081%   |
| FY 1999-00  |   32.000    |   57.805   |   85.709   |     64.37%     |    64.367%    |   67.443%   |
| FY 2004-05  |   34.138    |   95.861   |  124.302   |     73.74%     |    73.740%    |   77.120%   |
| FY 2009-10  |   33.398    |  159.259   |  186.562   |     82.66%     |    82.665%    |   85.365%   |
| FY 2014-15  |   37.469    |  189.435   |  223.264   |     83.49%     |    83.487%    |   84.850%   |
| FY 2019-20  |   32.169    |  226.955   |  254.386   |     87.59%     |    87.585%    |   89.217%   |
| FY 2022-23  |   29.179    |  232.700   |  255.232   |     88.86%     |    88.858%    |   91.172%   |
| FY 2023-24  |   29.356    |  234.262   |  261.546   |     88.86%     |    88.864%    |   89.568%   |
+-------------+-------------+------------+------------+----------------+---------------+-------------+
```

### Definitive Conclusion:
The reported headline escalation of **54.86% to 88.86%** is mathematically identical to **Formula A (Supply-Pool Import Share)**. Formula B (Crude Imports / Refinery Throughput) consistently produces higher ratios throughout the entire 26-year panel (starting at 58.08% and reaching 89.57% in FY24, with a peak of 91.17% in FY23).

---

## 3. Dissection of the Three Distinct Indicators

To avoid combining these indicators or using the same name for both, the research paper must clearly distinguish three separate metrics:

### Indicator 1: Crude Oil Supply-Pool Import Share ($\text{SPS}_t$)
- **Conceptual Definition:** The proportion of total physical crude oil supplied to the domestic economy that originates from foreign imports.
- **Mathematical Formula:**
  $$\text{SPS}_t = \left( \frac{M_{c,t}}{P_{c,t} + M_{c,t} - X_{c,t}} \right) \times 100 \quad (\%)$$
- **Treatment of Exports:** India does not export crude oil ($X_{c,t} = 0$). Hence, the denominator simplifies strictly to $(P_{c,t} + M_{c,t})$.
- **Baseline (FY 1998–99):** $54.86\%$
- **Terminal (FY 2023–24):** $88.86\%$
- **Total Shift:** $+34.00\text{ percentage points}$.
- **Analytical Role:** Measures macro feedstock availability risk and foreign exchange vulnerability independent of refinery operating dynamics.

### Indicator 2: Crude Imports Relative to Refinery Processing Throughput ($\text{IRR}_t$)
- **Conceptual Definition:** The volumetric ratio of crude imports to total crude oil processed by domestic refineries.
- **Mathematical Formula:**
  $$\text{IRR}_t = \left( \frac{M_{c,t}}{R_t} \right) \times 100 \quad (\%)$$
- **Baseline (FY 1998–99):** $58.08\%$
- **Terminal (FY 2023–24):** $89.57\%$ (Peak: $91.17\%$ in FY 2022–23).
- **Total Shift:** $+31.49\text{ percentage points}$.
- **Analytical Role:** Measures the reliance of domestic refinery operations on international crude logistics. 
- **Methodological Caveat:** Because refineries experience inventory changes ($\Delta S$) and process other minor non-crude feedstocks, this ratio can diverge slightly from the physical feedstock blend.

### Indicator 3: Indigenous Crude Self-Sufficiency Ratio ($\text{SSR}_t$)
- **Conceptual Definition:** The proportion of domestic refinery crude processing supplied by indigenous crude oil production.
- **Mathematical Formula:**
  $$\text{SSR}_t = \left( \frac{P_{c,t}}{R_t} \right) \times 100 \quad (\%)$$
- **Baseline (FY 1998–99):** $47.80\%$ ($32.760\text{ MMT} / 68.539\text{ MMT}$)
- **Terminal (FY 2023–24):** $11.22\%$ ($29.356\text{ MMT} / 261.546\text{ MMT}$)
- **Total Shift:** $-36.58\text{ percentage points}$.
- **Analytical Role:** Inversely tracks the erosion of domestic crude coverage relative to expanding downstream processing capacity. Note that $\text{SSR}_t + \text{IRR}_t \neq 100\%$ exactly, due to inventory variations and timing lags between port import discharge and refinery crude distillation units (CDUs).

---

## 4. Definitive Variable Dictionary and Formula Register

The following register must be adopted across all manuscript tables, equations, and text:

| Variable Code | Standardized Academic Name | Exact Mathematical Formula | Unit | Primary Data Sources | FY99 Value | FY24 Value |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: |
| $P_{c,t}$ | Domestic Crude Oil Production | Field production + Lease condensate | MMT | MoPNG IPNGS Table 1.1; PPAC | 32.760 | 29.356 |
| $M_{c,t}$ | Crude Oil Gross Imports | Customs cleared crude imports | MMT | DGCI&S Trade Data; PPAC | 39.808 | 234.262 |
| $R_t$ | Refinery Crude Processing Throughput | Total crude intake at refinery gates | MMT | MoPNG IPNGS Table 3.1; PPAC | 68.539 | 261.546 |
| $\text{SPS}_t$ | Supply-Pool Import Share | $\frac{M_{c,t}}{P_{c,t} + M_{c,t}} \times 100$ | % | Derived (`derived_indicators.csv`) | 54.86% | 88.86% |
| $\text{IRR}_t$ | Import-to-Throughput Ratio | $\frac{M_{c,t}}{R_t} \times 100$ | % | Derived (`derived_indicators.csv`) | 58.08% | 89.57% |
| $\text{SSR}_t$ | Indigenous Crude Sufficiency Ratio | $\frac{P_{c,t}}{R_t} \times 100$ | % | Derived (`derived_indicators.csv`) | 47.80% | 11.22% |

---

## 5. Standardized Manuscript Wording

To eliminate all ambiguity in the research paper, the following standardized text must be used in the Method and Results sections:

> **Recommended Manuscript Text (Method Section 3.5):**  
> *"National vulnerability to foreign crude oil supplies is evaluated using two distinct metrics. First, the **Supply-Pool Import Share** ($\text{SPS}_t$) measures the share of imported crude relative to total crude availability: $\text{SPS}_t = \frac{M_{c,t}}{P_{c,t} + M_{c,t}} \times 100$, noting that India does not export crude oil ($X_{c,t} = 0$). This metric rose from 54.86% in FY 1998–99 to 88.86% in FY 2023–24. Second, the **Import-to-Throughput Ratio** ($\text{IRR}_t$) measures crude imports relative to total refinery processing: $\text{IRR}_t = \frac{M_{c,t}}{R_t} \times 100$, rising from 58.08% to 89.57% over the same period. Concurrently, the **Indigenous Crude Sufficiency Ratio** ($\text{SSR}_t = \frac{P_{c,t}}{R_t} \times 100$) collapsed from 47.80% to 11.22%, directly illustrating how downstream refining growth outstripped indigenous production capacity."*

By strictly separating these definitions, the manuscript will adhere to the highest standard of academic precision and prevent reviewers from questioning contradictory percentages.
