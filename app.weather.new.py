import streamlit as st
from google import genai
import requests

API_KEY = "9b60f1d9eb5efb0b40963069fb2f23ca"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


#city Input
city = st.text_input("Please Enter City Name ")

if st.button("Get Weather Details"):
      if city:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            st.success("Weather Found")
        else:
            st.error(data.get("message", "Unknown error"))
else:
        st.warning("Please enter a city name")