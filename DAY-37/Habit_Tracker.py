import requests
from datetime import datetime

USER_NAME= "naolumer"
TOKEN= "ajsd35jfdf3esfjr5"
pixela_endpoint= "https://pixe.la/v1/users"

GRAPH_ID= "graph1"

user_params= {"token": TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"}

graph_config= {"id":"graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"}

today= datetime.now()

headers= {"X-USER-TOKEN": TOKEN}
dayy= today.strftime("%Y%m%d")



response= requests.post(url=pixela_endpoint, json=user_params,headers= headers)
print(response.text)
graph_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs"

pixel_data= {"date":today.strftime("%Y%m%d"),
                    "quantity":input("How many kilometers did you cycle today?  ")}
response= requests.post(url=graph_endpoint, json= graph_config,headers= headers)
print(response.text)

post_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
response= requests.post(url=post_endpoint, json=pixel_data, headers=headers)


# put/update
# put_params= {"quantity":"8.4"}
# put_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{dayy}"
# response= requests.put(url=put_endpoint, json=put_params, headers=headers)


# # delete
# delete_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{dayy}"
# response= requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
