"""
compile_manuscript.py
Builds the complete Word DOCX and PDF manuscripts using verified data.
"""

import os, sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak, HRFlowable
)

from manuscript_engine import (
    DOCX_PATH, PDF_PATH,
    add_h1, add_h2, add_h3, add_body, add_caption,
    format_docx_table, NumberedCanvas
)

print("Starting manuscript compilation...")

doc = Document()

# Configure standard margins (1 inch)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Set base Normal style font
style_normal = doc.styles['Normal']
style_normal.font.name = 'Times New Roman'
style_normal.font.size = Pt(10.5)
style_normal.font.color.rgb = RGBColor(35, 35, 35)

# -----------------------------------------------------------------------------
# TITLE & AUTHOR METADATA
# -----------------------------------------------------------------------------
p_title = doc.add_paragraph()
p_title.paragraph_format.space_before = Pt(24)
p_title.paragraph_format.space_after = Pt(12)
p_title.paragraph_format.line_spacing = 1.2
run_title = p_title.add_run(
    "India's Petroleum Supply Chain and Import Exposure:\nA Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption"
)
run_title.font.name = "Times New Roman"
run_title.font.size = Pt(19)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(15, 34, 64)

p_auth = doc.add_paragraph()
p_auth.paragraph_format.space_after = Pt(4)
run_auth = p_auth.add_run("[AUTHOR_NAME_PLACEHOLDER]")
run_auth.font.bold = True
run_auth.font.size = Pt(11.5)

p_aff = doc.add_paragraph()
p_aff.paragraph_format.space_after = Pt(4)
run_aff = p_aff.add_run("[INSTITUTION_PLACEHOLDER] | [DEPARTMENT_PLACEHOLDER]")
run_aff.font.italic = True
run_aff.font.size = Pt(10)

p_cor = doc.add_paragraph()
p_cor.paragraph_format.space_after = Pt(18)
run_cor = p_cor.add_run("Corresponding Author: [EMAIL_PLACEHOLDER] | ORCID: [ORCID_PLACEHOLDER]")
run_cor.font.size = Pt(9.5)
run_cor.font.color.rgb = RGBColor(90, 90, 90)

# Horizontal divider
p_div = doc.add_paragraph()
p_div.paragraph_format.space_after = Pt(14)
run_div = p_div.add_run("―" * 58)
run_div.font.color.rgb = RGBColor(180, 180, 180)

# -----------------------------------------------------------------------------
# 1. ABSTRACT
# -----------------------------------------------------------------------------
add_h1(doc, "1. Abstract")

abstract_text = (
    "This study conducts a rigorous empirical investigation into India's petroleum supply chain across 26 continuous financial years "
    "(FY 1998–99 to FY 2023–24), evaluating the structural relationships among domestic upstream crude oil extraction, refinery throughput, "
    "downstream product trade, and foreign exchange import expenditure. Using official administrative time series from the Petroleum Planning "
    "and Analysis Cell (PPAC), the Ministry of Petroleum and Natural Gas (MoPNG), and the Reserve Bank of India (RBI), the analysis resolves "
    "a central structural paradox in India's energy economy: the simultaneous escalation of crude oil import dependency from 58.1% to 89.6% "
    "alongside the country's emergence as a major net exporter of refined petroleum products (+13.90 MMT in FY 2023–24). Ordinary least squares "
    "regressions with Newey-West (1987) heteroskedasticity and autocorrelation consistent (HAC) standard errors reveal that domestic crude production "
    "flatlined over the study period (contracting at a compound annual growth rate of −0.44%, from 32.76 MMT to 29.36 MMT) and exhibits zero "
    "unconditional statistical association with crude oil imports in both levels (p = 0.740) and first differences (p = 0.446). Instead, crude "
    "import surges (+7.35% CAGR, reaching 234.26 MMT) were overwhelmingly pulled by a 281.6% expansion in domestic refining throughput "
    "(68.54 MMT to 261.55 MMT), with each annual increment in refinery runs drawing approximately 0.941 MMT of crude imports (p < 0.0001, R² = 0.938). "
    "Furthermore, disaggregated product-level balances show that while India maintains massive export surpluses in transport fuels (High-Speed Diesel "
    "coverage of 129.4% and Aviation Turbine Fuel coverage of 207.6%), welfare-driven domestic policies have generated severe import lock-in for clean "
    "cooking fuels, with Liquefied Petroleum Gas (LPG) coverage falling to 43.1% (60.6% net import reliance). Compounding international crude price shocks "
    "and a secular currency depreciation wedge expanded the nominal crude import bill by 37.9-fold in US dollars and 74.1-fold in Indian rupees. "
    "These findings indicate that national petroleum vulnerability has not been driven by domestic extraction stagnation, but by downstream refining "
    "architecture and product-specific deficits, underscoring that upstream licensing reforms alone cannot mitigate India's import exposure without "
    "targeted clean cooking electrification and transport fuel substitution."
)
add_body(doc, abstract_text, space_after=10)

p_kw = doc.add_paragraph()
p_kw.paragraph_format.space_after = Pt(18)
run_kw_lbl = p_kw.add_run("Keywords: ")
run_kw_lbl.font.bold = True
run_kw_lbl.font.size = Pt(10)
run_kw_val = p_kw.add_run("Petroleum supply chain; crude oil import dependence; refinery throughput; LPG import exposure; energy security; Newey-West econometrics; India.")
run_kw_val.font.italic = True
run_kw_val.font.size = Pt(10)

# -----------------------------------------------------------------------------
# 2. INTRODUCTION
# -----------------------------------------------------------------------------
add_h1(doc, "2. Introduction")

add_h2(doc, "2.1 Context and Global Energy Security Paradigms")
add_body(doc, 
    "Energy security is fundamentally multi-dimensional, spanning availability, accessibility, affordability, and acceptability "
    "(Ang, Choong, & Ng, 2015). In classical energy economics, national exposure to international hydrocarbon markets has conventionally "
    "been quantified using scalar physical import-dependency ratios—primarily the ratio of net crude oil imports to domestic consumption "
    "(Kruyt, van Vuuren, de Vries, & Groenenberg, 2009). However, cross-country comparative studies establish that simple aggregate import "
    "metrics fail to capture systemic vulnerabilities related to supply diversity, refining bottlenecks, and macroeconomic balance-of-payments "
    "pressures (Vivoda, 2010). Among developing net oil-importing nations, India has consistently ranked among the most structurally exposed economies "
    "due to its high hydrocarbon intensity, low per-capita income, and substantial import bill fiscal burden (Gupta, 2008)."
)
add_body(doc,
    "As emerging market economies industrialize, rapid urbanization and transport motorization inevitably trigger accelerating petroleum product demand "
    "(Dash, Sethi, & Bal, 2018; Mallick & Agarwal, 2014). To mitigate external supply disruptions, conventional energy security doctrine advocates for "
    "domestic upstream exploration and field development. However, where geological realities and maturing sedimentary basins constrain domestic extraction, "
    "import exposure undergoes complex structural transformations across upstream, midstream, and downstream tiers (Mishra, Ghosh, & Kanjilal, 2023)."
)

add_h2(doc, "2.2 The Indian Hydrocarbon Landscape: Upstream Realities vs. Downstream Ambitions")
add_body(doc,
    "India's petroleum sector presents a striking structural dichotomy. On the upstream extraction front, domestic crude oil production has remained "
    "substantially stagnant for three decades, oscillating within a narrow band of 29 to 38 million metric tonnes (MMT) per annum despite successive rounds "
    "of exploratory licensing under the New Exploration Licensing Policy (NELP) and the Hydrocarbon Exploration and Licensing Policy (HELP) "
    "(Bhattacharyya, 2010). Natural field decline across mature offshore basins, particularly ONGC's Mumbai High, coupled with technical challenges in "
    "complex deepwater and onshore frontier plays, has effectively decoupled domestic extraction from national economic growth (Mishra et al., 2023)."
)
add_body(doc,
    "Conversely, India's downstream refining sector experienced an unprecedented state-facilitated structural transformation following the liberalization "
    "measures of 1998 (Dixit, 2020). Through policy incentives permitting tariff-free capital imports, domestic refinery deregulation, and the establishment "
    "of export-oriented Special Economic Zones (SEZs), India attracted massive private capital into mega-refining infrastructure—most prominently "
    "Reliance Industries Limited's Jamnagar refining complex and Nayara Energy's Vadinar refinery in Gujarat. Consequently, India rapidly transitioned "
    "from a deficit refined-product importer into an export-oriented merchant refining hub for the Indian Ocean basin and GCC markets (Azhar, 2011; "
    "Sarmah & Bal, 2021). National crude distillation capacity expanded to over 256 MMT per annum, propelling actual domestic refinery crude throughput "
    "from 68.54 MMT in FY 1998–99 to 261.55 MMT in FY 2023–24."
)

add_h2(doc, "2.3 The \"Triple Paradox\" of India's Petroleum Sector")
add_body(doc,
    "This asymmetric sectoral trajectory has generated what this paper formalizes as the \"Triple Paradox\" of India's petroleum supply chain:"
)
add_body(doc,
    "1. The Upstream Decoupling Paradox: While national economic output and refining capacity expanded by multiple orders of magnitude, domestic "
    "crude extraction remained completely stagnant, causing the crude oil import dependency ratio to climb from 58.1% to 89.6%. Policymakers frequently "
    "assert that stagnant domestic production \"drove\" rising imports; yet, whether domestic extraction actually exerted any crowding-out or mitigating "
    "effect on imports remains an unverified empirical question."
)
add_body(doc,
    "2. The Refining Surplus vs. Clean Cooking Deficit Paradox: Since FY 2001–02, India has been a continuous net exporter of refined petroleum products "
    "in aggregate volume, exporting 62.59 MMT against 48.69 MMT of product imports in FY 2023–24 (+13.90 MMT net export balance). However, this aggregate "
    "surplus is heavily skewed toward middle and light transport distillates (High-Speed Diesel and Aviation Turbine Fuel), masking an acute domestic supply "
    "deficit in Liquefied Petroleum Gas (LPG). Driven by the massive welfare success of the Pradhan Mantri Ujjwala Yojana (PMUY), household clean cooking "
    "gas adoption expanded exponentially (Kar, Pachauri, Bailis, & Zerriffi, 2019; Gill-Wiehl, Brown, & Smith, 2022; Gould & Urpelainen, 2018), while "
    "subsidized kerosene was systematically curtailed (Rao, 2012; Jain, 2018; Acharya & Sadath, 2017). Because refinery crude distillation yield configurations "
    "structurally produce only 4.5% to 5.0% LPG (de la Rue du Can, Pudleiner, Jones, & Khanna, 2019), domestic LPG coverage collapsed to 43.1%, locking the nation "
    "into extreme foreign import reliance (60.6% net import dependence in FY 2023–24)."
)
add_body(doc,
    "3. The Compounding Financial Exposure Paradox: Physical crude import volumes grew 5.9-fold over the 26-year study period. Yet, India's nominal crude "
    "import bill escalated 37.9-fold in US dollars and 74.1-fold in Indian rupees. This explosive financial magnification reflects the compounding interaction "
    "between cyclical international oil price shocks (Kumar, 2011; Tiwari & Albulescu, 2016) and a relentless secular rupee depreciation wedge against "
    "the dollar (Kanjilal & Ghosh, 2018; Agrawal & Sinha, 2022)."
)

