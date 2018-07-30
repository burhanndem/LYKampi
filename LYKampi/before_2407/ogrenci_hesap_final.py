# seçtirecek : öğrenci eklemek çıkarma ve görmek

# pseudo
# kullanıcı ne yapmak istiyor sor whilela
# öğrenci eklemek istiyorsa sözlüğe öğrenci ismi vize finalini alacak ekliyecek
# tekrar ana menüye dönecek
#
# ana menü:   1 öğrenci ekle
#             2 öğrenci sil
#             3 öğrencileri görüntüle
#             4 çıkış
# öğrenci silmek için var mı baktır varsa sil yoksa bulunamadı yazdır
#
# öğrencileri görüntülemek için öğrenci listesini ekrana bas


print("""Öğrenci kayıt sistemine hoşgeldiniz !
      
      Yapabilecekleriniz:
      
      1.Öğrenci ekleme
      2.Öğrenci silme
      3.Öğrencileri görüntüleme
      4.Çıkış""")

ogrenci = {}

islem_no = int(input("\nYapmak istediğiniz işlemin numarası : "))

if islem_no == 1:
    print("\nEklemeyi seçtiniz\n")
    ogrenci_numarasi = int(input("Kaydetmek istediğiniz öğrencinin numarası nedir?"))
    vize_notu = int(input("Öğrencinin vize notu kaçtır?"))
    final_notu = int(input("Öğrencinin final notu kaçtır? "))
    ogrenci.update({'ogrenci_numarasi': ogrenci_numarasi,
                    'vize_notu': vize_notu,
                    'final notu': final_notu})
    print("\n", ogrenci_numarasi, "numarali", vize_notu, "vize ve", final_notu,
          " final notları olan öğrenciyi kaydettiniz.")

elif islem_no == 2:
    print("\nSilmeyi seçtiniz\n")
    ogrenci_sil = input("Silmek istediğiniz öğrenin numarası kaçtır?\n")
    ogrenci_sil.remove(ogrenci)
    print(ogrenci_sil, "numaralı öğrencinin kaydını sildiniz.")
