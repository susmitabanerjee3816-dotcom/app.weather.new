import streamlit as st
import requests

st.title("🌤️ Weather App")

API_KEY = st.secrets("OpenWeather_API_KEY")

city = st.text_input("Enter City Name:")

if st.button("Get Weather"):
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            condition = data['weather'][0]['description']
            humidity = data['main']['humidity']

            st.write("---")
            st.subheader(f"Weather in {city}")
            st.success(f"🌡️ Temperature: {temp}°C")
            st.info(f"🌥️ Condition: {condition}")
            st.info(f"💧 Humidity: {humidity}%")
        else:
            st.error("City not found!")
    else:
        st.error("Please enter a city name first!")
