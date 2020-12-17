# Rain Alert Using twilio

import requests

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

API_KEY = "f32840ec9669473b25c131c30a91e3e3"

weather_parameters = {
    "lat": 23.870038,
    "lon": 90.408723,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(API_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
# slice the weather data
weather_slice = weather_data["hourly"][:12]

# will it rain
will_rain = False

# check the weather condition
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
