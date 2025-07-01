import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast")

place = st.text_input("Place")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the no. of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temps = [temp["main"]["temp"]/10 for temp in filtered_data]/10
            dates = [date["dt_txt"] for date in filtered_data]
            figure = px.line(x=dates, y=temps, labels={"x":"Date","y":"Temperature(C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear":r"images\clear.png", "Clouds":r"images\cloud.png", "Rain":r"images\rain.png", "Snow":r"images\snow.png"}
            sky = [sky["weather"][0]["main"] for sky in filtered_data]
            image_paths = [images[condition] for condition in sky]
            st.image(image_paths, width=115)
    except KeyError:
        st.info("Invalid place name.")