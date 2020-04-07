from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

# Create 4, or more, exercises.
chicken = Exercise("Chicken Monkey", "Javascript")
arrays = Exercise("Array Methods", "Javascript")
urban = Exercise("Urban Planner", "CSharp")
kennel = Exercise("Kennel", "React")

# Create 3, or more, cohorts.
cohort38 = Cohort("Cohort 38")
cohort31 = Cohort("Cohort 31")
cohort33 = Cohort("Cohort 33")

# Create 4, or more, students and assign them to one of the cohorts.
mollie = Student("Mollie", "Goforth")
sydney = Student("Sydney", "Noh")
chris = Student("Chris", "Morgan")
trinity = Student("Trinity", "Terry")

cohort38.add_student(mollie)
cohort38.add_student(trinity)
cohort31.add_student(chris)
cohort33.add_student(sydney)

# Create 3, or more, instructors and assign them to one of the cohorts.
joe = Instructor("Joe", "Shepherd")
jisie = Instructor("Jisie", "David")
andy = Instructor("Andy", "Collins")

cohort31.add_instructor(jisie)
cohort33.add_instructor(joe)
cohort38.add_instructor(andy)

# Have each instructor assign 2 exercises to each of the students.
jisie.assign_exercise(chris, kennel)
jisie.assign_exercise(chris, urban)

joe.assign_exercise(sydney, chicken)
joe.assign_exercise(sydney, arrays)

andy.assign_exercise(mollie, kennel)
andy.assign_exercise(mollie, arrays)

andy.assign_exercise(trinity, urban)
andy.assign_exercise(trinity, chicken)

# Create a list of students. Add all of the student instances to it.
students = list()
students.append(mollie)
students.append(sydney)
students.append(chris)
students.append(trinity)

# Create a list of exercises. Add all of the exercise instances to it.
exercises = list()
exercises.append(kennel)
exercises.append(urban)
exercises.append(arrays)
exercises.append(chicken)

# Now, generate a report that displays which students are working on which exercises.
for student in students:
    exercise_string = ""
    for num, exercise in enumerate(student.exercises, start=1):
        if num != len(student.exercises) & len(student.exercises) == 2:
            exercise_string += f"{exercise.name} "
        elif num != len(student.exercises):
            exercise_string += f"{exercise.name}, "
        else:
            exercise_string += f"and {exercise.name}"
    print(f"{student.first} is working on {exercise_string}")
