import pandas as pd
import numpy as np

df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
df26 = df[(df['fiscal_year_start'] >= 1998) & (df['fiscal_year_start'] <= 2023)].copy()

df26['crude_export_quantity_mmt'] = df26['crude_export_quantity_mmt'].fillna(0.0)

# Identity: P_c + M_c - X_c = R_t + Delta_S_c + theta
# Here X_c = 0.
# Unreconciled residual: theta + Delta_S_c = (P_c + M_c) - R_t
df26['indigenous_deficit_mmt'] = df26['refinery_crude_processing_mmt'] - df26['domestic_crude_production_mmt']
df26['crude_residual_mmt'] = (df26['domestic_crude_production_mmt'] + df26['crude_import_quantity_mmt']) - df26['refinery_crude_processing_mmt']

print(df26[['reporting_period', 'domestic_crude_production_mmt', 'crude_import_quantity_mmt', 'refinery_crude_processing_mmt', 'indigenous_deficit_mmt', 'crude_residual_mmt']].to_string())

mean_res = df26['crude_residual_mmt'].mean()
std_res = df26['crude_residual_mmt'].std()
min_idx = df26['crude_residual_mmt'].idxmin()
max_idx = df26['crude_residual_mmt'].idxmax()

print(f"\n26-year Mean Crude Residual: {mean_res:.4f} MMT")
print(f"Standard Deviation: {std_res:.4f} MMT")
print(f"Min Residual: {df26.loc[min_idx, 'crude_residual_mmt']:.4f} MMT in {df26.loc[min_idx, 'reporting_period']}")
print(f"Max Residual: {df26.loc[max_idx, 'crude_residual_mmt']:.4f} MMT in {df26.loc[max_idx, 'reporting_period']}")
print(f"Sum of Domestic Crude Production: {df26['domestic_crude_production_mmt'].sum():.4f} MMT")
print(f"Sum of Crude Imports: {df26['crude_import_quantity_mmt'].sum():.4f} MMT")
print(f"Sum of Refinery Processing: {df26['refinery_crude_processing_mmt'].sum():.4f} MMT")
print(f"Cumulative Residual: {df26['crude_residual_mmt'].sum():.4f} MMT")
print(f"Mean residual = {df26['crude_residual_mmt'].sum() / 26:.4f} MMT")
