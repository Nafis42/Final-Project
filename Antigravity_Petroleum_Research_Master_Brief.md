# MASTER RESEARCH BRIEF FOR ANTIGRAVITY
## Research Project: India's Petroleum Supply Chain and Import Exposure

**Role:** Act as a research data analyst, petroleum-industry researcher, Python data engineer, and research-paper development assistant.

**Working title:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption.*

**Primary objective:** Develop a reproducible, statistically sound, evidence-based research study using the supplied Excel workbooks and PDF reports. Analyse India's domestic crude oil production, crude imports, refinery processing, petroleum product production, petroleum product imports and exports, and petroleum consumption. Establish how these components have changed over time, quantify the country's exposure to imports, and identify meaningful relationships and policy-relevant findings supported by the data.

This project must be executed in phases. Do not attempt the entire research paper in one operation. Each phase must produce verifiable outputs, document assumptions, and wait for approval before moving to the next phase.

---

# 1. Research objectives and scope

## 1.1 Primary research questions

Investigate the following questions using the supplied data.

1. How has India's domestic crude oil production changed over the available historical period?
2. How have crude oil imports changed over the same period?
3. How has the relationship between domestic crude production and refinery crude processing changed?
4. What has happened to India's apparent crude oil import dependence over time?
5. How has domestic petroleum product production changed?
6. How have petroleum product imports and exports changed, both in aggregate and by product?
7. How has domestic petroleum product consumption evolved?
8. Which petroleum products account for the largest consumption volumes and net import or export balances?
9. How has the value of petroleum imports changed, and how much of that change can be associated with changes in import quantities versus implied import unit values?
10. Do the data reveal meaningful differences between trends in crude oil supply, refinery processing, petroleum product trade, and domestic consumption?
11. What conclusions can be drawn about India's petroleum supply-chain exposure, and what conclusions cannot be supported by the available data?

These are research questions, not predetermined conclusions. Do not assume that import dependence has necessarily increased, that refinery processing has necessarily grown, or that any particular product is becoming more important. Calculate the results first.

## 1.2 Scope boundaries

The primary study concerns crude oil and petroleum products.

The core analysis must focus on:
- Domestic crude oil production.
- Crude oil imports and exports, where available.
- Refinery crude oil processing.
- Petroleum product production.
- Petroleum product imports and exports.
- Petroleum product consumption.
- Petroleum import expenditure and unit-value trends, subject to compatible data.
- Historical trends and the relationships between these variables.

Natural gas, LNG, LPG customer counts, subsidies, state-level sales, and other adjacent datasets must not automatically become central parts of the paper. They may be useful in a supplementary analysis only if their relevance is demonstrated and the researcher approves the expansion.

Do not change the research topic simply because another dataset contains more data or produces more attractive charts.

## 1.3 Research principles

Follow these rules throughout the project:

1. **Evidence before conclusions.** Every factual finding must be traceable to a source or a documented calculation.
2. **No invented data.** Never fabricate observations, dates, units, missing values, source references, or results.
3. **No silent assumptions.** Record all assumptions and obtain approval for material methodological decisions.
4. **Preserve original data.** Never overwrite, rename destructively, or modify the original Excel or PDF files.
5. **Keep raw and processed data separate.**
6. **Reproducibility.** Every reported number must be reproducible from the source data using saved code or a documented calculation.
7. **Distinguish correlation from causation.** Historical relationships alone do not establish causality.
8. **Respect source definitions.** Do not replace official definitions with convenient alternatives without documenting the difference.
9. **No unsupported policy recommendations.** Policy implications must follow from the actual findings and their limitations.
10. **Do not rush.** A smaller verified dataset is preferable to a large but unreliable dataset.

---

# 2. Initial file inventory: candidate source files

All supplied files will be accessible in the project workspace. The following filenames are known candidate sources from the initial project inventory.

Do not assume that a filename proves its contents. Confirm each file's existence, format, internal sheets, date coverage, units, definitions, and data quality before assigning it to an analysis.

## 2.1 Core supply and production data

### A. Historical crude oil production

- `1717395338_PT_Crude_oil_production_H.xls`
- `1717395338_PT_Crude_oil_production_H (1).xls`

Purpose:
- Identify historical domestic crude oil production.
- Determine whether the two workbooks are duplicates, different versions, or different extracts.
- Establish the observation frequency, time coverage, units, and whether data represent financial years or calendar years.

Use only the verified authoritative version for the primary dataset. Retain the other file in the audit record.

### B. Historical crude oil imports and exports

- `1751964547_PT_IMPORT_TMT_H.xlsx`

Purpose:
- Identify crude oil import quantities.
- Identify crude oil export quantities if available.
- Check whether crude oil is separately identifiable from other petroleum commodities.
- Determine whether quantities are reported in tonnes, thousand metric tonnes, or another unit.

This file may also contain petroleum product trade data. Inspect its commodity categories before assigning columns to crude oil or individual petroleum products.

### C. Refinery crude oil processing

- `1788266304_PT_crude_processing_H.xls`

Purpose:
- Extract historical refinery crude oil processing or throughput.
- Identify the reporting unit and period.
- Determine whether the figures represent actual processing volumes, not installed refining capacity.

