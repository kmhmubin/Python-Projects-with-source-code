import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API KEYS
STOCK_API_KEY = os.environ['STOCK_API']
NEWS_API_KEY = os.environ['NEWS_API']

ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

PHONE_NUMBER = "+12516640218"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stockData = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stockData.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

difference_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(difference_percent)

# If TODO4 percentage is greater than 5 then print("Get News").
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# Use Python slice operator to create a list that contains the first 3 articles. Hint:
#  https://stackoverflow.com/questions/509211/understanding-slice-notation

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.
if abs(difference_percent) > 5:
    # get the news
    news_parameters = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    three_article = articles[:3]
    # print(three_article)

# Create a new list of the first 3 article's headline and description using list comprehension.
formatted_article = [f"{STOCK_NAME}: {up_down} {difference_percent}% \n\nHeadline: {article['title']}. \n\nBrief:" \
                     f" {article['description']}"
                     for
                     article in
                     three_article]
# Send each article as a separate message via Twilio.
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

for article in formatted_article:
    message = client.messages \
        .create(
        body=article,
        from_=PHONE_NUMBER,
        to='+8801723896989'
    )

# print(message.sid)

# Optional: Format the message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or 
"TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash. """
