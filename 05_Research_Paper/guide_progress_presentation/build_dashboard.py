"""
Build Interactive Project Status Dashboard for Guide Presentation
Generates: 05_Research_Paper/guide_progress_presentation/project_status_dashboard.html
Offline, self-contained, interactive HTML dashboard with embedded verified datasets.
"""

import json
import os
import pandas as pd
import numpy as np

def generate_html_dashboard():
    # 1. Load Data
    core = pd.read_csv('03_Processed_Data/standardized/core_annual_petroleum_dataset.csv')
    add = pd.read_csv('04_Analysis/phase8/additional_indicators.csv')
    ptb = pd.read_csv('03_Processed_Data/standardized/product_trade_balance.csv')
    pcon = pd.read_csv('03_Processed_Data/standardized/product_consumption_dataset.csv')
    lmdi = pd.read_csv('04_Analysis/phase6/figure_data/fig6_expenditure_decomposition_contributions.csv')
    corr = pd.read_csv('04_Analysis/phase8/correlation_results.csv')
    reg = pd.read_csv('04_Analysis/phase8/regression_results.csv')
    disc = pd.read_csv('04_Analysis/phase7/discrepancy_register.csv')
    val = pd.read_csv('04_Analysis/phase7/variable_validation_status.csv')
    cat = pd.read_csv('05_Research_Paper/guide_progress_presentation/results_catalogue.csv')

    # 2. Prepare Annual Supply Chain Panel (FY 1998-99 to FY 2023-24)
    years = [f'FY {y}-{str(y+1)[2:]}' for y in range(1998, 2024)]
    annual_sc = []
    for y in years:
        rc = core[core['reporting_period'] == y]
        ra = add[add['reporting_period'] == y]
        if not rc.empty and not ra.empty:
            annual_sc.append({
                'year': y,
                'shortYear': y.replace('FY 19', 'FY').replace('FY 20', 'FY'),
                'domesticProd': round(float(rc['domestic_crude_production_mmt'].values[0]), 2),
                'crudeImports': round(float(rc['crude_import_quantity_mmt'].values[0]), 2),
                'refineryThroughput': round(float(rc['refinery_crude_processing_mmt'].values[0]), 2),
                'crudeDeficitGap': round(float(ra['physical_crude_deficit_gap_mmt'].values[0]), 2),
                'coverageRatio': round(float(ra['indigenous_crude_coverage_ratio_pct'].values[0]), 2),
                'importDep': round(float(ra['crude_import_dependence_proxy_pct'].values[0]), 2),
                'productProd': round(float(rc['petroleum_product_production_mmt'].values[0]), 2),
                'productCons': round(float(rc['petroleum_product_consumption_mmt'].values[0]), 2),
                'netExports': round(float(ra['net_product_export_balance_tmt'].values[0]) / 1000.0, 2),
                'sufficiency': round(float(ra['product_self_sufficiency_ratio_pct'].values[0]), 2),
                'valUSD': round(float(rc['crude_import_value'].values[0]), 1) if pd.notna(rc['crude_import_value'].values[0]) else None,
                'valINR': round(float(rc['crude_import_value_rs_crore'].values[0]), 1) if pd.notna(rc['crude_import_value_rs_crore'].values[0]) else None,
                'fx': round(float(ra['implied_exchange_rate_inr_per_usd'].values[0]), 2) if pd.notna(ra['implied_exchange_rate_inr_per_usd'].values[0]) else None,
                'crudePrice': round(float(rc['crude_price'].values[0]), 2) if pd.notna(rc['crude_price'].values[0]) else None,
                'unitVal': round(float(ra['realized_cif_import_unit_value_usd_bbl'].values[0]), 2) if pd.notna(ra['realized_cif_import_unit_value_usd_bbl'].values[0]) else None
            })

    # 3. Prepare FY 2023-24 Product Trade Balance
    ptb_24 = ptb[ptb['reporting_period'] == 'FY 2023-24'].copy()
    product_tb_list = []
    for _, row in ptb_24.iterrows():
        pname = row['product_name']
        if pname != 'Total Petroleum Products':
            product_tb_list.append({
                'product': pname,
                'imports': round(float(row['import_quantity_mmt']), 3),
                'exports': round(float(row['export_quantity_mmt']), 3),
                'netBalance': round(float(row['trade_balance_mmt']), 3),
                'status': row['trade_status']
            })
    product_tb_list.sort(key=lambda x: x['netBalance'], reverse=True)

    # 4. Prepare LPG vs SKO (Kerosene) Consumption
    lpg_sko = []
    for y in years:
        df_y = pcon[pcon['reporting_period'] == y]
        lpg_row = df_y[df_y['product_standardized_name'] == 'Liquefied Petroleum Gas (LPG)']
        sko_row = df_y[df_y['product_standardized_name'] == 'Superior Kerosene Oil (SKO)']
        lpg_val = round(float(lpg_row['value'].values[0]) / 1000.0, 2) if not lpg_row.empty else None
        sko_val = round(float(sko_row['value'].values[0]) / 1000.0, 2) if not sko_row.empty else None
        lpg_sko.append({
            'year': y.replace('FY 19', 'FY').replace('FY 20', 'FY'),
            'lpg': lpg_val,
            'sko': sko_val
        })

    # 5. Prepare Diesel vs Petrol (HSD vs MS) Consumption
    hsd_ms = []
    for y in years:
        df_y = pcon[pcon['reporting_period'] == y]
        hsd_row = df_y[df_y['product_standardized_name'] == 'High Speed Diesel (HSD)']
        ms_row = df_y[df_y['product_standardized_name'] == 'Motor Spirit (Petrol / MS)']
        hsd_val = round(float(hsd_row['value'].values[0]) / 1000.0, 2) if not hsd_row.empty else None
        ms_val = round(float(ms_row['value'].values[0]) / 1000.0, 2) if not ms_row.empty else None
        ratio = round(hsd_val / ms_val, 2) if hsd_val and ms_val and ms_val > 0 else None
        hsd_ms.append({
            'year': y.replace('FY 19', 'FY').replace('FY 20', 'FY'),
            'hsd': hsd_val,
            'ms': ms_val,
            'ratio': ratio
        })

    # 6. Prepare LMDI Decomposition
    lmdi_list = []
    for _, row in lmdi.iterrows():
        lmdi_list.append({
            'period': row['current_period'].replace('FY 19', 'FY').replace('FY 20', 'FY'),
            'deltaTotal': round(float(row['delta_expenditure_million_usd']), 1),
            'qtyContrib': round(float(row['quantity_contribution_million_usd']), 1),
            'priceContrib': round(float(row['price_contribution_million_usd']), 1),
            'driver': row['dominant_driver']
        })

    # 7. Prepare Correlation Results
    corr_list = []
    for _, row in corr.iterrows():
        corr_list.append({
            'pair': row['Pair Description'],
            'var1': row['Variable 1'],
            'var2': row['Variable 2'],
            'n': int(row['Sample Size (N)']),
            'period': row['Period Coverage'],
            'rLevels': round(float(row['Pearson r (Levels)']), 4),
            'pLevels': round(float(row['Pearson p-value (Levels)']), 5),
            'rDiff': round(float(row['Pearson r (First Differences)']), 4),
            'pDiff': round(float(row['Pearson p-value (First Differences)']), 5),
            'interpretation': row['Interpretation']
        })

    # 8. Prepare Regression Results
    reg_list = []
    for _, row in reg.iterrows():
        reg_list.append({
            'modelId': str(row['Model ID']),
            'rq': str(row['Model Name']),
            'depVar': str(row['Dependent Variable']),
            'indepVar': str(row['Independent Variable']),
            'beta': round(float(row['Coefficient']), 4) if pd.notna(row['Coefficient']) else None,
            'se': round(float(row['Std Error']), 4) if pd.notna(row['Std Error']) else None,
            'tStat': round(float(row['t-Statistic']), 2) if pd.notna(row['t-Statistic']) else None,
            'pVal': round(float(row['p-Value']), 5) if pd.notna(row['p-Value']) else None,
            'r2': round(float(row['Model R-Squared']), 4) if pd.notna(row['Model R-Squared']) else None,
            'interpretation': str(row['Specification Notes'])
        })

    # 9. Prepare Discrepancy Register
    disc_list = []
    for idx, row in disc.iterrows():
        disc_list.append({
            'id': f'DISC-0{idx+1}',
            'variable': str(row['variable']),
            'nature': f"{row['cause']} ({row['period']})",
            'magnitude': f"Diff: {row['absolute_diff']} ({row['percentage_diff']}%)",
            'resolution': str(row['action_required']),
            'status': str(row['resolution_status'])
        })

    # 10. Prepare Validation Status
    val_list = []
    for _, row in val.iterrows():
        val_list.append({
            'variable': str(row['Variable Name']),
            'description': f"{row['Commodity / Domain']} ({row['Historical Coverage']})",
            'status': str(row['Validation Status']),
            'evidence': str(row['Primary Source']),
            'notes': str(row['Summary Rationale'])
        })

    # 11. Prepare Results Catalogue
    cat_list = []
    for _, row in cat.iterrows():
        cat_list.append({
            'id': row['Result ID'],
            'rq': row['Research question'],
            'finding': row['Finding'],
            'value': row['Value'],
            'unit': row['Unit'],
            'period': row['Period'],
            'status': row['Validation status'],
            'limitations': row['Limitations']
        })

    data_json = json.dumps({
        'annualSupplyChain': annual_sc,
        'productTradeBalance': product_tb_list,
        'lpgSko': lpg_sko,
        'hsdMs': hsd_ms,
        'lmdi': lmdi_list,
        'correlations': corr_list,
        'regressions': reg_list,
        'discrepancies': disc_list,
        'validation': val_list,
        'catalogue': cat_list
    })

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>India Petroleum Supply Chain & Import Exposure Dashboard (FY 1998-99 to FY 2023-24)</title>
<style>
  :root {{
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-tertiary: #334155;
    --card-bg: #ffffff;
    --card-border: #e2e8f0;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --text-muted: #64748b;
    --navy-dark: #0a192f;
    --navy-header: #1e3a8a;
    --oil-amber: #d97706;
    --oil-amber-light: #fef3c7;
    --refinery-blue: #2563eb;
    --refinery-blue-light: #eff6ff;
    --crimson-red: #dc2626;
    --crimson-red-light: #fee2e2;
    --emerald-green: #059669;
    --emerald-green-light: #d1fae5;
    --purple: #7c3aed;
    --purple-light: #ede9fe;
    --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}

  body {{
    background-color: #f8fafc;
    color: var(--text-primary);
    line-height: 1.5;
  }}

  /* Top Academic Header */
  header.academic-header {{
    background: linear-gradient(135deg, #0a192f 0%, #1e3a8a 100%);
    color: #ffffff;
    padding: 24px 36px;
    border-bottom: 4px solid var(--oil-amber);
    box-shadow: var(--shadow-md);
  }}

  .header-content {{
    max-width: 1440px;
    margin: 0 auto;
  }}

  .header-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 16px;
  }}

  .header-titles h1 {{
    font-size: 24px;
    font-weight: 700;
    letter-spacing: -0.02em;
    margin-bottom: 6px;
  }}

  .header-titles p {{
    font-size: 14px;
    color: #cbd5e1;
    font-weight: 400;
  }}

  .badge-container {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }}

  .badge {{
    display: inline-flex;
    align-items: center;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .badge-success {{ background: var(--emerald-green-light); color: var(--emerald-green); }}
  .badge-warning {{ background: var(--oil-amber-light); color: var(--oil-amber); }}
  .badge-info {{ background: var(--refinery-blue-light); color: var(--refinery-blue); }}
  .badge-purple {{ background: var(--purple-light); color: var(--purple); }}

  /* Navigation Bar */
  nav.tab-nav {{
    background: #ffffff;
    border-bottom: 1px solid var(--card-border);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: var(--shadow-sm);
  }}

  .nav-container {{
    max-width: 1440px;
    margin: 0 auto;
    display: flex;
    overflow-x: auto;
    scrollbar-width: none;
  }}

  .nav-container::-webkit-scrollbar {{
    display: none;
  }}

  .tab-btn {{
    background: none;
    border: none;
    padding: 14px 20px;
    font-size: 13px;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
    white-space: nowrap;
    border-bottom: 3px solid transparent;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .tab-btn:hover {{
    color: var(--navy-header);
    background-color: #f1f5f9;
  }}

  .tab-btn.active {{
    color: var(--navy-header);
    border-bottom-color: var(--oil-amber);
    background-color: #f8fafc;
  }}

  /* Main Container */
  main.dashboard-body {{
    max-width: 1440px;
    margin: 24px auto;
    padding: 0 24px 60px 24px;
  }}

  .tab-content {{
    display: none;
    animation: fadeIn 0.25s ease-in-out;
  }}

  .tab-content.active {{
    display: block;
  }}

  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(4px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  /* Typography & Layout Components */
  .section-header {{
    margin-bottom: 20px;
  }}

  .section-header h2 {{
    font-size: 20px;
    font-weight: 700;
    color: var(--navy-dark);
    margin-bottom: 4px;
  }}

  .section-header p {{
    font-size: 13px;
    color: var(--text-muted);
  }}

  .grid-cols-4 {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }}

  .grid-cols-2 {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
    gap: 20px;
    margin-bottom: 24px;
  }}

  .card {{
    background: #ffffff;
    border-radius: 8px;
    border: 1px solid var(--card-border);
    padding: 20px;
    box-shadow: var(--shadow-sm);
    position: relative;
  }}

  .card-kpi {{
    border-left: 4px solid var(--refinery-blue);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .card-kpi.warning {{ border-left-color: var(--oil-amber); }}
  .card-kpi.danger {{ border-left-color: var(--crimson-red); }}
  .card-kpi.success {{ border-left-color: var(--emerald-green); }}

  .kpi-title {{
    font-size: 12px;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .kpi-val {{
    font-size: 26px;
    font-weight: 700;
    color: var(--navy-dark);
    margin-bottom: 4px;
  }}

  .kpi-unit {{
    font-size: 12px;
    color: var(--text-muted);
    font-weight: 400;
    margin-left: 4px;
  }}

  .kpi-meta {{
    font-size: 11px;
    color: var(--text-secondary);
    display: flex;
    justify-content: space-between;
    padding-top: 8px;
    border-top: 1px solid #f1f5f9;
    margin-top: 8px;
  }}

  .kpi-delta {{
    font-weight: 600;
  }}
  .delta-up {{ color: var(--emerald-green); }}
  .delta-down {{ color: var(--crimson-red); }}
  .delta-neutral {{ color: var(--oil-amber); }}

  /* Chart Containers & SVG Styling */
  .chart-card {{
    background: #ffffff;
    border-radius: 8px;
    border: 1px solid var(--card-border);
    padding: 20px;
    box-shadow: var(--shadow-sm);
    margin-bottom: 24px;
  }}

  .chart-title-area {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    flex-wrap: wrap;
    gap: 12px;
  }}

  .chart-title-area h3 {{
    font-size: 16px;
    font-weight: 600;
    color: var(--navy-dark);
  }}

  .chart-controls {{
    display: flex;
    gap: 8px;
  }}

  .filter-btn {{
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
  }}

  .filter-btn.active {{
    background: var(--navy-header);
    color: #ffffff;
    border-color: var(--navy-header);
  }}

  .svg-chart-container {{
    width: 100%;
    overflow-x: auto;
    position: relative;
  }}

  svg.academic-chart {{
    width: 100%;
    height: 380px;
    display: block;
  }}

  .chart-legend {{
    display: flex;
    gap: 16px;
    justify-content: center;
    margin-top: 12px;
    flex-wrap: wrap;
    font-size: 12px;
    color: var(--text-secondary);
  }}

  .legend-item {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}

  .legend-color {{
    width: 12px;
    height: 12px;
    border-radius: 2px;
  }}

  /* Tooltip */
  #chart-tooltip {{
    position: absolute;
    background: rgba(15, 23, 42, 0.95);
    color: #ffffff;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 12px;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.15s ease;
    z-index: 1000;
    box-shadow: var(--shadow-md);
    line-height: 1.4;
  }}

  /* Alert Callouts */
  .callout {{
    padding: 14px 18px;
    border-radius: 6px;
    font-size: 13px;
    margin-bottom: 20px;
    border-left: 4px solid;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }}

  .callout-info {{
    background: var(--refinery-blue-light);
    border-left-color: var(--refinery-blue);
    color: #1e3a8a;
  }}

  .callout-warning {{
    background: var(--oil-amber-light);
    border-left-color: var(--oil-amber);
    color: #78350f;
  }}

  .callout-danger {{
    background: var(--crimson-red-light);
    border-left-color: var(--crimson-red);
    color: #991b1b;
  }}

  /* Academic Tables */
  .table-container {{
    width: 100%;
    overflow-x: auto;
    border-radius: 6px;
    border: 1px solid var(--card-border);
  }}

  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    text-align: left;
  }}

  table.data-table th {{
    background: #f8fafc;
    color: var(--text-secondary);
    font-weight: 600;
    padding: 10px 14px;
    border-bottom: 1px solid var(--card-border);
    white-space: nowrap;
  }}

  table.data-table td {{
    padding: 10px 14px;
    border-bottom: 1px solid #f1f5f9;
    color: var(--text-primary);
  }}

  table.data-table tr:hover {{
    background-color: #f8fafc;
  }}

  .text-right {{ text-align: right; }}
  .text-center {{ text-align: center; }}
  .font-mono {{ font-family: ui-monospace, monospace; }}

  /* Search & Filter Bar */
  .search-filter-box {{
    display: flex;
    gap: 12px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }}

  .search-input {{
    flex: 1;
    min-width: 250px;
    padding: 8px 14px;
    border: 1px solid var(--card-border);
    border-radius: 6px;
    font-size: 13px;
    outline: none;
  }}

  .search-input:focus {{
    border-color: var(--navy-header);
    box-shadow: 0 0 0 2px rgba(30, 58, 138, 0.1);
  }}

  /* Footer */
  footer.academic-footer {{
    background: #ffffff;
    border-top: 1px solid var(--card-border);
    padding: 20px 36px;
    color: var(--text-muted);
    font-size: 12px;
    text-align: center;
  }}
</style>
</head>
<body>

<header class="academic-header">
  <div class="header-content">
    <div class="header-top">
      <div class="header-titles">
        <h1>India's Petroleum Supply Chain & Import Exposure</h1>
        <p>A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption (FY 1998-99 to FY 2023-24)</p>
      </div>
      <div class="badge-container">
        <span class="badge badge-success">&#10003; Phases 1-8 Complete</span>
        <span class="badge badge-warning">&#9888; Phase 9 Pending Review</span>
        <span class="badge badge-info">&#128202; Official PPAC / MoPNG Panel</span>
        <span class="badge badge-purple">&#128274; Reproducible Pipeline</span>
      </div>
    </div>
  </div>
</header>

<nav class="tab-nav">
  <div class="nav-container">
    <button class="tab-btn active" onclick="switchTab('tab-overview')"><span>&#128196;</span> Overview & Context</button>
    <button class="tab-btn" onclick="switchTab('tab-kpi')"><span>&#128200;</span> Executive KPI Matrix</button>
    <button class="tab-btn" onclick="switchTab('tab-supply')"><span>&#9981;</span> Crude Supply & Refining</button>
    <button class="tab-btn" onclick="switchTab('tab-products')"><span>&#128666;</span> Product Trade & LPG Paradox</button>
    <button class="tab-btn" onclick="switchTab('tab-expenditure')"><span>&#128177;</span> Import Bill & Price Effects</button>
    <button class="tab-btn" onclick="switchTab('tab-validation')"><span>&#9745;</span> Validation & Econometrics</button>
    <button class="tab-btn" onclick="switchTab('tab-status')"><span>&#128203;</span> Phase Status & Roadmap</button>
    <button class="tab-btn" onclick="switchTab('tab-catalogue')"><span>&#128218;</span> Results Catalogue (Interactive)</button>
  </div>
</nav>

<main class="dashboard-body">
  <div id="chart-tooltip"></div>

  <!-- TAB 1: OVERVIEW & CONTEXT -->
  <div id="tab-overview" class="tab-content active">
    <div class="section-header">
      <h2>Project Overview & Research Framework</h2>
      <p>Research questions, institutional context, and empirical dataset architecture.</p>
    </div>

    <div class="callout callout-info">
      <div>
        <strong>The Indian Petroleum Supply-Chain Paradox:</strong> Over the past 26 fiscal years, India transformed into one of the world's leading refining powerhouses and a structural net exporter of transport fuels (High Speed Diesel, Petrol, Jet Fuel), while simultaneously experiencing a dramatic escalation in raw crude oil import dependence from 54.86% to 88.86%, alongside an acute structural deficit in household cooking gas (LPG).
      </div>
    </div>

    <div class="grid-cols-2">
      <div class="card">
        <h3 style="font-size:16px; margin-bottom:12px; color:var(--navy-dark); font-weight:700;">Core Research Questions (RQ1 - RQ5)</h3>
        <ul style="padding-left:20px; font-size:13px; color:var(--text-secondary); line-height:1.7;">
          <li><strong>RQ1: Domestic Production vs. Imports:</strong> Has domestic upstream extraction stagnated, and does domestic extraction exert any measurable crowding-out effect on physical crude imports?</li>
          <li><strong>RQ2: Downstream Refining as Import Driver:</strong> How much of the crude import surge is mathematically attributable to the 282% expansion in domestic refining throughput?</li>
          <li><strong>RQ3: Product Trade Bifurcation:</strong> How does India reconcile macroscopic refined product self-sufficiency (>117%) with a massive -17.99 MMT structural import deficit in domestic LPG?</li>
          <li><strong>RQ4: Financial Bill Volatility:</strong> What fraction of the 38-fold increase in import expenditure is driven by global price shocks vs. physical volumes, and how severe is the Rupee depreciation wedge?</li>
          <li><strong>RQ5: Structural Transitions & Policies:</strong> How have landmark welfare policies (PAHAL, PMUY) displaced traditional fuels (Kerosene) and altered domestic consumption compositions?</li>
        </ul>
      </div>

      <div class="card">
        <h3 style="font-size:16px; margin-bottom:12px; color:var(--navy-dark); font-weight:700;">Data Pipeline Architecture & Verification Rigour</h3>
        <p style="font-size:13px; color:var(--text-secondary); margin-bottom:12px;">
          The research is founded entirely on primary administrative data from the Ministry of Petroleum and Natural Gas (MoPNG) and the Petroleum Planning and Analysis Cell (PPAC).
        </p>
        <div style="background:#f8fafc; padding:12px; border-radius:6px; font-size:12px; color:var(--text-secondary); border:1px solid #e2e8f0;">
          <div style="margin-bottom:6px;">&#128193; <strong>Primary Source Files:</strong> 33 documents (19 Excel Workbooks, 198 Worksheets, 14 Administrative PDFs)</div>
          <div style="margin-bottom:6px;">&#9745; <strong>Reconciliation Checks:</strong> 218 automated balance tests executed with 100% PASS rate</div>
          <div style="margin-bottom:6px;">&#128279; <strong>Master Supply-Chain Panel:</strong> 30 periods, 35 fields; full cell-level provenance mapped</div>
          <div style="margin-bottom:6px;">&#128202; <strong>Econometric Standards:</strong> Newey-West HAC standard errors; explicit non-causality safeguards</div>
          <div>&#128104;&#8205;&#128219; <strong>Supervisor Milestone:</strong> Guide presentation of verified Phases 1-8 prior to Phase 9 paper drafting</div>
        </div>
      </div>
    </div>
  </div>

  <!-- TAB 2: EXECUTIVE KPI MATRIX -->
  <div id="tab-kpi" class="tab-content">
    <div class="section-header">
      <h2>Executive KPI Matrix (FY 1998-99 to FY 2023-24)</h2>
      <p>Key historical metrics verified against official publications. All values represent settled full fiscal-year balances.</p>
    </div>

    <div class="grid-cols-4">
      <div class="card card-kpi warning">
        <div class="kpi-title">
          <span>Domestic Crude Production</span>
          <span class="badge badge-warning">Qualified</span>
        </div>
        <div class="kpi-val">29.36<span class="kpi-unit">MMT</span></div>
        <div class="kpi-meta">
          <span>FY99: 32.76 MMT</span>
          <span class="kpi-delta delta-down">-10.4% (CAGR -0.44%)</span>
        </div>
      </div>

      <div class="card card-kpi danger">
        <div class="kpi-title">
          <span>Crude Oil Imports</span>
          <span class="badge badge-success">Verified</span>
        </div>
        <div class="kpi-val">234.26<span class="kpi-unit">MMT</span></div>
        <div class="kpi-meta">
          <span>FY99: 39.81 MMT</span>
          <span class="kpi-delta delta-up">+488.5% (CAGR +7.37%)</span>
        </div>
      </div>

      <div class="card card-kpi">
        <div class="kpi-title">
          <span>Refinery Throughput</span>
          <span class="badge badge-success">Verified</span>
        </div>
        <div class="kpi-val">261.55<span class="kpi-unit">MMT</span></div>
        <div class="kpi-meta">
          <span>FY99: 68.54 MMT</span>
          <span class="kpi-delta delta-up">+281.6% (CAGR +5.51%)</span>
        </div>
      </div>

      <div class="card card-kpi danger">
        <div class="kpi-title">
          <span>Crude Deficit Gap</span>
          <span class="badge badge-success">Audited</span>
        </div>
        <div class="kpi-val">232.19<span class="kpi-unit">MMT</span></div>
        <div class="kpi-meta">
          <span>FY99: 35.78 MMT</span>
          <span class="kpi-delta delta-up">+549.0% (+196.4 MMT)</span>
        </div>
      </div>

      <div class="card card-kpi danger">
        <div class="kpi-title">
          <span>Crude Import Dependence</span>
          <span class="badge badge-success">Audited</span>
        </div>
        <div class="kpi-val">88.86<span class="kpi-unit">%</span></div>
        <div class="kpi-meta">
          <span>FY99: 54.86%</span>
          <span class="kpi-delta delta-up">+34.00 pp</span>
        </div>
      </div>

      <div class="card card-kpi success">
        <div class="kpi-title">
          <span>Product Trade Balance</span>
          <span class="badge badge-success">Verified</span>
        </div>
        <div class="kpi-val">+13.89<span class="kpi-unit">MMT</span></div>
        <div class="kpi-meta">
          <span>FY99: -23.05 MMT</span>
          <span class="kpi-delta delta-up">Structural Net Exporter</span>
        </div>
      </div>

      <div class="card card-kpi danger">
        <div class="kpi-title">
          <span>Crude Import Bill (USD)</span>
          <span class="badge badge-success">Verified</span>
        </div>
        <div class="kpi-val">$133.37<span class="kpi-unit">Billion</span></div>
        <div class="kpi-meta">
          <span>FY99: $3.52B</span>
          <span class="kpi-delta delta-up">38-fold (CAGR +15.70%)</span>
        </div>
      </div>

      <div class="card card-kpi danger">
        <div class="kpi-title">
          <span>Crude Import Bill (INR)</span>
          <span class="badge badge-success">Verified</span>
        </div>
        <div class="kpi-val">11.05<span class="kpi-unit">Lakh Cr</span></div>
        <div class="kpi-meta">
          <span>FY99: 0.15 Lakh Cr</span>
          <span class="kpi-delta delta-up">74-fold (CAGR +18.88%)</span>
        </div>
      </div>
    </div>

    <div class="callout callout-warning">
      <div>
        <strong>Institutional Data Boundary Note:</strong> Domestic crude production figures include lease condensate (accounting for ~7.45% of upstream output, ~2.5 MMT/yr). Motor Spirit retail sales figures include depot-level bio-ethanol blending (12-14% in FY24). Official import values represent CIF payments including international freight and insurance.
      </div>
    </div>
  </div>

  <!-- TAB 3: CRUDE SUPPLY & REFINING -->
  <div id="tab-supply" class="tab-content">
    <div class="section-header">
      <h2>Crude Supply Chain & Refining Throughput Dynamics</h2>
      <p>Tracking the upstream stagnation, downstream refining expansion, and the widening crude deficit gap.</p>
    </div>

    <div class="chart-card">
      <div class="chart-title-area">
        <div>
          <h3>Historical Supply Chain Trajectories: Production, Imports & Processing (MMT)</h3>
          <p style="font-size:12px; color:var(--text-muted);">Empirical decoupling: Stagnant domestic crude vs. surge in refinery throughput and crude imports</p>
        </div>
      </div>
      <div class="svg-chart-container">
        <svg id="chart-supply-trajectories" class="academic-chart" viewBox="0 0 1000 380"></svg>
      </div>
      <div class="chart-legend">
        <div class="legend-item"><span class="legend-color" style="background:#2563eb;"></span> Refinery Throughput (MMT)</div>
        <div class="legend-item"><span class="legend-color" style="background:#dc2626;"></span> Crude Imports (MMT)</div>
        <div class="legend-item"><span class="legend-color" style="background:#d97706;"></span> Domestic Crude Production (MMT)</div>
      </div>
    </div>

    <div class="grid-cols-2">
      <div class="chart-card">
        <div class="chart-title-area">
          <div>
            <h3>The Physical Crude Deficit Gap (MMT)</h3>
            <p style="font-size:12px; color:var(--text-muted);">Refinery Throughput minus Domestic Extraction (Demand deficit bridged by imports)</p>
          </div>
        </div>
        <div class="svg-chart-container">
          <svg id="chart-deficit-gap" class="academic-chart" viewBox="0 0 500 320"></svg>
        </div>
      </div>

      <div class="chart-card">
        <div class="chart-title-area">
          <div>
            <h3>Indigenous Crude Coverage Ratio (%)</h3>
            <p style="font-size:12px; color:var(--text-muted);">Domestic Production as % of Refinery Throughput (Collapsed from 47.8% to 11.2%)</p>
          </div>
        </div>
        <div class="svg-chart-container">
          <svg id="chart-coverage-ratio" class="academic-chart" viewBox="0 0 500 320"></svg>
        </div>
      </div>
    </div>

    <div class="card" style="margin-top:16px;">
      <h3 style="font-size:15px; margin-bottom:8px; color:var(--navy-dark); font-weight:700;">Econometric Investigation: The Crowding-Out Myth</h3>
      <p style="font-size:13px; color:var(--text-secondary); line-height:1.6;">
        A common assumption in energy debates is that domestic extraction displaces crude imports. Our empirical evaluation conclusively refutes this: bivariate correlation between domestic crude extraction and crude imports is zero ($r = 0.096, p = 0.641$). In annual first differences, $r = 0.173, p = 0.408$. In multiple regression controlling for refinery demand, the crowding-out elasticity of domestic production on imports is statistically indistinguishable from zero ($\\beta = -0.3204, t = -1.13, p = 0.2713$).
      </p>
    </div>
  </div>

  <!-- TAB 4: PRODUCT TRADE & LPG PARADOX -->
  <div id="tab-products" class="tab-content">
    <div class="section-header">
      <h2>Petroleum Product Portfolio & The Trade Paradox</h2>
      <p>Disentangling macro self-sufficiency from acute product-level structural deficits.</p>
    </div>

    <div class="chart-card">
      <div class="chart-title-area">
        <div>
          <h3>Product-Wise Net Trade Balances in FY 2023-24 (MMT)</h3>
          <p style="font-size:12px; color:var(--text-muted);">Massive export surpluses in transport fuels vs. structural deficit in LPG and Fuel Oil</p>
        </div>
      </div>
      <div class="svg-chart-container">
        <svg id="chart-product-trade-balance" class="academic-chart" viewBox="0 0 1000 380"></svg>
      </div>
    </div>

    <div class="grid-cols-2">
      <div class="chart-card">
        <div class="chart-title-area">
          <div>
            <h3>The Cooking Fuel Transition: LPG vs. Kerosene (MMT)</h3>
            <p style="font-size:12px; color:var(--text-muted);">LPG surge (+488%) and Kerosene collapse (-95.5%) post-PAHAL/PMUY</p>
          </div>
        </div>
        <div class="svg-chart-container">
          <svg id="chart-lpg-sko" class="academic-chart" viewBox="0 0 500 320"></svg>
        </div>
        <div class="chart-legend">
          <div class="legend-item"><span class="legend-color" style="background:#059669;"></span> LPG Consumption</div>
          <div class="legend-item"><span class="legend-color" style="background:#7c3aed;"></span> SKO (Kerosene) Consumption</div>
        </div>
      </div>

      <div class="chart-card">
        <div class="chart-title-area">
          <div>
            <h3>Automotive Transport Demand: Diesel vs. Petrol (MMT)</h3>
            <p style="font-size:12px; color:var(--text-muted);">Motor Spirit growth (CAGR 7.94%) narrows Diesel-to-Petrol ratio from 6.75 to 2.41</p>
          </div>
        </div>
        <div class="svg-chart-container">
          <svg id="chart-hsd-ms" class="academic-chart" viewBox="0 0 500 320"></svg>
        </div>
        <div class="chart-legend">
          <div class="legend-item"><span class="legend-color" style="background:#2563eb;"></span> HSD (Diesel)</div>
          <div class="legend-item"><span class="legend-color" style="background:#d97706;"></span> MS (Petrol)</div>
        </div>
      </div>
    </div>
  </div>

  <!-- TAB 5: IMPORT BILL & PRICE EFFECTS -->
  <div id="tab-expenditure" class="tab-content">
    <div class="section-header">
      <h2>Petroleum Import Expenditure & Macro Exposure</h2>
      <p>Financial valuation, price transmission, LMDI decomposition, and the currency depreciation wedge.</p>
    </div>

    <div class="grid-cols-2">
      <div class="chart-card">
        <div class="chart-title-area">
          <div>
            <h3>Dual-Currency Crude Import Bill (USD vs. INR)</h3>
            <p style="font-size:12px; color:var(--text-muted);">Rupee depreciation adds +3.18% p.a. growth wedge (CAGR: 18.88% INR vs 15.70% USD)</p>
          </div>
        </div>
        <div class="svg-chart-container">
          <svg id="chart-dual-currency" class="academic-chart" viewBox="0 0 500 320"></svg>
        </div>
        <div class="chart-legend">
          <div class="legend-item"><span class="legend-color" style="background:#2563eb;"></span> USD Bill (Billion $)</div>
          <div class="legend-item"><span class="legend-color" style="background:#dc2626;"></span> INR Bill (Lakh Crore Rs)</div>
        </div>
      </div>

      <div class="chart-card">
        <div class="chart-title-area">
          <div>
            <h3>Crude CIF Unit Value vs. Indian Basket FOB Price ($/bbl)</h3>
            <p style="font-size:12px; color:var(--text-muted);">Realized CIF import unit value closely mirrors benchmark (r = 0.988)</p>
          </div>
        </div>
        <div class="svg-chart-container">
          <svg id="chart-price-unit-val" class="academic-chart" viewBox="0 0 500 320"></svg>
        </div>
        <div class="chart-legend">
          <div class="legend-item"><span class="legend-color" style="background:#d97706;"></span> Indian Basket FOB ($/bbl)</div>
          <div class="legend-item"><span class="legend-color" style="background:#059669;"></span> Realized CIF Unit Value ($/bbl)</div>
        </div>
      </div>
    </div>

    <div class="chart-card">
      <div class="chart-title-area">
        <div>
          <h3>LMDI Annual Import Expenditure Decomposition ($ Million)</h3>
          <p style="font-size:12px; color:var(--text-muted);">Price changes account for 72% of inter-annual expenditure shocks, while volume anchors long-term growth</p>
        </div>
      </div>
      <div class="svg-chart-container">
        <svg id="chart-lmdi" class="academic-chart" viewBox="0 0 1000 340"></svg>
      </div>
      <div class="chart-legend">
        <div class="legend-item"><span class="legend-color" style="background:#dc2626;"></span> Price Contribution ($M)</div>
        <div class="legend-item"><span class="legend-color" style="background:#2563eb;"></span> Quantity Contribution ($M)</div>
      </div>
    </div>
  </div>

  <!-- TAB 6: VALIDATION & ECONOMETRICS -->
  <div id="tab-validation" class="tab-content">
    <div class="section-header">
      <h2>Source Verification & Econometric Robustness</h2>
      <p>Phase 7 audit statuses, systemic discrepancies, and Phase 8 econometric models.</p>
    </div>

    <div class="card" style="margin-bottom:20px;">
      <h3 style="font-size:16px; margin-bottom:12px; color:var(--navy-dark); font-weight:700;">Phase 7: Priority Variables Validation Status</h3>
      <div class="table-container">
        <table class="data-table" id="table-validation">
          <thead>
            <tr>
              <th>Variable Standardized Name</th>
              <th>Description & Metric</th>
              <th>Audit Status</th>
              <th>Primary Source Reference</th>
              <th>Validation Caveat / Boundary</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table>
      </div>
    </div>

    <div class="grid-cols-2">
      <div class="card">
        <h3 style="font-size:15px; margin-bottom:10px; color:var(--navy-dark); font-weight:700;">Systemic Discrepancy Register (Phase 7 Audit)</h3>
        <div class="table-container">
          <table class="data-table" id="table-discrepancies">
            <thead>
              <tr>
                <th>ID</th>
                <th>Variable</th>
                <th>Nature & Magnitude</th>
                <th>Methodological Resolution</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>

      <div class="card">
        <h3 style="font-size:15px; margin-bottom:10px; color:var(--navy-dark); font-weight:700;">Phase 8 Econometric Models (HAC Standard Errors)</h3>
        <div class="table-container">
          <table class="data-table" id="table-regressions">
            <thead>
              <tr>
                <th>Model</th>
                <th>Dependent Variable</th>
                <th>Independent (X)</th>
                <th>Beta (t-stat)</th>
                <th>p-value</th>
                <th>R²</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="callout callout-danger" style="margin-top:16px;">
      <div>
        <strong>Scientific Safeguard on Non-Causality:</strong> All statistical associations reported above reflect empirical co-movement and elasticity across historical annual panels. In accordance with econometrics best practice, these results are not interpreted as unconditional causal mechanisms.
      </div>
    </div>
  </div>

  <!-- TAB 7: PHASE STATUS & ROADMAP -->
  <div id="tab-status" class="tab-content">
    <div class="section-header">
      <h2>Project Phase Status & Academic Paper Roadmap</h2>
      <p>Formal status audit across all project phases and preparation for Phase 9 research paper drafting.</p>
    </div>

    <div class="card" style="margin-bottom:24px;">
      <h3 style="font-size:16px; margin-bottom:12px; color:var(--navy-dark); font-weight:700;">Phase-by-Phase Classification Audit</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Phase</th>
              <th>Phase Scope & Focus</th>
              <th>Verified Classification</th>
              <th>Key Artifacts Generated</th>
              <th>Validation / Verification Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Phase 1</strong></td>
              <td>Source Audit & File Inventory</td>
              <td><span class="badge badge-success">Confirmed complete</span></td>
              <td>`file_inventory.csv`, `workbook_sheet_inventory.csv`, reports</td>
              <td>100% files readable, zero corruption, sheet mappings verified</td>
            </tr>
            <tr>
              <td><strong>Phase 2</strong></td>
              <td>Extraction & Standardization</td>
              <td><span class="badge badge-success">Confirmed complete</span></td>
              <td>16 raw CSVs, 16 standardized panels, data dictionary</td>
              <td>218 automated balance tests passed (`PASS`)</td>
            </tr>
            <tr>
              <td><strong>Phase 3</strong></td>
              <td>Core Dataset Integration</td>
              <td><span class="badge badge-success">Confirmed complete</span></td>
              <td>`core_annual_petroleum_dataset.csv`, `derived_indicators.csv`</td>
              <td>Supply-chain identity verified, cell provenance tracked</td>
            </tr>
            <tr>
              <td><strong>Phase 4</strong></td>
              <td>Macro Trends & Structural Breaks</td>
              <td><span class="badge badge-success">Confirmed complete</span></td>
              <td>79 CAGRs, 9 turning points, 8 figures (PNG/SVG)</td>
              <td>Mann-Kendall trend tests, figure data archived</td>
            </tr>
            <tr>
              <td><strong>Phase 5</strong></td>
              <td>Product Trade & Consumption</td>
              <td><span class="badge badge-success">Confirmed complete</span></td>
              <td>`product_trade_balance.csv`, apparent availability residuals</td>
              <td>LPG structural deficit and SKO phaseout documented</td>
            </tr>
            <tr>
              <td><strong>Phase 6</strong></td>
              <td>Import Value & Price Analysis</td>
              <td><span class="badge badge-success">Confirmed complete</span></td>
              <td>LMDI series, unit values, currency multiplier, 8 figures</td>
              <td>Verified 72% price dominance and +3.18% Rupee wedge</td>
            </tr>
            <tr>
              <td><strong>Phase 7</strong></td>
              <td>Official Source Verification</td>
              <td><span class="badge badge-success">Confirmed complete</span></td>
              <td>`variable_validation_status.csv`, discrepancy register</td>
              <td>7 Verified, 3 Qualified; 82 cross-reconciliations verified</td>
            </tr>
            <tr>
              <td><strong>Phase 8</strong></td>
              <td>Econometrics & Robustness</td>
              <td><span class="badge badge-success">Confirmed complete</span></td>
              <td>Correlations, OLS models, subperiod & COVID checks</td>
              <td>Newey-West HAC standard errors, robustness confirmed</td>
            </tr>
            <tr style="background:#fffbeb;">
              <td><strong>Phase 9</strong></td>
              <td>Academic Research Paper Drafting</td>
              <td><span class="badge badge-warning">Not executed or unconfirmed</span></td>
              <td>Awaiting Supervisor Review & Formal Authorization</td>
              <td>Execution on hold to preserve academic workflow discipline</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="card">
      <h3 style="font-size:16px; margin-bottom:12px; color:var(--navy-dark); font-weight:700;">Phase 9 Research Paper Structure (Planned)</h3>
      <div style="font-size:13px; color:var(--text-secondary); line-height:1.7;">
        <p><strong>Chapter 1: Introduction & Institutional Context:</strong> Problem statement, research questions, APM dismantling, refining deregulation.</p>
        <p><strong>Chapter 2: Data Methodology & Provenance Auditing:</strong> Administrative datasets, harmonization protocols, reconciliation safeguards.</p>
        <p><strong>Chapter 3: The Refining Boom & The Trade Paradox:</strong> Upstream stagnation vs throughput expansion, export powerhouse vs LPG deficit.</p>
        <p><strong>Chapter 4: Import Expenditure Decomposition & Rupee Exposure:</strong> LMDI price-volume decomposition, CIF-FOB spreads, exchange rate pass-through.</p>
        <p><strong>Chapter 5: Policy Implications & Strategic Energy Security:</strong> Strategic petroleum reserves, biofuels, electrification, macro risks.</p>
      </div>
    </div>
  </div>

  <!-- TAB 8: RESULTS CATALOGUE -->
  <div id="tab-catalogue" class="tab-content">
    <div class="section-header">
      <h2>Presentation Results Catalogue (Interactive)</h2>
      <p>Searchable registry of presentation-worthy empirical findings with exact figures, periods, methods, and limitations.</p>
    </div>

    <div class="search-filter-box">
      <input type="text" id="catalogue-search" class="search-input" placeholder="Search findings by keyword, research question, or metric..." onkeyup="filterCatalogue()">
      <button class="filter-btn active" onclick="setCatFilter('all', this)">All Questions</button>
      <button class="filter-btn" onclick="setCatFilter('RQ1', this)">RQ1 (Production/Imports)</button>
      <button class="filter-btn" onclick="setCatFilter('RQ2', this)">RQ2 (Refining/Deficit)</button>
      <button class="filter-btn" onclick="setCatFilter('RQ3', this)">RQ3 (Products/LPG)</button>
      <button class="filter-btn" onclick="setCatFilter('RQ4', this)">RQ4 (Expenditure/FX)</button>
      <button class="filter-btn" onclick="setCatFilter('VAL', this)">Validation/Robustness</button>
    </div>

    <div class="card">
      <div class="table-container">
        <table class="data-table" id="table-catalogue">
          <thead>
            <tr>
              <th>ID</th>
              <th>Research Question</th>
              <th>Empirical Finding</th>
              <th>Value</th>
              <th>Unit</th>
              <th>Period</th>
              <th>Status</th>
              <th>Limitations / Boundary</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table>
      </div>
    </div>
  </div>
</main>

<footer class="academic-footer">
  <p><strong>India's Petroleum Supply Chain and Import Exposure Dashboard</strong> | Academic Research Project (Phases 1-8)</p>
  <p>Data Source: Petroleum Planning and Analysis Cell (PPAC) & Ministry of Petroleum and Natural Gas (MoPNG) | Generated October 2026</p>
</footer>

<script>
// Embedded Data Bundle
const DB = {data_json};

// Tab Switching
function switchTab(tabId) {{
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  
  const target = document.getElementById(tabId);
  if (target) target.classList.add('active');
  
  const btn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick').includes(tabId));
  if (btn) btn.classList.add('active');

  // Trigger chart re-render if active tab has charts
  if (tabId === 'tab-supply') {{ renderSupplyCharts(); }}
  if (tabId === 'tab-products') {{ renderProductCharts(); }}
  if (tabId === 'tab-expenditure') {{ renderExpenditureCharts(); }}
}}

// SVG Chart Utility Functions
function createSvgElement(tag, attrs) {{
  const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const [k, v] of Object.entries(attrs)) {{
    el.setAttribute(k, v);
  }}
  return el;
}}

const tooltip = document.getElementById('chart-tooltip');

function showTooltip(evt, text) {{
  tooltip.innerHTML = text;
  tooltip.style.opacity = '1';
  tooltip.style.left = (evt.pageX + 12) + 'px';
  tooltip.style.top = (evt.pageY - 28) + 'px';
}}

function hideTooltip() {{
  tooltip.style.opacity = '0';
}}

// 1. Supply Trajectories Chart
function renderSupplyCharts() {{
  const svg = document.getElementById('chart-supply-trajectories');
  svg.innerHTML = '';
  const data = DB.annualSupplyChain;
  
  const W = 1000, H = 380;
  const pad = {{ top: 30, right: 30, bottom: 40, left: 60 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  
  const maxVal = 280; // MMT
  const xStep = cW / (data.length - 1);
  
  // Grid & Y-Axis
  for (let val = 0; val <= maxVal; val += 50) {{
    const y = pad.top + cH - (val / maxVal) * cH;
    svg.appendChild(createSvgElement('line', {{
      x1: pad.left, y1: y, x2: W - pad.right, y2: y,
      stroke: '#e2e8f0', 'stroke-dasharray': '3,3'
    }}));
    const txt = createSvgElement('text', {{
      x: pad.left - 10, y: y + 4, 'text-anchor': 'end',
      'font-size': '11', fill: '#64748b'
    }});
    txt.textContent = val;
    svg.appendChild(txt);
  }}

  // Lines
  const seriesConfig = [
    {{ key: 'throughput', color: '#2563eb', label: 'Refinery Throughput' }},
    {{ key: 'imports', color: '#dc2626', label: 'Crude Imports' }},
    {{ key: 'domesticProd', color: '#d97706', label: 'Domestic Crude Production' }}
  ];

  seriesConfig.forEach(s => {{
    let pathD = '';
    data.forEach((d, i) => {{
      const x = pad.left + i * xStep;
      const y = pad.top + cH - (d[s.key] / maxVal) * cH;
      pathD += (i === 0 ? 'M' : 'L') + `${{x}},${{y}} `;
    }});
    svg.appendChild(createSvgElement('path', {{
      d: pathD, fill: 'none', stroke: s.color, 'stroke-width': '2.5'
    }}));

    // Points
    data.forEach((d, i) => {{
      const x = pad.left + i * xStep;
      const y = pad.top + cH - (d[s.key] / maxVal) * cH;
      const circle = createSvgElement('circle', {{
        cx: x, cy: y, r: 3.5, fill: s.color, stroke: '#ffffff', 'stroke-width': '1.5'
      }});
      circle.style.cursor = 'pointer';
      circle.addEventListener('mousemove', e => {{
        showTooltip(e, `<strong>${{d.year}}</strong><br>${{s.label}}: <strong>${{d[s.key]}} MMT</strong>`);
      }});
      circle.addEventListener('mouseout', hideTooltip);
      svg.appendChild(circle);
    }});
  }});

  // X-Axis Labels (alternate for space)
  data.forEach((d, i) => {{
    if (i % 3 === 0 || i === data.length - 1) {{
      const x = pad.left + i * xStep;
      const txt = createSvgElement('text', {{
        x: x, y: H - 12, 'text-anchor': 'middle',
        'font-size': '10', fill: '#64748b'
      }});
      txt.textContent = d.shortYear;
      svg.appendChild(txt);
    }}
  }});

  // Deficit Gap Chart
  renderDeficitChart();
  renderCoverageChart();
}}

function renderDeficitChart() {{
  const svg = document.getElementById('chart-deficit-gap');
  svg.innerHTML = '';
  const data = DB.annualSupplyChain;
  const W = 500, H = 320;
  const pad = {{ top: 25, right: 20, bottom: 40, left: 55 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  const maxVal = 250;
  const xStep = cW / (data.length - 1);

  for (let val = 0; val <= maxVal; val += 50) {{
    const y = pad.top + cH - (val / maxVal) * cH;
    svg.appendChild(createSvgElement('line', {{
      x1: pad.left, y1: y, x2: W - pad.right, y2: y, stroke: '#e2e8f0', 'stroke-dasharray': '2,2'
    }}));
    const txt = createSvgElement('text', {{
      x: pad.left - 8, y: y + 4, 'text-anchor': 'end', 'font-size': '10', fill: '#64748b'
    }});
    txt.textContent = val;
    svg.appendChild(txt);
  }}

  let areaD = `M ${{pad.left}},${{pad.top + cH}} `;
  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const y = pad.top + cH - (d.crudeDeficitGap / maxVal) * cH;
    areaD += `L ${{x}},${{y}} `;
  }});
  areaD += `L ${{pad.left + (data.length - 1) * xStep}},${{pad.top + cH}} Z`;

  svg.appendChild(createSvgElement('path', {{
    d: areaD, fill: 'rgba(220, 38, 38, 0.15)', stroke: 'none'
  }}));

  let lineD = '';
  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const y = pad.top + cH - (d.crudeDeficitGap / maxVal) * cH;
    lineD += (i === 0 ? 'M' : 'L') + `${{x}},${{y}} `;
  }});
  svg.appendChild(createSvgElement('path', {{
    d: lineD, fill: 'none', stroke: '#dc2626', 'stroke-width': '2.5'
  }}));

  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const y = pad.top + cH - (d.crudeDeficitGap / maxVal) * cH;
    const circle = createSvgElement('circle', {{
      cx: x, cy: y, r: 3, fill: '#dc2626', stroke: '#fff', 'stroke-width': '1'
    }});
    circle.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.year}}</strong><br>Deficit Gap: <strong>${{d.crudeDeficitGap}} MMT</strong>`));
    circle.addEventListener('mouseout', hideTooltip);
    svg.appendChild(circle);
    if (i % 5 === 0 || i === data.length - 1) {{
      const txt = createSvgElement('text', {{
        x: x, y: H - 12, 'text-anchor': 'middle', 'font-size': '9', fill: '#64748b'
      }});
      txt.textContent = d.shortYear;
      svg.appendChild(txt);
    }}
  }});
}}

function renderCoverageChart() {{
  const svg = document.getElementById('chart-coverage-ratio');
  svg.innerHTML = '';
  const data = DB.annualSupplyChain;
  const W = 500, H = 320;
  const pad = {{ top: 25, right: 20, bottom: 40, left: 50 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  const maxVal = 60;
  const xStep = cW / (data.length - 1);

  for (let val = 0; val <= maxVal; val += 10) {{
    const y = pad.top + cH - (val / maxVal) * cH;
    svg.appendChild(createSvgElement('line', {{
      x1: pad.left, y1: y, x2: W - pad.right, y2: y, stroke: '#e2e8f0', 'stroke-dasharray': '2,2'
    }}));
    const txt = createSvgElement('text', {{
      x: pad.left - 8, y: y + 4, 'text-anchor': 'end', 'font-size': '10', fill: '#64748b'
    }});
    txt.textContent = val + '%';
    svg.appendChild(txt);
  }}

  let lineD = '';
  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const y = pad.top + cH - (d.coverageRatio / maxVal) * cH;
    lineD += (i === 0 ? 'M' : 'L') + `${{x}},${{y}} `;
  }});
  svg.appendChild(createSvgElement('path', {{
    d: lineD, fill: 'none', stroke: '#d97706', 'stroke-width': '2.5'
  }}));

  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const y = pad.top + cH - (d.coverageRatio / maxVal) * cH;
    const circle = createSvgElement('circle', {{
      cx: x, cy: y, r: 3, fill: '#d97706', stroke: '#fff', 'stroke-width': '1'
    }});
    circle.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.year}}</strong><br>Coverage Ratio: <strong>${{d.coverageRatio}}%</strong>`));
    circle.addEventListener('mouseout', hideTooltip);
    svg.appendChild(circle);
    if (i % 5 === 0 || i === data.length - 1) {{
      const txt = createSvgElement('text', {{
        x: x, y: H - 12, 'text-anchor': 'middle', 'font-size': '9', fill: '#64748b'
      }});
      txt.textContent = d.shortYear;
      svg.appendChild(txt);
    }}
  }});
}}