Do not describe throughput as capacity utilisation. Capacity utilisation requires a compatible measure of available or installed capacity.

### D. Petroleum product production

- `1761642701_PT_production_product_H.xls`

Purpose:
- Extract domestic petroleum product production by product and period.
- Identify the product categories and whether the figures are comparable across years.
- Investigate changes in category definitions and product coverage.

### E. Petroleum product consumption

- `1788343376_PT_Consumption_English (1).xls`

Purpose:
- Extract historical petroleum product consumption.
- Identify whether the figures are sales, reported consumption, apparent consumption, or another official measure.
- Confirm units, reporting periods, and product categories.

### F. State-wise petroleum product sales

- `1787137273_Statewise_Sales-POL_Consumption_Final.xlsx`

Purpose:
- Assess whether state-wise sales data are sufficiently consistent and relevant for a supplementary geographical analysis.
- Identify the available years, product categories, and units.

This workbook is not automatically required for the core national historical analysis. Use it only if it provides a defensible additional research question.

## 2.2 Petroleum import expenditure and price data

### G. Historical import value in rupees

- `1751964598_PT_IMPORT_VAL_RS.CRS._H.xlsx`

Purpose:
- Extract petroleum import expenditure in Indian rupees.
- Verify the currency, value scale, commodity scope, and reporting periods.

### H. Historical import value in US dollars

- `1751964622_PT_IMPORT_VAL_US$_H.xlsx`

Purpose:
- Extract historical import expenditure in US dollars.
- Verify whether the coverage matches the import quantity series.

### I. Historical Indian crude oil basket price

- `1775133106_PP_Crude-Oil-FOB-Price-(Indian Basket)-Historical.xlsx`

Purpose:
- Extract the Indian crude oil basket price series.
- Identify the price unit, such as dollars per barrel, and the frequency of observations.
- Determine whether monthly or daily values need to be converted into annual averages.

### J. Additional import-value extracts

- `1787119859_PT_Import_Val_USD.xls`
- `1784609810_PT_IMPORT_VAL_US$_25-26.xlsx`

Purpose:
- Check whether these files contain a more recent period, a revised series, a separate reporting definition, or a duplicate extract.
- Do not append them to the historical import-value series until overlaps and differences have been reconciled.

## 2.3 PDF reports and recent-period data

### K. Combined estimates for FY 2025–26

- `1773137026_Revised Estimates FY 2025-26_Combined.pdf`

Purpose:
- Inspect for revised estimates, recent official figures, definitions, and notes relevant to the study.
- Determine whether any values supplement or revise the historical workbook series.

### L. ICR report

- `1787315734_ICR_July 26.pdf`

Purpose:
- Inspect the full report to identify its publication date, reporting period, source definitions, and relevance to the core study.
- Extract data only if it directly contributes to a defined research question.

### M. Flash report

- `1788266780_Flash_Report_WEB_UPLOAD_Aug26.pdf`

Purpose:
- Inspect for recent petroleum-sector data and reporting notes.
- Verify whether figures are preliminary, provisional, estimated, or final.
- Do not merge preliminary values with final historical values without explicit labels and a documented reason.

### N. Additional workbook requiring identification

- `1679651218_163fd52aba7df0b51c90.xls`

Purpose:
- Inspect its title, internal sheets, headers, source, units, and time coverage before assigning it to any analysis.
- Do not infer its contents from its filename.

## 2.4 Other supplied workbooks

The supplied collection also includes files relating to natural gas, LNG, subsidies, LPG customers, fiscal information, and other petroleum-sector statistics.

Inventory all of them, but do not automatically include them in the main study. For each, record its subject and explain one of the following:

- Core source: directly needed for the primary research questions.
- Supplementary source: potentially useful for a separate, clearly defined extension.
- Excluded: outside the approved scope, redundant, insufficiently comparable, or not relevant.

Record the reason for every exclusion.

---

# 3. Phase 1 — Workspace inventory and source audit

## Objective

Understand exactly what data exist before performing any analysis.

## Tasks

### 3.1 Inventory every file

Create a complete file inventory containing:

- Exact filename and extension.
- File type.
- File size, if available.
- Workbook sheet names for Excel files.
- Sheet dimensions, where feasible.
- Column and row counts.
- Header locations.
- Apparent subject and source.
- Date or period coverage.
- Units.
- Duplicate or overlap status.
- Proposed role in the research.
- Verification status and outstanding questions.

Do not rely on the candidate list alone. Scan the actual workspace and include all supplied files.

### 3.2 Inspect every Excel workbook

For each workbook:

1. List all worksheet names.
2. Identify the sheet containing the actual data.
3. Inspect the first several rows and the final several rows.
4. Determine whether the first rows contain titles, explanatory notes, merged headers, or actual observations.
5. Identify multi-row headers and merged cells.
6. Determine whether years are stored as rows or columns.
7. Check for blank rows, subtotals, grand totals, footnotes, formulas, and hidden sheets.
8. Record missing values, special symbols, and non-numeric observations.
9. Identify units and any notes explaining the statistical series.
10. Confirm whether observations are annual, monthly, quarterly, or irregular.

