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
        '''Retrive the exercises written in javascript'''
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
            WHERE e.Language = "Javascript"
            """)

            javascript_exercises = db_cursor.fetchall()

            print("\n*** Javascript Exercises ***")
            [print(e) for e in javascript_exercises]

    def python_exercises(self):
        '''Retrive the exercises written in python'''
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
            WHERE e.Language = "Python"
            """)

            python_exercises = db_cursor.fetchall()

            print("\n*** Python Exercises ***")
            [print(e) for e in python_exercises]

    def csharp_exercises(self):
        '''Retrive the exercises written in C#'''
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
            WHERE e.Language = "C#"
            """)

            csharp_exercises = db_cursor.fetchall()

            print("\n*** C# Exercises ***")
            [print(e) for e in csharp_exercises]

    def exercises_with_students(self):
        '''Retrieves the students working on each exercise'''
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.FirstName,
                    s.LastName
                FROM Exercise e
                JOIN StudentExercise se ON se.ExerciseId = e.Id
                JOIN Student s ON s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
            
            for exercise_name, students in exercises.items():
                print(f"{exercise_name} is being worked on by:")
                for student in students:
                    print(f'\t* {student}')
    
    def student_workload(self):
        '''Retrieves the exercises being worked on by each student'''
        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                s.Id,
                s.FirstName,
                s.LastName,
                e.Id AS "ExerciseId",
                e.Name
            FROM Student s 
            JOIN StudentExercise se ON se.StudentId = s.Id
            JOIN Exercise e ON e.Id = se.ExerciseId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                student_id = row[0]
                student_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(f"{student_name} is working on:")
                for exercise in exercises:
                    print(f"\t* {exercise}")
        
    
    def exercises_by_instructor(self):
        '''Retrieves the exercises that have been assigned by each instructor'''
        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(""" 
            SELECT 
                i.Id,
                i.FirstName,
                i.LastName,
                e.Id AS "ExerciseId",
                e.Name
                FROM Instructor i 
            JOIN StudentExercise se ON se.InstructorId = i.Id
            JOIN Exercise e ON e.Id = se.ExerciseId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                instructor_id = row[0]
                instructor_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    # only add the exercise to the list if it is not already in there
                    if exercise_name not in instructors[instructor_name]:
                        instructors[instructor_name].append(exercise_name)
            
            for instructor_name, exercises in instructors.items():
                print(f"{instructor_name} has assigned:")
                for exercise in exercises:
                    print(f"\t* {exercise}")

    def assigned_exercises(self):
        '''Retrieves all exercises and lists which instructor assign it to which student'''
        assignments = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                i.Id AS "InstructorId",
                i.FirstName,
                i.LastName,
                e.Id AS "ExerciseId",
                e.Name,
                s.id AS "StudentId",
                s.FirstName,
                s.LastName
            FROM Instructor i 
            JOIN StudentExercise se ON se.InstructorId = i.Id
            JOIN Exercise e ON e.Id = se.ExerciseId
            JOIN Student s ON se.StudentId = s.Id 
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                instructor_id = row[0]
                instructor_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]
                student_id = row[5]
                student_name = f'{row[6]} {row[7]}'

                if exercise_name not in assignments:
                    assignments[exercise_name] = {
                        instructor_name: [student_name]
                    }
                else:
                    if instructor_name not in assignments[exercise_name]:
                        assignments[exercise_name][instructor_name] = [student_name]
                    else:
                        assignments[exercise_name][instructor_name].append(student_name)
            
            for exercise_name, instructor_assignments in assignments.items():
                print(f"{exercise_name}:")
                for instructor_name, students in instructor_assignments.items():
                    for student_name in students:
                        print(f"\t* {instructor_name} assigned this to {student_name}")
            
    def cohort_report(self):
        cohorts = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(""" 
            SELECT 
                c.Id AS "CohortId",
                c.Name,
                s.Id AS "StudentId",
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                i.Id AS "InstructorId",
                i.FirstName, 
                i.LastName, 
                i.SlackHandle, 
                i.CohortId, 
                i.Specialty
            FROM Cohort c 
            JOIN Student s ON s.CohortId = c.Id
            JOIN Instructor i ON i.CohortId = c.Id
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                cohort_id = row[0]
                cohort_name = row[1]
                # first, last, handle, cohort
                student = Student(row[3], row[4], row[5], row[1])
                # first, last, handle, cohort, specialty
                instructor = Instructor(row[8], row[9], row[10], row[1], row[12])

                if cohort_name not in cohorts:
                    cohorts[cohort_name] = {
                        "students": [student],
                        "instructors": [instructor]
                    }
                else:
                    # convert the items in each list to only represent the student or instructor's full name
                    student_names_in_list = list(map(lambda s: s.full_name, cohorts[cohort_name]["students"]))
                    instructor_names_in_list = list(map(lambda i: i.full_name, cohorts[cohort_name]["instructors"]))
                    # check to see if that student or instructor name is already in the list, if it's not add it
                    if student.full_name not in student_names_in_list:
                        cohorts[cohort_name]["students"].append(student)
                    if instructor.full_name not in instructor_names_in_list:
                        cohorts[cohort_name]["instructors"].append(instructor)
            
            for cohort, value in cohorts.items():
                print(f"{cohort}:")
                if len(value["students"]) > 0:
                    print("\tStudents:")
                    [print(f"\t* {s}") for s in value["students"]]
                if len(value["instructors"]) > 0:
                    print("\tInstructors:")
                    [print(f"\t* {i}") for i in value["instructors"]]


reports = StudentExerciseReports()
# reports.all_students()
# reports.all_instructors()
# reports.all_cohorts()
# reports.all_exercises()
# reports.javascript_exercises()
# reports.python_exercises()
# reports.csharp_exercises()

# reports.exercises_with_students()
# reports.student_workload()
# reports.exercises_by_instructor()
# reports.assigned_exercises()
reports.cohort_report()
