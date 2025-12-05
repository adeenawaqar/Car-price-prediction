import streamlit as st
import pandas as pd

st.title("Car Price Prediction App")
st.write("Enter all car details to predict an estimated price:")

year = st.number_input("Year", 1990, 2025, 2020)
mileage = st.number_input("Mileage (km)", 0, 500000, 50000)
engine_size = st.number_input("Engine Size (cc)", 800, 5000, 1500)
horsepower = st.number_input("Horsepower", 50, 1000, 120)

brand = st.selectbox("Brand", ["Toyota", "Honda", "BMW", "Suzuki"])
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
condition = st.selectbox("Condition", ["New", "Used"])
model = st.selectbox("Model", ["Sedan", "Hatchback", "SUV", "Coupe"])

owners = st.number_input("Number of Previous Owners", 0, 10, 1)
accident_history = st.selectbox("Accident History", ["None", "Minor", "Major"])
color = st.selectbox("Color", ["White", "Black", "Silver", "Red", "Blue"])

price = 20000
price += (year - 2000) * 500
price -= mileage * 0.05
price += (engine_size - 1000) * 2
price += horsepower * 10

brand_effect = {"Toyota": 0, "Honda": 1000, "BMW": 5000, "Suzuki": -500}
price += brand_effect.get(brand, 0)

fuel_effect = {"Petrol": 0, "Diesel": 500, "Electric": 8000, "Hybrid": 4000}
price += fuel_effect.get(fuel, 0)

if transmission == "Automatic":
    price += 1000

if condition == "New":
    price += 5000

model_effect = {"Sedan": 0, "Hatchback": -1000, "SUV": 2000, "Coupe": 1500}
price += model_effect.get(model, 0)

price -= owners * 1000

accident_effect = {"None": 0, "Minor": -2000, "Major": -5000}
price += accident_effect.get(accident_history, 0)

color_effect = {"White": 0, "Black": 200, "Silver": 500, "Red": 300, "Blue": 300}
price += color_effect.get(color, 0)

if st.button("Predict Price"):
    st.success(f"Estimated Car Price: ${price:,.2f}")
