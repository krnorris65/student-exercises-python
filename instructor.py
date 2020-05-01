from nss_person import NSSPerson
class Instructor(NSSPerson):
    def __init__(self, first, last, handle, cohort, specialty):
        super().__init__(first, last, handle, cohort)
        self.specialty = specialty
    
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is an instructor for {self.cohort}'
