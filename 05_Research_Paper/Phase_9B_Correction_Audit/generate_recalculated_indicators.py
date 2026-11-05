import pandas as pd
import numpy as np

# Load core dataset and product dataset
df_core = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
df_ind = pd.read_csv('03_Processed_Data/standardized/derived_indicators.csv')
df_prod = pd.read_csv('03_Processed_Data/standardized/petroleum_product_level_dataset.csv')

# Filter to 26 balanced years (FY 1998-99 to FY 2023-24)
core_26 = df_core[(df_core['fiscal_year_start'] >= 1998) & (df_core['fiscal_year_start'] <= 2023)].copy().reset_index(drop=True)
ind_26 = df_ind[(df_ind['fiscal_year_start'] >= 1998) & (df_ind['fiscal_year_start'] <= 2023)].copy().reset_index(drop=True)

# Extract LPG series
lpg_df = df_prod[df_prod['product_name'].str.contains('LPG', case=False, na=False)].copy()
lpg_map = {}
for idx, r in lpg_df.iterrows():
    period = r['reporting_period']
    lpg_map[period] = {
        'lpg_production_mmt': r['production_mmt'],
        'lpg_import_mmt': r['import_quantity_mmt'],
        'lpg_export_mmt': r['export_quantity_mmt'] if pd.notna(r['export_quantity_mmt']) else 0.0,
        'lpg_net_import_mmt': r['import_quantity_mmt'] - (r['export_quantity_mmt'] if pd.notna(r['export_quantity_mmt']) else 0.0),
        'lpg_consumption_mmt': r['consumption_mmt']
    }

records = []
for idx, r in core_26.iterrows():
    period = r['reporting_period']
    yr_start = int(r['fiscal_year_start'])
    yr_end = int(r['fiscal_year_end'])
    
    # Upstream Crude
    p_c = r['domestic_crude_production_mmt']
    m_c = r['crude_import_quantity_mmt']
    x_c = 0.0 # Statutory export restriction
    r_t = r['refinery_crude_processing_mmt']
    
    # Indigenous crude deficit = Throughput - Domestic extraction
    gap_upstream = r_t - p_c
    
    # Crude accounting residual = Imports - Gap = (P_c + M_c) - R_t
    crude_residual = (p_c + m_c) - r_t
    
    # Distinct crude indicators
    # 1. Supply-Pool Import Share (SPS) = M_c / (M_c + P_c) * 100
    sps = (m_c / (m_c + p_c)) * 100.0
    
    # 2. Import-to-Refinery Ratio (IRR) = M_c / R_t * 100
    irr = (m_c / r_t) * 100.0
    
    # 3. Indigenous Crude Sufficiency Ratio (SSR) = P_c / R_t * 100
    ssr = (p_c / r_t) * 100.0
    
    # Downstream Total Products
    prod_output = r['petroleum_product_production_mmt']
    prod_cons = r['petroleum_product_consumption_mmt']
    prod_imp = r['petroleum_product_imports_mmt']
    prod_exp = r['petroleum_product_exports_mmt']
    net_prod_exp = prod_exp - prod_imp
    
    # Downstream Coverage Ratio = Total Product Production / Total Product Consumption * 100
    refining_coverage = (prod_output / prod_cons) * 100.0
    
    # LPG specific indicators
    lpg_data = lpg_map.get(period, {})
    lpg_prod_val = lpg_data.get('lpg_production_mmt', np.nan)
    lpg_imp_val = lpg_data.get('lpg_import_mmt', np.nan)
    lpg_exp_val = lpg_data.get('lpg_export_mmt', np.nan)
    lpg_net_imp_val = lpg_data.get('lpg_net_import_mmt', np.nan)
    lpg_cons_val = lpg_data.get('lpg_consumption_mmt', np.nan)
    
    lpg_gid = (lpg_imp_val / lpg_cons_val) * 100.0 if pd.notna(lpg_imp_val) and pd.notna(lpg_cons_val) and lpg_cons_val > 0 else np.nan
    lpg_nid = (lpg_net_imp_val / lpg_cons_val) * 100.0 if pd.notna(lpg_net_imp_val) and pd.notna(lpg_cons_val) and lpg_cons_val > 0 else np.nan
    
    records.append({
        'reporting_period': period,
        'fiscal_year_start': yr_start,
        'fiscal_year_end': yr_end,
        'domestic_crude_production_mmt': round(p_c, 4),
        'crude_import_quantity_mmt': round(m_c, 4),
        'crude_export_quantity_mmt': round(x_c, 4),
        'refinery_crude_processing_mmt': round(r_t, 4),
        'indigenous_crude_deficit_mmt': round(gap_upstream, 4),
        'unreconciled_crude_residual_mmt': round(crude_residual, 4),
        'crude_supply_pool_import_share_pct': round(sps, 4),
        'crude_import_to_refinery_ratio_pct': round(irr, 4),
        'indigenous_crude_sufficiency_ratio_pct': round(ssr, 4),
        'petroleum_product_production_mmt': round(prod_output, 4),
        'petroleum_product_consumption_mmt': round(prod_cons, 4),
        'petroleum_product_imports_mmt': round(prod_imp, 4),
        'petroleum_product_exports_mmt': round(prod_exp, 4),
        'net_product_export_balance_mmt': round(net_prod_exp, 4),
        'refining_product_coverage_ratio_pct': round(refining_coverage, 4),
        'lpg_production_mmt': round(lpg_prod_val, 4) if pd.notna(lpg_prod_val) else np.nan,
        'lpg_import_mmt': round(lpg_imp_val, 4) if pd.notna(lpg_imp_val) else np.nan,
        'lpg_export_mmt': round(lpg_exp_val, 4) if pd.notna(lpg_exp_val) else np.nan,
        'lpg_net_import_mmt': round(lpg_net_imp_val, 4) if pd.notna(lpg_net_imp_val) else np.nan,
        'lpg_consumption_mmt': round(lpg_cons_val, 4) if pd.notna(lpg_cons_val) else np.nan,
        'lpg_gross_import_dependence_gid_pct': round(lpg_gid, 4) if pd.notna(lpg_gid) else np.nan,
        'lpg_net_import_dependence_nid_pct': round(lpg_nid, 4) if pd.notna(lpg_nid) else np.nan,
        'provenance_and_verification_status': 'Verified Historical (PPAC Official Records; Full 26-Year Balanced Panel)'
    })

