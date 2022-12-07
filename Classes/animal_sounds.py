from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print('Meow')


class HimalayanCat(Cat):
    def make_sound(self):
        print(f'{super().make_sound()} Miouw Miouw')


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")


class Doberman(Dog):
    pass


class KingDoberman(Doberman):
    def make_sound(self):
        print(f'{super().make_sound()} WOAAAAAFFFFF')