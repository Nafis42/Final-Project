import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
sub = df[(df['fiscal_year_start'] >= 1998) & (df['fiscal_year_start'] <= 2023)].copy().reset_index(drop=True)

M = sub['crude_import_quantity_mmt'].values
P = sub['domestic_crude_production_mmt'].values
R = sub['refinery_crude_processing_mmt'].values

# Growth rates
pct_M = np.diff(M) / M[:-1]
pct_P = np.diff(P) / P[:-1]
pct_R = np.diff(R) / R[:-1]

def check(y, x, label):
    N = len(y)
    X = np.column_stack([np.ones(N), x])
    b = np.linalg.inv(X.T @ X) @ (X.T @ y)
    res = y - X @ b
    s2 = np.sum(res**2) / (N - 2)
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    t = b[1] / se[1]
    p = 2 * (1 - stats.t.cdf(np.abs(t), df=N-2))
    r2 = 1.0 - np.sum(res**2) / np.sum((y - np.mean(y))**2)
    if abs(t - (-1.13)) < 0.15 or abs(p - 0.2713) < 0.05 or abs(b[1] - (-0.3204)) < 0.05:
        print(f"MATCH in {label}: b={b[1]:.4f}, se={se[1]:.4f}, t={t:.4f}, p={p:.4f}, r2={r2:.4f}, N={N}")

check(pct_M, pct_P, "pct_M on pct_P")
check(pct_P, pct_M, "pct_P on pct_M")

# Log differences
dln_M = np.diff(np.log(M))
dln_P = np.diff(np.log(P))
check(dln_M, dln_P, "dln_M on dln_P")
check(dln_P, dln_M, "dln_P on dln_M")

# What about import share of throughput vs domestic production?
imp_share = M / R
check(imp_share, P, "imp_share on P")
check(imp_share, np.log(P), "imp_share on ln_P")
check(P, imp_share, "P on imp_share")

# What about net imports?
net_M = sub['crude_import_quantity_mmt'].values # exports are 0 so net_M = M
