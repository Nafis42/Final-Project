import pandas as pd

datasets = {
    'crude_prod': '03_Processed_Data/standardized/annual_crude_oil_production.csv',
    'crude_proc': '03_Processed_Data/standardized/annual_refinery_crude_processing.csv',
    'prod_prod': '03_Processed_Data/standardized/annual_petroleum_product_production.csv',
    'trade_vol': '03_Processed_Data/standardized/annual_petroleum_trade_volumes.csv',
    'consumption': '03_Processed_Data/standardized/annual_petroleum_product_consumption.csv',
    'trade_val': '03_Processed_Data/standardized/annual_petroleum_import_export_values.csv',
    'crude_price': '03_Processed_Data/standardized/crude_oil_fob_price_indian_basket.csv'
}

for k, path in datasets.items():
    df = pd.read_csv(path)
    print(f"=== {k} ===")
    print("Columns:", df.columns.tolist()[:6])
    print("Start years:", df['fiscal_year_start'].tolist())
    if 'financial_year' in df.columns:
        print("FY labels:", df['financial_year'].tolist()[:4], "...", df['financial_year'].tolist()[-3:])
