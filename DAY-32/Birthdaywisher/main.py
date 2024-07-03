from datetime import datetime
import pandas
import smtplib
import random

MY_EMAIL= "example@gmail.com"
MY_PASSWORD= "qwerty123"

today= datetime.now()
today_tuple= (today.month, today.day)

data= pandas.read_csv("./DAY-32/Birthdaywisher/birthdays.csv")

# birthdays_dict= {(birthday_day, birthday_month): data_row}

birthdays_dict= { (data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()}
# print(birthdays_dict) 

if today_tuple in birthdays_dict:
    birthday_person= birthdays_dict[today_tuple]
    file_path= f"./DAY-32/Birthdaywisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content= letter_file.read()
        content=content.replace("[RECEIVER_NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL, to_addrs= birthday_person["email"], msg=f"Subject: Happy Birhtday!\n\n\{content}")
        
        
    
    
    



    
    