If a legacy `.xls` workbook cannot be read, do not silently skip it. Try a suitable legacy Excel reader or a controlled conversion to `.xlsx`, retaining the original file and documenting the conversion.

### 3.3 Detect duplicate and overlapping sources

Compare apparent duplicates, including the two crude production files and the other overlapping extracts.

Use:
- Sheet names and dimensions.
- Header and metadata comparison.
- Exact data comparison.
- Overlapping year and value comparison.
- Source notes, revision dates, and publication details.

Classify each pair as:
- Exact duplicate.
- Duplicate with formatting differences.
- Overlapping but non-identical series.
- Different reporting periods.
- Different definitions.
- Unresolved.

Do not select one version merely because it is newer or easier to read. Explain the choice.

### 3.4 Deliverables

Create:

`outputs/phase_1/file_inventory.csv`

`outputs/phase_1/source_audit.csv`

`outputs/phase_1/source_inspection_report.md`

`outputs/phase_1/duplicate_and_overlap_report.md`

The inspection report must explain which files are suitable for which research questions and identify unresolved problems.

## Phase 1 completion gate

Stop and present the audit for review.

Do not start statistical modelling, generate research conclusions, or write the paper before the source inventory and the key data definitions have been checked.

---

# 4. Phase 2 — Data extraction and construction of a verified dataset

## Objective

Convert the relevant source sheets into clean, documented, analysis-ready datasets.

## 4.1 Create an immutable raw-data layer

Preserve original files unchanged.

Extract source tables into a separate directory:

`data/raw_extracted/`

For each extracted table, retain:
- Original filename.
- Original worksheet name.
- Original row or column labels.
- Original unit.
- Original reporting period.
- Source notes.
- A source reference sufficient to trace every observation back to the workbook and sheet.

Do not make the raw extracted data look cleaner by silently deleting inconvenient rows or changing values.

## 4.2 Create a standardised layer

Save processed data under:

`data/processed/`

Use explicit, consistent variable names, for example:

- `period`
- `period_type`
- `crude_production`
- `crude_imports`
- `crude_exports`
- `refinery_crude_processing`
- `product`
- `product_production`
- `product_imports`
- `product_exports`
- `product_consumption`
- `import_value_usd`
- `import_value_inr`
- `crude_basket_price`

These are proposed names, not permission to assume every variable exists.

Only create a variable if the corresponding source data have been verified.

Where product-level data are available, use one row per product and period rather than mixing all products into a single column.

## 4.3 Standardise units carefully

Create a unit-conversion table.

For example:
- Tonnes.
- Thousand metric tonnes (TMT).
- Million metric tonnes (MMT).
- Barrels.
- Barrels per day.
- Indian rupees.
- Crores of rupees.
- Million US dollars.
- US dollars per barrel.

Convert only when the original unit and conversion are clear.

Common conversions may include:

- \(1\text{ MMT}=1{,}000\text{ TMT}\)
- \(1\text{ TMT}=1{,}000\text{ metric tonnes}\)

Do not convert barrels to tonnes using a universal fixed factor unless an appropriate, justified density or conversion assumption is available. Crude oils and petroleum products differ in density.

For monetary data, document whether values are nominal or inflation-adjusted. Do not interpret nominal expenditure growth as real expenditure growth.

## 4.4 Standardise time periods

Identify whether each series uses:
- Indian financial years, such as FY 2020–21.
- Calendar years.
- Monthly observations.
- Daily observations.

Do not combine financial-year and calendar-year observations as though they represent the same period.

If monthly data must be converted to annual data, document the aggregation method:
- Sum monthly volumes or expenditures when appropriate.
- Calculate an appropriate weighted or arithmetic annual price average, depending on the source and research purpose.
- Do not add monthly stock levels or average quantities without justification.

Keep preliminary and final estimates distinguishable.

## 4.5 Missing values and data quality

For each series:
- Identify missing observations.
- Distinguish a blank from zero.
- Preserve special markers until their meaning is established.
- Detect duplicate periods.
- Detect non-numeric values in numeric columns.
- Flag implausible negative values.
- Check whether units or reporting definitions change.
- Record every transformation.

Never replace missing values with zero automatically.

Do not interpolate missing observations in the primary results without a clear methodological justification and approval.

## 4.6 Data provenance

Create a provenance record for every analytical variable. Each record must specify:

- Variable name.
- Original filename.
- Worksheet.
- Source header.
- Original unit.
- Transformation, if any.
- Final unit.
- Period coverage.
- Missing-data treatment.
- Verification status.

Where practical, retain a source-row identifier for each observation.

## 4.7 Deliverables

Create:

`data/processed/annual_crude_supply.csv`

`data/processed/annual_refinery_processing.csv`

`data/processed/annual_product_production.csv`

`data/processed/annual_product_trade.csv`

`data/processed/annual_product_consumption.csv`

`data/processed/annual_import_values.csv`

`data/processed/crude_basket_price.csv`

`data/processed/data_dictionary.csv`

`outputs/phase_2/data_quality_report.md`

