import pandas as pd

df = pd.read_csv('05_Research_Paper/phase9a_audit/04_literature_reference_audit.csv')
print("Columns:", df.columns.tolist())
print("\nVerification_Status value counts:")
print(df['Verification_Status'].value_counts())

print("\nAll 30 entries in 04_literature_reference_audit.csv:")
for idx, r in df.iterrows():
    ref_id = r.get('Reference_ID', '')
    status = r.get('Verification_Status', '')
    disc = str(r.get('Discrepancy_Notes', ''))
    title = str(r.get('Registered_Title', ''))
    auth = str(r.get('Registered_Authors', ''))
    print(f"{ref_id} | Status: {status} | Disc: {disc[:50]} | Title: {title[:50]}")
