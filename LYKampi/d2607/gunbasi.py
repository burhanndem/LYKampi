birler = {'0': '', '1': 'bir', '2': 'iki', '3': 'üç', '4': 'dört', '5': 'beş', '6': 'altı', '7': 'yedi', '8': 'sekiz',
          '9': 'dokuz'}
onlar = {'0': '', '1': 'on', '2': 'yirmi', '3': 'otuz', '4': 'kırk', '5': 'elli', '6': 'altmış', '7': 'yetmiş',
         '8': 'seksen', '9': 'doksan'}
num = int(input("yazdirmak istediğiniz sayi: "))


def numtotext():
    if len(str(num)) == 1:
        digit1 = num
        return digit1
    elif len(str(num)) == 2:
        digit2 = int(num / 10)
        digit1 = int(num % 10)
        return digit2, digit1
    elif len(str(num)) == 3:
        digit3 = (int(num / 100)) % 100
        digit2 = (int(num / 10)) % 10
        digit1 = int(num % 10)
        return digit3, digit2, digit1
    elif len(str(num)) == 4:
        digit4 = (int(num / 1000)) % 1000
        digit3 = str((int(num / 100)) % 1000)
        digit2 = str((int(num / 10)) % 100)
        digit1 = (int(num % 10)) % 10
        return digit4, digit3[1], digit2[1], digit1


def text():
    sayi = numtotext()
    if len(str(num)) == 1:
        print(birler.get(str(sayi)))
    elif len(str(num)) == 2:
        print(onlar.get(str(sayi[0])), birler.get(str(sayi[1])))
    elif len(str(num)) == 3:
        print(birler.get(str(sayi[0])), "yüz", onlar.get(str(sayi[1])), birler.get(str(sayi[2])))
    elif len(str(num)) == 4:
        print(birler.get(str(sayi[0])), "bin", birler.get(str(sayi[1])), "yüz", onlar.get(str(sayi[2])),
              birler.get(str(sayi[3])))


text()

sayi = input("sayi giriniz")
sayi = sayi[::3]  # her 3ncü eleman
sayi = sayi[::-1]  # tersten
print(sayi)

birler = [None, "bir", "iki", "üç"]

onlar = [None, "on", "yirmi", "otuz"]

sayi = "1111"
sayi = sayi[::-1]

kounus = []
kounus.append(birler[int(sayi[0])])

if len(sayi) >= 2:
    kounus.append(onlar[int(sayi[1])])
if len(sayi) >= 3:
    if sayi[2] == '1':
        kounus.append("yüz")
    else:
        kounus.append(birler[int(sayi[2])] + "yüz")

if len(sayi) >= 4:
    kounus.append((birler[int(sayi[3])]) + "bin")

print(kounus)
print(" ".join(kounus[::-1]))

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):  # enumerate usage
    print(c, value)
