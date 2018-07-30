# dogum gününe kac gun kaldı
class Zaman:
    """
    params:gun,ay,yil

    """
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    #     self.birthday=birthday
    #     self.birthmonth = birthmonth
    #     self.birthyear = birthyear
    #
    # def yearsold(self):
    #     return "Yaşınız:"+str(int(((self.year-self.birthyear)*365+(abs(self.month-self.birthmonth))*30+(abs(self.day-self.birthday)))/365))

    def __sub__(self, other):
        return (self.year - other.year)

    def tillbday(self, now_time):
        if now_time.year < self.year:
            return "Doğum yılı, güncel yıldan küçük olmalı!!"
        elif now_time.year > self.year:
            if 1 <= now_time.month <= 12 and 1 <= self.month <= 12:
                if 1 <= now_time.day <= 30 and 1 <= self.day <= 30:
                    if now_time.month < self.month:
                        return "Doğumgününüze" + " " + str(
                            (self.month - now_time.month) * 30 + (abs(self.day - now_time.day))) + " " + "gün kalmış."
                    elif now_time.month > self.month:
                        return "Doğumgününüze" + " " + str(((12 - now_time.month) * 30) + ((self.month) * 30)+self.day)+ " " + " gün kalmış."
                else:
                    return "1-30 arasında bir gün giriniz !!"
            else:
                return "1-12 arasında bir ay giriniz!!"


if __name__ == '__main__':
    # burhan = Zaman(28, 7, 2018, 21, 12, 1994)

    now_time = Zaman(28, 7, 2018)
    user_birthday = Zaman(21, 6, 1994)
    yas = now_time - user_birthday
    print(yas)
    sonraki=user_birthday.tillbday(now_time)
    print(sonraki)


    # now_time_str = input("nowtime gir")
    # user_birthday_str = input("ub gir")
    # now_time = Zaman(now_time_str)
    # user_birthday = Zaman(user_birthday_str)
    # yas = now_time - user_birthday
    # print(yas)
    # next = user_birthday.tillbday(now_time)

    # print(burhan.yearsold())
    # print(burhan.tillbday())
