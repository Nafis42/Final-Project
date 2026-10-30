# Data Issues, Anomalies, and Methodological Questions

**Project:** *India's Petroleum Supply Chain and Import Exposure*  
**Phase:** Phase 1 — Workspace Inventory and Source Audit  
**Author:** Antigravity Research Agent  
**Deliverable:** `02_Source_Audit/data_issues_and_questions.md`  
**Date:** October 2026  

---

## 1. Introduction

During the Phase 1 source audit of the 33 files supplied in [`01_Original_Data`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data), several critical format defects, accounting definitions, temporal asymmetries, and boundary conditions were identified. 

In strict adherence to the research principles established in the [Master Research Brief](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/Antigravity_Petroleum_Research_Master_Brief.md) (Evidence before conclusions, No silent assumptions, No invented data), this document logs every technical anomaly and presents the specific methodological decisions requiring researcher sign-off before Phase 2 extraction begins.

---

## 2. Technical Format Defects and Software Environment Issues

### 2.1 Critical Binary Format Mismatch: Named `.xls` but Binary Structure is `.xlsx` (OOXML)

* **Affected File:** [`1785841030_Under_Recoveries_to_Oil_Marketing_Companies_(OMCs)_on_Sale_of_Sensitive_Petroleum_Products_Rs_Crore.xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1785841030_Under_Recoveries_to_Oil_Marketing_Companies_(OMCs)_on_Sale_of_Sensitive_Petroleum_Products_Rs_Crore.xls)
* **Observed Defect:**
  - File extension is `.xls` (legacy Excel 97–2003 BIFF8).
  - Magic byte inspection reveals: `PK\x03\x04` (Zip archive / Office Open XML).
  - When parsed with `xlrd` (the standard `.xls` reader), it raises:
    `xlrd.biffh.XLRDError: Excel xlsx file; not supported`.
  - When passed directly by filename to `openpyxl`, `openpyxl` checks the file extension and raises:
    `openpyxl.utils.exceptions.InvalidFileException: openpyxl does not support the old .xls file format`.
* **Impact:** Standard automated scripts using file extensions to choose the engine will fail to read this file.
* **Safe Fix Implemented:**
  - In our audit pipeline, file bytes are inspected by magic signature first. If a file with a `.xls` extension contains a ZIP header, it is read into an in-memory byte stream (`io.BytesIO(fbytes)`) and passed to `openpyxl`.
  - *No modification or destructive renaming of the original source file was performed.*
  - The workbook was successfully parsed: it contains 1 sheet (`HISTORICAL`, 37 rows × 30 columns) reporting under-recoveries in Rs. Crore from 2002–03 to 2025–26.

### 2.2 Missing Legacy Excel and PDF Reader Libraries in Environment

* **Initial State:** The Python 3.13 environment in the workspace was equipped with `openpyxl` and `pandas`, but lacked `xlrd` (for `.xls`) and any PDF extraction library (`pypdf` / `pdfplumber`).
* **Safe Fix Applied:**
  - Installed `xlrd` (v2.0.2) and `pypdf` (v6.21.1) via pip in the environment.
  - All 12 `.xls` files and 4 `.pdf` files can now be read reproducibly by all project scripts.

---

## 3. Duplicate Files and Version Discrepancies

### 3.1 Binary Hash Discrepancies on Identical Data (OLE2 Timestamps)

Two core datasets exist as apparent duplicates with differing SHA-256 hashes:

1. **Crude Oil Production:**  
   - Master: [`1717395338_PT_Crude_oil_production_H.xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1717395338_PT_Crude_oil_production_H.xls) (`99f4de58b8...`)
   - Copy: [`1717395338_PT_Crude_oil_production_H (1).xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1717395338_PT_Crude_oil_production_H (1).xls) (`0c446c3b07...`)
2. **Petroleum Product Consumption:**  
   - Master: [`1788343376_PT_Consumption_English.xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1788343376_PT_Consumption_English.xls) (`35019485d5...`)
   - Copy: [`1788343376_PT_Consumption_English (1).xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1788343376_PT_Consumption_English (1).xls) (`153ff92a41...`)

* **Detailed Audit Findings:**
  - Both files in each pair have identical byte sizes (98,304 bytes for Crude Production; 431,616 bytes for Consumption).
  - Cell-by-cell script inspection confirmed **100.0% data identity** across all rows, columns, and sheets.
  - *Explanation:* In the Microsoft OLE2 Compound Document format, internal stream headers record creation and modification timestamps when a file is saved or downloaded from a browser at different times. This alters the cryptographic hash without modifying a single data byte.
* **Recommendation:** Designate the unnumbered file as the primary authoritative source for Phase 2 extraction. Retain the `(1)` file in the audit log for complete provenance tracking.

### 3.2 Exact Byte-Level Duplicates

The following pairs exhibit identical SHA-256 hashes:
1. `1761715894_petroleum-prices-and-under-recoveries.xlsx` and `... (1).xlsx` (Hash: `2e959a24e0...`)
2. `1781164918_NG-H_LNG_Import.xlsx` and `... (1).xlsx` (Hash: `c2a47ca874...`)

* **Audit Action:** Both are confirmed redundant downloads. Unnumbered masters will be referenced; duplicate copies will remain intact in `01_Original_Data`.

### 3.3 Master Historical Workbooks vs. Redundant Single-Year Monthly Extracts

Four workbooks in `01_Original_Data` are single-year monthly extracts whose contents are completely subsumed by the comprehensive historical master files:

* [`1729493890_pt_import_en.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1729493890_pt_import_en.xlsx) (1 sheet: FY 2023–24 monthly trade) \(\rightarrow\) Exact subset of sheet `PT_IMPORT_2023-24` in [`1751964547_PT_IMPORT_TMT_H.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1751964547_PT_IMPORT_TMT_H.xlsx).
* [`1729493957_val-in-dollar_en.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1729493957_val-in-dollar_en.xlsx) (1 sheet: FY 2023–24 monthly USD value) \(\rightarrow\) Exact subset of sheet `PT_Import_Val_2023-24` in [`1751964622_PT_IMPORT_VAL_US$_H.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1751964622_PT_IMPORT_VAL_US$_H.xlsx).
* [`1751966513_val-in-dollar-en.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1751966513_val-in-dollar-en.xlsx) (1 sheet: FY 2024–25 monthly USD value) \(\rightarrow\) Exact subset of sheet `PT_Import_Val_2024-25` in [`1751964622_PT_IMPORT_VAL_US$_H.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1751964622_PT_IMPORT_VAL_US$_H.xlsx).

* **Recommendation:** Extract all historical and monthly trade series directly from the master workbooks (`1751964547` and `1751964622`). Treat the single-year files as redundant verification checks.

---

## 4. Specific Data Anomalies, Omissions, and Asymmetries

### 4.1 Temporal Asymmetry Across Core Datasets (The FY 2024–25 Truncation)

* **Observation:**
  - Refinery Crude Processing extends through **FY 2024–25** (and FY 2025–26 provisional).
  - Petroleum Product Production extends through **FY 2024–25 (Provisional)**.
  - Petroleum Trade (TMT and US$) extends through **FY 2024–25**.
  - Petroleum Product Consumption extends through **FY 2024–25** (and FY 2025–26 provisional).
  - **However, Domestic Crude Oil Production ([`1717395338_PT_Crude_oil_production_H.xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1717395338_PT_Crude_oil_production_H.xls)) stops at FY 2023–24 (Provisional).**
