from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    @abstractmethod
    def eat(self):
        pass


class Horse(Animal):
    def __init__(self, weight, height, color, tail_length):
        super().__init__(weight, height)
        self.color = color
        self.tail_length = tail_length


class Dog(Animal):
    def __init__(self, weight, height, bark_volume):
        super().__init__(weight, height)
        self.bark_volume = bark_volume

    def bark(self):
        print('Woof woof')


class Doberman(Dog):
    def __init__(self, weight, height, bark_volume):
        super().__init__(weight, height, bark_volume)

    def run(self):
        print('Doberman started running! ')


class Bulldog(Dog):
    def __init__(self, weight, height, bark_volume, ear_size):
        super().__init__(weight, height, bark_volume)
        self.ear_size = ear_size

    def sleep(self):
        print('Bulldog sleeps! ')


boukefalas = Horse(500, 2, 'white', 0.3)
mark = Bulldog(10, 0.2, 60, 0.2)
shawn = Doberman(30, 1, 70)

print(boukefalas.color)
shawn.bark()
shawn.run()
shawn.bark()
mark.bark()
mark.sleep()
mark.sleep()