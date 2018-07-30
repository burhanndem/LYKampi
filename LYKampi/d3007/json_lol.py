import json
from pprint import pprint

busers = {
    "burhannde": {
        "isim": "Burhan",
        "soyisim": "Demirtas",
        "eposta": "burhanndemirtas@gmail.com",
        "parola": "12345"
    },
    "edayildiz": {
        "isim": "Eda",
        "soyisim": "Yildiz",
        "eposta": "123@123.com",
        "parola": "321654"
    }
}
# pprint(busers)
# ornk=json.dumps(busers)
# pprint(ornk)

with open("database.json", "w") as f:
    json.dump(busers, f)
with open("database.json","r") as r:
    data=json.load(r)
    pprint(data)
    print(data['burhannde'])

