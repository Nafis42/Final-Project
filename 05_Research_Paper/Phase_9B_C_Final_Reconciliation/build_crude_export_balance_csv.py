import pandas as pd
import numpy as np

# Load core dataset and trade volumes
df_core = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
core26 = df_core[(df_core['fiscal_year_start'] >= 1998) & (df_core['fiscal_year_start'] <= 2023)].copy().reset_index(drop=True)

df_trade = pd.read_csv('03_Processed_Data/standardized/annual_petroleum_trade_volumes.csv')

records = []
for idx, r in core26.iterrows():
    fy = r['reporting_period']
    yr_start = int(r['fiscal_year_start'])
    
    p_c = r['domestic_crude_production_mmt']
    m_c = r['crude_import_quantity_mmt']
    r_t = r['refinery_crude_processing_mmt']
    
    # In core_annual_petroleum_dataset, crude_export is NaN
    # In annual_petroleum_trade_volumes, crude_oil_exports_mmt is 0.0
    # In PPAC PT_IMPORT_TMT_H.xlsx, the table is PRODUCT EXPORT @, no crude export line is published.
    
    # Conditional residual under X_c = 0
    cond_res = (p_c + m_c) - r_t
    
    # Export-adjusted residual (since observed/statutory exports are 0, Res = cond_res; if hypothetical X_c > 0, Res would be lower)
    # Explicitly distinguish observation status:
    obs_status = "Unreported in PPAC Trade Returns (Statutorily Restricted / Mandated Domestic Processing; Treated as 0.0)"
    
    records.append({
        'Financial_Year': fy,
        'Fiscal_Year_Start': yr_start,
        'Domestic_Crude_Production_MMT': round(p_c, 4),
        'Gross_Crude_Imports_MMT': round(m_c, 4),
        'Crude_Exports_Observed_MMT': "Unreported (0.0 assumed)",
        'Export_Observation_Status': obs_status,
        'Refinery_Throughput_MMT': round(r_t, 4),
        'Indigenous_Deficit_Gap_MMT': round(r_t - p_c, 4),
        'Conditional_Residual_Zero_Exports_MMT': round(cond_res, 4),
        'Export_Adjusted_Residual_MMT': round(cond_res - 0.0, 4),
        'Source_File': "1751964547_PT_IMPORT_TMT_H.xlsx / core_annual_petroleum_dataset.csv",
        'Source_Table': "PPAC Historical Trade Table (PT_IMPORT_H, rows 9-41)",
        'Evidence_Status': "Conditional: Export line absent in official PPAC trade returns; statutory export restriction documented in Foreign Trade Policy (ITC-HS 2709)"
    })

df_exp_audit = pd.DataFrame(records)
out_csv = '05_Research_Paper/Phase_9B_C_Final_Reconciliation/Phase_9B_C_Crude_Export_and_Balance_Audit.csv'
df_exp_audit.to_csv(out_csv, index=False)
print(f"Generated {out_csv} with {len(df_exp_audit)} annual audit records.")

# Print summary statistics
res_vals = df_exp_audit['Conditional_Residual_Zero_Exports_MMT'].astype(float)
print(f"\n26-Year Residual Summary (Conditional on X=0):")
print(f"Mean:   {res_vals.mean():.4f} MMT")
print(f"Std:    {res_vals.std():.4f} MMT")
print(f"Min:    {res_vals.min():.4f} MMT ({df_exp_audit.loc[res_vals.idxmin(), 'Financial_Year']})")
print(f"Max:    {res_vals.max():.4f} MMT ({df_exp_audit.loc[res_vals.idxmax(), 'Financial_Year']})")
print(f"Cumulative: {res_vals.sum():.4f} MMT")
