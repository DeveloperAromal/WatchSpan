from tensorflow.keras import layers, models # type: ignore
from src.utils import process 
import os

def train_model(train_file):
    df_train = process(train_file)

    if 'Date' in df_train.columns:
        df_train = df_train.drop(columns='Date')

    X_train = df_train.drop(columns=['Demand Forecast']).select_dtypes(include=['int64', 'float64']).values.astype('float32')
                      
    y_train = df_train['Demand Forecast'].values.reshape(-1, 1).astype('float32')

    model = models.Sequential([
        layers.Input(shape=(X_train.shape[1],)),
        layers.Dense(int((X_train.shape[1] + 2) / 2), activation='relu'),
        layers.Dense(1)
    ])

    model.compile(optimizer="adam", loss="mse", metrics=["mae"])

    model.fit(X_train, y_train, epochs=50, batch_size=8)

    model.save(os.path.join("src/model", "demand_forecast.h5"))
    
    print("Model saved to demand_forecast_model.h5")

    return model
