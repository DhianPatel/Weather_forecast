import requests
import streamlit as st

st.set_page_config(page_title="Dhian's Weather Forecast App", page_icon="🌤️")
st.title("Dhian's Weather Forecast App")
st.write(
    "Check live weather conditions in Celsius and Fahrenheit for any city"
    " worldwide."
)

city = st.text_input("What city do you want to see weather condition for? ")

if city:
  url = "https://weatherapi.com"
  params = {"key": st.secrets["WEATHER_API_KEY"], "q": city, "aqi": "no"}

  response = requests.get(url, params=params)
  if response.status_code == 200:
    data = response.json()
    temp = data.get("current").get("temp_c")
    condition = data.get("current").get("condition").get("text")
    wea = data.get("current").get("temp_f")
    st.write(
        "Weather of",
        city,
        "is",
        temp,
        "Celsius",
        wea,
        "Fahrenheit and condition is",
        condition,
    )
  else:
    st.error(f"API Error {response.status_code}: {response.text}")
