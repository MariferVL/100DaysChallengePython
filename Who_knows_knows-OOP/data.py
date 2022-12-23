import requests
import json

parameters = {
    "amount": 10,
    "difficulty": "medium",
    "type": "boolean",
}


def create_json():
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Serializing json
    json_object = json.dumps(data, indent=4)
    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
        outfile.close()


create_json()

with open("data.json", "r") as file:
    json_file = json.load(file)
    triviaData = json_file["results"]

print(triviaData)

