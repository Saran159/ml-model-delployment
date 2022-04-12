import json
import requests


url = ' http://127.0.0.1:8000/model'

requests_data = json.dumps({'model':'knn'})

response = requests.post(url,requests_data)

print(response.text)