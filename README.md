# Invoice Intelligence System

This project is a web application for predicting freight costs and flagging vendor invoices for manual approval using machine learning.

## Features

- **Freight Cost Prediction**: Predict freight costs based on quantity and invoice dollars.
- **Invoice Flagging**: Predict whether an invoice should be flagged for manual approval based on various invoice metrics.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd data
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using Streamlit:

```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main Streamlit application
- `inference/`: Contains prediction logic
  - `predict_freight.py`: Freight cost prediction
  - `predict_invoice_flag.py`: Invoice flagging prediction
- `models/`: Trained machine learning models
- `data/`: Sample data files

## License

This project is licensed under the terms of the MIT license.