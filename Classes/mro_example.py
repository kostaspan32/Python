from random import randrange
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, salary):
        self.counter = 0
        self.name = name
        self.salary = salary

    def report(self):
        print(f'{self.name} served {self.counter} times!')


class Waiter(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name, salary)

    def serve(self, clients, barista):
        self.counter += len(clients)
        barista.prepare(clients)
        print(f'Waiter {self.name} served {len(clients)} clients!')


class Barista(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name, salary) #PROSOXH to self den mpainei automata

    def prepare(self, clients):
        self.counter += len(clients)
        print(f'Barista {self.name} prepared!')


class Owner(Waiter, Barista):
    def __init__(self, name, salary):
        Person.__init__(self, name, salary)


kostas = Owner('Kostas', 5000)
ninis = Waiter('Vangelis', 300)
knx = Waiter('Nikos', 100)
errika = Barista('Errika', 50)
waiters = [ninis, knx, kostas]
baristas = [errika, kostas]


for i in range(10):
    clients = []
    x = randrange(1, 6)
    for _ in range(x):
        clients.append(_)
    y = randrange(len(waiters))
    z = randrange(len(baristas))
    waiters[y].serve(clients, baristas[z])
    print('=' * 30)

kostas.report()
errika.report()
ninis.report()
knx.report()