* **Risk:** Attempting to build an annual crude balance for FY 2024–25 will result in a missing value for domestic crude production unless an official figure can be verified from supplementary official publications.
* **Proposed Resolution:**
  - Define the primary common core historical supply-chain table as **FY 1998–99 to FY 2023–24 (26 Financial Years)**.
  - Document FY 2024–25 in downstream processing, trade, and consumption tables as an extended year, while flagging the domestic production column as unobserved in the supplied upstream workbook.

### 4.2 Handling of Crude Oil Exports

* **Observation:**
  - In [`1751964547_PT_IMPORT_TMT_H.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1751964547_PT_IMPORT_TMT_H.xlsx) (sheet `PT_IMPORT_H`), the import block explicitly reports `CRUDE OIL$` on row 10.
  - The export block (rows 25–38) is titled `PRODUCT EXPORT @` and lists only petroleum products (LPG, MS, Naphtha, ATF, SKO, HSD, LDO, LOBS, Fuel Oil, Bitumen, Others).
  - There is **no row for Crude Oil Exports**.
* **Research Risk:** Master Brief Section 5.2.A warns: *"If exports are not reported, do not automatically assume they are zero. Investigate the source and explain how the measure is handled."*
* **Analytical Finding:**
  - India’s trade policy and domestic petroleum regulations strictly prohibit or severely restrict the export of domestic crude oil, as domestic crude production meets only a fraction of domestic refinery requirements. All domestically produced crude is refined internally.
  - Official PPAC trade statistics report total petroleum exports as synonymous with product exports.
* **Proposed Resolution:** In the supply chain balance, record crude oil exports as zero (or not reported / legally restricted) and document the official PPAC reporting scope in the provenance notes.

### 4.3 Strategic Petroleum Reserve (ISPRL) Exclusion Footnote in 2018–19

* **Observation:**
  - Footnote 47 in [`1751964622_PT_IMPORT_VAL_US$_H.xlsx`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1751964622_PT_IMPORT_VAL_US$_H.xlsx) explicitly notes:
    `"$Crude oil imports does not include value of crude oil quantity of 756 TMT imported at ISPRL, Mangalore during 2018-19."`
* **Impact on Unit-Value Calculations:**
  - If total crude import expenditure is divided by total crude import quantity in FY 2018–19 without adjusting for this 756 TMT SPR cargo, the implied unit value will be slightly understated.
* **Proposed Resolution:** In Phase 6 (Import Expenditure Analysis), explicitly adjust for this 756 TMT quantity when calculating implied unit values or report the sensitivity of the unit value to the SPR inclusion/exclusion.

### 4.4 Boundary Shift in Consumption Definition (FY 2017–18 SEZ Inclusion)

* **Observation:**
  - In [`1788343376_PT_Consumption_English.xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1788343376_PT_Consumption_English.xls), Note iii states that consumption represents market demand, comprising:
    (a) actual sales by oil companies in the domestic market,
    (b) consumption through direct imports by private parties, and
    (c) sales by SEZ units in the Domestic Tariff Area (DTA).
  - Note iii specifies: `"* Included from FY 2017-18 onwards"`.
