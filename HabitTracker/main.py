import requests as rq
import os
from datetime import datetime as dt

token = os.environ['Pixla_Token']
user = os.environ['Pixla_user']

# Getting current date and time
today = dt.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {"token": token, "username": user, "agreeTermsOfService": "yes", "notMinor": "yes"}
# response = rq.post(url=pixela_endpoint, json=parameters)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{user}/graphs"
graph_params = {"id": "walk", "name": "Con TODO si no ¿pa' qué? ", "unit": "minutes", "type": "int",
                "color": "ajisai", "timezone": "America/Santiago", "publishOptionalData": True}
header = {"X-USER-TOKEN": token}
# response = rq.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{user}/graphs/walk"
pixel_params = {"date": today, "quantity": "60"}

response = rq.post(url=pixel_endpoint, json=pixel_params, headers=header)
print(response.text)








# # Delete Graph
# response = rq.delete(url=pixel_endpoint, headers=header)
# print(response.text)
