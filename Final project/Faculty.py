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

    def course_graph_pie(self, labels, size):
        labels = ['test1', 'test2', 'test3', 'test4']
        size = [25, 25, 25, 25]
        # explode (0, 0, 0, 0)
        fig1, display = plt.subplots()
        display.pie(size, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
        display.axis('equal')

        plt.show()

def main():
    Faculty.course_graph()

main()