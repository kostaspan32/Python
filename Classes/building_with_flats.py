class Flat:
    def __init__(self):
        self.people = 0

class Storey:
    def __init__(self, flats_number):
        self.flats = [Flat() for i in range(flats_number)]
        self.people = 0

class Building:
    def __init__(self, storeys_number, flats_number):
        self.storeys = [Storey(flats_number) for i in range(storeys_number)]

    def add_people(self, storey, flat, people_number):
        self.storeys[storey].flats[flat].people += people_number

    def print_people(self):
        i = -1
        for storey in self.storeys:
            i += 1
            j = -1
            for flat in storey.flats:
                j += 1
                print(f'Storey {i}, Flat {j} has {flat.people} people')

my_building = Building(3, 4)
my_building.add_people(0, 1, 2)
my_building.print_people()

