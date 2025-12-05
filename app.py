import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

st.title("Car Price Prediction App")
st.write("Enter car details to predict its price:")

# --- Feature names ---
feature_columns = [
    "Year", "Mileage",
    "Brand_Toyota", "Brand_Honda",
    "Fuel_Petrol", "Fuel_Diesel",
    "Transmission_Manual", "Transmission_Automatic",
    "Condition_New", "Condition_Used"
]

# --- Train a dummy Decision Tree model (for demo only) ---
X_dummy = pd.DataFrame([[0]*len(feature_columns)], columns=feature_columns)
y_dummy = [0]  # dummy target
model = DecisionTreeRegressor()
model.fit(X_dummy, y_dummy)

# --- User Inputs ---
year = st.number_input("Year", 1990, 2025, 2020)
mileage = st.number_input("Mileage (km)", 0, 500000, 50000)
brand = st.selectbox("Brand", ["Toyota", "Honda"])
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
condition = st.selectbox("Condition", ["New", "Used"])

# --- Prepare input for prediction ---
user_input = {
    "Year": year,
    "Mileage": mileage,
    "Brand_Toyota": 1 if brand=="Toyota" else 0,
    "Brand_Honda": 1 if brand=="Honda" else 0,
    "Fuel_Petrol": 1 if fuel=="Petrol" else 0,
    "Fuel_Diesel": 1 if fuel=="Diesel" else 0,
    "Transmission_Manual": 1 if transmission=="Manual" else 0,
    "Transmission_Automatic": 1 if transmission=="Automatic" else 0,
    "Condition_New": 1 if condition=="New" else 0,
    "Condition_Used": 1 if condition=="Used" else 0
}

input_df = pd.DataFrame([user_input])

# --- Prediction ---
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Car Price: ${prediction:,.2f}")

st.write("Note: Replace the dummy model with your trained Decision Tree for real predictions.")

