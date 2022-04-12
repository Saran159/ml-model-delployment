import json
import requests


url = ' http://127.0.0.1:8000/model'

requests_data = json.dumps({'sinangle':-0.073888547,'cosangle':-0.651025712})

response = requests.post(url,requests_data)

print(response.text)