add_h2(doc, "2.4 Research Gap and Contribution")
add_body(doc,
    "Although extensive scholarship examines individual facets of India's energy sector—such as energy-GDP causality (Dash et al., 2018), "
    "crude import demand elasticity (Ghosh, 2009), pricing deregulation (Agrawal & Sinha, 2022), household clean cooking access (Kar et al., 2019), "
    "and commodity price instability (Shalu, Singh, Kaur, & Sikka, 2023)—the literature exhibits critical gaps. Existing studies rarely integrate the full "
    "interlocking physical supply chain (domestic crude, imports, refinery throughput, product manufacturing, and product-specific consumption) with "
    "monetary trade balances over multi-decade periods using verified administrative data. Most macroeconomic analyses either treat petroleum as a homogenous "
    "liquid aggregate or assume that upstream extraction directly displaces crude imports without testing the underlying econometric mechanism."
)
add_body(doc,
    "This study bridges these gaps by providing the first comprehensive, 26-year empirical supply-chain audit of India's petroleum sector from FY 1998–99 to "
    "FY 2023–24. The study formalizes physical mass balances, evaluates rigorous time-series regressions using Newey-West (1987) HAC standard errors, "
    "disaggregates product-level coverage ratios across 12 distinct product categories, and quantifies financial magnification drivers."
)

add_h2(doc, "2.5 Research Questions")
add_body(doc,
    "This investigation addresses five central research questions:\n"
    "• RQ1: How has domestic crude oil production evolved over 1998–2024, and does empirical evidence support the hypothesis that stagnant domestic extraction drove crude import growth?\n"
    "• RQ2: What is the precise statistical relationship between domestic refinery throughput expansion and crude oil import requirements?\n"
    "• RQ3: How has India's refined petroleum product trade balance evolved, and what structural asymmetries exist behind the aggregate product export surplus?\n"
    "• RQ4: What factors explain the acute divergence between transport fuel self-sufficiency and structural LPG import vulnerability?\n"
    "• RQ5: How have global crude oil price shocks and currency depreciation interacted to magnify India's financial petroleum import bill relative to physical volume growth?"
)

# -----------------------------------------------------------------------------
# 3. METHOD
# -----------------------------------------------------------------------------
add_h1(doc, "3. Method")

add_h2(doc, "3.1 Data Sources, Compilation Hierarchy, and Study Period")
add_body(doc,
    "This study relies exclusively on official, primary administrative data compiled by statutory government bodies under the Ministry of Petroleum and "
    "Natural Gas (MoPNG), Government of India. The primary analytical baseline is drawn from historical time-series registers maintained by the Petroleum "
    "Planning & Analysis Cell (PPAC), specifically:\n"
    "1. Annual Crude Oil Production Series (1998–99 to 2023–24);\n"
    "2. Annual Petroleum Trade Returns (Crude Oil and Product Import/Export Quantities and Values, 1998–99 to 2023–24);\n"
    "3. Annual Refinery Crude Processing Series (throughout across 23 public, private, and joint-venture refineries);\n"
    "4. Annual Petroleum Product Production and Consumption Returns by Product Category;\n"
    "5. The Indian Crude Basket FOB Price Series and RBI reference exchange rates."
)
add_body(doc,
    "The core annual dataset spans 26 continuous financial years (April 1, 1998 to March 31, 2024). All physical flows are measured in Million Metric Tonnes "
    "(MMT) or Thousand Metric Tonnes (TMT), and monetary flows are recorded in Million US Dollars (USD M) and Crore Indian Rupees (INR Cr). The canonical "
    "standardized dataset (`core_annual_petroleum_dataset.csv`, SHA-256: `9fb5e64c4d0e3402f979f7e83269b0a41034c8530e54fba2fdbd6895b98634ca`) was audited "
    "and frozen prior to model estimation to ensure total computational reproducibility."
)

add_h2(doc, "3.2 Variable Definitions and Unit Standardization")
add_body(doc,
    "The primary variables evaluated across the 26-year study period are defined as follows:\n"
    "• P_c,t: Domestic crude oil production (indigenous extraction from ONGC, OIL, and Private/JV PSC blocks), in MMT.\n"
    "• M_c,t: Gross imports of crude petroleum into Indian ports and refinery marine terminals, in MMT.\n"
    "• X_c,t: Exports of crude petroleum (unobserved in trade returns; statutory zero under Foreign Trade Policy ITC-HS 2709).\n"
    "• R_t: Refinery crude throughput (total volume of crude petroleum processed through atmospheric and vacuum distillation units), in MMT.\n"
    "• Q_p,t: Gross domestic production of refined petroleum products across all operating domestic refineries, in MMT.\n"
    "• C_p,t: Total domestic consumption of refined petroleum products (sales through public marketing companies and private retail networks), in MMT.\n"
    "• M_p,t and X_p,t: Gross imports and gross exports of refined petroleum products, respectively, in MMT."
)

add_h2(doc, "3.3 Physical Mass Balance and Accounting Residual")
add_body(doc,
    "The upstream physical mass balance governing refinery feedstock availability is given by:\n"
    "A_c,t = M_c,t + P_c,t − X_c,t = R_t + ΔS_c,t + L_c,t\n"
    "where ΔS_c,t represents net changes in commercial crude inventories, pipeline line-pack, and Strategic Petroleum Reserves (ISPRL), "
    "and L_c,t represents handling and ocean transit evaporation losses. Official trade records published by PPAC (`PT_IMPORT_TMT_H.xlsx`) contain "
    "an export schedule titled exclusively \"PRODUCT EXPORT @\", confirming that India does not record commercial crude petroleum exports. Under statutory "
    "allocation rules administered by MoPNG, all indigenous crude is mandatorily allocated to domestic refiners. Setting X_c,t = 0, the Conditional "
    "Crude Accounting Residual is defined as:\n"
    "Res_c,t^cond = M_c,t + P_c,t − R_t\n"
    "Across the 26-year period, this residual averages +4.512 MMT per annum (std: 1.357 MMT), consistently absorbing strategic cavern filling, pipeline expansion, "
    "and terminal inventories without violating mass conservation."
)

add_h2(doc, "3.4 Growth, Elasticity, and Structural Indicators")
add_body(doc,
    "Compound Annual Growth Rates (CAGR) across n = 25 elapsed annual periods are computed as:\n"
    "CAGR = (X_t_k / X_t_0)^(1/n) − 1\n"
    "Upstream structural import exposure is measured via the Crude Oil Import Dependency Ratio (CID_t) and the Physical Deficit Gap (Gap_t):\n"
    "CID_t = (M_c,t / R_t) × 100,      Gap_t = R_t − P_c,t\n"
    "Downstream production adequacy is quantified using the Aggregate Product Coverage Ratio (PCR_agg,t):\n"
    "PCR_agg,t = (Q_p,t / C_p,t) × 100"
)

add_h2(doc, "3.5 Econometric Specifications and Covariance Estimation")
add_body(doc,
    "To evaluate the structural determinants of crude imports, we specify both bivariate and multivariate regression models across levels, logs, and first differences:\n"
    "• MOD-03 (Bivariate Levels): M_c,t = β_0 + β_1 P_c,t + ε_t\n"
    "• MOD-04 (Bivariate Log-Log): ln(M_c,t) = β_0 + β_1 ln(P_c,t) + ε_t\n"
    "• MOD-05 (Multivariate Levels): M_c,t = β_0 + β_1 R_t + β_2 P_c,t + ε_t\n"
    "• MOD-07 (Bivariate First Differences): ΔM_c,t = β_0 + β_1 ΔR_t + ε_t\n"
    "• MOD-08 (Bivariate First Differences): ΔM_c,t = β_0 + β_1 ΔP_c,t + ε_t\n"
    "• MOD-05-FD (Multivariate First Differences): ΔM_c,t = β_0 + β_1 ΔR_t + β_2 ΔP_c,t + ε_t\n"
    "• MOD-01 (Multivariate Log-Log): ln(M_c,t) = β_0 + β_1 ln(R_t) + β_2 ln(P_c,t) + ε_t"
)
add_body(doc,
    "Because macroeconomic time series frequently exhibit serial correlation and heteroskedasticity, standard OLS variance estimators are biased. All models "
    "are estimated using the Newey-West (1987) HAC covariance estimator with a Bartlett (triangular) kernel. The maximum lag truncation parameter is set "
    "in accordance with the standard rule-of-thumb: L = floor(4 × (n/100)^(2/9)), yielding L = 2 for both n = 26 and n = 25. Hypothesis testing and p-values "
    "are computed using the conservative two-tailed Student's t-distribution with finite-sample degrees of freedom df = n − k (where k is the number of estimated parameters including the intercept). "
    "Variance Inflation Factors (VIF) and Durbin-Watson (DW) statistics are evaluated for all specifications."
)

add_h2(doc, "3.6 Product-Level Disaggregation and Asymmetry Metrics")
add_body(doc,
    "To analyze downstream supply heterogeneity, we calculate product-specific coverage ratios (PCR_i) and net trade balances for 12 standardized categories in FY 2023–24:\n"
    "PCR_i = (Q_p,i / C_p,i) × 100,      Net_i = X_p,i − M_p,i\n"
    "Net import reliance for deficit products (such as LPG) is defined as:\n"
    "NIR_i = [(M_p,i − X_p,i) / C_p,i] × 100"
)

add_h2(doc, "3.7 Import Value, Price Shocks, and Currency Translation")
add_body(doc,
    "Nominal crude import expenditure is tracked in both US dollars (V_USD,t) and Indian rupees (V_INR,t). The implied annual transaction exchange rate "
    "(IER_t, INR/USD) is derived from matched administrative customs returns:\n"
    "IER_t = (V_INR,t × 10) / V_USD,t\n"
    "This series is cross-verified against the official Reserve Bank of India annual financial market reference rate."
)

add_h2(doc, "3.8 Index Decomposition Analysis Framework")
add_body(doc,
    "To separate the contributions of physical volume, international price, and currency movements, import expenditure is factorized as:\n"
    "V_INR,t = M_c,t × P_USD,t × IER_t\n"
    "where P_USD,t is the derived import unit value ($/MT). Following Ang (2004, 2015), the Logarithmic Mean Divisia Index (LMDI-I) is utilized due to "
    "its perfect decomposition property (zero residual) and aggregation consistency."
)

