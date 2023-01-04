import os
from twilio.rest import Client
import requests

# Get the Weather Data:
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_apiKey = os.environ["Open_Weather_map_Key"]
lat = -33.0000000
lon = -77.0000000
parameters = {"lat": lat,
              "lon": lon,
              "appid": OWM_apiKey,
              }

# Set the SMS server:
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# Set Rain Alert:
weather_slice = weather_data["list"][:3]
will_rain = False

for every3hrs_data in weather_slice:
    condition_code = every3hrs_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
#
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="Bring an umbrella ☔",
            from_="+123456789",
            to="+123456789",
        )

    print(message.status)
