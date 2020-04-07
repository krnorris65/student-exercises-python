from nss_person import NSSPerson
class Instructor(NSSPerson):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.specialty = ""
    
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)