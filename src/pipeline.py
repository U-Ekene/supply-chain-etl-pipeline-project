from pathlib import Path

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

CSV_PATH = Path("data/raw/DataCoSupplyChainDataset.csv")
DB_PATH = Path("db/supply_chain.db")
TABLE_NAME = "orders"

def run_pipeline():
    print("Starting pipeline...")
    raw_df = extract_data(CSV_PATH)
    clean_df = transform_data(raw_df)
    load_data(clean_df, DB_PATH, TABLE_NAME)
    print("Pipeline complete.")

if __name__ == "__main__":
    run_pipeline()