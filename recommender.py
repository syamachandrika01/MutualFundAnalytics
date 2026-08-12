import pandas as pd

performance = pd.read_csv(
    "data/processed/scheme_performance.csv"
)

def recommend_funds(risk_appetite):

    risk_map = {
        "Low": "Low",
        "Moderate": "Moderate",
        "High": "High"
    }

    if risk_appetite not in risk_map:
        print(
            "Please enter Low, Moderate, or High"
        )
        return

    result = performance[
        performance["risk_grade"]
        .astype(str)
        .str.strip()
        .str.lower()
        ==
        risk_map[risk_appetite].lower()
    ].copy()

    result = result.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    print(
        result[
            [
                "scheme_name",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct",
                "expense_ratio_pct"
            ]
        ].to_string(index=False)
    )


risk = input(
    "Enter risk appetite "
    "(Low / Moderate / High): "
)

recommend_funds(risk)