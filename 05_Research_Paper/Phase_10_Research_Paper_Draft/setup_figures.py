import os
from PIL import Image

image_mapping = {
    "Figure_1_Supply_Chain_Overview.png": r"04_Analysis\phase4\figures\fig4_supply_chain_balance_multipanel.png",
    "Figure_2_Domestic_Production_vs_Imports.png": r"04_Analysis\phase8\figures\fig1_domestic_prod_vs_crude_imports.png",
    "Figure_3_Throughput_and_Deficit_Gap.png": r"04_Analysis\phase8\figures\fig2_production_vs_refinery_throughput.png",
    "Figure_4_Product_Trade_Balance_Evolution.png": r"04_Analysis\phase4\figures\fig8_product_balance_and_trade.png",
    "Figure_5_Product_Wise_Net_Trade_FY24.png": r"04_Analysis\phase8\figures\fig3_product_trade_dynamics.png",
    "Figure_6_LPG_vs_Kerosene_Transition.png": r"04_Analysis\phase5\figures\fig4_lpg_vs_sko_structural_shift.png",
    "Figure_7_Dual_Currency_Import_Bill.png": r"04_Analysis\phase6\figures\fig1_historical_crude_import_expenditure.png",
    "Figure_8_Crude_Unit_Value_vs_Indian_Basket.png": r"04_Analysis\phase6\figures\fig4_crude_unit_value_vs_indian_basket.png",
    "Figure_9_LMDI_Expenditure_Decomposition.png": r"04_Analysis\phase6\figures\fig6_expenditure_decomposition_contributions.png",
    "Figure_10_Correlation_Heatmap.png": r"04_Analysis\phase8\figures\fig5_correlation_heatmap.png"
}

out_dir = r"05_Research_Paper\Phase_10_Research_Paper_Draft\Figures"
os.makedirs(out_dir, exist_ok=True)

import shutil

print(f"{'Figure Target Name':<45} | {'Original Width':>14} | {'Original Height':>15} | {'Aspect Ratio':>12}")
print("-" * 95)
for target_name, src_path in image_mapping.items():
    dest_path = os.path.join(out_dir, target_name)
    shutil.copyfile(src_path, dest_path)
    # Also copy svg if exists
    src_svg = src_path.replace('.png', '.svg')
    if os.path.exists(src_svg):
        shutil.copyfile(src_svg, dest_path.replace('.png', '.svg'))
    
    im = Image.open(dest_path)
    w, h = im.size
    ar = w / h
    print(f"{target_name:<45} | {w:>14} | {h:>15} | {ar:>12.3f}")

print("\nAll figures copied to Figures/ directory successfully.")
