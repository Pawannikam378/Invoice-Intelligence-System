import joblib
import pandas as pd

Model_Path = "C:\Users\sai\Downloads\data-20260317T165009Z-1-001\data\models\predict_freight_model.pkl"


def load_model(model_path: str = MODEL_PATH):
  with open(model_path, "rb") as f:
    model = joblib.load(f)
  return model

def predict_invoice_flag(input_data):
  model = load_model()
  input_df = pd.DataFrame(input_data)
  input_df['Predicted_Invoice_Flag'] = model.predict(input_df)
  return input_df

if __name__ == "__main__":
  sample_data = {
    "Dollars": [18500, 5000, 3000, 200]
  }
  prediction = predict_invoice_flag(sample_data)
  print(prediction)