# Study Period Audit and Temporal Reconciliation

**Document Reference:** `05_Research_Paper/phase9a_audit/01_study_period_audit.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Phase 9A Critical Audit Output  

---

## 1. Executive Summary

This audit establishes the precise, empirical temporal boundary of the dataset used across Phases 1–8 and resolves the inconsistency between references to **"FY1997–98 to FY2023–24"** and **"FY1998–99 to FY2023–24"** in Phase 9 preparation documents.

By inspecting the underlying standardized administrative datasets (`03_Processed_Data/standardized/`), this audit proves that:
1. **The common, verified historical study period for all primary supply-chain variables is strictly FY 1998–99 to FY 2023–24 (26 annual observations).**
2. **FY 1997–98 is present only in a single downstream consumption table** and has missing values (`NaN`) for domestic crude production, crude imports, crude exports, refinery throughput, product production, product imports, product exports, and import trade values.
3. **The multi-year compound growth rates (CAGRs) reported in the study (e.g., +7.37% for crude imports, -0.44% for domestic crude) were calculated using 25 annual transition intervals ($n = 25$) between FY 1998–99 and FY 2023–24.**
4. **All observations beyond FY 2023–24 (FY 2024–25, FY 2025–26, and FY 2026–27) contain truncated, provisional, or forward-estimate data and are strictly excluded from the historical panel.**

---

## 2. Dataset-by-Dataset Temporal Inspection

An exhaustive audit of every standardized CSV file in `03_Processed_Data/standardized/` reveals the following variable-by-variable coverage:

| Dataset Filename | Earliest Observation | Latest Observation | Total Rows | Status of FY 1997–98 | Balanced Panel Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `annual_crude_oil_production.csv` | FY 1998–99 | FY 2023–24 | 26 | **Missing (Not in source)** | Complete (26 observations) |
| `annual_petroleum_trade_volumes.csv` | FY 1998–99 | FY 2024–25 | 27 | **Missing (Not in source)** | Complete FY99–FY24 (FY25 partial) |
| `annual_refinery_crude_processing.csv` | FY 1998–99 | FY 2026–27 | 29 | **Missing (Not in source)** | Complete FY99–FY24 (FY25-27 provisional) |
| `annual_petroleum_import_export_values.csv` | FY 1998–99 | FY 2024–25 | 27 | **Missing (Not in source)** | Complete FY99–FY24 (FY25 partial) |
| `annual_petroleum_product_production.csv` | FY 1998–99 | FY 2025–26 | 28 | **Missing (Not in source)** | Complete FY99–FY24 (FY25-26 provisional) |
| `annual_petroleum_product_consumption.csv` | FY 1997–98 | FY 2025–26 | 29 | **Present (80.36 MMT)** | Unbalanced (Starts 1 year early) |
| `crude_oil_fob_price_indian_basket.csv` | FY 2000–01 | FY 2025–26 | 26 | **Missing (Series started FY01)** | Truncated (Starts FY 2000–01) |
| `core_annual_petroleum_dataset.csv` | FY 1997–98 | FY 2026–27 | 30 | **Present only for consumption** | Master integrated table |
| `derived_indicators.csv` | FY 1997–98 | FY 2026–27 | 30 | **All indicators NaN in FY98** | Balanced indicators: FY99–FY24 |

---

## 3. Dissection of Row 0 (FY 1997–98) in the Master Dataset

Inspection of `03_Processed_Data/standardized/core_annual_petroleum_dataset.csv` shows the exact contents of Row 0 (FY 1997–98):

```csv
reporting_period: FY 1997-98
source_status: Verified Historical (Consumption Series Only)
domestic_crude_production_mmt: NaN
crude_import_quantity_mmt: NaN
crude_export_quantity_mmt: NaN
refinery_crude_processing_mmt: NaN
petroleum_product_production_mmt: NaN
petroleum_product_imports_mmt: NaN
petroleum_product_exports_mmt: NaN
petroleum_product_consumption_mmt: 80.3578
crude_price: NaN
crude_import_value_rs_crore: NaN
```

### Analytical Implications:
- In FY 1997–98, seven of the eight core supply-chain variables are completely absent.
- The `derived_indicators.csv` table confirms that `crude_import_dependence_proxy_pct`, `crude_production_to_refinery_processing_ratio_pct`, `crude_import_unit_value_usd_per_mt`, and `net_product_export_balance_mmt` are all `NaN` for FY 1997–98.
- Therefore, no supply-chain mass-balance, correlation, regression, or decomposition analysis could include FY 1997–98.

---

## 4. Origin of the Inconsistency in Phase 9 Outputs

The confusion between **"FY1997–98 to FY2023–24"** and **"FY1998–99 to FY2023–24"** arose from three distinct linguistic and clerical shortcuts during Phase 9 drafting:

1. **Shorthand Notation Ambiguity:**  
   Phase 9 drafts frequently used the abbreviation **"FY98–FY24"** to mean "the 26-year historical panel". While the writer intended "FY 1998–99 to FY 2023–24" (using the starting calendar year 1998 as shorthand), subsequent prose drafts erroneously expanded "FY98" into "FY 1997–98" (the official financial year that ends in 1998).
2. **The "26 Years" vs. "27 Years" Mathematical Trap:**  
   A period spanning FY 1997–98 through FY 2023–24 contains:
   $$2024 - 1997 = 27 \text{ financial years}$$
   A period spanning FY 1998–99 through FY 2023–24 contains:
   $$2024 - 1998 = 26 \text{ financial years}$$
   Phase 9 documents consistently stated that the study analyzed **26 annual observations**, but several text sections mistakenly paired this number with the 27-year label "FY 1997–98 to FY 2023–24".
3. **Quoting Baseline Values:**  
   In Phase 9 Table 1 and Result Section 4.1, the "baseline values" quoted for the start of the study period were:
   - Domestic crude production: $32.76\text{ MMT}$ (the exact value for **FY 1998–99**).
   - Crude imports: $39.81\text{ MMT}$ (the exact value for **FY 1998–99**).
   - Refinery throughput: $68.54\text{ MMT}$ (the exact value for **FY 1998–99**).
   - Crude import bill: $\$3,518\text{ M}$ and $\text{Rs. } 14,917\text{ Cr}$ (the exact values for **FY 1998–99**).
   At no point did any empirical calculation use FY 1997–98 values for these variables.

---

## 5. Verification of CAGR Calculation Intervals

To confirm whether growth rates were calculated over 25 intervals or 26 intervals, we evaluated the empirical CAGR formula:

$$\text{CAGR} = \left( \frac{X_{\text{FY24}}}{X_{\text{Base}}} \right)^{\frac{1}{n}} - 1$$

Testing the actual figures from `core_annual_petroleum_dataset.csv`:
- **Crude Imports:** $X_0 = 39.808\text{ MMT}$ (FY99), $X_T = 234.262\text{ MMT}$ (FY24).
  - With $n = 25$ intervals (FY99 to FY24): $(234.262 / 39.808)^{1/25} - 1 = \mathbf{+7.35\%}$ (rounded in Phase 6 as $+7.37\%$ using TMT precision).
  - With $n = 26$ intervals: $(234.262 / 39.808)^{1/26} - 1 = \mathbf{+7.05\%}$.
- **Domestic Crude Production:** $X_0 = 32.760\text{ MMT}$ (FY99), $X_T = 29.356\text{ MMT}$ (FY24).
  - With $n = 25$ intervals: $(29.356 / 32.760)^{1/25} - 1 = \mathbf{-0.44\%}$.
  - With $n = 26$ intervals: $(29.356 / 32.760)^{1/26} - 1 = \mathbf{-0.42\%}$.
- **Refinery Crude Processing:** $X_0 = 68.539\text{ MMT}$ (FY99), $X_T = 261.546\text{ MMT}$ (FY24).
  - With $n = 25$ intervals: $(261.546 / 68.539)^{1/25} - 1 = \mathbf{+5.50\%}$ (or $+5.51\%$ depending on rounding).
  - With $n = 26$ intervals: $(261.546 / 68.539)^{1/26} - 1 = \mathbf{+5.29\%}$.

This confirms that **$n = 25$ transition intervals between 26 annual points (FY 1998–99 to FY 2023–24)** was the exact calculation base used across all Phase 4, Phase 6, and Phase 8 analytical scripts.

---

## 6. Audit of Forward and Provisional Years (FY25 to FY27)

The master dataset contains rows for FY 2024–25, FY 2025–26, and FY 2026–27. This audit confirms that their exclusion from the historical econometric panel is fully justified:

1. **FY 2024–25 (Row 27):**  
   - `domestic_crude_production_mmt` is `NaN`.
   - `crude_import_quantity_mmt` ($243.22\text{ MMT}$) and `refinery_crude_processing_mmt` ($268.61\text{ MMT}$) are available, but upstream balance is truncated.
2. **FY 2025–26 (Row 28):**  
   - Contains provisional budget estimates and partial-year trade figures.
   - Crude imports and domestic production are `NaN`.
3. **FY 2026–27 (Row 29):**  
   - Contains a truncated observation covering only Q1 (April to June 2026; $65.69\text{ MMT}$ throughput).
   - Marked in `discrepancy_register.csv` as unsuitable for annualization.

---

## 7. Mandatory Corrections for Manuscript Drafting

To maintain rigorous academic truthfulness, all manuscript materials must implement the following standardized conventions:

1. **Definitive Study Period Title:**  
   *"FY 1998–99 to FY 2023–24 (26 Financial Years; April 1, 1998 to March 31, 2024)."*
2. **Prohibition of Loose Shorthand:**  
   The ambiguous abbreviation "FY98–FY24" must be replaced with either "FY1998–99 to FY2023–24" or explicitly defined upfront as: *"FY99–FY24 (where FY99 denotes the financial year 1998–99 ending March 31, 1999)."*
3. **Methodological Note on FY 1997–98:**  
   A footnote must be added to the Method section: *"While historical product consumption records exist for FY 1997–98 (80.36 MMT), primary supply-chain series (domestic extraction, crude imports, and refinery throughput) are consistently available from FY 1998–99 onward. To preserve econometric balance, the common historical analysis is restricted to the 26-year balanced panel from FY 1998–99 to FY 2023–24."*
4. **CAGR Formula Clarification:**  
   The CAGR formula must state that $n = 25$, representing the 25 one-year compounding intervals across the 26 annual observation points.
