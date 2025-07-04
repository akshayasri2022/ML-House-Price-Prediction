import pandas as pd
import pickle as pk
import streamlit as st

# ✅ Load the model from local repo (not C:\)
model = pk.load(open('bhp.pkl', 'rb'))

# ✅ Load cleaned data from repo
data = pd.read_csv('cleaned_data.csv')

# Streamlit UI
st.header("🏠 Bangalore House Price Predictor")

# User Inputs
loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter total sqft', min_value=500)
beds = st.number_input('Enter number of Bedrooms', min_value=1)
balc = st.number_input('Enter number of Balconies', min_value=0)
bath = st.number_input('Enter number of Bathrooms', min_value=1)

# Prepare input
input_data = pd.DataFrame([[loc, sqft, bath, balc, beds]],
                           columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

# Predict button
if st.button("Predict Price"):
    output = model.predict(input_data)
    price = round(output[0] * 100000, 2)
    st.success(f"🏡 Estimated Price: ₹ {price}")
