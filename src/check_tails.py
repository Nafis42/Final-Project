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
    cols_to_show = ['financial_year', 'fiscal_year_start']
    if 'source_period_label' in df.columns:
        cols_to_show.append('source_period_label')
    if 'is_partial_period' in df.columns:
        cols_to_show.append('is_partial_period')
    if 'is_provisional' in df.columns:
        cols_to_show.append('is_provisional')
    print(df[cols_to_show].tail(4).to_string())
