try:
    dosya = open('dosya.txt', 'w')
    dosya.write("ekle bakalım")

    icerik = dosya.readlines()


    icerik = [satir.strip() for satir in icerik]

    # temizlenmis_icerik=[]
    # for satir in icerik:
    #     temizlenmis_icerik.append(satir.strip)
    # print(temizlenmis_icerik)
    # dosya.close()

    # print(dosya.read())
    # dosya.close()
    # satirlar=dosya.readlines()
    # dosya.close()
    # print(satirlar)
except Exception:
    print("dosya yoktur")
