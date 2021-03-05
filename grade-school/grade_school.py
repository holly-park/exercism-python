class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append((grade, name))

    def roster(self):
        self.students.sort()
        return [name for grade, name in self.students]

    def grade(self, grade_number):
        self.students.sort()
        return [name for grade, name in self.students if grade == grade_number]
