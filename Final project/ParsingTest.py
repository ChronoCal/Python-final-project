#change: text file names, functions names, variables

def main():

    choice = input("What would you like to do? search (1), add person (2), register course (3), edit courses (4)")
    if choice == "1":
        searchStudents()
    elif choice == "2":
        addStudent()
    elif choice == "3":
        registerCourse()
    elif choice == "4":
        editCourses()


def addStudent():
    print("Enter the your info")
    sFirstName = str(input("First Name:"))
    sLastName = str(input("Last Name:"))
    sAddress = str(input("Address:"))
    sDoB = str(input("Date of Birth (dd/mm/yy):"))
    sDepartment = str(input("Department:"))
    sEmail = str(input("Email Address:"))
    sID = str(input("ID:"))
    sPassword = str(input("Password:"))
    studentEntry = sLastName + "^" + sFirstName + "^" + sAddress + "^" + sDoB + "^" + sDepartment + "^" + sEmail + "^" + sID + "^" + sPassword +"\n"
    testFile = open("testParseFile.txt", "a")
    testFile.write("%s" % studentEntry)
    testFile.write("\n")
    testFile.write("\n")
    testFile.close()
    main()

def addFaculty():
    print("Enter the your info")
    fFirstName = str(input("First Name:"))
    fLastName = str(input("Last Name:"))
    fAddress = str(input("Address:"))
    fDoB = str(input("Date of Birth (dd/mm/yy):"))
    fDepartment = str(input("Department:"))
    fEmail = str(input("Email Address:"))
    fID = str(input("ID:"))
    fPassword = str(input("Password:"))
    facultyEntry = fLastName + "^" + fFirstName + "^" + fAddress + "^" + fDoB + "^" + fDepartment + "^" + fEmail + "^" + fID + "^" + fPassword +"\n"
    testFile = open("testParseFile.txt", "a")
    testFile.write("%s" % facultyEntry)
    testFile.write("\n")
    testFile.write("\n")
    testFile.close()
    main()

"""Searchs the student text file by name or id"""
def searchStudents():
    testFile = open("testParseFile.txt", "r")
    input = input("Enter either the name ('first last') or the ID of the person you would like to see.")

    try:
        int(input)
    except ValueError:
        input.lower()
        input
    for line in testFile:
        lst = line.split("^")
        if lst.__contains__(input):
            print(lst)
        else:
            print("fail")
            pass
    main()

"""Make a temp file, rewrite everyline into the temp file, when done, change the name of the temp file"""
def registerCourse():

    #we will already know which student will be registering because they have to login, I will choose someone
    sID = '1111234567'

    #file with student info in it
    testFile = open("testParseFile.txt", "r")
    #file with student info in it
    courseFile = open("testCourseFile.txt", "r")

    coursesAvailable = []

    #uses student ID to find the students's department and season
    sDepartment = "str"
    for line in testFile:
        lst = line.split("^")
        if lst.__contains__(sID):
            sDepartment = lst[4]
            sID = lst[6]
            sCode = sID[:4]
            sSu = int(sCode[0])
            sFa = int(sCode[1])
            sWi = int(sCode[2])
            sSp = int(sCode[3])
    #uses student department to find courses they can take
    for line in courseFile:
        lst = line.split("^")
        # cID = lst[5]
        # cCode = cID[:4]
        # cSu = int(cCode[0])
        # cFa = int(cCode[1])
        # cWi = int(cCode[2])
        # cSp = int(cCode[3])
        if lst.__contains__(sDepartment) and int(lst[1]) < int(lst[2]) :
            #and sWi == cWi and sSp == cSp
            coursesAvailable.append(lst)
    #prints the avalible courses
    print('Courses available are:')
    a = 0
    while a < len(coursesAvailable):
        print('Course name:', coursesAvailable[a][0], ' Course code:', coursesAvailable[a][3])
        a += 1
    #prompts the user for which course they wish to enroll in
    try:
        courseRegister = input('\nEnter the ID of the course you wish to sign up for:')
    except ValueError:
        print('Please enter a numerical ID.')
    # updates the courses availability
    tempCourseFile = open("tempCourseFile.txt", 'w')
    courseFile = open("testCourseFile.txt", "r")
    for line in courseFile:
        lst = line.split("^")
        if lst.__contains__(courseRegister):
            # is there a better way to do this?
            cName = lst[0]
            cStudents = int(lst[1]) + 1
            cMaxStudents = lst[2]
            cID = lst[3]
            cDepartment = lst[4]
            cSeasons = lst[5]
            cEntry = cName + "^" + str(cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
            tempCourseFile.write("%s" % cEntry)

        else:
            tempCourseFile.write("%s" % line)
    #writing each line of the updated temp course file to the real one
    courseFile = open("testCourseFile.txt", "w")
    tempCourseFile = open("tempCourseFile.txt", 'r')
    for line in tempCourseFile:
        courseFile.write(line)


def editCourses():
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
    realCourse = False
    while realCourse == False:
        # cID = input('Enter the ID of the course you with to manage:')
        for line in courseFile:
            print('test')
            lst = line.split("^")
            if lst.__contains__(cID):
                correctCourse = input('Is this the correct course? (y/n)\n'
                                      'Course Name:', lst[0], ' Department:', lst[4], ' Max capacity:', lst[2], ' Course ID:', lst[3])
                if correctCourse == 'y':
                    realCourse = True
                else:
                    pass
                
    cPart = input('Which part would you like to change in this course? Name(1), Max students(2), ID(3), Department(4) or Avalible seasons(5) ')

    if cPart == '1':
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

    elif cPart == '2':
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
    elif cPart == '3':
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
    elif cPart == '4':
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
    elif cPart == '5':
        newSeasons = input('What would you like the available seasons to be? \n(Summer, Fall, Winter, Spring. a four digit number with a 1 if the course is available during the seasona and a 0 if it is not. eg: 0011)')
        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(cID):
                # is there a better way to do this?
                cName = lst[0]
                cStudents = lst[1]
                cMaxStudents = lst[2]
                cID = lst[3]
                cDepartment = lst[4]
                cSeasons = newSeasons
                cEntry = cName + "^" + str(
                    cStudents) + "^" + cMaxStudents + "^" + cID + "^" + cDepartment + "^" + cSeasons + "\n"
                tempCourseFile.write("%s" % cEntry)
            else:
                tempCourseFile.write(line)
    courseFile = open("testCourseFile.txt", "w")
    tempCourseFile = open("tempCourseFile.txt", 'r')
    for line in tempCourseFile:
        courseFile.write(line)

main()
#searchStudents()
