
class Parse:

    def __init__(self, sID, sPassword, courseID, fID, fPassword):
        self.sID = sID
        self.sPassword = sPassword
        self.courseID = courseID
        self.fID = fID
        self.fPassword = fPassword


    def s_get_info(self, sID):
        testFile = open("testParseFile.txt", "r")
        for line in testFile:
            slst = line.split("^")
            if slst.__contains__(sID):
                return slst

    def view_available_courses(selfself, sID):
        #file with student info in it
        testFile = open("testParseFile.txt", "r")
        #file with course info in it
        courseFile = open("testCourseFile.txt", "r")

        coursesAvailable = []

        #uses student ID to find the students's department
        sDepartment = "str"
        for line in testFile:
            lst = line.split("^")
            if lst.__contains__(sID):
                sDepartment = lst[4]
        for line in courseFile:
            lst = line.split("^")
            if lst[5].split(',').__contains__(sID):
                taken = (coursesAvailable[a][0], ', you are already registered for this course.')
                coursesAvailable.append(taken)

            elif lst.__contains__(sDepartment) and int(lst[1]) < int(lst[2]):
                coursesAvailable.append(lst)
        return coursesAvailable

    def get_all_courses(self):

        #file with course info in it
        courseFile = open("testCourseFile.txt", "r")
        allCourses = []
        for line in courseFile:
            lst = line.split("^")
            allCourses.append(lst)
        return allCourses


    def s_courses_enrolled(self, sID):
        courseFile = open("testCourseFile.txt", "r")
        coursesEnrolled = []
        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(sID):
                coursesEnrolled.append(lst)
        return coursesEnrolled

    def s_register_course(self, courseID, sID):
        # updates the courses availability
        tempCourseFile = open("tempCourseFile.txt", 'a')
        courseFile = open("testCourseFile.txt", "r")
        testFile = open("testParseFile.txt", "r")
        tempFile = open("tempParseFile.txt", "a")


        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(sID) and lst.__contains__(courseID):
                print("Sorry, you are already registered for this course")
            elif lst.__contains__(courseID):
                # is there a better way to do this?
                cName = lst[0]
                cStudents = int(lst[1]) + 1
                cMaxStudents = lst[2]
                cID = lst[3]
                cDepartment = lst[4]
                cStudent = str(lst[5].strip())
                cStudent = str(cStudent) + str(sID) + ","
                cEntry = cName + "^" + str(
                    cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cStudent + "\n"
                tempCourseFile.write("%s" % cEntry)

            else:
                tempCourseFile.write("%s" % line)

            for line in testFile:
                lst = line.split("^")
                if lst.__contains__(sID):
                    sFirstName = lst[0]
                    sLastName =lst[1]
                    sAddress =lst[2]
                    sDoB =lst[3]
                    sDepartment =lst[4]
                    sfEmail =lst[5]
                    sID =lst[6]
                    sPassword =lst[7]
                    sCourses = lst[8].strip()
                    sCourses = str(sCourses) + (courseID) + ","
                    studentEntry = sFirstName + "^" + sLastName + "^" + sAddress + "^" + sDoB + "^" + sDepartment + "^" + sfEmail + "^" + sID + "^" + sPassword + "^" + sCourses +"\n"
                    tempFile = open("tempParseFile.txt", "a")
                    tempFile.write("%s" % studentEntry)
                    tempFile.close()
                else:
                    tempFile = open("tempParseFile.txt", "a")
                    tempFile.write("%s" % line)
                    tempFile.close()

        # writing each line of the updated temp course file to the real one
        courseFile = open("testCourseFile.txt", "w")
        tempCourseFile = open("tempCourseFile.txt", 'r')
        for line in tempCourseFile:
            courseFile.write(line)
        courseFile.close()
        tempCourseFile.close()
        tempCourseFile = open("tempCourseFile.txt", 'w')
        tempCourseFile.write("")
        tempCourseFile.close()


        parseFile = open("testParseFile.txt", "w")
        tempFile = open("tempParseFile.txt", 'r')
        for line in tempFile:
            parseFile.write(line)
        parseFile.close()
        tempFile.close()
        tempFile = open("tempParseFile.txt", 'w')
        tempFile.write("")
        tempFile.close()


    def s_drop_course(self, sID, courseID):
        # file with student info in it
        testFile = open("testParseFile.txt", "r")
        # file with course info in it
        courseFile = open("testCourseFile.txt", "r")

        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(courseRegister):
                # is there a better way to do this?
                cName = lst[0]
                cStudents = int(lst[1]) - 1
                cMaxStudents = lst[2]
                cID = lst[3]
                cDepartment = lst[4]
                cStudent = lst[5]
                sNumbers = cStudent.split(',')
                index = sNumbers.find(sID)
                sNumbers.remove(index)
                cEntry = cName + "^" + str(
                    cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cStudent + "\n"
                tempCourseFile.write("%s" % cEntry)

            else:
                tempCourseFile.write("%s" % line)


        # writing each line of the updated temp course file to the real one
        courseFile = open("testCourseFile.txt", "w")
        tempCourseFile = open("tempCourseFile.txt", 'r')
        for line in tempCourseFile:
            courseFile.write(line)
        courseFile.close()
        tempCourseFile.close()

    def s_authenticate(self, sID, sPassword):
        testFile = open("testParseFile.txt", "r")
        loginAttempt = False
        id = sID
        password = sPassword
        for line in testFile:
            if line.__contains__("#"):
                continue
            else:
                lst = line.split('^')
                if lst[6] == sID and lst[7] == sPassword:
                    loginAttempt = True
                    print("test")


    def s_register_user(self):

        testFile = open("testParseFile.txt", "a")
        testFile.write("%s" % studentEntry)
        testFile.write("\n")
        testFile.close()

    #get the information from the factuly here, or in main line and import it
    def f_add_course(self):
        pass

    def f_update_course(self):

        courseFile = open("testCourseFile.txt", "r")
        tempCourseFile = open("tempCourseFile.txt", 'w')

        choice = input('Would you like to do: see all courses(1), search by name(2) or search by department(3)')
        if choice == '1':
            for line in courseFile:
                lst = line.split("^")
                print('Course Name:', lst[0], 'Department: ', lst[4], 'Max capacity', lst[2], 'Course ID:', lst[3])
        elif choice == '2':
            name = input('Enter then name of the course:')
            for line in courseFile:
                lst = line.split("^")
                if lst.__contains__(name):
                    print('Course Name:', lst[0], 'Department: ', lst[4], 'Max capacity', lst[2], 'Course ID:', lst[3])
        elif choice == '3':
            department = input('Enter then department of the course you are looking for:')
            for line in courseFile:
                lst = line.split("^")
                if lst.__contains__(department):
                    print('Course Name:', lst[0], 'Department: ', lst[4], 'Max capacity', lst[2], 'Course ID:', lst[3])
        cID = "10012345"
        while True:
            cID = input('Enter the ID of the course you with to manage: ')
            for line in courseFile:
                print('test')
                lst = line.split("^")
                if lst.__contains__(cID):
                    correctCourse = input('Is this the correct course? (y/n)\n'
                                          'Course Name:', lst[0], ' Department:', lst[4], ' Max capacity:', lst[2], ' Course ID:', lst[3])
                    if correctCourse == 'y':
                        break
                    else:
                        pass

        cPart = input('Which part would you like to change in this course? Name(1), Max students(2), ID(3), Department(4) or Avalible seasons(5) ')

        if cPart == '1':
            newName()
        elif cPart == '2':
            newMax()
        elif cPart == '3':
            newID()
        elif cPart == '4':
            newDepartment()


        def newName():
            newName = input('What would you like to change the name to?')
            for line in courseFile:
                lst = line.split("^")
                if lst.__contains__(cID):
                    # is there a better way to do this?
                    cName = newName
                    cStudents = lst[1]
                    cMaxStudents = lst[2]
                    cID = lst[3]
                    cDepartment = lst[4]
                    cSeasons = lst[5]
                    cEntry = cName + "^" + str(
                        cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
                    tempCourseFile.write("%s" % cEntry)
                else:
                    tempCourseFile.write(line)
                courseFile = open("testCourseFile.txt", "w")
                tempCourseFile = open("tempCourseFile.txt", 'r')
                for line in tempCourseFile:
                    courseFile.write(line)

        def newMax():
            newMax = input('What would you like the maximum students to be?')
            for line in courseFile:
                lst = line.split("^")
                if lst.__contains__(cID):
                    # is there a better way to do this?
                    cName = lst[0]
                    cStudents = lst[1]
                    cMaxStudents = newMax
                    cID = lst[3]
                    cDepartment = lst[4]
                    cSeasons = lst[5]
                    cEntry = cName + "^" + str(
                        cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
                    tempCourseFile.write("%s" % cEntry)
                else:
                    tempCourseFile.write(line)
                courseFile = open("testCourseFile.txt", "w")
                tempCourseFile = open("tempCourseFile.txt", 'r')
                for line in tempCourseFile:
                    courseFile.write(line)
        def newID():
            newID = input('What would you like the course ID to be?')
            for line in courseFile:
                lst = line.split("^")
                if lst.__contains__(cID):
                    # is there a better way to do this?
                    cName = lst[0]
                    cStudents = lst[1]
                    cMaxStudents = lst[2]
                    cID = newID
                    cDepartment = lst[4]
                    cSeasons = lst[5]
                    cEntry = cName + "^" + str(
                        cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
                    tempCourseFile.write("%s" % cEntry)
                else:
                    tempCourseFile.write(line)
                courseFile = open("testCourseFile.txt", "w")
                tempCourseFile = open("tempCourseFile.txt", 'r')
                for line in tempCourseFile:
                    courseFile.write(line)

        def newDepartment():
            newDepartment = input('What would you like the course department to be?')
            for line in courseFile:
                lst = line.split("^")
                if lst.__contains__(cID):
                    # is there a better way to do this?
                    cName = lst[0]
                    cStudents = lst[1]
                    cMaxStudents = lst[2]
                    cID = lst[3]
                    cDepartment = newDepartment
                    cSeasons = lst[5]
                    cEntry = cName + "^" + str(
                        cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
                    tempCourseFile.write("%s" % cEntry)
                else:
                    tempCourseFile.write(line)
                courseFile = open("testCourseFile.txt", "w")
                tempCourseFile = open("tempCourseFile.txt", 'r')
                for line in tempCourseFile:
                    courseFile.write(line)

    def f_see_all_courses(self):
        pass

    def f_view_course_info(self):
        pass

    def f_view_student_info(self):
        pass

    def f_list_students_in_courses(self):
        pass

    def f_authenticate(self, fID, fPassword):
        facultyFile = open("testFacultyFile.txt", "r")
        loginAttempt = False
        id = fID
        password = fPassword
        for line in facultyFile:
            if line.__contains__("#"):
                continue
            else:
                lst = line.split('^')
                if lst[6] == fID and lst[7] == fPassword:
                    loginAttempt = True
                    print("test")

    def f_register_user(self):

        testFile = open("testFacultyFile.txt", "a")
        testFile.write("%s" % facultyEntry + '\n')
        testFile.close()
        main()


# def main():
#
#     choice = input("What would you like to do? search (1), add person (2), register course (3), edit courses (4)")
#     if choice == "1":
#         searchStudents()
#     elif choice == "2":
#         addStudent()
#     elif choice == "3":
#         registerCourse()
#     elif choice == "4":
#         editCourses()
#
#
# def addStudent():
#     print("Enter the your info")
#     sFirstName = str(input("First Name:"))
#     sLastName = str(input("Last Name:"))
#     sAddress = str(input("Address:"))
#     sDoB = str(input("Date of Birth (dd/mm/yy):"))
#     sDepartment = str(input("Department:"))
#     sEmail = str(input("Email Address:"))
#     sID = str(input("ID:"))
#     sPassword = str(input("Password:"))
#     studentEntry = sLastName + "^" + sFirstName + "^" + sAddress + "^" + sDoB + "^" + sDepartment + "^" + sEmail + "^" + sID + "^" + sPassword + '^' + "\n"
#     testFile = open("testParseFile.txt", "a")
#     testFile.write("%s" % studentEntry)
#     testFile.write("\n")
#     testFile.write("\n")
#     testFile.close()
#     main()
#
# def addFaculty():
#     print("Enter the your info")
#     fFirstName = str(input("First Name:"))
#     fLastName = str(input("Last Name:"))
#     fAddress = str(input("Address:"))
#     fDoB = str(input("Date of Birth (dd/mm/yy):"))
#     fDepartment = str(input("Department:"))
#     fEmail = str(input("Email Address:"))
#     fID = str(input("ID:"))
#     fPassword = str(input("Password:"))
#     facultyEntry = fLastName + "^" + fFirstName + "^" + fAddress + "^" + fDoB + "^" + fDepartment + "^" + fEmail + "^" + fID + "^" + fPassword +"\n"
#     testFile = open("testFacultyFile.txt", "a")
#     testFile.write("%s" % facultyEntry + '\n')
#     testFile.close()
#     main()
#
# """Searchs the student text file by name or id"""
# def searchStudents():
#     testFile = open("testParseFile.txt", "r")
#     input = input("Enter either the name ('first last') or the ID of the person you would like to see.")
#
#     try:
#         int(input)
#     except ValueError:
#         input.lower()
#         input
#     for line in testFile:
#         lst = line.split("^")
#         if lst.__contains__(input):
#             print(lst)
#         else:
#             print("fail")
#             pass
#     main()
#
# """ make sure students cannot register for the same course again """
# def registerCourse():
#
#     #we will already know which student will be registering because they have to login, I will choose someone
#     sID = '1111234567'
#
#     #file with student info in it
#     testFile = open("testParseFile.txt", "r")
#     #file with student info in it
#     courseFile = open("testCourseFile.txt", "r")
#
#     coursesAvailable = []
#
#     #uses student ID to find the students's department
#     sDepartment = "str"
#     for line in testFile:
#         lst = line.split("^")
#         if lst.__contains__(sID):
#             sDepartment = lst[4]
#     #uses student department to find courses they can take
#     for line in courseFile:
#         lst = line.split("^")
#         if lst.__contains__(sDepartment) and int(lst[1]) < int(lst[2]):
#             coursesAvailable.append(lst)
#     #prints the avalible courses
#     print('Courses available are:')
#     a = 0
#     cStudentsRegistered = []
#     while a < len(coursesAvailable):
#         if coursesAvailable[a][5].__contains__(sID):
#             print(coursesAvailable[a][0], ', you are already registered for this course.')
#             cStudentList = coursesAvailable[a][5].split(',')
#             cStudentsRegistered.append(cStudentList)
#
#         else:
#             print('Course name:', coursesAvailable[a][0], ' Course code:', coursesAvailable[a][3])
#         a += 1
#     #prompts the user for which course they wish to enroll in
#     try:
#         courseRegister = input('\nEnter the ID of the course you wish to sign up for:')
#
#     except ValueError:
#         print('Please enter a numerical ID.')
#     # updates the courses availability
#     tempCourseFile = open("tempCourseFile.txt", 'w')
#     courseFile = open("testCourseFile.txt", "r")
#
#     for line in courseFile:
#         lst = line.split("^")
#         if lst.__contains__(sID) and lst.__contains__(courseRegister):
#             print("Sorry, you are already registered for this course")
#         elif lst.__contains__(courseRegister):
#             # is there a better way to do this?
#             cName = lst[0]
#             cStudents = int(lst[1]) + 1
#             cMaxStudents = lst[2]
#             cID = lst[3]
#             cDepartment = lst[4]
#             cStudent = lst[5].strip()
#             cStudent = cStudent + sID + ","
#             cEntry = cName + "^" + str(
#                 cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cStudent + "\n"
#             tempCourseFile.write("%s" % cEntry)
#
#         else:
#             tempCourseFile.write("%s" % line)
#     # writing each line of the updated temp course file to the real one
#     courseFile = open("testCourseFile.txt", "w")
#     tempCourseFile = open("tempCourseFile.txt", 'r')
#     for line in tempCourseFile:
#         courseFile.write(line)
#     courseFile.close()
#     tempCourseFile.close()
#     main()
#
# def editCourses():
#     courseFile = open("testCourseFile.txt", "r")
#     tempCourseFile = open("tempCourseFile.txt", 'w')
#
#     choice = input('Would you like to do: see all courses(1), search by name(2) or search by department(3)')
#     if choice == '1':
#         for line in courseFile:
#             lst = line.split("^")
#             print('Course Name:', lst[0], 'Department: ', lst[4], 'Max capacity', lst[2], 'Course ID:', lst[3])
#     elif choice == '2':
#         name = input('Enter then name of the course:')
#         for line in courseFile:
#             lst = line.split("^")
#             if lst.__contains__(name):
#                 print('Course Name:', lst[0], 'Department: ', lst[4], 'Max capacity', lst[2], 'Course ID:', lst[3])
#     elif choice == '3':
#         department = input('Enter then department of the course you are looking for:')
#         for line in courseFile:
#             lst = line.split("^")
#             if lst.__contains__(department):
#                 print('Course Name:', lst[0], 'Department: ', lst[4], 'Max capacity', lst[2], 'Course ID:', lst[3])
#     cID = "10012345"
#     while True:
#         cID = input('Enter the ID of the course you with to manage: ')
#         for line in courseFile:
#             print('test')
#             lst = line.split("^")
#             if lst.__contains__(cID):
#                 correctCourse = input('Is this the correct course? (y/n)\n'
#                                       'Course Name:', lst[0], ' Department:', lst[4], ' Max capacity:', lst[2], ' Course ID:', lst[3])
#                 if correctCourse == 'y':
#                     break
#                 else:
#                     pass
#
#     cPart = input('Which part would you like to change in this course? Name(1), Max students(2), ID(3), Department(4) or Avalible seasons(5) ')
#
#     if cPart == '1':
#         newName()
#     elif cPart == '2':
#         newMax()
#     elif cPart == '3':
#         newID()
#     elif cPart == '4':
#         newDepartment()
#     elif cPart == '5':
#         newSeasons()
#
#
# def newName():
#     newName = input('What would you like to change the name to?')
#     for line in courseFile:
#         lst = line.split("^")
#         if lst.__contains__(cID):
#             # is there a better way to do this?
#             cName = newName
#             cStudents = lst[1]
#             cMaxStudents = lst[2]
#             cID = lst[3]
#             cDepartment = lst[4]
#             cSeasons = lst[5]
#             cEntry = cName + "^" + str(
#                 cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
#             tempCourseFile.write("%s" % cEntry)
#         else:
#             tempCourseFile.write(line)
#         courseFile = open("testCourseFile.txt", "w")
#         tempCourseFile = open("tempCourseFile.txt", 'r')
#         for line in tempCourseFile:
#             courseFile.write(line)
# def newMax():
#     newMax = input('What would you like the maximum students to be?')
#     for line in courseFile:
#         lst = line.split("^")
#         if lst.__contains__(cID):
#             # is there a better way to do this?
#             cName = lst[0]
#             cStudents = lst[1]
#             cMaxStudents = newMax
#             cID = lst[3]
#             cDepartment = lst[4]
#             cSeasons = lst[5]
#             cEntry = cName + "^" + str(
#                 cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
#             tempCourseFile.write("%s" % cEntry)
#         else:
#             tempCourseFile.write(line)
#         courseFile = open("testCourseFile.txt", "w")
#         tempCourseFile = open("tempCourseFile.txt", 'r')
#         for line in tempCourseFile:
#             courseFile.write(line)
# def newID():
#     newID = input('What would you like the course ID to be?')
#     for line in courseFile:
#         lst = line.split("^")
#         if lst.__contains__(cID):
#             # is there a better way to do this?
#             cName = lst[0]
#             cStudents = lst[1]
#             cMaxStudents = lst[2]
#             cID = newID
#             cDepartment = lst[4]
#             cSeasons = lst[5]
#             cEntry = cName + "^" + str(
#                 cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
#             tempCourseFile.write("%s" % cEntry)
#         else:
#             tempCourseFile.write(line)
#         courseFile = open("testCourseFile.txt", "w")
#         tempCourseFile = open("tempCourseFile.txt", 'r')
#         for line in tempCourseFile:
#             courseFile.write(line)
# def newDepartment():
#     newDepartment = input('What would you like the course department to be?')
#     for line in courseFile:
#         lst = line.split("^")
#         if lst.__contains__(cID):
#             # is there a better way to do this?
#             cName = lst[0]
#             cStudents = lst[1]
#             cMaxStudents = lst[2]
#             cID = lst[3]
#             cDepartment = newDepartment
#             cSeasons = lst[5]
#             cEntry = cName + "^" + str(
#                 cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
#             tempCourseFile.write("%s" % cEntry)
#         else:
#             tempCourseFile.write(line)
#         courseFile = open("testCourseFile.txt", "w")
#         tempCourseFile = open("tempCourseFile.txt", 'r')
#         for line in tempCourseFile:
#             courseFile.write(line)
# def newSeasons():
#     newSeasons = input(
#         'What would you like the available seasons to be? \n(Summer, Fall, Winter, Spring. a four digit number with a 1 if the course is available during the seasona and a 0 if it is not. eg: 0011)')
#     for line in courseFile:
#         lst = line.split("^")
#         if lst.__contains__(cID):
#             cName = lst[0]
#             cStudents = lst[1]
#             cMaxStudents = lst[2]
#             cID = lst[3]
#             cDepartment = lst[4]
#             cSeasons = newSeasons
#             cEntry = cName + "^" + str(
#                 cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
#             tempCourseFile.write("%s" % cEntry)
#         else:
#             tempCourseFile.write(line)
#         courseFile = open("testCourseFile.txt", "w")
#         tempCourseFile = open("tempCourseFile.txt", 'r')
#         for line in tempCourseFile:
#             courseFile.write(line)
#
# main()
