# 100705779, 100702991, 100703659
# Kevin Nguyen, Mark Bermah , Matthew Martin

from Account import Account
from ParsingTest import Parse

class Faculty(Account):
    def __init__(self, ID):
        parse = Parse()
        info = parse.f_get_info(ID)

        try:
            if info != 'staff not found':
                first = info[0]
                last = info[1]
                ID = info[2]
                address = info[3]
                DoB = info[4]
                email = info[5]
                password = info[6]

                Account.__init__(self, first, last, address, DoB, email, password, ID)

            else:
                pass
        except TypeError:
            print('Login Failed')
            input('\npress ENTER to continue')

    def view_course(self, course_name):
        course = open('tempfile.txt', 'r')
        while True:
            line = course.readline()
            if line == course_name:
                find_course = True

            if find_course and line != '*':
                return line

            elif find_course and line == '*':
                break
