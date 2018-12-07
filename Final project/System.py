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
        login_type = input('\n> ')

        if login_type == '1':
            break

        elif login_type == '2':
            break

        elif login_type == '3':
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
        parse = Parse(ID, Password, courseID, fID, fPassword)

        parse.s_authenticate(sID, sPassword)

        while True:
            print('_______________________________________________')
            print('What would you like to do?\n')
            print('[1] Veiw info')
            print('[2] View available courses')
            print('[3] Drop a course')
            print('[4] View available courses')
            print('_______________________________________________')
            choice = input('\n>')

            if choice == '1':

                #format this to look nice
                slst = parse.s_get_info(ID)

                print(slst)

            elif choice == '2':

                coursesAvailable = parse.view_available_courses(ID)

                # prints the avalible courses
                print('Courses available are:')

                a = 0
                cStudentsRegistered = []

                while a < len(coursesAvailable):
                    if coursesAvailable[a].__contains__(str(sID)):
                        (coursesAvailable[a][0], ', you are already registered for this course.')
                        #not sure what this is:
                        cStudentList = coursesAvailable[a][5].split(',')
                        cStudentsRegistered.append(cStudentList)

                    else:
                        print('Course name:', coursesAvailable[a][0], ' Course code:', coursesAvailable[a][3])
                    a += 1
                # prompts the user for which course they wish to enroll in
                clst = parse.get_all_courses()

                while True:
                    #make sure that the input is 7 characters long
                    courseRegister = input('\nEnter the ID of the course you wish to sign up for:')

                    if parse.get_all_courses().__contains__(sID):
                        print("Sorry, you are already registered for this course")

                    elif len(courseRegister) != 9:
                        print("Enter a 9 character code please.")

                    else:
                        parse.s_register_course(courseRegister, ID)
                        print("You successfully registered ")
                        break



            elif choice == '3':

                coursesEnrolled = parse.s_courses_enrolled(ID)

                # prints the avalible courses
                print('Courses you are enrolled in are:')
                print(coursesEnrolled)
                a = 0
                cStudentsRegistered = []

                while a < len(coursesEnrolled):
                    if coursesEnrolled[a].__contains__(str(sID)):
                        print('Course name:', coursesAvailable[a][0], ' Course code:', coursesAvailable[a][3])
                    a += 1
                #


    elif login_type == '2':
        parse = Parse(ID, Password, courseID, fID, fPassword)

        parse.f_authenticate(sID, sPassword)

        while True:
            print('_______________________________________________')
            print('What would you like to do?\n')
            print('[1] Veiw courses')
            print('[2] View students')
            print('[3] Add course')
            print('[4] Update course')
            print('[5] View students in specific course')
            print('_______________________________________________')
            choice = input('\n>')

            if choice == '1':

                #format this to look nice
                slst = parse.f_view_course_info()



            elif choice == '2':
                break

            elif choice == '3':
                break

            elif choice == '4':
                break

            elif choice == '5':
                break
    elif login_type == '3':
        parse = Parse(ID, Password, courseID, fID, fPassword)

        slst = parse.s_get_info(ID)

        print(slst)
        # Faculty(id, password)

    else:
        print('OOPS something went wrong')

main()