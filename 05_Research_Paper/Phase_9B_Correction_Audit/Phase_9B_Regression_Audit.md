# Phase 9B — Econometric and Statistical Regression Audit

**Document Reference:** `05_Research_Paper/Phase_9B_Correction_Audit/Phase_9B_Regression_Audit.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Phase 9B Authoritative Econometric Deliverable  
**Underlying Dataset:** `03_Processed_Data/standardized/core_annual_petroleum_dataset.csv` (Balanced 26-Year Panel: FY 1998–99 to FY 2023–24)  

---

## 1. Executive Summary and Audit Scope

During the Phase 9A critical audit, two major methodological hazards were identified in previous draft descriptions of the econometric analysis:
1. **Conflating Level-Level Slopes with Elasticities (Workstream D):** An OLS level-level regression of crude imports ($M_c$) on refinery throughput ($R_t$) was reported with slope $\hat{lpha} pprox 1.011$ (or $0.993$) and described as a *"near-unitary elasticity"*. Econometrically, a level-level slope ($\Delta M_c / \Delta R_t$) measures physical marginal intake in million metric tonnes (MMT) per MMT of throughput; it is **not an elasticity**. An elasticity ($\% \Delta M_c / \% \Delta R_t$) can only be estimated from a logarithmic specification ($\ln M_c$ on $\ln R_t$).
2. **Overclaiming Statistical Non-Significance as Causal "Proof" (Workstream E):** An observational regression of crude imports on domestic crude extraction was cited as $\hat{eta} = -0.3204$ ($p = 0.2713, R^2 = 0.009$), and interpreted in earlier text as *"proving the absence of empirical crowding out"*. In frequentist statistical methodology, failing to reject a null hypothesis ($p > 0.05$) does **not** prove the null is true, nor does it establish causal independence.

This document provides a fully reproducible re-audit of all core regression models, provides exact parameter estimates with conventional and Newey-West Heteroskedasticity-and-Autocorrelation-Consistent (HAC) standard errors, documents time-series non-stationarity limitations, and establishes defensible academic interpretations for the forthcoming manuscript.

---

## 2. Summary Matrix of Audited Econometric Models

The table below summarizes the 8 reproducible specifications estimated across the 26-year balanced study period (FY 1998–99 to FY 2023–24, $N=26$; $N=25$ for first differences).

| Model ID | Model Specification / Name | Dep. Var. ($y$) | Indep. Var. ($x$) | Coef. ($\hat{eta}$) | Conv. SE | HAC SE (lags=2) | $t$-statistic | $p$-value | $R^2$ | Durbin-Watson | Parameter Classification & Economic Meaning |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MOD-01** | Level-Level Bivariate: Throughput Pull | $M_{c,t}$ | $R_t$ | **+0.9927** | 0.0086 | 0.0097 | 102.55 | $< 0.0001$ | **0.9982** | 0.967 | **Level-Level Marginal Slope:** Each additional 1.0 MMT of crude processed is associated with +0.993 MMT gross crude imports. (NOT an elasticity). |
| **MOD-01 (Const)** | Intercept | $M_{c,t}$ | Intercept | **-27.9826** | 1.6557 | 1.1857 | -23.60 | $< 0.0001$ | 0.9982 | 0.967 | Negative constant reflects baseline domestic extraction contribution. |
| **MOD-02** | Log-Log Bivariate: Throughput Elasticity | $\ln(M_{c,t})$ | $\ln(R_t)$ | **+1.2519** | 0.0154 | 0.0288 | 43.49 | $< 0.0001$ | **0.9964** | 0.694 | **True Elasticity Estimate:** A 1.0% expansion in refinery processing throughput is associated with a 1.25% expansion in crude imports. |
| **MOD-02 (Const)** | Intercept | $\ln(M_{c,t})$ | Intercept | **-1.5036** | 0.0796 | 0.1528 | -9.84 | $< 0.0001$ | 0.9964 | 0.694 | Log-linear scaling constant. |
| **MOD-03** | Level-Level Bivariate: Crowding-Out | $M_{c,t}$ | $P_{c,t}$ | **+2.1961** | 4.6487 | 6.5387 | 0.336 | **0.7399** | **0.0092** | 0.043 | **Statistically Insignificant:** Level regression fails to reject null hypothesis ($eta = 0, p = 0.740$). $R^2 < 0.01$. |
| **MOD-03 (Const)** | Intercept | $M_{c,t}$ | Intercept | **+79.8840** | 157.74 | 232.42 | 0.344 | 0.7341 | 0.0092 | 0.043 | Intercept statistically indistinguishable from zero ($p = 0.734$). |
| **MOD-04** | Log-Log Bivariate: Crowding-Out | $\ln(M_{c,t})$ | $\ln(P_{c,t})$ | **+0.8670** | 1.2398 | 1.7143 | 0.506 | **0.6177** | **0.0200** | 0.060 | **Statistically Insignificant Elasticity:** Log-log fails to reject null of zero elasticity ($p = 0.618$). |
| **MOD-05** | Multivariate Level-Level: Both Drivers | $M_{c,t}$ | $R_t$ | **+0.9976** | 0.0044 | 0.0027 | 373.17 | $< 0.0001$ | **0.9996** | 2.855 | Throughput retains near-unity marginal slope (+0.998) when controlling for domestic crude extraction. |
| **MOD-05 (b)** | Multivariate Level-Level: Both Drivers | $M_{c,t}$ | $P_{c,t}$ | **-0.8475** | 0.1002 | 0.0709 | -11.96 | $< 0.0001$ | 0.9996 | 2.855 | Holding throughput fixed, +1 MMT domestic extraction displaces -0.848 MMT imports (accounting substitution effect). |
| **MOD-06** | First Differences Multivariate ($N=25$) | $\Delta M_{c,t}$ | $\Delta R_t$ | **+0.9810** | 0.0461 | 0.0229 | 42.85 | $< 0.0001$ | **0.9550** | 3.103 | **Stationary Short-Run Co-movement:** Annual throughput shocks pass through to import volume changes with slope +0.981. |
| **MOD-06 (b)** | First Differences Multivariate ($N=25$) | $\Delta M_{c,t}$ | $\Delta P_{c,t}$ | **-1.0871** | 0.3799 | 0.1742 | -6.24 | $< 0.0001$ | 0.9550 | 3.103 | Short-run annual extraction changes show negative coefficient (-1.087) controlling for throughput variations. |
| **MOD-07** | Bivariate First Differences: Throughput | $\Delta M_{c,t}$ | $\Delta R_t$ | **+0.9406** | 0.0503 | 0.0219 | 43.03 | $< 0.0001$ | **0.9382** | 2.899 | Bivariate short-run changes confirm throughput alone accounts for 93.8% of annual variance in crude imports. |
| **MOD-08** | Bivariate First Differences: Extraction | $\Delta M_{c,t}$ | $\Delta P_{c,t}$ | **+1.3851** | 1.6419 | 1.7848 | 0.776 | **0.4456** | **0.0300** | 2.049 | Bivariate short-run changes show domestic extraction changes have no statistically significant association ($p = 0.446$). |

---

## 3. Detailed Audit of Workstream D: Throughput-Import Relationship

### 3.1 Level-Level Regression ($M_{c,t} = lpha_0 + lpha_1 R_t + u_t$)
- **Reproduced Formula:**
  $$	ext{Crude Imports}_t = -27.9826 + 0.9927 \cdot 	ext{Throughput}_t + u_t$$
- **Reproduced Statistics ($N=26$):**
  - Slope ($\hat{lpha}_1$): **0.9927** (Conventional SE = 0.0086; Newey-West HAC SE = 0.0097)
  - $t$-statistic: **102.55** ($p < 0.0001$)
  - Model $R^2$: **0.9982** (Adjusted $R^2$: 0.9981)
  - Residual Standard Error: **2.67 MMT**
  - Durbin-Watson: **0.967**
- **Audit Diagnosis:**
  - In earlier Phase 9/9A documentation, this slope was reported as $pprox 1.011$ with $R^2 = 0.9982$. That 1.011 value arose from an uncentered or sample-extended variant. The exact balanced 26-year OLS slope is **0.9927**.
  - **Critical Terminology Correction:** This coefficient is a **level-level regression slope**, expressing marginal physical import requirements in MMT per MMT throughput. **It is NOT an elasticity.** Calling it a "near-unitary elasticity" is an econometric category mistake.

### 3.2 True Log-Log Elasticity Model ($\ln(M_{c,t}) = \gamma_0 + \gamma_1 \ln(R_t) + v_t$)
- **Reproduced Formula:**
  $$\ln(	ext{Crude Imports}_t) = -1.5036 + 1.2519 \cdot \ln(	ext{Throughput}_t) + v_t$$
- **Reproduced Statistics ($N=26$):**
  - Elasticity Estimate ($\hat{\gamma}_1$): **1.2519** (Conventional SE = 0.0154; Newey-West HAC SE = 0.0288)
  - $t$-statistic: **43.49** ($p < 0.0001$)
  - 95% Confidence Interval for Elasticity: $[1.1926, 1.3112]$
  - Model $R^2$: **0.9964** (Adjusted $R^2$: 0.9962)
  - Residual Standard Error: **0.0303**
  - Durbin-Watson: **0.694**
- **Economic Interpretation:**
  - The true elasticity of crude imports with respect to refinery processing throughput is **1.252**, significantly greater than 1.0 ($p < 0.0001$).
  - Because domestic crude production stagnated while throughput expanded four-fold, crude imports had to expand *faster* in percentage terms (+488.5%) than throughput (+281.6%), generating an empirical elasticity of 1.25.

### 3.3 Time-Series Non-Stationarity Limitations
- **Secular Trend and Spurious Correlation Risk:** Both crude imports and refinery throughput exhibited persistent upward trends over 1998–2024. The Durbin-Watson statistic of 0.967 in levels (and 0.694 in logs) reveals positive first-order residual autocorrelation.
- **Methodological Disclosure:** While Newey-West HAC covariance matrices correct standard errors for autocorrelation and heteroskedasticity, they **do not resolve unit-root non-stationarity or cointegration**. A high $R^2$ ($> 0.99$) between trending level series cannot be treated as mathematical proof of a structural relationship without formal cointegration testing.
- **Robustness Confirmation via First Differences (MOD-06 and MOD-07):**
  - When series are transformed into first differences ($\Delta M_{c,t}$ and $\Delta R_t$), eliminating secular linear and non-linear deterministic trends, the bivariate model yields $\hat{eta} = 0.9406$ ($t = 43.03, p < 0.0001, R^2 = 0.9382, 	ext{DW} = 2.899$).
  - This confirms that the tight link between refining expansion and crude import growth is **not** an artifact of spurious trending; short-run annual changes in refining volume explain 93.8% of the annual fluctuations in crude imports.

---

## 4. Detailed Audit of Workstream E: Crowding-Out Hypothesis

### 4.1 Examination of Reported Phase 9A Figures
- Earlier Phase 9A materials cited: $\hat{eta} = -0.3204$, $	ext{SE} = 0.283$, $t = -1.13$, $p = 0.2713$, $R^2 = 0.009$.
- Re-audit of the balanced 26-year panel demonstrates:
  - Bivariate level regression ($M_{c,t}$ on $P_{c,t}$, MOD-03): $\hat{eta} = +2.1961$, $	ext{HAC SE} = 6.5387$, $t = 0.336$, $p = 0.7399$, $R^2 = 0.0092$.
  - Bivariate log-log regression ($\ln M_c$ on $\ln P_c$, MOD-04): $\hat{eta} = +0.8670$, $	ext{HAC SE} = 1.7143$, $t = 0.506$, $p = 0.6177$, $R^2 = 0.0200$.
  - Bivariate first differences ($\Delta M_c$ on $\Delta P_c$, MOD-08): $\hat{eta} = +1.3851$, $	ext{HAC SE} = 1.7848$, $t = 0.776$, $p = 0.4456$, $R^2 = 0.0300$.
  - In all bivariate specifications, the coefficient of determination $R^2$ is less than 0.03 ($R^2 pprox 0.009$ in levels), and the association is statistically indistinguishable from zero ($p > 0.40$).

### 4.2 Multivariate Accounting Substitution (MOD-05)
- When both refinery throughput ($R_t$) and domestic crude extraction ($P_{c,t}$) are included in a level-level regression ($M_{c,t} = eta_0 + eta_1 R_t + eta_2 P_{c,t} + \epsilon_t$):
  - $\hat{eta}_1 (	ext{Throughput}) = \mathbf{+0.9976}$ ($p < 0.0001$)
  - $\hat{eta}_2 (	ext{Domestic Crude}) = \mathbf{-0.8475}$ ($p < 0.0001$)
  - Model $R^2 = \mathbf{0.9996}$, $	ext{DW} = 2.855$.
- **Econometric Meaning:**
  - Holding refinery throughput constant, an increase of 1.0 MMT in domestic extraction is associated with a 0.85 MMT reduction in imports. This reflects the physical crude accounting identity ($P_c + M_c pprox R$).
  - However, because refinery throughput expanded by $+193.0	ext{ MMT}$ while domestic production stagnated at $\sim 30	ext{ MMT}$, the massive positive throughput pull completely dominated domestic extraction in aggregate import determination.

### 4.3 Rigorous Academic Framing and Reporting Language
- **Prohibited Claim:** *"The econometric analysis proves that domestic crude extraction does not crowd out crude imports."*
- **Approved Scholarly Formulation:**  
  > *"Bivariate time-series regressions of crude imports on domestic crude production yield statistically insignificant parameter estimates ($p > 0.10$) and near-zero explanatory power ($R^2 < 0.01$). Observational data over the 26-year study period therefore fail to reject the null hypothesis of no linear relationship. These observational findings must be interpreted cautiously: small sample size ($N=26$), aggregate annual frequency, and lack of exogenous instruments preclude causal inference or definitive assertions regarding the presence or absence of market crowding-out mechanisms."*

---

## 5. Diagnostic and Model Limitations Checklist

1. **Sample Size ($N=26$):** The small sample of annual observations restricts econometric degrees of freedom. While sufficient for descriptive OLS and subperiod comparisons, it limits high-order VAR or VECM modeling.
2. **Deterministic Trends:** Both throughput and imports trend strongly upward; level-level regressions reflect long-run secular co-movement. First-difference transformations confirm short-run robustness.
3. **Absence of Cointegration Tests:** Formal Johansen or Engle-Granger cointegration tests are not reported in the standardized pipeline; therefore, no claims of a formal cointegrating vector should be made in the manuscript.
4. **Omitted Factors:** Annual crude import volumes are also influenced by international freight spreads, geopolitical trade realignments (e.g., Russian crude discounts post-2022), and commercial refinery slate optimization, which are not modeled in these bivariate specifications.

---

## 6. Execution Code Provenance

The statistical results documented in this audit report were computed using `05_Research_Paper/Phase_9B_Correction_Audit/audit_regressions.py` executed against `03_Processed_Data/standardized/core_annual_petroleum_dataset.csv`. All outputs are 100% reproducible.
