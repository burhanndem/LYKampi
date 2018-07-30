import random


def menu():
    secenek = input("""
    1-Oynamaya başla
    2-Toplam puanı gör
    3-Çıkış
    
    Seçiminiz:
    """)
    return secenek


def zarkontrol():
    lucky = random.randint(1, 6)
    print(lucky)
    guess = int(input("Tahmininiz: "))
    if lucky == guess:
        print("Doğru !!!+1 puan kazandınız")
        return True
    else:
        print("Tekrar deneyin :(")
        return False


if __name__ == '__main__':
    points = 0
    while True:
        try:
            secenek = int(menu())
        except ValueError:
            print("Lütfen sayi giriniz")
        else:
            if secenek == 1:
                cevap = zarkontrol()
                if cevap:
                    points += 1
            elif secenek == 2:
                print("{} puanınız var".format(points))
            elif secenek == 3:
                break
            else:
                print("Yanlış giriş!!!")