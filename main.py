import streamlit as st
import plotly.express as px

st.title("Weather forecast")

place = st.text_input("Place")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the no. of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

