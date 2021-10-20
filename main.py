import pandas
import datetime as dt
import random
import smtplib

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
PLACEHOLDER = "[NAME]"
MY_EMAIL = "YOUR EMAIL HERE"
PASSWORD = "YOUR PASSWORD HERE"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")
print(birthdays)

for entry in birthdays:
    if entry["month"] == month and entry["day"] == day:
        random_letter_file_name = random.choice(letters)
        birthday_person = entry["name"]
        birthday_email = entry["email"]
        with open(f"./letter_templates/{random_letter_file_name}") as template_file:
            email_contents = template_file.read()
            new_email = email_contents.replace(PLACEHOLDER, birthday_person)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg=f"Subject:Happy Birthday\n\n{new_email}"
            )



