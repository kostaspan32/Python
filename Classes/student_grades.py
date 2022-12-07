from random import randrange

class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.grade = -1

    def __str__(self):
        return f'Name: {self.full_name}, Grade: {self.grade}'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.grade > other.grade
        elif isinstance(other, int):
            return self.grade > other

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.grade >= other.grade
        elif isinstance(other, int):
            return self.grade >= other

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.grade == other.grade
        elif isinstance(other, int):
            return self.grade == other


def grade_student(student):
    student.grade = randrange(11)


def average(student_list):
    student_grade_sum = 0
    for student in student_list:
        student_grade_sum += student.grade

    return student_grade_sum / len(student_list)


names = ['Kostas Panagiotopoulos',
         'Ioannis Panagiotopoulos',
         'Nikos Soulounias',
         'Spyros Tsattalios',
         'Konstantinos Aggelopoulos',
         'Maria Panagiotopoulou',
         'Xrisanthi Diakostamatiou',
         'Serpil Kiokekli',
         'Giorgos Dospras',
         'Xristos Swtopoulos']

student_list = [Student(name for name in names)]

for name in names:
    student = Student(name)
    grade_student(student)
    student_list.append(student)



print(f'Average is : {average(student_list)}')
student_list.sort(reverse=True)
for student in student_list:
    print(student)
















