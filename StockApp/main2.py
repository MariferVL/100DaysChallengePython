import os
import requests
from twilio.rest import Client
from datetime import date, timedelta
from itertools import islice

STOCK = "MSFT"
COMPANY_NAME = "Microsoft Corp"
news_list = []

# Current and Yesterday Date:
current_date = date.today()
yesterday = current_date - timedelta(days=1)
before_yesterday = current_date - timedelta(days=2)

# Twilio Data:
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Stock API:
alpha_apiKey = os.environ['ALPHA-VANTAGE-Key']
Alpha_Endpoint = "https://www.alphavantage.co/query"
parameters = {"function": "TIME_SERIES_DAILY_ADJUSTED",
              "symbol": STOCK,
              "interval": "5min",
              "apikey": alpha_apiKey,
              }

response = requests.get(Alpha_Endpoint, params=parameters)
response.raise_for_status()
timeseries = response.json()["Time Series (Daily)"]

# Return the first n items of the iterable as a list.
n_items = list(islice(timeseries.items(), 2))

stockClosed = [item[1]["4. close"] for item in n_items]
priceYesterday = float(stockClosed[0])
priceBYesterday = float(stockClosed[1])
difference = (priceYesterday - priceBYesterday)
percent = round(((difference * priceBYesterday) / 100), 2)

# To get the news related with the stock event date.
lastStock = n_items[0][0]
print(lastStock)
secondLastStock = n_items[1][0]
print(secondLastStock)

# News API:
apiKey = os.environ['NEWSapiKey']
NEWS_Endpoint = "https://newsapi.org/v2/everything"


def create_msg(change):
    """Create SMS text from News API."""
    parameters = {"q": COMPANY_NAME,
                  "from": secondLastStock,
                  "to": lastStock,
                  "sortBy": "popularity",
                  "apiKey": apiKey,
                  "language": "en",
                  "pageSize": "3",
                  "searchIn": "title",
                  }
    response = requests.get(NEWS_Endpoint, params=parameters)
    response.raise_for_status()
    news_data = response.json()
    for item in news_data["articles"]:
        news_title = item["title"]
        stock_msg = f"\n{STOCK}: {change}%\nTitle: {news_title}"
        # Longer version changed because of character limit segmentation.
        # stock_msg = f"\n{STOCK}: {change} \nTitle: {news_title}\nDescription: {news_descrip} "
        news_list.append(stock_msg)


important_change = False

if -5 >= percent or percent >= 5:
    create_msg(percent)
    important_change = True

# Send SMS if the % is > to 5 or -5.
if important_change:
    # for msg in news_list:
    #     client = Client(account_sid, auth_token)
    #     for msg in news_list:
    #         message = client.messages.create(
    #             body=msg,
    #             from_="+123456789",
    #             to="+123456789",
    #         )
