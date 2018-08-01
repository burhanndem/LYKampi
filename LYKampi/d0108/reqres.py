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
        data=resp.json()
        pprint(resp)

        for serhat in data["data"]:
            for key, value in serhat.items():
                print(key,value)




    def silme(self):

        resp3=requests.delete(f"{self.path}/2")
        pprint(resp3)


    def guncelle(self,user):
        resp4 = requests.put(f"{self.path}/2", data={"name": user.name,
                                               "surname": user.surname})
        pprint(resp4)
        pprint(resp4.json())


# {'data': [{'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg',
#            'first_name': 'Eve',
#            'id': 4,
#            'last_name': 'Holt'},
#           {'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/stephenmoon/128.jpg',
#            'first_name': 'Charles',
#            'id': 5,
#            'last_name': 'Morris'},
#           {'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/bigmancho/128.jpg',
#            'first_name': 'Tracey',
#            'id': 6,
#            'last_name': 'Ramos'}],
#  'page': 2,
#  'per_page': 3,
#  'total': 12,
#  'total_pages': 4}