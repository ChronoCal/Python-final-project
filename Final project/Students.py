from System import account

class students(account):
    def __init__(self, First, Last, DoB, Address, Email, Department, ID, Password):
        account.__init__(self, First, Last, DoB, Address, Email)
        self.Department = Department
        self.ID = ID
        self.Password = Password

    def Password_Set(self, Password_old, Password_new):
        if Password_old == self.password:
            self.Password = Password_new
        else:
            print("Incorrect password \nPlease try again")

    def ID_Get(self):
        return self.ID

    def Password_Get(self):
        return self.Password

    def Department_Get(self):
        return self.Department
