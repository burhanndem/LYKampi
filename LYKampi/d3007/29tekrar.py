import json
class Kullanici:

    def __init__(self, username, password, email, name, surname, veritabani="database2.json"):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.surname = surname


    @staticmethod
    def varlik_kontrolu(username, veritabani="database2.json"):
        listst = {}
        with open(veritabani, "r") as f:
            str_user = f.readlines()
            listst.extend(x.split(",")[0] for x in str_user)
        cevap = list(filter(lambda x: x == username, listst))
        return bool(len(cevap))

    def show_info(self):
        print(f"Kullanici adi:\t{self.username}\nEmail:\t{self.email}\nİsim:\t{self.name}\nSoyisim:\t{self.surname}")


if __name__ == '__main__':
