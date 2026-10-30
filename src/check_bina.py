import pandas as pd
df = pd.read_csv('03_Processed_Data/raw_extractions/raw_refinery_crude_processing_historical.csv')
for yr in ['2011-12', '2012-13', '2018-19', '2019-20']:
    sub = df[df['reporting_period'] == yr]
    print('===', yr, '===')
    for pat in ['BINA', 'BPCL-TOTAL', 'BORL']:
        m = sub[sub['source_row_label'].str.contains(pat, case=False, na=False)]
        for idx, r in m.iterrows():
            lbl = r['source_row_label'].replace('\n', ' ')[:45]
            val = r['source_raw_value']
            print(f'  {lbl:<45}: {val}')
