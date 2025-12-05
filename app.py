import streamlit as st
import pandas as pd

st.title("Car Price Prediction Demo (No scikit-learn)")

year = st.number_input("Year", 1990, 2025, 2020)
mileage = st.number_input("Mileage (km)", 0, 500000, 50000)
brand = st.selectbox("Brand", ["Toyota", "Honda"])
condition = st.selectbox("Condition", ["New", "Used"])

# --- Simple fake prediction ---
price = 20000 + (year - 2000)*500 - mileage*0.05
if brand=="Honda":
    price += 1000
if condition=="New":
    price += 5000

if st.button("Predict Price"):
    st.success(f"Estimated Car Price: ${price:,.2f}")
