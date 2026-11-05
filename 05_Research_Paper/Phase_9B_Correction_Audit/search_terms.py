import glob

print("Searching all .md and .csv files in 04_Analysis and 05_Research_Paper for LPG numbers...")
terms = ["18.10", "30.40", "62.74", "17.99", "18.51", "29.66", "12.78"]

for fpath in glob.glob('04_Analysis/**/*', recursive=True) + glob.glob('05_Research_Paper/**/*', recursive=True):
    if fpath.endswith(('.md', '.csv', '.txt')):
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    for t in ["18.10", "30.40", "62.74"]:
                        if t in line:
                            print(f"{fpath}:{i+1} [matched {t}] -> {line.strip()[:120]}")
        except Exception as e:
            pass