// 2. Product Charts
function renderProductCharts() {{
  renderHorizontalTradeBalance();
  renderLpgSkoChart();
  renderHsdMsChart();
}}

function renderHorizontalTradeBalance() {{
  const svg = document.getElementById('chart-product-trade-balance');
  svg.innerHTML = '';
  const data = DB.productTradeBalance;
  const W = 1000, H = 380;
  const pad = {{ top: 20, right: 50, bottom: 30, left: 220 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  const barH = cH / data.length;

  const minVal = -20, maxVal = 30;
  const zeroX = pad.left + (Math.abs(minVal) / (maxVal - minVal)) * cW;

  // Zero Line
  svg.appendChild(createSvgElement('line', {{
    x1: zeroX, y1: pad.top, x2: zeroX, y2: H - pad.bottom, stroke: '#64748b', 'stroke-width': '1.5'
  }}));

  data.forEach((d, i) => {{
    const y = pad.top + i * barH + 4;
    const val = d.netBalance;
    const isExport = val >= 0;
    const barWidth = Math.abs(val) / (maxVal - minVal) * cW;
    const x = isExport ? zeroX : zeroX - barWidth;

    const rect = createSvgElement('rect', {{
      x: x, y: y, width: barWidth, height: barH - 8,
      fill: isExport ? '#059669' : '#dc2626', rx: 3
    }});
    rect.style.cursor = 'pointer';
    rect.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.product}}</strong><br>Net Balance: <strong>${{val > 0 ? '+' : ''}}${{val}} MMT</strong><br>Exports: ${{d.exports}} MMT | Imports: ${{d.imports}} MMT`));
    rect.addEventListener('mouseout', hideTooltip);
    svg.appendChild(rect);

    // Label
    const label = createSvgElement('text', {{
      x: pad.left - 10, y: y + (barH - 8) / 2 + 4, 'text-anchor': 'end',
      'font-size': '11', fill: '#334155'
    }});
    label.textContent = d.product;
    svg.appendChild(label);

    // Value text
    const valTxt = createSvgElement('text', {{
      x: isExport ? x + barWidth + 6 : x - 6, y: y + (barH - 8) / 2 + 4,
      'text-anchor': isExport ? 'start' : 'end', 'font-size': '11', 'font-weight': '600',
      fill: isExport ? '#059669' : '#dc2626'
    }});
    valTxt.textContent = (val > 0 ? '+' : '') + val.toFixed(2);
    svg.appendChild(valTxt);
  }});
}}

function renderLpgSkoChart() {{
  const svg = document.getElementById('chart-lpg-sko');
  svg.innerHTML = '';
  const data = DB.lpgSko;
  const W = 500, H = 320;
  const pad = {{ top: 25, right: 20, bottom: 40, left: 50 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  const maxVal = 35;
  const xStep = cW / (data.length - 1);

  for (let val = 0; val <= maxVal; val += 10) {{
    const y = pad.top + cH - (val / maxVal) * cH;
    svg.appendChild(createSvgElement('line', {{
      x1: pad.left, y1: y, x2: W - pad.right, y2: y, stroke: '#e2e8f0', 'stroke-dasharray': '2,2'
    }}));
    const txt = createSvgElement('text', {{
      x: pad.left - 8, y: y + 4, 'text-anchor': 'end', 'font-size': '10', fill: '#64748b'
    }});
    txt.textContent = val;
    svg.appendChild(txt);
  }}

  // LPG line
  let lpgD = '', skoD = '';
  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const yLpg = pad.top + cH - (d.lpg / maxVal) * cH;
    const ySko = pad.top + cH - (d.sko / maxVal) * cH;
    lpgD += (i === 0 ? 'M' : 'L') + `${{x}},${{yLpg}} `;
    skoD += (i === 0 ? 'M' : 'L') + `${{x}},${{ySko}} `;
  }});

  svg.appendChild(createSvgElement('path', {{ d: lpgD, fill: 'none', stroke: '#059669', 'stroke-width': '2.5' }}));
  svg.appendChild(createSvgElement('path', {{ d: skoD, fill: 'none', stroke: '#7c3aed', 'stroke-width': '2.5' }}));

  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const yLpg = pad.top + cH - (d.lpg / maxVal) * cH;
    const c1 = createSvgElement('circle', {{ cx: x, cy: yLpg, r: 3, fill: '#059669', stroke: '#fff', 'stroke-width': '1' }});
    c1.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.year}}</strong><br>LPG: <strong>${{d.lpg}} MMT</strong>`));
    c1.addEventListener('mouseout', hideTooltip);
    svg.appendChild(c1);

    const ySko = pad.top + cH - (d.sko / maxVal) * cH;
    const c2 = createSvgElement('circle', {{ cx: x, cy: ySko, r: 3, fill: '#7c3aed', stroke: '#fff', 'stroke-width': '1' }});
    c2.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.year}}</strong><br>SKO: <strong>${{d.sko}} MMT</strong>`));
    c2.addEventListener('mouseout', hideTooltip);
    svg.appendChild(c2);

    if (i % 5 === 0 || i === data.length - 1) {{
      const txt = createSvgElement('text', {{ x: x, y: H - 12, 'text-anchor': 'middle', 'font-size': '9', fill: '#64748b' }});
      txt.textContent = d.year;
      svg.appendChild(txt);
    }}
  }});
}}

function renderHsdMsChart() {{
  const svg = document.getElementById('chart-hsd-ms');
  svg.innerHTML = '';
  const data = DB.hsdMs;
  const W = 500, H = 320;
  const pad = {{ top: 25, right: 20, bottom: 40, left: 50 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  const maxVal = 100;
  const xStep = cW / (data.length - 1);

  for (let val = 0; val <= maxVal; val += 20) {{
    const y = pad.top + cH - (val / maxVal) * cH;
    svg.appendChild(createSvgElement('line', {{
      x1: pad.left, y1: y, x2: W - pad.right, y2: y, stroke: '#e2e8f0', 'stroke-dasharray': '2,2'
    }}));
    const txt = createSvgElement('text', {{
      x: pad.left - 8, y: y + 4, 'text-anchor': 'end', 'font-size': '10', fill: '#64748b'
    }});
    txt.textContent = val;
    svg.appendChild(txt);
  }}

  let hsdD = '', msD = '';
  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const yHsd = pad.top + cH - (d.hsd / maxVal) * cH;
    const yMs = pad.top + cH - (d.ms / maxVal) * cH;
    hsdD += (i === 0 ? 'M' : 'L') + `${{x}},${{yHsd}} `;
    msD += (i === 0 ? 'M' : 'L') + `${{x}},${{yMs}} `;
  }});

  svg.appendChild(createSvgElement('path', {{ d: hsdD, fill: 'none', stroke: '#2563eb', 'stroke-width': '2.5' }}));
  svg.appendChild(createSvgElement('path', {{ d: msD, fill: 'none', stroke: '#d97706', 'stroke-width': '2.5' }}));

  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const yHsd = pad.top + cH - (d.hsd / maxVal) * cH;
    const c1 = createSvgElement('circle', {{ cx: x, cy: yHsd, r: 3, fill: '#2563eb', stroke: '#fff', 'stroke-width': '1' }});
    c1.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.year}}</strong><br>Diesel (HSD): <strong>${{d.hsd}} MMT</strong>`));
    c1.addEventListener('mouseout', hideTooltip);
    svg.appendChild(c1);

    const yMs = pad.top + cH - (d.ms / maxVal) * cH;
    const c2 = createSvgElement('circle', {{ cx: x, cy: yMs, r: 3, fill: '#d97706', stroke: '#fff', 'stroke-width': '1' }});
    c2.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.year}}</strong><br>Petrol (MS): <strong>${{d.ms}} MMT</strong><br>Ratio HSD/MS: <strong>${{d.ratio}}:1</strong>`));
    c2.addEventListener('mouseout', hideTooltip);
    svg.appendChild(c2);

    if (i % 5 === 0 || i === data.length - 1) {{
      const txt = createSvgElement('text', {{ x: x, y: H - 12, 'text-anchor': 'middle', 'font-size': '9', fill: '#64748b' }});
      txt.textContent = d.year;
      svg.appendChild(txt);
    }}
  }});
}}

// 3. Expenditure Charts
function renderExpenditureCharts() {{
  renderDualCurrencyChart();
  renderPriceUnitValChart();
  renderLmdiChart();
}}

function renderDualCurrencyChart() {{
  const svg = document.getElementById('chart-dual-currency');
  svg.innerHTML = '';
  const data = DB.annualSupplyChain;
  const W = 500, H = 320;
  const pad = {{ top: 25, right: 50, bottom: 40, left: 55 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  const maxUSD = 160; // Billion USD
  const maxINR = 14;  // Lakh Crore Rs
  const xStep = cW / (data.length - 1);

  for (let val = 0; val <= maxUSD; val += 40) {{
    const y = pad.top + cH - (val / maxUSD) * cH;
    svg.appendChild(createSvgElement('line', {{
      x1: pad.left, y1: y, x2: W - pad.right, y2: y, stroke: '#e2e8f0', 'stroke-dasharray': '2,2'
    }}));
    const txt = createSvgElement('text', {{
      x: pad.left - 8, y: y + 4, 'text-anchor': 'end', 'font-size': '10', fill: '#2563eb'
    }});
    txt.textContent = '$' + val + 'B';
    svg.appendChild(txt);
  }}

  let usdD = '', inrD = '';
  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const uVal = d.valUSD / 1000.0;
    const iVal = d.valINR / 100000.0;
    const yU = pad.top + cH - (uVal / maxUSD) * cH;
    const yI = pad.top + cH - (iVal / maxINR) * cH;
    usdD += (i === 0 ? 'M' : 'L') + `${{x}},${{yU}} `;
    inrD += (i === 0 ? 'M' : 'L') + `${{x}},${{yI}} `;
  }});

  svg.appendChild(createSvgElement('path', {{ d: usdD, fill: 'none', stroke: '#2563eb', 'stroke-width': '2.5' }}));
  svg.appendChild(createSvgElement('path', {{ d: inrD, fill: 'none', stroke: '#dc2626', 'stroke-width': '2.5' }}));

  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const uVal = d.valUSD / 1000.0;
    const iVal = d.valINR / 100000.0;
    const yU = pad.top + cH - (uVal / maxUSD) * cH;
    const c1 = createSvgElement('circle', {{ cx: x, cy: yU, r: 3, fill: '#2563eb', stroke: '#fff', 'stroke-width': '1' }});
    c1.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.year}}</strong><br>USD Bill: <strong>$${{uVal.toFixed(1)}}B</strong><br>INR Bill: <strong>${{iVal.toFixed(2)}} Lakh Cr</strong><br>FX: ${{d.fx}} INR/USD`));
    c1.addEventListener('mouseout', hideTooltip);
    svg.appendChild(c1);

    if (i % 5 === 0 || i === data.length - 1) {{
      const txt = createSvgElement('text', {{ x: x, y: H - 12, 'text-anchor': 'middle', 'font-size': '9', fill: '#64748b' }});
      txt.textContent = d.shortYear;
      svg.appendChild(txt);
    }}
  }});
}}

