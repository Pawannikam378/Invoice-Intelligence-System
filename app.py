import streomlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from inference.predict_freight import predict_freight
from inference.predict_invoice_flag import predict_invoice_flag

st.set_page_config(page_title="Vendor Invoice Intelligence Prediction",page_icon="📦", layout="wide")


st.markdown("""
# 📦 Vendor Invoice Intelligence Portal
### AI-Driven Freight Cost Prediction & Invoice Risk Flagging

This internal analytics portal levarage machine learning to 
- **Forecast freight cost accurately**
- **Detect risky or abnormal vendor choice**
- **Flag invoices that may require manual review**
- **Optimize transportation spending**
""")

st.divider()

# ---------------------------------------------------------------
#Sidebar
# ---------------------------------------------------------------
st.sidebar.title("🔍Model Selector")
selected_model = st.sidebar.radio(
    "Choose Prediction Module",
    [
        "Freight Cost Prediction"
        "Invoice Manuel Approval Flag"
    ]
)

st.sidebar.markdown("""
---
**Business Impact**
-- Improved cost forecasting
-- Reduced Invoice fraud & anomalies
-- Faster finance operations
""")

# ---------------------------------------------------------------
# Freigth Cost Prediction
# ---------------------------------------------------------------
if selected_model == "Freight Cost Prediction":
    st.subheader("🚚 Freight Cost Prediction")

    st.markdown("""
    **Objective:**
    Predict freight for a vendor invioce using **Quantity** and **Invoice Dollars**
    to support budgeting, forecasting, and vendor negotiation.
    """)
    with st.form("freight_form"):
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input(
                "📦Quantity",
                min_value=1,
                max_value=12000,
                value=1200
            )
        with col2:
            dollar = st.number_input(
                "Invoice Dollar",
                min_value=1.0,
                value=18500.0,
            )
        
        submit_freight = st.form_submit_button(" Predict Freight Cost")

    if submit_freigth:
        input_data = {
            "Quantity": [quantity]
            "Dollars": [dollars]
        }
        
        prediction = predict_freight_cost(input_data)['Predicted_Freight']

        st.success("Prediction complete successfully.")

        st.metrics(
            label=" Estimated Freight Cost",
            value=f"${prediction:,.2f}"
        )

    

# ---------------------------------------------------------------
# Invoice Flag Prediction
# ---------------------------------------------------------------
else:
    st.subheader("🪧 Invoice Manuel Approval Flag")

    st.markdown("""
    **Objective:**
    Predict weather a vendor invoice should be **flagged** for manual approval**
    based on abnormal cost, freight, or delivery patterns.
    """)
    with st.form("invoice_flag_form"):
        col1, col2 = st.columns(3)
        with col1:
            invoice_quantity = st.number_input(
                "📦Invoice Quantity",
                min_value=1,
                max_value=12000,
                value=50
            )
            freight_cost = st.number_input(
                "📦Freight Cost",
                min_value=0.0,
                max_value=12000,
                value=1.73
            )
        with col2:
            invoice_dollar = st.number_input(
                "Invoice Dollar",
                min_value=1.0,
                value=162.0,
            )
            total_item_quantity = st.number_input(
                "Total Item Quantity",
                min_value=1,
                max_value=12000,
                value=162
            )
        with col3:
            total_item_dollar = st.number_input(
                "Total Item Dollar",
                min_value=1.0,
                max_value=12000,
                value=2467.0,
            )
    
        submit_flag = st.form_submit_button(" Evaluate Invoice Flag")   

    if submit_flag:
        input_data = {
            "Invoice_Quantity": [invoice_quantity],
            "Invoice_Dollar": [invoice_dollar],
            "Freight":[freight]
            "Total_Item_Quantity": [total_item_quantity],
            "Total_Item_Dollar": [total_item_dollar]
        }

        flag_prediction = predict_invoice_flag(input_data)['Predicted Flag']

        is_flagged = bool(flag_prediction[0])

        if is_flagged:
            st.error(" Invoice requires **MANUEL APPORVAL**")
        else:
            st.success('✅ Invoice is **SAFE FOR Auto-Approval**')
        
        prediction = predict_invoice_flag(input_data)['Predicted_Invoice_Flag']

        st.success("Prediction complete successfully.")

        st.metrics(
            label=" Estimated Invoice Flag",
            value=f"{prediction}"
        )
