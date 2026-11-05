# Corrected Master Manuscript Outline

**Document Reference:** `05_Research_Paper/phase9a_audit/11_corrected_manuscript_outline.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Phase 9A Critical Audit Output  
**Structure Alignment:** Complies verbatim with the 11-part structure of the Professor's Journal Template (`Journal paper template.docx`), incorporating all Phase 9A corrections, tone adjustments, and methodological boundaries.

---

## Master Structural Architecture

The manuscript strictly follows the 11 mandatory sections stipulated by the professor's template, incorporating audited nomenclature, statistically defensible phrasing, and flexible display item allocation:

```
+----------------------------------------------------------------------------------------------------+
|                               PROFESSOR'S JOURNAL TEMPLATE STRUCTURE                               |
+----------------------------------------------------------------------------------------------------+
|  1. Abstract                                                                                       |
|  2. Introduction (integrating 29 verified peer-reviewed citations)                                 |
|  3. Method (numbered subsections 3.1 to 3.9)                                                       |
|  4. Result (structured subsections 4.1 to 4.7 with publication tables and figures)                 |
|  5. Discussion (thematic comparison with literature, nuanced mechanisms, and boundaries)          |
|  6. Conclusion                                                                                     |
|  7. References (APA 7th edition format; 29 authentic verified sources)                             |
|  8. Acknowledgement (pending confirmed institutional and funding details)                         |
|  9. Conflict of Interest (formal author disclosure statement)                                      |
|  10. Funding statement (formal funding status disclosure)                                          |
|  11. Author contributions (CRediT taxonomy statement pending confirmed co-authorship)             |
+----------------------------------------------------------------------------------------------------+
```

---

## Section 1: Abstract

- **Target Word Count:** 200–250 words.
- **Core Structural Components:**
  - *Context:* India's simultaneous expansion of downstream refining capacity and escalation of crude oil import dependency.
  - *Objective:* Provide an empirical, physical mass-balanced historical analysis of India's petroleum supply chain across the verified 26-year panel (FY 1998–99 to FY 2023–24).
  - *Method:* Multi-source administrative data harmonization (MoPNG, PPAC, DGCI&S, RBI), Newey-West HAC time-series regression, first-difference co-movement testing, and 3-factor Logarithmic Mean Divisia Index (LMDI-I) decomposition.
  - *Key Empirical Results:*
    - Domestic crude production remained confined within a narrow band of 32.00–38.09 MMT (CAGR -0.44% p.a.).
    - Gross crude imports expanded +488.5% (39.81 to 234.26 MMT; CAGR +7.35% p.a.).
    - Supply-Pool Import Share escalated from 54.86% to 88.86%, while the Import-to-Throughput ratio rose from 58.08% to 89.57%.
    - Observational regressions fail to reject the null hypothesis of no linear relationship between domestic extraction and crude imports ($\hat{\beta} = -0.3204, p = 0.2713$), indicating an absence of empirical crowding-out.
    - Refinery throughput expanded +281.6% (68.54 to 261.55 MMT), exhibiting near-unitary elasticity with crude imports ($\hat{\alpha}_1 = 1.011, R^2 = 0.9982$).
    - Refined product trade maintained an unbroken annual net export surplus since FY 2001–02 (+13.89 MMT in FY 2023–24), driven by large surpluses in diesel (+28.16 MMT) and petrol (+12.76 MMT), even while LPG experienced an acute structural deficit (-17.99 MMT; 62.74% imported).
    - Crude import expenditure grew 37.9-fold in USD ($3,518M to $133,366M) and 74.1-fold in INR (Rs. 14,917 Cr to Rs. 1,105,176 Cr), driven by international price shocks compounded by a +3.14% to +3.18% p.a. currency depreciation wedge.
    - LMDI-I decomposition reveals price effects (43.27%) and volume effects (41.17%) dominate long-run expenditure growth, with currency depreciation contributing 15.56% (zero closure residual).
  - *Academic Significance:* Demonstrates that physical crude import exposure was driven primarily by downstream refining expansion and domestic demand growth rather than upstream depletion.
- *Status:* **Drafting deferred until Phase 10 authorization.**

---

## Section 2: Introduction

- **Target Word Count:** 2,000–2,500 words.
- **Tone Mandate:** Analytical, objective, non-polemical. Avoid treating the "Triple Paradox" as established theory; use it strictly as an empirical organizing motif. Avoid unqualified assertions regarding the "failure" of exploration policies (NELP/HELP).

### 2.1 The Conceptual Challenge of National Energy Security
- Review multi-dimensional energy security concepts: the 4-As framework (*Ang, Choong, & Ng, 2015*).
- Limitations of scalar import-dependency ratios in economies with large merchant conversion sectors (*Kruyt et al., 2009; Vivoda, 2010*).
- India's historical vulnerability ranking in cross-country oil vulnerability indices (*Gupta, 2008*).

### 2.2 The Indian Hydrocarbon Landscape: Upstream Realities and Downstream Transformation
- Economic growth, industrialization, and liquid fuel demand in India (*Dash, Sethi, & Bal, 2018; Ghosh, 2006*).
- Historical upstream exploration governance: reserve accretion, mature field depletion, and institutional challenges (*Bhattacharyya, 2010; Azhar, 2011; Dixit, 2021*).
- Downstream sector expansion, coastal private refinery development (Jamnagar, Vadinar), and India's role as an Asian refining hub (*Sarmah & Bal, 2021; Shalu et al., 2023*).

### 2.3 The "Triple Paradox" as an Empirical Organizing Framework
Present the three core empirical tensions not as theoretical laws, but as observed supply-chain phenomena:
1. *Upstream Stagnation vs. Downstream Expansion:* Domestic extraction remained stagnant (32–38 MMT) while refining expanded nearly fourfold (+281.6%), pulling crude imports from 39.8 MMT to 234.3 MMT.
2. *Aggregate Product Surplus vs. Specific Stream Deficits:* India maintained net product export surpluses every year since FY02 (+13.89 MMT in FY24), but experienced an acute, growing deficit in clean cooking LPG (-17.99 MMT; 62.7% imported) (*Kar et al., 2019; Gill-Wiehl et al., 2022; Gould & Urpelainen, 2018; de la Rue du Can et al., 2019*).
3. *Physical Quantity Stability vs. Compounding Financial Volatility:* Physical import growth (+7.35% CAGR) compounded into dramatic financial expenditure swings (USD bill grew 38-fold, INR bill grew 74-fold) due to global price volatility and steady rupee depreciation (*Tiwari & Albulescu, 2016; Ghosh, 2009; Kanjilal & Ghosh, 2018; Kumar, 2009*).

### 2.4 Research Questions (RQ1–RQ5)
- State the 5 core research questions established in `03_research_questions_and_contribution.md`.

### 2.5 Paper Contributions and Structural Roadmap
- Articulate the paper's empirical contributions in resolving the 5 literature gaps (`06_literature_gap_and_research_positioning.md`).

---

## Section 3: Method

- **Target Word Count:** 1,800–2,200 words.
- **Structure:** Numbered subsections 3.1 through 3.9, incorporating the exact equations validated in `08_equation_and_calculation_validation.csv`.

### 3.1 Data Acquisition and Administrative Source Architecture
- Primary administrative sources: MoPNG *Indian Petroleum & Natural Gas Statistics*, PPAC historical registers, DGCI&S foreign trade data, and RBI reference exchange rates.
- Multi-tier audit hierarchy and data reconciliation.

### 3.2 Harmonization, Time-Basis Calibration, and Unit Standardization
- Standard Indian Financial Year calibration (April 1 to March 31).
- Specification of the common balanced 26-year historical panel (**FY 1998–99 to FY 2023–24**). Footnote disclosing that FY 1997–98 is excluded from supply-chain modeling due to missing upstream/refining data.
- Units: Physical in MMT and TMT; financial in INR Crore and USD Million; implied exchange rate formulation ($\text{IER}_t = (\text{Value}_{\text{INR}} \times 10) / \text{Value}_{\text{USD}}$).

### 3.3 Physical Mass-Balance and Energy Flow Accounting
- True physical crude mass-balance equation:
  $$R_t = P_{c,t} + M_{c,t} - X_{c,t} - \Delta S_{c,t} - \theta_{c,t}$$
  Explicitly disclosing that $(R_t - P_{c,t})$ represents the domestic production-to-throughput gap, and that actual imports exceed this gap by $\sim 4.41\text{ MMT/yr}$ due to inventory builds, pipeline line-fill, and transit losses.
- Refining yield transformation and fuel/loss fraction: $Q_{p,t} = R_t \cdot (1 - \lambda_t)$.
- Refined product net trade: $\text{NPT}_t = X_{p,t} - M_{p,t}$.

### 3.4 Growth Metrics and Transition Calibration
- CAGR formula across $n = 25$ one-year compounding intervals:
  $$\text{CAGR} = (X_{\text{FY24}} / X_{\text{FY99}})^{1/25} - 1$$
- Continuous log-linear OLS trend fitting: $\ln(X_t) = \alpha + \beta t + \varepsilon_t$.

### 3.5 Disambiguated Supply-Chain Vulnerability Indicators
- **Supply-Pool Import Share:** $\text{SPS}_t = \frac{M_{c,t}}{P_{c,t} + M_{c,t}} \times 100$ (54.86% to 88.86%).
- **Import-to-Throughput Ratio:** $\text{IRR}_t = \frac{M_{c,t}}{R_t} \times 100$ (58.08% to 89.57%).
- **Indigenous Crude Sufficiency Ratio:** $\text{SSR}_t = \frac{P_{c,t}}{R_t} \times 100$ (47.80% to 11.22%).
- **Product-Specific Import Dependency:** $\text{PID}_{i,t} = \frac{M_{i,t} - X_{i,t}}{C_{i,t}} \times 100$.
- **Refining Coverage Ratio:** $\text{RCR}_t = \frac{Q_{p,t}}{C_t} \times 100$.

### 3.6 Econometric Specifications and Time-Series Co-Movement
- Bivariate Pearson and Spearman correlations in raw levels and first differences ($\Delta X_t = X_t - X_{t-1}$).
- OLS specifications for testing crowding-out ($M_c$ on $P_c$) and throughput pull ($M_c$ on $R$).
- Newey-West HAC covariance estimator formulation with Bartlett kernel truncation lag $m = 2$.
- **Mandatory Disclosure:** Transparent statement that stationarity was addressed via first-difference co-movement and HAC corrections; no ADF unit-root tests were performed.
- Non-causality disclosure: observational regressions establish empirical associations and elasticities, not structural exogenous causality.

### 3.7 Index Decomposition Analysis (LMDI)
- Formal 3-factor factorization of domestic import expenditure: $V_{\text{INR}, t} = Q_t \times P_{\text{USD}, t} \times E_t$.
- Additive LMDI-I formulas with logarithmic weight $L(V_T, V_0)$ (*Ang, 2004, 2015*), demonstrating exact zero residual.

### 3.8 Validation Hierarchy and Cross-Verification Framework
- Multi-tier validation protocol (Level 1 administrative, Level 2 customs trade, Level 3 multilateral benchmarking).

### 3.9 Methodological Disclosures and Accounting Boundaries
- Inclusion of lease condensate in domestic crude production ($P_c$).
- Exclusion of depot-level bio-ethanol blending from refinery-gate motor spirit production.

---

## Section 4: Result

- **Target Word Count:** 2,800–3,200 words.
- **Display Items:** Tables and Figures allocated logically to support findings (without artificial mandates requiring exactly 7 tables and 7 figures).

### 4.1 Long-Run Overview of India's Hydrocarbon Supply Chain (FY99–FY24)
- Presentation of summary statistics across the verified 26-year panel (**Table 1**).
- Comprehensive visualization of domestic extraction, crude imports, refinery throughput, consumption, and net trade (**Figure 1**).

### 4.2 Upstream Decoupling: Stagnant Production vs. Surging Crude Imports
- Presentation of correlation and Newey-West HAC regression results (**Table 2**).
- Visualization of the upstream corridor (32–38 MMT) contrasted with gross import volumes (**Figure 2**).
- Statistically accurate reporting: failure to reject the null hypothesis of no linear relationship ($\hat{\beta} = -0.3204, p = 0.2713$); no evidence of crowding-out.

### 4.3 Downstream Expansion: Refinery Throughput as the Primary Import Engine
- Throughput-driven import regression: near-unitary elasticity ($\hat{\alpha}_1 = 1.011, R^2 = 0.9982$) (**Table 3**).
- Visualization of refinery throughput, crude imports, and the expanding production-to-throughput gap (**Figure 3**).
- Expansion of the production-to-throughput gap (+549.0%, from 35.78 to 232.19 MMT) with explicit footnote explaining the ~4.41 MMT logistical wedge.

### 4.4 The Refining Surplus: Persistent Net Product Exporter Status
- Longitudinal product trade balance table: gross imports, gross exports, and net balance (**Table 4**).
- Visualization of India's transition to net product exporter status from FY02 onward (**Figure 4**).
- Analysis of the refining coverage ratio (118.37% in FY24; peak 139.38% in FY14).

### 4.5 Product-Level Asymmetries: Transport Fuel Surplus vs. Clean Cooking Deficit
- Comprehensive product-level mass-balance table for FY24 (**Table 5**).
- Visualization of structural divergence: massive export surpluses in diesel (+28.16 MMT) and petrol (+12.76 MMT) vs. acute deficit in LPG (-17.99 MMT) (**Figure 5**).
- Clean cooking transition: collapse of kerosene (-95.5%) vs. scaling of LPG (+488.5%; 62.74% imported). Clarification that LPG import dependence is driven by crude distillation yield limits (~4.8%) relative to current cooking fuel choices.
- Automotive fuel demand divergence: petrol CAGR (+7.94%) outpacing diesel (+3.58%).

### 4.6 Macroeconomic Exposure: Price Shocks, Currency Depreciation, and Import Bills
- Historical trade expenditure values, CIF unit values, and exchange rates (**Table 6**).
- Visualization of the compounding financial wedge: physical imports (5.9x) vs. USD bill (37.9x) vs. INR bill (74.1x) (**Figure 6**).
- Analysis of unit value swings ($88 to $828/MT) and the +3.14% to +3.18% p.a. currency depreciation compounding penalty.

### 4.7 Index Decomposition Analysis: LMDI Factorization of Expenditure Growth
- Additive and multiplicative LMDI-I decomposition table (**Table 7**).
- Waterfall decomposition graphic (**Figure 7**).
- Reconciled exact percentage shares: Price effect (43.27%), Quantity effect (41.17%), Exchange rate effect (15.56%), with exact closure to Rs. 1,090,259 Crore.

---

## Section 5: Discussion

- **Target Word Count:** 2,200–2,500 words.
- **Tone Mandate:** Nuanced, objective comparison with published literature. Avoid prescriptive policy mandates unsupported by the data.

### 5.1 Upstream Stagnation and the Decoupling Reality
- Compare flatline (32–38 MMT) with upstream literature (*Bhattacharyya, 2010; Mishra et al., 2023; Dash et al., 2018*).
- Contextualize upstream licensing challenges (*Azhar, 2011; Dixit, 2021*) without making sweeping claims that exploration policies "failed".
- Reconcile lack of crowding-out ($\hat{\beta} = -0.3204, p = 0.2713$) with conventional policy narratives.

### 5.2 Downstream Industrial Policy and Merchant Export Refining Dynamics
- Contextualize throughput surge with downstream literature (*Sarmah & Bal, 2021; Shalu et al., 2023*).
- Analyze coastal private mega-refineries as export-oriented conversion hubs capturing regional crack spreads.
- Critique scalar import-dependency metrics (*Ang et al., 2015; Kruyt et al., 2009; Gupta, 2008*) that treat India as purely import-dependent while ignoring net product export capacity.

### 5.3 Product-Level Asymmetries and Clean Cooking Policy Interactions
- Synthesize household energy access studies (*Kar et al., 2019; Gill-Wiehl et al., 2022; Gould & Urpelainen, 2018*).
- Connect household LPG adoption to refinery crude distillation yield configurations (*de la Rue du Can et al., 2019*).
- Note that while LPG yield limits make imports unavoidable under current fuel choices, alternative clean cooking vectors (piped natural gas, induction cooktops) represent technological substitutes.
- Contrast kerosene subsidy phase-out (*Rao, 2012; Jain, 2018; Acharya & Sadath, 2017*) with the resulting LPG import exposure.

### 5.4 Macroeconomic Vulnerability, Terms-of-Trade, and Currency Wedges
- Relate price volatility findings to macroeconomic oil shock literature (*Kumar, 2009; Tiwari & Albulescu, 2016; Kanjilal & Ghosh, 2018*).
- Analyze the compounding currency depreciation wedge (+3.14% to +3.18% p.a.) as an unhedged domestic fiscal burden.
- Assess Strategic Petroleum Reserve adequacy (5.33 MMT Phase-I) against gross import scale (*Agrawal & Sinha, 2022*).

### 5.5 Analytical Limitations and Future Research Directions
- Explicitly acknowledge limitations: annual aggregation smoothing sub-annual price volatility; lack of commercial refinery-level margin data (GRMs); exclusion of post-FY24 provisional observations.
- Propose future research: high-frequency financial modeling of crack spreads, petchem integration, and electric mobility substitution curves.

---

## Section 6: Conclusion

- **Target Word Count:** 600–800 words.
- **Key Takeaways:**
  - Synthesis of verified empirical realities: 26-year upstream stagnation, downstream refining pull, transport surplus vs. cooking deficit, and currency compounding.
  - Final resolution of how downstream industrial policy decoupled crude import exposure from domestic upstream extraction.
  - Methodological takeaways for energy security accounting in refining hub economies.

---

## Section 7: References

- **Format:** APA 7th Edition.
- **Coverage:** Complete, verified bibliographic records for all **29 authentic peer-reviewed publications** cataloged in `05_literature_corrections_and_replacements.md`. Excludes unverified citation (LIT-27). Zero synthetic citations.

---

## Sections 8–11: Frontmatter and Backmatter Disclosures

In accordance with strict academic audit guidelines, these sections will contain objective statements and avoid inventing unauthorized personal details:

### Section 8: Acknowledgement
```markdown
## Acknowledgement
The authors express their sincere gratitude to the Ministry of Petroleum and Natural Gas (MoPNG), Government of India, the Petroleum Planning & Analysis Cell (PPAC), the Directorate General of Commercial Intelligence and Statistics (DGCI&S), and the Reserve Bank of India (RBI) for maintaining and publishing historical administrative and statistical datasets. Academic mentors and institutional reviewers are acknowledged for constructive feedback on data harmonization and index decomposition methodologies. [Author to insert specific institutional acknowledgements prior to submission].
```

### Section 9: Conflict of Interest
```markdown
## Conflict of Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
```

### Section 10: Funding Statement
```markdown
## Funding Statement
This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. [Author to confirm whether institutional fellowship or departmental support applies].
```

### Section 11: Author Contributions
```markdown
## Author Contributions
**Nafis (Lead Author):** Conceptualization, Data Curation, Econometric Methodology, Formal Analysis, Validation, Visualization, Writing – Original Draft, Writing – Review & Editing. [Author to confirm whether project guide or collaborators should be added under CRediT taxonomy prior to submission].
```
