# Student IDs
# names

from Students import students
from Faculty import Faculty
from ParsingTest import Parse

def main():

    while True:
        print('_______________________________________________')
        print('Welcome to the Student Registration System\n')
        print('[1] Student login')
        print('[2] Faculty login')
        print('_______________________________________________')
        login_type = input('\nSpecify login: ')

        if login_type == '1':
            break

        elif login_type == '2':
            break

        else:
            print('\nplease make a valid selection')
            input('\npress ENTER to continue\n')

    print('Please enter credentials')
    ID = input('\nID: ')
    Password = input('Password: ')
    sID = 0
    sPassword = 0
    courseID = 0
    fID = 0
    fPassword = 0

    if login_type == '1':
        print('pick 1')
        parse = Parse(ID, Password, courseID, fID, fPassword)

        parse.s_authenticate(sID, sPassword)

    elif login_type == '2':
        print('pick 2')
        # Faculty(id, password)

    else:
        print('OOPS something went wrong')

main()