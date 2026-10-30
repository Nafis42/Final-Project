import os
import sys
import openpyxl
import xlrd
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

print("=== STARTING DETAILED SOURCE INSPECTION ===")

data_dir = "01_Original_Data"

# 1. Inspect 1788266304_PT_crude_processing_H.xls
xls_path = os.path.join(data_dir, "1788266304_PT_crude_processing_H.xls")
wb = xlrd.open_workbook(xls_path)
print(f"\n1. {xls_path}")
print("Sheets:", wb.sheet_names())
for sheet_name in wb.sheet_names()[:3]:
    ws = wb.sheet_by_name(sheet_name)
    print(f"Sheet: {sheet_name}, rows={ws.nrows}, cols={ws.ncols}")
    for r in range(min(12, ws.nrows)):
        row_vals = [str(ws.cell_value(r, c)).strip() for c in range(min(10, ws.ncols))]
        if any(row_vals):
            print(f"  R{r+1}: {row_vals}")

# 2. Inspect 1787137273_Statewise_Sales-POL_Consumption_Final.xlsx
xlsx_path = os.path.join(data_dir, "1787137273_Statewise_Sales-POL_Consumption_Final.xlsx")
wb = openpyxl.load_workbook(xlsx_path, data_only=True)
print(f"\n2. {xlsx_path}")
print("Sheets:", wb.sheetnames)
ws = wb.active
print(f"Active sheet: {ws.title}, max_row={ws.max_row}, max_col={ws.max_column}")
for r in range(1, min(15, ws.max_row+1)):
    row_vals = [str(ws.cell(r, c).value).strip() if ws.cell(r, c).value is not None else "" for c in range(1, min(12, ws.max_column+1))]
    if any(row_vals):
        print(f"  R{r}: {row_vals}")

# 3. Inspect 1761715894_petroleum-prices-and-under-recoveries.xlsx
xlsx_path = os.path.join(data_dir, "1761715894_petroleum-prices-and-under-recoveries.xlsx")
wb = openpyxl.load_workbook(xlsx_path, data_only=True)
print(f"\n3. {xlsx_path}")
print("Sheets:", wb.sheetnames)
ws = wb.active
print(f"Active sheet: {ws.title}, max_row={ws.max_row}, max_col={ws.max_column}")
for r in range(1, min(15, ws.max_row+1)):
    row_vals = [str(ws.cell(r, c).value).strip() if ws.cell(r, c).value is not None else "" for c in range(1, min(10, ws.max_column+1))]
    if any(row_vals):
        print(f"  R{r}: {row_vals}")

# 4. Inspect Monthly Import files (1729493890, 1729493957, 1751966513, 1784609810, 1787119859)
monthly_files = [
    "1729493890_pt_import_en.xlsx",
    "1729493957_val-in-dollar_en.xlsx",
    "1751966513_val-in-dollar-en.xlsx",
    "1784609810_PT_IMPORT_VAL_US$_25-26.xlsx",
    "1787119859_PT_Import_Val_USD.xls"
]
for mf in monthly_files:
    p = os.path.join(data_dir, mf)
    print(f"\nMonthly: {mf}")
    if mf.endswith(".xlsx"):
        wb = openpyxl.load_workbook(p, data_only=True)
        ws = wb.active
        print(f"  Sheet: {ws.title}, rows={ws.max_row}, cols={ws.max_column}")
        for r in range(8, min(20, ws.max_row+1)):
            row_vals = [str(ws.cell(r, c).value).strip() if ws.cell(r, c).value is not None else "" for c in range(1, min(15, ws.max_column+1))]
            if any(row_vals):
                print(f"  R{r}: {row_vals[:6]}")
    else:
        wb = xlrd.open_workbook(p)
        ws = wb.sheet_by_index(0)
        print(f"  Sheet: {ws.name}, rows={ws.nrows}, cols={ws.ncols}")
        for r in range(7, min(20, ws.nrows)):
            row_vals = [str(ws.cell_value(r, c)).strip() for c in range(min(15, ws.ncols))]
            if any(row_vals):
                print(f"  R{r+1}: {row_vals[:6]}")
