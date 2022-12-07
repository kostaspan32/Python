

class Length:
    def __init__(self, number=0, measure='m'):
        self.measure = measure.strip().lower()
        if measure.strip().lower() == 'm':
            self.number = number
        elif measure.strip().lower() == 'cm':
            self.number = number/100
        elif measure.strip().lower() == 'inch':
            self.number = number * 0.0254
        else:
            self.number = 0

    def __str__(self):
        return f'Length = {self.number}m'

    def __add__(self, other):
        if isinstance(other, Length):
            return Length(self.number + other.number, 'm')
        elif isinstance(other, int):
            return Length(self.number + other, 'm')

    def __round__(self, n=None):
        return round(self.number, n)

    def __int__(self):
        return int(self.number)


l1 = Length(1, 'm')
l2 = Length(50, 'cm')
l3 = Length(100, 'inch')
print(l1 + l2)
print(l1 + l2 + l3)
print(round(l3, 1))