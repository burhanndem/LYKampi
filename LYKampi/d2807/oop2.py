print(2+6)
print(2*5)

print(type(2))

class Sayi:
    def __init__(self,deger):
        self.deger=deger
    def __add__(self, other):
        return self.deger+other.deger

class Iki(Sayi):
    pass
class Alti(Sayi):
    pass

print(Alti(6).deger+Iki(2).deger)

print(Alti(6)+Iki(3))