import pandas as pd
import numpy as np

# Load product-level dataset
df_prod = pd.read_csv('03_Processed_Data/standardized/petroleum_product_level_dataset.csv')
print("Columns in petroleum_product_level_dataset:")
print(df_prod.columns.tolist())

lpg_rows = df_prod[df_prod['product_name'].str.contains('LPG', case=False, na=False)]
print("\nLPG in petroleum_product_level_dataset:")
print(lpg_rows[['reporting_period', 'product_name', 'production_mmt', 'import_quantity_mmt', 'export_quantity_mmt', 'net_export_quantity_mmt', 'consumption_mmt']].to_string())

# Load consumption by product
df_cons = pd.read_csv('03_Processed_Data/standardized/annual_petroleum_product_consumption_by_product.csv')
print("\nColumns in annual_petroleum_product_consumption_by_product:")
print(df_cons.columns.tolist())
lpg_cons = df_cons[df_cons['product_name'].str.contains('LPG', case=False, na=False)]
print("\nLPG in annual_petroleum_product_consumption_by_product (tail 10):")
print(lpg_cons[['reporting_period', 'product_name', 'consumption_tmt', 'consumption_mmt']].tail(10).to_string())

# Load production by product
df_prod_ind = pd.read_csv('03_Processed_Data/standardized/annual_petroleum_product_production.csv')
lpg_prod = df_prod_ind[df_prod_ind['product_name'].str.contains('LPG', case=False, na=False)]
print("\nLPG in annual_petroleum_product_production (tail 10):")
print(lpg_prod[['reporting_period', 'product_name', 'production_tmt', 'production_mmt']].tail(10).to_string())

# Check Phase 8 / Phase 5 outputs for LPG
import glob
print("\nSearching Phase 5 / Phase 6 / Phase 8 files for LPG dependence or 62.74%:")
for fpath in glob.glob('04_Analysis/**/*.csv', recursive=True) + glob.glob('04_Analysis/**/*.md', recursive=True) + glob.glob('05_Research_Paper/**/*.md', recursive=True) + glob.glob('05_Research_Paper/**/*.csv', recursive=True):
    try:
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if '62.74' in content or '62.7' in content:
                print(f"Found in: {fpath}")
    except Exception as e:
        pass
