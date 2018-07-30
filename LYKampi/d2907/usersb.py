class User:

    def __init__(self, username, password, name, surname):
        self.username = "@" + username
        self.password = password
        self.name = name
        self.surname = surname




class Process:
    list = []

    def read_list(self):
        okunmus_data = []
        with open("database.txt", "r") as r:
            okunmus_data = r.read()
            return okunmus_data

    def __init__(self, user):
        self.user = user

    def signup(self):
        okunmus_data = self.read_list()
        result = okunmus_data.find(self.user.username)
        if result == 1:
            print("hata")
        else:
            return self.user.username, self.user.password, self.user.name, self.user.surname

    def write_list(self):
        self.list.append(self.user.username + "," + self.user.password + "," + self.user.name + "," + self.user.surname)
        with open("database.txt", "w+") as w:
            for self.user in self.list:
                w.write("{}".format(self.user))

    def show_info(self):
        print("{}".format(self.user))

    def signin(self):
        pass


if __name__ == '__main__':
    ornk = Process(User("burhannde", "ahahah", "Burhan", "Demirtas\n"))
    ornk2 = Process(User("ramazande", "a23423", "Ramazan", "Demirtas\n"))
    ornk3 = Process(User("burhannde", "ahahah", "Burhan", "Demirtas\n"))

    try:
        while True:
            choice = int(input("""
            1-Sign in
            2-Sign up
            3-Exit
            4-Show info\n"""))

            if choice == 1:
                ornk.signin()
                ornk2.signin()

            elif choice == 2:
                ornk.signup()
                ornk2.signup()
                ornk.write_list()
                ornk2.write_list()
                ornk3.signup()
                ornk3.write_list()
            elif choice == 3:
                ornk.show_info()
                ornk2.show_info()
                ornk3.show_info()
            elif choice == 4:
                break
            else:
                print("Yanlis bir deger girdiniz")

    except ValueError:
        print("Value Error!!")