from tensorflow.keras.models import load_model # type: ignore
import os
import numpy as np
from src.utils import process




def test_model(test_file):
    
    model_path = os.path.join("src/model", "demand_forecast.h5")
    
    df_test = process(test_file)

    if 'Date' in df_test['Date']:
        df_test = df_test.drop(columns=['Date'])

    X_test = df_test.drop(columns=['Demand Forecast'], errors='ignore').select_dtypes(include=['int64', 'float64']).values.astype('float32')


    model = load_model(model_path, compile=False)
    
    predictions = model.predict(X_test)
    print("Predictions (first 5):")
    print(predictions[:5])

    return predictions
 