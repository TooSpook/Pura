import time
import pandas as pd

def load(filepath: str) -> pd.DataFrame:
    raw_data = pd.read_csv(filepath)
    return raw_data

def any_duplicates(raw_data: pd.DataFrame) -> bool:
    print("Checking for duplicates...")
    time.sleep(1)
    # implement later

def remove_duplicates(raw_data: pd.DataFrame) -> pd.DataFrame:
    raw_data.dropna()