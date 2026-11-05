import pandas as pd
import numpy as np

df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
sub = df[(df['fiscal_year_start'] >= 1998) & (df['fiscal_year_start'] <= 2023)].copy()

cols = sub.select_dtypes(include=[np.number]).columns

print("Testing all pairwise numeric regressions for slope ~ -0.3204 or slope ~ 1.011:")
for y_col in cols:
    for x_col in cols:
        if y_col == x_col: continue
        y = sub[y_col].values
        x = sub[x_col].values
        valid = ~np.isnan(y) & ~np.isnan(x)
        if np.sum(valid) >= 20:
            y_v = y[valid]
            x_v = x[valid]
            X = np.column_stack([np.ones(len(y_v)), x_v])
            try:
                beta = np.linalg.inv(X.T @ X) @ (X.T @ y_v)
                r2 = 1.0 - np.sum((y_v - X @ beta)**2) / np.sum((y_v - np.mean(y_v))**2)
                if abs(beta[1] - (-0.3204)) < 0.01:
                    print(f"MATCH -0.3204: y={y_col}, x={x_col} -> Coef={beta[1]:.4f}, Intercept={beta[0]:.4f}, R2={r2:.4f}, N={len(y_v)}")
                if abs(beta[1] - 1.011) < 0.01:
                    print(f"MATCH 1.011: y={y_col}, x={x_col} -> Coef={beta[1]:.4f}, Intercept={beta[0]:.4f}, R2={r2:.4f}, N={len(y_v)}")
            except:
                pass

print("\nAlso testing logs:")
for y_col in cols:
    for x_col in cols:
        if y_col == x_col: continue
        y = sub[y_col].values
        x = sub[x_col].values
        valid = ~np.isnan(y) & ~np.isnan(x) & (y > 0) & (x > 0)
        if np.sum(valid) >= 20:
            y_v = np.log(y[valid])
            x_v = np.log(x[valid])
            X = np.column_stack([np.ones(len(y_v)), x_v])
            try:
                beta = np.linalg.inv(X.T @ X) @ (X.T @ y_v)
                r2 = 1.0 - np.sum((y_v - X @ beta)**2) / np.sum((y_v - np.mean(y_v))**2)
                if abs(beta[1] - (-0.3204)) < 0.01:
                    print(f"MATCH LOG -0.3204: y={y_col}, x={x_col} -> Coef={beta[1]:.4f}, Intercept={beta[0]:.4f}, R2={r2:.4f}, N={len(y_v)}")
                if abs(beta[1] - 1.011) < 0.01:
                    print(f"MATCH LOG 1.011: y={y_col}, x={x_col} -> Coef={beta[1]:.4f}, Intercept={beta[0]:.4f}, R2={r2:.4f}, N={len(y_v)}")
            except:
                pass
