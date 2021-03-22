import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "niramay"
TOKEN = "add_token_here"
GRAPH_ID = "graph123"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}


graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}
response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)

#  response = requests.post(url=PIXELA_END_POINT, json=user_params)
# print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20210322",
    "quantity": "9.74",
}

response = requests.post(url= pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)