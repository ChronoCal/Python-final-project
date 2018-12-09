# 100705779, 100702991, 100703659
# Kevin Nguyen, Mark Bermah , Matthew Martin


import matplotlib.pyplot as plt
import numpy as np


class Parse:

    def __init__(self):
        pass

    def s_get_info(self, sID):
        testFile = open("testParseFile.txt", "r")
        for line in testFile:
            slst = line.split("^")
            if slst.__contains__(sID):
                return slst

    def f_get_info(self, fID):
        facultyFile = open("testFacultyFile.txt", "r")
        for line in facultyFile:
            flst = line.split("^")
            if flst.__contains__(fID):
                return flst

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
                tempCourseFile.write("%s" % line)

            elif lst.__contains__(courseID):

                cStudents = int(lst[1]) + 1
                cStudent = str(lst[5].strip())
                cStudent = str(cStudent) + str(sID) + "^"
                cEntry = lst[0] + "^" + str(
                    cStudents) + "^" + lst[2] + "^" + lst[3] + "^" + lst[4] + "^" + cStudent + "\n"
                tempCourseFile.write("%s" % cEntry)

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

        # writing each line of the updated temp course file to the permanent file
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

        print("You successfully registered for this course.")
        input('\npress ENTER to continue')

    def s_drop_course(self, sID, courseID):
        # file with course info in it
        courseFile = open("testCourseFile.txt", "r")
        tempCourseFile = open("tempCourseFile.txt", "a")

        for line in courseFile:
            lst = line.split("^")
            if lst.__contains__(courseID):

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
        
        # writing each line of the updated temp course file to the permanent one
        courseFile = open("testCourseFile.txt", "w")
        tempCourseFile = open("tempCourseFile.txt", 'r')
        for line in tempCourseFile:
            courseFile.write(line)
        tempCourseFile.close()
        tempCourseFile = open("tempCourseFile.txt", 'w')
        tempCourseFile.write("")
        courseFile.close()

    def s_register_user(self):
        testFile = open("testParseFile.txt", "a")
        testFile.write("%s" % studentEntry)
        testFile.write("\n")
        testFile.close()

    def s_new_password(self, ID, newPassword ):
        studentFile = open("testParseFile.txt", "r")
        tempStudentFile = open("tempParseFile.txt", "a")

        for line in studentFile:
            lst = line.split("^")
            if lst.__contains__(ID):
                # is there a better way to do this?
                lst[7] = newPassword
                a = 0
                cEntry = ''
                while a < (len(lst)) - 1:
                    cEntry += str(lst[a]) + "^"
                    a += 1
                tempStudentFile.write("%s" % cEntry + '\n')

            else:
                tempStudentFile.write("%s" % line)

        studentFile.close()
        tempStudentFile.close()
        # writing each line of the updated temp course file to the real one
        studentFile = open("testParseFile.txt", "w")
        tempStudentFile = open("tempParseFile.txt", 'r')
        for line in tempStudentFile:
            studentFile.write(line)
        tempStudentFile.close()
        tempStudentFile = open("tempParseFile.txt", 'w')
        tempStudentFile.write("")
        studentFile.close()

    def f_new_password(self, ID, newPassword ):
        facultyFile = open("testFacultyFile.txt", "r")
        tempFacultyFile = open("tempFacultyFile.txt", "a")

        for line in facultyFile:
            lst = line.split("^")
            if lst.__contains__(ID):

                lst[6] = newPassword
                a = 0
                cEntry = ''
                while a < (len(lst)) - 1:
                    cEntry += str(lst[a]) + "^"
                    a += 1
                tempFacultyFile.write("%s" % cEntry + '\n')

            else:
                tempFacultyFile.write("%s" % line)

        facultyFile.close()
        tempFacultyFile.close()
        # writing each line of the updated temp course file to the real one
        facultyFile = open("testFacultyFile.txt", "w")
        tempFacultyFile = open("tempFacultyFile.txt", 'r')
        for line in tempFacultyFile:
            facultyFile.write(line)
        tempFacultyFile.close()
        tempFacultyFile = open("tempFacultyFile.txt", 'w')
        tempFacultyFile.write("")
        facultyFile.close()

    def f_add_course(self, course):
        courseFile = open("testFacultyFile.txt", "a")
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

    def f_view_students_in_courses(self):
        courseFile = open("testCourseFile.txt", "r")
        numberOfStudents = []
        courseNames = []
        for line in courseFile:
            lst = line.split("^")
            if lst[1] != "0":
                numberOfStudents.append(lst[1])
                courseNames.append(lst[0])

        print('View as: ')
        print('[1] Pie chart')
        print('[2] Bar graph')
        graph = input('\n> ')

        while True:
            if graph == '1':
                fig1, display = plt.subplots()
                display.pie(numberOfStudents, labels=courseNames, autopct='%1.1f%%', startangle=90, shadow=True)
                display.axis('equal')

                plt.show()
                break

            elif graph == '2':
                plt.rcdefaults()
                fig, course_chart = plt.subplots()

                x_pos = np.arange(len(courseNames))

                course_chart.bar(x_pos, numberOfStudents, align='center', color='blue')
                course_chart.set_xticks(x_pos)
                course_chart.set_xticklabels(courseNames)
                course_chart.set_ylabel('Number of Students')
                course_chart.set_title('Number of Students Enrolled per Course')

                plt.show()
                break

            else:
                print('ERROR: invalid input')

    def f_register_user(self):
        testFile = open("testFacultyFile.txt", "a")
        testFile.write("%s" % facultyEntry + '\n')
        testFile.close()
        main()