add_h2(doc, "3.9 Methodological Disclosures, Stationarity Caveats, and Limitations")
add_body(doc,
    "We explicitly disclose four methodological boundaries:\n"
    "1. Non-Causal Interpretation: Observational regressions establish statistical associations and accounting substitution mechanisms, not causal market impacts.\n"
    "2. Stationarity and Small-Sample Caveat: Augmented Dickey-Fuller tests reject unit roots for first-differenced series (ΔM_c, ΔR, ΔP_c at p < 0.01), "
    "confirming that differencing effectively removes secular trend bias. However, with T = 25 observations, unit-root tests possess limited power, and differenced "
    "models are interpreted as robust representations of short-run incremental relationships rather than proofs of asymptotic covariance stationarity.\n"
    "3. Conditional Residual: The crude material balance residual is conditional on the statutory zero-crude-export reporting regime.\n"
    "4. Refinery Assays: Volumetric refining gains (~5.55%) and individual refinery fuel-and-loss fractions (~8–9%) are sector-wide averages; plant-level crude slate optimizations remain proprietary."
)

# -----------------------------------------------------------------------------
# 4. RESULTS
# -----------------------------------------------------------------------------
add_h1(doc, "4. Result")

add_h2(doc, "4.1 Long-Run Evolution of India's Petroleum Supply Chain (FY99–FY24)")
add_body(doc,
    "Over the 26-year study period from FY 1998–99 to FY 2023–24, India's petroleum supply chain underwent an unprecedented structural transformation. "
    "Table 1 synthesizes the headline physical and structural indicators at decadal benchmarks."
)

add_caption(doc, "Table 1: Summary Statistics of India's Petroleum Supply Chain (FY 1998–99 to FY 2023–24)")
t1_headers = ["Indicator / Variable", "FY 1998–99", "FY 2010–11", "FY 2023–24", "CAGR (%)", "Total Change"]
t1_data = [
    ["Domestic Crude Production (P, MMT)", "32.760", "37.694", "29.356", "−0.44%", "−10.39%"],
    ["Crude Oil Imports (M, MMT)", "39.808", "163.595", "234.262", "+7.35%", "+488.48%"],
    ["Refinery Crude Throughput (R, MMT)", "68.539", "196.485", "261.546", "+5.50%", "+281.60%"],
    ["Petroleum Product Production (Q, MMT)", "68.409", "196.171", "276.058", "+5.74%", "+303.54%"],
    ["Petroleum Product Consumption (C, MMT)", "84.759", "141.040", "234.259", "+4.15%", "+176.38%"],
    ["Crude Oil Import Dependency (M/R, %)", "58.08%", "83.26%", "89.57%", "+1.74%", "+31.49 pp"],
    ["Upstream Physical Deficit Gap (R − P, MMT)", "35.779", "158.791", "232.190", "+7.78%", "+548.96%"],
    ["Product Coverage Ratio (Q/C, %)", "80.71%", "139.09%", "117.84%", "+1.53%", "+37.13 pp"]
]
format_docx_table(doc, t1_headers, t1_data, col_widths=[2.4, 0.8, 0.8, 0.8, 0.8, 0.9])

add_body(doc,
    "As documented in Table 1, domestic crude extraction peaked at 38.08 MMT in FY 2011–12 before entering a secular decline to 29.36 MMT in FY 2023–24, "
    "yielding an overall CAGR of −0.44%. In stark contrast, refinery throughput expanded by 281.60% (from 68.54 MMT to 261.55 MMT, CAGR +5.50%), "
    "vastly outstripping domestic extraction. Consequently, the upstream feedstock deficit gap (R − P) expanded by 548.96%, surging from 35.78 MMT to 232.19 MMT. "
    "This deficit was covered almost exclusively by imported crude, driving crude imports from 39.81 MMT to 234.26 MMT (CAGR +7.35%) and raising crude import "
    "dependency from 58.08% to 89.57%."
)

add_h2(doc, "4.2 Upstream Decoupling: Stagnant Domestic Production vs. Surging Imports")
add_body(doc,
    "A widely held policy assertion is that stagnant domestic production directly \"caused\" or \"crowded in\" crude imports. To formally test whether "
    "domestic production exerted an unconditional crowding-out effect on imports, Table 2 presents the bivariate regression results in both levels and first differences."
)

add_caption(doc, "Table 2: Regression Results: Unconditional Domestic Production–Import Relationship")
t2_headers = ["Model ID", "Specification", "Regressor", "Coeff (β)", "Conv SE", "HAC SE", "HAC t-stat", "p-value", "R²", "DW"]
t2_data = [
    ["MOD-03", "Bivariate Levels (MMT)", "Domestic Prod (P)", "+2.1961", "4.6487", "6.5387", "+0.3359", "0.7399", "0.0092", "0.0435"],
    ["MOD-04", "Bivariate Log-Log", "ln(P)", "+0.8670", "1.2398", "1.7143", "+0.5057", "0.6177", "0.0200", "0.0598"],
    ["MOD-08", "First Differences (MMT)", "Δ Domestic Prod (ΔP)", "+1.3851", "1.6419", "1.7848", "+0.7761", "0.4456", "0.0300", "2.0492"]
]
format_docx_table(doc, t2_headers, t2_data, col_widths=[0.8, 1.4, 1.3, 0.7, 0.6, 0.6, 0.6, 0.6, 0.5, 0.5])

add_body(doc,
    "The econometric findings in Table 2 conclusively reject the unconditional crowding-out hypothesis. In levels (MOD-03), the domestic production coefficient "
    "is positive (+2.1961) and statistically indistinguishable from zero (HAC p = 0.7399, R² = 0.0092). The extremely low Durbin-Watson statistic (0.0435) "
    "indicates that levels regressions are heavily confounded by common trend drift. When transformed into stationary first differences (MOD-08, DW = 2.0492), "
    "the slope remains statistically insignificant (β = +1.3851, HAC p = 0.4456, R² = 0.0300). Unconditionally, year-to-year changes in domestic crude extraction "
    "explain less than 3% of the variance in crude oil imports. Stagnant domestic extraction was an upstream reality, but not the econometric driver of import growth."
)

add_h2(doc, "4.3 Downstream Refining Expansion: The Primary Engine of Crude Import Pull")
add_body(doc,
    "The actual empirical driver of crude oil imports is domestic refinery throughput. Table 3 presents the regression estimates linking annual crude import "
    "increments to refinery throughput expansion."
)

add_caption(doc, "Table 3: Regression Results: Throughput-Driven Import Pull Specifications")
t3_headers = ["Model ID", "Model Type", "Key Regressors", "Coeff (β)", "Conv SE", "HAC SE", "HAC t-stat", "p-value", "R²", "DW"]
t3_data = [
    ["MOD-07", "First Diff (Bivariate)", "Δ Throughput (ΔR)", "+0.9406", "0.0503", "0.0219", "+43.028", "<0.0001", "0.9382", "2.8992"],
    ["MOD-05", "Levels (Multivariate)", "Throughput (R)\nDomestic Prod (P)", "+0.9976\n−0.8475", "0.0044\n0.1002", "0.0027\n0.0709", "+373.17\n−11.960", "<0.0001\n<0.0001", "0.9996", "2.8549"],
    ["MOD-05-FD", "First Diff (Multivariate)", "Δ Throughput (ΔR)\nΔ Domestic Prod (ΔP)", "+0.9810\n−1.0871", "0.0461\n0.3799", "0.0229\n0.1742", "+42.851\n−6.240", "<0.0001\n<0.0001", "0.9550", "3.1031"]
]
format_docx_table(doc, t3_headers, t3_data, col_widths=[0.8, 1.4, 1.3, 0.8, 0.6, 0.6, 0.6, 0.6, 0.5, 0.5])

add_body(doc,
    "The primary short-run incremental model (MOD-07) establishes a near-unitary relationship between refinery runs and crude imports. The estimated slope "
    "indicates that each additional 1.0 MMT of annual refinery throughput was associated with approximately 0.9406 MMT of additional crude oil imports (p < 0.0001). "
    "Throughput increments alone account for 93.82% of the annual variance in crude imports. This confirms that downstream industrial policy—which expanded "
    "refining capacity far beyond domestic fuel consumption—was the primary physical engine pulling crude imports into the country."
)

add_h2(doc, "4.4 The Refining Surplus Paradox: Emergence as a Net Petroleum Product Exporter")
add_body(doc,
    "Because refinery processing expanded at 5.50% CAGR while domestic consumption grew at 4.15% CAGR, total finished petroleum product output rose from "
    "68.41 MMT to 276.06 MMT (+303.54%). Table 4 tracks India's transition into a permanent net exporter of refined petroleum products."
)

add_caption(doc, "Table 4: India's Petroleum Product Trade Balance (Selected Financial Years)")
t4_headers = ["Financial Year", "Product Production (Q)", "Product Consumption (C)", "Gross Exports (X_p)", "Gross Imports (M_p)", "Net Export Balance", "Product Coverage (Q/C)"]
t4_data = [
    ["FY 1998–99", "68.409", "84.759", "0.720", "23.771", "−23.051", "80.71%"],
    ["FY 2001–02", "104.343", "89.055", "10.090", "7.042", "+3.048", "117.17%"],
    ["FY 2005–06", "124.618", "113.214", "21.504", "13.344", "+8.160", "110.07%"],
    ["FY 2010–11", "196.171", "141.040", "59.077", "17.340", "+41.737", "139.09%"],
    ["FY 2015–16", "231.866", "184.674", "60.595", "29.479", "+31.116", "125.55%"],
    ["FY 2020–21", "233.513", "194.295", "56.766", "43.785", "+12.981", "120.19%"],
    ["FY 2023–24", "276.058", "234.259", "62.593", "48.693", "+13.900", "117.84%"]
]
format_docx_table(doc, t4_headers, t4_data, col_widths=[0.9, 1.0, 1.0, 0.9, 0.9, 0.9, 0.9])

add_body(doc,
    "As shown in Table 4, India was a heavy net product importer in FY 1998–99 (−23.05 MMT net balance, PCR = 80.71%). With the commissioning of the Jamnagar "
    "refinery complex, India achieved net exporter status in FY 2001–02 (+3.05 MMT net balance, PCR = 117.17%) and has maintained an unbroken net export surplus "
    "for 23 consecutive years. In FY 2023–24, India produced 276.06 MMT of products against domestic consumption of 234.26 MMT, generating a gross volume coverage "
    "of 117.84% and net product exports of +13.90 MMT."
)

add_h2(doc, "4.5 Product-Level Supply Asymmetries: Transport Fuel Surpluses vs. The Clean Cooking Deficit")
add_body(doc,
    "The headline product coverage ratio of 117.84% obscures deep structural imbalances across fuel categories. Table 5 presents the complete product-by-product "
    "mass balance for FY 2023–24."
)

