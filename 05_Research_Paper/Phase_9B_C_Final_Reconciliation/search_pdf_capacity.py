import pypdf
import glob

pdf_files = glob.glob('01_Original_Data/*.pdf')
print("Searching PDFs for 'capacity' and '256'...")

for pdf_path in pdf_files:
    try:
        reader = pypdf.PdfReader(pdf_path)
        print(f"\nScanning {pdf_path} ({len(reader.pages)} pages)...")
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            if '256.8' in text or '256' in text or 'refining capacity' in text.lower():
                lines = text.splitlines()
                for line in lines:
                    if 'capacity' in line.lower() or '256' in line:
                        print(f"  Page {i+1}: {line.strip()[:120]}")
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
