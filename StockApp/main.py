import datetime
import os
import requests
from twilio.rest import Client
from datetime import date, timedelta, datetime
from itertools import islice

STOCK = "MSFT"
COMPANY_NAME = "Microsoft Corp"
news_list = []

# Twilio Data:
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Current Date and time:
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = date.today()
# Yesterday date
yesterday = current_date - timedelta(days=1)
before_yesterday = current_date - timedelta(days=2)

# Stock Api:
alpha_apiKey = os.environ['ALPHA-VANTAGE-Key']
Alpha_Endpoint = "https://www.alphavantage.co/query"
parameters = {"function": "TIME_SERIES_DAILY_ADJUSTED",
              "symbol": STOCK,
              "interval": "5min",
              "apikey": alpha_apiKey,
              }

response = requests.get(Alpha_Endpoint, params=parameters)
response.raise_for_status()
alpha_data = response.json()
timeseries = alpha_data["Time Series (Daily)"]


def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))


n_items = take(2, timeseries.items())

i = 0
stockClosed = []
for key in n_items:
    value = n_items[i][1]["4. close"]
    stockClosed.append(value)
    i += 1

priceBYesterday = float(stockClosed[1])
priceYesterday = float(stockClosed[0])
difference = (priceYesterday - priceBYesterday)
percent = round(((difference * priceBYesterday) / 100), 2)

# To get the news related with the stock change date.
lastStock = n_items[0][0]
secondLastStock = n_items[1][0][0]

# News Api:
apiKey = os.environ['NEWSapiKey']
NEWS_Endpoint = "https://newsapi.org/v2/everything"
parameters = {"q": COMPANY_NAME,
              "from": secondLastStock,
              "to": lastStock,
              "sortBy": "popularity",
              "apiKey": apiKey,
              "language": "en",
              "pageSize": "3",
              "searchIn": "title,description",
              }

response = requests.get(NEWS_Endpoint, params=parameters)
response.raise_for_status()
news_data = response.json()
print(news_data)


def send_msg(number, percent_change):
    index = 0
    for _ in news_data:
        news_title = news_data["articles"][i]["title"]
        # noinspection SpellCheckingInspection
        news_descrip = news_data["articles"][i]["description"]
        if percent_change == "decrease":
            change = f"📉{number}%"
            print(f"Get News cause is {change}")

        elif percent_change == "increase":
            change = f"📈{number}%"
            print(f"Get News cause is {change}")
        stock_msg = f"\n{STOCK}: {change} \n📰Title: {news_title}\nDescription: {news_descrip} "
        index += 1
        news_list.append(stock_msg)


important_change = False
percent = 6
if -5 >= percent:
    decrease = percent * -1
    send_msg(decrease, "decrease")
    print("Get News cause is lower")
    important_change = True
elif percent >= 5:
    send_msg(percent, "increase")
    print("Get News cause is higher")
    important_change = True
else:
    print("not big change")

print(news_list)
if important_change:
    for msg in news_list:
        print(msg)
    #     client = Client(account_sid, auth_token)
    #
    #     message = client.messages \
    #         .create(
    #             body=msg,
    #             from_="+12517662823",
    #             to="+56978665819",
    #         )
    #
    # print(message.status)

# Send a seperate message with the percentage change and each article's title and description to your phone number.
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
