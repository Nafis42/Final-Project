import os
import re
import csv
from pathlib import Path
import openpyxl
import xlrd
import pypdf

base_dir = Path(".")
data_dir = base_dir / "01_Original_Data"
audit_dir = base_dir / "02_Source_Audit"

# 1. Search Excel files for charts and chart-related sheets
excel_files = sorted([f for f in data_dir.iterdir() if f.suffix.lower() in [".xls", ".xlsx"]])

charts_found = []

print(f"Scanning {len(excel_files)} Excel files for embedded charts and visualizations...")

for f in excel_files:
    fname = f.name
    ext = f.suffix.lower()
    
    # Check with openpyxl if xlsx or misnamed xls
    with open(f, "rb") as fp:
        magic = fp.read(8)
    is_zip = magic.startswith(b"PK\x03\x04")
    
    if is_zip:
        try:
            wb = openpyxl.load_workbook(f, data_only=False)
            for sname in wb.sheetnames:
                ws = wb[sname]
                # Check embedded charts in openpyxl
                ws_charts = getattr(ws, '_charts', [])
                if ws_charts:
                    for c_idx, chart in enumerate(ws_charts, 1):
                        title = str(chart.title) if chart.title else "Untitled Chart"
                        chart_type = type(chart).__name__
                        charts_found.append({
                            "source_file": fname,
                            "sheet_name": sname,
                            "chart_id": f"{fname}_{sname}_C{c_idx}",
                            "chart_title": title,
                            "chart_type": chart_type,
                            "axis_labels": f"X: {getattr(chart, 'x_axis', 'N/A')} | Y: {getattr(chart, 'y_axis', 'N/A')}",
                            "units": "Inferred from sheet data",
                            "series_names": "Dynamic / embedded",
                            "covered_period": "Derived from sheet data",
                            "source_data_range": "Embedded chart references",
                            "data_availability": "Available",
                            "notes": f"Native openpyxl chart found: {chart_type}"
                        })
                # Check if sheet itself is a chart / graph sheet or contains chart drawing clues
                if "graph" in sname.lower() or "chart" in sname.lower():
                    # Inspect sheet cells
                    charts_found.append({
                        "source_file": fname,
                        "sheet_name": sname,
                        "chart_id": f"{fname}_{sname}_Sheet",
                        "chart_title": f"Dedicated Visualization Sheet: {sname}",
                        "chart_type": "Chart/Dashboard Worksheet",
                        "axis_labels": "See worksheet content",
                        "units": "See sheet header",
                        "series_names": "Sheet-level series",
                        "covered_period": "Historical FY",
                        "source_data_range": f"{sname}!A1:Z50",
                        "data_availability": "Available",
                        "notes": "Dedicated visualization / graph sheet present in workbook."
                    })
            wb.close()
        except Exception as e:
            print(f"Warning scanning charts in {fname}: {e}")
    else:
        # For .xls files, check sheet names
        try:
            wb = xlrd.open_workbook(f)
            for sname in wb.sheet_names():
                if "graph" in sname.lower() or "chart" in sname.lower():
                    charts_found.append({
                        "source_file": fname,
                        "sheet_name": sname,
                        "chart_id": f"{fname}_{sname}_Sheet",
                        "chart_title": f"Dedicated Visualization Sheet: {sname}",
                        "chart_type": "Chart/Dashboard Worksheet",
                        "axis_labels": "See worksheet content",
                        "units": "See sheet header",
                        "series_names": "Sheet-level series",
                        "covered_period": "Historical FY",
                        "source_data_range": f"{sname}!A1:Z50",
                        "data_availability": "Available",
                        "notes": "Dedicated visualization / graph sheet in legacy .xls."
                    })
        except Exception as e:
            print(f"Warning scanning xls {fname}: {e}")

print(f"Excel charts found: {len(charts_found)}")

# 2. Search PDF files for figures, charts, and tables
pdf_files = sorted([f for f in data_dir.iterdir() if f.suffix.lower() == ".pdf"])

figures_in_pdfs = []
tables_in_pdfs = []

figure_patterns = [
    r'(Figure[-\s]*[0-9A-Za-z]+)\s*[:\.]\s*([^\n\r]+)',
    r'(Fig\.[-\s]*[0-9A-Za-z]+)\s*[:\.]\s*([^\n\r]+)',
    r'(Chart[-\s]*[0-9A-Za-z]+)\s*[:\.]\s*([^\n\r]+)',
]

table_patterns = [
    r'(Table[-\s]*[0-9A-Za-z]+)\s*[:\.]\s*([^\n\r]+)',
    r'(Statement[-\s]*[0-9A-Za-z]+)\s*[:\.]\s*([^\n\r]+)',
    r'(Annexure[-\s]*[0-9A-Za-z]+)\s*[:\.]\s*([^\n\r]+)',
]

for f in pdf_files:
    fname = f.name
    print(f"Scanning PDF: {fname}...")
    reader = pypdf.PdfReader(f)
    for p_idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        lines = text.split("\n")
        
        # Check figures
        for line in lines:
            line_str = line.strip()
            for pat in figure_patterns:
                m = re.search(pat, line_str, re.IGNORECASE)
                if m:
                    fig_id = m.group(1).strip()
                    fig_title = m.group(2).strip()
                    figures_in_pdfs.append({
                        "source_file": fname,
                        "page_number": p_idx + 1,
                        "figure_id": fig_id,
                        "figure_title": fig_title,
                        "figure_type": "PDF Graphical Figure / Plot",
                        "reporting_period": "See title/context",
                        "source_attribution": "PPAC / Oil Companies / OMCs",
                        "underlying_data_status": "Available in corresponding tables or workbooks",
                        "data_linkage": "Corresponds to monthly/annual consumption & trade series",
                        "notes": line_str[:150]
                    })
            for t_pat in table_patterns:
                m = re.search(t_pat, line_str, re.IGNORECASE)
                if m:
                    tbl_id = m.group(1).strip()
                    tbl_title = m.group(2).strip()
                    tables_in_pdfs.append({
                        "source_file": fname,
                        "page_number": p_idx + 1,
                        "table_id": tbl_id,
                        "table_title": tbl_title,
                        "reporting_period": "See title/context",
                        "source_attribution": "PPAC / MoPNG / DGCIS",
                        "units": "TMT / MMT / bbl.",
                        "extractable_status": "Extractable text / Table structure",
                        "notes": line_str[:150]
                    })

print(f"PDF Figures identified: {len(figures_in_pdfs)}")
print(f"PDF Tables identified: {len(tables_in_pdfs)}")

# Output summary to console
