class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.hunger = hunger

    def express(self):
        if self.hunger > 5:
            print('Mowwwwwwwwwww')

        else:
            print('Moww')

molly = Cow(500, 5)
print(type(molly))
print(molly.hunger)
molly.express()


class TexasLongHorn(Cow):
    def __init__(self, weight, hunger, horn_length):
        super().__init__(weight, hunger)
        self.horn_length = horn_length

    def express(self):
        if self.hunger > 5:
            print('MoEEEEEwwEEEwwwwwwwww')

        else:
            print('MEowEw')

bob = TexasLongHorn(400, 20, 0.50)
bob.express()
print(f"Bob's horns are {bob.horn_length} meters long")
print(f"Bob's weight = {bob.weight}, hunger = {bob.hunger}, horn length = {bob.horn_length}")
