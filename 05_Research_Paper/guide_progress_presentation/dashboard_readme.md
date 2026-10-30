# Project Status Dashboard — User Guide & Architecture Documentation

**Project Title:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Artifact Path:** [`05_Research_Paper/guide_progress_presentation/project_status_dashboard.html`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/05_Research_Paper/guide_progress_presentation/project_status_dashboard.html)  
**Reporting Milestone:** Project Guide / Supervisor Progress Presentation  
**Release Date:** October 2026  

---

## 1. How to Open the Dashboard

The dashboard is engineered as a **100% self-contained, offline HTML5 application**. It requires **no local webserver**, no node/npm build step, and no active internet connection. All datasets, styling, and SVG vector rendering algorithms are fully embedded inside the single HTML document.

### Option A: Open Directly in Any Web Browser (Recommended)
1. Navigate to the project directory:  
   `c:\Users\nafis\OneDrive\Desktop\Final-Project\05_Research_Paper\guide_progress_presentation\`
2. Double-click [`project_status_dashboard.html`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/05_Research_Paper/guide_progress_presentation/project_status_dashboard.html) to launch it in your default browser (Google Chrome, Microsoft Edge, Mozilla Firefox, or Apple Safari).
3. Alternatively, copy and paste the absolute local file URI into your browser address bar:  
   ```text
   file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/05_Research_Paper/guide_progress_presentation/project_status_dashboard.html
   ```

### Option B: Open within Visual Studio Code
1. Right-click [`project_status_dashboard.html`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/05_Research_Paper/guide_progress_presentation/project_status_dashboard.html) in the VS Code file explorer.
2. Select **"Open with Live Server"** (if the extension is installed) or select **"Reveal in File Explorer"** and double-click to launch in a browser.
3. You can also view it in an integrated VS Code simple browser tab using `Ctrl + Shift + P` -> `Simple Browser: Show`.

---

## 2. Dashboard Architecture & Data Linkages

The dashboard embeds verified data extracted and standardized across Phases 1 through 8. No synthetic or simulated values are utilized.

| Dashboard Section / Chart | Source Dataset Path | Source Fields / Metrics | Description |
| :--- | :--- | :--- | :--- |
| **Executive KPI Matrix** | [`core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv)<br>[`additional_indicators.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/additional_indicators.csv) | `domestic_crude_production_mmt`<br>`crude_import_quantity_mmt`<br>`refinery_crude_processing_mmt`<br>`physical_crude_deficit_gap_mmt`<br>`crude_import_dependence_proxy_pct`<br>`crude_import_value`<br>`crude_import_value_rs_crore` | Displays baseline FY99 vs latest FY24 balances, net deltas, and compounding annual growth rates (CAGRs). |
| **Crude Supply & Refining Trajectories** | [`core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv) | `refinery_crude_processing_mmt`<br>`crude_import_quantity_mmt`<br>`domestic_crude_production_mmt` | Multi-line SVG chart illustrating the decoupling of stagnant domestic extraction from the parallel surge in refinery throughput and crude imports. |
| **Crude Deficit Gap & Coverage** | [`additional_indicators.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/additional_indicators.csv) | `physical_crude_deficit_gap_mmt`<br>`indigenous_crude_coverage_ratio_pct` | Area chart showing the physical deficit expanding from 35.78 MMT to 232.19 MMT, and indigenous coverage collapsing from 47.80% to 11.22%. |
| **Product-Wise Trade Balances (FY24)** | [`product_trade_balance.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_trade_balance.csv) | `trade_balance_mmt`<br>`import_quantity_mmt`<br>`export_quantity_mmt` | Horizontal diverging bar chart contrasting transport fuel export surpluses (Diesel, Petrol, ATF) against the structural cooking gas deficit (LPG). |
| **Cooking Fuel Shift (LPG vs SKO)** | [`product_consumption_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_consumption_dataset.csv) | `product_standardized_name`<br>`value` (TMT converted to MMT) | Tracks the six-fold scaling of LPG (+488%) and the near-total elimination of subsidized kerosene (-95.5%) across 26 fiscal years. |
| **Automotive Transport Demand** | [`product_consumption_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/product_consumption_dataset.csv) | `High Speed Diesel (HSD)`<br>`Motor Spirit (Petrol / MS)` | Dual trajectories showing gasoline outgrowing diesel, narrowing the consumption ratio from 6.75:1 to 2.41:1. |
| **Dual-Currency Import Bill** | [`core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv)<br>[`additional_indicators.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/additional_indicators.csv) | `crude_import_value`<br>`crude_import_value_rs_crore`<br>`implied_exchange_rate_inr_per_usd` | Dual-axis line chart illustrating the +3.18% p.a. Rupee depreciation compounding growth wedge. |
| **CIF Unit Value vs Indian Basket** | [`additional_indicators.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/additional_indicators.csv)<br>[`core_annual_petroleum_dataset.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/03_Processed_Data/standardized/core_annual_petroleum_dataset.csv) | `realized_cif_import_unit_value_usd_bbl`<br>`crude_price` (Indian Basket FOB $/bbl) | Tracks benchmark international pricing against realized import costs, demonstrating near-perfect co-movement ($r = 0.988$). |
| **LMDI Decomposition** | [`fig6_expenditure_decomposition_contributions.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase6/figure_data/fig6_expenditure_decomposition_contributions.csv) | `price_contribution_million_usd`<br>`quantity_contribution_million_usd`<br>`dominant_driver` | Stacked diverging bar chart demonstrating that international price swings explain 72% of inter-annual crude import bill volatility. |
| **Validation & Discrepancies** | [`variable_validation_status.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase7/variable_validation_status.csv)<br>[`discrepancy_register.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase7/discrepancy_register.csv) | `Validation Status`<br>`resolution_status` | Comprehensive audit tables documenting 10 evaluated variables and 7 systemic administrative discrepancies. |
| **Econometric Models** | [`regression_results.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/04_Analysis/phase8/regression_results.csv) | `Model ID`, `Coefficient`, `Std Error`, `t-Statistic`, `p-Value`, `Model R-Squared` | Newey-West HAC regression models quantifying throughput-import elasticity and testing the crowding-out hypothesis. |
| **Results Catalogue** | [`results_catalogue.csv`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/05_Research_Paper/guide_progress_presentation/results_catalogue.csv) | All fields | Searchable, interactive registry of 23 presentation-ready empirical findings. |

