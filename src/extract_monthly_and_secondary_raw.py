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

print("Extracting monthly, regional, and secondary tables...")

# ------------------------------------------------------------------------------
# 1. Statewise Sales POL Consumption
# ------------------------------------------------------------------------------
src_file = "1787137273_Statewise_Sales-POL_Consumption_Final.xlsx"
wb = openpyxl.load_workbook(data_dir / src_file, data_only=True)
raw_statewise = []

for sname in ["PT_Cons_Statewise", "PT_Cons_Statewise MS", "PT_Cons_Statewise HSD"]:
    ws = wb[sname]
    product_cat = "All Products" if sname == "PT_Cons_Statewise" else ("MS / Petrol" if "MS" in sname else "HSD / Diesel")
    # Row 8 (1-indexed) contains year headers
    years = [str(ws.cell(8, c).value).strip() for c in range(2, ws.max_column + 1) if ws.cell(8, c).value is not None]
    
    current_region = "National"
    for r_idx in range(9, ws.max_row + 1):
        lbl = ws.cell(r_idx, 1).value
        if not lbl:
            continue
        lbl_str = str(lbl).strip()
        if "REGION -" in lbl_str:
            current_region = lbl_str
            continue
        is_note = "source" in lbl_str.lower() or "*" in lbl_str
        for c_idx, yr in enumerate(years, 2):
            val = ws.cell(r_idx, c_idx).value
            raw_statewise.append({
                "source_file": src_file,
                "source_sheet": sname,
                "source_row_number": r_idx,
                "product_category": product_cat,
                "region": current_region,
                "state_or_total_label": lbl_str,
                "financial_year": yr,
                "source_raw_value": clean_val(val),
                "source_unit": "'000 Metric Tonnes (TMT)",
                "is_metadata_or_footnote": "Yes" if is_note else "No",
                "extraction_timestamp": timestamp,
                "notes": "Statewise POL industry sales."
            })
wb.close()
save_raw_table(
    "raw_statewise_sales_pol_consumption.csv",
    raw_statewise,
    ["source_file", "source_sheet", "source_row_number", "product_category", "region", "state_or_total_label", "financial_year", "source_raw_value", "source_unit", "is_metadata_or_footnote", "extraction_timestamp", "notes"]
)

# ------------------------------------------------------------------------------
# 2. Monthly Trade Volumes across Fiscal Year Sheets
# ------------------------------------------------------------------------------
src_file = "1751964547_PT_IMPORT_TMT_H.xlsx"
wb = openpyxl.load_workbook(data_dir / src_file, data_only=True)
raw_monthly_trade = []
months = ['APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER', 'JANUARY', 'FEBRUARY', 'MARCH', 'TOTAL']

for sname in wb.sheetnames:
    if sname == "PT_IMPORT_H":
        continue # historical handled
    ws = wb[sname]
    # Check if FY sheet
    m_fy = re.search(r'(20[0-2][0-9]-[0-2][0-9])', sname)
    fy = m_fy.group(1) if m_fy else sname
    
    # Locate header row with months
    header_r = -1
    for r in range(1, min(15, ws.max_row + 1)):
        row_vals = [str(ws.cell(r, c).value).strip().upper() for c in range(1, min(15, ws.max_column + 1))]
        if "APRIL" in row_vals or "APR" in row_vals:
            header_r = r
            break
            
    if header_r != -1:
        for r_idx in range(header_r + 1, ws.max_row + 1):
            lbl = ws.cell(r_idx, 1).value
            if not lbl:
                continue
            lbl_str = str(lbl).strip()
            for c_idx in range(2, min(15, ws.max_column + 1)):
                m_name = str(ws.cell(header_r, c_idx).value or f"Col_{c_idx}").strip().upper()
                val = ws.cell(r_idx, c_idx).value
                raw_monthly_trade.append({
                    "source_file": src_file,
                    "source_sheet": sname,
                    "source_row_number": r_idx,
                    "financial_year": fy,
                    "row_label": lbl_str,
                    "month_name": m_name,
                    "source_raw_value": clean_val(val),
                    "source_unit": "'000 Metric Tonnes (TMT)",
                    "extraction_timestamp": timestamp
                })
wb.close()
save_raw_table(
    "raw_monthly_trade_volumes.csv",
    raw_monthly_trade,
    ["source_file", "source_sheet", "source_row_number", "financial_year", "row_label", "month_name", "source_raw_value", "source_unit", "extraction_timestamp"]
)

