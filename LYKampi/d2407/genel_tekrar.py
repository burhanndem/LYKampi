# liste = ["bir", "birr"]
# sorted(liste)
#
# meyves= {'a','b','a'}
# demet = ('a','b','a')
#
# print(meyves)
# print(demet)
#
#
# print(type(demet))
# print(type(meyves))
#
# liste1=['a','b','a']
# liste2=['c','d','e']
#
# liste1.extend(*liste2)
# print(liste1)


# cumle="hava cok guzel"
#
# cumle=cumle.replace(' ','\t\t')
# print(cumle)

# for loop u tek satırda yazmak


# sayilar = []
# sayilar = [say * say for say in range(1, 10) if say % 2 == 0]
# print(sayilar)


# def args_yazdir(ilki,ikinci,*args):
#     print(args)
#
# args_yazdir(1,2,3,4,5,6)
#
# def args_yazdir(*args,ilki,ikinci):
#     print(args)
#
# args_yazdir(1,2,3,4,5,6)
#
# def args_yazdir(*args,ilki,ikinci):
#     print(args)
#
# args_yazdir(1,2,3,4,ilki=5,ikinci=6)
#
# def kwargs_yazdir(**kwargs):
#     print(kwargs)
#
#
# kwargs_yazdir(bir=10, iki=93)

#
# def kwargs_yazdir(bir=2,**kwargs):
#     print(kwargs)
#     print(bir)
#
#
# kwargs_yazdir(bir=10, iki=93)


# def kwargs_yazdir(ilki,ikinci,*args,bir=2,hasan,**kwargs):
#     print(ilki)
#     print(ikinci)
#     print(args)
#     print(hasan)
#     print(kwargs)
#     print(bir)
#
#
# kwargs_yazdir(9,8,7,8,6,bir=1,hasan=2,test=1,heey=19)

#
# def dosya_ac(dosya_ismi):
#     dosya = open(dosya_ismi, 'r')
#     dosyaverisi=dosya.read()
#     return dosyaverisi
#
#
#
# def dosya_yarat(dosya_isim):
#     dosyayaratma=open(dosya_isim,'w')
#     dosyayaratma.write(dosya_ac(dosya_isim))


# dosya_yarat('lalala3.txt')

def dosya_oku(dosya):
    with open(dosya, "r") as dosya1:
        dosya_okunan = dosya1.read()
        return dosya_okunan


def dosya_yaz(dosya, okunacak_dosya):
    with open(dosya, "w") as dosya2:
        dosya2.write(dosya_oku(okunacak_dosya))


dosya_yaz("yeni_dosya3.txt", "lalala.txt")

# x = 5
#
#
# def fonk(deger):
#     x = 8
#     print(x)
#
#
# fonk(8)
# print(x)

# def dosya_yaz(dosya_ismi,)

#  dosya = dosya_ac('lalala.txt')
#
#
# dosya=open('lalala.txt','r')
#
# print(dosya)
