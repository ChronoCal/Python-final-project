from Account import Account
import matplotlib.pyplot as plt

class Faculty(Account):
    def __init__(self, first, last, DoB, address, email, ID, password):
        Account.__init__(self, first, last, DoB, address, email, password, ID)

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

    def course_graph(self, course_data):

