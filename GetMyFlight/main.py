import os
import requests as rq
from datetime import datetime as dt

apiKey = os.environ["Nutritionix_Key"]
sheety_Token = os.environ["Sheety_Token"]

# Getting current date and time
today = dt.now().strftime("%d/%m/%Y")
now = dt.now().strftime("%X")

# User Queries

flyFrom = input("Enter the city from where you travel: \n")
flyFromCode = "buscar"
flyTo = input("Enter the city/cities where you want to go split by a space: \n")
flyToCode = "buscar"
flyDateFrom = input("Enter the date you plan to travel. Format: mm/dd/yyyy: \n")
flyDateTo = input("Enter the date you plan to comeback. Format: mm/dd/yyyy: \n")


# Acquire ground transport station IDs
# TODO create a fn for from ann to cities.
tequilaIDEndpoint = "https://api.tequila.kiwi.com/locations/query"

params = {
    "term": flyFrom,
    "locations_type": "city",
    "apikey": apiKey
}

response = rq.get(url=tequilaIDEndpoint, params=params)
userData = response.json()

## Search Flights:

tequilaSearchEndpoint = "https://api.tequila.kiwi.com/search"

parameters = {
    "fly_from": flyFromCode,
    "fly_to": flyTo,
    "date_from": flyDateFrom,
    "date_to": flyDateTo,
    "one_for_city": 1,
    "sort": "quality"
}
# params = {"x-user-jwt": "string(header)", "gender": "string(body)male/female", "weight_kg": "number(body)weight",
#           "height_cm": "number", "age": "number"}

header = {"apikey": appKey, "Content-Type": "application/json"}

response = rq.post(url=tequilaSearchEndpoint, json=parameters, headers=header)
userData = response.json()

## Adding Row to Spreadsheet:

sheetyUrl = 'https://api.sheety.co/2cd01f49c403153f17de4b6be63293b4/getMyFlight/hoja1'
for i in userData["exercises"]:
    distance = i["met"]
    calories = i["nf_calories"]
    activity = i["name"].title()
    duration = i["duration_min"]
    body = {
        "workout": {
            "date": today, "time": now, "exercise": activity, "duration": duration, "calories": calories
        }
    }
    header = {"Content-Type": "application/json", "Authorization": sheety_Token}

    resp = rq.post(url=sheetyUrl, json=body, headers=header)
    print("response.status_code =", resp.status_code)
    print("response.text =", resp.text)
