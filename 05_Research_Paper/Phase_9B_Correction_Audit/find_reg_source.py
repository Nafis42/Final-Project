import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')

print("Testing samples for Crude Imports on Throughput:")
for start_yr in [1997, 1998, 1999]:
    for end_yr in [2022, 2023, 2024, 2025]:
        sub = df[(df['fiscal_year_start'] >= start_yr) & (df['fiscal_year_start'] <= end_yr)].dropna(subset=['crude_import_quantity_mmt', 'refinery_crude_processing_mmt'])
        N = len(sub)
        y = sub['crude_import_quantity_mmt'].values
        x = sub['refinery_crude_processing_mmt'].values
        
        # OLS
        X = np.column_stack([np.ones(N), x])
        beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
        r2 = 1.0 - np.sum((y - X @ beta)**2) / np.sum((y - np.mean(y))**2)
        if abs(beta[1] - 1.011) < 0.05 or abs(beta[1] - 0.9927) < 0.05:
            print(f"Sample {start_yr}-{end_yr} (N={N}): Intercept={beta[0]:.2f}, Slope={beta[1]:.4f}, R2={r2:.4f}")

print("\nTesting samples for Crude Imports on Domestic Crude Production:")
for start_yr in [1997, 1998, 1999]:
    for end_yr in [2022, 2023, 2024, 2025]:
        sub = df[(df['fiscal_year_start'] >= start_yr) & (df['fiscal_year_start'] <= end_yr)].dropna(subset=['crude_import_quantity_mmt', 'domestic_crude_production_mmt'])
        N = len(sub)
        y = sub['crude_import_quantity_mmt'].values
        x = sub['domestic_crude_production_mmt'].values
        
        # OLS
        X = np.column_stack([np.ones(N), x])
        beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
        r2 = 1.0 - np.sum((y - X @ beta)**2) / np.sum((y - np.mean(y))**2)
        print(f"Sample {start_yr}-{end_yr} (N={N}): Intercept={beta[0]:.2f}, Slope={beta[1]:.4f}, R2={r2:.4f}")

# What if x is normalized / standardized? Or what if y is net imports? Or what if x is something else?
# Let's check `04_Analysis/phase8` scripts!
