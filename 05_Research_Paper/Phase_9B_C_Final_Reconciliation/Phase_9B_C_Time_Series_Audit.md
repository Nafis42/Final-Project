# Phase 9B-C — Time-Series Econometric Audit: Differencing, Stationarity Testing, and Trend Robustness

**Document Reference:** `05_Research_Paper/Phase_9B_C_Final_Reconciliation/Phase_9B_C_Time_Series_Audit.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Authoritative Phase 9B-C Time-Series Audit Deliverable  
**Underlying Data Source:** `03_Processed_Data/standardized/core_annual_petroleum_dataset.csv` (Balanced 26-Year Panel: FY 1998–99 to FY 2023–24)  

---

## 1. Executive Summary and Methodological Objective

In previous draft documentation, the first-difference regression of crude imports on refinery throughput (Model MOD-07) was repeatedly described as a *"stationary first differences model"* and cited as *"proving that differencing eliminates the secular trend."*

As established in econometric methodology (e.g., Hamilton, 1994; Wooldridge, 2010):
1. **Differencing does not automatically guarantee covariance stationarity.** An integrated process $I(1)$ becomes $I(0)$ upon first differencing only if it has a single unit root without structural breaks, fractional integration, or heteroskedastic variance regimes.
2. **Asserting stationarity requires empirical testing**, and applying unit-root tests to small annual samples ($T=25$ to $26$) entails severe power limitations.

This document formally audits the time-series properties of the supply-chain variables, reproduces MOD-07 with complete diagnostic metrics, executes Augmented Dickey-Fuller (ADF) unit-root tests across levels and first differences, documents sample limitations, and provides defensible academic phrasing for the research manuscript.

---

## 2. Reproduction of Model MOD-07 (Bivariate First Differences)

### 2.1 Model Specification
$$\Delta M_{c,t} = lpha + eta \Delta R_t + arepsilon_t$$
Where:
- $\Delta M_{c,t} = M_{c,t} - M_{c,t-1}$: Annual change in gross crude-oil imports (Million Metric Tonnes, MMT)
- $\Delta R_t = R_t - R_{t-1}$: Annual change in refinery crude processing throughput (MMT)
- Sample Period: FY 1999–2000 to FY 2023–24 ($N=25$ annual intervals derived from the 26-year balanced panel)

### 2.2 Reproduced Statistical Output

| Parameter / Statistic | Variable / Term | Estimate | Conventional OLS SE | Newey-West HAC SE (maxlags=2) | $t$-statistic (HAC) | $p$-value (HAC) | 95% Confidence Interval (HAC) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Intercept ($\hat{lpha}$)** | Constant | **+0.5164** | 0.6520 | 0.2995 | 1.724 | 0.0981 | $[-0.103, +1.136]$ |
| **Slope ($\hat{eta}$)** | $\Delta R_t$ | **+0.9406** | 0.0503 | 0.0219 | 43.028 | $< 0.0001$ | $[+0.895, +0.986]$ |

#### Model-Level Diagnostics:
- **Sample Size ($N$):** 25 annual differences
- **Coefficient of Determination ($R^2$):** **0.9382**
- **Adjusted $R^2$:** **0.9355**
- **Residual Standard Error:** **2.618 MMT**
- **Durbin-Watson Statistic:** **2.8992** (indicates mild negative first-order residual autocorrelation in differences, accounted for by HAC standard errors)
- **$F$-statistic ($1, 23$):** **349.38** ($p = 2.11 	imes 10^{-15} < 0.0001$)

### 2.3 Economic Interpretation
The estimated slope indicates that **each 1.0 MMT annual expansion in refinery crude processing throughput is associated with an incremental +0.941 MMT of crude imports in the same financial year**. Short-run annual changes in refining volume account for **93.8% of the annual variation in crude import volumes**, confirming that the relationship observed in levels is not an artifact of uncoordinated secular trending.

---

## 3. Empirical Unit-Root Testing: Augmented Dickey-Fuller (ADF)

To test the stationarity properties of the core variables, Augmented Dickey-Fuller (ADF) regressions were estimated:
$$\Delta y_t = \mu + \gamma \cdot t + (ho - 1) y_{t-1} + \sum_{i=1}^p \delta_i \Delta y_{t-i} + e_t$$
Under the null hypothesis $H_0: (ho - 1) = 0$ (the series contains a unit root / is non-stationary). The alternative hypothesis is $H_1: (ho - 1) < 0$ (the series is stationary).

Critical values for small samples ($T pprox 25$) were evaluated against Fuller (1976) / MacKinnon (1996) finite-sample response surfaces:
- **Specification with Constant ($c$):** $1\% = -3.75, \quad 5\% = -3.00, \quad 10\% = -2.63$
- **Specification with Constant and Linear Trend ($ct$):** $1\% = -4.38, \quad 5\% = -3.60, \quad 10\% = -3.24$
- **Specification with No Deterministic Terms ($nc$):** $1\% = -2.66, \quad 5\% = -1.95, \quad 10\% = -1.60$

### 3.1 ADF Test Results Matrix

| Series Tested | Transformation | Deterministic Specification | Lags ($p$) | Effective $T$ | ADF $t$-statistic | 5% Critical Value | Test Outcome ($p < 0.05$) | Inferred Time-Series Property |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Crude Imports ($M_c$)** | Levels | Constant ($c$) | 0 | 25 | **-1.587** | -3.00 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Crude Imports ($M_c$)** | Levels | Constant ($c$) | 1 | 24 | **-1.230** | -3.00 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Crude Imports ($M_c$)** | Levels | Trend ($ct$) | 0 | 25 | **-1.738** | -3.60 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Crude Imports ($M_c$)** | Levels | Trend ($ct$) | 1 | 24 | **-1.663** | -3.60 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Throughput ($R_t$)** | Levels | Constant ($c$) | 0 | 25 | **-1.634** | -3.00 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Throughput ($R_t$)** | Levels | Constant ($c$) | 1 | 24 | **-1.299** | -3.00 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Throughput ($R_t$)** | Levels | Trend ($ct$) | 0 | 25 | **-1.509** | -3.60 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Throughput ($R_t$)** | Levels | Trend ($ct$) | 1 | 24 | **-1.483** | -3.60 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Domestic Crude ($P_c$)** | Levels | Constant ($c$) | 0 | 25 | **-0.610** | -3.00 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **Domestic Crude ($P_c$)** | Levels | Trend ($ct$) | 0 | 25 | **-0.586** | -3.60 | Fail to Reject $H_0$ | Non-Stationary (Unit Root) |
| **$\Delta$ Crude Imports** | First Diff | Constant ($c$) | 0 | 24 | **-4.630** | -3.00 | **Reject $H_0$** | **Stationary $I(0)$ at 1%** |
| **$\Delta$ Crude Imports** | First Diff | Constant ($c$) | 1 | 23 | **-4.356** | -3.00 | **Reject $H_0$** | **Stationary $I(0)$ at 1%** |
| **$\Delta$ Throughput** | First Diff | Constant ($c$) | 0 | 24 | **-4.526** | -3.00 | **Reject $H_0$** | **Stationary $I(0)$ at 1%** |
| **$\Delta$ Throughput** | First Diff | Constant ($c$) | 1 | 23 | **-3.821** | -3.00 | **Reject $H_0$** | **Stationary $I(0)$ at 5%** |
| **$\Delta$ Domestic Crude** | First Diff | Constant ($c$) | 0 | 24 | **-4.064** | -3.00 | **Reject $H_0$** | **Stationary $I(0)$ at 1%** |
| **$\Delta$ Domestic Crude** | First Diff | Constant ($c$) | 1 | 23 | **-2.716** | -3.00 | Fail to Reject at 5% (Rejects at 10%) | Marginally Stationary $I(0)$ |

---

## 4. Methodological Limitations of Unit-Root Tests on Small Annual Panels

While the empirical ADF test statistics for first-differenced imports ($	ext{ADF} = -4.63$) and throughput ($	ext{ADF} = -4.53$) comfortably exceed 1% and 5% critical thresholds, academic integrity demands explicit disclosure of time-series limitations:

1. **Small Sample Size ($T=25$):**  
   Standard asymptotic Dickey-Fuller distributions assume $T ightarrow \infty$. In a 25-observation sample, ADF tests have notoriously low statistical power against stationary alternatives with high autoregressive roots ($ho \in [0.85, 0.95]$) and are susceptible to size distortions.
2. **Structural Breaks:**  
   The 1998–2024 study period spans several major macro-structural disruptions:
   - Commissioning of the Reliance Jamnagar export refineries (1999–2000 and 2008–09).
   - The 2008 Global Financial Crisis oil price spike and collapse.
   - The COVID-19 demand disruption in FY 2020–21.
   - Post-2022 Russian discounted crude trade diversion.
   Standard ADF tests without endogenous structural break parameters (e.g., Zivot-Andrews) can fail to reject a unit root when the true process is stationary around a broken trend.
3. **Differencing vs. Stationarity:**  
   First differencing transforms an integrated $I(1)$ series into an $I(0)$ process, removing deterministic and stochastic linear trends. However, it does not eliminate time-varying conditional variance (heteroskedasticity) or non-linear structural breaks.

---

## 5. Required Manuscript Wording and Stylistic Corrections

### 5.1 Problematic Phrasing Purged:
- ❌ *"MOD-07 is a stationary first differences model."* (Confuses a differenced specification with a proven covariance stationary data-generating process).
- ❌ *"First differencing definitively eliminates the secular trend and proves parameter stability."* (Overstates the power of a mechanical subtraction).
- ❌ *"Stationarity is mathematically confirmed by the differenced regression."* (Conflates regression $R^2$ with time-series stationarity).

### 5.2 Approved Scholarly Formulation for Sections 3.4 and 4.2:
> *"Because level series of refinery throughput and crude imports exhibit persistent secular upward trends and fail to reject the unit-root null under Augmented Dickey-Fuller tests ($	ext{ADF} > -1.80, p > 0.10$), level-level regressions carry potential spurious correlation risks. To assess short-run robustness, we estimate a first-difference specification ($\Delta M_{c,t} = lpha + eta \Delta R_t + arepsilon_t$). Augmented Dickey-Fuller tests on the first-differenced series reject the unit-root null at the 1% and 5% significance levels ($	ext{ADF} = -4.63$ for imports; $	ext{ADF} = -4.53$ for throughput). The first-difference regression yields a slope of $\hat{eta} = 0.9406$ ($	ext{HAC SE} = 0.0219, p < 0.0001, R^2 = 0.9382$). While unit-root tests on small annual samples ($T=25$) possess recognized power limitations, this transformation substantially reduces the influence of common level trends and confirms that annual variations in refining throughput strongly drive annual changes in crude import requirements."*

---

## 6. Execution Code and Provenance

The statistical calculations and ADF tests documented herein were produced using `05_Research_Paper/Phase_9B_C_Final_Reconciliation/test_stationarity.py` against `03_Processed_Data/standardized/core_annual_petroleum_dataset.csv`. All estimates are fully reproducible.
