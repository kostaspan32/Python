class Storey:
    def __init__(self):
        self.people = 0

class Building:
    def __init__(self, storeys_number):
        self.storeys = [Storey() for i in range(storeys_number)]

    def add_people(self, storey, people_number):
        self.storeys[storey].people += people_number

    def print_people(self):
        i = 0
        for storey in self.storeys:
            i += 1
            print(f'Storey {i} has {storey.people} people')

my_building = Building(3)
my_building.add_people(0, 2)
my_building.print_people()

