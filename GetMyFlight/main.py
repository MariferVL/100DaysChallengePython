import os
import requests as rq
from datetime import datetime as dt

appID = os.environ["Nutritionix_ID"]
appKey = os.environ["Nutritionix_Key"]
sheety_Token = os.environ["Sheety_Token"]

# Getting current date and time
today = dt.now().strftime("%d/%m/%Y")
now = dt.now().strftime("%X")


## Getting Exercises User info:

tequilaEndpoint = "https://api.tequila.kiwi.com/search"
flightQuery = input("Enter the city where you want to go: \n")
parameters = {
    "query": flightQuery,
}
# params = {"x-user-jwt": "string(header)", "gender": "string(body)male/female", "weight_kg": "number(body)weight",
#           "height_cm": "number", "age": "number"}

header = {"x-app-id": appID, "x-app-key": appKey, "x-remote-user-id": "0", "Content-Type": "application/json"}

response = rq.post(url=tequilaEndpoint, json=parameters, headers=header)
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




