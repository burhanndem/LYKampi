ogrenciler={}

with open("ogrencilerim",'r') as f:
    for ogr_no,notlar in ogrenciler.items():
        f.write("{} {} {}\n".format(ogr_no,
                                   notlar.get('vize'),
                                   notlar.get('final')))
veri_tabani={}
with open('ogrencilerim','r') as f:
    okunan_ogrenciler=f.readlines()
    print(okunan_ogrenciler)
    for satir in okunan_ogrenciler:
        ogrenci=satir.strip().split(' ')
        veri_tabani.update({ogr_no: {'vize': notlar.get('vize'),
                                     'final': notlar.get('final')}})


open