function renderPriceUnitValChart() {{
  const svg = document.getElementById('chart-price-unit-val');
  svg.innerHTML = '';
  const data = DB.annualSupplyChain.filter(d => d.crudePrice !== null);
  const W = 500, H = 320;
  const pad = {{ top: 25, right: 20, bottom: 40, left: 50 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  const maxVal = 130;
  const xStep = cW / (data.length - 1);

  for (let val = 0; val <= maxVal; val += 25) {{
    const y = pad.top + cH - (val / maxVal) * cH;
    svg.appendChild(createSvgElement('line', {{
      x1: pad.left, y1: y, x2: W - pad.right, y2: y, stroke: '#e2e8f0', 'stroke-dasharray': '2,2'
    }}));
    const txt = createSvgElement('text', {{
      x: pad.left - 8, y: y + 4, 'text-anchor': 'end', 'font-size': '10', fill: '#64748b'
    }});
    txt.textContent = '$' + val;
    svg.appendChild(txt);
  }}

  let fD = '', cD = '';
  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const yF = pad.top + cH - (d.crudePrice / maxVal) * cH;
    const yC = pad.top + cH - (d.unitVal / maxVal) * cH;
    fD += (i === 0 ? 'M' : 'L') + `${{x}},${{yF}} `;
    cD += (i === 0 ? 'M' : 'L') + `${{x}},${{yC}} `;
  }});

  svg.appendChild(createSvgElement('path', {{ d: fD, fill: 'none', stroke: '#d97706', 'stroke-width': '2.5' }}));
  svg.appendChild(createSvgElement('path', {{ d: cD, fill: 'none', stroke: '#059669', 'stroke-width': '2.5' }}));

  data.forEach((d, i) => {{
    const x = pad.left + i * xStep;
    const yF = pad.top + cH - (d.crudePrice / maxVal) * cH;
    const c1 = createSvgElement('circle', {{ cx: x, cy: yF, r: 3, fill: '#d97706', stroke: '#fff', 'stroke-width': '1' }});
    c1.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.year}}</strong><br>Indian Basket FOB: <strong>$${{d.crudePrice}}/bbl</strong><br>Realized CIF Unit Val: <strong>$${{d.unitVal}}/bbl</strong>`));
    c1.addEventListener('mouseout', hideTooltip);
    svg.appendChild(c1);

    if (i % 4 === 0 || i === data.length - 1) {{
      const txt = createSvgElement('text', {{ x: x, y: H - 12, 'text-anchor': 'middle', 'font-size': '9', fill: '#64748b' }});
      txt.textContent = d.shortYear;
      svg.appendChild(txt);
    }}
  }});
}}

function renderLmdiChart() {{
  const svg = document.getElementById('chart-lmdi');
  svg.innerHTML = '';
  const data = DB.lmdi;
  const W = 1000, H = 340;
  const pad = {{ top: 20, right: 30, bottom: 40, left: 60 }};
  const cW = W - pad.left - pad.right;
  const cH = H - pad.top - pad.bottom;
  const barW = cW / data.length;

  const minVal = -60000, maxVal = 60000;
  const zeroY = pad.top + (maxVal / (maxVal - minVal)) * cH;

  // Zero Line
  svg.appendChild(createSvgElement('line', {{
    x1: pad.left, y1: zeroY, x2: W - pad.right, y2: zeroY, stroke: '#64748b', 'stroke-width': '1.5'
  }}));

  for (let val = -60000; val <= 60000; val += 30000) {{
    const y = pad.top + ((maxVal - val) / (maxVal - minVal)) * cH;
    if (val !== 0) {{
      svg.appendChild(createSvgElement('line', {{
        x1: pad.left, y1: y, x2: W - pad.right, y2: y, stroke: '#e2e8f0', 'stroke-dasharray': '2,2'
      }}));
      const txt = createSvgElement('text', {{
        x: pad.left - 8, y: y + 4, 'text-anchor': 'end', 'font-size': '10', fill: '#64748b'
      }});
      txt.textContent = (val / 1000) + 'k';
      svg.appendChild(txt);
    }}
  }}

  data.forEach((d, i) => {{
    const x = pad.left + i * barW + 2;
    const w = (barW - 4) / 2;

    // Price bar
    const pVal = d.priceContrib;
    const pH = Math.abs(pVal) / (maxVal - minVal) * cH;
    const pY = pVal >= 0 ? zeroY - pH : zeroY;
    const r1 = createSvgElement('rect', {{
      x: x, y: pY, width: w, height: pH, fill: '#dc2626', rx: 1.5
    }});
    r1.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.period}}</strong><br>Price Effect: <strong>$${{pVal}}M</strong><br>Dominant: ${{d.driver}}`));
    r1.addEventListener('mouseout', hideTooltip);
    svg.appendChild(r1);

    // Quantity bar
    const qVal = d.qtyContrib;
    const qH = Math.abs(qVal) / (maxVal - minVal) * cH;
    const qY = qVal >= 0 ? zeroY - qH : zeroY;
    const r2 = createSvgElement('rect', {{
      x: x + w + 1, y: qY, width: w, height: qH, fill: '#2563eb', rx: 1.5
    }});
    r2.addEventListener('mousemove', e => showTooltip(e, `<strong>${{d.period}}</strong><br>Volume Effect: <strong>$${{qVal}}M</strong><br>Total Delta: $${{d.deltaTotal}}M`));
    r2.addEventListener('mouseout', hideTooltip);
    svg.appendChild(r2);

    if (i % 3 === 0 || i === data.length - 1) {{
      const txt = createSvgElement('text', {{
        x: x + w, y: H - 12, 'text-anchor': 'middle', 'font-size': '9', fill: '#64748b'
      }});
      txt.textContent = d.period;
      svg.appendChild(txt);
    }}
  }});
}}

