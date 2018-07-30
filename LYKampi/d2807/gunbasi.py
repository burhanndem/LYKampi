# INHERITANCE

class Canli:
    def __init__(self, enerji):
        self.enerji = enerji


class Hayvan(Canli):
    def __init__(self, enerji, tur):
        self.tur = tur
        super(Hayvan, self).__init__(enerji)

    def yemek_yer(self):
        return "besin tüketiyor"

    def iletisim(self):
        print("T_T")


class Kopek(Hayvan):

    def __init__(self, enerji, isim, tur):
        super(Kopek, self).__init__(tur, enerji)
        self.isim = isim

    def iletisim(self):
        print('Aouu,hav,hav')

    def __str__(self):
        print(self.__dict__)
        return self.isim        #str methodu string dönmeli o yüzden return ile ismi döndürüyorum

    def yemek_yer(self):
        return super(Kopek, self).yemek_yer(), "et tüketiyor"


class Kedi(Hayvan):
    def __init__(self, enerji, isim, tur):
        super(Kedi, self).__init__(tur, enerji)
        self.isim = isim

    def iletisim(self):
        print('Miyavv')


def sescikarma(hayvanTuru):  # polymorphism
    hayvanTuru.iletisim()


canli = Canli(100)
print(canli.enerji)
hayvan = Hayvan(75, "memeli")
print(hayvan.enerji, hayvan.tur)
koppek = Kopek(200, "fiko", "memelii")
print(koppek.isim, koppek.enerji, koppek.tur)
print("objenin ismi: " + koppek.__dict__.get('isim') + "\n")

print(hayvan.yemek_yer())
print(koppek.yemek_yer())

print(koppek)

keddi = Kedi(120, "pia", "memeli")

sescikarma(keddi)  # polymorphism
sescikarma(koppek)
