from DataBase import Query
courselist = []
class Course(Query):
    def __init__(self, course, account):
        Query.__init__(self, course, account)

    def add_course(self, account):
        coursename = input("What would you like to name the course?")
        courselist.append(coursename)