import datetime as dt
import smtplib
from random import choice
import pandas as pd

today = (dt.datetime.now().day, dt.datetime.now().month)
print(today)
## Another option:
# today = dt.datetime.now()
# today_tuple = (today.month, today.day)

data = pd.read_csv("contacts.csv")
# birthday_dict = {(birthday_month, birthday_day): data_row}
birthday_dict = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)

if today in birthday_dict:
    person = birthday_dict[today]
    my_email = "username@gmail.com"
    password = "*********"
    print(person["sex"])
    print(person["email"])
    print(person["name"])

    with open("quotes.txt") as file:
        content = file.readlines()
        message = choice(content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # encript
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=f'Subject:Hi, B-day {person["sex"]} !\n\nHappy B-Day, {person["name"]}!! I wish you the best plus a '
                f'necessary quote for you today:{message}')


