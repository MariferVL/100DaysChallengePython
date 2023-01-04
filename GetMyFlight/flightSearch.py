import os
import requests as rq

apiKey = os.environ["Tequila_Key"]


class FlightSearch:
    def __init__(self):
        self.url = "https://api.tequila.kiwi.com"
        self.code = ""
        self.header = {"apikey": apiKey, "Content-Type": "application/json"}

# TODO catch IndexError
    def get_city_code(self, city):
        id_endpoint = self.url + "/locations/query"
        params = {
            "term": city,
            "locations_type": "city",
            "locale": "en - US",
            "location_types": "city",
            "limit": 1,
            "active_only": True,
        }

        response = rq.get(url=id_endpoint, params=params, headers=self.header)
        self.code = response.json()["locations"][0]["code"]

        print("response.status_code =", response.status_code)
        print(f"This is the city code: {self.code}")
        return self.code

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
