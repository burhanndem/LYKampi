ogrenciler={}


class Ogrenci(object):

    def __init__(self, isim, soyisim, numara, vize, final):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.vize = vize
        self.final = final

    def show(self):
        print(self.isim,self.soyisim,self.numara,self.vize,self.final)


    def ortalama_hesap(self):
        self.ortalama = int(((int(self.vize) * 4) / 10) + ((int(self.final) * 6)) / 10)
        print("ortalama: {}".format(self.ortalama))
        return self.ortalama




studs=Ogrenci('','','','','',)

studs.ogrenci_ekle()
studs.show()

burhan=Ogrenci('burhan','demirtas','151024055','50','60')
burhan.show()
burhan.ortalama_hesap()

burhan.ogrenci_ekle()
burhan.show()

class Sinif:
    def ogrenci_ekle(self):
        isim=input("ismi ne olsun: ")
        soyisim = input("soyismi ne olsun: ")
        self.numara = input("numara ne olsun: ")
        self.vize = input("vize ne olsun: ")
        self.final = input("final ne olsun: ")




studs.ogr