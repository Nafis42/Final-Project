import os
import re
import pandas as pd
import numpy as np
from pathlib import Path

base_dir = Path(".")
raw_dir = base_dir / "03_Processed_Data" / "raw_extractions"
std_dir = base_dir / "03_Processed_Data" / "standardized"

def parse_num(val):
    if val is None or val == "" or str(val).strip() == "" or str(val).strip().lower() in ["none", "nan", "-", "null"]:
        return np.nan
    s = str(val).strip().replace(",", "")
    if s.startswith("(") and s.endswith(")"):
        s = "-" + s[1:-1].strip()
    try:
        return float(s)
    except ValueError:
        return np.nan

# 1. Statewise Sales
df_state = pd.read_csv(raw_dir / "raw_statewise_sales_pol_consumption.csv")
df_state_obs = df_state[df_state["is_metadata_or_footnote"] == "No"].copy()
df_state_obs["sales_tmt"] = df_state_obs["source_raw_value"].apply(parse_num)
df_state_obs["sales_mmt"] = df_state_obs["sales_tmt"] / 1000.0
df_state_std = df_state_obs[["financial_year", "product_category", "region", "state_or_total_label", "sales_tmt", "sales_mmt"]].copy()
df_state_std.columns = ["financial_year", "product_category", "geographic_region", "state_or_territory", "sales_quantity_tmt", "sales_quantity_mmt"]
df_state_std = df_state_std.dropna(subset=["sales_quantity_tmt"])
df_state_std.to_csv(std_dir / "statewise_sales_pol_consumption.csv", index=False)
df_state_std.to_parquet(std_dir / "statewise_sales_pol_consumption.parquet", index=False)
print(f"Saved statewise_sales_pol_consumption: {len(df_state_std)} records")

# 2. Monthly Trade Volumes
df_m_trade = pd.read_csv(raw_dir / "raw_monthly_trade_volumes.csv")
df_m_trade["quantity_tmt"] = df_m_trade["source_raw_value"].apply(parse_num)
df_m_trade["quantity_mmt"] = df_m_trade["quantity_tmt"] / 1000.0
# filter valid months (not TOTAL)
df_m_valid = df_m_trade[~df_m_trade["month_name"].str.contains("TOTAL|COL_", case=False, na=False)].copy()
df_m_valid = df_m_valid.dropna(subset=["quantity_tmt"])
df_m_valid_std = df_m_valid[["financial_year", "row_label", "month_name", "quantity_tmt", "quantity_mmt", "source_file", "source_sheet"]].copy()
df_m_valid_std.columns = ["financial_year", "commodity_name", "month_name", "quantity_tmt", "quantity_mmt", "source_file", "source_sheet"]
df_m_valid_std.to_csv(std_dir / "monthly_petroleum_trade_volumes.csv", index=False)
df_m_valid_std.to_parquet(std_dir / "monthly_petroleum_trade_volumes.parquet", index=False)
print(f"Saved monthly_petroleum_trade_volumes: {len(df_m_valid_std)} records")

# 3. Monthly Refinery Processing
df_m_proc = pd.read_csv(raw_dir / "raw_monthly_refinery_crude_processing.csv")
df_m_proc["throughput_tmt"] = df_m_proc["source_raw_value"].apply(parse_num)
df_m_proc["throughput_mmt"] = df_m_proc["throughput_tmt"] / 1000.0
df_m_proc_valid = df_m_proc[~df_m_proc["month_name"].str.contains("TOTAL|COL_", case=False, na=False)].copy()
df_m_proc_valid = df_m_proc_valid.dropna(subset=["throughput_tmt"])
df_m_proc_std = df_m_proc_valid[["financial_year", "refinery_or_company", "month_name", "throughput_tmt", "throughput_mmt", "source_file", "source_sheet"]].copy()
df_m_proc_std.columns = ["financial_year", "refinery_or_company_name", "month_name", "throughput_tmt", "throughput_mmt", "source_file", "source_sheet"]
df_m_proc_std.to_csv(std_dir / "monthly_refinery_crude_processing.csv", index=False)
df_m_proc_std.to_parquet(std_dir / "monthly_refinery_crude_processing.parquet", index=False)
print(f"Saved monthly_refinery_crude_processing: {len(df_m_proc_std)} records")
