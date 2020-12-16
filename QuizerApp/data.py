import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

# send request to open trivia api
response = requests.get("https://opentdb.com/api.php", params=parameters)
# if errors then raise error
response.raise_for_status()
# grab the data from api
data = response.json()

# print the data
# print(data["results"])

# assign data to a variable
question_data = data["results"]
