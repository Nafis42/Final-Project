# Audit of Crude Supply-Gap Interpretation and Physical Mass Balance

**Document Reference:** `05_Research_Paper/phase9a_audit/03_crude_balance_audit.md`  
**Research Project:** *India's Petroleum Supply Chain and Import Exposure: A Historical Analysis of Domestic Production, Refinery Throughput, Petroleum Product Trade and Consumption*  
**Date:** November 2026  
**Status:** Phase 9A Critical Audit Output  

---

## 1. Executive Summary

In Phase 9 preparation documents (notably `01_evidence_audit.md`, `07_methodology_register.md`, and `08_result_section_plan.md`), the metric:
$$\Delta_{\text{upstream}, t} = \text{Refinery Throughput}_t - \text{Domestic Crude Production}_t$$
was repeatedly referred to as the *"physical crude deficit gap"*, and in several instances loosely described as the country's *"crude import requirement"* or as a *"mass-balanced crude deficit"*.

This audit establishes the precise accounting boundaries of this metric. By comparing actual historical values of $\Delta_{\text{upstream}, t}$ with gross crude imports ($M_{c,t}$) across all 26 years, this audit proves:
1. **$\Delta_{\text{upstream}, t}$ is strictly a domestic-production-to-refinery-intake gap**, measuring the volumetric shortfall between indigenous field extraction and refinery processing demand.
2. **It is NOT an exact crude import requirement.** In every single year from FY 1998–99 to FY 2023–24, actual gross crude oil imports exceeded $\Delta_{\text{upstream}, t}$ by between **+0.37 MMT and +6.93 MMT** (averaging approximately $+4.4\text{ MMT}$ annually).
3. **The difference represents physical supply-chain logistics**: pipeline line-fill, ocean transit lags, refinery tank farm stock variations ($\Delta S_c$), Strategic Petroleum Reserve (ISPRL) injections, and minor non-crude refinery feedstock adjustments.
4. The research paper must explicitly describe this metric as the **"Domestic Production-to-Throughput Gap"** and avoid describing simple subtraction as an exact import requirement or closed mass balance.

---

## 2. Empirical Verification: Throughput Gap vs. Actual Imports

The table below contrasts the calculated gap ($\Delta_{\text{gap}} = R_t - P_{c,t}$) against actual customs-cleared crude imports ($M_{c,t}$) from `core_annual_petroleum_dataset.csv`:

```
+----------------------------------------------------------------------------------------------------+
|                         PRODUCTION-TO-THROUGHPUT GAP VS. CRUDE OIL IMPORTS                          |
+-------------+------------+------------+--------------------+---------------+-----------------------+
| Financial   | Refinery   | Domestic   | Production-to-     | Actual Crude  | Unaccounted Logistics |
| Year        | Throughput | Production | Throughput Gap     | Imports       | & Stock Wedge         |
|             | $R_t$ (MMT)| $P_c$ (MMT)| $\Delta$ Gap (MMT) | $M_c$ (MMT)   | ($M_c - \Delta$ Gap)  |
+-------------+------------+------------+--------------------+---------------+-----------------------+
| FY 1998-99  |   68.539   |   32.760   |       35.779       |    39.808     |        +4.029 MMT     |
| FY 1999-00  |   85.709   |   32.000   |       53.709       |    57.805     |        +4.096 MMT     |
| FY 2004-05  |  124.302   |   34.138   |       90.164       |    95.861     |        +5.697 MMT     |
| FY 2009-10  |  186.562   |   33.398   |      153.164       |   159.259     |        +6.095 MMT     |
| FY 2014-15  |  223.264   |   37.469   |      185.795       |   189.435     |        +3.640 MMT     |
| FY 2019-20  |  254.386   |   32.169   |      222.217       |   226.955     |        +4.738 MMT     |
| FY 2021-22  |  241.704   |   29.688   |      212.015       |   212.382     |        +0.367 MMT     |
| FY 2022-23  |  255.232   |   29.179   |      226.053       |   232.700     |        +6.647 MMT     |
| FY 2023-24  |  261.546   |   29.356   |      232.190       |   234.262     |        +2.072 MMT     |
+-------------+------------+------------+--------------------+---------------+-----------------------+
| Mean Wedge  |    ---     |    ---     |        ---         |      ---      |        +4.414 MMT     |
+-------------+------------+------------+--------------------+---------------+-----------------------+
```

### Key Quantitative Findings:
- Over 26 years, the production-to-throughput gap expanded by **+548.96%** (from $35.78\text{ MMT}$ to $232.19\text{ MMT}$, an increase of $+196.41\text{ MMT}$).
- Over the exact same period, crude imports expanded by **+488.48%** (from $39.81\text{ MMT}$ to $234.26\text{ MMT}$, an increase of $+194.45\text{ MMT}$).
- Actual crude imports were persistently higher than the gap in all 26 years, with a standard deviation of the wedge of $\pm 1.48\text{ MMT}$.

---

## 3. Physical Supply-Chain Factors Explaining the Wedge

The systematic wedge between gross crude imports and $(R_t - P_{c,t})$ is explained by five structural supply-chain mechanisms:

