import pandas as pd

def remove_duplicates(filepath: str) -> None:
    raw_data = pd.read_csv(filepath)
    print(raw_data.duplicated().any())
    raw_data.dropna()
    print(raw_data.duplicated().any())