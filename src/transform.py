import pandas as pd
from pathlib import Path

from src.extract import extract_data

def transform_data(df):
    # Drop useless columns (null or not useful for analysis)
    useless_columns = [
        "Product Description", #mostly null
        "Order Zipcode", #mostly null
        "Product Image", #all urls
    ]
    df = df.drop(columns=useless_columns)

    # Drop PII columns 
    pii_columns = [
        "Customer Email",
        "Customer Password",
        "Customer Fname",
        "Customer Lname",
        "Customer Street",
    ]
    df = df.drop(columns=pii_columns)

    #  Change date columns from string to datetime
    date_columns = [
    "order date (DateOrders)",
    "shipping date (DateOrders)",
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    # Make the column names uniform
    df.columns = (
        df.columns
        .str.lower()                          #everything lowercase
        .str.replace(r"\(.*?\)", "", regex=True)  #remove brackets and content inside
        .str.strip()                          #trim leading/trailing whitespace
        .str.replace(r"\s+", "_", regex=True) #change spaces to underscores
    )

    #Handle remaining nulls in customer_zipcode column
    df = df.dropna(subset=["customer_zipcode"])

    print(f"Transformed: {df.shape[0]:,} rows × {df.shape[1]} columns")
    return df

    

if __name__ == "__main__":
    csv_path = Path("data/raw/DataCoSupplyChainDataset.csv")
    raw_df = extract_data(csv_path)
    clean_df = transform_data(raw_df)
    print(clean_df.columns.tolist())