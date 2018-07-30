#
#   Manav Uygulaması
#
#   1-Ürün ekle
#   2-Ürün sil
#   3-Stok Görüntüler
#
#


def menu():
    secenek=input("""
    1-Ürün ekle
    2-Ürün sil
    3-Stok Görüntüler
    """)
    return secenek

def main():
    try:
        secenek=int(menu())
        secenek/0
    except ValueError:
        print('Harf')
    except ZeroDivisionError:
        print("zero div")

    #print(secenek)
#
# main()
#

def hata_dondur():
    return ValueError("hata")

hata_dondur()
try:
    degiken=hata_dondur()
    print(degiken)
    # hata_dondur()
except:
    print("diğer hata")