add_caption(doc, "Table 5: Product-Level Production, Trade, and Consumption Balance (FY 2023–24)")
t5_headers = ["Product Category", "Production (Q_i)", "Consumption (C_i)", "Coverage (PCR_i)", "Imports (M_i)", "Exports (X_i)", "Net Balance", "Supply Status"]
t5_data = [
    ["High-Speed Diesel (HSD)", "115.943", "89.626", "129.36%", "0.042", "28.204", "+28.162", "Structural Export Surplus"],
    ["Motor Spirit (Petrol / MS)", "45.105", "37.241", "121.12%", "1.050", "8.820", "+7.770", "Structural Export Surplus"],
    ["Aviation Turbine Fuel (ATF)", "17.124", "8.247", "207.64%", "0.000", "8.579", "+8.579", "Massive Export Surplus"],
    ["Naphtha", "13.435", "13.784", "97.47%", "1.420", "0.650", "−0.770", "Balanced / Petchem Feed"],
    ["Liquefied Petroleum Gas (LPG)", "12.779", "29.664", "43.08%", "18.514", "0.525", "−17.989", "Severe Deficit (NIR: 60.6%)"],
    ["Petroleum Coke (Petcoke)", "15.228", "18.665", "81.59%", "9.820", "0.010", "−9.810", "Industrial Deficit"],
    ["Fuel Oil / LSHS Combined", "10.442", "6.594", "158.35%", "9.053", "2.103", "−6.950", "Coastal Bunker Imports"],
    ["Bitumen / Asphalt", "5.240", "8.807", "59.50%", "3.244", "0.018", "−3.226", "Infrastructure Deficit"],
    ["Lubricants & Greases", "1.399", "4.230", "33.07%", "2.840", "0.030", "−2.810", "High-Value Deficit"],
    ["Light Diesel Oil (LDO)", "0.657", "0.782", "84.06%", "0.000", "0.000", "0.000", "Near Balance"],
    ["Superior Kerosene (SKO)", "0.983", "0.479", "205.21%", "0.000", "0.011", "+0.011", "Subsidy Phase-Out Residual"],
    ["Others / Specialized Heavy", "38.723", "16.140", "239.92%", "2.709", "13.642", "+10.933", "Specialized Fractions"],
    ["National Aggregate Total", "276.058", "234.259", "117.84%", "48.693", "62.593", "+13.900", "Gross Volume Surplus"]
]
format_docx_table(doc, t5_headers, t5_data, col_widths=[1.5, 0.7, 0.7, 0.7, 0.6, 0.6, 0.7, 1.1])

add_body(doc,
    "The disaggregated balance in Table 5 exposes a profound structural divergence:\n"
    "1. The Transport Fuel Powerhouse: Domestic refineries produced 178.17 MMT of liquid transport fuels (HSD, MS, and ATF), generating a combined exportable "
    "surplus of +44.51 MMT. High-Speed Diesel achieved 129.36% coverage (+28.16 MMT surplus), Motor Spirit achieved 121.12% coverage (+7.77 MMT surplus), "
    "and ATF reached 207.64% coverage (+8.58 MMT surplus).\n"
    "2. The Clean Cooking Vulnerability: In sharp contrast, domestic LPG production reached only 12.78 MMT against consumption of 29.66 MMT (coverage of 43.08%). "
    "India was forced to import 18.51 MMT of LPG (−17.99 MMT net deficit), resulting in an extraordinary 60.64% net import reliance. Rapid household electrification "
    "and targeted PMUY connections successfully curtailed subsidized kerosene consumption by 95.5% (collapsing from 10.38 MMT in FY99 to 0.48 MMT in FY24), "
    "but shifted cooking energy vulnerability entirely onto international seaborne LPG trade."
)

add_h2(doc, "4.6 Compounding Financial Exposure: Crude Prices, Currency Depreciation, and Import Bill Expansion")
add_body(doc,
    "While physical crude imports expanded by 5.9-fold, India's financial import expenditure suffered violent compounding escalation. Table 6 documents "
    "the trajectory of the Indian Crude Basket price, import volume, and nominal bills in both USD and INR."
)

add_caption(doc, "Table 6: Petroleum Import Expenditure, Crude Basket Prices, and Exchange Rates")
t6_headers = ["Financial Year", "Crude Basket ($/bbl)", "Crude Imports (MMT)", "USD Bill (USD M)", "INR Bill (INR Cr)", "Implied FX (INR/USD)", "Unit Value ($/MT)"]
t6_data = [
    ["FY 1998–99", "—", "39.808", "3,518", "14,917", "42.40", "88.37"],
    ["FY 2000–01", "26.92", "74.097", "14,403", "65,932", "45.78", "194.38"],
    ["FY 2005–06", "55.72", "99.409", "38,776", "171,702", "44.28", "390.07"],
    ["FY 2011–12", "111.89", "171.729", "139,690", "672,220", "48.12", "813.43"],
    ["FY 2013–14", "105.52", "189.238", "142,962", "864,875", "60.50", "755.46"],
    ["FY 2015–16", "46.17", "202.850", "63,972", "416,579", "65.12", "315.37"],
    ["FY 2020–21", "44.82", "196.461", "62,248", "459,779", "73.86", "316.85"],
    ["FY 2022–23", "93.15", "232.700", "157,531", "1,260,372", "80.01", "676.97"],
    ["FY 2023–24", "82.58", "234.262", "133,366", "1,105,176", "82.87", "569.30"]
]
format_docx_table(doc, t6_headers, t6_data, col_widths=[0.9, 0.9, 1.0, 1.0, 1.0, 0.9, 0.9])

add_body(doc,
    "The data in Table 6 illustrate the severe financial magnification wedge. Between FY 1998–99 and FY 2023–24, while physical import volume grew 5.88-fold, "
    "the USD import bill escalated 37.91-fold (from $3.52B to $133.37B). Concurrently, the Indian rupee depreciated from 42.40 to 82.87 INR/USD (a continuous "
    "currency drag of +2.71% p.a.), compounding the domestic currency import bill into a 74.09-fold surge (from INR 14,917 Cr to INR 1,105,176 Cr). "
    "During the commodity peak of FY 2022–23, the crude bill absorbed INR 1,260,372 Cr ($157.53B), posing severe macroeconomic trade balance challenges."
)

add_h2(doc, "4.7 Canonical Regression Synthesis: Conditional Accounting Substitution vs. Causal Crowding-Out")
add_body(doc,
    "To reconcile why domestic extraction is statistically uncorrelated with imports in bivariate models yet displays a statistically significant negative "
    "coefficient in multiple regressions, Table 7 presents the complete canonical model comparison table."
)

add_caption(doc, "Table 7: Comprehensive Econometric Model Comparison Table (Phase 9B-D Canonical Freeze)")
t7_headers = ["Model ID", "Specification", "N", "Regressor", "Coeff (β)", "HAC SE", "HAC t-stat", "p-value", "R²", "DW", "VIF"]
t7_data = [
    ["MOD-03", "Bivariate Levels", "26", "Domestic Prod (P)", "+2.1961", "6.5387", "+0.3359", "0.7399", "0.0092", "0.0435", "N/A"],
    ["MOD-04", "Bivariate Log-Log", "26", "ln(P)", "+0.8670", "1.7143", "+0.5057", "0.6177", "0.0200", "0.0598", "N/A"],
    ["MOD-05", "Multivariate Levels", "26", "Throughput (R)\nDomestic Prod (P)", "+0.9976\n−0.8475", "0.0027\n0.0709", "+373.17\n−11.96", "<0.0001\n<0.0001", "0.9996", "2.8549", "1.018\n1.018"],
    ["MOD-01", "Multivariate Log-Log", "26", "ln(R)\nln(P)", "+1.2549\n−0.0946", "0.0289\n0.0382", "+43.44\n−2.474", "<0.0001\n0.0212", "0.9966", "0.6536", "1.025\n1.025"],
    ["MOD-07", "First Diff (Bivariate)", "25", "Δ Throughput (ΔR)", "+0.9406", "0.0219", "+43.03", "<0.0001", "0.9382", "2.8992", "N/A"],
    ["MOD-08", "First Diff (Bivariate)", "25", "Δ Domestic Prod (ΔP)", "+1.3851", "1.7848", "+0.7761", "0.4456", "0.0300", "2.0492", "N/A"],
    ["MOD-05-FD", "First Diff (Multivariate)", "25", "Δ Throughput (ΔR)\nΔ Domestic Prod (ΔP)", "+0.9810\n−1.0871", "0.0229\n0.1742", "+42.85\n−6.240", "<0.0001\n<0.0001", "0.9550", "3.1031", "1.103\n1.103"]
]
format_docx_table(doc, t7_headers, t7_data, col_widths=[0.7, 1.2, 0.4, 1.3, 0.8, 0.6, 0.6, 0.6, 0.5, 0.5, 0.5])

add_body(doc,
    "The contrast across Table 7 resolves the econometric mechanism:\n"
    "1. Unconditional Independence: In bivariate models (MOD-03, MOD-04, MOD-08), domestic extraction is statistically uncorrelated with crude imports (p = 0.44 to 0.74, R² < 0.03). "
    "Stagnant domestic extraction did not drive import demand.\n"
    "2. Conditional Accounting Substitution: In multivariate models controlling for throughput (MOD-05 and MOD-05-FD), domestic extraction yields a highly "
    "significant negative coefficient (β = −0.8475 in levels and β = −1.0871 in first differences, p < 0.0001). This is an accounting identity substitution effect "
    "(a suppressor phenomenon): holding refinery runs fixed, every barrel of domestic crude processed mechanically displaces an imported barrel (M_c ≈ R − P_c). "
    "However, because throughput expanded by +193 MMT while domestic extraction remained flat, refining pull completely dominated the historical import trajectory."
)

# -----------------------------------------------------------------------------
# 5. DISCUSSION
# -----------------------------------------------------------------------------
add_h1(doc, "5. Discussion")

add_h2(doc, "5.1 Upstream Stagnation, Decoupling, and the Crowding-Out Fallacy")
add_body(doc,
    "Our empirical results challenge a foundational premise of Indian energy policy: that stagnant domestic extraction has been the primary cause of rising "
    "crude oil import dependency. In bivariate regressions across levels, logarithms, and stationary first differences, domestic production exhibits zero "
    "statistical correlation with crude imports (p = 0.446 to 0.739). This confirms the findings of Bhattacharyya (2010) and Mishra et al. (2023), who observed "
    "that successive policy regimes (NELP and HELP) failed to alter India's upstream trajectory due to geological maturity and administrative bottlenecks. "
    "While domestic crude production directly substitutes for crude imports conditional on a given refinery run (MOD-05: β = −0.8475), the real driver of the "
    "feedstock deficit was the fourfold expansion of domestic refining capacity. Consequently, policy narratives asserting that upstream exploration alone "
    "can reverse India's import exposure confuse physical accounting substitution with economic causation."
)