* **Impact:** A structural break occurs in FY 2017–18. A portion of the consumption growth in FY 2017–18 represents an accounting boundary expansion (capturing SEZ sales to DTA) rather than organic market demand expansion.
* **Proposed Resolution:** Document this structural break explicitly in Phase 4 trend analysis and Phase 5 product balances. Do not interpret all post-2017 demand shifts as purely organic growth.

### 4.5 Separation of Condensate Production from Crude Oil (FY 2006–07)

* **Observation:**
  - In [`1717395338_PT_Crude_oil_production_H.xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1717395338_PT_Crude_oil_production_H.xls), Note `*` states:
    `"*Condensate production is shown seperately from 2006-07 onwards."`
  - From FY 1998–99 to 2005–06, the condensate row is blank, and condensate is bundled inside the crude oil production figures of ONGC and OIL.
* **Proposed Resolution:** Use `Total (Crude oil + condensate)` (Row 19) as the primary upstream domestic production series to ensure longitudinal consistency before and after 2006–07.

### 4.6 File Heading Anomaly in `1787119859_PT_Import_Val_USD.xls`

* **Observation:**
  - Workbook [`1787119859_PT_Import_Val_USD.xls`](file:///c:/Users/nafis/OneDrive/Desktop/Final-Project/01_Original_Data/1787119859_PT_Import_Val_USD.xls) contains a single sheet titled `PT_Import_Val_USD`.
  - Cell R4:C0 reads: `2026-27`.
  - The column headers are monthly (April, May, June, July, ..., Total).
  - Values exist only for April, May, June, and July; August through March are `0.0`.
  - In cell R10:C13, the Crude Oil total is recorded as `63,374.017` Million US$ for these 4 months.
* **Assessment:**
  - This appears to be either a preliminary early-year extract for FY 2026–27 or a mislabeled fiscal year extract.
* **Proposed Resolution:** Exclude this file from the historical core dataset. Retain it solely as a flagged anomaly in the audit log.

### 4.7 Identification of Hash-Named Workbook `1679651218_163fd52aba7df0b51c90.xls`

* **Audit Resolution:**
  - The workbook has been completely identified:
    - Sheet Name: `PS_1_Fiscal Subsidy`
    - Publisher: Petroleum Planning & Analysis Cell (PPAC)
    - Title: "Fiscal Subsidy on PDS Kerosene and Domestic LPG (under Subsidy Scheme, 2002)"
    - Unit: Rs. Crore
    - Period: FY 2002–03 to FY 2014–15
  - *Research Role:* Supplementary / Excluded from core physical supply-chain balance.

---

## 5. Decisions Requiring Researcher Approval Before Phase 2

The researcher's formal sign-off is requested on the following methodological decisions:

### Decision 1: Approval of the Common Historical Time Window
* **Proposed Core Window:** **FY 1998–99 to FY 2023–24 (26 Financial Years)** for the core physical supply chain (Crude Production, Imports, Processing, Product Production, Consumption).
* **Proposed Price & Value Window:** **FY 2000–01 to FY 2023–24 (24 Financial Years)** for joint analysis including the Indian Crude Basket FOB price.
* *Alternative:* Truncate the entire study to FY 2000–01 to 2023–24 so that price and volume share an identical start year.

### Decision 2: Upstream Production Measure (Crude Oil vs. Crude + Condensate)
* **Recommendation:** Adopt `Total (Crude oil + condensate)` (Row 19 of `PT_PRODUCTION_H`) as the primary measure of domestic upstream crude supply.
* *Rationale:* Prior to 2006–07, condensate was included within reported crude figures. Using the combined total ensures unbroken historical comparability.

### Decision 3: Treatment of Crude Oil Exports
* **Recommendation:** Record crude oil exports as zero (or not reported / restricted) in the supply chain accounting table, accompanied by a footnote citing Indian export restrictions and PPAC reporting convention.

### Decision 4: Supercedence of Single-Year Extract Workbooks
* **Recommendation:** Extract all trade volume and value data directly from the master multi-sheet workbooks (`1751964547_PT_IMPORT_TMT_H.xlsx` and `1751964622_PT_IMPORT_VAL_US$_H.xlsx`). Defer single-year extract workbooks (`1729493890`, `1729493957`, `1751966513`) to secondary verification status.

### Decision 5: Exclusion of Adjacent Natural Gas and Fiscal Datasets
* **Recommendation:** Maintain the research scope strictly focused on crude oil and petroleum products. Exclude the 5 Natural Gas / LNG files and 4 Fiscal Subsidy files from the primary supply-chain master table.
