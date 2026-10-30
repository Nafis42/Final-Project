# Phase 4 Analytical Methodology: Statistical Trend, Growth, and Structural Change

**Project:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** Phase 4 — Empirical Trend & Growth Analysis  
**Foundation Datasets:** Standardized Phase 3 Core Tables (`core_annual_petroleum_dataset`, `derived_indicators`, `petroleum_supporting_variables`)  

---

## 1. Analysis Sample & Periodization Framework

### A. Authoritative Reporting Basis
All official petroleum sector data published by the Petroleum Planning & Analysis Cell (PPAC) are anchored strictly in the **Indian Financial Year (1 April to 31 March)**. In accordance with project instructions:
- Financial years are preserved explicitly (e.g. `FY 1998-99`) and are never relabeled as calendar years.
- Continuous integer temporal key `fiscal_year_start` (e.g. `1998`) serves as the quantitative time-series anchor.

### B. Valid Analytical Samples
To ensure rigorous comparability without distorting growth rates or statistical tests, the empirical analysis defines three distinct sample horizons:
1. **Primary Multi-Tier Harmonized Baseline (FY 1998–99 to FY 2023–24, $N = 26$ years):**  
   The primary sample where all 7 core supply-chain tiers (domestic crude production, crude imports, refinery throughput, product production, product imports, product exports, domestic product consumption, trade values, and derived indicators) are 100% complete and synchronized.
2. **Extended Downstream Sample (FY 1998–99 to FY 2024–25, $N = 27$ years):**  
   Utilized for downstream refining throughput, petroleum trade, domestic consumption, and international crude prices, where complete FY 2024–25 observations are verified. Upstream domestic crude production is excluded from FY 2024–25 due to source workbook truncation.
3. **Crude FOB Price Sample (FY 2000–01 to FY 2024–25, $N = 25$ years):**  
   The official PPAC Indian Crude Basket FOB historical price series begins in FY 2000–01.

### C. Treatment of Partial & Provisional Data
- Forward partial periods (FY 2025–26 Apr–Sep and FY 2026–27 Till June) are cataloged in Phase 3 metadata but are **strictly excluded** from annual growth rate and CAGR calculations to prevent seasonal distortion.

---

## 2. Mathematical & Statistical Formulas

### A. Descriptive Statistics
For sample observations $y_1, y_2, \dots, y_N$:
- **Arithmetic Mean:** $\bar{y} = \frac{1}{N} \sum_{t=1}^N y_t$
- **Median:** $y_{\text{med}} = \text{middle observation of sorted series}$
- **Sample Standard Deviation:** $s = \sqrt{\frac{1}{N-1} \sum_{t=1}^N (y_t - \bar{y})^2}$
- **Absolute Change:** $\Delta y = y_{\text{end}} - y_{\text{start}}$
- **Percentage Change:** $\Delta y (\%) = \left[ \frac{y_{\text{end}} - y_{\text{start}}}{y_{\text{start}}} \right] \times 100$

### B. Year-on-Year Growth Metrics
- **Annual Absolute Change:** $\Delta y_t = y_t - y_{t-1}$
- **Annual Percentage Growth Rate:** $g_t (\%) = \left[ \frac{y_t - y_{t-1}}{y_{t-1}} \right] \times 100$
*(Computed strictly across consecutive, verified fiscal years; never calculated across missing gaps).*

### C. Compound Annual Growth Rate (CAGR)
$$\text{CAGR} (\%) = \left[ \left( \frac{y_T}{y_0} \right)^{1/n} - 1 \right] \times 100$$
where:
- $y_0$ is the beginning observation.
- $y_T$ is the ending observation.
- $n = T - 0$ is the actual number of elapsed financial years between periods (not simply row count).
*Note: CAGR summarizes the smooth geometric progression over an interval and does not imply a constant annual expansion.*

### D. Non-Parametric Trend Testing: Mann–Kendall & Sen's Slope
Given that macroeconomic time series frequently exhibit non-normal distributions, the analysis deploys robust non-parametric trend estimators:
1. **Mann–Kendall Trend Test:**
   - Evaluates the null hypothesis $H_0$ (no monotonic trend) against $H_1$ (monotonic upward or downward trend).
   - Test statistic $S$:
     $$S = \sum_{i=1}^{n-1} \sum_{j=i+1}^n \text{sgn}(y_j - y_i)$$
   - Kendall's rank correlation coefficient $\tau$:
     $$\tau = \frac{S}{\frac{1}{2} n (n - 1)}$$
   - Standardized normal test statistic $Z$ (for $n > 10$):
     $$Z = \begin{cases} \frac{S - 1}{\sqrt{\text{Var}(S)}} & \text{if } S > 0 \\ 0 & \text{if } S = 0 \\ \frac{S + 1}{\sqrt{\text{Var}(S)}} & \text{if } S < 0 \end{cases}$$
2. **Sen's Slope Estimator:**
   - Robust non-parametric slope estimator calculated as the median of all pairwise slopes:
     $$Q = \text{median} \left\{ \frac{y_j - y_i}{j - i} \right\} \quad \text{for } 1 \le i < j \le n$$
   - Insensitive to single-year outliers, cyclical spikes, or geopolitical shocks.
