import requests
from reqres import Kisi, Methods


class Console:

    def __init__(self):
        self.choice = ""

    def menu(self):
        choices_list = ["1", "2", "3", "4","5"]
        print("Menüye hoşgeldiniz!")
        while True:
            print("""
            İşlemler

            1.Ekle
            2.Görüntüle
            3.Sil
            4.Güncelle
            5.List all\n""")
            self.choice = input("Seçiminiz: ")
            if self.choice in choices_list:
                break
            print("Yanlış bir seçim numarası girdiniz!!!")

    def secim(self):
        usser = Methods()
        if self.choice == "1":
            usser.ekle(self.get_user())
        elif self.choice == "2":
            usser.goruntule()
        elif self.choice == "3":
            usser.silme()
        elif self.choice == "4":
            usser.guncelle(self.get_user())
        elif self.choice == "5":
            usser.listele()

    def run(self):
        self.menu()
        self.secim()

    @staticmethod
    def get_user():
        ornk = Kisi()
        ornk.name = input("isim: ")
        ornk.surname = input("soyisim: ")
        return ornk


if __name__ == '__main__':
    c = Console()
    c.run()
