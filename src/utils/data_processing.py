import pandas as pd
import os

path = os.path.join("src/data", "retail_store_inventory_test.csv")

def process():
    df = pd.read_csv(path)


    df_date = df['Date'] = pd.to_datetime(df["Date"], errors='coerce')

    print(df_date)