The files listed above are expected outputs where the relevant data exist. If a series is unavailable, record the reason rather than manufacturing a file with invented observations.

## Phase 2 completion gate

Present:
1. The verified period coverage of every major series.
2. Units and definitions.
3. Missing-data issues.
4. Duplicate-resolution decisions.
5. Any incompatible series.
6. The proposed common time window for the primary analysis.

Do not proceed until the researcher approves the data definitions and the common period.

---

# 5. Phase 3 — Build the core annual petroleum supply-chain dataset

## Objective

Create one master dataset linking the major components of India's crude oil supply chain.

The first major analytical output must be a reconciled annual table.

## 5.1 Required variables

Where the source data permit, include:

- Year or financial year.
- Domestic crude oil production.
- Crude oil imports.
- Crude oil exports.
- Net crude oil imports.
- Refinery crude oil processing.
- Apparent crude import dependence.
- Domestic crude production as a share of refinery processing.
- Data-quality flags.
- Source and revision notes.

## 5.2 Core calculations

### A. Net crude oil imports

If imports and exports have compatible coverage and units:

\[
N_t=M_t-X_t
\]

where:
- \(M_t\) = crude oil imports.
- \(X_t\) = crude oil exports.
- \(N_t\) = net crude oil imports.

If exports are not reported, do not automatically assume they are zero. Investigate the source and explain how the measure is handled.

### B. Apparent crude import dependence proxy

A candidate measure is:

\[
D_t=\frac{N_t}{P_t+N_t}\times100
\]

where:
- \(P_t\) = domestic crude oil production.
- \(N_t\) = net crude oil imports.

Use this formula only when the quantities are compatible in units, timing, and coverage.

**Important limitation:** This is a simplified apparent supply-based proxy, not automatically an official import-dependence statistic. It does not fully reconcile refinery inputs, stock changes, losses, exports, or all other supply adjustments. If the official source provides a defined import-dependence measure, compare the official definition with the proxy and report the distinction.

If the data cannot support the formula, do not calculate it.

### C. Domestic production as a share of refinery crude processing

\[
R_t=\frac{P_t}{T_t}\times100
\]

where \(T_t\) is refinery crude processing.

This measures domestic crude production relative to refinery processing, subject to compatible units and timing.

It is not refinery capacity utilisation, and it does not by itself measure the actual crude oil sourced domestically by refineries.

### D. Refinery processing relative to domestic production

\[
Q_t=\frac{T_t}{P_t}
\]

This ratio can be reported descriptively where both series are valid. Explain its interpretation and avoid presenting it as an official supply-chain indicator.

## 5.3 Reconciliation checks

For every year:
- Verify that all variables refer to the same reporting period.
- Confirm compatible units.
- Compare reported imports with available independent official totals.
- Check whether revisions explain differences.
- Flag any series that fail basic consistency checks.
- Document any residual that cannot be explained from the available data.

Do not force different sources to match.

## 5.4 Deliverables

Create:

`data/processed/master_crude_supply_chain.csv`

`outputs/phase_3/annual_supply_chain_table.xlsx`

`outputs/phase_3/reconciliation_report.md`

The annual table must be readable and suitable for later inclusion in the paper.

## Phase 3 completion gate

Present the completed annual table, the definitions of all derived variables, and a list of unresolved discrepancies.

Obtain approval before moving to trend analysis.

---

# 6. Phase 4 — Historical trend and growth analysis

## Objective

Quantify long-term changes in domestic production, imports, processing, consumption, and trade.

## 6.1 Time-series plots

Produce clear, publication-quality plots for:

1. Domestic crude oil production over time.
2. Crude oil imports over time.
3. Net crude oil imports over time.
4. Refinery crude processing over time.
5. Apparent crude import dependence over time, if validly calculated.
6. Domestic production as a share of refinery processing.
7. Petroleum product production over time.
8. Petroleum product consumption over time.
9. Petroleum product imports and exports over time.
10. Petroleum import expenditure over time.
11. Indian crude basket price over time.

Use the common approved period for comparisons. If a chart requires a different period, label it clearly.

Do not create dozens of nearly identical charts. Prioritise plots that answer specific research questions.

## 6.2 Growth calculations

Calculate year-on-year growth when the observations and definitions allow it:

\[
g_t=\left(\frac{X_t}{X_{t-1}}-1\right)\times100
\]

If the previous value is zero or negative, flag the calculation instead of producing misleading percentages.

Calculate compound annual growth rates for selected variables:

\[
CAGR=\left(\frac{X_{\text{end}}}{X_{\text{start}}}\right)^{1/n}-1
\]

Here \(n\) is the number of elapsed annual intervals, not simply the number of rows.

Use CAGR only when its mathematical assumptions and endpoint values are appropriate. If values are zero, negative, or otherwise unsuitable, report an alternative trend measure.

## 6.3 Descriptive statistics

For major variables, report:
- Mean.
- Median.
- Standard deviation.
- Minimum and maximum.
- First and last valid observations.
- Absolute change.
- Percentage change, where valid.
- CAGR, where valid.

Clearly label the period and units for each statistic.

## 6.4 Trend estimation and statistical tests

