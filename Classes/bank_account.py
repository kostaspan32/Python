class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


class Bank_Account:
    def __init__(self, number, owner, deposit):
        self.number = number
        self.owner = owner
        self.deposit = deposit

    def transfer_to(self, owner, deposit):
        if self.deposit >= deposit:
            self.deposit -= deposit
            owner.deposit += deposit
            print(f'Transaction from {self.owner.name} to {owner.owner.name} of {deposit}$ complete!')

        else:
            print('Not enough money! ')

kostas = Person('Kostas', 24, 'AI423327')
john = Person('John', 26, 'AI423326')

b1 = Bank_Account('123456789012345', kostas, 5000)
b2 = Bank_Account('123456789012346', john, 6000)
b1.transfer_to(b2, 2000)
print(b1.deposit, b2.deposit)