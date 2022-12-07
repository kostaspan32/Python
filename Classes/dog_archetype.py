class Dog:
    def __init__(self, name, weight, race):
        self.name = name
        self.weight = weight
        self.race = race
        self.mood = 5

    def eat(self):
        if self.mood < 10:
            self.mood += 1

    def bark(self):
        if self.mood > 5:
            print('Woof woof woof')

        else:
            print('Woof')

    def walk(self):
        if self.mood < 10:
            self. mood += 1

pico = Dog('Pico', 10, 'Terrier')
lassie = Dog('Lassie', 30, 'Colley')

pico.bark()
pico.walk()
pico.bark()
pico.walk()
pico.bark()
pico.eat()
pico.bark()