```
                                  +---------------------------------------+
                                  |     GROSS CRUDE IMPORTS (M_c,t)       |
                                  +-------------------+-------------------+
                                                      |
                         +----------------------------+----------------------------+
                         |                                                         |
                         v                                                         v
         +-------------------------------+                         +-------------------------------+
         |   REFINERY CRUDE PROCESSING   |                         |  LOGISTICS & INVENTORY WEDGE  |
         |         INTAKE (R_t)          |                         |  (Average +4.41 MMT / year)   |
         +---------------+---------------+                         +---------------+---------------+
                         ^                                                         |
                         | (Less Domestic Crude)                                   |
         +---------------+---------------+                         +---------------+---------------+
         |    DOMESTIC CRUDE OIL (P_c)   |                         | 1. Crude Tank Farm Stocks     |
         +-------------------------------+                         | 2. Pipeline Line-Fill         |
                                                                   | 3. Strategic Storage (ISPRL)  |
                                                                   | 4. Ocean In-Transit Losses    |
                                                                   | 5. Reporting Timing Lags      |
                                                                   +-------------------------------+
```

1. **Refinery Storage and Terminal Inventory Changes ($\Delta S_{c,\text{ref}}$):**  
   Coastal and inland refineries maintain mandatory commercial crude inventories (typically 10–15 days of operating throughput) in on-site tank farms. Net inventory builds increase imports without appearing in current-year processing throughput.
2. **Cross-Country Crude Pipeline Line-Fill ($\Delta S_{c,\text{pipe}}$):**  
   India operates over 10,000 km of crude oil pipelines (e.g., Mundra–Panipat, Salaya–Mathura, Paradip–Haldia–Barauni). Commissioning new pipelines or expanding diameter requires thousands of tonnes of crude oil permanently locked as physical line-fill.
3. **Strategic Petroleum Reserves (ISPRL Phase-I):**  
   Between FY 2015–16 and FY 2019–20, the Indian Strategic Petroleum Reserves Limited filled underground rock caverns at Visakhapatnam (1.33 MMT), Mangalore (1.50 MMT), and Padur (2.50 MMT). These strategic stock injections represented imported crude that was never directed to commercial refinery throughput in the year of import.
4. **Ocean Transit and Port Handling Discrepancies:**  
   Crude oil imported via Very Large Crude Carriers (VLCCs) experiences small volumetric transit losses (evaporation, ocean sludge, ocean voyage shrinkage) and customs clearance timing differences (vessels anchored offshore on March 31 cleared in April).
5. **Domestic Field Losses and Internal Consumption:**  
   A fraction of domestic crude production is consumed internally at field production facilities (heaters, field gathering stations) or lost in transit before reaching refinery delivery manifolds.

---

## 4. Formalization of the True Hydrocarbon Mass Balance

In the manuscript Method section (Section 3.3), the complete physical crude mass-balance equation must be presented as follows:

$$R_t = P_{c,t} + M_{c,t} - X_{c,t} - \Delta S_{c,t} - \theta_{c,t}$$

Where:
- $R_t$: Refinery crude processing throughput (MMT).
- $P_{c,t}$: Domestic crude oil extraction, including lease condensate (MMT).
- $M_{c,t}$: Gross crude oil imports (MMT).
- $X_{c,t}$: Gross crude oil exports ($X_{c,t} \equiv 0$ for India).
- $\Delta S_{c,t}$: Net crude inventory change across refineries, pipelines, and strategic reserves (MMT).
- $\theta_{c,t}$: Net logistical adjustment, transport losses, and non-crude feedstock correction (MMT).

### Academic Caution Mandate:
Rearranging this relationship gives:
$$M_{c,t} = (R_t - P_{c,t}) + (\Delta S_{c,t} + \theta_{c,t})$$
This proves that $(R_t - P_{c,t})$ equals crude imports **only if** net inventory changes and logistical wedges are exactly zero ($\Delta S_{c,t} + \theta_{c,t} = 0$). Because this term averages $+4.41\text{ MMT}$ annually, the subtraction $(R_t - P_{c,t})$ must **never** be labeled as the exact import requirement in the manuscript.

---

## 5. Corrected Manuscript Nomenclature and Presentation Guidelines

To ensure precise presentation in the final paper:

1. **Standardized Variable Label:**  
   The metric $(R_t - P_{c,t})$ must be consistently designated as the **"Domestic Production-to-Throughput Gap"** or **"Physical Refining Feedstock Deficit"**.
2. **Explicit Disclosure in Footnotes:**  
   Whenever Table 1, Table 3, or Figure 3 present this gap, the following footnote must be attached:  
   *"Note: The physical production-to-throughput gap ($R_t - P_{c,t}$) measures the volumetric shortfall between indigenous extraction and refinery intake. Actual crude imports exceed this gap by an average of 4.41 MMT annually due to refinery tank farm stock builds, pipeline line-fill, ocean transit adjustments, and strategic reserve storage (ISPRL)."*
3. **Removal of Unqualified Claims:**  
   Prose describing this gap as an "exact import requirement" or asserting that "refinery throughput mathematically mandates an identical volume of crude imports" must be rephrased to reflect the operational buffer of inventories and logistics.