After inspecting the time series, consider:
- Linear trend estimation.
- Mann–Kendall trend test.
- Sen's slope estimator.

Use these only when appropriate for the data structure.

Document:
- The null hypothesis.
- The test statistic.
- The p-value.
- The slope estimate and its units.
- Any assumptions or limitations.
- Whether autocorrelation or structural breaks may affect interpretation.

Do not treat a statistically significant trend as proof of a causal mechanism.

For a short series or one with major reporting changes, prefer descriptive analysis over unnecessary statistical complexity.

## 6.5 Deliverables

Create:
- A trend-statistics workbook.
- A directory of saved plots.
- A report describing the most important verified trends.
- A table listing each statistical method and why it was used.

Suggested locations:

`outputs/phase_4/figures/`

`outputs/phase_4/trend_statistics.xlsx`

`outputs/phase_4/trend_analysis.md`

## Phase 4 completion gate

Show the charts and descriptive statistics first. Do not draft the results or discussion sections until the researcher has reviewed the trends.

---

# 7. Phase 5 — Petroleum product production, trade and consumption

## Objective

Determine which petroleum products dominate domestic production, consumption, imports, and exports, and assess their historical changes.

## 7.1 Harmonise product categories

Before calculations, create a product-mapping table.

For each source:
- Record the original product name.
- Record the standardised product name.
- Record the source and unit.
- Identify whether the category represents an individual product or an aggregate.
- Identify category changes over time.
- Explain any mapping between different naming conventions.

Do not combine categories just because their names appear similar.

Do not double-count a total and its component products.

## 7.2 Product-level trade balance

For product \(i\) in period \(t\):

\[
B_{i,t}=X_{i,t}-M_{i,t}
\]

where:
- \(X_{i,t}\) = exports.
- \(M_{i,t}\) = imports.

Interpretation:
- Positive values indicate net exports.
- Negative values indicate net imports.
- Zero indicates equal reported imports and exports.

This interpretation is valid only when product definitions, reporting periods, and units match.

Calculate the measure for individual products and, where defensible, for the total petroleum product group.

## 7.3 Apparent product availability balance

A candidate calculation is:

\[
A_{i,t}=Q_{i,t}+M_{i,t}-X_{i,t}-C_{i,t}
\]

where:
- \(Q_{i,t}\) = domestic product production.
- \(M_{i,t}\) = imports.
- \(X_{i,t}\) = exports.
- \(C_{i,t}\) = reported consumption.

This is an apparent balance or reconciliation residual, not a complete physical inventory balance.

It may differ from zero because of inventory changes, refinery own-use, losses, timing differences, processing gains, classification differences, and inconsistent statistical coverage.

Calculate it only if the units and definitions are sufficiently comparable. Investigate substantial residuals and report them honestly.

Do not force the residual to zero or use it as a direct estimate of inventory change unless the source definitions justify that interpretation.

## 7.4 Product ranking

Identify:
- Largest products by domestic production.
- Largest products by consumption.
- Largest products by imports.
- Largest products by exports.
- Products with the largest net import volumes.
- Products with the largest net export volumes.
- Products whose rankings change materially over the available period.

Distinguish rankings by volume from rankings by monetary value.

## 7.5 Charts

Produce:
- Product consumption trend charts for the most relevant products.
- Product trade balance charts.
- Production versus consumption comparisons where compatible.
- A stacked chart of product composition only if categories are exhaustive and mutually exclusive.
- A heatmap or matrix showing net import/export positions across products and years, if it improves interpretation.

Keep the full product-level dataset available even when the paper displays only selected products.

## 7.6 Deliverables

Create:

`data/processed/product_supply_trade_consumption.csv`

`outputs/phase_5/product_balance_table.xlsx`

`outputs/phase_5/product_trade_analysis.md`

`outputs/phase_5/figures/`

## Phase 5 completion gate

Present the product mapping, the key product-level results, and all significant reconciliation limitations. Obtain approval before analysing import expenditure.

---

# 8. Phase 6 — Petroleum import expenditure and price effects

## Objective

Investigate the historical change in India's petroleum import expenditure and distinguish changes associated with import quantities from changes associated with implied unit values.

## 8.1 Verify the value and quantity series

Before any calculations:
- Determine whether the import-value series covers crude oil only, petroleum products, or a broader petroleum category.
- Determine whether the import-quantity series covers the same commodities.
- Confirm the currency, scale, units, and time period.
- Investigate revisions and overlapping extracts.
- Identify whether the Indian crude basket price is a benchmark or an actual transaction price.

Do not divide the total petroleum import bill by crude-only import quantities.

Do not assume that the Indian crude basket price is equal to the actual unit price of all imported crude or petroleum products.

## 8.2 Implied import unit value

If import value is reported in million US dollars and import quantity is reported in thousand metric tonnes, then:

\[
U_t=\frac{V_t}{M_t}\times1000
\]

The resulting unit is US dollars per metric tonne, provided the value and quantity series have matching commodity coverage and periods.

More generally:

\[
\text{Implied unit value}=
\frac{\text{Import expenditure}}{\text{Import quantity}}
\]

The conversion factor depends on the original units.

