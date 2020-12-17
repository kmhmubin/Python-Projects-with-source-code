# Rain Alert Using twilio
import os
import requests
from twilio.rest import Client

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
# get the api key from environment variable
API_KEY = os.getenv("OWM_API_KEY")

PHONE_NUMBER = "+12516640218"

# Your Account SID from twilio.com/console
account_sid = os.getenv("ACCOUNT_SID")
# Your Auth Token from twilio.com/console
auth_token = os.getenv("AUTH_TOKEN")

weather_parameters = {
    "lat": 1.352083,
    "lon": 103.819839,
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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's Going to rain today. Remember to bring an Umbrella ",
        from_=PHONE_NUMBER,
        to='+8801713343232'
    )
    print(message.status)
