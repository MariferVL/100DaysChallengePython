import json
import os
from twilio.rest import Client

import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
apiKey = "3f043878b843e805021e59fd3a499118"
lat = -33.005916
lon = -71.5414576
parameters = {"lat": lat,
              "lon": lon,
              "appid": apiKey,
              "exclude": "current,minutely,daily",
              }

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# TODO chequear clave activa
# response = requests.get(OWM_Endpoint, params=parameters)
# response.raise_for_status()
# weather_data = response.json()
# print(weather_data)

# Opening JSON file
file = open("testing.json")
# returns JSON object as a dictionary
data = json.load(file)

# Closing file
file.close()

# weatherHourly = data["hourly"]
#
# print(weatherHourly)
#
# for i in range(0, 12):
#     if weatherHourly[i]["weather"][0]["id"] < 700:
#         print("Bring an umbrella☔")


# Course Version:
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="Bring an umbrella☔",
            from_="+12517662823",
            to="+56978665819"
        )

    print(message.status)
