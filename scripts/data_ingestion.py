from pathlib import Path
import os

# Project root = D:\MutualFundAnalytics
BASE_DIR = Path(__file__).resolve().parent.parent

# Raw data folder
DATA_FOLDER = BASE_DIR / "data" / "raw"

print("Project directory:", BASE_DIR)
print("Raw data directory:", DATA_FOLDER)

if not DATA_FOLDER.exists():
    raise FileNotFoundError(
        f"Raw data folder not found: {DATA_FOLDER}"
    )

files = [
    f.name for f in DATA_FOLDER.iterdir()
    if f.is_file() and f.suffix.lower() == ".csv"
]

print(f"Found {len(files)} CSV files:")
for file in files:
    print(" -", file)