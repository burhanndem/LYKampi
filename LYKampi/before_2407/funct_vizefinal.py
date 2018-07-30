ogrenciler = {}


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
                ogrenci_goruntule()
            elif secenek == 4:
                ogrenci_reset()
            elif secenek == 5:
                break
            else:
                print("bilinmeyen bir komut girdiniz")


def ogrenci_ekle():

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
        ogr_vize = input("Vize notunu giriniz")
        ogr_final = input("Final notunu giriniz")
        ogrenciler.update({ogr_no: {'vize': ogr_vize,
                                    'final': ogr_final}
                           })
        break


def ogrenci_sil():
    silinecek_ogr_no = input("lütfen silinecek ogr no giriniz")
    if silinecek_ogr_no in ogrenciler.keys():
        ogrenciler.pop(silinecek_ogr_no)
        print("{} numaralı öğrenci silinmiştir.".format(silinecek_ogr_no))
    else:
        print("{} numaralı öğrenci bulunamadı".format(silinecek_ogr_no))


def ogrenci_goruntule():
    for ogr_no, ogr_notlari in ogrenciler.items():
        print("""ogrenci no: {}
            ogrenci vize: {}
            ogrenci final: {}""".format(ogr_no,
                                        ogr_notlari.get('vize'),
                                        ogr_notlari.get('final')))
    if len(ogrenciler.keys()) == 0:
        print("Listede öğrenci bulunmuyor")


def ogrenci_reset():
    ogrenciler.clear()
    print("öğrenci listesi basarıyla temizlendi")


main()