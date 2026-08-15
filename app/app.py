import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------------------------
# Load model
# --------------------------------------------------

model = joblib.load("models/house_price_pipeline.pkl")

# --------------------------------------------------
# Load original data
# Used only to populate City and ZIP dropdowns
# --------------------------------------------------

df = pd.read_csv("data/raw/house_data.csv")

# Get cities
cities = sorted(df["city"].dropna().unique())

# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666666;
        margin-bottom: 30px;
    }

    .prediction-box {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        background-color: #E8F5E9;
        border: 1px solid #A5D6A7;
        margin-top: 25px;
    }

    .prediction-label {
        font-size: 18px;
        color: #444444;
    }

    .prediction-price {
        font-size: 40px;
        font-weight: 700;
        color: #2E7D32;
    }

    .footer {
        text-align: center;
        color: #888888;
        font-size: 14px;
        margin-top: 50px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning powered house price prediction</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# House Information
# --------------------------------------------------

st.subheader("🏡 House Information")

col1, col2, col3 = st.columns(3)

with col1:
    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        max_value=20,
        value=3
    )

with col2:
    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0.0,
        max_value=20.0,
        value=2.0,
        step=0.5
    )

with col3:
    floors = st.number_input(
        "Floors",
        min_value=1.0,
        max_value=5.0,
        value=1.0,
        step=0.5
    )

col1, col2, col3 = st.columns(3)

with col1:
    sqft_living = st.number_input(
        "Living Area (sqft)",
        min_value=0,
        value=1800,
        step=100
    )

with col2:
    sqft_lot = st.number_input(
        "Lot Area (sqft)",
        min_value=0,
        value=5000,
        step=100
    )

with col3:
    sqft_above = st.number_input(
        "Above Ground Area (sqft)",
        min_value=0,
        value=1500,
        step=100
    )

col1, col2, col3 = st.columns(3)

with col1:
    sqft_basement = st.number_input(
        "Basement Area (sqft)",
        min_value=0,
        value=300,
        step=50
    )

with col2:
    yr_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2026,
        value=1985
    )

with col3:
    yr_renovated = st.number_input(
        "Year Renovated",
        min_value=0,
        max_value=2026,
        value=0
    )

# --------------------------------------------------
# Property characteristics
# --------------------------------------------------

st.subheader("🔎 Property Characteristics")

col1, col2, col3 = st.columns(3)

with col1:
    waterfront = st.selectbox(
        "Waterfront",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

with col2:
    view = st.number_input(
        "View Rating",
        min_value=0,
        max_value=4,
        value=0
    )

with col3:
    condition = st.number_input(
        "Condition",
        min_value=1,
        max_value=5,
        value=3
    )

# --------------------------------------------------
# Location
# --------------------------------------------------

st.subheader("📍 Location")

col1, col2 = st.columns(2)

with col1:

    city = st.selectbox(
        "City",
        options=cities
    )

with col2:

    # Get ZIP codes belonging to selected city
    city_zips = sorted(
        df.loc[df["city"] == city, "statezip"]
        .dropna()
        .unique()
    )

    statezip = st.selectbox(
        "State / ZIP Code",
        options=city_zips
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.divider()

predict_button = st.button(
    "🔮 Predict House Price",
    use_container_width=True
)

if predict_button:

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
        "street": [df[df["city"] == city]["street"].iloc[0]],
        "city": [city],
        "statezip": [statezip]
    })

    prediction = model.predict(input_data)

    predicted_price = prediction[0]

    st.markdown(
        f"""
        <div class="prediction-box">
            <div class="prediction-label">
                Estimated House Price
            </div>
            <div class="prediction-price">
                ${predicted_price:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Designed and built by <b>Harish Sharma</b><br>
        Machine Learning House Price Prediction Project
    </div>
    """,
    unsafe_allow_html=True
)