from random import randrange

class Character:
    def __init__(self, name, attack_speed=2, delay=0):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack_speed = self.__validate(1, 10, attack_speed)
        self.delay = delay

    def __validate(self, lower, upper, obj):
        if lower <= obj <= upper:
            return obj
        else:
            return None

    def attack(self):
        self.delay = 5 - self.attack_speed
        return randrange(3, 11)

    def is_dead(self):
        return self.health <= 0

    def end_round(self):
        if self.health < 100:
            self.health += 1
        self.delay -= 1

    def __str__(self):
        return f'{self.name} H: {self.health} AS: {self.attack_speed} D: {self.delay}'

    def __repr__(self):
        return f'Character({self.name},{self.health},{self.attack_speed},{self.delay})'

    def __iadd__(self, other):
        self.health += other

    def __isub__(self, other):
        self.health -= other