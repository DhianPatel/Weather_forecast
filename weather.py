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


  response = requests.get(url)
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
