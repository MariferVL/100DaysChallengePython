from datetime import timedelta, datetime as dt

# Getting current date and time
date = (dt.now() + timedelta(days=180)).strftime("%d/%m/%Y")
print(date)


class FlightData:
    def __init__(self, departure_airport_code, departure_city):
        self.price = 0
        self.departureAirportCode = departure_airport_code
        self.departureCity = departure_city
        self.departureDate = date