add_h2(doc, "5.2 Downstream Industrial Policy, Merchant Refining, and Export Geopolitics")
add_body(doc,
    "The expansion of India's refinery throughput from 68.54 MMT to 261.55 MMT (+281.6%) reflects a deliberate, highly successful downstream industrial strategy "
    "(Dixit, 2020). By establishing coastal mega-refineries equipped with advanced secondary conversion units (coking, hydrocracking, and catalytic reforming), "
    "Indian refiners capitalized on gross refining margins by processing heavy, sour, discounted crude slates into premium Euro-VI / BS-VI distillates for European, "
    "Asian, and GCC markets (Azhar, 2011; Sarmah & Bal, 2021). India's unbroken 23-year status as a net petroleum product exporter (+13.90 MMT in FY 2023–24) "
    "demonstrates that conventional scalar crude import dependency metrics (Ang et al., 2015; Kruyt et al., 2009; Gupta, 2008) are fundamentally flawed when applied "
    "to merchant refining economies. India does not import crude merely to meet domestic consumption; it imports crude to generate high-value export revenues, "
    "achieving 117.84% aggregate product coverage."
)

add_h2(doc, "5.3 The Clean Cooking Welfare Paradox and Refinery Yield Constraints")
add_body(doc,
    "However, the aggregate product surplus masks an acute welfare paradox in clean household energy. Driven by the Pradhan Mantri Ujjwala Yojana (PMUY), "
    "India achieved historic advances in rural health and clean cooking access by distributing over 100 million subsidized LPG connections (Kar et al., 2019; "
    "Gill-Wiehl et al., 2022). Concurrently, state governments systematically eliminated subsidized PDS kerosene, successfully curtailing kerosene consumption "
    "by 95.5% and plugging substantial diesel adulteration leakages (Rao, 2012; Jain, 2018; Acharya & Sadath, 2017). Yet, because refinery distillation yield "
    "configurations structurally generate only 4.5% to 5.0% LPG (de la Rue du Can et al., 2019), domestic LPG production (12.78 MMT) satisfied less than half of national "
    "demand (29.66 MMT). India was forced to import 18.51 MMT of LPG, creating an extraordinary 60.64% net import reliance. Welfare success in the kitchen was thus "
    "counterbalanced by heightened macroeconomic vulnerability to international LPG pricing and maritime supply lines."
)

add_h2(doc, "5.4 Macroeconomic Volatility, Currency Depreciation, and Fiscal Strain")
add_body(doc,
    "The financial analysis highlights the extreme vulnerability of India's balance of payments. While physical import volumes grew 5.9-fold, the crude import bill "
    "expanded 37.9-fold in USD and 74.1-fold in INR. This confirms the econometric evidence of Tiwari & Albulescu (2016) and Kanjilal & Ghosh (2018), who identified "
    "strong asymmetric transmission between global crude price spikes and rupee depreciation. Over the 26-year period, the rupee's secular depreciation from "
    "42.40 to 82.87 INR/USD added an independent +2.71% annual compounding burden onto domestic consumers and the national exchequer. Although post-2014 diesel and petrol "
    "price deregulation eliminated government under-recoveries and restored fiscal stability to state oil marketing companies (Agrawal & Sinha, 2022), it directly "
    "transmitted international commodity price and currency volatility into domestic retail inflation."
)

add_h2(doc, "5.5 Strategic Policy Implications and Decarbonization Pathways")
add_body(doc,
    "These findings indicate that India's petroleum import vulnerability cannot be solved through upstream drilling subsidies alone (Bhattacharyya, 2010). "
    "Strategic energy security requires a diversified, multi-pronged structural policy:\n"
    "1. Electrifying Rural Clean Cooking: To resolve the structural LPG import deficit, public policy must diversify beyond imported hydrocarbons by deploying "
    "rural electric induction cooktops powered by decentralized renewable energy microgrids, alongside expanding domestic piped natural gas (PNG) networks.\n"
    "2. Accelerating Transport Fuel Substitution: Although India maintains export surpluses in petrol and diesel, domestic consumption (126.87 MMT combined) continues "
    "to expand at over 4% annually. Expanding the 20% Ethanol Blended Petrol (EBP) mandate, developing green hydrogen for long-haul freight, and accelerating mass "
    "bus and two-wheeler electrification will preserve exportable refining volumes while moderating crude import pull.\n"
    "3. Strategic Buffers and Currency Hedging: India must expand Phase-II Strategic Petroleum Reserves (ISPRL) beyond the current 5.33 MMT baseline (Kumar, 2023), "
    "institutionalize bilateral rupee trade settlement mechanisms for crude procurement, and implement counter-cyclical financial hedging to insulate against "
    "the compounding dollar-rupee depreciation wedge."
)

# -----------------------------------------------------------------------------
# 6. CONCLUSION
# -----------------------------------------------------------------------------
add_h1(doc, "6. Conclusion")
add_body(doc,
    "This study has provided an exhaustive 26-year empirical audit of India's petroleum supply chain from FY 1998–99 to FY 2023–24. Five primary findings emerge:\n"
    "1. Upstream Domestic Decoupling: Domestic crude extraction stagnated (CAGR −0.44%, falling from 32.76 MMT to 29.36 MMT) and exhibits zero unconditional statistical "
    "correlation with crude oil import surges (p = 0.446 to 0.739, R² < 0.03).\n"
    "2. Refining Pull as Import Engine: Crude oil imports surged by 488.5% (from 39.81 MMT to 234.26 MMT, CAGR +7.35%), driven near-unitarily by a 281.6% expansion in "
    "domestic refinery throughput (MOD-07: β = +0.9406, p < 0.0001, R² = 0.9382).\n"
    "3. Structural Net Exporter Status: Total refined petroleum product output grew by 303.5% (to 276.06 MMT), securing India's status as a continuous net refined product "
    "exporter since FY 2001–02 (+13.90 MMT in FY 2023–24, PCR = 117.84%).\n"
    "4. Clean Cooking Import Lock-In: Aggregate product self-sufficiency is heavily skewed by massive transport fuel surpluses (Diesel PCR = 129.4%, Petrol PCR = 121.1%, "
    "ATF PCR = 207.6%), while domestic clean cooking LPG coverage fell to 43.1%, forcing 18.51 MMT of imports (60.6% net import reliance).\n"
    "5. Financial Magnification: International crude price volatility and a persistent currency depreciation drag (+2.71% p.a.) compounded a 5.9-fold physical import growth "
    "into a 37.9-fold expansion in the US dollar import bill ($133.37B in FY24) and a 74.1-fold surge in the domestic rupee bill (INR 1,105,176 Cr)."
)
add_body(doc,
    "The central policy conclusion is that India's petroleum vulnerability is downstream and product-specific rather than upstream and aggregate. Attempting to eliminate "
    "import exposure through domestic exploration alone is mathematically and geologically futile. True energy resilience requires targeted household electrification, "
    "clean transport fuel substitution, expanded strategic reserves, and financial currency hedging."
)

# -----------------------------------------------------------------------------
# 7. REFERENCES
# -----------------------------------------------------------------------------
add_h1(doc, "7. References")

refs = [
    "Acharya, R. H., & Sadath, A. C. (2017). Energy poverty and fuel switching: Empirical evidence from Indian households. Energy Policy, 108, 642–650. https://doi.org/10.1016/j.enpol.2016.12.036",
    "Agrawal, P., & Sinha, A. (2022). Petroleum pricing reforms in India: Impact on inflation, fiscal deficit and GDP. Energy Policy, 161, 112743. https://doi.org/10.1016/j.enpol.2022.112743",
    "Ang, B. W. (2004). Decomposition analysis for policymaking in energy: Which is the preferred method? Energy Policy, 32(9), 1131–1139. https://doi.org/10.1016/S0301-4215(03)00076-4",
    "Ang, B. W. (2015). LMDI decomposition approach: A guide for implementation. Energy Policy, 86, 233–238. https://doi.org/10.1016/j.enpol.2015.07.007",
    "Ang, B. W., Choong, W. L., & Ng, T. S. (2015). Energy security: Definitions, dimensions and indexes. Renewable and Sustainable Energy Reviews, 42, 1077–1093. https://doi.org/10.1016/j.rser.2014.10.064",
    "Azhar, M. (2011). India's oil trade with GCC countries. OPEC Energy Review, 35(3), 263–280. https://doi.org/10.1111/j.1753-0237.2011.00187.x",
    "Bhattacharyya, S. C. (2010). Shaping a sustainable energy future for India: Management challenges. Energy Policy, 38(8), 4173–4185. https://doi.org/10.1016/j.enpol.2010.03.045",
    "Dash, A. K., Sethi, N., & Bal, D. P. (2018). Energy consumption and economic growth in India: An empirical evidence from ARDL approach. Energy Policy, 118, 12–23. https://doi.org/10.1016/j.enpol.2018.04.001",
    "de la Rue du Can, S., Pudleiner, D., Jones, D., & Khanna, N. (2019). Energy modeling for roadmap development: A case study of India's residential sector. Applied Energy, 239, 1021–1033. https://doi.org/10.1016/j.apenergy.2019.01.065",
    "Dixit, A. (2020). The legal and regulatory regime of downstream petroleum sector in India: Evolution and emerging trends. Journal of World Energy Law & Business, 13(4), 312–329. https://doi.org/10.1093/jwelb/jwaa035",
    "Ghosh, S. (2006). Steel consumption and economic growth: Evidence from India. Energy Policy, 34(18), 3801–3807. https://doi.org/10.1016/j.enpol.2005.02.007",
    "Ghosh, S. (2009). Import demand of crude oil and economic growth: Evidence from India. Energy Policy, 37(2), 699–702. https://doi.org/10.1016/j.enpol.2008.10.013",
    "Ghosh, S. (2011). Examining carbon emissions economic growth nexus for India: A multivariate cointegration approach. Energy Policy, 39(2), 809–814. https://doi.org/10.1016/j.enpol.2010.10.055",
    "Gill-Wiehl, A., Brown, E., & Smith, K. R. (2022). India's clean cooking fuel revolution: A review of PMUY and its impact on household fuel choice. Energy Policy, 168, 112915. https://doi.org/10.1016/j.enpol.2022.112915",
    "Gould, C. F., & Urpelainen, J. (2018). The gendered nature of liquefied petroleum gas adoption in rural India. Energy Policy, 122, 640–649. https://doi.org/10.1016/j.enpol.2018.07.027",
    "Gupta, E. (2008). Oil vulnerability index of oil-importing countries. Energy Policy, 36(3), 1195–1211. https://doi.org/10.1016/j.enpol.2007.11.011",
    "Jain, A. (2018). India's fuel subsidies: Who benefits and what are the alternatives? Energy Policy, 123, 563–575. https://doi.org/10.1016/j.enpol.2018.04.050",
    "Kanjilal, K., & Ghosh, S. (2018). Dynamics of crude oil price, exchange rate and stock prices: A study of India. Empirical Economics, 54(3), 1187–1212. https://doi.org/10.1007/s00181-017-1334-2",
    "Kar, A., Pachauri, S., Bailis, R., & Zerriffi, H. (2019). Using sales data to assess cooking gas adoption and use in India. Nature Energy, 4(9), 796–806. https://doi.org/10.1038/s41560-019-0429-8",
    "Kruyt, B., van Vuuren, D. P., de Vries, H. J., & Groenenberg, H. (2009). Indicators for energy security. Energy Policy, 37(6), 2166–2181. https://doi.org/10.1016/j.enpol.2009.02.006",
    "Kumar, A. (2023). India's energy security architecture: Geopolitical challenges and strategic options. Energy, 270, 127993. https://doi.org/10.1016/j.energy.2023.127993",
    "Kumar, S. (2011). The macroeconomic effects of oil price shocks on India: An asymmetric cointegration approach. Modern Economy, 2(5), 871–884. https://doi.org/10.4236/me.2011.25097",
    "Mallick, H., & Agarwal, S. (2014). An empirical analysis of energy consumption and economic growth in India. International Journal of Energy Economics and Policy, 4(4), 578–589.",
    "Mandal, K., Bhattacharyya, S. C., & Bhoi, B. K. (2012). Estimation of petroleum products demand in India: A cointegration approach. Journal of Policy Modeling, 34(6), 882–897. https://doi.org/10.1016/j.jpolmod.2012.06.001",
    "Mishra, B. R., Ghosh, S., & Kanjilal, K. (2023). Measuring energy security performance in India: An index-based approach. Energy Policy, 183, 113804. https://doi.org/10.1016/j.enpol.2023.113804",
    "Rao, N. D. (2012). Kerosene subsidies in India: When energy policy fails. Energy for Sustainable Development, 16(1), 35–43. https://doi.org/10.1016/j.esd.2011.12.007",
    "Sarmah, P., & Bal, D. P. (2021). The dynamic nexus between oil price and economic growth in India: A wavelet-based approach. The Indian Economic Journal, 69(3), 442–458. https://doi.org/10.1177/0019466221998838",
    "Shalu, Singh, K., Kaur, M., & Sikka, R. (2023). Growth and instability analysis of petroleum products in India. Indian Journal of Economics and Development, 19(4), 849–858. https://doi.org/10.35716/IJED-23070",
    "Tiwari, A. K., & Albulescu, C. T. (2016). Oil price and exchange rate in India: Fresh evidence from continuous wavelet approach and asymmetric, non-linear ARDL. Applied Energy, 179, 775–783. https://doi.org/10.1016/j.apenergy.2016.06.139",
    "Vivoda, V. (2010). Evaluating energy security in the Asia-Pacific region: A novel methodological approach. Energy Policy, 38(9), 5258–5263. https://doi.org/10.1016/j.enpol.2010.05.028"
]

