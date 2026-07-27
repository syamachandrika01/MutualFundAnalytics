import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("="*50)
print("UNIQUE FUND HOUSES")
print(fund_master["fund_house"].unique())

print("\n" + "="*50)
print("UNIQUE CATEGORIES")
print(fund_master["category"].unique())

print("\n" + "="*50)
print("UNIQUE SUB-CATEGORIES")
print(fund_master["sub_category"].unique())

print("\n" + "="*50)
print("UNIQUE RISK CATEGORIES")
print(fund_master["risk_category"].unique())

print("\n" + "="*50)
print("VALIDATING AMFI CODES")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

if len(missing_codes) == 0:
    print("✅ All AMFI codes are present in nav_history.csv")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)

print("\n" + "="*50)
print("DATA QUALITY SUMMARY")

print(f"Total Funds: {len(fund_master)}")
print(f"Total NAV Records: {len(nav_history)}")
print(f"Unique AMFI Codes: {len(master_codes)}")
print(f"Missing Codes: {len(missing_codes)}")