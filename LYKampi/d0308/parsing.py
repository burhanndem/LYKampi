import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

resp=requests.get("https://projecteuler.net/archives")
pprint(resp.status_code)
soup =  BeautifulSoup(resp.text,'html.parser')

liste=[]

for row in soup.find_all("tr"):
    k= row.find_all("td")
    if  k != []:
        n={
            "no":k[0].string,
            "name":k[1].string,
            "solved times":k[2].string
        }
        liste.append(n)

with open("islenmis.json","w") as f:
    json.dump(liste,f)
    pprint("json'a yazildi")

