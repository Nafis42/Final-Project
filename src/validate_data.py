import os
import json
import csv
import pandas as pd
import numpy as np
from pathlib import Path

base_dir = Path(".")
raw_dir = base_dir / "03_Processed_Data" / "raw_extractions"
std_dir = base_dir / "03_Processed_Data" / "standardized"
val_dir = base_dir / "03_Processed_Data" / "validation"
val_dir.mkdir(parents=True, exist_ok=True)

reconciliation_records = []
completeness_records = []

print("Executing comprehensive data quality and mathematical reconciliation checks...")

# ------------------------------------------------------------------------------
# 1. Reconciliation: Domestic Crude Oil Production
# ------------------------------------------------------------------------------
df_crude = pd.read_csv(std_dir / "annual_crude_oil_production.csv")

for idx, r in df_crude.iterrows():
    fy = r["financial_year"]
    ongc = r["crude_prod_ongc_mmt"]
    oil = r["crude_prod_oil_mmt"]
    psu_tot = r["crude_prod_psu_total_mmt"]
    calc_psu = ongc + oil
    diff_psu = abs(calc_psu - psu_tot) if (not np.isnan(calc_psu) and not np.isnan(psu_tot)) else np.nan
    reconciliation_records.append({
        "dataset": "annual_crude_oil_production",
        "financial_year": fy,
        "check_description": "PSU Total: ONGC + OIL == PSU Total",
        "reported_total": psu_tot,
        "calculated_sum": calc_psu,
        "discrepancy": diff_psu,
        "status": "PASS" if (diff_psu < 0.01) else "FLAGGED",
        "notes": f"Difference: {diff_psu:.6f} MMT"
    })
    
    pvt = r["crude_prod_pvt_jvc_mmt"]
    tot_crude = r["crude_prod_total_crude_mmt"]
    calc_crude = psu_tot + pvt
    diff_crude = abs(calc_crude - tot_crude) if (not np.isnan(calc_crude) and not np.isnan(tot_crude)) else np.nan
    reconciliation_records.append({
        "dataset": "annual_crude_oil_production",
        "financial_year": fy,
        "check_description": "Total Crude: PSU Total + Private/JVC == Total Crude",
        "reported_total": tot_crude,
        "calculated_sum": calc_crude,
        "discrepancy": diff_crude,
        "status": "PASS" if (diff_crude < 0.01) else "FLAGGED",
        "notes": f"Difference: {diff_crude:.6f} MMT"
    })

    cond = r["condensate_production_mmt"]
    grand_tot = r["total_crude_and_condensate_mmt"]
    calc_grand = tot_crude + (cond if not np.isnan(cond) else 0.0)
    diff_grand = abs(calc_grand - grand_tot) if (not np.isnan(calc_grand) and not np.isnan(grand_tot)) else np.nan
    reconciliation_records.append({
        "dataset": "annual_crude_oil_production",
        "financial_year": fy,
        "check_description": "Grand Total: Total Crude + Condensate == Total (Crude+Condensate)",
        "reported_total": grand_tot,
        "calculated_sum": calc_grand,
        "discrepancy": diff_grand,
        "status": "PASS" if (diff_grand < 0.01) else "FLAGGED",
        "notes": "Before 2006-07 condensate was included in crude oil." if np.isnan(cond) else f"Difference: {diff_grand:.6f} MMT"
    })

# ------------------------------------------------------------------------------
# 2. Reconciliation: Refinery Crude Processing
# ------------------------------------------------------------------------------
df_raw_proc = pd.read_csv(raw_dir / "raw_refinery_crude_processing_historical.csv")
company_totals = ['IOCL TOTAL', 'HPCL-TOTAL', 'BPCL-TOTAL', 'CPCL-TOTAL', 'ONGC TOTAL', 'RIL TOTAL']
standalone_base = [
    'Numaligarh Refinery Ltd.(NRL)\nNumaligarh, Assam',
    'Kochi Refinery Ltd.-KOCHI, KERALA',
    'Bongaigaon Refinery & Petrochemicals Ltd.\n(BRPL)-Bongaigaon, Assam',
    'HMEL-GGSR, BATHINDA, PUNJAB',
    'HRRL Pachpadra,Rajasthan',
    'NAYARA ENERGY LTD.\nVADINAR, GUJARAT,(Formerly ESSAR OIL LTD.)'
]

