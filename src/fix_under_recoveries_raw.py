import os
import io
import csv
import json
import re
import datetime
from pathlib import Path
import openpyxl
import xlrd

base_dir = Path(".")
data_dir = base_dir / "01_Original_Data"
raw_out_dir = base_dir / "03_Processed_Data" / "raw_extractions"
raw_out_dir.mkdir(parents=True, exist_ok=True)

timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

def clean_val(v):
    if v is None:
        return ""
    if isinstance(v, float):
        if v.is_integer():
            return str(int(v))
        return f"{v:.4f}".rstrip('0').rstrip('.')
    return str(val).strip() if (val := str(v)) else ""

def save_raw_table(output_filename, records, fieldnames):
    out_path = raw_out_dir / output_filename
    with open(out_path, "w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"Extracted {len(records)} raw records to {output_filename}")

# Fix OMC Under-recoveries extraction
src_file = "1785841030_Under_Recoveries_to_Oil_Marketing_Companies_(OMCs)_on_Sale_of_Sensitive_Petroleum_Products_Rs_Crore.xls"
with open(data_dir / src_file, "rb") as fp:
    bio = io.BytesIO(fp.read())
wb = openpyxl.load_workbook(bio, data_only=True)
ws = wb.active
raw_under_rec = []

# Header row is R6: Particulars is col 2, years start at col 5
years_dict = {}
for c in range(5, ws.max_column + 1):
    val = ws.cell(6, c).value
    if val:
        years_dict[c] = clean_val(val)

for r_idx in range(7, ws.max_row + 1):
    lbl = ws.cell(r_idx, 2).value
    if not lbl:
        continue
    lbl_str = clean_val(lbl)
    for c_idx, yr in years_dict.items():
        val = ws.cell(r_idx, c_idx).value
        raw_under_rec.append({
            "source_file": src_file,
            "source_sheet": ws.title,
            "source_row_number": r_idx,
            "particulars": lbl_str,
            "financial_year": yr,
            "source_raw_value": clean_val(val),
            "source_unit": "Rs. Crore",
            "extraction_timestamp": timestamp
        })
wb.close()
save_raw_table(
    "raw_omc_under_recoveries_sensitive_products.csv",
    raw_under_rec,
    ["source_file", "source_sheet", "source_row_number", "particulars", "financial_year", "source_raw_value", "source_unit", "extraction_timestamp"]
)

# Extract Fiscal Subsidies 1679651218_163fd52aba7df0b51c90.xls as well
src_file = "1679651218_163fd52aba7df0b51c90.xls"
wb = xlrd.open_workbook(data_dir / src_file)
ws = wb.sheet_by_index(0)
raw_fiscal = []
# Row 13 (0-indexed) has Year, PDS Kerosene, Domestic LPG, Total
for r in range(14, ws.nrows):
    yr = clean_val(ws.cell_value(r, 1))
    if not yr:
        continue
    raw_fiscal.append({
        "source_file": src_file,
        "source_sheet": ws.name,
        "source_row_number": r + 1,
        "financial_year": yr,
        "pds_kerosene_subsidy_rs_crore": clean_val(ws.cell_value(r, 2)),
        "domestic_lpg_subsidy_rs_crore": clean_val(ws.cell_value(r, 3)),
        "total_fiscal_subsidy_rs_crore": clean_val(ws.cell_value(r, 4)),
        "source_unit": "Rs. Crore",
        "extraction_timestamp": timestamp
    })
save_raw_table(
    "raw_fiscal_subsidy_scheme_2002.csv",
    raw_fiscal,
    ["source_file", "source_sheet", "source_row_number", "financial_year", "pds_kerosene_subsidy_rs_crore", "domestic_lpg_subsidy_rs_crore", "total_fiscal_subsidy_rs_crore", "source_unit", "extraction_timestamp"]
)
