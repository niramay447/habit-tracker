import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "niramay"
TOKEN = "add_token_here"
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
    "id": "graph123",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}
response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)

# response = requests.post(url=PIXELA_END_POINT, json=user_params)
print(response.text)