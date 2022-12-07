class Lesson:
    def __init__(self, name):
        self.name = name
        self.lesson_pupil_list = []
        self.lesson_teachers_list = []


class Lessons:
    pass

with open('lessons.json', 'w') as f:
    f.write('')