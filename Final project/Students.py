from Account import Account
from ParsingTest import Parse


class students(Account):
    def __init__(self, ID):
        parse = Parse()
        info = parse.read_file(ID)

        if info != 'student not found':
            first = info[0]
            last = info[1]
            address = info[2]
            DoB = info[3]
            self.department = info[4]
            email = info[5]
            ID = info[6]
            password = info[7]

            Account.__init__(self, first, last, address, DoB, email, password, ID)

        else:
            print(info)



    def department_get(self):
        return self.department


