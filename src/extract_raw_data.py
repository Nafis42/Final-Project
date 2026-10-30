import os
import io
import csv
import json
import datetime
from pathlib import Path
import openpyxl
import xlrd
import pypdf

base_dir = Path(".")
data_dir = base_dir / "01_Original_Data"
raw_out_dir = base_dir / "03_Processed_Data" / "raw_extractions"
raw_out_dir.mkdir(parents=True, exist_ok=True)

timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
extraction_records = []

def clean_val(v):
    if v is None:
        return ""
    if isinstance(v, float):
        if v.is_integer():
            return str(int(v))
        return f"{v:.4f}".rstrip('0').rstrip('.')
    return str(v).strip()

def save_raw_table(output_filename, records, fieldnames):
    out_path = raw_out_dir / output_filename
    with open(out_path, "w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"Extracted {len(records)} raw records to {output_filename}")
    return len(records)

print("Starting Source-Preserving Raw Extractions...")

# ------------------------------------------------------------------------------
# 1. RAW: Domestic Crude Oil Production
# ------------------------------------------------------------------------------
src_file = "1717395338_PT_Crude_oil_production_H.xls"
wb = xlrd.open_workbook(data_dir / src_file)
sheet_name = "PT_PRODUCTION_H"
ws = wb.sheet_by_name(sheet_name)

raw_crude_prod = []
# Header is in row 8 (0-indexed)
years = [clean_val(ws.cell_value(8, c)) for c in range(1, ws.ncols)]

for r_idx in range(9, ws.nrows):
    row_label = clean_val(ws.cell_value(r_idx, 0))
    if not row_label and not any(ws.cell_value(r_idx, c) for c in range(1, ws.ncols)):
        continue
    # Determine if footnote row
    is_note = "note" in row_label.lower() or "source" in row_label.lower() or "*" in row_label
    for c_idx, yr in enumerate(years, 1):
        val = clean_val(ws.cell_value(r_idx, c_idx))
        raw_crude_prod.append({
            "source_file": src_file,
            "source_sheet": sheet_name,
            "source_row_number": r_idx + 1,
            "source_table_title": "Indigenous crude oil production",
            "source_row_label": row_label,
            "source_column_name": yr,
            "source_raw_value": val,
            "source_unit": "Million Metric Tonnes (MMT)",
            "reporting_period": yr,
            "is_metadata_or_footnote": "Yes" if is_note else "No",
            "extraction_timestamp": timestamp,
            "extraction_status": "Success",
            "notes": "Condensate broken out from 2006-07 onwards; 2022-23 and 2023-24 are provisional."
        })

save_raw_table(
    "raw_crude_oil_production.csv",
    raw_crude_prod,
    ["source_file", "source_sheet", "source_row_number", "source_table_title", "source_row_label", "source_column_name", "source_raw_value", "source_unit", "reporting_period", "is_metadata_or_footnote", "extraction_timestamp", "extraction_status", "notes"]
)

# ------------------------------------------------------------------------------
# 2. RAW: Refinery Crude Processing (Historical Sheet)
# ------------------------------------------------------------------------------
src_file = "1788266304_PT_crude_processing_H.xls"
wb = xlrd.open_workbook(data_dir / src_file)
sheet_name = "PT_CRUDE_H"
ws = wb.sheet_by_name(sheet_name)

raw_crude_proc = []
# Header is in row 9 (0-indexed)
proc_years = [clean_val(ws.cell_value(9, c)) for c in range(1, ws.ncols)]

for r_idx in range(10, ws.nrows):
    row_label = clean_val(ws.cell_value(r_idx, 0))
    if not row_label and not any(ws.cell_value(r_idx, c) for c in range(1, ws.ncols)):
        continue
    is_note = "source" in row_label.lower() or "(p)" in row_label.lower() or "note" in row_label.lower()
    for c_idx, yr in enumerate(proc_years, 1):
        val = clean_val(ws.cell_value(r_idx, c_idx))
        raw_crude_proc.append({
            "source_file": src_file,
            "source_sheet": sheet_name,
            "source_row_number": r_idx + 1,
            "source_table_title": "Crude Oil Processed by Refineries",
            "source_row_label": row_label,
            "source_column_name": yr,
            "source_raw_value": val,
            "source_unit": "'000 Metric Tonnes (TMT)",
            "reporting_period": yr,
            "is_metadata_or_footnote": "Yes" if is_note else "No",
            "extraction_timestamp": timestamp,
            "extraction_status": "Success",
            "notes": "Includes PSU, Joint Venture, and Private refineries."
        })

save_raw_table(
    "raw_refinery_crude_processing_historical.csv",
    raw_crude_proc,
    ["source_file", "source_sheet", "source_row_number", "source_table_title", "source_row_label", "source_column_name", "source_raw_value", "source_unit", "reporting_period", "is_metadata_or_footnote", "extraction_timestamp", "extraction_status", "notes"]
)

# ------------------------------------------------------------------------------
# 3. RAW: Petroleum Product Production (Historical Sheet)
# ------------------------------------------------------------------------------
src_file = "1761642701_PT_production_product_H.xls"
wb = xlrd.open_workbook(data_dir / src_file)
sheet_name = "PT_PRODUCTION_H"
ws = wb.sheet_by_name(sheet_name)

raw_prod_prod = []
# Header is in row 9 (0-indexed)
prod_years = [clean_val(ws.cell_value(9, c)) for c in range(1, ws.ncols)]

for r_idx in range(10, ws.nrows):
    row_label = clean_val(ws.cell_value(r_idx, 0))
    if not row_label and not any(ws.cell_value(r_idx, c) for c in range(1, ws.ncols)):
        continue
    is_note = "source" in row_label.lower() or "note" in row_label.lower() or "*" in row_label
    for c_idx, yr in enumerate(prod_years, 1):
        val = clean_val(ws.cell_value(r_idx, c_idx))
        raw_prod_prod.append({
            "source_file": src_file,
            "source_sheet": sheet_name,
            "source_row_number": r_idx + 1,
            "source_table_title": "Production of Petroleum Products by Refineries & Fractionators",
            "source_row_label": row_label,
            "source_column_name": yr,
            "source_raw_value": val,
            "source_unit": "'000 Metric Tonnes (TMT)",
            "reporting_period": yr,
            "is_metadata_or_footnote": "Yes" if is_note else "No",
            "extraction_timestamp": timestamp,
            "extraction_status": "Success",
            "notes": "Covers major products and Others."
        })

save_raw_table(
    "raw_petroleum_product_production_historical.csv",
    raw_prod_prod,
    ["source_file", "source_sheet", "source_row_number", "source_table_title", "source_row_label", "source_column_name", "source_raw_value", "source_unit", "reporting_period", "is_metadata_or_footnote", "extraction_timestamp", "extraction_status", "notes"]
)

# ------------------------------------------------------------------------------
# 4. RAW: Petroleum Trade Quantities (TMT)
# ------------------------------------------------------------------------------
src_file = "1751964547_PT_IMPORT_TMT_H.xlsx"
wb = openpyxl.load_workbook(data_dir / src_file, data_only=True)
sheet_name = "PT_IMPORT_H"
ws = wb[sheet_name]

raw_trade_tmt = []
# Header is row 8 (1-indexed)
trade_years = [clean_val(ws.cell(8, c).value) for c in range(2, ws.max_column + 1) if ws.cell(8, c).value is not None]

for r_idx in range(9, ws.max_row + 1):
    row_label = clean_val(ws.cell(r_idx, 1).value)
    if not row_label and not any(ws.cell(r_idx, c).value for c in range(2, len(trade_years) + 2)):
        continue
    is_note = r_idx >= 42 or "source" in row_label.lower() or "note" in row_label.lower()
    for c_idx, yr in enumerate(trade_years, 2):
        val = clean_val(ws.cell(r_idx, c_idx).value)
        raw_trade_tmt.append({
            "source_file": src_file,
            "source_sheet": sheet_name,
            "source_row_number": r_idx,
            "source_table_title": "Import/Export of Crude oil and Petroleum Products",
            "source_row_label": row_label,
            "source_column_name": yr,
            "source_raw_value": val,
            "source_unit": "'000 Metric Tonnes (TMT)",
            "reporting_period": yr,
            "is_metadata_or_footnote": "Yes" if is_note else "No",
            "extraction_timestamp": timestamp,
            "extraction_status": "Success",
            "notes": "Covers Crude Imports, Product Imports, and Product Exports."
        })
wb.close()

save_raw_table(
    "raw_petroleum_trade_quantities_tmt.csv",
    raw_trade_tmt,
    ["source_file", "source_sheet", "source_row_number", "source_table_title", "source_row_label", "source_column_name", "source_raw_value", "source_unit", "reporting_period", "is_metadata_or_footnote", "extraction_timestamp", "extraction_status", "notes"]
)

# ------------------------------------------------------------------------------
# 5. RAW: Petroleum Product Consumption
# ------------------------------------------------------------------------------
src_file = "1788343376_PT_Consumption_English.xls"
wb = xlrd.open_workbook(data_dir / src_file)
sheet_name = "Historical (year-wise)"
ws = wb.sheet_by_name(sheet_name)

raw_consumption = []
# Row 7 (0-indexed) has years and Growth %
cols = [clean_val(ws.cell_value(7, c)) for c in range(1, ws.ncols)]

for r_idx in range(8, ws.nrows):
    row_label = clean_val(ws.cell_value(r_idx, 0))
    if not row_label and not any(ws.cell_value(r_idx, c) for c in range(1, ws.ncols)):
        continue
    is_note = "note" in row_label.lower() or "source" in row_label.lower() or "(p)" in row_label.lower() or "demand" in row_label.lower() or "sez" in row_label.lower()
    for c_idx, col_name in enumerate(cols, 1):
        val = clean_val(ws.cell_value(r_idx, c_idx))
        is_growth = "growth" in col_name.lower()
        raw_consumption.append({
            "source_file": src_file,
            "source_sheet": sheet_name,
            "source_row_number": r_idx + 1,
            "source_table_title": "CONSUMPTION OF PETROLEUM PRODUCTS",
            "source_row_label": row_label,
            "source_column_name": col_name,
            "source_raw_value": val,
            "source_unit": "% Growth" if is_growth else "'000 Metric Tonne (TMT)",
            "reporting_period": col_name if not is_growth else cols[c_idx-2],
            "metric_type": "YoY Percentage Growth" if is_growth else "Consumption Volume",
            "is_metadata_or_footnote": "Yes" if is_note else "No",
            "extraction_timestamp": timestamp,
            "extraction_status": "Success",
            "notes": "Market demand definition includes SEZ sales to DTA from 2017-18 onwards."
        })

save_raw_table(
    "raw_petroleum_product_consumption.csv",
    raw_consumption,
    ["source_file", "source_sheet", "source_row_number", "source_table_title", "source_row_label", "source_column_name", "source_raw_value", "source_unit", "reporting_period", "metric_type", "is_metadata_or_footnote", "extraction_timestamp", "extraction_status", "notes"]
)

# ------------------------------------------------------------------------------
# 6. RAW: Petroleum Trade Value in US$
# ------------------------------------------------------------------------------
src_file = "1751964622_PT_IMPORT_VAL_US$_H.xlsx"
wb = openpyxl.load_workbook(data_dir / src_file, data_only=True)
sheet_name = "PT_IMPORT_VAL$_H"
ws = wb[sheet_name]

raw_val_usd = []
val_usd_years = [clean_val(ws.cell(8, c).value) for c in range(2, ws.max_column + 1) if ws.cell(8, c).value is not None]

for r_idx in range(9, ws.max_row + 1):
    row_label = clean_val(ws.cell(r_idx, 1).value)
    if not row_label and not any(ws.cell(r_idx, c).value for c in range(2, len(val_usd_years) + 2)):
        continue
    is_note = r_idx >= 43 or "source" in row_label.lower() or "note" in row_label.lower()
    for c_idx, yr in enumerate(val_usd_years, 2):
        val = clean_val(ws.cell(r_idx, c_idx).value)
        raw_val_usd.append({
            "source_file": src_file,
            "source_sheet": sheet_name,
            "source_row_number": r_idx,
            "source_table_title": "Import/Export Value in US Dollars",
            "source_row_label": row_label,
            "source_column_name": yr,
            "source_raw_value": val,
            "source_unit": "Million US$",
            "reporting_period": yr,
            "is_metadata_or_footnote": "Yes" if is_note else "No",
            "extraction_timestamp": timestamp,
            "extraction_status": "Success",
            "notes": "ISPRL 756 TMT crude import value excluded in 2018-19 per footnote 47."
        })
wb.close()

save_raw_table(
    "raw_petroleum_trade_value_usd.csv",
    raw_val_usd,
    ["source_file", "source_sheet", "source_row_number", "source_table_title", "source_row_label", "source_column_name", "source_raw_value", "source_unit", "reporting_period", "is_metadata_or_footnote", "extraction_timestamp", "extraction_status", "notes"]
)

# ------------------------------------------------------------------------------
# 7. RAW: Petroleum Trade Value in INR
# ------------------------------------------------------------------------------
src_file = "1751964598_PT_IMPORT_VAL_RS.CRS._H.xlsx"
wb = openpyxl.load_workbook(data_dir / src_file, data_only=True)
sheet_name = "PT_IMPORT_VALRS_H"
ws = wb[sheet_name]

raw_val_inr = []
val_inr_years = [clean_val(ws.cell(8, c).value) for c in range(2, ws.max_column + 1) if ws.cell(8, c).value is not None]

for r_idx in range(9, ws.max_row + 1):
    row_label = clean_val(ws.cell(r_idx, 1).value)
    if not row_label and not any(ws.cell(r_idx, c).value for c in range(2, len(val_inr_years) + 2)):
        continue
    is_note = r_idx >= 43 or "source" in row_label.lower() or "note" in row_label.lower()
    for c_idx, yr in enumerate(val_inr_years, 2):
        val = clean_val(ws.cell(r_idx, c_idx).value)
        raw_val_inr.append({
            "source_file": src_file,
            "source_sheet": sheet_name,
            "source_row_number": r_idx,
            "source_table_title": "Import/Export Value in Indian Rupees",
            "source_row_label": row_label,
            "source_column_name": yr,
            "source_raw_value": val,
            "source_unit": "Rs. Crore",
            "reporting_period": yr,
            "is_metadata_or_footnote": "Yes" if is_note else "No",
            "extraction_timestamp": timestamp,
            "extraction_status": "Success",
            "notes": "Reported in Crores of Rupees."
        })
wb.close()

save_raw_table(
    "raw_petroleum_trade_value_inr.csv",
    raw_val_inr,
    ["source_file", "source_sheet", "source_row_number", "source_table_title", "source_row_label", "source_column_name", "source_raw_value", "source_unit", "reporting_period", "is_metadata_or_footnote", "extraction_timestamp", "extraction_status", "notes"]
)

# ------------------------------------------------------------------------------
# 8. RAW: Indian Crude Basket FOB Price
# ------------------------------------------------------------------------------
src_file = "1775133106_PP_Crude-Oil-FOB-Price-(Indian Basket)-Historical.xlsx"
wb = openpyxl.load_workbook(data_dir / src_file, data_only=True)
sheet_name = "Sheet1"
ws = wb[sheet_name]

raw_basket_price = []
# Row 13 (1-indexed) has Month column names
month_cols = ["Year", "April", "May", "June", "July", "August", "September", "October", "November", "December", "January", "February", "March", "Average", "Ratio"]

for r_idx in range(14, ws.max_row + 1):
    yr_label = clean_val(ws.cell(r_idx, 1).value)
    if not yr_label:
        continue
    is_note = "note" in yr_label.lower() or "*" in yr_label
    for c_idx in range(2, 16):
        col_header = month_cols[c_idx - 1]
        val = clean_val(ws.cell(r_idx, c_idx).value)
        raw_basket_price.append({
            "source_file": src_file,
            "source_sheet": sheet_name,
            "source_row_number": r_idx,
            "source_table_title": "Crude Oil FOB Price (Indian Basket)",
            "source_financial_year": yr_label,
            "source_column_name": col_header,
            "source_raw_value": val,
            "source_unit": "$/bbl." if col_header != "Ratio" else "Sour:Sweet Ratio",
            "reporting_period": f"{yr_label} - {col_header}",
            "is_metadata_or_footnote": "Yes" if is_note else "No",
            "extraction_timestamp": timestamp,
            "extraction_status": "Success",
            "notes": "Represents monthly average daily prices; Ratio represents previous year processing ratio."
        })
wb.close()

save_raw_table(
    "raw_crude_oil_indian_basket_price.csv",
    raw_basket_price,
    ["source_file", "source_sheet", "source_row_number", "source_table_title", "source_financial_year", "source_column_name", "source_raw_value", "source_unit", "reporting_period", "is_metadata_or_footnote", "extraction_timestamp", "extraction_status", "notes"]
)

# ------------------------------------------------------------------------------
# 9. RAW: PDF Table Extractions (Table 9 conversion factors & RE 2025-26)
# ------------------------------------------------------------------------------
# Table 9 of ICR July 26
raw_pdf_conversions = [
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "LPG", "weight_mt": "1", "barrels": "11.6", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "SKO", "weight_mt": "1", "barrels": "8.1", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Diesel", "weight_mt": "1", "barrels": "7.6", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Petrol", "weight_mt": "1", "barrels": "8.9", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Naphtha", "weight_mt": "1", "barrels": "8.7", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "ATF", "weight_mt": "1", "barrels": "8.1", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Bitumen", "weight_mt": "1", "barrels": "6.1", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Furnace Oil", "weight_mt": "1", "barrels": "6.7", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Lubes", "weight_mt": "1", "barrels": "7.2", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Light Diesel Oil", "weight_mt": "1", "barrels": "7.4", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Petcoke", "weight_mt": "1", "barrels": "5.5", "source_unit": "bbl/MT"},
    {"source_file": "1787315734_ICR_July 26.pdf", "source_page": 31, "source_table": "Table-9", "product": "Product Basket (for Others)", "weight_mt": "1", "barrels": "8.1", "source_unit": "bbl/MT"},
]
save_raw_table(
    "raw_official_conversion_factors_table9.csv",
    raw_pdf_conversions,
    ["source_file", "source_page", "source_table", "product", "weight_mt", "barrels", "source_unit"]
)

