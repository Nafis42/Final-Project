import pandas as pd
import numpy as np

# Load the standardized datasets
df_p = pd.read_csv('03_Processed_Data/standardized/annual_petroleum_product_production_by_product.csv')
df_t = pd.read_csv('03_Processed_Data/standardized/annual_petroleum_product_trade_by_product.csv')
df_c = pd.read_csv('03_Processed_Data/standardized/annual_petroleum_product_consumption_by_product.csv')
df_all = pd.read_csv('03_Processed_Data/standardized/petroleum_product_level_dataset.csv')

print("=== Unique products in petroleum_product_level_dataset ===")
print(df_all['product_name'].value_counts())

print("\n=== Check sample of df_all for FY 2023-24 ===")
print(df_all[df_all['fiscal_year_start'] == 2023][['product_name', 'production_tmt', 'import_quantity_tmt', 'export_quantity_tmt', 'consumption_tmt']])