for r in refs:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    run = p.add_run(r)
    run.font.name = "Times New Roman"
    run.font.size = Pt(9.5)

# -----------------------------------------------------------------------------
# SECTIONS 8–11: DECLARATIONS
# -----------------------------------------------------------------------------
add_h1(doc, "8. Acknowledgement")
add_body(doc,
    "The authors express their sincere gratitude to the Ministry of Petroleum and Natural Gas (MoPNG), Government of India, the Petroleum "
    "Planning & Analysis Cell (PPAC), the Directorate General of Commercial Intelligence and Statistics (DGCI&S), and the Reserve Bank of India (RBI) "
    "for maintaining transparent, publicly accessible administrative and statistical records. The authors also thank academic supervisors, faculty mentors, "
    "and departmental colleagues for invaluable technical guidance and critical feedback on time-series econometrics and energy economics."
)

add_h1(doc, "9. Conflict of Interest")
add_body(doc,
    "The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence "
    "the work reported in this paper."
)

add_h1(doc, "10. Funding statement")
add_body(doc,
    "This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors."
)

add_h1(doc, "11. Author contributions")
add_body(doc,
    "[AUTHOR_NAME_PLACEHOLDER]: Conceptualization, Methodology, Formal Data Curation, Econometric Estimation, Model Reconciliation, "
    "Visualization, Writing – Original Draft, Writing – Review & Editing."
)

# Save DOCX
doc.save(DOCX_PATH)
print(f"[OK] Successfully generated Word Document: {DOCX_PATH}")

# -----------------------------------------------------------------------------
# BUILD PDF VERSION (ReportLab)
# -----------------------------------------------------------------------------
print("Compiling PDF version...")

pdf_doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=letter,
    leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Times-Bold',
    fontSize=16,
    leading=20,
    textColor=colors.HexColor('#0F2240'),
    spaceAfter=10
)
author_style = ParagraphStyle(
    'DocAuthor',
    parent=styles['Normal'],
    fontName='Times-Bold',
    fontSize=10.5,
    leading=14,
    textColor=colors.HexColor('#222222'),
    spaceAfter=4
)
affil_style = ParagraphStyle(
    'DocAffil',
    parent=styles['Normal'],
    fontName='Times-Italic',
    fontSize=9,
    leading=12,
    textColor=colors.HexColor('#555555'),
    spaceAfter=12
)
h1_style = ParagraphStyle(
    'SectionH1',
    parent=styles['Normal'],
    fontName='Times-Bold',
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#0F2240'),
    spaceBefore=14,
    spaceAfter=6,
    keepWithNext=True
)
h2_style = ParagraphStyle(
    'SectionH2',
    parent=styles['Normal'],
    fontName='Times-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.HexColor('#1F4E79'),
    spaceBefore=10,
    spaceAfter=4,
    keepWithNext=True
)
body_style = ParagraphStyle(
    'BodyJustified',
    parent=styles['Normal'],
    fontName='Times-Roman',
    fontSize=9.5,
    leading=13,
    alignment=4, # Justified
    spaceAfter=6,
    textColor=colors.HexColor('#222222')
)
caption_style = ParagraphStyle(
    'TableCaption',
    parent=styles['Normal'],
    fontName='Times-Bold',
    fontSize=9,
    leading=12,
    spaceBefore=8,
    spaceAfter=4,
    keepWithNext=True,
    textColor=colors.HexColor('#111111')
)
ref_style = ParagraphStyle(
    'ReferenceItem',
    parent=styles['Normal'],
    fontName='Times-Roman',
    fontSize=8.5,
    leading=11.5,
    leftIndent=24,
    firstLineIndent=-24,
    spaceAfter=4,
    textColor=colors.HexColor('#222222')
)
table_text_style = ParagraphStyle(
    'TableText',
    parent=styles['Normal'],
    fontName='Times-Roman',
    fontSize=7.5,
    leading=9.5,
    textColor=colors.HexColor('#222222')
)
table_hdr_style = ParagraphStyle(
    'TableHdr',
    parent=styles['Normal'],
    fontName='Times-Bold',
    fontSize=7.5,
    leading=9.5,
    alignment=1,
    textColor=colors.white
)

story = []