Label this result as an **implied average import unit value**, not as a spot crude price or a pure market-price measure. It may change because of commodity mix, quality, origin, freight, contract structure, and other factors.

If value and quantity are incompatible, do not calculate the ratio.

## 8.3 Import bill decomposition

If the total import value can reasonably be represented by compatible quantity and unit-value series:

\[
V_t=M_tU_t
\]

For two periods, an exact decomposition is:

\[
\Delta V=U_0\Delta M+M_0\Delta U+\Delta M\Delta U
\]

where:
- \(M_0\) and \(U_0\) are the initial quantity and unit value.
- \(\Delta M\) and \(\Delta U\) are the changes between the two periods.

Report the quantity contribution, unit-value contribution, and interaction term separately.

Do not interpret the decomposition as a causal model. It is an accounting decomposition.

If the commodity scope is not sufficiently consistent, omit the decomposition and explain why.

## 8.4 Indian crude basket price analysis

If the source provides appropriate data:
- Convert the observations into an annual series using a documented method.
- Plot the price trend.
- Compare it with import expenditure and the compatible implied unit value.
- Calculate correlations only where appropriate.
- Examine major divergences descriptively.

Do not attribute import expenditure changes to the benchmark price alone.

## 8.5 Nominal versus real expenditure

The primary expenditure series may be reported in nominal currency.

If a suitable, justified deflator is available and the researcher approves an extension, produce a separate inflation-adjusted series. State the base year and deflator.

If no suitable deflator is available, retain nominal expenditure and explicitly state that inflation adjustment was not performed.

## 8.6 Deliverables

Create:

`data/processed/import_expenditure_analysis.csv`

`outputs/phase_6/import_bill_decomposition.xlsx`

`outputs/phase_6/import_value_analysis.md`

`outputs/phase_6/figures/`

## Phase 6 completion gate

Present the coverage checks, unit-value methodology, expenditure decomposition, and limitations. Do not proceed to external validation until these are reviewed.

---

# 9. Phase 7 — Validation against official reports and independent checks

## Objective

Confirm that the main findings are supported by reliable sources and that any recent estimates are correctly handled.

## 9.1 Validate historical values

Use the supplied official reports to cross-check:
- Recent crude oil production.
- Recent refinery processing.
- Recent petroleum product production.
- Recent petroleum product consumption.
- Recent import and export statistics.
- Recent import expenditure, where reported.

Record the exact report, page, table, reporting period, unit, and whether the value is preliminary, provisional, revised, or final.

Do not cite a report generally when a specific table or page is available.

## 9.2 Resolve discrepancies

If an Excel series and a PDF report differ:
1. Confirm that they measure the same variable.
2. Check their reporting periods.
3. Check units and conversion factors.
4. Check publication dates and revisions.
5. Check whether one is preliminary.
6. Determine whether the discrepancy can be reconciled.
7. Record the decision and preserve the original figures.

Never alter source values simply to make two sources agree.

## 9.3 External sources

External research may be used only when it materially improves the study, for example:
- Establishing official statistical definitions.
- Understanding methodological revisions.
- Confirming the meaning of a reported indicator.
- Locating authoritative historical context.

Prefer primary official sources, such as relevant Indian government petroleum-sector statistics and official statistical publications.

Maintain a separate external-source register containing URLs, publication dates, access dates, and the claims each source supports.

Clearly distinguish:
- Supplied-data findings.
- Findings from additional official sources.
- The researcher's own calculations.
- Interpretations and hypotheses.

Do not use unverified web snippets as substitutes for actual data tables.

## 9.4 Deliverables

Create:

`outputs/phase_7/validation_table.xlsx`

`outputs/phase_7/source_register.csv`

`outputs/phase_7/discrepancy_log.md`

## Phase 7 completion gate

Present the validation results and unresolved discrepancies. Obtain approval before testing relationships between variables.

---

# 10. Phase 8 — Relationships, robustness and additional analysis

## Objective

Investigate whether the verified series exhibit meaningful relationships and determine whether the results are robust to reasonable methodological choices.

Do not begin this phase before the core dataset and descriptive trends have been approved.

## 10.1 Potential relationships

Depending on data availability, examine:
- Domestic crude production versus refinery processing.
- Net crude imports versus refinery processing.
- Product production versus reported product consumption.
- Product imports and exports versus domestic product consumption.
- Import expenditure versus import quantity.
- Import expenditure versus implied import unit value.
- Implied import unit value versus the Indian crude basket price, where commodity coverage permits comparison.

Use scatterplots and time-series plots before fitting models.

## 10.2 Correlation analysis

Calculate Pearson or Spearman correlations only where meaningful.

For each reported correlation:
- State the variables.
- State the sample period.
- Report the number of observations.
- Explain the correlation method.
- Report the coefficient.
- Report uncertainty or statistical significance where appropriate.
- Discuss possible confounding factors and common time trends.

A correlation between two upward-trending series can be misleading. Do not interpret a high correlation as proof that one variable causes the other.

## 10.3 Regression analysis

Regression is optional, not compulsory.

Consider a regression only if:
- A clear research question motivates it.
- There are enough observations.
- Variable definitions and periods are consistent.
- The model specification has a defensible rationale.
- The assumptions and limitations can be assessed.

