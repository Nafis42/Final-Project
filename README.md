# India's Petroleum Supply Chain and Import Exposure

> **A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption (FY 1998-99 to FY 2023-24)**

[![Phases 1-8 Status](https://img.shields.io/badge/Phases%201--8-Confirmed%20Complete-059669?style=flat-square)](./05_Research_Paper/guide_progress_presentation/project_status_report.md)
[![Data Integrity](https://img.shields.io/badge/Reconciliation%20Checks-218%2F218%20PASS-2563eb?style=flat-square)](./04_Analysis/phase2/validation_report.md)
[![Primary Data](https://img.shields.io/badge/Sources-PPAC%20%7C%20MoPNG-d97706?style=flat-square)](./02_Source_Audit/file_inventory.csv)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

---

## 1. Executive Abstract

Over the past quarter-century, India has emerged as one of the world's leading petroleum refining hubs and a major net exporter of transport fuels (High Speed Diesel, Petrol, and Jet Fuel). Concurrently, the nation has experienced a sharp escalation in crude oil import dependence—rising from **54.86% in FY 1998-99 to 88.86% in FY 2023-24**—alongside an acute structural deficit in household cooking gas (Liquefied Petroleum Gas, LPG) and heightened macroeconomic sensitivity to international oil price swings.

This research project conducts a reproducible, empirical investigation into India's petroleum supply chain across 26 settled fiscal years post-dismantling of the Administered Pricing Mechanism (APM). Using administrative records published by the **Petroleum Planning and Analysis Cell (PPAC)** and the **Ministry of Petroleum and Natural Gas (MoPNG)**, the study untangles the structural mechanisms connecting upstream extraction, downstream refining expansion, finished product trade dynamics, and macroeconomic import expenditure.

---

## 2. Core Empirical Findings: The "Triple Paradox"

1. **Decoupling of Upstream Stagnation from the Import Surge (RQ1 & RQ2):**
   - Domestic crude oil production (including lease condensate) stagnated within a narrow **32.0 to 38.1 MMT** corridor (averaging $34.14\text{ MMT}$, CAGR $-0.44\%$), falling from $32.76\text{ MMT}$ (FY99) to $29.36\text{ MMT}$ (FY24).
   - In contrast, downstream refining crude throughput expanded nearly four-fold (**+281.6%**, $68.54\text{ MMT} \to 261.55\text{ MMT}$, CAGR $+5.51\%$).
   - The physical crude deficit gap ($\text{Throughput} - \text{Domestic Extraction}$) widened by **+549%** ($35.78\text{ MMT} \to 232.19\text{ MMT}$), driving physical crude imports from $39.81\text{ MMT}$ to $234.26\text{ MMT}$ (CAGR $+7.37\%$).
   - Statistical correlation between domestic extraction and imports is zero ($r = 0.096, p = 0.641$). Econometric modeling confirms domestic production does **not** crowd out imports ($\beta = -0.320, p = 0.271$).

2. **The Product Trade Paradox: Export Powerhouse vs. LPG Deficit (RQ3):**
   - India has maintained permanent net exporter status in refined products for 23 consecutive years (since FY02), with aggregate product self-sufficiency peaking at **139.38%** in FY14 ($117.84\%$ in FY24).
   - In FY 2023-24, India generated massive export surpluses in transport fuels: **Diesel (+28.16 MMT)**, **Petrol (+12.76 MMT)**, and **Aviation Turbine Fuel (+8.58 MMT)**.
   - Concurrently, household cooking gas (LPG) suffered an acute structural deficit of **-17.99 MMT** (with **62.7%** of domestic demand met by foreign imports) due to national clean-cooking welfare expansion (PMUY).

3. **Import Bill Volatility & Currency Depreciation Wedge (RQ4 & RQ5):**
   - Crude import expenditure rose 38-fold from **\$3.52B to \$133.37B** (15.70% CAGR; peak \$144.29B in FY13), and 74-fold in domestic currency from **Rs. 14,917 Crore to Rs. 1,105,176 Crore** (18.88% CAGR).
   - Logarithmic Mean Divisia Index (LMDI) decomposition reveals that inter-annual import bill variance is dominated **72% by international oil price shocks** ($r = 0.9168, p < 0.0001$), while physical import volumes anchor long-run baseline levels.
   - Continuous Indian Rupee depreciation (42.40 to 82.87 INR/USD) added a compounding growth penalty wedge of **+3.18% p.a.** in domestic currency terms.

---

## 3. Interactive Research Dashboard

The project includes a self-contained, offline-compatible HTML5 dashboard for academic presentations:

- **Location:** [`05_Research_Paper/guide_progress_presentation/project_status_dashboard.html`](./05_Research_Paper/guide_progress_presentation/project_status_dashboard.html)
- **Features:** 
  - Executive KPI matrix with verified CAGR growth rates and deltas.
  - Interactive multi-line vector SVG trajectories (Production vs. Throughput vs. Imports).
  - Product-level diverging trade balances and clean-cooking fuel transition charts (LPG vs. Kerosene).
  - Dual-currency import expenditure and LMDI price-volume decomposition panels.
  - Multi-source validation matrix and econometric robustness tables.
  - Interactive, searchable catalogue of 23 presentation-ready empirical findings.

To open, double-click `project_status_dashboard.html` in any web browser.

---

## 4. Repository Structure

```text
Final-Project/
├── 01_Original_Data/             # Primary administrative files (19 Excel workbooks, 14 PDFs)
├── 02_Source_Audit/              # Source inventories, MD5 checksums, sheet/page mappings
│   ├── file_inventory.csv
│   ├── workbook_sheet_inventory.csv
│   ├── pdf_inventory.csv
│   └── source_audit_report.md
├── 03_Processed_Data/            # Standardized and reconciled datasets
│   ├── raw_extractions/          # Cell-exact raw CSV extractions (16 files)
│   └── standardized/             # Harmonized MMT/USD panel datasets (76 files)
│       ├── core_annual_petroleum_dataset.csv
│       ├── petroleum_product_level_dataset.csv
│       ├── product_trade_balance.csv
│       ├── product_consumption_dataset.csv
│       └── core_dataset_provenance.csv
├── 04_Analysis/                  # Analytical phases & econometric models
│   ├── phase2/                   # Data dictionary & 218 reconciliation checks
│   ├── phase3/                   # Supply-chain balance audits
│   ├── phase4/                   # Macro trends, 79 CAGRs, turning points & 8 figures
│   ├── phase5/                   # Product trade balances & LPG deficit analysis & 8 figures
│   ├── phase6/                   # Financial valuation, LMDI decomposition & 8 figures
│   ├── phase7/                   # Official source verification & discrepancy register
│   └── phase8/                   # Econometric models (HAC errors), robustness & 8 figures
├── 05_Research_Paper/            # Presentation & paper drafting
│   └── guide_progress_presentation/
│       ├── project_status_dashboard.html    # Interactive HTML5 dashboard
│       ├── results_catalogue.csv            # 23 presentation-ready findings
│       ├── project_status_report.md         # Formal phase audit report
│       ├── guide_presentation_outline.md    # 10-slide academic talk outline
│       └── dashboard_readme.md              # Dashboard architecture & update guide
├── src/                          # Reproducible Python processing pipeline
│   ├── extract_raw_data.py
│   ├── standardize_data.py
│   ├── validate_data.py
│   └── build_core_supply_chain_dataset.py
├── .gitignore                    # Python, OS, and IDE ignore rules
└── README.md                     # Research overview & documentation
```

---

## 5. Research Phases & Governance

| Phase | Description | Status | Evidence / Artifacts |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Source Audit & File Inventory | **Confirmed complete** | 33 files cataloged; 198 sheets mapped; 100% readable |
| **Phase 2** | Data Extraction & Standardization | **Confirmed complete** | 16 raw CSVs; 218 balance checks passed (`PASS`) |
| **Phase 3** | Core Dataset Integration | **Confirmed complete** | 30-year panel; full cell provenance mapped |
| **Phase 4** | Macro Historical Trends & Breaks | **Confirmed complete** | 79 CAGRs; 9 turning points; 8 publication figures |
| **Phase 5** | Product Trade & Consumption | **Confirmed complete** | Diverging balances; LPG structural deficit tracked |
| **Phase 6** | Import Value & Price Analysis | **Confirmed complete** | LMDI decomposition; currency multiplier (+3.18% p.a.) |
| **Phase 7** | Official Source Verification | **Confirmed complete** | 10 priority variables evaluated; 7 discrepancies resolved |
| **Phase 8** | Econometrics & Robustness | **Confirmed complete** | Newey-West HAC models; COVID sensitivity invariant |
| **Phase 9** | Academic Paper Drafting | *Pending Review* | Scheduled post-supervisor progress presentation |

---

## 6. Reproducibility & Pipeline Execution

### Prerequisites
- Python 3.10+
- Recommended packages:
  ```bash
  pip install pandas numpy scipy matplotlib openpyxl xlrd pyarrow
  ```

### Rebuilding the Dashboard
To update the embedded data bundle and regenerate the interactive presentation dashboard:
```bash
python 05_Research_Paper/guide_progress_presentation/build_dashboard.py
```

---

## 7. Institutional Data Disclosures

To maintain strict academic integrity, several institutional definitions are explicitly disclosed:
- **Lease Condensate:** Domestic crude production includes lease condensate (~7.45% of upstream output, ~2.5 MMT/yr).
- **Bio-Ethanol Blending:** Motor Spirit (petrol) retail consumption figures include depot-level bio-ethanol blending (12–14% in FY24), whereas refinery production reflects pure mineral gasoline.
- **CIF vs. FOB Spread:** Calculated crude import unit values reflect realized CIF expenses (ocean freight, insurance, grade differentials), creating an expected spread over the benchmark FOB Indian Basket price.
- **Non-Causality:** Statistical correlations and regression coefficients establish historical co-movement and elasticity, not mechanistic macroeconomic causality.

---

## 8. Primary Data Sources

- **Petroleum Planning & Analysis Cell (PPAC)**, Ministry of Petroleum and Natural Gas (MoPNG), Government of India:
  - *Indian Petroleum & Natural Gas Statistics (IPNGS)* (Annual compendia)
  - *Monthly Reports on Petroleum & Natural Gas*
  - *Import-Export Trade Statements & Historical Prices*
- **Directorate General of Commercial Intelligence and Statistics (DGCIS)**, Ministry of Commerce and Industry.
- **Reserve Bank of India (RBI)**, Reference Exchange Rate Archive.

---

## 9. Author & Citation

**Author:** Nafis ([@nafisdmk](https://github.com/nafisdmk))  
**Academic Focus:** Energy Economics, Supply Chain Analysis, Petroleum Trade Policy  
**Project:** Academic Research Project (Phases 1–8)

```bibtex
@misc{india_petroleum_supply_chain_2026,
  author = {Nafis},
  title = {India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/nafisdmk/india-petroleum-supply-chain}}
}
```