---

## 3. Mathematical Definitions & Analytical Logic

1. **Crude Import Dependence Proxy (%):**
   $$\text{Import Dependence Proxy} = \frac{\text{Crude Oil Imports (MMT)}}{\text{Domestic Crude Production (MMT)} + \text{Crude Oil Imports (MMT)}} \times 100$$
   *Note: PPAC's demand-based formula uses product consumption and refinery volumetric expansion. Our supply-side proxy strictly monitors physical feedstock exposure.*

2. **Physical Crude Supply Deficit Gap (MMT):**
   $$\text{Deficit Gap} = \text{Refinery Crude Throughput (MMT)} - \text{Domestic Crude Production (MMT)}$$
   *Represents the physical volume of crude that must be imported from foreign markets to maintain refinery utilization.*

3. **Indigenous Crude Coverage Ratio (%):**
   $$\text{Indigenous Coverage} = \frac{\text{Domestic Crude Production (MMT)}}{\text{Refinery Crude Throughput (MMT)}} \times 100$$

4. **Product Net Trade Balance (MMT):**
   $$\text{Net Trade Balance} = \text{Finished Product Exports (MMT)} - \text{Finished Product Imports (MMT)}$$
   *Positive values denote a net export surplus; negative values denote a net import deficit.*

5. **Realized CIF Import Unit Value ($/bbl):**
   $$\text{Unit Value} = \frac{\text{Crude Import Value (Million US\$)} \times 10^6}{\text{Crude Import Quantity (TMT)} \times 10^3 \times 7.33\text{ bbl/MT}}$$
   *Standard Indian conversion factor of 7.33 barrels per metric tonne applied as certified in PPAC ICR Table 9.*

6. **Logarithmic Mean Divisia Index (LMDI) Decomposition:**
   $$\Delta V = V^t - V^{t-1} = \Delta V_{price} + \Delta V_{quantity}$$
   $$\Delta V_{price} = \frac{V^t - V^{t-1}}{\ln(V^t) - \ln(V^{t-1})} \times \ln\left(\frac{P^t}{P^{t-1}}\right)$$
   $$\Delta V_{quantity} = \frac{V^t - V^{t-1}}{\ln(V^t) - \ln(V^{t-1})} \times \ln\left(\frac{Q^t}{Q^{t-1}}\right)$$

---

## 4. How to Update or Rebuild the Dashboard

If underlying standardized datasets are updated or if supervisor guidance requires modifying specific visual panels, execute the Python build script:

```powershell
python 05_Research_Paper/guide_progress_presentation/build_dashboard.py
```

The script will reload the certified CSV files from `03_Processed_Data/` and `04_Analysis/`, recompute all JSON data bundles, and overwrite `project_status_dashboard.html` with updated figures while preserving full styling and offline compatibility.

---

## 5. Critical Methodological Disclosures for Guide Review

When presenting this dashboard to the supervisor, highlight the following documented safeguards:
- **No Synthetic Data:** Every numerical figure corresponds to an official administrative filing.
- **Lease Condensate Disclosure:** Domestic crude extraction data includes lease condensate (~7.45% of upstream totals).
- **Ethanol Blending Boundary:** Motor Spirit consumption figures include depot-level bio-ethanol blending, whereas refinery output represents mineral gasoline.
- **CIF vs. FOB Distinction:** Import unit values reflect realized CIF expenses (insurance, freight, grade premium), explaining minor spreads against benchmark FOB market quotations.
- **Non-Causality Safeguard:** High statistical correlations ($r = 0.9991$ for throughput and imports) demonstrate co-movement, not structural causal mechanisms.