// 4. Data Tables Population
function populateTables() {{
  // Validation Table
  const tbodyVal = document.querySelector('#table-validation tbody');
  tbodyVal.innerHTML = '';
  DB.validation.forEach(v => {{
    const isQual = v.status.includes('qualification');
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${{v.variable}}</strong></td>
      <td>${{v.description}}</td>
      <td><span class="badge ${{isQual ? 'badge-warning' : 'badge-success'}}">${{v.status}}</span></td>
      <td>${{v.evidence}}</td>
      <td><small style="color:#64748b;">${{v.notes}}</small></td>
    `;
    tbodyVal.appendChild(tr);
  }});

  // Discrepancy Table
  const tbodyDisc = document.querySelector('#table-discrepancies tbody');
  tbodyDisc.innerHTML = '';
  DB.discrepancies.forEach(d => {{
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><span class="badge badge-purple">${{d.id}}</span></td>
      <td><strong>${{d.variable}}</strong></td>
      <td>${{d.nature}} (<em>${{d.magnitude}}</em>)</td>
      <td><small>${{d.resolution}}</small></td>
    `;
    tbodyDisc.appendChild(tr);
  }});

  // Regression Table
  const tbodyReg = document.querySelector('#table-regressions tbody');
  tbodyReg.innerHTML = '';
  DB.regressions.forEach(r => {{
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${{r.modelId}}</strong></td>
      <td>${{r.depVar}}</td>
      <td>${{r.indepVar}}</td>
      <td>${{r.beta}} (${{r.tStat}})</td>
      <td>${{r.pVal < 0.001 ? '<0.001' : r.pVal}}</td>
      <td><strong>${{r.r2}}</strong></td>
    `;
    tbodyReg.appendChild(tr);
  }});

  // Catalogue Table
  renderCatalogue(DB.catalogue);
}}

function renderCatalogue(items) {{
  const tbodyCat = document.querySelector('#table-catalogue tbody');
  tbodyCat.innerHTML = '';
  items.forEach(c => {{
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><span class="badge badge-info">${{c.id}}</span></td>
      <td><small style="color:#2563eb; font-weight:600;">${{c.rq}}</small></td>
      <td><strong>${{c.finding}}</strong></td>
      <td style="color:#0a192f; font-weight:700;">${{c.value}}</td>
      <td>${{c.unit}}</td>
      <td>${{c.period}}</td>
      <td><span class="badge ${{c.status.includes('qualification') ? 'badge-warning' : 'badge-success'}}">${{c.status}}</span></td>
      <td><small style="color:#64748b;">${{c.limitations}}</small></td>
    `;
    tbodyCat.appendChild(tr);
  }});
}}

