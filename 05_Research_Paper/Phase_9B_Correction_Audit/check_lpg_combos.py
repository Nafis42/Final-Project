import pandas as pd

df_prod = pd.read_csv('03_Processed_Data/standardized/petroleum_product_level_dataset.csv')
lpg = df_prod[df_prod['product_name'].str.contains('LPG', na=False)]

print("LPG rows from petroleum_product_level_dataset:")
for idx, row in lpg.iterrows():
    year = row['reporting_period']
    prod = row['production_mmt']
    imp = row['import_quantity_mmt']
    exp = row['export_quantity_mmt']
    net_imp = imp - exp if pd.notnull(imp) and pd.notnull(exp) else np.nan
    cons = row['consumption_mmt']
    gid = (imp / cons) * 100 if pd.notnull(imp) and pd.notnull(cons) and cons > 0 else np.nan
    nid = (net_imp / cons) * 100 if pd.notnull(net_imp) and pd.notnull(cons) and cons > 0 else np.nan
    # Also check if net_imp / prod, or imp / (prod + imp - exp)
    app_cons = prod + imp - exp if pd.notnull(prod) and pd.notnull(imp) and pd.notnull(exp) else np.nan
    app_dep = (net_imp / app_cons) * 100 if pd.notnull(app_cons) and app_cons > 0 else np.nan
    print(f"{year}: Prod={prod:.3f}, Imp={imp:.3f}, Exp={exp:.3f}, NetImp={net_imp:.3f}, Cons={cons:.3f}, GID={gid:.2f}%, NID={nid:.2f}%, AppCons={app_cons:.3f}, AppDep={app_dep:.2f}%")

print("\nLet's test mathematical combinations that produce ~62.74%:")
# What gives 62.74%?
# 18.00 / 28.69? 17.9888 / 28.67?
# 18.514 / 29.6636 = 62.41%
# 18.514 / 29.50?
# What about 2022-23: Imp=18.335, Cons=28.504 -> 18.335/28.504 = 64.32%
# What if 17.99 / 28.67? 17.99 / 28.67 = 62.748% ~ 62.75%
# Let's check where 28.67 comes from. In FY 2022-23 or FY 2023-24?
