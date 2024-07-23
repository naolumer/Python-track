import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
header= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

response= requests.get(URL, headers=header)
soup= BeautifulSoup(response.content, "lxml")

price_text= soup.find(class_= "a-offscreen").get_text()

price_wo_sign= price_text.split("$")[1]
price_float= float(price_wo_sign)




title = soup.find(id="productTitle").get_text().strip()


BUY_PRICE = 200
my_email= "example@gmail.com"
my_password= "qwerty1234"

if price_float < BUY_PRICE:
    message = f"{title} is now {price_text}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )