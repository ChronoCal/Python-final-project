# 100705779, 100702991, 100703659
# Kevin Nguyen, Mark Bermah , Matthew Martin

from Students import students
from Faculty import Faculty
from ParsingTest import Parse


def main():

    while True:
        print('_______________________________________________')
        
        print('Welcome to the Student Registration System\n')
        print('[1] Student login')
        print('[2] Faculty login')
        print('[3] Exit')
        print('_______________________________________________')
        login_type = input('\n> ')

        if login_type == '1':
            print('Please enter credentials')
            ID = input('\nID: ')
            input_password = input('Password: ')
            ID = ID.strip()
            input_password = input_password.strip()
            student_login(ID, input_password)

        elif login_type == '2':
            print('Please enter credentials')
            ID = input('\nID: ')
            input_password = input('Password: ')
            ID = ID.strip()
            input_password = input_password.strip()
            faculty_login(ID, input_password)

        elif login_type == '3':
            exit()

        else:
            print('\nplease make a valid selection')
            input('\npress ENTER to continue\n')


def student_login(ID, input_password):
    loginCheck = False
    parse = Parse()
    try:
        student = students(ID)
        user_password = student.verify(input_password)
        if user_password:
            print('Student Login Successful')
            input('\npress ENTER to continue')
            loginCheck = True

        else:
            loginCheck = False
            print('Login Failed')
            reset = input('\nReset password [y/n]?')
            if reset == 'y':
                first = input('First name: ')
                last = input('Last name: ')
                DoB = input('Date of birth(dd/mm/yy): ')
                address = input('Address: ')

                if first == student.get_Fname() and last == student.get_Lname() and address == student.get_address() and DoB == student.get_DoB():
                    newPassword = input('Enter a new password: ')
                    parse.s_new_password(ID, newPassword)

                else:
                    print('invalid information')
                    input('\npress ENTER to continue')
                main()
            else:
                main()

    except AttributeError:
        print('Login Failed')
        input('\npress ENTER to continue')

    while loginCheck:
        print('\nStudent control')
        print('_______________________________________________')
        
        print('What would you like to do?\n')
        print('[1] View info')
        print('[2] View available courses')
        print('[3] Drop a course')
        print('[4] View course load')
        print('[5] Logout')
        print('_______________________________________________')
        choice = input('\nWhat would you like to do?> ')

        if choice == '1':
            #format the output
            slst = parse.s_get_info(ID)
            # print(slst)
            print('\nFirst name:', slst[0])
            print('last name:', slst[1])
            print('Address:', slst[2])
            print('Date of Birth:', slst[3])
            print('Department:', slst[4])
            print('Email:', slst[5])
            print('Student ID:', slst[6])
            input('\npress ENTER to continue')


        elif choice == '2':

            coursesAvailable = parse.view_available_courses(ID)
            # prints the available courses
            print('Courses available are: ')

            a = 0
            while a < len(coursesAvailable):
                    print('Course name:', coursesAvailable[a][0], ' Course code:', coursesAvailable[a][3])
                    a += 1

            # prompts the user for which course they wish to enroll in
            
            while True:
                courseRegister = input('\nEnter the ID of the course you wish to sign up for: ')

                Course = parse.get_course(courseRegister)

                if ID in Course:
                    print("You are already registered for this course")
                    input('\npress ENTER to continue')
                    break

                elif len(courseRegister) != 9:
                    print("Enter a 9 character code please.")
                    input('\npress ENTER to continue')
                    break

                else:
                    parse.s_register_course(courseRegister, ID)
                    break

        elif choice == '3':

            coursesEnrolled = parse.s_courses_enrolled(ID)

            print('Courses you are enrolled in are: ')
            a = 0

            while a < len(coursesEnrolled):
                if coursesEnrolled[a].__contains__(str(ID)):
                    print(a, '- Course name:', coursesEnrolled[a][0], ' Course code:', coursesEnrolled[a][3])
                a += 1

            choice = input('Enter the ID of the course that you wish to drop out of: ')


            if len(choice) != 9:
                print('Please enter a valid course')
                input('\npress ENTER to continue')


            else:
                parse.s_drop_course(ID, choice)

        elif choice == '4':
            coursesEnrolled = parse.s_courses_enrolled(ID)

            print('Courses you are enrolled in are: ')
            a = 0
            b = 1
            while a < len(coursesEnrolled):
                if coursesEnrolled[a].__contains__(str(ID)):
                    print(b, '- Course name:', coursesEnrolled[a][0], ' Course code:', coursesEnrolled[a][3])
                    b += 1
                a += 1

            input('\npress ENTER to continue')

        elif choice == '5':
            leave = input('Are you sure [y/n]? ')
            if leave == 'y':
                break
            else:
                pass


def faculty_login(ID, input_password):
    loginCheck = False
    parse = Parse()
    try:
        faculty = Faculty(ID)
        user_password = faculty.verify(input_password)
        if user_password:
            print('Faculty Login Successful')
            input('\npress ENTER to continue')
            loginCheck = True

        else:
            loginCheck = False
            reset = input('Reset password [y/n]?')
            if reset == 'y':
                first = input('First name: ')
                last = input('Last name: ')
                DoB = input('Date of birth(dd/mm/yy): ')
                address = input('Address: ')

                if first == faculty.get_Fname() and last == faculty.get_Lname() and address == faculty.get_address() and DoB == faculty.get_DoB():
                    newPassword = input('Enter a new password: ')
                    parse.f_new_password(ID, newPassword)
                    print('Password reset successfully')
                    input('\npress ENTER to continue')

                else:
                    print('invalid information')
                    input('\npress ENTER to continue')
                main()
            else:
                main()

    except AttributeError:
        print('Login Failed')
        input('\npress ENTER to continue')

    while loginCheck:
        print('\nFaculty control')
        print('_______________________________________________')
        print('[1] View courses')
        print('[2] View students')
        print('[3] Add course')
        print('[4] Update course')
        print('[5] View students in all courses')
        print('[6] View a student and their course load')
        print('_______________________________________________')
        choice = input('\nWhat would you like to do?> ')

        if choice == '1':

            slst = parse.get_all_courses()
            a = 0
            while a < len(slst):
                print('Course name:', slst[a][0], ' Course code:', slst[a][3])
                a += 1
            input('\npress ENTER to continue')

        elif choice == '2':
            pass

        elif choice == '3':
            cName = input('Enter the course name: ')
            cStudents = '0'
            cMax = input('Enter the max number of students: ')
            cID = input('Enter the course ID: ')
            cDepartment = input('Enter the course department: ')
            course = cName + '^' + cStudents + '^' + cMax + '^' + cID + '^' + cDepartment + '^'
            parse.f_add_course(course)

        elif choice == '4':
            courses = parse.get_all_courses()

            a = 0
            while a < len(courses):
                print('Course name:', courses[a][0], ' Course code:', courses[a][3])
                a += 1

            # prompts the user for which course they wish to change
            while True:
                # make sure that the input is 9 characters long
                choice = input('Enter the ID of the course you wish to change: ')
                if len(choice) != 9:
                    print("Please enter a correct course ID")
                    input('\npress ENTER to continue')
                    break

                else:
                    course = parse.get_course(choice)
                    if course == []:
                        print('Course does not exist')
                        input('\npress ENTER to continue')

                    else:
                        cName = input('Enter the course name: ')
                        cMax = input('Enter the max number of students (do not make this number lower '
                                     'than the students registered): ')
                        cID = input('Enter the course ID: ')
                        cDepartment = input('Enter the course department: ')
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
                        print("You successfully updated this course.")
                        input('\npress ENTER to continue')
                        break


        elif choice == '5':
            parse.f_view_students_in_courses()

        elif choice == '6':
            sID = input("Enter the ID of the student: ")

            slst = parse.s_get_info(sID)
            print('\nFirst name:', slst[0])
            print('last name:', slst[1])
            print('Address:', slst[2])
            print('Date of Birth:', slst[3])
            print('Department:', slst[4])
            print('Email:', slst[5])
            print('Student ID:', slst[6])

            clst = parse.s_courses_enrolled(sID)
            # print(clst)
            print('The courses this student is enrolled in: ')

            a = 0

            while a < len(clst):
                if clst[a].__contains__(str(sID)):
                    print(a, '- Course name:', clst[a][0], ' Course code:', clst[a][3])
                a += 1
            input('\npress ENTER to continue')
main()