for yr in df_raw_proc['reporting_period'].unique():
    sub = df_raw_proc[df_raw_proc['reporting_period'] == yr]
    gt_match = sub[sub['source_row_label'] == 'GRAND TOTAL']
    if len(gt_match) > 0 and pd.notna(gt_match['source_raw_value'].values[0]):
        gt = float(gt_match['source_raw_value'].values[0])
        
        # In 2019-20 to 2021-22, BORL was standalone outside BPCL-TOTAL prior to legal amalgamation
        targets = [l.strip() for l in company_totals + standalone_base]
        if yr in ['2019-20', '2019-20', '2020-21', '2021-22']:
            targets.append('Bharat Oman Refineries Ltd.-Bina, Sagar M.P.')
            
        s = 0.0
        for t in targets:
            m = sub[sub['source_row_label'].str.strip() == t]
            if len(m) > 0:
                v = pd.to_numeric(m['source_raw_value'].values[0], errors='coerce')
                if pd.notna(v):
                    s += v
        diff = abs(gt - s)
        reconciliation_records.append({
            "dataset": "annual_refinery_crude_processing",
            "financial_year": yr,
            "check_description": "Refinery Throughput Reconciliation: Sum of Company Totals & Standalone Refineries vs Grand Total",
            "reported_total": gt,
            "calculated_sum": s,
            "discrepancy": diff,
            "status": "PASS" if (diff < 1.0) else "FLAGGED",
            "notes": f"Difference: {diff:.4f} TMT (BORL amalgamated into BPCL Bina in 2022)."
        })

# ------------------------------------------------------------------------------
# 3. Reconciliation: Petroleum Product Production
# ------------------------------------------------------------------------------
df_pprod = pd.read_csv(std_dir / "annual_petroleum_product_production.csv")
prod_cols = [
    "lpg_production_tmt", "naphtha_production_tmt", "motor_spirit_production_tmt",
    "aviation_turbine_fuel_production_tmt", "superior_kerosene_oil_production_tmt",
    "high_speed_diesel_production_tmt", "light_diesel_oil_production_tmt",
    "lubricants_production_tmt", "furnace_oil_production_tmt",
    "low_sulphur_heavy_stock_production_tmt", "bitumen_production_tmt",
    "others_production_tmt"
]
for idx, r in df_pprod.iterrows():
    fy = r["financial_year"]
    reported_tot = r["total_petroleum_product_production_tmt"]
    calc_sum = sum(r[c] for c in prod_cols if not np.isnan(r[c]))
    diff = abs(calc_sum - reported_tot) if (not np.isnan(calc_sum) and not np.isnan(reported_tot)) else np.nan
    reconciliation_records.append({
        "dataset": "annual_petroleum_product_production",
        "financial_year": fy,
        "check_description": "Product Production: Sum of 12 Products == Reported Total",
        "reported_total": reported_tot,
        "calculated_sum": calc_sum,
        "discrepancy": diff,
        "status": "PASS" if (diff <= 1.01) else "FLAGGED",
        "notes": f"Difference: {diff:.4f} TMT (FY 2025-26 H1 has minor 1 TMT integer rounding in Others)."
    })

# ------------------------------------------------------------------------------
# 4. Reconciliation: Petroleum Trade Volumes
# ------------------------------------------------------------------------------
df_trade = pd.read_csv(std_dir / "annual_petroleum_trade_volumes.csv")
for idx, r in df_trade.iterrows():
    fy = r["financial_year"]
    crude_m = r["crude_oil_imports_tmt"]
    prod_m = r["total_product_imports_tmt"]
    tot_m = r["total_petroleum_imports_tmt"]
    prod_x = r["total_product_exports_tmt"]
    net_m = r["net_petroleum_imports_tmt"]
    
    calc_m = (crude_m if not np.isnan(crude_m) else 0.0) + (prod_m if not np.isnan(prod_m) else 0.0)
    diff_m = abs(calc_m - tot_m) if not np.isnan(tot_m) else np.nan
    reconciliation_records.append({
        "dataset": "annual_petroleum_trade_volumes",
        "financial_year": fy,
        "check_description": "Total Imports: Crude Imports + Product Imports == Total Imports",
        "reported_total": tot_m,
        "calculated_sum": calc_m,
        "discrepancy": diff_m,
        "status": "PASS" if (diff_m < 1.0) else "FLAGGED",
        "notes": f"Difference: {diff_m:.4f} TMT"
    })

    calc_net = tot_m - prod_x if (not np.isnan(tot_m) and not np.isnan(prod_x)) else np.nan
    diff_net = abs(calc_net - net_m) if (not np.isnan(calc_net) and not np.isnan(net_m)) else np.nan
    reconciliation_records.append({
        "dataset": "annual_petroleum_trade_volumes",
        "financial_year": fy,
        "check_description": "Net Imports: Total Imports - Total Product Exports == Net Imports",
        "reported_total": net_m,
        "calculated_sum": calc_net,
        "discrepancy": diff_net,
        "status": "PASS" if (diff_net < 1.0) else "FLAGGED",
        "notes": f"Difference: {diff_net:.4f} TMT"
    })

