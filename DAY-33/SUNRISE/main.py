import requests
from datetime import datetime

MY_longitude=39.269459
My_latitude=8.541080
parameters= {"lat": My_latitude, "lng": MY_longitude, "formatted":0,}
response= requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data= response.json()



sunrise= int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset= int(data  ["results"]["sunset"].split("T")[1].split(":")[0]) 

print(sunrise)
print(sunset)

time_now= datetime.now()
print(time_now.hour)