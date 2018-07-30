ogrenciler = {
    '125153115': {'vize': 80, "final": 90},
    '125468486': {'vize': 60, "final": 100}

}

print("hosgeldiniz")
while True:
    secim = input("""
        1)öğrenci ekle (e)
        2)öğrenci sil (s)
        3)öğrencileri görüntüle (g)
        4)öğrencilerin tümünü sil (d)
        5)çıkış (c)\n""").lower()
    if secim == 'e':
        tmp_sayac = 0
        while True:
            ogr_no = input("ogrencinin numarasını girin")
            if tmp_sayac == 3:
                tmp_sayac += 1
                print("deneme hakkını doldurdunuz")
            if len(ogr_no) == 9:
                ogr_vize = input("ogrencinin vize notunu girin")
                ogr_final = input("ogrencinin final notunu girin")
                ogrenciler.update({ogr_no: {'vize': ogr_vize, 'final': ogr_final}})
                break
            else:
                print("ogrenci numarası 9 haneli olmalı")
                # if tmp_sayac == 3:
                #     tmp_sayac += 1
                #     print("deneme hakkını doldurdunuz")
                break
    elif secim == 's':
        silinecek_ogr_no = input("lütfen silinecek ogr no giriniz")
        if silinecek_ogr_no in ogrenciler.keys():
            ogrenciler.pop(silinecek_ogr_no)
            print("{} numaralı öğrenci silinmiştir.".format(silinecek_ogr_no))
        else:
            print("{} numaralı öğrenci bulunamadı".format(silinecek_ogr_no))

    elif secim == 'g':
        # print(ogrenciler)
        # for ogr_num  in ogrenciler:
        #     print("""ogrenci no: {}
        #     ogrenci vize: {}
        #     ogrenci final: {}""".format(ogr_num,
        #                                 ogrenciler[ogr_num].get('vize'),
        #                                 ogrenciler[ogr_num].get('final')))
        for ogr_no, ogr_notlari in ogrenciler.items():
            print("""ogrenci no: {}
                ogrenci vize: {}
                ogrenci final: {}""".format(ogr_no,
                                            ogr_notlari.get('vize'),
                                            ogr_notlari.get('final')))
        if len(ogrenciler.keys()) == 0:
            print("Listede öğrenci bulunmuyor")

    elif secim == 'd':
        ogrenciler.clear()
        print("öğrenci listesi basarıyla temizlendi")
    elif secim == 'c':
        break
    else:
        print("bilinmeyen bir komut girdiniz")
