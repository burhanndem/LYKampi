class Motorsiklet(object):
    lastik = 2
    parcalar = ['gidon', 'teker']

    def __init__(self, lastik):
        self.lastik = lastik
        self._lastik=lastik    #protected---
        self.__motor='btwin'    #private----class içinden erişim


sezer_hocanin_chooperi=Motorsiklet(2)
print(sezer_hocanin_chooperi._lastik)
print(sezer_hocanin_chooperi.__motor)
print(sezer_hocanin_chooperi.get_lastik)



# print(Motorsiklet)
#
# motor = Motorsiklet
# print(Motorsiklet)
# print(motor)
# print(motor.lastik)
# print(Motorsiklet().lastik)
