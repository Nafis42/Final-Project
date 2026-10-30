import os
import re
import csv
import pandas as pd
import numpy as np
from pathlib import Path

base_dir = Path(".")
raw_dir = base_dir / "03_Processed_Data" / "raw_extractions"
std_dir = base_dir / "03_Processed_Data" / "standardized"
std_dir.mkdir(parents=True, exist_ok=True)

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

def clean_fy(fy_str):
    """Normalize FY string like '1998-99' or '1999-00' or '2022 - 23' or '2022-23 (P)'"""
    s = str(fy_str).strip()
    is_prov = "(P)" in s.upper() or "(PROV)" in s.upper()
    is_partial = "TILL" in s.upper() or "APR-SEP" in s.upper() or "H-1" in s.upper()
    # Handle whitespace around hyphen like '2022 - 23'
    m = re.search(r'(199[0-9]|20[0-2][0-9])\s*-\s*([0-9]{2})', s)
    if m:
        start_y = int(m.group(1))
        end_short = int(m.group(2))
        century = (start_y // 100) * 100
        end_y = century + end_short
        if end_y < start_y:
            end_y += 100
        standard_fy = f"FY {start_y}-{str(end_y)[2:]}"
        return standard_fy, start_y, end_y, is_prov, is_partial
    return s, np.nan, np.nan, is_prov, is_partial

print("Standardizing all datasets with robust FY parsing and footnote separation...")

# 1. Domestic Crude Production
df_raw_crude = pd.read_csv(raw_dir / "raw_crude_oil_production.csv")
obs_labels = {
    "ONGC": "crude_prod_ongc",
    "OIL": "crude_prod_oil",
    "PSU total": "crude_prod_psu_total",
    "JVC/ Private": "crude_prod_pvt_jvc",
    "Total crude oil": "crude_prod_total_crude",
    "Condensate*": "condensate_production",
    "Total\n( Crude oil + condensate)": "total_crude_and_condensate"
}
crude_rows = []
for yr in df_raw_crude["reporting_period"].unique():
    std_fy, start_y, end_y, is_prov, is_part = clean_fy(yr)
    if np.isnan(start_y):
        continue
    sub = df_raw_crude[df_raw_crude["reporting_period"] == yr]
    rec = {
        "financial_year": std_fy,
        "fiscal_year_start": start_y,
        "fiscal_year_end": end_y,
        "is_provisional": is_prov,
        "is_partial_period": is_part,
        "source_period_label": yr,
    }
    for orig_lbl, std_field in obs_labels.items():
        match_val = sub[sub["source_row_label"].str.strip() == orig_lbl.strip()]
        val_mmt = parse_num(match_val["source_raw_value"].values[0]) if len(match_val) > 0 else np.nan
        rec[f"{std_field}_mmt"] = val_mmt
        rec[f"{std_field}_tmt"] = val_mmt * 1000.0 if not np.isnan(val_mmt) else np.nan
    crude_rows.append(rec)
df_std_crude = pd.DataFrame(crude_rows).sort_values("fiscal_year_start").reset_index(drop=True)
df_std_crude.to_csv(std_dir / "annual_crude_oil_production.csv", index=False)
df_std_crude.to_parquet(std_dir / "annual_crude_oil_production.parquet", index=False)

# 2. Refinery Crude Processing
df_raw_proc = pd.read_csv(raw_dir / "raw_refinery_crude_processing_historical.csv")
proc_rows = []
for yr in df_raw_proc["reporting_period"].unique():
    std_fy, start_y, end_y, is_prov, is_part = clean_fy(yr)
    if np.isnan(start_y):
        continue
    sub = df_raw_proc[df_raw_proc["reporting_period"] == yr]
    def get_val(pattern):
        m = sub[sub["source_row_label"].str.contains(pattern, case=False, na=False, regex=True)]
        return parse_num(m["source_raw_value"].values[0]) if len(m) > 0 else np.nan
    rec = {
        "financial_year": std_fy,
        "fiscal_year_start": start_y,
        "fiscal_year_end": end_y,
        "is_provisional": is_prov,
        "is_partial_period": is_part,
        "source_period_label": yr,
        "iocl_throughput_tmt": get_val(r"^IOCL TOTAL"),
        "bpcl_throughput_tmt": get_val(r"^BPCL-TOTAL"),
        "hpcl_throughput_tmt": get_val(r"^HPCL-TOTAL"),
        "cpcl_throughput_tmt": get_val(r"^CPCL-TOTAL"),
        "mrpl_throughput_tmt": get_val(r"^MRPL"),
        "ongc_throughput_tmt": get_val(r"^ONGC TOTAL"),
        "nrl_throughput_tmt": get_val(r"^NRL"),
        "psu_subtotal_throughput_tmt": get_val(r"^TOTAL PUBLIC SECTOR"),
        "jv_subtotal_throughput_tmt": get_val(r"^TOTAL JV"),
        "ril_dta_throughput_tmt": get_val(r"^RIL \(DTA\)"),
        "ril_sez_throughput_tmt": get_val(r"^RIL \(SEZ\)"),
        "ril_total_throughput_tmt": get_val(r"^RIL TOTAL"),
        "nayara_eol_throughput_tmt": get_val(r"^EOL|NAYARA"),
        "private_subtotal_throughput_tmt": get_val(r"^TOTAL PRIVATE"),
        "grand_total_refinery_throughput_tmt": get_val(r"^GRAND TOTAL"),
    }
    rec["grand_total_refinery_throughput_mmt"] = rec["grand_total_refinery_throughput_tmt"] / 1000.0 if not np.isnan(rec["grand_total_refinery_throughput_tmt"]) else np.nan
    proc_rows.append(rec)
df_std_proc = pd.DataFrame(proc_rows).sort_values("fiscal_year_start").reset_index(drop=True)
df_std_proc.to_csv(std_dir / "annual_refinery_crude_processing.csv", index=False)
df_std_proc.to_parquet(std_dir / "annual_refinery_crude_processing.parquet", index=False)

# 3. Product Production
df_raw_pprod = pd.read_csv(raw_dir / "raw_petroleum_product_production_historical.csv")
pprod_rows = []
pprod_long = []
product_mapping = {
    "LPG": "lpg_production_tmt", "Naphtha": "naphtha_production_tmt", "MS": "motor_spirit_production_tmt",
    "ATF": "aviation_turbine_fuel_production_tmt", "SKO": "superior_kerosene_oil_production_tmt",
    "HSD": "high_speed_diesel_production_tmt", "LDO": "light_diesel_oil_production_tmt",
    "Lubes": "lubricants_production_tmt", "FO": "furnace_oil_production_tmt",
    "LSHS": "low_sulphur_heavy_stock_production_tmt", "Bitumen": "bitumen_production_tmt",
    "Others*": "others_production_tmt", "Total": "total_petroleum_product_production_tmt"
}
for yr in df_raw_pprod["reporting_period"].unique():
    std_fy, start_y, end_y, is_prov, is_part = clean_fy(yr)
    if np.isnan(start_y):
        continue
    sub = df_raw_pprod[df_raw_pprod["reporting_period"] == yr]
    rec = {
        "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
        "is_provisional": is_prov, "is_partial_period": is_part, "source_period_label": yr,
    }
    for orig_lbl, std_col in product_mapping.items():
        m = sub[sub["source_row_label"].str.strip() == orig_lbl.strip()]
        val = parse_num(m["source_raw_value"].values[0]) if len(m) > 0 else np.nan
        rec[std_col] = val
        if orig_lbl != "Total":
            pprod_long.append({
                "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
                "product_name": orig_lbl.replace("*", "").strip(), "production_tmt": val,
                "production_mmt": val / 1000.0 if not np.isnan(val) else np.nan,
                "is_provisional": is_prov, "is_partial_period": is_part
            })
    rec["total_petroleum_product_production_mmt"] = rec["total_petroleum_product_production_tmt"] / 1000.0 if not np.isnan(rec["total_petroleum_product_production_tmt"]) else np.nan
    pprod_rows.append(rec)
df_std_pprod = pd.DataFrame(pprod_rows).sort_values("fiscal_year_start").reset_index(drop=True)
df_std_pprod.to_csv(std_dir / "annual_petroleum_product_production.csv", index=False)
df_std_pprod.to_parquet(std_dir / "annual_petroleum_product_production.parquet", index=False)
df_pprod_long = pd.DataFrame(pprod_long).sort_values(["fiscal_year_start", "product_name"]).reset_index(drop=True)
df_pprod_long.to_csv(std_dir / "annual_petroleum_product_production_by_product.csv", index=False)
df_pprod_long.to_parquet(std_dir / "annual_petroleum_product_production_by_product.parquet", index=False)

# 4. Petroleum Trade Volumes
df_raw_trade = pd.read_csv(raw_dir / "raw_petroleum_trade_quantities_tmt.csv")
trade_wide = []
trade_long = []
for yr in df_raw_trade["reporting_period"].unique():
    std_fy, start_y, end_y, is_prov, is_part = clean_fy(yr)
    if np.isnan(start_y):
        continue
    sub = df_raw_trade[df_raw_trade["reporting_period"] == yr]
    def get_trade_val(row_min, row_max, lbl_pattern):
        m = sub[(sub["source_row_number"] >= row_min) & (sub["source_row_number"] <= row_max) & (sub["source_row_label"].str.contains(lbl_pattern, case=False, na=False, regex=True))]
        return parse_num(m["source_raw_value"].values[0]) if len(m) > 0 else np.nan

    crude_imports = get_trade_val(10, 10, r"CRUDE OIL")
    total_prod_imports = get_trade_val(22, 22, r"TOTAL PRODUCT IMPORT")
    total_imports = get_trade_val(24, 24, r"TOTAL IMPORT")
    total_prod_exports = get_trade_val(37, 37, r"TOTAL EXPORT")
    net_imports = get_trade_val(39, 39, r"NET IMPORT")
    net_prod_exports = get_trade_val(41, 41, r"Net Product Export")

    rec = {
        "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
        "crude_oil_imports_tmt": crude_imports,
        "crude_oil_imports_mmt": crude_imports / 1000.0 if not np.isnan(crude_imports) else np.nan,
        "crude_oil_exports_tmt": 0.0, "crude_oil_exports_mmt": 0.0,
        "net_crude_oil_imports_tmt": crude_imports,
        "net_crude_oil_imports_mmt": crude_imports / 1000.0 if not np.isnan(crude_imports) else np.nan,
        "total_product_imports_tmt": total_prod_imports,
        "total_product_imports_mmt": total_prod_imports / 1000.0 if not np.isnan(total_prod_imports) else np.nan,
        "total_petroleum_imports_tmt": total_imports,
        "total_petroleum_imports_mmt": total_imports / 1000.0 if not np.isnan(total_imports) else np.nan,
        "total_product_exports_tmt": total_prod_exports,
        "total_product_exports_mmt": total_prod_exports / 1000.0 if not np.isnan(total_prod_exports) else np.nan,
        "net_petroleum_imports_tmt": net_imports,
        "net_petroleum_imports_mmt": net_imports / 1000.0 if not np.isnan(net_imports) else np.nan,
        "net_product_exports_tmt": net_prod_exports,
        "net_product_exports_mmt": net_prod_exports / 1000.0 if not np.isnan(net_prod_exports) else np.nan,
        "is_provisional": is_prov, "source_period_label": yr
    }
    trade_wide.append(rec)
    for r_idx in range(12, 22):
        m_r = sub[sub["source_row_number"] == r_idx]
        if len(m_r) > 0:
            prod_name = re.sub(r'[\^$#@!%&]', '', str(m_r["source_row_label"].values[0])).strip()
            val = parse_num(m_r["source_raw_value"].values[0])
            trade_long.append({
                "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
                "trade_flow": "Import", "commodity_category": "Petroleum Product", "product_name": prod_name,
                "quantity_tmt": val, "quantity_mmt": val / 1000.0 if not np.isnan(val) else np.nan
            })
    for r_idx in range(26, 37):
        m_r = sub[sub["source_row_number"] == r_idx]
        if len(m_r) > 0:
            prod_name = re.sub(r'[\^$#@!%&]', '', str(m_r["source_row_label"].values[0])).strip()
            val = parse_num(m_r["source_raw_value"].values[0])
            trade_long.append({
                "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
                "trade_flow": "Export", "commodity_category": "Petroleum Product", "product_name": prod_name,
                "quantity_tmt": val, "quantity_mmt": val / 1000.0 if not np.isnan(val) else np.nan
            })
df_std_trade = pd.DataFrame(trade_wide).sort_values("fiscal_year_start").reset_index(drop=True)
df_std_trade.to_csv(std_dir / "annual_petroleum_trade_volumes.csv", index=False)
df_std_trade.to_parquet(std_dir / "annual_petroleum_trade_volumes.parquet", index=False)
df_trade_long = pd.DataFrame(trade_long).sort_values(["fiscal_year_start", "trade_flow", "product_name"]).reset_index(drop=True)
df_trade_long.to_csv(std_dir / "annual_petroleum_product_trade_by_product.csv", index=False)
df_trade_long.to_parquet(std_dir / "annual_petroleum_product_trade_by_product.parquet", index=False)

# 5. Petroleum Consumption
df_raw_cons = pd.read_csv(raw_dir / "raw_petroleum_product_consumption.csv")
cons_vol = df_raw_cons[df_raw_cons["metric_type"] == "Consumption Volume"]
cons_wide = []
cons_long = []
cons_products = {
    "LPG": "lpg_consumption_tmt", "Naphtha": "naphtha_consumption_tmt", "MS": "motor_spirit_consumption_tmt",
    "ATF": "aviation_turbine_fuel_consumption_tmt", "SKO": "superior_kerosene_oil_consumption_tmt",
    "HSD": "high_speed_diesel_consumption_tmt", "LDO": "light_diesel_oil_consumption_tmt",
    "Lubricants & Greases": "lubricants_greases_consumption_tmt", "FO & LSHS": "fo_lshs_consumption_tmt",
    "Bitumen": "bitumen_consumption_tmt", "Petroleum coke": "petcoke_consumption_tmt", "Others": "others_consumption_tmt",
    "TOTAL": "total_petroleum_product_consumption_tmt"
}
for yr in cons_vol["reporting_period"].unique():
    std_fy, start_y, end_y, is_prov, is_part = clean_fy(yr)
    if np.isnan(start_y):
        continue
    sub = cons_vol[cons_vol["reporting_period"] == yr]
    sez_dta_included = (start_y >= 2017)
    rec = {
        "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
        "is_provisional": is_prov, "is_partial_period": is_part,
        "sez_dta_sales_included": sez_dta_included, "source_period_label": yr,
    }
    for orig_lbl, std_col in cons_products.items():
        m = sub[sub["source_row_label"].str.strip() == orig_lbl.strip()]
        val = parse_num(m["source_raw_value"].values[0]) if len(m) > 0 else np.nan
        rec[std_col] = val
        if orig_lbl != "TOTAL":
            cons_long.append({
                "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
                "product_name": orig_lbl, "consumption_tmt": val,
                "consumption_mmt": val / 1000.0 if not np.isnan(val) else np.nan,
                "is_provisional": is_prov, "sez_dta_sales_included": sez_dta_included
            })
    rec["total_petroleum_product_consumption_mmt"] = rec["total_petroleum_product_consumption_tmt"] / 1000.0 if not np.isnan(rec["total_petroleum_product_consumption_tmt"]) else np.nan
    cons_wide.append(rec)
df_std_cons = pd.DataFrame(cons_wide).sort_values("fiscal_year_start").reset_index(drop=True)
df_std_cons.to_csv(std_dir / "annual_petroleum_product_consumption.csv", index=False)
df_std_cons.to_parquet(std_dir / "annual_petroleum_product_consumption.parquet", index=False)
df_cons_long = pd.DataFrame(cons_long).sort_values(["fiscal_year_start", "product_name"]).reset_index(drop=True)
df_cons_long.to_csv(std_dir / "annual_petroleum_product_consumption_by_product.csv", index=False)
df_cons_long.to_parquet(std_dir / "annual_petroleum_product_consumption_by_product.parquet", index=False)

# 6. Petroleum Trade Values (USD and INR)
df_raw_vusd = pd.read_csv(raw_dir / "raw_petroleum_trade_value_usd.csv")
df_raw_vinr = pd.read_csv(raw_dir / "raw_petroleum_trade_value_inr.csv")
val_rows = []
for yr in df_raw_vusd["reporting_period"].unique():
    std_fy, start_y, end_y, is_prov, is_part = clean_fy(yr)
    if np.isnan(start_y):
        continue
    sub_u = df_raw_vusd[df_raw_vusd["reporting_period"] == yr]
    sub_i = df_raw_vinr[df_raw_vinr["reporting_period"] == yr]
    def get_v(sub_df, row_min, row_max, lbl_pat):
        m = sub_df[(sub_df["source_row_number"] >= row_min) & (sub_df["source_row_number"] <= row_max) & (sub_df["source_row_label"].str.contains(lbl_pat, case=False, na=False, regex=True))]
        return parse_num(m["source_raw_value"].values[0]) if len(m) > 0 else np.nan

    crude_imp_usd = get_v(sub_u, 10, 10, r"CRUDE OIL")
    prod_imp_usd = get_v(sub_u, 22, 23, r"PRODUCT IMPORT")
    tot_imp_usd = get_v(sub_u, 24, 25, r"TOTAL IMPORT")
    prod_exp_usd = get_v(sub_u, 37, 39, r"TOTAL.*PRODUCT EXPORT|TOTAL EXPORT")
    net_imp_usd = get_v(sub_u, 39, 41, r"NET IMPORT")

    crude_imp_inr = get_v(sub_i, 10, 10, r"CRUDE OIL")
    prod_imp_inr = get_v(sub_i, 22, 23, r"PRODUCT IMPORT")
    tot_imp_inr = get_v(sub_i, 24, 25, r"TOTAL IMPORT")
    prod_exp_inr = get_v(sub_i, 37, 39, r"TOTAL.*EXPORT")
    net_imp_inr = get_v(sub_i, 39, 41, r"NET IMPORT")
    implied_fx = (tot_imp_inr * 10.0) / tot_imp_usd if (not np.isnan(tot_imp_inr) and not np.isnan(tot_imp_usd) and tot_imp_usd > 0) else np.nan

    val_rows.append({
        "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
        "crude_oil_import_value_million_usd": crude_imp_usd, "product_import_value_million_usd": prod_imp_usd,
        "total_petroleum_import_value_million_usd": tot_imp_usd, "product_export_value_million_usd": prod_exp_usd,
        "net_petroleum_import_value_million_usd": net_imp_usd,
        "crude_oil_import_value_rs_crore": crude_imp_inr, "product_import_value_rs_crore": prod_imp_inr,
        "total_petroleum_import_value_rs_crore": tot_imp_inr, "product_export_value_rs_crore": prod_exp_inr,
        "net_petroleum_import_value_rs_crore": net_imp_inr,
        "implied_exchange_rate_inr_per_usd": implied_fx, "is_provisional": is_prov,
        "source_period_label": yr, "spr_mangalore_excluded_flag": (start_y == 2018)
    })
df_std_val = pd.DataFrame(val_rows).sort_values("fiscal_year_start").reset_index(drop=True)
df_std_val.to_csv(std_dir / "annual_petroleum_import_export_values.csv", index=False)
df_std_val.to_parquet(std_dir / "annual_petroleum_import_export_values.parquet", index=False)

# 7. Indian Crude Basket Price (Filtering out footer rows)
df_raw_price = pd.read_csv(raw_dir / "raw_crude_oil_indian_basket_price.csv")
price_rows = []
for fy in df_raw_price["source_financial_year"].unique():
    std_fy, start_y, end_y, is_prov, is_part = clean_fy(fy)
    if np.isnan(start_y):
        continue # filters out "Notes:", "* The composition...", "- Crude oil prices..."
    sub = df_raw_price[df_raw_price["source_financial_year"] == fy]
    avg_row = sub[sub["source_column_name"] == "Average"]
    ratio_row = sub[sub["source_column_name"] == "Ratio"]
    annual_avg = parse_num(avg_row["source_raw_value"].values[0]) if len(avg_row) > 0 else np.nan
    ratio_str = str(ratio_row["source_raw_value"].values[0]).strip() if len(ratio_row) > 0 else ""
    m_ratio = re.search(r'([0-9\.]+)\s*:\s*([0-9\.]+)', ratio_str)
    sour_wt = float(m_ratio.group(1)) if m_ratio else np.nan
    sweet_wt = float(m_ratio.group(2)) if m_ratio else np.nan

    rec = {
        "financial_year": std_fy, "fiscal_year_start": start_y, "fiscal_year_end": end_y,
        "annual_average_price_usd_per_bbl": annual_avg,
        "basket_composition_ratio_sour_to_sweet": ratio_str,
        "sour_crude_weight_pct": sour_wt, "sweet_crude_weight_pct": sweet_wt,
        "is_provisional": is_prov, "source_period_label": fy
    }
    months_list = ["April", "May", "June", "July", "August", "September", "October", "November", "December", "January", "February", "March"]
    for m in months_list:
        m_match = sub[sub["source_column_name"] == m]
        rec[f"price_{m.lower()}_usd_per_bbl"] = parse_num(m_match["source_raw_value"].values[0]) if len(m_match) > 0 else np.nan
    price_rows.append(rec)
df_std_price = pd.DataFrame(price_rows).sort_values("fiscal_year_start").reset_index(drop=True)
df_std_price.to_csv(std_dir / "crude_oil_fob_price_indian_basket.csv", index=False)
df_std_price.to_parquet(std_dir / "crude_oil_fob_price_indian_basket.parquet", index=False)

print("Standardized datasets successfully updated and cleaned!")
