
from Account import Account
from ParsingTest import Parse


class students(Account):
    def __init__(self, ID):
        parse = Parse()
        info = parse.s_get_info(ID)
        try:
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
                pass
        except TypeError:
            print('Try again')

    def department_get(self):
        return self.department
