# from math import pow
#

a = lambda num1, num2: pow(num1, num2)
b = lambda deger: deger % 3 == 0

# print(a(3, 2))
#

bir_dizi_var = [5, 10, 2, 18, 21, 55]

#
# string_deger=[]
# for deger in bir_dizi_var:
#     string_deger.append(str(deger))
#
# print((bir_dizi_var, string_deger),sep="\n")
# bir_dizi_var=[]
#
yeni_deger = map(lambda deger: str(deger), bir_dizi_var)
#
#
# print(yeni_deger)
# print(list(yeni_deger))
#
# print((lambda deger: str(deger),bir_dizi_var))

yeni_deger2 = map(b, bir_dizi_var)
# print(yeni_deger)
# print(list(yeni_deger))

ciftler = filter(lambda say: say % 2 == 0, bir_dizi_var)
# print(list(ciftler))

ciftler2 = filter(b, bir_dizi_var)
# print(list(ciftler))

from functools import reduce

print(bir_dizi_var)
toplam = 0
for deger in bir_dizi_var:
    toplam += deger

print(toplam)

resp = reduce((lambda x, y: x + y, bir_dizi_var )
