import requests
from datetime import datetime

# PIXELA API CONSTANTS

USERNAME = "kmhmubin"
TOKEN = "alsdljsldjlasjdjkjls"
GRAPH_ID = "code-graph"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

CREATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# Create a user account on Pixela
# user parameters
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode",
}

# sent the request to the server for create an user account
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)
# account created -> https://pixe.la/@kmhmubin


# create the graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "ichou",
    "timezone": "Asia/Dhaka",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# sent the post request and create graph
# graph_response = requests.put(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(graph_response.text)

# Create pixel data

# get today date
today = datetime(year=2020, month=12, day=23)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7.2",
}

# # sent request and create pixel
pixel_response = requests.post(url=PIXELA_ENDPOINT, json=pixel_data, headers=headers)
print(pixel_response.text)
