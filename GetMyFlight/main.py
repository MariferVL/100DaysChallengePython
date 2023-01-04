import os
import requests as rq
from datetime import datetime as dt
from pprint import pprint
from flightSearch import FlightSearch

apiKey = os.environ["Tequila_Key"]
sheety_Token = os.environ["Sheety_Token"]

# Getting current date and time
today = dt.now().strftime("%d/%m/%Y")
now = dt.now().strftime("%X")

# TODO Use Flight Search and Sheety API to populate Google Sheet with IATA codes for e/city.
# TODO Check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
# TODO  If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
# TODO  SMS should include: 1.departure airport IATA code, 2.destination airport IATA code, 3.departure city, 4.destination city, 5.flight price and 6.flight dates. e.g.

# User Queries
# TODO create a fn to get the Cities IDs.
# flyFrom = input("Enter the city from where you travel: \n")
# flyFromCode = "SCL"
# flyTo = input("Enter the city/cities where you want to go split by a space: \n")
# flyToCode = "buscar"
# flyDateFrom = input("Enter the date you plan to travel. Format: mm/dd/yyyy: \n")
# flyDateTo = input("Enter the date you plan to comeback. Format: mm/dd/yyyy: \n")
#
# destinations = flyTo.split()
# destinationsCodes = []
# for city in destinations:
#     # Acquire city IDs with Locations API:
#     tequilaIDEndpoint = "https://api.tequila.kiwi.com/locations/query"
#     header = {"apikey": apiKey, "Content-Type": "application/json"}
#
#     params = {
#         "term": city,
#         "locations_type": "city",
#         "apikey": apiKey
#     }
#     response = rq.get(url=tequilaIDEndpoint, params=params, headers=header)
#     print(f"This is the response: {response}")
#     cityID = response.json()
#     destinationsCodes.append(cityID)
#     print(f"This is the city ID: {cityID}")
#
# print(destinationsCodes)
# ## Search Flights:
#
# tequilaSearchEndpoint = "https://api.tequila.kiwi.com/search"
#
# parameters = {
#     "fly_from": flyFromCode,
#     "fly_to": flyTo,
#     "date_from": flyDateFrom,
#     "date_to": flyDateTo,
#     "one_for_city": 1,
#     "sort": "price"
# }
#
# header = {"apikey": apiKey, "Content-Type": "application/json"}
#
# response = rq.post(url=tequilaSearchEndpoint, json=parameters, headers=header)
# userData = response.json()
#
# ## Adding Row to Spreadsheet:

sheetyUrl = 'https://api.sheety.co/2cd01f49c403153f17de4b6be63293b4/getMyFlight/prices'
header = {"Content-Type": "application/json", "Authorization": sheety_Token}
# for i in userData["exercises"]:
#     city = i["met"]
#     iataCode = i["met"]
#     lowestPrice = i["met"]
#     body = {
#         "hoja1": {
#             "city": today, "iataCode": now, "lowestPrice": activity
#         }
#     }
#
#
#     resp = rq.post(url=sheetyUrl, json=body, headers=header)
# print("response.status_code =", resp.status_code)
# print("response.text =", resp.text)
resp = rq.get(url=sheetyUrl, headers=header)

jsonData = resp.json()
sheetData = jsonData["prices"]

pprint(sheetData)

for item in sheetData:
    iataCode = FlightSearch()
    item["iataCode"] = iataCode.get_city_code()
    print(item["iataCode"])

print(sheetData)
