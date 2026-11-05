import csv

reaudit_records = [
    {
        'Result_ID': 'RES-01',
        'Finding_Description': 'Domestic crude production (including lease condensate) stagnation in narrow corridor',
        'Starting_Obs': '32.76 MMT (FY 1998-99)',
        'Ending_Obs': '29.36 MMT (FY 2023-24)',
        'Units': 'Million Metric Tonnes (MMT); % p.a.',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (26 years, 25 intervals)',
        'Calculation_Method': 'Historical mean (34.14 MMT), min (32.00 MMT in FY00), max (38.09 MMT in FY12); CAGR = (29.356/32.760)**(1/25) - 1',
        'Numerical_Result': 'CAGR: -0.44% p.a.; Absolute: 32.76 -> 29.36 MMT',
        'Source_Dataset': '03_Processed_Data/standardized/annual_crude_oil_production.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Justified with Qualification: Must disclose inclusion of lease condensate (~2.19 MMT in FY24) per MoPNG definition.'
    },
    {
        'Result_ID': 'RES-02',
        'Finding_Description': 'Crude oil physical import volume surge',
        'Starting_Obs': '39.81 MMT (FY 1998-99)',
        'Ending_Obs': '234.26 MMT (FY 2023-24)',
        'Units': 'MMT; % p.a.',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (26 years, 25 intervals)',
        'Calculation_Method': 'Total growth: (234.262 - 39.808)/39.808; CAGR = (234.262/39.808)**(1/25) - 1',
        'Numerical_Result': '+488.5% total growth; CAGR: +7.35% (+7.37% with TMT precision)',
        'Source_Dataset': '03_Processed_Data/standardized/annual_petroleum_trade_volumes.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Direct customs cleared physical trade volume.'
    },
    {
        'Result_ID': 'RES-03',
        'Finding_Description': 'Crude oil import dependence proxy escalation (Supply-Pool Import Share)',
        'Starting_Obs': '54.86% (FY 1998-99)',
        'Ending_Obs': '88.86% (FY 2023-24)',
        'Units': 'Percentage (%)',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'SPS_t = (M_c,t / (P_c,t + M_c,t)) * 100 with X_c = 0',
        'Numerical_Result': '54.86% -> 88.86% (+34.00 percentage points)',
        'Source_Dataset': '03_Processed_Data/standardized/derived_indicators.csv',
        'Reproducibility_Status': 'Reproduced Exactly (Clarified Formula)',
        'Academic_Interpretation_Status': 'Justified with Correction: Disambiguated as Supply-Pool Import Share (Formula A), distinct from Import-to-Throughput ratio (58.08% to 89.57%).'
    },
    {
        'Result_ID': 'RES-04',
        'Finding_Description': 'Statistical decoupling of domestic crude extraction and crude imports',
        'Starting_Obs': 'FY 1998-99',
        'Ending_Obs': 'FY 2023-24',
        'Units': 'Pearson r; Spearman rho; p-value',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'Bivariate Pearson and Spearman correlation on raw levels and first differences',
        'Numerical_Result': 'Levels: r = 0.0960 (p = 0.6409); First Differences: r = 0.1732 (p = 0.4076)',
        'Source_Dataset': '04_Analysis/phase8/correlation_results.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Justified with Caution: Demonstrates lack of linear co-movement in observational series; must not be framed as proof of causal exogeneity.'
    },
    {
        'Result_ID': 'RES-05',
        'Finding_Description': 'Econometric test of domestic crude crowding-out hypothesis',
        'Starting_Obs': 'FY 1998-99',
        'Ending_Obs': 'FY 2023-24',
        'Units': 'Regression slope coefficient (beta); p-value',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'OLS regression with Newey-West HAC standard errors (lag m=2)',
        'Numerical_Result': 'beta = -0.3204, SE = 0.283, t = -1.13, p = 0.2713, R2 = 0.009',
        'Source_Dataset': '04_Analysis/phase8/regression_results.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Corrected Language: Must state \"fails to reject the null hypothesis of no relationship\", replacing overly strong claims of \"refuting crowding-out\".'
    },
    {
        'Result_ID': 'RES-06',
        'Finding_Description': 'Downstream refinery crude throughput expansion',
        'Starting_Obs': '68.54 MMT (FY 1998-99)',
        'Ending_Obs': '261.55 MMT (FY 2023-24)',
        'Units': 'MMT; % p.a.',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (26 years, 25 intervals)',
        'Calculation_Method': 'Total growth: (261.546 - 68.539)/68.539; CAGR = (261.546/68.539)**(1/25) - 1',
        'Numerical_Result': '+281.6% total expansion; CAGR: +5.50% (+5.51% with TMT)',
        'Source_Dataset': '03_Processed_Data/standardized/annual_refinery_crude_processing.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Direct administrative record of refinery gate throughput.'
    },
    {
        'Result_ID': 'RES-07',
        'Finding_Description': 'Physical crude supply deficit gap expansion (Production-to-Throughput Gap)',
        'Starting_Obs': '35.78 MMT (FY 1998-99)',
        'Ending_Obs': '232.19 MMT (FY 2023-24)',
        'Units': 'MMT; % expansion',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'Delta_gap = Refinery Throughput minus Domestic Crude Production',
        'Numerical_Result': '35.78 -> 232.19 MMT (+549.0%; Absolute Increase: +196.41 MMT)',
        'Source_Dataset': '04_Analysis/phase8/figure_data/fig2_data.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Justified with Critical Caveat: Measures domestic production shortfall relative to throughput; NOT an exact import requirement (imports exceed by ~4.41 MMT/yr).'
    },
    {
        'Result_ID': 'RES-08',
        'Finding_Description': 'Indigenous crude coverage ratio collapse',
        'Starting_Obs': '47.80% (FY 1998-99)',
        'Ending_Obs': '11.22% (FY 2023-24)',
        'Units': 'Percentage (%)',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'SSR_t = (P_c,t / R_t) * 100',
        'Numerical_Result': '47.80% -> 11.22% (-36.58 percentage points)',
        'Source_Dataset': '03_Processed_Data/standardized/derived_indicators.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Measures domestic extraction against refinery processing scale.'
    },
    {
        'Result_ID': 'RES-09',
        'Finding_Description': 'Refinery crude throughput as primary empirical driver of crude imports',
        'Starting_Obs': 'FY 1998-99',
        'Ending_Obs': 'FY 2023-24',
        'Units': 'Pearson r; OLS slope (beta); R2',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'OLS regression and first-difference correlation of crude imports on throughput',
        'Numerical_Result': 'r = 0.9991 (p < 0.0001); diff r = 0.9680; Elasticity beta = 1.011, R2 = 0.9982',
        'Source_Dataset': '04_Analysis/phase8/regression_results.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Demonstrates strong structural co-movement and near-unitary elasticity.'
    },
    {
        'Result_ID': 'RES-10',
        'Finding_Description': 'Transformation into a structural net exporter of refined petroleum products',
        'Starting_Obs': '-23.05 MMT (FY 1998-99)',
        'Ending_Obs': '+13.89 MMT (FY 2023-24)',
        'Units': 'Million Metric Tonnes (MMT)',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'Net Product Trade = Product Exports minus Product Imports',
        'Numerical_Result': 'Net balance: -23.05 MMT (FY99) -> +13.89 MMT (FY24); Peak: +43.08 MMT (FY14)',
        'Source_Dataset': '03_Processed_Data/standardized/product_trade_balance.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Uninterrupted annual export surplus verified from FY02 through FY24.'
    },
    {
        'Result_ID': 'RES-11',
        'Finding_Description': 'Aggregate refined petroleum product self-sufficiency ratio (Refining Coverage)',
        'Starting_Obs': '80.71% (FY 1998-99)',
        'Ending_Obs': '117.84% (FY 2023-24)',
        'Units': 'Percentage (%)',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'RCR_t = (Total Product Production / Total Product Consumption) * 100',
        'Numerical_Result': '80.71% -> 117.84% (Peak: 139.38% in FY 2013-14)',
        'Source_Dataset': '03_Processed_Data/standardized/derived_indicators.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Justified with Qualification: Macro product self-sufficiency coexists with severe single-stream product deficits (LPG).'
    },
    {
        'Result_ID': 'RES-12',
        'Finding_Description': 'Massive structural export surpluses in transport fuels (FY24)',
        'Starting_Obs': 'FY 2023-24',
        'Ending_Obs': 'FY 2023-24',
        'Units': 'Million Metric Tonnes (MMT)',
        'Study_Period': 'FY 2023-24 (Single-year cross-section)',
        'Calculation_Method': 'Product Exports minus Product Imports by Category',
        'Numerical_Result': 'HSD (Diesel): +28.16 MMT; MS (Petrol): +12.76 MMT; ATF: +8.58 MMT; Naphtha: +4.06 MMT',
        'Source_Dataset': '03_Processed_Data/standardized/petroleum_product_level_dataset.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Direct customs-cleared trade statistics by refined stream.'
    },
    {
        'Result_ID': 'RES-13',
        'Finding_Description': 'Acute structural import deficit in Liquefied Petroleum Gas (LPG)',
        'Starting_Obs': '-1.45 MMT (FY 1998-99)',
        'Ending_Obs': '-17.99 MMT (FY 2023-24)',
        'Units': 'MMT; Percentage imported (%)',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'LPG Net Trade = Exports minus Imports; PID = Net Imports / Consumption',
        'Numerical_Result': 'Net deficit: -1.45 -> -17.99 MMT; Import share: 62.74% of consumption imported',
        'Source_Dataset': '03_Processed_Data/standardized/petroleum_product_level_dataset.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Highlights the domestic clean cooking import exposure paradox.'
    },
    {
        'Result_ID': 'RES-14',
        'Finding_Description': 'Domestic clean cooking transition: Kerosene collapse vs. LPG scaling',
        'Starting_Obs': 'SKO: 10.60 MMT; LPG: 5.04 MMT (FY99)',
        'Ending_Obs': 'SKO: 0.48 MMT; LPG: 29.66 MMT (FY24)',
        'Units': 'MMT; Percentage change (%)',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Calculation_Method': 'Consumption change: SKO (0.48 - 10.60)/10.60; LPG (29.66 - 5.04)/5.04',
        'Numerical_Result': 'SKO: -95.5%; LPG: +488.5% (Production baseline 5.17 to 30.40 MMT apparent absorption)',
        'Source_Dataset': '03_Processed_Data/standardized/annual_petroleum_product_consumption_by_product.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Reflects deliberate policy curtailment of PDS kerosene and PMUY scaling.'
    },
    {
        'Result_ID': 'RES-15',
        'Finding_Description': 'Automotive transport demand divergence: Petrol outgrew Diesel',
        'Starting_Obs': 'Ratio 6.75:1 (FY 1998-99)',
        'Ending_Obs': 'Ratio 2.41:1 (FY 2023-24)',
        'Units': 'CAGR (% p.a.); Ratio',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (25 intervals)',
        'Calculation_Method': 'CAGR across 25 intervals for MS and HSD consumption',
        'Numerical_Result': 'MS CAGR: +7.94%; HSD CAGR: +3.58%; Ratio collapsed from 6.75:1 to 2.41:1',
        'Source_Dataset': '03_Processed_Data/standardized/annual_petroleum_product_consumption_by_product.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Captures diesel price deregulation (2014) and 2-wheeler automotive motorization.'
    },
    {
        'Result_ID': 'RES-16',
        'Finding_Description': 'Crude oil import expenditure escalation in US Dollars',
        'Starting_Obs': '$3,518 Million (FY 1998-99)',
        'Ending_Obs': '$133,366 Million (FY 2023-24)',
        'Units': 'Million US$; % p.a.',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (25 intervals)',
        'Calculation_Method': 'CAGR = (133366 / 3518)**(1/25) - 1; Multiplier = 133366 / 3518',
        'Numerical_Result': '37.9-fold (38-fold) increase; CAGR: +15.65% (+15.70% with detailed decimals)',
        'Source_Dataset': '03_Processed_Data/standardized/annual_petroleum_import_export_values.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Reflects combined physical growth and global oil price shocks.'
    },
    {
        'Result_ID': 'RES-17',
        'Finding_Description': 'Crude oil import expenditure escalation in Indian Rupees',
        'Starting_Obs': 'Rs. 14,917 Crore (FY 1998-99)',
        'Ending_Obs': 'Rs. 1,105,176 Crore (FY 2023-24)',
        'Units': 'Indian Rupees Crore; % p.a.',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (25 intervals)',
        'Calculation_Method': 'CAGR = (1105176 / 14917)**(1/25) - 1; Multiplier = 1105176 / 14917',
        'Numerical_Result': '74.1-fold (74-fold) increase; CAGR: +18.79% (+18.88% with detailed decimals)',
        'Source_Dataset': '03_Processed_Data/standardized/annual_petroleum_import_export_values.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Demonstrates dramatic expansion of domestic currency energy import liability.'
    },
    {
        'Result_ID': 'RES-18',
        'Finding_Description': 'Exchange rate depreciation compounding penalty wedge',
        'Starting_Obs': '42.40 INR/USD (FY 1998-99)',
        'Ending_Obs': '82.87 INR/USD (FY 2023-24)',
        'Units': 'INR/USD; % p.a.',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (25 intervals)',
        'Calculation_Method': 'INR CAGR minus USD CAGR; Exchange rate CAGR = (82.87/42.40)**(1/25) - 1',
        'Numerical_Result': 'Compounding wedge: +3.18% p.a. (Exchange rate depreciated at 2.71% to 3.18% p.a.)',
        'Source_Dataset': '03_Processed_Data/standardized/import_quantity_value_aligned_dataset.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Disentangles currency devaluation from international dollar price movements.'
    },
    {
        'Result_ID': 'RES-19',
        'Finding_Description': 'Decomposition of crude import expenditure: Price vs. Volume vs. Currency',
        'Starting_Obs': 'FY 1998-99',
        'Ending_Obs': 'FY 2023-24',
        'Units': 'Rs. Crore; Percentage share (%)',
        'Study_Period': 'FY 1998-99 to FY 2023-24 (26 years)',
        'Calculation_Method': '3-Factor LMDI-I (Ang 2004/2015): Delta V = Delta Q + Delta P + Delta E',
        'Numerical_Result': 'Delta V = 1,090,259 Cr: Quantity = 41.17% (448,833 Cr); Price = 43.27% (471,742 Cr); FX = 15.56% (169,684 Cr)',
        'Source_Dataset': 'Recalculated via LMDI-I on standardized core endpoints',
        'Reproducibility_Status': 'Discrepancy Corrected',
        'Academic_Interpretation_Status': 'Corrected from Draft: Draft stated 29.8% Q, 41.1% P, 29.0% FX. Mathematically exact LMDI-I shares established.'
    },
    {
        'Result_ID': 'RES-20',
        'Finding_Description': 'Calculated CIF crude import unit value co-movement with Indian Basket FOB price',
        'Starting_Obs': 'FY 2000-01',
        'Ending_Obs': 'FY 2023-24',
        'Units': 'USD / barrel; Pearson r',
        'Study_Period': 'FY 2000-01 to FY 2023-24 (N=24)',
        'Calculation_Method': 'Bivariate correlation between CIF unit value ($/bbl) and Indian Basket ($/bbl)',
        'Numerical_Result': 'r = 0.9880 (p < 0.0001); Unit Value: $77.67/bbl vs Indian Basket: $82.58/bbl in FY24',
        'Source_Dataset': '03_Processed_Data/standardized/derived_indicators.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Confirms strong co-movement between customs valuation and international benchmarks.'
    },
    {
        'Result_ID': 'RES-21',
        'Finding_Description': 'Econometric parameter stability across historical policy regimes',
        'Starting_Obs': 'FY 1998-99',
        'Ending_Obs': 'FY 2023-24',
        'Units': 'Subperiod slope (beta); R2',
        'Study_Period': 'FY99-05 (Post-APM); FY05-14 (Export Boom); FY14-24 (Reforms)',
        'Calculation_Method': 'Subperiod OLS regressions of crude imports on refinery throughput',
        'Numerical_Result': 'Throughput-import elasticity beta = 1.011 overall; Subperiod R2 > 0.98 in all regimes',
        'Source_Dataset': '04_Analysis/phase8/subperiod_comparison.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Proves elasticity relationship is robust across major policy regimes.'
    },
    {
        'Result_ID': 'RES-22',
        'Finding_Description': 'Robustness to COVID-19 pandemic shock outlier sensitivity',
        'Starting_Obs': 'FY 1998-99',
        'Ending_Obs': 'FY 2023-24',
        'Units': 'Pearson r; OLS beta',
        'Study_Period': 'FY 1998-99 to FY 2023-24 excluding FY 2020-21 (N=25)',
        'Calculation_Method': 'Re-estimation of correlations and regressions omitting pandemic shock year',
        'Numerical_Result': 'Baseline r = 0.9991; Excluding FY21 r = 0.9992; Crowding-out beta remains non-significant (p = 0.312)',
        'Source_Dataset': '04_Analysis/phase8/robustness_results.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Proves findings are not driven by pandemic-induced drop in demand.'
    },
    {
        'Result_ID': 'RES-23',
        'Finding_Description': 'Provisional status of fiscal years FY 2024-25 and FY 2025-26',
        'Starting_Obs': 'FY 2024-25',
        'Ending_Obs': 'FY 2025-26',
        'Units': 'Qualitative status; $/bbl',
        'Study_Period': 'FY 2024-25 to FY 2025-26',
        'Calculation_Method': 'Verification of data completeness across reporting tiers',
        'Numerical_Result': 'Partial/provisional data: FY25 crude price $78.56/bbl; FY26 price $70.99/bbl; upstream crude missing',
        'Source_Dataset': '03_Processed_Data/standardized/source_coverage_matrix.csv',
        'Reproducibility_Status': 'Reproduced Exactly',
        'Academic_Interpretation_Status': 'Fully Justified: Confirms academic necessity of excluding post-FY24 observations from econometric modeling.'
    }
]

out_path = '05_Research_Paper/phase9a_audit/09_headline_results_reaudit.csv'
fieldnames = [
    'Result_ID', 'Finding_Description', 'Starting_Obs', 'Ending_Obs', 
    'Units', 'Study_Period', 'Calculation_Method', 'Numerical_Result', 
    'Source_Dataset', 'Reproducibility_Status', 'Academic_Interpretation_Status'
]

with open(out_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in reaudit_records:
        writer.writerow(row)

print(f'Successfully wrote {len(reaudit_records)} re-audited headline results to {out_path}')
