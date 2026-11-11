import pandas as pd
import numpy as np

# Load product-level dataset
df_prod = pd.read_csv('03_Processed_Data/standardized/petroleum_product_level_dataset.csv')
print("Columns in petroleum_product_level_dataset:")
print(df_prod.columns.tolist())

# Inspect FY 2023-24
fy24 = df_prod[df_prod['reporting_period'] == 'FY 2023-24'].copy()

print("\n=== FY 2023-24 PRODUCT-LEVEL BALANCE ===")
print(fy24[['product_name', 'production_mmt', 'consumption_mmt', 'import_quantity_mmt', 'export_quantity_mmt', 'net_export_quantity_mmt']].to_string())

# Calculate PCR_i for each product
fy24['pcr_pct'] = (fy24['production_mmt'] / fy24['consumption_mmt']) * 100.0
fy24['trade_balance_mmt'] = fy24['production_mmt'] - fy24['consumption_mmt'] # apparent balance
fy24['net_exports_reported_mmt'] = fy24['net_export_quantity_mmt']

print("\n--- Product Coverage Ratios (PCR_i) FY 2023-24 ---")
for idx, r in fy24.iterrows():
    p = r['product_name']
    prod = r['production_mmt']
    cons = r['consumption_mmt']
    pcr = r['pcr_pct']
    net_exp = r['net_export_quantity_mmt']
    print(f"{p:30}: Prod={prod:8.3f} MMT, Cons={cons:8.3f} MMT, PCR={pcr:7.2f}%, NetExp={net_exp:8.3f} MMT")

# Sum of products vs core aggregate
sum_prod = fy24['production_mmt'].sum()
sum_cons = fy24['consumption_mmt'].sum()
sum_pcr = (sum_prod / sum_cons) * 100.0

core = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
core24 = core[core['reporting_period'] == 'FY 2023-24'].iloc[0]
core_prod = core24['petroleum_product_production_mmt']
core_cons = core24['petroleum_product_consumption_mmt']
core_pcr = (core_prod / core_cons) * 100.0

print(f"\nSum of 8 Major Products: Prod={sum_prod:.3f} MMT, Cons={sum_cons:.3f} MMT, PCR={sum_pcr:.2f}%")
print(f"Core Aggregate Dataset:   Prod={core_prod:.3f} MMT, Cons={core_cons:.3f} MMT, PCR={core_pcr:.2f}%")
print(f"Difference (Others/Misc): Prod={core_prod - sum_prod:.3f} MMT, Cons={core_cons - sum_cons:.3f} MMT")
