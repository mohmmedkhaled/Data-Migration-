import pandas as pd
from sqlalchemy import create_engine
import os


DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# create_connection_engine
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')

def load_csv_to_postgres(file_path, table_name):
    print(f"Uploading {file_path} to table {table_name}...")
    df = pd.read_csv(file_path)

    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Successfully uploaded {len(df)} records.")

data_files = {
    "../data/olist_customers_dataset.csv": "raw_customers",
    "../data/olist_geolocation_dataset.csv": "raw_geolocation",
    "../data/olist_order_items_dataset.csv": "raw_order_items",
    "../data/olist_order_payments_dataset.csv": "raw_order_payments",
    "../data/olist_order_reviews_dataset.csv": "raw_orders_reviews",
    "../data/olist_orders_dataset.csv": "raw_orders",
    "../data/olist_products_dataset.csv": "raw_products",
    "../data/olist_sellers_dataset.csv": "raw_sellers",
    "../data/product_category_name_translation.csv": "raw_product_category_name_translation"
    
}

for file, table in data_files.items():
    load_csv_to_postgres(file, table)

    