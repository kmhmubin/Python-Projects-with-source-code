import os
import requests
from datetime import datetime

# Constant for apis

APP_ID = "0a2b2c85"
API_KEY = "02462c197f879c28a08f5c389fc83d87"

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety api endpoint
SHEETY_ENDPOINT = "https://api.sheety.co/7bdab4900d8f11059efacc57af848a27/myWorkouts/workouts"

# sheet authentication
USERNAME = "coderuseless"
PASSWORD = "CUCl*8ry0CB&7P*elas$"

# constant for user
GENDER = "male"
WEIGHT_KG = 78.1
HEIGHT_CM = 176.53
AGE = 23

# exercise input 
exercise_input = input("Tell me which exercise you did: ")

# exercise api header
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# exercise response
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_parameters, headers=headers)
result = response.json()
# print(result)

# ----------- Excel sheet ----------- # 
# today date and current time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# add those values into the excel sheet
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, auth=(USERNAME, PASSWORD))

    print(sheet_response.text)