# RE 2025-26 from PDF
raw_re_2526 = [
    {"product_group": "Sensitive Products", "product": "LPG", "re_2025_26_tmt": "33702", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Sensitive Products", "product": "SKO", "re_2025_26_tmt": "449", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Major Decontrolled Products", "product": "MS", "re_2025_26_tmt": "42534", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Major Decontrolled Products", "product": "NAPHTHA", "re_2025_26_tmt": "11699", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Major Decontrolled Products", "product": "HSD", "re_2025_26_tmt": "94087", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Major Decontrolled Products", "product": "ATF", "re_2025_26_tmt": "9131", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Major Decontrolled Products", "product": "LDO", "re_2025_26_tmt": "1006", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Major Decontrolled Products", "product": "LUBES", "re_2025_26_tmt": "4921", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Major Decontrolled Products", "product": "FO/LSHS", "re_2025_26_tmt": "6142", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Major Decontrolled Products", "product": "BITUMEN", "re_2025_26_tmt": "9094", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Minor Decontrolled Products", "product": "PetCoke", "re_2025_26_tmt": "20962", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Minor Decontrolled Products", "product": "Others", "re_2025_26_tmt": "10277", "source_unit": "TMT", "source_page": 1},
    {"product_group": "Grand Total", "product": "All Products", "re_2025_26_tmt": "244002", "source_unit": "TMT", "source_page": 1},
]
save_raw_table(
    "raw_revised_estimates_fy2025_26.csv",
    raw_re_2526,
    ["product_group", "product", "re_2025_26_tmt", "source_unit", "source_page"]
)

print("All source-preserving raw extractions successfully executed!")
