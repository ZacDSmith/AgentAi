
import requests
from flask import jsonify

url = "<API_URL>/items"
data = {"name": "John Doe", "age": 30}
response = requests.post(url, json=jsonify(data))

if response.status_code == 201:
    print("Item created successfully")
else:
    print("Failed to create item")
