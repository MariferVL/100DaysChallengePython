import os
import requests as rq
from datetime import datetime as dt
from pprint import pprint
from flightSearch import FlightSearch
from dataManager import DataManager

apiKey = os.environ["Tequila_Key"]
sheety_Token = os.environ["Sheety_Token"]

# Getting current date and time
today = dt.now().strftime("%d/%m/%Y")
now = dt.now().strftime("%X")

# TODO Check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
# TODO  If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
# TODO  SMS should include: 1.departure airport IATA code, 2.destination airport IATA code, 3.departure city, 4.destination city, 5.flight price and 6.flight dates. e.g.

## User Queries
# flyFrom = input("Enter the city from where you travel: \n")
# flyTo = input("Enter the city/cities where you want to go split by a comma: \n")
# flyDateFrom = input("Enter the date you plan to travel. Format: dd/mm/yyyy: \n")
# flyDateTo = input("Enter the date you plan to comeback. Format: dd/mm/yyyy: \n")


## Get Spreadsheet data:

sheetyUrl = 'https://api.sheety.co/2cd01f49c403153f17de4b6be63293b4/getMyFlight/prices'
header = {"Content-Type": "application/json", "Authorization": sheety_Token}

resp = rq.get(url=sheetyUrl, headers=header)
sheetData = resp.json()["prices"]

for item in sheetData:
    iataCode = FlightSearch()
    item["iataCode"] = iataCode.get_city_code(item["city"])
    new_item = DataManager(item["city"], item["iataCode"], item["id"], item["lowestPrice"])
    new_item.edit_sheet()

