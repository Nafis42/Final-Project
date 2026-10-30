# Phase 3 Execution Environment, Dependencies, and Reproduction Guide

**Project:** India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption  
**Phase:** Phase 3 — Core Petroleum Supply-Chain Dataset Construction  

---

## 1. System & Runtime Environment

- **Operating System:** Windows 11 (PowerShell terminal)
- **Python Version:** 3.13.5 (64-bit)
- **Execution Working Directory:** Project Root (`c:\Users\nafis\OneDrive\Desktop\Final-Project`)

---

## 2. Required Python Dependencies

The pipeline relies on the following standard, tested packages:

```
pandas>=2.2.0, <4.0.0
numpy>=1.26.0, <3.0.0
pyarrow>=15.0.0, <26.0.0
openpyxl>=3.1.0, <4.0.0
xlrd>=2.0.1, <3.0.0
pypdf>=4.0.0, <7.0.0
```

To install or verify dependencies in a clean virtual environment:

```bash
pip install pandas numpy pyarrow openpyxl xlrd pypdf
```

---

## 3. Reproduction Instructions

To execute Phase 3 from scratch and rebuild all standardized datasets, derived indicators, provenance matrices, and reports:

```bash
# Execute Phase 3 master build script
python 04_Analysis/phase3/build_core_supply_chain_dataset.py
# (Or alternatively: python src/build_core_supply_chain_dataset.py)
```

### Execution Flow:
1. `[Step 1]` Reads standardized series from `03_Processed_Data/standardized/` and constructs `core_annual_petroleum_dataset.csv` & `.parquet` (30 fiscal periods).
2. `[Step 2]` Reshapes and harmonizes 12 product lines into `petroleum_product_level_dataset.csv` & `.parquet` (404 product-period observations).
3. `[Step 3]` Merges trade values (USD and INR), exchange rates, crude FOB basket prices, and exchequer contributions into `petroleum_supporting_variables.csv` & `.parquet` (28 periods).
4. `[Step 4]` Computes derived indicators (net crude imports, import-dependence proxy, production-to-processing ratio, import unit values, refining multiplier) and saves to `derived_indicators.csv` & `.parquet`.
5. `[Step 5]` Generates `source_coverage_matrix.csv` detailing temporal spans and coverage for 10 variable domains.
6. `[Step 6]` Compiles record-level traceability matrix into `core_dataset_provenance.csv` (300 lineage records).
7. `[Step 7]` Generates `dataset_schema_and_definitions.md` documenting accounting identities and formulas.
8. `[Step 8]` Cross-references 50 published audit figures in `graph_and_report_reference_catalogue.csv`.
9. `[Step 9]` Executes the 10-dimension validation suite and writes `phase3_validation_report.md`.
10. `[Step 10]` Compiles the final Phase 3 completion report in `phase3_build_report.md`.