# Title & Metadata
story.append(Paragraph("India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption", title_style))
story.append(Paragraph("[AUTHOR_NAME_PLACEHOLDER]", author_style))
story.append(Paragraph("[INSTITUTION_PLACEHOLDER] | [DEPARTMENT_PLACEHOLDER]<br/>Corresponding Author: [EMAIL_PLACEHOLDER] | ORCID: [ORCID_PLACEHOLDER]", affil_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#B0B0B0'), spaceAfter=10))

# 1. Abstract
story.append(Paragraph("1. Abstract", h1_style))
story.append(Paragraph(abstract_text, body_style))
story.append(Paragraph("<b>Keywords:</b> <i>Petroleum supply chain; crude oil import dependence; refinery throughput; LPG import exposure; energy security; Newey-West econometrics; India.</i>", body_style))

# 2. Introduction
story.append(Paragraph("2. Introduction", h1_style))
story.append(Paragraph("2.1 Context and Global Energy Security Paradigms", h2_style))
story.append(Paragraph(
    "Energy security is fundamentally multi-dimensional, spanning availability, accessibility, affordability, and acceptability "
    "(Ang, Choong, & Ng, 2015). In classical energy economics, national exposure to international hydrocarbon markets has conventionally "
    "been quantified using scalar physical import-dependency ratios—primarily the ratio of net crude oil imports to domestic consumption "
    "(Kruyt, van Vuuren, de Vries, & Groenenberg, 2009). However, cross-country comparative studies establish that simple aggregate import "
    "metrics fail to capture systemic vulnerabilities related to supply diversity, refining bottlenecks, and macroeconomic balance-of-payments "
    "pressures (Vivoda, 2010). Among developing net oil-importing nations, India has consistently ranked among the most structurally exposed economies "
    "due to its high hydrocarbon intensity, low per-capita income, and substantial import bill fiscal burden (Gupta, 2008).", body_style))
story.append(Paragraph(
    "As emerging market economies industrialize, rapid urbanization and transport motorization inevitably trigger accelerating petroleum product demand "
    "(Dash, Sethi, & Bal, 2018; Mallick & Agarwal, 2014). To mitigate external supply disruptions, conventional energy security doctrine advocates for "
    "domestic upstream exploration and field development. However, where geological realities and maturing sedimentary basins constrain domestic extraction, "
    "import exposure undergoes complex structural transformations across upstream, midstream, and downstream tiers (Mishra, Ghosh, & Kanjilal, 2023).", body_style))

story.append(Paragraph("2.2 The Indian Hydrocarbon Landscape: Upstream Realities vs. Downstream Ambitions", h2_style))
story.append(Paragraph(
    "India's petroleum sector presents a striking structural dichotomy. On the upstream extraction front, domestic crude oil production has remained "
    "substantially stagnant for three decades, oscillating within a narrow band of 29 to 38 million metric tonnes (MMT) per annum despite successive rounds "
    "of exploratory licensing under the New Exploration Licensing Policy (NELP) and the Hydrocarbon Exploration and Licensing Policy (HELP) "
    "(Bhattacharyya, 2010). Natural field decline across mature offshore basins, particularly ONGC's Mumbai High, coupled with technical challenges in "
    "complex deepwater and onshore frontier plays, has effectively decoupled domestic extraction from national economic growth (Mishra et al., 2023).", body_style))
story.append(Paragraph(
    "Conversely, India's downstream refining sector experienced an unprecedented state-facilitated structural transformation following the liberalization "
    "measures of 1998 (Dixit, 2020). Through policy incentives permitting tariff-free capital imports, domestic refinery deregulation, and the establishment "
    "of export-oriented Special Economic Zones (SEZs), India attracted massive private capital into mega-refining infrastructure—most prominently "
    "Reliance Industries Limited's Jamnagar refining complex and Nayara Energy's Vadinar refinery in Gujarat. Consequently, India rapidly transitioned "
    "from a deficit refined-product importer into an export-oriented merchant refining hub for the Indian Ocean basin and GCC markets (Azhar, 2011; "
    "Sarmah & Bal, 2021). National crude distillation capacity expanded to over 256 MMT per annum, propelling actual domestic refinery crude throughput "
    "from 68.54 MMT in FY 1998–99 to 261.55 MMT in FY 2023–24.", body_style))

story.append(Paragraph("2.3 The \"Triple Paradox\" of India's Petroleum Sector", h2_style))
story.append(Paragraph(
    "This asymmetric sectoral trajectory has generated what this paper formalizes as the \"Triple Paradox\" of India's petroleum supply chain:<br/>"
    "<b>1. The Upstream Decoupling Paradox:</b> While national economic output and refining capacity expanded by multiple orders of magnitude, domestic "
    "crude extraction remained completely stagnant, causing the crude oil import dependency ratio to climb from 58.1% to 89.6%. Policymakers frequently "
    "assert that stagnant domestic production \"drove\" rising imports; yet, whether domestic extraction actually exerted any crowding-out or mitigating "
    "effect on imports remains an unverified empirical question.<br/>"
    "<b>2. The Refining Surplus vs. Clean Cooking Deficit Paradox:</b> Since FY 2001–02, India has been a continuous net exporter of refined petroleum products "
    "in aggregate volume, exporting 62.59 MMT against 48.69 MMT of product imports in FY 2023–24 (+13.90 MMT net export balance). However, this aggregate "
    "surplus is heavily skewed toward middle and light transport distillates (High-Speed Diesel and Aviation Turbine Fuel), masking an acute domestic supply "
    "deficit in Liquefied Petroleum Gas (LPG). Driven by the massive welfare success of the Pradhan Mantri Ujjwala Yojana (PMUY), household clean cooking "
    "gas adoption expanded exponentially (Kar et al., 2019; Gill-Wiehl et al., 2022; Gould & Urpelainen, 2018), while subsidized kerosene was systematically "
    "curtailed (Rao, 2012; Jain, 2018; Acharya & Sadath, 2017). Because refinery crude distillation yield configurations structurally produce only 4.5% to 5.0% LPG "
    "(de la Rue du Can et al., 2019), domestic LPG coverage collapsed to 43.1%, locking the nation into extreme foreign import reliance (60.6% net import reliance in FY 2023–24).<br/>"
    "<b>3. The Compounding Financial Exposure Paradox:</b> Physical crude import volumes grew 5.9-fold over the 26-year study period. Yet, India's nominal crude "
    "import bill escalated 37.9-fold in US dollars and 74.1-fold in Indian rupees. This explosive financial magnification reflects the compounding interaction "
    "between cyclical international oil price shocks (Kumar, 2011; Tiwari & Albulescu, 2016) and a relentless secular rupee depreciation wedge against "
    "the dollar (Kanjilal & Ghosh, 2018; Agrawal & Sinha, 2022).", body_style))

story.append(Paragraph("2.4 Research Gap and Contribution", h2_style))
story.append(Paragraph(
    "Although extensive scholarship examines individual facets of India's energy sector—such as energy-GDP causality (Dash et al., 2018), "
    "crude import demand elasticity (Ghosh, 2009), pricing deregulation (Agrawal & Sinha, 2022), household clean cooking access (Kar et al., 2019), "
    "and commodity price instability (Shalu et al., 2023)—the literature exhibits critical gaps. Existing studies rarely integrate the full "
    "interlocking physical supply chain (domestic crude, imports, refinery throughput, product manufacturing, and product-specific consumption) with "
    "monetary trade balances over multi-decade periods using verified administrative data. This study bridges these gaps by providing the first comprehensive, "
    "26-year empirical supply-chain audit of India's petroleum sector from FY 1998–99 to FY 2023–24, establishing reproducible mass balances, Newey-West HAC "
    "econometric models, product-level coverage metrics, and financial decomposition analyses.", body_style))

story.append(Paragraph("2.5 Research Questions", h2_style))
story.append(Paragraph(
    "This investigation addresses five central research questions:<br/>"
    "• <b>RQ1:</b> How has domestic crude oil production evolved over 1998–2024, and does empirical evidence support the hypothesis that stagnant domestic extraction drove crude import growth?<br/>"
    "• <b>RQ2:</b> What is the precise statistical relationship between domestic refinery throughput expansion and crude oil import requirements?<br/>"
    "• <b>RQ3:</b> How has India's refined petroleum product trade balance evolved, and what structural asymmetries exist behind the aggregate product export surplus?<br/>"
    "• <b>RQ4:</b> What factors explain the acute divergence between transport fuel self-sufficiency and structural LPG import vulnerability?<br/>"
    "• <b>RQ5:</b> How have global crude oil price shocks and currency depreciation interacted to magnify India's financial petroleum import bill relative to physical volume growth?", body_style))

# 3. Method
story.append(Paragraph("3. Method", h1_style))
story.append(Paragraph("3.1 Data Sources, Compilation Hierarchy, and Study Period", h2_style))
story.append(Paragraph(
    "This study relies exclusively on official, primary administrative data compiled by statutory government bodies under the Ministry of Petroleum and "
    "Natural Gas (MoPNG), Government of India. The primary analytical baseline is drawn from historical time-series registers maintained by the Petroleum "
    "Planning & Analysis Cell (PPAC). The core annual dataset spans 26 continuous financial years (April 1, 1998 to March 31, 2024; N = 26). "
    "All physical flows are measured in Million Metric Tonnes (MMT), and monetary flows are recorded in Million US Dollars (USD M) and Crore Indian Rupees (INR Cr). "
    "The canonical standardized dataset (`core_annual_petroleum_dataset.csv`, SHA-256: `9fb5e64c4d0e3402f979f7e83269b0a41034c8530e54fba2fdbd6895b98634ca`) "
    "was audited and frozen prior to model estimation.", body_style))

story.append(Paragraph("3.2 Variable Definitions and Unit Standardization", h2_style))
story.append(Paragraph(
    "Primary supply-chain variables are: Domestic crude production (P_c,t, MMT), gross crude imports (M_c,t, MMT), crude exports (X_c,t = 0), "
    "refinery crude throughput (R_t, MMT), refined product production (Q_p,t, MMT), product consumption (C_p,t, MMT), product imports (M_p,t, MMT), "
    "and product exports (X_p,t, MMT). All reporting periods follow the official Indian Financial Year (April 1 to March 31).", body_style))

story.append(Paragraph("3.3 Physical Mass Balance and Accounting Residual", h2_style))
story.append(Paragraph(
    "The upstream physical mass balance is governed by: M_c,t + P_c,t − X_c,t = R_t + ΔS_c,t + L_c,t. "
    "Because official PPAC returns contain only refined product export entries and statutory allocation mandates domestic processing of all indigenous crude, "
    "we set X_c,t = 0. The conditional crude accounting residual Res_c,t^cond = M_c,t + P_c,t − R_t averages +4.512 MMT/yr (std: 1.357 MMT), "
    "capturing unobserved strategic storage additions (ISPRL), commercial pipeline line-pack, and transit losses.", body_style))

story.append(Paragraph("3.4 Growth, Elasticity, and Structural Indicators", h2_style))
story.append(Paragraph(
    "Compound Annual Growth Rates (CAGR) are calculated as: CAGR = (X_T / X_0)^(1/n) − 1. "
    "Upstream Crude Import Dependency is: CID_t = (M_c,t / R_t) × 100. "
    "The Upstream Deficit Gap is: Gap_t = R_t − P_c,t. "
    "The Aggregate Product Coverage Ratio is: PCR_agg,t = (Q_p,t / C_p,t) × 100.", body_style))

story.append(Paragraph("3.5 Econometric Specifications and Covariance Estimation", h2_style))
story.append(Paragraph(
    "To analyze import determinants, we estimate bivariate and multivariate models in levels, logs, and first differences. "
    "To correct for autocorrelation and heteroskedasticity, all standard errors are estimated using the Newey-West (1987) HAC covariance estimator "
    "with a Bartlett kernel. The maximum lag truncation parameter is set to L = floor(4 × (n/100)^(2/9)) = 2. Hypothesis tests use two-tailed Student's t-distributions "
    "with finite-sample degrees of freedom df = n − k.", body_style))

story.append(Paragraph("3.6 Product-Level Disaggregation and Asymmetry Metrics", h2_style))
story.append(Paragraph(
    "Product coverage ratios are computed across 12 product lines: PCR_i = (Q_p,i / C_p,i) × 100. "
    "For deficit products, net import reliance is: NIR_i = [(M_p,i − X_p,i) / C_p,i] × 100.", body_style))

story.append(Paragraph("3.7 Import Value, Price Shocks, and Currency Translation", h2_style))
story.append(Paragraph(
    "Nominal import expenditure is analyzed in USD and INR. The implied exchange rate is: IER_t = (V_INR,t × 10) / V_USD,t. "
    "International crude prices are benchmarked against the official Indian Crude Basket FOB price.", body_style))

story.append(Paragraph("3.8 Index Decomposition Analysis Framework", h2_style))
story.append(Paragraph(
    "Expenditure is factorized into physical quantity, unit price, and currency exchange components: V_INR,t = M_c,t × P_USD,t × IER_t. "
    "Logarithmic Mean Divisia Index (LMDI-I) formulations (Ang, 2004, 2015) are applied to allocate expenditure expansion across factors.", body_style))

story.append(Paragraph("3.9 Methodological Disclosures, Stationarity Caveats, and Limitations", h2_style))
story.append(Paragraph(
    "Four boundaries are noted: (1) observational regressions represent statistical associations, not causal proofs; (2) Augmented Dickey-Fuller tests confirm "
    "stationarity in first differences (p < 0.01), but T = 25 small-sample power limitations mean differenced models represent robust short-run representations "
    "rather than asymptotic proofs; (3) the crude residual is conditional on X_c,t = 0; (4) refining gains (~5.55%) and losses (~8–9%) are aggregate benchmarks.", body_style))

# 4. Results
story.append(Paragraph("4. Result", h1_style))
story.append(Paragraph("4.1 Long-Run Evolution of India's Petroleum Supply Chain (FY99–FY24)", h2_style))
story.append(Paragraph(
    "Over the 26-year study period, India's petroleum supply chain experienced profound structural divergence. Table 1 summarizes decadal indicators.", body_style))

story.append(Paragraph("<b>Table 1: Summary Statistics of India's Petroleum Supply Chain (FY 1998–99 to FY 2023–24)</b>", caption_style))
def make_pdf_table(headers, data, col_widths):
    table_data = [[Paragraph(h, table_hdr_style) for h in headers]]
    for r_idx, row in enumerate(data):
        row_cells = []
        for c_idx, val in enumerate(row):
            is_num = False
            sval = str(val).strip().replace('%', '').replace(',', '').replace('+', '').replace('−', '-').replace('$', '')
            try:
                float(sval)
                is_num = True
            except ValueError:
                is_num = False
            align = 2 if is_num and c_idx > 0 else 0
            ts = ParagraphStyle('tc', parent=table_text_style, alignment=align)
            row_cells.append(Paragraph(str(val), ts))
        table_data.append(row_cells)
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E79')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F5F7FA')])
    ]))
    return t

