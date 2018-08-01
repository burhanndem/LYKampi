import requests, json
from pprint import pprint


class Kisi:

    def __init__(self):
        self.name=""
        self.surname=""


class Methods:

    def __init__(self):
        self.path="https://reqres.in/api/users"

    def ekle(self,user):

        resp2=requests.post(self.path,data={"name":user.name,
                                      "surname":user.surname})
        pprint(resp2)
        pprint(resp2.json())


    def goruntule(self):

        resp=requests.get(f"{self.path}?page=2")

        pprint(resp)
        pprint(resp.json())

    def silme(self):

        resp3=requests.delete(f"{self.path}/2")
        pprint(resp3)


    def guncelle(self,user):
        resp4 = requests.put(f"{self.path}/2", data={"name": user.name,
                                               "surname": user.surname})
        pprint(resp4)
        pprint(resp4.json())
