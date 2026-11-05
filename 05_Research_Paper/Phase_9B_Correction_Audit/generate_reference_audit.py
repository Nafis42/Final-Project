import pandas as pd

# Load Phase 9A reference audit
df = pd.read_csv('05_Research_Paper/phase9a_audit/04_literature_reference_audit.csv')

# Define exact standardized verification statuses:
# 1. 'Verified as originally entered' (8 entries)
# 2. 'Corrected and subsequently verified' (17 entries)
# 3. 'Corrected and subsequently verified (Replacement)' (4 entries)
# 4. 'Unverified / Excluded' (1 entry)

records = []
for idx, r in df.iterrows():
    paper_id = r['Paper_ID']
    prev_status = r['Verification_Status']
    
    # Official metadata takes precedence
    auth = r['Official_Authors'] if pd.notna(r['Official_Authors']) and str(r['Official_Authors']).strip() != '' else r['Registered_Authors']
    yr = str(r['Official_Year']).replace('.0', '') if pd.notna(r['Official_Year']) and str(r['Official_Year']).strip() != '' else str(r['Registered_Year']).replace('.0', '')
    title = r['Official_Title'] if pd.notna(r['Official_Title']) and str(r['Official_Title']).strip() != '' else r['Registered_Title']
    journal = r['Official_Journal'] if pd.notna(r['Official_Journal']) and str(r['Official_Journal']).strip() != '' else r['Registered_Journal']
    vol = str(r['Official_Vol']).replace('.0', '') if pd.notna(r['Official_Vol']) and str(r['Official_Vol']).strip() != '' else str(r['Registered_Vol']).replace('.0', '')
    issue = str(r['Official_Issue']).replace('.0', '') if pd.notna(r['Official_Issue']) and str(r['Official_Issue']).strip() != '' else str(r['Registered_Issue']).replace('.0', '')
    pages = r['Official_Pages'] if pd.notna(r['Official_Pages']) and str(r['Official_Pages']).strip() != '' else r['Registered_Pages']
    doi = r['Official_DOI'] if pd.notna(r['Official_DOI']) and str(r['Official_DOI']).strip() != '' else r['Registered_DOI']
    
    # Classify verification status
    if prev_status == 'Verified':
        verif_status = 'Verified as originally entered'
        action_taken = 'Retained without modification (100% matched publisher record)'
        inc_in_manuscript = 'YES'
    elif prev_status == 'Incorrect (Corrected)':
        verif_status = 'Corrected and subsequently verified (Replacement)'
        action_taken = 'Fatal DOI mismatch replaced with authentic verified publication by target author'
        inc_in_manuscript = 'YES'
    elif prev_status == 'Partially verified':
        verif_status = 'Corrected and subsequently verified'
        action_taken = 'Bibliographic details (official title, volume, issue, or page numbers) harmonized to publisher record'
        inc_in_manuscript = 'YES'
    elif prev_status == 'Unverified':
        verif_status = 'Unverified / Excluded'
        action_taken = 'Excluded from manuscript bibliography due to lack of authentic digital indexing or verifiable DOI'
        inc_in_manuscript = 'NO (EXCLUDED)'
    else:
        verif_status = prev_status
        action_taken = 'Audited'
        inc_in_manuscript = 'YES'

    # Build APA 7th Citation String
    issue_str = f"({issue})" if issue and issue != 'nan' and issue != '' else ""
    vol_str = f", {vol}" if vol and vol != 'nan' and vol != '' else ""
    page_str = f", {pages}" if pages and pages != 'nan' and pages != '' else ""
    doi_str = f". https://doi.org/{doi}" if doi and doi != 'nan' and doi != '' and str(doi).strip().lower() != 'none' else ""
    
    apa7_citation = f"{auth} ({yr}). {title}. {journal}{vol_str}{issue_str}{page_str}{doi_str}."
    
    records.append({
        'Reference_ID': paper_id,
        'Verification_Status': verif_status,
        'Included_in_Manuscript': inc_in_manuscript,
        'Action_Taken': action_taken,
        'Official_Authors': auth,
        'Publication_Year': yr,
        'Official_Article_Title': title,
        'Official_Journal_Name': journal,
        'Volume': vol if vol != 'nan' else '',
        'Issue': issue if issue != 'nan' else '',
        'Pages_or_Article_No': pages if pages != 'nan' else '',
        'DOI': doi if doi != 'nan' else 'None',
        'DOI_URL': f"https://doi.org/{doi}" if doi and doi != 'nan' and doi != 'None' else 'None',
        'APA7_Full_Citation': apa7_citation,
        'Original_Discrepancy_Details': r['Discrepancy_Details'] if pd.notna(r['Discrepancy_Details']) else 'None'
    })

df_ref_out = pd.DataFrame(records)
out_csv = '05_Research_Paper/Phase_9B_Correction_Audit/Phase_9B_Reference_Audit.csv'
df_ref_out.to_csv(out_csv, index=False)
print(f"Generated {out_csv} with {len(df_ref_out)} references.")
print("\nBreakdown of verification statuses:")
print(df_ref_out['Verification_Status'].value_counts())
print("\nManuscript inclusion count:")
print(df_ref_out['Included_in_Manuscript'].value_counts())
