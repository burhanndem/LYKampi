#dogum gününe kac gun kaldı
class Zaman:
    """
    params:gun,ay,yil
    """
    def __init__(self,day,month,year,birthday,birthmonth,birthyear):
        self.day = day
        self.month = month
        self.year = year
        self.birthday=birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear

    def yearsold(self):
        return "Yaşınız:"+str(int(((self.year-self.birthyear)*365+(abs(self.month-self.birthmonth))*30+(abs(self.day-self.birthday)))/365))

    def tillbday(self):
        if self.year < self.birthyear:
            print("Doğum yılı, güncel yıldan küçük olmalı!!")
        elif self.year > self.birthyear:
            if 1<=self.month<=12 and 1<=self.birthmonth<=12:
                if 1<=self.day<=30 and 1<=self.birthday<=30:
                    if self.month < self.birthmonth:
                        return "Doğumgününüze"+" "+str((self.birthmonth-self.month)*30+(abs(self.birthday-self.day)))+" "+"gün kalmış."
                    elif self.birthmonth < self.month:
                        return  "Doğumgününüze"+" "+str(((12-self.month)*30)+((self.birthmonth)*30))+str(abs(self.birthday))+" "+" gün kalmış."
                else:
                    return "1-30 arasında bir gün giriniz !!"
            else:
                return "1-12 arasında bir ay giriniz!!"





burhan=Zaman(28,7,2018,21,12,1994)
print(burhan.yearsold())
print(burhan.tillbday())
