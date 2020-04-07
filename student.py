from nss_person import NSSPerson
class Student(NSSPerson):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.exercises = list()

