import datetime
import smtplib
import random

my_email= "example@gmaip.com"
my_password= "qwerty123"


now= datetime.datetime.now()
weekday=now.weekday()

if weekday==1:
    with open("./DAY-32/quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote= random.choice(all_quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email, to_addrs= my_email, msg=f"Subject: Qoute of the day\n\n{quote}")
