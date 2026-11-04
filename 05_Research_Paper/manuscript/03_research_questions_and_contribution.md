# Research Questions, Theoretical Motivation, and Scholarly Contribution

**Project Title:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Research Phase:** Phase 9 — Manuscript Preparation  
**Target Architecture:** Professor's Journal Paper Template  
**Workspace:** `c:\Users\nafis\OneDrive\Desktop\Final-Project`  
**Date:** November 2026  

---

## 1. Context and Problem Statement

Over the past quarter-century (FY 1998-99 to FY 2023-24), India has experienced a profound structural transformation in its energy economy. Following the phased dismantling of the Administered Pricing Mechanism (APM) in 2002 and the entry of world-scale private merchant refiners, India developed one of the world's most sophisticated and expansive downstream refining complexes. Today, India ranks as the world's third-largest crude oil consumer and refiner, and simultaneously acts as a major net exporter of refined transport fuels (High Speed Diesel, Motor Spirit, and Aviation Turbine Fuel) to global markets.

However, this downstream expansion has coincided with a severe, monotonic escalation in national crude oil import dependence—surging from **54.86% in FY 1998-99 to 88.86% in FY 2023-24**. Concurrently, domestic upstream extraction has remained stagnant, household cooking fuel demand has generated an acute structural import deficit in Liquefied Petroleum Gas (LPG), and international oil price volatility has imposed massive macroeconomic strain on India's balance of payments and foreign exchange reserves.

In public discourse and generic policy commentary, India's energy vulnerability is frequently mischaracterized as a simple story of domestic field depletion colliding with rising domestic vehicular demand. Existing empirical literature, while extensive in isolated pockets (such as crude import demand elasticity or oil price macroeconomic shocks), has rarely integrated the entire physical and financial supply chain—linking upstream extraction stagnation, downstream refining capacity choices, finished product trade bifurcation, household welfare transitions, and dual-currency import expenditure dynamics—into a single, unified empirical panel.

This study formulates five core, evidence-based research questions (RQ1 through RQ5) that can be defensibly answered using the verified 26-year administrative panel assembled across Phases 1 through 8.

---

## 2. Formulation of the Five Core Research Questions

### Research Question 1 (RQ1): Upstream Extraction vs. Import Surge
* **Research Question:** To what extent has India's domestic crude oil production changed over the 1998–2024 period, and does domestic crude extraction exert any measurable crowding-out or substitution effect on crude oil physical import volumes?
* **Why It Matters:** Energy security policy often assumes that incentives for domestic extraction will directly substitute for imported crude. Determining whether domestic production actually displaces imports is essential for evaluating upstream exploration policies (NELP and HELP).
* **Variables Required:** Domestic crude oil production (including lease condensate, MMT), crude oil import quantity (MMT), constructed crude import dependence proxy (%).
* **Available Datasets:** [`core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv), [`additional_indicators.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/additional_indicators.csv).
* **Analysis Already Completed:** CAGR growth rates (-0.44% vs +7.37%), Mann-Kendall monotonic trend tests, bivariate correlation in levels ($r=0.096$) and first differences ($r=0.173$), OLS regression testing the crowding-out hypothesis ($\beta = -0.320, p=0.271$).
* **Additional Analysis Required:** None. The empirical evidence is complete and verified.
* **Expected Contribution:** Conclusively establishes the empirical decoupling between domestic crude production and crude imports. Refutes the assumption that domestic extraction fluctuations drive import variations, proving that imports are driven by downstream demand rather than upstream availability.
* **Limitations:** Official administrative data report crude oil jointly with lease condensate (~7.45% of total extraction).

---

