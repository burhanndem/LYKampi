from hw import Kisi, Islevler
import json, os, uuid

class Console:

    def __init__(self):
        self.secimi=""
        self.secim_list=["1","2","3","4","5"]

    def menu(self):
        print("   Rehber'e hoşgeldiniz!!!")
        while True:
            print("""
            Yapılabilecekler:
            
            1.Kişi ekleme
            2.Kişi silme
            3.Kişi güncelle
            4.Kişi görüntüle
            5.Çıkış""")
            self.secimi = input("   Seçiminiz: ")
            if self.secimi in self.secim_list:
                break
            else:
                print("Yanlış girdi")



    def secim(self):
        try:
            if self.secimi=="1":
                user=Islevler()
                user.isim=input(" numara : ")
                user.numara = input(" isim : ")
                user.soyisim = input(" soyisim : ")
                Islevler.ekle(user,user)

            elif self.secimi=="2":
                pass
            elif self.secimi=="3":
                pass
            elif self.secimi=="4":
                pass
            elif self.secimi=="5":
                pass
        except ValueError:
            return "Hata"




    def calistir(self):

        self.menu()
        self.secim()










if __name__ == '__main__':
    n=Console()
    n.calistir()