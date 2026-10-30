# Phase 2 Extraction Summary Report

**Project:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** Phase 2 — Data Extraction, Standardisation, and Validation  
**Date of Execution:** October 2026  
**Pipeline Status:** Verified Complete and Auditable  

---

## 1. Executive Summary & Scope Adherence

In strict adherence to the project brief and Phase 2 requirements:
- **Scope Boundary:** Phase 2 encompasses exclusively data extraction, standardization, reconciliation, and validation. No trend analysis, econometric modeling, hypothesis testing, causal inference, or research-paper drafting has been initiated.
- **Data Isolation:** All original source files in `01_Original_Data` have been preserved completely unaltered with zero in-place modifications.
- **Traceability:** Every extracted record across raw and standardized tiers retains complete provenance back to its original workbook, worksheet name, PDF page number, and source table title.
- **Dual Serialization:** Every standardized tabular dataset is published simultaneously in both interoperable comma-separated values (`.csv`) and high-performance columnar Apache Parquet (`.parquet`).

---

## 2. Classification of Source Workbooks & Files

All 33 source files in `01_Original_Data` (totaling 241 worksheets and 4 PDFs) were inspected and systematically categorized into the 5 designated operational classes:

### Class 1: Core Petroleum Supply-Chain Sources (Primary Extraction)
1. `1717395338_PT_Crude_oil_production_H.xls` — Upstream domestic crude oil production (FY 1998–99 to FY 2023–24).
2. `1788266304_PT_crude_processing_H.xls` — Downstream refinery crude processing throughput (FY 1998–99 to FY 2026–27 Till June).
3. `1761642701_PT_production_product_H.xls` — Domestic petroleum product production by category (FY 1998–99 to FY 2025–26 Apr–Sep).
4. `1751964547_PT_IMPORT_TMT_H.xlsx` — Petroleum trade physical quantities (imports and exports of crude and products, FY 1998–99 to FY 2024–25).
5. `1788343376_PT_Consumption_English.xls` — Domestic petroleum product consumption by category (FY 1997–98 to FY 2025–26).

### Class 2: Supporting Sources for Prices, Import Expenditure, Consumption & Validation
6. `1751964622_PT_IMPORT_VAL_US$_H.xlsx` — Petroleum trade values in nominal Million US$ (FY 1998–99 to FY 2024–25).
7. `1751964598_PT_IMPORT_VAL_RS.CRS._H.xlsx` — Petroleum trade values in nominal INR Crore (FY 1998–99 to FY 2024–25).
8. `1775133106_PP_Crude-Oil-FOB-Price-(Indian Basket)-Historical.xlsx` — FOB price of the Indian Crude Basket ($/bbl) and sour:sweet weighting evolution (FY 2000–01 to FY 2025–26).
9. `1787137273_Statewise_Sales-POL_Consumption_Final.xlsx` — Sub-national state-level petroleum product consumption sales (FY 2008–09 to FY 2025–26).
10. `1787315734_ICR_July 26.pdf` — PPAC Indian Petroleum & Natural Gas Monthly Report (July 2026), providing official Table 9 physical conversion factors (Metric Tonnes to Barrels).
11. `1773137026_Revised Estimates FY 2025-26_Combined.pdf` — Official PPAC demand projections and revised consumption estimates for FY 2025–26.
12. `1788266780_Flash_Report_WEB_UPLOAD_Aug26.pdf` — High-frequency monthly flash benchmark report for August 2026.

### Class 3: Potentially Relevant Secondary Sources (Duplicates, Redundant Extracts, Fiscal Context)
13. `1717395338_PT_Crude_oil_production_H (1).xls` — Verified byte-identical content copy of primary crude production workbook (retained in audit; bypassed).
14. `1788343376_PT_Consumption_English (1).xls` — Verified byte-identical content copy of primary consumption workbook (retained in audit; bypassed).
15. `1761715894_petroleum-prices-and-under-recoveries (1).xlsx` — Exact byte-level duplicate (identical SHA-256 hash).
16. `1761715894_petroleum-prices-and-under-recoveries.xlsx` — Retail price build-up, excise tariffs, and OMC under-recoveries; cataloged for secondary fiscal context.
17. `1784281292_PP_4_ContributionToExchequer.xls` — Tax contributions of petroleum sector to central and state exchequers; extracted to raw tier (`raw_contribution_to_exchequer.csv`).
18. `1679651218_163fd52aba7df0b51c90.xls` — Historical fiscal subsidy scheme 2002 on PDS kerosene and domestic LPG; extracted to raw tier (`raw_fiscal_subsidy_scheme_2002.csv`).
19. `1729493890_pt_import_en.xlsx` — Single-year monthly extract for FY 2024–25; 100% redundant with master workbook 1751964547.
20. `1729493957_val-in-dollar_en.xlsx` — Single-year monthly import value extract for FY 2024–25; 100% redundant with master workbook 1751964622.
21. `1751966513_val-in-dollar-en.xlsx` — Duplicate single-year import value extract for FY 2024–25; 100% redundant with master workbook 1751964622.
22. `1784609810_PT_IMPORT_VAL_US$_25-26.xlsx` — Single-year partial forward extract (Apr–Jun FY 2025–26); redundant with ongoing monitoring.
23. `1748348757_Foundation_Day_Report_vfinal_26052025.pdf` — PPAC 23rd Foundation Day narrative report; qualitative background, no primary tabular series.