### Research Question 2 (RQ2): Downstream Refining as the True Physical Import Driver
* **Research Question:** How has the expansion of India's domestic refining capacity and throughput reshaped the physical crude supply deficit gap, and what is the exact elasticity of physical crude imports with respect to refinery processing?
* **Why It Matters:** Demonstrates whether India's escalating crude import dependence is primarily an upstream failure or a deliberate downstream industrial policy choice to create an export-oriented refining complex.
* **Variables Required:** Refinery crude throughput (MMT), domestic crude production (MMT), crude oil imports (MMT), physical crude supply deficit gap (MMT), indigenous crude coverage ratio (%).
* **Available Datasets:** [`core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv), [`additional_indicators.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/additional_indicators.csv).
* **Analysis Already Completed:** Deficit gap tracking ($35.78 \to 232.19\text{ MMT}$, +549%), coverage ratio collapse ($47.80\% \to 11.22\%$), bivariate correlation ($r=0.9991$), log-log OLS elasticity estimation ($\beta = 1.011, R^2 = 0.998$).
* **Additional Analysis Required:** None. All calculations audited and verified.
* **Expected Contribution:** Provides precise empirical proof that refinery throughput expansion (+282%) is the true mathematical and physical engine driving crude imports, operating with near-unit elasticity ($\beta \approx 1.01$).
* **Limitations:** Distinguishes operational throughput from installed nameplate capacity; slight timing wedges occur due to crude tank inventory adjustments and transit lag.

---

### Research Question 3 (RQ3): The Product Trade Paradox (Export Surplus vs. LPG Deficit)
* **Research Question:** How does India reconcile macroscopic self-sufficiency in refined petroleum products (>117%) with an acute, growing structural import deficit in domestic cooking gas (LPG)?
* **Why It Matters:** Reveals the internal bifurcation of India's petroleum supply chain. Shows that aggregate national self-sufficiency figures mask critical vulnerabilities in essential household fuels.
* **Variables Required:** Product-wise production (MMT), product-wise exports (MMT), product-wise imports (MMT), product net trade balances (MMT), product self-sufficiency ratio (%), category-level disaggregation across 14 refined products.
* **Available Datasets:** [`product_trade_balance.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_trade_balance.csv), [`petroleum_product_level_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/petroleum_product_level_dataset.csv).
* **Analysis Already Completed:** 23-year tracking of net exporter status (peaked at +43.08 MMT in FY14; +13.89 MMT in FY24); quantification of transport fuel surpluses in FY24 (Diesel +28.16 MMT, Petrol +12.76 MMT, Jet Fuel +8.58 MMT); identification of the -17.99 MMT structural LPG deficit (62.7% imported).
* **Additional Analysis Required:** None. All product balance tables audited and cross-checked against apparent availability residuals.
* **Expected Contribution:** Documents the "Refining Paradox": India acts as a major global exporter of middle distillates while simultaneously operating as one of the world's largest finished importers of LPG. Connects this paradox directly to refinery yield configurations and chemical limitations.
* **Limitations:** Trade data disaggregated across 14 standardized streams; bunker fuels and minor specialty petrochemicals classified under "Others".

---

