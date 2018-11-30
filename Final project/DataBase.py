import sqlite3 as sql


class Query:
    def __init__(self):
        course = sql.connect("course.db")
        c = course.cursor()
        account = sql.connect("account.db")
        a = account.cursor()

        if c.fetchone() is None:
            course_create = """
            CREATE TABLE Course(
            course_name VARCHAR(20) NOT NULL,
            course_desc VARCHAR(200) NOT NULL,
            department VARCHAR(20) NOT NULL,
            capacity int NOT NULL,
            semester VARCHAR(6) NOT NULL);"""

            c.execute(course_create)

            c.commit()

            c.close()

        if a.fetchone() is None:
            account_create = """
            Create TABLE Student(
            student_id INT NOT NULL AUTO_INCREMENT,
            first_name VARCHAR(20),
            last_name VARCHAR(30),
            address VARCHAR(30),
            department VARCHAR(20),
            email VARCHAR(30),
            PRIMARY KEY (student_id) );
            Create TABLE Faculty(
            faculty_id INT NOT NULL AUTO_INCREMENT,
            first_name VARCHAR(20),
            last_name VARCHAR(30),
            address VARCHAR(30),
            email VARCHAR(30),
            PRIMARY KEY (faculty_id) );"""

            a.execute(account_create)

            increment_id = """
            ALTER TABLE Student AUTO_INCREMENT=100000,
            ALTER TABLE Faculty AUTO_INCREMENT=1000;"""

            a.execute(increment_id)

            a.commit()

            a.close()

