varsayilan_not={"vize":0, "final":0}

ogrenciler={
    'sezer bozkir':{ 'vize':80, "final":90},
    'fatmanur bilke':{ 'vize':60, "final":100}

}

if ogrenciler.get('enes şahin')== None:
    ogrenciler.update({'enes şahin': varsayilan_not,
                       'mustafa ersoy': varsayilan_not})

# #yaşar celep
# print(ogrenciler.get('yasar celep',varsayilan_not))
# print(ogrenciler)
# print(ogrenciler.items())

for ogrenci, notu in ogrenciler.items():
    ogrenciler[ogrenci]['vize']=0

# print(ogrenci,notu)





vize_final_notlari={}


for i in range(5):
    ogrenci_ismi = input('ogrenci ismi: ')
    vize_notu = int(input('vize notu'))
    final_notu = int(input('final notu'))
    vize_final_notlari.update({ogrenci_ismi:{'vize':vize_notu, 'final':final_notu}})

print(vize_final_notlari)

