from sqlalchemy import create_engine
import pandas as pd

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "fund_master": "fund_master.csv",
    "nav_history": "nav_history.csv",
    "aum_by_fund_house": "aum_by_fund_house.csv",
    "monthly_sip_inflows": "monthly_sip_inflows.csv",
    "category_inflows": "category_inflows.csv",
    "industry_folio_count": "industry_folio_count.csv",
    "scheme_performance": "scheme_performance.csv",
    "investor_transactions": "investor_transactions.csv",
    "portfolio_holdings": "portfolio_holdings.csv",
    "benchmark_indices": "benchmark_indices.csv"
}

for table_name, file_name in files.items():

    df = pd.read_csv(f"data/processed/{file_name}")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name}: {len(df)} rows loaded")

print("\nAll tables loaded successfully into bluestock_mf.db")