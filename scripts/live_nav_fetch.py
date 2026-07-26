import requests
import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Scheme names and AMFI codes
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"Fetching {scheme_name}...")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "data" in data:
            df = pd.DataFrame(data["data"])

            filename = f"data/raw/{scheme_name}.csv"
            df.to_csv(filename, index=False)

            print(f"Saved: {filename}")
        else:
            print(f"No NAV data found for {scheme_name}")
    else:
        print(f"Failed to fetch {scheme_name} (HTTP {response.status_code})")

print("Done!")