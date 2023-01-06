import requests as rq
import os

apiKey = os.environ["Tequila_Key"]
sheety_Token = os.environ["Sheety_Token"]


class DataManager:
    def __init__(self, city, iata_code, id):
        self.url = 'https://api.sheety.co/2cd01f49c403153f17de4b6be63293b4/getMyFlight/prices/'
        self.header = {"Content-Type": "application/json", "Authorization": sheety_Token}
        self.city = city
        self.iata_Code = iata_code
        self.id = id

    def edit_code(self):
        """Edit a row in your Spreadsheet."""
        url = self.url + str(self.id)
        body = {
            "price": {
                "iataCode": self.iata_Code
            }
        }
        response = rq.put(url=url, json=body, headers=self.header)
        print("response.status_code =", response.status_code)

    def edit_price(self, lowest_price, flight_date):
        """Edit flightDate and lowestPrice row  in your Spreadsheet."""
        url = self.url + str(self.id)
        body = {
            "price": {
                "flightDate": flight_date,
                "lowestPrice": lowest_price,
            }
        }
        response = rq.put(url=url, json=body, headers=self.header)
        print("response.status_code =", response.status_code)
