class Instructor:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.slack_handle = ""
        self.cohort = ""
        self.specialty = ""
    
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)