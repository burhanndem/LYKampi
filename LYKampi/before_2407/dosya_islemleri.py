# def us_alma(deger_1, deger_2):
#     sonuc = deger_1 ** deger_2
#     print("sonuc: {}".format(sonuc))
#     return sonuc
#
#
# try:
#     deger1 = int(input("lütfen ilk deger"))
#     deger2 = int(input("lütfen ikinci deger"))
#     sonucu = us_alma(deger1, deger2)
# except ValueError as e:
#     print(e)
#     print("lütfen sayi girin")
# except Exception as e:
#     print(e)
#     print("bir hata oldu")
# else:
#     print(sonucu)


# if type(deger1)==int and type(deger_2)==int:
#     sonucu=us_alma(deger_1,deger_2)
#     print(sonucu)
# else:
#     print("lütfen sayi degeri giriniz")
#
# def topla_cikar(say1, say2, topla=True):
#     return say1+say2 if topla else say1-say2
#
# if topla:
#     return say1 + say2
# else:
# return say1 - say2

# sonuc=0
# if topla:
#     sonuc +=say1
# m1 #     sonuc +=say2
#     # sonuc=say1+say2
# else:
#     sonuc=say1-say2
# return sonuc

# deger1=int(input("lütfen ilk deger"))
# deger2=int(input("lütfen ikinci deger"))

# print(range(start=0,stop=10,step=2))




# def yazdirma(*args):
#     yazdirilacak=args[:-2]
#     bitirici=args[-1]
#     ayirici=args[-2]
#     # for kelime in yazdirilacak:
#     #     print(kelime, end='', sep='')
#     #     print(ayirici,end='',sep='')
#     # print(bitirici)
#     print(*yazdirilacak,sep=ayirici,end=bitirici)
#
# yazdirma("ahmet", "mehmet","hey",'#22','bitirdik')

# def args_kwargs_yazdirma(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
#     print(*args, sep=kwargs.get('ayirici'),
#                  end=kwargs.get('bitirici'))
#
#
# args_kwargs_yazdirma("ahmet", "mehmet","hey",ayirici='#34',bitirici='bitirdik')


# def args_kwargs_yazdirma(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
#     print(*args, sep=kwargs.get('ayirici'),
#                  end=kwargs.get('bitirici'))
#
# kwargs={'ayirici':'#',
#         'bitirici':'bitirdik'}
#
# args=["ahmet", "mehmet","hey"]
#
# args_kwargs_yazdirma(*args,**kwargs)
