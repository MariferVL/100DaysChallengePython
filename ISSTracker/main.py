import requests
from datetime import *
from time import sleep
import smtplib

MY_LAT = -33.0059115
MY_LNG = -71.5436463
MY_EMAIL = "conectadox.cl@gmail.com"
MY_PASSWORD= "mnpioqealsolsdxn"

def iss_locator():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    if iss_lat in range(-28, -38) and iss_lng in range(-66, -76):
        return True

# Your position is within +5 or -5 degrees of the ISS position.


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # hour in 24 format
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True


active = True

while active:
    if iss_locator() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is approaching you")

        connection.close()

    sleep(60)

