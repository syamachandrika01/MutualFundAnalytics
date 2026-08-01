import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

# 1. FUND MASTER

df = pd.read_csv(f"{RAW}/01_fund_master.csv")

df["launch_date"] = pd.to_datetime(df["launch_date"], errors="coerce")

numeric_cols = [
    "expense_ratio_pct",
    "exit_load_pct",
    "min_sip_amount",
    "min_lumpsum_amount"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.drop_duplicates(subset="amfi_code")
df.to_csv(f"{PROCESSED}/01_fund_master.csv", index=False)

print("01 Fund Master Cleaned")


# 2. NAV HISTORY


df = pd.read_csv(f"{RAW}/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

df = df.sort_values(["amfi_code", "date"])
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df[df["nav"] > 0]
df = df.drop_duplicates()

df.to_csv(f"{PROCESSED}/02_nav_history.csv", index=False)

print("02 NAV History Cleaned")

# 3. AUM

df = pd.read_csv(f"{RAW}/03_aum_by_fund_house.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")

for col in [
    "aum_lakh_crore",
    "aum_crore",
    "num_schemes"
]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.drop_duplicates()

df.to_csv(f"{PROCESSED}/03_aum_by_fund_house.csv", index=False)

print("03 AUM Cleaned")

# 4. SIP

df = pd.read_csv(f"{RAW}/04_monthly_sip_inflows.csv")

df["month"] = pd.to_datetime(df["month"], errors="coerce")

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_csv(f"{PROCESSED}/04_monthly_sip_inflows.csv", index=False)

print("04 SIP Cleaned")

# 5. CATEGORY INFLOWS

df = pd.read_csv(f"{RAW}/05_category_inflows.csv")

df["month"] = pd.to_datetime(df["month"], errors="coerce")
df["net_inflow_crore"] = pd.to_numeric(df["net_inflow_crore"], errors="coerce")

df.to_csv(f"{PROCESSED}/05_category_inflows.csv", index=False)

print("05 Category Inflows Cleaned")

# 6. FOLIO COUNT

df = pd.read_csv(f"{RAW}/06_industry_folio_count.csv")

df["month"] = pd.to_datetime(df["month"], errors="coerce")

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_csv(f"{PROCESSED}/06_industry_folio_count.csv", index=False)

print("06 Folio Count Cleaned")

# 7. SCHEME PERFORMANCE

df = pd.read_csv(f"{RAW}/07_scheme_performance.csv")

returns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in returns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies")
print(anomalies)

df.to_csv(f"{PROCESSED}/07_scheme_performance.csv", index=False)

print("07 Scheme Performance Cleaned")

# 8. TRANSACTIONS

df = pd.read_csv(f"{RAW}/08_investor_transactions.csv")

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

df["amount_inr"] = pd.to_numeric(
    df["amount_inr"],
    errors="coerce"
)

df = df[df["amount_inr"] > 0]

df["transaction_type"] = (
    df["transaction_type"]
      .astype(str)
      .str.strip()
      .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

df = df[df["kyc_status"].isin(valid_kyc)]

df.to_csv(f"{PROCESSED}/08_investor_transactions.csv", index=False)

print("08 Transactions Cleaned")

# 9. PORTFOLIO

df = pd.read_csv(f"{RAW}/09_portfolio_holdings.csv")

df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"],
    errors="coerce"
)

for col in [
    "weight_pct",
    "market_value_cr",
    "current_price_inr"
]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_csv(f"{PROCESSED}/09_portfolio_holdings.csv", index=False)

print("09 Portfolio Cleaned")

# 10. BENCHMARK

df = pd.read_csv(f"{RAW}/10_benchmark_indices.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["close_value"] = pd.to_numeric(df["close_value"], errors="coerce")

df.to_csv(f"{PROCESSED}/10_benchmark_indices.csv", index=False)

print("10 Benchmark Cleaned")

print("\nAll 10 datasets cleaned successfully!")