# 100705779, 100702991, 100703659
# Kevin Nguyen, Mark Bermah , Matthew Martin

class Account:

    def __init__(self, firstname, lastname, address, DoB, email, password, ID):
        self.f_name = firstname
        self.l_name = lastname
        self.DoB = DoB
        self.address = address
        self.email = email
        self.password = password
        self.ID = ID

    def get_Fname(self):
        return self.f_name

    def get_Lname(self):
        return self.l_name

    def get_DoB(self):
        return self.DoB

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def password_set(self, password_old, password_new):
        if password_old == self.password:
            self.password = password_new
        else:
            print("Incorrect password \nPlease try again")
            input('\npress ENTER to continue')

    def password_get(self):
        return self.Password

    def verify(self, password):
        if password == self.password:
            return True

        else:
            return False

    def ID_get(self):
        return self.ID
