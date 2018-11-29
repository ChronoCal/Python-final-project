import sqlite3 as sql
course = sql.connect("course.db")
c = course.cursor()
account = sql.connect("account.db")
a = account.cursor()


class querry:
    def __init__(self):
        if c.fetchone() == None:
           course_create = """
           CREATE TABLE Course(
           course_name VARCHAR(20) NOT NULL,
           course_desc VARCHAR(200) NOT NULL,
           department VARCHAR(20) NOT NULL,
           capacity int NOT NULL,
           semester VARCHAR(6) NOT NULL,
           PRIMARY KEY(course_name)"""
