import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

resp=requests.get("https://sezerbozkir.com")



soup =  BeautifulSoup(resp.text,'html.parser')

k=soup.find_all("header")

liste=[]

for k in soup.find_all("header"):
    a3=k.find("h1").string
    liste.append(a3)

pprint(liste)






