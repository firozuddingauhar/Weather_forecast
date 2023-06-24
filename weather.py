import requests
import json

api_key = "0a22fefa658c17fe10c45d304fc205f6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

data = response.json()

if data["cod"] != "404":
    main = data["main"]
    current_temperature = main["temp"]
    current_pressure = main["pressure"]
    current_humidity = main["humidity"]
    weather = data["weather"]
    weather_description = weather[0]["description"]

    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ")
