import requests as rq
import os

apiKey = os.environ["Tequila_Key"]
sheety_Token = os.environ["Sheety_Token"]


class DataManager:
    def __init__(self, city, iatacode, id, lowestprice):
        self.url = 'https://api.sheety.co/2cd01f49c403153f17de4b6be63293b4/getMyFlight/prices/'
        self.header = {"Content-Type": "application/json", "Authorization": sheety_Token}
        self.city = city
        self.iataCode = iatacode
        self.id = id
        self.lowestPrice = lowestprice

    def edit_sheet(self):
        """Edit a row in your Spreadsheet."""
        url = self.url + str(self.id)
        body = {
            "price": {
                "city": self.city,
                "iataCode": self.iataCode,
                "lowestPrice": self.lowestPrice,
                "id": self.id
            }
        }
        response = rq.put(url=url, json=body, headers=self.header)

        data = response.json()
        print("response.status_code =", response.status_code)
        print("response.text =", response.text)
        print(data)
