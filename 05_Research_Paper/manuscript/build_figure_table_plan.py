import csv

items = [
    {
        'Item_Type': 'Table',
        'Item_Number': 'Table 1',
        'Caption_Title': 'Summary Statistics of India\'s Petroleum Supply Chain (FY98–FY24)',
        'Section_Mapping': '4.1 Long-Run Overview of India\'s Hydrocarbon Supply Chain',
        'Variables_Included': 'Domestic Production, Crude Imports, Refinery Throughput, Consumption, Product Exports, Product Imports, Crude Import Dependency Ratio',
        'Units': 'MMT; Percentage (%)',
        'Time_Period': 'FY1997-98 to FY2023-24 (26 years)',
        'Underlying_Dataset_Path': 'core_annual_petroleum_dataset.csv',
        'Generating_Script': '04_historical_trends.py',
        'Validation_Status': 'Verified (Level 1 MoPNG/PPAC Audited)',
        'Publication_Readiness': 'Ready (Full 26-year summary statistics compiled)',
        'Academic_Significance': 'Establishes the macro empirical baseline of the paper across the post-reform period.'
    },
    {
        'Item_Type': 'Figure',
        'Item_Number': 'Figure 1',
        'Caption_Title': 'The Evolution of India\'s Petroleum Supply Chain: Production, Refining, Consumption, and Net Trade (FY98–FY24)',
        'Section_Mapping': '4.1 Long-Run Overview of India\'s Hydrocarbon Supply Chain',
        'Variables_Included': 'Domestic Production, Crude Imports, Refinery Throughput, Domestic Consumption',
        'Units': 'Million Metric Tonnes (MMT)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': 'core_annual_petroleum_dataset.csv',
        'Generating_Script': '04_historical_trends.py',
        'Validation_Status': 'Verified (Level 1 MoPNG/PPAC Audited)',
        'Publication_Readiness': 'Ready (Figure 1 exists in 03_Figures_and_Tables)',
        'Academic_Significance': 'Visualizes the core macro trajectory: widening gulf between flat domestic output and escalating downstream processing.'
    },
    {
        'Item_Type': 'Table',
        'Item_Number': 'Table 2',
        'Caption_Title': 'Decoupling Econometrics: Correlation and OLS Regression of Crude Imports on Domestic Production',
        'Section_Mapping': '4.2 Upstream Decoupling: Stagnant Domestic Production vs. Surging Crude Imports',
        'Variables_Included': 'Pearson Correlation (levels and first differences), OLS Coefficient, Newey-West HAC Standard Error, t-stat, p-value, R-squared',
        'Units': 'Dimensionless correlation; Regression coefficients (MMT/MMT)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': 'core_annual_petroleum_dataset.csv',
        'Generating_Script': '08_supply_chain_relationships.py',
        'Validation_Status': 'Verified (Statistically verified)',
        'Publication_Readiness': 'Ready (Econometric results tabulated)',
        'Academic_Significance': 'Empirically refutes the upstream crowding-out fallacy (r = 0.096, p = 0.641; beta = -0.320, p = 0.271).'
    },
    {
        'Item_Type': 'Figure',
        'Item_Number': 'Figure 2',
        'Caption_Title': 'The Decoupling Paradox: Stagnant Upstream Extraction (32–38 MMT) vs. Surging Crude Imports (FY98–FY24)',
        'Section_Mapping': '4.2 Upstream Decoupling: Stagnant Domestic Production vs. Surging Crude Imports',
        'Variables_Included': 'Domestic Crude Production, Crude Oil Imports, Import Dependency Share (%)',
        'Units': 'MMT (Left Axis); Share % (Right Axis)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': 'core_annual_petroleum_dataset.csv',
        'Generating_Script': '04_historical_trends.py',
        'Validation_Status': 'Verified (Audited)',
        'Publication_Readiness': 'Ready (High-resolution figure generated)',
        'Academic_Significance': 'Dramatic visualization of the 26-year upstream flatline contrasted with the 5.9-fold surge in imported crude.'
    },
    {
        'Item_Type': 'Table',
        'Item_Number': 'Table 3',
        'Caption_Title': 'Throughput-Driven Crude Import Regressions and Elasticity Estimates (Newey-West HAC)',
        'Section_Mapping': '4.3 Downstream Expansion: Refinery Throughput as the Primary Import Engine',
        'Variables_Included': 'OLS Intercept, Slope (beta), HAC SE, t-ratio, p-value, Adjusted R-squared, Log-log Elasticity',
        'Units': 'MMT/MMT; Elasticity coefficient (dimensionless)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': 'core_annual_petroleum_dataset.csv',
        'Generating_Script': '08_supply_chain_relationships.py',
        'Validation_Status': 'Verified (Level 1 Audited)',
        'Publication_Readiness': 'Ready (Newey-West HAC models verified)',
        'Academic_Significance': 'Proves crude imports are pulled into India with near-unitary elasticity (beta = 1.011, R2 = 0.9982) by refinery throughput.'
    },
    {
        'Item_Type': 'Figure',
        'Item_Number': 'Figure 3',
        'Caption_Title': 'The Refining Pull: Refinery Throughput vs. Crude Oil Imports and Physical Deficit Gap (FY98–FY24)',
        'Section_Mapping': '4.3 Downstream Expansion: Refinery Throughput as the Primary Import Engine',
        'Variables_Included': 'Refinery Processing Throughput, Gross Crude Imports, Physical Deficit Gap (Throughput minus Production)',
        'Units': 'Million Metric Tonnes (MMT)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': 'core_annual_petroleum_dataset.csv',
        'Generating_Script': '08_supply_chain_relationships.py',
        'Validation_Status': 'Verified (Audited)',
        'Publication_Readiness': 'Ready (Figure exists in 03_Figures_and_Tables)',
        'Academic_Significance': 'Demonstrates that the physical crude deficit expanded +549% (from 35.8 to 232.2 MMT) to feed domestic refineries.'
    },
    {
        'Item_Type': 'Table',
        'Item_Number': 'Table 4',
        'Caption_Title': 'India\'s Petroleum Product Trade Balance: Gross Imports, Exports, and Net Balance (FY98–FY24)',
        'Section_Mapping': '4.4 The Refining Surplus Paradox: Emergence as a Net Product Exporter',
        'Variables_Included': 'Gross Product Exports, Gross Product Imports, Net Product Trade Balance, Refining Coverage Ratio',
        'Units': 'Million Metric Tonnes (MMT); Ratio (%)',
        'Time_Period': 'Selected 5-year benchmark intervals and FY24',
        'Underlying_Dataset_Path': 'core_annual_petroleum_dataset.csv',
        'Generating_Script': '04_historical_trends.py',
        'Validation_Status': 'Verified (DGCI&S Customs / PPAC Reconciled)',
        'Publication_Readiness': 'Ready (Full panel trade balance calculated)',
        'Academic_Significance': 'Verifies uninterrupted net product export surplus since FY02 (+13.89 MMT in FY24, peaking at +43.08 MMT in FY14).'
    },
    {
        'Item_Type': 'Figure',
        'Item_Number': 'Figure 4',
        'Caption_Title': 'The Product Trade Paradox: Gross Exports, Gross Imports, and Net Export Balance (FY98–FY24)',
        'Section_Mapping': '4.4 The Refining Surplus Paradox: Emergence as a Net Product Exporter',
        'Variables_Included': 'Product Exports, Product Imports, Net Trade Balance (Exports minus Imports)',
        'Units': 'Million Metric Tonnes (MMT)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': 'core_annual_petroleum_dataset.csv',
        'Generating_Script': '04_historical_trends.py',
        'Validation_Status': 'Verified (Audited)',
        'Publication_Readiness': 'Ready (Figure exists in 03_Figures_and_Tables)',
        'Academic_Significance': 'Illustrates India\'s transformation from a product-deficit nation in FY98 into a major global refining clearinghouse.'
    },
    {
        'Item_Type': 'Table',
        'Item_Number': 'Table 5',
        'Caption_Title': 'Product-Level Production, Trade, and Consumption Balance (FY24)',
        'Section_Mapping': '4.5 Product-Level Asymmetries: Transport Fuel Surplus vs. LPG Clean Cooking Deficit',
        'Variables_Included': 'Domestic Production, Imports, Exports, Net Trade, Domestic Consumption, Import Dependency Ratio by Product (LPG, MS, HSD, ATF, SKO, Naphtha, FO, Bitumen)',
        'Units': 'Million Metric Tonnes (MMT); Percentage (%)',
        'Time_Period': 'FY2023-24 (with historical growth rates FY98-FY24)',
        'Underlying_Dataset_Path': '02_Standardized_Data/product_annual_dataset.csv',
        'Generating_Script': '05_product_analysis.py',
        'Validation_Status': 'Verified (PPAC validated product series)',
        'Publication_Readiness': 'Ready (Complete 8-product balance compiled)',
        'Academic_Significance': 'Documents the structural split: Diesel (+28.16 MMT net export) vs LPG (-17.99 MMT physical deficit; 62.74% import reliance).'
    },
    {
        'Item_Type': 'Figure',
        'Item_Number': 'Figure 5',
        'Caption_Title': 'Structural Product Divergence: Massive Diesel/Petrol Net Exports vs. Acute LPG Deficit (FY98–FY24)',
        'Section_Mapping': '4.5 Product-Level Asymmetries: Transport Fuel Surplus vs. LPG Clean Cooking Deficit',
        'Variables_Included': 'Net Export Trajectories of Diesel (HSD), Petrol (MS), Aviation Turbine Fuel (ATF) vs LPG Net Import Deficit and Kerosene Collapse',
        'Units': 'Million Metric Tonnes (MMT)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': '02_Standardized_Data/product_annual_dataset.csv',
        'Generating_Script': '05_product_analysis.py',
        'Validation_Status': 'Verified (Audited)',
        'Publication_Readiness': 'Ready (Figure exists in 03_Figures_and_Tables)',
        'Academic_Significance': 'Pivotal figure showing how PMUY clean cooking rollout drove massive LPG import reliance despite national refining self-sufficiency.'
    },
    {
        'Item_Type': 'Table',
        'Item_Number': 'Table 6',
        'Caption_Title': 'Historical Petroleum Import Values, Unit Values, and Rupee/Dollar Exchange Rates (FY98–FY24)',
        'Section_Mapping': '4.6 Financial Exposure: Price Shocks, Currency Depreciation, and Import Bill Expansion',
        'Variables_Included': 'Crude Import Bill (USD B), Crude Import Bill (INR Cr), Crude Quantity (MMT), Calculated Unit Value (USD/MT), Calculated Unit Value (INR/MT), RBI Exchange Rate (INR/USD)',
        'Units': 'USD Billion; INR Crore; MMT; USD/MT; INR/MT; INR/USD',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': '02_Standardized_Data/import_expenditure_dataset.csv',
        'Generating_Script': '06_import_expenditure_analysis.py',
        'Validation_Status': 'Verified (DGCI&S Customs / RBI Audited)',
        'Publication_Readiness': 'Ready (Full financial panel compiled)',
        'Academic_Significance': 'Documents the divergence between physical growth (5.9x), USD bill (37.9x), and INR bill (74.1x).'
    },
    {
        'Item_Type': 'Figure',
        'Item_Number': 'Figure 6',
        'Caption_Title': 'The Compounding Financial Wedge: Physical Imports (6x) vs. USD Expenditure (38x) vs. INR Import Bill (74x) (FY98–FY24)',
        'Section_Mapping': '4.6 Financial Exposure: Price Shocks, Currency Depreciation, and Import Bill Expansion',
        'Variables_Included': 'Indexed Trajectories (FY98 = 100) of Physical Crude Imports, Crude Bill in USD, and Crude Bill in INR',
        'Units': 'Index (FY1997-98 = 100)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': '02_Standardized_Data/import_expenditure_dataset.csv',
        'Generating_Script': '06_import_expenditure_analysis.py',
        'Validation_Status': 'Verified (Audited)',
        'Publication_Readiness': 'Ready (Figure exists in 03_Figures_and_Tables)',
        'Academic_Significance': 'Visualizes the "double-whammy": how currency depreciation (+3.18% p.a.) widened the gap between physical volumes and domestic fiscal burden.'
    },
    {
        'Item_Type': 'Table',
        'Item_Number': 'Table 7',
        'Caption_Title': 'LMDI-I Additive and Multiplicative Decomposition of Crude Import Expenditure Changes (FY98–FY24)',
        'Section_Mapping': '4.7 Index Decomposition Analysis: LMDI Factorization of Volume, Price, and Currency Wedges',
        'Variables_Included': 'Total Expenditure Change (INR Cr), Quantity Effect (INR Cr, %), Dollar Price Effect (INR Cr, %), Exchange Rate Effect (INR Cr, %), Multiplicative Factor Ratios (D_tot, D_Q, D_P, D_E)',
        'Units': 'INR Crore; Percentage Share (%); Factor Ratio (Dimensionless)',
        'Time_Period': 'Sub-periods (FY98-08, FY08-14, FY14-20, FY20-24) and Full Period (FY98-FY24)',
        'Underlying_Dataset_Path': '02_Standardized_Data/import_expenditure_dataset.csv',
        'Generating_Script': '06_import_expenditure_analysis.py',
        'Validation_Status': 'Verified (Ang 2004/2015 formulation verified)',
        'Publication_Readiness': 'Ready (LMDI calculations tabulated)',
        'Academic_Significance': 'Rigorously proves price shocks (41.1%) and currency depreciation (29.0%) together account for 70.1% of secular import bill expansion.'
    },
    {
        'Item_Type': 'Figure',
        'Item_Number': 'Figure 7',
        'Caption_Title': 'LMDI Decomposition Waterfall: Contribution of Physical Quantity, International Dollar Price, and Currency Depreciation to Import Bill Growth',
        'Section_Mapping': '4.7 Index Decomposition Analysis: LMDI Factorization of Volume, Price, and Currency Wedges',
        'Variables_Included': 'Waterfall bars showing Base Value (FY98), Quantity Effect, Price Effect, Exchange Rate Effect, and Terminal Value (FY24)',
        'Units': 'Indian Rupees Crore (INR Cr)',
        'Time_Period': 'FY1997-98 to FY2023-24',
        'Underlying_Dataset_Path': '02_Standardized_Data/import_expenditure_dataset.csv',
        'Generating_Script': '06_import_expenditure_analysis.py',
        'Validation_Status': 'Verified (Audited)',
        'Publication_Readiness': 'Ready (Waterfall chart script verified)',
        'Academic_Significance': 'Clean, definitive decomposition graphic demonstrating zero unexplained residual in import bill growth.'
    }
]

out_path = '05_Research_Paper/manuscript/10_figure_table_plan.csv'
fieldnames = [
    'Item_Type', 'Item_Number', 'Caption_Title', 'Section_Mapping', 
    'Variables_Included', 'Units', 'Time_Period', 'Underlying_Dataset_Path', 
    'Generating_Script', 'Validation_Status', 'Publication_Readiness', 'Academic_Significance'
]

with open(out_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in items:
        writer.writerow(row)

print(f'Successfully wrote {len(items)} items to {out_path}')
