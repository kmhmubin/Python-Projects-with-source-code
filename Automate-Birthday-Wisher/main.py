import smtplib
import datetime as dt
import random

MY_EMAIL = "example@example.com"
MY_PASSWORD = "aslkdjflsjdlajk"

# current day
now = dt.datetime.now()
# current weekday
weekday = now.weekday()

if weekday == 1:
    with open("qoutes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Monday Motivation \n\n {quote}")
