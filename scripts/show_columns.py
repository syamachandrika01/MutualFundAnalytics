import os
import pandas as pd

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path, nrows=5)
        print("=" * 80)
        print(file)
        print(df.columns.tolist())