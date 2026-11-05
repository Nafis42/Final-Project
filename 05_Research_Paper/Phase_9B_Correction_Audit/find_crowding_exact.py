import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
df_ind = pd.read_csv('03_Processed_Data/standardized/derived_indicators.csv')
merged = pd.merge(df, df_ind, on='reporting_period')
sub = merged[(merged['fiscal_year_start_x'] >= 1998) & (merged['fiscal_year_start_x'] <= 2023)].copy()

cols = sub.select_dtypes(include=[np.number]).columns

print("Searching all columns for regression slope on domestic_crude_production_mmt:")
P = sub['domestic_crude_production_mmt'].values
for col in cols:
    y = sub[col].values
    valid = ~np.isnan(y) & ~np.isnan(P)
    if np.sum(valid) >= 20:
        y_v = y[valid]
        P_v = P[valid]
        X = np.column_stack([np.ones(len(y_v)), P_v])
        try:
            beta = np.linalg.inv(X.T @ X) @ (X.T @ y_v)
            resid = y_v - X @ beta
            s2 = np.sum(resid**2) / (len(y_v) - 2)
            se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
            t_stat = beta[1] / se[1]
            p_val = 2 * (1 - stats.t.cdf(np.abs(t_stat), df=len(y_v)-2))
            r2 = 1.0 - np.sum(resid**2) / np.sum((y_v - np.mean(y_v))**2)
            if abs(p_val - 0.2713) < 0.05 or abs(beta[1] - (-0.3204)) < 0.05 or abs(t_stat - (-1.13)) < 0.1:
                print(f"MATCH: y={col}, beta={beta[1]:.4f}, se={se[1]:.4f}, t={t_stat:.2f}, p={p_val:.4f}, r2={r2:.4f}, N={len(y_v)}")
        except:
            pass

print("\nSearching with y on X where X is something else:")
for c1 in cols:
    for c2 in cols:
        if c1 == c2: continue
        y = sub[c1].values
        x = sub[c2].values
        valid = ~np.isnan(y) & ~np.isnan(x)
        if np.sum(valid) == 26:
            y_v = y[valid]
            x_v = x[valid]
            X = np.column_stack([np.ones(len(y_v)), x_v])
            try:
                beta = np.linalg.inv(X.T @ X) @ (X.T @ y_v)
                resid = y_v - X @ beta
                s2 = np.sum(resid**2) / 24
                se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
                t_stat = beta[1] / se[1]
                p_val = 2 * (1 - stats.t.cdf(np.abs(t_stat), df=24))
                r2 = 1.0 - np.sum(resid**2) / np.sum((y_v - np.mean(y_v))**2)
                if abs(p_val - 0.2713) < 0.005:
                    print(f"EXACT P-VAL MATCH: y={c1}, x={c2} -> beta={beta[1]:.4f}, se={se[1]:.4f}, t={t_stat:.2f}, p={p_val:.4f}, r2={r2:.4f}")
            except:
                pass