### Class 4: Out of Scope for Main Study (Natural Gas, Micro-Retail & Customer Demographics)
24. `1781164726_NG_H_Production.xls` — Upstream natural gas production (gaseous hydrocarbon; excluded from liquid petroleum scope).
25. `1781164814_NG-H_LNG_Consumption.xlsx` — Liquefied natural gas consumption (natural gas sector).
26. `1781164918_NG-H_LNG_Import.xlsx` — LNG import volumes and values (natural gas sector).
27. `1781164918_NG-H_LNG_Import (1).xlsx` — Exact duplicate of LNG import workbook.
28. `1781859871_2_NG-H_Sectoral_Consumption.xlsx` — Natural gas sectoral consumption (power, fertilizer, CGD).
29. `1785758008_Subsidy_Natural_Gas_in_North_East_Region.xlsx` — Natural gas pipeline subsidy scheme in North Eastern region.
30. `1734585644_Dealer_Commision_MS_HSD_english_01.12. 2024.xls` — Petrol pump dealer commissions; micro-retail level.
31. `1787123639_active-domestic-cus-lpg.xlsx` — Domestic active LPG customer household connections; micro-demographic.

### Class 5: Unreadable or Unresolved Sources Requiring Attention (Container Defects & Header Anomalies)
32. `1785841030_Under_Recoveries_to_Oil_Marketing_Companies_(OMCs)_on_Sale_of_Sensitive_Petroleum_Products_Rs_Crore.xls` — Container Format Defect: Named `.xls` but contains a PK zip/OOXML stream. Safely resolved by reading into an in-memory `io.BytesIO` buffer with `openpyxl`, leaving original intact, and extracting 672 records into `raw_omc_under_recoveries_sensitive_products.csv`.
33. `1787119859_PT_Import_Val_USD.xls` — Header Anomaly: Labeled '2026-27' in worksheet title but contains FY 2025–26 monthly data. Bypassed in favor of verified master series.

---

## 3. Standardized Datasets Portfolio

The extraction pipeline produced 16 standardized datasets in `03_Processed_Data/standardized/`, each serialized as both `.csv` and `.parquet`:

| Dataset Name | Temporal Coverage | Frequency / Granularity | Records | Columns | Primary Units |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `annual_crude_oil_production` | FY 1998–99 to 2023–24 | Annual / Sectoral (ONGC, OIL, PSC) | 26 | 20 | MMT & TMT |
| `annual_refinery_crude_processing` | FY 1998–99 to 2026–27 (Till June) | Annual / Corporate Aggregates | 29 | 22 | TMT & MMT |
| `annual_refinery_crude_processing_detailed` | FY 1998–99 to 2026–27 (Till June) | Annual / Individual Refinery Units | 1,160 | 10 | TMT & MMT |
| `annual_petroleum_product_production` | FY 1998–99 to 2025–26 (Apr–Sep) | Annual / 12 Product Categories | 28 | 20 | TMT & MMT |
| `annual_petroleum_product_production_by_product` | FY 1998–99 to 2025–26 (Apr–Sep) | Long Panel by Product | 336 | 8 | TMT & MMT |
| `annual_petroleum_trade_volumes` | FY 1998–99 to 2024–25 | Annual / Crude & Product Trade Flows | 27 | 21 | TMT & MMT |
| `annual_petroleum_product_trade_by_product` | FY 1998–99 to 2024–25 | Long Panel by Traded Product | 567 | 8 | TMT & MMT |
| `annual_petroleum_product_consumption` | FY 1997–98 to 2025–26 | Annual / 12 Consumed Products | 29 | 21 | TMT & MMT |
| `annual_petroleum_product_consumption_by_product` | FY 1997–98 to 2025–26 | Long Panel by Consumed Product | 348 | 8 | TMT & MMT |
| `annual_petroleum_import_export_values` | FY 1998–99 to 2024–25 | Annual / Value Flows & Exchange Rate | 27 | 17 | Million US$ & Rs. Crore |
| `crude_oil_fob_price_indian_basket` | FY 2000–01 to 2025–26 | Annual & Monthly / Sour-Sweet Ratios | 26 | 21 | US$ per Barrel ($/bbl.) |
| `statewise_sales_pol_consumption` | FY 2008–09 to 2025–26 | Annual / 36 States/UTs & Products | 2,210 | 6 | TMT & MMT |
| `monthly_petroleum_trade_volumes` | FY 2011–12 to 2024–25 (168 Months) | Monthly / Traded Products | 4,488 | 7 | TMT & MMT |
| `monthly_refinery_crude_processing` | FY 2011–12 to 2025–26 (174 Months) | Monthly / Operating Refineries | 5,667 | 7 | TMT & MMT |
| `conversion_factors_mt_to_barrels` | Benchmark Standard (July 2026) | Product Physical Densities | 12 | 4 | Barrels per MT (bbl/MT) |
| `revised_estimates_fy2025_26` | Forecast Period (FY 2025–26) | Product Demand Forecast Benchmark | 13 | 5 | TMT & MMT |

---

## 4. Key Methodological Implementations

1. **Dual Metric Tracking:** All physical quantity datasets provide parallel columns in both Thousand Metric Tonnes (TMT) and Million Metric Tonnes (MMT), ensuring consistent scaling across upstream, midstream, and downstream analysis.
2. **Implied Foreign Exchange Rate:** By integrating Million US$ and INR Crore trade flows, the pipeline calculates an annual implied transaction exchange rate (`implied_exchange_rate_inr_per_usd`), accurately tracking historical Rupee depreciation without introducing external exchange rate bias.
3. **Provisional and Partial-Year Flagging:** All records carry explicit boolean metadata flags (`is_provisional`, `is_partial_period`, and `source_period_label`), preventing partial periods (e.g., FY 2025–26 Apr–Sep) from being mistakenly analyzed as full annual totals.
4. **Refinery Amalgamation Normalization:** The legal absorption of Bharat Oman Refineries Limited (BORL, Bina) into Bharat Petroleum Corporation Limited (BPCL) in 2022 is documented and accommodated in both aggregate and unit-level series.
