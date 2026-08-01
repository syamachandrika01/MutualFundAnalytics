from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///bluestock_mf.db")

files = [
    "fund_master",
    "nav_history",
    "investor_transactions",
    "scheme_performance"
]

for file in files:

    df = pd.read_csv(
        f"data/processed/{file}.csv"
    )

    df.to_sql(
        file,
        engine,
        if_exists="replace",
        index=False
    )

    print(file, len(df))