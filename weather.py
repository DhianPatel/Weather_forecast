import requests

city = input("What city do you want to see weather condition for? ")

url = "http://api.weatherapi.com/v1/current.json?key=371d208957f5498082c100904260210&q="+ city +"&aqi=no"


temp = requests.get(url).json().get("current").get("temp_c")

condition = requests.get(url).json().get("current").get("condition").get("text")

wea = requests.get(url).json().get("current").get("temp_f")

print("Weather of", city, "is", temp, "Celsius", wea, "Fahrenheit and condition is", condition)

