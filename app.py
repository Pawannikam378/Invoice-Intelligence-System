import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag

st.set_page_config(page_title="Vendor Invoice Intelligence Prediction", page_icon="📦", layout="wide")


st.markdown("""
# 📦 Vendor Invoice Intelligence Portal
### AI-Driven Freight Cost Prediction & Invoice Risk Flagging

This internal analytics portal leverages machine learning to:
- **Forecast freight cost accurately**
- **Detect risky or abnormal vendor invoices**
- **Flag invoices that may require manual review**
- **Optimize transportation spending**
""")

st.divider()

# ---------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------
st.sidebar.title("🔍 Model Selector")
selected_model = st.sidebar.radio(
    "Choose Prediction Module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("""
---
**Business Impact**
- Improved cost forecasting
- Reduced invoice fraud & anomalies
- Faster finance operations
""")

# ---------------------------------------------------------------
# Freight Cost Prediction
# ---------------------------------------------------------------
if selected_model == "Freight Cost Prediction":
    st.subheader("🚚 Freight Cost Prediction")

    st.markdown("""
    **Objective:**
    Predict freight for a vendor invoice using **Invoice Dollars**
    to support budgeting, forecasting, and vendor negotiation.
    """)
    with st.form("freight_form"):
        col1, col2 = st.columns(2)
        with col1:
            dollars = st.number_input(
                "💲 Invoice Dollars",
                min_value=1.0,
                value=18500.0,
            )
        with col2:
            st.write("")  # Spacer

        submit_freight = st.form_submit_button("🔮 Predict Freight Cost")

    if submit_freight:
        input_data = {
            "Dollars": [dollars]
        }

        result = predict_freight_cost(input_data)
        prediction = result['Predicted_Freight'].iloc[0]

        st.success("Prediction completed successfully!")

        st.metric(
            label="📦 Estimated Freight Cost",
            value=f"${prediction:,.2f}"
        )



# ---------------------------------------------------------------
# Invoice Flag Prediction
# ---------------------------------------------------------------
else:
    st.subheader("🚩 Invoice Manual Approval Flag")

    st.markdown("""
    **Objective:**
    Predict whether a vendor invoice should be **flagged** for manual approval
    based on abnormal cost, freight, or delivery patterns.
    """)
    with st.form("invoice_flag_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            invoice_quantity = st.number_input(
                "📦 Invoice Quantity",
                min_value=1,
                max_value=12000,
                value=50
            )
            freight_cost = st.number_input(
                "🚚 Freight Cost",
                min_value=0.0,
                max_value=12000.0,
                value=1.73
            )
        with col2:
            invoice_dollars = st.number_input(
                "💲 Invoice Dollars",
                min_value=1.0,
                value=162.0,
            )
            total_item_quantity = st.number_input(
                "📊 Total Item Quantity",
                min_value=1,
                max_value=12000,
                value=162
            )
        with col3:
            total_item_dollars = st.number_input(
                "💰 Total Item Dollars",
                min_value=1.0,
                max_value=100000.0,
                value=2467.0,
            )

        submit_flag = st.form_submit_button("🔮 Evaluate Invoice Flag")

    if submit_flag:
        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight_cost],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        result = predict_invoice_flag(input_data)
        flag_prediction = result['Predicted_Invoice_Flag'].iloc[0]

        is_flagged = bool(flag_prediction)

        if is_flagged:
            st.error("⚠️ Invoice requires **MANUAL APPROVAL**")
        else:
            st.success("✅ Invoice is **SAFE for Auto-Approval**")

        st.metric(
            label="🚩 Invoice Flag Result",
            value="FLAGGED" if is_flagged else "SAFE"
        )
