import json
import os
from pprint import pprint


class Kisiler:


    def __init__(self, numara, isim, soyisim, database="rehber.json"):
        self.isim = isim
        self.numara = numara
        self.soyisim = soyisim
        self.database=database
        self.kisiler=[]
        self.se
        # if os.path.exists(database):
        #     with open(database, "r") as f


    def kisi_ekle(self):
        self.kisiler.append(self.numara+","+
            self.isim+","+
            self.soyisim)

        if not os.path.exists(self.database):
            with open(self.database, "w") as f:
                pass
        with open(self.database, "a") as w:
            json.dump(self.sep,w)
            json.dump(self.kisiler, w)

    def kisi_silme(self):
        with open(self.database, "r") as r:
            data = json.load(r)
            data2 = data.pop(self.kisiler)
        with open(self.database, "w") as w:
            json.dump(data2, w)

    def kisi_guncelleme(self):
        pass

    def arama(self):
        pass


if __name__ == '__main__':
    ornk = Kisiler("123345", "hebe5", "hub5e")
    ornk2 = Kisiler("54987964", "fdhdfh", "sdgig")
    try:
        while True:
            choice = int(input("""
            1-kayit
            2-silme
            3-guncelleme
            4-cikis\n
            seciminiz="""))

            if choice == 1:
                ornk.kisi_ekle()
                ornk2.kisi_ekle()
            elif choice == 2:
                print("halo")
                ornk.kisi_silme()
                # ornk2.kisi_silme()

            elif choice == 3:
                pass
            elif choice == 4:
                break
            else:
                print("Yanlis bir deger girdiniz")

    except ValueError:
        print("Value Error!!")
