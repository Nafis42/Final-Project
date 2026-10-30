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

df_raw_proc = pd.read_csv(raw_dir / "raw_refinery_crude_processing_historical.csv")

# Identify row labels that represent primary entities (refineries or company totals)
# To avoid double counting, if an entity has a TOTAL row (IOCL TOTAL, HPCL-TOTAL, BPCL-TOTAL, CPCL-TOTAL, ONGC TOTAL, RIL TOTAL), we use the TOTAL row.
# Otherwise, we use the standalone entity row (NRL, Kochi, BORL, BRPL, HMEL, HRRL, Nayara).
def get_refinery_components(sub_df):
    labels = sub_df['source_row_label'].unique()
    company_totals = ['IOCL TOTAL', 'HPCL-TOTAL', 'BPCL-TOTAL', 'CPCL-TOTAL', 'ONGC TOTAL', 'RIL TOTAL']
    standalone = [
        'Numaligarh Refinery Ltd.(NRL)\nNumaligarh, Assam',
        'Kochi Refinery Ltd.-KOCHI, KERALA',
        'Bharat Oman Refineries Ltd.-Bina, Sagar M.P.',
        'Bongaigaon Refinery & Petrochemicals Ltd.\n(BRPL)-Bongaigaon, Assam',
        'HMEL-GGSR, BATHINDA, PUNJAB',
        'HRRL Pachpadra,Rajasthan',
        'NAYARA ENERGY LTD.\nVADINAR, GUJARAT,(Formerly ESSAR OIL LTD.)'
    ]
    
    total_sum = 0.0
    for lbl in company_totals:
        m = sub_df[sub_df['source_row_label'].str.strip() == lbl.strip()]
        if len(m) > 0:
            val = float(m['source_raw_value'].values[0]) if m['source_raw_value'].values[0] else 0.0
            total_sum += val
            
    for lbl in standalone:
        m = sub_df[sub_df['source_row_label'].str.strip() == lbl.strip()]
        if len(m) > 0:
            val = float(m['source_raw_value'].values[0]) if m['source_raw_value'].values[0] else 0.0
            total_sum += val
            
    return total_sum

print("Testing refinery component sum across all years:")
for yr in df_raw_proc['reporting_period'].unique():
    sub = df_raw_proc[df_raw_proc['reporting_period'] == yr]
    gt_match = sub[sub['source_row_label'] == 'GRAND TOTAL']
    if len(gt_match) > 0 and gt_match['source_raw_value'].values[0]:
        gt = float(gt_match['source_raw_value'].values[0])
        calc_s = get_refinery_components(sub)
        diff = abs(gt - calc_s)
        status = "PASS" if diff < 1.0 else "FAIL"
        print(f"  {yr:<15}: GT={gt:>12.2f} | Calc={calc_s:>12.2f} | Diff={diff:>8.4f} | {status}")
