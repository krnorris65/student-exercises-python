import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/knorris/NSS/python/student_exercises/student_exercises.db"

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            FROM Student s
            JOIN Cohort c ON s.CohortId = c.Id
            ORDER BY s.CohortId
            """)

            all_students = db_cursor.fetchall()
            print("\n*** All Students with Cohort Name ***")
            [print(s) for s in all_students]
    
    def all_instructors(self):
        '''Retrieve all instructors with the cohort name'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[5], row[6]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT i.Id,
                i.FirstName, 
                i.LastName, 
                i.SlackHandle, 
                i.CohortId, 
                c.Name,
                i.Specialty 
            FROM Instructor i
            JOIN Cohort c ON i.CohortId = c.Id
            ORDER BY i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            print("\n*** All Instructors with Cohort Name ***")
            [print(i) for i in all_instructors]

    def all_cohorts(self):
        '''Retrive all cohorts'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.Id,
                c.Name
            FROM Cohort c
            """)

            all_cohorts = db_cursor.fetchall()

            print("\n*** All Cohorts ***")
            [print(c) for c in all_cohorts]

    def all_exercises(self):
        '''Retrive all the exercises'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
                e.Name,
                e.Language
            FROM Exercise e
            """)

            all_exercises = db_cursor.fetchall()

            print("\n*** All Exercises ***")
            [print(e) for e in all_exercises]

    def javascript_exercises(self):
        pass

    def python_exercises(self):
        pass

    def csharp_exercises(self):
        pass




reports = StudentExerciseReports()
reports.all_students()
reports.all_instructors()
reports.all_cohorts()
reports.all_exercises()
