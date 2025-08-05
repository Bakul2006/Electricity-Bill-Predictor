import streamlit as st
import joblib
import numpy as np

# Load saved model
model, _ = joblib.load('pipeline_model.joblib')


st.title("💡 Electricity Cost Prediction")

# Input fields
water_consumption = st.number_input("Water Consumption", min_value=0.0)
site_area = st.number_input("Site Area", min_value=0.0)

# Predict button
if st.button("Predict"):
    input_data = np.array([[ water_consumption, site_area]])
    prediction = model.predict(input_data)[0]
    st.success(f"🔋 Predicted Electricity Cost: ₹ {prediction:.2f}")
