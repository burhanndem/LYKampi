from crud import User, DBMethods

from pprint import pprint
import os, sys


class ConsoleProgram:

    def __init__(self):
        self.main_choice = ""
        self.choices_list = ["1", "2", "3", "4"]

    def Main_Page(self):
        print("\nHoşgeldiniz...\n")
        while True:
            print("1.Kayıtları göster")
            print("2.Ekle")
            print("3.Güncelle")
            print("4.Sil\n")
            print("Seçiminiz:")
            self.main_choice = input()
            if self.main_choice in self.choices_list:
                break
            ConsoleProgram.clear_screen()
            print("Girdiğiniz değer yanlış!\n")

    def GoTo_choice(self):
        db = DBMethods()
        if self.main_choice == "1":
            pprint(db.get())

        elif self.main_choice == "2":

            db.add(self.Get_User())
            pprint(db.get())

        elif self.main_choice == "3":
            user_id = input("user_id girin: ")
            if db.Check_UserID(user_id):
                db.update(user_id,self.Get_User())
                print("Güncellendi")
            else:
                print("bulunamadı")
            pprint(db.get())


        elif self.main_choice == "4":
            user_id = input("kullanıcı id giriniz:")
            if db.delete(user_id):
                print("kullanıcı silindi")
            else:
                print("kullanıcı bulunamadı")
            pprint(db.get())

    @staticmethod
    def clear_screen():
        os.system("cls" if sys.platform == "nt" else "clear")

    def Run(self):
        self.Main_Page()
        self.GoTo_choice()

    @staticmethod
    def Get_User():
        user = User()
        user.isim = input("isim: ")
        user.soyisim = input("soyisim: ")
        user.numara = input("numara: ")
        return user


if __name__ == '__main__':
    # c = ConsoleProgram()
    # c.Run()
    n = ConsoleProgram()
    n.Run()

    # ConsoleProgram.Run() #eğer run staticmethod sa run çalışır değilse hata verir
