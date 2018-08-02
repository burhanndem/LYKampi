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

        resp2 = requests.post(self.path, data={"name": user.name,
                                               "surname": user.surname})

        if resp2.status_code == HTTPStatus.CREATED:
            pprint(resp2)
            pprint(resp2.json())
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

        resp3 = requests.delete(f"{self.path}/2")
        if resp3.status_code == HTTPStatus.NO_CONTENT:
            pprint(resp3)
            return "basarili"
        return json.dumps({"hata": "istek hatali"})

    def guncelle(self, user):
        resp4 = requests.put(f"{self.path}/2", data={"name": user.name,
                                                     "surname": user.surname})
        pprint(resp4)
        pprint(resp4.json())

