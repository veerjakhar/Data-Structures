class user:
    # Hidden Variable
    __password = "1croissantdw"
    dob = "MM/DD/YY"
    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username

    def get_password(self):
        return self.__password

    def set_password(self):
        old_pass = input("Enter Your Old Password")
        if old_pass == self.__password:
            new_pass = input("Please Enter The New Password")
            self.__password = new_pass
        else:
            print("The Password Is Incorrect")
            emi = input("Enter Your Email")
            if emi == self.email:
                newemi = input("Please Enter The New Password")
                self.__password = newemi
                if self.__password == old_pass:
                    print("This was you previous password")

numone = user("Croissant", "1eggysant@gmail.com", "Reev_Rahkaj2")
print(numone.name)
print(numone.email)
print(numone.username)
print(numone.get_password())
print(numone.dob)
numone.set_password()
print(numone.get_password())


