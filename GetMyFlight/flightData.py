from datetime import timedelta, datetime as dt
import os
import requests as rq

apiKey = os.environ["Tequila_Key"]


class FlightData:
    def __init__(self, flight_from_code,flight_to_code, departure_city):
        self.price = 0
        self.flightFromCode = flight_from_code
        self.flightToCode = flight_to_code
        self.departureCity = departure_city
        self.departureDateFrom = (dt.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        self.departureDateTo = (dt.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        self.return_from = (dt.now() + timedelta(days=187)).strftime("%d/%m/%Y")
        self.return_to = (dt.now() + timedelta(days=217)).strftime("%d/%m/%Y")

## Search Flights:

    def get_lower_price(self):
        search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        header = {"apikey": apiKey, "Content-Type": "application/json"}

        params = {
            "fly_from": self.flightFromCode,
            "fly_to": self.flightToCode,
            "date_from": self.departureDateFrom,
            "date_to": self.departureDateTo,
            "return_from": self.return_from,
            "return_to": self.return_to,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0,
            "sort": "price",
        }

        response = rq.get(url=search_endpoint, params=params, headers=header)
        data = response.json()
        print("response.status_code =", response.status_code)
        print(f"This is the city code: {self.code}")
