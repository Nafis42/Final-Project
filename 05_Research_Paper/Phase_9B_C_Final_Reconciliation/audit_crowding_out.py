import pandas as pd
import numpy as np
import scipy.stats as stats

# Load standardized core annual petroleum dataset
df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
df26 = df[(df['fiscal_year_start'] >= 1998) & (df['fiscal_year_start'] <= 2023)].copy().reset_index(drop=True)

M_c = df26['crude_import_quantity_mmt'].values
R_t = df26['refinery_crude_processing_mmt'].values
P_c = df26['domestic_crude_production_mmt'].values

# First differences (N=25)
d_M_c = np.diff(M_c)
d_R_t = np.diff(R_t)
d_P_c = np.diff(P_c)

def regress(y, X_mat, var_names, model_name, hac_lags=2):
    N = len(y)
    X = np.column_stack([np.ones(N), X_mat])
    k = X.shape[1]
    df_resid = N - k
    
    XtX = X.T @ X
    XtX_inv = np.linalg.inv(XtX)
    beta = XtX_inv @ (X.T @ y)
    
    y_hat = X @ beta
    resid = y - y_hat
    
    ss_tot = np.sum((y - np.mean(y))**2)
    ss_res = np.sum(resid**2)
    r2 = 1.0 - (ss_res / ss_tot)
    adj_r2 = 1.0 - (1.0 - r2) * (N - 1) / df_resid
    
    s2 = ss_res / df_resid
    cov_ols = s2 * XtX_inv
    se_ols = np.sqrt(np.diag(cov_ols))
    t_ols = beta / se_ols
    p_ols = 2.0 * (1.0 - stats.t.cdf(np.abs(t_ols), df=df_resid))
    
    # Newey-West HAC
    meat = np.zeros((k, k))
    for t in range(N):
        x_t = X[t, :].reshape(-1, 1)
        meat += (resid[t]**2) * (x_t @ x_t.T)
    for l in range(1, hac_lags + 1):
        w = 1.0 - (l / (hac_lags + 1.0))
        for t in range(l, N):
            x_t = X[t, :].reshape(-1, 1)
            x_tl = X[t - l, :].reshape(-1, 1)
            cross = resid[t] * resid[t - l] * (x_t @ x_tl.T + x_tl @ x_t.T)
            meat += w * cross
    cov_hac = XtX_inv @ meat @ XtX_inv
    se_hac = np.sqrt(np.diag(cov_hac))
    t_hac = beta / se_hac
    p_hac = 2.0 * (1.0 - stats.t.cdf(np.abs(t_hac), df=df_resid))
    
    diff_res = np.diff(resid)
    dw = np.sum(diff_res**2) / ss_res
    
    # Multicollinearity: VIF for regressors (excluding constant)
    vifs = []
    if X_mat.shape[1] > 1:
        for j in range(X_mat.shape[1]):
            y_j = X_mat[:, j]
            X_other = np.delete(X_mat, j, axis=1)
            X_other_c = np.column_stack([np.ones(N), X_other])
            b_j = np.linalg.inv(X_other_c.T @ X_other_c) @ (X_other_c.T @ y_j)
            res_j = y_j - X_other_c @ b_j
            r2_j = 1.0 - np.sum(res_j**2) / np.sum((y_j - np.mean(y_j))**2)
            vif_j = 1.0 / (1.0 - r2_j) if (1.0 - r2_j) > 0 else np.inf
            vifs.append(vif_j)
    else:
        vifs = [1.0]
        
    # Condition number
    cond_num = np.linalg.cond(X)
    
    return {
        'model_name': model_name,
        'N': N,
        'df_resid': df_resid,
        'beta': beta,
        'se_ols': se_ols,
        't_ols': t_ols,
        'p_ols': p_ols,
        'se_hac': se_hac,
        't_hac': t_hac,
        'p_hac': p_hac,
        'r2': r2,
        'adj_r2': adj_r2,
        'dw': dw,
        'vifs': vifs,
        'cond_num': cond_num,
        'var_names': ['Intercept'] + var_names
    }

print("Running regressions...")
m3 = regress(M_c, P_c.reshape(-1, 1), ['P_c'], 'MOD-03: Bivariate Level (Imports on Production)')
m4 = regress(np.log(M_c), np.log(P_c).reshape(-1, 1), ['ln_P_c'], 'MOD-04: Bivariate Log-Log (ln Imports on ln Production)')
m5 = regress(M_c, np.column_stack([R_t, P_c]), ['R_t', 'P_c'], 'MOD-05 (Phase 9B): Multivariate Level (Imports on Throughput & Production)')
m8 = regress(d_M_c, d_P_c.reshape(-1, 1), ['d_P_c'], 'MOD-08: Bivariate First Differences (dImports on dProduction)')
m_mv_diff = regress(d_M_c, np.column_stack([d_R_t, d_P_c]), ['d_R_t', 'd_P_c'], 'MOD-05 (Phase 8) / Model 6 (Phase 9B): Multivariate First Differences')
m_mv_log = regress(np.log(M_c), np.column_stack([np.log(R_t), np.log(P_c)]), ['ln_R_t', 'ln_P_c'], 'MOD-01 (Phase 8): Multivariate Log-Log')

models = [m3, m4, m5, m8, m_mv_diff, m_mv_log]
for m in models:
    print("\n" + "="*70)
    print(m['model_name'])
    print(f"N = {m['N']}, R2 = {m['r2']:.4f}, Adj R2 = {m['adj_r2']:.4f}, DW = {m['dw']:.4f}, Cond Num = {m['cond_num']:.2f}")
    for idx, name in enumerate(m['var_names']):
        vif_str = f"VIF={m['vifs'][idx-1]:.2f}" if idx > 0 and len(m['vifs']) >= idx else ""
        print(f"  {name:15}: Coef={m['beta'][idx]:10.4f}, OLS_SE={m['se_ols'][idx]:8.4f}, HAC_SE={m['se_hac'][idx]:8.4f}, t_HAC={m['t_hac'][idx]:8.3f}, p_HAC={m['p_hac'][idx]:.6f}  {vif_str}")
