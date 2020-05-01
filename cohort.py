class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()
    
    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)
    
    def __repr__(self):
        return f'{self.name}'