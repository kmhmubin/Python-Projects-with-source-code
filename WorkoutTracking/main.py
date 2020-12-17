import os
import requests

# Constant for apis

APP_ID = os.getenv("EXERCISE_ID")
API_KEY = os.getenv("EXERCISE_API_KEY")

NUTRITIONIX_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"

# constant for user
GENDER = "male"
WEIGHT_KG = 78.1
HEIGHT_CM = 176.53
AGE = 23

# exercise input
exercise_input = input("Tell me which exercise you did: ")

# api header
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
print(result)
