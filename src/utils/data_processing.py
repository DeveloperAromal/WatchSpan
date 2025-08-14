import pandas as pd
from sklearn.preprocessing import StandardScaler
import os


def process(file):
    
    path = os.path.join("src/data", file)

    df = pd.read_csv(path)


    df['Date'] = pd.to_datetime(df["Date"], errors='coerce')

    df = df[df['Demand Forecast'] >= 0] 
    
    categorial_col = [
        'Store ID', 'Product ID', 'Category', 'Region',
        'Weather Condition', 'Seasonality'
    ]
    
    df = pd.get_dummies[df, categorial_col]
    
    scaler = StandardScaler()
    
    numeric_cols = ['Inventory Level', 'Units Sold', 'Units Ordered', 
                    'Demand Forecast', 'Price', 'Discount', 
                    'Holiday/Promotion', 'Competitor Pricing']
    
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df