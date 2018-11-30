from Account import Account


class students(Account):
    def __init__(self, first, last, DoB, address, email, department, ID, password):
        Account.__init__(self, first, last, DoB, address, email, password, ID)
        self.Department = department

    def department_get(self):
        return self.department
