import json
import os

import requests
from twilio.rest import Client

STOCK = "MSFT"
COMPANY_NAME = "Microsoft Corp"
priceToday = 105
priceYesterday = 100
difference = priceToday - priceYesterday
percent = (difference * priceYesterday) / 100
print(percent)
## Use https://www.alphavantage.co
# TODO When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

if -5.0 >= percent or percent >= 5.0:
    print("Get News")
    print(difference)

#TODO chequear fecha actual
#Stock Api:
alpha_apiKey = os.environ['ALPHA-VANTAGE-Key']
Alpha_Endpoint = "https://www.alphavantage.co/query"
parameters = {"function": "TIME_SERIES_INTRADAY",
              "symbol": STOCK,
              "interval": "5min",
              "apikey": alpha_apiKey,
              }

response = requests.get(Alpha_Endpoint, params=parameters)
response.raise_for_status()
alpha_data = response.json()
print(alpha_data)


##  2: Use https://newsapi.org
# TODO Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# News Api:
apiKey = os.environ['NEWSapiKey']
NEWS_Endpoint = "https://newsapi.org/v2/everything"
parameters = {"q": COMPANY_NAME,
              "from": "2022-12-25",
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




## TODO 3: Use https://www.twilio.com
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

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+15558675310'
#                  )
