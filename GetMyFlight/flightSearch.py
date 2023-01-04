import os
import requests as rq

apiKey = os.environ["Tequila_Key"]


class FlightSearch:
    def __init__(self):
        self.code = ""
        self.header = {"apikey": apiKey, "Content-Type": "application/json"}

    def get_city_code(self, city):
        tequila_id_endpoint = "https://api.tequila.kiwi.com/locations/query"
        params = {
                    "term": city,
                    "locations_type": "city",
                    "apikey": apiKey
                }

        response = rq.get(url=tequila_id_endpoint, params=params, headers=self.header)
        print(f"This is the response: {response}")
        city_id = response.json()
        print(f"This is the city ID: {city_id}")
        print("response.status_code =", response.status_code)
        print("response.text =", response.text)
        # self.code = "Testing"
        # return self.code



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
