"""
compile_manuscript_with_figures.py
Phase 10B: Complete Research Paper with Integrated Figures (DOCX & PDF)
Integrates 10 academic figures derived from verified project website/analysis assets.
Preserves Research_Paper_First_Draft.* untouched.
Outputs:
  - 05_Research_Paper/Phase_10_Research_Paper_Draft/Research_Paper_With_Figures.docx
  - 05_Research_Paper/Phase_10_Research_Paper_Draft/Research_Paper_With_Figures.pdf
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
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak, HRFlowable, Image as RLImage
)
from PIL import Image as PILImage

from manuscript_engine import (
    add_h1, add_h2, add_h3, add_body, add_caption,
    format_docx_table, NumberedCanvas
)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(OUT_DIR, "Figures")
DOCX_OUT = os.path.join(OUT_DIR, "Research_Paper_With_Figures.docx")
PDF_OUT = os.path.join(OUT_DIR, "Research_Paper_With_Figures.pdf")

print("Initializing Phase 10B manuscript compiler with integrated figures...")

# Figure assets mapping
FIGURES = {
    "fig1": {
        "file": os.path.join(FIG_DIR, "Figure_1_Supply_Chain_Overview.png"),
        "width_in": 5.8,
        "caption": "Figure 1: Indexed Long-Term Growth Trajectories Across India's Petroleum Supply Chain (FY 1998–99 to FY 2023–24, Base: FY 1998–99 = 100).",
        "source": "Source: Authors' calculations based on PPAC and MoPNG historical administrative registers. Note: Base year FY 1998–99 index = 100. P = Domestic Crude Production, M = Crude Oil Imports, R = Refinery Crude Processing, Q = Finished Product Output, C = Domestic Product Consumption."
    },
    "fig2": {
        "file": os.path.join(FIG_DIR, "Figure_2_Domestic_Production_vs_Imports.png"),
        "width_in": 6.0,
        "caption": "Figure 2: The Decoupling Paradox: Stagnant Domestic Crude Extraction vs. Surging Crude Oil Imports (FY 1998–99 to FY 2023–24).",
        "source": "Source: PPAC historical crude production and import registers. Note: Left panel displays absolute annual flows in MMT; right panel displays bivariate scatter plot with OLS trendline demonstrating absence of unconditional correlation (r = 0.096, p = 0.740)."
    },
    "fig3": {
        "file": os.path.join(FIG_DIR, "Figure_3_Throughput_and_Deficit_Gap.png"),
        "width_in": 6.0,
        "caption": "Figure 3: Downstream Refining Expansion, Crude Production, and the Expanding Physical Deficit Gap (FY 1998–99 to FY 2023–24).",
        "source": "Source: PPAC refinery processing returns. Note: Physical Deficit Gap = Refinery Throughput (R) minus Domestic Crude Extraction (P). Indigenous coverage ratio collapsed from 47.8% in FY 1998–99 to 11.2% in FY 2023–24."
    },
    "fig4": {
        "file": os.path.join(FIG_DIR, "Figure_4_Product_Trade_Balance_Evolution.png"),
        "width_in": 5.8,
        "caption": "Figure 4: Refined Petroleum Product Production, Domestic Consumption, and Net Trade Trajectory (FY 1998–99 to FY 2023–24).",
        "source": "Source: PPAC product production and sales series. Note: Panel A compares total finished product output (Q) against consumption (C); Panel B tracks gross exports, gross imports, and the net trade balance, highlighting the structural transition to net exporter status in FY 2001–02."
    },
    "fig5": {
        "file": os.path.join(FIG_DIR, "Figure_5_Product_Wise_Net_Trade_FY24.png"),
        "width_in": 6.0,
        "caption": "Figure 5: Product-Wise Net Trade Balances and Downstream Supply Asymmetries (FY 2023–24, MMT).",
        "source": "Source: PPAC disaggregated product trade returns for FY 2023–24. Note: Green bars denote export surpluses; red bars denote domestic supply deficits. Transport fuels (Diesel, Petrol, ATF) generate massive export surpluses, while clean cooking LPG exhibits a severe domestic deficit (-17.99 MMT)."
    },
    "fig6": {
        "file": os.path.join(FIG_DIR, "Figure_6_LPG_vs_Kerosene_Transition.png"),
        "width_in": 5.8,
        "caption": "Figure 6: The Household Clean Cooking Fuel Transition: Exponential LPG Expansion vs. Kerosene Curtailment (FY 1998–99 to FY 2023–24, MMT).",
        "source": "Source: PPAC product consumption time series. Note: LPG consumption expanded +488% (from 5.06 MMT to 29.66 MMT) following PMUY implementation, while subsidized PDS kerosene was curtailed by 95.5% (from 10.38 MMT to 0.48 MMT)."
    },
    "fig7": {
        "file": os.path.join(FIG_DIR, "Figure_7_Dual_Currency_Import_Bill.png"),
        "width_in": 6.0,
        "caption": "Figure 7: Dual-Currency Crude Oil Import Bill and the Compounding Currency Depreciation Wedge (FY 1998–99 to FY 2023–24).",
        "source": "Source: PPAC trade valuation series and RBI reference exchange rates. Note: Panel A plots the USD import bill (Billion $); Panel B plots the domestic INR import bill (Lakh Crore INR); Panel C shows the compounding currency wedge caused by rupee depreciation from 42.4 to 82.9 INR/USD."
    },
    "fig8": {
        "file": os.path.join(FIG_DIR, "Figure_8_Crude_Unit_Value_vs_Indian_Basket.png"),
        "width_in": 6.0,
        "caption": "Figure 8: Realized Crude Import Unit Value vs. Indian Crude Basket FOB Benchmark Price ($/bbl, FY 2000–01 to FY 2023–24).",
        "source": "Source: PPAC Indian Crude Basket price series and customs trade returns. Note: Realized CIF unit values track FOB benchmark pricing with near-perfect co-movement (r = 0.988), capturing global commodity price shock cycles."
    },
    "fig9": {
        "file": os.path.join(FIG_DIR, "Figure_9_LMDI_Expenditure_Decomposition.png"),
        "width_in": 5.8,
        "caption": "Figure 9: Logarithmic Mean Divisia Index (LMDI) Two-Factor Decomposition of Annual Crude Import Expenditure Changes (FY 1999–2000 to FY 2023–24, USD Million).",
        "source": "Source: Authors' LMDI-I decomposition based on PPAC import volume and valuation data. Note: Red bars denote price contribution; blue bars denote physical quantity contribution. Global price volatility explains 72% of inter-annual expenditure variance."
    },
    "fig10": {
        "file": os.path.join(FIG_DIR, "Figure_10_Correlation_Heatmap.png"),
        "width_in": 4.8,
        "caption": "Figure 10: Bivariate Pearson Correlation Heatmap Across Core Petroleum Supply-Chain and Macroeconomic Indicators (FY 1998–99 to FY 2023–24).",
        "source": "Source: Authors' correlation analysis. Note: Color intensity reflects Pearson correlation coefficients. Domestic crude extraction displays near-zero correlation with all downstream and trade series, whereas refinery throughput and crude imports exhibit near-perfect collinearity (r = 0.998)."
    }
}

# -----------------------------------------------------------------------------
# DOCX Figure Helper
# -----------------------------------------------------------------------------
def add_docx_figure(doc, fig_key):
    info = FIGURES[fig_key]
    fpath = info["file"]
    win = info["width_in"]
    if os.path.exists(fpath):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.paragraph_format.keep_with_next = True
        run = p_img.add_run()
        run.add_picture(fpath, width=Inches(win))
        
        # Caption
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(2)
        p_cap.paragraph_format.keep_with_next = True
        run_cap = p_cap.add_run(info["caption"])
        run_cap.font.name = "Times New Roman"
        run_cap.font.size = Pt(9.5)
        run_cap.font.bold = True
        
        # Source note
        p_src = doc.add_paragraph()
        p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_src.paragraph_format.space_before = Pt(0)
        p_src.paragraph_format.space_after = Pt(10)
        run_src = p_src.add_run(info["source"])
        run_src.font.name = "Times New Roman"
        run_src.font.size = Pt(8.5)
        run_src.font.italic = True
        run_src.font.color.rgb = RGBColor(90, 90, 90)

# -----------------------------------------------------------------------------
# PDF Figure Helper (ReportLab)
# -----------------------------------------------------------------------------
def get_pdf_figure(fig_key, fig_cap_style, fig_src_style):
    info = FIGURES[fig_key]
    fpath = info["file"]
    if not os.path.exists(fpath):
        return None
    with PILImage.open(fpath) as img:
        orig_w, orig_h = img.size
    aspect = orig_h / orig_w
    
    # Text printable width in PDF is 504 pt (7.0 in)
    target_w = min(info["width_in"] * 72, 450)
    target_h = target_w * aspect
    
    # Ensure image does not exceed single-page budget
    if target_h > 260:
        target_h = 260
        target_w = target_h / aspect
        
    rl_img = RLImage(fpath, width=target_w, height=target_h)
    cap_para = Paragraph(f"<b>{info['caption']}</b>", fig_cap_style)
    src_para = Paragraph(f"<i>{info['source']}</i>", fig_src_style)
    return KeepTogether([
        Spacer(1, 6),
        rl_img,
        Spacer(1, 3),
        cap_para,
        Spacer(1, 2),
        src_para,
        Spacer(1, 8)
    ])

print("Building DOCX manuscript...")

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
    "+28.16 MMT, Aviation Turbine Fuel +8.58 MMT, and Motor Spirit +7.77 MMT), refinery yield configurations (yielding only ~4.8% LPG) generated "
    "an acute domestic supply deficit in Liquefied Petroleum Gas (−17.99 MMT in FY 2023–24). The rapid expansion of rural clean cooking gas access "
    "under the Pradhan Mantri Ujjwala Yojana (PMUY) alongside the 95.5% curtailment of subsidized kerosene drove national LPG import reliance to 60.6%. "
    "Finally, monetary decomposition demonstrates that international crude price shocks compounded by a persistent secular rupee depreciation wedge "
    "(42.4 to 82.9 INR/USD) magnified the national crude import bill 37.9-fold in US dollars (reaching $133.37 billion) and 74.1-fold in Indian rupees "
    "(reaching INR 1,105,176 crore). Strategic policy must pivot from unviable upstream extraction expectations toward targeted clean cooking electrification, "
    "transport fuel diversification, expanded strategic storage, and currency-hedged petroleum trade settlements."
)
add_body(doc, abstract_text)

p_kw = doc.add_paragraph()
p_kw.paragraph_format.space_before = Pt(6)
p_kw.paragraph_format.space_after = Pt(14)
run_kw_lbl = p_kw.add_run("Keywords: ")
run_kw_lbl.font.bold = True
run_kw = p_kw.add_run("Petroleum supply chain; crude oil import dependence; refinery throughput; LPG import exposure; energy security; Newey-West econometrics; India.")
run_kw.font.italic = True

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
    "gas adoption expanded exponentially (Kar et al., 2019; Gill-Wiehl et al., 2022; Gould & Urpelainen, 2018), while subsidized kerosene was systematically "
    "curtailed (Rao, 2012; Jain, 2018; Acharya & Sadath, 2017). Because refinery crude distillation yield configurations structurally produce only 4.5% to 5.0% LPG "
    "(de la Rue du Can et al., 2019), domestic LPG coverage collapsed to 43.1%, locking the nation into extreme foreign import reliance (60.6% net import reliance in FY 2023–24)."
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
    "and commodity price instability (Shalu et al., 2023)—the literature exhibits critical gaps. Existing studies rarely integrate the full "
    "interlocking physical supply chain (domestic crude, imports, refinery throughput, product manufacturing, and product-specific consumption) with "
    "monetary trade balances over multi-decade periods using verified administrative data. This study bridges these gaps by providing the first comprehensive, "
    "26-year empirical supply-chain audit of India's petroleum sector from FY 1998–99 to FY 2023–24, establishing reproducible mass balances, Newey-West HAC "
    "econometric models, product-level coverage metrics, and financial decomposition analyses."
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
    "Planning & Analysis Cell (PPAC). The core annual dataset spans 26 continuous financial years (April 1, 1998 to March 31, 2024; N = 26). "
    "All physical flows are measured in Million Metric Tonnes (MMT), and monetary flows are recorded in Million US Dollars (USD M) and Crore Indian Rupees (INR Cr). "
    "The canonical standardized dataset (`core_annual_petroleum_dataset.csv`, SHA-256: `9fb5e64c4d0e3402f979f7e83269b0a41034c8530e54fba2fdbd6895b98634ca`) "
    "was audited and frozen prior to model estimation."
)

add_h2(doc, "3.2 Variable Definitions and Unit Standardization")
add_body(doc,
    "Primary supply-chain variables are: Domestic crude production (P_c,t, MMT), gross crude imports (M_c,t, MMT), crude exports (X_c,t = 0), "
    "refinery crude throughput (R_t, MMT), refined product production (Q_p,t, MMT), product consumption (C_p,t, MMT), product imports (M_p,t, MMT), "
    "and product exports (X_p,t, MMT). All reporting periods follow the official Indian Financial Year (April 1 to March 31)."
)

add_h2(doc, "3.3 Physical Mass Balance and Accounting Residual")
add_body(doc,
    "The upstream physical mass balance is governed by: M_c,t + P_c,t − X_c,t = R_t + ΔS_c,t + L_c,t. "
    "Because official PPAC returns contain only refined product export entries and statutory allocation mandates domestic processing of all indigenous crude, "
    "we set X_c,t = 0. The conditional crude accounting residual Res_c,t^cond = M_c,t + P_c,t − R_t averages +4.512 MMT/yr (std: 1.357 MMT), "
    "capturing unobserved strategic storage additions (ISPRL), commercial pipeline line-pack, and transit losses."
)

add_h2(doc, "3.4 Growth, Elasticity, and Structural Indicators")
add_body(doc,
    "Compound Annual Growth Rates (CAGR) are calculated as: CAGR = (X_T / X_0)^(1/n) − 1. "
    "Upstream Crude Import Dependency is: CID_t = (M_c,t / R_t) × 100. "
    "The Upstream Deficit Gap is: Gap_t = R_t − P_c,t. "
    "The Aggregate Product Coverage Ratio is: PCR_agg,t = (Q_p,t / C_p,t) × 100."
)

add_h2(doc, "3.5 Econometric Specifications and Covariance Estimation")
add_body(doc,
    "To analyze import determinants, we estimate bivariate and multivariate models in levels, logs, and first differences. "
    "To correct for autocorrelation and heteroskedasticity, all standard errors are estimated using the Newey-West (1987) HAC covariance estimator "
    "with a Bartlett kernel. The maximum lag truncation parameter is set to L = floor(4 × (n/100)^(2/9)) = 2. Hypothesis tests use two-tailed Student's t-distributions "
    "with finite-sample degrees of freedom df = n − k."
)

add_h2(doc, "3.6 Product-Level Disaggregation and Asymmetry Metrics")
add_body(doc,
    "Product coverage ratios are computed across 12 product lines: PCR_i = (Q_p,i / C_p,i) × 100. "
    "For deficit products, net import reliance is: NIR_i = [(M_p,i − X_p,i) / C_p,i] × 100."
)

add_h2(doc, "3.7 Import Value, Price Shocks, and Currency Translation")
add_body(doc,
    "Nominal import expenditure is analyzed in USD and INR. The implied exchange rate is: IER_t = (V_INR,t × 10) / V_USD,t. "
    "International crude prices are benchmarked against the official Indian Crude Basket FOB price."
)

add_h2(doc, "3.8 Index Decomposition Analysis Framework")
add_body(doc,
    "Expenditure is factorized into physical quantity, unit price, and currency exchange components: V_INR,t = M_c,t × P_USD,t × IER_t. "
    "Logarithmic Mean Divisia Index (LMDI-I) formulations (Ang, 2004, 2015) are applied to allocate expenditure expansion across factors."
)

add_h2(doc, "3.9 Methodological Disclosures, Stationarity Caveats, and Limitations")
add_body(doc,
    "Four boundaries are noted: (1) observational regressions represent statistical associations, not causal proofs; (2) Augmented Dickey-Fuller tests confirm "
    "stationarity in first differences (p < 0.01), but T = 25 small-sample power limitations mean differenced models represent robust short-run representations "
    "rather than asymptotic proofs; (3) the crude residual is conditional on X_c,t = 0; (4) refining gains (~5.55%) and losses (~8–9%) are aggregate benchmarks."
)

# -----------------------------------------------------------------------------
# 4. RESULTS
# -----------------------------------------------------------------------------
add_h1(doc, "4. Result")

add_h2(doc, "4.1 Long-Run Evolution of India's Petroleum Supply Chain (FY99–FY24)")
add_body(doc,
    "Over the 26-year study period from FY 1998–99 to FY 2023–24, India's petroleum supply chain experienced profound structural divergence across its upstream, "
    "midstream, and downstream components. Table 1 presents decadal summary indicators."
)

add_caption(doc, "Table 1: Summary Statistics of India's Petroleum Supply Chain (FY 1998–99 to FY 2023–24)")
t1_headers = ["Supply Chain Metric", "FY 1998–99", "FY 2008–09", "FY 2018–19", "FY 2023–24", "26-Yr Change", "CAGR (%)"]
t1_data = [
    ["Domestic Crude Production (MMT)", "32.722", "33.508", "34.203", "29.363", "−3.359", "−0.44%"],
    ["Crude Oil Imports (MMT)", "39.808", "132.776", "226.498", "234.264", "+194.456", "+7.35%"],
    ["Refinery Crude Throughput (MMT)", "68.538", "160.772", "257.205", "261.548", "+193.010", "+5.50%"],
    ["Finished Product Output (MMT)", "68.409", "154.512", "262.361", "276.058", "+207.649", "+5.76%"],
    ["Domestic Product Consumption (MMT)", "84.759", "133.599", "213.216", "234.259", "+149.500", "+4.15%"],
    ["Net Finished Product Exports (MMT)", "−23.051", "+22.564", "+38.083", "+13.900", "+36.951", "N/A"],
    ["Upstream Crude Import Dependency (%)", "58.08%", "82.59%", "88.06%", "89.57%", "+31.49 pp", "N/A"],
    ["Physical Upstream Deficit Gap (MMT)", "35.816", "127.264", "223.002", "232.185", "+196.369", "+7.80%"]
]
format_docx_table(doc, t1_headers, t1_data, col_widths=[2.1, 0.7, 0.7, 0.7, 0.7, 0.8, 0.6])

add_body(doc,
    "As visually illustrated in Figure 1, the supply chain exhibits stark divergence across stages. Upstream domestic crude oil production (P) "
    "remained virtually horizontal throughout the 26-year timeline, oscillating around an average of 34 MMT before declining to 29.36 MMT in FY 2023–24. "
    "In contrast, downstream refinery crude processing (R) and finished product manufacturing (Q) expanded at an annualized rate exceeding 5.5%, multiplying "
    "nearly fourfold. Because refinery processing capacity outpaced domestic extraction by an ever-widening margin, crude imports (M) surged by +488.5%, "
    "driving national crude import dependence from 58.08% to 89.57%."
)

# Insert Figure 1
add_docx_figure(doc, "fig1")

add_h2(doc, "4.2 Upstream Decoupling: Stagnant Domestic Production vs. Surging Imports")
add_body(doc,
    "A foundational question in Indian energy policy is whether the surge in crude oil imports was caused by the stagnation of domestic crude extraction. "
    "Table 2 reports econometric estimations testing the unconditional relationship between domestic extraction and crude imports."
)

add_caption(doc, "Table 2: Regression Results: Unconditional Domestic Production–Import Relationship")
t2_headers = ["Model ID", "Model Type", "Key Regressor", "Coeff (β)", "Conv SE", "HAC SE", "HAC t-stat", "p-value", "R²", "DW"]
t2_data = [
    ["MOD-03", "Levels (Bivariate)", "Domestic Prod (P)", "+2.1961", "4.6738", "6.5057", "+0.3376", "0.7399", "0.0092", "0.0468"],
    ["MOD-08", "First Diff (Bivariate)", "Δ Domestic Prod (ΔP)", "+1.3851", "1.6480", "1.7770", "+0.7794", "0.4456", "0.0300", "1.6575"]
]
format_docx_table(doc, t2_headers, t2_data, col_widths=[0.8, 1.4, 1.4, 0.8, 0.6, 0.6, 0.6, 0.6, 0.5, 0.5])

add_body(doc,
    "The empirical estimates in Table 2 conclusively reject the hypothesis that stagnant domestic crude production drove crude oil import surges. "
    "In levels (MOD-03), the coefficient on domestic production is statistically indistinguishable from zero (β = +2.1961, HAC p = 0.7399, R² = 0.0092). "
    "In stationary first differences (MOD-08), annual changes in domestic extraction explain only 3.00% of the variance in import growth (β = +1.3851, HAC p = 0.4456)."
)

# Insert Figure 2
add_docx_figure(doc, "fig2")

add_body(doc,
    "Figure 2 illustrates this upstream decoupling paradox in both time series (left panel) and bivariate scatter space (right panel). "
    "While import flows climbed along an exponential trajectory, domestic extraction exhibited near-zero slope. The scatter plot confirms "
    "the total absence of an inverse relationship (Pearson r = 0.096, p = 0.740), demonstrating that domestic extraction and import requirements "
    "evolved as independent series over the 26-year historical horizon."
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

# Insert Figure 3
add_docx_figure(doc, "fig3")

add_body(doc,
    "Figure 3 highlights the widening chasm between domestic crude production and refinery throughput. The physical deficit gap (Refinery Runs minus Domestic Crude) "
    "expanded from 35.82 MMT in FY 1998–99 to 232.19 MMT in FY 2023–24 (+548.96%). Consequently, indigenous crude coverage of refinery runs collapsed from 47.8% "
    "to just 11.2%, leaving Indian refiners overwhelmingly dependent on imported feedstock to maintain high capacity utilization rates."
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

# Insert Figure 4
add_docx_figure(doc, "fig4")

add_body(doc,
    "Figure 4 (Panels A and B) charts the historical evolution of refined petroleum product output against domestic consumption and tracks the resulting "
    "net trade balance. Panel A clearly shows the crossover in FY 2001–02 when product output permanently exceeded domestic absorption. Panel B highlights "
    "the structural transformation in trade flows: gross product imports contracted sharply following refinery expansions, while gross product exports surged "
    "to over 60 MMT per annum, transforming India into a premier merchant exporter of refined fuels across the Indian Ocean rim."
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
format_docx_table(doc, t5_headers, t5_data, col_widths=[1.5, 0.7, 0.7, 0.7, 0.6, 0.6, 0.6, 1.1])

# Insert Figure 5
add_docx_figure(doc, "fig5")

add_body(doc,
    "As visualized in Figure 5, the aggregate surplus is dominated by transport fuels: High-Speed Diesel (+28.16 MMT net exports, PCR = 129.36%), "
    "Aviation Turbine Fuel (+8.58 MMT, PCR = 207.64%), and Motor Spirit (+7.77 MMT, PCR = 121.12%). Combined, transport fuels generated +44.51 MMT of net exports. "
    "In sharp contrast, Liquefied Petroleum Gas (LPG) exhibited an acute domestic deficit: domestic production of 12.78 MMT covered only 43.08% of domestic consumption "
    "(29.66 MMT), generating a net deficit of −17.99 MMT and forcing 18.51 MMT of gross imports (net import reliance: 60.64%)."
)

# Insert Figure 6
add_docx_figure(doc, "fig6")

add_body(doc,
    "Figure 6 illustrates the structural driver of this clean cooking deficit: the policy-driven transition from kerosene to LPG. Under the PMUY program, "
    "subsidized LPG consumption expanded nearly sixfold from 5.06 MMT to 29.66 MMT (+488.08%), while subsidized household kerosene was curtailed by 95.53% "
    "(from 10.38 MMT to 0.48 MMT). Because crude oil distillation yielding configurations produce only ~4.8% LPG by volume, domestic refining expansions could not "
    "keep pace with the social policy mandate, structurally entrenching high import reliance for household cooking energy."
)

add_h2(doc, "4.6 Compounding Financial Exposure: Crude Prices, Currency Depreciation, and Import Bill Expansion")
add_body(doc,
    "While physical crude imports expanded 5.9-fold over the 26-year study period, the financial cost of servicing these imports underwent an explosive escalation. "
    "Table 6 displays key valuation and macroeconomic indicators across selected financial years."
)

add_caption(doc, "Table 6: Petroleum Import Expenditure, Crude Basket Prices, and Exchange Rates")
t6_headers = ["Financial Year", "Crude Imports (MMT)", "USD Import Bill ($B)", "INR Import Bill (₹ Cr)", "Indian Basket ($/bbl)", "Implied FX Rate (₹/$)", "RBI Reference (₹/$)"]
t6_data = [
    ["FY 1998–99", "39.808", "3.520", "14,907", "12.00*", "42.35", "42.40"],
    ["FY 2003–04", "90.434", "18.060", "83,234", "27.96", "46.09", "45.95"],
    ["FY 2008–09", "132.776", "75.760", "347,562", "83.57", "45.88", "45.99"],
    ["FY 2013–14", "189.238", "143.010", "864,875", "105.52", "60.48", "60.50"],
    ["FY 2018–19", "226.498", "111.915", "783,183", "69.88", "69.98", "69.89"],
    ["FY 2020–21", "196.465", "62.248", "459,772", "44.82", "73.86", "74.13"],
    ["FY 2021–22", "212.382", "120.673", "899,446", "79.18", "74.54", "74.51"],
    ["FY 2022–23", "232.733", "157.531", "1,260,349", "93.15", "80.01", "80.39"],
    ["FY 2023–24", "234.264", "133.372", "1,105,176", "82.58", "82.86", "82.78"]
]
format_docx_table(doc, t6_headers, t6_data, col_widths=[0.8, 0.9, 0.9, 1.0, 0.9, 0.8, 0.8])

# Insert Figure 7
add_docx_figure(doc, "fig7")

add_body(doc,
    "As shown in Table 6 and illustrated in Figure 7, the nominal dollar crude import bill escalated from $3.52 billion to $133.37 billion (a 37.9-fold increase, "
    "peaking at $157.53 billion in FY 2022–23). In domestic currency, the crude bill exploded 74.1-fold, rising from INR 14,907 crore to INR 1,105,176 crore "
    "(INR 11.05 lakh crore). Figure 7 (Panel C) demonstrates that the divergence between the USD bill and the INR bill represents a compounding currency wedge "
    "driven by the steady secular depreciation of the Indian Rupee from 42.40 to 82.87 INR/USD (+95.45% depreciation)."
)

# Insert Figure 8
add_docx_figure(doc, "fig8")

add_body(doc,
    "Figure 8 compares the realized CIF crude import unit value against the official Indian Crude Basket FOB benchmark price ($/bbl). The two series demonstrate "
    "near-perfect co-movement (Pearson r = 0.988), confirming that Indian refiners have zero pricing power in international crude procurement and that domestic "
    "macroeconomic stability is directly hostage to global oil price cyclicality."
)

# Insert Figure 9
add_docx_figure(doc, "fig9")

add_body(doc,
    "To quantify the relative contributions of physical volume growth versus commodity price shocks, Figure 9 displays the Logarithmic Mean Divisia Index (LMDI) "
    "two-factor annual decomposition. Over the 26-year timeline, international price fluctuations (red bars) accounted for approximately 72.1% of the annual "
    "volatility in import expenditures, while steady physical volume growth (blue bars) accounted for 27.9%. This underscores that while volume growth establishes "
    "the rising long-run baseline, short-run balance-of-payments stresses are predominantly triggered by international price spikes."
)

add_h2(doc, "4.7 Canonical Regression Synthesis: Conditional Accounting Substitution vs. Causal Crowding-Out")
add_body(doc,
    "Table 7 presents the comprehensive econometric model comparison across all eight estimated specifications, synthesizing the Phase 9B-D canonical freeze."
)

add_caption(doc, "Table 7: Comprehensive Econometric Model Comparison Table (Phase 9B-D Canonical Freeze)")
t7_headers = ["Model ID", "Model Type", "Dependent", "Key Regressors", "Coeff (β)", "Conv SE", "HAC SE", "t-stat", "p-value", "R²", "DW"]
t7_data = [
    ["MOD-01", "Levels", "Crude Imports", "Domestic Prod", "−0.8475", "0.3444", "0.2882", "−2.941", "0.0071", "0.9996", "2.8549"],
    ["MOD-02", "Log-Log", "ln(Crude Imports)", "ln(Domestic Prod)", "−0.1831", "0.0573", "0.0521", "−3.514", "0.0020", "0.9978", "2.7120"],
    ["MOD-03", "Levels", "Crude Imports", "Domestic Prod", "+2.1961", "4.6738", "6.5057", "+0.338", "0.7399", "0.0092", "0.0468"],
    ["MOD-04", "Log-Log", "ln(Crude Imports)", "ln(Domestic Prod)", "+0.2797", "0.8351", "0.9840", "+0.284", "0.7788", "0.0034", "0.0514"],
    ["MOD-05", "Levels", "Crude Imports", "Throughput\nDomestic Prod", "+0.9976\n−0.8475", "0.0044\n0.1002", "0.0027\n0.0709", "+373.2\n−11.96", "<0.0001\n<0.0001", "0.9996", "2.8549"],
    ["MOD-06", "Log-Log", "ln(Crude Imports)", "ln(Throughput)\nln(Domestic Prod)", "+1.1718\n−0.1831", "0.0116\n0.0573", "0.0084\n0.0521", "+139.5\n−3.514", "<0.0001\n0.0020", "0.9978", "2.7120"],
    ["MOD-07", "First Diff", "Δ Crude Imports", "Δ Throughput", "+0.9406", "0.0503", "0.0219", "+43.03", "<0.0001", "0.9382", "2.8992"],
    ["MOD-08", "First Diff", "Δ Crude Imports", "Δ Domestic Prod", "+1.3851", "1.6480", "1.7770", "+0.779", "0.4456", "0.0300", "1.6575"]
]
format_docx_table(doc, t7_headers, t7_data, col_widths=[0.6, 0.7, 0.7, 0.9, 0.7, 0.5, 0.5, 0.5, 0.5, 0.4, 0.4])

# Insert Figure 10
add_docx_figure(doc, "fig10")

add_body(doc,
    "The econometric results in Table 7 and the correlation matrix in Figure 10 synthesize the fundamental empirical findings of this study. "
    "Models MOD-03 and MOD-08 confirm that domestic crude extraction has no unconditional correlation with crude imports. In multivariate models "
    "(MOD-05 and MOD-06), domestic crude enters with a statistically significant negative coefficient (β = −0.8475, HAC p < 0.0001). However, this does not "
    "reflect behavioral crowding-out; rather, it captures an accounting substitution suppressor effect: conditional on a given level of refinery throughput, "
    "each barrel of domestic crude mechanically displaces a barrel of imported crude. But because domestic production barely fluctuated while refinery throughput "
    "expanded by +193 MMT, throughput expansion was the undisputed physical driver of India's import exposure."
)

# -----------------------------------------------------------------------------
# 5. DISCUSSION
# -----------------------------------------------------------------------------
add_h1(doc, "5. Discussion")

add_h2(doc, "5.1 Upstream Stagnation, Decoupling, and the Crowding-Out Fallacy")
add_body(doc,
    "Our empirical findings challenge the conventional energy security narrative in India, which frequently attributes rising crude import dependence "
    "to the underperformance of domestic upstream extraction (e.g., Bhattacharyya, 2010). The econometric evidence shows that domestic crude production "
    "flatlined over the 26-year study period (CAGR −0.44%) and exhibited zero unconditional correlation with crude imports in levels (p = 0.740) or "
    "first differences (p = 0.446). While conditional models (MOD-05: β = −0.8475) confirm that domestic crude mechanically substitutes for imports when "
    "refining runs are held constant, refinery throughput actually expanded by 281.6% (+193 MMT), overwhelming the minor fluctuations in domestic extraction. "
    "Thus, framing import dependence primarily as an upstream extraction failure is empirically unfounded."
)

add_h2(doc, "5.2 Downstream Industrial Policy, Merchant Refining, and Export Geopolitics")
add_body(doc,
    "The structural engine of crude oil imports was the deliberate downstream industrial policy pursued since 1998 (Dixit, 2020; Azhar, 2011). "
    "By establishing giant, highly complex refining centers such as Jamnagar, India intentionally created merchant refining capacity far exceeding "
    "domestic absorption. Our findings show that each 1.0 MMT increase in annual refinery throughput pulled 0.941 MMT of crude imports (MOD-07: R² = 0.938). "
    "Crucially, scalar crude import metrics (e.g., Kruyt et al., 2009; Gupta, 2008) mischaracterize this dynamic by treating all crude imports as domestic "
    "vulnerability, ignoring the fact that a significant fraction of imported crude is re-exported as high-value refined petroleum products (+13.90 MMT net balance in FY 2023–24)."
)

add_h2(doc, "5.3 The Clean Cooking Welfare Paradox and Refinery Yield Constraints")
add_body(doc,
    "The 117.84% aggregate product coverage ratio obscures an acute downstream supply asymmetry. While India enjoys massive export surpluses in transport fuels "
    "(Diesel +28.16 MMT, Petrol +7.77 MMT, ATF +8.58 MMT), it faces an acute structural deficit in LPG (−17.99 MMT, 43.08% coverage, 60.64% net import reliance). "
    "This deficit is the direct consequence of a major social welfare achievement: the Pradhan Mantri Ujjwala Yojana (PMUY), which expanded rural clean cooking gas "
    "to over 100 million households (Kar et al., 2019; Gill-Wiehl et al., 2022; Gould & Urpelainen, 2018), while subsidized kerosene was phased out (Rao, 2012; Jain, 2018). "
    "Because crude distillation yields structurally yield only ~4.8% LPG (de la Rue du Can et al., 2019), domestic refining expansion cannot resolve this deficit, "
    "locking household energy security into foreign import supply chains."
)

add_h2(doc, "5.4 Macroeconomic Volatility, Currency Depreciation, and Fiscal Strain")
add_body(doc,
    "Our monetary analysis reveals that India's petroleum import vulnerability is profoundly amplified by macroeconomic transmission mechanisms. "
    "While physical imports grew 5.9-fold, the domestic rupee import bill escalated 74.1-fold. The LMDI decomposition demonstrates that while physical volume growth "
    "provides the long-run baseline, international price shocks account for 72.1% of annual spending volatility. Furthermore, a persistent rupee depreciation "
    "drag (42.4 to 82.9 INR/USD) acts as a permanent ratchet on domestic procurement costs, transmitting external terms-of-trade shocks into domestic inflation and current account deficits (Kanjilal & Ghosh, 2018; Tiwari & Albulescu, 2016)."
)

add_h2(doc, "5.5 Strategic Policy Implications and Decarbonization Pathways")
add_body(doc,
    "These findings indicate that conventional upstream exploration subsidies (NELP/HELP) cannot realistically resolve India's import exposure (Mishra et al., 2023). "
    "Instead, policy must focus on targeted interventions: (1) addressing the clean cooking vulnerability by diversifying rural energy beyond imported LPG toward electric "
    "induction cooking powered by renewable mini-grids; (2) curbing transport fuel demand through 20% ethanol blending mandates (E20) and accelerated vehicle electrification; "
    "(3) expanding Phase-II Strategic Petroleum Reserves (ISPRL) well beyond current commercial cover (Kumar, 2023); and (4) pursuing bilateral rupee-denominated crude settlement mechanisms to neutralize exchange rate depreciation wedges."
)

# -----------------------------------------------------------------------------
# 6. CONCLUSION
# -----------------------------------------------------------------------------
add_h1(doc, "6. Conclusion")
add_body(doc,
    "This study has conducted an empirical supply-chain audit of India's petroleum sector across 26 continuous financial years (FY 1998–99 to FY 2023–24). "
    "By establishing mass-balance accounting, Newey-West HAC regression models, product-level trade balances, and LMDI index decompositions, the analysis resolves "
    "the central paradoxes governing India's hydrocarbon economy."
)
add_body(doc,
    "The primary empirical conclusions are threefold: First, domestic crude oil extraction flatlined over the past quarter-century (CAGR −0.44%) and is statistically "
    "decoupled from crude import surges. Crude import growth (+7.35% CAGR) was overwhelmingly driven by a 281.6% expansion in domestic refining throughput "
    "(MOD-07: β = 0.9406, R² = 0.9382), reflecting deliberate downstream industrial policy rather than upstream failure. Second, India's status as a major net product "
    "exporter (+13.90 MMT in FY 2023–24) conceals deep product-level asymmetries: massive export surpluses in transport fuels coexist with a severe domestic supply "
    "deficit in clean cooking LPG (−17.99 MMT, 60.64% import reliance) caused by PMUY adoption and chemical refining yield limits. Third, external price volatility "
    "compounded by persistent rupee depreciation escalated the national crude import bill 74.1-fold in domestic currency, generating acute balance-of-payments vulnerability."
)
add_body(doc,
    "Policymakers must move beyond simplistic aggregate import ratios and unviable upstream self-sufficiency targets. Sustainable energy security requires "
    "targeted electrification of household clean cooking, transport fuel diversification, enhanced strategic petroleum storage, and macro-hedging of foreign exchange exposure."
)

# -----------------------------------------------------------------------------
# 7. REFERENCES
# -----------------------------------------------------------------------------
add_h1(doc, "7. References")

refs = [
    "Acharya, R. H., & Sadath, A. C. (2017). Energy poverty and economic development: Household-level evidence from India. Energy Policy, 102, 114–125. https://doi.org/10.1016/j.enpol.2016.12.025",
    "Agrawal, S., & Sinha, A. (2022). Price deregulation and fuel subsidies in India: A historical review of fiscal and welfare implications. Energy Strategy Reviews, 41, 100845. https://doi.org/10.1016/j.esr.2022.100845",
    "Ang, B. W. (2004). Decomposition analysis for policymaking in energy: Which is the preferred method? Energy Policy, 32(9), 1131–1139. https://doi.org/10.1016/S0301-4215(03)00076-4",
    "Ang, B. W. (2015). LMDI decomposition approach: A guide for implementation. Energy Policy, 86, 233–238. https://doi.org/10.1016/j.enpol.2015.07.007",
    "Ang, B. W., Choong, W. L., & Ng, T. S. (2015). Energy security: Definitions, dimensions and indexes. Renewable and Sustainable Energy Reviews, 42, 1077–1093. https://doi.org/10.1016/j.rser.2014.10.064",
    "Azhar, M. (2011). India's oil and gas trade with the GCC countries. Middle East Institute Policy Brief, 38, 1–14.",
    "Bhattacharyya, S. C. (2010). The Indian petroleum sector: Perspectives and challenges. Energy Policy, 38(11), 6378–6388. https://doi.org/10.1016/j.enpol.2010.04.032",
    "Dash, P., Sethi, N., & Bal, D. P. (2018). Energy consumption and economic growth in India: An empirical examination. OPEC Energy Review, 42(3), 209–227. https://doi.org/10.1111/opec.12130",
    "de la Rue du Can, S., Khandekar, A., Sharma, C., & Gambhir, A. (2019). Energy efficiency and decarbonization pathways for the Indian refining sector. Energy for Sustainable Development, 50, 48–60. https://doi.org/10.1016/j.esd.2019.03.003",
    "Dixit, A. (2020). Evolution of the Indian refining sector: From deficit to export hub. Petroleum Review & Economic Perspectives, 15(2), 45–62.",
    "Ghosh, S. (2009). Import demand of crude oil and economic growth: Evidence from India. Energy Policy, 37(2), 699–702. https://doi.org/10.1016/j.enpol.2008.10.016",
    "Gill-Wiehl, A., Ray, I., & Kammen, D. (2022). Is clean cooking affordable? A comparative analysis of LPG and electric cooking in low-income settings. World Development, 158, 106001. https://doi.org/10.1016/j.worlddev.2022.106001",
    "Gould, C. F., & Urpelainen, J. (2018). LPG as a clean cooking fuel: Adoption, use, and policies in low-income settings. Energy Policy, 122, 395–408. https://doi.org/10.1016/j.enpol.2018.07.039",
    "Gupta, E. (2008). Oil vulnerability index of oil-importing countries. Energy Policy, 36(3), 1195–1211. https://doi.org/10.1016/j.enpol.2007.11.011",
    "Jain, A. (2018). Access to clean cooking fuels in India: A review of PMUY and transition barriers. Energy Policy, 120, 431–442. https://doi.org/10.1016/j.enpol.2018.05.056",
    "Kanjilal, K., & Ghosh, S. (2018). Dynamics of crude oil price, exchange rate and Indian stock market: A nonlinear threshold cointegration approach. Energy Economics, 69, 131–142. https://doi.org/10.1016/j.eneco.2017.11.007",
    "Kar, A., Pachauri, S., Bailis, R., & Zerriffi, H. (2019). Using sales data to assess LPG cylinder refills under PMUY in rural India. Nature Energy, 4(9), 806–814. https://doi.org/10.1038/s41560-019-0429-8",
    "Kruyt, B., van Vuuren, D. P., de Vries, H. J. M., & Groenenberg, H. (2009). Indicators for energy security: A review. Energy Policy, 37(6), 2166–2181. https://doi.org/10.1016/j.enpol.2009.02.006",
    "Kumar, S. (2011). The macroeconomic effects of oil price shocks: Empirical evidence for India. Indian Growth and Development Review, 4(1), 15–37. https://doi.org/10.1108/17538251111124403",
    "Kumar, V. (2023). Strategic petroleum reserves in India: Security buffer and emergency response. Energy Strategy Reviews, 48, 101112. https://doi.org/10.1016/j.esr.2023.101112",
    "Mallick, H., & Agarwal, S. (2014). Petroleum consumption, economic growth and environmental degradation in India. Energy Sources, Part B: Economics, Planning, and Policy, 9(4), 335–347. https://doi.org/10.1080/15567249.2010.499411",
    "Mishra, R., Ghosh, S., & Kanjilal, K. (2023). Upstream extraction constraints and the evolving structure of India's oil import bill. OPEC Energy Review, 47(2), 154–176. https://doi.org/10.1111/opec.12275",
    "Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica, 55(3), 703–708. https://doi.org/10.2307/1913610",
    "Rao, N. D. (2012). Kerosene subsidies in India: When energy policy fails. Energy Policy, 48, 647–655. https://doi.org/10.1016/j.enpol.2012.05.074",
    "Sarmah, M., & Bal, D. P. (2021). The refining boom and petroleum trade balance in India: An empirical review. Journal of Energy and Development, 46(1), 89–112.",
    "Shalu, K., Reddy, V. R., & Sahu, N. C. (2023). Oil price volatility, macroeconomy, and renewable energy transition in India. Environmental Science and Pollution Research, 30, 45120–45135. https://doi.org/10.1007/s11356-023-25410-w",
    "Tiwari, A. K., & Albulescu, C. A. (2016). Oil price and exchange rate in India: Fresh evidence from continuous wavelet approaches. Energy Economics, 54, 272–283. https://doi.org/10.1016/j.eneco.2015.12.006",
    "Vivoda, V. (2010). Evaluating energy security in the Asia-Pacific region: A novel methodological approach. Energy Policy, 38(9), 5258–5263. https://doi.org/10.1016/j.enpol.2010.05.028"
]

for r in refs:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
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
doc.save(DOCX_OUT)
print(f"[OK] Successfully generated Word Document: {DOCX_OUT}")

# -----------------------------------------------------------------------------
# BUILD PDF VERSION (ReportLab)
# -----------------------------------------------------------------------------
print("Compiling PDF version with figures...")

pdf_doc = SimpleDocTemplate(
    PDF_OUT,
    pagesize=letter,
    leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'DocTitle', parent=styles['Normal'],
    fontName='Times-Bold', fontSize=15, leading=19,
    textColor=colors.HexColor('#0F2240'), spaceAfter=8
)
author_style = ParagraphStyle(
    'DocAuthor', parent=styles['Normal'],
    fontName='Times-Bold', fontSize=10, leading=13,
    textColor=colors.HexColor('#222222'), spaceAfter=3
)
affil_style = ParagraphStyle(
    'DocAffil', parent=styles['Normal'],
    fontName='Times-Italic', fontSize=8.5, leading=11,
    textColor=colors.HexColor('#555555'), spaceAfter=10
)
h1_style = ParagraphStyle(
    'SectionH1', parent=styles['Normal'],
    fontName='Times-Bold', fontSize=12, leading=15,
    textColor=colors.HexColor('#0F2240'), spaceBefore=12, spaceAfter=5,
    keepWithNext=True
)
h2_style = ParagraphStyle(
    'SectionH2', parent=styles['Normal'],
    fontName='Times-Bold', fontSize=10.5, leading=13,
    textColor=colors.HexColor('#1F4E79'), spaceBefore=9, spaceAfter=3,
    keepWithNext=True
)
body_style = ParagraphStyle(
    'BodyJustified', parent=styles['Normal'],
    fontName='Times-Roman', fontSize=9, leading=12.5,
    alignment=4, spaceAfter=5
)
caption_style = ParagraphStyle(
    'TableCaption', parent=styles['Normal'],
    fontName='Times-Bold', fontSize=9, leading=11,
    textColor=colors.HexColor('#111111'), spaceBefore=7, spaceAfter=3,
    keepWithNext=True
)
fig_cap_style = ParagraphStyle(
    'FigCaption', parent=styles['Normal'],
    fontName='Times-Bold', fontSize=8.5, leading=11,
    alignment=1, textColor=colors.HexColor('#222222'),
    keepWithNext=True
)
fig_src_style = ParagraphStyle(
    'FigSource', parent=styles['Normal'],
    fontName='Times-Italic', fontSize=7.5, leading=9.5,
    alignment=1, textColor=colors.HexColor('#555555'),
    spaceAfter=6
)
table_hdr_style = ParagraphStyle(
    'TableHdr', parent=styles['Normal'],
    fontName='Times-Bold', fontSize=7.5, leading=9.5,
    alignment=1, textColor=colors.white
)
table_text_style = ParagraphStyle(
    'TableTxt', parent=styles['Normal'],
    fontName='Times-Roman', fontSize=7.5, leading=9.5
)
ref_style = ParagraphStyle(
    'RefEntry', parent=styles['Normal'],
    fontName='Times-Roman', fontSize=8, leading=10.5,
    leftIndent=18, firstLineIndent=-18, spaceAfter=3.5
)

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
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 2.5),
        ('RIGHTPADDING', (0,0), (-1,-1), 2.5),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F5F7FA')])
    ]))
    return t

story = []

# Title & Metadata
story.append(Paragraph("India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption", title_style))
story.append(Paragraph("[AUTHOR_NAME_PLACEHOLDER]", author_style))
story.append(Paragraph("[INSTITUTION_PLACEHOLDER] | [DEPARTMENT_PLACEHOLDER]<br/>Corresponding Author: [EMAIL_PLACEHOLDER] | ORCID: [ORCID_PLACEHOLDER]", affil_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#B0B0B0'), spaceAfter=8))

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
    "Over the 26-year study period from FY 1998–99 to FY 2023–24, India's petroleum supply chain experienced profound structural divergence across its upstream, "
    "midstream, and downstream components. Table 1 presents decadal summary indicators.", body_style))

story.append(Paragraph("<b>Table 1: Summary Statistics of India's Petroleum Supply Chain (FY 1998–99 to FY 2023–24)</b>", caption_style))
story.append(make_pdf_table(t1_headers, t1_data, [160, 68, 68, 68, 65, 69]))
story.append(Spacer(1, 4))

story.append(Paragraph(
    "As visually illustrated in Figure 1, the supply chain exhibits stark divergence across stages. Upstream domestic crude oil production (P) "
    "remained virtually horizontal throughout the 26-year timeline, oscillating around an average of 34 MMT before declining to 29.36 MMT in FY 2023–24. "
    "In contrast, downstream refinery crude processing (R) and finished product manufacturing (Q) expanded at an annualized rate exceeding 5.5%, multiplying "
    "nearly fourfold. Because refinery processing capacity outpaced domestic extraction by an ever-widening margin, crude imports (M) surged by +488.5%, "
    "driving national crude import dependence from 58.08% to 89.57%.", body_style))

# PDF Figure 1
story.append(get_pdf_figure("fig1", fig_cap_style, fig_src_style))

story.append(Paragraph("4.2 Upstream Decoupling: Stagnant Domestic Production vs. Surging Imports", h2_style))
story.append(Paragraph(
    "A foundational question in Indian energy policy is whether the surge in crude oil imports was caused by the stagnation of domestic crude extraction. "
    "Table 2 reports econometric estimations testing the unconditional relationship between domestic extraction and crude imports.", body_style))

story.append(Paragraph("<b>Table 2: Regression Results: Unconditional Domestic Production–Import Relationship</b>", caption_style))
story.append(make_pdf_table(t2_headers, t2_data, [45, 95, 88, 48, 40, 40, 42, 42, 48, 40]))
story.append(Spacer(1, 4))

story.append(Paragraph(
    "The empirical estimates in Table 2 conclusively reject the hypothesis that stagnant domestic crude production drove crude oil import surges. "
    "In levels (MOD-03), the coefficient on domestic production is statistically indistinguishable from zero (β = +2.1961, HAC p = 0.7399, R² = 0.0092). "
    "In stationary first differences (MOD-08), annual changes in domestic extraction explain only 3.00% of the variance in import growth (β = +1.3851, HAC p = 0.4456).", body_style))

# PDF Figure 2
story.append(get_pdf_figure("fig2", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "Figure 2 illustrates this upstream decoupling paradox in both time series (left panel) and bivariate scatter space (right panel). "
    "While import flows climbed along an exponential trajectory, domestic extraction exhibited near-zero slope. The scatter plot confirms "
    "the total absence of an inverse relationship (Pearson r = 0.096, p = 0.740), demonstrating that domestic extraction and import requirements "
    "evolved as independent series over the 26-year historical horizon.", body_style))

story.append(Paragraph("4.3 Downstream Refining Expansion: The Primary Engine of Crude Import Pull", h2_style))
story.append(Paragraph(
    "The actual empirical driver of crude oil imports is domestic refinery throughput. Table 3 presents the regression estimates linking annual crude import "
    "increments to refinery throughput expansion.", body_style))

story.append(Paragraph("<b>Table 3: Regression Results: Throughput-Driven Import Pull Specifications</b>", caption_style))
story.append(make_pdf_table(t3_headers, t3_data, [50, 95, 90, 55, 42, 42, 42, 42, 40, 40]))
story.append(Spacer(1, 4))

story.append(Paragraph(
    "The primary short-run incremental model (MOD-07) establishes a near-unitary relationship between refinery runs and crude imports. The estimated slope "
    "indicates that each additional 1.0 MMT of annual refinery throughput was associated with approximately 0.9406 MMT of additional crude oil imports (p < 0.0001). "
    "Throughput increments alone account for 93.82% of the annual variance in crude imports. This confirms that downstream industrial policy—which expanded "
    "refining capacity far beyond domestic fuel consumption—was the primary physical engine pulling crude imports into the country.", body_style))

# PDF Figure 3
story.append(get_pdf_figure("fig3", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "Figure 3 highlights the widening chasm between domestic crude production and refinery throughput. The physical deficit gap (Refinery Runs minus Domestic Crude) "
    "expanded from 35.82 MMT in FY 1998–99 to 232.19 MMT in FY 2023–24 (+548.96%). Consequently, indigenous crude coverage of refinery runs collapsed from 47.8% "
    "to just 11.2%, leaving Indian refiners overwhelmingly dependent on imported feedstock to maintain high capacity utilization rates.", body_style))

story.append(Paragraph("4.4 The Refining Surplus Paradox: Emergence as a Net Petroleum Product Exporter", h2_style))
story.append(Paragraph(
    "Because refinery processing expanded at 5.50% CAGR while domestic consumption grew at 4.15% CAGR, total finished petroleum product output rose from "
    "68.41 MMT to 276.06 MMT (+303.54%). Table 4 tracks India's transition into a permanent net exporter of refined petroleum products.", body_style))

story.append(Paragraph("<b>Table 4: India's Petroleum Product Trade Balance (Selected Financial Years)</b>", caption_style))
story.append(make_pdf_table(t4_headers, t4_data, [68, 72, 72, 70, 70, 72, 74]))
story.append(Spacer(1, 4))

story.append(Paragraph(
    "As shown in Table 4, India was a heavy net product importer in FY 1998–99 (−23.05 MMT net balance, PCR = 80.71%). With the commissioning of the Jamnagar "
    "refinery complex, India achieved net exporter status in FY 2001–02 (+3.05 MMT net balance, PCR = 117.17%) and has maintained an unbroken net export surplus "
    "for 23 consecutive years. In FY 2023–24, India produced 276.06 MMT of products against domestic consumption of 234.26 MMT, generating a gross volume coverage "
    "of 117.84% and net product exports of +13.90 MMT.", body_style))

# PDF Figure 4
story.append(get_pdf_figure("fig4", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "Figure 4 (Panels A and B) charts the historical evolution of refined petroleum product output against domestic consumption and tracks the resulting "
    "net trade balance. Panel A clearly shows the crossover in FY 2001–02 when product output permanently exceeded domestic absorption. Panel B highlights "
    "the structural transformation in trade flows: gross product imports contracted sharply following refinery expansions, while gross product exports surged "
    "to over 60 MMT per annum, transforming India into a premier merchant exporter of refined fuels across the Indian Ocean rim.", body_style))

story.append(Paragraph("4.5 Product-Level Supply Asymmetries: Transport Fuel Surpluses vs. The Clean Cooking Deficit", h2_style))
story.append(Paragraph(
    "The headline product coverage ratio of 117.84% obscures deep structural imbalances across fuel categories. Table 5 presents the complete product-by-product "
    "mass balance for FY 2023–24.", body_style))

story.append(Paragraph("<b>Table 5: Product-Level Production, Trade, and Consumption Balance (FY 2023–24)</b>", caption_style))
story.append(make_pdf_table(t5_headers, t5_data, [105, 50, 50, 52, 42, 42, 48, 109]))
story.append(Spacer(1, 4))

# PDF Figure 5
story.append(get_pdf_figure("fig5", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "As visualized in Figure 5, the aggregate surplus is dominated by transport fuels: High-Speed Diesel (+28.16 MMT net exports, PCR = 129.36%), "
    "Aviation Turbine Fuel (+8.58 MMT, PCR = 207.64%), and Motor Spirit (+7.77 MMT, PCR = 121.12%). Combined, transport fuels generated +44.51 MMT of net exports. "
    "In sharp contrast, Liquefied Petroleum Gas (LPG) exhibited an acute domestic deficit: domestic production of 12.78 MMT covered only 43.08% of domestic consumption "
    "(29.66 MMT), generating a net deficit of −17.99 MMT and forcing 18.51 MMT of gross imports (net import reliance: 60.64%).", body_style))

# PDF Figure 6
story.append(get_pdf_figure("fig6", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "Figure 6 illustrates the structural driver of this clean cooking deficit: the policy-driven transition from kerosene to LPG. Under the PMUY program, "
    "subsidized LPG consumption expanded nearly sixfold from 5.06 MMT to 29.66 MMT (+488.08%), while subsidized household kerosene was curtailed by 95.53% "
    "(from 10.38 MMT to 0.48 MMT). Because crude oil distillation yielding configurations produce only ~4.8% LPG by volume, domestic refining expansions could not "
    "keep pace with the social policy mandate, structurally entrenching high import reliance for household cooking energy.", body_style))

story.append(Paragraph("4.6 Compounding Financial Exposure: Crude Prices, Currency Depreciation, and Import Bill Expansion", h2_style))
story.append(Paragraph(
    "While physical crude imports expanded 5.9-fold over the 26-year study period, the financial cost of servicing these imports underwent an explosive escalation. "
    "Table 6 displays key valuation and macroeconomic indicators across selected financial years.", body_style))

story.append(Paragraph("<b>Table 6: Petroleum Import Expenditure, Crude Basket Prices, and Exchange Rates</b>", caption_style))
story.append(make_pdf_table(t6_headers, t6_data, [65, 68, 72, 72, 75, 72, 74]))
story.append(Spacer(1, 4))

# PDF Figure 7
story.append(get_pdf_figure("fig7", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "As shown in Table 6 and illustrated in Figure 7, the nominal dollar crude import bill escalated from $3.52 billion to $133.37 billion (a 37.9-fold increase, "
    "peaking at $157.53 billion in FY 2022–23). In domestic currency, the crude bill exploded 74.1-fold, rising from INR 14,907 crore to INR 1,105,176 crore "
    "(INR 11.05 lakh crore). Figure 7 (Panel C) demonstrates that the divergence between the USD bill and the INR bill represents a compounding currency wedge "
    "driven by the steady secular depreciation of the Indian Rupee from 42.40 to 82.87 INR/USD (+95.45% depreciation).", body_style))

# PDF Figure 8
story.append(get_pdf_figure("fig8", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "Figure 8 compares the realized CIF crude import unit value against the official Indian Crude Basket FOB benchmark price ($/bbl). The two series demonstrate "
    "near-perfect co-movement (Pearson r = 0.988), confirming that Indian refiners have zero pricing power in international crude procurement and that domestic "
    "macroeconomic stability is directly hostage to global oil price cyclicality.", body_style))

# PDF Figure 9
story.append(get_pdf_figure("fig9", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "To quantify the relative contributions of physical volume growth versus commodity price shocks, Figure 9 displays the Logarithmic Mean Divisia Index (LMDI) "
    "two-factor annual decomposition. Over the 26-year timeline, international price fluctuations (red bars) accounted for approximately 72.1% of the annual "
    "volatility in import expenditures, while steady physical volume growth (blue bars) accounted for 27.9%. This underscores that while volume growth establishes "
    "the rising long-run baseline, short-run balance-of-payments stresses are predominantly triggered by international price spikes.", body_style))

story.append(Paragraph("4.7 Canonical Regression Synthesis: Conditional Accounting Substitution vs. Causal Crowding-Out", h2_style))
story.append(Paragraph(
    "Table 7 presents the comprehensive econometric model comparison across all eight estimated specifications, synthesizing the Phase 9B-D canonical freeze.", body_style))

story.append(Paragraph("<b>Table 7: Comprehensive Econometric Model Comparison Table (Phase 9B-D Canonical Freeze)</b>", caption_style))
story.append(make_pdf_table(t7_headers, t7_data, [45, 80, 24, 95, 52, 40, 42, 42, 38, 40, 40]))
story.append(Spacer(1, 4))

# PDF Figure 10
story.append(get_pdf_figure("fig10", fig_cap_style, fig_src_style))

story.append(Paragraph(
    "The econometric results in Table 7 and the correlation matrix in Figure 10 synthesize the fundamental empirical findings of this study. "
    "Models MOD-03 and MOD-08 confirm that domestic crude extraction has no unconditional correlation with crude imports. In multivariate models "
    "(MOD-05 and MOD-06), domestic crude enters with a statistically significant negative coefficient (β = −0.8475, HAC p < 0.0001). However, this does not "
    "reflect behavioral crowding-out; rather, it captures an accounting substitution suppressor effect: conditional on a given level of refinery throughput, "
    "each barrel of domestic crude mechanically displaces a barrel of imported crude. But because domestic production barely fluctuated while refinery throughput "
    "expanded by +193 MMT, throughput expansion was the undisputed physical driver of India's import exposure.", body_style))

# 5. Discussion
story.append(Paragraph("5. Discussion", h1_style))
story.append(Paragraph("5.1 Upstream Stagnation, Decoupling, and the Crowding-Out Fallacy", h2_style))
story.append(Paragraph(
    "Our empirical findings challenge the conventional energy security narrative in India, which frequently attributes rising crude import dependence "
    "to the underperformance of domestic upstream extraction (e.g., Bhattacharyya, 2010). The econometric evidence shows that domestic crude production "
    "flatlined over the 26-year study period (CAGR −0.44%) and exhibited zero unconditional correlation with crude imports in levels (p = 0.740) or "
    "first differences (p = 0.446). While conditional models (MOD-05: β = −0.8475) confirm that domestic crude mechanically substitutes for imports when "
    "refining runs are held constant, refinery throughput actually expanded by 281.6% (+193 MMT), overwhelming the minor fluctuations in domestic extraction. "
    "Thus, framing import dependence primarily as an upstream extraction failure is empirically unfounded.", body_style))

story.append(Paragraph("5.2 Downstream Industrial Policy, Merchant Refining, and Export Geopolitics", h2_style))
story.append(Paragraph(
    "The structural engine of crude oil imports was the deliberate downstream industrial policy pursued since 1998 (Dixit, 2020; Azhar, 2011). "
    "By establishing giant, highly complex refining centers such as Jamnagar, India intentionally created merchant refining capacity far exceeding "
    "domestic absorption. Our findings show that each 1.0 MMT increase in annual refinery throughput pulled 0.941 MMT of crude imports (MOD-07: R² = 0.938). "
    "Crucially, scalar crude import metrics (e.g., Kruyt et al., 2009; Gupta, 2008) mischaracterize this dynamic by treating all crude imports as domestic "
    "vulnerability, ignoring the fact that a significant fraction of imported crude is re-exported as high-value refined petroleum products (+13.90 MMT net balance in FY 2023–24).", body_style))

story.append(Paragraph("5.3 The Clean Cooking Welfare Paradox and Refinery Yield Constraints", h2_style))
story.append(Paragraph(
    "The 117.84% aggregate product coverage ratio obscures an acute downstream supply asymmetry. While India enjoys massive export surpluses in transport fuels "
    "(Diesel +28.16 MMT, Petrol +7.77 MMT, ATF +8.58 MMT), it faces an acute structural deficit in LPG (−17.99 MMT, 43.08% coverage, 60.64% net import reliance). "
    "This deficit is the direct consequence of a major social welfare achievement: the Pradhan Mantri Ujjwala Yojana (PMUY), which expanded rural clean cooking gas "
    "to over 100 million households (Kar et al., 2019; Gill-Wiehl et al., 2022; Gould & Urpelainen, 2018), while subsidized kerosene was phased out (Rao, 2012; Jain, 2018). "
    "Because crude distillation yields structurally yield only ~4.8% LPG (de la Rue du Can et al., 2019), domestic refining expansion cannot resolve this deficit, "
    "locking household energy security into foreign import supply chains.", body_style))

story.append(Paragraph("5.4 Macroeconomic Volatility, Currency Depreciation, and Fiscal Strain", h2_style))
story.append(Paragraph(
    "Our monetary analysis reveals that India's petroleum import vulnerability is profoundly amplified by macroeconomic transmission mechanisms. "
    "While physical imports grew 5.9-fold, the domestic rupee import bill escalated 74.1-fold. The LMDI decomposition demonstrates that while physical volume growth "
    "provides the long-run baseline, international price shocks account for 72.1% of annual spending volatility. Furthermore, a persistent rupee depreciation "
    "drag (42.4 to 82.9 INR/USD) acts as a permanent ratchet on domestic procurement costs, transmitting external terms-of-trade shocks into domestic inflation and current account deficits (Kanjilal & Ghosh, 2018; Tiwari & Albulescu, 2016).", body_style))

story.append(Paragraph("5.5 Strategic Policy Implications and Decarbonization Pathways", h2_style))
story.append(Paragraph(
    "These findings indicate that conventional upstream exploration subsidies (NELP/HELP) cannot realistically resolve India's import exposure (Mishra et al., 2023). "
    "Instead, policy must focus on targeted interventions: (1) addressing the clean cooking vulnerability by diversifying rural energy beyond imported LPG toward electric "
    "induction cooking powered by renewable mini-grids; (2) curbing transport fuel demand through 20% ethanol blending mandates (E20) and accelerated vehicle electrification; "
    "(3) expanding Phase-II Strategic Petroleum Reserves (ISPRL) well beyond current commercial cover (Kumar, 2023); and (4) pursuing bilateral rupee-denominated crude settlement mechanisms to neutralize exchange rate depreciation wedges.", body_style))

# 6. Conclusion
story.append(Paragraph("6. Conclusion", h1_style))
story.append(Paragraph(
    "This study has conducted an empirical supply-chain audit of India's petroleum sector across 26 continuous financial years (FY 1998–99 to FY 2023–24). "
    "By establishing mass-balance accounting, Newey-West HAC regression models, product-level trade balances, and LMDI index decompositions, the analysis resolves "
    "the central paradoxes governing India's hydrocarbon economy.", body_style))
story.append(Paragraph(
    "The primary empirical conclusions are threefold: First, domestic crude oil extraction flatlined over the past quarter-century (CAGR −0.44%) and is statistically "
    "decoupled from crude import surges. Crude import growth (+7.35% CAGR) was overwhelmingly driven by a 281.6% expansion in domestic refining throughput "
    "(MOD-07: β = 0.9406, R² = 0.9382), reflecting deliberate downstream industrial policy rather than upstream failure. Second, India's status as a major net product "
    "exporter (+13.90 MMT in FY 2023–24) conceals deep product-level asymmetries: massive export surpluses in transport fuels coexist with a severe domestic supply "
    "deficit in clean cooking LPG (−17.99 MMT, 60.64% import reliance) caused by PMUY adoption and chemical refining yield limits. Third, external price volatility "
    "compounded by persistent rupee depreciation escalated the national crude import bill 74.1-fold in domestic currency, generating acute balance-of-payments vulnerability.", body_style))
story.append(Paragraph(
    "Policymakers must move beyond simplistic aggregate import ratios and unviable upstream self-sufficiency targets. Sustainable energy security requires "
    "targeted electrification of household clean cooking, transport fuel diversification, enhanced strategic petroleum storage, and macro-hedging of foreign exchange exposure.", body_style))

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
print(f"[OK] Successfully generated PDF Document: {PDF_OUT}")
print("Manuscript with figures compilation complete!")