df_out = pd.DataFrame(records)
out_path = '05_Research_Paper/Phase_9B_Correction_Audit/Phase_9B_Recalculated_Indicators.csv'
df_out.to_csv(out_path, index=False)
print(f"Successfully generated {out_path} with {len(df_out)} rows and {len(df_out.columns)} columns.")

# Print summary of key corrected values for FY 2023-24
r24 = df_out[df_out['reporting_period'] == 'FY 2023-24'].iloc[0]
print("\n=== FY 2023-24 AUDITED VALUES ===")
print(f"Domestic Crude Production: {r24['domestic_crude_production_mmt']} MMT")
print(f"Crude Imports: {r24['crude_import_quantity_mmt']} MMT")
print(f"Refinery Crude Processing: {r24['refinery_crude_processing_mmt']} MMT")
print(f"Indigenous Crude Deficit (Throughput - Prod): {r24['indigenous_crude_deficit_mmt']} MMT")
print(f"Unreconciled Crude Residual (Imports - Deficit): {r24['unreconciled_crude_residual_mmt']} MMT")
print(f"Product Production: {r24['petroleum_product_production_mmt']} MMT")
print(f"Product Consumption: {r24['petroleum_product_consumption_mmt']} MMT")
print(f"Refining Product Coverage Ratio: {r24['refining_product_coverage_ratio_pct']}%")
print(f"LPG Imports: {r24['lpg_import_mmt']} MMT")
print(f"LPG Exports: {r24['lpg_export_mmt']} MMT")
print(f"LPG Net Imports: {r24['lpg_net_import_mmt']} MMT")
print(f"LPG Consumption: {r24['lpg_consumption_mmt']} MMT")
print(f"LPG Gross Import Dependence (GID): {r24['lpg_gross_import_dependence_gid_pct']}%")
print(f"LPG Net Import Dependence (NID): {r24['lpg_net_import_dependence_nid_pct']}%")
print(f"Crude Supply-Pool Import Share (SPS): {r24['crude_supply_pool_import_share_pct']}%")
print(f"Crude Import-to-Refinery Ratio (IRR): {r24['crude_import_to_refinery_ratio_pct']}%")
print(f"Indigenous Crude Sufficiency Ratio (SSR): {r24['indigenous_crude_sufficiency_ratio_pct']}%")
