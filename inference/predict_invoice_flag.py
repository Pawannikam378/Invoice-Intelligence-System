import os
import joblib
import numpy as np
import pandas as pd

# Resolve paths relative to the project root (one level up from this script)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "predict_flag_invoice.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")


def load_model(model_path: str = MODEL_PATH):
  with open(model_path, "rb") as f:
    model = joblib.load(f)
  return model

def load_scaler(scaler_path: str = SCALER_PATH):
  with open(scaler_path, "rb") as f:
    scaler = joblib.load(f)
  return scaler

def predict_invoice_flag(input_data):
  model = load_model()
  scaler = load_scaler()
  input_df = pd.DataFrame(input_data)
  input_scaled = scaler.transform(input_df.values)
  input_df['Predicted_Invoice_Flag'] = model.predict(input_scaled)
  return input_df

if __name__ == "__main__":
  sample_data = {
    "invoice_quantity": [50],
    "invoice_dollars": [162.0],
    "Freight": [1.73],
    "total_item_quantity": [162],
    "total_item_dollars": [2467.0]
  }
  prediction = predict_invoice_flag(sample_data)
  print(prediction)