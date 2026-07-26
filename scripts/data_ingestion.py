import os
import pandas as pd

DATA_FOLDER = "data/raw"

files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print(f"Total CSV Files: {len(files)}")

for file in files:

    path = os.path.join(DATA_FOLDER, file)

    print("="*70)
    print(file)

    df = pd.read_csv(path)

    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst Five Rows")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())