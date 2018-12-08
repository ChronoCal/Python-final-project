from Account import Account
import matplotlib.pyplot as plt
import numpy as np

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

    def course_graph_pie():
        labels = ['test1', 'test2', 'test3', 'test4']
        size = [125, 125, 25, 25]
        # explode (0, 0, 0, 0)
        fig1, display = plt.subplots()
        display.pie(size, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
        display.axis('equal')

        plt.show()

    def course_graph_bar():

        plt.rcdefaults()
        fig, course_chart = plt.subplots()

        course = ['test1', 'test2', 'test3', 'test4']
        size = [125, 125, 25, 25]

        x_pos = np.arange(len(course))

        course_chart.bar(x_pos, size, align='center', color='blue')
        course_chart.set_xticks(x_pos)
        course_chart.set_xticklabels(course)
        course_chart.set_ylabel('Number of Students')
        course_chart.set_title('Number of Students Enrolled per Course')

        plt.show()

def main():
    Faculty.course_graph_bar()

main()