For time-series models, consider trend effects, serial correlation, structural breaks, non-stationarity, and small sample size.

Do not use complex models merely to make the paper appear sophisticated.

## 10.4 Robustness checks

Possible checks include:
- Repeating the analysis over a shorter common period.
- Comparing the result using alternative verified source versions.
- Excluding a preliminary or revised observation where justified.
- Comparing calendar-year and financial-year analyses only when each can be constructed correctly.
- Comparing alternative definitions of import dependence, if authoritative data support them.

Do not cherry-pick the time window or methodology that produces the most dramatic result.

## 10.5 Deliverables

Create:

`outputs/phase_8/relationship_analysis.md`

`outputs/phase_8/robustness_checks.xlsx`

`outputs/phase_8/figures/`

The report must distinguish descriptive association, statistical evidence, and causal interpretation.

## Phase 8 completion gate

Present the proposed results, robustness checks, and limitations. Obtain approval before writing the full paper.

---

# 11. Phase 9 — Research-paper development

## Objective

Turn the verified analysis into a coherent research paper.

Do not start writing the full paper during the initial data-cleaning phases. The paper must reflect actual results, not predetermined expectations.

## 11.1 Proposed structure

### 1. Title

Use the approved working title or a more precise title justified by the final analysis.

### 2. Abstract

Write only after the analysis is complete.

Include:
- Research objective.
- Data sources and period.
- Methods.
- Principal numerical findings.
- Main conclusion.
- Important limitation.

Do not insert placeholder statistics or generic claims.

### 3. Introduction

Explain:
- Why India's petroleum supply chain is an important subject of study.
- Why domestic production, refinery processing, petroleum product trade, and consumption should be examined together.
- The precise research questions.
- The scope and contribution of the study.

Support contextual claims with reliable sources.

### 4. Literature review

Review relevant studies and official publications on:
- India's crude oil import dependence.
- Domestic crude oil production and supply.
- Refining and petroleum product trade.
- Petroleum product consumption.
- Petroleum import expenditure and price exposure.

Use genuine, verifiable references. Never invent authors, paper titles, journals, DOIs, or publication dates.

Identify a research gap only after reviewing the relevant literature.

### 5. Data and methodology

Document:
- Source files and institutions.
- Time coverage.
- Definitions and units.
- Data-cleaning procedures.
- Duplicate resolution.
- Treatment of missing values.
- Derived variables.
- Statistical methods.
- Reconciliation procedures.
- Limitations.

Every formula must match the actual implemented code.

### 6. Results

Present the verified numerical results in a logical order:
1. Domestic crude production and import dependence.
2. Refinery processing and the crude supply relationship.
3. Petroleum product production, consumption, and trade.
4. Import expenditure and unit-value analysis.
5. Additional relationships and robustness checks, if justified.

Use numbered tables and figures. Explain what each one shows without repeating every number in the caption and paragraph.

### 7. Discussion

Interpret the findings in relation to:
- Domestic production relative to refinery requirements.
- Crude supply exposure.
- Product-specific import and export positions.
- Consumption trends.
- Import expenditure and unit-value changes.
- Comparison with verified official sources and relevant literature.

Distinguish the evidence from possible explanations.

### 8. Limitations

Explicitly discuss relevant limitations, such as:
- Incomplete or inconsistent historical coverage.
- Revisions to official statistics.
- Differences between financial years and calendar years.
- Differences in commodity definitions.
- Missing inventory or stock-change information.
- Limitations of simplified import-dependence measures.
- The difference between implied unit values and market prices.
- The limits of correlational analysis.

Include only limitations that actually apply, but do not omit material limitations simply because they weaken a result.

### 9. Conclusion

Answer the original research questions using the verified results.

Do not introduce new data or unsupported claims.

### 10. References and appendices

Include:
- Complete, verifiable references.
- Source-data notes.
- Supplementary tables.
- Definitions and formulas.
- Additional figures where useful.
- A reproducibility statement.

## 11.2 Deliverables

Create:

`paper/research_paper_draft.md`

`paper/tables/`

`paper/figures/`

`paper/references.md`

`paper/limitations_and_future_work.md`

A Word or PDF version may be generated after the researcher approves the draft.

## Phase 9 completion gate

Provide the complete draft with a table-to-source map, figure-to-data map, references, and a list of claims requiring further verification.

---

# 12. Phase 10 — Reproducibility, quality assurance and final handover

## Objective

Ensure the project can be rerun, audited, and extended without depending on undocumented manual operations.

## 12.1 Recommended project structure

Use this structure, adapting it only when necessary:

