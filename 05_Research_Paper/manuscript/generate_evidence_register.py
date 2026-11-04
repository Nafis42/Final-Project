"""
Generate 02_results_evidence_register.csv
Captures all audited empirical findings and indicators for Phase 9 manuscript preparation.
"""

import csv

records = [
    {
        "Result ID": "RES-01",
        "Finding or Variable": "Domestic crude oil production (including lease condensate) stagnation within a narrow corridor",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "32.76 -> 29.36 MMT (Mean: 34.14 MMT; Min: 32.00 MMT; Max: 38.09 MMT; CAGR: -0.44%)",
        "Unit": "MMT / % p.a.",
        "Source File and Worksheet": "1717395338_PT_Crude_oil_production_H.xls -> Sheet: Indigenous Production",
        "Processed Dataset or Output": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv -> domestic_crude_production_mmt",
        "Relevant Analysis Script": "src/phase4_analysis.py; 04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Available, validation required",
        "Limitations": "Includes lease condensate (~7.45% of upstream extraction); mature field decline (Bombay High) partially offset by EOR and onshore Rajasthan fields.",
        "Can be used in manuscript": "Yes (with explicit qualification of condensate inclusion)"
    },
    {
        "Result ID": "RES-02",
        "Finding or Variable": "Crude oil physical import volume surge",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "39.81 -> 234.26 MMT (+488.5%; CAGR: +7.37% p.a.)",
        "Unit": "MMT / % p.a.",
        "Source File and Worksheet": "1751964547_PT_IMPORT_TMT_H.xlsx -> Sheet: Import Quantities",
        "Processed Dataset or Output": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv -> crude_import_quantity_mmt",
        "Relevant Analysis Script": "src/standardize_data.py; src/phase4_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Excludes minor ocean transit evaporation losses and unrefined strategic petroleum reserve (ISPRL) storage caverns.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-03",
        "Finding or Variable": "Crude oil import dependence proxy escalation",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "54.86% -> 88.86% (+34.00 percentage points)",
        "Unit": "Percentage (%)",
        "Source File and Worksheet": "Derived from 1717395338_PT_Crude_oil_production_H.xls & 1751964547_PT_IMPORT_TMT_H.xlsx",
        "Processed Dataset or Output": "04_Analysis/phase8/additional_indicators.csv -> crude_import_dependence_proxy_pct",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Supply-side proxy formula: Imports / (Production + Imports). Differs from PPAC consumption formula which includes volumetric expansion.",
        "Can be used in manuscript": "Yes (with definition disclosed)"
    },
    {
        "Result ID": "RES-04",
        "Finding or Variable": "Statistical decoupling of domestic crude extraction and crude imports",
        "Relevant Period": "FY 1998-99 to FY 2023-24 (N=26)",
        "Value": "Levels: r = 0.0960 (p = 0.6409); First Differences: r = 0.1732 (p = 0.4076)",
        "Unit": "Pearson r / p-value",
        "Source File and Worksheet": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv",
        "Processed Dataset or Output": "04_Analysis/phase8/correlation_results.csv -> Pair 0",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Measures bivariate co-movement; first-differencing successfully filters out common macroeconomic secular drift.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-05",
        "Finding or Variable": "Econometric test of domestic crude crowding-out hypothesis",
        "Relevant Period": "FY 1998-99 to FY 2023-24 (N=26)",
        "Value": "beta = -0.3204 (t = -1.13, p = 0.2713; 95% CI: [-0.91, +0.27])",
        "Unit": "OLS regression coefficient",
        "Source File and Worksheet": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv",
        "Processed Dataset or Output": "04_Analysis/phase8/regression_results.csv -> Model RQ1-A",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Small annual macroeconomic sample size (N=26); Newey-West HAC standard errors applied; indicates lack of crowding out.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-06",
        "Finding or Variable": "Downstream refinery crude throughput hyper-expansion",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "68.54 -> 261.55 MMT (+281.6%; CAGR: +5.51% p.a.)",
        "Unit": "MMT / % p.a.",
        "Source File and Worksheet": "1788266304_PT_crude_processing_H.xls -> Sheet: Refinery Processing",
        "Processed Dataset or Output": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv -> refinery_crude_processing_mmt",
        "Relevant Analysis Script": "src/phase4_analysis.py; src/standardize_data.py",
        "Validation Status": "Verified",
        "Limitations": "Aggregates PSU, JV, and Private/SEZ export refineries; reflects operational throughput, not installed design capacity.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-07",
        "Finding or Variable": "Physical crude supply deficit gap expansion",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "35.78 -> 232.19 MMT (+549.0%; Absolute Expansion: +196.41 MMT)",
        "Unit": "MMT",
        "Source File and Worksheet": "Residual balance of PT_crude_processing_H.xls and PT_Crude_oil_production_H.xls",
        "Processed Dataset or Output": "04_Analysis/phase8/additional_indicators.csv -> physical_crude_deficit_gap_mmt",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Deficit represents refinery feedstock requirement over and above domestic crude extraction.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-08",
        "Finding or Variable": "Indigenous crude coverage ratio collapse",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "47.80% -> 11.22% (-36.58 percentage points)",
        "Unit": "Percentage (%)",
        "Source File and Worksheet": "Ratio of domestic production to refinery crude throughput",
        "Processed Dataset or Output": "04_Analysis/phase8/additional_indicators.csv -> indigenous_crude_coverage_ratio_pct",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Must NOT be confused with or labeled as refinery capacity utilization; strictly monitors feedstock indigenous coverage.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-09",
        "Finding or Variable": "Refinery crude throughput as primary driver of crude import volumes",
        "Relevant Period": "FY 1998-99 to FY 2024-25 (N=27)",
        "Value": "r = 0.9991 (p < 0.0001); diff r = 0.9680 (p < 0.0001); Elasticity beta = 1.011 (R2 = 0.998)",
        "Unit": "Correlation / Elasticity",
        "Source File and Worksheet": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv",
        "Processed Dataset or Output": "04_Analysis/phase8/correlation_results.csv -> Pair 2; regression_results.csv -> Model RQ2-A",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Small discrepancy between throughput and imports reflects crude tank storage inventory adjustments and transit timing.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-10",
        "Finding or Variable": "India transformation into a structural net exporter of refined petroleum products",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "Net balance: -23.05 MMT (FY99) -> +13.89 MMT (FY24); Peak: +43.08 MMT (FY14)",
        "Unit": "MMT",
        "Source File and Worksheet": "1729493890_pt_import_en.xlsx & 1761642701_PT_production_product_H.xls",
        "Processed Dataset or Output": "03_Processed_Data/standardized/product_trade_balance.csv -> Total Petroleum Products",
        "Relevant Analysis Script": "src/phase5_product_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Net exporter status maintained continuously for 23 consecutive years; macro surplus conceals sub-product deficits.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-11",
        "Finding or Variable": "Aggregate refined petroleum product self-sufficiency ratio",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "80.71% -> 117.84% (Peak: 139.38% in FY 2013-14)",
        "Unit": "Percentage (%)",
        "Source File and Worksheet": "Ratio of total product production to total product consumption",
        "Processed Dataset or Output": "04_Analysis/phase8/additional_indicators.csv -> product_self_sufficiency_ratio_pct",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Aggregate self-sufficiency (>100%) coexists with critical foreign import exposure in specific finished streams.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-12",
        "Finding or Variable": "Massive structural export surpluses in transport fuels",
        "Relevant Period": "FY 2023-24",
        "Value": "HSD (Diesel): +28.16 MMT; MS (Petrol): +12.76 MMT; ATF (Jet Fuel): +8.58 MMT; Naphtha: +4.06 MMT",
        "Unit": "MMT net trade balance",
        "Source File and Worksheet": "Product-wise import and export schedules in PPAC statistical filings",
        "Processed Dataset or Output": "03_Processed_Data/standardized/product_trade_balance.csv",
        "Relevant Analysis Script": "src/phase5_product_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Export volumes heavily concentrated in private coastal merchant refineries (Reliance Jamnagar, Nayara Vadinar).",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-13",
        "Finding or Variable": "Acute structural import deficit in Liquefied Petroleum Gas (LPG)",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "Net deficit: -1.45 MMT (FY99) -> -17.99 MMT (FY24); 62.7% of consumption imported",
        "Unit": "MMT / % imported",
        "Source File and Worksheet": "PPAC product trade balances and LPG consumption series",
        "Processed Dataset or Output": "03_Processed_Data/standardized/product_trade_balance.csv -> Liquefied Petroleum Gas (LPG)",
        "Relevant Analysis Script": "src/phase5_product_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Driven by clean cooking welfare mandates (PAHAL DBTL, PMUY); refinery LPG yield is chemically constrained.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-14",
        "Finding or Variable": "Domestic clean cooking fuel transition: Kerosene collapse vs LPG scaling",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "SKO (Kerosene): 10.60 -> 0.48 MMT (-95.5%); LPG: 5.04 -> 29.66 MMT (+488.5%)",
        "Unit": "MMT",
        "Source File and Worksheet": "1788343376_PT_Consumption_English.xls -> Sheet: Product Consumption",
        "Processed Dataset or Output": "03_Processed_Data/standardized/product_consumption_dataset.csv",
        "Relevant Analysis Script": "src/phase5_product_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Deliberate policy phase-out of subsidized PDS kerosene allocations as states achieved kerosene-free status.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-15",
        "Finding or Variable": "Automotive transport demand structural divergence: Petrol outgrew Diesel",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "MS (Petrol) CAGR: +7.94%; HSD (Diesel) CAGR: +3.58%; Ratio: 6.75:1 (FY99) -> 2.41:1 (FY24)",
        "Unit": "CAGR / Ratio",
        "Source File and Worksheet": "1788343376_PT_Consumption_English.xls",
        "Processed Dataset or Output": "03_Processed_Data/standardized/product_consumption_dataset.csv -> HSD, MS",
        "Relevant Analysis Script": "src/phase5_product_analysis.py",
        "Validation Status": "Available, validation required",
        "Limitations": "Reported MS retail sales figures include depot-level bio-ethanol blending (reaching 12-14% by FY24).",
        "Can be used in manuscript": "Yes (with ethanol blending noted)"
    },
    {
        "Result ID": "RES-16",
        "Finding or Variable": "Crude oil import expenditure escalation in US Dollars",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "$3,518M -> $133,366M (38-fold; CAGR: +15.70% p.a.; Peak: $144,293M in FY13)",
        "Unit": "Million US$ / % p.a.",
        "Source File and Worksheet": "1729493957_val-in-dollar_en.xlsx & 1751964622_PT_IMPORT_VAL_US$_H.xlsx",
        "Processed Dataset or Output": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv -> crude_import_value",
        "Relevant Analysis Script": "src/phase6_import_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Valued in CIF terms; includes international ocean freight, transit insurance, and grade quality differentials.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-17",
        "Finding or Variable": "Crude oil import expenditure escalation in Indian Rupees",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "Rs. 14,917 Cr -> Rs. 1,105,176 Cr (74-fold; CAGR: +18.88% p.a.)",
        "Unit": "Rs. Crore / % p.a.",
        "Source File and Worksheet": "1751964598_PT_IMPORT_VAL_RS.CRS._H.xlsx",
        "Processed Dataset or Output": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv -> crude_import_value_rs_crore",
        "Relevant Analysis Script": "src/phase6_import_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Nominal domestic expenditure; not adjusted for domestic general inflation (CPI/WPI).",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-18",
        "Finding or Variable": "Exchange rate depreciation growth penalty wedge",
        "Relevant Period": "FY 1998-99 to FY 2023-24",
        "Value": "INR CAGR (18.88%) minus USD CAGR (15.70%) = +3.18% p.a. compounding penalty; FX: 42.40 -> 82.87 INR/USD",
        "Unit": "% p.a. / FX",
        "Source File and Worksheet": "Dual-currency reported import valuations vs RBI reference rates",
        "Processed Dataset or Output": "04_Analysis/phase8/additional_indicators.csv -> implied_exchange_rate_inr_per_usd",
        "Relevant Analysis Script": "src/phase6_import_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Implied exchange rate derived from official dual-currency totals matches RBI annual averages within +/-0.3%.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-19",
        "Finding or Variable": "LMDI decomposition of crude import expenditure: Price vs Volume dominance",
        "Relevant Period": "FY 1999-00 to FY 2023-24 (25 annual transitions)",
        "Value": "International crude price shocks account for ~72% of inter-annual expenditure variance; volume anchors baseline",
        "Unit": "% / Million US$",
        "Source File and Worksheet": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv",
        "Processed Dataset or Output": "04_Analysis/phase6/figure_data/fig6_expenditure_decomposition_contributions.csv",
        "Relevant Analysis Script": "src/phase6_import_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Logarithmic Mean Divisia Index (LMDI) perfect decomposition with zero residual; isolates price vs volume effects.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-20",
        "Finding or Variable": "Calculated CIF crude import unit value co-movement with Indian Basket FOB price",
        "Relevant Period": "FY 2000-01 to FY 2023-24 (N=24)",
        "Value": "r = 0.9880 (p < 0.0001); Unit Value: $77.67/bbl vs Indian Basket: $82.58/bbl in FY24",
        "Unit": "USD / barrel",
        "Source File and Worksheet": "1775133106_PP_Crude-Oil-FOB-Price-(Indian Basket)-Historical.xlsx & ICR Table 9",
        "Processed Dataset or Output": "04_Analysis/phase6/figure_data/fig4_crude_unit_value_vs_indian_basket.csv",
        "Relevant Analysis Script": "src/phase6_import_analysis.py",
        "Validation Status": "Available, validation required",
        "Limitations": "Conversion factor 7.33 bbl/MT applied; unit value reflects realized CIF costs across diverse grades (sour/sweet).",
        "Can be used in manuscript": "Yes (with conversion qualification)"
    },
    {
        "Result ID": "RES-21",
        "Finding or Variable": "Econometric parameter stability across historical policy regimes",
        "Relevant Period": "FY99-05 (Post-APM); FY05-14 (Export Boom); FY14-24 (Welfare/Reform)",
        "Value": "Throughput-import elasticity beta = 1.011 overall; Subperiod R2 > 0.98 in all regimes; Chow break test non-significant",
        "Unit": "Econometric beta / R2",
        "Source File and Worksheet": "04_Analysis/phase8/subperiod_comparison.csv",
        "Processed Dataset or Output": "04_Analysis/phase8/robustness_results.csv",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Policy subperiod boundaries defined based on major institutional reforms (APM dismantling, private refining entry, PMUY).",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-22",
        "Finding or Variable": "Robustness to COVID-19 pandemic shock outlier sensitivity",
        "Relevant Period": "FY 1998-99 to FY 2023-24 (N=25 excluding FY21)",
        "Value": "Baseline r = 0.9991; Excluding FY21 r = 0.9992; Crowding-out beta remains non-significant (p = 0.312)",
        "Unit": "Sensitivity metric",
        "Source File and Worksheet": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv",
        "Processed Dataset or Output": "04_Analysis/phase8/robustness_results.csv -> Test ROB-01",
        "Relevant Analysis Script": "04_Analysis/phase8/scripts/phase8_statistical_analysis.py",
        "Validation Status": "Verified",
        "Limitations": "Pandemic lockdown induced sharp temporary volume contraction in FY21, rebounding fully by FY22.",
        "Can be used in manuscript": "Yes"
    },
    {
        "Result ID": "RES-23",
        "Finding or Variable": "Provisional status of fiscal years FY 2024-25 and FY 2025-26",
        "Relevant Period": "FY 2024-25 to FY 2025-26",
        "Value": "Partial data only: FY25 crude price $78.56/bbl; FY26 partial price $70.99/bbl; full supply chain balances unsettled",
        "Unit": "Various",
        "Source File and Worksheet": "1773137026_Revised Estimates FY 2025-26_Combined.pdf & Flash reports",
        "Processed Dataset or Output": "03_Processed_Data/standardized/core_annual_petroleum_dataset.csv",
        "Relevant Analysis Script": "src/extract_monthly_and_secondary_raw.py",
        "Validation Status": "Preliminary",
        "Limitations": "Not settled in official annual compendia; excluded from core econometric panels to prevent partial-year bias.",
        "Can be used in manuscript": "No (Disclosed only as boundary/limitation)"
    }
]

out_path = "05_Research_Paper/manuscript/02_results_evidence_register.csv"
fields = [
    "Result ID", "Finding or Variable", "Relevant Period", "Value", "Unit", 
    "Source File and Worksheet", "Processed Dataset or Output", "Relevant Analysis Script", 
    "Validation Status", "Limitations", "Can be used in manuscript"
]

with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)

print(f"Successfully created {out_path} with {len(records)} audited evidence records.")