### Research Question 4 (RQ4): Financial Import Expenditure Volatility & Currency Depreciation
* **Research Question:** What proportion of the 38-fold increase in India's crude oil import expenditure is attributable to international crude price shocks versus physical volume growth, and how severely has Rupee depreciation compounded the domestic fiscal burden?
* **Why It Matters:** Determines whether the economic exposure of India's oil import bill is primarily a volume-control problem or an external commodity price and foreign-exchange risk problem.
* **Variables Required:** Crude import value in US$ (Million $), crude import value in INR (Rs. Crore), physical import quantity (MMT), Indian Basket crude FOB price ($/bbl), calculated CIF import unit value ($/bbl), implied exchange rate (INR/USD).
* **Available Datasets:** [`core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv), [`04_Analysis/phase6/figure_data/fig6_expenditure_decomposition_contributions.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figure_data/fig6_expenditure_decomposition_contributions.csv), [`fig7_currency_depreciation_multiplier.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figure_data/fig7_currency_depreciation_multiplier.csv).
* **Analysis Already Completed:** Dual-currency CAGR comparison (USD 15.70% vs INR 18.88%; growth wedge +3.18% p.a.); Logarithmic Mean Divisia Index (LMDI) decomposition across 25 annual transitions (price explains ~72% of annual variance); correlation of expenditure with price ($r=0.917$) vs quantity ($r=0.605$); CIF-to-FOB spread tracking ($r=0.988$).
* **Additional Analysis Required:** None. LMDI decomposition and price-spread metrics are fully verified.
* **Expected Contribution:** Separates price shocks from volume growth using index decomposition analysis (LMDI). Quantifies the compounding currency penalty (+3.18% p.a.) caused by secular Rupee depreciation, demonstrating that India faces a structural "currency-commodity double squeeze."
* **Limitations:** Calculated import unit values represent realized CIF prices across heterogeneous crude grades, not pure spot prices.

---

### Research Question 5 (RQ5): Domestic Demand Composition Shifts & Energy Welfare Policy
* **Research Question:** How have national welfare policies (such as the PAHAL DBTL and Pradhan Mantri Ujjwala Yojana) altered the composition of domestic petroleum product consumption, specifically regarding the displacement of subsidized kerosene by LPG and the changing ratio of diesel to gasoline?
* **Why It Matters:** Bridges macroeconomic supply-chain analysis with microeconomic energy access and welfare policy, illustrating how social policy interventions directly transform physical commodity trade balances.
* **Variables Required:** Product consumption series for LPG, SKO (Kerosene), HSD (Diesel), and MS (Petrol); Diesel-to-Petrol consumption ratios; annual growth rates across subperiods.
* **Available Datasets:** [`product_consumption_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_consumption_dataset.csv).
* **Analysis Already Completed:** Tracking of the -95.5% collapse in kerosene consumption (10.60 to 0.48 MMT) alongside the +488.5% scaling of LPG (5.04 to 29.66 MMT); demonstration of petrol demand outgrowing diesel (CAGR +7.94% vs +3.58%), narrowing the consumption ratio from 6.75:1 to 2.41:1.
* **Additional Analysis Required:** None. Verified against official PPAC consumption records.
* **Expected Contribution:** Provides macro empirical evidence of the clean cooking transition in India's national energy balance, showing how social welfare programs successfully eradicated subsidized kerosene while unintentionally locking in structural LPG import dependency.
* **Limitations:** Motor Spirit retail sales figures include depot-level bio-ethanol blending (12–14% in FY24).

---

## 3. Scholarly Contribution and Research Positioning

Rather than claiming to be the first study on Indian petroleum, this research positions its contribution on three clear methodological and empirical advances:

1. **Full Supply-Chain Integration:** Unlike prior studies that focus narrowly on upstream exploration (Azhar, 2011; Dixit, 2020), import demand elasticity (Ghosh, 2009; Dash et al., 2018; Mishra et al., 2023), or macroeconomic price shocks (Bhattacharya & Bhattacharyya, 2001; Mandal et al., 2012; Sarmah & Bal, 2021), this study constructs a single, unified empirical panel covering upstream extraction, downstream refining, finished product trade, household consumption, and financial expenditures over 26 settled years.
2. **Empirical Refutation of Upstream Crowding-Out:** While national policy documents frequently imply that upstream incentives will directly alleviate import reliance, this paper provides robust econometric proof that domestic extraction has had zero statistical crowding-out effect on physical crude imports ($\beta = -0.320, p=0.271$), identifying refinery throughput expansion as the primary driver ($\beta = 1.011$).
3. **Disentangling the Macro vs. Micro Energy Security Paradox:** The study documents the stark co-existence of high macroscopic self-sufficiency in refined transport fuels (>117%) with acute micro-vulnerability in domestic cooking energy (LPG at 62.7% import dependence), highlighting the unintended trade consequences of domestic welfare interventions.
