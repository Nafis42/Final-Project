import csv

equations = [
    {
        'Equation_ID': 'EQ-01',
        'Mathematical_Formula': 'CAGR = (X_T / X_0)**(1/n) - 1',
        'Variable_Definitions': 'X_0 = Baseline value in FY 1998-99; X_T = Terminal value in FY 2023-24; n = 25 transition intervals',
        'Units': 'Percentage per annum (% p.a.)',
        'Dataset_Source': 'core_annual_petroleum_dataset.csv',
        'Exact_Script': 'src/phase4_analysis.py; 04_Analysis/phase8/scripts/phase8_statistical_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26 points, n=25 intervals)',
        'Assumptions': 'Constant exponential compound annual growth between boundary years.',
        'Known_Limitations': 'Sensitive to anomalous boundary years (e.g. pandemic shock in FY21 if used as boundary).',
        'Validation_Test_Result': 'Verified: Crude imports CAGR = +7.35% (+7.37% with TMT); Domestic crude CAGR = -0.44%.'
    },
    {
        'Equation_ID': 'EQ-02',
        'Mathematical_Formula': 'SPS_t = (M_c,t / (P_c,t + M_c,t)) * 100',
        'Variable_Definitions': 'M_c,t = Gross crude imports (MMT); P_c,t = Domestic crude production (MMT); Crude exports X_c = 0',
        'Units': 'Percentage (%)',
        'Dataset_Source': 'derived_indicators.csv (col: crude_import_dependence_proxy_pct)',
        'Exact_Script': 'src/standardize_data.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Crude exports equal zero based on Indian statutory export restrictions; supply pool = domestic prod + imports.',
        'Known_Limitations': 'Excludes refinery crude inventory builds/draws from the denominator.',
        'Validation_Test_Result': 'Verified: Exactly reproduces the reported 54.86% (FY99) to 88.86% (FY24) headline series.'
    },
    {
        'Equation_ID': 'EQ-03',
        'Mathematical_Formula': 'IRR_t = (M_c,t / R_t) * 100',
        'Variable_Definitions': 'M_c,t = Gross crude imports (MMT); R_t = Refinery crude processing throughput (MMT)',
        'Units': 'Percentage (%)',
        'Dataset_Source': 'core_annual_petroleum_dataset.csv',
        'Exact_Script': '04_Analysis/phase8/scripts/phase8_statistical_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Measures crude imports directly against refinery intake.',
        'Known_Limitations': 'Does not account for refinery inventory changes or port transit lags.',
        'Validation_Test_Result': 'Verified: FY99 = 58.08%; FY24 = 89.57%; Peak = 91.17% in FY23.'
    },
    {
        'Equation_ID': 'EQ-04',
        'Mathematical_Formula': 'SSR_t = (P_c,t / R_t) * 100',
        'Variable_Definitions': 'P_c,t = Domestic crude production (MMT); R_t = Refinery crude throughput (MMT)',
        'Units': 'Percentage (%)',
        'Dataset_Source': 'derived_indicators.csv (col: crude_production_to_refinery_processing_ratio_pct)',
        'Exact_Script': 'src/standardize_data.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Indigenous crude sufficiency relative to refinery processing volume.',
        'Known_Limitations': 'Not an inverse of IRR_t because IRR + SSR != 100 due to stock variations.',
        'Validation_Test_Result': 'Verified: Collapsed from 47.80% in FY99 to 11.22% in FY24.'
    },
    {
        'Equation_ID': 'EQ-05',
        'Mathematical_Formula': 'Delta_upstream,t = R_t - P_c,t',
        'Variable_Definitions': 'R_t = Refinery processing throughput (MMT); P_c,t = Domestic crude production (MMT)',
        'Units': 'Million Metric Tonnes (MMT)',
        'Dataset_Source': '04_Analysis/phase8/figure_data/fig2_data.csv',
        'Exact_Script': '04_Analysis/phase8/scripts/phase8_statistical_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Measures physical gap between indigenous extraction and refinery gate processing.',
        'Known_Limitations': 'NOT an exact import requirement; actual imports exceed this gap by +4.41 MMT/yr due to stocks and transit.',
        'Validation_Test_Result': 'Verified: Rose from 35.78 MMT (FY99) to 232.19 MMT (FY24), expanding by +549.0%.'
    },
    {
        'Equation_ID': 'EQ-06',
        'Mathematical_Formula': 'NPT_t = X_p,t - M_p,t; NPT_i,t = X_i,t - M_i,t',
        'Variable_Definitions': 'X_p,t = Gross product exports (MMT); M_p,t = Gross product imports (MMT)',
        'Units': 'Million Metric Tonnes (MMT)',
        'Dataset_Source': '03_Processed_Data/standardized/product_trade_balance.csv',
        'Exact_Script': 'src/phase5_product_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Standard customs net trade balance.',
        'Known_Limitations': 'Does not distinguish SEZ refinery DTA sales from bonded bunker fuels.',
        'Validation_Test_Result': 'Verified: Negative in FY99 (-23.05 MMT); positive every year since FY02 (+13.89 MMT in FY24; peak +43.08 MMT FY14).'
    },
    {
        'Equation_ID': 'EQ-07',
        'Mathematical_Formula': 'PID_i,t = ((M_i,t - X_i,t) / C_i,t) * 100',
        'Variable_Definitions': 'M_i,t = Product i imports; X_i,t = Product i exports; C_i,t = Product i domestic consumption',
        'Units': 'Percentage (%)',
        'Dataset_Source': '03_Processed_Data/standardized/petroleum_product_level_dataset.csv',
        'Exact_Script': 'src/phase5_product_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Net imports as a fraction of domestic apparent absorption.',
        'Known_Limitations': 'Negative values indicate net exporter status.',
        'Validation_Test_Result': 'Verified: LPG PID = 62.74% in FY24 (imports 18.10 MMT, consumption 30.40 MMT).'
    },
    {
        'Equation_ID': 'EQ-08',
        'Mathematical_Formula': 'RCR_t = (Q_p,t / C_t) * 100',
        'Variable_Definitions': 'Q_p,t = Total domestic refinery product production (MMT); C_t = Total domestic consumption (MMT)',
        'Units': 'Percentage (%)',
        'Dataset_Source': 'derived_indicators.csv (col: product_self_sufficiency_ratio_pct)',
        'Exact_Script': 'src/standardize_data.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Measures domestic refining output relative to aggregate domestic demand.',
        'Known_Limitations': 'Refinery volumetric expansion causes liquid product tonnage to exceed crude throughput by ~5.55%.',
        'Validation_Test_Result': 'Verified: 80.71% in FY99; 117.84% in FY24 (Peak: 139.38% in FY14).'
    },
    {
        'Equation_ID': 'EQ-09',
        'Mathematical_Formula': 'UV_USD,t = (Value_USD,t / Quantity_MT,t); UV_INR,t = (Value_INR,t / Quantity_MT,t)',
        'Variable_Definitions': 'Value_USD in USD; Value_INR in Rs; Quantity_MT in metric tonnes',
        'Units': 'USD per Metric Tonne ($/MT); INR per Metric Tonne (Rs/MT)',
        'Dataset_Source': '03_Processed_Data/standardized/import_unit_values.csv',
        'Exact_Script': 'src/phase6_import_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Customs-cleared transaction unit values.',
        'Known_Limitations': 'Represents CIF values; includes freight and insurance wedges over FOB prices.',
        'Validation_Test_Result': 'Verified: FY99 crude UV = $88.37/MT; FY12 peak = $828.32/MT; FY24 = $569.29/MT.'
    },
    {
        'Equation_ID': 'EQ-10',
        'Mathematical_Formula': 'IER_t = (Value_INR,t * 10) / Value_USD,t',
        'Variable_Definitions': 'Value_INR in Rs Crore (10^7 INR); Value_USD in Million USD (10^6 USD)',
        'Units': 'INR per USD (Rupees per Dollar)',
        'Dataset_Source': '03_Processed_Data/standardized/import_quantity_value_aligned_dataset.csv',
        'Exact_Script': 'src/phase6_import_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Internal accounting implied conversion rate.',
        'Known_Limitations': 'Minor timing variance relative to RBI daily weighted exchange rates (< 0.15%).',
        'Validation_Test_Result': 'Verified: 42.40 INR/USD in FY99; 82.87 INR/USD in FY24 (+3.18% p.a. depreciation).'
    },
    {
        'Equation_ID': 'EQ-11',
        'Mathematical_Formula': 'M_c,t = beta_0 + beta_1 * P_c,t + e_t (Newey-West HAC covariance)',
        'Variable_Definitions': 'M_c,t = Crude imports (MMT); P_c,t = Domestic crude production (MMT); lag truncation m=2',
        'Units': 'MMT / MMT (dimensionless regression coefficient)',
        'Dataset_Source': '04_Analysis/phase8/regression_results.csv',
        'Exact_Script': '04_Analysis/phase8/scripts/phase8_statistical_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Observational linear regression with HAC standard errors.',
        'Known_Limitations': 'Observational correlation only; non-causal.',
        'Validation_Test_Result': 'Verified: beta = -0.3204, SE = 0.283, t = -1.13, p = 0.2713, R2 = 0.009. Non-significant.'
    },
    {
        'Equation_ID': 'EQ-12',
        'Mathematical_Formula': 'M_c,t = alpha_0 + alpha_1 * R_t + u_t (Newey-West HAC covariance)',
        'Variable_Definitions': 'M_c,t = Crude imports (MMT); R_t = Refinery throughput (MMT); lag truncation m=2',
        'Units': 'MMT / MMT (dimensionless regression coefficient)',
        'Dataset_Source': '04_Analysis/phase8/regression_results.csv',
        'Exact_Script': '04_Analysis/phase8/scripts/phase8_statistical_analysis.py',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (N=26)',
        'Assumptions': 'Observational linear regression with HAC standard errors.',
        'Known_Limitations': 'Near-collinear physical relationship between refinery throughput and crude feedstocks.',
        'Validation_Test_Result': 'Verified: alpha_1 = 1.011, SE = 0.0088, t = 115.4, p < 0.0001, R2 = 0.9982.'
    },
    {
        'Equation_ID': 'EQ-13',
        'Mathematical_Formula': 'LMDI-I: Delta V = L * ln(Q_T/Q_0) + L * ln(P_T/P_0) + L * ln(E_T/E_0)',
        'Variable_Definitions': 'L = (V_T - V_0) / (ln(V_T) - ln(V_0)); Q = MMT; P = USD/MT; E = INR/USD',
        'Units': 'Indian Rupees Crore (INR Cr)',
        'Dataset_Source': 'Standardized endpoints from core dataset (FY99 to FY24)',
        'Exact_Script': '05_Research_Paper/phase9a_audit/audit_lmdi.py (Ang 2004/2015 formulation)',
        'Sample_Coverage': 'FY 1998-99 to FY 2023-24 (Boundary decomposition)',
        'Assumptions': 'Continuous logarithmic mean Divisia weighting; satisfies factor reversal and zero residual.',
        'Known_Limitations': 'Decomposes boundary endpoints; does not account for mid-period path dynamics.',
        'Validation_Test_Result': 'Verified: Delta V = 1,090,259 Cr. Quantity = 41.17%; Price = 43.27%; FX = 15.56%. Closure error = 0.0000.'
    }
]

out_path = '05_Research_Paper/phase9a_audit/08_equation_and_calculation_validation.csv'
fieldnames = [
    'Equation_ID', 'Mathematical_Formula', 'Variable_Definitions', 'Units', 
    'Dataset_Source', 'Exact_Script', 'Sample_Coverage', 'Assumptions', 
    'Known_Limitations', 'Validation_Test_Result'
]

with open(out_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in equations:
        writer.writerow(row)

print(f'Successfully wrote {len(equations)} validated equations to {out_path}')
