# Methodology Correction Register and Quantitative Specification Audit

**Document Reference:** `05_Research_Paper/phase9a_audit/07_methodology_correction_register.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Phase 9A Critical Audit Output  

---

## 1. Executive Summary

This register audits every mathematical formula, econometric specification, index decomposition equation, and empirical convention proposed for **Section 3 (Method)** of the manuscript.

By auditing the actual Python scripts (`src/`, `04_Analysis/phase6/`, `04_Analysis/phase8/`) and standardized datasets (`03_Processed_Data/standardized/`), this audit resolves four critical methodology flaws present in Phase 9 draft documents:
1. **Stationarity Testing Correction:** Phase 9 drafts asserted that Augmented Dickey-Fuller (ADF) tests were performed. This audit confirms that **no ADF test was ever executed in Phases 1–8**. Stationarity was addressed via first-difference co-movement testing and Newey-West HAC covariance corrections. All claims of ADF testing are removed.
2. **Decomposition Methodology Clarification:** Phase 6 originally implemented a **two-factor symmetric decomposition** ($\Delta V = \Delta Q \cdot \bar{P} + \Delta P \cdot \bar{Q}$) in USD and INR. Phase 9 introduced a three-factor **Logarithmic Mean Divisia Index (LMDI-I)** framework (Ang, 2004, 2015) to isolate the currency depreciation wedge, but quoted inconsistent percentage shares. We re-estimate the exact LMDI-I decomposition, confirming zero closure residual.
3. **CAGR Transition Calibration:** Compound growth rates were calculated over **$n = 25$ one-year compounding intervals** across 26 points, not $n = 26$.
4. **Non-Causality and Observational Regression Boundary:** All econometric estimates are explicitly re-designated as structural empirical correlations and supply-chain elasticities, removing any assertion of econometric causality.

---

## 2. Subsection-by-Subsection Equation and Specification Audit

### 3.1 Financial Year Calibration and Accounting Boundaries
- **Empirical Definition:**
  $$\text{FY}_t \equiv \text{April 1, Year } (t-1) \text{ to March 31, Year } t$$
- **Balanced Study Panel:** FY 1998–99 ($t = 1$) to FY 2023–24 ($t = 26$), exactly 26 annual points.
- **Excluded Forward Periods:** FY 2024–25 (partial-year trade, truncated upstream), FY 2025–26 (provisional budget estimates), and FY 2026–27 (Q1 partial observation).

---

### 3.2 Physical and Monetary Unit Standardization
- **Physical Quantities:**
  $$1 \text{ MMT} = 1,000 \text{ TMT} = 10^6 \text{ Metric Tonnes} = 10^9 \text{ kg}$$
- **Domestic Currency:** Indian Rupees Crore ($\text{Rs. Cr} = 10^7 \text{ INR}$).
- **Foreign Currency:** United States Dollars Million ($\text{USD M} = 10^6 \text{ USD}$) and Billion ($\text{USD B} = 10^9 \text{ USD}$).
- **Implied Annual Exchange Rate ($\text{IER}_t$):**
  $$\text{IER}_t = \frac{\text{Value}_{\text{INR}, t} \times 10^7}{\text{Value}_{\text{USD}, t} \times 10^6} = \frac{\text{Value}_{\text{INR}, t} \times 10}{\text{Value}_{\text{USD}, t}} \quad (\text{INR/USD})$$
  *Audit Validation:* In FY 1998–99, $\text{IER} = (14,917.0 \times 10) / 3,518.0 = 42.40\text{ INR/USD}$. In FY 2023–24, $\text{IER} = (1,105,176.0 \times 10) / 133,366.0 = 82.87\text{ INR/USD}$. Matches RBI annual reference series within $<0.15\%$.

---

### 3.3 Compound Annual Growth Rate (CAGR)
- **Mathematical Formulation:**
  $$\text{CAGR}_{t_0, t_T}(X) = \left( \frac{X_T}{X_0} \right)^{\frac{1}{T - t_0}} - 1$$
- **Corrected Interval Parameter:**
  $$n = T - t_0 = 2024 - 1999 = 25 \text{ one-year compounding intervals}$$
- **Verification Table:**
  - Crude Imports: $(234.262 / 39.808)^{1/25} - 1 = \mathbf{+7.35\%}$ (or $+7.37\%$ with TMT precision).
  - Domestic Crude Production: $(29.356 / 32.760)^{1/25} - 1 = \mathbf{-0.44\%}$.
  - Refinery Throughput: $(261.546 / 68.539)^{1/25} - 1 = \mathbf{+5.50\%}$.
  - Crude Import Bill (USD): $(133,366 / 3,518)^{1/25} - 1 = \mathbf{+15.65\%}$ (or $+15.70\%$).
  - Crude Import Bill (INR): $(1,105,176 / 14,917)^{1/25} - 1 = \mathbf{+18.79\%}$ (or $+18.88\%$).

---

### 3.4 Crude Oil Import-Dependence Indicators (Disambiguated)
To prevent combining metrics, the paper will publish both indicators with distinct notation:

1. **Supply-Pool Import Share ($\text{SPS}_t$):**
   $$\text{SPS}_t = \left( \frac{M_{c,t}}{P_{c,t} + M_{c,t}} \right) \times 100 \quad (\%)$$
   *Baseline (FY99):* $54.86\%$; *Terminal (FY24):* $88.86\%$.
2. **Import-to-Throughput Ratio ($\text{IRR}_t$):**
   $$\text{IRR}_t = \left( \frac{M_{c,t}}{R_t} \right) \times 100 \quad (\%)$$
   *Baseline (FY99):* $58.08\%$; *Terminal (FY24):* $89.57\%$ (Peak: $91.17\%$ in FY23).
3. **Indigenous Crude Sufficiency Ratio ($\text{SSR}_t$):**
   $$\text{SSR}_t = \left( \frac{P_{c,t}}{R_t} \right) \times 100 \quad (\%)$$
   *Baseline (FY99):* $47.80\%$; *Terminal (FY24):* $11.22\%$.

---

### 3.5 Physical Supply Gap vs. Complete Feedstock Balance
- **Physical Domestic Production-to-Throughput Gap:**
  $$\Delta_{\text{upstream}, t} = R_t - P_{c,t} \quad (\text{MMT})$$
  *Audit Warning:* This is strictly an accounting shortfall between indigenous production and refinery gate intake.
- **True Feedstock Mass-Balance Formulation:**
  $$M_{c,t} = (R_t - P_{c,t}) + \Delta S_{c,t} + \theta_{c,t}$$
  Where $\Delta S_{c,t} + \theta_{c,t}$ represents inventory changes, pipeline line-fill, and ocean transit losses, averaging $+4.41\text{ MMT}$ per year.

---

### 3.6 Refined Petroleum Product Trade and Self-Sufficiency
1. **Net Product Trade Balance ($\text{NPT}_t$):**
   $$\text{NPT}_t = X_{p,t} - M_{p,t} \quad (\text{MMT})$$
   $$\text{NPT}_{i,t} = X_{i,t} - M_{i,t} \quad (\text{MMT for product } i)$$
   *Audit Result:* Permanent net export surplus every year since FY02 ($+13.89\text{ MMT}$ in FY24).
2. **Product-Specific Import Dependency ($\text{PID}_{i,t}$):**
   $$\text{PID}_{i,t} = \left( \frac{M_{i,t} - X_{i,t}}{C_{i,t}} \right) \times 100 \quad (\%)$$
   *Audit Result for LPG (FY24):* $\text{PID}_{\text{LPG}} = \frac{18.10 - 0.11}{30.40} \times 100 = \mathbf{62.74\%}$.
3. **Refining Coverage Ratio ($\text{RCR}_t$):**
   $$\text{RCR}_t = \left( \frac{Q_{p,t}}{C_t} \right) \times 100 \quad (\%)$$
   *Audit Result (FY24):* $\text{RCR} = \frac{276.14}{233.28} \times 100 = \mathbf{118.37\%}$.

---

### 3.7 Econometric Specifications (Newey-West HAC)

#### OLS Models:
1. **Crude Imports on Domestic Production (Testing Crowding-Out):**
   $$M_{c,t} = \beta_0 + \beta_1 P_{c,t} + \varepsilon_t$$
   *Verified Result (N=26):* $\hat{\beta}_1 = -0.3204$ ($t = -1.13, p = 0.2713, R^2 = 0.009$). Null hypothesis of no linear relationship cannot be rejected.
2. **Crude Imports on Refinery Processing (Throughput Pull):**
   $$M_{c,t} = \alpha_0 + \alpha_1 R_t + u_t$$
   *Verified Result (N=26):* $\hat{\alpha}_1 = 1.011$ ($t = 115.4, p < 0.0001, R^2 = 0.9982$). Near-unitary elasticity.

#### Covariance Estimator (Newey-West HAC):
$$\widehat{\text{Var}}(\hat{\beta}) = (X'X)^{-1} \hat{\Omega}_{\text{HAC}} (X'X)^{-1}$$
$$\hat{\Omega}_{\text{HAC}} = \hat{\Gamma}_0 + \sum_{v=1}^{m} \left( 1 - \frac{v}{m+1} \right) (\hat{\Gamma}_v + \hat{\Gamma}_v')$$
With Bartlett kernel truncation lag $m = 2$ for $T = 26$.

#### Correction Regarding Stationarity:
- **AUDIT FINDING:** No Augmented Dickey-Fuller (ADF) test script exists in the repository.
- **MANUSCRIPT CORRECTION:** Remove all references claiming ADF unit-root tests were conducted. Instead, state:
  > *"To ensure robustness against non-stationary trending series, Pearson and Spearman correlation coefficients were evaluated on both raw levels and first differences ($\Delta X_t = X_t - X_{t-1}$). Co-movement in first differences confirms that the correlation between refinery throughput and crude imports ($r_{\Delta} = 0.884, p < 0.0001$) is structural, while the correlation between domestic crude extraction and crude imports ($r_{\Delta} = 0.173, p = 0.408$) remains statistically indistinguishable from zero."*

---

### 3.8 Index Decomposition Analysis (LMDI) Reconciliation

#### Distinction Between Phase 6 and Phase 9:
- **Phase 6 Implementation:** Two-factor symmetric decomposition:
  $$\Delta V = \Delta Q \cdot \bar{P} + \Delta P \cdot \bar{Q}$$
  Executed separately for USD and INR import series.
- **Phase 9 Proposed Implementation:** Three-factor Logarithmic Mean Divisia Index (LMDI-I) (Ang, 2004, 2015):
  $$V_{\text{INR}, t} = Q_t \times P_{\text{USD}, t} \times E_t$$
  Where $Q$ is MMT, $P_{\text{USD}}$ is USD/MT, and $E$ is INR/USD.

#### Mathematically Exact LMDI-I Re-estimation (FY99 to FY24):
Using verified endpoint data ($Q_0 = 39.808$, $P_0 = 88.374$, $E_0 = 42.402$, $V_0 = 14,917.0$; $Q_T = 234.262$, $P_T = 569.294$, $E_T = 82.868$, $V_T = 1,105,176.0$):

$$\Delta V_{\text{tot}} = V_T - V_0 = \text{Rs. } 1,090,259.00 \text{ Crore}$$
$$L(V_T, V_0) = \frac{V_T - V_0}{\ln(V_T) - \ln(V_0)} = 253,238.92 \text{ Rs. Cr}$$

$$\Delta V_Q = L \cdot \ln\left( \frac{Q_T}{Q_0} \right) = \mathbf{+448,833.19 \text{ Rs. Cr}} \quad (\mathbf{41.17\%})$$
$$\Delta V_P = L \cdot \ln\left( \frac{P_T}{P_0} \right) = \mathbf{+471,742.11 \text{ Rs. Cr}} \quad (\mathbf{43.27\%})$$
$$\Delta V_E = L \cdot \ln\left( \frac{E_T}{E_0} \right) = \mathbf{+169,683.70 \text{ Rs. Cr}} \quad (\mathbf{15.56\%})$$

$$\text{Closure Residual: } \Delta V_{\text{tot}} - (\Delta V_Q + \Delta V_P + \Delta V_E) = \mathbf{0.0000 \text{ Rs. Cr (Exact Closure)}}$$

*Audit Warning:* Phase 9 draft documents erroneously stated that $\Delta V_Q = 29.8\%$, $\Delta V_P = 41.1\%$, and $\Delta V_E = 29.0\%$. These numbers must be corrected to the exact mathematical shares above (**Quantity: 41.17%, Price: 43.27%, Exchange Rate: 15.56%**).

---

### 3.9 Disclosures and Methodological Boundaries
1. **Lease Condensate:** In official MoPNG/PPAC accounting, domestic crude extraction includes lease condensate. This is disclosed in all tables presenting $P_c$.
2. **Ethanol Blended Petrol (EBP):** Ethanol blending occurs at OMC distribution depots, not at refinery crude distillation units. Motor spirit production statistics reflect pure refinery hydrocarbon output.
3. **Non-Causality:** All regression models reflect empirical correlations and structural elasticity relationships in observational time series; no structural vector autoregressive identification or exogenous instrumental variable causal claim is made.
