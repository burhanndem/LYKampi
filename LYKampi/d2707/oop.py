class Ogrenci(object):

    def __init__(self, isim, soyisim, numara, vize, final,):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.vize = vize
        self.final = final

    def ortalama_hesap(self):
        return self.vize * 0.4 + self.final * 0.6

    def __str__(self):
        return " Ogrenci ismi: "+self.isim+" soyismi:"+ self.soyisim+" ve " +self.numara+ \
               " numarali öğrencinin vizesi "+self.vize+ "finali"+self.final+\
               " ve ortalaması: "+self.ortalama_hesap+"dir"

class Sinif:
    ogrenciler = []
    def ogrenci_ekle(self):
        try:
            isim = input("ogrencinin ismi: ")
            soyisim = input("ogrencinin soyyismi: ")
            numarasi = int(input("numarasi: "))
            vize = int(input("vizesi: "))
            final = int(input("finali: "))

            self.ogrenciler.append(Ogrenci(isim, soyisim,
                                           numarasi,
                                           vize=vize,
                                           final=final))
            return True
        except Exception as a:
            print(a)
            return False
    def showstudlist(self):
        for ogrenciler in self.ogrenciler:
            ogrenciler.show()
    def ogrenci_sil(self):
        ogrenci_no=input("ogrenci numarasi :")
        self.ogrenciler=list(filter(lambda x: x.numara==ogrenci_no,self.ogrenciler))
    def snfort(self):
        from functools import reduce
        ortalama = reduce(lambda x,y: x.ortalama_hesap()+y.ortalama_hesap(),self.ogrenciler/len(self.ogrenciler))
        return ortalama

    def dosyaya_yazdir(self):
        with open("ogrenciler.txt","w+") as f:
            for ogrenci in self.ogrenciler:
                f.write(f"{ogrenci.numara},{ogrenci.isim},{ogrenci.soyisim},{str(ogrenci.vize)},{str(ogrenci.final)}")
                print(ogrenci,file=f)


if __name__ == '__main__':
    python_1b = Sinif()
    while True:
        secenek = int(input("""
        1-Öğrenci ekle
        2-Öğrenci sil
        3-Öğrenci görüntüle
        4-sınıf ortalaması göster
        5-Çıkış
        6-dosyaya kaydet
        """))
        if secenek == 1:
            python_1b.ogrenci_ekle()
        elif secenek == 3:
            python_1b.showstudlist()
        elif secenek == 2:
            python_1b.ogrenci_sil()
        elif secenek == 4:
            python_1b.snfort()
        elif secenek == 5:
            break
        elif secenek == 6:
            python_1b.dosyaya_yazdir()
        else:
            print("bilinmeyen bir komut girdiniz")