import smtplib
from hidden_config_file import my_email, password
import datetime as dt
import random
import pandas as pd


def send_email(message, addressee):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=addressee, msg=message)


birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")
today = dt.datetime.now()
birthdays_men = []

for birthday in birthdays:
    if birthday["day"] == today.day and birthday["month"] == today.month:
        birthdays_men.append(birthday)

for man in birthdays_men:
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        subject = "Subject:Happy Birthday!\n\n"
        letter = file.read().replace("[NAME]", man['name'])
        send_email(f"{subject}{letter}", man['email'])
        print(letter)
