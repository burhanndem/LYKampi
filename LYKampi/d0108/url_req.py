import requests, json
from pprint import pprint

r = requests.get("https://reqres.in/api/users", data={"name": "serhat", "job": "developer"})

js=json.loads(r)
