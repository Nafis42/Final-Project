import pandas as pd
import numpy as np
import scipy.stats as stats

# Load data
df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
df26 = df[(df['fiscal_year_start'] >= 1998) & (df['fiscal_year_start'] <= 2023)].copy().reset_index(drop=True)

M_c = df26['crude_import_quantity_mmt'].values
R_t = df26['refinery_crude_processing_mmt'].values
P_c = df26['domestic_crude_production_mmt'].values

d_M_c = np.diff(M_c)
d_R_t = np.diff(R_t)
d_P_c = np.diff(P_c)

print("=== 1. REPRODUCE MOD-07 (Bivariate First Differences) ===")
# Regress d_M_c on d_R_t
N = len(d_M_c)
X = np.column_stack([np.ones(N), d_R_t])
beta = np.linalg.inv(X.T @ X) @ (X.T @ d_M_c)
resid = d_M_c - X @ beta
s2 = np.sum(resid**2) / (N - 2)
cov_ols = s2 * np.linalg.inv(X.T @ X)
se_ols = np.sqrt(np.diag(cov_ols))
t_ols = beta / se_ols
p_ols = 2.0 * (1.0 - stats.t.cdf(np.abs(t_ols), df=N-2))

# HAC Newey-West (lags=2)
meat = np.zeros((2, 2))
for t in range(N):
    x_t = X[t, :].reshape(-1, 1)
    meat += (resid[t]**2) * (x_t @ x_t.T)
for l in range(1, 3):
    w = 1.0 - (l / 3.0)
    for t in range(l, N):
        x_t = X[t, :].reshape(-1, 1)
        x_tl = X[t - l, :].reshape(-1, 1)
        meat += w * resid[t] * resid[t - l] * (x_t @ x_tl.T + x_tl @ x_t.T)
cov_hac = np.linalg.inv(X.T @ X) @ meat @ np.linalg.inv(X.T @ X)
se_hac = np.sqrt(np.diag(cov_hac))
t_hac = beta / se_hac
p_hac = 2.0 * (1.0 - stats.t.cdf(np.abs(t_hac), df=N-2))

r2 = 1.0 - np.sum(resid**2) / np.sum((d_M_c - np.mean(d_M_c))**2)
adj_r2 = 1.0 - (1.0 - r2) * (N - 1) / (N - 2)
dw = np.sum(np.diff(resid)**2) / np.sum(resid**2)

print(f"Sample: N = {N} (FY 1999-00 to FY 2023-24)")
print(f"Intercept: {beta[0]:.4f} (OLS SE={se_ols[0]:.4f}, HAC SE={se_hac[0]:.4f}, t_HAC={t_hac[0]:.3f}, p_HAC={p_hac[0]:.6f})")
print(f"Slope (d_R_t): {beta[1]:.4f} (OLS SE={se_ols[1]:.4f}, HAC SE={se_hac[1]:.4f}, t_HAC={t_hac[1]:.3f}, p_HAC={p_hac[1]:.6f})")
print(f"R2 = {r2:.4f}, Adj R2 = {adj_r2:.4f}, DW = {dw:.4f}")

print("\n=== 2. DICKEY-FULLER / ADF UNIT ROOT TESTING ===")
def adf_test(series, name, regression='c', lags=0):
    """
    Implements Dickey-Fuller / Augmented Dickey-Fuller test:
    dy_t = alpha + (beta*t) + gamma * y_{t-1} + sum(delta_i * dy_{t-i}) + e_t
    regression: 'c' (constant only), 'ct' (constant + trend), 'nc' (no constant)
    """
    y = np.array(series, dtype=float)
    T = len(y)
    dy = np.diff(y)
    
    # We construct y_{t-1} and lagged dy
    # effective sample length depends on lags
    y_lag = y[lags:-1]
    dy_curr = dy[lags:]
    
    regressors = [y_lag]
    
    # Lagged differences
    if lags > 0:
        for i in range(1, lags + 1):
            dy_lag_i = dy[lags - i : -i]
            regressors.append(dy_lag_i)
            
    eff_T = len(dy_curr)
    
    if regression == 'c':
        regressors.append(np.ones(eff_T))
    elif regression == 'ct':
        regressors.append(np.ones(eff_T))
        regressors.append(np.arange(1, eff_T + 1))
    elif regression == 'nc':
        pass
        
    X_mat = np.column_stack(regressors)
    beta_adf = np.linalg.inv(X_mat.T @ X_mat) @ (X_mat.T @ dy_curr)
    res_adf = dy_curr - X_mat @ beta_adf
    df_e = eff_T - X_mat.shape[1]
    s2_adf = np.sum(res_adf**2) / df_e
    cov_adf = s2_adf * np.linalg.inv(X_mat.T @ X_mat)
    se_gamma = np.sqrt(cov_adf[0, 0])
    gamma = beta_adf[0]
    t_stat = gamma / se_gamma
    
    # Critical values for T ~ 25 (from Fuller 1976 / MacKinnon 1996 tables):
    if regression == 'c':
        crit = {'1%': -3.75, '5%': -3.00, '10%': -2.63}
    elif regression == 'ct':
        crit = {'1%': -4.38, '5%': -3.60, '10%': -3.24}
    else:
        crit = {'1%': -2.66, '5%': -1.95, '10%': -1.60}
        
    decision = "Reject Null (Stationary)" if t_stat < crit['5%'] else "Fail to Reject (Non-Stationary / Unit Root)"
    
    return {
        'Series': name,
        'Deterministic': regression,
        'Lags': lags,
        'Eff_T': eff_T,
        'Gamma': gamma,
        'SE': se_gamma,
        'ADF_t_stat': t_stat,
        'Crit_1%': crit['1%'],
        'Crit_5%': crit['5%'],
        'Crit_10%': crit['10%'],
        'Decision_5pct': decision
    }

tests = []
for reg in ['c', 'ct']:
    tests.append(adf_test(M_c, 'Crude Imports (Levels)', regression=reg, lags=0))
    tests.append(adf_test(M_c, 'Crude Imports (Levels)', regression=reg, lags=1))
    tests.append(adf_test(R_t, 'Refinery Throughput (Levels)', regression=reg, lags=0))
    tests.append(adf_test(R_t, 'Refinery Throughput (Levels)', regression=reg, lags=1))
    tests.append(adf_test(P_c, 'Domestic Crude (Levels)', regression=reg, lags=0))
    tests.append(adf_test(P_c, 'Domestic Crude (Levels)', regression=reg, lags=1))

for reg in ['c', 'nc']:
    tests.append(adf_test(d_M_c, 'Delta Crude Imports (First Diff)', regression=reg, lags=0))
    tests.append(adf_test(d_M_c, 'Delta Crude Imports (First Diff)', regression=reg, lags=1))
    tests.append(adf_test(d_R_t, 'Delta Refinery Throughput (First Diff)', regression=reg, lags=0))
    tests.append(adf_test(d_R_t, 'Delta Refinery Throughput (First Diff)', regression=reg, lags=1))
    tests.append(adf_test(d_P_c, 'Delta Domestic Crude (First Diff)', regression=reg, lags=0))
    tests.append(adf_test(d_P_c, 'Delta Domestic Crude (First Diff)', regression=reg, lags=1))

adf_df = pd.DataFrame(tests)
print(adf_df[['Series', 'Deterministic', 'Lags', 'Eff_T', 'ADF_t_stat', 'Crit_5%', 'Decision_5pct']].to_string(index=False))