# ------------------------------------------------------------------------------
# 3. Monthly Refinery Crude Processing across FY Sheets
# ------------------------------------------------------------------------------
src_file = "1788266304_PT_crude_processing_H.xls"
wb = xlrd.open_workbook(data_dir / src_file)
raw_monthly_proc = []

for sname in wb.sheet_names():
    if sname == "PT_CRUDE_H":
        continue
    ws = wb.sheet_by_name(sname)
    m_fy = re.search(r'(20[0-2][0-9]-[0-2][0-9])', sname)
    fy = m_fy.group(1) if m_fy else sname
    
    header_r = -1
    for r in range(min(15, ws.nrows)):
        row_vals = [str(ws.cell_value(r, c)).strip().upper() for c in range(min(15, ws.ncols))]
        if any(m in row_vals for m in ["APRIL", "APR"]):
            header_r = r
            break
            
    if header_r != -1:
        for r_idx in range(header_r + 1, ws.nrows):
            lbl = ws.cell_value(r_idx, 0)
            if not lbl:
                continue
            lbl_str = str(lbl).strip()
            for c_idx in range(1, min(14, ws.ncols)):
                m_name = str(ws.cell_value(header_r, c_idx)).strip().upper()
                val = ws.cell_value(r_idx, c_idx)
                raw_monthly_proc.append({
                    "source_file": src_file,
                    "source_sheet": sname,
                    "source_row_number": r_idx + 1,
                    "financial_year": fy,
                    "refinery_or_company": lbl_str,
                    "month_name": m_name,
                    "source_raw_value": clean_val(val),
                    "source_unit": "'000 Metric Tonnes (TMT)",
                    "extraction_timestamp": timestamp
                })
save_raw_table(
    "raw_monthly_refinery_crude_processing.csv",
    raw_monthly_proc,
    ["source_file", "source_sheet", "source_row_number", "financial_year", "refinery_or_company", "month_name", "source_raw_value", "source_unit", "extraction_timestamp"]
)

# ------------------------------------------------------------------------------
# 4. Secondary Fiscal: Contribution to Exchequer
# ------------------------------------------------------------------------------
src_file = "1784281292_PP_4_ContributionToExchequer.xls"
wb = xlrd.open_workbook(data_dir / src_file)
ws = wb.sheet_by_index(0)
raw_exchequer = []
# Row 9 (0-indexed) has years
ex_years = [clean_val(ws.cell_value(9, c)) for c in range(2, ws.ncols) if clean_val(ws.cell_value(9, c))]

for r_idx in range(10, ws.nrows):
    lbl = clean_val(ws.cell_value(r_idx, 0))
    if not lbl:
        continue
    for c_idx, yr in enumerate(ex_years, 2):
        val = ws.cell_value(r_idx, c_idx)
        raw_exchequer.append({
            "source_file": src_file,
            "source_sheet": ws.name,
            "source_row_number": r_idx + 1,
            "particulars": lbl,
            "financial_year": yr,
            "source_raw_value": clean_val(val),
            "source_unit": "Rs. Crore",
            "extraction_timestamp": timestamp
        })
save_raw_table(
    "raw_contribution_to_exchequer.csv",
    raw_exchequer,
    ["source_file", "source_sheet", "source_row_number", "particulars", "financial_year", "source_raw_value", "source_unit", "extraction_timestamp"]
)

# ------------------------------------------------------------------------------
# 5. Secondary Fiscal: OMC Under-recoveries (BytesIO handled)
# ------------------------------------------------------------------------------
src_file = "1785841030_Under_Recoveries_to_Oil_Marketing_Companies_(OMCs)_on_Sale_of_Sensitive_Petroleum_Products_Rs_Crore.xls"
with open(data_dir / src_file, "rb") as fp:
    bio = io.BytesIO(fp.read())
wb = openpyxl.load_workbook(bio, data_only=True)
ws = wb.active
raw_under_rec = []
ur_years = [clean_val(ws.cell(6, c).value) for c in range(2, ws.max_column + 1) if ws.cell(6, c).value is not None]

for r_idx in range(7, ws.max_row + 1):
    lbl = clean_val(ws.cell(r_idx, 1).value)
    if not lbl:
        continue
    for c_idx, yr in enumerate(ur_years, 2):
        val = ws.cell(r_idx, c_idx).value
        raw_under_rec.append({
            "source_file": src_file,
            "source_sheet": ws.title,
            "source_row_number": r_idx,
            "particulars": lbl,
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

print("Monthly and secondary raw tables successfully extracted!")