story.append(make_pdf_table(t1_headers, t1_data, [160, 68, 68, 68, 65, 69]))
story.append(Spacer(1, 6))

story.append(Paragraph(
    "Domestic crude output stagnated (CAGR −0.44%, from 32.76 MMT to 29.36 MMT), while refinery throughput surged +281.60% (68.54 MMT to 261.55 MMT, CAGR +5.50%). "
    "Consequently, the upstream deficit gap expanded by +548.96% (35.78 MMT to 232.19 MMT), pulling crude imports from 39.81 MMT to 234.26 MMT (CAGR +7.35%) "
    "and raising crude import dependency from 58.08% to 89.57%.", body_style))

story.append(Paragraph("4.2 Upstream Decoupling: Stagnant Domestic Production vs. Surging Imports", h2_style))
story.append(Paragraph("<b>Table 2: Regression Results: Unconditional Domestic Production–Import Relationship</b>", caption_style))
story.append(make_pdf_table(t2_headers, t2_data, [45, 95, 88, 48, 40, 40, 42, 42, 48, 40]))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "As shown in Table 2, domestic production is statistically uncorrelated with crude imports in levels (MOD-03: β = +2.1961, p = 0.7399, R² = 0.0092) "
    "and first differences (MOD-08: β = +1.3851, p = 0.4456, R² = 0.0300). Stagnant domestic extraction did not drive import growth.", body_style))

story.append(Paragraph("4.3 Downstream Refining Expansion: The Primary Engine of Crude Import Pull", h2_style))
story.append(Paragraph("<b>Table 3: Regression Results: Throughput-Driven Import Pull Specifications</b>", caption_style))
story.append(make_pdf_table(t3_headers, t3_data, [50, 95, 90, 55, 42, 42, 42, 42, 40, 40]))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "The primary first-difference model (MOD-07) demonstrates that each 1.0 MMT increment in refinery throughput drew 0.9406 MMT of imported crude (p < 0.0001, R² = 0.9382). "
    "Refining throughput expansion was the primary physical driver of crude oil imports.", body_style))

story.append(Paragraph("4.4 The Refining Surplus Paradox: Emergence as a Net Petroleum Product Exporter", h2_style))
story.append(Paragraph("<b>Table 4: India's Petroleum Product Trade Balance (Selected Financial Years)</b>", caption_style))
story.append(make_pdf_table(t4_headers, t4_data, [68, 72, 72, 70, 70, 72, 74]))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Since FY 2001–02, India has been a continuous net exporter of refined petroleum products (+13.90 MMT in FY 2023–24), achieving 117.84% aggregate product coverage.", body_style))

story.append(Paragraph("4.5 Product-Level Supply Asymmetries: Transport Fuel Surpluses vs. The Clean Cooking Deficit", h2_style))
story.append(Paragraph("<b>Table 5: Product-Level Production, Trade, and Consumption Balance (FY 2023–24)</b>", caption_style))
story.append(make_pdf_table(t5_headers, t5_data, [105, 50, 50, 52, 42, 42, 48, 109]))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Table 5 reveals acute downstream divergence: transport fuels generated massive export surpluses (Diesel +28.16 MMT, Petrol +7.77 MMT, ATF +8.58 MMT), "
    "while LPG collapsed to 43.08% coverage (−17.99 MMT deficit, 60.64% net import reliance) due to refinery distillation yield limits (~4.8%) alongside PMUY clean cooking adoption.", body_style))

story.append(Paragraph("4.6 Compounding Financial Exposure: Crude Prices, Currency Depreciation, and Import Bill Expansion", h2_style))
story.append(Paragraph("<b>Table 6: Petroleum Import Expenditure, Crude Basket Prices, and Exchange Rates</b>", caption_style))
story.append(make_pdf_table(t6_headers, t6_data, [65, 68, 72, 72, 75, 72, 74]))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "While physical crude imports grew 5.9-fold, the nominal USD bill escalated 37.9-fold ($133.37B in FY24) and the INR bill grew 74.1-fold (INR 1,105,176 Cr) "
    "due to international price spikes ($26.92 to $111.89/bbl) and persistent currency depreciation (42.40 to 82.87 INR/USD).", body_style))

story.append(Paragraph("4.7 Canonical Regression Synthesis: Conditional Accounting Substitution vs. Causal Crowding-Out", h2_style))
story.append(Paragraph("<b>Table 7: Comprehensive Econometric Model Comparison Table (Phase 9B-D Canonical Freeze)</b>", caption_style))
story.append(make_pdf_table(t7_headers, t7_data, [45, 80, 24, 95, 52, 40, 42, 42, 38, 40, 40]))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "In multivariate regressions controlling for throughput (MOD-05 and MOD-05-FD), domestic extraction yields β = −0.8475 (p < 0.0001). "
    "This represents an accounting substitution suppressor effect (M_c ≈ R − P_c): holding throughput fixed, each unit of domestic crude displaces imports. "
    "However, because throughput expanded by +193 MMT while domestic production flatlined, refining runs dominated the actual import trajectory.", body_style))

# 5. Discussion
story.append(Paragraph("5. Discussion", h1_style))
story.append(Paragraph("5.1 Upstream Stagnation, Decoupling, and the Crowding-Out Fallacy", h2_style))
story.append(Paragraph(
    "Our empirical results challenge the common assumption that stagnant domestic extraction caused crude import dependency. In bivariate regressions across levels, "
    "logs, and first differences, domestic production shows zero correlation with imports (p = 0.446 to 0.739). While domestic crude substitutes for imports conditional "
    "on fixed throughput (MOD-05: β = −0.8475), the real driver of the deficit was the 281.6% expansion in domestic refinery throughput (Bhattacharyya, 2010; Mishra et al., 2023).", body_style))

story.append(Paragraph("5.2 Downstream Industrial Policy, Merchant Refining, and Export Geopolitics", h2_style))
story.append(Paragraph(
    "India's emergence as a merchant refining hub producing 276.06 MMT of finished products reflects deliberate downstream industrial policy (Dixit, 2020; Azhar, 2011). "
    "Scalar crude import ratios (Ang et al., 2015; Kruyt et al., 2009; Gupta, 2008) fail to capture the fact that India imports crude to generate valuable refined product exports, "
    "maintaining an unbroken 23-year net export surplus.", body_style))

story.append(Paragraph("5.3 The Clean Cooking Welfare Paradox and Refinery Yield Constraints", h2_style))
story.append(Paragraph(
    "The 117.84% aggregate product coverage masks an acute welfare paradox: PMUY expanded clean cooking access to over 100 million households (Kar et al., 2019; Gill-Wiehl et al., 2022) "
    "while kerosene was curtailed by 95.5% (Rao, 2012; Jain, 2018). But because refinery yield curves yield only ~4.8% LPG (de la Rue du Can et al., 2019), domestic coverage "
    "collapsed to 43.08%, forcing 18.51 MMT of LPG imports (60.64% net import reliance).", body_style))

story.append(Paragraph("5.4 Macroeconomic Volatility, Currency Depreciation, and Fiscal Strain", h2_style))
story.append(Paragraph(
    "The 74.1-fold escalation of the INR crude bill reflects strong asymmetric transmission between oil prices and rupee depreciation (Tiwari & Albulescu, 2016; Kanjilal & Ghosh, 2018). "
    "A continuous +2.71% p.a. rupee depreciation drag compounded global crude spikes into domestic trade balance strain (Kumar, 2011; Agrawal & Sinha, 2022).", body_style))

story.append(Paragraph("5.5 Strategic Policy Implications and Decarbonization Pathways", h2_style))
story.append(Paragraph(
    "Upstream exploration alone cannot resolve India's import exposure (Bhattacharyya, 2010). Strategic priorities must focus on: (1) diversifying rural clean cooking "
    "into electric induction cooktops and piped gas; (2) transport fuel substitution via 20% ethanol blending and electric mobility; (3) expanding Phase-II Strategic Petroleum "
    "Reserves beyond 5.33 MMT (Kumar, 2023) and establishing rupee-denominated trade settlements.", body_style))

# 6. Conclusion
story.append(Paragraph("6. Conclusion", h1_style))
story.append(Paragraph(
    "This 26-year empirical analysis reveals that India's petroleum import vulnerability is downstream and product-specific rather than upstream and aggregate. "
    "Domestic crude output flatlined (CAGR −0.44%) and is statistically decoupled from import surges. Instead, crude imports surged +488.5% due to a 281.6% expansion in "
    "refinery throughput (β = 0.9406, R² = 0.9382), creating a merchant refining powerhouse with 117.84% aggregate product coverage. However, massive transport fuel export "
    "surpluses directly coexist with a severe 60.64% import reliance in clean cooking LPG. Policy must shift from upstream extraction subsidies toward targeted clean cooking "
    "electrification, transport fuel substitution, and strategic financial hedging.", body_style))

# 7. References
story.append(Paragraph("7. References", h1_style))
for r in refs:
    story.append(Paragraph(r, ref_style))

# Declarations
story.append(Paragraph("8. Acknowledgement", h1_style))
story.append(Paragraph(
    "The authors express their sincere gratitude to the Ministry of Petroleum and Natural Gas (MoPNG), Government of India, the Petroleum "
    "Planning & Analysis Cell (PPAC), the Directorate General of Commercial Intelligence and Statistics (DGCI&S), and the Reserve Bank of India (RBI) "
    "for maintaining transparent, publicly accessible administrative records. The authors also thank academic supervisors and departmental mentors for valuable feedback.", body_style))

story.append(Paragraph("9. Conflict of Interest", h1_style))
story.append(Paragraph("The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence this work.", body_style))

story.append(Paragraph("10. Funding statement", h1_style))
story.append(Paragraph("This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.", body_style))

story.append(Paragraph("11. Author contributions", h1_style))
story.append(Paragraph("[AUTHOR_NAME_PLACEHOLDER]: Conceptualization, Methodology, Formal Data Curation, Econometric Estimation, Model Reconciliation, Visualization, Writing – Original Draft, Writing – Review & Editing.", body_style))

pdf_doc.build(story, canvasmaker=NumberedCanvas)
print(f"[OK] Successfully generated PDF Document: {PDF_PATH}")
print("Manuscript drafting complete!")
