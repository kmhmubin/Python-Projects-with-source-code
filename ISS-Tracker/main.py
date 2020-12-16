# international Space Station Tracker
import requests
from datetime import datetime
import smtplib
import time

# Constant values of my latitudes and Longitude
MY_LAT = 23.870013
MY_LONG = 90.408708
EMAIL = "example@example.com"
PASS = "123456789"


def is_iss_overhead():
    # fetching the response from api
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # rise error if failed
    response.raise_for_status()
    # fetching data from api requests
    data = response.json()

    # catching iss latitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # my position is within +5 or -5 degrees of the iss position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }

    # fetching data from sunrise and sunset api
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_data = response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    # current time in hour
    time_now = datetime.now().hour
    # check the time
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    # wait 60 s
    time.sleep(60)
    # if it's night time and iss in my position then sent a notification mail
    if is_iss_overhead() and is_night():
        # connecting the gmail server
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASS)
        # send the mail
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject: Look Up \n\n The ISS is above you in the sky."
        )