```text
petroleum_supply_chain_research/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── original/
│   ├── raw_extracted/
│   └── processed/
│
├── notebooks/
│   ├── 01_source_audit.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_core_supply_chain.ipynb
│   ├── 04_trend_analysis.ipynb
│   ├── 05_product_trade.ipynb
│   ├── 06_import_expenditure.ipynb
│   ├── 07_validation_and_robustness.ipynb
│   └── 08_final_results.ipynb
│
├── src/
│   ├── inventory.py
│   ├── extract_data.py
│   ├── clean_data.py
│   ├── build_supply_chain.py
│   ├── trend_analysis.py
│   ├── product_trade.py
│   ├── import_expenditure.py
│   └── validation.py
│
├── outputs/
│   ├── phase_1/
│   ├── phase_2/
│   ├── phase_3/
│   ├── phase_4/
│   ├── phase_5/
│   ├── phase_6/
│   ├── phase_7/
│   └── phase_8/
│
├── paper/
│   ├── tables/
│   ├── figures/
│   ├── research_paper_draft.md
│   └── references.md
│
└── logs/
    ├── processing_log.md
    └── data_issues.csv
```

Do not duplicate large original workbooks unnecessarily. If the files are already in a separate source directory, reference them there and document the path.

## 12.2 Reproducibility requirements

- Use Python and suitable data-analysis libraries where practical.
- Make transformations explicit in code.
- Save figures at publication-quality resolution.
- Use descriptive figure and table names.
- Set random seeds if any randomised method is used.
- Record library versions.
- Avoid hard-coded paths that break when the project moves.
- Make scripts fail visibly when required variables are missing.
- Validate outputs against source totals where possible.
- Keep logs of warnings and exceptions.
- Separate exploratory analysis from the final, reproducible pipeline.

## 12.3 Final quality-assurance checklist

Before declaring the project complete, verify:

1. Every reported number is traceable to source data or code.
2. All units are clearly stated.
3. All reporting periods are correctly labelled.
4. Duplicate sources have been resolved transparently.
5. Missing values have not been silently replaced.
6. Every formula has been checked.
7. No product totals double-count component categories.
8. No incompatible series have been combined.
9. Preliminary figures are clearly labelled.
10. Figures and tables agree with the underlying data.
11. All citations support the claims they accompany.
12. All references are real and verifiable.
13. Limitations are disclosed.
14. The final pipeline can be rerun from the documented instructions.

---

# 13. Mandatory operating instructions for Antigravity

These instructions apply to every phase.

## 13.1 Work in small, controlled stages

Execute only one phase at a time.

At the beginning of a phase, state:
- Its objective.
- The files and sheets being used.
- The intended calculations.
- The expected outputs.
- The unresolved questions.

At the end, state:
- What was completed.
- What files were created.
- What was verified.
- What remains uncertain.
- Whether the completion gate has been met.

Stop at the gate and request researcher approval before starting the next phase.

Do not interpret permission to access all workbooks as permission to analyse everything at once.

## 13.2 Do not hallucinate

If a sheet cannot be read, report the error.

If a variable is missing, say it is missing.

If two sources conflict, flag the conflict.

If a calculation cannot be justified, do not perform it.

If a proposed statistical test is unsuitable, explain why and recommend a simpler alternative.

If the data do not support a research question, state that the question cannot currently be answered.

Never fabricate results to complete a table or meet a deadline.

## 13.3 Keep research decisions visible

Maintain a decision log covering:
- Source selection.
- Duplicate resolution.
- Unit conversion.
- Time-period alignment.
- Missing-data handling.
- Variable definitions.
- Statistical-method selection.
- Exclusions.
- Revisions to the research scope.

For each material decision, record the rationale and its effect on the results.

## 13.4 Do not overstate conclusions

Avoid unsupported statements such as:
- “India's import dependence is increasing” before calculating the relevant measure.
- “Oil prices caused the import bill to rise” based solely on a correlation.
- “Refinery utilisation increased” when only throughput is available.
- “Domestic production meets a particular percentage of demand” when the denominator is incompatible.
- “The study proves energy security has deteriorated” based solely on an import ratio.

Use precise wording that reflects the actual measure.

## 13.5 Do not overcomplicate the paper

The primary goal is a credible, well-executed study, not the maximum number of algorithms, regressions, or charts.

Prioritise:
1. Accurate data.
2. Defensible definitions.
3. Clear historical analysis.
4. Reproducible calculations.
5. Meaningful findings.
6. Transparent limitations.

Use advanced statistical methods only when they answer a real research question and the available observations support them.

---

# 14. Initial instruction: execute Phase 1 only

**Start now with Phase 1 and do not proceed to Phase 2.**

Inspect all accessible supplied Excel workbooks and PDFs. Use the exact filenames and actual worksheet contents to create the source inventory, identify the core datasets, investigate duplicates, and determine which files are relevant to the approved primary study.

Return the following:

1. Complete inventory of all accessible source files.
2. Worksheet-level inventory for each Excel workbook.
3. Verified data coverage, units, frequency, and source definitions for the core candidate datasets.
4. Duplicate and overlap findings.
5. A mapping from each research question to its candidate source workbook and worksheet.
6. A list of missing variables, incompatible periods, and unresolved issues.
7. A recommendation for the most defensible historical period for the primary study.
8. The Phase 1 output files and a concise audit report.
9. A list of decisions requiring the researcher's approval.

Do not calculate final trends, run regressions, or draft the paper at this stage.

If a file cannot be accessed or a worksheet cannot be interpreted, explicitly identify it and explain the limitation.

**Wait for approval after Phase 1.**
