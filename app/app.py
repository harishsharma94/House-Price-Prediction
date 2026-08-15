import streamlit as st
import pandas as pd
import joblib

# Load saved pipeline
model = joblib.load(
    "models/house_price_pipeline.pkl"
)

st.title("House Price Prediction")

bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
sqft_living = st.number_input("Living Area (sqft)")
sqft_lot = st.number_input("Lot Area (sqft)")
floors = st.number_input("Floors")
waterfront = st.number_input("Waterfront")
view = st.number_input("View")
condition = st.number_input("Condition")
sqft_above = st.number_input("Above Ground Area")
sqft_basement = st.number_input("Basement Area")
yr_built = st.number_input("Year Built")
yr_renovated = st.number_input("Year Renovated")

city = st.text_input("City")
statezip = st.text_input("State/ZIP")

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "sqft_living": [sqft_living],
        "sqft_lot": [sqft_lot],
        "floors": [floors],
        "waterfront": [waterfront],
        "view": [view],
        "condition": [condition],
        "sqft_above": [sqft_above],
        "sqft_basement": [sqft_basement],
        "yr_built": [yr_built],
        "yr_renovated": [yr_renovated],
        "city": [city],
        "statezip": [statezip]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")
