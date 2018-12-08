from Faculty import Faculty

class Parse:

    def __init__(self):
        pass


    def s_get_info(self, sID):
        testFile = open("testParseFile.txt", "r")
        for line in testFile:
            slst = line.split("^")
            if slst.__contains__(sID):
                return slst



    def view_available_courses(self, sID):
        courses = Parse.get_all_courses(self)
        sInfo = Parse.s_get_info(self, sID)
        sDepartment = sInfo[4]
        coursesAvailable = []
        for lst in courses:
            if lst.__contains__(sID):
                pass
            elif lst.__contains__(sDepartment) and int(lst[1]) < int(lst[2]):
                coursesAvailable.append(lst)
        return coursesAvailable


    def get_course(self, ID):
        courseFile = open("testCourseFile.txt", "r")
        course = []
        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(ID):
                course = lst
        return course


    def get_all_courses(self):

        #file with course info in it
        courseFile = open("testCourseFile.txt", "r")
        allCourses = []
        for line in courseFile:
            lst = line.split("^")
            allCourses.append(lst)
        return allCourses




    def s_courses_enrolled(self, sID):
        allCourses = Parse.get_all_courses(self)
        coursesEnrolled = []
        a = 0
        while a < len(allCourses):
            # if sID in allCourses[a]:
            lst = allCourses[a]
            coursesEnrolled.append(lst)
            a += 1
        return coursesEnrolled



    def s_register_course(self, courseID, sID):
        # updates the courses availability
        tempCourseFile = open("tempCourseFile.txt", 'a')
        courseFile = open("testCourseFile.txt", "r")
        testFile = open("testParseFile.txt", "r")
        tempFile = open("tempParseFile.txt", "a")


        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(sID):
                print("Sorry, you are already registered for this course")
            elif lst.__contains__(courseID):
                # is there a better way to do this?
                cStudents = int(lst[1]) + 1
                cStudent = str(lst[5].strip())
                cStudent = str(cStudent) + str(sID) + "^"
                cEntry = lst[0] + "^" + str(
                    cStudents) + "^" + lst[2] + "^" + lst[3] + "^" + lst[4] + "^" + cStudent + "\n"
                tempCourseFile.write("%s" % cEntry)
                print('test')

            else:
                tempCourseFile.write("%s" % line)

            for student in testFile:
                lst = student.split("^")
                if lst.__contains__(sID):
                    sCourses = (courseID) + "^"
                    studentEntry = lst.append(sCourses)
                    tempFile = open("tempParseFile.txt", "a")
                    tempFile.write("%s" % studentEntry)
                    tempFile.close()
                else:
                    tempFile = open("tempParseFile.txt", "a")
                    tempFile.write("%s" % student)
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

        parseFile = open("testParseFile.txt", "r")
        tempParseFile = open("tempParseFile.txt", 'w')
        for line in parseFile:
            tempParseFile.write(line)
        parseFile.close()
        tempParseFile.close()
        tempParseFile = open("tempParseFile.txt", 'w')
        tempParseFile.write("")
        tempParseFile.close()

        print("You successfully registered this course.")

    def s_drop_course(self, sID, courseID):
        # file with student info in it
        testFile = open("testParseFile.txt", "r")
        testFile = open("testParseFile.txt", "r")
        # file with course info in it
        courseFile = open("testCourseFile.txt", "r")
        tempCourseFile = open("tempCourseFile.txt", "a")

        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(courseID):
                # is there a better way to do this?
                lst[1] = int(lst[1]) - 1
                index = lst.index(str(sID))
                lst.pop(index)
                a = 0
                cEntry = ''
                while a < (len(lst)) - 1:
                    cEntry += str(lst[a]) + "^"
                    a += 1
                tempCourseFile.write("%s" % cEntry + '\n')

            else:
                tempCourseFile.write("%s" % line)

        courseFile.close()
        tempCourseFile.close()
        # writing each line of the updated temp course file to the real one
        courseFile = open("testCourseFile.txt", "w")
        tempCourseFile = open("tempCourseFile.txt", 'r')
        for line in tempCourseFile:
            courseFile.write(line)
        tempCourseFile.close()
        tempCourseFile = open("tempCourseFile.txt", 'w')
        tempCourseFile.write("")
        courseFile.close()



    def s_authenticate(self, sID, sPassword):
        testFile = open("testParseFile.txt", "r")
        loginAttempt = False
        id = sID
        password = sPassword
        for line in testFile:
            lst = line.split('^')
            if lst[6] == sID and lst[7] == sPassword:
                loginAttempt = True




    def s_register_user(self):

        testFile = open("testParseFile.txt", "a")
        testFile.write("%s" % studentEntry)
        testFile.write("\n")
        testFile.close()



    #get the information from the factuly here, or in main line and import it
    def f_add_course(self, course):
        courseFile = open("testCourseFile.txt", "a")
        courseFile.write(course)
        courseFile.close()



    def f_update_course(self, course, ID):
        # files with course info in it
        courseFile = open("testCourseFile.txt", "r")
        tempCourseFile = open("tempCourseFile.txt", "a")

        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(ID):
                cEntry = str(course)
                tempCourseFile.write("%s" % cEntry)

            else:
                tempCourseFile.write("%s" % line)
        courseFile.close()
        tempCourseFile.close()

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


    def f_see_all_courses(self):
        pass

    def f_view_course_info(self):
        pass

    def f_view_student_info(self):
        pass

    def f_list_students_in_courses(self):
        pass

    def f_veiw_students_in_courses(self):
        courseFile = open("testCourseFile.txt", "r")
        numberOfStudents = []
        courseNames = []
        for line in courseFile:
            lst = line.split("^")
            if lst[1] != "0":
                numberOfStudents.append(lst[1])
                courseNames.append(lst[0])
        # faculty = Faculty()
        Faculty.course_graph_pie(self, courseNames, numberOfStudents)



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
