# Master Manuscript Outline: Professor's Journal Template

**Document Reference:** `05_Research_Paper/manuscript/11_professor_template_manuscript_outline.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption (FY98–FY24)*  
**Date:** November 2026  
**Status:** Phase 9 Preparation Output  
**Structure Alignment:** Verbatim compliance with the structure prescribed in `Journal paper template.docx`.

---

## Master Structural Overview

The manuscript strictly follows the 11-part structural architecture stipulated by the professor's journal template:

```
+----------------------------------------------------------------------------------------------------+
|                               PROFESSOR'S JOURNAL TEMPLATE STRUCTURE                               |
+----------------------------------------------------------------------------------------------------+
|  1. Abstract                                                                                       |
|  2. Introduction (integrating 30 verified peer-reviewed citations)                                 |
|  3. Method (structured into numbered subsections 3.1 to 3.9)                                       |
|  4. Result (structured into numbered subsections 4.1 to 4.7 with Tables 1-7 & Figures 1-7)        |
|  5. Discussion (thematic comparison with literature and policy implications)                       |
|  6. Conclusion                                                                                     |
|  7. References (APA 7th edition format)                                                            |
|  8. Acknowledgement                                                                                |
|  9. Conflict of Interest                                                                           |
|  10. Funding statement                                                                             |
|  11. Author contributions                                                                          |
+----------------------------------------------------------------------------------------------------+
```

---

## Section 1: Abstract

- **Target Word Count:** 200–250 words.
- **Drafting Mandate:** Follows standard journal structure (Background, Objective, Method, Key Results, Policy Significance).
- **Core Verification Checklist for Writing Turn:**
  - [ ] State core research paradox: simultaneous escalation of crude import dependency (54.9% to 88.9%) alongside permanent net petroleum product export status (+13.89 MMT).
  - [ ] State verified time period: 26 continuous financial years (FY1997–98 through FY2023–24).
  - [ ] Summarize empirical method: Administrative data harmonization (MoPNG, PPAC, DGCI&S, RBI), Newey-West HAC econometric regressions, and Logarithmic Mean Divisia Index (LMDI-I).
  - [ ] State key numerical findings: Domestic extraction flatlined (32–38 MMT; CAGR -0.44%); refinery throughput surged +281.6% (68.5 to 261.6 MMT); crude imports pulled with near-unitary elasticity ($\beta = 1.011, R^2 = 0.998$); zero crowding-out correlation ($r = 0.096$); LPG deficit expanded to -17.99 MMT (62.7% imported); USD bill grew 38-fold and INR bill grew 74-fold due to a +3.18% p.a. currency depreciation wedge.
  - [ ] Summarize policy implication: Macroeconomic vulnerability cannot be addressed by upstream exploration alone; requires targeted downstream clean fuel substitution, electric mobility, and currency hedging.
- *Strict Phase 9 Stop Condition:* Full abstract prose will be compiled upon user approval of Phase 9 preparatory architecture.

---

## Section 2: Introduction

- **Target Word Count:** 2,000–2,500 words.
- **Mandate:** Synthesize 20–30 peer-reviewed scholarly papers, articulate the "Triple Paradox", establish 5 research questions, and outline the theoretical framework.

### 2.1 Context and Global Energy Security Paradigms
- The classical energy security paradigm: the "4 As" framework (*Ang, Choong, & Ng, 2015*).
- Limitations of scalar import-dependency ratios in economies with large merchant refining sectors (*Kruyt et al., 2009; Vivoda, 2010*).
- India's historical vulnerability ranking in cross-country oil vulnerability indices (*Gupta, 2008*).

### 2.2 The Indian Hydrocarbon Landscape: Upstream Realities vs. Downstream Ambitions
- Long-run energy-growth nexus and economic expansion in India (*Dash, Sethi, & Bal, 2018; Mallick & Agarwal, 2014*).
- Upstream policy interventions (NELP/HELP) and reserve depletion challenges (*Bhattacharyya, 2010; Mishra, Ghosh, & Kanjilal, 2023*).
- Downstream deregulation, private capital entry (RIL Jamnagar, Nayara Vadinar), and the emergence of India as an Asian refining hub (*Dixit, 2020; Azhar, 2011; Sarmah & Bal, 2021*).

### 2.3 The "Triple Paradox" of India's Petroleum Sector
- **Paradox 1 (Upstream Stagnation vs. Downstream Giant):** Domestic crude output flatlined (32–38 MMT) while refining expanded +281.6%, pulling crude imports from 39.8 MMT to 234.3 MMT.
- **Paradox 2 (Aggregate Surplus vs. Structural Clean Cooking Deficit):** India has been a net product exporter since FY02 (+13.89 MMT in FY24; massive diesel/petrol surplus), yet faces an acute 62.7% import reliance on LPG driven by PMUY clean cooking adoption (*Kar et al., 2019; Gill-Wiehl et al., 2022; Gould & Urpelainen, 2018; de la Rue du Can et al., 2019*).
- **Paradox 3 (Physical Stability vs. Compounding Financial Exposure):** Steady physical growth compounded into violent financial swings (38-fold USD bill, 74-fold INR bill) driven by global price shocks and continuous rupee depreciation (*Tiwari & Albulescu, 2016; Kanjilal & Ghosh, 2018; Kumar, 2011; Agrawal & Sinha, 2022*).

### 2.4 Research Questions (RQs)
- Articulate **RQ1** through **RQ5** (as defined in `03_research_questions_and_contribution.md`).

### 2.5 Theoretical Contribution and Paper Roadmap
- Outline how the paper addresses the 5 literature gaps identified in `06_literature_gap_and_research_positioning.md`.
- Preview the structural organization of subsequent sections.

---

## Section 3: Method

- **Structure:** Formatted strictly into numbered subsections (3.1 to 3.9) as documented in `07_methodology_register.md`.
- **Target Word Count:** 1,800–2,200 words.

### 3.1 Data Acquisition and Multi-Source Auditing Architecture
- Primary administrative sources: MoPNG IPNGS, PPAC historical registers, DGCI&S customs series, RBI financial handbooks.
- Source audit hierarchy and data triangulation.

### 3.2 Harmonization, Time-Basis Calibration, and Unit Standardization
- Standard Indian Financial Year calibration (April 1 to March 31).
- Physical unit standardization to MMT/TMT; monetary standardization to INR Cr / USD M.
- Implied exchange rate formulation: $\text{IER}_t = (\text{Value}_{\text{INR}, t} \times 10) / \text{Value}_{\text{USD}, t}$.

### 3.3 Physical Mass-Balance and Energy Flow Accounting
- Feedstock mass-balance equation: $A_{c,t} = P_{c,t} + M_{c,t} \pm \Delta S_{c,t}$.
- Refining yield transformation and fuel/loss fraction: $Q_{p,t} = R_t \cdot (1 - \lambda_t)$.
- Net product trade formulation: $\text{NPT}_t = X_{p,t} - M_{p,t}$.

### 3.4 Growth and Instability Metrics (CAGR and Trend Fitting)
- Mathematical CAGR formula across $n = 26$ years: $\text{CAGR} = (X_{t_k} / X_{t_0})^{1/n} - 1$.
- Continuous log-linear OLS trend estimation: $\ln(X_t) = \alpha + \beta t + \varepsilon_t$.

### 3.5 Supply-Chain Structural Indicators
- Crude oil import dependency ratio: $\text{CID}_t = (M_{c,t} / R_t) \times 100$.
- Physical upstream feedstock deficit gap: $\Delta_{\text{upstream}, t} = R_t - P_{c,t}$.
- Product-specific import dependency: $\text{PID}_{i,t} = (M_{i,t} - X_{i,t}) / C_{i,t} \times 100$.
- Refining coverage ratio: $\text{RCR}_t = (Q_{p,t} / C_t) \times 100$.

### 3.6 Econometric Specifications and Robustness Protocols
- ADF unit-root tests on levels and first differences.
- Newey-West HAC covariance estimator formulation ($\hat{\Omega}_{\text{HAC}}$) to correct for heteroskedasticity and autocorrelation.
- Log-log elasticity regression specifications.

### 3.7 Index Decomposition Analysis (LMDI)
- Factorization of import expenditure: $V_{\text{INR}, t} = Q_t \times P_{\text{USD}, t} \times E_t$.
- Additive LMDI-I formula with logarithmic weight function $L(V_T, V_0)$ (*Ang, 2004, 2015*).
- Multiplicative LMDI-I formula satisfying factor reversal ($D_{\text{tot}} = D_Q \cdot D_P \cdot D_E$).

### 3.8 Validation Hierarchy and Cross-Verification Framework
- Multi-tier validation protocol (Level 1 administrative, Level 2 cross-agency, Level 3 multilateral benchmarking).

### 3.9 Methodological Disclosures and Boundaries
- Lease condensate accounting disclosure.
- Ethanol blended petrol (EBP) refinery gate boundary disclosure.
- Non-causal empirical correlation and structural elasticity disclosure.

---

## Section 4: Result

- **Structure:** Formatted into 7 numbered subsections (4.1 to 4.7) as planned in `08_result_section_plan.md`.
- **Target Word Count:** 2,500–3,000 words.
- **Figures and Tables:** Exactly 7 Figures and 7 Tables (mapped from `10_figure_table_plan.csv`).

### 4.1 Long-Run Overview of India's Hydrocarbon Supply Chain (FY98–FY24)
- **Table 1:** Summary Statistics of India's Petroleum Supply Chain (FY98–FY24).
- **Figure 1:** Evolution of India's Petroleum Supply Chain (Production, Refining, Consumption, Net Trade).
- Comprehensive analysis of macro trends across 26 years.

### 4.2 Upstream Decoupling: Stagnant Domestic Production vs. Surging Crude Imports
- **Table 2:** Decoupling Econometrics: Correlation and OLS Regression.
- **Figure 2:** The Decoupling Paradox: Stagnant Extraction (32–38 MMT) vs. Surging Imports.
- Evidence of zero correlation ($r = 0.096$) and lack of crowding-out ($\beta = -0.320, p = 0.271$).

### 4.3 Downstream Expansion: Refinery Throughput as the Primary Import Engine
- **Table 3:** Throughput-Driven Crude Import Regressions and Elasticity Estimates (Newey-West HAC).
- **Figure 3:** The Refining Pull: Refinery Throughput vs. Crude Oil Imports and Physical Deficit Gap.
- Near-unitary throughput elasticity ($\beta = 1.011, R^2 = 0.998$); deficit expansion to 232.19 MMT (+549%).

### 4.4 The Refining Surplus Paradox: Emergence as a Net Product Exporter
- **Table 4:** India's Petroleum Product Trade Balance: Gross Imports, Exports, and Net Balance.
- **Figure 4:** The Product Trade Paradox: Gross Exports, Gross Imports, and Net Export Balance.
- Unbroken net product exporter status since FY02 (+13.89 MMT in FY24); refining coverage ratio of 118.4%.

### 4.5 Product-Level Asymmetries: Transport Fuel Surplus vs. LPG Clean Cooking Deficit
- **Table 5:** Product-Level Production, Trade, and Consumption Balance (FY24).
- **Figure 5:** Structural Product Divergence: Diesel/Petrol Net Exports vs. LPG Deficit.
- Disaggregated analysis: Diesel (+28.16 MMT) and Petrol (+12.76 MMT) surplus vs. LPG (-17.99 MMT deficit; 62.74% import reliance); collapse of kerosene (-95.5%).

### 4.6 Financial Exposure: Price Shocks, Currency Depreciation, and Import Bill Expansion
- **Table 6:** Historical Petroleum Import Values, Unit Values, and Rupee/Dollar Exchange Rates.
- **Figure 6:** The Compounding Financial Wedge: Physical Imports (6x) vs. USD Bill (38x) vs. INR Bill (74x).
- Analysis of 9.4-fold unit value swings ($88 to $828/MT) and +3.18% p.a. currency depreciation wedge.

### 4.7 Index Decomposition Analysis: LMDI Factorization of Volume, Price, and Currency Wedges
- **Table 7:** LMDI-I Additive and Multiplicative Decomposition of Crude Import Expenditure Changes.
- **Figure 7:** LMDI Decomposition Waterfall: Contribution of Quantity, Price, and Exchange Rate.
- Decomposition of Rs. 1,090,259 Cr increase: Price (41.1%), Quantity (29.8%), Exchange Rate (29.0%).

---

## Section 5: Discussion

- **Target Word Count:** 2,000–2,500 words.
- **Mandate:** Compare every empirical finding with the verified literature using `09_discussion_comparison_matrix.csv`.

### 5.1 Upstream Stagnation, Decoupling, and the Crowding-Out Fallacy
- Contrast flatline (32–38 MMT) with upstream failure literature (*Bhattacharyya, 2010; Mishra et al., 2023*).
- Discuss why NELP/HELP failed to move the needle.
- Reconcile statistical independence ($r = 0.096$) with policy myths of domestic substitution.

### 5.2 Downstream Industrial Policy, Merchant Refining, and Export Geopolitics
- Compare throughput surge with downstream liberalization literature (*Dixit, 2020; Azhar, 2011; Sarmah & Bal, 2021*).
- Analyze coastal private mega-refineries (RIL Jamnagar, Nayara Vadinar) as global merchant processing hubs.
- Critique traditional scalar import-dependency metrics (*Ang et al., 2015; Kruyt et al., 2009; Gupta, 2008*) that fail to account for India's net product exporter status.

### 5.3 Product-Level Asymmetries and the Clean Cooking Welfare Paradox
- Synthesize PMUY household energy access literature (*Kar et al., 2019; Gill-Wiehl et al., 2022; Gould & Urpelainen, 2018*).
- Connect micro household LPG adoption to macro refinery engineering yield limits (~4.8%) (*de la Rue du Can et al., 2019*).
- Contrast the triumph of kerosene subsidy elimination (*Rao, 2012; Jain, 2018*) with the resulting 62.7% foreign LPG import lock-in.

### 5.4 Macroeconomic Exposure, Currency Depreciation, and Price Shocks
- Relate 72.3% price volatility finding to macroeconomic shock literature (*Kumar, 2011; Tiwari & Albulescu, 2016; Kanjilal & Ghosh, 2018*).
- Analyze the compounding currency depreciation wedge (+3.18% p.a.) as an unhedged domestic fiscal drain (*Agrawal & Sinha, 2022*).

### 5.5 Policy Implications and Strategic Roadmap
- Why upstream exploration alone cannot secure India's energy future.
- Integrated downstream transition: expanding 20% ethanol blending (EBP), green hydrogen, and electric mobility for transport fuels.
- Diversifying household clean cooking beyond imported LPG: rural electric induction cooktops and piped natural gas (PNG) networks.
- Macroeconomic hedging: Bilateral rupee trade settlements, expansion of Strategic Petroleum Reserves (ISPRL Phase-II), and counter-cyclical financial hedging.

---

## Section 6: Conclusion

- **Target Word Count:** 600–800 words.
- **Key Takeaways:**
  - Recapitulation of the core empirical findings: upstream flatline, downstream refining pull, product-level asymmetry, and financial compounding.
  - Final resolution of the "Triple Paradox".
  - Methodological contributions to energy economics.
  - Research limitations and future directions (sub-annual seasonal volatility, commercial financial margins, refinery petchem integration).

---

## Section 7: References

- **Format:** APA 7th Edition.
- **Coverage:** Complete, verified bibliographic records for all 30 peer-reviewed papers cataloged in `04_literature_review_and_reference_register.csv`. Zero synthetic citations.

---

## Sections 8–11: Formal Frontmatter and Backmatter

### Section 8: Acknowledgement
```markdown
## Acknowledgement
The authors express their sincere gratitude to the Ministry of Petroleum and Natural Gas (MoPNG), Government of India, the Petroleum Planning & Analysis Cell (PPAC), the Directorate General of Commercial Intelligence and Statistics (DGCI&S), and the Reserve Bank of India (RBI) for making historical administrative and statistical data publicly accessible. The authors also thank academic mentors and departmental colleagues for valuable methodological feedback on time-series econometrics and index decomposition analysis.
```

### Section 9: Conflict of Interest
```markdown
## Conflict of Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
```

### Section 10: Funding Statement
```markdown
## Funding Statement
This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.
```

### Section 11: Author Contributions
```markdown
## Author Contributions
**Nafis (Author):** Conceptualization, Methodology, Formal Data Curation, Econometric Analysis, Index Decomposition Modeling, Visualization, Writing – Original Draft, Writing – Review & Editing.
```
