import requests
from twilio.rest import Client

auth_token= "3922c6e3cdeb0e1df87875eb91be6bed"
account_sid= "ACf41a9378cd2ae363e05e1c1699a0d775"
api_key= "7426acced97ca16ea8673533a7d3088c"
OWM_path= "https://api.openweathermap.org/data/3.0/onecall"
paramete= {"lat":51.50735, "lon":-0.127758,"appid": api_key, "exclude": "current, minutely, daily"}

response = requests.get(OWM_path, params= paramete)
response.raise_for_status()
weather_data=response.json()
weather_slice= weather_data["hourly"][:12]

will_rain= False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    
    if int(condition_code)<700:
        will_rain= True

if will_rain:
    
    client= Client(account_sid, auth_token)
    messages= client.messages\
    .create(body="It is going to rain today.Remember to bring an umbrella.", from_="+13342316855",to="+251983777202")
        
    print(messages.status)




