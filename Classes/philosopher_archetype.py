class Philosopher:
    def __init__(self, full_name, age, books, school):
        self.full_name = full_name
        self.age = age
        self.books = books
        self.school = school
        self.controversial_work = []

plato = Philosopher('Plato', 'Ancient Greek', ['The Republic', 'Phaedon'], 'Platonism')
spinoza = Philosopher('Baruch Spinoza', 'Modern Netherlands', ['Ethics', 'Political Treatise'], 'Rationalism')

print(spinoza.controversial_work)
print(plato.school)