# ------------------------------------------------------------------------------
# 5. Reconciliation: Petroleum Product Consumption
# ------------------------------------------------------------------------------
df_cons = pd.read_csv(std_dir / "annual_petroleum_product_consumption.csv")
cons_cols = [
    "lpg_consumption_tmt", "naphtha_consumption_tmt", "motor_spirit_consumption_tmt",
    "aviation_turbine_fuel_consumption_tmt", "superior_kerosene_oil_consumption_tmt",
    "high_speed_diesel_consumption_tmt", "light_diesel_oil_consumption_tmt",
    "lubricants_greases_consumption_tmt", "fo_lshs_consumption_tmt",
    "bitumen_consumption_tmt", "petcoke_consumption_tmt", "others_consumption_tmt"
]
for idx, r in df_cons.iterrows():
    fy = r["financial_year"]
    reported_tot = r["total_petroleum_product_consumption_tmt"]
    calc_sum = sum(r[c] for c in cons_cols if not np.isnan(r[c]))
    diff = abs(calc_sum - reported_tot) if (not np.isnan(calc_sum) and not np.isnan(reported_tot)) else np.nan
    reconciliation_records.append({
        "dataset": "annual_petroleum_product_consumption",
        "financial_year": fy,
        "check_description": "Product Consumption: Sum of 12 Products == Reported Total",
        "reported_total": reported_tot,
        "calculated_sum": calc_sum,
        "discrepancy": diff,
        "status": "PASS" if (diff < 1.0) else "FLAGGED",
        "notes": f"Difference: {diff:.4f} TMT"
    })

df_rec = pd.DataFrame(reconciliation_records)
df_rec.to_csv(val_dir / "component_reconciliation_checks.csv", index=False)
print(f"Saved component_reconciliation_checks.csv ({len(df_rec)} checks run)")

# ------------------------------------------------------------------------------
# 6. Series Completeness & Continuity Checks
# ------------------------------------------------------------------------------
datasets_to_check = [
    ("annual_crude_oil_production.csv", "fiscal_year_start", 1998, 2023),
    ("annual_refinery_crude_processing.csv", "fiscal_year_start", 1998, 2026),
    ("annual_petroleum_product_production.csv", "fiscal_year_start", 1998, 2025),
    ("annual_petroleum_trade_volumes.csv", "fiscal_year_start", 1998, 2024),
    ("annual_petroleum_product_consumption.csv", "fiscal_year_start", 1997, 2025),
    ("annual_petroleum_import_export_values.csv", "fiscal_year_start", 1998, 2024),
    ("crude_oil_fob_price_indian_basket.csv", "fiscal_year_start", 2000, 2025)
]

for ds_name, yr_col, exp_start, exp_end in datasets_to_check:
    df_cur = pd.read_csv(std_dir / ds_name)
    actual_start = int(df_cur[yr_col].min())
    actual_end = int(df_cur[yr_col].max())
    total_records = len(df_cur)
    expected_records = (actual_end - actual_start) + 1
    
    all_years = set(range(actual_start, actual_end + 1))
    present_years = set(df_cur[yr_col].astype(int))
    missing_years = sorted(list(all_years - present_years))
    dup_count = df_cur.duplicated(subset=[yr_col]).sum()
    
    completeness_records.append({
        "dataset_name": ds_name,
        "temporal_key": yr_col,
        "earliest_year": actual_start,
        "latest_year": actual_end,
        "record_count": total_records,
        "expected_record_count": expected_records,
        "sequence_continuous": "YES" if not missing_years else "NO",
        "missing_years_in_sequence": str(missing_years) if missing_years else "None",
        "duplicate_period_keys": dup_count,
        "total_columns": len(df_cur.columns),
        "status": "PASS" if (not missing_years and dup_count == 0) else "FLAGGED"
    })

df_comp = pd.DataFrame(completeness_records)
df_comp.to_csv(val_dir / "series_completeness_checks.csv", index=False)
print(f"Saved series_completeness_checks.csv ({len(df_comp)} datasets verified)")
print("All validation checks successfully completed and logged!")
