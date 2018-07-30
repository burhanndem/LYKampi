# öğrenci kayıt
# öğrenci silme
# öğrenci görüntüleme
# ogrencilerin tümünü temizleme
# bunların hepsini dosyaya yapıcak


ogrenciler={

}

def menu():
    secenek = input("""
    1-Öğrenci ekle
    2-Öğrenci sil
    3-Öğrenci görüntüle
    4-Öğrencileri toplu şekilde sil
    5-Çıkış
    """)
    return secenek

def main():
    while True:
        try:
            secenek = int(menu())
        except ValueError:
            print("Lütfen sayı giriniz.")
        else:
            if secenek == 1:
                ogrenci_ekle()
            elif secenek == 2:
                ogrenci_sil()
            elif secenek == 3:
                ogrenci_gor()
            elif secenek == 4:
                ogrenci_reset()
            elif secenek == 5:
                break
            else:
                print("bilinmeyen bir komut girdiniz")


def ogrenci_ekle():

        try:
            dosya=open('ogrenciler.txt','a+')
        except Exception:
            dosya=open('ogrenciler.txt','x')
        else:
            tmp_sayac=0
            while True:
                ogr_no = input("Ogrencinin numarasini giriniz.")
                tmp_sayac += 1
                if tmp_sayac == 4:
                    print("Deneme hakkınızı doldurdunuz.")
                    break
                if len(ogr_no) != 9:
                    print("Ogrenci numarasi 9 haneli olmalidir")
                    continue
                ogrvize = input("Vize notunu giriniz")
                ogrfinal = input("Final notunu giriniz")
                ogrenciler.update({ogr_no: {'vize': ogrvize,
                                            'final': ogrfinal}
                                   })

                break



            dosya = open("ogrenciler.txt", "a+")
            dosya.write(str(ogrenciler))
            dosya.close()


def ogrenci_sil():
    pass

metin=""
metin.split()
def ogrenci_gor():
    pass


def ogrenci_reset():
    ogrenciler.clear()
    print("öğrenci listesi basarıyla temizlendi")


main()

