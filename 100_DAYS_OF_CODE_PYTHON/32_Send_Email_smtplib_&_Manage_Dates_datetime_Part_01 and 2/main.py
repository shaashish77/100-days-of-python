import smtplib
import datetime as dt
import random

MY_EMAIL = "user@mail.com"
PASSWORD = "app code"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    my_email = MY_EMAIL
    password = PASSWORD
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="user@mail.com",
            msg=f"Subject:Monday Motivation \n\n {quote}")
