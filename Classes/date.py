class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'Date is : {str(self.day).zfill(2)}/{str(self.month).zfill(2)}/{str(self.year).zfill(2)}'

    def __repr__(self):
        return f'Date({self.day},{self.month},{self.year})'

    def __eq__(self, other):
        return (self.day == other.day and self.month == other.month and self.year == other.year)

