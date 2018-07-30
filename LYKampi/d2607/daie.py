from math import pi
# print(pi)

def dairenin_cevre_alan(r):
    cevre=2*pi*r
    r2=pow(r,r)
    alan=pi*r2
    print(r,"yarıcaplı dairenin cevresi:",cevre,"ve alanı",alan)


dairenin_cevre_alan(2)