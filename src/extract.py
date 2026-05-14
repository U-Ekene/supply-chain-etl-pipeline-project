import pandas as pd
from pathlib import Path

def extract_data(file_path):
    if not file_path.exists():
        raise FileNotFoundError(f"Expected CSV at {file_path}, but not found")
    # DataCo CSV is Latin-1 encoded
    df = pd.read_csv(file_path, encoding="latin-1")
    
    print(f"Extracted {df.shape[0]:,} rows × {df.shape[1]} columns from {file_path.name}")
    return df

if __name__ == "__main__":
    # Allows running this file directly for testing: python -m src.extract
    csv_path = Path("data/raw/DataCoSupplyChainDataset.csv")
    df = extract_data(csv_path)
    print(df.head())