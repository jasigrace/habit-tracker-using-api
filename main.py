import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "jasigrace"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "YOUR_ID"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Workout and Step Tracking Graph",
    "unit": "steps",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


new_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
new_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many steps did you complete today? ")
}

response = requests.post(url=new_pixel_endpoint, json=new_pixel_config, headers=headers)
print(response.text)

graph_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_param = {
    "unit": "steps",
    "color": "shibafu"
}

# response = requests.put(url=graph_update_endpoint, json=update_param, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{graph_update_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
