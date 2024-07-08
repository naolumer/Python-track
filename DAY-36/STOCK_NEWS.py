import requests
from dotenv import load_dotenv, dotenv_values
import os
from twilio.rest import Client

load_dotenv()

ACC_SID= os.environ.get("ACC_SID")
AUTH_TOKEN=os.environ.get("AUTH_TOKEN")

STOCK_NAME= "TSLA"
COMPANY_NAME= "Tesla Inc"


API_KEY_NEWS= os.environ.get("API_KEY_NEWS")
API_KEY = os.environ.get("API_KEY")

api_path= "https://www.alphavantage.co/query"
parameters= {"function":"TIME_SERIES_DAILY",
            "symbol":STOCK_NAME,
            "outputsize":"compact",
            "apikey": API_KEY}

response= requests.get(api_path, params=parameters)
response.raise_for_status()
data= response.json()["Time Series (Daily)"]

data_list= [value for (key, value) in data.items()]

yesterday= data_list[0]
yesterday_stock= yesterday["4. close"]

day_before_yesterday= data_list[1]
day_before_yesterday_stock=day_before_yesterday["4. close"]

difference= (float(yesterday_stock)-float(day_before_yesterday_stock))

percentage_difference= (difference/float(yesterday_stock)) * 100

if percentage_difference>0.5:
    
    NEWS_ENDPOINT = ("https://newsapi.org/v2/everything")
    news_params= {"apikey": API_KEY_NEWS,"qIntitle":COMPANY_NAME}

    response_news= requests.get(NEWS_ENDPOINT, news_params)
    response_news.raise_for_status()
    articles=response_news.json()["articles"]
    three_articles= articles[:3]

    formatted_articles= [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client= Client(ACC_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message= client.messages.create(body= article, from_=+13342316855, to= +251983777202)



