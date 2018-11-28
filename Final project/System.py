# Student IDs
# names

import Students
import Faculty


class account:

    def __init__(self, Firstname, Lastname, DoB, Address, Email):
        self.f_name = Firstname
        self.l_name = Lastname
        self.DoB = DoB
        self.address = Address
        self.email = Email

    def Get_Name(self):
        return self.f_name + self.l_name

    def Get_DoB(self):
        return self.DoB

    def Get_Address(self):
        return self.address

    def Get_Email(self):
        return self.address

