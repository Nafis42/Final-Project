# Generate Phase_9B_Revised_Manuscript_Outline.md

outline_content = """# Phase 9B — Revised Manuscript Structure and Section-by-Section Plan

**Document Reference:** `05_Research_Paper/Phase_9B_Correction_Audit/Phase_9B_Revised_Manuscript_Outline.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Phase 9B Authoritative Structural Plan (Strictly Aligned with Professor's 11-Section Template)  
**Verification Baseline:** Derived strictly from Phase 9B Recalculated Indicators and Econometric Re-audits  

---

## Important Notice on Scope Boundaries
In strict compliance with Phase 9B instructions:
- **This is an structural outline and evidence-mapping document, NOT a full manuscript draft.**
- **No abstract or full body paragraphs are drafted herein.** Full text drafting is strictly reserved for Phase 10 upon user authorization.
- Every section heading, planned subsection, table reference, figure mapping, and empirical claim is harmonized with the audited data in `Phase_9B_Recalculated_Indicators.csv` and `Phase_9B_Regression_Audit.md`.

---

## 1. Required Structural Compliance: Professor's 11 Sections

The manuscript structure strictly follows the mandatory sequence prescribed in `Journal paper template.docx`:

```
+----------------------------------------------------------------------------------------------------+
|                         PROFESSOR'S MANDATORY 11-SECTION PAPER STRUCTURE                           |
+----------------------------------------------------------------------------------------------------+
|  1. Abstract (Reserved for Phase 10; structured according to target journal specifications)        |
|  2. Introduction (Problem context, policy background, research gap, empirical framing)             |
|  3. Method (Supply-chain framework, 26-year panel dataset, formulas, econometric specifications)   |
|  4. Result (Disaggregated findings across upstream, refining, downstream trade, prices/costs)     |
|  5. Discussion (Comparison with literature, structural mechanisms, policy synthesis)               |
|  6. Conclusion (Summary of key findings, strategic implications, research limitations)             |
|  7. References (29 authentic peer-reviewed publications, APA 7th edition, 100% verified DOIs)      |
|  8. Acknowledgement (Institutional data providers, university facilities, research mentors)        |
|  9. Conflict of Interest (Formal neutrality disclosure; zero commercial/financial conflicts)       |
| 10. Funding Statement (Academic self-funded / institutional non-commercial research disclosure)    |
| 11. Author Contributions (CRediT taxonomy: conceptualization, data curation, formal analysis)      |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Detailed Section-by-Section Plan and Evidence Mapping

### Section 1: Abstract *(To be drafted in Phase 10)*
- **Planned Word Count:** 200–250 words (structured or unstructured per journal requirements).
- **Core Content Elements:**
  - *Context:* India's rapid economic growth and escalating petroleum import dependence.
  - *Data & Methods:* A 26-year balanced physical and financial supply-chain panel (FY 1998–99 to FY 2023–24; $N=26$) integrating upstream crude extraction, refinery processing, refined product trade, and consumption.
  - *Key Audited Findings:*
    1. Domestic crude extraction stagnated (+0.36% CAGR), causing indigenous crude sufficiency relative to throughput to collapse from 47.80% to 11.22%.
    2. Crude import expansion (+488.5%, from 39.81 MMT to 234.26 MMT) was statistically tied to downstream refinery throughput expansion (+281.6%, from 68.54 MMT to 261.55 MMT), with an OLS level slope of 0.993 MMT/MMT ($R^2 = 0.998$) and an estimated log-log elasticity of 1.252 ($p < 0.0001$).
    3. Refined product exports (+62.59 MMT in FY24) generated an unbroken net product trade surplus since FY02 (+13.90 MMT net export balance in FY24), yielding a downstream product coverage ratio of 117.84% of domestic consumption.
    4. Product-level asymmetries: Massive surpluses in transport fuels (Diesel +28.16 MMT, Petrol +12.76 MMT) coexisted with an acute clean cooking deficit in LPG (Net Import Dependence = 60.64%, Gross Import Dependence = 62.41% on 29.66 MMT consumption).
  - *Significance:* Demonstrates that national import dependence is structurally bifurcated between refining feedstock exposure and consumer product trade balances.

---

### Section 2: Introduction
- **2.1 Context and Problem Statement:**
  - India's transition to the world's third-largest crude oil consumer and importer.
  - Energy security vulnerability: Crude import bill surging to US$ 133.4 billion (Rs. 11.05 lakh crore) in FY 2023–24.
  - Macroeconomic exposure: Vulnerability to international crude price shocks and exchange rate volatility.
- **2.2 Policy Evolution and Institutional Context:**
  - Upstream exploration policies: New Exploration Licensing Policy (NELP rounds 1–9) and Hydrocarbon Exploration and Licensing Policy (HELP/OALP).
  - Downstream liberalization: Dismantling of the Administered Pricing Mechanism (APM) in 2002, entry of world-class private refining complexes (Jamnagar DTA in 1999–2000, SEZ in 2008–09, Vadinar).
  - Social energy transition: The Pradhan Mantri Ujjwala Yojana (PMUY) and targeted substitution of polluting kerosene (SKO) with clean LPG.
- **2.3 Literature Synthesis and Identified Research Gaps:**
  - *Macroeconomic / Vulnerability Literature:* Gupta (2008), Vivoda (2010), Ghosh (2009), Surender Kumar (2009). Gap: Focuses almost exclusively on aggregate macroeconomic shocks or crude imports, treating India's domestic refining sector as an exogenous "black box".
  - *Microeconomic / Household Energy Literature:* Kar et al. (2019), Gould & Urpelainen (2018), Gill-Wiehl et al. (2022). Gap: Examines LPG adoption and health benefits without linking LPG demand to macro refinery distillation yields and balance-of-payments import exposure.
  - *Engineering / Refining Systems Literature:* de la Rue du Can et al. (2019), Kumar et al. (2012). Gap: Analyzes refinery efficiency without econometric modeling of import pull dynamics.
- **2.4 Research Objective and Empirical Framing:**
  - Objective: Construct an integrated, mass-balanced empirical analysis of India's petroleum supply chain across 26 years.
  - Conceptual Framework: The "Triple Paradox" framing used strictly as an *empirical organizing motif*:
    1. *The Extraction Paradox:* Stagnant domestic crude extraction alongside surging downstream refining capacity.
    2. *The Trade Asymmetry Paradox:* Simultaneous crude import dependence (88.86% SPS) and aggregate refined product export capability (117.84% product coverage).
    3. *The Clean Cooking Paradox:* Surpassing domestic self-sufficiency in transport fuels while remaining acutely dependent on imports for clean cooking fuel (60.64% NID).

---

### Section 3: Method
- **3.1 Supply-Chain Conceptual Framework:**
  - Four-tier physical balance: Upstream Extraction $\rightarrow$ Midstream Refining Throughput $\rightarrow$ Downstream Product Slate $\rightarrow$ Final Product Consumption.
- **3.2 Data Sources and Panel Harmonization:**
  - Sources: Ministry of Petroleum & Natural Gas (MoPNG) and Petroleum Planning & Analysis Cell (PPAC) official publications (*Indian Petroleum & Natural Gas Statistics*, monthly trade and processing returns).
  - Panel Scope: FY 1998–99 to FY 2023–24 (26 annual observations, 25 first-difference intervals). FY 1997–98 retained solely for downstream baseline consumption context.
- **3.3 Mathematical Formulations and Indicator Definitions:**
  - *Supply-Pool Import Share (SPS):* $\text{SPS}_t = \frac{M_{c,t}}{M_{c,t} + P_{c,t}} \times 100$
  - *Import-to-Refinery Ratio (IRR):* $\text{IRR}_t = \frac{M_{c,t}}{R_t} \times 100$
  - *Indigenous Crude Sufficiency Ratio (SSR):* $\text{SSR}_t = \frac{P_{c,t}}{R_t} \times 100$
  - *Crude Physical Accounting Identity:* $P_{c,t} + M_{c,t} - X_{c,t} = R_t + \Delta S_{c,t} + \theta_t$ (where $X_{c,t} = 0$). Unreconciled residual: $\text{Res}_t = M_{c,t} - (R_t - P_{c,t})$.
  - *Downstream Product Coverage Ratio:* $\text{PCR}_t = \frac{\text{Total Product Production}_t}{\text{Total Product Consumption}_t} \times 100$ (disclosed as net physical output coverage, NOT capacity utilization).
  - *LPG Gross Import Dependence:* $\text{GID}_t = \frac{\text{Gross LPG Imports}_t}{\text{LPG Consumption}_t} \times 100$
  - *LPG Net Import Dependence:* $\text{NID}_t = \frac{\text{Gross LPG Imports}_t - \text{LPG Exports}_t}{\text{LPG Consumption}_t} \times 100$
- **3.4 Econometric Specifications and Diagnostic Procedures:**
  - Level-level OLS models with Newey-West HAC covariance matrices (maxlags=2) to correct for residual autocorrelation and heteroskedasticity.
  - Log-log specifications to estimate constant elasticities ($\ln Y = \beta_0 + \beta_1 \ln X$).
  - First-difference models ($\Delta Y_t = \alpha + \beta \Delta X_t$) to evaluate short-run annual changes and mitigate secular trend non-stationarity.
  - Explicit disclosure of non-stationarity limitations (Durbin-Watson diagnostics, spurious correlation caveats).

---

### Section 4: Result
- **4.1 Upstream Stagnation and the Widening Crude Deficit:**
  - Trajectory of domestic crude extraction: 32.76 MMT (FY99) to 29.36 MMT (FY24), peaking at 38.08 MMT in FY 2011–12 (+0.36% CAGR over 26 years).
  - Expansion of refinery crude throughput: 68.54 MMT to 261.55 MMT (+5.51% CAGR).
  - Widening domestic production-to-throughput gap: $R_t - P_{c,t}$ increased from 35.78 MMT to 232.19 MMT (+549.0%).
  - Collapse of indigenous crude sufficiency (SSR): 47.80% in FY99 to 11.22% in FY24 (-36.58 percentage points).
  - Evolution of Supply-Pool Import Share (SPS): 54.86% to 88.86% (+34.00 percentage points).
- **4.2 Midstream Refining Expansion and Crude Import Determinants:**
  - OLS Level-Level Slope (MOD-01): $\text{Imports}_t = -27.98 + 0.9927 \cdot \text{Throughput}_t$ ($R^2 = 0.9982, p < 0.0001, \text{HAC SE} = 0.0097$).
  - OLS Log-Log Elasticity (MOD-02): $\ln(\text{Imports}_t) = -1.5036 + 1.2519 \cdot \ln(\text{Throughput}_t)$ ($R^2 = 0.9964, p < 0.0001, \text{HAC SE} = 0.0288$).
  - Stationary First Differences (MOD-07): $\Delta \text{Imports}_t = 0.516 + 0.9406 \cdot \Delta \text{Throughput}_t$ ($R^2 = 0.9382, p < 0.0001$).
  - Crude Accounting Residual Analysis: Unreconciled residual averaged +4.5122 MMT annually (std = 1.357 MMT; min = +0.366 MMT in FY22, max = +6.926 MMT in FY16). Formally presented as an unmeasured inventory/logistics residual.
- **4.3 Econometric Testing of the Domestic Crowding-Out Hypothesis:**
  - Bivariate Level Regression (MOD-03): $\hat{\beta} = +2.1961, \text{HAC SE} = 6.5387, p = 0.7399, R^2 = 0.0092$.
  - Bivariate Log-Log Regression (MOD-04): $\hat{\beta} = +0.8670, \text{HAC SE} = 1.7143, p = 0.6177, R^2 = 0.0200$.
  - Statistical Decision: Observational data fail to reject the null hypothesis of no linear relationship at conventional significance levels. No claim of causal absence of crowding out.
  - Multivariate Accounting Substitution (MOD-05): Controlling for throughput, $\hat{\beta}_{P} = -0.8475$ ($p < 0.0001$), confirming accounting identity substitution.
- **4.4 Downstream Product Trade Balance and Refining Coverage:**
  - Product output expanded from 68.41 MMT to 276.06 MMT (+5.56% CAGR).
  - Product consumption expanded from 84.76 MMT to 234.26 MMT (+4.08% CAGR).
  - Downstream Product Coverage Ratio: Surpassed 100% in FY 2000–01 (110.69%) and reached 117.84% in FY 2023–24.
  - Net product trade balance maintained continuous export surplus since FY 2001–02, exporting 62.59 MMT against 48.69 MMT imports (+13.90 MMT net export balance in FY24).
- **4.5 Product-Level Structural Asymmetries:**
  - *Automotive Transport Fuels:* Massive physical export surpluses in Diesel / HSD (+28.16 MMT net exports in FY24) and Petrol / MS (+12.76 MMT net exports).
  - *Clean Cooking Transition:* Dramatic collapse of Kerosene / SKO consumption (-95.5%, from 10.60 MMT in FY99 to 0.48 MMT in FY24) alongside massive expansion of LPG consumption (+488.5%, from 5.04 MMT to 29.66 MMT).
  - *LPG Deficit Arithmetic:* LPG gross imports of 18.51 MMT against domestic production of 12.78 MMT and consumption of 29.66 MMT generated a net trade deficit of -17.99 MMT.
  - LPG Gross Import Dependence ($\text{GID}$) reached 62.41%; Net Import Dependence ($\text{NID}$) reached 60.64% in FY 2023–24.
- **4.6 Import Value, Realized Unit Values, and Price Decoupling:**
  - Value decoupling: In US$ terms, crude import bill surged from $3.52B to $133.37B (+3,691%); in INR terms, from Rs. 14,917 crore to Rs. 11,05,176 crore (+7,309%).
  - Price vs. volume contribution: Log-linear decomposition confirming import expenditure variation was driven primarily by international crude price cycles ($r = 0.895$ with Indian Basket FOB) and currency depreciation.

---

### Section 5: Discussion
- **5.1 Upstream Stagnation and Policy Regimes:**
  - Discussion of NELP/HELP outcomes: Contextualizing stagnant production within geological complexity, mature field decline (Bombay High), and deepwater offshore gestation lags, rather than asserting pure policy failure.
- **5.2 Downstream Refining Orientation and the Export Surplus:**
  - Why India expanded refining beyond domestic absorption: Scale economies, coastal private refining complexes (Reliance, Nayara), and high complexity indices designed to process heavy/sour discount crudes for global export markets.
  - Comparison with international literature on export refining hubs (Singapore, South Korea).
- **5.3 Product-Level Asymmetries and the Clean Cooking Paradox:**
  - Integrating household energy policy (PMUY) with macro supply-chain constraints.
  - Addressing refinery yield realities: Refining crude yields ~4.8% LPG by weight; domestic refining alone could not scale to meet +488% household demand without creating immense transport fuel oversupply.
  - Policy implication: Need for multidimensional clean cooking diversification (piped natural gas, induction cooking).
- **5.4 Geopolitical Risk and Strategic Petroleum Reserves:**
  - Re-evaluating the Supply-Pool Import Share (88.86%) in light of recent trade realignments (Russian crude inflows post-2022).
  - Discussion of the unreconciled crude accounting residual (+4.51 MMT mean) and the operational necessity for commercial and strategic crude buffers (ISPRL).

---

### Section 6: Conclusion
- **6.1 Synthesis of Empirical Findings:**
  - Recapitulation of the decoupled upstream/downstream trajectories.
- **6.2 Strategic and Policy Implications:**
  - Import dependence must be analyzed as a two-tier phenomenon: physical feedstock exposure vs. product-level trade balances.
  - Enhancing energy security requires targeting specific product deficits (LPG) rather than treating "petroleum" as a homogeneous commodity.
- **6.3 Study Limitations:**
  - Annual observation frequency ($N=26$) limits high-order dynamic modeling.
  - Reliance on aggregate national balances rather than refinery-level operational slates.
  - Lack of independent measured annual time-series for refinery crude tank farm inventories and pipeline line-fill.

---

### Section 7: References
- Complete list of **29 verified authentic peer-reviewed publications** formatted strictly in APA 7th edition (from `Phase_9B_Reference_Audit.csv`).
- 0 unverified citations; 0 synthetic references; 100% verified DOI URLs.

---

### Section 8: Acknowledgement *(Placeholder for Phase 10)*
- Standard institutional acknowledgement of PPAC, MoPNG data repositories, university infrastructure, and academic advisory guidance.

### Section 9: Conflict of Interest
- Formal declaration: The author declares that there are no financial, personal, or professional conflicts of interest that could have appeared to influence the work reported in this paper.

### Section 10: Funding Statement
- Formal declaration: This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

### Section 11: Author Contributions
- CRediT Taxonomy Specification:
  - *Conceptualization:* Project formulation and research questions.
  - *Data Curation:* Extraction, standardization, and audit of 26-year supply-chain datasets.
  - *Formal Analysis:* Econometric modeling, indicator calculation, and sensitivity audits.
  - *Writing – Original Draft:* To be executed in Phase 10.
  - *Writing – Review & Editing:* Phase 9B quality control and methodological harmonization.

---

## 3. Mandatory Planned Tables and Figures

The revised plan includes 6 core tables and 6 core figures, ensuring complete empirical coverage without artificial padding:

| Item ID | Type | Title / Caption | Mapping to Section | Key Audited Variables Included |
| :--- | :--- | :--- | :--- | :--- |
| **Table 1** | Table | Core Petroleum Supply-Chain Annual Panel (Benchmark Years) | Section 3.2 | $P_c, M_c, R_t$, Products Output, Products Consumption, Imports, Exports (MMT) |
| **Table 2** | Table | Upstream and Midstream Crude Indicators (FY99 to FY24) | Section 4.1 | Production-to-Throughput Gap, SPS (%), IRR (%), SSR (%) |
| **Table 3** | Table | Econometric Regression Models: Crude Import Determinants | Section 4.2 & 4.3 | MOD-01 to MOD-08: Coefs, HAC SEs, $t$-stats, $p$-values, $R^2$, DW |
| **Table 4** | Table | Crude-Oil Accounting Balance and Annual Unreconciled Residual | Section 4.2 | $P_c + M_c - R_t = \text{Res}_t$ (MMT); Mean, Min, Max, Std Dev |
| **Table 5** | Table | Disaggregated Petroleum Product Balance and Trade Position (FY24) | Section 4.5 | Production, Consumption, Imports, Exports, Net Trade, GID, NID by Product |
| **Table 6** | Table | Subperiod Historical Regime Performance (4 Regimes) | Section 4.4 | Post-APM (FY99-05), High Oil (FY05-14), Low Oil (FY14-20), Geopolitical (FY20-24) |
| **Figure 1** | Figure | The Upstream-Midstream Divergence: Domestic Extraction vs Throughput | Section 4.1 | $P_c$ vs $R_t$ (MMT) and Indigenous Crude Sufficiency Ratio (%) |
| **Figure 2** | Figure | Throughput-Driven Crude Import Trajectory and Level Slope | Section 4.2 | Scatter of $M_c$ against $R_t$ with OLS regression line and residual bounds |
| **Figure 3** | Figure | Downstream Product Self-Sufficiency and Net Export Expansion | Section 4.4 | Product Production vs Consumption; Net Product Exports (MMT); Coverage Ratio (%) |
| **Figure 4** | Figure | The Clean Cooking Structural Asymmetry: LPG Deficit vs Kerosene Phase-out | Section 4.5 | LPG vs SKO consumption; LPG net imports and Import Dependence Ratio (%) |
| **Figure 5** | Figure | Automotive Transport Fuel Surpluses: Diesel and Petrol Net Exports | Section 4.5 | HSD and MS production, consumption, and growing net export surpluses |
| **Figure 6** | Figure | Import Value Surge vs Realized Unit Value Decoupling | Section 4.6 | Physical Import Volume Index vs Import Bill Index (USD and INR) |
"""

with open('05_Research_Paper/Phase_9B_Correction_Audit/Phase_9B_Revised_Manuscript_Outline.md', 'w', encoding='utf-8') as f:
    f.write(outline_content)

print("Successfully written 05_Research_Paper/Phase_9B_Correction_Audit/Phase_9B_Revised_Manuscript_Outline.md")