let currentCatFilter = 'all';

function setCatFilter(cat, btn) {{
  currentCatFilter = cat;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  filterCatalogue();
}}

function filterCatalogue() {{
  const search = document.getElementById('catalogue-search').value.toLowerCase();
  const filtered = DB.catalogue.filter(c => {{
    const matchesCat = (currentCatFilter === 'all') ||
      (currentCatFilter === 'RQ1' && c.rq.includes('RQ1')) ||
      (currentCatFilter === 'RQ2' && c.rq.includes('RQ2')) ||
      (currentCatFilter === 'RQ3' && c.rq.includes('RQ3')) ||
      (currentCatFilter === 'RQ4' && c.rq.includes('RQ4')) ||
      (currentCatFilter === 'VAL' && (c.id.includes('VAL') || c.id.includes('ROB')));
    
    const matchesSearch = c.finding.toLowerCase().includes(search) ||
      c.value.toLowerCase().includes(search) ||
      c.rq.toLowerCase().includes(search) ||
      c.id.toLowerCase().includes(search);

    return matchesCat && matchesSearch;
  }});
  renderCatalogue(filtered);
}}

// Initialize
window.addEventListener('DOMContentLoaded', () => {{
  populateTables();
  renderSupplyCharts();
}});
</script>
</body>
</html>'''

    out_file = '05_Research_Paper/guide_progress_presentation/project_status_dashboard.html'
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f'Successfully generated: {out_file} ({os.path.getsize(out_file):,} bytes)')

if __name__ == '__main__':
    generate_html_dashboard()
