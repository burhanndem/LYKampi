import json, os, uuid


class Kisi:
    def __init__(self):
        self.numara = ""
        self.isim = ""
        self.soyisim = ""


class Islevler:
    def __init__(self):
        self.dosya = "data.json"
        self.dkontrol()

    def dkontrol(self):
        if not os.path.exists(self.dosya):
            with open("data.json", "w") as f:
                json.dump({}, f)

    def ekle(self, user):
        with open("data.json") as r:
            data = json.load(r)

        data.update({
            str(uuid.uuid1()): {
                "numara": user.numara,
                "isim": user.isim,
                "soyisim": user.soyisim
            }
        })

        with open("data.json", "w") as w:
            json.dump(data, w)

    def sil(self):
        pass

    def guncelle(self):
        pass

    def goruntule(self):
        pass
