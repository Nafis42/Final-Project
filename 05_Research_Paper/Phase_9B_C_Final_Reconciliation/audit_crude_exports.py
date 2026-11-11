import glob
import pandas as pd
import numpy as np

print("=== SEARCHING FOR CRUDE EXPORTS IN ALL DATASETS ===")
# 1. Search standardized datasets
for f in glob.glob('03_Processed_Data/standardized/*.csv'):
    try:
        df = pd.read_csv(f)
        for col in df.columns:
            if 'crude' in col.lower() and 'export' in col.lower():
                print(f"Found in {f} -> col: {col}")
                print(df[['reporting_period', col]].dropna().head(10))
    except:
        pass

# 2. Search raw extractions
print("\n--- Raw Extractions Search ---")
for f in glob.glob('03_Processed_Data/raw_extractions/*.csv'):
    try:
        df = pd.read_csv(f)
        for col in df.columns:
            matches = df[df[col].astype(str).str.contains('crude.*export|export.*crude', case=False, regex=True, na=False)]
            if len(matches) > 0:
                print(f"Match in {f} | col: {col} | count: {len(matches)}")
                print(matches.head(3).to_dict(orient='records'))
    except:
        pass

# 3. Check core_annual_petroleum_dataset.csv
core_df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
print("\n--- Core Annual Petroleum Dataset Crude Export Column ---")
print(core_df[['reporting_period', 'fiscal_year_start', 'crude_export_quantity', 'crude_export_quantity_unit', 'crude_export_quantity_mmt', 'source_notes']].to_string())

# 4. Check derived indicators
ind_df = pd.read_csv('03_Processed_Data/standardized/derived_indicators.csv')
print("\n--- Derived Indicators Notes on Net Crude Imports ---")
print(ind_df[['reporting_period', 'net_crude_imports_tmt', 'net_crude_imports_assumption_notes']].drop_duplicates().to_string())
