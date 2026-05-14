import pandas as pd
from pathlib import Path
import sqlite3

from src.extract import extract_data
from src.transform import transform_data

def load_data(df, db_path, table_name):
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded {len(df):,} rows into '{table_name}' at {db_path}")

if __name__ == "__main__":
    csv_path = Path("data/raw/DataCoSupplyChainDataset.csv")
    db_path = Path("db/supply_chain.db")

    raw_df = extract_data(csv_path)
    clean_df = transform_data(raw_df)
    load_data(clean_df, db_path, "orders")