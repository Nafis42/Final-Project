import urllib.request
import json
import pandas as pd
import time

df = pd.read_csv('05_Research_Paper/manuscript/04_literature_review_and_reference_register.csv')
results = []

for i, r in df.iterrows():
    doi = str(r['DOI']).strip()
    pid = r['Paper_ID']
    title = r['Title']
    reg_authors = r['Authors']
    reg_year = r['Year']
    reg_journal = r['Journal']
    reg_vol = r['Volume']
    reg_issue = r['Issue']
    reg_page = r['Pages']
    
    print(f"\n--- Checking {pid}: {title[:50]} ---")
    
    if doi.startswith('10.'):
        url = f"https://api.crossref.org/works/{doi}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'AcademicAuditBot/1.0 (mailto:academic_audit@research.edu)'})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                item = data['message']
                cr_title = item.get('title', [''])[0]
                cr_authors = '; '.join([f"{a.get('family', '')}, {a.get('given', '')}" for a in item.get('author', [])])
                cr_journal = item.get('container-title', [''])[0]
                cr_vol = str(item.get('volume', ''))
                cr_issue = str(item.get('issue', ''))
                cr_page = str(item.get('page', ''))
                pub_parts = item.get('published-print', {}).get('date-parts', []) or item.get('published', {}).get('date-parts', [])
                cr_year = pub_parts[0][0] if pub_parts and pub_parts[0] else None
                
                # Check match
                title_match = title.lower().strip() == cr_title.lower().strip()
                print(f"Status: OK (DOI resolved)")
                print(f"CR Journal: {cr_journal}")
                print(f"CR Year: {cr_year} (Reg: {reg_year})")
                print(f"CR Vol: {cr_vol} (Reg: {reg_vol}) | Issue: {cr_issue} (Reg: {reg_issue}) | Page: {cr_page} (Reg: {reg_page})")
                print(f"CR Title: {cr_title}")
                print(f"CR Authors: {cr_authors}")
                
                results.append({
                    'pid': pid,
                    'status': 'RESOLVED',
                    'doi': doi,
                    'cr_title': cr_title,
                    'cr_authors': cr_authors,
                    'cr_journal': cr_journal,
                    'cr_vol': cr_vol,
                    'cr_issue': cr_issue,
                    'cr_page': cr_page,
                    'cr_year': cr_year,
                    'error': None
                })
        except Exception as e:
            print(f"Status: FAILED ({e})")
            results.append({
                'pid': pid,
                'status': 'FAILED',
                'doi': doi,
                'error': str(e)
            })
    else:
        print(f"Status: NO DOI PROVIDED (Value: {doi})")
        results.append({
            'pid': pid,
            'status': 'NO_DOI',
            'doi': doi,
            'error': 'No standard DOI'
        })
    time.sleep(0.5)

with open('05_Research_Paper/phase9a_audit/crossref_audit_dump.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print("\n\nCompleted Crossref audit of all 30 references.")
