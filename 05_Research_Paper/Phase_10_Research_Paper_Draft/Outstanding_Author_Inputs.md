# Outstanding Author Inputs Required
## Phase 10 — Research Paper First Draft

**Before submission, the author must complete all items marked [REQUIRED].**  
Items marked [OPTIONAL] improve the manuscript but are not strictly necessary for submission.

---

## 1. Author Identification [REQUIRED]

| Field | Current Placeholder | Required Input |
|:---|:---|:---|
| Author Name(s) | [AUTHOR_NAME_PLACEHOLDER] | Full name(s) in journal preferred format |
| Institution/Affiliation | [INSTITUTION_PLACEHOLDER] | Full department, institution, city, country |
| Email Address | [EMAIL_PLACEHOLDER] | Corresponding author institutional email |
| ORCID iD | [ORCID_PLACEHOLDER] | Author's ORCID (register at orcid.org if none) |

---

## 2. Title Page [REQUIRED]

The manuscript title is confirmed as:

> **India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption**

No changes needed to the title unless the submission journal requires a shorter running head (typically ≤60 characters). Suggested running head:  
**"India's Petroleum Supply Chain: A 26-Year Analysis"**

---

## 3. Acknowledgement [OPTIONAL — Recommended]

The current draft contains:

> *"The authors express their sincere gratitude to the Ministry of Petroleum and Natural Gas (MoPNG), Government of India, the Petroleum Planning & Analysis Cell (PPAC), the Directorate General of Commercial Intelligence and Statistics (DGCI&S), and the Reserve Bank of India (RBI) for making historical administrative and statistical data publicly accessible. The authors also thank academic mentors and departmental colleagues for valuable methodological feedback on time-series econometrics and index decomposition analysis."*

**Action Required:** Replace "academic mentors and departmental colleagues" with specific names (if any) or remove that sentence if no specific acknowledgement is intended.

---

## 4. Author Contributions [REQUIRED]

Current draft contains the CRediT taxonomy statement with [AUTHOR_NAME_PLACEHOLDER]. Replace with actual name(s).

If this is a solo-authored paper, the full statement reads:
> **[Author Name]:** Conceptualisation; Methodology; Data curation; Formal analysis; Visualisation; Writing – original draft; Writing – review & editing.

If co-authored, allocate CRediT roles among contributors.

---

## 5. Journal Selection [REQUIRED Before Submission]

The professor's template specifies the journal format. Before submission:
1. Confirm the target journal with your professor.
2. Check word limits, table count limits, and figure requirements.
3. Adjust reference style if the journal uses numbered citations rather than APA author-date.
4. The current manuscript is approximately 8,000–10,000 words (excluding references and tables). Verify this meets the target journal's scope.

Recommended journals for this paper's scope:
- *Energy Policy* (Elsevier)
- *Energy Economics* (Elsevier)
- *Energy for Sustainable Development* (Elsevier)
- *Indian Journal of Economics and Development*
- *The Energy Journal*

---

## 6. Data Availability Statement [REQUIRED by most journals]

Add a data availability statement such as:

> *"All data used in this study are derived from publicly available official administrative databases maintained by the Ministry of Petroleum and Natural Gas (MoPNG), the Petroleum Planning & Analysis Cell (PPAC), the Directorate General of Commercial Intelligence and Statistics (DGCI&S), and the Reserve Bank of India (RBI). Processed datasets and analysis scripts are available from the corresponding author upon reasonable request."*

If the GitHub repository is to be made public, add the repository URL.

---

## 7. Figures [REQUIRED — 7 Figures Not Yet Created as Publication-Quality Images]

The manuscript references 7 figures described in the text. These must be created as:
- High-resolution images (≥300 DPI for print journals)
- Preferred format: EPS/SVG (vector) or high-resolution TIFF/PNG
- Colour-blind-safe colour palette

**Figure list:**
1. Fig. 1 — Evolution of India's Petroleum Supply Chain (FY99–FY24): P, M, R, C trend lines
2. Fig. 2 — The Decoupling: Domestic Production vs. Crude Imports (scatter or dual-axis time series)
3. Fig. 3 — Refinery Throughput vs. Crude Imports (scatter with MOD-07 regression line)
4. Fig. 4 — Product Trade Balance: Gross Exports, Imports, and Net Position (stacked bar)
5. Fig. 5 — Product-Level Coverage Asymmetry: HSD/MS surplus vs. LPG deficit (bar chart)
6. Fig. 6 — Import Expenditure Growth: Physical volume (6×) vs. USD bill (38×) vs. INR bill (74×)
7. Fig. 7 — Crude Price and Import Unit Value Trajectory (dual-axis)

**Action Required:** Create or commission professional publication-quality figures. Python matplotlib/seaborn scripts can be provided.

---

## 8. Peer Review Responses [POST-SUBMISSION]

After submission, reviewers may request:
- Sub-annual analysis (quarterly/monthly data)
- Formal cointegration testing (Johansen or ARDL bounds)
- Comparison with other emerging-economy oil importers (China, Brazil, Indonesia)
- Explicit LMDI decomposition numerical results (additive/multiplicative waterfall values)
- Sensitivity analysis on HAC lag choice (L=1 vs L=2 vs L=3)

These are not required for the first draft but should be anticipated for revision.

---

## 9. LMDI Decomposition Results [CONDITIONAL — Section 4.7]

The manuscript currently presents the financial exposure narrative (Section 4.6) qualitatively. If Section 4.7 is to include formal LMDI numerical results (quantity effect, price effect, currency effect in absolute INR crore), the author must:
1. Run the Phase 7 LMDI decomposition script.
2. Verify that the additive components sum to the total change.
3. Insert the numerical table (Table 7 currently shows regression summary — LMDI table would be Table 7 or an additional table).

---

## 10. Ethics / IRB [NOT REQUIRED]

This study uses only publicly available aggregate administrative data. No human subjects research is involved. No IRB approval is required. This should be explicitly stated in the submission cover letter.

---

*Document prepared: November 2026*  
*Phase 10, Research Paper First Draft*
