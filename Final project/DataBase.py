import sqlite3 as sql


class Query:
    def __init__(self):
        course = sql.connect("course.db")
        c = course.cursor()
        account = sql.connect("account.db")
        a = account.cursor()

        if c.fetchone() is None:
            course_create = """
            CREATE TABLE IF NOT EXISTS Course(
            course_name VARCHAR(20) NOT NULL,
            course_desc VARCHAR(200) NOT NULL,
            department VARCHAR(20) NOT NULL,
            capacity int NOT NULL,
            semester VARCHAR(6) NOT NULL);"""

            c.execute(course_create)

            course.commit()

            course.close()

        if a.fetchone() is None:
            student_create = """
            CREATE TABLE IF NOT EXISTS Student(
            student_id INTEGER PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(30),
            address VARCHAR(30),
            department VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(30));
            """
            faculty_create = """
            CREATE TABLE IF NOT EXISTS Faculty(
            faculty_id INTEGER PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(30),
            address VARCHAR(30),
            password VARCHAR(20),
            email VARCHAR(30));"""

            a.execute(student_create)
            a.execute(faculty_create)

            account.commit()

            account.close()

    def Get_student(self, ID):
        account = sql.connect("account.db")
        a = account.cursor()

        a.execute("Select * FROM Student Where student_id =" + str(ID))

        return a.fetchall()

        account.commit()

        account.close()

    def Get_password_student(self, ID):
        account = sql.connect("account.db")
        a = account.cursor()

        a.execute("Select password FROM Student Where student_id =" + str(ID))

        return a.fetchall()

        account.commit()

        account.close()

    def Get_password_faculty(self, ID):
        account = sql.connect("account.db")
        a = account.cursor()

        a.execute("Select password FROM faculty Where faculty_id = " + str(id))
