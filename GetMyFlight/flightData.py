from datetime import timedelta, datetime as dt
import os
import requests as rq

apiKey = os.environ["Tequila_Key"]


class FlightData:
    def __init__(self, flight_from_code, flight_to_code):
        self.price = 0
        self.flightFromCode = flight_from_code
        self.flightToCode = flight_to_code
        # self.departureCity = departure_city
        self.departureDateFrom = (dt.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        self.departureDateTo = (dt.now() + timedelta(days=180)).strftime("%d/%m/%Y")

    ## Search Flights:
    def get_lower_price(self):
        search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        header = {"apikey": apiKey, "Content-Type": "application/json"}
        print("fly_from:", self.flightFromCode, "fly_to:", self.flightToCode, "date_from:", self.departureDateFrom,
              "date_to:", self.departureDateTo)

        params = {
            "fly_from": self.flightFromCode,
            "fly_to": self.flightToCode,
            "date_from": self.departureDateFrom,
            "date_to": self.departureDateTo,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0,
            "locale": "en",
        }
        response = rq.get(url=search_endpoint, params=params, headers=header)
        if response.json()["_results"] == 0:
            return 0
        else:
            self.price = response.json()["data"][0]["price"]
            date = response.json()["data"][0]["local_departure"]
            flight_date = date[:10]
            print("response.status_code =", response.status_code)
            print(f"This is the flight_date: { flight_date}")
            print(f"This is the price: { self.price}")
            return self.price, flight_date
        # print("data =", response.json())



