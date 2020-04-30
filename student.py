from nss_person import NSSPerson
class Student(NSSPerson):
    def __init__(self, first, last, handle, cohort):
        super().__init__(first, last, handle, cohort)
        self.exercises = list()

