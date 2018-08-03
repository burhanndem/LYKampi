import requests, json
from http import HTTPStatus
from pprint import pprint


class Kisi:

    def __init__(self):
        self.name = ""
        self.surname = ""


class Methods:

    def __init__(self):
        self.path = "https://reqres.in/api/users"

    def ekle(self, user):

        resp = requests.post(self.path, data={"name": user.name,
                                               "surname": user.surname})

        if resp.status_code == HTTPStatus.CREATED:
            pprint(resp)
            pprint(resp.json())
        return {"hata":"hata mesaji"}

    def goruntule(self):

        resp = requests.get(f"{self.path}?page=2")
        if resp.status_code == HTTPStatus.OK:
            data = resp.json()
            pprint(resp)

            for serhat in data["data"]:
                for key, value in serhat.items():
                    print(key, value)
        return {"hata": "hata mesaji"}

    def silme(self):

        resp = requests.delete(f"{self.path}/2")
        if resp.status_code == HTTPStatus.NO_CONTENT:
            pprint(resp)
            return "basarili"
        return json.dumps({"hata": "istek hatali"})

    def guncelle(self, user):
        resp = requests.put(f"{self.path}/2", data={"name": user.name,
                                                     "surname": user.surname})
        pprint(resp)
        pprint(resp.json())

    def listele(self):
        resp=requests.get(self.path,params={"page":"1"})
        olcek=resp.json().get("total_pages")

        liste = []
        for k in range(2,olcek,1):
            resp=requests.get(self.path,params={"page":k})
            resp.json().get("data")
            liste.append(resp.json().get("data"))

        pprint(liste)







