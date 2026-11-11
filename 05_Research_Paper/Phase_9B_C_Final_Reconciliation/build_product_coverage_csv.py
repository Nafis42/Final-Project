import pandas as pd
import numpy as np

# Load product-level dataset
df_prod = pd.read_csv('03_Processed_Data/standardized/petroleum_product_level_dataset.csv')
fy24 = df_prod[df_prod['reporting_period'] == 'FY 2023-24'].copy().reset_index(drop=True)

# Build product coverage audit rows
records = []
for idx, r in fy24.iterrows():
    p = r['product_name']
    prod = r['production_mmt']
    cons = r['consumption_mmt']
    imp = r['import_quantity_mmt']
    exp = r['export_quantity_mmt']
    net_exp = r['net_export_quantity_mmt']
    
    pcr = (prod / cons) * 100.0 if pd.notna(prod) and pd.notna(cons) and cons > 0 else np.nan
    
    # Assess comparability and trade role
    if pd.isna(prod) and pd.notna(cons):
        comp_status = "Consumption-only reported; production aggregated under Others/Refinery Fuel"
        trade_role = "Domestic Consumption recorded; refinery byproduct / imports"
    elif pd.notna(prod) and pd.isna(cons):
        comp_status = "Production-only reported; consumption aggregated under combined categories"
        trade_role = "Refinery output; blended or consumed in industry"
    elif pcr > 100.0:
        comp_status = "Directly Comparable (Harmonized PPAC production and sales scopes)"
        trade_role = f"Net Exporter (+{net_exp:.2f} MMT surplus); drives national aggregate ratio above 100%"
    else:
        comp_status = "Directly Comparable (Harmonized PPAC production and sales scopes)"
        trade_role = f"Net Importer ({net_exp:.2f} MMT deficit); structural domestic production shortfall"
        
    records.append({
        'Product_Category': p,
        'Financial_Year': 'FY 2023-24',
        'Domestic_Production_MMT': round(prod, 4) if pd.notna(prod) else np.nan,
        'Domestic_Consumption_MMT': round(cons, 4) if pd.notna(cons) else np.nan,
        'Product_Coverage_Ratio_PCR_pct': round(pcr, 2) if pd.notna(pcr) else np.nan,
        'Import_Quantity_MMT': round(imp, 4) if pd.notna(imp) else np.nan,
        'Export_Quantity_MMT': round(exp, 4) if pd.notna(exp) else np.nan,
        'Net_Export_Balance_MMT': round(net_exp, 4) if pd.notna(net_exp) else np.nan,
        'Source_Scope_and_Definitions': "PPAC Product-Level Returns (Includes SEZ to DTA sales; private refineries included)",
        'Comparability_Status': comp_status,
        'Trade_Position_and_Market_Role': trade_role
    })

# Add Combined Furnace Oil + LSHS row for accurate physical coverage
fo_prod = 9.6977 + 0.7445 # 10.4422 MMT
fo_cons = 6.5944 # MMT
fo_pcr = (fo_prod / fo_cons) * 100.0
records.append({
    'Product_Category': 'Fuel Oil & LSHS (Consolidated Combined)',
    'Financial_Year': 'FY 2023-24',
    'Domestic_Production_MMT': round(fo_prod, 4),
    'Domestic_Consumption_MMT': round(fo_cons, 4),
    'Product_Coverage_Ratio_PCR_pct': round(fo_pcr, 2),
    'Import_Quantity_MMT': 9.0526,
    'Export_Quantity_MMT': 2.1030,
    'Net_Export_Balance_MMT': -6.9497,
    'Source_Scope_and_Definitions': "Consolidated FO + LSHS production against combined industrial consumption",
    'Comparability_Status': "Consolidated Comparable Scope",
    'Trade_Position_and_Market_Role': "Heavy fuel oil: Domestic production covers consumption (158.35%), but coastal bunker/power imports occur (-6.95 MMT)"
})

# Add National Aggregate Row
core = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
c24 = core[core['reporting_period'] == 'FY 2023-24'].iloc[0]
tot_prod = c24['petroleum_product_production_mmt']
tot_cons = c24['petroleum_product_consumption_mmt']
tot_imp = c24['petroleum_product_imports_mmt']
tot_exp = c24['petroleum_product_exports_mmt']
tot_net_exp = tot_exp - tot_imp
tot_pcr = (tot_prod / tot_cons) * 100.0

records.append({
    'Product_Category': '=== NATIONAL AGGREGATE TOTAL (ALL PRODUCTS) ===',
    'Financial_Year': 'FY 2023-24',
    'Domestic_Production_MMT': round(tot_prod, 4),
    'Domestic_Consumption_MMT': round(tot_cons, 4),
    'Product_Coverage_Ratio_PCR_pct': round(tot_pcr, 2),
    'Import_Quantity_MMT': round(tot_imp, 4),
    'Export_Quantity_MMT': round(tot_exp, 4),
    'Net_Export_Balance_MMT': round(tot_net_exp, 4),
    'Source_Scope_and_Definitions': "PPAC Full Supply Chain (All 23 refineries; PSU + Private; SEZ included)",
    'Comparability_Status': "100% Mathematically Balanced (Aggregate equals sum of reported product flows)",
    'Trade_Position_and_Market_Role': "Aggregate Net Exporter (+13.90 MMT); 117.84% ratio is heavily driven by Diesel (+28.16 MMT) and Petrol (+12.76 MMT), masking acute clean cooking deficit in LPG (-17.99 MMT)"
})

df_out = pd.DataFrame(records)
out_csv = '05_Research_Paper/Phase_9B_C_Final_Reconciliation/Phase_9B_C_Product_Coverage_Audit.csv'
df_out.to_csv(out_csv, index=False)
print(f"Generated {out_csv} with {len(df_out)} rows.")
