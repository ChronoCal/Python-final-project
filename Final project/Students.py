from Account import account


class students(account):
    def __init__(self, first, last, DoB, address, email, department, ID, password):
        account.__init__(self, first, last, DoB, address, email, password, ID)
        self.Department = department

    def department_get(self):
        return self.department
