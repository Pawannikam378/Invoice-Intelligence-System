import os
import joblib
import pandas as pd

# Resolve paths relative to the project root (one level up from this script)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "predict_freight_model.pkl")

def load_model(model_path: str = MODEL_PATH):
  with open(model_path, "rb") as f:
    model = joblib.load(f)
  return model

def predict_freight_cost(input_data):
  model = load_model()
  input_df = pd.DataFrame(input_data)
  input_df['Predicted_Freight'] = model.predict(input_df).round()
  return input_df

if __name__ == "__main__":
  sample_data = {
    "Dollars": [18500, 5000, 3000, 200]
  }
  prediction = predict_freight_cost(sample_data)
  print(prediction)