import pandas as pd
import numpy as np
import scipy.stats as stats

def run_ols(y, X_vars, var_names, y_name, hac_lags=2):
    """
    Run OLS regression with conventional and HAC (Newey-West) standard errors.
    """
    y = np.array(y, dtype=float)
    N = len(y)
    
    # Add constant
    X = np.column_stack([np.ones(N), X_vars])
    k = X.shape[1] # number of parameters
    df_resid = N - k
    
    # OLS estimator: beta = (X'X)^(-1) X'y
    XtX = X.T @ X
    XtX_inv = np.linalg.inv(XtX)
    beta = XtX_inv @ (X.T @ y)
    
    # Residuals & Fitted
    y_hat = X @ beta
    resid = y - y_hat
    
    # Sum of squares
    ss_tot = np.sum((y - np.mean(y))**2)
    ss_res = np.sum(resid**2)
    ss_reg = ss_tot - ss_res
    
    r_squared = 1.0 - (ss_res / ss_tot)
    adj_r_squared = 1.0 - (1.0 - r_squared) * (N - 1) / df_resid
    
    # Residual variance
    s2 = ss_res / df_resid
    std_err_resid = np.sqrt(s2)
    
    # Conventional OLS Covariance Matrix
    cov_ols = s2 * XtX_inv
    se_ols = np.sqrt(np.diag(cov_ols))
    t_ols = beta / se_ols
    p_ols = 2.0 * (1.0 - stats.t.cdf(np.abs(t_ols), df=df_resid))
    
    # HAC (Newey-West) Covariance Matrix
    # S_0 = sum(e_t^2 * x_t * x_t')
    # S_l = sum(w_l * e_t * e_{t-l} * (x_t * x_{t-l}' + x_{t-l} * x_t'))
    e = resid
    meat = np.zeros((k, k))
    for t in range(N):
        x_t = X[t, :].reshape(-1, 1)
        meat += (e[t]**2) * (x_t @ x_t.T)
        
    for l in range(1, hac_lags + 1):
        weight = 1.0 - (l / (hac_lags + 1.0))
        for t in range(l, N):
            x_t = X[t, :].reshape(-1, 1)
            x_tl = X[t - l, :].reshape(-1, 1)
            cross = e[t] * e[t - l] * (x_t @ x_tl.T + x_tl @ x_t.T)
            meat += weight * cross
            
    cov_hac = XtX_inv @ meat @ XtX_inv
    se_hac = np.sqrt(np.diag(cov_hac))
    t_hac = beta / se_hac
    p_hac = 2.0 * (1.0 - stats.t.cdf(np.abs(t_hac), df=df_resid))
    
    # Durbin-Watson
    diff_resid = np.diff(resid)
    dw = np.sum(diff_resid**2) / ss_res
    
    # F-statistic (against intercept-only)
    if k > 1:
        f_stat = (ss_reg / (k - 1)) / (ss_res / df_resid)
        f_pval = 1.0 - stats.f.cdf(f_stat, k - 1, df_resid)
    else:
        f_stat, f_pval = np.nan, np.nan
        
    names = ['Intercept'] + var_names
    
    res_df = pd.DataFrame({
        'Variable': names,
        'Coef': beta,
        'SE_OLS': se_ols,
        't_OLS': t_ols,
        'p_OLS': p_ols,
        'SE_HAC': se_hac,
        't_HAC': t_hac,
        'p_HAC': p_hac
    })
    
    summary_stats = {
        'Dependent': y_name,
        'N': N,
        'df_resid': df_resid,
        'R2': r_squared,
        'Adj_R2': adj_r_squared,
        'Resid_Std_Err': std_err_resid,
        'F_stat': f_stat,
        'F_pval': f_pval,
        'DW': dw
    }
    
    return res_df, summary_stats

# Load data
df = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
df26 = df[(df['fiscal_year_start'] >= 1998) & (df['fiscal_year_start'] <= 2023)].copy().reset_index(drop=True)

M_c = df26['crude_import_quantity_mmt'].values
R_t = df26['refinery_crude_processing_mmt'].values
P_c = df26['domestic_crude_production_mmt'].values

print("="*80)
print("MODEL 1: Level-Level Bivariate Regression: Crude Imports on Refinery Throughput")
res1, stats1 = run_ols(M_c, R_t.reshape(-1, 1), ['Refinery_Throughput_R_t'], 'Crude_Imports_M_c')
print(res1.to_string(index=False))
for k, v in stats1.items():
    print(f"  {k}: {v}")

print("\n" + "="*80)
print("MODEL 2: Log-Log Bivariate Regression: ln(Crude Imports) on ln(Refinery Throughput)")
res2, stats2 = run_ols(np.log(M_c), np.log(R_t).reshape(-1, 1), ['ln_Refinery_Throughput'], 'ln_Crude_Imports')
print(res2.to_string(index=False))
for k, v in stats2.items():
    print(f"  {k}: {v}")

print("\n" + "="*80)
print("MODEL 3: Crowding-Out Level-Level Bivariate: Crude Imports on Domestic Crude Production")
res3, stats3 = run_ols(M_c, P_c.reshape(-1, 1), ['Domestic_Crude_P_c'], 'Crude_Imports_M_c')
print(res3.to_string(index=False))
for k, v in stats3.items():
    print(f"  {k}: {v}")

print("\n" + "="*80)
print("MODEL 4: Crowding-Out Log-Log Bivariate: ln(Crude Imports) on ln(Domestic Crude Production)")
res4, stats4 = run_ols(np.log(M_c), np.log(P_c).reshape(-1, 1), ['ln_Domestic_Crude'], 'ln_Crude_Imports')
print(res4.to_string(index=False))
for k, v in stats4.items():
    print(f"  {k}: {v}")

print("\n" + "="*80)
print("MODEL 5: Multivariate Level-Level: Crude Imports on Throughput AND Production")
X5 = np.column_stack([R_t, P_c])
res5, stats5 = run_ols(M_c, X5, ['Refinery_Throughput', 'Domestic_Crude'], 'Crude_Imports_M_c')
print(res5.to_string(index=False))
for k, v in stats5.items():
    print(f"  {k}: {v}")

print("\n" + "="*80)
print("MODEL 6: First Differences: d(Crude Imports) on d(Throughput) and d(Production)")
d_M_c = np.diff(M_c)
d_R_t = np.diff(R_t)
d_P_c = np.diff(P_c)
X6 = np.column_stack([d_R_t, d_P_c])
res6, stats6 = run_ols(d_M_c, X6, ['d_Refinery_Throughput', 'd_Domestic_Crude'], 'd_Crude_Imports')
print(res6.to_string(index=False))
for k, v in stats6.items():
    print(f"  {k}: {v}")

print("\n" + "="*80)
print("MODEL 7: Bivariate First Differences: d(Crude Imports) on d(Throughput)")
res7, stats7 = run_ols(d_M_c, d_R_t.reshape(-1, 1), ['d_Refinery_Throughput'], 'd_Crude_Imports')
print(res7.to_string(index=False))
for k, v in stats7.items():
    print(f"  {k}: {v}")

print("\n" + "="*80)
print("MODEL 8: Bivariate First Differences: d(Crude Imports) on d(Production)")
res8, stats8 = run_ols(d_M_c, d_P_c.reshape(-1, 1), ['d_Domestic_Crude'], 'd_Crude_Imports')
print(res8.to_string(index=False))
for k, v in stats8.items():
    print(f"  {k}: {v}")
