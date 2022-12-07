from date import Date
from class_time import Time

class DateTime:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def __setitem__(self, d, mon, y, h, min, s):
        self.date = Date(d, mon, y)
        self.time = Time(h, min, s)

    def __str__(self):
        return f'Date is: {self.date}\nTime is : {self.time}'

    def __repr__(self):
        return f'DateTime({repr(self.date)},{repr(self.time)})'


d = Date(7, 9, 97)
t = Time(15, 56, 5)
obj = DateTime(d, t)
print(obj)
print(repr(obj))
