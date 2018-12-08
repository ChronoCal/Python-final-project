# Student IDs
# names

from Students import students
from Faculty import Faculty
from ParsingTest import Parse

def main():

    loginCheck = False

    while True:
        print('_______________________________________________')
        print('Welcome to the Student Registration System\n')
        print('[1] Student login')
        print('[2] Faculty login')
        print('_______________________________________________')
        login_type = input('\n> ')

        print('Please enter credentials')
        ID = input('\nID: ')
        Password = input('Password: ')
        ID = ID.strip()
        Password = Password.strip()

        if login_type == '1':
            type1(ID, Password)

        elif login_type == '2':
            type2(ID, Password)

        elif login_type == '3':
            break

        else:
            print('\nplease make a valid selection')
            input('\npress ENTER to continue\n')


def type1(ID, Password):
    loginCheck = False
    parse = Parse()
    # print('pick 1')
    try:
        student = students(ID)
        detective_pikachu_is_danny_devito = student.verify(Password)
        if detective_pikachu_is_danny_devito:
            print('welcome to the club')
            loginCheck = True

        else:
            loginCheck = False
            main()


    except AttributeError:
        print('TOO BAD')

    while loginCheck:
        print('_______________________________________________')
        print('What would you like to do?\n')
        print('[1] View info')
        print('[2] View available courses')
        print('[3] Drop a course')
        print('[4] View course load')
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
                    print('Course name:', coursesAvailable[a][0], ' Course code:', coursesAvailable[a][3])
                    a += 1

            # prompts the user for which course they wish to enroll in
            while True:
                #make sure that the input is 7 characters long
                courseRegister = input('\nEnter the ID of the course you wish to sign up for:')

                Course = parse.get_course(courseRegister)

                if ID in Course:
                    print("Sorry, you are already registered for this course")
                    break

                elif len(courseRegister) != 9:
                    print("Enter a 9 character code please.")
                    break

                else:
                    parse.s_register_course(courseRegister, ID)
                    break



        elif choice == '3':

            coursesEnrolled = parse.s_courses_enrolled(ID)

            # prints the avalible courses
            print('Courses you are enrolled in are:')
            a = 0
            cStudentsRegistered = []

            while a < len(coursesEnrolled):
                if coursesEnrolled[a].__contains__(str(ID)):
                    print(a, '- Course name:', coursesEnrolled[a][0], ' Course code:', coursesEnrolled[a][3])
                a += 1
            choice = input('Enter the ID of the course that you wish to drop out of.')

            parse.s_drop_course(ID, choice)

            elif choice == '4':
                pass


def type2(ID, Password):
    loginCheck = False
    parse = Parse()

    parse.f_authenticate(ID, Password)

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
            slst = parse.get_all_courses()




        elif choice == '2':
            break

        elif choice == '3':
            cName = input('Enter the course name:')
            cStudents = '0'
            cMax = input('Enter the max number of students:')
            cID = input('Enter the course ID:')
            cDepartment = input('Enter the course department:')
            course = " "
            course = cName + '^' + cStudents + '^' + cMax + '^' + cID + '^' + cDepartment + '^'
            parse.f_add_course(course)


        elif choice == '4':
            courses = parse.get_all_courses()

            a = 0
            cStudentsRegistered = []

            while a < len(courses):
                print('Course name:', courses[a][0], ' Course code:', courses[a][3])
                a += 1

            # prompts the user for which course they wish to change
            while True:
                #make sure that the input is 9 characters long
                choice = input('Enter the ID of the course you wish to change:')
                if len(choice) != 9:
                    print("Enter a 9 character code please.")

                else:
                    course = parse.get_course(choice)
                    print(course)
                    cName = input('Enter the course name:')
                    cMax = input('Enter the max number of students (do not make this number lower than the students registered):')
                    cID = input('Enter the course ID:')
                    cDepartment = input('Enter the course department:')
                    course[0] = cName
                    course[2] = cMax
                    course[3] = cID
                    course[4] = cDepartment
                    a = 0
                    courseStr = ""
                    while a < len(course) - 1:
                        courseStr += course[a] + "^"
                        a += 1
                    parse.f_update_course(courseStr, choice)
                    print("You successfully registered for this course.")
                    break


        elif choice == '5':

            parse.f_veiw_students_in_courses()


    # elif login_type == '3':
    #     parse = Parse(ID, Password, courseID, fID, fPassword)
    #
    #     slst = parse.s_get_info(ID)
    #
    #     print(slst)
    #     # Faculty(id, password)


main()