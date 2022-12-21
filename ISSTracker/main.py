import requests
from datetime import *
from time import sleep
import smtplib

MY_LAT = 11.1111111  # your location latitude
MY_LNG = 11.1111111  # your location longitude
MY_EMAIL = "username@gmail.com"
MY_PASSWORD = "password"  # Given by Gmail To Use In Apps


def iss_locator():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if iss_lat in range(6, 16) and iss_lng in range(6, 16):
        return True


# to confirm if is night in your location when the iss is approaching.
def detect_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,  # Change the time format to 24hrs
    }
    # get info about sunrise and sunset in your location.
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # get only the hour from sunrise and sunset in your location.
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True


active = True

while active:
    # if this 2 events happen you'll receive an email.
    if iss_locator() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is approaching you")

        connection.close()
    # Allows you to update the process every 60 seconds if you activate the code in a daily task.
    sleep(60)
