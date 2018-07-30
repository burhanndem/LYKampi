class User(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password



class Process():
    Users = []

    def signup(self):
        self.username = input("Olusturmak istediginiz kullanici adi: ")
        self.password = input("Olusacak kullanicinin sifresi: ")

        self.Users.append(User(self.username, self.password))
        with open("Users.txt", "w+") as f:
            for ogrenci in self.Users:
                f.write(f"{self.username},{self.password}")

    def signin(self):
        pass










if __name__ == '__main__':
    burhannde=Process()
    try:
        while True:
            choice = int(input("""
            1-Sign in
            2-Sign up
            3-Exit\n"""))

            if choice == 1:
                burhannde.signin()
            elif choice == 2:
                burhannde.signup()
            elif choice == 3:
                break
            else:
                print("Yanlis bir deger girdiniz")

    except ValueError:
        print("Value Error!!")